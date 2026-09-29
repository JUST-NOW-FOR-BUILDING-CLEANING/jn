#!/usr/bin/env python3
"""Aggregate per-conversation reviews into the daily report numbers.

Reads WORK/audit/*.json (one review per conversation, fields in supervisor/rubric.md) and
WORK/metrics/*.json (written by render.py). Prints a JSON summary.

Usage:
    python3 aggregate.py WORK [--split "YYYY-MM-DD HH:MM=label" ...]
--split cuts the day into periods by first message time (e.g. before/after an instruction change).
"""
import argparse
import collections
import glob
import json
import os
import statistics
import sys

NON_LEADS = {"job_seeker", "sales_or_spam", "outside_uae", "existing_customer_support"}
BOOKED_STAGES = {"customer_said_booked", "booking_confirmed"}


def load(pattern):
    out = {}
    for path in glob.glob(pattern):
        try:
            with open(path, encoding="utf-8") as f:
                d = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"skipping {path}: {e}", file=sys.stderr)
            continue
        key = d.get("contact_id") or os.path.basename(path).split(".")[0]
        out[str(key)] = d
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("work")
    ap.add_argument("--split", action="append", default=[])
    a = ap.parse_args()

    reviews = load(os.path.join(a.work, "audit", "*.json"))
    metrics = load(os.path.join(a.work, "metrics", "*.json"))
    inw = {k: v for k, v in reviews.items() if v.get("in_window")}
    leads = {k: v for k, v in inw.items() if v.get("outcome") not in NON_LEADS}
    booked = {k for k, v in inw.items() if v.get("outcome") == "booked" or v.get("furthest_stage") in BOOKED_STAGES}
    first = {k: (metrics.get(k) or {}).get("first_msg_in_window") or "" for k in inw}

    cuts = sorted((s.partition("=")[0].strip(), s.partition("=")[2].strip()) for s in a.split)

    def period(k):
        label = "start"
        for when, name in cuts:
            if first[k] >= when:
                label = name
        return label

    mistakes = collections.Counter()
    convs_with = collections.Counter()
    severity = collections.Counter()
    for v in inw.values():
        types = set()
        for m in v.get("mistakes") or []:
            mistakes[m.get("type")] += 1
            severity[m.get("severity")] += 1
            types.add(m.get("type"))
        convs_with.update(types)

    hourly = collections.defaultdict(collections.Counter)
    periods = collections.defaultdict(collections.Counter)
    for k, v in leads.items():
        for bucket in (hourly[first[k][:13]], periods[period(k)]):
            bucket["leads"] += 1
            bucket["answered_first_reply"] += bool(v.get("customer_answered_greeting"))
            bucket["priced"] += bool(v.get("prices_quoted"))
            bucket["booked"] += k in booked
            bucket["silent_after_price"] += v.get("outcome") == "silent_after_price"
            bucket["high_mistakes"] += sum(1 for m in v.get("mistakes") or [] if m.get("severity") == "high")

    delays = [m["reply_delay_max_min"] for k, m in metrics.items()
              if k in inw and m.get("reply_delay_max_min") is not None]
    human = [v["owner_reply_delay_min"] for v in inw.values()
             if isinstance(v.get("owner_reply_delay_min"), (int, float))]
    prices = [p for v in inw.values() for p in v.get("prices_quoted") or []]

    out = {
        "conversations": len(inw),
        "leads": len(leads),
        "bookings": sorted(booked),
        "outcomes": collections.Counter(v.get("outcome") for v in inw.values()).most_common(),
        "furthest_stage": collections.Counter(v.get("furthest_stage") for v in leads.values()).most_common(),
        "answered_first_reply": sum(1 for v in leads.values() if v.get("customer_answered_greeting")),
        "priced": sum(1 for v in leads.values() if v.get("prices_quoted")),
        "prices_quoted": len(prices),
        "prices_wrong": sum(1 for p in prices if p.get("correct") is False),
        "links_sent": sum(1 for v in inw.values() if v.get("booking_link_sent")),
        "links_exact": sum(1 for v in inw.values() if v.get("booking_link_exact") is True),
        "mistakes": mistakes.most_common(),
        "conversations_with_mistake": convs_with.most_common(),
        "severity": severity.most_common(),
        "good": collections.Counter(g for v in inw.values() for g in v.get("good_types") or []).most_common(),
        "waiting_for_human_now": sorted(k for k, v in inw.items() if v.get("waiting_for_human_now")),
        "unanswered": sorted(k for k, v in inw.items() if v.get("unanswered_customer_message")),
        "bot_reply_max_delay_median_min": statistics.median(delays) if delays else None,
        "human_reply_delay_median_min": statistics.median(human) if human else None,
        "failed_message_conversations": sorted(k for k, m in metrics.items() if k in inw and m.get("failed_msgs")),
        "hourly": {h: dict(c) for h, c in sorted(hourly.items()) if h},
        "periods": {p: dict(c) for p, c in periods.items()},
    }
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    print()


if __name__ == "__main__":
    main()
