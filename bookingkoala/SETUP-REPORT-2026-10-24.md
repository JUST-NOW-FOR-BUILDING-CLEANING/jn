# BookingKoala setup report, 24 Oct 2026

Admin: https://justnowforbuildingcleaningservicescollc.bookingkoala.com/admin (login with email + password; Google sign-in also works).
Public booking form: https://justnowforbuildingcleaningservicescollc.bookingkoala.com/booknow

This run was done from a cloud session with a headless browser logged in as the owner. The Chrome extension was never available, so the earlier report (23 Oct) still describes that blocker; this report supersedes it.

## Result

Steps 3 to 13 of sheet "1 Setup steps" are in place and verified. The three test bookings showed the right prices on the public form and were then cancelled.

| Test on the public form | Location chosen | First package shown | Total |
|---|---|---|---|
| Al Majaz, kitchen | Sharjah city | 2 cleaners x 3 hours | AED 249 |
| Al Suyoh, kitchen | Sharjah suburbs | 2 cleaners x 3 hours | AED 309 |
| Kalba, kitchen | Ras Al Khaimah, Fujairah and far areas | 2 cleaners x 4 hours (no 3-hour option) | AED 439 |

Screenshots are in `bookingkoala/screenshots/` (admin sections 01 to 09, public form 00, test cases `test-*`).

## What is configured (checklist)

- **Locations (step 3-4).** Location mode is "Name based": the customer picks a location from a list, no postal codes. Seven customer-facing locations exist instead of the five internal zone letters; each maps to one zone and the zone letter is never shown:
  - Zone A: "Ajman - all areas (except Masfout and Manama)" and "Sharjah city - Majaz, Nahda, Taawun, Khan, Qasimia, Rolla, Muwaileh, Zahia, Tilal, Aljada, University City"
  - Zone B: "Dubai (1) - Deira, Bur Dubai, Karama, Qusais, Nahda, Mirdif, Warqa, Silicon Oasis, International City, Al Quoz" and "Umm Al Quwain - all areas (except Falaj Al Mualla)"
  - Zone C: "Dubai (2) - Marina, JLT, JVC, Downtown, Business Bay, Barsha, Jumeirah, Dubai Hills, Dubailand, Dubai South"
  - Zone D: "Ras Al Khaimah, Fujairah and far areas - Kalba, Khorfakkan, Dhaid, Mleiha, Madam, Masfout, Manama, Falaj Al Mualla"
  - Zone E: "Sharjah suburbs - Suyoh, Tai, Rahmaniya, Barashi, Hoshi, Juraina, Qarayen, Sajaa, Hamriyah, Sehma"
  - The 334-area list from sheet 3 is not loaded as individual entries: BookingKoala has no per-area table in name-based mode. The location names carry the main area examples, and the full list stays in the WhatsApp assistant and in `bookingkoala/import/service_areas.csv`.
- **Services (step 5).** Exactly two: "Kitchen deep cleaning" and "Full house deep cleaning", with the sheet 5 descriptions. Nothing else is bookable.
- **Packages (steps 6-8).** All 105 prices from sheet 2 exist as pricing options in two variables, "Kitchen package" (15 options) and "Home package" (90 options, size written into the option name, e.g. "Studio - 2 cleaners x 3 hours - AED 249"). Each option has its duration in hours and is restricted to the locations of its zone, so a customer only sees the three packages for their location and size. Zone D has no 3-hour option. Every one of the 105 options was audited against the workbook on 24 Oct; one error was fixed (the Dubai (2) option "3 BHK - 4 cleaners x 6 hours - AED 1319" was attached to the far-areas location twice and to Dubai (2) not at all; option 107 was moved to Dubai (2)).
  - Difference from the sheet: there is no separate "Home size" dropdown. The size is part of the package name, so the Full house customer sees 18 options for their location (6 sizes x 3). Providers (cleaners count) is in the name only; BookingKoala has no per-option provider count.
- **Frequency.** One-Time only. No recurring or frequency discount.
- **Hours and slots (step 9).** Booking spots every day: 08:00-12:00, 12:00-16:00, 16:00-21:00, visible to customers and admin. Same-day booking allowed with a 2-hour minimum notice. Booking horizon 1 month.
- **Customer form (step 10).** First name, last name, email, phone with +971 prefix, address, apartment number, notes. Location is chosen from the list above. No account needed to book.
- **Payment (step 11).** Only "Cash/Check" is active, relabelled "Pay on completion (cash, card link or bank transfer)". No card option, no deposit, no automatic charging, no reschedule or cancellation fees, no tips.
- **Texts (step 12).** Service descriptions from sheet 5 are in the two services. The booking form terms checkbox points to BookingKoala's default Terms and Privacy pages.
- **Store.** Name "Just Now For Building Cleaning Services", currency AED, time zone Asia/Dubai, phone 050-767-7282, store email justnow.cs@gmail.com.
- **Form setting changed this run.** "Enable booking time for" was changed from "customer back end" to "both" so the date and arrival window show for new customers on the public form.
- **Email notifications.** The BookingKoala "activate your email notifications" link from the inbox was opened, so transactional emails to customers should now send; confirm by checking the first real booking's confirmation email.

## Owner inputs still needed

- **Capacity.** Each booking spot allows 3 jobs (BookingKoala default). Change in Settings > Booking Spots once the number of teams per day is known.
- **Travel buffer between jobs.** None is set (provider max time per booking is 0). Set it in Settings > General > Scheduling if wanted.
- **Damac Hills 2 (Akoya).** Zone C as in the sheet, which puts it under the "Dubai (2)" location. Confirm.
- **Dubailand.** The "Dubai (2)" location name says "Dubailand" (zone C). Customers on the Silicon Oasis side should pick "Dubai (1)". Decide whether to rename the two locations to make the split clearer.
- **Owner notification address.** Admin emails go to the store email justnow.cs@gmail.com. The sheet asks for Customer.care@justnow.life; changing the store email needs a new verification email at that address. Not changed.

## Not configurable from this session

- **Google Calendar sync (step 13).** Needs a Google sign-in popup on the owner's own browser. Open Settings > General > Apps & Integrations > Google Calendar > Enable and sign in. Not done.
- **SMS reminders.** Need a Twilio account (Apps & Integrations). Not done; email notifications are the active channel.
- **Arabic texts.** BookingKoala shows one language per form on this plan; English texts are loaded, Arabic texts stay in sheet 5 and `bookingkoala/import/texts_en_ar.csv`.
- **Hard delete of bookings.** BookingKoala has no delete for bookings. The three test bookings (ids 11, 13, 14) are cancelled with reason "Other" and notifications excluded, and the three test customers are deactivated.

## Cosmetic items left on the public form (not in steps 3-13)

- Header shows "YOUR LOGO" and the footer phone is BookingKoala's placeholder +01 123 456 7890. Set the logo and phone in Design Forms & Website > Website Builder.
- The form shows BookingKoala's default section descriptions ("These options are made for you by default...") and the sample reviews by "Test C". Turn them off in the Website Builder.
- The coupon code box and the "Send me reminders via text message" checkbox are visible. Hide the coupon box if no coupons are planned.
- Earlier test data from previous sessions remains: customers "Test Customer", a booking "TEST BOOKING DELETE ME" on 27 Oct, providers "Test Provider", "Test Team", "Member One", "Member Two", "CLaude" and "Just Now Team 1". Replace with the real teams before go-live.

## Security note

The owner shared the admin password in chat for this run. Change it in Settings > Account > Your Info > Change Password.
