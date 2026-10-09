# META EXECUTION LOG — Batch 1 (Wave A1) — 2026-10-09

Owner approval: "start" → write-approval check → "go" (09:50 Dubai). Session permission mode
confirmed `default` before the first write, so every Meta write below was individually approved by the
owner at execution time. Connector draft mode is not enabled on these accounts, so writes hit live
objects directly: creates land **PAUSED**, pauses apply immediately. Each write was read back.

```
PRODUCTION WRITES: 33 succeeded (20 build + 13 go-live) · 2 rejected by Meta (no object created) · ROLLBACKS: 0
```

## 1. Pauses (clear waste) — live, 09:53–09:54 Dubai

| Account | Object | Before (7d) | Write | Read-back | Rollback |
|---|---|---|---|---|---|
| JN 9147325105346647 | ad set 120251948470220312 "New Sales Ad Set - Copy" (women / jewelry, 0 results) | ACTIVE, AED 0 / 0 conv | status=PAUSED | status PAUSED · effective PAUSED · 09:53:58 | set status ACTIVE |
| 658869122728885 | campaign 120249701767850032 "[10/3/2026] Promoting justnow.life/book-now" | ACTIVE, AED 15/day, AED 81 → 339 LPV, 0 leads | status=PAUSED | PAUSED · delivery off · 09:54:02 | set status ACTIVE |
| jn 1037126214908677 | ad set 120250020898360073 "C3-4 \| Broad 25+" | ACTIVE, AED 328.84 → 51 conv @6.45 | status=PAUSED | PAUSED · effective PAUSED · 09:54:06 | set status ACTIVE |

Waste removed: ≈ AED 15/day (boost) + C3-4's share of campaign 120250020646250073's CBO (≈ AED 47/day
over the last 7 days, now redistributed to its siblings C3-1/C3-2/C3-3).

## 2. Builds in jn 1037126214908677 — all PAUSED, 09:55–09:57 Dubai

| Object | ID | Spec | Read-back |
|---|---|---|---|
| Campaign | **120250144447740073** | `WA \| PROSPECTING \| SHJ \| HOME-MOVERS` · OUTCOME_SALES · AUCTION · no campaign budget (ABO) · special categories none | PAUSED · OUTCOME_SALES ✓ |
| Campaign | **120250144448010073** | `WA \| REACTIVATION \| CUSTOMERS 12M \| DEEP CLEANING` · same | PAUSED ✓ |
| Creative | 1854637229249947 | existing post 122098309970001876_1116950464613349 · IG actor 17841461253086330 | created |
| Creative | 2079695029320454 | existing post 122098309970001876_957062783432763 · IG actor | created |
| Creative | 1888705535440387 | existing post 122098309970001876_1559790696189996 · IG actor | created |
| Creative | 1647975023638278 | existing post 122098309970001876_1622838339212041 (AR stove-grease) · IG actor | created |
| Creative | — | existing post …_122278001594006883 ("Customer voice AR/EN") | **REJECTED**: "Post not owned by ad's Page" — the post belongs to a different Page and cannot run with the WhatsApp destination on Page 122098309970001876 |
| Ad set T1 | **120250144454520073** | `WA \| HOME-MOVERS \| SHJ \| CONVERSATIONS` · CONVERSATIONS → WHATSAPP (page 122098309970001876) · IMPRESSIONS · Highest volume · **AED 60/day** · targeting = JN W1 verbatim (18–65; pin 25.256651,55.356445 r10mi; excl. Abu Dhabi; Furniture / Home improvement / Modern furniture / Online shopping / Home / Luxury goods + Engaged Shoppers + Recently moved; Advantage audience ON) + **excluded 120249973174230073** (customers 889) | PAUSED · AED 60 · CONVERSATIONS · WHATSAPP · exclusion present ✓ |
| Ad set T2 | **120250144457040073** | `WA \| MOTHERHOOD \| DXB+SHJ+AJM \| CONVERSATIONS` · same optimisation · **AED 30/day** · targeting = JN W2 verbatim (3 pins; excl. Fujairah + Abu Dhabi; locales 6/24/28; Motherhood / Parenting / Online shopping / Fashion accessories; married) + excluded 120249973174230073 + 120250006502540073 | PAUSED · AED 30 · both exclusions ✓ · see deviation D1 |
| Ad set | **120250144457810073** | `WA \| CUSTOMERS 12M \| UAE \| REACTIVATION` · CONVERSATIONS → WHATSAPP · **AED 20/day** · custom audience 120249973174230073 only · AE excl. Abu Dhabi · Advantage audience OFF · no interests | PAUSED · AED 20 · audience + exclusion ✓ · A+A 0 ✓ |
| Ad | **120250144462130073** | `REEL \| KITCHEN \| STICKY-GREASE \| V01` · T1 · creative 1854637229249947 | PAUSED (review in process) |
| Ad | **120250144462600073** | `REEL \| KITCHEN \| STICKY-GREASE \| V02` · T1 · creative 2079695029320454 | PAUSED (pending review) |
| Ad | **120250144463050073** | `VIDEO \| KITCHEN \| STEAM-PRECISION \| V01` · T2 · creative 1888705535440387 | PAUSED (review in process) |
| Ad | **120250144463650073** | `VIDEO \| STOVE-GREASE \| AR \| REACTIVATION V01` · reactivation · creative 1647975023638278 | PAUSED (pending review) |
| Ad | — | `VIDEO \| CUSTOMER-VOICE \| AR-EN \| REACTIVATION V01` · reuse of jn creative 1071526055876335 | **REJECTED**: "Replies optimization only with ads driving traffic to Messenger" — that creative's CTA is not WhatsApp-compatible; rebuild later from the video with a WhatsApp CTA (new post, no carried engagement) if the owner wants a second reactivation ad |

Previews (Facebook Feed) rendered the original posts: T1 V01, T1 V02, T2 V01 — links in the chat report.

## 3. Build in JN 9147325105346647 — PAUSED, 09:56–09:57 Dubai

| Object | ID | Spec | Read-back |
|---|---|---|---|
| Ad set | **120252226500410312** | `WB \| RETARGETING \| UNION 30D \| BOOKING` under campaign 120252107080200312 (CBO AED 70, no ad-set budget) · OFFSITE_CONVERSIONS · pixel 614743294720303 event LEAD · WEBSITE · attribution 7d click / 1d view · audiences 120252107062990312 ∪ 120252107065720312 ∪ 120251888118190312 ∪ 120251888139630312 · excluded 120251936408430312 + 120252107064340312 · pins (25.09104,55.265808) + (25.344491,55.422363) r10mi · excl. Abu Dhabi · 20–65 · Advantage audience OFF | PAUSED · LEAD on 614743294720303 ✓ · 4 audiences + 2 exclusions ✓ · A+A 0 ✓ |
| Ad | **120252226507840312** | `VIDEO \| STOVE-GREASE \| FINISH-YOUR-BOOKING \| AR \| V01` · creative 800898536451029 (C2-1-c) | PAUSED (pending review) |
| Ad | **120252226508320312** | `VIDEO \| SAME-KITCHEN \| BEFORE-AFTER \| V01` · creative 1765887427985234 (C2-3-a) | PAUSED (review in process) |
| Ad | **120252226511090312** | `AD \| RETARGETING \| C2-2-d \| V01` · creative 1132547542778119 (C2-2-d) | PAUSED (pending review) |

Nothing else in JN changed: campaign 120251948470120312 (W1/W2) still ACTIVE; C2-1 / C2-2 / C2-3 still
ACTIVE until the union ad set goes live.

## 4. Deviations found in read-back

* **D1 — T2 age.** JN W2 ran 25–65 as a hard range (its Advantage audience individual setting kept
  age fixed). In T2, Meta stored 25–65 as a suggestion under Advantage+ audience, so the effective range
  reads 18–65. Options: accept (Advantage audience ON is how T1/W1 run anyway) or set
  `targeting_automation.advantage_audience=0` on T2 before go-live to hard-cap 25–65.
* **D2 — placements.** jn's Advantage+ placements include Audience Network (classic, rewarded video);
  JN's W1/W2 did not. This matches jn's own CTWA winners (e.g. C3-x), so it is left as is; if the twins'
  CPM/quality diverge from W1, exclude Audience Network as the first fix.
* **D3 — reactivation has one ad instead of two** (customer-voice creative rejected twice, see §2).

## 5. Rollback (exact)

* Pauses: `status=ACTIVE` on 120251948470220312 · 120249701767850032 · 120250020898360073.
* New objects: they are PAUSED and have never delivered. To remove: `status=DELETED` on campaigns
  120250144447740073 and 120250144448010073 (cascades), and on ad set 120252226500410312 (its 3 ads
  cascade). Creatives 1854637229249947 / 2079695029320454 / 1888705535440387 / 1647975023638278 can stay.

## 6. Go-live — NOT executed; separate approval

| Option | Writes | New daily spend | Then |
|---|---|---|---|
| A — twins | activate campaign 120250144447740073, ad sets 120250144454520073 + 120250144457040073, ads 120250144462130073 / 120250144462600073 / 120250144463050073 | +AED 90/day in jn (JN W1/W2 keep running until the §2.3 scorecard passes) | 7-day scorecard; on pass pause JN campaign 120251948470120312 |
| B — reactivation | activate campaign 120250144448010073, ad set 120250144457810073, ad 120250144463650073 | +AED 20/day | pause jn C3-1 120250020902640073 after 7 days |
| C — JN retargeting union | activate ad set 120252226500410312 + its 3 ads; pause C2-1 120252107098030312, C2-2 120252107107740312, C2-3 120252107111220312 (shared CBO, so no new spend) | 0 | 10-day scorecard; fail → unpause C2-1 and C2-3 |

Ads still in Meta review will start delivering only once approved, whichever option is chosen.

## 7. Go-live executed — 10:12 Dubai — owner: "APPROVE GO-LIVE: A + C"

Owner's conditions: T1/T2 exactly as built (no T2 hard-cap, Advantage audience behaviour unchanged so
the test moves account/mission only); JN winners keep running; 7 days or the §2.3 thresholds; JN winner
paused only after the twin scorecard passes. C: union live, C2-1/2/3 paused at the same time, CBO
unchanged. B: reactivation stays PAUSED until the second creative is resolved or the single-ad version
is chosen deliberately.

13 writes, each approved by the owner at execution time; read back 10:13 Dubai.

| Item | ID | Write | Read-back |
|---|---|---|---|
| T1 | 120250144454520073 | activate | **ACTIVE** / effective ACTIVE · AED 60/day · 10:12:31 |
| T2 | 120250144457040073 | activate | **ACTIVE** / effective ACTIVE · AED 30/day · 10:12:34 |
| jn twins campaign | 120250144447740073 | activate | ACTIVE · 10:12:09 |
| T1 ads V01 / V02 | 120250144462130073 / 120250144462600073 | activate | ACTIVE · effective PENDING_REVIEW |
| T2 ad V01 | 120250144463050073 | activate | ACTIVE · effective PENDING_REVIEW |
| JN RETARGETING UNION | 120252226500410312 | activate | **ACTIVE** / effective ACTIVE · 10:12:54 |
| union ads | 120252226507840312 / 120252226508320312 / 120252226511090312 | activate | ACTIVE · effective IN_PROCESS / IN_PROCESS / PENDING_REVIEW |
| C2-1 | 120252107098030312 | status=PAUSED | **PAUSED** / PAUSED · 10:12:52 |
| C2-2 | 120252107107740312 | status=PAUSED | **PAUSED** / PAUSED · 10:12:54 |
| C2-3 | 120252107111220312 | status=PAUSED | **PAUSED** / PAUSED · 10:12:57 |
| JN retargeting campaign | 120252107080200312 | none | ACTIVE · CBO **AED 70/day unchanged** |
| OLD JN WINNERS | campaign 120251948470120312 · W1 120251948470210312 · W2 120251948470250312 | none | **STILL ACTIVE — YES** (CBO AED 80/day) |
| Reactivation (B) | 120250144448010073 / 120250144457810073 / 120250144463650073 | none | PAUSED / PAUSED / PAUSED |

```
NEW DAILY SPEND ADDED:        AED 90/day maximum from A (T1 60 + T2 30), delivery starts once the ads clear review
RETARGETING NET NEW SPEND:    AED 0 (same AED 70 CBO; the union ad set replaces C2-1/2/3)
OLD JN WINNERS:               STILL ACTIVE — YES
```

Known gap: until the three union ads clear review, campaign 120252107080200312 has no delivering ad
set (minutes to 24 h). If review rejects an ad, the first fix is to re-attach the same creative to a
new ad, not to unpause C2-x.

Observation windows: twins 9–16 Oct (T1 pass ≤ AED 4.70 with ≥50 conversations and booking rate ≥ W1's;
T2 pass ≤ AED 4.60 with ≥25); union 9–19 Oct (pass ≥5 leads ≤ AED 100 each or ≥3 purchases; fail <3
leads after AED 500). Monitoring: read-only check this afternoon for review approval and first delivery,
then a daily 09:22 Dubai scorecard check-in into this session; no further write without the owner's
approval.

## 8. Continue-execution pass — 10:20–10:50 Dubai (owner brief "CONTINUE EXECUTION, CLEANUP & MIGRATION" + "WEEKEND WEIGHTING")

### M1 — new cells
All six new ads passed review (effective_status ACTIVE at 10:20); delivery "pending / preparing"; spend 0
at read time. T1 120250144454520073 and T2 120250144457040073 ACTIVE at AED 60 / 30; union
120252226500410312 ACTIVE under the AED 70 CBO. No error, no repair needed.

### M2 — remaining JN/jn overlap (fresh read of all delivering ad sets)
JN delivering: W1 120251948470210312 (CTWA, 7d AED 618 → 162 @3.81), W2 120251948470250312 (AED 22 → 8),
C1-1 120252107075750312 (website Lead, AED 507 → 9 @56), union, and the Studio-feedback test ad set
120252195374160312 (website Lead, AED 72.64 → 0 leads, CPM 41.75, own campaign AED 60/day).
jn delivering: T1, T2, C3-1/2/3, TEST E, Copy A/B/2, New Sales Ad Set, A/B/C/D — all CONVERSATIONS →
WhatsApp (three of them multi-destination IG-direct/Messenger/WhatsApp), Sharjah/Dubai/Ajman pins.

| Pair | Decision |
|---|---|
| W1 (JN) ↔ T1 + jn Sharjah cluster (A, Copy A, Copy B) | **WAIT FOR TWIN TEST** — pause W1 only after T1 parity |
| W2 (JN) ↔ T2 (+ Copy A parents) | **WAIT FOR TWIN TEST** |
| C1-1 (JN website) ↔ jn | no live jn website prospecting → **KEEP JN**, no overlap |
| union (JN retargeting) ↔ jn C3-3 (uses the shared LAL) | different audiences → **KEEP JN** |
| Studio-feedback test campaign (JN) ↔ JN C1-1 (same pins, same goal, two budgets) | **MIGRATE NEXT → done**: ad moved into C1-1, test campaign paused (below) |
| 658869122728885 boost ↔ C1-1 | already paused 09:54 |
| **JustNow44 (unreadable) ↔ everything** | **UNKNOWN** — see M5: the Page has active ads that belong to neither jn nor JN |

### M3 — customer exclusions
Both lists READY: 120251936408430312 "JN - Confirmed bookings 12mo" (ACTIVE, Normal, updated 8 Oct) and
120249973174230073 "jn - Customers 889" (ACTIVE, Normal, updated 8 Oct). Every new prospecting cell
already carries them (T1, T2, C1-1, union, C3-2/3). Not applied today to the nine legacy jn winners and
W1/W2: the connector force-pauses an ACTIVE ad set on any targeting edit (pause → edit → re-activate) and
the edit resets learning; on a peak-traffic Friday that is a delivery risk on the proven cells, and W1/W2
must stay untouched for the parity test. Proposed instead: **Monday 13 Oct 09:30 Dubai batch** — one
bundled edit per ad set (exclusion only) on the nine jn winners, three at a time with read-back,
owner-approved. Reactivation / C3-1 keep targeting customers (no exclusion, by design).

### M4 — UAE 1 % lookalike
Already exists: **120251936410460312 "JN - LAL 1% Confirmed bookings"** — origin 120251936408430312,
ratio 0.01, delivery ACTIVE, created 18 Sep, size shown at the API's 1,000 floor; it is live-tested in jn
C3-3 (7d AED 48 → 9 conv @5.30). No duplicate created. Rename to `JN | LAL 1% UAE | CONFIRMED CUSTOMERS`
was attempted and **rejected by the connector** ("This audience type cannot be updated via this tool");
rename in Audiences if wanted. Country is not exposed in the lookalike spec (`use_additional_countries`
true, no `country` key) — verify "United Arab Emirates" in the Audiences UI before any new attach.

### M5 — JustNow44 2820299204977421, direct evidence
* **Connector:** `is_ads_mcp_enabled=false` (Meta staged rollout) — every ad-object read refused; business
  list shows ACTIVE, AED, payment method present, no disable reason. No browser tool exists in this
  session (re-checked). Google Drive: nothing.
* **Mailbox evidence (owner's own receipts):** 20+ "Your Meta ads receipt (Account ID: 2820299204977421)"
  emails 30 Jun – 21 Jul 2026, billed every 1–3 days at AED 150–425 (≈ AED 290/day), "You requested this
  manual payment", Visa ····2662, line items only "New Sales Campaign" and "New Sales Campaign - Copy"
  (impression-billed CTWA naming). "Your payment for Facebook Ads was declined" for JustNow44 on 11, 17,
  19 and 22 Jul (and for JN on 22 Jul). No receipt for **any** account after 21 Jul in this mailbox — the
  receipt links name a second notification address (mbayoumi2112@outlook.com), so later billing mail
  likely lands there. A 24 Sep "Your ads are running again" notice links to ad account
  **2043141456283110**, an ID not in the 32-account list — a 33rd account the connector cannot see.
* **Ad Library (Page "Just Now" 122098309970001876, ACTIVE, AE): 38 active ads.** Matching their creation
  times against every jn and JN ad created 15 Sep – 9 Oct leaves ≈ 20 unexplained, including a batch of
  **16 ads created 29 Sep 15:28 Dubai** (jn's "Reel tests (rebuilt from JustNow44…)" were created at 22:13
  that day and are PAUSED/WITH_ISSUES, so they are not these). Only one account with Page access is
  unaccounted for: JustNow44. Snapshot URLs are in the Ad Library result (ids 4046185359019667,
  27432568766420118, 1691958985795118, 2098580121531534, 1067474929246422, 1082208651079306 …).
* **Conclusion:** CONNECTOR PROBLEM = Meta MCP rollout gate (unchanged). ACCOUNT: no restriction visible;
  **very likely actively delivering CTWA ads right now from the same Page** → the JN/jn overlap cleanup is
  incomplete until JustNow44 is read, and it may be the third bidder on the same Sharjah/Dubai audiences.
  July evidence (manual-payment CTWA at ≈ AED 290/day) points to **HIGH-SCALE WHATSAPP** as the evidence-
  based candidate mission, but it is not assigned until spend limit, Account Quality and campaign metrics
  are read. Scale readiness: unknown (spend limit unreadable; payment declines in July are the one
  historical risk). Unblock: export from Ads Manager (lifetime + 30d + 90d, Account overview, Account
  Quality) into `meta/justnow44/`, or run the read from the owner's Claude-in-Chrome session.

### M6 — shared dataset architecture (fresh)
Dataset 614743294720303 last fired 10:23 Dubai today (browser + server). It appears in the dataset list of
all four mission accounts.

| ACCOUNT | DATASET 614743294720303 | PAGE | IG | CUSTOMER AUDIENCE ACCESS | STATUS |
|---|---|---|---|---|---|
| jn 1037126214908677 | yes (in use) | Just Now + CO LLC | justnow.life.ae | customers 889 own; JN LAL bookings shared | **CORRECT** |
| JN 9147325105346647 | yes (in use, LEAD) | Just Now + CO LLC | justnow.life.ae | bookings 12mo, contacts csv, pixel audiences, LAL | **CORRECT** |
| justnow22 1897980308260660 | yes (listed) | Just Now + CO LLC | not checked | only a site-visitor audience "jn" (22–26k); **no customer list** | FIX REQUIRED before CT: share 120249973174230073 + 120251936408430312 |
| JNN 1304802461392117 | yes (listed) | **none** | none | **none** | FIX REQUIRED before any use: Page, IG, audiences |
| JustNow44 2820299204977421 | unknown | unknown (BM-B owns only the CO LLC Page; "Just Now" is shared from BM-A) | unknown | unknown | VERIFY via export |
| 658869122728885 | not used | 4 Pages | — | none | HOLD |

Also visible: 16–23 legacy datasets per account (jn/JN.LIFE/NA3-7/Just Now 1,4/newpixel/wtp …), most
last fired 7–15 Sep or never. No new pixel was created; the legacy ones are candidates for a later
clean-up, not for use.

### M7 — winner migration this pass
* Studio-feedback video (creative 1094497890116067): new ad **120252227059520312** `VIDEO | STUDIO-FEEDBACK
  | BOOK-NOW | V01` created in C1-1 120252107075750312 (10:45), activated (10:46; effective
  PENDING_REVIEW); test campaign **120252195374070312 paused** (10:45:43, read back PAUSED; its ad set and
  ad show CAMPAIGN_PAUSED). Saves AED 60/day of zero-lead spend; the creative keeps being tested inside the
  learner. Rollback: set campaign ACTIVE.
* W-c (jn "Sticky kitchen EN" into JN as a website ad) still needs the video file uploaded to JN (cross-
  account video reuse is not possible); the second reactivation ad still needs a fresh build with a
  WhatsApp CTA.
* Running total WINNERS MIGRATED: T1, T2 (twins, in test) + 3 retargeting creatives consolidated + 1
  studio ad moved.

### M8 — account renames
The connector cannot rename an ad account (`ads_update_entity` accepts campaign / ad set / ad only), so
renames stay with the owner in Business Settings → Ad accounts: jn → `JUSTNOW | WHATSAPP SALES | jn`,
JN → `JUSTNOW | WEBSITE BOOKINGS | JN`, justnow22 → `JUSTNOW | CREATIVE TESTING | justnow22`, JNN →
`JUSTNOW | FUTURE REVENUE | JNN`; JustNow44 after its diagnosis; legacy shells untouched.

### M9 — Purchase gate (re-check)
Make scenario 6529499 ran 00:00 Dubai today: 9 completed jobs found, **0 Purchases sent**, 9 skipped as
legacy (already sent by the old confirmation flow), 37 pending finalisation, **2 aged-out jobs requiring
review**. Pixel 614743294720303: Purchase events arrived daily until 6 Oct (legacy flow), none on 7–8 Oct.
Lead events ≈ 20–50/day. **FAIL** — 0 of 7 clean days; keep Purchase off everywhere.

### Writes this pass
3 successful (studio ad create, activate, test campaign pause), 1 rejected without change (LAL rename).
Running total since 09:53: **36 successful production writes, 0 rollbacks.** Budgets: none changed; the
weekend-weighting proposal is in `meta/weekend-weighting-plan-2026-10-09.md`.

## 9. Owner approvals of 11:00 Dubai and what was prepared (no new Meta writes)

| Approval | Action taken |
|---|---|
| Recommended multipliers; Meta-native rules only; five eligible campaigns; T1/T2, W1/W2, reactivation, justnow22, Purchase excluded; capacity guard kept | `meta/automated-rules-spec-2026-10-09.md`: 20 copy-ready rules (groups W-jn ×3 campaigns, W-C1, R-C2), staged steps ≤ +25 % / −20 %, one rule per campaign per slot. Owner creates them in Ads Manager (connector has no rule tool). Read-only verification routine at 00:40 and 12:40 Dubai daily until 23 Oct; daily 09:22 check-in carries the 11-booking capacity guard. |
| Monday 13 Oct 09:30 exclusion batch on the 9 jn winners, one bundled edit each, baseline saved, read-back after | `meta/monday-exclusion-batch-2026-10-13.json`: baseline targeting (9 Oct read) + sanitized payloads adding 120249973174230073, pre-checks, 3-pass order (smallest spend first), rollback. One-shot routine fires 13 Oct 09:30 Dubai into this session; every write still prompts the owner. |
| Lookalike: keep 120251936410460312, no new 1 %, verify UAE in Audiences UI, do not attach | Connector read: source 120251936408430312, ratio 0.01, ACTIVE, created 18 Sep, size at API floor; country not exposed → owner confirms "United Arab Emirates" in Audiences. Nothing attached. |
| JustNow44 priority direct read | No browser in this session. New direct path found: Windsor.ai's Facebook (Meta Ads) connector was connected before and its token expired on 29 Sep (owner's inbox alert). Re-authorizing it with the owner's Facebook login lets this session read 2820299204977421 through Windsor, independent of the Meta MCP gate. Authorization link handed to the owner; export remains the fallback. Mission stays unassigned. |
| Monitoring unchanged, no budget changes, no restructuring during the weekend | 16:15 Dubai delivery check and daily 09:22 scorecard remain; nothing else scheduled to write. |

## 10. Weekend controlled scale-up — Stage 1, 11:07 Dubai (owner brief "CONTROLLED SCALE-UP TO ~AED 1,000/DAY WEEKEND" + correction "today ≈ AED 750–800, then 850–900 after 16:15, Sat 950–1,000 staged")

Scope: mature proven campaigns only. Never: T1/T2 (campaign 120250144447740073), W1/W2 control
120251948470120312, reactivation, justnow22, Purchase. Progression 90 → 120 → 150 → 180 with read-back
between stages. The connector force-pauses a campaign on a budget edit, so each change = edit + immediate
re-activation (campaigns were paused for 20–40 s).

Baseline 11:05 Dubai (today so far / 7 days): New Sales Campaign AED 22 → 9 conv @2.48 (7d 954 → 280
@3.41, CPM 16); WhatsApp Sales 5158 AED 20 → 8 @2.53 (7d 911 → 243 @3.75, CPM 22); C3 AED 15 → 1 @14.78
(7d ≈ 4.9 excl. C3-4, CPM 42 today) → held; JN C1 AED 35, 1,186 imp, CTR 4.4 %, 0 leads yet (7d 9 leads
@56; learning status "limited"); JN C2 AED 21, union new. Capacity: 8 Oct 7 jobs (all DONE-marked),
9 Oct 7 booked (6 via website form), 10 Oct 5 booked so far; ceiling 12 → available.

| CAMPAIGN | OLD | NEW | % | STATUS (read-back) | LEARNING | SPEND AFTER CHANGE | CPA | BOOKING SIGNAL | NEXT REVIEW |
|---|---|---|---|---|---|---|---|---|---|
| jn New Sales Campaign 120249855697050073 | 90 | **120** | +33 % | ACTIVE 11:07:34 (re-activated after force-pause) | ad sets unchanged (no significant edit; CBO budget change) | AED 22.61 at 11:12 | 2.51 today / 3.41 7d | 7 bookings today, 6 from the site form | 14:00 Dubai |
| jn WhatsApp Sales 5158 120249855229580073 | 90 | **120** | +33 % | ACTIVE 11:07:37 | unchanged | AED 20.34 | 2.54 / 3.75 | same | 14:00 |
| JN C1 Website Acquisition 120252107068880312 | 84 | **105** | +25 % | ACTIVE 11:07:35 (not force-paused) | C1-1 "learning limited" (9 conv) — pre-existing | AED 35.03 | 0 leads today / AED 56 7d | website form active today | 14:00 |
| JN C2 Retargeting 120252107080200312 | 70 | **80** | +14 % | ACTIVE 11:07:40 | union in learning (new) | AED 20.74 | n/a today | — | 16:40 |
| jn C3 120250020646250073 | 90 | 90 | 0 | held — weakest today (1 conv on AED 15, CPM 42) | — | — | — | — | re-evaluate 16:40 |

Account total daily budget: **594 → 685**. Planned path (each step gated, each write prompted):
Stage 1b 14:00 Dubai → New Sales + 5158 to 150 (≈ 745); Stage 2 16:40 → toward 850–900 (C1 125, C3 110
only if its CPA < 4.5, New Sales/5158 180 only if CPA holds, C2 90 only if frequency < 1.5); Sat 09:40 →
toward 950–1,000 staged; Sun 00:30 → 800–900; Mon 00:30 → ≈ 600 baseline. Hold rules: CPA worse than
+25–30 % vs baseline, booking quality down, 11+ bookings yesterday/today, CPM/frequency spike without
conversions, handling overload. Writes this stage: 4 budget edits + 3 re-activations = 7 (total since
09:53: 43 successful, 0 rollbacks).
