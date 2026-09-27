# Corrections sent to customers

The supervisor sends these as soon as it finds the mistake (owner's order, 28 Sep 2026: "correct it and send it
to the customer"). Fill the brackets from the live instruction (`supervisor/work/instruction.txt`) – never from
memory. Write in the customer's language, as one short message.

| Mistake | English | Arabic |
| --- | --- | --- |
| Price too high for the zone / size | Sorry, a small correction 😊 For [service] in [area], it's [cleaners] cleaners × [hours] hours – AED [price], everything included. Book here: [booking link] | عذراً، تصحيح بسيط 😊 [الخدمة] في [المنطقة]: [عدد] عاملات × [ساعات] ساعات – [السعر] درهم، كل شي شامل. احجز من هنا: [رابط الحجز] |
| Extra packages given without being asked | – no correction; log it | – |
| Price given without the booking link, or with a wrong link | You can book your slot here in one minute 😊 [booking link] | تقدر تحجز موعدك من هنا خلال دقيقة 😊 [رابط الحجز] |
| Kitchen price given when the customer asked for full house / a home size (or the other way round) | Sorry, a small correction 😊 For [the right service] in [area], it's [cleaners] cleaners × [hours] hours – AED [price], everything included. Book here: [booking link] | same as the price row |
| Same-day promised after 6 PM | Sorry, a small correction 😊 Today's bookings are closed, but you can book tomorrow's first slot here: [booking link] | عذراً، تصحيح بسيط 😊 حجوزات اليوم انتهت، لكن تقدر تحجز أول موعد بكرة من هنا: [رابط الحجز] |
| "Your booking is confirmed" (the bot cannot see bookings) | Sorry, a small correction 😊 Our booking team will contact you on WhatsApp to confirm your booking. | عذراً، تصحيح بسيط 😊 فريق الحجز بيتواصل معك على واتساب لتأكيد حجزك. |
| An office or street address was given | Sorry, a small correction 😊 We come to you – our team serves Dubai, Sharjah, Ajman, Umm Al Quwain, Ras Al Khaimah and Fujairah. | عذراً، تصحيح بسيط 😊 نحن نجيك لين عندك – نخدم دبي والشارقة وعجمان وأم القيوين ورأس الخيمة والفجيرة. |
| A question left unanswered (the answer is in the instruction) | Sorry for the wait 😊 [the answer, in the instruction's words] | عذراً على التأخير 😊 [الجواب من التعليمات] |
| Voice note ignored | Sorry, I can't play voice notes here 😊 Could you please type your message? | عذراً، ما أقدر أسمع الرسائل الصوتية هنا 😊 ممكن تكتب رسالتك؟ |

## Rules

- One correction per conversation per day; check the transcript for an earlier one of ours first.
- Never a correction that raises the price the customer was given: the lower quote stands; log it.
- Never to a customer whose last message declined or thanked, unless the correction lowers their price.
- Never correct sofa / mattress / carpet / curtains or commercial prices – there is no table for them.
- Outside the 24-hour WhatsApp window: only the `follow_up` template, 09:00–21:00, e.g.
  {{1}} = first name, {{2}} = "correct the price we sent: for your kitchen in Al Qusais it's 2 cleaners × 3 hours, AED [price], everything included. Book here: [booking link]".
- Log every correction in the doc's log tab (time, contact id, what was wrong, what was sent).
