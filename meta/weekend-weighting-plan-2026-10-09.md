# META BUDGET STRATEGY — WEEKEND WEIGHTING (day-of-week analysis and rule design)

Prepared 2026-10-09 ≈ 10:50 Dubai. Status: **PROPOSAL — no budget changed yet.** Sources: Meta daily
campaign rows for jn 1037126214908677 and JN 9147325105346647, 11 Jul – 8 Oct 2026 (13 weeks, 48
campaigns, read in three 30-day windows after the connector's 1,000-row cap silently truncated the single
90-day pull); the "Cleaning Services Schedule" Google Calendar for the same window (582 events, 13 marked
cancelled/postponed → 569 confirmed bookings); the Make Purchase ledger for completed-service status.

## 1. Day-of-week performance

### 1a. Meta (jn + JN combined, averages per weekday over 13 weeks)

| Day | Spend/day | CPM | Conversations/day | Cost / conversation | Website leads/day | Meta-attributed purchases/day |
|---|---|---|---|---|---|---|
| MON | 853 | 10.4 | 156.6 | 5.45 | 1.54 | 0.15 |
| TUE | 596 | 9.0 | 111.8 | 5.33 | 1.46 | 0.38 |
| WED | 567 | 9.1 | 105.1 | 5.40 | 0.85 | 0.00 |
| THU | 614 | 9.1 | 110.2 | 5.57 | 1.15 | 0.15 |
| FRI | 579 | 9.0 | 110.2 | **5.26** | 0.83 | 2.00 (test events) |
| SAT | 552 | 9.2 | 110.7 | **4.99** | 1.85 | 0.31 |
| SUN | 791 | 9.8 | 134.9 | 5.87 | **2.38** | 0.46 |

Conversation volume follows spend almost one-to-one; the efficiency signal is cost per conversation:
best Saturday and Friday, worst Sunday and Thursday. Per account: jn cost/conv Sat 5.10 … Sun 6.04; JN
Sat 4.80 … Thu 6.21.

### 1b. Bookings (calendar, confirmed events)

| Day | Jobs served/day (13 wk) | Jobs served/day (Sep 9 – Oct 8) | Bookings **created**/day | Meta spend per booking created |
|---|---|---|---|---|
| MON | 4.85 | 4.00 | 6.23 | 137 |
| TUE | 5.62 | 4.25 | 6.62 | 90 |
| WED | 5.31 | 4.00 | 5.15 | 110 |
| THU | 5.31 | 4.60 | **6.85** | 90 |
| FRI | 6.75 | 5.00 | **7.25** | **80** |
| SAT | **8.77** | **8.50** | 5.31 | 104 |
| SUN | **7.69** | **8.25** | 6.31 | 125 |

Median lead time from booking to service is **1 day** (62 % same- or next-day), so Saturday's service
peak is bought on Thursday and Friday, and Sunday's on Friday and Saturday. Completed-service rate and
revenue per weekday are **not measurable historically**: the DONE marker exists on only 17 events (all
after the 6 Oct cutover) and only 95 events carry an AED amount (average AED 436). Cleaner-hours
(parsed for 226 jobs, median 8) are flat across weekdays (≈10 per job), so revenue tracks job count.

### 1c. Classification

```
MON: LOW DEMAND   (fewest jobs served, most expensive booking)
TUE: NORMAL
WED: LOW DEMAND
THU: HIGH         (booking creation rises; buys Friday/Saturday jobs)
FRI: PEAK         (most bookings created, cheapest booking, cheapest conversation after Saturday)
SAT: PEAK         (most jobs served; creation lower but still the cheapest conversation)
SUN: HIGH         (second-most jobs served and most website leads, but the most expensive conversation/booking)
```

Capacity signal: 90/90 days had bookings; median 6 jobs/day, p90 10, **observed maximum 12** (Sat 15 Aug,
Sun 16 Aug, Sat 22 Aug, Sat 12 Sep). Weekend days are currently at 8–9, so headroom is ≈ 3 jobs/day
before the historical ceiling. Weekly bookings fell from 55–61 (August) to 28–45 (late Sep / Oct) in
step with the September spend dip, so volume is still spend-elastic.

## 2. Multipliers

The owner's starting shape (Mon–Wed 80 %, Thu 120 %, Fri 140 %, Sat 140 %, Sun 120 %) is **not strongly
contradicted**. The data suggests two refinements: Sunday is the least efficient high day (cost/booking
125, cost/conv 5.87) and Saturday-created bookings are modest, so part of Saturday's weight is better
spent on Friday. Tuesday is more efficient than Mon/Wed.

| | MON | TUE | WED | THU | FRI | SAT | SUN | Weekly factor |
|---|---|---|---|---|---|---|---|---|
| Owner intent | 0.80 | 0.80 | 0.80 | 1.20 | 1.40 | 1.40 | 1.20 | 7.60 (+8.6 %) |
| **Recommended** | **0.80** | **0.90** | **0.80** | **1.20** | **1.40** | **1.30** | **1.10** | **7.50 (+7.1 %)** |

Either shape is acceptable; the recommended one keeps the Thu–Sun shift and trims the two days where
the extra dirham buys the least. Final choice is the owner's.

## 3. Scope by account mission (baseline = today's budgets)

| Campaign | Mission | Baseline /day | Rule set | Note |
|---|---|---|---|---|
| jn 120249855229580073 "jn - WhatsApp Sales 5158" (CBO) | WhatsApp sales | 90 | **W** (full weekend shape) | proven, 5 winners |
| jn 120249855697050073 "New Sales Campaign" (CBO) | WhatsApp sales | 90 | **W** | proven, 4 winners |
| jn 120250020646250073 "JN \| C3 WhatsApp Bookings" (CBO) | WhatsApp sales | 90 | **W** | C3-1/2/3 live, C3-4 paused today |
| JN 120252107068880312 "C1 Website Acquisition" (CBO) | Website bookings | 84 | **W** | website rate supports Thu–Sun (leads Sun 2.4/day, Sat 1.9) |
| JN 120252107080200312 "C2 Retargeting" (CBO) | Retargeting | 70 | **R** (stable: Fri/Sat 1.15, all other days 1.00) | never starved Mon–Wed |
| **EXCLUDED** jn 120250144447740073 T1/T2 (ABO 60 + 30) | migration test | 90 | none until the 16 Oct scorecard | clean baseline first |
| **EXCLUDED** JN 120251948470120312 W1/W2 (CBO 80) | migration source | 80 | none | changing it would break the T1/T2 parity comparison |
| **EXCLUDED** jn 120250144448010073 reactivation | — | 0 (PAUSED) | none | not live |
| **EXCLUDED** justnow22 | creative testing | 0 | none | no campaigns yet; test budgets stay flat by rule |
| **EXCLUDED** Purchase | — | 0 | none | gate FAIL |

```
CURRENT WEEKLY META BUDGET:   AED 4,158  (594/day: jn 360 + JN 234, after today's pauses; was 654/day this morning)
PROPOSED WEEKLY META BUDGET:  AED 4,391  (recommended shape)  ·  AED 4,427 (owner shape)
EXPECTED EXTRA THU–SUN SPEND: +AED 446 per week on the W set (jn 324 + C1 101 + C2 21), offset by −AED 212 Mon–Wed
PEAK-DAY TOTAL (Fri):         ≈ AED 747/day across both accounts   ·   WEEKDAY TOTAL (Mon–Wed): ≈ AED 523/day
```

## 4. Automated rules (UAE time, Asia/Dubai) — exact schedule

Meta Automated Rules are not exposed by the connector, so they are created once in Ads Manager
(Automated rules → Create → Custom rule, Action "Adjust budget → Set to", Schedule "Custom", apply to
the five campaigns above). Each campaign gets **one rule per time slot** and nothing else, so no two
rules can fire on the same campaign at the same time. Steps are staged so no single change exceeds
+25 % / −20 %.

| Slot (Asia/Dubai) | W set: jn ×3 (base 90) | W set: JN C1 (base 84) | R set: JN C2 (base 70) |
|---|---|---|---|
| Thu 00:00 | set to 90 (1.00) | set to 84 | no rule |
| Thu 12:00 | set to 108 (1.20) | set to 101 | no rule |
| Fri 00:00 | set to 126 (1.40) | set to 118 | set to 80 (1.15) |
| Sat 00:00 | set to 117 (1.30) · owner shape: 126 | set to 109 · owner: 118 | no change (80) |
| Sun 00:00 | set to 99 (1.10) · owner shape: 108 | set to 92 · owner: 101 | set to 70 |
| Mon 00:00 | set to 86 (−13 %) | set to 80 | no rule |
| Mon 12:00 | set to 72 (0.80) | set to 67 | no rule |
| Tue 00:00 | set to 81 (0.90) · owner shape: 72 | set to 76 · owner: 67 | no rule |
| Wed 00:00 | set to 72 (0.80) | set to 67 | no rule |

Capacity guard (one extra rule, all W campaigns): **if yesterday's confirmed bookings ≥ 11 or today's
booked jobs ≥ 11, skip the next increase** (hold the current budget) — Meta rules cannot read the
calendar, so this guard runs through the daily 09:22 check-in: it reads the calendar count and, on a
breach, proposes the hold to the owner before the next slot. Quality guard tracked daily: CPA, booking
rate (bookings created ÷ conversations), frequency, CPM; if Fri/Sat spend lifts volume but booking rate
falls more than 20 % versus the Tue–Wed baseline, cap at the Thursday level.

Read-back after creation: Ads Manager → Automated rules → each rule's "Schedule" and "Apply to" list,
and Campaigns view at 00:05 and 12:05 Dubai on the first Thursday (16 Oct) to confirm the set-to values.

## 5. T1 / T2 handling

T1 (AED 60) and T2 (AED 30) stay flat through the 7-day observation window (to 16 Oct). After the first
scorecard they join the W set at their then-current budgets (or the raised AED 80 / 40 if they pass), as
a separate rule group created at that time. W1/W2 (JN) are never scheduled: they are paused after parity,
not scaled.

## 6. First-cycle option (if rules are not yet created by Thursday)

The same values can be applied as owner-approved manual writes through this session on Thu 16 Oct
12:00, Fri 00:00, Sat 00:00, Sun 00:00 and Mon 00:00 / 12:00 Dubai (each a prompted write with
read-back). Not applied today: it is already Friday, T1/T2 went live two hours ago, and a +40 % jump on
the proven campaigns the same morning would violate the owner's "no abrupt one-step change" rule.
