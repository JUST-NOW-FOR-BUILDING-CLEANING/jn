# BookingKoala setup report, 23 Oct 2026

## Status: NOT configured. Blocked on browser access.

The configuration run was attempted from a Claude cloud session. Two things made it impossible from there:

1. The Claude in Chrome tools were never available in the session, even after the owner connected Chrome. A cloud container cannot attach to the Chrome extension on the owner's computer.
2. Outbound connections from the container to bookingkoala.com and support.bookingkoala.com were refused by the network policy, so neither the admin nor the help pages could be reached directly.

Nothing was changed in the BookingKoala account. No test bookings were made. No screenshots exist (the `screenshots/` folder stays empty until the admin run happens).

## What was produced instead

`bookingkoala/import/` holds the workbook data flattened for the admin screens, in the order of sheet "1 Setup steps":

* `areas_Zone_A.txt` to `areas_Zone_E.txt`: area names, one per line, to paste into each Zone location's postal-code box (area name used as the code, as the sheet instructs).
* `service_areas.csv`: the same 338 areas with emirate, Arabic name, aliases and notes.
* `packages.csv`: all 105 prices with providers and duration.
* `hours_and_rules.csv` and `texts_en_ar.csv`: business hours, booking rules and the English and Arabic texts.

Data checks against the three required test bookings pass on the source data:

| Test | Zone | First package | Price |
|---|---|---|---|
| Al Majaz, kitchen | A | 2 x 3 h | AED 249 |
| Al Suyoh (Sharjah), kitchen | E | 2 x 3 h | AED 309 |
| Kalba, kitchen | D | 2 x 4 h | AED 439 |

## How to run the admin configuration

Run the original task from a session on the owner's own computer (Claude Desktop app, or `claude remote-control` in this repo folder) with the Chrome extension connected. Follow sheet 1 steps 3 to 13, using the import pack above, then steps 14 (three test bookings, delete afterwards). Step 15 (go-live) stays out of scope.

## Owner inputs still needed

* Number of cleaners available per day (capacity). Leave the BookingKoala default until answered.
* Travel buffer between jobs. The sheet suggests 60 minutes; leave the default until confirmed.
* Damac Hills 2 (Akoya): currently Zone C in the sheet. Confirm or change.
* "Dubailand" alone: the sheet lists "Dubailand (Arabian Ranches / Global Village side)" as Zone C and the Silicon Oasis side (DLRC, Liwan, Wadi Al Safa, Queue Point, Skycourts) as Zone B. Decide whether a plain "Dubailand" entry should exist and, if so, which zone, or whether the form should ask which side.

## Fields that may not map 1:1 in BookingKoala (to verify during the admin run)

* Locations normally key on postal codes. The UAE has none, so the area name is the code. Check that BookingKoala accepts text codes and that the customer-facing field can be labelled "Area".
* Zone D's missing 3-hour package needs a per-location rule or a separate package set; confirm which the plan supports.
* Arabic texts: enter only if the plan supports a second language; otherwise keep English and note it.
* Google Calendar sync and SMS reminders depend on the plan; record what is available.

## Branch note

The task text named branch `claude/epic-carson-p0nj97`; this session was assigned `claude/confident-ritchie-k8x2yy` by the harness and pushes there.
