# C1 (website acquisition) and C3 (WhatsApp bookings) — diagnosis and challenger plan

Prepared 2026-10-11 ≈ 13:40 Dubai for the owner's decisions of 11 Oct: "C1: hold at AED 84. Do not scale. Prepare a
creative/landing-message diagnosis and challenger creative plan. If it remains at zero website leads after another
controlled observation window, propose PAUSE." and "C3: hold at AED 90. Do not scale. Treat as a creative problem, not a
budget problem." Read-only; every item below is a proposal.

## 1. C1 — JN 120252107068880312 "C1 Website Acquisition | book-now", ad set C1-1 Broad 25+ (OFFSITE_CONVERSIONS → Lead, pixel 614743294720303)

### 1a. Where the funnel breaks (last 7 days, 5–11 Oct, ad set level)

| Step | Count | Rate | Cost |
|---|---|---|---|
| Impressions | 18,831 | — | CPM AED 31.16 |
| Link clicks | 558 | **CTR 5.02 %** (jn winners 1.5–2.9 %) | AED 1.05 / click |
| Landing page views | 115 | **20.6 % of clicks** (healthy 50–80 %) | AED 5.10 / LPV |
| Website leads (Lead event) | 7 (all 5–8 Oct; **0 on AED 258 since Fri 9 Oct**) | 6.1 % of LPVs (normal for a booking form) | AED 83.8 / lead (7 d) |

Learning status: FAIL ("learning limited", 9 conversions). Frequency 1.12–1.30, so not fatigue.

**Diagnosis:** the creative is doing its job (5 % CTR is the best in all three accounts) and the form converts normally
once seen (6 % of landing-page viewers). **Four out of five people who click never register a landing-page view.** The
same collapse shows on the retargeting union (warm traffic, same destination): 49 outbound clicks → 16 LPVs (33 %), and
on C2-2-d 9 → 3 (33 %). So the problem sits between the click and the first paint of justnow.life/book-now on a phone
inside the Facebook/Instagram in-app browser: page weight / time to first paint, a redirect, or a PageView pixel that
fires late or not at all. It is not a C1 creative problem and not a budget problem. (The page could not be fetched from
this environment — DNS to justnow.life is blocked here — so the Webflow read in §1c and the owner's own PageSpeed test
are the confirmation steps.)

### 1b. Creative and message audit (live ads, 7-day spend share)

| Ad | Spend share | Copy / CTA | LPV ÷ clicks | Leads | Verdict |
|---|---|---|---|---|---|
| C1-1-d "Stove-grease video, AR (control)" 120252109342810312 | 79 % | Arabic copy of the *cabinets* post ("لحد إمتى هتفضلي تأجلي تنظيف جوة الخزائن…") ending with **"ابعتي كلمة مطبخ على الواتساب"** — a WhatsApp instruction on an ad that sends people to the website; no headline, no CTA button (boosted organic post) | 17 % | 5 @ 92.33 | message/destination mismatch; carries the account |
| C1-1-b "Same kitchen, before-after, EN+AR (challenger)" 120252107434020312 | 6 % | Arabic customer-testimonial copy + 30 hashtags, CTA LEARN_MORE, video on Page 503162459555897 | 37 % | 2 @ 17.14 | best lead efficiency; tiny sample |
| C1-1-a "Stove-grease reel, AR (control)" 120252107427390312 | 7 % | English copy "Book in 1 minute: **link in bio** (justnow.life/book-now)", CTA BOOK_TRAVEL | 57 % | 0 | Instagram-organic copy reused on a link ad |
| C1-1-e "Cabinets video, postponed chore (challenger)" 120252109350130312 | 4 % | "Watch the grease melt… **link in bio**", CTA BOOK_TRAVEL | 31 % | 0 | same |
| Studio feedback 120252227059520312 (moved in 9 Oct) | 4 % | the only copy written for the website ("Choose your service and area, see your price, and request your booking online"), headline "Book your deep clean online", CTA BOOK_TRAVEL | 40 % | 0 | right message, 481 impressions only |

Three of five ads tell people to use "link in bio" or WhatsApp; four of five have no headline; the button type is
BOOK_TRAVEL (renders as "Book now", but it is the travel variant). None of the copy mentions the price range or the
"see your price before booking" promise that the booking page actually delivers.

### 1c. Landing page — could not be inspected from this session

justnow.life is not reachable from this environment (DNS blocked) and it is not on the connected Webflow account (the
only Webflow site there is "Neighborhood Fix & Install"). Three checks for the owner, each takes minutes and settles the
diagnosis:

1. **PageSpeed Insights, mobile**, on https://www.justnow.life/book-now — note LCP and total page weight. Anything above
   LCP 4 s on a mid-range Android explains an 80 % click-to-view loss on its own.
2. **Meta Pixel Helper** (Chrome extension) on the same URL — PageView must fire on load without interaction; Lead must
   fire on submit. If PageView fires only after a consent click or a language choice, the "landing page views" metric
   under-counts and the real leak is smaller than it looks (then the AED 83/lead cost is the real problem, not the leak).
3. **Open the ad link on a phone from the Facebook app** (the ad's URL with its utm parameters) and count redirects /
   seconds to first paint; if the site redirects utm → canonical → /ar or /en, each hop loses in-app-browser users.

### 1d. Challenger plan (proposal; no write without approval)

**Fix the leak first (owner / developer, outside Meta):**
1. Mobile PageSpeed test of /book-now; target LCP < 2.5 s inside the in-app browser (compress hero media, defer scripts,
   no autoplay video above the form).
2. Confirm the Meta Pixel base code is in `<head>` and PageView fires before any consent gate; confirm the Lead event
   fires on form submit (7 leads in 7 days proves it fires sometimes).
3. Check the ad URL path for redirects (utm → canonical → language redirect): each hop costs in-app-browser users.

**Then the creative challengers (two new ads inside C1-1, budget unchanged at AED 84):**
- **C1-1-f "See your price before you book" (EN+AR, video A-EN 2163113240903678 or the before-after video):** primary
  text leads with the page promise — "Choose your area and service, see the price, book in one minute. Kitchens from
  AED 249, everything included, pay after the job." Headline "See your price, book in 1 minute". CTA BOOK_NOW (not
  BOOK_TRAVEL). Arabic version: "اختار منطقتك والخدمة، شوف السعر، واحجز في دقيقة. المطبخ من 249 درهم."
- **C1-1-g "Same kitchen, before/after" re-cut for the website:** the current best lead-efficiency video with new copy
  (no hashtags, no "link in bio"), headline "Book online, pay after the job", CTA BOOK_NOW, link to /book-now.
- Pause the two "link in bio" ads (C1-1-a, C1-1-e: 0 leads on AED 70) so spend concentrates on -d, -b, studio and the
  two challengers. Keep -d live until a challenger beats AED 60/lead.

**Observation window and pause rule:** 7 days from the landing-page fix (or from 14 Oct if no fix). Pass = ≥ 3 website
leads at ≤ AED 60 and LPV ÷ clicks ≥ 40 %. If LPV ÷ clicks stays < 30 % after the fix, the destination is the problem
whatever the creative; if it recovers but leads stay at zero after AED 250, **propose PAUSE of C1** and move its AED 84
to the union retargeting (which converts the same page at 33 % LPV and AED 40–78/lead).

## 2. C3 — jn 120250020646250073 "C3 WhatsApp Bookings" (CONVERSATIONS → WhatsApp)

### 2a. Evidence (last 7 days)

| Ad set | Targeting | Spend | Conversations | CPA | CPM | CTR |
|---|---|---|---|---|---|---|
| C3-1 Women 25+ | 10-mile pin Sharjah + customer list 889 + LAL expansion, women only | 174.40 | 24 | 7.27 | 33.1 | 1.79 % |
| C3-2 Arabic speakers 25+ | 10-mile pin Dubai, Arabic locale, age cap 46, interests Online shopping + Engaged Shoppers + **work position Teacher** | 154.76 | 25 | 6.19 | 34.9 | 2.68 % |
| C3-3 LAL 1 % customers | 10-mile pins Dubai + Ajman, Parents + Engaged Shoppers | 54.74 | 6 | 9.12 | 27.1 | 2.08 % |
| C3-4 Broad 25+ (PAUSED 9 Oct) | 10-mile pin Dubai, Jewelry/Luxury interests | 292.19 | 40 | 7.30 | 33.8 | 2.15 % |

Same creative assets in the mature jn campaigns, same 7 days:

| Ad (campaign) | Spend | Conversations | CPA | CPM | CTR |
|---|---|---|---|---|---|
| "Arabic stove grease video" (5158, B Arabic speakers Sharjah+Ajman, emirate-level geo) | 67.82 | 22 | **3.08** | **16.1** | 2.61 % |
| "Sticky kitchen video" (5158, A Sharjah city families) | 187.20 | 47 | 3.98 | 14.6 | 1.78 % |
| "Creator reel 2" (5158, A) | 203.38 | 63 | 3.23 | 25.4 | 2.88 % |
| "New Sales Ad" (New Sales, Copy B) | 311.14 | 89 | 3.50 | 16.4 | 1.56 % |

The stove-grease reel converts at AED 3.08 in 5158 and AED 6–7 in C3 with the same CTR; conversation rate per click is
healthy in C3 (24 conversations on 39 clicks). **The 2× cost is the CPM (27–35 vs 15–17), i.e. the auction price of
10-mile custom-location pins stacked with interests, behaviours, a work position and an age cap, with Advantage
audience on top.** C3's C3-1-b and C3-4-c "POV team just left your kitchen" ads are WITH_ISSUES (not delivering).

### 2b. What a creative plan can and cannot do here

Rotating creative at the same CPM moves the CPA from ≈ 7 to perhaps ≈ 5.5 (the best C3 creative, cabinets reel AR, is
at 6.10; the POV challenger did 8.04). Reaching the 5158 level (≈ 3) needs the CPM to come down, which is targeting.
Both are proposed; the owner decides which to approve:

**Creative challengers (inside C3, budget unchanged at AED 90):**
- Add "Creator reel 2" (video 4303960699820816, AED 3.23 in 5158) and "Top creator reel" (1732956274575988) to C3-1 and
  C3-2 as challengers — they are the account's proven WhatsApp converters and are not in C3 today.
- Keep C3-2-b cabinets reel AR (6.10) and C3-1-a stove-grease reel AR (7.27) as controls; pause the two WITH_ISSUES POV
  ads and the three near-zero-delivery duplicates (C3-2-a/c/e, C3-3-c) so the ad sets stop fragmenting.
- New hook test (one ad): first 2 seconds = greasy stove close-up with the Arabic overlay "كنت مفكرة إن البوتاجاز
  نضيف؟" (the line that already carries the best Arabic CTR), then the steam reveal; same WhatsApp CTA.

**Targeting fix (the lever that actually reaches AED 3–4):** replace the 10-mile pins with emirate-level regions as in
5158 (Dubai / Sharjah / Ajman), drop the interest, behaviour and work-position stacks and the age cap at 46, keep the
customer exclusion. One targeting edit per ad set (force-pauses → re-activate), owner-present.

**Decision rule:** 7 days after approval. If C3's CPA is still > AED 5.50 with the challengers live, C3 duplicates what
5158 already does better → propose folding C3's AED 90 into 5158 and pausing C3.
