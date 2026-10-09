# META AUTOMATED RULES — WEEKEND WEIGHTING (approved multipliers, copy-ready spec)

Approved by the owner 2026-10-09: MON 0.80 · TUE 0.90 · WED 0.80 · THU 1.20 · FRI 1.40 · SAT 1.30 · SUN 1.10.
Meta-native Automated Rules only (the connector has no rule-creation tool, so these are created once in
Ads Manager → All tools → Automated rules → Create rule → *Custom rule*). No recurring session writes.

## Scope

| Group | Campaigns (CBO, Asia/Dubai account time zone) | Base daily budget |
|---|---|---|
| **W-jn** | jn 120249855229580073 "jn - WhatsApp Sales 5158 - New Audiences Sep 2026" · jn 120249855697050073 "New Sales Campaign" · jn 120250020646250073 "JN \| C3 WhatsApp Bookings \| Oct 2026" | AED 90 each |
| **W-C1** | JN 120252107068880312 "JN \| C1 Website Acquisition \| book-now \| Oct 2026" | AED 84 |
| **R-C2** | JN 120252107080200312 "JN \| C2 Retargeting High-intent \| Oct 2026" | AED 70 (stable profile) |

Never in any rule: jn T1/T2 campaign 120250144447740073 (baseline until 16 Oct), JN W1/W2 campaign
120251948470120312 (parity control), jn reactivation 120250144448010073, anything in justnow22, any
Purchase campaign.

## Rule table — action "Adjust budget → Set daily budget to", condition "Daily budget > AED 1", schedule "Custom" (day + time, account time zone), one rule per row, applied to the whole group

| # | Rule name | Group | Schedule (Dubai) | Set daily budget to | Multiplier |
|---|---|---|---|---|---|
| 1 | `WW \| W-jn \| THU 00:00 \| 1.00` | W-jn (3 campaigns) | Thursday 00:00 | AED 90 | 1.00 (staged step up from 0.80) |
| 2 | `WW \| W-jn \| THU 12:00 \| 1.20` | W-jn | Thursday 12:00 | AED 108 | 1.20 |
| 3 | `WW \| W-jn \| FRI 00:00 \| 1.40` | W-jn | Friday 00:00 | AED 126 | 1.40 |
| 4 | `WW \| W-jn \| SAT 00:00 \| 1.30` | W-jn | Saturday 00:00 | AED 117 | 1.30 |
| 5 | `WW \| W-jn \| SUN 00:00 \| 1.10` | W-jn | Sunday 00:00 | AED 99 | 1.10 |
| 6 | `WW \| W-jn \| MON 00:00 \| 0.95` | W-jn | Monday 00:00 | AED 86 | 0.95 (staged step down) |
| 7 | `WW \| W-jn \| MON 12:00 \| 0.80` | W-jn | Monday 12:00 | AED 72 | 0.80 |
| 8 | `WW \| W-jn \| TUE 00:00 \| 0.90` | W-jn | Tuesday 00:00 | AED 81 | 0.90 |
| 9 | `WW \| W-jn \| WED 00:00 \| 0.80` | W-jn | Wednesday 00:00 | AED 72 | 0.80 |
| 10 | `WW \| W-C1 \| THU 00:00 \| 1.00` | W-C1 | Thursday 00:00 | AED 84 | 1.00 |
| 11 | `WW \| W-C1 \| THU 12:00 \| 1.20` | W-C1 | Thursday 12:00 | AED 101 | 1.20 |
| 12 | `WW \| W-C1 \| FRI 00:00 \| 1.40` | W-C1 | Friday 00:00 | AED 118 | 1.40 |
| 13 | `WW \| W-C1 \| SAT 00:00 \| 1.30` | W-C1 | Saturday 00:00 | AED 109 | 1.30 |
| 14 | `WW \| W-C1 \| SUN 00:00 \| 1.10` | W-C1 | Sunday 00:00 | AED 92 | 1.10 |
| 15 | `WW \| W-C1 \| MON 00:00 \| 0.95` | W-C1 | Monday 00:00 | AED 80 | 0.95 |
| 16 | `WW \| W-C1 \| MON 12:00 \| 0.80` | W-C1 | Monday 12:00 | AED 67 | 0.80 |
| 17 | `WW \| W-C1 \| TUE 00:00 \| 0.90` | W-C1 | Tuesday 00:00 | AED 76 | 0.90 |
| 18 | `WW \| W-C1 \| WED 00:00 \| 0.80` | W-C1 | Wednesday 00:00 | AED 67 | 0.80 |
| 19 | `WW \| R-C2 \| FRI 00:00 \| 1.15` | R-C2 | Friday 00:00 | AED 81 | 1.15 (holds through Saturday) |
| 20 | `WW \| R-C2 \| SUN 00:00 \| 1.00` | R-C2 | Sunday 00:00 | AED 70 | 1.00 (Mon–Thu stay at 70) |

No step exceeds +25 % or −20 %. Every campaign has at most one rule per time slot, so rules cannot
conflict. If "Set daily budget to" is not offered in your Ads Manager version, use the percentage
variant: same slots, actions +25 %, +20 %, +17 %, −7 %, −15 %, −14 %, −16 %, +13 %, and replace row 9/18
with "Set to AED 72 / 67" as the weekly anchor (prevents rounding drift).

Rule settings common to all rows: Apply rule to → the group's campaigns only; Action → Adjust budget →
Set daily budget to [amount]; Conditions → Daily budget greater than 1; Time range → Today;
Schedule → Custom → the one day/time in the row; Notification → email on action (keeps a Meta-side
audit trail); Rule name as in the table.

## Capacity guard (approved)

Meta rules cannot read bookings, so the guard is a read-only check in this session: the daily 09:22
Dubai check-in counts confirmed calendar bookings for yesterday and today; **at 11 or more on either
day it reports CAPACITY FULL and proposes holding the next increase** (owner then pauses rules 2/3/11/12
for that cycle, or approves a one-off hold write). Observed ceiling 12 jobs/day; weekend currently 8–9.

## Read-back after creation

1. Ads Manager → Automated rules → confirm 20 rules, each with the right "Applies to" list and schedule.
2. Session verification (read-only): the 09:22 daily check-in compares the five campaigns' daily budgets
   with the expected level for that day; an extra read on Thursday and Monday at 12:40 Dubai verifies
   the 12:00 steps. First live cycle: Thursday 16 Oct.
3. First-week scorecard: Fri–Sun conversations, cost per conversation, bookings created, booking rate
   (bookings ÷ conversations) vs the Tue–Wed baseline; if booking rate drops > 20 % on the peak days,
   cap at the Thursday level.

## What changes when T1/T2 finish their window

After the 16 Oct scorecard, T1/T2 join as group **W-T** (ABO, budgets on the ad sets): same 9 slots,
amounts = 60/30 × multiplier (or 80/40 × multiplier if the scorecard raised them). Until then they are
untouched. W1/W2 are never scheduled; they are paused after parity.
