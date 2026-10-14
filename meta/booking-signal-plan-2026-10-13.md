# Why the bookings do not improve the ads — and the plan to make them, for WhatsApp AND the website (Tue 13 Oct 2026, read-only)

Owner, Tue 13 Oct ≈ 13:00 Dubai: "So where is the optimization of the current booking which we are receiving? Why there is
no enhancement on the current ads? And if the current ads is not going to read from the optimization, we can switch it off
and create new ads to read properly from the meta optimization." — and at ≈ 13:40: "not only to use the optimization in
messages conversion also through website conversion as well."

Short answer: **the ads cannot learn from bookings because the bookings never reach Meta.** Every live ad set optimises for
a proxy (a WhatsApp conversation started, or a browser-pixel Lead). The hourly feed that used to send every confirmed
booking to Meta was **switched off at the 6–7 Oct cutover** and replaced by a nightly completed-job feed that depends on a
"DONE" line nobody writes. The owner's instinct is right: rebuild the booking signal for both channels, then build
**new** ad sets on it — one for WhatsApp, one for the website; the current ad sets cannot be re-pointed.

## 1. What each live ad set actually optimises for (read 13 Oct)

| Ad sets | Optimisation event Meta receives | Does a booking change delivery? |
|---|---|---|
| jn New Sales (5), 5158 (4), C3 (3), T1/T2, JN W1/W2 | `messaging_conversation_started_7d` (a WhatsApp chat opened) | **No.** Meta is rewarded for a chat. Price, booking and completed job happen after the first message and are invisible to the auction. |
| JN C1-1, JN retargeting union | browser-pixel `Lead` on justnow.life | **Barely.** Friday ≈ 20 form submissions vs 2 attributed (§21); browser events fire in clusters of five from one page; a second server source sends Lead + Schedule + Contact per form without a shared event_id, so Meta cannot deduplicate. Since Friday C1 spent ≈ AED 412 for **0 attributed Leads** while the calendar received 6 website-form bookings. Lead match quality is 7.8 — matching is fine, the count is wrong. |
| none | `Purchase` / `Schedule` (a real booking) | — no ad set uses them |

## 2. The booking feeds, and what happened to them

The calendar is already the single source of truth: Make scenario **6369438** receives every website booking form
(webhook from justnow.life, CORS origin www.justnow.life, returns the calendar id to the browser) **and** every WhatsApp
booking message the AI agent forwards (`source = agent`), creates the UNCONFIRMED entry and dedups by phone|date. The
team confirms by removing UNCONFIRMED from the title. So both channels' booking requests and confirmations are visible in
one place.

| Feed | State | Evidence |
|---|---|---|
| **6410541 "Confirmed booking → Meta Purchase"** (hourly, both channels, phone-matched, ledger 158380) | **INACTIVE since the 6–7 Oct cutover** | ≈ 30 Purchases/week until 6 Oct. This was the booking signal. |
| **6529499 "Completed job → Meta Purchase"** (nightly 00:00, needs `DONE YYYY-MM-DD HH:mm` in the description) | ENABLED, runs every night | 9 Oct 0 sent · 10 Oct 0 · **11 Oct 6 (AED 2,377)** · 12 Oct 0 · 13 Oct 0. **31 completed jobs aged past Meta's 7-day limit without a DONE line and can never be reported**; 23 still pending. Monday's two DONE lines were written at 01:30 Tue, after the run: Reem goes out tonight; Noura is held because her DONE time 08:30 is before the 16:00 job start. |
| respond.io workflow 1789918101031833 "Send CAPI for Converted Leads" (fires on lifecycle → paying stage) | published 1 Oct | 17 "Customer" + 3 "Qualified" contacts since 20 Sep, none created after 6 Oct, against ≈ 150–180 chats/day → sends ≈ nothing. Event name not visible through the connector. |
| 6415385 "Confirmed booking → TikTok CompletePayment" (hourly) | ACTIVE | the same confirmed-booking trigger still feeds TikTok; only Meta lost it. |

## 3. Why "enhance the current ads" is not available

The optimisation event is fixed per ad set. Changing it is a new learning phase, and for click-to-WhatsApp ad sets built
under the Engagement objective it is not offered at all — they can only optimise for conversations. A booking-optimised
WhatsApp ad set must be a **new** ad set under the Sales objective (click to WhatsApp, optimise for conversions), fed by
Conversions API events that carry the click-to-WhatsApp click id. The website ad set could be re-pointed, but that is
also a full relearn; a new ad set next to the old one is cleaner because the old one stays as the control.

## 4. Phase 1 — three booking events, both channels (this week; Make and respond.io builds, no Meta ad writes)

| Event | Moment | Channel tag | Sender | Volume |
|---|---|---|---|---|
| **A. Lead = booking request** | the calendar entry is created (form submitted / agent booking message) | `action_source` **website** when `source = browser`, **chat** when `source = agent` | add one CAPI module to **6369438** right after "createAnEvent": `event_id` = calendar id, `event_time` now, ph/fn/ln/ct/country, value = price, content_category `booking_request` | ≈ 30–45/week (website 25–35, WhatsApp 5–10) |
| **B. Schedule = booking confirmed** | UNCONFIRMED removed from the title | website / chat from the description ("From the website booking form" vs the WhatsApp template) | **clone 6410541** → "Confirmed booking → Meta Schedule": `event_name` Schedule, `event_id` = calendar id + `:booked`, **new ledger datastore** (158380 must stay untouched — 6529499 reads it as the legacy "already sent" list), no top-up branch, hourly | ≈ 25–40/week |
| **C. Purchase = completed job, with value** | DONE line, or (recommended) **24 h after the job end when no DONE line and not cancelled** | chat | 6529499 with the auto-complete rule; a DONE line still wins | ≈ 25–35/week |

**Website dedup (needed for A to be clean):** the site already receives the calendar id back from 6369438
("booking_v1|created|{id}"). The browser pixel's Lead must fire **after** that response with `eventID` = the same calendar
id, and the second server Lead source (not in Make; identify it in Events Manager → Data sources → the Lead event's
connections) is switched off or given the same event_id. Until that is done, A is sent with `action_source` website and
the browser Lead is left as is; Meta deduplicates only on matching event_id, so the switch-off is the reliable fix.

**WhatsApp click id (needed for the WhatsApp ad set, not for reporting):** Meta's click-to-WhatsApp conversion
optimisation expects events sent through the Conversions API for business messaging with the `ctwa_clid` of the
conversation. respond.io has that id; Make does not. Mechanism: the hourly Schedule flow (B) also calls the respond.io
API to set the matched contact's lifecycle to **Customer**, which fires the already-published "Send CAPI for Converted
Leads" workflow → the event goes out with the click id, automatically, no agent action. Owner check before Phase 2: open
that workflow and confirm its event name is **Schedule** (or Purchase, consistently with B/C) and that the pixel is
614743294720303. Phone-matched events from Make remain the fallback and are enough for attribution and reporting.

**Reports after 7 days:** Events Manager shows A/B/C by channel; the log carries cost per booking request, per confirmed
booking and per completed job for every campaign — the numbers the owner asked for.

## 5. Phase 2 — new ad sets that optimise on bookings, one per channel (after 7 clean days of Phase 1, target Wed 21 Oct; earlier if ≥ 50 events)

| New object | Account | Objective / optimisation | Targeting | Budget (no net scale) | Creatives | Control kept |
|---|---|---|---|---|---|---|
| `jn \| BOOK-WA \| Sales \| WhatsApp conversions` → ad set `BOOK-WA-1 \| broad 25–65` | jn | Sales → click to WhatsApp → optimise for **conversions = Schedule** (B, with click id via respond.io) | Dubai + Sharjah + Ajman regions, 25–65, Advantage audience on, excl. customers 120249973174230073 | **AED 80** from New Sales (80 → 40) and 5158 (80 → 40) | Creator Reel 2 3592620130898135, Arabic stove-grease 1870108203957859, Sticky-kitchen reel | New Sales/5158 at 40/40 |
| `JN \| BOOK-WEB \| Leads \| website booking` → ad set `BOOK-WEB-1 \| broad 25–65` | JN | Leads → website → optimise for **Lead = booking request** (A, server-sent, deduplicated, action_source website); Schedule and Purchase reported for the pass/fail | UAE excl. Abu Dhabi, 25–65, Advantage audience on, excl. customers | **AED 42** from C1 (84 → 42) | C1-1-f and C1-1-g (prepared, §21) + the C1 control ad | C1 at 42 |

* Website optimises on the **request** (A) rather than the confirmation because it fires minutes after the click and is
  the larger count; the request-to-confirmation rate on the website is high and is reported anyway. WhatsApp optimises on
  the **confirmation** (B) because the WhatsApp request moment is only as structured as the agent's message.
* **One** booking ad set per channel on purpose: at 30–45 events/week per event type, two ad sets can approach Meta's
  ≈ 50 events/week learning threshold; six would all stay "learning limited".
* Pass/fail after 7 days on **cost per confirmed booking** (calendar), not cost per conversation or per pixel Lead:
  PASS = ≤ 80 % of the control's → fold the control's budget into the booking ad set and pause the control; FAIL = ≥ the
  control's after ≥ AED 400 spent → pause the challenger, keep the control.
* T1/T2 (window ends 16 Oct) and W1/W2 are not touched; the winner of that test joins the booking ad set's creative pool.
* Purchase (C, with value) is the revenue event for reporting; it is not the optimisation event because it arrives 1–3
  days late.

## 6. Decisions needed (one word each)

1. **BUILD PHASE 1** — add the Lead module to 6369438, clone 6410541 as the Schedule sender (new ledger), add the
   auto-complete rule to 6529499 and the respond.io lifecycle call; everything created inactive, read back, tested on a
   fictional booking (the 6529364 harness), then enabled by the owner.
2. **AUTO-COMPLETE yes/no** — option (ii) in §4 row C; "no" means the team writes a DONE line within 24 h, time ≥ job start.
3. **PREPARE PHASE 2** — build the two campaigns/ad sets PAUSED now (no spend) so they go live the day the signal has 7
   clean days; activation and the 40/40/42 budget moves are a separate, owner-present approval.

Owner-side checks: (a) open respond.io workflow "Send CAPI for Converted Leads" and read its event name and pixel;
(b) Events Manager → Lead event → connections, to name the second server source; (c) confirm the website script can
fire the browser Lead with the returned calendar id as eventID (Webador custom code).

**Execution status (Wed 14 Oct 06:40 Dubai):** on the owner's order "fix the optimization of the booking page now",
Phase 1 events A and B are live (Make scenario 6624989, hourly, both channels — built as one scenario instead of the two
edits above; event C / auto-complete still awaits the owner's yes/no) and the website row of Phase 2 is live (JN campaign
120252289064660312, ad set 120252289067460312 at AED 42/day, three ads; C1 84 → 42). The WhatsApp row (BOOK-WA) is not
built. Details and read-backs: `meta/execution-log-2026-10-09.md` §28.
