# Why the bookings do not improve the ads — and the plan to make them (Tue 13 Oct 2026, read-only diagnosis)

Owner, Tue 13 Oct ≈ 13:00 Dubai: "So where is the optimization of the current booking which we are receiving? Why there is
no enhancement on the current ads? And if the current ads is not going to read from the optimization, we can switch it off
and create new ads to read properly from the meta optimization."

Short answer: **the ads cannot learn from bookings because the bookings never reach Meta.** Every live ad set optimises for
a proxy (a WhatsApp conversation started, or a browser-pixel Lead), and the two feeds that were meant to carry real
bookings to Meta are starved — one by a missing "DONE" line on the calendar, the other by a lifecycle stage nobody sets.
The owner's instinct is right: the fix is a complete booking signal plus **new** ad sets built on it; the current ad sets
cannot be re-pointed.

## 1. What each live ad set actually optimises for (read 13 Oct)

| Ad sets | Optimisation event Meta receives | Does a booking change delivery? |
|---|---|---|
| jn New Sales (5), 5158 (4), C3 (3), T1/T2, JN W1/W2 | `messaging_conversation_started_7d` (a WhatsApp chat opened) | **No.** Meta is rewarded for a chat, not for a booking. What happens after the first message (price, booking, completed job) is invisible to the auction. |
| JN C1-1, JN retargeting union | browser-pixel `Lead` on justnow.life | **Barely.** §21: Friday ≈ 20 form submissions vs 2 attributed; events fire at the root URL; duplicates. Since Friday C1 spent ≈ AED 412 for **0 attributed Leads** while the calendar received 6 website-form bookings. Lead EMQ is 7.8 (match quality is fine); the count and dedup are the problem. |
| none | `Purchase` / `Schedule` (a real booking) | — no ad set uses them |

## 2. The two booking feeds and why they are empty

**2a. Make scenario 6529499 "Completed job → Meta Purchase" (daily 00:00 Dubai, ENABLED, runs every night):**

| Run (Dubai) | Completed jobs found | Purchases sent | Pending a DONE line | Aged out (never reportable) |
|---|---|---|---|---|
| Thu 9 Oct | 9 | 0 (all legacy) | 37 | 2 |
| Fri 10 Oct | 17 | 0 | 42 | 5 |
| Sat 11 Oct | 25 | **6 (AED 2,377)** | 31 | 16 |
| Sun 12 Oct | 25 | 0 | 29 | 24 |
| Mon 13 Oct | 25 | 0 | 23 | **31** |

The flow only sends a job once its calendar description carries `DONE YYYY-MM-DD HH:mm`. Six jobs were marked on 10 Oct
and went out; **31 completed jobs have now passed Meta's 7-day limit without a DONE line and can never be reported**.
Monday's two DONE lines (Reem 12:30, Noura 08:30) were written at 01:30 Tue, after the midnight run — Reem goes out
tonight; Noura will be **held** because her DONE time (08:30) is before the job start (16:00). Meta shows no Purchase
match-quality row at all because the volume is too small.

**2b. respond.io workflow 1789918101031833 "Send CAPI for Converted Leads"** (published 1 Oct): fires when an agent moves
a contact's lifecycle to the paying stage. Since 20 Sep only **17 contacts are "Customer" and 3 "Qualified"**, none of
them created after 6 Oct, against ≈ 150–180 WhatsApp conversations a day. The stage is set for well under 1 % of chats,
so this feed sends ≈ nothing. (Which event name it sends is not visible through the connector; the pixel shows no server
Purchases other than Make's six.)

**2c. Website:** browser Lead/Schedule/Contact fire in clusters of five from one page, plus a server source sends
Lead + Schedule + Contact per form — without a shared event_id, so Meta cannot deduplicate. Result: the Lead count C1
optimises on is both inflated (duplicates) and incomplete (6 bookings, 0 attributed).

## 3. Why "enhance the current ads" is not available

* The optimisation event is fixed per ad set at creation. Changing it is a new learning phase in Meta's eyes, and for
  click-to-WhatsApp ad sets built under the Engagement objective it is not even offered — they can only optimise for
  conversations. A booking-optimised WhatsApp ad set must be a **new** ad set under the Sales objective ("click to
  WhatsApp, optimise for conversions"), fed by Conversions API events.
* The website ad set can be re-pointed to a server event, but that is also a full relearn; a new ad set next to the old
  one is cleaner because the old one stays as the control.

## 4. Phase 1 — make the booking signal complete (this week; Make and respond.io builds, no Meta ad writes)

**4a. New Make scenario "Booking confirmed → Meta Schedule" (hourly).** Source of truth = the Cleaning Services Schedule
calendar; the website form and the WhatsApp agents both write their bookings there.

* Trigger: calendar events with `start` in [now − 7 d, now + 14 d], `updated` in the last 2 h.
* Filter: title does **not** contain UNCONFIRMED / غير مؤكد, does **not** match the cancel pattern already used by
  6529499, and the datastore has no `BOOKED` record for `event.id`.
* Payload (facebook-conversions-api:SendEvent, pixel 614743294720303): `event_name` **Schedule**, `event_id` =
  `{calendar id}:booked` (idempotent), `event_time` = the event's `updated` time, `user_data` ph (normalised 971…), fn, ln,
  ct, country ae, external_id = phone; `custom_data` value = the price in the description, currency AED,
  content_category `booking_confirmed`, content_name = service. `action_source` = **website** when the description
  contains "From the website booking form", else **chat**.
* Ledger: datastore record `BOOKED|time` with value and phHash; a cancellation later writes `CANCELLED` (no event is
  sent for it — Meta has no negative event; the Purchase flow already excludes cancelled jobs).
* Expected volume: 25–45 events/week (every confirmed booking, both channels, within the hour).
* Created **inactive**, read back, one test run on a fictional event (the 6529364 test harness exists), then enabled by
  the owner.

**4b. Fix the Purchase flow's human dependency.** Two options for the owner:
* (i) Team rule: a `DONE YYYY-MM-DD HH:mm` line within 24 h of every job, time ≥ job start. Evidence says this does not
  happen (31 aged-out jobs in 5 days).
* (ii) **Recommended:** amend 6529499 so a confirmed, non-cancelled job counts as completed **24 h after its end time**
  when no DONE line exists (`event_time` = end time); a DONE line still wins when present. Risk: a no-show that nobody
  marks cancelled is reported as a Purchase; mitigation: the team already titles cancellations "CANCELLED - …".

**4c. respond.io:** keep the "Converted Leads" workflow, but do not depend on it. If the owner wants the WhatsApp ad set to
optimise on business-messaging events specifically, the agent (or a workflow step at "booking confirmed") must also send
the event with `action_source` business_messaging and the click-to-WhatsApp click id; this is verified in Events Manager
→ Business messaging before Phase 2 is built. Until then the phone-hash match of 4a is what Meta has.

## 5. Phase 2 — new ad sets that optimise on bookings (after 7 clean days of 4a, target Wed 21 Oct; earlier if ≥ 50 events)

| New object | Account | Objective / optimisation | Targeting | Budget (no net scale) | Creatives | Control |
|---|---|---|---|---|---|---|
| `jn \| BOOK-WA \| Sales \| Schedule \| UAE excl. AUH` → ad set `BOOK-WA-1 \| broad 25–65` | jn | Sales → click to WhatsApp → optimise for **conversions = Schedule** on 614743294720303 | Dubai + Sharjah + Ajman regions, 25–65, Advantage audience on, excl. customers 120249973174230073 | **AED 80**, taken from New Sales (80 → 40) and 5158 (80 → 40) on activation | Creator Reel 2 3592620130898135, Arabic stove-grease 1870108203957859, Sticky-kitchen reel | the remaining New Sales/5158 ad sets at 40/40 |
| `JN \| BOOK-WEB \| Leads \| Schedule \| UAE excl. AUH` → ad set `BOOK-WEB-1 \| broad 25–65` | JN | Leads/Sales → website → optimise for **Schedule** (server event, deduplicated) | UAE excl. Abu Dhabi, 25–65, Advantage audience on, excl. customers | **AED 42**, taken from C1 (84 → 42) | C1-1-f and C1-1-g (prepared, §21) + the C1 control ad | C1 at 42 |

* **One** booking ad set per channel on purpose: at 25–45 bookings/week in total, two ad sets can reach Meta's ≈ 50
  events/week learning threshold only if nothing else splits the signal. Six booking ad sets would all stay "learning
  limited".
* Pass/fail after 7 days, on **cost per confirmed booking** (calendar), not cost per conversation: PASS = cost per
  booking ≤ 80 % of the control's → fold the control's budget into the booking ad set and pause the control; FAIL = cost
  per booking ≥ the control's after ≥ AED 400 spent → pause the challenger, keep the control.
* T1/T2 (window ends 16 Oct) and W1/W2 are not touched by this; the winner of that test joins the booking ad set's
  creative pool afterwards.
* Purchase (completed job, with value) stays the reporting event for revenue; it is not the optimisation event because
  it arrives 1–3 days late and loses the no-DONE jobs.

## 6. Decisions needed (one word each)

1. **BUILD 4a** — create the hourly "Booking confirmed → Schedule" Make scenario inactive, read it back, test on a fictional
   event, then you enable it.
2. **4b option (i) or (ii)** — team DONE discipline, or auto-complete 24 h after the job end.
3. **PHASE 2 PREPARE** — build the two new campaigns/ad sets PAUSED now (no spend) so they can go live the day the
   signal has 7 clean days; activation and the 40/40/42 budget moves are a separate, owner-present approval.

Nothing in this file has been executed. No Meta write was made.
