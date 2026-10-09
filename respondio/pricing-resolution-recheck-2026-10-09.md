# PRICING RESOLUTION CORRECTION — re-check of the recent wrong / unlisted quotes (2026-10-09, evening)

Owner order: exact-area match → geographic mapping to an existing zone → landmark/building/street
resolution (ask once if unclear) → Level 2 only when exact matching AND reliable geographic resolution
both fail. Never an emirate-wide default, never another emirate's zone, never an invented zone, never
conversational memory instead of the map. No permanent list additions without owner approval.

Source of the approved zone list and price table: the live agent prompt ("Just Now update",
respond.io user 76226525, Knowledge 03–04 lists) and `respondio/whatsapp-agent-prompt.txt` (full
area lists). The two Level 2 knowledge files (kb_justnow_v3_l2.md 168623, fixed_texts_l2.md 168624)
are stored on an S3 host this session cannot reach; they still carry the old "unlisted area → Level 2"
wording and should be re-uploaded by the owner with the new sequence (the prompt wins over Knowledge,
so the live behaviour is already corrected).

Prices used (first package, AED): zone A kitchen/partial 249 · 1BHK 379 · 2BHK 499 · 3BHK 669;
zone B 279 · 409 · 549 · 729; zone C 329 · 499 · 659 · 879.

## 1. Re-check of today's unlisted / landmark quotes (all handled by the live agent on 9 Oct)

| # | Customer ID | Provided location | Exact-list match | Geographic location resolved | Mapped JustNow zone | Correct package price | Agent actually sent | Confidence | Action |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 554921504 | "الشارقة القصباء" (Al Qasba, Sharjah), full house 1 BHK | NO | Al Qasba canal district inside Al Khan, between Al Khan lagoon and Al Majaz (both zone A) | Sharjah **A** | 3 cleaners × 3 h – **AED 379** | AED 379 | HIGH | price was correct |
| 2 | 554912916 | "القصباء" (Al Qasba, Sharjah), 2 BHK | NO | same as #1 | Sharjah **A** | 3 cleaners × 4 h – **AED 499** | **AED 549** (zone B row) | HIGH | **send correction** (549 → 499) |
| 3 | 555035920 | "mahatta", Sharjah, partial (living, toilet, kitchen) | NO | Al Mahatta, central Sharjah between Al Qasimia, Abu Shagara and Al Nabba (all A) | Sharjah **A** | 2 cleaners × 3 h – **AED 249** | AED 249 | HIGH | price was correct |
| 4 | 554942211 | "خلف الميجا مول" (behind Mega Mall), Sharjah, 3 BHK + sofa | NO (landmark) | Mega Mall, Al Estiqlal St, Bu Daniq / Al Qasimia (A) | Sharjah **A** | 4 cleaners × 4 h – **AED 669** (+ sofa photos → Level 2 by design) | AED 669 + photo request | HIGH | price was correct |
| 5 | 554906582 | "Burjuman", Dubai, 1 bedroom | NO (landmark) | BurJuman Centre, Al Mankhool, Bur Dubai (B) | Dubai **B** | 3 cleaners × 3 h – **AED 409** | AED 409 (customer declined) | HIGH | price was correct |
| 6 | 555013483 | "Al Hudaiba", Dubai, kitchen | NO | Al Hudaiba community (Bur Dubai sector): Al Jafiliya, Satwa and Al Mankhool (all B) on its east and south, Jumeirah 1 (C) only on its west; it lies on the Bur Dubai side of the B/C line | Dubai **B** | 2 cleaners × 3 h – **AED 279** | Level 2 line | MEDIUM (edge community) | **send correction** once the owner confirms Al Hudaiba = B (otherwise: ask for a location pin) |
| 7 | 554741396 | "دبي دماك هيلز ٢" (Damac Hills 2), 3-bedroom villa | NO ("Damac Hills" is listed; Damac Hills 2 / Akoya Oxygen is a different community ≈ 20 km further out) | Outer Dubailand belt near Al Qudra / Lehbab; every approved area around it is C (Arabian Ranches, Damac Hills, Mudon, Remraam, Town Square, Lehbab) | Dubai **C** | 3-bedroom = 3 BHK row: 4 cleaners × 4 h – **AED 879** | Level 2 line (Arabic) | HIGH | **send correction** |
| 8 | 554734499 | "جمال عبد الناصر" (Jamal Abdul Nasser St), Sharjah, kitchen | NO (street) | The main street of Al Majaz, running Al Majaz 1–3 to Al Taawun / Al Khan (all A) | Sharjah **A** | 2 cleaners × 3 h – **AED 249** | Level 2 line + "غير موجودة ضمن المناطق المسعّرة" | HIGH | **send correction** (customer explicitly asked "عاملتان في ثلاث ساعات كم") |
| 9 | 554869856 | "Mwilih commercial" (Muwaileh Commercial), Sharjah, 1 BHK | NO as written ("Muwaileh" is listed) | Sub-area inside Muwaileh | Sharjah **A** | 3 cleaners × 3 h – **AED 379** | AED 379 | HIGH | price was correct |
| 10 | 554976892 | "البراحه" then "اشارقه" (Al Baraha, Sharjah), kitchen | NO for Sharjah ("Al Baraha" exists only in the Dubai B list, Deira) | Not resolvable: no Al Baraha community in Sharjah; could be Al Baraha, Deira (customer living elsewhere), a local nickname or a typo | — | B 279 if Al Baraha, Deira; A 249 if a Sharjah-city district | Level 2 line after asking "Dubai or Sharjah?" | LOW | **ask for exact location** (community name or pin), Level 2 only if still unresolved |
| 11 | 555063773 | "Alnahda" after "Sharjah", kitchen | **YES** (Al Nahda, Sharjah) | — | Sharjah **A** | AED 249 | AED 249 | HIGH | price was correct (agent asked the emirate first — correct handling of the shared name) |

Summary: 7 of the 11 were priced correctly (the agent already resolved Al Qasba, Al Mahatta, Mega Mall,
BurJuman and Muwaileh Commercial by geography); 1 wrong zone (Al Qasba 2 BHK quoted at B); 3 sent to
Level 2 although they resolve (Al Hudaiba, Damac Hills 2, Jamal Abdul Nasser St); 1 genuinely
unresolved (Al Baraha, Sharjah). The four named by the owner — Al Qasba, Al Mahatta, Behind Mega Mall,
BurJuman — all resolve with HIGH confidence; only the Arabic Al Qasba 2 BHK quote needs a correction.

## 2. Correction messages (prepared, NOT sent — owner approval first)

* **#2 — 554912916 (Arabic):** "عذراً على الخطأ 🙏 السعر الصحيح لتنظيف بيت غرفتين وصالة في القصباء، الشارقة 👇\n• 3 عاملات × 4 ساعات – 499 درهم\nكل شي شامل: الفريق والمواصلات وجهاز البخار والأدوات والمواد.\nاحجز موعدك خلال دقيقة: https://www.justnow.life/book-now?utm_source=whatsapp"
* **#7 — 554741396 (Arabic):** "تحديث من فريقنا 😊 دماك هيلز 2 ضمن مناطق خدمتنا. تنظيف البيت العميق لفيلا 3 غرف في دماك هيلز 2، دبي 👇\n• 4 عاملات × 4 ساعات – 879 درهم\nكل شي شامل: الفريق والمواصلات وجهاز البخار والأدوات والمواد.\nاحجز موعدك خلال دقيقة: https://www.justnow.life/book-now?utm_source=whatsapp"
* **#8 — 554734499 (Arabic):** "تحديث من فريقنا 😊 شارع جمال عبد الناصر ضمن منطقة المجاز، الشارقة. تنظيف المطبخ العميق 👇\n• عاملتان × 3 ساعات – 249 درهم\nكل شي شامل: الفريق والمواصلات وجهاز البخار والأدوات والمواد.\nاحجز موعدك خلال دقيقة: https://www.justnow.life/book-now?utm_source=whatsapp"
* **#6 — 555013483 (English, after the owner confirms B):** "Update from our team 😊 Al Hudaiba is covered. Kitchen deep cleaning in Al Hudaiba, Dubai 👇\n• 2 cleaners × 3 hours – AED 279\nEverything included: team, transport, steam machine, tools and materials.\nBook your slot in one minute: https://www.justnow.life/book-now?utm_source=whatsapp"
* **#10 — 554976892 (Arabic, ask once):** "عشان نعطيك السعر الصحيح، ممكن تكتب اسم المنطقة أو المجمع بالضبط، أو ترسل اللوكيشن؟ 😊"

## 3. Proposed permanent additions to the approved lists (NOT applied — owner approval required)

| Area / landmark | Emirate | Proposed zone | Basis | Confidence |
|---|---|---|---|---|
| Al Qasba (القصباء) | Sharjah | A | inside Al Khan / next to Al Majaz | HIGH |
| Al Mahatta (المحطة) | Sharjah | A | central Sharjah, between Al Qasimia and Abu Shagara | HIGH |
| Mega Mall (ميجا مول) → Bu Daniq / Al Qasimia | Sharjah | A | landmark inside listed A areas | HIGH |
| Jamal Abdul Nasser Street (شارع جمال عبد الناصر) → Al Majaz | Sharjah | A | street inside Al Majaz / Al Taawun | HIGH |
| Muwaileh Commercial | Sharjah | A | part of Muwaileh | HIGH |
| BurJuman → Al Mankhool, Bur Dubai | Dubai | B | landmark inside listed B areas | HIGH |
| Damac Hills 2 (Akoya Oxygen) | Dubai | C | outer Dubailand belt, surrounded by C areas | HIGH |
| Al Hudaiba (الحضيبة) | Dubai | B (decision) | Bur Dubai-sector community on the B/C edge | MEDIUM |

Seen on 7–8 Oct (previous agent version, not re-checked here, same method gives): Al Qadisiya (Sharjah,
next to Al Qasimia / Al Yarmook → A, HIGH), Al Butina (Sharjah city → A, HIGH), Aljada (Sharjah,
Muwaileh / University City → A, HIGH), Al Mareija (Sharjah old town next to Rolla → A, HIGH),
"Downtown Jebel Ali" (Dubai → C via Jebel Ali, HIGH), "Italy cluster, International City" (Dubai → B,
HIGH). Unresolved without asking: "Al Wadha" (contact 554659547), "Shaheen Tower" (553970991), "behind
Al Maya market, second row from the Corniche" (554126088).

## 4. What changed in the live agent (respond.io user 76226525 "Just Now update")

* ZONES section replaced by the four-step PRICING RESOLUTION (exact match → geographic mapping with
  zone boundaries per emirate → landmark/building/street with one clarifying question → Level 2 only
  when 1 and 2 both fail), plus the explicit bans (no emirate-wide default, no borrowed emirate zone,
  no invented zone, no memory instead of the map).
* FLOW step 5: "Emirate alone is enough" now only for RAK and Fujairah (single-zone emirates); for
  Ajman and UAQ the agent asks the area once because Masfout, Manama and Falaj Al Mualla are zone D.
  **Owner can revert this one line if the extra question is unwanted.**
* LEVEL 2 list: "unlisted area" → "an area that fails ZONES steps 1–3".
* Knowledge sources (168623, 168624), actions, tags, lifecycle, reminders: unchanged.
* Rollback: `respondio/live-agent-prompt-2026-10-09.before-pricing-resolution.txt` (exact live text
  before the change); new text: `respondio/live-agent-prompt-2026-10-09.pricing-resolution.txt`.
* Not touched: the test agent 76239818 "JN repair test copy (do not route customers)" and the
  inactive older agents.

## 5. Owner decisions pending

1. Approve (or edit) the correction messages in §2 — sent only on approval.
2. Confirm Al Hudaiba = zone B (or ask the customer for a pin).
3. Approve the permanent additions in §3 (then they go into the prompt lists and the re-uploaded
   Knowledge 03–04 files).
4. Re-upload kb_justnow_v3_l2.md / fixed_texts_l2.md with the new wording (this session cannot
   reach their S3 host).
