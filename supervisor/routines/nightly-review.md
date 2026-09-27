# Nightly review (23:30 UAE) and morning apply (07:45 UAE)

## Nightly review

1. Same setup as `hourly-check.md` steps 1–2.
2. Every conversation with activity since 00:00 UAE today: fetch, render and judge exactly as the hourly check does
   (`--since "<today> 00:00"`), then write one review JSON per conversation into `supervisor/work/audit/`
   (fields in `supervisor/rubric.md`).
3. `python3 supervisor/tools/aggregate.py supervisor/work` → funnel, bookings, outcomes, mistakes by type,
   hourly timeline, reply speed, hand-off response time.
4. Write the daily report into the supervisor doc (new dated section in the "Daily log" tab):
   - headline: conversations, prices given, bookings (lifecycle Qualified/Customer or "I booked"), vs yesterday
   - what won today's bookings (quotes), where leads dropped (stage counts), top 5 mistakes with examples
   - customers still waiting for a human (contact ids)
5. **Proposed instruction changes** — for each mistake type seen 3+ times today, or any high-severity one:
   the exact current wording, the exact new wording, why, and the example contact ids. Add each as an unchecked
   task under "Pending instruction changes" in the doc, e.g. `- [ ] Change #3: link rule — …`.
   Never touch prices, zones or policies unless the owner wrote them in a comment.

## Morning apply

1. Read "Pending instruction changes" in the doc. Only items the owner ticked (or approved in a comment) count.
2. `get_ai_agent` → keep the full current `bundle` and `knowledgeSourceIds`.
3. Save the current instruction as a new dated entry in the doc's "Instruction history" tab **before** changing it.
4. Apply the approved edits to the instruction text, then `update_ai_agent` with the new `bundle.instruction` and
   **the full current `knowledgeSourceIds` list** — omitting it deletes every knowledge source of the agent.
   Change the actions or follow-up settings only if an approved item says so.
5. `get_ai_agent` again and confirm the new text is live; mark the items done in the doc with the time applied.
6. The hourly checks of the day compare against the previous day: a new high-severity mistake type after a
   change, or fewer prices/bookings per 10 conversations over 6+ hours, goes into the alert with a one-line
   rollback proposal (restore the saved version from "Instruction history").
