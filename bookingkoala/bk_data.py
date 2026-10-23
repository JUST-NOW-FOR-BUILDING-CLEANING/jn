ARABIC = {
 "Al Majaz":"المجاز","Al Nahda":"النهدة","Al Nahda (Sharjah)":"النهدة","Al Qusais":"القصيص","Al Mirgab":"المرقاب","Al Nuaimiya":"النعيمية",
 "Al Rashidiya":"الراشدية","Al Barsha":"البرشاء","Dubai Marina":"المرينا","Deira":"ديرة","Bur Dubai":"بر دبي","Al Karama":"الكرامة",
 "Muwaileh":"مويلح","Al Taawun":"التعاون","Al Khan":"الخان","Al Mowaihat":"المويهات","Al Jaddaf (Jaddaf)":"الجداف","Al Muraqqabat":"المرقبات",
 "Al Suyoh (السيوح)":"السيوح","Silicon Oasis":"واحة السيليكون","Arabian Ranches":"المرابع العربية","Al Rigga":"الرقة","Naif":"نايف",
 "Al Murar":"المرر","Muteena":"المطينة","Hor Al Anz":"هور العنز","Abu Hail":"أبو هيل","Al Mamzar":"الممزر","Al Mamzar (Sharjah)":"الممزر",
 "Al Mankhool":"المنخول","Oud Metha":"عود ميثاء","Zabeel":"زعبيل","Garhoud":"القرهود","Nad Al Hamar":"ند الحمر","Ras Al Khor":"رأس الخور",
 "Muhaisnah":"محيصنة","Al Warqa":"الورقاء","International City":"المدينة العالمية","Al Quoz":"القوز","Satwa":"السطوة",
 "Business Bay":"الخليج التجاري","Umm Suqeim":"أم سقيم","Al Sufouh":"الصفوح","Palm Jumeirah":"نخلة جميرا","Al Furjan":"الفرجان",
 "Jebel Ali":"جبل علي","Meydan":"ميدان","Hatta":"حتا","Jumeirah":"جميرا","Al Qasimia":"القاسمية","Al Ghuwair":"الغوير","Rolla":"رولا",
 "Abu Shagara":"أبو شغارة","Al Nabba":"النباعة","Al Khaledia":"الخالدية","Al Yarmook":"اليرموك","Al Rifaa":"الرفاع","Al Nasserya":"الناصرية",
 "Al Zahia":"الزاهية","Al Tai":"الطي","Al Rahmaniya":"الرحمانية","Al Hamriyah":"الحمرية","Mleiha":"مليحة","Al Dhaid":"الذيد","Al Madam":"المدام",
 "Kalba":"كلباء","Khorfakkan":"خورفكان","Al Jurf":"الجرف","Al Hamidiya":"الحميدية","Al Rawda":"الروضة","Al Rumailah":"الرميلة","Al Zorah":"الزوراء",
 "Masfout":"مصفوت","Manama":"المنامة","Falaj Al Mualla":"فلج المعلا","Al Jazirah Al Hamra":"الجزيرة الحمراء","Al Rams":"الرمس",
 "Masafi":"مسافي","Dibba Al Fujairah":"دبا الفجيرة","Dubailand (Arabian Ranches / Global Village side)":"دبي لاند",
}

ALIAS = {
 "JVC":"Jumeirah Village Circle","JVT":"Jumeirah Village Triangle","JLT":"Jumeirah Lake Towers","JBR":"Jumeirah Beach Residence",
 "Silicon Oasis":"DSO, Dubai Silicon Oasis","Production City (IMPZ)":"IMPZ","Dubai Investment Park":"DIP",
 "Dubailand Residence Complex (DLRC)":"DLRC","Dubai Marina":"Marina","Satwa":"Al Satwa","Garhoud":"Al Garhoud",
 "Muhaisnah":"Muhaisnah 1-4","Al Nahda":"Al Nahda 1-2","Al Qusais":"Al Qusais 1-5","Al Nuaimiya":"Al Nuaimiya 1-3 / Al Nuaimiyah",
 "Al Mowaihat":"Al Mowaihat 1-3 / Al Mowaihat","Al Rashidiya":"Al Rashidiya 1-3","Al Rawda":"Al Rawda 1-3",
}

EMIRATE_AR = {"Dubai":"دبي","Sharjah":"الشارقة","Ajman":"عجمان","Umm Al Quwain":"أم القيوين","Ras Al Khaimah":"رأس الخيمة","Fujairah":"الفجيرة"}

ZONE_NOTE = {"A":"Sharjah/Ajman standard","B":"Old Dubai, Silicon Oasis side, UAQ","E":"Far from base (Dubai default price)","C":"New Dubai","D":"Far areas: 4-hour minimum"}

STEPS = [
 ("1","Create account","bookingkoala.com -> Start free trial. Use justnow.cs@gmail.com. Industry: Home cleaning. Currency: AED. Time zone: Asia/Dubai. Language: English (add Arabic later if the plan supports it)."),
 ("2","Company profile","Name: Just Now For Building Cleaning Services. Phone: +971 50 767 7282. Email: Customer.care@justnow.life. Website: https://www.justnow.life. No street address shown to customers."),
 ("3","Locations (= your zones)","Settings -> Locations. Create 5 locations named exactly: Zone A, Zone B, Zone C, Zone D, Zone E. These are not shown to customers; they only carry the prices. See sheet '3 Zones & Areas' for which area belongs to which zone."),
 ("4","Service areas","If BookingKoala asks for zip/postal codes, use the area NAME as the code (e.g. 'Al Majaz'). Load every row of sheet '3 Zones & Areas' under its zone. The customer types or picks the area and the zone price applies."),
 ("5","Service categories","Create 2 bookable services: 'Kitchen deep cleaning' and 'Full house deep cleaning'. Do NOT create sofa/mattress/carpet or commercial as bookable (they are quoted from photos on WhatsApp)."),
 ("6","Pricing variables","For Full house: a 'Home size' dropdown with Studio, 1 BHK, 2 BHK, 3 BHK, Villa 4 BR, Villa 5+ BR. For Kitchen: no size question (always the kitchen row). Then a 'Package' dropdown per size with the 3 options from sheet '2 Packages'. Price = per location (zone). Enter every price from sheet '2 Packages'; never leave a formula or 'from' price."),
 ("7","Duration","Set each package's duration to its hours (3, 4, 5, 6 or 7 h) and the number of providers to the cleaners count, so the calendar blocks the right time and team."),
 ("8","Minimum","Zone D must not offer any 3-hour package. Use the location rule to hide the 3-hour option for Zone D (its first package is 2 x 4 h)."),
 ("9","Hours and slots","Settings -> Business hours: every day 08:00-21:00. Arrival windows: 8-12, 12-4, 4-9. Same-day booking allowed until 18:00; after that the earliest slot is tomorrow 8-12. See sheet '4 Hours & Slots'."),
 ("10","Customer form fields","Name, mobile (+971), email (optional), emirate, area, building/villa + apartment number, notes ('What should the team focus on?'). All mandatory except email. No account creation required to book."),
 ("11","Payment","Pay on completion (cash, card payment link, bank transfer). In BookingKoala set 'Pay later / no card required' for now. No deposit. No discount codes. No tips. Turn OFF any 'frequency discount' option: regular cleaning is not offered."),
 ("12","Policies text","Copy the texts from sheet '5 Policies & texts' into Settings -> Terms / Cancellation policy / Booking confirmation message."),
 ("13","Notifications","Customer: booking confirmation + reminder 24 h before (SMS if the plan includes it, else email). Owner: new booking email to Customer.care@justnow.life and push to the app. Add Google Calendar sync so each booking appears as 'UNCONFIRMED - [service] - [name]' on the 'Cleaning Services Schedule' calendar."),
 ("14","Test","Make one booking named 'TEST - DO NOT CONFIRM' for Al Majaz / Kitchen / 2 x 3 h and check: price AED 249, calendar entry created, confirmation received. Then one for Al Suyoh (must show AED 309) and one for a Zone D area (must offer 2 x 4 h = AED 439 first). Delete the tests."),
 ("15","Go live","Put the BookingKoala link on https://www.justnow.life/book-now (keep ?utm_source=whatsapp on the WhatsApp link) and update the WhatsApp assistant's booking link. Keep the old Webador form until the new one has taken 10 real bookings without a problem."),
]

HOURS = [
 ("Working days", "Every day, including Friday and public holidays"),
 ("Working hours", "08:00 - 21:00 (Asia/Dubai)"),
 ("Arrival window 1", "08:00 - 12:00"),
 ("Arrival window 2", "12:00 - 16:00"),
 ("Arrival window 3", "16:00 - 21:00"),
 ("Arrival promise", "Team arrives within the window; up to 1 hour delay possible due to traffic. Service hours start when the team arrives."),
 ("Same-day booking", "Allowed until 18:00 for the 16:00-21:00 window, only if a team is free. After 18:00 the first bookable slot is tomorrow 08:00-12:00."),
 ("Lead time (BookingKoala 'minimum notice')", "2 hours"),
 ("Booking horizon", "30 days ahead"),
 ("Teams / providers", "Enter the number of cleaners available per day so the calendar blocks capacity correctly (fill in)."),
 ("Buffer between jobs", "60 minutes travel (fill in if different)"),
 ("Recurring / frequency option", "OFF. Regular, weekly, monthly and subscription cleaning are not offered."),
 ("Discount codes / tips", "OFF"),
]

TEXTS = [
 ("Service description: Kitchen deep cleaning",
  "Cooker, hob, hood and oven steam cleaned inside and out. Fridge inside and out, every cabinet inside, outside and on top. Walls, tiles, grout, sink and floor. Food-safe: you can cook right after. Our trained all-female team brings all machines, tools and materials. Also choose this package for bathrooms only, kitchen + bathrooms, one room, balcony, inside windows or a full home refresh, and tell our team what to focus on when they confirm.",
  "البوتاجاز والشفاط والفرن بالبخار من الداخل والخارج. الثلاجة من الداخل والخارج، وكل الخزائن من الداخل والخارج ومن فوق. الجدران والسيراميك والفواصل والحوض والأرضية. آمن على الأكل: تقدر تطبخ بعدها مباشرة. فريقنا النسائي المدرّب يجيب كل الماكينات والأدوات والمواد."),
 ("Service description: Full house deep cleaning",
  "Kitchen and bathrooms deep cleaned with high-temperature steam. Bedrooms, living areas, floors, doors, windows, AC vents and balcony deep cleaned by hand. Furniture moved and cleaned behind. Our trained all-female team brings everything.",
  "المطبخ والحمامات بالبخار بدرجة حرارة عالية. غرف النوم والصالة والأرضيات والأبواب والشبابيك وفتحات التكييف والبلكونة تنظيف عميق يدوي. نحرّك الأثاث وننظف وراه. فريقنا النسائي المدرّب يجيب كل شي."),
 ("Price note under the form",
  "The price shown is the total: team, hours, transport, steam machine, tools and materials included. No call-out fee. Pay on completion by cash, card payment link or bank transfer.",
  "السعر المعروض هو الإجمالي: الفريق والساعات والمواصلات وماكينة البخار والأدوات والمواد. بدون رسوم زيارة. الدفع بعد الانتهاء نقداً أو برابط بطاقة أو تحويل بنكي."),
 ("Cancellation policy",
  "Reschedule: one free reschedule if requested more than 24 hours before, subject to availability. Less than 24 hours: only against a deposit toward the new booking; a second reschedule counts as a cancellation. Cancellation: more than 12 hours before - no charge. 12 to 8 hours before - 30%. Less than 8 hours and before dispatch - 50%. After dispatch, on arrival, or no access - 100%. If we cancel - no charge and we offer the earliest slot.",
  "إعادة الجدولة: مرة واحدة مجاناً إذا طُلبت قبل أكثر من 24 ساعة وحسب التوفر. أقل من 24 ساعة: مقابل عربون يُحتسب من الحجز الجديد؛ إعادة الجدولة الثانية تُعتبر إلغاء. الإلغاء: قبل أكثر من 12 ساعة بدون رسوم. من 12 إلى 8 ساعات 30%. أقل من 8 ساعات وقبل انطلاق الفريق 50%. بعد الانطلاق أو عند الوصول أو عدم التمكن من الدخول 100%. إذا ألغينا نحن: بدون رسوم ونقدم أقرب موعد."),
 ("Booking confirmation message",
  "Thank you for booking with Just Now 😊 Our team will confirm your booking with you on WhatsApp shortly. Please make sure running water and electricity are available and someone can open the door. You can add one more hour on the day if needed; tell the team before the last booked hour starts.",
  "شكراً لحجزك مع جست ناو 😊 فريقنا بيأكد حجزك معك على الواتساب قريباً. الرجاء التأكد من توفر الماء والكهرباء ووجود شخص لفتح الباب. تقدر تضيف ساعة إضافية في نفس اليوم إذا احتجت؛ خبر الفريق قبل بداية آخر ساعة محجوزة."),
 ("Quality guarantee",
  "Report any issue on site or within 24 hours and we redo that part free of charge. We do not repair pre-existing damage.",
  "بلّغنا عن أي ملاحظة في الموقع أو خلال 24 ساعة ونعيد تنظيف ذلك الجزء مجاناً. لا نصلح الأضرار الموجودة مسبقاً."),
 ("Not bookable online (show as a note)",
  "Sofa, mattress, carpet and curtains, offices and shops, Abu Dhabi and Al Ain: message us on WhatsApp +971 50 767 7282 with photos or a video for an exact price.",
  "الكنب والمراتب والسجاد والستائر، المكاتب والمحلات، أبوظبي والعين: راسلنا على واتساب +971 50 767 7282 مع صور أو فيديو لسعر دقيق."),
]
