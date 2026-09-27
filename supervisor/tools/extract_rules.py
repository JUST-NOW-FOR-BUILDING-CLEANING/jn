#!/usr/bin/env python3
"""Extract the PRICE TABLE and ZONES from the live respond.io AI agent instruction.

The bot's own prompt is the single source of truth for prices, so nothing price-related is stored in this repo.
Usage:
    python3 extract_rules.py instruction.txt > rules.json
where instruction.txt is `bundle.instruction` from respond.io get_ai_agent.
"""
import json
import re
import sys

ROW = re.compile(r"^-\s*(?P<row>.+?),\s*zone\s+(?P<zone>[A-E]):\s*(?P<pkgs>.+)$", re.I)
PKG = re.compile(r"(?P<cleaners>\d+)\s*cleaners?\s*x\s*(?P<hours>\d+)\s*h\s*=\s*(?P<aed>\d[\d,]*)", re.I)
EMIRATE = re.compile(r"^-\s*(?P<emirate>Dubai|Sharjah|Ajman|Umm Al Quwain|Ras Al Khaimah|Fujairah):\s*default zone\s+(?P<default>[A-E])", re.I)
ZONE_LIST = re.compile(r"Zone\s+(?P<zone>[A-E]):\s*(?P<areas>[^.]+)\.")


def row_key(name):
    n = name.lower()
    if n.startswith("kitchen"):
        return "kitchen"
    if n.startswith("studio"):
        return "studio"
    if n.startswith("1 bhk"):
        return "1bhk"
    if n.startswith("2 bhk"):
        return "2bhk"
    if n.startswith("3 bhk"):
        return "3bhk"
    if n.startswith("villa 4"):
        return "villa4"
    if n.startswith("villa 5"):
        return "villa5plus"
    return re.sub(r"[^a-z0-9]+", "_", n).strip("_")


def extract(text):
    prices, zones = {}, {}
    for line in text.splitlines():
        line = line.strip()
        m = ROW.match(line)
        if m and PKG.search(m.group("pkgs")):
            pk = [{"cleaners": int(p["cleaners"]), "hours": int(p["hours"]), "aed": int(p["aed"].replace(",", ""))}
                  for p in PKG.finditer(m.group("pkgs"))]
            prices.setdefault(row_key(m.group("row")), {})[m.group("zone").upper()] = pk
            continue
        e = EMIRATE.match(line)
        if e:
            em = e.group("emirate").title()
            entry = {"default": e.group("default").upper(), "areas": {}}
            for z in ZONE_LIST.finditer(line):
                for area in z.group("areas").split(","):
                    area = area.strip()
                    if area:
                        entry["areas"][area] = z.group("zone").upper()
            zones[em] = entry
    first = sorted({pk[0]["aed"] for row in prices.values() for pk in row.values()})
    every = sorted({p["aed"] for row in prices.values() for pk in row.values() for p in pk})
    links = sorted({l.rstrip(".,;:") for l in re.findall(r"https://www\.justnow\.life/book-now[^\s\"')]*", text)})
    banned = re.search(r"Never say these numbers:\s*([^\n]+)", text)
    banned_nums = sorted({int(x) for x in re.findall(r"\b(\d{3})\b", banned.group(1))}) if banned else []
    return {"prices": prices, "zones": zones, "first_package_prices": first, "all_prices": every,
            "booking_links_in_prompt": links, "banned_numbers": banned_nums}


if __name__ == "__main__":
    src = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    rules = extract(src)
    if not rules["prices"]:
        sys.exit("no PRICE TABLE rows found - has the prompt format changed?")
    json.dump(rules, sys.stdout, ensure_ascii=False, indent=1)
