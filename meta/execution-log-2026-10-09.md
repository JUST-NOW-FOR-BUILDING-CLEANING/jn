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

## 11. Brand expansion layer — built and published 11:47 Dubai (owner brief "BUILD TOP-OF-FUNNEL BRAND EXPANSION LAYER")

Full spec, creative map, bench, audiences, metrics and rotation design: `meta/brand-expansion-layer-2026-10-09.md`.

* Home account **justnow22 1897980308260660** (BRAND / CREATIVE TESTING): mission separation kept — jn
  stays WhatsApp sales, JN website bookings + retargeting. Draft mode is ON in this account, so every
  object was staged as a draft (nothing spent), read back, and published in one call at 11:47.
* Campaign **23860638577100791** `BR | Video Views ThruPlay | UAE excl. Abu Dhabi | Deep Cleaning | Oct 2026`
  — OUTCOME_ENGAGEMENT, CBO **AED 60/day**, Highest volume → read back ACTIVE, budget AED 60, start
  11:47:22, delivery pending (ads in review).
* Ad set **23860638584760791** `BR-1 | Broad 25+ | UAE excl. Abu Dhabi (incl. Al Ain) | ThruPlay` —
  THRUPLAY / IMPRESSIONS / ON_VIDEO, Page 122098309970001876; UAE (home + recent) minus region Abu Dhabi
  key 8 (Al Ain is inside it); Facebook + Instagram placements only; Advantage+ audience on (25–65 as
  suggestion) → read back ACTIVE with exactly that targeting.
* Ads (ACTIVE, PENDING_REVIEW / IN_PROCESS at 11:50): A-EN 23860638592800791 (post _2163113240903678),
  A-AR 23860638592980791 (_1622838339212041), B 23860638593040791 (_1559790696189996), C 23860638593450791
  (_4303960699820816, branded-content post with an external creator tag — review result to be checked),
  D 23860638593500791 (_890288284018661), E 23860638607180791 (new positioning creative 1427446799529368 on
  Page video 1387153059699272, copy "JustNow specializes in professional deep cleaning. We do not provide
  regular cleaning." EN + AR), F 23860638601130791 (_2187572902181730). Deviation: the first E creative
  1396311642317311 produced the draft error "ObjectStorySpecRedundant" (connector wrote image_url and
  image_hash); rebuilt with the hash only, the broken draft ad 23860638593520791 was set DELETED before
  publish (never live, no history).
* Warm audiences in JN: **created** 120252228024070312 (video 25 %), 120252228030340312 (50 %),
  120252228030930312 (75 %) — Page-wide single-rule form, 365 d, prefill on (the 11-video form was
  rejected: max 5 rules per audience); **verified** IG engagers 120251888118190312 (31.4–37k) and FB
  engagers of the Just Now Page 120241682713780312 "just now . facebook" (26.2–30.8k; the union ad set
  still uses only the CO LLC Page audience 120251888139630312, 2.7–3.2k). Nothing attached.
* Customer exclusion **not applied**: no customer list exists in justnow22; owner shares 120251936408430312
  (JN) or 120249973174230073 (jn) to ad account 1897980308260660 in Business Settings, then one prompted
  edit adds it to BR-1.
* Budget profile: AED 60 flat in week 1; Automated Rules group **BR** (rows 21–27 of
  `meta/automated-rules-spec-2026-10-09.md`: Mon 58 · Tue/Wed 50 · Thu 60→70 · Fri 85 · Sat 90 · Sun 72)
  for the owner to create natively, first cycle Thu 16 Oct; brand share 8–10 % of planned totals.
* Monitoring: the daily 09:22 Dubai routine now also reads the brand campaign (ThruPlay rate, cost per
  ThruPlay, hook rate, frequency, audience growth, fatigue flags, 8–12 % share) — read-only.
* Writes: 22 successful (1 campaign, 1 ad set, 8 creatives, 8 draft ads, 1 draft delete, 1 publish, 3
  audiences), 1 rejected audience attempt. **Running total since 09:53: 65 successful production writes, 0
  rollbacks.** Untouched: T1/T2, W1/W2, NSC/5158/C1/C2/C3 budgets (Stage 1 levels), reactivation, Purchase,
  protected account 1679026507158086.

## 12. 16:15–16:30 Dubai — go-live delivery check #1, budget verification, and weekend Stage 1b (delayed from 14:00)

### 12a. Delivery check #1 (routine "review approval + first delivery check", read-only)

| Object | State at 16:20 Dubai | Today (since 00:00) |
|---|---|---|
| T1 ad set 120250144454520073 (AED 60) | ACTIVE, budget 60 untouched | AED 22.95 → 7 conversations @ 3.28, CPM 15.3, freq 1.03 |
| T2 ad set 120250144457040073 (AED 30) | ACTIVE, budget 30 untouched | AED 10.43 → 3 @ 3.48, CPM 23.0, freq 1.08 |
| T1/T2 ads 120250144462130073 / 120250144462600073 / 120250144463050073 | all ACTIVE, delivery `active` (review passed) | 5.63 / 17.25 / 10.26 spend, 3 / 4 / 3 conversations |
| Twin campaign 120250144447740073 | ACTIVE | AED 33.14 → 10 @ 3.31 (W1 control today: AED 41.57 → 7 @ 5.94) |
| Reactivation 120250144448010073 + ad 120250144463650073 | PAUSED / PAUSED, 0 spend | — |
| JN union ad set 120252226500410312 | ACTIVE, LEARNING (1 conversion) | AED 24.63 → 1 website lead, CPM 42.9, freq 1.25 |
| Union ads 120252226507840312 / 120252226508320312 / 120252226511090312 | all ACTIVE, `ad_set_in_learning_phase` (review passed) | 1.22 / 18.38 (the lead) / 5.03 |
| C2-1 / C2-2 / C2-3 | PAUSED / PAUSED / PAUSED (residual spend 5.00 / 0.65 / 12.23 is from before the 10:12 pause) | — |
| W1 120251948470210312 / W2 120251948470250312 | ACTIVE / ACTIVE (W2 barely delivering: AED 0.61, 40 impressions) | W1 AED 41.57 → 7 @ 5.94 |
| Studio ad 120252227059520312 in C1-1 | ACTIVE, warning `ad_set_learning_exit_unsuccessfully` (pre-existing C1-1 learning-limited) | AED 1.51, 46 impressions |
| Brand layer (justnow22) | all 7 ads ACTIVE, delivery `active` (review passed within ~4 h) | AED 19.70 → 1,319 ThruPlays @ ≈ AED 0.015; A-EN carries 4,536 of 5,502 impressions (ThruPlay rate 24 %), E 157 imp / 40 ThruPlays (25 %), F 513 / 112 (22 %) |

No rejected ad, no policy issue, no delivery error. Nothing to fix.

### 12b. Budget verification (routine 12:40 Dubai, completed here; the 12:40 run read jn and the brand campaign, the JN and T1/T2 reads were cut off by the next event)

| Campaign | Expected (approved Stage 1 level) | Actual | OK |
|---|---|---|---|
| jn New Sales Campaign | 120 | 120 (until 16:28, see 12c) | yes |
| jn WhatsApp Sales 5158 | 120 | 120 (until 16:28) | yes |
| jn C3 | 90 | 90 | yes |
| JN C1 | 105 | 105 | yes |
| JN C2 | 80 | 80 | yes |
| JN W1/W2 control | 80 | 80 | yes |
| T1 / T2 | 60 / 30 | 60 / 30 | yes |
| justnow22 brand | 60 | 60 | yes |

The verification routine's prompt was pointed at "the latest approved level recorded in this log" (it still said "base" from before the weekend scale-up); from 16 Oct it compares with the rule values.

### 12c. Weekend Stage 1b — executed 16:28 Dubai (routine fired 14:00; the session was idle until 16:16)

Gates at 16:20: New Sales Campaign CPA 2.76 today vs 3.41 baseline (−19 %); 5158 CPA 4.20 vs 3.75 (+12 %, inside the +25–30 % tolerance; its CPM 22.9 equals its 7-day CPM, so no spike without conversions); frequency 1.05–1.06; capacity 7 bookings today (all confirmed), 7 booked tomorrow (4 still UNCONFIRMED) vs the 11-booking hold line; handling normal. All gates PASS. Weak campaigns not raised: C3 (AED 49 → 4 conversations @ 12.36, CPM 34), JN C1 (AED 62 → 0 website leads today; 7-day AED 56/lead).

| CAMPAIGN | OLD | NEW | % | CPA BASELINE (7d) | CURRENT CPA (today) | BOOKING SIGNAL | CAPACITY STATUS | STATUS (read-back) | NEXT REVIEW |
|---|---|---|---|---|---|---|---|---|---|
| jn New Sales Campaign 120249855697050073 | 120 | **150** | +25 % | 3.41 | 2.76 (24 conv on AED 66) | 7 bookings today, 6 via the site form; 7 tomorrow | 7/12 today, 7/12 tomorrow → available | ACTIVE, budget 150, delivery active, 16:28:45 (not force-paused this time) | 16:40 Dubai (Stage 2 routine) |
| jn WhatsApp Sales 5158 120249855229580073 | 120 | **150** | +25 % | 3.75 | 4.20 (13 conv on AED 55) | same | same | ACTIVE, budget 150, delivery active, 16:28:52 | 16:40 Dubai |

Conversion accounts total daily budget: **685 → 745** (jn 480 incl. T1/T2 90; JN 265). Brand layer 60 on top (7.5 %
of 805). Stage 2 at 16:40: C1 HOLD (0 leads today), C3 HOLD (CPA 12.4), C2 80 → 90 eligible (frequency 1.25 < 1.5,
1 lead), New Sales/5158 150 → 180 only after ≥ 2 hours of read-back at 150 (earliest ≈ 18:30 Dubai), so today's
realistic ceiling is ≈ 755–815 rather than 850–900 unless C1 produces leads this evening. Writes this section: 2
budget edits (no re-activation needed). **Running total since 09:53: 67 successful production writes, 0 rollbacks.**

## 13. Weekend Stage 2 — 16:43 Dubai (routine 16:40; owner: "after the 16:15 checkpoint … prepare the next increase toward AED 850–900 … do not force 900")

Fresh read 16:43 (today): New Sales AED 68.47 → 24 conversations @ 2.85 (baseline 3.41), CPM 17.5, freq 1.05;
5158 AED 56.09 → 15 @ 3.74 (baseline 3.75), CPM 22.8, freq 1.06; C3 AED 51.20 → 5 @ 10.24 (gate < 4.5: FAIL);
C1 AED 63.57 → 0 website leads (gate "leads/bookings came in": FAIL); C2 AED 44.12 → 1 lead @ 44.12, CPM 39.0,
freq 1.26 (gate < 1.5: PASS). Capacity unchanged since 16:20: 7 today / 7 tomorrow (4 unconfirmed), 4 bookings
created today (3 via the website form) — available, handling normal.

| CAMPAIGN | OLD | NEW | % | CPA BASELINE | CURRENT CPA | BOOKING SIGNAL | CAPACITY STATUS | STATUS (read-back) | NEXT REVIEW |
|---|---|---|---|---|---|---|---|---|---|
| JN C2 Retargeting 120252107080200312 | 80 | **90** | +12.5 % (modest, retargeting) | union new (10-day window); C2 7-day n/a | AED 44.12/lead (1 lead) | 4 bookings created today | 7/12 · 7/12 → available | ACTIVE, budget 90, 16:44:50; effective IN_PROCESS (Meta re-processing after the edit, normal) | Sat 09:40 Dubai |
| jn New Sales Campaign | 150 | 150 (hold) | — | 3.41 | 2.85 | — | — | ACTIVE at 150 since 16:28 — only 15 min of read-back | **18:30 Dubai Stage 2b**: 150 → 180 if CPA holds |
| jn WhatsApp Sales 5158 | 150 | 150 (hold) | — | 3.75 | 3.74 | — | — | same | 18:30 Dubai Stage 2b |
| JN C1 | 105 | 105 (hold) | — | AED 56/lead | 0 leads on AED 64 today | no website leads yet today | — | ACTIVE | Sat 09:40 |
| jn C3 | 90 | 90 (hold) | — | ≈ 4.9 | 10.24 | — | — | ACTIVE | Sat 09:40 |

Conversion accounts total daily budget: **745 → 755** (brand 60 on top = 815). Stage 2b one-shot routine armed for
18:30 Dubai (two hours of read-back at 150 before the 180 step, each write prompted). Writes this section: 1 budget
edit (not force-paused). **Running total since 09:53: 68 successful production writes, 0 rollbacks.**

## 14. Weekend Stage 2b — 18:33 Dubai: 150 → 180 step HELD until Saturday 09:40 (no writes)

Read 18:33 (today): New Sales AED 92.29 → 29 conversations @ 3.18 (baseline 3.41, −7 %), CPM 17.8, freq 1.05;
5158 AED 71.95 → 20 @ 3.60 (baseline 3.75, −4 %), CPM 21.8, freq 1.08; C3 AED 72.76 → 5 @ 14.55 (held); C1
AED 69.44 → 0 website leads (held); C2 AED 52.31 → 1 lead, freq 1.28, ACTIVE at 90 (edit processed). Increment
since the 16:28 step: New Sales +AED 23.82 → +5 conversations (marginal 4.76 = +40 % vs baseline, 5-conversation
sample); 5158 +AED 15.86 → +5 (marginal 3.17, healthy). Capacity: 8 jobs today (Harinder 19:30 added at 17:17 via
the website form), 7 tomorrow (3 still unconfirmed) → available; booking signal positive (5 created today).

| CAMPAIGN | OLD | NEW | % | CPA BASELINE | CURRENT CPA | BOOKING SIGNAL | CAPACITY STATUS | DECISION | NEXT REVIEW |
|---|---|---|---|---|---|---|---|---|---|
| jn New Sales Campaign 120249855697050073 | 150 | 150 | 0 | 3.41 | 3.18 today; 4.76 on the last 5 conversations | 5 bookings created today | 8/12 today, 7/12 tomorrow | HOLD — marginal CPA at 150 inconclusive (+40 % on 5 conversations) and only 61 % of the day's 150 spent by 18:33; a +20 % raise now would force ≈ 5× faster evening pacing | Sat 09:40 Stage 3: 150 → 180 if Friday's full-day CPA at 150 ≤ baseline +25 % |
| jn WhatsApp Sales 5158 120249855229580073 | 150 | 150 | 0 | 3.75 | 3.60 today; 3.17 marginal | same | same | HOLD — passes the CPA gate, held only for pacing (48 % of 150 spent by 18:33); first in line on Saturday | Sat 09:40 Stage 3 |

Day total stays at **AED 755 conversion + 60 brand = 815** (owner's envelope for today 750–800, stretch 850–900 "if
healthy" — not forced: C1 had no lead all day and C3 stayed above AED 10 per conversation). Stage 3 (Sat 09:40)
inherits: 5158 → 180 first, New Sales → 180 if its Friday evening holds, C2 90 (modest, no further), C1/C3 only on
proof. No writes this section. **Running total since 09:53: 68 successful production writes, 0 rollbacks.**

## 15. Daily scorecard — day 1 (Sat 10 Oct, read 09:25–09:40 Dubai; routine 09:22, read-only)

Window: since go-live 2026-10-09 10:12 Dubai (metrics from 00:00 Fri) to the read. No Meta write in this section.

| Item | Day | Numbers (Fri 00:00 → Sat 09:25) | Status |
|---|---|---|---|
| T1 ad set 120250144454520073 (AED 60) | 1 of 7 | AED 58.32 → 19 conversations @ **3.07**, CPM 17.77, freq 1.03, reach 3,185; ACTIVE, both ads ACTIVE (review passed) | **PASS-TRACK** (pass line ≤ 4.70 with ≥ 50; pace ≈ 19/day) |
| T2 ad set 120250144457040073 (AED 30) | 1 of 7 | AED 29.09 → 8 @ **3.64**, CPM 23.35, freq 1.09, reach 1,141; ACTIVE, ad ACTIVE | **PASS-TRACK** (pass line ≤ 4.60 with ≥ 25; pace ≈ 8/day) |
| Twin campaign 120250144447740073 | — | Fri full day AED 66.98 → 21 @ 3.19 (CPM 19.13, freq 1.06); Sat to 09:25 AED 21.01 → 7 @ 3.00 | — |
| W1 120251948470210312 / W2 120251948470250312 (control, must stay ACTIVE) | — | ACTIVE / ACTIVE. W1 AED 75.42 → 17 @ 4.44 (CPM 13.87, freq 1.05); W2 AED 1.43 → 2 (62 impressions, barely delivering). Campaign 120251948470120312 at AED 80: Fri AED 75.73 → 19 @ 3.99 | parity window open; twins 27 @ 3.24 vs W1+W2 19 @ 4.04 on the same window (−20 % CPA, +42 % volume on +14 % spend) |
| Union ad set 120252226500410312 | 1 of 10 | AED 85.54 → **2 website leads @ 42.77**, 0 purchases, CPM 42.26, freq 1.36, reach 1,485; ACTIVE. Fri (campaign) AED 78.99 → 2 @ 39.50; Sat to 09:25 AED 26.03 → 0 (CPM 49.87 on 522 impressions) | **PASS-TRACK** (≥ 5 leads ≤ AED 100 by 19 Oct; 17 % of the AED 500 fail-spend used) |
| C2-1 / C2-2 / C2-3 | — | PAUSED / PAUSED / PAUSED (residual 5.14 / 0.65 / 12.25, pre-pause attribution) | OK |
| C2 campaign 120252107080200312 budget | — | AED 90 = §13 weekend level | OK |
| Reactivation 120250144448010073 | — | PAUSED | OK |
| Capacity (calendar) | — | **Fri 8 jobs** (all confirmed, all DONE) · **Sat 7** (6 confirmed and staffed, 1 UNCONFIRMED 16:00) · **Sun 3** (1 confirmed villa 5+, 2 UNCONFIRMED) vs ceiling 12 / hold 11 | available, no CAPACITY FULL |
| Bookings created | — | **Fri 7** = 6 via the website form (08:52, 12:43, 14:45, 15:32, 17:17, 22:07 Dubai) + 1 phone (02:15); Sat none by 09:25. Fri conversations across all WhatsApp campaigns 129 (New Sales 40, 5158 42, C3 7, twins 21, W1/W2 19); website leads 2 (C2) + 0 (C1) | booking-rate proxy Fri ≈ 5.4 % (7 ÷ 129; account level, the calendar carries no ad-set source, so T1-vs-W1 booking rate is not measurable yet) |

### 15a. Brand layer (justnow22, campaign 23860638577100791 at AED 60 flat) — day 2

Campaign: Fri AED 36.39 → 12,506 impressions, reach 12,226, CPM 2.91, freq 1.02, **3,649 ThruPlays @ AED 0.010**,
5,896 25 %-plays; Sat to 09:25 AED 18.96 → 6,464 impressions, 1,861 ThruPlays, 2,869 25 %-plays. Cumulative
AED 55.35 → 18,970 impressions, **5,510 ThruPlays (ThruPlay rate 29.0 %), hook rate 46.2 %, cost per ThruPlay
AED 0.010, frequency 1.02–1.05**. Instagram profile visits: not returned at ad level for this objective.

| Ad | Spend | Impr. | CPM | Freq | ThruPlays | AED/TP | TP rate | 25 % | Hook | 50 % | 75 % | 100 % | Post eng. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A-EN 23860638592800791 | 45.63 | 15,716 | 2.90 | 1.02 | 4,680 | 0.010 | 29.8 % | 7,373 | 46.9 % | 4,281 | 3,219 | 2,164 | 11,401 |
| A-AR 23860638592980791 | 0.54 | 217 | 2.49 | 1.01 | 34 | 0.016 | 15.7 % | 34 | 15.7 % | 22 | 21 | 20 | 128 |
| B 23860638593040791 | 1.70 | 634 | 2.68 | 1.02 | 176 | 0.010 | 27.8 % | 256 | 40.4 % | 183 | 125 | 95 | 418 |
| C 23860638593450791 | 0.68 | 158 | 4.30 | 1.01 | 39 | 0.017 | 24.7 % | 36 | 22.8 % | 29 | 20 | 7 | 103 |
| D 23860638593500791 | 0.32 | 152 | 2.11 | 1.03 | 43 | 0.007 | 28.3 % | 39 | 25.7 % | 28 | 24 | 22 | 97 |
| E 23860638607180791 | 2.95 | 945 | 3.12 | 1.04 | 316 | 0.009 | 33.4 % | 292 | 30.9 % | 214 | 153 | 37 | 685 |
| F 23860638601130791 | 3.53 | 1,148 | 3.07 | 1.01 | 276 | 0.013 | 24.0 % | 816 | 71.1 % | 524 | 340 | 264 | 892 |

Benchmarks (first week, report only): ThruPlay rate ≥ 15 % → 29.0 % PASS · cost per ThruPlay ≤ AED 0.25 → 0.010
PASS · hook ≥ 30 % → 46.2 % PASS · 7-day frequency ≤ 2.0 → 1.05 PASS. A-AR, C and D sit under the 30 % hook line
on ≤ 220 impressions each (not judged yet). CBO concentration: A-EN carries 83 % of impressions and spend; no
fatigue flag (frequency 1.02, day 2, first-week baseline forms on day 7), no rotation proposed.
Brand share of Meta spend: **Fri 5.1 %** (36.39 of 712.46 = jn 404.74 + JN 271.33 + justnow22 36.39) — below the
8–12 % band because week 1 runs flat at AED 60 by design and Friday was a partial first day; Sat to 09:25 13.1 %
(video delivers early in the day; full-day expectation ≈ 7 % of 875). No budget change proposed; the band is reached
from Thu 16 Oct when rules 21–24 lift the brand to 60–90.
Warm audiences: video 25 % 120252228024070312, 50 % 120252228030340312, 75 % 120252228030930312 all still read
"below 1,000" (delivery INACTIVE, status 441 = populating; Meta reports a size only above the 1,000 minimum, with a
24–48 h lag, although the Page already has 8,765 25 %-plays); IG engagers 120251888118190312 31.4–36.9k (unchanged);
FB engagers 120241682713780312 26.3–31.0k (+0.1–0.2k vs 26.2–30.8k yesterday).

Recommended next action (proposal only, nothing executed): keep T1/T2 and W1/W2 untouched until the 16 Oct
scorecard; union continues; brand stays flat at 60 with no rotation. **Flag for the owner: JN C1 120252107068880312
has 0 website leads on AED 132 since Friday 00:00 (90.45 Fri + 41.94 Sat to 09:40)** — proposal: let Sunday's 00:30
reduce routine take C1 back to its AED 84 base rather than a proportional cut, and review the book-now path and C1's
creatives on Sunday.

## 16. Weekend Stage 3 — Sat 10 Oct 09:40 Dubai: New Sales and 5158 150 → 180 (writes approved and executed 10:28)

Gates on Friday's full day (owner: "if Friday remains healthy, allow staged scale toward AED 950–1,000. Do not
jump directly … in one step"):

* New Sales Campaign: AED 125.75 → 40 conversations @ **3.14** (baseline 3.41, −8 %; tolerance 4.26–4.43) PASS; CPM
  17.06, frequency 1.05 PASS; the §14 worry (marginal 4.76 on 5 conversations) cleared — the evening after 18:33
  added AED 33.46 → 11 conversations (marginal 3.04); 84 % of the 150 spent (budget was lifted mid-day). Sat to
  09:40: AED 13.38 → 5 @ 2.68.
* WhatsApp Sales 5158: AED 116.47 → 42 @ **2.77** (baseline 3.75, −26 %) PASS; CPM 20.64 (7-day 22.9), frequency 1.05
  PASS; evening after 18:33 AED 44.52 → 22 conversations (marginal 2.02); 78 % of the 150 spent. Sat to 09:40:
  AED 27.62 → 9 @ 3.07.
* C3: AED 95.58 → 7 @ 13.65 (baseline ≈ 4.9, +179 %) FAIL → hold 90. C1: AED 90.45 → 0 website leads (baseline
  AED 56/lead) FAIL → hold 105 (see §15 flag). C2: AED 78.99 → 2 leads @ 39.50, frequency 1.32 < 1.5, CPM 38.46
  stable → PASS but held at 90 per §14 ("modest, no further"); re-checked at 16:00 (Stage 3b, below).
* Capacity: Fri 8/12 done, Sat 7/12 (6 confirmed, all five 12:00 jobs staffed), Sun 3/12 → available. Booking
  signal: 7 created Friday, 6 via the website form. No CPM or frequency spike (today ≤ 1.17 everywhere; C2's 49.87
  CPM is on 522 impressions). Handling normal. T1/T2 and W1/W2 untouched.

| CAMPAIGN | OLD | NEW | % | CPA BASELINE (7d) | CURRENT CPA | BOOKING SIGNAL | CAPACITY STATUS | STATUS (read-back) | NEXT REVIEW |
|---|---|---|---|---|---|---|---|---|---|
| jn WhatsApp Sales 5158 120249855229580073 | 150 | **180** | +20 % | 3.75 | 2.77 Fri full day; 3.07 today | 7 bookings created Fri (6 web) | 8/12 Fri · 7/12 Sat · 3/12 Sun → available | ACTIVE, budget 180, delivery active, updated 10:28:21 Dubai (connector force-paused the edit → re-activated in the same minute; 6 live ad sets ACTIVE, the 3 "ZZ DO NOT USE" ad sets were PAUSED before and stay PAUSED) | Sun 00:30 Dubai (reduce routine) |
| jn New Sales Campaign 120249855697050073 | 150 | **180** | +20 % | 3.41 | 3.14 Fri full day; 2.68 today | same | same | ACTIVE, budget 180, delivery active, updated 10:28:24 Dubai (force-paused → re-activated; 4 ad sets ACTIVE) | Sun 00:30 Dubai |
| JN C2 Retargeting 120252107080200312 | 90 | 90 (hold) | — | AED 56/lead (C1 ref.) | 39.50 Fri (2 leads); 0 leads today on 26.03 | — | — | ACTIVE at 90 | **Sat 16:00 Stage 3b**: 90 → 100 only if ≥ 1 lead today and frequency < 1.5 |
| JN C1 120252107068880312 | 105 | 105 (hold) | — | AED 56/lead | 0 leads on AED 132 since Fri 00:00 | none | — | ACTIVE at 105 | Sat 16:00 Stage 3b: 105 → 125 only if ≥ 2 leads today at ≤ AED 60 |
| jn C3 120250020646250073 | 90 | 90 (hold) | — | ≈ 4.9 | 13.65 Fri; 0 on 7.45 today | — | — | ACTIVE at 90 | Sun 00:30 |
| T1 / T2 · W1 / W2 | 60 / 30 · 80 | unchanged | — | — | §15 | — | — | ACTIVE | 16 Oct scorecard |

Conversion accounts total daily budget: **755 → 815** (jn 540 = 180 + 180 + 90 + T1/T2 90; JN 275 = 105 + 90 + 80);
brand 60 on top = **875**. This is below the owner's 950–1,000 Saturday target: the two mature CBOs are at their
180 ceiling, and the remaining AED 75–125 sits in C1/C3 (gates failed) and C2 (modest step only). A one-shot
Stage 3b check is armed for 16:00 Dubai (trig_01JshCwFSwBQEtb3fVsa6FwD): C1 105 → 125 and/or C2 90 → 100 only on
the proof above, otherwise Saturday closes at 875 and I do not recommend lifting the 180 ceiling on the same day
as a +20 % step. Writes this section: 2 budget edits + 2 re-activations (each approved on its prompt; the approval
wait moved execution from 09:46 to 10:28). **Running total since 09:53 Thu: 72 successful production writes, 0
rollbacks.**
