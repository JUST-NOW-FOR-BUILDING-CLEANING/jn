# Judging a batch of conversations (for the nightly review's subagents)

A subagent gets: a list of contact ids, `DAY` (e.g. 2026-09-28), `SINCE` (the epoch second of `DAY` 00:00 UAE),
`NOW` (local time, e.g. "2026-09-28 23:45") and `OUT` (e.g. `supervisor/work/day`). It only READS respond.io and
writes files under `OUT`. It never sends, assigns, tags, closes or changes anything.

Read first: `supervisor/rubric.md` (how to judge), `supervisor/work/instruction.txt` (the bot's live rule book:
greeting, services list, flow, prices by zone and size, zones, booking link, hand-offs), `supervisor/playbook.md`.

Tools: ToolSearch `select:mcp__Respond_io__list_messages,mcp__Respond_io__get_contact`. Every respond.io call needs
a `context` argument (15–25 words, third person, no personal data). A denied call: do not retry or work around
it; note it in the summary.

Write files only for your own contacts, and only under `OUT`. Never copy other files there.

## For each contact

1. `list_messages` (`id:<id>`, `{"limit": 50}`; newest first). Newest message older than `SINCE` → write
   `OUT/audit/<id>.json` = `{"contact_id": <id>, "in_window": false}` and go on (the contact only moved because of
   an assignment or a tag). If `pagination.next` is set and the oldest message you got is still newer than
   `SINCE − 86400`, fetch one more page (`cursorId` from the next URL).
2. Write `OUT/raw/<id>.jsonl` exactly as described at the top of `supervisor/tools/render.py` (text verbatim; for a
   failed outgoing message the failure reason in `err` when the item carries it).
3. `python3 supervisor/tools/render.py OUT/raw/<id>.jsonl --config supervisor/work/config.json --rules supervisor/work/rules.json --since "DAY 00:00" --now "NOW" --out-dir OUT --quiet`
   plus a `--marker "DAY HH:MM=<label>"` for every instruction change of the day given in your prompt.
4. Read `OUT/transcripts/<id>.txt` and `OUT/metrics/<id>.json`, judge the day's part of the conversation against the
   live rules (earlier messages are context), and write `OUT/audit/<id>.json`.

Messages with `sender.source = "user"` and the owner's user id were sent by the supervisor or by the owner from the
inbox: they are ours. Do not judge them as bot mistakes; a correction we sent counts as `handed_off_answered` or as
context for the outcome.

## `OUT/audit/<id>.json`

```
{
 "contact_id": 0, "in_window": true,
 "new_today": true,                 // the customer's first ever message is from DAY
 "customer_active_today": true,     // at least one customer message on DAY (false = only follow-ups / our messages)
 "channel": "WhatsApp",             // WhatsApp | Instagram | Messenger | TikTok
 "language": "en",                  // ar | en | mixed | unknown
 "entry": "meta_ad_text",           // rubric.md
 "customer_answered_greeting": true,// did the customer reply after the bot's first message? null if no bot reply
 "service": "kitchen",              // rubric.md
 "home_size": null, "emirate": "Dubai", "area": "Al Nahda",
 "expected_zone": "B", "expected_first_price_aed": 279,
 "prices_quoted": [{"aed": 279, "package": "2 cleaners x 3h", "time": "DAY 10:58", "correct": true, "note": ""}],
 "booking_link_sent": true, "booking_link_exact": true,
 "furthest_stage": "link_sent",     // rubric.md
 "outcome": "silent_after_price",   // rubric.md
 "booked_evidence": null,           // quote, or the "Booked on website" tag, when booked
 "unanswered_customer_message": false, "unanswered_detail": null,
 "handoff_expected": false, "handoff_done": false,
 "waiting_for_human_now": false,    // still waiting for a person (a price, a call) at the end
 "followups_sent": 0,
 "good_types": ["fast_reply", "correct_price"],
 "mistakes": [{"type": "services_list_error", "severity": "medium", "time": "DAY 20:56",
               "bot_quote": "exact short excerpt", "explanation": "one line"}],
 "lost_booking_reason": null,       // one concrete sentence when a lead was lost today
 "coach_note": "what the bot should have said, 1–2 sentences"
}
```

Contact only got follow-ups or our messages today (`customer_active_today: false`): fill `in_window`, `new_today`,
`customer_active_today`, `channel`, `outcome` ("ongoing" or the earlier outcome), `followups_sent`, and `mistakes` only
if a follow-up was wrong (sent after a thanks, a decline, a booking or a hand-off, or the same text repeated).

## How to judge

- Quote the bot's exact words; never invent quotes. Every mistake carries its time.
- Price check: zone from the ZONES list (area not listed = the emirate's default zone), row from the service and
  size (kitchen / partial = the kitchen row; full house = the size row), first package only.
- Silence after thanks, "no thanks", "I'll get back to you" or a second discount request is correct.
- Hand-offs: the only hand-off is the "Price needed" tag plus a hand-off line; nobody is assigned (owner's order).
  The bot's tag action does not fire, so a missing tag is the supervisor's job – log it as `handoff_missed` only when
  the customer was left without any hand-off line.
- The services list must come before any price when the customer did not name a service (a number reply "1"/"2"
  after the greeting chooses the LANGUAGE, not a service).

## Summary to return (under 250 words)

Contacts processed / in window / customer active today / new today; bookings or "I booked" (id, first name, one line
on what worked); customers still waiting for a person (id, what they need, since when); the 5 most frequent mistake
types with counts and one example id each; anything alarming (wrong prices, customers ignored, failed messages,
invented facts). No phone numbers.
