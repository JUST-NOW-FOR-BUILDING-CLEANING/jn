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
