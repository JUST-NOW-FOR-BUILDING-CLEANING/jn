# BookingKoala setup report - 23 Oct 2026

## Status: NOT CONFIGURED - browser access was not available

This session ran in a cloud container. The Claude in Chrome tools
(`mcp__claude-in-chrome__*`, including `tabs_context_mcp`) were not present in the
session and no Chrome connector is attached to this workspace, so the logged-in
BookingKoala admin tab on the owner's computer could not be reached.

Nothing was entered in BookingKoala. No screenshots exist. No test bookings were made.
The justnow.life website and respond.io were not touched.

To run the setup, start the same task from a session that runs on the owner's
computer (Claude Desktop app, or `claude remote-control` in this repo folder), with
the BookingKoala admin open and logged in in Chrome.

## What was prepared in this branch

- `bookingkoala/paste-lists/Zone-A.txt` ... `Zone-E.txt`: one file per zone with the
  comma-separated area list ready to paste into the location's area / zip-code field,
  plus a detail table (emirate, Arabic name, aliases, notes).
  Counts from the approved sheet: Zone A 101, Zone B 81, Zone C 85, Zone D 61, Zone E 10,
  not online 1 (Abu Dhabi / Al Ain). 338 bookable areas in total.
- Data cross-check of `bookingkoala/JustNow-BookingKoala-Setup.xlsx` sheet 2:
  105 price rows, 3 packages for every size in every zone, Zone D has no 3-hour package.
  The three test expectations match the sheet: Al Majaz = Zone A kitchen 2 x 3 h AED 249,
  Al Suyoh = Zone E kitchen 2 x 3 h AED 309, Kalba = Zone D kitchen first package 2 x 4 h AED 439.

## Checklist for the session that gets browser access (sheet 1, steps 3-13)

1. Settings -> Locations: create Zone A, Zone B, Zone C, Zone D, Zone E (internal names).
2. Per location, paste the area list from `paste-lists/Zone-X.txt`. If BookingKoala requires
   postal codes, use the area name as the code and record that in this report.
3. Services: "Kitchen deep cleaning" (no size question) and "Full house deep cleaning"
   (Home size: Studio, 1 BHK, 2 BHK, 3 BHK, Villa 4 BR, Villa 5+ BR). No sofa / mattress /
   carpet / commercial services. Descriptions EN + AR from sheet 5.
4. Packages: per size a "Package" dropdown with the 3 rows from sheet 2, price per location,
   duration = hours, providers = cleaners. Package 1 listed first. Hide the 3-hour option for
   Zone D. No "from" prices, no VAT line, no discounts, recurring / frequency OFF, tips OFF.
5. Hours: every day 08:00-21:00 Asia/Dubai; arrival windows 08-12, 12-16, 16-21; minimum
   notice 2 h; same-day allowed until 18:00; booking horizon 30 days.
6. Customer form: name, mobile (+971), email (optional), emirate, area, building / villa +
   apartment, notes "What should the team focus on?". No account required.
7. Payment: pay later / no card, no deposit.
8. Texts: cancellation policy, confirmation message, price note, quality guarantee,
   "not bookable online" note, EN + AR from sheet 5.
9. Notifications: customer confirmation + 24 h reminder; owner email Customer.care@justnow.life;
   Google Calendar sync to "Cleaning Services Schedule" if the plan offers it.
10. Screenshot after each section into `bookingkoala/screenshots/`.
11. Three test bookings "TEST - DO NOT CONFIRM" (Al Majaz kitchen 249, Al Suyoh kitchen 309,
    Kalba kitchen first option 2 x 4 h 439), then delete them. Warn before any button that
    opens a browser confirm dialog.

## Owner inputs still needed (do not guess)

- Number of cleaners available per day (capacity). Leave the BookingKoala default until answered.
- Travel buffer between jobs (sheet says 60 min as a placeholder). Leave the default until answered.
- Damac Hills 2 (Akoya): currently Zone C in the sheet. Confirm or change.
- "Dubailand" alone: currently Zone C. Decide whether the form should ask which side instead.

## Branch note

The task text named branch `claude/epic-carson-p0nj97`; this session was assigned
`claude/eager-tesla-8kywxv`, so the work is pushed there.
