# BRAND WARM AUDIENCES — why the 25 / 50 / 75 % video audiences are empty, and the proposed fix (nothing created or attached)

Prepared 2026-10-11 ≈ 13:30 Dubai for the owner's brief "Investigate why 25/50/75% video audiences remain below 1,000
despite >14k ThruPlays … Do not attach anything yet; return the exact proposed audience setup first." Read-only.

## 1. Findings

**1a. The Instagram hypothesis is ruled out.** Brand campaign 23860638577100791 delivery since launch (Thu 9 Oct 11:47 →
Sun 11 Oct 12:44 Dubai, breakdown by publisher platform and position):

| Platform / position | Spend | Impressions | Share | ThruPlays | 25 %-plays |
|---|---|---|---|---|---|
| Facebook feed | 69.14 | 27,916 | 59.6 % | 8,261 | 12,732 |
| Facebook Reels | 56.27 | 18,510 | 39.5 % | 5,824 | 9,328 |
| Facebook Stories | 0.53 | 132 | 0.3 % | 55 | 65 |
| Facebook profile feed / Marketplace | 0.01 | 4 | — | 1 | 1 |
| Instagram Reels | 0.78 | 240 | 0.5 % | 63 | 126 |
| Instagram feed / Explore / Stories | 0.21 | 46 | 0.1 % | 12 | 26 |
| **Total** | **126.94** | **46,848** | | **14,216** | **22,278** |

99.4 % of impressions and 99.3 % of ThruPlays happened on Facebook, where Page-video views are exactly what the current
audiences count. The audiences are not starved by Instagram delivery.

**1b. What the current audiences are.** All three (120252228024070312 / 120252228030340312 / 120252228030930312) carry
one Page-wide rule and **no video selection**:

```json
{"inclusions":{"operator":"or","rules":[{"event_sources":[{"type":"page","id":122098309970001876}],
 "retention_seconds":31536000,
 "filter":{"operator":"and","filters":[{"field":"event","operator":"eq","value":"video_view_25_percent"}]}}]}}
```

They were created in that form on 9 Oct because the first attempt (one rule per video, 11 rules) was rejected by Meta
("max 5 rules per audience"). Meta's own documentation for this audience type ([Create a video engagement custom
audience](https://www.facebook.com/business/help/1099865760056389)) says the audience is built from **selected videos
(up to 200)** chosen from a Facebook Page, an Instagram professional account, a campaign or video IDs, and that it counts
views **on Facebook or Instagram**. A Page-wide rule without `video.id` is accepted by the API but is not a form the
product builds, and it is the prime suspect for "below 1,000" after 22k qualifying plays. Secondary factors: size
estimates for audiences not yet used in an ad set lag by 24–48 h, and Audience Network views are never counted
([Troubleshoot video engagement custom audiences](https://www.facebook.com/business/help/288658087296355)) — the brand
ad set does not use Audience Network, so this is not the cause. Status code 441 is not "too small": the healthy
31–37k Instagram-engagers audience carries the same code.

**1c. Comparison.** IG engagers 120251888118190312 (ig_business_profile_all, 365 d) 31.4–36.9k and FB engagers
120241682713780312 (page_engaged/visited/post_interaction/cta/messaged, 365 d) 26.5–31.2k are both sized and ACTIVE —
the engagement-audience pipeline for this Page and IG account works; only the video-rule form is the problem.

## 2. Proposed setup (exact objects, to be created only after the owner's approval; nothing attached)

All on the JN ad account 9147325105346647 (same account as the retargeting layer), subtype ENGAGEMENT, Page source
122098309970001876, retention 365 days as in the brand-layer plan, **one rule per audience with an explicit video list**
(Meta allows up to 200 videos; the 5-rule limit is not touched):

Video IDs on the Just Now Page (all confirmed from the live creatives on 11 Oct):

| Video ID | Used by |
|---|---|
| 2163113240903678 | brand A-EN "Sticky kitchen" (also jn 5158 "Sticky kitchen video") |
| 1622838339212041 | brand A-AR "Stove grease" (also jn 5158 "Arabic stove grease video") |
| 1559790696189996 | brand B "Steam. Precision. Results." |
| 4303960699820816 | brand C "Team montage" (also jn 5158 "Creator reel 2") |
| 890288284018661 | brand D "It feels different" |
| 925115713754619 | brand E v2 "Professional deep cleaning only" |
| 2187572902181730 | brand F "Extractor filter" |
| 1732956274575988 | jn 5158 "Top creator reel" |
| 4535244356773903 | JN C1 "Studio feedback" |
| 2284866958999660 | JN C1 "Stove-grease reel" |
| 3803897336416182 | JN C1 "Cabinets video" |

(T1/T2 and union video IDs can be appended once read; the before-after video 28340961415525425 lives on Page
503162459555897, not on the Just Now Page, so it needs that Page as an extra event source if wanted.)

**A1 — `JN - Video 25% 365d (brand + winners, 11 videos)`**

```json
{"inclusions":{"operator":"or","rules":[{"event_sources":[{"type":"page","id":"122098309970001876"}],
 "retention_seconds":31536000,
 "filter":{"operator":"and","filters":[
   {"field":"event","operator":"eq","value":"video_view_25_percent"},
   {"field":"video.id","operator":"any","value":["2163113240903678","1622838339212041","1559790696189996",
     "4303960699820816","890288284018661","925115713754619","2187572902181730","1732956274575988",
     "4535244356773903","2284866958999660","3803897336416182"]}]}}]}}
```

**A2 — `JN - Video 50% 365d (brand + winners)`** — same rule with `video_view_50_percent`.
**A3 — `JN - Video 75% 365d (brand + winners)`** — same rule with `video_view_75_percent`.

**B — Instagram side (optional, for when IG delivery grows):** there is no Instagram video-view event for custom
audiences; the IG equivalents are engagement-based. The existing `JN - Instagram engagers 365d` already covers it; a
fresher tier is `JN - IG engaged 90d`:

```json
{"inclusions":{"operator":"or","rules":[{"event_sources":[{"type":"ig_business","id":"6574883522599414"}],
 "retention_seconds":7776000,
 "filter":{"operator":"and","filters":[{"field":"event","operator":"eq","value":"ig_business_profile_engaged"}]}}]}}
```

**C — Cross-placement warm layer (later, separate approval):** the retargeting ad set's warm include = A1 OR
`JN - IG engaged 90d` OR FB engagers 365d, with the existing exclusions (confirmed bookings 12 mo, Book Now visitors 14 d,
Lead event 14 d). Not part of this proposal.

## 3. Sequence after approval

1. Create A1–A3 (3 writes, each prompted). Keep the three old audiences untouched until the new ones show a size.
2. Read sizes after 24–48 h (daily scorecard). Expected: A1 ≫ 1,000 (A-EN alone has 19,890 25 %-plays).
3. If A1 is still "below 1,000" after 48 h, the fault is in Meta's population pipeline, not the rule → owner opens a
   Meta Business Support case; fallback warm layer = IG/FB engager audiences (both grow daily).
4. Delete the three empty audiences only after A1–A3 are sized (owner-present).
