# Website customer blocklist

Blocks named customers from booking on justnow.life, and auto-blocks anyone who
books and cancels 3 times (`auto_block_after_cancellations` in `blocklist.json`).

Files:

| File | Purpose |
|---|---|
| `blocklist.php` | Functions: `jn_is_blocked`, `jn_render_blocked_page`, `jn_record_cancellation`, `jn_add_to_blocklist`, `jn_notify_blocked_attempt`. |
| `blocklist.json` | The blocked customers (phone + emails) and the auto-block limit. Edit by hand to add or remove someone. |
| `cancellations.json` | Counter of cancellations per customer, written by `jn_record_cancellation`. |
| `.htaccess` | Denies direct web access to this folder. |

Integration (three lines in the live site, see the header of `blocklist.php`):

1. `book-now` submit handler: check `jn_is_blocked($phone, $email)` **before** saving the booking, sending the customer email or calling the Make webhook. Blocked customers see the 403 block page; the owner gets an email on `customer.care@justnow.life`.
2. `booking/manage` cancel handler: call `jn_record_cancellation($phone, $email, $name, $reference)` after the cancellation is saved. The 3rd cancellation adds the customer to `blocklist.json` automatically and emails the owner.
3. `booking/manage` page: show the block page for blocked customers so old manage links stop working.

Phone numbers are matched after normalisation (`050 453 2529`, `0504532529`, `+971504532529` and `971504532529` are the same). Emails are matched case-insensitively.

To unblock someone: delete their entry from `blocklist.json` (and optionally reset their row in `cancellations.json`).

Deployment: this folder is not yet on the live site; it needs upload to Hostinger next to the booking code and the three integration calls above.
