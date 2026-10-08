# JUSTNOW — FULL META AD ACCOUNT OPTIMIZATION MAP

Audit date: 2026-10-09 (Asia/Dubai). Read-only audit of every Meta ad account reachable from the
connected Meta Ads connector. **No production write was made.**

```
WRITE APPROVAL ENFORCEMENT: NOT VERIFIED
PRODUCTION WRITES:          0
ACCOUNT RENAMES EXECUTED:   0
READY FOR EXECUTION:        NO
```

Sources: Meta Ads connector (accounts, campaigns, ad sets incl. targeting/exclusions, custom
audiences, Pages, IG accounts, creatives, dataset list/quality/stats), Make scenarios (Purchase
pipeline), respond.io agent prompt (service zones). Spend figures are AED unless stated. "7d / 30d /
90d" = Meta presets `last_7d / last_30d / last_90d` on 2026-10-09; "lifetime" = preset `maximum`.

Fallback connectors for the accounts the Meta connector refuses: Markifact has **no Meta Ads
connection**, Windsor.ai has only GA4 + Instagram-public, Madgicx has no active subscription. So
JustNow44 (2820299204977421) and "Just Now" 311791788087024 could not be read from this session.

---

## 0. Executive summary

* 32 ad accounts are reachable: 29 JustNow-related, 3 belong to other brands (Clean House ×2,
  UAE Property). Only **4 have ever spent**: `jn` (AED ~116.6k lifetime), `JN` (AED ~66.4k),
  `justnow22` (AED 831), and the unnamed personal account `658869122728885` (AED ~3.4k, still
  spending AED 15/day on an unmanaged boost). Everything else is zero-spend, disabled, closed,
  unsettled or system-created ("Read-Only" USD accounts from WhatsApp/Shopify/IG integrations).
* `jn` and `JN` run the **same mission against each other**: both buy click-to-WhatsApp
  conversations from the same Pages, same IG identity, same creatives, same Sharjah/Dubai pins,
  same interest stacks, same pixel. Combined 30d: AED 9.7k → 2,434 conversations at AED 4.0.
  `jn` carries 3× the volume at the same CPA; `JN` is the only account with a working website-Lead
  structure (C1/C2, pixel audiences, exclusions) and it attributed **10 purchases / AED 2,853 in the
  last 7 days** from website campaigns.
* Purchase signal is **not healthy enough for a dedicated Purchase account**: 118 Purchases in 28 days
  on the pixel, all from the legacy "confirmed booking" flow; the new "completed job" flow has sent
  0 so far (37 jobs pending a DONE line). Recommendation: ONE consolidated Purchase ad set inside the
  website account once the pipeline proves itself; reserve `JNN` as the future Purchase account.
* Final structure: **jn → WHATSAPP SALES · JN → WEBSITE BOOKINGS (+ retargeting, + Purchase test) ·
  justnow22 → CREATIVE TESTING · JNN → HOLD (reserved for Purchase/Revenue) ·
  658869122728885 → HOLD / LEGACY · 311791788087024 → HOLD / LEGACY (unsettled) ·
  JustNow44 → decision deferred (unreadable) · 1679026507158086 → OWNER-PROTECTED, untouched.**

---

## 1. Inventory — every accessible ad account

Business portfolios: **BM-A** = Just Now For Building Cleaning Services CO LLC (228069640223666);
**BM-B** = JustNow (579302160985190); CH = Clean House (1352078595617299); UP = UAE Property
business (2389946897832557). Timezone is Asia/Dubai on every account that could be read.

| # | Account name | ID | BM | Cur. | Status | Readable | Lifetime spend | Last spend | Active / paused campaigns | Dataset in use | Page / IG | WhatsApp dest. | Historical purpose |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **jn** ("JN Small") | 1037126214908677 | BM-A | AED | ACTIVE, payment ✓ | yes | ~116.6k (Mar 2025→) | 2026-10-09 | 3 active (13 ad sets) / ≥97 paused (100 returned, page limit) | 614743294720303 (Lead + ContentView ad sets) | Pages: Just Now 122098309970001876, CO LLC 503162459555897, 2 personal Pages · IG justnow.life.ae | WhatsApp via Page "Just Now"; copy links wa.me/+971507677282 | CTWA sales since Mar 2025; Madgicx tests Aug 2025; website-purchase tests Sep–Oct 2025; lead form Nov 2025; reach/boosts |
| 2 | **JN** ("JN Capital") | 9147325105346647 | BM-B | AED | ACTIVE, payment ✓ | yes | ~66.4k (May 2025→) | 2026-10-09 | 4 active (8 ad sets) / 51 paused | 614743294720303 (5 Lead ad sets) | Pages: Just Now, CO LLC, 2 personal Pages · IG justnow.life.ae + justnow.cs | WhatsApp via Page "Just Now" (1 CTWA campaign) | CTWA sales since May 2025; website Leads since 30 Sep 2026; reach; IG boosts; call test |
| 3 | justnow22 | 1897980308260660 | BM-A | AED | ACTIVE, payment ✓ | yes | 831 (Feb + Apr 2026) | 2026-04-18 | 0 delivering (4 ended boosts still "ACTIVE") / 5 paused | none | Pages: Just Now, CO LLC | WhatsApp (CTWA, Feb 2026) | 5-day CTWA test Feb 2026; post boosts Apr 2026 |
| 4 | (unnamed) "Personal / IG-app" | 658869122728885 | none | AED | ACTIVE, payment ✓ | yes | ~3.36k (Sep 2023→) | 2026-10-09 (AED 82 in Oct) | 1 delivering boost / 32 old | none (traffic boost, no event) | Pages: CO LLC, Just Now, Clean.House.ae, "Real State agency" | old campaigns point to **…7949**, a different number | Clean House promos 2023–24, Marketplace listing boosts, IG boosts, now a traffic boost to justnow.life/book-now |
| 5 | JNN | 1304802461392117 | BM-A | AED | ACTIVE, payment ✓ | yes | 0 — never spent | — | 0 / 0 | none | not checked (empty) | — | never used |
| 6 | (unnamed) | 1679026507158086 | BM-A | AED | ACTIVE, payment ✓ | yes (read only) | 0 | — | — | — | — | — | **OWNER-PROTECTED — EXCLUDED FROM EXECUTION** |
| 7 | JustNow44 | 2820299204977421 | BM-B | AED | ACTIVE, payment ✓ | **no** (connector: "Ads MCP gradually rolling out") | unknown | unknown | unknown | unknown | unknown | unknown | jn campaign "jn - Reel tests (rebuilt from JustNow44, no WhatsApp marketing msgs)" (29 Sep 2026) implies Reel tests ran here and were rebuilt in jn |
| 8 | Just Now | 311791788087024 | BM-A | AED | **UNSETTLED**, payment ✓ | no ("Unknown error") | unknown | unknown | unknown | unknown | unknown | unknown | unpaid balance blocks delivery; history unreadable |
| 9 | unknown (Read-Only) | 856564090492076 | BM-B | USD | ACTIVE, payment ✓ | yes | 0 | — | 0 | — (catalog "Professional_Services" recommended) | — | — | system-created |
| 10 | Just Now (Read-Only) | 1720532878634926 | BM-A | USD | ACTIVE, no payment | yes | 0 | — | 0 | — | — | — | system-created |
| 11 | Test WhatsApp Business Account (Read-Only) | 996359675586790 | BM-A | USD | ACTIVE, payment ✓ | yes | 0 | — | 0 | — | — | — | WhatsApp Business integration |
| 12 | Justnow.life.ae (Read-Only) | 1553685189104802 | BM-A | USD | ACTIVE, payment ✓ | yes | 0 | — | 0 | — | — | — | IG integration |
| 13 | … WhatsApp for Shopify (Read-Only) | 1504118357546048 | BM-A | USD | ACTIVE, payment ✓ | yes | 0 | — | 0 | — | — | — | Shopify integration |
| 14 | justnow.cs (Read-Only) | 1499748364956496 | BM-B | USD | ACTIVE, payment ✓ | yes | 0 | — | 0 | — | — | — | IG integration |
| 15 | unknown (Read-Only) | 741583665672939 | BM-B | USD | ACTIVE, payment ✓ | yes | 0 | — | 0 | — | — | — | system-created |
| 16 | JustNow (Read-Only) | 1373981191582615 | BM-B | USD | ACTIVE, payment ✓ | yes | 0 | — | 0 | — | — | — | system-created |
| 17 | … COLLC (Read-Only) | 3052111794970919 | BM-B | USD | ACTIVE, no payment | yes | 0 | — | 0 | — | — | — | system-created |
| 18 | … COLLC (Read-Only) | 815346134471737 | BM-B | USD | ACTIVE, no payment | yes | 0 | — | 0 | — | — | — | system-created |
| 19 | … CO LLC (Read-Only) | 1583312996307869 | BM-B | USD | ACTIVE, no payment | yes | 0 | — | 0 | — | — | — | system-created |
| 20 | Just Now (Read-Only) | 1340906084205111 | BM-A | USD | ACTIVE, no payment | yes | 0 | — | 0 | — | — | — | system-created |
| 21 | justnow.life.ae (Read-Only) | 1909989033058072 | BM-A | USD | ACTIVE, no payment | yes | 0 | — | 0 | — | — | — | system-created |
| 22 | Just Now (Read-Only) | 1007292425694931 | BM-A | USD | ACTIVE, no payment | yes | 0 | — | 0 | — | — | — | system-created |
| 23 | … CO LLC (Read-Only) | 1524467415226667 | BM-A | USD | ACTIVE, no payment | no (MCP disabled) | — | — | — | — | — | — | system-created |
| 24 | … WhatsApp for Shopify (Read-Only) | 1852789671986208 | BM-A | USD | ACTIVE, no payment | no (MCP disabled) | — | — | — | — | — | — | Shopify integration |
| 25 | justnow.life.ae (Read-Only) | 1843769482985909 | BM-A | USD | ACTIVE, no payment | no (MCP disabled) | — | — | — | — | — | — | IG integration |
| 26 | … CO LLC (Read-Only) | 825353993434985 | none | USD | **DISABLED** (flagged "unusual activity") | no | — | — | — | — | — | — | legacy |
| 27 | … CO LLC (Read-Only) | 2053880215357344 | BM-A | USD | **DISABLED** (flagged) | no | — | — | — | — | — | — | legacy |
| 28 | … CO LLC (Read-Only) | 844053351344804 | none | USD | **DISABLED** (flagged) | no | — | — | — | — | — | — | legacy |
| 29 | (unnamed) | 261191663067349 | none | AED | **CLOSED** | no | — | — | — | — | — | — | legacy |
| 30 | (unnamed) | 245158590746748 | CH | AED | UNSETTLED | no | — | — | — | — | — | — | **Clean House brand — out of JustNow scope** |
| 31 | (unnamed) | 975903583434612 | CH | AED | UNSETTLED | no | — | — | — | — | — | — | **Clean House brand — out of scope** |
| 32 | UAE Property | 720576909373045 | UP | AED | UNSETTLED | no | — | — | — | — | — | — | **other business — out of scope** |

Shared identities: both spending accounts advertise from Page **Just Now (122098309970001876)**
and Page **Just Now For Building Cleaning Services CO LLC (503162459555897)**, IG
**justnow.life.ae** (JN also justnow.cs), and both uploaded the same creative set on 30 Sep 2026.

---

## 2. Account-by-account analysis

### 2.1 jn — 1037126214908677 (BM-A, "JN Small")

**A. History.** First spend Mar 2025. Monthly spend (AED): Mar-25 6.8k · Apr 11.8k · May 7.8k ·
Jul 2.1k · Aug 16.4k · Sep 8.6k · Oct 12.5k · Nov 4.8k · *dark Dec-25→May-26* · Jun-26 1.3k ·
Jul 10.9k · **Aug 19.1k** · Sep 11.1k · Oct 1–9 3.2k. Lifetime ≈ **AED 116.6k**.
Totals: 7d AED 2,798 (CPM 17.45, CTR 2.46%, freq 1.55) · 30d AED 10,595 (CPM 13.62, CTR 1.79%,
freq 1.95, 30 attributed purchases / AED 1,882, 20 leads) · 90d AED 43,155 (CPM 7.41, CTR 0.95%,
**freq 4.05**).
Strongest periods: Sep–Oct 2025 (CTWA at AED 2.50–2.91 per conversation: 1,636 and 1,342
conversations) and the current Sep 20→ structure (AED 3.4–4.3). Weakest: Aug 2026 (CTR 0.74%,
frequency 3.05 — Reach campaigns + a single AED 23k-budget CTWA campaign run to fatigue at AED 4.95,
freq 2.39); Sep 12–14 "Sales - Copy" clusters at AED 9–16. Structural changes: Madgicx automation
Aug 2025 (purchase-optimised campaigns, no purchases); website Sales/purchase attempts Sep–Oct 2025
(2–4 purchases each, AED 68–546 per purchase); lead-form campaign Nov 2025 (75 leads @ AED 4.99);
full stop Dec 2025–May 2026; relaunch Jun 2026; "5158" audience test structure 19 Sep 2026; website
Lead attempts 21–27 Sep 2026 (paused).

**B. Campaign mix (100 campaigns returned; the list hit the page limit).** WhatsApp/Messages ≈ 55 ·
Awareness/Reach ≈ 18 · Boosts (post engagement, IG posts, "Promoting local business") ≈ 12 ·
Traffic/link clicks 4 · Website Lead (book-now) 3 · Purchase-optimised (Sales/Madgicx/Advantage+
shopping) 7 · Lead form 1 · Click-to-call 1.

**C. Active ad sets (all CONVERSATIONS, destination WhatsApp — two also IG Direct/Messenger).**

| Campaign → ad set | Budget | 7d spend → conv (CPA) | 30d spend → conv (CPA) | 90d | CPM 30d | Audience | Exclusions | Verdict |
|---|---|---|---|---|---|---|---|---|
| jn - WhatsApp Sales 5158 → **A - Sharjah city families 25-60** | CBO d90 | 667 → 177 (3.77) | 1,982 → 510 (3.89) | 1,982 | 18.5 | broad, 1 pin Sharjah r12km, Advantage audience | none | **WINNER** |
| New Sales Campaign (20 Sep) → **Copy A** | CBO d90 | 446 → 117 (3.81) | 1,080 → 309 (3.49) | 1,080 | 19.8 | Parents/parenting, Sharjah r10mi | none | **WINNER** |
| New Sales Campaign → **New Sales Ad Set** | " | 193 → 67 (2.88) | 834 → 243 (3.43) | 834 | 18.5 | luxury/property/landlord, pin Ajman-Sharjah r10mi | none | **WINNER** |
| New Sales Campaign → **Copy 2** | " | 93 → 32 (2.91) | 1,258 → 294 (4.28) | 1,258 | 17.7 | teachers + jewelry, 2 pins Dubai/Sharjah | none | KEEP |
| New Sales Campaign → **Copy B** | " | 222 → 64 (3.46) | 431 → 113 (3.81) | 431 | 19.0 | interior design/renovation/recently moved, Sharjah | none | KEEP |
| 5158 → **B - Arabic speakers Sharjah+Ajman** | " | 91 → 26 (3.48) | 337 → 85 (3.96) | 337 | 15.8 | Arabic locale, 2 pins | none | KEEP |
| 5158 → **TEST 24 Sep - E - Dubai women 25-55** | " | 111 → 25 (4.44) | 229 → 63 (3.63) | 229 | 20.9 | women, 6 small Dubai pins | none | KEEP (test) |
| 5158 → **C - Dubai premium communities** | " | 32 → 10 (3.21) | 184 → 41 (4.50) | 184 | 23.7 | 6 Dubai pins | none | KEEP, under-funded |
| 5158 → **D - Dubai inner belt families** | " | 10 → 5 (1.99) | 159 → 34 (4.69) | 159 | 20.3 | 4 Dubai pins | none | KEEP, under-funded |
| JN \| C3 WhatsApp Bookings → **C3-4 Broad 25+** | CBO d90 | 329 → 51 (**6.45**) | 373 → 61 (6.11) | 373 | **30.6** | jewelry/luxury, Dubai r10mi | excl. customers list | **WEAK** |
| C3 → **C3-1 Women 25+** | " | 201 → 40 (5.01) | 211 → 41 (5.15) | 211 | 25.8 | **includes** customers list (889) | — | REACTIVATION (mislabelled) |
| C3 → **C3-2 Arabic speakers 25+** | " | 143 → 31 (4.61) | 187 → 39 (4.80) | 187 | 26.2 | Arabic, teachers | excl. customers | KEEP |
| C3 → **C3-3 Lookalike 1% customers** | " | 48 → 9 (5.30) | 61 → 11 (5.55) | 61 | 20.6 | LAL customers + LAL bookings | excl. customers | TEST |

Paused/ended in the last 30 days: website Lead ad sets "Book Now – Lead (booking confirm)" ×3
(AED 427 → 5 leads @85 + 1 purchase AED 279; AED 154 → 1 lead @154; AED 24 → 1 lead @24 + 1
purchase AED 379); LPV boosts "Watch the grease melt" ×2 (AED 231 → 568 landing-page views, no
event optimisation); Reach boosts "[9/20/2026] Promoting local business Just Now" ×2 (AED 139);
"Sales - Copy" / "New Sales Campaign - Copy" clusters 5–14 Sep (CPA 7.7–18.3, CPM 24–43).
Learning status is not exposed for CONVERSATIONS ad sets; the winners clear 50 conversations/week
easily (A: 177/week), so they are out of learning.

**D. Stability.** Stable performer for WhatsApp (18 months, CPA band AED 2.5–5.0); website Lead and
Purchase attempts = insufficient data / weak.

**E. Data quality.** Result volume: excellent for conversations. Fragmentation: 13 active ad sets
across 3 campaigns, 6 of them centred on Sharjah within 10–12 mi of each other (same people, the
model copes but frequency 1.2–1.5 after 3 weeks). **Customer exclusions missing on 10 of 13 active
acquisition ad sets** (only C3 excludes "jn - Customers Jan 2025–Sep 2026"); the Jul–Sep mega
campaign *did* exclude engagers and 180-day audiences — the hygiene was dropped on 19–20 Sep.
Mixed destinations (WhatsApp vs "IG Direct + Messenger + WhatsApp") inside one campaign. Dozens of
identical names ("New Sales Campaign", "New Sales Ad Set - Copy"). Dead Madgicx audiences (eRFM,
video lookalikes) and a duplicated "365 - sep 2026" audience. One ad set optimises for
CONTENT_VIEW on the pixel (AED 27, nothing). No wrong WhatsApp number found in current ads.

### 2.2 JN — 9147325105346647 (BM-B, "JN Capital")

**A. History.** First spend May 2025. Monthly (AED): May-25 2.5k · Jun 6.7k · Jul 5.3k · *dark
Aug–Oct* · Nov 1.3k · *dark Dec* · Jan-26 2.0k · Feb 1.8k · *dark Mar* · Apr 0.8k · May 4.1k · Jun 5.5k
· Jul 6.7k · Aug 12.9k · **Sep 14.5k** · Oct 1–9 2.2k. Lifetime ≈ **AED 66.4k**.
Totals: 7d AED 1,862 (CPM 16.91, CTR 3.84%, 17 leads, **10 purchases / AED 2,853**) · 30d AED 10,817
(CPM 14.13, CTR 2.10%, freq 1.93, 65 leads of which 51 "Meta leads" in messaging, 13 purchases /
AED 2,855) · 90d AED 34,385 (CPM 10.48, CTR 1.70%, freq 2.86, 164 leads).
Strongest: Jan–Feb 2026 CTWA at AED 1.42–2.05 per conversation (CPM 6.5–6.8); Apr–Aug 2026 "New
Sales Campaign" AED 13.5k → 3,910 conversations @ 3.45; Jul 2026 "abu Dhabi" campaign 465 @ 2.36
(cheapest ever, but Abu Dhabi has been excluded from every campaign since — only resume if Abu
Dhabi is actually served); Jun 2026 ad sets @ 2.88–3.28. Weakest: Nov 2025 (CPM 22, CPA 4.2–5.1);
Aug 10–Sep 17 2026 fragmentation into 20+ "New Sales" ad sets at AED 5–12 (two flagged
WITH_ISSUES); Sep 26–27 "June-July segments" at AED 12–19 on AED 36–40 CPM.

**B. Campaign mix (55).** WhatsApp/Messages 33 · Awareness 8 · Traffic/IG-profile/link-click
boosts 7 · Website Leads 5 (4 built 26 Sep–7 Oct) · Click-to-call 1 · custom pixel conversion test 1.

**C. Active ad sets.**

| Campaign → ad set | Goal / event | Budget | 7d | 30d | CPM 30d | Learning | Audience / exclusions | Verdict |
|---|---|---|---|---|---|---|---|---|
| New Sales Campaign - Copy 2 → **New Sales Ad Set - Copy** | CONVERSATIONS → WhatsApp | CBO d80 | 617 → 162 conv (3.81) | 2,096 → 515 (4.07) | 15.1 | n/a | furniture / home improvement / recently moved, Sharjah r10mi, 18–65; **no exclusions** | **WINNER** |
| " → **New Sales Ad Set** | CONVERSATIONS | " | 22 → 8 (2.78) | 300 → 75 (4.00) | 16.9 | n/a | motherhood/parenting; excl. "lead" audience | KEEP |
| " → **New Sales Ad Set - Copy** (id …470220312) | CONVERSATIONS | " | 0 | 14 → 0 | 36.9 | n/a | women 25–65 | WEAK (no results) |
| JN \| C1 Website Acquisition → **C1-1 Broad 25+** | OFFSITE_CONVERSIONS → pixel 614743294720303 / **LEAD** | d84 | 506 → 9 leads (56) · **6 purchases AED 1,776** | 589 → 9 (65) | 27.9 | **FAIL (limited), 9 conv** | 3 pins Dubai/Shj/Ajman r10mi; excl. confirmed bookings 12mo, Book Now 14d, Lead 14d | **WINNER (website)** |
| JN \| C2 Retargeting → **C2-1 Book Now visitors 14d** | LEAD | d70 | 275 → 2 (138) · 3 purchases AED 578 | 339 → 2 (169) | 36.2 | FAIL, 2 | CA Book Now 14d; excl. bookings, Lead 14d | RETARGETING STRONG (consolidate) |
| C2 → **C2-3 IG+FB engagers 365d** | LEAD | " | 203 → 3 (68) · 1 purchase AED 499 | 217 → 3 (72) | 35.7 | FAIL, 3 | CA engagers; excl. bookings, site visitors | RETARGETING STRONG (consolidate) |
| C2 → **C2-2 Website visitors 30d** | LEAD | " | 14 → 0 | 15 → 0 | 38.7 | FAIL, 0 | CA site visitors 30d | WEAK (fold in) |
| JN \| Website Leads \| Studio Feedback Video → **Website Lead \| C1 service areas \| Video** | LEAD | d60 | 72 → 0 | 72 → 0 | 41.7 | LEARNING, 0 | same as C1-1 | CREATIVE TEST (7-day review) |

Recently paused: "Persona Launch Sep 2026" (3 Women decision-makers 1,140 → 229 @4.98; 4 Indian &
South Asian 413 → 81 @5.10; 2 Lookalikes 314 → 83 @3.78; 1 Warm retargeting 257 → 63 @4.09);
"June-July Segments + Past Customers" (AED 112 total, 6 conversations); "Same kitchen" IG boost
(AED 304 → 2,542 link clicks @0.12, nothing downstream); 3 big "New Sales" campaigns of Aug–Sep.
Zero-spend drafts kept: "JN - Website Booking (book-now) - VIDEO - AED 250/day", "JN - WhatsApp
(respond.io AI) - VIDEO - AED 100/day test", "Retest Campaign", "[OLD - DELETE]" ×3.

**D. Stability.** WhatsApp: historically good, currently one strong ad set (declining breadth).
Website: recent performer only (10 days) but the only account producing attributed purchases with
real values. Retargeting: insufficient volume (5 leads / 10 days) but correctly built.

**E. Data quality.** 51 campaigns paused, ~45 share the name "New Sales Campaign"; duplicate
audiences created twice on 30 Sep (Website visitors 30d, Lead 14d, Book Now 14d; two identical
LAL "Book Now visitors"); Clean House audiences (CH.FB/CH.INS) still present; 2 personal Pages
linked. Lead budget split over 5 ad sets → every one learning-limited (Meta needs ~50
events/week per ad set; the whole account made 14 leads in 10 days). The current CTWA winner has
no customer exclusion. Pixel use is correct (614743294720303 everywhere).

### 2.3 justnow22 — 1897980308260660 (BM-A)

Lifetime AED 831 across 9 campaigns. Feb 22–26 2026: two CTWA campaigns, AED 337 → 109
conversations @ **3.09** and AED 217 → 130 @ **1.67** (women 25–60, Dubai + Sharjah pins,
jewelry/luxury interests, Audience Network on, no exclusions); one Awareness AED 103. Apr 13–18
2026: four boosted posts (AED 175 → 49 conversations @ 1.85–7.55). "Madgicx - Custom Campaign"
and a Mar 2026 Sales campaign never spent. No pixel use, no audiences, both Just Now Pages linked.
7d/30d/90d spend: 0. Stability: insufficient data, but every test was cheap. Health: clean and
isolated. Strength: a sandbox that does not pollute the two production accounts.

### 2.4 658869122728885 — unnamed personal account (no business)

Lifetime ≈ AED 3.36k since Sep 2023: Clean.House.ae page promotions (2023–24), Facebook
Marketplace listing boosts (furniture — personal), Clean House WhatsApp promotions pointing at
**+971 50 767 7949** (a different number from the current business line), IG post boosts, a
"Boosted Story" (Jan 2025). **Live now:** "[10/3/2026] Promoting http://www.justnow.life/book-now"
— LANDING_PAGE_VIEWS, AED 15/day, AED 82 so far, 11.6k impressions, 344 landing-page views @ 0.24,
Sharjah r10mi, interests Luxury/Online shopping/Parents, excludes employer "Cleaner", **no pixel
event, no exclusions** — it drives traffic to the same page JN's C1 campaign is buying Leads on.
Four Pages linked incl. Clean.House.ae and a real-estate Page. 20+ ended campaigns still show
status ACTIVE. Verdict: personal/boost account, not a governed JustNow asset.

### 2.5 JNN — 1304802461392117 (BM-A)

Never spent, no campaigns, AED, payment method attached, same BM as jn. Structurally the cleanest
account available; no data.

### 2.6 1679026507158086 — OWNER-PROTECTED

Read only for the inventory: BM-A, AED, ACTIVE, payment method attached, zero lifetime spend.
**Excluded from every recommendation, rename and execution wave.**

### 2.7 Not readable from this session

* **JustNow44 — 2820299204977421** (BM-B, AED, ACTIVE, payment ✓). Connector refuses the account.
  Indirect evidence: jn campaign "jn - Reel tests (rebuilt from JustNow44, no WhatsApp marketing
  msgs)" (29 Sep 2026) → Reel tests ran in JustNow44 and were rebuilt in jn, possibly after a
  WhatsApp-marketing-message restriction. Mission **deferred until the owner exports its campaign
  history** (Ads Manager → Export) or the connector enables it. Do not rename yet.
* **Just Now — 311791788087024** (BM-A, AED, **UNSETTLED**). Billing must be settled before it can
  deliver; history unreadable. Default: HOLD / LEGACY.
* Disabled (825353993434985, 2053880215357344, 844053351344804 — "unusual activity"), closed
  (261191663067349), MCP-disabled read-only (1524467415226667, 1852789671986208, 1843769482985909):
  no role, no action.
* Clean House ×2 and UAE Property: other brands, out of JustNow scope (they share the owner's
  access, which is why they appear).

---

## 3. What each account learned best (scores /10, evidence-based)

| Account | WhatsApp conv. | Website leads | Purchase / revenue | Retargeting | Creative testing | Structural health | Data depth |
|---|---|---|---|---|---|---|---|
| **jn** 1037126214908677 | **9** — 1,844 conv/28d, CPA 3.4–4.3 on winners, 18 months, best-ever 2.5 | 3 — 7 leads @24–154, paused | 3 — 30 attributed/30d but mostly AED 1 placeholder values; 2025 Sales: 4 purchases @68 | 5 — customer list 889 + engager audiences, reactivation ad set @5.15, exclusions dropped | 6 — 5158 A–E is a live audience test; boosts mixed into production | 4 — 100+ campaigns, duplicates, no exclusions on winners, mixed destinations | 9 — AED 116k, 15k+ conversations |
| **JN** 9147325105346647 | **8** — 13.5k @3.45 (Apr–Aug), 1.4–2.1 (Jan–Feb), 515 @4.07 now | **6** — only working Lead structure; 14 leads/10d @ ~88 but 10 purchases AED 2,853 (ROAS ≈ 2.5–3.5) | **5** — 13 real-value purchases/90d; no Purchase-optimised ad set yet | **7** — C2 built right (pixel audiences, exclusions), tiny volume | 5 — persona + video tests, mixed into production | 5 — new "JN \| C1/C2" naming but 45 duplicate legacy names, WITH_ISSUES ad sets, duplicate audiences | 8 — AED 66k, 17 months |
| **justnow22** 1897980308260660 | 4 — 239 conv @1.67–3.09 in 5 days (tiny) | 0 | 0 | 1 | **6** — isolated, cheap, already used for tests | 7 — 9 campaigns, clean | 2 |
| **658869122728885** | 2 — 2023 boosts @2–11 | 1 — LPV boosts, no event | 0 | 0 | 2 | 2 — personal + Clean House + marketplace, stale statuses | 2 |
| **JNN** 1304802461392117 | 0 | 0 | 0 | 0 | 0 | 10 — empty | 0 |
| 1679026507158086 | protected — not scored | | | | | | |
| JustNow44 / 311791788087024 | not readable — not scored | | | | | | |

---

## 4. Ad set classification (every relevant ad set, with reason)

**jn**
* WHATSAPP STRONG / KEEP RUNNING / WINNER: A - Sharjah city families (510 @3.89), Copy A (309 @3.49),
  New Sales Ad Set 20 Sep (243 @3.43), Copy 2 (294 @4.28), Copy B (113 @3.81), B - Arabic speakers
  (85 @3.96), TEST E Dubai women (63 @3.63) — all at or below the account's AED 4.5 ceiling with
  CPM 16–21.
* WHATSAPP STRONG but under-funded: C - Dubai premium (41 @4.50), D - Dubai inner belt (34 @4.69) —
  cheap 7d CPA (3.21 / 1.99), starved by CBO.
* CREATIVE TESTING: C3-3 Lookalike 1% customers (11 @5.55, AED 61) — keep as a test, decide at AED 300.
* RETARGETING / REACTIVATION: C3-1 Women 25+ — it *targets* the 889-customer list; relabel and
  judge on bookings, not conversations.
* WEAK: C3-4 Broad 25+ (61 @6.11, CPM 30.6) — most expensive active ad set, same Dubai pin as others.
* WEBSITE: Book Now - Lead ad sets ×3 — DO NOT RESUME in jn (website lead belongs in JN).
* LEGACY: "Watch the grease melt" LPV boosts, "[9/20/2026] Promoting local business" Reach boosts,
  "New Awareness" ad sets (CTR 0.15–0.27%, freq 2.2–2.8), CONTENT_VIEW ad set, 2025 Sales/Madgicx
  purchase campaigns, "Sales - Copy" clusters (CPA 9–18).

**JN**
* WHATSAPP STRONG / WINNER: New Sales Ad Set - Copy (Copy 2 campaign; 515 @4.07, 162 @3.81 last 7d).
  PROTECT now; MOVE to jn only after a twin proves equal CPA (see A2).
* WHATSAPP STRONG: New Sales Ad Set (75 @4.00) — same treatment.
* WEAK: New Sales Ad Set - Copy …470220312 (AED 14, 0 results).
* WEBSITE STRONG / WINNER: C1-1 Broad 25+ — 9 leads, 6 purchases AED 1,776 on AED 589.
* RETARGETING STRONG: C2-1 Book Now visitors 14d, C2-3 IG+FB engagers 365d — correct audiences and
  exclusions, 5 leads / 4 purchases AED 1,077 on AED 556; consolidate to exit learning-limited.
* WEAK: C2-2 Website visitors 30d (AED 15, 0) — fold into the consolidated retargeting ad set.
* CREATIVE TESTING: Website Lead | C1 service areas | Video (Studio feedback) — 7-day review.
* PURCHASE CANDIDATE: none yet; C1-1's audience/exclusion set is the template for the single
  Purchase ad set in A4.
* LEGACY: Persona Launch ad sets (3 Women decision-makers 229 @4.98 is the only one worth
  re-using — in jn), June-July Segments (AED 12–19), "abu Dhabi" (DO NOT RESUME unless Abu Dhabi is
  served), Aug–Sep "New Sales" clusters, [OLD - DELETE] campaigns, zero-spend drafts.

**justnow22**: Feb 2026 CTWA ad sets (109 @3.09, 130 @1.67) = LEGACY reference / test template;
Apr boosts = LEGACY.

**658869122728885**: "[10/3/2026] Promoting book-now" = WEAK / WASTE (stop in A1); everything
else LEGACY / DO NOT RESUME (old WhatsApp number …7949, Clean House, marketplace).

---

## 5. Account-vs-account comparison

**WhatsApp.** jn: 1,844 conversations / AED 7,326 (30d) = **AED 3.97**, 13 ad sets, CPM 16–31,
best-ever AED 2.5 (Sep–Oct 2025), 18 months of learning, routing to WhatsApp via Page "Just Now"
(+971 50 767 7282). JN: 590 / AED 2,410 = **AED 4.08**, 3 ad sets, CPM 15–17, best-ever AED
1.4–2.4 (Jan–Feb, Jul 2026). Same CPA, jn has 3× the live volume and more conversation-optimised
history; JN's WhatsApp strength is real but is now one ad set. justnow22's 1.67–3.09 is the
cheapest on record but on AED 554 — a test result, not a track record. Quality beyond
"conversation started" is not traceable from Meta; respond.io/Make hold the booking outcome.

**Website.** Only JN has a functioning Lead structure (pixel 614743294720303 / LEAD, exclusions,
pixel audiences): 14 leads @ ~AED 88 with 10 attributed purchases worth AED 2,853 in 7 days. jn's
three attempts produced 7 leads @ AED 24–154 and were paused. Learning status: every Lead ad set is
learning-limited because 14 leads are split across 5 ad sets.

**Purchase.** Pixel: 118 Purchases / 28d, 100% server-side, from the legacy "Confirmed booking →
Meta Purchase" flow (26 Sep–6 Oct); the "Completed job → Meta Purchase (daily 00:00 Dubai)" flow is
ENABLED, ran successfully on 9 Oct 00:00 but sent 0 (9 jobs found, all already sent by the legacy
flow; 37 pending a `DONE YYYY-MM-DD HH:mm` line; 2 aged out). Attributed: JN 13 purchases/90d with
real values (AED 2,855) — 10 of them from website campaigns in the last week; jn 30/30d but 20 of
them carry a value of AED 1 (legacy test values). Neither account has ever run a Purchase-optimised
ad set with results (jn's 2025 "Sales" campaigns: 2–4 purchases at AED 68–546). → No account
qualifies as a Purchase account today; JN is the natural host for the single Purchase ad set.

**Retargeting.** JN owns the right assets: Confirmed bookings 12mo (calendar, 1,000+), contacts
list (14.9–17.6k), LAL 1% confirmed bookings, Book Now 14d, Lead 14d, site visitors 30/90d, IG
engagers 365d (31–37k), FB engagers 365d (2.7–3.2k), WhatsApp clickers 180d — and uses them as
exclusions. jn owns the 889-customer calendar list and large engager audiences but uses them
inconsistently (C3-1 includes customers, acquisition ad sets exclude nothing). Both BMs can share
audiences across accounts, so retargeting does not need its own account at this volume.

---

## 6. Funnel mission allocation

| Account | Primary mission | Secondary | Why | Confidence | Decision |
|---|---|---|---|---|---|
| **jn** 1037126214908677 | WHATSAPP ACQUISITION | CUSTOMER REACTIVATION (WhatsApp, customer list) | 3× JN's conversation volume at the same CPA, deepest conversation history, 7 winners live; reactivation already exists (C3-1) | HIGH | RESTRUCTURE (exclusions, consolidation, naming) |
| **JN** 9147325105346647 | WEBSITE ACQUISITION | RETARGETING + the single PURCHASE test ad set | only account with Lead structure, pixel audiences and attributed real-value purchases; retargeting assets live here | HIGH (website) / MEDIUM (purchase) | RESTRUCTURE (consolidate 5 Lead ad sets → 2; keep CTWA winner until twin proves out) |
| **justnow22** 1897980308260660 | CREATIVE TESTING | — | isolated AED account, payment attached, both Pages linked, cheap test history, nothing to pollute | MEDIUM | TEST |
| **JNN** 1304802461392117 | HOLD — reserved for PURCHASE / REVENUE | — | clean empty account; Purchase signal not healthy enough yet (0 completed-job Purchases sent, ~30/week total) | MEDIUM | HOLD |
| **658869122728885** | HOLD / LEGACY | — | personal account mixing Clean House, marketplace, a different WhatsApp number and an unmanaged boost | HIGH | HOLD (stop the boost in A1) |
| **311791788087024** | HOLD / LEGACY | — | unsettled, unreadable | HIGH | HOLD (owner: settle or close) |
| **JustNow44** 2820299204977421 | DEFERRED | — | unreadable from here; needs owner export | — | HOLD until read |
| **1679026507158086** | OWNER-PROTECTED | — | excluded by owner | — | NO ACTION |
| 14 Read-Only USD accounts, 3 disabled, 1 closed | UNUSED / NO ROLE | — | system-created or disabled, zero spend | HIGH | none |
| Clean House ×2, UAE Property | OUT OF SCOPE | — | other businesses | — | none |

Not every account must be used: of 32, **three deserve investment** (jn, JN, justnow22 at test
scale), one is held in reserve (JNN), the rest get no spend.

---

## 7. Shared dataset strategy — verified

Primary dataset **614743294720303** ("Just Now For Building Cleaning Services CO LLC", BM-B): fired
today from browser and server; 28-day volume PageView 27.2k · ViewContent 8.9k · Contact 2.3k ·
Lead 438 (EMQ 7.8) · Schedule 209 · Purchase 118 (server only); 23.6k server vs 14.2k browser events.

| Account | Ad sets optimising on a pixel | Dataset | OK? |
|---|---|---|---|
| JN | C1-1, C2-1, C2-2, C2-3, Website Lead video (LEAD) | 614743294720303 | ✓ |
| jn | Book Now Lead ×3 (paused), 1 CONTENT_VIEW ad set | 614743294720303 | ✓ |
| justnow22 | none | — | n/a |
| 658869122728885 | none (LPV boost, no event) | — | should be LEAD on 614743294720303 if it ever runs again |
| Make CAPI (Purchase) | — | 614743294720303 | ✓ |

Hygiene: 37 datasets exist across the two BMs. "…API Event Data" 2173595413219328 (created 20 Sep)
has never fired — orphan, do not point anything at it. Pixels 706289834670044 and 1400794378663670
still received browser events on 30 Sep → check the website tag for leftover pixel IDs. **Keep one
dataset for all missions; do not create a Purchase-only dataset.**

---

## 8. Purchase / Revenue readiness

| Check | Finding |
|---|---|
| Current Purchase flow | Make scenario 6529499 "Completed job → Meta Purchase (daily 00:00 Asia/Dubai)", ENABLED (cutover approved 6–7 Oct); legacy hourly "Confirmed booking → Meta Purchase" is off |
| Completed-service volume | 118 Purchases / 28d on the pixel, all legacy flow; new flow: 0 sent (9 Oct run: 9 found / 9 already sent / **37 pending finalisation** / 2 aged out) |
| Latest Purchase timestamp | 6 Oct 2026 ≈ 22:00 Dubai (legacy flow) |
| event_id | calendar event id → dedup ✓ (plus Make ledger states SENT/LEGACY/UNCERTAIN) |
| value / currency | AED, job price (incl. "final price" line) ✓ |
| action_source | `chat` ✓ |
| user_data | ph, fn, ln, ct, country=ae, external_id=phone ✓ ; EMQ for Purchase not yet reported by the API |
| DONE pipeline | depends on staff adding `DONE YYYY-MM-DD HH:mm` to the calendar entry within 7 days; 7 Oct run failed (Calendar eventTypes bug, fixed 8 Oct) |
| Attribution caveat | event_time = completion time; jobs completed >7 days after the ad click fall outside the 7-day click window |

**Verdict: volume is low → ONE consolidated Purchase ad set (in JN) after the new flow has sent
real completed-job Purchases for 7 consecutive days. Do not fragment. Dedicated Purchase account
(JNN) only after ≥50 Purchases/week with values for 4 straight weeks.**

---

## 9. Overlap analysis

| Pair | Overlap | Evidence | Business impact |
|---|---|---|---|
| **jn vs JN** | **HIGH** | same Pages (Just Now + CO LLC), same IG justnow.life.ae, identical creative set uploaded 30 Sep to both, same WhatsApp line, same pixel, same customer list (calendar bookings / contacts csv), same geos (Dubai–Sharjah–Ajman pins, "UAE excl. Abu Dhabi"), same interest stack (Jewelry / Online shopping / Luxury goods / Engaged Shoppers), both bidding CONVERSATIONS → WhatsApp at the same time (JN AED 80/day vs jn AED 270/day) | the two accounts bid against each other for the same Sharjah/Dubai women 25–65; CTWA CPM rose from AED 13–15 (Aug) to 15–31 (Sep–Oct); learning split across 16 ad sets |
| jn vs 658869122728885 | MEDIUM | same Sharjah r10mi pin, same interests, same Pages; LPV boost to book-now | duplicate traffic buying with no event optimisation |
| JN vs 658869122728885 | MEDIUM | both send Sharjah traffic to justnow.life/book-now (JN optimises LEAD, personal account optimises LPV) | the boost steals impressions from the Lead ad set and reports nothing |
| jn vs justnow22 | LOW (dormant) | same Pages, same interests, no live spend in justnow22 | none while dormant; would be HIGH if justnow22 re-launched CTWA prospecting |
| JN C1 vs JN C2 | LOW–MEDIUM | C1 excludes Book Now 14d / Lead 14d / bookings; C2 targets them | correct separation |
| Within jn | MEDIUM | 6 active ad sets centred on Sharjah within 10–12 mi; no customer exclusions on 10 | self-competition and re-acquiring existing customers |

---

## 10. Budget / spend quality (no pauses yet)

**GOOD SPEND (clear mission, in band):** jn — A Sharjah (AED 1,982/30d), Copy A, New Sales Ad Set,
Copy 2, Copy B, B Arabic, TEST E, C, D (AED 6.4k/30d → 1,692 conversations @ 3.8); JN — CTWA
winner (AED 2,096 → 515 @ 4.07), C1-1 Broad (AED 589 → 9 leads, 6 purchases AED 1,776), C2-1/C2-3
(AED 556 → 5 leads, 4 purchases AED 1,077).

**WASTED / QUESTIONABLE:**
1. Duplicate CTWA acquisition in JN (AED ~80/day) against jn's identical audiences — overlapping
   acquisition.
2. 658869122728885 "[10/3/2026] Promoting book-now" — AED 15/day unmanaged IG-app traffic boost,
   no conversion event, competes with JN C1.
3. jn Reach/awareness: "[9/20/2026] Promoting local business" ×2 (AED 139), "New Awareness" ad sets
   Jun–Sep 2026 (≈ AED 3.2k at CTR 0.17–0.27%, frequency up to 3.4) — traffic/awareness with no
   strategic role.
4. jn LPV boosts "Watch the grease melt" ×2 (AED 231) and JN IG boost "Same kitchen" (AED 304 →
   2,542 clicks, nothing downstream).
5. Acquisition hitting existing customers: 10 of 13 jn ad sets and JN's CTWA winner have no customer
   exclusion while customer lists (889 / 14.9k) exist in both accounts.
6. Learning-limited fragmentation: JN's 14 leads across 5 Lead ad sets (C2-2 AED 15 → 0); JN CTWA
   ad set …470220312 (AED 14 → 0); jn C3-4 Broad (AED 373 → 61 @ 6.11, CPM 30.6).
7. Duplicate campaigns/ad sets: ~45 "New Sales Campaign" in JN, dozens in jn; duplicate audiences.

---

## 11. Winners to protect (no edits until A2/A3 twins prove out)

| Account | Ad set (id) | 30d | 7d |
|---|---|---|---|
| jn | A - Sharjah city families 25-60 [5158] (120249855372950073) | 510 conv @3.89 | 177 @3.77 |
| jn | New Sales Ad Set - Copy A (120249855745520073) | 309 @3.49 | 117 @3.81 |
| jn | New Sales Ad Set, 20 Sep (120249855697040073) | 243 @3.43 | 67 @2.88 |
| jn | New Sales Ad Set - Copy 2 (120249855757070073) | 294 @4.28 | 32 @2.91 |
| jn | New Sales Ad Set - Copy B (120249855813520073) | 113 @3.81 | 64 @3.46 |
| jn | B - Arabic speakers Sharjah + Ajman (120249855378300073) | 85 @3.96 | 26 @3.48 |
| jn | TEST 24 Sep - E - Dubai women (120249947966990073) | 63 @3.63 | 25 @4.44 |
| JN | New Sales Ad Set - Copy, Copy 2 campaign (120251948470210312) | 515 @4.07 | 162 @3.81 |
| JN | C1-1 Broad 25+ (120252107075750312) | 9 leads @65, 6 purchases AED 1,776 | same |

---

## 12. Final output — every account

**TOTAL AD ACCOUNTS FOUND: 32** (29 JustNow-related + 3 other-brand accounts visible through the
same access).

**ACCOUNT 1** — Name: jn · ID: 1037126214908677 · Current role: WhatsApp acquisition (13 live ad
sets) + stray boosts + paused website-lead tests · Historical strength: conversations at AED 2.5–4.3
over 18 months · Best optimization: CONVERSATIONS → WhatsApp · Best ad sets: A Sharjah, Copy A, New
Sales Ad Set (20 Sep), Copy 2, Copy B, B Arabic, TEST E · Weaknesses: no customer exclusions, 100+
duplicate campaigns, boosts/awareness without role, C3-4 expensive · Recommended mission: WHATSAPP
SALES (+ customer reactivation) · Action: RESTRUCTURE — add exclusions, consolidate, adopt WA naming,
absorb JN's CTWA winner via a twin.

**ACCOUNT 2** — Name: JN · ID: 9147325105346647 · Current role: website Leads (C1/C2) + one CTWA
campaign + a video test · Historical strength: CTWA AED 1.4–3.5 (Jan–Aug 2026); website Leads with
attributed purchases (Oct 2026) · Best optimization: OFFSITE_CONVERSIONS/LEAD on 614743294720303;
CONVERSATIONS · Best ad sets: C1-1 Broad, CTWA "Copy", C2-1, C2-3 · Weaknesses: Lead budget split 5
ways (learning-limited), duplicate audiences, 45 legacy "New Sales" campaigns, CTWA winner without
exclusions · Recommended mission: WEBSITE BOOKINGS (+ retargeting, + single Purchase test ad set) ·
Action: RESTRUCTURE — 2 Lead ad sets, WB naming, Purchase ad set in A4, hand CTWA to jn after twin.

**ACCOUNT 3** — Name: justnow22 · ID: 1897980308260660 · Current role: dormant · Historical
strength: CTWA tests @ AED 1.67–3.09 (Feb 2026) · Best optimization: CONVERSATIONS (test scale) ·
Best ad sets: "New Sales Campaign ind" ad sets (Feb 2026) · Weaknesses: tiny data, no pixel, no
audiences · Recommended mission: CREATIVE TESTING · Action: TEST — small daily budgets, every test
tagged CT, winners rebuilt in jn/JN.

**ACCOUNT 4** — Name: (none) · ID: 658869122728885 · Current role: personal boost account, live
AED 15/day traffic boost · Historical strength: none relevant (Clean House, marketplace) · Best
optimization: none · Best ad sets: none · Weaknesses: no business, mixed brands, old WhatsApp number
…7949 in legacy ads, boost overlaps JN C1 · Recommended mission: HOLD / LEGACY · Action: HOLD; stop
the boost in A1; never resume legacy ads.

**ACCOUNT 5** — Name: JNN · ID: 1304802461392117 · Current role: none · Historical strength: none ·
Recommended mission: HOLD, reserved for PURCHASE / REVENUE when the completed-job flow sustains ≥50
Purchases/week · Action: HOLD.

**ACCOUNT 6** — ID: 1679026507158086 · OWNER-PROTECTED — EXCLUDED FROM EXECUTION (zero spend,
read only).

**ACCOUNT 7** — Name: JustNow44 · ID: 2820299204977421 · Current role: unknown (unreadable) ·
Historical strength: unknown; Reel tests were rebuilt from it into jn · Recommended mission:
DEFERRED → owner to export history · Action: HOLD, no rename.

**ACCOUNT 8** — Name: Just Now · ID: 311791788087024 · Current role: UNSETTLED · Recommended
mission: HOLD / LEGACY · Action: settle or close; rename only after it is readable.

**ACCOUNTS 9–22** — the 14 queryable "(Read-Only)" USD accounts (856564090492076,
1720532878634926, 996359675586790, 1553685189104802, 1504118357546048, 1499748364956496,
741583665672939, 1373981191582615, 3052111794970919, 815346134471737, 1583312996307869,
1340906084205111, 1909989033058072, 1007292425694931): system-created by WhatsApp Business /
Shopify / Instagram integrations, zero lifetime spend, mostly no payment method · Mission: UNUSED /
NO ROLE · Action: none (do not add payment methods; leave as integration shells).

**ACCOUNTS 23–25** — MCP-disabled read-only shells 1524467415226667, 1852789671986208,
1843769482985909: UNUSED / NO ROLE.

**ACCOUNTS 26–29** — 825353993434985, 2053880215357344, 844053351344804 (DISABLED — flagged),
261191663067349 (CLOSED): HOLD / LEGACY, no action; do not attempt to reactivate.

**ACCOUNTS 30–32** — 245158590746748, 975903583434612 (Clean House), 720576909373045 (UAE
Property): other businesses, out of JustNow scope.

---

## 13. Global mission map

* **BEST WHATSAPP ACCOUNT:** jn — 1037126214908677. WHY: 1,844 conversations/28d at AED 3.97, seven
  live winners, 18 months of conversation learning; JN matches the CPA but with a third of the volume.
* **BEST WEBSITE ACCOUNT:** JN — 9147325105346647. WHY: the only Lead-optimised structure on pixel
  614743294720303 with correct exclusions, pixel audiences, and 10 attributed real-value purchases
  (AED 2,853) in 7 days.
* **BEST PURCHASE / REVENUE ACCOUNT:** none qualifies today. Interim host: JN (one consolidated
  Purchase ad set after pipeline proof). Reserved future home: JNN — 1304802461392117.
* **BEST RETARGETING ACCOUNT:** JN — 9147325105346647 (C2 structure, pixel audiences, exclusions);
  WhatsApp reactivation of past customers runs inside jn.
* **BEST CREATIVE TEST ACCOUNT:** justnow22 — 1897980308260660. WHY: isolated, AED, payment attached,
  both Pages linked, cheap test history, nothing to pollute.
* **ACCOUNTS TO HOLD / RETIRE:** 658869122728885 (hold), 311791788087024 (settle/close),
  JustNow44 2820299204977421 (hold until readable), 3 disabled + 1 closed (retire), 14+3 read-only
  shells (leave), 1679026507158086 (protected).

---

## 14. Ad set migration map

| Current account | Ad set | Current optimization | Recommended funnel | Decision | Why |
|---|---|---|---|---|---|
| jn | A - Sharjah city families 25-60 | CONVERSATIONS | WA prospecting | KEEP | 510 @3.89 |
| jn | Copy A / New Sales Ad Set (20 Sep) / Copy 2 / Copy B | CONVERSATIONS | WA prospecting | KEEP (add customer exclusion in A2) | 243–309 conv @3.4–4.3 |
| jn | B Arabic / TEST E / C premium / D inner belt | CONVERSATIONS | WA prospecting | KEEP; fund C and D | CPA 3.2–4.7 |
| jn | C3-1 Women 25+ (targets customers) | CONVERSATIONS | WA reactivation | REBUILD as "WA \| REACTIVATION \| CUSTOMERS 12M" | mislabelled, right idea |
| jn | C3-2 Arabic 25+ | CONVERSATIONS | WA prospecting | KEEP | 39 @4.80 |
| jn | C3-3 LAL customers | CONVERSATIONS | test | KEEP to AED 300 then decide | 11 @5.55 |
| jn | C3-4 Broad 25+ | CONVERSATIONS | — | HOLD (pause in A1) | 61 @6.11, CPM 30.6 |
| jn | Book Now Lead ×3 (paused) | LEAD | website | DO NOT RESUME here | belongs in JN |
| jn | Reach / LPV boosts | REACH / LPV | — | HOLD; future boosts as CT tests in justnow22 | no role |
| JN | New Sales Ad Set - Copy (CTWA winner) | CONVERSATIONS | WA | KEEP now → MOVE to jn via twin, pause after 7-day parity | protect AED 4.07 |
| JN | New Sales Ad Set (motherhood) | CONVERSATIONS | WA | same as above | 75 @4.00 |
| JN | New Sales Ad Set - Copy …470220312 | CONVERSATIONS | — | HOLD (pause in A1) | AED 14, 0 |
| JN | C1-1 Broad 25+ | LEAD | WB prospecting | KEEP (rename WB) | 6 purchases AED 1,776 |
| JN | C2-1 + C2-3 + C2-2 | LEAD | WB retargeting | REBUILD as one "WB \| RETARGETING \| UNION 30D" | exit learning-limited |
| JN | Website Lead \| Video (7 Oct) | LEAD | WB creative test | KEEP 7 days → fold or stop | 0 so far |
| JN | Persona Launch "3 Women decision-makers" | CONVERSATIONS (paused) | WA | REBUILD in jn when a new women segment is needed | 229 @4.98 |
| JN | "abu Dhabi" | CONVERSATIONS (paused) | — | HOLD; resume only if Abu Dhabi is serviceable | 347 @2.46 but excluded since |
| 658869122728885 | [10/3/2026] Promoting book-now | LPV | — | HOLD (stop in A1) | duplicate traffic, no event |
| justnow22 | Feb 2026 CTWA ad sets | CONVERSATIONS (paused) | CT template | HOLD as reference | 1.67–3.09 on AED 554 |

---

## 15. Cross-account waste

1. jn ↔ JN simultaneous CTWA prospecting on identical identities, audiences, geos and creatives.
2. 658869122728885 traffic boost to /book-now while JN C1 buys Leads on the same page.
3. Customer acquisition without customer exclusions in both production accounts.
4. Awareness/Reach and LPV boosts with no downstream event (jn ≈ AED 3.6k in 90d; JN AED 1.2k).
5. Learning fragmentation: 5 Lead ad sets for 14 leads (JN); 20+ "New Sales" ad sets at AED 5–12
   in Aug–Sep (JN); "Sales - Copy" clusters at AED 9–18 (jn).
6. Duplicate custom audiences (JN ×3 pairs on 30 Sep; jn "365 - sep 2026" ×2) and ~60 dead Madgicx
   audiences in jn.
7. Legacy campaigns kept ACTIVE by status although ended (658869122728885, justnow22) — cosmetic,
   but misleading in Ads Manager.

---

## 16. Final recommended structure

```
jn               1037126214908677 → WHATSAPP SALES (+ customer reactivation)
JN               9147325105346647 → WEBSITE BOOKINGS (+ retargeting, + single Purchase test ad set)
justnow22        1897980308260660 → CREATIVE TESTING
JNN              1304802461392117 → HOLD (reserved: PURCHASE / REVENUE when signal is healthy)
658869122728885                   → HOLD / LEGACY
311791788087024  Just Now         → HOLD / LEGACY (unsettled)
2820299204977421 JustNow44        → DEFERRED (unreadable) — no decision, no rename
1679026507158086                  → OWNER-PROTECTED — untouched
14 Read-Only USD + 3 MCP-disabled shells → UNUSED / NO ROLE
3 DISABLED + 1 CLOSED             → retire
Clean House ×2, UAE Property      → out of scope
```

---

## 17. Execution plan (prepared, NOT executed)

**A0 — Preserve winners (day 0).** No edits to the 9 winners in §11. Record 7-day baselines (CPA,
CPM, frequency). Freeze budgets.

**A1 — Remove proven overlap / waste (after write approval).**
Pause: 658869122728885 "[10/3/2026] Promoting book-now" (120249701767850032); JN ad set
120251948470220312 (0 results); jn C3-4 Broad (120250020898360073). Archive: JN "[OLD - DELETE]"
campaigns and zero-spend drafts; jn "Sales - Copy"/"New Sales Campaign - Copy" clusters of 5–14
Sep. Delete duplicate audiences (JN: the 09:59 copies of Website visitors 30d / Lead 14d / Book
Now 14d and one LAL Book Now; jn: one "365 - sep 2026"). Expected saving ≈ AED 30/day + cleaner
learning.

**A2 — WhatsApp mission (jn).** (1) Add exclusions "jn - Customers Jan 2025–Sep 2026 (889)" and the
shared "JN - Confirmed bookings 12mo (calendar)" to all 10 unexcluded acquisition ad sets. (2) Build
a twin of JN's CTWA winner in jn: `WA | PROSPECTING | SHJ | HOME-MOVERS` (interests Furniture / Home
improvement / Modern furniture / Recently moved + Engaged Shoppers, Sharjah r10mi, 18–65, Advantage
audience on, same creatives). (3) Run 7 days side by side; when the twin is within ±15% of AED 4.07,
move the AED 80/day and pause JN's CTWA campaign. (4) Rebuild C3-1 as
`WA | REACTIVATION | CUSTOMERS 12M` (customer list only, exclude Lead 14d). (5) Rename the 3 active
jn campaigns to the WA convention (renaming does not reset learning).

**A3 — Website mission (JN).** Consolidate 5 Lead ad sets → 2: `WB | PROSPECTING | DXB+SHJ+AJM |
BOOKING` (C1-1 as is, fold the Studio video in as an extra ad) and `WB | RETARGETING | UNION 30D |
BOOKING` (Book Now 14d ∪ site visitors 30d ∪ IG/FB engagers 365d; exclude bookings 12mo + Lead 14d).
Budgets AED 84+70+60 → ≈ AED 150/day prospecting + AED 60/day retargeting. Keep pixel
614743294720303 / LEAD until the Purchase ad set exists.

**A4 — Purchase mission.** Gate: the "Completed job → Meta Purchase" flow has sent real Purchases
with AED values on 7 consecutive days (clear the 37 pending DONE lines first) and Events Manager
shows an EMQ for Purchase. Then launch exactly one ad set in JN: `PUR | PROSPECTING | UAE |
COMPLETED SERVICE` — campaign objective Sales, optimisation Purchase on 614743294720303, Advantage+
audience, UAE excl. Abu Dhabi, AED ≥150/day, exclusions as C1-1, no second Purchase ad set anywhere.
Graduate to JNN (rename it PURCHASE / REVENUE) only after ≥50 Purchases/week for 4 weeks.

**A5 — Retargeting.** Lives in A3 (JN) and A2 step 4 (jn reactivation). Share the customer-list and
pixel audiences across both BMs so one definition serves both accounts.

**A6 — Budget reallocation.** JN CTWA AED 80/day → jn winners (C and D first, they are under-funded
at CPA 2–3). 658869122728885 AED 15/day → 0. jn Reach/LPV boost money → justnow22 CT tests (cap
AED 50/day). Keep total CTWA where blended CPA stays ≤ AED 4.5.

**A7 — Observation / scaling.** Weekly: CPA/CPM/frequency per mission; conversation→booking rate from
respond.io/Make calendar; Purchase events vs completed jobs. Scale a winner +20%/week while CPA
holds; stop any test at AED 300 without a result. Confirm overlap relief: CTWA CPM should drift
back toward AED 13–15.

---

## 18. Mission-based account naming

### 18.1 Final account label table (every account)

| Current account name | Account ID | Current main use | Recommended mission | New account name | Why this mission | Confidence | Rename |
|---|---|---|---|---|---|---|---|
| jn | 1037126214908677 | WhatsApp acquisition | WHATSAPP SALES | **JUSTNOW \| WHATSAPP SALES \| jn** | largest, cheapest-at-scale conversation engine | HIGH | YES |
| JN | 9147325105346647 | website Leads + CTWA | WEBSITE BOOKINGS | **JUSTNOW \| WEBSITE BOOKINGS \| JN** | only Lead structure; attributed real purchases; retargeting assets | HIGH | YES |
| justnow22 | 1897980308260660 | dormant | CREATIVE TESTING | **JUSTNOW \| CREATIVE TESTING \| justnow22** | isolated sandbox with cheap test history | MEDIUM | YES |
| JNN | 1304802461392117 | none | HOLD (reserved Purchase/Revenue) | **JUSTNOW \| HOLD / LEGACY \| JNN** | Purchase signal not healthy enough to earn the Purchase label yet | MEDIUM | YES |
| (unnamed) | 658869122728885 | personal boosts | HOLD / LEGACY | **JUSTNOW \| HOLD / LEGACY \| Personal** | mixed brands, old number, unmanaged boost | HIGH | YES |
| Just Now | 311791788087024 | unsettled | HOLD / LEGACY | **JUSTNOW \| HOLD / LEGACY \| Just Now** | unpaid balance, unreadable | HIGH | YES — conditional (after it becomes writable/settled) |
| JustNow44 | 2820299204977421 | unknown | DEFERRED | — (keep "JustNow44") | no evidence readable | — | NO (pending) |
| (unnamed) | 1679026507158086 | — | OWNER-PROTECTED | — | excluded by owner | — | **NEVER** |
| 14 "(Read-Only)" USD accounts (§12, accounts 9–22) | see §1 | none | UNUSED / NO ROLE | — | integration shells, zero spend | HIGH | NO |
| 1524467415226667 · 1852789671986208 · 1843769482985909 | | none | UNUSED / NO ROLE | — | MCP-disabled shells | HIGH | NO |
| 825353993434985 · 2053880215357344 · 844053351344804 | | disabled | HOLD / LEGACY | — | flagged by Meta, cannot deliver | HIGH | NO |
| 261191663067349 | | closed | HOLD / LEGACY | — | closed | HIGH | NO |
| 245158590746748 · 975903583434612 · 720576909373045 | | other brands | OUT OF SCOPE | — | not JustNow | — | NO |

### 18.2 Final map — ACCOUNT ID → OLD NAME → NEW NAME → MISSION

```
1037126214908677 → jn              → JUSTNOW | WHATSAPP SALES | jn            → WHATSAPP ACQUISITION (+ reactivation)
9147325105346647 → JN              → JUSTNOW | WEBSITE BOOKINGS | JN          → WEBSITE ACQUISITION (+ retargeting, + Purchase test)
1897980308260660 → justnow22       → JUSTNOW | CREATIVE TESTING | justnow22   → CREATIVE TESTING
1304802461392117 → JNN             → JUSTNOW | HOLD / LEGACY | JNN            → HOLD (reserved PURCHASE / REVENUE)
658869122728885  → (unnamed)       → JUSTNOW | HOLD / LEGACY | Personal       → HOLD / LEGACY
311791788087024  → Just Now        → JUSTNOW | HOLD / LEGACY | Just Now       → HOLD / LEGACY (conditional on billing)
2820299204977421 → JustNow44       → (unchanged)                              → DEFERRED
1679026507158086 → (unnamed)       → (never renamed)                          → OWNER-PROTECTED
all others       → (unchanged)                                                → UNUSED / NO ROLE / OUT OF SCOPE
```

### 18.3 Internal naming convention (future builds only; winners keep their names until moved)

```
JUSTNOW | WHATSAPP SALES | jn
  Campaign: WA | PROSPECTING | UAE | DEEP CLEANING
            WA | REACTIVATION | CUSTOMERS 12M | DEEP CLEANING
  Ad set:   WA | BROAD | SHJ | CONVERSATIONS
            WA | PARENTS | SHJ | CONVERSATIONS
            WA | HOME-MOVERS | SHJ | CONVERSATIONS
            WA | ARABIC | SHJ+AJM | CONVERSATIONS
            WA | WOMEN | DXB | CONVERSATIONS
            WA | CUSTOMERS 12M | UAE | REACTIVATION
  Ads:      REEL | KITCHEN | GREASE-MELT | V01 · REEL | CABINETS | INSIDE-STEAM | V02 ·
            VIDEO | KITCHEN | SAME-KITCHEN | V03 · TESTIMONIAL | KITCHEN | STUDIO-FEEDBACK | V01

JUSTNOW | WEBSITE BOOKINGS | JN
  Campaign: WB | PROSPECTING | UAE | DEEP CLEANING
            WB | RETARGETING | UAE | DEEP CLEANING
            PUR | PROSPECTING | UAE | COMPLETED SERVICE        (A4, one ad set only)
  Ad set:   WB | BROAD | DXB+SHJ+AJM | BOOKING
            WB | RETARGETING | UNION 30D | BOOKING
            PUR | BROAD | UAE | PURCHASE
  Ads:      VIDEO | KITCHEN | BOOK-ONLINE | V01 · REEL | KITCHEN | FINISH-YOUR-BOOKING | V01

JUSTNOW | CREATIVE TESTING | justnow22
  Campaign: CT | <YYYY-MM> | <HYPOTHESIS>            e.g. CT | 2026-10 | ARABIC-HOOKS
  Ad set:   CT | <AUDIENCE> | <GEO> | <GOAL>          e.g. CT | WOMEN 25-55 | DXB | CONVERSATIONS
  Ads:      CREATIVE TYPE | SERVICE | HOOK | VERSION
```

Rename only the 3 active jn campaigns and 4 active JN campaigns to the convention (safe: renaming
never resets learning); leave paused/legacy items untouched to preserve history references.

### 18.4 Rename batch — prepared, NOT executed

Write enforcement is unverified, so this is the exact batch to show the owner once it is verified.
Each line is one Marketing API call `POST /act_<ID>` with `{"name": "<NEW NAME>"}` (equivalent to
Business Settings → Ad accounts → rename). No tool in this session is permitted to send them now.

```
POST /act_1037126214908677   name="JUSTNOW | WHATSAPP SALES | jn"
POST /act_9147325105346647   name="JUSTNOW | WEBSITE BOOKINGS | JN"
POST /act_1897980308260660   name="JUSTNOW | CREATIVE TESTING | justnow22"
POST /act_1304802461392117   name="JUSTNOW | HOLD / LEGACY | JNN"
POST /act_658869122728885    name="JUSTNOW | HOLD / LEGACY | Personal"
POST /act_311791788087024    name="JUSTNOW | HOLD / LEGACY | Just Now"      # conditional: account must be settled/writable
--  2820299204977421 JustNow44: no rename until its history is read
--  1679026507158086: NEVER
```

Read-back verification to run after any approved rename (`GET /act_<ID>?fields=name`):

| ACCOUNT ID | EXPECTED NAME | ACTUAL NAME | MISSION | RENAME VERIFIED |
|---|---|---|---|---|
| 1037126214908677 | JUSTNOW \| WHATSAPP SALES \| jn | — | WHATSAPP SALES | NO (not executed) |
| 9147325105346647 | JUSTNOW \| WEBSITE BOOKINGS \| JN | — | WEBSITE BOOKINGS | NO (not executed) |
| 1897980308260660 | JUSTNOW \| CREATIVE TESTING \| justnow22 | — | CREATIVE TESTING | NO (not executed) |
| 1304802461392117 | JUSTNOW \| HOLD / LEGACY \| JNN | — | HOLD (reserved Purchase) | NO (not executed) |
| 658869122728885 | JUSTNOW \| HOLD / LEGACY \| Personal | — | HOLD / LEGACY | NO (not executed) |
| 311791788087024 | JUSTNOW \| HOLD / LEGACY \| Just Now | — | HOLD / LEGACY | NO (not executed) |

### 18.5 META ACCOUNT ORGANIZATION MAP

```
WHATSAPP SALES:       Account ID 1037126214908677 · New name: JUSTNOW | WHATSAPP SALES | jn
WEBSITE BOOKINGS:     Account ID 9147325105346647 · New name: JUSTNOW | WEBSITE BOOKINGS | JN
PURCHASE / REVENUE:   no account qualifies yet — single Purchase ad set inside JN (A4);
                      reserved: 1304802461392117 (JNN), to be renamed when the signal is healthy
RETARGETING:          inside 9147325105346647 (JN) — no separate account at current volume
CREATIVE TESTING:     Account ID 1897980308260660 · New name: JUSTNOW | CREATIVE TESTING | justnow22
HOLD / LEGACY:        1304802461392117 → JUSTNOW | HOLD / LEGACY | JNN
                      658869122728885  → JUSTNOW | HOLD / LEGACY | Personal
                      311791788087024  → JUSTNOW | HOLD / LEGACY | Just Now (conditional)
                      2820299204977421 JustNow44 → unchanged until readable
                      825353993434985, 2053880215357344, 844053351344804 (disabled), 261191663067349 (closed) → unchanged
UNUSED / NO ROLE:     856564090492076, 1720532878634926, 996359675586790, 1553685189104802,
                      1504118357546048, 1499748364956496, 741583665672939, 1373981191582615,
                      3052111794970919, 815346134471737, 1583312996307869, 1340906084205111,
                      1909989033058072, 1007292425694931, 1524467415226667, 1852789671986208,
                      1843769482985909
OUT OF SCOPE:         245158590746748, 975903583434612 (Clean House), 720576909373045 (UAE Property)
PROTECTED:            1679026507158086 — never renamed, never touched

ACCOUNT RENAMES PLANNED:   6  (5 ready + 1 conditional)
ACCOUNT RENAMES EXECUTED:  0
ACCOUNT RENAMES VERIFIED:  0
```

---

## 19. Permission safety

```
WRITE APPROVAL ENFORCEMENT: NOT VERIFIED
PRODUCTION WRITES:          0   (no pause, no budget edit, no campaign creation, no optimisation change, no rename)
READY FOR EXECUTION:        NO
```

Next step when enforcement is verified: show the owner §18.4, obtain approval per line, execute,
then run the read-back table in §18.4 and fill ACTUAL NAME / RENAME VERIFIED.
