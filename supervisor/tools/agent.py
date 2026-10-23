#!/usr/bin/env python3
"""Read, guard, patch and verify the respond.io AI agent instruction.

The agent JSON comes from the respond.io tools `list_ai_agents` or `get_ai_agent`. Their result is large, so
the tool output is usually saved to a file by the harness; pass that file as DUMP (any text around the JSON is
ignored).

    python3 agent.py extract DUMP --agent ID --out DIR
        DIR/instruction.txt, DIR/agent.json, DIR/rules.json + a guard report (JSON) on stdout.
    python3 agent.py patch INSTRUCTION EDITS --out NEW [--max 5]
        EDITS = JSON list of {"old": exact text, "new": replacement, "why": reason}. Every `old` must occur
        exactly once. Protected: the ZONES + PRICE TABLE block, the TERMS AND POLICY section, the booking link,
        the banned-numbers line and the no-assign rule; an edit may not add numbers of 3+ digits. Prints a diff.
    python3 agent.py verify DUMP --agent ID --expected NEW
        Exit 0 and "OK" when the live instruction equals NEW, else prints the first differences and exits 1.
"""
import argparse
import difflib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_rules import extract  # noqa: E402

BOOKING_LINK = "https://www.justnow.life/book-now?utm_source=whatsapp"
NO_ASSIGN_RULE = "Never assign a conversation to anyone"


def load_agent(dump, agent_id):
    raw = open(dump, encoding="utf-8").read()
    data = json.loads(raw[raw.index("{"):raw.rindex("}") + 1])
    agents = data.get("agents", [data])
    for a in agents:
        if int(a.get("id", -1)) == agent_id:
            return a
    sys.exit(f"agent {agent_id} not found in {dump}")


def guard(agent):
    b = agent.get("bundle", {})
    text = b.get("instruction", "")
    actions = {x.get("name"): x for x in b.get("actions", [])}
    assign = actions.get("assignConversation", {})
    return {
        "agent_id": agent.get("id"),
        "active": agent.get("active"),
        "updated_at": agent.get("updatedAt"),
        "assign_action_enabled": bool(assign.get("isEnabled")),
        "no_assign_rule_present": NO_ASSIGN_RULE in text,
        # list_ai_agents leaves knowledgeSourceIds out; only get_ai_agent returns them
        "knowledge_source_ids": agent.get("knowledgeSourceIds", "not in this dump - read get_ai_agent"),
        "booking_link_present": BOOKING_LINK in text,
        "instruction_chars": len(text),
        "ok": bool(agent.get("active")) and not assign.get("isEnabled") and NO_ASSIGN_RULE in text
              and agent.get("knowledgeSourceIds", True) != [] and BOOKING_LINK in text,
    }


def protected_spans(text):
    spans = []
    z = text.find("ZONES (find the zone")
    if z >= 0:
        spans.append((z, len(text), "ZONES / PRICE TABLE"))
    t = text.find("# TERMS AND POLICY")
    if t >= 0:
        nxt = text.find("\n# ", t + 1)
        spans.append((t, nxt if nxt > 0 else len(text), "TERMS AND POLICY"))
    for m in re.finditer(r"^.*Never say these numbers:.*$", text, re.M):
        spans.append((m.start(), m.end(), "banned numbers line"))
    for m in re.finditer(re.escape(NO_ASSIGN_RULE) + r"[^\n]*", text):
        spans.append((m.start(), m.end(), "no-assign rule"))
    return spans


def cmd_extract(a):
    agent = load_agent(a.dump, a.agent)
    os.makedirs(a.out, exist_ok=True)
    text = agent["bundle"]["instruction"]
    with open(os.path.join(a.out, "instruction.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    with open(os.path.join(a.out, "agent.json"), "w", encoding="utf-8") as f:
        json.dump(agent, f, ensure_ascii=False, indent=1)
    rules = extract(text)
    with open(os.path.join(a.out, "rules.json"), "w", encoding="utf-8") as f:
        json.dump(rules, f, ensure_ascii=False, indent=1)
    report = guard(agent)
    report["price_rows"] = len(rules["prices"])
    report["zones_emirates"] = len(rules["zones"])
    print(json.dumps(report, indent=1))


def cmd_patch(a):
    text = open(a.instruction, encoding="utf-8").read()
    edits = json.load(open(a.edits, encoding="utf-8"))
    if len(edits) > a.max:
        sys.exit(f"{len(edits)} edits > max {a.max}")
    spans = protected_spans(text)
    new = text
    for i, e in enumerate(edits, 1):
        old, rep = e["old"], e["new"]
        n = text.count(old)
        if n != 1:
            sys.exit(f"edit {i}: `old` occurs {n} times in the instruction (must be exactly 1)")
        start = text.index(old)
        for s, t, name in spans:
            if start < t and start + len(old) > s:
                sys.exit(f"edit {i}: touches the protected {name}")
        added = set(re.findall(r"\d{3,}", rep)) - set(re.findall(r"\d{3,}", old))
        if added:
            sys.exit(f"edit {i}: adds numbers {sorted(added)} - prices and numbers are not changed automatically")
        if old not in new:
            sys.exit(f"edit {i}: overlaps an earlier edit")
        new = new.replace(old, rep, 1)
    for must, name in ((BOOKING_LINK, "booking link"), (NO_ASSIGN_RULE, "no-assign rule")):
        if text.count(must) and new.count(must) < text.count(must):
            sys.exit(f"the edits remove the {name}")
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(new)
    sys.stdout.writelines(difflib.unified_diff(text.splitlines(True), new.splitlines(True), "live", "new", n=0))
    print(f"\n{len(edits)} edit(s) applied → {a.out}")


def cmd_verify(a):
    live = load_agent(a.dump, a.agent)["bundle"]["instruction"]
    want = open(a.expected, encoding="utf-8").read()
    if live == want:
        print("OK")
        return
    diff = list(difflib.unified_diff(want.splitlines(), live.splitlines(), "expected", "live", n=0, lineterm=""))
    print("\n".join(d[:300] for d in diff[:40]))
    sys.exit(1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("extract")
    p.add_argument("dump")
    p.add_argument("--agent", type=int, required=True)
    p.add_argument("--out", required=True)
    p.set_defaults(fn=cmd_extract)
    p = sub.add_parser("patch")
    p.add_argument("instruction")
    p.add_argument("edits")
    p.add_argument("--out", required=True)
    p.add_argument("--max", type=int, default=5)
    p.set_defaults(fn=cmd_patch)
    p = sub.add_parser("verify")
    p.add_argument("dump")
    p.add_argument("--agent", type=int, required=True)
    p.add_argument("--expected", required=True)
    p.set_defaults(fn=cmd_verify)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
