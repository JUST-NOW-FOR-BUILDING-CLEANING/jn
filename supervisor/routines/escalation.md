# Escalation (when a scheduled run calls for help)

The owner asked for alerts to go to Claude, not to him. The hourly check and the nightly review call the
escalation routine (`fire_trigger` with a short text) when they meet something they must not or cannot fix
alone. The escalation session is a Claude session with the full history of this project; it reads the text,
investigates in respond.io and fixes what can be fixed.

| Escalation | What the escalation session does |
| --- | --- |
| No-assign rule undone / instruction overwritten | Read the live agent; find what changed (another editor?); re-apply the owner's standing orders and any lost fixes on top of the new version (never throw away the other editor's changes); verify; log. |
| Agent inactive | Check whether it was switched off on purpose (a recent instruction change, a note in the doc). If not, reactivate it with `update_ai_agent` (`active: true`, full `knowledgeSourceIds`). |
| Channel disconnected (Instagram / Messenger token) | Only the owner can reconnect it (respond.io → Settings → Channels). Put one line in the doc's "Needs the owner" box with the number of customers affected; answer those customers on WhatsApp when they gave a number. |
| Same mistake corrected 3+ times in a day | Patch the instruction now (nightly-review step 3 rules) instead of waiting for the night. |
| Many customers unanswered at once | Check workflows (`list_workflows`: "Assign new conversations to AI agent" must be published), assignments, the agent's state; fix and answer the customers. |
| Anything else | Investigate, fix within the guardrails in `supervisor/README.md`, log. |

Every escalation ends with a line in the doc's log tab. Nothing is sent to the owner; items only he can do go to
the "Needs the owner" box, once.
