# Safety net: nobody left without a reply (every 10 minutes, 08:00–21:00 UAE)

The hourly check is too slow for a customer who is waiting right now. This light loop runs every 10 minutes and
does one thing: find customers whose last message has had no answer, and get a person on it.

## Why a filter alone is not enough

respond.io's `pendingSince` marks every conversation whose last message came from the customer, including the
ones where the bot is correctly silent after "thanks" or "no". A check on 27–28 Sep 2026 returned 100+ "pending"
conversations. So each candidate needs a look at the last message before anyone is alerted.

## Logic

1. `search_contacts`: `status isEqualTo open` AND `pendingSince isTimestampBetween <now − 60 min> and <now − 10 min>`.
2. For each: last 5 messages (`list_messages`, limit 5).
3. Skip when the customer's last message only closes the chat (thanks, ok, no thanks, 👍, شكرا, تمام, لا شكرا)
   or when an internal comment for this issue already exists.
4. Otherwise: assign to the owner and comment `Waiting <N> min: "<their words>"` + a suggested reply;
   notify the owner (push, or a WhatsApp template to the owner's own number).
5. Any outgoing message with status `failed` in those 5 messages → the channel alert from `hourly-check.md` (A).

## Where it runs

- **Make.com scenario** (recommended for a 10-minute cadence): Schedule every 10 min → respond.io "Make an API
  call" (contact list with the filter above) → Iterator → respond.io list messages → Router (rule from step 3,
  or an Anthropic Claude module for the judgement) → respond.io assign + comment → notification.
- **Claude routine** when the plan allows sub-hourly schedules: this file is the whole prompt; phase rules from
  `hourly-check.md` apply.
