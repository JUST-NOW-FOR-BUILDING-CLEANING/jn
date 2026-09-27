# Playbook – how the business and the bot work

What the supervisor needs to remember between runs. Prices, zones and exact wording are NOT here: they live in
the bot's live instruction and are read fresh every run. No customer data here – this repository is public.

## The business

- Just Now For Building Cleaning Services, UAE: steam deep cleaning inside homes and offices, all-female teams,
  every day 8 AM – 9 PM. Services: kitchen deep cleaning, full house deep cleaning, sofa / mattress / carpet
  cleaning (priced by a person from photos), commercial interiors (priced from a video).
- Leads come mostly from Meta click-to-WhatsApp ads (first message "Hello! Can I get more info on this?").
- Customers book themselves on the booking page (link with `?utm_source=whatsapp`); the booking team then
  confirms on WhatsApp from the main company number. The bot never takes a booking in the chat.
- Abu Dhabi / Al Ain: minimum order AED 1,000, handled on the main number. Job seekers → HR WhatsApp.

## The conversation that books

greeting with the language menu → services list (1 / 2 / 3) → size (full house) → area and emirate →
the short description, then the FIRST package price and the booking link right under it → customer books on the
page → "Thank you, our booking team will contact you on WhatsApp to confirm it."

What the bookings of 26–27 Sep 2026 had in common: an answer within seconds; the entry package (2 cleaners × 3 h,
AED 249–329) quoted correctly for the area; the link right under the price; side questions (a discount card, what
is included) answered directly; the customer booked within minutes of the price. Mornings (10:00–13:00) convert
best.

## Where leads are lost

- About a third never answer the first language menu – do not chase; the two follow-ups are enough.
- The services list skipped and kitchen guessed from the ad text; number replies ("2") to the list ignored.
- A question from the first message left unanswered (price per hour, "are you in Dubai?", where we are).
- Wrong or old prices; extra packages nobody asked for; price before the area was known.
- Hand-off lines ("our team will send you the price") with nobody told – now fixed by the "Price needed" tag.
- Voice notes ignored after a price; replies after "thanks"; follow-ups after the customer booked.
- System failures: Instagram / Messenger access tokens invalidated (all sends fail until the owner reconnects),
  a stopped workflow leaving new chats unassigned (nobody answers), the WhatsApp 24-hour window closing.

## Baseline (26 Sep 12:00 – 28 Sep 02:00, before the 28 Sep fixes)

321 new customer chats · 69 % answered the first menu · 54 % reached a price · 6 bookings (1.9 %) · 124 went
silent or declined after the price · 238 price quotes, 17 wrong · 51 chats with a serious mistake. Use these to
judge whether a day, or an instruction change, is better or worse.

## Known system facts

- AI agent "Just Now update" is the live bot; the older agents are inactive and must stay so.
- Workflow "Assign new conversations to AI agent" must stay published; when it stops, new chats sit unassigned.
- `update_ai_agent` replaces the knowledge sources with exactly the list sent – always send the full list.
- `list_ai_agents` returns every agent with its instruction (large, usually saved to a file); `get_ai_agent`
  also returns `knowledgeSourceIds`.
- A message's time = `messageId // 1_000_000` (epoch seconds). UAE time = UTC+4.
- Another Claude session may also edit the agent: always read the live version right before changing it, and
  never overwrite someone else's newer changes.
