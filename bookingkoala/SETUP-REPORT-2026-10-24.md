# BookingKoala setup report – Just Now For Building Cleaning Services

Date: 24 October 2026
Account: https://justnowforbuildingcleaningservicescollc.bookingkoala.com
Public booking page: https://justnowforbuildingcleaningservicescollc.bookingkoala.com/booknow

## 1. What is configured and verified

| Area | Status | Details |
|---|---|---|
| Store info | Done | Name, AED, Asia/Dubai, support phone 050-767-7282, payment "Pay on completion (cash, card link or bank transfer)", card payments off, admin logo uploaded (225×50). |
| Locations | Done | Name-based. 7 zone locations the customer picks from a dropdown: Sharjah City (A), Ajman (A), Dubai (1) Deira/Bur Dubai side (B), Umm Al Quwain (B), Dubai (2) Marina/Jumeirah side (C), Sharjah Suburbs (E), Ras Al Khaimah/Fujairah/far areas (D). Each name lists its main areas. |
| Services | Done | Kitchen deep cleaning, Full house deep cleaning. BookingKoala sample services archived. |
| Prices | Done, verified on the live form | 105 package options (21 per zone). Kitchen: 3 options (2 cleaners × 3/4/5 h; zone D 4/5/6 h). Home: Studio, 1 BHK, 2 BHK, 3 BHK, Villa 4 BR, Villa 5+ BR, 3 hour options each. Every option is visible only for its zone's location, and the price is in the option name, e.g. "2 cleaners × 3 hours – AED 249". Order fixed (kitchen first, then Studio → Villa). |
| Frequency / extras | Done | One-time only. No extras, no recurring. |
| Booking spots | Done, verified | Every day: 08:00–12:00, 12:00–16:00, 16:00–21:00 arrival windows. Max 3 jobs per window per day (placeholder, see decisions). |
| Scheduling | Done | Spots do not depend on provider calendars. Provider assignment is manual: every online booking lands in Bookings → Unassigned and you assign a team. Booking horizon 1 month. Same-day booking allowed up to 2 hours before the window start. |
| Customer form | Done | Phone required; secondary email/phone hidden; provider names and sample reviews hidden from customers; payment summary shows the total. |
| Policies | Done | Terms & Conditions and Privacy Policy pop-ups replaced with Just Now texts (prices total, arrival window, pay on completion, reschedule/cancellation rules, 24-hour redo guarantee). |
| Cancellation fee | Off | BookingKoala can only auto-charge a card. With pay-on-completion the fee cannot be collected automatically, so the default "AED 50" fee was switched off; the policy is stated in the Terms. Customers can cancel/reschedule from their account; a cancellation reason is required. |
| Notifications | Set, waiting for you | Sender/admin/reply-to = justnow.cs@gmail.com, display name "Just Now For Building Cleaning Services". BookingKoala sent a verification email to justnow.cs@gmail.com: open it and click the activation link, otherwise no booking emails go out. |
| Provider | Created | "Just Now Team 1" (justnow.cs+team1@gmail.com, no invitation sent). Enabled for all locations, services and packages. Rename or add your real teams under Providers. |
| Test bookings | Done and removed | 3 live test bookings placed through the public form (Sharjah City kitchen 249, Sharjah Suburbs kitchen 309, far areas 2×4 h 439). All reached the confirmation page with the right price, date and arrival window, then were cancelled and the test customers deactivated. |

## 2. How a booking works now

1. Customer opens /booknow, picks the location (zone), the service and the package; the price shows immediately.
2. Picks a day in the calendar and one of the three arrival windows (max 3 bookings per window).
3. Enters name, phone, email, address, notes, ticks the terms and presses Save Booking. Payment method is pay on completion.
4. The booking appears in Bookings → Unassigned. You assign a team ("Just Now Team 1" or any you add) and the customer gets the confirmation email once notifications are activated.
5. A returning customer with the same email is asked to log in (BookingKoala rule). New customers get a "set your password" page after booking.

## 3. Decisions you should confirm or change

- Capacity: 3 jobs per arrival window per day (9 per day). Change in Settings → Booking Spots → Day settings → Edit each window → Max jobs per spot (then Apply to all days).
- Same-day cut-off: BookingKoala counts hours before the window start, so the 16:00–21:00 window closes for same-day booking at 14:00, not 18:00. Change in Settings → General → Store Options → Customer → Bookings → "limit how early a customer can book a same day appointment".
- Zone of Damac Hills 2 and "Dubailand" alone, and any area not in the location names: customers pick the nearest zone; the WhatsApp assistant knows the full 334-area list.
- Email identity: booking emails will come from justnow.cs@gmail.com. If you prefer info@justnow.life, change it in Settings → Notifications → Email settings and verify again.

## 4. Manual steps left for you (each takes about a minute)

1. Gmail justnow.cs@gmail.com: click the BookingKoala "verify email" link.
2. Website builder header: Settings → Design Forms & Website → Website Builder & Themes → Customize Theme → click the "YOUR LOGO" box top-left → Edit → hover the logo → Replace → upload `bookingkoala/automation/jn-logo-450x100.png` → Save & Publish. Same for the footer logo. (The admin-panel logo is already set; the website header logo is a separate setting that the automation could not reach.)
3. Website builder phone: in the same builder, the "Give Us A Call +01 123 456 7890" box in the home page and footer: hover it → Edit → type +971 50 767 7282 → Save & Publish.
4. Providers: rename "Just Now Team 1" and add your other teams (Providers → Add → Add Individual or Add Team), then Settings → Scheduling can stay as it is (manual assignment).
5. Optional: Settings → remove BookingKoala sample data ("Test Provider", "Test Team", "Member One/Two", "Test Customer"). BookingKoala has a "flush test data" option in the account settings; or deactivate them from Providers / Customers.
6. Optional: the BookingKoala home page still shows the template marketing text ("Thanks For Stopping By", "Cash Free Payment", referral program). Link customers straight to /booknow from the website and WhatsApp so they never see it, or edit it in the builder.

## 5. Connect it to the website and WhatsApp

- Website booking page (justnow.life/book-now): paste this embed code into the page, or make the "Book now" button open the link directly:

```html
<iframe src="https://justnowforbuildingcleaningservicescollc.bookingkoala.com/booknow?embed=true" style="border:none;height:1000px" width="100%" scrolling="no"></iframe>
<script src="https://justnowforbuildingcleaningservicescollc.bookingkoala.com/resources/embed.js" defer></script>
```

- WhatsApp assistant: the LINK in the respond.io prompt stays https://www.justnow.life/book-now?utm_source=whatsapp as long as that page embeds the form above. If you want to skip the website, replace LINK with https://justnowforbuildingcleaningservicescollc.bookingkoala.com/booknow (prompt is at the 10,000-character limit, so the URL swap must be character-neutral or trimmed elsewhere).
- Prices: the booking page is now the single place with prices; the website pages should stay price-free as agreed.

## 6. Price table loaded (AED, first / second / third package)

| Size | Cleaners × hours | A | B | E | C | D |
|---|---|---|---|---|---|---|
| Kitchen / Studio | 2 × 3/4/5 h (D: 4/5/6 h) | 249/329/419 | 279/369/459 | 309/409/509 | 329/439/549 | 439/549/659 |
| 1 BHK | 3 × 3/4/5 h | 379/499/629 | 409/549/689 | 459/609/759 | 499/659/829 | 499/659/829 |
| 2 BHK | 3 × 4/5/6 h | 499/629/749 | 549/689/819 | 609/759/909 | 659/829/989 | 659/829/989 |
| 3 BHK | 4 × 4/5/6 h | 669/839/999 | 729/919/1099 | 809/1009/1209 | 879/1099/1319 | 879/1099/1319 |
| Villa 4 BR | 6 × 4/5/6 h | 999/1259/1499 | 1099/1379/1649 | 1209/1519/1819 | 1319/1649/1979 | 1319/1649/1979 |
| Villa 5+ BR | 8 × 5/6/7 h | 1679/1999/2349 | 1839/2199/2569 | 2019/2419/2829 | 2199/2639/3079 | 2199/2639/3079 |

Zones: A = Sharjah city, Ajman. B = Dubai Deira/Bur Dubai side, Umm Al Quwain. C = Dubai Marina/Jumeirah side. E = Sharjah suburbs. D = Ras Al Khaimah, Fujairah, Kalba, Khorfakkan, Dhaid, Mleiha, Madam, Masfout, Manama, Falaj Al Mualla.

## 7. Re-running the automation

See `bookingkoala/automation/README.md`. The scripts log in with your BookingKoala email and password passed as environment variables; nothing is stored in the repository.

## ملخص بالعربي

- صفحة الحجز جاهزة ومجربة: الزبون يختار المنطقة (7 مناطق تمثل الزونات A–E) والخدمة والباقة، يشوف السعر فوراً، يختار اليوم وفترة الوصول (8–12، 12–4، 4–9)، يكتب بياناته ويحجز. الدفع بعد الخدمة.
- كل حجز جديد يظهر في Bookings → Unassigned وأنت تعيّن الفريق.
- 105 سعر مرفوعة ومطابقة للجدول المعتمد، والشروط والأحكام وسياسة الخصوصية بنصوص جست ناو.
- مطلوب منك: (1) فتح إيميل التفعيل من BookingKoala على justnow.cs@gmail.com، (2) رفع اللوجو في هيدر الموقع من الـ Website Builder، (3) تغيير رقم الهاتف الوهمي في الهيدر/الفوتر، (4) تسمية الفرق الحقيقية في Providers، (5) ربط زر Book now في موقع justnow.life بكود الـ embed أعلاه.
- قرارات تحتاج تأكيدك: 3 حجوزات لكل فترة يومياً، وحد الحجز في نفس اليوم ساعتين قبل بداية الفترة.
