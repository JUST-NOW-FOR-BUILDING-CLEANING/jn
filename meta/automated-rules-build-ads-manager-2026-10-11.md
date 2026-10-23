# META-NATIVE AUTOMATED RULES — Ads Manager build instructions (exact target budgets, no chained deltas)

Prepared 2026-10-11 ≈ 14:00 Dubai from `meta/automated-rules-spec-2026-10-09.md` after the owner's corrections of 11 Oct:
no third-party connector, native Ads Manager rules only; **exact target budgets** so that a missed rule or a manual edit
never propagates; C1 and C3 stay out of the weekly cycle; Monday budget changes never go through a session.
Calendar: Sun 11 Oct → Mon 12 → Tue 13 → Wed 14 → **Thu 15** → Fri 16 → Sat 17 → Sun 18 Oct 2026.

## 1. How every rule lands on an exact target (and why it cannot drift)

Ads Manager budget actions are "Increase daily budget by …" / "Decrease daily budget by …" with a **cap**. Used with a cap
equal to the target, the action becomes "set the budget to exactly the target", in both directions, idempotently:

| Direction | Action | Cap | Result |
|---|---|---|---|
| UP to target T | Increase daily budget by **100 %** (percentage) | **Maximum daily budget cap = T** | any budget between T/2 and T lands exactly on T; a budget already ≥ T is left untouched (the rule cannot go above the cap) |
| DOWN to target T | Decrease daily budget by **50 %** (percentage) | **Minimum daily budget cap = T** | any budget between T and 2T lands exactly on T; a budget already ≤ T is left untouched (the rule cannot go below the floor) |

So a skipped execution or a manual edit is corrected by the next slot instead of being carried forward, which is the
drift-proofing the owner asked for. If your Ads Manager offers **"Set daily budget to"** as an action, use it with the
same target and skip the percentage/cap mechanics — the rest of this document is unchanged.

Common settings for every rule: *Apply rule to* → the campaigns listed for the group (search by name or ID); *Conditions*
→ **Amount spent (Lifetime) > AED 0** (always true for these live campaigns; it only satisfies the "one condition"
requirement) — add **Daily budget < T** for UP rules / **Daily budget > T** for DOWN rules if the condition is offered;
*Time range* → Lifetime; *Schedule* → **Custom**, one day, the 30-minute window starting at the stated time (ad account
time zone = Asia/Dubai); *Notification* → email on action; *Rule name* exactly as in the table.

## 2. Rule table

Groups: **W-jn** = "New Sales Campaign" 120249855697050073 + "jn - WhatsApp Sales 5158 - New Audiences Sep 2026"
120249855229580073 (jn account 1037126214908677). **R-C2** = "JN | C2 Retargeting High-intent | Oct 2026"
120252107080200312 (JN account 9147325105346647). **BR** = "BR | Video Views ThruPlay | UAE excl. Abu Dhabi | Deep
Cleaning | Oct 2026" 23860638577100791 (justnow22 account 1897980308260660). Never in any rule: T1/T2 campaign
120250144447740073, W1/W2 120251948470120312, C1 120252107068880312 (flat 84), C3 120250020646250073 (flat 90),
reactivation 120250144448010073, anything with Purchase optimisation.

| # | Rule name | Group | Execution time (Dubai) | Current expected budget (before) | Target | Action | Failsafe | Read-back check |
|---|---|---|---|---|---|---|---|---|
| 6 | `WW \| W-jn \| MON 00:00 \| →86` | W-jn | Monday 00:00 | 99 (Sun level); **Mon 12 Oct: 150** | **86** | Decrease 50 %, min cap 86 | floor = target; no-op if already ≤ 86 | Mon 00:40 verification: both campaigns read 86 |
| 7 | `WW \| W-jn \| MON 12:00 \| →72` | W-jn | Monday 12:00 | 86 | **72** | Decrease 50 %, min cap 72 | floor = target | Mon 12:40 verification: 72 |
| 8 | `WW \| W-jn \| TUE 00:00 \| →81` | W-jn | Tuesday 00:00 | 72 | **81** | Increase 100 %, max cap 81 | cap = target; no-op if already ≥ 81 | Tue 00:40: 81 |
| 9 | `WW \| W-jn \| WED 00:00 \| →72` | W-jn | Wednesday 00:00 | 81 | **72** | Decrease 50 %, min cap 72 | floor = target | Wed 00:40: 72 |
| 1 | `WW \| W-jn \| THU 00:00 \| →90` | W-jn | Thursday 00:00 | 72 | **90** | Increase 100 %, max cap 90 | cap = target | Thu 15 Oct 00:40: 90 |
| 2 | `WW \| W-jn \| THU 12:00 \| →108` | W-jn | Thursday 12:00 | 90 | **108** | Increase 100 %, max cap 108 | cap = target | Thu 12:40: 108 |
| 3 | `WW \| W-jn \| FRI 00:00 \| →126` | W-jn | Friday 00:00 | 108 | **126** | Increase 100 %, max cap 126 | cap = target | Fri 16 Oct 00:40: 126 |
| 4 | `WW \| W-jn \| SAT 00:00 \| →117` | W-jn | Saturday 00:00 | 126 | **117** | Decrease 50 %, min cap 117 | floor = target | Sat 00:40: 117 |
| 5 | `WW \| W-jn \| SUN 00:00 \| →99` | W-jn | Sunday 00:00 | 117 | **99** | Decrease 50 %, min cap 99 | floor = target | Sun 00:40: 99 |
| 20b | `WW \| R-C2 \| MON 00:00 \| →70` | R-C2 | Monday 00:00 | 70 (Sun level); **Mon 12 Oct: 80** | **70** | Decrease 50 %, min cap 70 | floor = target; weekly re-anchor | Mon 00:40: 70 |
| 19 | `WW \| R-C2 \| FRI 00:00 \| →81` | R-C2 | Friday 00:00 | 70 | **81** | Increase 100 %, max cap 81 | cap = target | Fri 00:40: 81 |
| 20 | `WW \| R-C2 \| SUN 00:00 \| →70` | R-C2 | Sunday 00:00 | 81 | **70** | Decrease 50 %, min cap 70 | floor = target | Sun 00:40: 70 |
| 21 | `BR \| THU 00:00 \| →60` | BR | Thursday 00:00 | 50 (Wed level); **Thu 15 Oct: 60, no-op** | **60** | Increase 100 %, max cap 60 | cap = target | Thu 00:40: 60 |
| 22 | `BR \| THU 12:00 \| →70` | BR | Thursday 12:00 | 60 | **70** | Increase 100 %, max cap 70 | cap = target | Thu 12:40: 70 |
| 23 | `BR \| FRI 00:00 \| →85` | BR | Friday 00:00 | 70 | **85** | Increase 100 %, max cap 85 | cap = target | Fri 00:40: 85 |
| 24 | `BR \| SAT 00:00 \| →90` | BR | Saturday 00:00 | 85 | **90** | Increase 100 %, max cap 90 | cap = target | Sat 00:40: 90 |
| 25 | `BR \| SUN 00:00 \| →72` | BR | Sunday 00:00 | 90 | **72** | Decrease 50 %, min cap 72 | floor = target | Sun 00:40: 72 |
| 26 | `BR \| MON 00:00 \| →58` | BR | Monday 00:00 | 72 | **58** | Decrease 50 %, min cap 58 | floor = target | Mon 00:40: 58 |
| 27 | `BR \| TUE 00:00 \| →50` | BR | Tuesday 00:00 | 58 | **50** (holds Wednesday) | Decrease 50 %, min cap 50 | floor = target | Tue 00:40: 50 |

19 rules. Every step is within the 50 %–100 % band the actions need (largest move: 150 → 86 on Mon 12 Oct = ×0.57).
Rows 10–18 (C1) are parked; C3 is no longer in W-jn.

**Failsafes that apply to all rows:** (a) cap/floor equals the target, so a rule can never overshoot and is a no-op when
the budget is already past the target in its own direction; (b) the "Amount spent (Lifetime) > 0" condition keeps the rule
valid without ever blocking it; (c) email on every execution gives a Meta-side audit trail; (d) the session's read-only
00:40 / 12:40 verification compares every campaign with the target of the current slot and reports any gap with the
likely cause (rule not created / not fired / manual edit); (e) no rule can touch an entity outside its "Apply to" list.

**Read-back after each first firing:** Ads Manager → Automated rules → the rule → *Activity* shows the execution and the
old → new budget; the campaign row shows the target; the verification line of the same slot confirms it. First firings:
Mon 12 Oct 00:00 (6, 20b) and 12:00 (7); Tue 13 Oct (8); Wed 14 Oct (9); Thu 15 Oct (1, 21, 2, 22); Fri 16 Oct (3, 19,
23); Sat 17 Oct (4, 24); Sun 18 Oct (5, 20, 25); Mon 19 Oct (26); Tue 20 Oct (27).

## 3. Build order (≈ 30 minutes)

1. Ads Manager → *All tools* → *Automated rules* → *Create rule* → *Custom rule*.
2. **Tonight first (they fire within hours): rules 6, 7, 20b.** They move New Sales and 5158 from 150 to 86 at 00:00 and to
   72 at 12:00 Monday, and C2 from 80 to 70 — i.e. Monday 12 Oct = 86 + 86 + 90 (C3) + 84 (C1) + 70 + T1/T2 90 + W1/W2 80
   = **AED 586** at 00:00 and **558** after 12:00, plus brand 60. If you prefer the original "return to 90" for this one
   Monday, set 90/90/70 by hand instead and let rule 7 (→72) run at 12:00, or create rules 6/7 on Monday evening.
3. Then rules 8, 9, 1–5 (W-jn), 19, 20 (C2), 21–27 (BR), in any order; all can be ENABLED on creation because each one is
   a no-op until its own slot and lands on its target from any starting value in the band.
4. Manual fallback if the rules are not built tonight: budgets stay at the Sunday levels (724 + 60) until you edit them in
   Ads Manager; the Monday 00:30 read-only routine will remind you with the prepared batch, and the 09:22 scorecard repeats
   it. The session will not write them.

## 4. What the session does from here (read-only)

00:40 / 12:40 budget verification against the slot target; 09:22 daily scorecard; Mon 12 Oct 09:30 exclusion-batch
readiness check. Writes only when the owner approves them in a fresh message while present.
