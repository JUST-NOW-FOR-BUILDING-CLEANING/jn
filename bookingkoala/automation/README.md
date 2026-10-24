# BookingKoala automation scripts

Playwright scripts used on 24 Oct 2026 to configure the Just Now BookingKoala account. They drive the admin UI in a headless Chromium; nothing calls private APIs. Credentials are passed as environment variables and the login session is stored in `bk-state.json` (git-ignored).

Requirements: Node 18+, Playwright with Chromium installed globally (`npm i -g playwright && npx playwright install chromium`). Behind a proxy set `HTTPS_PROXY`; the launch options in each script pass it to Chromium.

| Script | Purpose |
|---|---|
| `bklogin.mjs` | `BK_USER=... BK_PASS=... node bklogin.mjs` logs in and saves `bk-state.json`. Run first. |
| `bkdo.mjs` | Generic step runner: `node bkdo.mjs '[{"goto":"/admin/..."},{"click":"Save"},{"eval":"document.title"}]'`. |
| `bkvarsdata.mjs` | The 105 package options (zone → locations, names, prices, hours). Edit prices here. |
| `bkvars.mjs` | Creates every option in `bkvarsdata.mjs` that is not yet logged in `bkvars-log.json` (dependencies: zone locations + service category). |
| `bkorder.mjs --apply` | Drags the pricing options into the intended order and saves priority. |
| `bkspots.mjs [maxJobs]` | Replaces the day's booking spots with the three arrival windows; `bkspots2.mjs` applies Sunday to all days. |
| `bkverify.mjs` | Anonymous check of the public form: lists the options and prices shown for each location. |
| `bkbook.mjs "<location>" "<service>" "<package>" <day> <email> [--submit]` | Walks the public form to the slot step; with `--submit` places a real booking. |
| `bkcleanup.mjs [/admin/bookings/upcoming]` | Cancels bookings named TEST in the calendar (reason Other, notifications off). |
| `bkpopup3.mjs <0|1> <file.html> "<first words>"` | Replaces the Terms (0) or Privacy (1) popup text in the website builder and publishes. `terms.html` / `privacy.html` are the texts used. |
| `bklogo.mjs` | Uploads `jn-logo-225x50.png` as the admin logo (Store Info). `mklogo.mjs` renders the logo files from the Facebook profile picture. |

Known limits: the website builder's header logo and the placeholder phone number could not be changed by script (hover-only controls); do those by hand as described in `../SETUP-REPORT-2026-10-24.md`.
