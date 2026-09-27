# Conversation review rubric

How the supervisor judges one respond.io conversation handled by the Just Now AI agent. The rule book is the
agent's **live** instruction (`get_ai_agent` → `bundle.instruction`), read fresh on every run; this file only says
how to judge against it. Nothing customer-specific or price-specific is stored here.

## Per conversation, record

| Field | Values |
| --- | --- |
| entry | meta_ad_text, named_service, greeting_only, price_question, job_seeker, returning_customer, existing_booking_support, sales_or_spam, other |
| service | kitchen, full_house, sofa_mattress_carpet, bathrooms_only, kitchen_plus_bathrooms, refresh_or_partial, commercial, regular_or_maid, not_offered, not_stated, other |
| furthest_stage | no_bot_reply, greeting_only, language_chosen, service_known, size_known, emirate_known, area_known, price_given, link_sent, customer_said_booked, booking_confirmed, handed_off |
| outcome | booked, says_will_book, handed_off_waiting_price, handed_off_answered, silent_after_price, silent_before_price, silent_after_greeting, declined_price, declined_other, service_not_offered, abu_dhabi_al_ain, outside_uae, job_seeker, sales_or_spam, existing_customer_support, ongoing, other |
| expected_zone / expected_first_price_aed | from the ZONES list and PRICE TABLE in the live instruction |
| waiting_for_human_now | true when the customer is still waiting for a human answer or price |

## Mistake types (one per finding, with the bot's exact words and the time)

| Type | Severity guide |
| --- | --- |
| wrong_price, price_before_area, extra_packages_unasked, price_missing | high when the customer saw a wrong number |
| link_missing, link_missing_utm | medium |
| hallucination (invented facts, numbers, availability, confirmed slots) | high if a customer relies on it |
| no_reply, slow_reply, misunderstood_customer | high when a buying question was ignored |
| handoff_missed, handoff_wrong | high when a hand-off line went out without the "Price needed" tag, or the instruction already had the answer |
| parked (assigned to the owner, or unassigned) | high – nobody answers it; the supervisor moves it back to the AI |
| greeting_error, language_error, services_list_error, description_error | medium |
| repeated_message, replied_after_close, followup_error, pushy_or_chasing | medium |
| money_rule (discount, VAT, "from" price, hourly rate), not_offered_handling, abu_dhabi_rule, job_seeker_rule, sofa_commercial_rule, voice_media_rule | medium |
| markdown_formatting (`**` or `#` — WhatsApp shows the symbols), too_long_or_unstructured | low |
| channel_failure (message status failed) | high; quote the error text |

Silence after "thank you", "no thanks", "I'll get back to you" is **correct** behaviour, not a missed reply.

## What to capture for learning

- For every booking: what made it work (speed, direct answers, correct price, booking-page guidance, reassurance).
- For every lost lead: one concrete sentence on why ("went silent right after the AED 309 price",
  "never answered the language menu", "asked for 1 cleaner; minimum explained; left").
- A coach note: what the bot should have said instead, in one or two sentences.
