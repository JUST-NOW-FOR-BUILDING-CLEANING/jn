# Just Now bot supervisor

A Claude-run supervisor that sits beside the respond.io AI agent all day, the way a team lead would: it reads
every conversation, catches mistakes, makes sure no customer is left without a reply, hands customers to a person
when needed, and turns repeated mistakes into instruction updates that the owner approves.

## How it works

```
 customers ──► respond.io AI agent ("Just Now update") ──► booking page
                    ▲            │
                    │            ▼
     approved       │     every 10 min  SAFETY NET      customer waiting 10+ min → assign to owner + alert
     instruction    │     every hour    HOURLY CHECK    wrong price / invented fact / channel down → comment,
     changes        │                                   correction, assign, alert; everything else → log
                    │     23:30         NIGHTLY REVIEW  daily report + proposed instruction changes
                    └──── 07:45         MORNING APPLY   applies only the changes the owner ticked
```

| Loop | When (UAE) | Runs on | Prompt |
| --- | --- | --- | --- |
| Safety net | every 10 min, 08:00–21:00 | Make.com scenario (or a sub-hourly Claude routine) | `routines/safety-net.md` |
| Hourly check | every hour, 08:00–23:00 | Claude routine, fresh session, respond.io connector | `routines/hourly-check.md` |
| Nightly review | 23:30 | Claude routine | `routines/nightly-review.md` |
| Morning apply | 07:45 | Claude routine | `routines/nightly-review.md` (second half) |

The owner's control panel is a private Claude doc (report, daily log, pending instruction changes to tick,
instruction history). Nothing customer-related is stored in this repository — **this repository is public**.

## Rollout

| Phase | Days | The supervisor may | Owner does |
| --- | --- | --- | --- |
| 1 Watch | 1–2 | read, comment, alert; propose instruction changes | checks the alerts and comments are right; ticks changes |
| 2 Assist | 3–7 | also assign waiting customers to the owner | answers assigned customers; ticks changes |
| 3 Fix | week 2+ | also send the pre-approved corrections in `routines/corrections.md` | reviews the nightly report |

The supervisor never changes prices, zones or policies on its own, never closes or deletes anything, and never
edits the AI agent outside the morning apply step. Every instruction change is saved to the history first, and
`update_ai_agent` is always sent with the agent's full `knowledgeSourceIds` list (omitting it wipes the agent's
knowledge sources).

## Tools

| File | What it does |
| --- | --- |
| `tools/extract_rules.py` | pulls the PRICE TABLE, ZONES, banned numbers and booking link out of the live agent instruction → `rules.json` |
| `tools/render.py` | one conversation → transcript in UAE time + automatic checks (reply delays, unanswered tail, prices vs table, booking link, markdown, repeats, failed deliveries) |
| `tools/aggregate.py` | all reviews of a day → funnel, bookings, outcomes, mistakes, hourly timeline, before/after splits |
| `rubric.md` | how each conversation is judged; the mistake types |
| `tools/config.example.json` | ids and thresholds; copy to `config.json` (git-ignored) |

## Setting it up

1. Make this repository private, or move `supervisor/` to a private one (the routines write working files).
2. Create the routines (Claude Code on the web → Routines, or ask Claude in this repo): hourly check, nightly
   review, morning apply — each "new session per run", with the respond.io connector attached, `PHASE 1`.
3. Build the Make.com safety-net scenario from `routines/safety-net.md` (or a sub-hourly routine if available).
4. After two days in phase 1, move to phase 2 by editing the routine prompt.

## Daily numbers it tracks

Conversations, % answering the first reply, % reaching a price, bookings (lifecycle Qualified/Customer or
"I booked"), % silent after price, bot reply time, customers left waiting, owner reply time on hand-offs,
wrong prices, mistakes per 100 conversations by type, failed deliveries per channel.
