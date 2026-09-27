# Nightly review (23:40 UAE)

Once a day: judge every conversation of the day, write the daily report into the owner's doc, and improve the
bot's instruction where it keeps making the same mistake – automatically, inside the guardrails. Nobody watches
this run: never ask questions, never message the owner. Read `supervisor/README.md`, `supervisor/playbook.md`
and `supervisor/rubric.md` first. Same inputs and setup as `ten-minute-check.md` (steps 1 and 3).

## 1. Judge the day

1. `search_contacts`: `lastInteractionTime isTimestampAfter <today> 00:00` (Asia/Dubai, limit 100, follow
   `pagination.next`).
2. For each contact: `list_messages` (limit 50) → `supervisor/work/raw/<id>.jsonl` → `render.py` with
   `--since "<today> 00:00"` → judge with `rubric.md` → `supervisor/work/audit/<id>.json` (the rubric's fields
   and mistakes, each mistake with the bot's exact words and time). With more than 40 conversations, split them
   across parallel subagents (Agent tool), each writing the same files.
3. `python3 supervisor/tools/aggregate.py supervisor/work` → the day's numbers.

## 2. Daily report → the doc's "Daily reports" tab (newest on top)

- Headline: conversations, new leads, prices given, bookings (lifecycle Qualified/Customer or "I booked") –
  against yesterday and the baseline in `playbook.md`.
- What won today's bookings (quote the turning point), where leads dropped (stage counts).
- Top mistakes with counts and 1–2 contact ids each.
- What the supervisor did today (from the log tab): replies, corrections, reassignments, escalations.
- **Price needed** – open sofa / mattress / carpet / curtains / commercial chats and unanswered "let me check"
  questions: contact id, first name, what they need, waiting since. This list is how the team prices them.
- Channel problems and anything only the owner can do (e.g. reconnect Instagram) – one line each, no nagging.

## 3. Instruction updates (automatic)

1. Candidates: a mistake type seen 3+ times today, or any high-severity one, that the current wording causes or
   fails to prevent. One edit per cause.
2. For each, write the smallest edit that fixes it into `supervisor/work/edits.json` as
   `{"old": <exact text, occurring once>, "new": <text>, "why": <mistake type, count, example contact ids>}`.
   Prefer adding one line or one example next to the rule it sharpens; keep the instruction's style (short
   points, English + Arabic versions of customer-facing lines).
3. Never: prices, packages, zones, TERMS AND POLICY, the booking link, the banned numbers, the no-assign rule,
   the owner's facts; never delete a rule unless it contradicts another; at most 5 edits a night.
   `agent.py patch` enforces most of this – if it refuses an edit, drop that edit.
4. Save the current instruction first: a new dated entry in the doc's "Instruction history" tab (time, reason,
   the full current text in a code block).
5. `python3 supervisor/tools/agent.py patch supervisor/work/instruction.txt supervisor/work/edits.json --out supervisor/work/instruction.new.txt`
6. `get_ai_agent` → current `knowledgeSourceIds`. `update_ai_agent` with `bundle.instruction` = the full text of
   `instruction.new.txt`, `bundle.description` = the current description + " <DD Mon HH:MM>: <one line>", and
   `knowledgeSourceIds` = that exact list (omitting it deletes every knowledge source).
7. Verify: `list_ai_agents` → `python3 supervisor/tools/agent.py verify <dump> --agent AI_AGENT --expected supervisor/work/instruction.new.txt`
   must print OK. If not, send again once; still not → restore the saved version the same way and escalate.
8. Add "Instruction changes" to the daily report: each edit, why, the example contact ids.

## 4. Regression check (yesterday's changes)

Compare today with the three days before: prices given per 10 new chats, bookings, mistakes per 100 chats, and
the mistake type each change targeted. Roll a change back (reverse edit, same steps 4–7) when the targeted type
did not drop, a new high-severity mistake traces to the new wording, or prices per 10 chats fell by more than a
quarter on 40+ chats. Log every rollback in the report. Unsure → escalate instead of guessing.

## 5. Escalate

As in `ten-minute-check.md` step 7: anything the report shows that needs deeper work (a sudden drop, a new kind
of failure, a change that could not be verified).
