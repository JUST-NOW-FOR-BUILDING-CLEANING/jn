# JUSTNOW META — OVERNIGHT CLEANUP, JUSTNOW44 REPAIR & MISSION MIGRATION

Night of 2026-10-08 → 09 (Asia/Dubai). Baseline: `ad-account-audit-2026-10-09.md` and
`mission-migration-plan-2026-10-09.md`. No broad re-audit was run; only the reads needed for the
phases below (JustNow44 attempts, dataset freshness, Make connections).

```
WRITE APPROVAL ENFORCEMENT: NOT VERIFIED   → stopped before the first production write
PRODUCTION WRITES:          0
ROLLBACKS:                  0
```

Owner clarification applied: the several JustNow numbers in creatives are all operational; number
variation is **not** a blocker and no winner is paused for it. Only broken/unreachable destinations
would be flagged — none was found (every CTWA ad set routes through Page 122098309970001876, every
website ad to justnow.life/book-now).

---

## M0 — snapshot (done, read-only)

Winner baselines are frozen in `mission-migration-plan-2026-10-09.md` §1 (9 jn/JN WhatsApp winners,
JN C1-1, JN C2-1/C2-3). Account state at snapshot: jn 13 active CTWA ad sets ≈ AED 270/day · JN 3
CTWA ad sets ≈ AED 80/day + 5 Lead ad sets ≈ AED 214/day · 658869122728885 one LPV boost AED 15/day ·
justnow22 nothing delivering · JNN empty.

---

## M1 — JN vs jn internal competition

Both accounts advertise from Page **Just Now 122098309970001876** and IG **justnow.life.ae
17841461253086330**, into the same WhatsApp line, on pixel 614743294720303, with the same Sep-30
creative upload, in Sharjah/Dubai/Ajman pins that sit within ~8 km of each other, all with Advantage
audience ON (so interest layers are suggestions, not fences). Booking quality is not traceable per ad
set from Meta; attributed purchases are used as the proxy where present.

### Currently spending CTWA assets, mapped

| Account / ad set (id) | 7d spend → conv (CPA) | CPM 7d | Geo | Audience layer | Exclusions | Creative (post) |
|---|---|---|---|---|---|---|
| JN · New Sales Ad Set - Copy (120251948470210312) | 617 → 162 (3.81) | 15.1 | Sharjah pin 25.257,55.356 r10mi | 18–65, furniture / home improvement / recently moved, Engaged Shoppers | none | "sticky kitchen" EN — posts _1116950464613349, _957062783432763 |
| JN · New Sales Ad Set (120251948470250312) | 22 → 8 (2.78) | 10.4 | 3 pins Dubai S / Dubai-Shj / Shj-Ajman | 25–65 motherhood / parenting, married | CA "lead" | "Steam. Precision. Results." — post _1559790696189996 |
| JN · New Sales Ad Set - Copy (120251948470220312) | 0 (AED 14 / 30d) | 36.9 | same 3 pins | women 25–65 jewelry / luxury | none | — |
| jn · A - Sharjah city families (120249855372950073) | 667 → 177 (3.77) | 17.8 | Sharjah pin 25.346,55.421 r12km | broad | none | Creator reel 2, Top creator reel (sticky kitchen EN), Sticky kitchen video |
| jn · Copy A (120249855745520073) | 446 → 117 (3.81) | 21.6 | Sharjah pin 25.325,55.425 r10mi | parents | none | "We pride ourselves" video |
| jn · New Sales Ad Set (120249855697040073) | 193 → 67 (2.88) | 19.4 | Ajman/Shj pin 25.227,55.444 r10mi | luxury / landlord | none | "أقسم بالله الفرق" video |
| jn · Copy 2 (120249855757070073) | 93 → 32 (2.91) | 26.7 | pins 25.105,55.285 + 25.316,55.396 r10mi | teachers / jewelry | none | Arabic status "ما بنرضى بالحل السهل" |
| jn · Copy B (120249855813520073) | 222 → 64 (3.46) | 17.2 | Sharjah pin 25.318,55.378 r10mi | interior design / recently moved | none | "You live premium" status |
| jn · B Arabic (120249855378300073) | 91 → 26 (3.48) | 16.2 | Sharjah + Ajman pins | Arabic locale | none | Arabic stove-grease video, customer voice |
| jn · TEST E Dubai women (120249947966990073) | 111 → 25 (4.44) | 23.2 | 6 small Dubai pins | women 25–55 | none | Top creator reel, sticky kitchen |
| jn · C / D Dubai (…379550073 / …379980073) | 32 → 10 (3.21) / 10 → 5 (1.99) | 24.6 / 23.4 | Dubai pins | broad | none | sticky kitchen family |
| jn · C3-4 Broad (120250020898360073) | 329 → 51 (6.45) | 32.1 | Dubai pin 25.153,55.321 r10mi | jewelry / luxury | customers 889 | POV / stove-grease |
| jn · C3-1 Women (120250020902640073) | 201 → 40 (5.01) | 25.7 | Ajman pin 25.397,55.494 | **targets** customers 889 | — | "3 years of grease" status |
| jn · C3-2 Arabic (120250020907890073) | 143 → 31 (4.61) | 27.9 | Dubai/Shj pin 25.241,55.39 | Arabic, teachers | customers 889 | inside-cabinets AR |
| jn · C3-3 LAL (120250020914410073) | 48 → 9 (5.30) | 21.8 | 2 pins | LAL customers | customers 889 | stove-grease |

### Overlap pairs

```
OVERLAP PAIR: P1 — JN home-movers CTWA vs jn Sharjah cluster
JN ASSET:      ad set 120251948470210312 (campaign 120251948470120312), ads 120251948470150312 / 120251948470350312
jn ASSET:      120249855372950073 (A Sharjah), 120249855813520073 (Copy B, recently-moved), 120249855745520073 (Copy A), 120249855757070073 (Copy 2)
SPEND:         JN ≈ AED 70–88/day · jn cluster ≈ AED 200/day (7d)
OBJECTIVE:     both OUTCOME_SALES → CONVERSATIONS → WhatsApp (same Page, same line)
AUDIENCE OVERLAP: HIGH — JN pin 25.257,55.356 r10mi sits 6–8 km from the four jn pins (r10–12); 18–65 vs 25–65; Advantage audience ON on all five; Copy B uses the same "recently moved / home improvement" layer
CREATIVE OVERLAP: HIGH — same "Why does your kitchen feel sticky?" concept and copy; JN posts _1116950464613349/_957062783432763, jn runs video 1732956274575988 / 2163113240903678 of the same family
AUCTION COMPETITION: direct — same people, same result, same hour; CTWA CPM 15–27 now vs 13–15 in August when one account carried the volume
BUSINESS VALUE: JN 515 conv/30d @4.07 (7 leads); jn cluster 1,226 conv/30d @3.4–4.3
KEEP WHICH:    jn cluster (3× the volume at equal CPA, the mission home)
MIGRATE WHICH: JN ad set → twin T1 "WA | HOME-MOVERS | SHJ | CONVERSATIONS" in jn (plan §2.2), same posts, AED 60/day
PAUSE WHICH:   JN campaign 120251948470120312 after T1 parity (≤ AED 4.70, ≥50 conv, booking rate ≥ JN's)
WHY:           one WhatsApp home; the JN winner's knowledge (home-mover layer + sticky-kitchen posts) survives in jn

OVERLAP PAIR: P2 — JN motherhood CTWA vs jn Copy A (parents)
JN ASSET:      ad set 120251948470250312, ad 120251948470130312 (post _1559790696189996)
jn ASSET:      120249855745520073 (Copy A: parenting / Parents (All), Sharjah r10mi)
SPEND:         JN ≈ AED 10/day · jn Copy A ≈ AED 64/day
OBJECTIVE:     both CONVERSATIONS → WhatsApp
AUDIENCE OVERLAP: HIGH — JN pin 25.202,55.364 r10mi vs jn 25.325,55.425 r10mi; both parent layers; married filter on JN only
CREATIVE OVERLAP: LOW — different creative ("Steam. Precision. Results." vs "We pride ourselves")
AUCTION COMPETITION: present but small (JN spends AED 10/day)
BUSINESS VALUE: JN 75 @4.00 / 30d; jn Copy A 309 @3.49
KEEP WHICH:    jn Copy A
MIGRATE WHICH: JN ad set → twin T2 "WA | MOTHERHOOD | DXB+SHJ+AJM | CONVERSATIONS" (plan §2.2), AED 30/day — or, if T1 passes and T2 is judged redundant, its post is added as a challenger ad inside Copy A
PAUSE WHICH:   covered by the campaign pause in P1
WHY:           same mission, same Page, 8 conv/week — not worth a separate JN structure

OVERLAP PAIR: P3 — JN women/jewelry ad set vs jn TEST E + C3-1
JN ASSET:      ad set 120251948470220312 (AED 14 / 30d, 0 results, CPM 36.9)
jn ASSET:      120249947966990073 (TEST E, 63 @3.63), 120250020902640073 (C3-1)
AUDIENCE OVERLAP: HIGH (women, Dubai/Sharjah) · CREATIVE OVERLAP: n/a · AUCTION COMPETITION: negligible
BUSINESS VALUE: none on the JN side
KEEP WHICH:    jn TEST E · MIGRATE WHICH: nothing · PAUSE WHICH: JN 120251948470220312 — PAUSE NOW (clear waste)
WHY:           zero results, no learning worth preserving

OVERLAP PAIR: P4 — personal-account LPV boost vs JN C1-1 website prospecting
JN ASSET:      ad set 120252107075750312 (LEAD on 614743294720303, excludes bookings / Book Now 14d / Lead 14d)
jn ASSET:      — (the competitor is 658869122728885 campaign 120249701767850032, LPV to justnow.life/book-now, AED 15/day, no event, no exclusions)
SPEND:         AED 15/day vs AED 84/day
OBJECTIVE:     LPV vs LEAD on the same landing page
AUDIENCE OVERLAP: HIGH (Sharjah r10mi, 25–65, luxury/parents) · CREATIVE OVERLAP: LOW · AUCTION COMPETITION: direct, for the same visitors
BUSINESS VALUE: boost = 344 landing-page views, 0 leads attributable
KEEP WHICH:    JN C1-1 · MIGRATE WHICH: nothing · PAUSE WHICH: 658869122728885 campaign 120249701767850032 — PAUSE NOW (clear waste)
WHY:           pays for traffic the Lead ad set is optimising for, and leaves no business signal

OVERLAP PAIR: P5 — inside jn: C3-4 Broad vs the five Sharjah/Dubai winners
JN ASSET:      —
jn ASSET:      120250020898360073 (C3-4, 51 @6.45, CPM 32.1) vs 120249855372950073 / …757070073 / …379550073 / …379980073
AUDIENCE OVERLAP: HIGH (Dubai pin 25.153,55.321 r10mi overlaps Copy 2's 25.105,55.285 and C/D) · CREATIVE OVERLAP: HIGH (same POV / stove-grease ads)
AUCTION COMPETITION: internal; CPM 2× its siblings
BUSINESS VALUE: 61 conv/30d at 6.11 — above the AED 4.5 ceiling
KEEP WHICH:    the siblings · PAUSE WHICH: C3-4 — PAUSE NOW (reallocates its CBO share to C and D, which run at AED 2–3)
WHY:           most expensive active ad set in the account, duplicating cheaper neighbours

OVERLAP PAIR: P6 — wrong-purpose website campaigns inside jn vs JN website structure
JN ASSET:      C1/C2 (website Lead, 14 leads, 10 purchases AED 2,853 in 7d)
jn ASSET:      Book Now Lead ad sets 120249937413970073, 120249870700990073, 120249942058590073 (paused; 7 leads @24–154)
STATE:         already paused — classify ARCHIVE / do not resume in jn; their one usable creative concept ("sticky kitchen EN", 3 leads @61) goes into JN as ad W-c
```

```
JN / jn OVERLAP
BEFORE: CTWA prospecting in both accounts (JN 3 ad sets ≈ AED 80/day; jn 13 ad sets ≈ AED 270/day) on one Page, one line,
        overlapping Sharjah/Dubai pins, same creative family; plus a third account (658869122728885) buying the same
        Sharjah traffic for the website page; plus website Lead attempts inside the WhatsApp account.
AFTER (target state once the batch is approved and T1/T2 pass): CTWA prospecting only in jn (13 + 2 twins);
        JN = website Lead + retargeting only; 658869122728885 silent; jn website attempts archived;
        the sticky-kitchen home-mover knowledge preserved as T1; estimated AED 60–75/day of overlap premium and
        no-outcome spend removed (CTWA CPM expected to fall back toward AED 13–15; AED 15/day boost; C3-4 share).
```

---

## M2 — JustNow44 (2820299204977421) diagnosis

### Every read path tried tonight

| Path | Result |
|---|---|
| Meta Ads connector — account-level insights | refused: "This ad account is not enabled for the Ads MCP. Ads MCP is being gradually rolled out across ad accounts. Please check back at a later date. Ad account ID: 2820299204977421" |
| Meta Ads connector — Pages endpoint | same refusal |
| Meta Ads connector — accounts list (business-level) | **readable**: name JustNow44, business **JustNow 579302160985190**, currency **AED**, account_status **ACTIVE**, has_payment_method **true**, is_queryable true, disable reason null, no "unusual activity" flag (unlike 825353993434985 / 2053880215357344 / 844053351344804) |
| Markifact Meta Ads operations | "No meta_ads connection found" |
| Windsor.ai | only GA4 + Instagram-public connectors |
| Madgicx | "You need an active or trial Madgicx subscription" |
| Make RPC via the owner's Facebook login | only a Conversions-API system-user connection exists (`facebook-business-extension`, used by the Purchase scenarios); no Facebook Ads/Insights connection → no ads-read RPC available |
| Logged-in Ads Manager / Business Manager (browser) | no browser tools exist in this cloud session |

### Connector problem vs account problem — separated

* **CONNECTOR PROBLEM (confirmed):** Meta gates its Ads MCP per ad account during a staged rollout.
  The refusal is the connector's own message; it is not an account health signal. Twenty other
  accounts in the same businesses are enabled; three "(Read-Only)" shells and JustNow44 are not.
  Nothing the owner configured causes it, and nothing in Ads Manager fixes it.
* **ACTUAL META ACCOUNT PROBLEM: none found at the business level.** The account is ACTIVE with a
  payment method and no disable reason — the only facts visible from here. Whether there is an
  Account Quality restriction, a spend limit or billing issue cannot be seen through any connected
  tool. The only hint of past trouble is the jn campaign named "jn - Reel tests (rebuilt from
  JustNow44, no WhatsApp marketing msgs)" (29 Sep 2026): Reel tests were moved out of JustNow44 and
  rebuilt without WhatsApp marketing messages — consistent with an ad-level rejection of the
  WhatsApp "marketing messages" feature, not with an account restriction. Unverified.

### Requested fields

| Field | Value |
|---|---|
| ACCOUNT STATUS | ACTIVE (Meta business list) |
| BUSINESS OWNER | JustNow — 579302160985190 |
| PAYMENT STATUS | payment method present (balance / billing health not readable) |
| DAILY SPEND LIMIT · ACCOUNT SPENDING LIMIT · BILLING HEALTH | not readable from this session — owner: Ads Manager → Account overview / Billing |
| PAGE · INSTAGRAM · DATASET · WHATSAPP | not readable (Pages endpoint refused); expected assets = Page 122098309970001876, IG 17841461253086330, pixel 614743294720303 |
| ACTIVE / PAUSED CAMPAIGNS · HISTORICAL / 30D / 90D SPEND · OBJECTIVES · GOALS · CPM · CTR · CPA · LEADS · CONVERSATIONS · PURCHASES · LEARNING · AUDIENCES · EXCLUSIONS | not readable — needs the export below |
| RESTRICTIONS · ACCOUNT QUALITY · DELIVERY WARNINGS | not readable — owner: business.facebook.com/accountquality |

### Repair / unblock plan (exact)

1. **Give this session a readable copy (fastest, tonight-compatible):** Ads Manager → select JustNow44
   → Campaigns / Ad sets / Ads tabs → Reports → Export (CSV, lifetime + last 30 d + last 90 d, columns:
   delivery, objective, optimisation goal, budget, spend, impressions, CPM, CTR, results, cost per
   result, leads, messaging conversations started, purchases, learning phase) and Account overview
   (spend limit, daily limit, payment, Account Quality). Drop the files into `meta/justnow44/` in this
   repo — the mission decision and the M6 build follow the same scorecard rules as jn/JN.
2. **Or re-enable the connector path:** reconnect the Meta connector once Meta lists 2820299204977421
   as enabled (check `ads_get_ad_accounts` → `is_ads_mcp_enabled`), or link a browser session so Ads
   Manager can be read directly.
3. **Asset checklist to apply in Business Settings regardless of history** (no spend involved):
   pixel 614743294720303 → assign to JustNow44 (Data sources → Pixels → Add assets); Page
   122098309970001876 and IG justnow.life.ae → assign with advertise permission; share audiences
   "JN - Confirmed bookings 12mo (calendar)" 120251936408430312 and "contacts (9).csv"
   120251835232100312 (same business, no new audiences); confirm the WhatsApp number on the Page;
   payment method + spending limit per the owner's scale target; Account Quality clean.
4. **Mission — decided from evidence, not assumed:** provisional branches, resolved by the export:
   * history shows CTWA at ≤ AED 4.5 with volume and the largest spend limit → **HIGH-SCALE WHATSAPP
     home**: twin jn's 7 winners into JustNow44 (same posts, same rules as T1/T2), jn keeps
     reactivation + Arabic segments only — one WhatsApp prospecting home at any time, never both;
   * history shows website Lead / Purchase work or nothing usable → **HIGH-SCALE WEBSITE** mirror of
     the JN WB structure, or **CREATIVE SCALE** (graduated CT winners at scale) — JN keeps the Lead
     learning until JustNow44 proves parity;
   * restriction found in Account Quality → HOLD until resolved.
   Name after the decision: `JUSTNOW | HIGH-SCALE [MISSION] | JustNow44`.

```
JUSTNOW44
ROOT PROBLEM:  connector-side (Meta Ads MCP staged rollout); no account-side problem visible at business level
FIXED:         NO — not readable from this session; unblock = export to meta/justnow44/ or enable a read path
MISSION:       DEFERRED (branches above)
DAILY SCALE CAPABILITY: unknown (spend limit not readable)
```

---

## M3 — shared data architecture (fresh check 2026-10-09 03:50 Dubai)

Pixel **614743294720303** "Just Now For Building Cleaning Services CO LLC" (business 579302160985190):
active, browser last fired 02:51 Dubai, server last fired 02:54 Dubai (CAPI live), first-party cookies
on. Orphan dataset 2173595413219328 still never fired; pixels 706289834670044 / 1400794378663670 last
saw browser hits 30 Sep — check the site tag for leftover IDs. **No new pixel for any mission.**

| ACCOUNT | PIXEL / DATASET | PAGE | IG | WEBSITE DOMAIN | BOOKING EVENT | CUSTOMER AUDIENCES | STATUS |
|---|---|---|---|---|---|---|---|
| jn 1037126214908677 | 614743294720303 (Lead ad sets, paused; ContentView test) | 122098309970001876 Just Now (+ CO LLC 503162459555897) | justnow.life.ae | justnow.life | Lead (438/28d, EMQ 7.8); Schedule 209 | jn customers 889 (120249973174230073), LAL 1% 120250006505260073, shared JN LAL bookings 120251936410460312 | **CORRECT** — hygiene: exclusions on winners (A3, staggered) |
| JN 9147325105346647 | 614743294720303 (5 Lead ad sets) ✓ | same | justnow.life.ae + justnow.cs | justnow.life | Lead | confirmed bookings 12mo 120251936408430312, contacts csv 120251835232100312, LAL bookings, pixel audiences (Book Now 14d, Lead 14d, site 30/90d), engagers | **CORRECT** — delete the 09:59 duplicate audiences later |
| justnow22 1897980308260660 | none assigned to an ad set | both Just Now Pages | not checked | — | — | none | **FIX REQUIRED before CT**: assign pixel 614743294720303, share customers 889 |
| JNN 1304802461392117 | none | none visible | none | — | — | none | **FIX REQUIRED before any use**: assign pixel, Page, IG, audiences |
| JustNow44 2820299204977421 | unknown | unknown | unknown | — | — | unknown | **VERIFY / FIX** via checklist in M2 |
| 658869122728885 | none (LPV boost) | 4 Pages incl. Clean House, real estate | — | — | — | none | HOLD — no fix, no investment |
| Make CAPI Purchase flow | 614743294720303 ✓ | — | — | — | Purchase (completed job) | — | CORRECT config, 0 events sent so far |

Architecture verdict: account mission separation YES, data fragmentation NO — every mission account
uses or will be assigned the one pixel; the booking truth stays website → booking → confirmation →
completed service (calendar → Make → CAPI).

---

## M4–M7 — replacement structure and winner migration (built on paper, 0 writes)

Object specs with full targeting blocks are in `mission-migration-plan-2026-10-09.md` §2.2, §2.4,
§3.2, §5 and §9. Consolidated build list:

| Home | Campaign | Ad set | Budget | Ads (CONTROL / CHALLENGERS) |
|---|---|---|---|---|
| **WHATSAPP HOME = jn** | `WA \| PROSPECTING \| SHJ \| HOME-MOVERS` (new) | T1 `WA \| HOME-MOVERS \| SHJ \| CONVERSATIONS` | AED 60/day | CONTROL post _1116950464613349 · CHALLENGER post _957062783432763 |
| | same | T2 `WA \| MOTHERHOOD \| DXB+SHJ+AJM \| CONVERSATIONS` | AED 30/day | CONTROL post _1559790696189996 |
| | `WA \| REACTIVATION \| CUSTOMERS 12M \| DEEP CLEANING` (new) | `WA \| CUSTOMERS 12M \| UAE \| REACTIVATION` | AED 20/day | CONTROL customer-voice post _122278001594006883 · CHALLENGER Arabic stove-grease post _1622838339212041 |
| | existing 3 campaigns | 9 winners — rename to WA convention only | unchanged | unchanged |
| **WEBSITE HOME = JN** | 120252107068880312 → `WB \| PROSPECTING \| UAE \| DEEP CLEANING` | keep 120252107075750312 → `WB \| BROAD \| DXB+SHJ+AJM \| BOOKING` | CBO 84 → 100 | CONTROL C1-1-d (1484505567067844) · CHALLENGERS C1-1-b (2012729279425471), studio video (1094497890116067), W-c sticky-kitchen EN (video 2163113240903678) |
| **RETARGETING HOME = JN** | 120252107080200312 → `WB \| RETARGETING \| UAE \| DEEP CLEANING` | new `WB \| RETARGETING \| UNION 30D \| BOOKING` | CBO 70 | CONTROL C2-1-c (800898536451029) · CHALLENGERS C2-3-a (1765887427985234), C2-2-d (1132547542778119) |
| **CREATIVE TEST HOME = justnow22** | `CT \| 2026-10 \| HOOK-TEST-01` (new) | `CT \| WOMEN 25-55 \| DXB+SHJ \| CONVERSATIONS` | AED 40/day | CONTROL sticky-kitchen post _2163113240903678 · TESTS 2012729279425471, video 2380999242725474, post _122374924118006883, 1834696980892667 (+EN cut) |
| **PURCHASE FUTURE HOME** | JN single test ad set `PUR \| BROAD \| UAE \| PURCHASE` — **gated**, see below; JNN reserved | | AED 150/day when open | CONTROL = WB control |
| **JUSTNOW44** | built only after M2 export (M6) | | | |

Totals prepared: **4 new campaigns, 6 new ad sets, 15 ads** (3 twins + 2 reactivation + 1 W-c + 1
studio move + 3 retargeting + 5 CT). Built tonight: **0** (write enforcement unverified).

### Winner migration cards

```
WINNER 1
SOURCE ACCOUNT: JN 9147325105346647 · SOURCE CAMPAIGN: 120251948470120312 · SOURCE AD SET: 120251948470210312
SOURCE AD: 120251948470150312 (+ variant 120251948470350312) · CREATIVE ID: 1388128153493483 (1065906929646208)
POST ID: 122098309970001876_1116950464613349 (122098309970001876_957062783432763) · IG media 17896642608283094
30D RESULT: 391 conv @4.03 (variant 123 @4.20) · 7D RESULT: 113 @3.85 (48 @3.79) · CPA: AED 4.03 · BOOKING QUALITY: 7 Meta leads in-thread / 30d; purchases not attributed
TARGET ACCOUNT: jn 1037126214908677 · TARGET CAMPAIGN: WA | PROSPECTING | SHJ | HOME-MOVERS · TARGET AD SET: T1
TARGET OPTIMIZATION: CONVERSATIONS → WhatsApp (Page 122098309970001876) · TARGET AUDIENCE: 18–65, Sharjah pin 25.257,55.356 r10mi,
furniture / home improvement / modern furniture / online shopping / home / luxury goods, Engaged Shoppers, Recently moved, Advantage audience ON
EXCLUSIONS: customers 889 (120249973174230073) · STARTING BUDGET: AED 60/day · SOCIAL PROOF PRESERVED: YES (same Page, same post IDs)

WINNER 2
SOURCE ACCOUNT: JN · SOURCE CAMPAIGN: 120251948470120312 · SOURCE AD SET: 120251948470250312 · SOURCE AD: 120251948470130312
CREATIVE ID: 1100574565779685 · POST ID: 122098309970001876_1559790696189996 · IG media 18040239875751399
30D RESULT: 34 conv @3.78 (ad set 75 @4.00) · 7D RESULT: 8 @2.78 · CPA: AED 3.78 · BOOKING QUALITY: n/a
TARGET ACCOUNT: jn · TARGET CAMPAIGN: WA | PROSPECTING | SHJ | HOME-MOVERS · TARGET AD SET: T2
TARGET OPTIMIZATION: CONVERSATIONS → WhatsApp · TARGET AUDIENCE: 25–65, 3 pins, motherhood / parenting / online shopping / fashion accessories, married, locales 6/24/28
EXCLUSIONS: customers 889 + Lead 14d (120250006502540073) · STARTING BUDGET: AED 30/day · SOCIAL PROOF PRESERVED: YES

WINNER 3 (website, stays home — consolidation not migration)
SOURCE/TARGET ACCOUNT: JN · AD SET: 120252107075750312 · AD: 120252109342810312 · CREATIVE ID: 1484505567067844 · POST ID: 122098309970001876_122378467106006883
30D: 6 leads @78, 5 purchases AED 1,497 · 7D: same (started 30 Sep) · TARGET: WB | BROAD | DXB+SHJ+AJM | BOOKING (rename only) · OPTIMIZATION: LEAD on 614743294720303
EXCLUSIONS: bookings 12mo, Book Now 14d, Lead 14d · BUDGET: CBO 100 · SOCIAL PROOF PRESERVED: YES (untouched)

WINNER 4 (website challenger)
SOURCE/TARGET: JN · AD: 120252107434020312 · CREATIVE ID: 2012729279425471 · POST ID: 503162459555897_28340961415525425 (CO LLC Page) · 30D: 3 leads @10 on AED 30, 1 purchase AED 279 → keep as challenger in WB prospecting; also CT test #1

WINNER 5 (retargeting)
SOURCE: JN C2-1 120252107098030312 · AD: 120252109354160312 · CREATIVE ID: 800898536451029 · POST ID: 122098309970001876_122379608342006883 · 30D: 2 leads, 3 purchases AED 578
TARGET: JN WB | RETARGETING | UNION 30D | BOOKING · OPTIMIZATION: LEAD · AUDIENCE: Book Now 14d ∪ site 30d ∪ IG/FB engagers 365d · EXCLUSIONS: bookings 12mo, Lead 14d · BUDGET: CBO 70 · SOCIAL PROOF: YES

WINNER 6 (jn reference winners — not moved; jn is the home)
A Sharjah 120249855372950073 (Creator reel 2 3592620130898135 post _4303960699820816 204 @3.55; Top creator reel 1771707910750120 post _1732956274575988 135 @4.15; Sticky kitchen 839133225923661 post _2163113240903678 137 @3.90) ·
Copy A 1660090815679685 post _1387153059699272 309 @3.49 · New Sales Ad Set 1417053363666139 post _890288284018661 243 @3.43 ·
Copy 2 1310716354436732 post _122297017868006883 294 @4.28 · Copy B 1041458758894040 post _122312434262006883 113 @3.81 ·
B Arabic 1870108203957859 post _1622838339212041 74 @4.15 — all KEEP; the sticky-kitchen family is the universal CONTROL.
```

---

## M8 — activation plan

Order per batch: create PAUSED → read back (name, budget, destination, exclusions, preview shows the
original post with its engagement) → activate → observe 7 days (10 for retargeting) → compare CPA +
booking rate (respond.io / calendar) → then M9. Nothing activated tonight.

---

## M9 — waste classification (exact state)

| Item | ID | Class | Trigger |
|---|---|---|---|
| jn 9 WhatsApp winners | …372950073, …745520073, …697040073, …757070073, …813520073, …378300073, …947966990073, …379550073, …379980073 | **KEEP** | — |
| jn C3-2 Arabic, C3-3 LAL | 120250020907890073, 120250020914410073 | KEEP (C3-3 to AED 300 then decide) | — |
| JN C1-1 Broad | 120252107075750312 | **KEEP** (rename) | — |
| JN CTWA winner + motherhood | 120251948470210312, 120251948470250312 | **MIGRATE** (T1, T2) | A1 |
| JN CTWA campaign | 120251948470120312 | **PAUSE AFTER REPLACEMENT** | T1/T2 pass |
| JN C2-1, C2-2, C2-3 | 120252107098030312, 120252107107740312, 120252107111220312 | **PAUSE AFTER REPLACEMENT** (at union launch, shared CBO) | A2 |
| JN video test ad set | 120252195374160312 | PAUSE AFTER REPLACEMENT (ad moved into WB prospecting) | A2 |
| jn C3-1 Women (customer list) | 120250020902640073 | PAUSE AFTER REPLACEMENT (reactivation ad set) | 7 days after |
| JN 0-result women ad set | 120251948470220312 | **PAUSE NOW IF CLEAR WASTE** ✓ | first approved batch |
| 658869122728885 LPV boost | campaign 120249701767850032 | **PAUSE NOW IF CLEAR WASTE** ✓ | first approved batch |
| jn C3-4 Broad | 120250020898360073 | **PAUSE NOW IF CLEAR WASTE** ✓ (CPA 6.1–6.5, CPM 2× siblings) | first approved batch |
| jn Book Now Lead campaigns (wrong-purpose website in WhatsApp account) | 120249937413940073, 120249870686550073, 120249942058580073 | **ARCHIVE** (already paused) | any time |
| jn Reach / LPV boosts; JN IG boost; JN Persona + June-July campaigns | 120249856739720073, 120249858947210073, 120250027208020073, 120250080111120073, 120252051375920312, 120251888623070312, 120252041385800312 | ARCHIVE (already paused) | any time |
| JN "[OLD - DELETE]" + zero-spend drafts | 120227646457240312, 120231157544050312, 120229999555140312, 120251632668990312, 120252057337460312, 120252057331920312, 120252043242550312, 120251956780710312 | ARCHIVE | any time |
| 658869122728885 legacy …7949 campaigns (ended, status ACTIVE) | 120201463296540032, 120202633367610032, 23859136563650031, 23859135342840031 | ARCHIVE (set PAUSED) | any time |
| JN duplicate audiences | 120252106926760312, 120252106929540312, 120252106931330312, 120252110720830312 | ARCHIVE (delete, unreferenced) | any time |
| jn "365 - sep 2026" pair | 120249629710440073, 120249629704230073 | RENAME (not duplicates — different sizes) | any time |
| protected / unreadable | 1679026507158086, 2820299204977421, 311791788087024 | **DO NOT TOUCH** | — |

---

## M10 — account renames (prepared; after missions are verified and enforcement is verified)

```
POST /act_1037126214908677  name="JUSTNOW | WHATSAPP SALES | jn"
POST /act_9147325105346647  name="JUSTNOW | WEBSITE BOOKINGS | JN"
POST /act_1897980308260660  name="JUSTNOW | CREATIVE TESTING | justnow22"
POST /act_1304802461392117  name="JUSTNOW | FUTURE REVENUE | JNN"
POST /act_658869122728885   name="JUSTNOW | HOLD / LEGACY | Personal"
POST /act_311791788087024   name="JUSTNOW | HOLD / LEGACY | Just Now"            # once settled/writable
--  2820299204977421 → "JUSTNOW | HIGH-SCALE [MISSION] | JustNow44" only after M2 evidence
--  1679026507158086 NEVER
```

## M11 — read-back plan

After every approved batch: GET each created/edited object (campaign, ad set, ad: name, status,
budget, optimisation goal, destination, promoted_object, targeting exclusions, creative → post id) and
each renamed account (`?fields=name`); record EXPECTED vs ACTUAL in the plan's §18.4-style table; any
mismatch → rollback that object (PAUSE / revert name) before continuing.

---

## Purchase / Revenue gate — FAIL (re-checked 03:50 Dubai)

Latest Purchase on the pixel: 6 Oct ≈ 22:00 Dubai, from the old **confirmation-time** flow — not
evidence for the completed-service feed. Completed-job flow: configured (value AED, event_id =
calendar id, dedup ledger) but **0 events sent** (9 Oct run: 9 found / 9 already sent / 37 pending
DONE lines); 0/7 consecutive days; EMQ for Purchase not visible; volume 0. No Purchase optimisation
anywhere until 7 straight days of real DONE-service events.

---

## FINAL MORNING REPORT

```
JN / jn OVERLAP:
BEFORE: CTWA prospecting in both accounts (JN 3 ad sets ≈ AED 80/day; jn 13 ≈ AED 270/day) on the same Page, line,
        pins and creative family; personal account buying the same Sharjah traffic; website attempts inside jn.
AFTER:  designed, not yet live — jn sole WhatsApp home (+T1/T2 twins), JN website + retargeting only, 3 "pause now"
        items and 3 "pause after replacement" items with exact IDs; awaiting write approval.

WASTE REMOVED:  0 AED/day tonight (no writes). Estimated on approval: AED 60–75/day
                (658869122728885 boost 15 + C3-4 share ≈ 12 + JN/jn auction premium ≈ 35–50).

JUSTNOW44:
ROOT PROBLEM:   connector-side — Meta Ads MCP staged rollout refuses 2820299204977421; business-level data shows
                ACTIVE, payment present, no disable flag → no account-side problem visible
FIXED:          NO (unreadable from this session; export or enabled read path needed — steps in M2)
MISSION:        DEFERRED — HIGH-SCALE WHATSAPP if history shows CTWA ≤ AED 4.5 at volume (jn winners then twin
                into it, one WhatsApp home only); else HIGH-SCALE WEBSITE / CREATIVE SCALE; HOLD if restricted
DAILY SCALE CAPABILITY: unknown (spend limit not readable)

SHARED DATASET: VERIFIED — 614743294720303 live (browser 02:51, server 02:54 Dubai), used by jn + JN + CAPI;
                justnow22 / JNN / JustNow44 need asset assignment (no new pixels)

WHATSAPP HOME:        jn 1037126214908677
WEBSITE HOME:         JN 9147325105346647
RETARGETING HOME:     JN 9147325105346647 (WB | RETARGETING | UNION 30D) + reactivation in jn
PURCHASE FUTURE HOME: single test ad set in JN when the gate passes; JNN 1304802461392117 reserved
CREATIVE TEST HOME:   justnow22 1897980308260660

NEW CAMPAIGNS BUILT: 0 (4 fully specified)
NEW ADS BUILT:       0 (15 fully specified)
WINNERS MIGRATED:    0 (2 ready with post IDs; 4 more consolidated in place)
OLD DUPLICATES PAUSED: 0 (3 pause-now + 4 pause-after-replacement with exact IDs)
ACCOUNT RENAMES:     0 executed; 6 prepared (jn, JN, justnow22, JNN, Personal, Just Now-unsettled); JustNow44 pending
PRODUCTION WRITES:   0
ROLLBACKS:           0

STILL BLOCKED:
  1. Write approval enforcement NOT VERIFIED → every build/pause/rename waits for line-by-line approval
  2. JustNow44 unreadable through every connected path → export to meta/justnow44/ or enable a read path
  3. Purchase gate FAIL → 37 DONE lines + 7 clean days before any Purchase ad set
  4. justnow22 / JNN have no pixel, Page or audiences assigned → Business Settings asset sharing first

SYSTEM READY FOR SCALE: NO
  (structure fully specified and reversible; nothing live changed; scale depends on blockers 1 and 2)
```
