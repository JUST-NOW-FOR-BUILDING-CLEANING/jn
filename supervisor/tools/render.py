#!/usr/bin/env python3
"""Turn one respond.io conversation into a readable transcript plus deterministic checks.

Input: a JSON Lines file written from respond.io `list_messages` results. First line is a header
`{"contact": <id>, "name": "...", "channel": <channelId>}`, then one line per message:
    {"id": <messageId>, "d": "in"|"out", "s": <sender.source>, "u": <userId|workflowId|null>,
     "t": <type>, "x": <exact text or caption>, "st": <final status or null>, "err": <failure reason>, "ch": <channelId>}
messageId // 1_000_000 is the epoch second of the message.

Usage:
    python3 render.py RAW.jsonl --config config.json [--rules rules.json] [--since "2026-09-26 12:00"]
                      [--out-dir DIR] [--quiet]
Writes DIR/transcripts/<id>.txt and DIR/metrics/<id>.json and prints both unless --quiet.
"""
import argparse
import datetime
import json
import os
import re
import statistics
import sys


def load_json(path, default=None):
    if not path:
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def parse_local(s, tz):
    return int(datetime.datetime.strptime(s, "%Y-%m-%d %H:%M").replace(tzinfo=tz).timestamp())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("raw")
    ap.add_argument("--config", required=True)
    ap.add_argument("--rules")
    ap.add_argument("--since", help="window start, local time 'YYYY-MM-DD HH:MM'")
    ap.add_argument("--marker", action="append", default=[],
                    help="extra timeline marker 'YYYY-MM-DD HH:MM=label' (e.g. a prompt update); repeatable")
    ap.add_argument("--now", help="local time used to judge an unanswered tail (default: now)")
    ap.add_argument("--out-dir", default=".")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    cfg = load_json(a.config)
    rules = load_json(a.rules, {}) or {}
    tz = datetime.timezone(datetime.timedelta(hours=cfg.get("utc_offset_hours", 4)))
    since = parse_local(a.since, tz) if a.since else 0
    now = parse_local(a.now, tz) if a.now else int(datetime.datetime.now(tz).timestamp())
    markers = []
    for m in a.marker:
        when, _, label = m.partition("=")
        markers.append((parse_local(when.strip(), tz), label.strip() or when.strip()))
    markers.sort()

    bots = set(cfg["bot_user_ids"])
    humans = set(cfg.get("human_user_ids", []))
    channels = {int(k): v for k, v in cfg.get("channels", {}).items()}
    link = cfg["booking_link"]
    greeting_marker = cfg.get("greeting_marker", "")
    handoff_phrases = [p.lower() for p in cfg.get("handoff_phrases", [])]
    all_prices = set(rules.get("all_prices", []))
    banned = set(rules.get("banned_numbers", cfg.get("banned_numbers", [])))

    def fmt(t):
        return datetime.datetime.fromtimestamp(t, tz).strftime("%Y-%m-%d %H:%M:%S")

    def who(m):
        s, u = m.get("s"), m.get("u")
        if m.get("d") == "in" or s == "contact":
            return "CUSTOMER"
        if s == "ai_agent" or (s == "user" and u in bots):
            return "BOT"
        if s == "user":
            return "HUMAN" if (not humans or u in humans) else f"USER:{u}"
        if s == "echo":
            return "HUMAN_PHONE"
        if s == "workflow":
            return f"WORKFLOW:{u}"
        return (s or "OUT").upper()

    header, msgs, seen = {}, [], set()
    with open(a.raw, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except json.JSONDecodeError as e:
                sys.exit(f"{a.raw} line {n}: invalid JSON ({e})")
            if "contact" in o:
                header = o
            elif o["id"] not in seen:
                seen.add(o["id"])
                msgs.append(o)
    msgs.sort(key=lambda m: int(m["id"]))
    for m in msgs:
        m["_t"] = int(m["id"]) // 1_000_000
        m["_w"] = who(m)
    cid = header.get("contact") or os.path.basename(a.raw).split(".")[0]

    lines = [f"# contact {cid} | {header.get('name', '')} | "
             f"{', '.join(sorted({channels.get(m.get('ch'), str(m.get('ch'))) for m in msgs if m.get('ch')}))}"]
    pending_markers = [(since, "WINDOW START")] if since else []
    pending_markers += markers
    pending_markers.sort()
    for m in msgs:
        while pending_markers and m["_t"] >= pending_markers[0][0]:
            lines.append(f"===== {pending_markers.pop(0)[1]} =====")
        text = (m.get("x") or "").replace("\r", "").replace("\n", " ⏎ ")
        kind = m.get("t") or "text"
        tag = "" if kind == "text" else f"[{kind}] "
        fail = ""
        if m.get("d") == "out" and m.get("st") in ("failed", "pending"):
            fail = f"  ({m['st'].upper()}{': ' + m['err'] if m.get('err') else ''})"
        lines.append(f"[{fmt(m['_t'])}] {m['_w']}: {tag}{text}{fail}")

    win = [m for m in msgs if m["_t"] >= since]
    bot_w = [m for m in win if m["_w"] == "BOT"]
    cust_w = [m for m in win if m["_w"] == "CUSTOMER"]
    human_w = [m for m in win if m["_w"] in ("HUMAN", "HUMAN_PHONE") or m["_w"].startswith("USER:")]

    def delivered(x):
        # a failed send never reached the customer, so it does not count as a reply
        return not (x.get("d") == "out" and x.get("st") == "failed")

    delays, tail = [], None
    for i, m in enumerate(msgs):
        if m["_w"] != "CUSTOMER" or m["_t"] < since:
            continue
        nxt = next((x for x in msgs[i + 1:] if x["_w"] != "CUSTOMER" and delivered(x)), None)
        if nxt is None:
            tail = m
        elif msgs[i + 1]["_w"] != "CUSTOMER":
            delays.append((nxt["_t"] - m["_t"]) / 60)

    bot_texts = [m.get("x") or "" for m in bot_w]
    joined = "\n".join(bot_texts)
    links = [l.rstrip(".,;:!)*") for l in re.findall(r"https?://\S*justnow\.life\S*", joined)]
    prices = []
    for m in bot_w:
        for mm in re.finditer(r"(?:AED|Dhs?|درهم)\s*([\d٠-٩][\d٠-٩,،]*)|([\d٠-٩][\d٠-٩,،]*)\s*(?:AED|درهم|dirham)",
                              m.get("x") or "", re.I):
            raw = (mm.group(1) or mm.group(2)).translate(str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789"))
            raw = raw.replace(",", "").replace("،", "")
            if raw.isdigit():
                v = int(raw)
                prices.append({"aed": v, "time": fmt(m["_t"]),
                               "in_price_table": (v in all_prices) if all_prices else None,
                               "banned": v in banned})
    counts = {}
    for x in bot_texts:
        k = re.sub(r"\s+", " ", x.strip())
        if len(k) > 15:
            counts[k] = counts.get(k, 0) + 1

    metrics = {
        "contact_id": int(cid) if str(cid).isdigit() else cid,
        "name": header.get("name"),
        "in_window": bool(win),
        "first_msg": fmt(msgs[0]["_t"]) if msgs else None,
        "first_msg_in_window": fmt(win[0]["_t"]) if win else None,
        "last_msg": fmt(msgs[-1]["_t"]) if msgs else None,
        "started_before_window": bool(msgs) and msgs[0]["_t"] < since,
        "n_customer": len(cust_w), "n_bot": len(bot_w), "n_human": len(human_w),
        "reply_delay_max_min": round(max(delays), 1) if delays else None,
        "reply_delay_median_min": round(statistics.median(delays), 1) if delays else None,
        "last_msg_from_customer": bool(tail),
        "waiting_min": round((now - tail["_t"]) / 60) if tail else None,
        "waiting_text": ((tail.get("x") or tail.get("t") or "")[:200]) if tail else None,
        "greetings_sent": sum(1 for x in bot_texts if greeting_marker and greeting_marker in x),
        "booking_links": len(links),
        "booking_links_exact": sum(1 for l in links if l == link),
        "markdown": sum(1 for x in bot_texts if "**" in x or re.search(r"^#{1,3} ", x, re.M)),
        "literal_backslash_n": sum(1 for x in bot_texts if "\\n" in x),
        "prices_quoted": prices,
        "prices_not_in_table": sorted({p["aed"] for p in prices if p["in_price_table"] is False}),
        "banned_numbers": sorted({p["aed"] for p in prices if p["banned"]}),
        "money_words": sum(1 for x in bot_texts if re.search(r"\bVAT\b|\btax\b|ضريب|discount|خصم|promo", x, re.I)),
        "repeated_bot_texts": [k[:120] for k, c in counts.items() if c > 1],
        "consecutive_bot_msgs": sum(1 for p, q in zip(msgs, msgs[1:])
                                    if p["_t"] >= since and p["_w"] == "BOT" and q["_w"] == "BOT"),
        "handoff_phrase": any(p in joined.lower() for p in handoff_phrases),
        "failed_msgs": [{"time": fmt(m["_t"]), "err": m.get("err")} for m in win
                        if m.get("d") == "out" and m.get("st") == "failed"],
        "customer_media": sum(1 for m in cust_w if (m.get("t") or "text") != "text"),
    }

    for sub, content in (("transcripts", "\n".join(lines) + "\n"),
                         ("metrics", json.dumps(metrics, ensure_ascii=False, indent=1))):
        os.makedirs(os.path.join(a.out_dir, sub), exist_ok=True)
        ext = "txt" if sub == "transcripts" else "json"
        with open(os.path.join(a.out_dir, sub, f"{cid}.{ext}"), "w", encoding="utf-8") as f:
            f.write(content)
    if not a.quiet:
        print("\n".join(lines))
        print("\n--- AUTOMATIC CHECKS ---")
        print(json.dumps(metrics, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
