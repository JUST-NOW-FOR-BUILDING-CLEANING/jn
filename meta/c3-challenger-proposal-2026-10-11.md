# C3 — one controlled challenger (creative + targeting), proposal only — nothing executed

Owner, 11 Oct: "APPROVE CREATIVE + TARGETING TEST, but DO NOT rewrite all existing C3 ad sets. Create ONE controlled
challenger proposal … Keep current C3 structure as the control. Do not execute yet." Account jn 1037126214908677.

## 1. The challenger

**Campaign (new, so the control keeps its own budget):** `jn | C3-X Challenger | WhatsApp conversations | DXB+SHJ+AJM
emirate-level | Oct 2026` — same objective and optimisation as C3 (messaging conversations, destination WhatsApp,
same Page 122098309970001876 and WhatsApp number as C3-2), CBO **AED 45/day**, lowest cost, no bid cap, created PAUSED.

**Budget:** C3 campaign 120250020646250073 goes **90 → 45** at the moment the challenger is activated, so the C3 mission
stays at AED 90/day in total ("hold at 90, do not scale"). Alternative if you prefer not to touch the control at all:
challenger at 45 on top (total 135) — this is a scale, so it needs your explicit yes.

**Ad set:** `C3-X-1 | Dubai + Sharjah + Ajman 25–65 | emirate regions | no interests`

```json
{"geo_locations":{"regions":[{"key":"10","name":"Dubai"},{"key":"9","name":"Sharjah"},{"key":"13","name":"Ajman"}],
                  "location_types":["home","recent"]},
 "age_min":25,"age_max":65,
 "excluded_custom_audiences":[{"id":"120249973174230073","name":"jn - Customers Jan 2025-Sep 2026 (booking calendar, 889)"}],
 "targeting_automation":{"advantage_audience":0}}
```

(Region keys 10 / 9 / 13 are the ones Meta returns inside C1's and C3's own custom-location pins for Dubai, Sharjah and
Ajman; Abu Dhabi is simply not included. No genders, no locales, no interests, no behaviours, no work positions, no age cap
at 46; Advantage+ placements as in the control; Advantage audience off so the test measures the targeting as written.)

**Ads (existing creatives of the jn account, both already click-to-WhatsApp):**

| Ad | Creative ID | Video | Evidence (last 7 days in 5158) |
|---|---|---|---|
| `C3-X-a \| Creator Reel 2 \| EN` | **3592620130898135** | 4303960699820816 | AED 203.38 → 63 conversations @ **3.23**, CPM 25.4, CTR 2.88 % |
| `C3-X-b \| Arabic stove-grease video \| AR` | **1870108203957859** | 1622838339212041 | AED 67.82 → 22 @ **3.08**, CPM 16.1, CTR 2.61 % |

## 2. Control

C3's three live ad sets as they are (C3-1 Women 25+ Sharjah pin, C3-2 Arabic speakers Dubai pin, C3-3 LAL 1 %), CBO at
45 after the split. Last 7 days (5–11 Oct) blended: **AED 383.90 → 55 conversations @ 6.98**, CPM 27–35, CTR 1.8–2.7 %,
frequency 1.13–1.33. Reference for "what the same creatives do in a healthy audience": 5158 at CPA 3.1–4.0 and CPM 15–25.

## 3. Pass / fail thresholds

| Checkpoint | Minimum delivery | PASS-TRACK | FAIL |
|---|---|---|---|
| **3 days** (first read Thu 15 Oct 09:22 if activated Mon 12 Oct) | ≥ AED 100 spent and ≥ 15 conversations | CPA ≤ AED 5.00 **and** CPM ≤ 22 | CPA > 7.00, or CPM ≥ 30 with CTR < 1.5 % (then targeting is not the lever either) |
| **7 days** (Sun 19 Oct) | ≥ AED 250 and ≥ 50 conversations | CPA ≤ AED 4.50 → fold the control's 45 into the challenger (or into 5158) | **CPA > 5.50 → fold C3's whole budget into 5158 and pause C3 + challenger** (the mission is already served there) |

Guards during the test: frequency < 1.6; no scaling of either side; capacity guard 11 bookings applies; bookings are
handled by the WhatsApp agent as for every WhatsApp campaign (no separate attribution is possible, so the comparison is on
cost per conversation and conversation quality as reported by the agent tags).

## 4. Execution steps when approved (each write prompts you; owner-present)

1. Create the campaign PAUSED → read back. 2. Create the ad set PAUSED with the targeting above → read back. 3. Create the
two ads PAUSED from the creative IDs → read back (review status). 4. Activate ad → ad set → campaign. 5. C3 90 → 45
(force-paused → re-activated) → read back. 6. Log the before/after in `meta/execution-log-2026-10-09.md`, commit, push.
Rollback = pause the challenger campaign and set C3 back to 90.
