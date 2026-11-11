"""Folder rules for the customer.care@justnow.life mailbox (Hostinger Email).

One place for the rules used by:
  * the one-off sort of the whole inbox on 2026-11-11,
  * the daily triage task (same table, written out in its prompt),
  * the Make scenario "Hostinger mail listener" (simplified: category + priority only).

Only the sender address and the subject are used. Message bodies are never
needed to pick a folder, so the rules cannot be steered by text inside an email.

    from mail_rules import classify, FOLDERS
    key = classify("noreply@business-updates.facebook.com", "Your ads were approved")
    FOLDERS[key]  # -> "INBOX.06 Ads - Approvals & Notices"
"""
import re

FOLDERS = {
    "lead": "INBOX.01 Leads - Booking Requests",
    "customer": "INBOX.02 Customers - Replies & Complaints",
    "confirmation": "INBOX.03 Bookings - Confirmations",
    "bounce": "INBOX.04 Bounces - Failed Delivery",
    "ads_alert": "INBOX.05 Ads - Alerts & Issues",
    "ads_notice": "INBOX.06 Ads - Approvals & Notices",
    "billing": "INBOX.07 Billing - Receipts & Invoices",
    "tools": "INBOX.08 Tools & Vendors",
    "security": "INBOX.09 Accounts & Security",
    "recruitment": "INBOX.10 Recruitment & Offers",
    "newsletter": "INBOX.11 Newsletters & Promotions",
    "junk": "INBOX.Junk",
}

# Folders whose mail is pure noise: marked as read when filed.
MARK_READ = {"ads_notice", "newsletter", "junk"}

# Human mail that needs an answer stays in INBOX until it is answered or 14 days old.
KEEP_IN_INBOX = {"customer"}

OWN = "customer.care@justnow.life"
OWNER_GMAIL = "justnow.cs@gmail.com"

# Senders seen pretending to be Meta / law firms. Real Meta mail only comes from
# facebook.com, facebookmail.com, business.facebook.com or meta.com.
PHISHING_DOMAINS = (
    "deped.gov.ph", "jisuniversity.ac.in", "klu.ac.in", "iedcj.edu.pe", "kts.ac.th",
    "indus.edu.pk", "sellluna.com", "morrisonfoersterlaw.com",
)
# Subjects used by the fake "Meta support" and fake "law firm" senders. A cleaning
# company has no copyright business, so these words from a non-platform sender are junk.
PHISH_SUBJ = re.compile(
    r"copyright|intellectual property|ad account|advertising account|advertising policy|"
    r"community (policy|standards)|حقوق النشر|الملكية الفكرية|حساب الإعلانات|مراجعة justnow", re.I)
PHISH_NAME = re.compile(r"meta|facebook|الإعلانات", re.I)
META_REAL = re.compile(r"@([a-z0-9-]+\.)*(facebook\.com|facebookmail\.com|meta\.com)$")

NEWSLETTER = re.compile(r"pushwoosh|rapidr|n8n\.io|wetracked|crif|theaccountant|betterlife|farahat|googlehome|adspirer")
TOOLS = re.compile(r"bookingkoala|ziina|setmore|respond\.io|hubspot|hs-send|bigin|zoho|hostinger")
RECRUIT_FROM = re.compile(r"manpower|800lawuae")
RECRUIT_SUBJ = re.compile(
    r"resume|reasme|\bcv\b|application for|recruitment|hiring|partnership opportunity|authorized dealer|"
    r"google ads|\bseo\b|landing page|web ?design|app idea|digital marketing", re.I)


def classify(from_addr, subject, from_name=""):
    """Return the folder key for one message."""
    a = (from_addr or "").strip().lower()
    s = (subject or "").strip()
    sl = s.lower()

    # 1. Phishing: known fake senders, TestFlight "ads tool" invites, or mail that
    #    talks about Meta / ad accounts / copyright but does not come from Meta.
    if a.endswith(PHISHING_DOMAINS) or "testflight" in a:
        return "junk"
    is_meta = bool(META_REAL.search(a))
    is_tiktok = a.endswith("tiktok.com")
    is_platform = is_meta or is_tiktok or a.endswith(("google.com", "microsoft.com", "apple.com"))
    if not is_platform and a not in (OWN, OWNER_GMAIL):
        if PHISH_NAME.search(from_name or "") or PHISH_SUBJ.search(s):
            return "junk"

    # 2. Mail system and our own website.
    if "mailer-daemon" in a or "postmaster@" in a:
        return "bounce"
    if "new booking request" in sl:
        return "tools" if "[test" in sl else "lead"
    if a == "no-reply@www.justnow.life":
        return "lead"
    if a == OWN:
        return "tools" if "test" in sl else "confirmation"

    # 3. Ad platforms.
    if is_meta or is_tiktok:
        if re.search(r"receipt|إيصال|invoice", sl) or "invoice" in a:
            return "billing"
        if re.search(r"security code|use code|confirm your email|verify your email", sl):
            return "security"
        if re.search(r"disabled|declined|rejected|restricted|suspended|no longer have access|verification help", sl):
            return "ads_alert"   # "verification help" = TikTok login codes, kept with the open TikTok access issue
        return "ads_notice"

    # 4. Accounts, receipts, tools, newsletters.
    if a in ("no-reply@accounts.google.com", "noreply@google.com") or "microsoft" in a:
        return "security"
    if a == "noreply@github.com" or (a == "googleplay-noreply@google.com" and "receipt" in sl):
        return "billing"
    if a == "googleplay-noreply@google.com":
        return "tools"
    if NEWSLETTER.search(a):
        return "newsletter"
    if TOOLS.search(a):
        return "tools"
    if a == OWNER_GMAIL:  # system mail sent with the owner's Gmail as sender, and owner's own notes
        if "password" in sl:
            return "security"
        if "tiktok" in sl:
            return "ads_alert"
        return "tools"

    # 5. People.
    if RECRUIT_FROM.search(a) or RECRUIT_SUBJ.search(s):
        return "recruitment"
    return "customer"


if __name__ == "__main__":
    import json, sys, collections
    # Input: JSON list of message envelopes as returned by the Hostinger Mail API
    # (uid, subject, from{name,address}). Prints the folder plan.
    msgs = json.load(open(sys.argv[1]))
    plan = collections.defaultdict(list)
    for m in msgs:
        k = classify(m["from"]["address"], m.get("subject"), m["from"].get("name"))
        plan[k].append(m["uid"])
    for k in FOLDERS:
        print(f"{FOLDERS[k]:45s} {len(plan[k]):4d}")
    json.dump({FOLDERS[k]: sorted(v) for k, v in plan.items()}, open("folder_plan.json", "w"), indent=1)
