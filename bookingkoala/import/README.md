# BookingKoala import pack (generated 2026-10-23)

Flat files generated from `JustNow-BookingKoala-Setup.xlsx` so each admin screen
can be filled by copy-paste or CSV import, in the order of sheet "1 Setup steps".

| File | Admin screen (step) | Content |
|---|---|---|
| `areas_Zone_A.txt` … `areas_Zone_E.txt` | Settings > Locations > zip/postal codes (steps 3-4) | One area name per line, ready to paste into the location's code box. Area name is used as the code. |
| `service_areas.csv` | same, with emirate, Arabic name, aliases and notes | 338 areas, one zone each. Abu Dhabi / Al Ain are excluded (not bookable). |
| `packages.csv` | Services > pricing variables (steps 5-8) | 105 rows: service, home size, zone, order, label, providers, duration hours, price AED, minimum flag. |
| `hours_and_rules.csv` | Settings > Business hours / booking rules (step 9, 11) | Working hours, arrival windows, notice, horizon, recurring OFF. |
| `texts_en_ar.csv` | Service descriptions, policies, confirmation message (step 12) | English and Arabic texts side by side. |

Checks (from the data, must match what BookingKoala shows after setup):

* Al Majaz is Zone A: Kitchen package 1 = 2 cleaners x 3 h = AED 249.
* Al Suyoh is Zone E: Kitchen package 1 = 2 cleaners x 3 h = AED 309.
* Kalba is Zone D: Kitchen package 1 = 2 cleaners x 4 h = AED 439 (no 3-hour option).
