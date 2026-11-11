"""Turn the website's "New booking request" emails into a lead register and a report.

The website (justnow.life) sends staff two kinds of email (checked on 2026-11-11):
  * "New booking request JN-..." to customer.care@justnow.life for requests it cannot confirm
    by itself: no free team at the requested time, no listed price (sofa, mattress and carpet
    only, or a home or area that is not in the price list), or kitchen add-ons;
  * "New booking - JN-..." to the company Gmail for bookings it confirms by itself.
This script reads the first kind. They are plain text in a fixed layout:

    Booking request JN-147290 (website, EN)

    Service: Full home deep cleaning
    Home: Furnished, 2 bedrooms
    Team: 3 cleaners × 4 hours
    Price shown: AED 549
    Area: International City, Dubai (zone B)
    Address: ...
    Preferred: 2026-10-24, Afternoon (12 – 2 PM)
    No free team in the website schedule at this time - ...      (optional line)
    Name: ...
    Mobile: ...
    Email: ...
    Notes: ...                                                   (may span several lines)

    Possible conflict: another request exists for this date, slot and area.   (optional line)

Input: a JSONL file, one email per line: {"uid": 562, "received_utc": "2026-11-11T08:46:14Z",
"unread": true, "text": "<plain text body>"}. The file holds customer data, so it is
never committed; only the aggregated report (no names, phones or emails) is.

    python3 hostinger/booking_requests.py requests.jsonl \
        --crm crm_match.json --bounces bounces.json --calendar calendar.json \
        --xlsx JustNow-Email-Leads.xlsx --report hostinger/REPORT-booking-requests.md

crm_match.json (optional): {"emails": [...], "phones": [...]} already found in HubSpot.
bounces.json   (optional): [{"ref": "JN-147351", "recipient": "...", "reason": "..."}].
calendar.json  (optional): Google Calendar export of "Cleaning Services Schedule", {"events": [...]}.
                           Export from the first booking date to at least 60 days ahead, otherwise
                           later jobs look as if they had left the calendar. A booking event carries
                           "Reference: JN-xxxxxx"; its title starts with UNCONFIRMED until the owner
                           confirms it; a line "Done <date>" is added when the job is completed;
                           a deleted event is simply absent.
"""
import argparse
import collections
import datetime as dt
import json
import re

DUBAI = dt.timezone(dt.timedelta(hours=4))
FIELDS = [
    ("service", "Service"), ("home", "Home"), ("team", "Team"), ("price_shown", "Price shown"),
    ("pieces", r"Pieces \(price from photos\)"), ("area_raw", "Area"), ("address", "Address"),
    ("preferred", "Preferred"), ("name", "Name"), ("mobile", "Mobile"), ("email", "Email"),
]


ARABIC_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩۰۱۲۳۴۵۶۷۸۹", "01234567890123456789")


def norm_phone(p):
    """UAE mobile in any spelling -> +9715xxxxxxxx. Foreign numbers keep their own code."""
    first = re.split(r"[/,;]| or ", (p or "").translate(ARABIC_DIGITS))[0]   # first number in the field
    d = re.sub(r"\D", "", first)
    if d.startswith("00"):
        d = d[2:]
    if d.startswith("9710"):
        d = "971" + d[4:]
    if d.startswith("0") and len(d) in (9, 10):      # 05x mobile or 0x landline
        d = "971" + d[1:]
    if len(d) == 9 and d[0] == "5":
        d = "971" + d
    return "+" + d if d else ""


def uae_guess(phone):
    """A UAE mobile typed after a wrong country code (+20 5xxxxxxxx): return the +971 form, else ''."""
    d = phone.lstrip("+")
    m = re.fullmatch(r"(\d{1,2})(5\d{8})", d)
    return "+971" + m.group(2) if m and not d.startswith("971") else ""


def parse_request(text, received_utc="", uid=None, unread=None):
    t = text.replace("\r", "")
    # Customer-typed notes come last; never let them overwrite the fields above them.
    head, _, tail = t.partition("\nNotes:")
    d = {"uid": uid, "received_utc": received_utc, "unread": unread}
    h = re.match(r"Booking request (\S+) \((\w+), (\w+)\)", head)
    d["ref"], d["channel"], d["lang"] = h.groups() if h else ("", "", "")
    for key, label in FIELDS:
        m = re.search(r"^" + label + r": (.*)$", head, re.M)
        d[key] = m.group(1).strip() if m else ""
    d["possible_conflict"] = bool(re.search(r"^Possible conflict:", tail, re.M))
    notes = re.split(r"\n\s*Possible conflict:", "\n" + tail)[0]
    d["notes"] = " ".join(notes.split())
    d["no_free_team"] = bool(re.search(r"^No free team in the website schedule", head, re.M))

    m = re.match(r"(.*), ([^,(]+) \((.*)\)$", d["area_raw"])
    if m:
        d["area"], d["emirate"] = m.group(1).strip(), m.group(2).strip()
        z = re.search(r"zone (\w)", m.group(3))
        d["zone"] = z.group(1) if z else "not in price list"
    else:
        d["area"], d["emirate"], d["zone"] = d["area_raw"], "", ""
    m = re.search(r"AED ([\d,]+)", d["price_shown"])
    d["price_aed"] = int(m.group(1).replace(",", "")) if m else None
    m = re.search(r"(\d+) cleaners? . (\d+) hours?", d["team"])
    d["cleaners"], d["hours"] = (int(m.group(1)), int(m.group(2))) if m else (None, None)
    m = re.match(r"(\d{4}-\d{2}-\d{2}), (.*)", d["preferred"])
    d["pref_date"], d["pref_slot"] = (m.group(1), m.group(2)) if m else ("", "")
    d["slot"] = (re.match(r"\w+", d["pref_slot"]) or [""])[0] if d["pref_slot"] else ""

    d["phone"] = norm_phone(d["mobile"])
    d["phone_guess"] = uae_guess(d["phone"])
    d["email"] = "" if d["email"] in ("—", "-") else d["email"].strip().lower()
    if d["notes"] in ("—", "-"):
        d["notes"] = ""
    d["service_group"] = d["service"].split(" +")[0]
    # Why the website could not confirm it by itself.
    if d["no_free_team"]:
        d["reason"] = "No free team at requested time"
    elif d["service"] != d["service_group"]:
        d["reason"] = "Kitchen add-ons"
    elif d["price_aed"] is None:
        d["reason"] = "No listed price"
    else:
        d["reason"] = "Other (before 18 Oct every request came here)"
    d["is_test"] = bool(
        re.search(r"\btest\b|^b+$", d["name"], re.I)
        or d["email"] in ("justnow.cs@gmail.com",)
        or d["mobile"].strip("0+ ") == ""
    )
    if received_utc:
        local = dt.datetime.fromisoformat(received_utc.replace("Z", "+00:00")).astimezone(DUBAI)
        d["received_dubai"] = local.strftime("%Y-%m-%d %H:%M")
        d["lead_days"] = (dt.date.fromisoformat(d["pref_date"]) - local.date()).days if d["pref_date"] else None
    else:
        d["received_dubai"], d["lead_days"] = "", None
    return d


def load(path):
    rows = []
    for line in open(path, encoding="utf-8"):
        if line.strip():
            j = json.loads(line)
            rows.append(parse_request(j["text"], j.get("received_utc", ""), j.get("uid"), j.get("unread")))
    return sorted(rows, key=lambda r: r["received_utc"])


def load_calendar(path):
    """Google Calendar export -> ({ref: outcome}, set of customer phones that have any event)."""
    j = json.load(open(path, encoding="utf-8"))
    events = j["events"] if isinstance(j, dict) else j
    by_ref, phones = {}, set()
    for e in events:
        desc = re.sub(r"<[^>]+>", "\n", e.get("description") or "")
        title = e.get("summary") or ""
        # Phones first, from every event: a customer rebooked by hand has no reference.
        for raw in re.findall(r"wa\.me/(\d+)", desc) + re.findall(r"(?:\+|00)?971[\s-]?5[\d\s-]{8,11}|\b05\d[\d\s-]{7,9}", desc + " " + title):
            if norm_phone(raw):
                phones.add(norm_phone(raw))
        # Only the event's own reference counts, not a number mentioned in a note.
        refs = set(re.findall(r"(?:Reference:|Booking request)\s*(JN-\d{6})", desc)) or set(re.findall(r"JN-\d{6}", title))
        if not refs:
            continue
        done = re.search(r"(?im)^\s*-?\s*done\s*-?\s*(\d{4}-\d{2}-\d{2})", desc)
        if title.upper().lstrip().startswith("UNCONFIRMED"):
            status = "unconfirmed"
        elif done:
            status = "done"
        else:
            status = "confirmed"
        start = e.get("start") or {}
        day = (start.get("dateTime") or start.get("date") or "")[:10] if isinstance(start, dict) else ""
        for r in refs:
            by_ref[r] = {"status": status, "done_on": done.group(1) if done else "", "title": title, "date": day}
    return by_ref, phones


OUTCOME_LABEL = {
    "done": "Done",
    "confirmed": "In calendar, not marked done",
    "unconfirmed": "In calendar, still UNCONFIRMED",
    "gone": "No longer in the calendar",
}


def enrich(rows, crm=None, bounces=None, calendar=None):
    crm = crm or {}
    emails = {e.lower() for e in crm.get("emails", [])}
    phones = set(crm.get("phones", []))
    bounced = {b["ref"]: b for b in (bounces or [])}
    cal_refs, cal_phones = calendar or ({}, set())
    per_phone = collections.Counter(r["phone"] for r in rows if not r["is_test"])
    for r in rows:
        if not crm:
            r["in_crm"] = ""
        elif r["email"] and r["email"] in emails:
            r["in_crm"] = "yes (email)"
        elif r["phone"] and r["phone"] in phones:
            r["in_crm"] = "yes (phone)"
        else:
            r["in_crm"] = "no"
        b = bounced.get(r["ref"])
        r["email_bounced"] = b["reason"] if b else ""
        r["requests_by_phone"] = per_phone.get(r["phone"], 1)
        if calendar:
            c = cal_refs.get(r["ref"])
            r["outcome"] = c["status"] if c else "gone"
            r["done_on"] = c["done_on"] if c else ""
            # the same customer may have been booked under another reference
            r["customer_in_calendar"] = bool(c) or (r["phone"] in cal_phones)
        else:
            r["outcome"], r["done_on"], r["customer_in_calendar"] = "", "", None
    return rows


def ref_number(ref):
    m = re.match(r"JN-(\d{6})$", ref or "")
    return int(m.group(1)) if m else None


# ---------------------------------------------------------------- report (no customer data)

def pct(a, b):
    return f"{100 * a / b:.0f}%" if b else "-"


def table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" if i == 0 else "---:" for i in range(len(header))) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def counter_table(rows, key, title, top=None):
    c = collections.Counter(r[key] or "(blank)" for r in rows)
    return table([title, "Requests", "Share"], [[k, v, pct(v, len(rows))] for k, v in c.most_common(top)])


def safe_area(text):
    """Area names are typed by customers: keep them short and drop anything that looks like a number."""
    return re.sub(r"\s+", " ", re.sub(r"\d{4,}", "", text)).strip()[:40]


def build_report(rows, bounces=None, calendar=None, title="Website booking requests in the mailbox"):
    real = [r for r in rows if not r["is_test"]]
    n = len(real)
    first, last = real[0]["received_dubai"][:10], real[-1]["received_dubai"][:10]
    days = (dt.date.fromisoformat(last) - dt.date.fromisoformat(first)).days + 1
    priced = [r for r in real if r["price_aed"]]
    total = sum(r["price_aed"] for r in priced)
    phones = collections.Counter(r["phone"] for r in real)
    repeat = {p: c for p, c in phones.items() if c > 1}
    unread = [r for r in real if r["unread"]]
    unread_from = min((r["received_dubai"] for r in unread), default="")
    since_unread = [r for r in real if unread_from and r["received_dubai"] >= unread_from]
    nums = sorted(x for x in (ref_number(r["ref"]) for r in rows) if x and x > 100000)
    lo, hi = (nums[0], nums[-1]) if nums else (0, 0)
    issued = hi - lo + 1 if nums else 0                     # booking numbers are sequential, no gaps
    emailed = len(nums)
    in_range = [r for r in real if lo <= (ref_number(r["ref"]) or 0) <= hi]

    L = [f"# {title}\n"]
    L.append(f"Period: {first} to {last} ({days} days, Dubai time). Source: the website's \"New booking request\" emails in "
             f"`INBOX.01 Leads - Booking Requests`. No customer names, phones or emails in this file.\n")
    L.append("## Read this first: what these emails are\n")
    L.append(f"The website sends staff two kinds of email. Requests it cannot confirm by itself arrive in this mailbox as "
             f"\"New booking request\": no free team at the requested time, no listed price (sofa, mattress and carpet only, "
             f"or a home or area that is not in the price list), or kitchen add-ons. Bookings it confirms by itself are "
             f"announced as \"New booking\" to the company Gmail and are not in this report. Booking numbers JN-{lo:06d} to "
             f"JN-{hi:06d} were issued for {issued} bookings, owner tests included; {emailed} of them ({pct(emailed, issued)}) "
             f"came to this mailbox. Every share below is a share of the requests in this mailbox unless it says otherwise.\n")
    L.append("## Totals\n")
    L.append(table(["Metric", "Value"], [
        ["Booking requests received by email", len(rows)],
        ["Test / owner entries excluded below", len(rows) - n],
        ["Real requests", n],
        ["Unique customers (by mobile)", len(phones)],
        ["Customers who sent more than one request", f"{len(repeat)} ({sum(repeat.values())} requests)"],
        ["Average per day", f"{n / days:.1f}"],
        ["Requests with a price shown", f"{len(priced)} ({pct(len(priced), n)})"],
        ["Value of prices shown (AED)", f"{total:,}"],
        ["Average price shown (AED)", f"{total / len(priced):.0f}" if priced else "-"],
        ["Request emails still unread in the mailbox", f"{len(unread)} ({pct(len(unread), n)})"],
    ]))
    if unread:
        L.append(f"\nAll {len(unread)} unread emails arrived from {unread_from} on ({len(unread)} of the {len(since_unread)} "
                 f"requests since then). Every earlier one was read.")

    if calendar:
        cal_refs, _ = calendar
        order = ["done", "confirmed", "unconfirmed", "gone"]
        L.append("\n## What happened to these requests (from the calendar)\n")
        oc = collections.Counter(r["outcome"] for r in real)
        val = lambda k: sum(r["price_aed"] or 0 for r in real if r["outcome"] == k)
        L.append(table(["Outcome", "Requests", "Share", "Prices shown (AED)"],
                       [[OUTCOME_LABEL[k], oc[k], pct(oc[k], n), f"{val(k):,}"] for k in order]))
        L.append("\nThe amounts are the prices the website showed at request time, not the final prices in the calendar.")
        gone = [r for r in real if r["outcome"] == "gone"]
        rebooked = sum(1 for r in gone if r["customer_in_calendar"])
        L.append(f"\nA request that is no longer in the calendar was cancelled, was a duplicate, was never confirmed, or was "
                 f"booked again under another number: {rebooked} of the {len(gone)} belong to customers who still have "
                 f"another booking in the calendar.")
        cust = collections.defaultdict(list)
        for r in real:
            cust[r["phone"]].append(r)
        lost = {p: rs for p, rs in cust.items() if not any(r["customer_in_calendar"] for r in rs)}
        lost_priced = [max((r["price_aed"] or 0) for r in rs) for rs in lost.values()]
        L.append(f"\nCustomers with no booking in the calendar at all: {len(lost)} of {len(cust)} ({pct(len(lost), len(cust))}). "
                 f"{sum(1 for v in lost_priced if v)} of them were shown a price, AED {sum(lost_priced):,} in total. "
                 f"They are the \"Lost leads\" sheet of the lead register.\n")

        emailed_refs = {r["ref"] for r in rows}
        others = [k for k, v in cal_refs.items() if lo <= (ref_number(k) or 0) <= hi and k not in emailed_refs]
        others_done = sum(1 for k in others if cal_refs[k]["status"] == "done")
        not_emailed = issued - emailed
        kept = [r for r in in_range if r["outcome"] != "gone"]
        done_in = sum(1 for r in in_range if r["outcome"] == "done")
        L.append(table(["Booking numbers in the same range", "Bookings", "Still in calendar", "Done"], [
            ["Sent to this mailbox (the website could not confirm)", len(in_range),
             f"{len(kept)} ({pct(len(kept), len(in_range))})", f"{done_in} ({pct(done_in, len(in_range))})"],
            ["Confirmed by the website itself (announced to the Gmail)", not_emailed,
             f"{len(others)} ({pct(len(others), not_emailed)})", f"{others_done} ({pct(others_done, not_emailed)})"],
        ]))
        L.append("\nThe second group includes a few owner test bookings that cannot be told apart here. "
                 "A gap of a few points between the two groups is within chance at these sizes.")
        waiting = [k for k in others if cal_refs[k]["status"] == "unconfirmed"]
        overdue = sum(1 for k in waiting if cal_refs[k]["date"] and cal_refs[k]["date"] < last)
        L.append(f"\nA booking the website confirms by itself also starts as UNCONFIRMED in the calendar, until someone "
                 f"confirms with the customer and removes the word. {len(waiting)} of them are still UNCONFIRMED"
                 + (f", {overdue} for a date that has already passed.\n" if overdue else ".\n"))

        def split(label, key_fn, keys=None):
            groups = collections.defaultdict(list)
            for r in real:
                groups[key_fn(r)].append(r)
            ks = keys or [k for k, _ in sorted(groups.items(), key=lambda kv: -len(kv[1]))]
            body = []
            for k in ks:
                g = groups.get(k, [])
                if g:
                    d_, g_ = sum(1 for r in g if r["outcome"] == "done"), sum(1 for r in g if r["outcome"] == "gone")
                    body.append([k, len(g), f"{d_} ({pct(d_, len(g))})", f"{g_} ({pct(g_, len(g))})"])
            return table([label, "Requests", "Done", "No longer in calendar"], body)

        L.append("Groups of fewer than about 30 requests are too small to compare reliably.\n")
        L.append(split("Why it came to this mailbox", lambda r: r["reason"]))
        L.append("")
        L.append(split("Service", lambda r: r["service_group"]))
        L.append("")
        L.append(split("Slot asked", lambda r: r["slot"] or "(blank)"))
        L.append("")
        lead_lbl = lambda r: "Same day" if r["lead_days"] == 0 else ("Next day" if r["lead_days"] == 1 else "2+ days ahead")
        L.append(split("Preferred date", lead_lbl, ["Same day", "Next day", "2+ days ahead"]))
        L.append("")
        L.append(split("Emirate", lambda r: r["emirate"] or "(blank)"))
        conflicts = [r for r in real if r["possible_conflict"]]
        if conflicts:
            L.append(f"\nPossible duplicates: the website marked {len(conflicts)} requests with \"Possible conflict: another "
                     f"request exists for this date, slot and area\". {sum(1 for r in conflicts if r['outcome'] == 'gone')} "
                     f"of them are no longer in the calendar.")

    nft = [r for r in real if r["no_free_team"]]
    L.append("\n## Capacity signal: \"No free team in the website schedule\"\n")
    if nft:
        first_nft = min(ref_number(r["ref"]) for r in nft if ref_number(r["ref"]))
        since = min(r["received_dubai"][:10] for r in nft)
        issued_since = hi - first_nft + 1
        unchecked = sum(1 for r in rows if (ref_number(r["ref"]) or 0) >= first_nft and not r["no_free_team"])
        checked = issued_since - unchecked
        L.append(f"The website adds this line when its team schedule has no free team for the slot the customer picked. "
                 f"The first customer request with it arrived on {since}. Since then {issued_since} bookings were made on the "
                 f"website and {len(nft)} of them ({pct(len(nft), issued_since)}) carried the flag. The website does not run "
                 f"this check for sofa requests, kitchen add-ons or unlisted prices; among the {checked} bookings it does "
                 f"check, the share is {pct(len(nft), checked)}.\n")
        by_slot = collections.Counter(r["slot"] for r in nft)
        L.append(table(["Slot asked", "Flagged requests", "Share of flagged"],
                       [[k, v, pct(v, len(nft))] for k, v in by_slot.most_common()]))
    else:
        L.append("No request carried this line.")

    L.append("\n## Requests per day\n")
    per_day = collections.Counter(r["received_dubai"][:10] for r in real)
    per_day_f = collections.Counter(r["received_dubai"][:10] for r in real if r["no_free_team"])
    L.append(table(["Day", "Requests", "No free team"], [[d, per_day[d], per_day_f[d]] for d in sorted(per_day)]))
    L.append("\n## By service\n")
    sg = collections.Counter(r["service_group"] for r in real)
    rowsv = []
    for k, v in sg.most_common():
        p = [r["price_aed"] for r in real if r["service_group"] == k and r["price_aed"]]
        rowsv.append([k, v, pct(v, n), f"{sum(p):,}" if p else "-", f"{sum(p) / len(p):.0f}" if p else "-"])
    L.append(table(["Service", "Requests", "Share", "Prices shown (AED)", "Average (AED)"], rowsv))
    addons = sum(1 for r in real if r["service"] != r["service_group"])
    pieces = sum(1 for r in real if r["pieces"] and not r["service"].startswith("Sofa"))
    L.append(f"\nKitchen requests with bathroom or balcony add-ons: {addons}. "
             f"Kitchen or home requests that also asked for sofa, mattress, carpet or curtain pieces: {pieces}.\n")
    L.append("## By emirate\n")
    L.append(counter_table(real, "emirate", "Emirate"))
    L.append("\n## By price zone\n")
    L.append(counter_table(real, "zone", "Zone"))
    L.append("\n## Top areas\n")
    areas = collections.Counter(f"{r['area']} ({r['emirate']}, zone {r['zone']})" for r in real if r["zone"] != "not in price list")
    L.append(table(["Area", "Requests"], areas.most_common(15)))
    missing = collections.Counter(f"{safe_area(r['area'])} ({r['emirate']})" for r in real if r["zone"] == "not in price list")
    L.append("\n## Areas typed by customers that are not in the price list\n")
    L.append(table(["Area as typed", "Requests"], missing.most_common()) if missing else "None.")
    L.append("\n## Home size (full-home requests)\n")
    L.append(counter_table([r for r in real if r["home"]], "home", "Home"))
    L.append("\n## Team asked (requests with a team line)\n")
    L.append(counter_table([r for r in real if r["team"]], "team", "Team"))
    L.append("\n## How far ahead customers book\n")
    lead = collections.Counter(r["lead_days"] for r in real if r["lead_days"] is not None)
    label = lambda k: "Same day" if k == 0 else ("Next day" if k == 1 else f"{k} days ahead")
    L.append(table(["Preferred date", "Requests", "Share"], [[label(k), v, pct(v, n)] for k, v in sorted(lead.items())]))
    L.append("\n## Preferred slot\n")
    L.append(counter_table(real, "slot", "Slot"))
    L.append("\n## When requests arrive (Dubai time)\n")
    hours = collections.Counter(int(r["received_dubai"][11:13]) for r in real)
    bands = [("00:00-07:59", range(0, 8)), ("08:00-11:59", range(8, 12)), ("12:00-15:59", range(12, 16)),
             ("16:00-19:59", range(16, 20)), ("20:00-23:59", range(20, 24))]
    L.append(table(["Time band", "Requests", "Share"], [[b, sum(hours[h] for h in rng), pct(sum(hours[h] for h in rng), n)] for b, rng in bands]))
    wd = collections.Counter(dt.date.fromisoformat(r["received_dubai"][:10]).strftime("%A") for r in real)
    L.append("")
    L.append(table(["Weekday", "Requests"], [[d, wd[d]] for d in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]]))
    L.append("\n## Language and data quality\n")
    foreign = [r for r in real if not r["phone"].startswith("+9715")]
    L.append(table(["Check", "Requests"], [
        ["English form", sum(1 for r in real if r["lang"] == "EN")],
        ["Arabic form", sum(1 for r in real if r["lang"] == "AR")],
        ["With customer notes", sum(1 for r in real if r["notes"])],
        ["Without an email address", sum(1 for r in real if not r["email"])],
        ["Mobile is not a UAE mobile number", len(foreign)],
        ["of which a UAE mobile typed after a wrong country code", sum(1 for r in foreign if r["phone_guess"])],
        ["Email to the customer bounced", sum(1 for r in real if r.get("email_bounced"))],
    ]))
    if any(r.get("in_crm") for r in real):
        cust = {}
        for r in real:
            cust.setdefault(r["phone"], []).append(r["in_crm"])
        found = sum(1 for v in cust.values() if any(x.startswith("yes") for x in v))
        L.append("\n## HubSpot coverage\n")
        L.append(table(["Check", "Customers"], [
            ["Unique customers in these requests", len(cust)],
            ["Found in HubSpot by email or mobile", f"{found} ({pct(found, len(cust))})"],
            ["Not found in HubSpot", len(cust) - found],
        ]))
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------- lead register (customer data)

def build_xlsx(rows, path, bounces=None):
    from openpyxl import Workbook
    from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter

    wb = Workbook()
    head_fill, head_font = PatternFill("solid", fgColor="1F4E79"), Font(bold=True, color="FFFFFF")

    def sheet(ws, header, data, widths):
        assert len(header) == len(widths) and all(len(r) == len(header) for r in data), ws.title
        ws.append(header)
        for c in ws[1]:
            c.fill, c.font, c.alignment = head_fill, head_font, Alignment(vertical="center", wrap_text=True)
        for row in data:
            # Customer-typed text: remove characters Excel rejects.
            ws.append([ILLEGAL_CHARACTERS_RE.sub("", v) if isinstance(v, str) else v for v in row])
            for c in ws[ws.max_row]:
                if isinstance(c.value, str) and c.value[:1] in "=+-@":
                    c.data_type = "s"            # never a live formula, whatever the customer typed
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = ws.dimensions
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w

    wa = lambda r: f"https://wa.me/{(r['phone_guess'] or r['phone']).lstrip('+')}" if r["phone"] else ""
    check = lambda r: f"Typed as {r['phone']}. Looks like a UAE mobile: the link uses {r['phone_guess']}" if r["phone_guess"] else ""
    yn = lambda b: "yes" if b else ""
    real = [r for r in rows if not r["is_test"]]

    ws = wb.active
    ws.title = "Leads"
    sheet(ws, ["Received (Dubai)", "Booking ref", "Name", "Mobile", "WhatsApp", "Check number", "Email", "Service", "Home",
               "Cleaners", "Hours", "Price shown (AED)", "Extra pieces", "Area", "Emirate", "Zone", "Address", "Preferred date",
               "Slot", "Days ahead", "Why it came to the mailbox", "Possible duplicate", "Notes", "Lang", "Outcome (calendar)",
               "Done on", "In HubSpot", "Email bounced", "Requests from this mobile", "Unread in mailbox", "Test entry"],
          [[r["received_dubai"], r["ref"], r["name"], r["phone"] or r["mobile"], wa(r), check(r), r["email"], r["service"], r["home"],
            r["cleaners"], r["hours"], r["price_aed"], r["pieces"], r["area"], r["emirate"], r["zone"], r["address"], r["pref_date"],
            r["pref_slot"], r["lead_days"], r["reason"], yn(r["possible_conflict"]), r["notes"], r["lang"],
            OUTCOME_LABEL.get(r.get("outcome"), ""), r.get("done_on", ""), r.get("in_crm", ""), r.get("email_bounced", ""),
            r.get("requests_by_phone", ""), yn(r["unread"]), yn(r["is_test"])] for r in rows],
          [17, 12, 24, 16, 30, 34, 30, 30, 26, 9, 7, 11, 34, 26, 12, 9, 40, 13, 22, 8, 30, 10, 50, 6, 26, 12, 13, 30, 10, 9, 7])

    cust = collections.OrderedDict()
    for r in real:
        cust.setdefault(r["phone"] or r["mobile"], []).append(r)
    data = []
    for phone, rs in cust.items():
        prices = [r["price_aed"] for r in rs if r["price_aed"]]
        best = min(rs, key=lambda r: ["done", "confirmed", "unconfirmed", "gone", ""].index(r.get("outcome", "")))
        data.append([rs[-1]["name"], phone, wa(rs[-1]), ", ".join(sorted({r["email"] for r in rs if r["email"]})), len(rs),
                     rs[0]["received_dubai"][:10], rs[-1]["received_dubai"][:10], ", ".join(sorted({r["service_group"] for r in rs})),
                     f"{rs[-1]['area']}, {rs[-1]['emirate']}", rs[-1]["zone"], max(prices) if prices else None,
                     ", ".join(r["ref"] for r in rs), OUTCOME_LABEL.get(best.get("outcome"), ""), rs[-1].get("in_crm", ""),
                     "; ".join(sorted({r["email_bounced"] for r in rs if r.get("email_bounced")}))])
    ws = wb.create_sheet("Customers")
    sheet(ws, ["Name", "Mobile", "WhatsApp", "Email(s)", "Requests", "First request", "Last request", "Services", "Area",
               "Zone", "Highest price shown (AED)", "Booking refs", "Best outcome (calendar)", "In HubSpot", "Email bounced"],
          data, [24, 16, 30, 34, 9, 13, 13, 40, 30, 8, 12, 36, 26, 13, 30])

    if any(r.get("outcome") for r in real):
        lost = [(phone, rs) for phone, rs in cust.items() if not any(r["customer_in_calendar"] for r in rs)]
        ws = wb.create_sheet("Lost leads")
        sheet(ws, ["Name", "Mobile", "WhatsApp", "Check number", "Email", "Last request", "Booking refs", "Service", "Home", "Team",
                   "Price shown (AED)", "Asked for", "Why it came to the mailbox", "Area", "Notes", "In HubSpot", "Email bounced"],
              [[rs[-1]["name"], phone, wa(rs[-1]), check(rs[-1]), rs[-1]["email"], rs[-1]["received_dubai"],
                ", ".join(r["ref"] for r in rs), rs[-1]["service"], rs[-1]["home"], rs[-1]["team"],
                max((r["price_aed"] or 0) for r in rs) or None, f"{rs[-1]['pref_date']} {rs[-1]['pref_slot']}", rs[-1]["reason"],
                f"{rs[-1]['area']}, {rs[-1]['emirate']} (zone {rs[-1]['zone']})", rs[-1]["notes"], rs[-1].get("in_crm", ""),
                "; ".join(sorted({r["email_bounced"] for r in rs if r.get("email_bounced")}))] for phone, rs in lost],
              [24, 16, 30, 34, 30, 17, 24, 30, 26, 20, 11, 30, 30, 36, 50, 13, 30])

    ws = wb.create_sheet("Not in HubSpot")
    sheet(ws, ["Name", "Mobile", "WhatsApp", "Email(s)", "Requests", "Last request", "Services", "Area", "Highest price shown (AED)",
               "Booking refs", "Best outcome (calendar)"],
          [[d[0], d[1], d[2], d[3], d[4], d[6], d[7], d[8], d[10], d[11], d[12]] for d in data if d[13] == "no"],
          [24, 16, 30, 34, 9, 13, 40, 30, 12, 36, 26])

    by_ref = {r["ref"]: r for r in rows}
    ws = wb.create_sheet("Bounced emails")
    sheet(ws, ["Booking ref", "Address that failed", "Why", "Customer name", "Mobile", "WhatsApp"],
          [[b["ref"], b["recipient"], b["reason"], by_ref[b["ref"]]["name"] if b["ref"] in by_ref else "(confirmed by the website, see the Gmail)",
            by_ref[b["ref"]]["phone"] if b["ref"] in by_ref else "", wa(by_ref[b["ref"]]) if b["ref"] in by_ref else ""] for b in (bounces or [])],
          [12, 36, 46, 36, 16, 30])
    wb.save(path)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("requests")
    ap.add_argument("--crm")
    ap.add_argument("--bounces")
    ap.add_argument("--calendar")
    ap.add_argument("--xlsx")
    ap.add_argument("--report")
    a = ap.parse_args()
    crm = json.load(open(a.crm)) if a.crm else None
    bounces = json.load(open(a.bounces)) if a.bounces else None
    calendar = load_calendar(a.calendar) if a.calendar else None
    rows = enrich(load(a.requests), crm, bounces, calendar)
    if a.xlsx:
        build_xlsx(rows, a.xlsx, bounces)
    report = build_report(rows, bounces, calendar)
    if a.report:
        open(a.report, "w", encoding="utf-8").write(report)
    else:
        print(report)
