import re, sys, html
sys.path.insert(0, "/tmp/claude-0/-home-user-jn/e7bf3707-aa63-56e7-ba2e-0c39ba53f1fa/scratchpad")
from xlsxwrite import Sheet, write
PROMPT = open("/home/user/jn/respondio/whatsapp-agent-prompt.txt", encoding="utf-8").read()
OUT = sys.argv[1]
exec(open("/tmp/claude-0/-home-user-jn/e7bf3707-aa63-56e7-ba2e-0c39ba53f1fa/scratchpad/bk_data.py", encoding="utf-8").read())

# ---------- parse zones & prices ----------
zones_block = PROMPT[PROMPT.index("ZONES (find the zone"):PROMPT.index("PRICE TABLE (AED")]
areas, defaults = [], {}
for line in zones_block.splitlines():
    m = re.match(r"- (.+?): default zone ([A-E]) for any area not listed\. (.*)", line)
    if not m: continue
    emirate, default, rest = m.groups(); defaults[emirate] = default
    for zm in re.finditer(r"Zone ([A-E])(?: \([^)]*\))?: (.*?)(?=(?: Zone [A-E]| ?$))", rest):
        z, lst = zm.groups()
        for a in lst.rstrip(".").split(", "):
            a = a.strip().rstrip(".")
            if a: areas.append((emirate, a, z))
rows = []
for line in PROMPT[PROMPT.index("PRICE TABLE (AED"):].splitlines():
    m = re.match(r"- (.+?), zone ([A-E]): (.*)", line)
    if not m: continue
    size, z, pk = m.groups()
    size = re.sub(r" \(.*?\)", "", size).replace("Kitchen only / partial jobs / full house refresh", "Kitchen only / partial / refresh")
    rows.append((size, z, [(int(c), int(h), int(p)) for c, h, p in re.findall(r"(\d) cleaners x (\d)h = (\d+)", pk)]))

S = lambda v: (v, "str"); N = lambda v: (v, "num"); F = lambda v: (v, "formula"); B_ = lambda v: (v, "bold")
sheets = []

# Sheet 1
sh = Sheet("1 Setup steps", [5, 26, 120]); sheets.append(sh)
sh.add([("Just Now - BookingKoala setup pack", "title")])
sh.add([("Source: owner-approved price table (2 Oct 2026, amended 8-9 Oct) as loaded in the WhatsApp assistant. Prepared 23 Oct 2026. Yellow cells are for you to fill.", "note")])
sh.add([])
sh.add([("#", "hdr"), ("Step", "hdr"), ("What to do", "hdr")])
for s in STEPS: sh.add([S(s[0]), B_(s[1]), S(s[2])], height=48)

# Sheet 2
sh = Sheet("2 Packages", [24, 30, 12, 30, 7, 24, 18, 16, 11, 11, 4, 44], freeze=5, autofilter="A4:J109"); sheets.append(sh)
sh.add([("Approved packages (AED, everything included, no VAT shown)", "title")])
sh.add([("Every row is one price BookingKoala must store. 'Order' 1 = the package shown first / minimum. Do not round, do not show 'from'.", "note")])
sh.add([])
sh.add([(h, "hdr") for h in ["Service", "Home size (variable)", "Zone (location)", "Zone note", "Order", "Package label", "Cleaners (providers)", "Hours (duration)", "Price AED", "Minimum?", "", "Key (helper)"]])
pk_first = 5; r = 5
for size, z, pks in rows:
    service = "Kitchen deep cleaning" if size.startswith("Kitchen") else "Full house deep cleaning"
    sizev = "(no size question)" if size.startswith("Kitchen") else size
    for n, (c, h, p) in enumerate(pks, 1):
        key = f'IF(B{r}="(no size question)","Kitchen only / partial / refresh",B{r})&"|"&C{r}&"|"&E{r}'
        sh.add([S(service), S(sizev), S(f"Zone {z}"), S(ZONE_NOTE[z]), N(n), S(f"{c} cleaners x {h} hours"), N(c), N(h), N(p), S("Yes" if n == 1 else ""), S(""), F((key, f"{size}|Zone {z}|{n}"))])
        r += 1
pk_last = r - 1
sh.add([])
sh.add([("Notes: 'Kitchen deep cleaning' is also used for partial jobs (bathrooms only, kitchen + bathrooms, one room, balcony, inside windows, full house refresh). Villa / very large / very greasy kitchen = first package of the 1 BHK row (3 cleaners). Bedroom count decides the row whatever the home type (3-bedroom villa = 3 BHK row; 4-bedroom apartment = Villa 4 BR row).", "note")])

# Sheet 3
sh = Sheet("3 Zones & Areas", [16, 14, 42, 22, 34, 11, 70], freeze=5); sheets.append(sh)
sh.add([("Areas and their zone (load each as a service area under its Zone location)", "title")])
sh.add([("Dubai and Sharjah: only listed areas have a price. An unlisted Dubai/Sharjah area = 'price on request' (do not book online; send to WhatsApp). Ajman, UAQ, RAK, Fujairah: the emirate's default zone applies to any unlisted area.", "note")])
sh.add([])
sh.add([(h, "hdr") for h in ["Emirate", "Emirate (Arabic)", "Area (English, as the customer should see it)", "Area (Arabic)", "Also known as / sub-areas", "Zone", "Note"]])
r = 5
for emirate, a, z in areas:
    note = ""
    if a.startswith("Dubailand ("): note = "If the customer says only 'Dubailand', ask which side. Silicon Oasis side = Zone B (DLRC, Liwan, Wadi Al Safa, Queue Point, Skycourts)."
    if a.startswith("Al Suyoh"): note = "Far from base: Zone E price (owner decision 28 Sep 2026)."
    if z == "D": note = note or "4-hour minimum (no 3-hour package)."
    sh.add([S(emirate), (EMIRATE_AR[emirate], "ar"), S(a.replace(" (السيوح)", "")), (ARABIC.get(a, ""), "ar"), S(ALIAS.get(a, "")), S(f"Zone {z}"), S(note)]); r += 1
for emirate, z in defaults.items():
    if emirate in ("Dubai", "Sharjah"): continue
    sh.add([S(emirate), (EMIRATE_AR[emirate], "ar"), S("(any other area in this emirate)"), S(""), S(""), S(f"Zone {z}"), S("Emirate default: the emirate alone is enough.")]); r += 1
for a, ar in [("Al Zubair", "الزبير"), ("Al Mahatta", "المحطة"), ("Al Ghafiya", "الغافية")]:
    sh.add([S("Sharjah"), ("الشارقة", "ar"), S(a), (ar, "ar"), S(""), S("ASK"), S("Price verification required (owner decision 8 Oct 2026): no online price until the owner adds it.")]); r += 1
sh.add([S("Abu Dhabi / Al Ain"), ("أبوظبي / العين", "ar"), S("(all areas)"), S(""), S(""), S("NOT ONLINE"), S("Minimum AED 1,000, quoted by the specialist on WhatsApp +971 50 767 7282. Do not offer online booking.")]); r += 1
ar_last = r - 1

# Sheet 4
sh = Sheet("4 Hours & Slots", [42, 100]); sheets.append(sh)
sh.add([("Working hours, arrival windows and booking rules", "title")]); sh.add([])
sh.add([("Setting", "hdr"), ("Value", "hdr")])
for k, v in HOURS: sh.add([B_(k), (v, "input" if "fill in" in v else "str")])

# Sheet 5
sh = Sheet("5 Policies & texts", [34, 80, 70]); sheets.append(sh)
sh.add([("Texts to paste into BookingKoala", "title")]); sh.add([])
sh.add([("Where", "hdr"), ("Text (English)", "hdr"), ("Text (Arabic)", "hdr")])
for k, en, ar in TEXTS: sh.add([B_(k), S(en), (ar, "ar")], height=110)

# Sheet 6: price check
sh = Sheet("6 Price check", [36, 34, 40]); sheets.append(sh)
sh.add([("Price check (type an area and pick a size; the zone and prices appear)", "title")])
sh.add([("Use this to verify BookingKoala after setup: the price it shows must equal column C here. Yellow cells are inputs.", "note")])
sh.add([])
sh.add([B_("Area (type exactly as in sheet 3)"), ("Al Majaz", "input")])
sh.add([B_("Service / size (Kitchen only / partial / refresh, Studio, 1 BHK, 2 BHK, 3 BHK, Villa 4 BR, Villa 5+ BR)"), ("Kitchen only / partial / refresh", "input")])
sh.add([])
Z = "'3 Zones & Areas'"; P = "'2 Packages'"
KA = [(f"{c} cleaners x {h} hours", p) for (sz, z, pks) in rows if sz.startswith("Kitchen") and z == "A" for (c, h, p) in pks]
sh.add([B_("Zone"), F((f'IFERROR(INDEX({Z}!$F$5:$F${ar_last},MATCH($B$4,{Z}!$C$5:$C${ar_last},0)),"Area not listed - price on request")', "Zone A"))])
sh.add([B_("Lookup key"), F(('IF(LEFT($B$5,7)="Kitchen","Kitchen only / partial / refresh",$B$5)&"|"&$B$7', "Kitchen only / partial / refresh|Zone A"))])
sh.add([])
sh.add([("Package", "hdr"), ("Cleaners x hours", "hdr"), ("Price AED", "hdr")])
for n in (1, 2, 3):
    sh.add([B_(f"Package {n}" + (" (shown first / minimum)" if n == 1 else "")),
            F((f'IFERROR(INDEX({P}!$F${pk_first}:$F${pk_last},MATCH($B$8&"|{n}",{P}!$L${pk_first}:$L${pk_last},0)),"-")', KA[n-1][0])),
            F((f'IFERROR(INDEX({P}!$I${pk_first}:$I${pk_last},MATCH($B$8&"|{n}",{P}!$L${pk_first}:$L${pk_last},0)),"-")', KA[n-1][1]))])


write(OUT, sheets)
print("areas", len(areas), "package rows", len(rows), "pk rows", pk_first, pk_last, "areas rows", ar_last)
