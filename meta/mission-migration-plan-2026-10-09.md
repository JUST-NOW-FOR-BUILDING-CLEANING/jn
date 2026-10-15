# JUSTNOW — META MISSION MIGRATION & CLEANUP EXECUTION PLAN

Prepared 2026-10-09 (Asia/Dubai) from the audit in `ad-account-audit-2026-10-09.md`. Migration design
only — **no production write was made** (no campaign/ad set/ad created, nothing paused, no budget
edit, no rename).

```
WRITE APPROVAL ENFORCEMENT: NOT VERIFIED
PRODUCTION WRITES:          0
READY TO EXECUTE:           NO
PURCHASE GATE:              FAIL
```

Mission map used: jn 1037126214908677 → WHATSAPP SALES · JN 9147325105346647 → WEBSITE BOOKINGS +
RETARGETING (+ one future Purchase test) · justnow22 1897980308260660 → CREATIVE TESTING · JNN
1304802461392117 → HOLD / future PURCHASE-REVENUE · personal/legacy → HOLD · JustNow44 → deferred ·
1679026507158086 → NEVER TOUCH.

Learning rule acknowledged: a rebuilt ad set re-enters learning; the gain sought is a clean mission
per account, less internal auction competition, cleaner budgets/reporting/exclusions and the correct
optimisation event — not inherited "account learning".

---

## 0. Shared identities and the WhatsApp-number pre-flight

| Item | Value |
|---|---|
| Page used by every CTWA/website ad in jn and JN | **Just Now — 122098309970001876** (CO LLC Page 503162459555897 also appears on 2 JN website creatives) |
| Instagram identity | justnow.life.ae — 17841461253086330 (both accounts); JN also has justnow.cs 17841460086264801 |
| Click-to-WhatsApp destination | the WhatsApp number connected to Page 122098309970001876 (not readable through the API) |
| respond.io AI agent channel | one WhatsApp Business channel, id **541167** ("Whatsapp Business (01) - Migrated"); its number is not exposed by the API |
| Numbers quoted inside ad copy | jn Arabic ads: **wa.me/+971507677282** · JN winner + jn "sticky kitchen" ads: **+971585658859** · 2023 personal-account ads: …7949 |

**Pre-flight (owner, before Wave A1):** confirm that the Page-connected WhatsApp number equals the
respond.io channel-541167 number, and which of +971507677282 / +971585658859 that is. A twin built
from an existing post inherits the post's copy, so if the quoted number is not the agent's line the
twin must be built as a new creative with corrected copy (social proof not preserved — see scorecards).

---

## 1. Wave A0 — snapshot of winners and baselines (read-only, done)

| Account | Entity | ID | 30d | 7d |
|---|---|---|---|---|
| jn | A - Sharjah city families 25-60 [5158] | 120249855372950073 | AED 1,982 → 510 conv @3.89 | 667 → 177 @3.77 |
| jn | New Sales Ad Set - Copy A | 120249855745520073 | 1,080 → 309 @3.49 | 446 → 117 @3.81 |
| jn | New Sales Ad Set (20 Sep) | 120249855697040073 | 834 → 243 @3.43 | 193 → 67 @2.88 |
| jn | New Sales Ad Set - Copy 2 | 120249855757070073 | 1,258 → 294 @4.28 | 93 → 32 @2.91 |
| jn | New Sales Ad Set - Copy B | 120249855813520073 | 431 → 113 @3.81 | 222 → 64 @3.46 |
| jn | B - Arabic speakers Sharjah + Ajman | 120249855378300073 | 337 → 85 @3.96 | 91 → 26 @3.48 |
| jn | TEST 24 Sep - E - Dubai women | 120249947966990073 | 229 → 63 @3.63 | 111 → 25 @4.44 |
| JN | New Sales Ad Set - Copy (CTWA) | 120251948470210312 | 2,096 → 515 @4.07 | 617 → 162 @3.81 |
| JN | New Sales Ad Set (CTWA, motherhood) | 120251948470250312 | 300 → 75 @4.00 | 22 → 8 @2.78 |
| JN | C1-1 Broad 25+ (website Lead) | 120252107075750312 | 589 → 9 leads @65, 6 purchases AED 1,776 | 506 → 9 @56 |
| JN | C2-1 + C2-3 (retargeting) | 120252107098030312 / 120252107111220312 | 556 → 5 leads, 4 purchases AED 1,077 | 479 → 5 |

Account baselines (30d): jn CTWA AED 7,326 → 1,844 conv @3.97, CPM 13.6 · JN CTWA AED 2,410 → 590
@4.08, CPM 15.1 · JN website AED 1,233 → 14 leads @88, 10 purchases AED 2,853 (7d).

---

## 2. WhatsApp migration — jn

### 2.1 Current WhatsApp winners outside jn (all in JN, campaign "New Sales Campaign - Copy 2" 120251948470120312, CBO AED 80/day)

| | W1 | W2 |
|---|---|---|
| CURRENT ACCOUNT | JN 9147325105346647 | JN 9147325105346647 |
| CAMPAIGN | New Sales Campaign - Copy 2 — 120251948470120312 | same |
| AD SET | New Sales Ad Set - Copy — **120251948470210312** | New Sales Ad Set — **120251948470250312** |
| AD | "New Sales Ad and Message" 120251948470150312 (control) · "New Sales Ad and Message - Copy" 120251948470350312 (variant) · "Sep 23 - Look closer filter reel" 120252006507920312 (starved, AED 4) | "New Sales Ad and Message - Copy 2" 120251948470130312 |
| CREATIVE | 1388128153493483 → video 1116950464613349, post **122098309970001876_1116950464613349**, IG media 17896642608283094 · 1065906929646208 → video 957062783432763, post **122098309970001876_957062783432763** | 1100574565779685 → video 1559790696189996, post **122098309970001876_1559790696189996**, IG media 18040239875751399 |
| COPY / CTA | "Why does your kitchen feel sticky? 😬 … Try the service today 📲+971585658859" EN · CTA WHATSAPP_MESSAGE | "Steam. Precision. Results. 💨✨ That's real deep cleaning. 👉 Book now" EN · CTA WHATSAPP_MESSAGE |
| TARGETING | 18–65 · pin (25.257, 55.356) r10 mi (Sharjah) · interests Furniture, Home improvement, Modern furniture, Online shopping, Home, Luxury goods · behaviour Engaged Shoppers · life event Recently moved · Advantage audience ON · excl. region Abu Dhabi · **no audience exclusions** | 25–65 · pins (24.993, 55.147) r12 mi, (25.202, 55.364) r10 mi, (25.373, 55.483) r10 mi · interests Motherhood, Parenting, Online shopping, Fashion accessories · relationship status married · locales 6, 24, 28 · Advantage audience ON · excl. Fujairah + Abu Dhabi · excl. CA "lead" 120251575303130312 |
| 30D CPA | AED 4.07 (ad: 4.03 / 4.20) | AED 4.00 (ad: 3.78) |
| 7D CPA | AED 3.81 (ad: 3.85 / 3.79) | AED 2.78 |
| VOLUME | 515 conv / 30d, 162 / 7d (≈ AED 70–88/day) | 75 / 30d, 8 / 7d (≈ AED 10/day) |

Not migrated: JN's paused "Persona Launch" ad sets (best 229 @4.98) — not winners at jn's AED 4.5
ceiling; keep as paused references. justnow22's Feb-2026 ad sets (@1.67–3.09, AED 554) — test
scale only; their targeting is reused as a CT template.

### 2.2 Twins to build in jn (Wave A1)

New campaign in act_1037126214908677: **`WA | PROSPECTING | SHJ | HOME-MOVERS`** — objective
OUTCOME_SALES, buying AUCTION, ad-set budgets (no CBO), special ad categories none, created PAUSED.

**T1 `WA | HOME-MOVERS | SHJ | CONVERSATIONS`** (twin of W1)
* optimization_goal CONVERSATIONS · billing IMPRESSIONS · destination_type WHATSAPP ·
  promoted_object page_id 122098309970001876 · attribution 7d click / 1d view · bid Highest volume
* daily_budget **AED 60.00** (API: 6000)
* targeting = W1 verbatim (above) **plus** excluded_custom_audiences
  [120249973174230073 "jn - Customers Jan 2025-Sep 2026 (booking calendar, 889)"]; placements
  Advantage+ (as W1); no new audiences created
* ads: T1-a = existing post 122098309970001876_1116950464613349 (control) · T1-b = existing post
  122098309970001876_957062783432763 · both CTA WHATSAPP_MESSAGE, Instagram actor 17841461253086330,
  welcome message copied from the JN ad (read it in Ads Manager before build; not readable here)
* KEEP SOCIAL PROOF: **YES** — both accounts advertise from Page 122098309970001876, so the same post
  IDs (and their IG media) can be selected as "existing post". Becomes **NOT POSSIBLE** if the
  pre-flight shows +971585658859 is not the agent's line: then build from video_id
  1116950464613349 / 957062783432763 with corrected copy (new post, likes/comments not carried).

**T2 `WA | MOTHERHOOD | DXB+SHJ+AJM | CONVERSATIONS`** (twin of W2)
* same optimisation/destination as T1 · daily_budget **AED 30.00** (3000)
* targeting = W2 verbatim, replacing the JN-only exclusion "lead" with
  [120249973174230073 jn customers, 120250006502540073 "jn - Booking request sent (Lead event) 14d"]
* ad: T2-a = existing post 122098309970001876_1559790696189996 · CTA WHATSAPP_MESSAGE ·
  KEEP SOCIAL PROOF: **YES** (same condition as T1)

### 2.3 Migration scorecards

| | W1 → T1 | W2 → T2 |
|---|---|---|
| OLD ACCOUNT / CAMPAIGN / AD SET | JN / 120251948470120312 / 120251948470210312 | JN / 120251948470120312 / 120251948470250312 |
| CREATIVE | posts …_1116950464613349, …_957062783432763 | post …_1559790696189996 |
| CURRENT CPA / VOLUME | AED 4.07 (7d 3.81) / 515 conv per 30d | AED 4.00 (7d 2.78) / 75 per 30d |
| TARGET ACCOUNT / NEW CAMPAIGN / NEW AD SET | jn / `WA \| PROSPECTING \| SHJ \| HOME-MOVERS` / T1 | jn / same campaign / T2 |
| OPTIMIZATION | CONVERSATIONS → WhatsApp (Page 122098309970001876) | same |
| STARTING BUDGET | AED 60/day | AED 30/day |
| KEEP SOCIAL PROOF | YES (conditional on number pre-flight) | YES (same condition) |
| OBSERVATION WINDOW | 7 days, or earlier once ≥50 conversations | 7 days, or earlier once ≥25 conversations |
| SUCCESS THRESHOLD | 7-day CPA ≤ **AED 4.70** (= 4.07 × 1.15) with ≥50 conversations, frequency < 1.6 | 7-day CPA ≤ **AED 4.60** with ≥25 conversations |
| FAIL THRESHOLD | CPA > **AED 5.50** after ≥ AED 300 spent, or < 30 conversations after 7 days | CPA > **AED 5.50** after ≥ AED 150 spent, or < 12 conversations after 7 days |
| OLD VERSION ACTION AFTER TEST | success → PAUSE campaign 120251948470120312 (removes W1, W2 and the 0-result ad set 120251948470220312 together), raise T1 to AED 80/day · fail → KEEP W1, pause T1, investigate welcome message / number / placements before retry | success → PAUSE (covered by the campaign pause), raise T2 to AED 40/day · fail → KEEP W2, pause T2 |
| ROLLBACK | set T1/T2/ads to PAUSED (campaign 120251948470120312 untouched until success) | same |

Quality parity is judged on respond.io / calendar outcomes as well as CPA: the twin must produce
booking requests at ≥ the JN ad set's rate over the same 7 days (read from the Make calendar
pipeline), otherwise treat as fail even if CPA passes.

### 2.4 Reactivation (customers are NOT excluded here)

New campaign `WA | REACTIVATION | CUSTOMERS 12M | DEEP CLEANING` in jn · ad set
`WA | CUSTOMERS 12M | UAE | REACTIVATION`: CONVERSATIONS → WhatsApp, AED 20/day, custom audience
120249973174230073 only (add JN's "contacts (9).csv" 120251835232100312 once shared from BM-B), no
interest layer, UAE excl. Abu Dhabi, Advantage audience OFF; ads: "Customer voice AR/EN" post
122098309970001876_122278001594006883 and Arabic stove-grease post …_1622838339212041. Replaces
jn C3-1 (120250020902640073, which already targets this list at AED 5.15); pause C3-1 after 7 days of
the new ad set. KPI: bookings per AED, not conversations.

### 2.5 Customer-exclusion hygiene on the 9 jn winners (Wave A3, staggered)

Add excluded_custom_audiences [120249973174230073] to 120249855372950073, 120249855745520073,
120249855697040073, 120249855757070073, 120249855813520073, 120249855378300073, 120249947966990073,
120249855379550073, 120249855379980073 — **three ad sets every 3 days**, never all at once (a
targeting edit is a significant edit and restarts learning). Rollback = remove the exclusion
(targeting snapshots are in the audit's ad-set tables). The customer list is 889 people against
audiences of hundreds of thousands, so this is hygiene, not urgency — it waits until the twins
have stabilised.

---

## 3. Website migration — JN

### 3.1 Website/Lead activity outside JN

| Account | Item | Result | Decision |
|---|---|---|---|
| jn | "jn - Book Now page - Bookings - 25 Sep 2026" ad set 120249937413970073 (paused): ads 1448987757295289 "Sticky kitchen video EN" 182 → 3 leads @61 · 2116406612332211 "Top creator reel EN" 165 → 1 @165 (+1 purchase AED 279) · 1799183478088831 Arabic stove grease 80 → 1 @80 | 5 leads @85 total — weaker than JN C1-1 (9 @65, 6 purchases) | DO NOT REBUILD as a structure. Carry one creative concept into JN (§3.2 ad W-c). Keep paused. |
| jn | "jn - Booking Page Leads" 120249870686550073 and "- Copy" 120249942058580073 (paused) | 1 lead @154; 1 lead @24 (+1 purchase AED 379) | keep paused |
| jn | CONTENT_VIEW ad set 120249845713720073 | AED 27, nothing | keep paused |
| 658869122728885 | "[10/3/2026] Promoting justnow.life/book-now" campaign 120249701767850032 (LPV, no event) | 344 landing-page views, no leads | pause in A3 (nothing to migrate) |

### 3.2 Consolidation inside JN (Wave A2) — event: **LEAD on pixel 614743294720303** (438 events / 28d,
EMQ 7.8; the deepest reliable website event; Purchase stays off until §4 passes)

**WB | PROSPECTING | DXB+SHJ+AJM | BOOKING** — keep ad set **120252107075750312** (it holds the only
website learning: 9 leads, 6 purchases); rename only. Campaign 120252107068880312 renamed
`WB | PROSPECTING | UAE | DEEP CLEANING`, CBO raised from AED 84 to **AED 100/day** after the merge.
Ads inside it:
* keep C1-1-d 120252109342810312 (creative 1484505567067844, 6 leads @78, 5 purchases AED 1,497) — control
* keep C1-1-b 120252107434020312 (creative 2012729279425471, 3 leads @10 on AED 30 — the best lead
  rate in the account, under-delivered) — challenger
* move the Studio-feedback ad (creative 1094497890116067, from test ad set 120252195374160312) in as
  a third ad; then pause ad set 120252195374160312 (it only split budget away from the learner)
* W-c (new, from jn): "Sticky kitchen video EN" — build from video 2163113240903678 / post
  122098309970001876_2163113240903678 with CTA BOOK_NOW → justnow.life/book-now
* kill rule for C1-1-a 120252107427390312 (AED 64 → 0) and C1-1-e 120252109350130312 (AED 25 → 0):
  pause at AED 100 spent without a lead

**WB | RETARGETING | UNION 30D | BOOKING** — NEW ad set in campaign 120252107080200312 (renamed
`WB | RETARGETING | UAE | DEEP CLEANING`, CBO AED 70/day):
* optimisation OFFSITE_CONVERSIONS / LEAD / pixel 614743294720303 · attribution 7d click, 1d view
* custom_audiences = 120252107062990312 (Book Now 14d) ∪ 120252107065720312 (site visitors 30d) ∪
  120251888118190312 (IG engagers 365d) ∪ 120251888139630312 (FB Page engagers 365d)
* excluded_custom_audiences = 120251936408430312 (confirmed bookings 12mo) + 120252107064340312
  (Lead 14d)
* geo: pins (25.091, 55.266) r10 mi + (25.344, 55.422) r10 mi, excl. Abu Dhabi; age 20–65;
  Advantage audience OFF; placements Advantage+
* ads: C2-1-c creative 800898536451029 ("finish your booking", 2 leads, 3 purchases AED 578) ·
  C2-3-a 1765887427985234 ("Same kitchen", 3 leads, 1 purchase AED 499) · C2-2-d 1132547542778119
* no new audiences are created; the duplicate 09:59 audiences (120252106926760312,
  120252106929540312, 120252106931330312) and one duplicate LAL (120252110720830312) stay unused
  and can be deleted later — none of them is referenced by any ad set

| Scorecard | C2-1 + C2-2 + C2-3 → UNION |
|---|---|
| OLD | JN / 120252107080200312 / 120252107098030312 · 120252107107740312 · 120252107111220312 |
| CREATIVE | 800898536451029 · 1765887427985234 · 1132547542778119 (reused as-is) |
| CURRENT CPA / VOLUME | AED 114 per lead (5 leads, 4 purchases AED 1,077) / 10 days |
| TARGET | JN / `WB \| RETARGETING \| UAE \| DEEP CLEANING` / `WB \| RETARGETING \| UNION 30D \| BOOKING` |
| OPTIMIZATION | LEAD on 614743294720303 |
| STARTING BUDGET | the campaign's AED 70/day (the three old ad sets paused at launch, since they share the CBO) |
| KEEP SOCIAL PROOF | YES — same creatives, same account |
| OBSERVATION WINDOW | 10 days (small audiences) |
| SUCCESS | ≥5 leads at ≤ AED 100 per lead, or ≥3 attributed purchases |
| FAIL | < 3 leads after AED 500 |
| OLD VERSION ACTION | success → leave old three PAUSED · fail → unpause C2-1 and C2-3 (not C2-2), pause union |
| ROLLBACK | pause union ad set; set 120252107098030312 and 120252107111220312 ACTIVE |

---

## 4. Purchase gate — **FAIL** (re-check daily)

| Gate item | Status today |
|---|---|
| Completed-job Purchase flow sending correctly | configured correctly (Make 6529499: pixel 614743294720303, event_id = calendar id, value + AED, action_source chat, ph/fn/ln/ct/external_id), but **0 events sent**: 9 Oct run found 9 jobs, all already sent by the legacy flow; 37 pending a DONE line; 2 aged out |
| 7 consecutive days of real completed-service events | 0 / 7 — pixel shows **no Purchase since 6 Oct 22:00 Dubai** (checked 9 Oct 03:50 Dubai) |
| Correct value / currency | configured ✓ (job price, AED) — unverified in production |
| Stable dedup | event_id + Make ledger (SENT / LEGACY / UNCERTAIN) ✓ |
| EMQ visible | not reported for Purchase yet |
| Enough weekly volume | legacy flow ≈ 30/week; new flow 0 |

To pass: add `DONE YYYY-MM-DD HH:mm` to the 37 pending jobs, then 7 straight days with ≥3 real
Purchases/day and an EMQ row for Purchase. Only then Wave A5: **one** ad set in JN —
campaign `PUR | PROSPECTING | UAE | COMPLETED SERVICE` (OUTCOME_SALES), ad set
`PUR | BROAD | UAE | PURCHASE` (OFFSITE_CONVERSIONS / PURCHASE on 614743294720303, Advantage+
audience, UAE excl. Abu Dhabi, exclusions as WB prospecting, AED 150/day, 7d click / 1d view). No
second Purchase ad set anywhere; JNN stays reserved.

---

## 5. Creative testing — justnow22 (Wave A4)

Structure in act_1897980308260660 (same Page 122098309970001876 / IG 17841461253086330; share
audience 120249973174230073 from jn first, same BM-A):
* campaign `CT | 2026-10 | HOOK-TEST-01` — OUTCOME_SALES, ad-set budget
* ad set `CT | WOMEN 25-55 | DXB+SHJ | CONVERSATIONS` — CONVERSATIONS → WhatsApp, **AED 40/day**,
  women 25–55, pins (25.346, 55.421) r12 km + (25.202, 55.364) r10 mi, Advantage audience ON,
  exclude 120249973174230073, dynamic creative OFF, one control ad + 4 test ads so delivery splits
  by creative
* control ad in every CT ad set: the proven "sticky kitchen" family (post …_1116950464613349 or jn's
  …_2163113240903678)
* rules: pause a test ad at AED 60 with 0 conversations, or at AED 150 with CPA > AED 6; **graduate**
  at CPA ≤ AED 4.00 with ≥25 conversations → rebuild in jn (WhatsApp) or JN (website) as a new ad in
  the mission ad set; cap AED 300 per creative

CREATIVES TO TEST (evidence from the last 30 days):
1. "Same kitchen, different result" before-after EN+AR — creative 2012729279425471 / video
   28340961415525425 (Page 503162459555897 post): 3 website leads @ AED 10 on AED 30 — strongest
   lead rate, never funded; test as a WhatsApp hook.
2. "Look closer — extractor filter" reel — video 2380999242725474 (post …_2380999242725474): starved
   at AED 4 in JN; proof-style hook.
3. "3 years of grease buildup disappearing" EN status — post …_122374924118006883 (jn C3-1-a, 41 conv
   @5.12 on a customer audience): test on cold traffic.
4. Inside-the-cabinets AR video — 1834696980892667 / video 1400901805493555 (39 @4.62): test an EN
   cut vs AR.
5. "Customer voice AR/EN" testimonial — post …_122278001594006883 (11 conv @2.71 on AED 30): UGC
   angle, under-funded.
6. Studio-feedback testimonial video — video 4535244356773903 (0 leads on AED 72 as a website ad):
   retest as a WhatsApp hook.
7. "POV: our team just left your kitchen" — creative 1462260255814296 (jn C3-4-c, WITH_ISSUES):
   fix the issue first, then test.
8. Arabic vs English on one concept: Arabic stove-grease video 1622838339212041 (74 @4.15) vs EN
   sticky-kitchen video 1732956274575988 (135 @4.15) — equal so far; run both in the same ad set.

---

## 6. Cleanup (Wave A3, after replacements stabilise) — pause/archive, never delete history

| Item | ID | Action | Condition |
|---|---|---|---|
| JN CTWA campaign "New Sales Campaign - Copy 2" | 120251948470120312 | PAUSE | T1 + T2 pass |
| JN 0-result CTWA ad set | 120251948470220312 | PAUSE | with the campaign above (or immediately — AED 14/30d) |
| 658869122728885 LPV boost | campaign 120249701767850032 / ad set 120249701767810032 | PAUSE | first A3 batch |
| jn C3-4 Broad | 120250020898360073 | PAUSE | first A3 batch (CPA 6.1–6.5, CPM 30.6) |
| jn C3-1 Women (customer list) | 120250020902640073 | PAUSE | reactivation ad set live 7 days |
| JN C2-1 / C2-2 / C2-3 | 120252107098030312 / 120252107107740312 / 120252107111220312 | PAUSE | at union launch (shared CBO) |
| JN Website-video test ad set | 120252195374160312 | PAUSE | after its ad is moved into WB prospecting |
| jn Book Now Lead campaigns | 120249937413940073, 120249870686550073, 120249942058580073 | keep PAUSED | do not resume in jn |
| jn Reach / LPV boosts, JN IG boost | 120249856739720073, 120249858947210073, 120250027208020073, 120250080111120073, 120252051375920312 | keep PAUSED | no strategic role |
| 658869122728885 legacy …7949 WhatsApp ads (ended but status ACTIVE) | campaigns 120201463296540032, 120202633367610032, 23859136563650031, 23859135342840031 | set PAUSED | hygiene; wrong number |
| JN "[OLD - DELETE]" campaigns and zero-spend drafts | 120227646457240312, 120231157544050312, 120229999555140312, 120251632668990312 + drafts | ARCHIVE | any time |
| jn "365 - sep 2026" twins | 120249629710440073 / 120249629704230073 | RENAME (sizes differ: 9.5–11k vs 31–37k — not duplicates) | any time |

Not cleanup: budgets of the 9 jn winners and JN C1-1 stay untouched throughout.

---

## 7. Account names (Wave A6 — after write enforcement is verified)

```
POST /act_1037126214908677  name="JUSTNOW | WHATSAPP SALES | jn"
POST /act_9147325105346647  name="JUSTNOW | WEBSITE BOOKINGS | JN"
POST /act_1897980308260660  name="JUSTNOW | CREATIVE TESTING | justnow22"
POST /act_1304802461392117  name="JUSTNOW | HOLD / FUTURE REVENUE | JNN"
POST /act_658869122728885   name="JUSTNOW | HOLD / LEGACY | Personal"
POST /act_311791788087024   name="JUSTNOW | HOLD / LEGACY | Just Now"      # only once settled/writable
--  2820299204977421 JustNow44: unchanged until readable · 1679026507158086: NEVER
```

---

## 8. Execution order and budget flow

| Wave | Content | New daily spend | Removed daily spend |
|---|---|---|---|
| A0 | snapshot (done, §1) | — | — |
| A1 | T1 + T2 in jn (§2.2) | +AED 90 for ≤7 days | — |
| A2 | WB consolidation in JN (§3.2) | +AED 16 (CBO 84 → 100) | test ad set AED 60 |
| A3 | pauses of §6 after parity; exclusions §2.5 staggered; reactivation ad set | +AED 20 | JN CTWA AED 80; 658869122728885 AED 15; C3-4 share of CBO |
| A4 | CT structure in justnow22 (§5) | +AED 40 | — |
| A5 | one Purchase ad set in JN — **blocked by §4** | +AED 150 when gate passes | — |
| A6 | renames (§7) | — | — |
| A7 | reallocate: raise T1 to 80, T2 to 40, fund jn C and D ad sets (+AED 20 each), keep blended CTWA CPA ≤ AED 4.5; scale winners +20 %/week while CPA holds | | |

---

## 9. FIRST EXECUTION BATCH — Wave A1 (prepared, NOT executed; needs line-by-line approval)

Pre-flight P0: owner confirms the WhatsApp number (§0) and the welcome message text of JN ad
120251948470150312. Everything below is created PAUSED; step 9 is the only go-live write.

```
1. POST /act_1037126214908677/campaigns
   name="WA | PROSPECTING | SHJ | HOME-MOVERS"  objective=OUTCOME_SALES  buying_type=AUCTION
   special_ad_categories=[]  status=PAUSED                                   → CAMPAIGN_ID
2. POST /act_1037126214908677/adsets   (T1)
   name="WA | HOME-MOVERS | SHJ | CONVERSATIONS"  campaign_id=CAMPAIGN_ID  status=PAUSED
   optimization_goal=CONVERSATIONS  billing_event=IMPRESSIONS  bid_strategy=LOWEST_COST_WITHOUT_CAP
   destination_type=WHATSAPP  promoted_object={page_id:122098309970001876}
   daily_budget=6000  attribution_spec=[{event_type:CLICK_THROUGH,window_days:7},{event_type:VIEW_THROUGH,window_days:1}]
   targeting={age_min:18,age_max:65,
     geo_locations:{custom_locations:[{latitude:25.257,longitude:55.356,radius:10,distance_unit:mile}],location_types:[home,recent,frequently_in]},
     excluded_geo_locations:{regions:[{key:"8"}]},
     flexible_spec:[{interests:[Furniture,Home improvement,Modern furniture,Online shopping,Home,Luxury goods],
                     behaviors:[Engaged Shoppers],life_events:[Recently moved]}],   # copy the exact IDs from ad set 120251948470210312
     excluded_custom_audiences:[{id:120249973174230073}],
     targeting_automation:{advantage_audience:1}}                              → T1_ID
3. POST /act_1037126214908677/adsets   (T2)
   name="WA | MOTHERHOOD | DXB+SHJ+AJM | CONVERSATIONS"  campaign_id=CAMPAIGN_ID  status=PAUSED
   same optimisation block as T1  daily_budget=3000
   targeting={age_min:25,age_max:65,
     geo_locations:{custom_locations:[{24.993,55.147,r12mi},{25.202,55.364,r10mi},{25.373,55.483,r10mi}],location_types:[home,recent,frequently_in]},
     excluded_geo_locations:{regions:[{key:"11"},{key:"8"}]},
     flexible_spec:[{interests:[Motherhood,Parenting,Online shopping,Fashion accessories],relationship_statuses:[3]}],
     locales:[6,24,28],
     excluded_custom_audiences:[{id:120249973174230073},{id:120250006502540073}],
     targeting_automation:{advantage_audience:1}}                              → T2_ID
4. POST /act_1037126214908677/adcreatives  object_story_id=122098309970001876_1116950464613349
   instagram_user_id=17841461253086330  call_to_action={type:WHATSAPP_MESSAGE}            → CR_T1a
5. POST /act_1037126214908677/adcreatives  object_story_id=122098309970001876_957062783432763  (same)  → CR_T1b
6. POST /act_1037126214908677/adcreatives  object_story_id=122098309970001876_1559790696189996 (same)  → CR_T2a
7. POST /act_1037126214908677/ads  name="REEL | KITCHEN | STICKY-GREASE | V01"   adset_id=T1_ID creative={creative_id:CR_T1a} status=PAUSED
   POST /act_1037126214908677/ads  name="REEL | KITCHEN | STICKY-GREASE | V02"   adset_id=T1_ID creative={creative_id:CR_T1b} status=PAUSED
   POST /act_1037126214908677/ads  name="VIDEO | KITCHEN | STEAM-PRECISION | V01" adset_id=T2_ID creative={creative_id:CR_T2a} status=PAUSED
8. Read back: GET CAMPAIGN_ID, T1_ID, T2_ID, 3 ads — verify names, budgets, destination WHATSAPP,
   exclusions present, preview renders the original post with its likes/comments.
9. Go-live (separate approval): POST T1_ID status=ACTIVE · T2_ID status=ACTIVE · 3 ads status=ACTIVE
   · CAMPAIGN_ID status=ACTIVE. JN campaign 120251948470120312 is NOT touched in this batch.
```

Rollback for the whole batch: POST status=PAUSED on T1_ID, T2_ID and the three ads (or delete the
campaign while it is still PAUSED and has no delivery). Nothing in JN changes until the scorecard
in §2.3 passes.

Writes in this batch: 10 creates + 1 activation set = **0 executed**.

---

## 10. Return block

```
READY-TO-MIGRATE WHATSAPP WINNERS:
  W1  JN ad set 120251948470210312 (ads 120251948470150312, 120251948470350312; posts …_1116950464613349, …_957062783432763) — 515 conv/30d @4.07, 7d @3.81
  W2  JN ad set 120251948470250312 (ad 120251948470130312; post …_1559790696189996) — 75 conv/30d @4.00, 7d @2.78

READY-TO-MIGRATE WEBSITE WINNERS:
  none outside JN (jn Book Now 5 leads @85 < JN C1-1 9 @65 + 6 purchases) — only creative W-c (sticky-kitchen video EN) carried into JN
  inside JN: keep 120252107075750312 as WB prospecting; build WB | RETARGETING | UNION 30D replacing C2-1/C2-2/C2-3; merge video test ad set 120252195374160312

CREATIVES TO TEST (justnow22):
  2012729279425471 same-kitchen before/after · video 2380999242725474 extractor-filter · post …_122374924118006883 "3 years of grease" ·
  1834696980892667 inside-cabinets AR (+EN cut) · post …_122278001594006883 customer voice · video 4535244356773903 studio feedback ·
  1462260255814296 POV (fix issue first) · AR vs EN stove-grease pair 1622838339212041 vs 1732956274575988

PAUSE AFTER MIGRATION:
  JN campaign 120251948470120312 (incl. ad sets 120251948470210312, 120251948470250312, 120251948470220312) · jn C3-4 120250020898360073 ·
  jn C3-1 120250020902640073 · JN C2-1 120252107098030312, C2-2 120252107107740312, C2-3 120252107111220312 · JN 120252195374160312 ·
  658869122728885 campaign 120249701767850032 · legacy …7949 campaigns 120201463296540032, 120202633367610032, 23859136563650031, 23859135342840031

DO NOT TOUCH:
  1679026507158086 (protected) · JustNow44 2820299204977421 · 311791788087024 · the 9 jn winners (120249855372950073, 120249855745520073,
  120249855697040073, 120249855757070073, 120249855813520073, 120249855378300073, 120249947966990073, 120249855379550073, 120249855379980073) ·
  JN C1-1 120252107075750312 · pixel 614743294720303 configuration · Make scenario 6529499 · Page 122098309970001876 / IG 17841461253086330

PURCHASE GATE: FAIL  (0 completed-job Purchases sent; 0/7 days; EMQ not visible; 37 jobs pending DONE)

FIRST EXECUTION BATCH: §9 — 1 campaign + 2 ad sets + 3 creatives + 3 ads created PAUSED in act_1037126214908677, read-back, then a separate go-live approval

PRODUCTION WRITES: 0
READY TO EXECUTE: NO
```
