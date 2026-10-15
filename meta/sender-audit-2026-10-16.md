# Completed-job → Meta Purchase sender: audit of 8–15 Oct 2026 (Dubai) and reviewable fixes

Prepared Fri 16 Oct 2026 02:30 Dubai, read-only. No Meta, Make or Calendar write was made.
Sources: Make blueprint of 6529499 (nightly Purchase sender) and 6624989 (hourly Lead/Schedule sender); Make
data stores 165821 (completion ledger, 65 records), 158380 (shared "already sent" registry, 205 records,
first 100 read), 158570 (values sent, 103 records, first 100 read), 158811 (TikTok values, first 100 read),
161445 (website booking records); Google Calendar "Cleaning Services Schedule" 8–15 Oct (43 entries);
Meta dataset 614743294720303 stats (28-day limit) and quality; Ads Manager insights 8–15 Oct for jn
(1037126214908677) and JN (9147325105346647).

## 1. How the sender actually works (from the live blueprint, scenario 6529499)

| Item | Live behaviour |
|---|---|
| Schedule | once a day at 00:00 Asia/Dubai (20:00 UTC) |
| Calendar window | events with end > run − 8 days and start < run; calendar justnow.cs@gmail.com |
| Completion marker | description must contain a line starting with `DONE` followed by `YYYY-MM-DD HH:mm` (24 h, two-digit hour); any other form = `HOLD_FORMAT` |
| Time checks | DONE must be ≥ event start and ≤ event end + 24 h, otherwise `HOLD_TIME_CONFLICT`; DONE in the future = `HOLD_FUTURE` |
| Price | taken from a line that **starts** with `Final/New/Updated/Revised/Adjusted price|total|amount:` (preferred) or `Price:|Total price:|Total:|السعر:`; nothing found = `HOLD_PRICE` |
| Phone | taken from a line that **starts** with `Mobile:|Phone:|Number:|Mob:|رقم الموبايل:|رقم موبايل:`; 10–15 digits after normalisation, otherwise `HOLD_PHONE` |
| Event sent | `Purchase`, `event_time` = DONE time (Asia/Dubai), `action_source` = `chat`, `event_id` = `order_id` = calendar event id, value = parsed price, currency AED, `user_data` = ph, fn, ln, ct, country `ae`, external_id = phone (no email, fbp, fbc, IP or user agent) |
| Dedup | ledger 165821 status per calendar id (`SENT`, `LEGACY`, `UNCERTAIN`, `CLAIMED`, `AGED_OUT*`) blocks resends; key present in 158380 = already sent under the old confirmation-time flow → `LEGACY`, never resent; `CLAIMED` written before each send; auto-STOP on any unconfirmed receipt |
| Ageing | a job whose end is older than 601,200 s (6 d 23 h) at run time is written as `AGED_OUT_UNFINALISED` (no DONE) or `AGED_OUT_REVIEW` (DONE but blocked) and is never sent afterwards; this matches Meta's 7-day `event_time` limit |
| Visibility | only `SENT`, `LEGACY`, `AGED_OUT*` are written to the ledger; every `HOLD_*` job is invisible except as a count ("pending finalisation") in the nightly summary |

Hourly sender 6624989 (live since 14 Oct 05:46 Dubai): sends `Lead` (`<id>:lead`) for every non-cancelled booking
with a labelled phone and start within 8 days, and `Schedule` (`<id>:booked`) once the title has no UNCONFIRMED;
`event_time` = time of the hourly run (not the booking time); `action_source` = `website` when the description says
"website booking form", otherwise `chat`; writes `<id>:lead` / `<id>:booked` into 158380. Because the keys carry a
suffix, the Purchase sender's legacy check (bare id) is **not** affected. First run on 14 Oct 06:00 Dubai sent a
backfill burst (38 Lead + 29 Schedule) for bookings since 6 Oct, all stamped with that hour.

## 2. 8–15 Oct: completed jobs vs what Meta received

43 calendar entries: 1 CANCELLED (correctly excluded), 1 blogger collaboration at AED 0, 41 paid completed jobs
(AED 21,097 as written in the descriptions; final amounts are the owner's to confirm).

| Outcome | Jobs | AED | Detail |
|---|---|---|---|
| Sent as completion Purchase (unique, `events_received = 1`, each visible in dataset stats at its DONE hour) | 13 | 4,560 | 11 Oct run 6 (2,377), 14 Oct 2 (798), 15 Oct 4 (1,136), 16 Oct 1 (249) |
| Already in Meta from the old confirmation-time sender (26 Sep–6 Oct), never resent | 7 | 4,133 final / 3,963 in Meta | two values changed after completion: `ipg7odfjvbe98ncko321a8ch1o` 279→369, `1bnb3m54vc8p5b34231774gocs` 249→329; `nkm4t2s3r831jmj9092aoou7pk` and `ug9m60ilguqahf1pbgd8apdttc` carry event_time 27 Sep |
| Never sent and now outside Meta's 7-day window (lost for CAPI) | 5 | 3,555 | see table, "LOST" |
| Never sent, still fixable if the description is corrected before the deadline | 16 | 8,849 | see table, "FIX by" |

Unique accepted Purchase events in the window: **13 server events, 0 browser events**. Attributed in Ads Manager
(8–15 Oct): JN C2 Retargeting 3 purchases (AED 1,207), JN C1 (paused 15 Oct) 1 purchase (AED 350), jn 0 → **4 of 13**.
No live ad set optimises for Purchase, so none of the 13 influenced delivery.

### Per-event verdict (sender logic replayed from the blueprint; nothing was changed)

Phone/price/DONE are quoted as written. "FIX by" = last nightly run (00:00 Dubai) that can still send the job inside
Meta's 7-day limit; the real completion time is the owner's to state, it must not be inferred from the scheduled end
and an ambiguous `02:00` must not be read as `14:00`.

| # | Calendar id | Job (Dubai) | Price line | DONE as written | Sender verdict | Meta state | Action |
|---|---|---|---|---|---|---|---|
| 1 | jvk5jl43rm1e8qvn84h1e7i9qs | 8 Oct 09:15–12:30 Hkriem | 499, mid-paragraph | `DONE 2026-10-08 12:30` | HOLD_PRICE/HOLD_PHONE (labels not at line start) | nothing | LOST (window closed 15 Oct 12:30) |
| 2 | 6626vgmm3s9u2b5mblkhhgstco | 8 Oct 12:00–20:00 Srujana | 999, mid-paragraph | `DONE 2026-10-08 20:00` | same | nothing | LOST |
| 3 | npt4mvr7q5h1075dkj5hmcua3c | 8 Oct 12:00–16:00 Kefah | 249, mid-paragraph | `DONE 2026-10-08 16:00` | blocked before legacy check | LEGACY 249 (6 Oct) | none |
| 4 | 1bnb3m54vc8p5b34231774gocs | 8 Oct 12:20–16:20 Sarangi | 329, mid-paragraph | `DONE 2026-10-08 16:20` | same | LEGACY 249 (3 Oct); final 329 | undercount 80, not correctable |
| 5 | u92tg14c8ucp86av5b8dgkbvl8 | 8 Oct 13:00–17:00 Siraj | 409, mid-paragraph | `DONE 2026-10-08 17:00` | HOLD_PRICE/PHONE | nothing | LOST |
| 6 | ik6t1bmtmqicmj8g3ig5csdmos | 8 Oct 18:00–21:00 Assil | 499, mid-paragraph | `DONE 2026-10-08 21:00` | HOLD_PRICE/PHONE | nothing | LOST |
| 7 | cpgj6c1lc4sm4b9h6lh68b9kcgpmabb16dj64bb675gm6dhk6ph68dpk6g | 8 Oct 21:00–00:00 نوال villa 3 | `Price: AED 1149` | `DONE 2026-10-09 00:00` | HOLD_PHONE (number without `Mobile:` label) | nothing | LOST (window closed 16 Oct 00:00) |
| 8 | vt5dij9do69pce995vfgn5kphs | 9 Oct 09:00–13:00 نجوان | 329 | `DONE 2026-10-09 13:00` | SENT 11 Oct | Purchase 329 | none |
| 9 | 6kp30dph6lij6bb564s36b9k69gj0b9o61j3ib9jcoo3go9l6lh32pj164 | 9 Oct 10:15–14:15 Nour | 479 | `DONE 2026-10-09 14:15` | SENT | Purchase 479 | none |
| 10 | i9doqofq6gjqulnekk2npusas8 | 9 Oct 12:00–16:00 Krunal | 350 | `DONE 2026-10-09 16:00` | SENT | Purchase 350 | none |
| 11 | l1mbnnv31tku1gk4jn4vas57qo | 9 Oct 16:00–21:00 Savita | 320 | `DONE 2026-10-09 21:00` | SENT | Purchase 320 | none |
| 12 | pqbi62oun8c29ravc7bo0qrn0c | 9 Oct 16:00–21:00 ام جمال | 329 | `DONE 2026-10-09 21:00` | LEGACY | 329 (6 Oct) | none |
| 13 | rrqk6btei2mrlo11v55kao5ioo | 9 Oct 16:30–21:30 كنان | 350 | `DONE 2026-10-09 21:30` | SENT | Purchase 350 | none |
| 14 | 6kq30c36cphjebb36grm6b9k6so3ebb26hhjib9m64sj4cpk65i38e1o6k | 9 Oct 17:45–22:00 نوال villa 7 | `Price: AED 919` | `DONE 2026-10-09 22:00` | HOLD_PHONE (number without label) | nothing | add line `Mobile: 0566131332`; Meta window closes **16 Oct 22:00**, before the next nightly run → only an owner-approved manual run of 6529499 before 22:00 today can send it |
| 15 | 49qek6l157m2rj2vqpq651la14 | 9 Oct 19:30–00:30 Harinder | 549 | `DONE 2026-10-10 00:30` | SENT | Purchase 549 | none |
| 16 | m740q2qnjejebkpa230d6nak9o | 10 Oct 12:00–16:00 Praveen | 409 | `DONE 2026-10-10 03:30` | HOLD_TIME_CONFLICT (before start) | nothing | owner writes real time, 24 h; FIX by 17 Oct 00:00 run |
| 17 | nkm4t2s3r831jmj9092aoou7pk | 10 Oct 12:00–16:00 Meera | 329 | `DONE 2026-10-10 04:30` | HOLD_TIME_CONFLICT | LEGACY 329 (27 Sep) | none |
| 18 | qftdnsm4ihoh2ub2mso6hu4nis | 10 Oct 12:00–16:00 Hana | 309 | `DONE 2026-10-10 03:30` | HOLD_TIME_CONFLICT | nothing | FIX by 17 Oct 00:00 |
| 19 | t9fjpjpjkhprenevkmuq0303q4 | 10 Oct 12:15–16:15 Amanie | 459 | `DONE 2026-10-10 05:30` | HOLD_TIME_CONFLICT | nothing | FIX by 17 Oct 00:00 |
| 20 | d0bjd0mlni1mthvfj3ruk3t9pk | 10 Oct 14:30–18:30 Maha | 329 | `DONE 2026-10-10 05:30` | HOLD_TIME_CONFLICT | LEGACY 329 (4 Oct) | none |
| 21 | bflak66pme093qlrtmb557vpds | 10 Oct 16:45–20:45 nabila | 329 | `DONE 2026-10-10 08:30` | HOLD_TIME_CONFLICT | nothing | FIX by 17 Oct 00:00 |
| 22 | bbcoa36jsgjokluvhpcp1tmujs | 11 Oct 08:00–12:00 Rana | 249 | `DONE 2026-10-11 11:30` | SENT 14 Oct | Purchase 249 | none |
| 23 | ug9m60ilguqahf1pbgd8apdttc | 11 Oct 08:00–14:00 Maryam | 2,199 | `DONE 2026-10-11 2:30` | HOLD_FORMAT (one-digit hour) | LEGACY 2199 (27 Sep) | none needed for Meta |
| 24 | t9ble2af1t61r51oqnaep3vrbs | 11 Oct 09:00–13:00 Nisreen | 549 | `DONE 2026-10-11 12:30` | SENT | Purchase 549 | none |
| 25 | 6pijid1pccrjib9gcopm4b9kc9hj0bb260om2bb2clgj8d9o6lh3ic1o70 | 11 Oct 12:00–15:00 Hamza | 329 | `DONE 2026-10-11 04:30` | HOLD_TIME_CONFLICT | nothing | FIX by 18 Oct 00:00 |
| 26 | vr9is2upq7ajd9jd4viujqoc0s | 11 Oct 12:00–16:00 Nour (Shj) | 249 | `DONE 2026-10-11 03:30` | HOLD_TIME_CONFLICT | nothing | FIX by 18 Oct 00:00 |
| 27 | f5sgov73spe58khkne01m5plfg | 11 Oct 16:00–21:00 مروان | 279 | none | EXCL_CANCELLED (title) | nothing | correct |
| 28 | ipg7odfjvbe98ncko321a8ch1o | 12 Oct 08:15–12:15 Reem | 369 | `DONE 2026-10-12 12:30` | LEGACY | 279 (6 Oct); final 369 | undercount 90, not correctable |
| 29 | se3g6n6vl58pubr2jsnlh2crag | 12 Oct 16:00–21:00 Noura S. | `Price: 1,250 AED` | `DONE 2026-10-12 08:30` | HOLD_TIME_CONFLICT | nothing | FIX by 19 Oct 00:00 |
| 30 | 98ce4f57om0466r8ig63qj4d5s | 13 Oct 08:00–11:00 yasmin | 249 | `DONE 2026-10-13 11:30` | SENT 15 Oct | Purchase 249 | none |
| 31 | 3havvhddap46ka2okckru92o60 | 13 Oct 12:00–16:00 Maria | 439 | `DONE 2026-10-13 04:30` | HOLD_TIME_CONFLICT | nothing | FIX by 20 Oct 00:00 |
| 32 | 74ojacpn74q6ab9g69h6cb9kc8s3ab9p6pgmabb6coq66c356cq3echk74 | 13 Oct 13:00–17:00 كفاح | `المبلغ: 379 AED` (label not recognised) | `DONE 2026-10-13 05:30` | HOLD_TIME_CONFLICT, then HOLD_PRICE | nothing | real time + line `Price: AED 379`; FIX by 20 Oct 00:00 |
| 33 | 68p32d1pcgp64b9k64p62b9k6th36bb16th34b9j6ti3cdb3c9h3ec32c4 | 13 Oct 14:15–17:15 mirna | `Total: 350 AED` | `DONE 2026-10-13 05:45` | HOLD_TIME_CONFLICT, then HOLD_PHONE (no label) | nothing | real time + line `Mobile: 0503967172`; FIX by 20 Oct 00:00 |
| 34 | gnavd0uhrhgmj3cb2ulekec2cs | 14 Oct 08:00–12:00 Moukaram | 279 | `DONE 2026-10-14 12:00` | SENT | Purchase 279 | none |
| 35 | em5tnjrhs8acclmqiqval2ef60 | 14 Oct 08:30–11:30 jhonalyn | 279 | `DONE 2026-10-14 11:30` | SENT | Purchase 279 | none |
| 36 | ccp68p9pchij4b9n6hhm8b9kcphmab9o60p34b9mcpi34pj1cgs34c9mcg | 14 Oct 08:45–11:45 Maricar | 329 | `DONE 2026-10-14 11:40` | SENT | Purchase 329 | none |
| 37 | nlruf6uncbm88k8ms4i69ckaf8 | 15 Oct 08:15–11:15 Rafik | 249 | `DONE 2026-10-15 11:15` | SENT 16 Oct | Purchase 249 | none |
| 38 | bs06fbhjj5muvj6jf1t1u9l23c | 15 Oct 08:30–14:00 Hamisha (JN-000039, 050 224 1142) | 550 | `DONE 2026-10-15 02:00` | HOLD_TIME_CONFLICT (ambiguous, do not assume 14:00) | nothing | owner states real time; FIX by 22 Oct 00:00 |
| 39 | q923t476bn8oocncd5ljde1jmo | 15 Oct 11:45–17:45 Porkodi | 750 | `Done 2026-10-15  05:45` | HOLD_TIME_CONFLICT | nothing | FIX by 22 Oct 00:00 |
| 40 | s7lol06rhef58lh1nblq05k0n4 | 15 Oct 12:30–19:30 Manoj | 870 | `Done  2026-10-15 07:30` | HOLD_TIME_CONFLICT | nothing | FIX by 22 Oct 00:00 |
| 41 | g5ssme7hrjf5ttirfp66g98c1s | 15 Oct 13:00–19:00 Mariam J. (blogger) | `Collaboration visit 0 AED` | `Done 2026-10-15 7:00` | HOLD_FORMAT; would send value 0 if the format were fixed | nothing | keep out of Meta; sender needs a zero-value exclusion |
| 42 | si4k60p69ch24bvhker6gg16ek | 15 Oct 15:15–20:15 Delye | 929 | `Done 2026-10-15 9:00 PM` | HOLD_FORMAT (12-hour suffix) | nothing | rewrite `DONE 2026-10-15 21:00`; FIX by 22 Oct 00:00 |
| 43 | 4nan0nd7pc8h28ufef4052a568 | 15 Oct 18:30–21:30 Hamisha (JN-000041, 050 459 5611) | 329 | `Done 2026-10-15 09:00 PM` | HOLD_FORMAT | nothing | rewrite `DONE 2026-10-15 21:00`; FIX by 22 Oct 00:00 |

Hamisha (#38, #43): two calendar events, two references, two different phone numbers and services, same villa. The
owner confirmed on 15 Oct that both bookings are correct (the morning job was extended, the evening job added). For
Meta they are two distinct event_ids and two distinct hashed phones, so no duplicate risk; neither has been sent.

Observation to verify in Make: for the six 8 Oct jobs the blueprint should have written `AGED_OUT_REVIEW` records at
the 16 Oct 00:00 run (end older than 6 d 23 h), yet the ledger gained only the Rafik `SENT` record and the summary.
The per-module execution detail was not retrievable through the API. A plausible cause is the classification module
evaluating `parseNumber(priceStr)` on an empty price and hitting its "ignore" error handler, which drops the bundle
silently. Treat as unproven until the owner opens execution 74a0e338f4264aafb2daf106deced61d in Make.

## 3. Optimization event actually selected per live ad set (8–15 Oct spend)

| Account | Ad set | Optimization | Promoted object | Spend AED | Result |
|---|---|---|---|---|---|
| jn | WA HOME-MOVERS SHJ (T1, 60/day) | CONVERSATIONS (WhatsApp) | none | 397.43 | 133 conversations |
| jn | WA MOTHERHOOD (T2, 30/day) | CONVERSATIONS | none | 204.03 | 69 |
| jn | New Sales Copy B / Copy A / original | CONVERSATIONS (IG/Messenger/WhatsApp) | none | 405.95 / 402.31 / 94.82 | 108 / 106 / 27 |
| jn | 5158 A / B / D | CONVERSATIONS (WhatsApp) | none | 720.80 / 48.47 / 42.53 | 226 / 19 / 11 |
| JN | C2 Retargeting UNION 30D copy | OFFSITE_CONVERSIONS | pixel 614743294720303, event LEAD | 115.05 (ad set) / 717.56 (campaign) | 11 leads (ad set); campaign 27 leads = 11 instant-form + 16 pixel/server, 3 purchases AED 1,207, learning (12 conversions) |
| JN | BOOK-WEB-1 broad (42/day, live since 14 Oct) | OFFSITE_CONVERSIONS | pixel, event LEAD | 85.77 | 20 landing-page views, **0 attributed leads**, learning with 0 conversions |
| JN | W1 / W2 (New Sales Copy 2) | CONVERSATIONS (WhatsApp) | none | 620.49 / 7.38 | 179 / 2 conversations, 10 instant-form leads |

Conclusions: (a) Purchase is not an optimization event anywhere; it is reporting-only today. (b) The two JN website
ad sets optimise on the pixel's **Lead** event from any source. Server Lead events 8–15 Oct: 106 (incl. the 38+4
backfill burst on 14 Oct 06:00 Dubai from 6624989); Schedule 81 (incl. 29+5 backfill). Before 14 Oct a second
sender already produced Lead and Schedule in identical hourly pairs (2–10 a day, phone/name keys only); the likely
source is the respond.io workflow switched to a Lead event on 28 Sep. Since 14 Oct the same booking can therefore
produce two Lead events with different event_ids (respond.io + 6624989). (c) BOOK-WEB-1 cannot learn: server Leads
carry no fbp/fbc/IP/user agent, so a booking after an ad click is rarely attributed; C2 shows attribution only
through phone/name identity matching (EMQ 4.8).

## 4. Reviewable fixes (ranked; every item needs the owner's approval; nothing has been changed)

1. **Make 6529499, module 8 (text normalisation)** – before the label regexes, break one-paragraph website
   descriptions into one label per line: `replace(txt; "/\s(name|mobile|phone|email|whatsapp|service|price|requested slot|address)\s*:/gi"; newline+"$1:")`.
   Effect: jobs like #1, #2, #5, #6 are parsed. Same change in 6624989 module 2.
2. **Phone fallback (6529499 module 9, 6624989 module 3)** – when no labelled phone is found, take the first
   `(\+?971|0)5\d{8}` (also `\+?61\d{9}`) found anywhere in the text. Effect: #7, #14, #33 are parsed.
3. **Price labels** – add `المبلغ`, `الاجمالي|الإجمالي`, `amount`, `cost` to the price regex (module 8). Effect: #32.
4. **DONE time formats (module 9)** – normalise `H:mm`, `h:mm am|pm`, `hh:mm am|pm`, `DONE -`, before the format check
   and convert to 24 h; keep `HOLD_TIME_CONFLICT` for any DONE earlier than the start (never shift 02:00 to 14:00).
   Effect: #23, #42, #43 parse; #38–#40 still wait for the owner's real times.
5. **Zero value** – new class `EXCL_ZERO_VALUE`: never send a Purchase with value 0 (collaborations, #41).
6. **Make every hold visible** – write `HOLD_<reason>` records (status, doneStr, no value) into 165821 for each held
   job and list the held ids and reasons in the nightly "Just Now – Alerts" calendar entry (module 37), so the owner
   sees what to correct before the 7-day limit. Today 16 jobs (AED 8,849) are held and invisible.
7. **Guard `parseNumber`** – in module 10 use `parseNumber(ifempty(priceStr; "0"))` so an empty price can never route a
   bundle into the "ignore" error handler (see the unproven observation above).
8. **Second daily run** – add a 12:00 Dubai run (sends are idempotent through the ledger). Corrections made in the
   morning then reach Meta the same day; the 7-day limit is missed one night less often.
9. **Email as match key** – website bookings since 9 Oct contain `Email:`; add `em` to `user_data` in 6529499 and in
   both branches of 6624989. Zero risk, immediate match-quality gain (today 4.8 with phone/name only).
10. **Browser identifiers from the booking page** – add `fbp`, `fbc` (from `_fbp`, `_fbc`/`fbclid`), client IP and
    user agent to the website webhook (scenario 6369438 interface), keep them on the calendar event or in 161445, and
    pass them in Lead, Schedule and Purchase. This is the change that lets BOOK-WEB-1 and C2 attribute leads and
    purchases to ad clicks; without it BOOK-WEB-1 stays at 0 conversions. Website change: owner/Codex.
11. **One owner per event type** – identify the pre-14 Oct Lead/Schedule sender (respond.io workflow
    1789918101031833 is the candidate) and keep a single sender per event, or dedupe on a shared event_id;
    until then Lead counts in Ads Manager are inflated.
12. **Legacy values** – the confirmation-time Purchases for #4 and #28 under-report by AED 80 and 90; a corrected
    event cannot be sent under the same event_id after 48 h and a new id would double count. Record, do not resend.

Owner-side corrections possible today (no automation change needed), in the sender's required format, each on its own
line in the description: `DONE 2026-10-10 15:30` (24 h), `Price: AED 409`, `Mobile: 0558450318`. Deadlines are in the
table; #14 needs a manual run before 16 Oct 22:00 Dubai in addition to the label.

## 5. New campaign: none proposed (HOLD)

Signal availability does not support a Purchase-optimised or value-optimised ad set: 13 accepted completion
Purchases in 8 days (4 attributed), against Meta's practical need of about 50 attributed events a week. The Lead event
exists (106 server events in 8 days) but is unattributable for BOOK-WEB-1 until fix 10 lands, and is currently
double-sourced (fix 11). Decision under the owner's mandate: HOLD all budgets and structures; FUNNEL FIX items 9–11
first; re-evaluate a Lead-optimised scale-up only after BOOK-WEB-1 shows attributed leads.
