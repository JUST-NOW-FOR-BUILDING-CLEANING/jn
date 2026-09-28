# Just Now bot supervisor

A Claude-run supervisor that sits beside the respond.io AI agent all day, the way a team lead would: it reads
every new conversation, answers customers the bot left waiting, corrects wrong replies directly to the customer,
keeps every conversation with the AI, and turns repeated mistakes into instruction updates. It works without
asking the owner anything; problems it cannot solve alone go to Claude (the escalation routine), not to the owner.

## Standing orders from the owner (28 Sep 2026)

1. **Never assign anything to the owner.** Every conversation stays with, or is moved back to, the AI agent.
   The agent's `assignConversation` action stays disabled.
2. **Reply to every customer who needs a reply**, and when the bot said something wrong, **send the correction to
   the customer** – no approval step.
3. **Update the bot's instructions** when a mistake repeats – automatically, with the guardrails below.
4. **Alerts go to Claude, not to the owner.** Anything the runs cannot fix is escalated to the Claude escalation
   routine, which investigates and fixes it.
5. Exception – prices only a person can give: sofa / mattress / carpet / curtain photos and commercial places
   (office, shop, restaurant, salon). The bot asks for the photos or video, tags the conversation
   **"Price needed"** and keeps it; nothing is assigned. The supervisor never invents these prices; the open ones
   are listed in the daily report so the team can price them from the tag.
6. **No WhatsApp templates, no marketing messages** (28 Sep 2026, 23:30 – the owner does not want the number
   blocked). Never send any template (`follow_up`, `job_feedback_en` or any other), never create, edit or submit
   one, never retry or re-send a failed message. Only free-form replies inside the customer's 24-hour window. A
   customer who could only be reached with a template goes on the doc's "Needs the owner" list instead. Template
   or follow-up sending is never added to the bot's instruction either.

## How it works

```
 customers ──► respond.io AI agent ("Just Now update") ──► booking page
                    ▲            │
   nightly          │            ▼
   instruction      │   every hour    SUPERVISOR CHECK   answer waiting customers · correct wrong replies ·
   updates          │                                    move chats back to the AI · guard the no-assign rule
   (guarded)        │   23:40         NIGHTLY REVIEW     daily report · instruction updates · regression rollback
                    └── anytime       ESCALATION         Claude session with the full history fixes what the
                                                         runs could not (prompt overwritten, channel down, …)
```

| Run | When (UAE, GST = UTC+4) | Prompt |
| --- | --- | --- |
| Supervisor check | every hour, all day (the shortest interval routines allow here; every 10 min if the plan allows) | `routines/check.md` |
| Nightly review | 23:40 | `routines/nightly-review.md` |
| Escalation | when a run calls it | `routines/escalation.md` |

Each scheduled run is a fresh Claude session with the respond.io connector. It fetches this branch, reads these
files, reads the bot's **live** instruction (the single source of truth for prices, zones and wording), does its
job and ends. Quiet runs end after one search.

## Memory

| What | Where |
| --- | --- |
| Prices, zones, policies, wording | the live agent instruction (`get_ai_agent`), parsed by `tools/extract_rules.py` every run |
| How the business works, what wins and loses bookings, known failure modes | `playbook.md` |
| How to judge a conversation | `rubric.md` |
| What to send when correcting | `routines/corrections.md` |
| What was already done in a conversation | the conversation itself (supervisor messages are visible in `list_messages`) and the doc's "Supervisor log" tab |
| Daily reports, instruction history (every version before a change), open "Price needed" list | the owner's private Claude doc |

**This repository is public**: no customer names, numbers, messages or prompt text are ever committed here. Working
files go to `supervisor/work/` (git-ignored).

## Guardrails

- Never assign to the owner or anyone else except the AI agent; never close, delete, block or merge contacts.
- Never invent a price, a slot, an address or a confirmation. Prices come only from the live PRICE TABLE.
- Never send a price correction that raises the price the customer was given – log it instead.
- At most one correction per conversation per day; never to a customer who declined or said thank you.
- WhatsApp free text only within 24 h of the customer's last message; outside it nothing is sent (no templates,
  standing order 6) – the customer goes on the "Needs the owner" list. Failed messages are never retried.
- Between 23:00 and 08:00 only answer customers whose last message is less than 75 minutes old.
- Instruction changes: only through `tools/patch_instruction.py` (exact, single-match edits; the PRICE TABLE,
  ZONES, TERMS AND POLICY, prices, links and the no-assign rule are protected), the previous version saved first,
  `update_ai_agent` always with the full `knowledgeSourceIds` list (omitting it wipes the knowledge sources), the
  saved result verified, at most 5 edits a night, rolled back if the next day gets worse.

## Tools

| File | What it does |
| --- | --- |
| `tools/extract_rules.py` | PRICE TABLE, ZONES, banned numbers and booking link from the live instruction → `rules.json` |
| `tools/render.py` | one conversation → transcript in UAE time + automatic checks (unanswered tail, reply delays, prices vs table, booking link, markdown, repeats, failed deliveries) |
| `tools/patch_instruction.py` | applies reviewed edits to the instruction with the protections above; verifies the saved version |
| `tools/aggregate.py` | a day of reviews → funnel, bookings, outcomes, mistakes, hourly timeline, before/after splits |
| `tools/config.example.json` | ids and thresholds; each run writes `work/config.json` from it |

## Daily numbers

Conversations, % answering the first reply, % reaching a price, bookings (lifecycle Qualified/Customer or
"I booked"), % silent after a price, bot reply time, customers the supervisor had to answer, corrections sent,
wrong prices, mistakes per 100 conversations by type, failed deliveries per channel, open "Price needed" chats.
