<?php
/**
 * Just Now – customer blocklist for the website booking flow.
 *
 * Drop this folder next to the booking code and include blocklist.php:
 *   require_once __DIR__ . '/blocklist/blocklist.php';
 *
 * 1. In the book-now submit handler, BEFORE saving the booking, sending the
 *    customer email or calling the Make webhook:
 *
 *      if (jn_is_blocked($phone, $email)) {
 *          jn_notify_blocked_attempt($phone, $email, $name);
 *          jn_render_blocked_page($lang);   // prints the block message and exits
 *      }
 *
 * 2. In the booking/manage cancel handler, AFTER a cancellation is saved:
 *
 *      jn_record_cancellation($phone, $email, $name, $reference);
 *
 *    When a customer reaches the limit in blocklist.json
 *    (auto_block_after_cancellations, default 3) they are added to the
 *    blocklist automatically and the owner is emailed.
 *
 * 3. In the booking/manage page, at the top:
 *
 *      if (jn_is_blocked($booking['phone'], $booking['email'])) jn_render_blocked_page($lang);
 *
 * Data files (same folder, must be writable by PHP): blocklist.json, cancellations.json.
 * Keep the folder outside the public web root or deny direct access with .htaccess.
 */

const JN_BLOCKLIST_FILE      = __DIR__ . '/blocklist.json';
const JN_CANCELLATIONS_FILE  = __DIR__ . '/cancellations.json';
const JN_OWNER_ALERT_EMAIL   = 'customer.care@justnow.life';
const JN_FROM_EMAIL          = 'customer.care@justnow.life';
const JN_FROM_NAME           = 'Just Now For Building Cleaning Services Co. L.L.C';

/** Normalise a UAE phone number to digits with country code, e.g. 971504532529. */
function jn_normalize_phone(?string $phone): string
{
    $d = preg_replace('/\D+/', '', (string) $phone);
    if ($d === '') return '';
    if (str_starts_with($d, '00')) $d = substr($d, 2);
    if (str_starts_with($d, '971')) return $d;
    if (str_starts_with($d, '0'))   return '971' . substr($d, 1);
    if (strlen($d) === 9)           return '971' . $d;      // 5XXXXXXXX
    return $d;
}

function jn_normalize_email(?string $email): string
{
    return strtolower(trim((string) $email));
}

function jn_read_json(string $file): array
{
    if (!is_file($file)) return [];
    $data = json_decode((string) file_get_contents($file), true);
    return is_array($data) ? $data : [];
}

function jn_write_json(string $file, array $data): void
{
    $tmp = $file . '.tmp';
    file_put_contents($tmp, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES), LOCK_EX);
    rename($tmp, $file);
}

/** Returns the matching blocklist entry, or null when the customer is not blocked. */
function jn_blocked_entry(?string $phone, ?string $email): ?array
{
    $p = jn_normalize_phone($phone);
    $e = jn_normalize_email($email);
    foreach (jn_read_json(JN_BLOCKLIST_FILE)['blocked'] ?? [] as $entry) {
        $phones = array_map('jn_normalize_phone', $entry['phones'] ?? []);
        $emails = array_map('jn_normalize_email', $entry['emails'] ?? []);
        if (($p !== '' && in_array($p, $phones, true)) || ($e !== '' && in_array($e, $emails, true))) {
            return $entry;
        }
    }
    return null;
}

function jn_is_blocked(?string $phone, ?string $email): bool
{
    return jn_blocked_entry($phone, $email) !== null;
}

/** Add a customer to the blocklist (idempotent). */
function jn_add_to_blocklist(?string $phone, ?string $email, string $name, string $reason, string $addedBy = 'system'): void
{
    $list = jn_read_json(JN_BLOCKLIST_FILE);
    $list['auto_block_after_cancellations'] = $list['auto_block_after_cancellations'] ?? 3;
    $list['blocked'] = $list['blocked'] ?? [];
    if (jn_blocked_entry($phone, $email) !== null) return;
    $list['blocked'][] = [
        'name'     => $name,
        'phones'   => array_values(array_filter([jn_normalize_phone($phone)])),
        'emails'   => array_values(array_filter([jn_normalize_email($email)])),
        'reason'   => $reason,
        'added'    => date('Y-m-d'),
        'added_by' => $addedBy,
    ];
    jn_write_json(JN_BLOCKLIST_FILE, $list);
}

/**
 * Record one cancellation. Returns the new count for this customer.
 * Auto-blocks when the count reaches auto_block_after_cancellations.
 */
function jn_record_cancellation(?string $phone, ?string $email, string $name = '', string $reference = ''): int
{
    $p   = jn_normalize_phone($phone);
    $e   = jn_normalize_email($email);
    $key = $p !== '' ? 'p:' . $p : 'e:' . $e;
    if ($key === 'p:' || $key === 'e:') return 0;

    $all = jn_read_json(JN_CANCELLATIONS_FILE);
    $row = $all[$key] ?? ['name' => $name, 'phone' => $p, 'emails' => [], 'count' => 0, 'references' => []];
    $row['count']++;
    if ($e !== '' && !in_array($e, $row['emails'], true)) $row['emails'][] = $e;
    if ($reference !== '') $row['references'][] = ['ref' => $reference, 'at' => date('c')];
    if ($name !== '') $row['name'] = $name;
    $all[$key] = $row;
    jn_write_json(JN_CANCELLATIONS_FILE, $all);

    $limit = (int) (jn_read_json(JN_BLOCKLIST_FILE)['auto_block_after_cancellations'] ?? 3);
    if ($row['count'] >= $limit && !jn_is_blocked($p, $e)) {
        $reason = sprintf('Booked and cancelled %d times (%s)', $row['count'],
            implode(', ', array_column($row['references'], 'ref')));
        jn_add_to_blocklist($p, $e, $row['name'], $reason, 'auto');
        foreach ($row['emails'] as $extra) {            // block every email this phone used
            if ($extra !== $e) jn_add_to_blocklist('', $extra, $row['name'], $reason, 'auto');
        }
        jn_mail_owner('Customer auto-blocked after ' . $row['count'] . ' cancellations',
            "Name: {$row['name']}\nPhone: $p\nEmails: " . implode(', ', $row['emails']) .
            "\nReason: $reason\n\nRemove the entry from blocklist.json to unblock.");
    }
    return $row['count'];
}

/** Email the owner when a blocked customer tries to book. */
function jn_notify_blocked_attempt(?string $phone, ?string $email, string $name = ''): void
{
    $entry = jn_blocked_entry($phone, $email);
    jn_mail_owner('Blocked customer tried to book',
        "Name entered: $name\nPhone: " . jn_normalize_phone($phone) . "\nEmail: " . jn_normalize_email($email) .
        "\nBlocklist entry: " . ($entry['name'] ?? '-') . " – " . ($entry['reason'] ?? '-') .
        "\nTime: " . date('Y-m-d H:i') . " (server time)\n\nNo booking was created and no email was sent to the customer.");
}

function jn_mail_owner(string $subject, string $body): void
{
    $headers = 'From: ' . JN_FROM_NAME . ' <' . JN_FROM_EMAIL . ">\r\nContent-Type: text/plain; charset=UTF-8";
    @mail(JN_OWNER_ALERT_EMAIL, '[Blocklist] ' . $subject, $body, $headers);
}

/** The message the blocked customer sees. */
function jn_block_message(string $lang = 'en'): array
{
    if ($lang === 'ar') {
        return [
            'title' => 'لا يمكن إتمام الحجز',
            'text'  => 'عذراً، لا يمكننا قبول حجوزات جديدة من هذا الرقم أو البريد الإلكتروني بسبب تكرار إلغاء الحجوزات السابقة. إذا كنت تعتقد أن هذا خطأ، يرجى التواصل معنا على البريد customer.care@justnow.life.',
        ];
    }
    return [
        'title' => 'We are unable to accept this booking',
        'text'  => 'Sorry, we cannot accept new bookings from this phone number or email address because previous bookings were cancelled repeatedly. If you believe this is a mistake, please contact us at customer.care@justnow.life.',
    ];
}

/** Render a minimal, on-brand block page and stop. For JSON APIs use jn_block_message() instead. */
function jn_render_blocked_page(string $lang = 'en'): void
{
    $m   = jn_block_message($lang);
    $dir = $lang === 'ar' ? 'rtl' : 'ltr';
    http_response_code(403);
    header('Content-Type: text/html; charset=UTF-8');
    echo '<!doctype html><html lang="' . $lang . '" dir="' . $dir . '"><head><meta charset="utf-8">'
       . '<meta name="viewport" content="width=device-width,initial-scale=1"><title>' . htmlspecialchars($m['title']) . '</title></head>'
       . '<body style="margin:0;padding:40px 16px;background:#f3f6fb;font-family:Arial,sans-serif;color:#15304f">'
       . '<div style="max-width:560px;margin:0 auto;background:#fff;border-radius:18px;padding:32px;text-align:center">'
       . '<div style="display:inline-block;background:#fdf1f0;color:#b3261e;border-radius:999px;padding:6px 14px;font-size:13px;font-weight:bold">403</div>'
       . '<h1 style="font-size:22px;margin:16px 0 12px">' . htmlspecialchars($m['title']) . '</h1>'
       . '<p style="font-size:15px;line-height:1.7;margin:0 0 20px">' . htmlspecialchars($m['text']) . '</p>'
       . '<a href="https://www.justnow.life" style="color:#3771c1">www.justnow.life</a>'
       . '</div></body></html>';
    exit;
}
