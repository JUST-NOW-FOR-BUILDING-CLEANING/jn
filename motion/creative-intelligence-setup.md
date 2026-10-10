# JustNow – Motion Creative Intelligence Setup

Prepared 10 Oct 2026 (Dubai). Read-only verification; no integration, billing or account settings were changed.
Data window: last 30 days (10 Sep – 9 Oct 2026). Currency AED.

---

## 1. CONNECTED DATA

| Source | Status | Notes |
|---|---|---|
| Motion workspace | **Empty** | Auth returns 0 organisations, 0 workspaces. No ad account connected, no reports, no glossary, no AI tagging has ever run. |
| Meta ad account **jn** (1037126214908677) | Readable via Meta Ads API | Active, AED, payment OK. ~AED 10.3k spend last 30 d on top 40 ads. Data current to 9 Oct (hourly). |
| Meta ad account **JN** (9147325105346647) | Readable | Active, AED. ~AED 9.9k spend last 30 d on top 40 ads. Data current to 9 Oct. |
| Meta ad account **justnow22** (1897980308260660) | Readable | Active, AED. Only AED 36 spend (new "BR" ThruPlay video test launched 9 Oct, 7 ads). |
| Meta ad account **JustNow44** (2820299204977421) | **Not readable** | Account is active but not yet enabled for the Ads API tool ("gradually rolling out"). Not included. |
| Video / image visibility | Yes | 60+ creatives per account, video IDs, thumbnails, headlines and primary text all readable. |
| Ad naming | Inconsistent | Three conventions coexist (see Gaps). |
| Existing reports | None | No Motion reports. Madgicx subscription is inactive (tool refuses). Windsor.ai has jn, JN, justnow22, JustNow44, "Just Now", JNN connected and can serve as a data pipeline. |
| AI tagging | Not available until Motion is connected | Motion glossary + AI tags only exist inside a workspace. |

Result types in use: WhatsApp **messaging conversations started** (all "Sales" campaigns), **website leads** via pixel 614743294720303 (C1/C2/BookNow campaigns), ThruPlay (BR test).

---

## 2. GAPS (fix before Motion can work weekly)

1. **Motion has no workspace.** Create one, connect jn + JN (+ justnow22, JustNow44 when API-enabled). Nothing below can run inside Motion until this is done.
2. **Generic ad names hide the creative.** "New Sales Ad", "New Sales Ad – Copy 2", "New Sales Ad and Message – Copy 3" carry ~70% of spend. From the name alone nobody can tell which video is running. Motion groups by creative asset, so it will survive this, but PATTERN reports need names or tags.
3. **Untitled video library.** Most uploads are called "Auto_Cropped_AR_4_X_5_DCO_" with no title. Rename on upload: `SVC-ANG-LANG-FMT-HOOK-SRC-v01`.
4. **Two naming systems in the October tests.** jn uses `C3-1-a | Stove-grease reel | problem-solution | AR (control)`; justnow22 uses `BR-A-EN | Kitchen grease | Sticky kitchen`. Pick one (proposal below).
5. **Permission-blocked creatives.** 14 creatives in jn and 4 in JN sit in WITH_ISSUES (the "Ad Processing Permission Issue" from 27 Sep). They cannot deliver and will show as zero-spend noise in any report.
6. **Lead vs chat results are not comparable.** WhatsApp chats cost AED 3–5, website leads AED 60–170. Reports must be split by result type or they will always "prove" WhatsApp wins.
7. **Purchase attribution is thin.** Only 60 purchases attributed across both accounts in 30 d; most ads show null. Keep "cost per chat" as the weekly goal metric and treat purchases as a secondary tie-breaker.
8. **JustNow44 unreadable** through the API tool; connect it to Motion directly via Meta login instead.

---

## 3. CREATIVE TAXONOMY (Motion glossary categories)

Create these six custom categories in Motion → Glossary, with exactly these values.

| Category | Values |
|---|---|
| SERVICE | Kitchen · Full Home · Upholstery |
| ANGLE | Grease · Steam · Mold · Process · Transformation · Testimonial · Brand Positioning |
| LANGUAGE | Arabic · English · Bilingual |
| FORMAT | UGC · Customer Voice · Process · POV · Team · Before/After · Static |
| HOOK | Problem · Shock · Question · Education · Result |
| SOURCE | Customer · Staff · Creator · Brand |

(Added "Bilingual" and "Static" because 9 live creatives are EN+AR and 6 are images; without them those rows would be untaggable.)

### Naming convention (ad name and video title)

```
ACCT | SVC-ANG-LANG-FMT-HOOK-SRC | short label | vNN | DDMMM
JN | KIT-GRE-AR-UGC-QUE-CRE | Stove grease creator | v01 | 10OCT
```

Motion can auto-parse this with "name rules" so every new ad is tagged on upload without manual work.

### Tagging of the current live creatives (what the data tells us)

| Creative (as named today) | SVC | ANG | LANG | FMT | HOOK | SRC |
|---|---|---|---|---|---|---|
| Creator reel 2 / Top creator reel | Kitchen | Transformation | English | UGC | Problem | Creator |
| Sticky kitchen video ("Why does your kitchen feel sticky?") | Kitchen | Grease | English | Before/After | Question | Brand |
| Arabic stove grease ("كنت مفكرة إن البوتاجاز نضيف؟") | Kitchen | Grease | Arabic | Before/After | Question | Brand |
| Inside-the-cabinets ("لحد إمتى هتفضلي تأجلي") | Kitchen | Process | Arabic | Process | Problem | Brand |
| Same kitchen… different result | Kitchen | Transformation | Bilingual | Before/After | Result | Brand |
| POV: Our team just left your kitchen | Kitchen | Transformation | English | POV | Result | Brand |
| Watch the grease melt | Kitchen | Steam | English | Process | Result | Brand |
| Extractor filter ("This is what comes out…") | Kitchen | Grease | English | Process | Shock | Brand |
| Why steam > traditional cleaning | Kitchen | Steam | English | Static | Education | Brand |
| Customer voice (first time my home feels clean) | Full Home | Testimonial | English | Customer Voice | Result | Customer |
| Studio feedback video (Book Now, 7 Oct) | Full Home | Testimonial | English | Customer Voice | Result | Customer |
| Steam. Precision. Results. | Kitchen | Steam | English | Process | Result | Brand |
| Full-home process team montage (BR-C) | Full Home | Process | English | Team | Result | Staff |

---

## 4. THE FOUR CORE REPORTS (Motion configuration)

All four: platform Meta, accounts jn + JN (+ justnow22), **groupBy = creative**, attribution 7-day click / 1-day view, spend threshold AED 150, refreshed every Monday 09:00 Dubai.

### Report 1 – WINNERS
*Which creatives are producing the strongest business results?*
- Date range: last 14 days.
- Primary metric: **cost per messaging conversation** (goal metric). Secondary: purchases, cost per purchase, website leads.
- Filter: spend ≥ AED 150 AND result type = conversation. Separate tab for result type = website lead (threshold AED 200).
- Sort: cost per result ascending. Show CTR, CPM, frequency, thumbstop.
- Rule: a creative is a *winner* when cost/chat ≤ AED 3.80 (15% better than account average 4.30) on ≥ AED 150 spend, or cost/purchase ≤ AED 110.

### Report 2 – FATIGUE
*Which proven creatives are losing efficiency?*
- Date range: last 28 days, **compared week-over-week** (Motion comparison mode).
- Filter: creatives that were winners in any prior week (cost/chat ≤ 3.80) AND spend this week ≥ AED 100.
- Flags: cost/chat up ≥ 25% vs best week · CTR down ≥ 25% · frequency ≥ 1.6 · spend share dropping while cost rises.
- Output: Keep / Refresh / Kill per creative.

### Report 3 – PATTERN ANALYSIS
*Which hooks, formats, languages and service angles win?*
- Date range: last 30 days. GroupBy: glossary category (one tab each: HOOK, FORMAT, LANGUAGE, SERVICE, ANGLE, SOURCE).
- Metrics per tag: spend, spend share, cost/chat, CTR, purchases.
- Coverage view: tags with zero spend = untested combinations (creative opportunities).

### Report 4 – WHAT TO PRODUCE NEXT
*Give the creative team specific production briefs.*
- Not a Motion report but a Monday ritual: take Report 3's top tag per category + Report 1's top 3 creatives + Report 3's zero-spend tags → write 5–10 briefs using the template in section 7. Store briefs in `motion/briefs/YYYY-WW.md`.

---

## 5. CURRENT WINNERS (last 30 days)

Account average cost per WhatsApp chat: **AED 4.30** (jn) / **AED 4.60** (JN).

| # | Creative / ad | Acct | Spend | Chats | Cost/chat | CTR | Purchases | Trend (weekly cost/chat) |
|---|---|---|---|---|---|---|---|---|
| 1 | **Creator reel 2** (UGC, EN) | jn | 763 | 219 | 3.48 | 2.87% | **10** | 4.21 → 3.71 → 2.86 → 2.65 (improving) |
| 2 | New Sales Ad – ad set "Copy A" | jn | 1,122 | 322 | 3.48 | 3.48% | 2 | 3.58 → 3.19 → 3.68 → 3.41 (stable) |
| 3 | New Sales Ad – ad set "New Sales Ad Set" | jn | 846 | 246 | 3.44 | 3.76% | 3 | 3.40 → 4.06 → 2.71 → 4.13 |
| 4 | New Sales Ad and Message (main) | JN | 1,624 | 403 | 4.03 | 2.22% | 0 | 4.24 → 4.14 → 3.91 → 3.20 (improving) |
| 5 | Arabic stove grease video | jn | 313 | 77 | 4.06 | 2.87% | 3 | 5.55 → 3.95 → 3.67 → 1.49 (best CPM 15.4) |
| 6 | AS2 – Clients rebook monthly reel | JN | 150 | 48 | **3.12** | 3.97% | 0 | ad set paused since 23 Sep |
| 7 | Sticky kitchen video | jn | 564 | 148 | 3.81 | 1.84% | 0 | 2.65 → 4.18 → 4.14 → 2.88 |

Website-lead winners (different funnel): **C1-1-d Stove-grease AR** – AED 542, 6 leads at AED 90, CTR 5.6%, **5 purchases (AED 108 each)**; C2-3-a Same kitchen before/after EN+AR – 3 leads at AED 77, 1 purchase. Cheapest traffic ever: "Same kitchen" promoted post, AED 0.09 per click, 1,671 clicks on AED 158.

Best cost per purchase: Creator reel 2 (AED 76) > Arabic stove grease (AED 104) > C1-1-d (AED 108) > New Sales Ad Copy 2 (AED 180).

---

## 6. CURRENT FATIGUE

| Creative | Signal | Action |
|---|---|---|
| **Top creator reel** (jn) | Ad name promises AED 2.19/chat; last 30 d is AED 4.07, 0 purchases, CTR fell to 2.0%. Still ACTIVE on AED 581. | Refresh: same creator, new opening 3 s and new first shot. |
| **New Sales Ad – ad set "Copy 2"** (jn, highest spender) | Meta cut its weekly spend 754 → 106 → 7; CTR 2.08% is lowest of the trio; AED 4.28/chat. | Kill in its current ad set, re-upload as a fresh ad in the "Copy A" set. |
| **New Sales Ad and Message – Copy** (JN) | Cost/chat rising every week 3.85 → 4.47 → 4.23 → 4.72. | Refresh hook. |
| **C3-1-a Stove-grease reel AR (control)** (jn) | 5.03 → 10.26 in the last two days at frequency 1.26; the stove-grease question hook appears in 12+ live creatives, so this is concept fatigue, not ad fatigue. | Pause; the hook needs a new visual, not another copy. |
| **C2-1-c "finish your booking" retarget** (JN) | Frequency 1.68, AED 172 per lead, 1 lead in the last week. | Replace creative (brief 7). |
| **Sticky kitchen video** (jn) | CTR 2.85% → 1.75% → 1.72%; cost oscillating. | Watch list; refresh in two weeks. |

---

## 7. WINNING PATTERNS

- **Service**: Kitchen carries ~95% of spend and all winners. Full Home exists only as two testimonial videos; Upholstery has never been advertised. Two open lanes.
- **Angle**: Grease and Transformation win chats. Steam/Process gets views but fewer chats. Testimonial is weak as a WhatsApp driver (Customer voice: AED 6.61/chat) but strong as a booking-page asset (studio feedback video). Mold: untested. Brand Positioning: only in the AED 1 BR test.
- **Language**: Arabic has the lowest CPM (15.4 vs 17–20 EN), the fastest-improving cost/chat, the best website CTR (5.6%) and the most purchases per dirham on the website funnel. Yet there is **no Arabic creator/UGC** creative at all. Bilingual before/after gets the cheapest clicks.
- **Format**: Creator UGC → purchases (10 of the 30 attributed in jn). Before/After → clicks and CTR. POV in English underperformed (AED 6.46). Team/Process montage and Static are untested at scale.
- **Hook**: Problem/Question hooks ("Why does your kitchen feel sticky?", "كنت مفكرة إن البوتاجاز نضيف؟") = volume. Result hooks ("Same kitchen… different result", "Watch the grease melt") = CTR. Shock ("This is what comes out of a kitchen extractor filter", "3 years of grease disappearing") exists only as low-spend posts and has never been tested with budget. Education ("Why steam > vinegar") earned 4.4–5.4% CTR as a static post.
- **Source**: Creator > Brand for purchases. Customer voice needs a better edit (start on the result, not the person). Staff has zero spend.
- **Funnel**: WhatsApp conversation objective is 15–40× cheaper per lead than the website objective, but the website campaigns are the ones producing attributed purchases. Run both; judge WhatsApp on cost/chat and website on cost/purchase.

---

## 8. NEXT 10 CREATIVE BRIEFS

Template for every brief: tags · the first 3 seconds · body · CTA · deliverables · success metric · kill rule.
All videos: 9:16 and 4:5, 15–25 s, captions burned in, no music-only versions. Upload titled with the naming convention.

### Brief 1 – Creator reel 3 (replicate the #1 winner)
Tags: Kitchen · Transformation · English · UGC · Problem · Creator.
First 3 s: creator opens her own greasy hood with "I haven't cleaned this since we moved in… don't judge."
Body: team arrives, steam close-ups, she reacts on camera at the end, mentions price "from AED 249".
CTA: "WhatsApp us, we reply in 2 minutes."
Deliverables: 2 cuts (20 s, 12 s), 2 thumbnails (face / grease).
Success: ≤ AED 3.50/chat on AED 300. Kill: > AED 5 after AED 200.

### Brief 2 – Arabic creator reel (fills the biggest gap)
Tags: Kitchen · Grease · Arabic · UGC · Question · Creator.
First 3 s: Emirati/Egyptian-dialect creator: "كنتي مفكرة البوتاجاز نضيف؟ شوفي ده" with a finger wipe on the "clean" cooker.
Body: same structure as Brief 1, Arabic voice, Arabic captions.
CTA: "ابعتيلنا واتساب".
Success: ≤ AED 3.20/chat (Arabic CPM advantage). Kill: > AED 4.50.

### Brief 3 – Full Home before/after (bilingual)
Tags: Full Home · Transformation · Bilingual · Before/After · Result · Brand.
First 3 s: split screen "Same 2BHK… completely different result / نفس الشقة… نتيجة مختلفة".
Body: 5 rooms, 2 s each, before→after wipe, end card "3 cleaners · 4 hours · from AED 659".
Success: CTR ≥ 4%, ≤ AED 4.50/chat. Kill: CTR < 2%.

### Brief 4 – Upholstery extraction shock
Tags: Upholstery · Grease · Bilingual · Process · Shock · Staff.
First 3 s: the dirty water tank from a "clean-looking" sofa, caption "This came out of a 2-year-old sofa".
Body: extraction pass, dry result, mattress variant.
CTA: WhatsApp.
Success: ≤ AED 5/chat (new service, allow higher). Kill: > AED 8.

### Brief 5 – Customer voice v2 (fix the weak format)
Tags: Full Home · Testimonial · Arabic · Customer Voice · Result · Customer.
First 3 s: **start on the result** (gleaming kitchen pan), customer voice-over "أول مرة أحس بيتي نضيف فعلاً", face appears at second 4.
Body: 12 s max, one sentence on price transparency.
Success: ≤ AED 4.50/chat. Kill: > AED 6.50 (today's level).

### Brief 6 – Extractor filter shock, scaled
Tags: Kitchen · Grease · English + Arabic cuts · Process · Shock · Brand.
First 3 s: the filter lifted out, grease dripping, caption "This is what you breathe when you cook".
Body: steam strips it in real time, end on clean filter.
Success: thumbstop ≥ 35%, ≤ AED 4/chat. Kill: > AED 5.50.

### Brief 7 – "Finish your booking" retarget refresh
Tags: Kitchen · Process · Arabic · Team · Problem · Staff.
First 3 s: screen recording of the booking page with cursor on "AED 249", voice "بدأتي الحجز وما كمّلتيه؟".
Body: 8 s, team photo, "نفس الفريق، نفس السعر، كمّلي خلال دقيقة".
Success: ≤ AED 60/lead, frequency cap 2 per 7 days. Kill: > AED 120/lead.

### Brief 8 – Education: why steam beats vinegar (video version)
Tags: Kitchen · Steam · English + Arabic cuts · Static→Video · Education · Brand.
First 3 s: three-way split: vinegar / baking soda / steam on the same burner grate.
Body: 15 s side-by-side result, "surface clean vs real clean".
Success: CTR ≥ 4% (the static got 4.4–5.4%), ≤ AED 4.50/chat.

### Brief 9 – Mold angle (bathroom silicone and AC vents)
Tags: Full Home · Mold · Arabic · Before/After · Problem · Brand.
First 3 s: black silicone line in a shower, caption "ده مش وسخ… ده عفن".
Body: steam on silicone, grout, AC vent; dry result.
Success: ≤ AED 5/chat. Kill: > AED 7.

### Brief 10 – A day with the team (brand positioning)
Tags: Full Home · Brand Positioning · Arabic · Team · Result · Staff.
First 3 s: four uniformed cleaners stepping out of the van, "فريق نسائي مدرّب، الأدوات معانا".
Body: 20 s montage: unloading tools, kitchen, bathroom, handover, customer smile.
Success: ThruPlay ≤ AED 0.02 in the BR campaign, then promote the best cut to a WhatsApp ad at ≤ AED 4.50/chat.

---

## 9. SETUP CHECKLIST (requires your approval before any change)

1. Create the Motion workspace "JustNow" and connect Meta accounts jn, JN, justnow22, JustNow44 (Meta login in Motion; read-only).
2. Create the six glossary categories above and the name-parsing rule.
3. Rename the top 15 live ads to the convention (names only; delivery is not affected).
4. Delete or archive the 18 WITH_ISSUES creatives once the asset permission issue is fixed.
5. Save the four reports with the settings in section 4; set Monday 09:00 refresh and email to the creative lead.
6. First production sprint: briefs 1, 2, 3, 6, 7 (five pieces, two weeks).
