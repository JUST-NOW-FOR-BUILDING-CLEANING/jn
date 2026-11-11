"""Folder rules for the customer.care@justnow.life mailbox (Hostinger Email).

One place for the rules used by:
  * the one-off sort of the whole inbox on 2026-11-11 (classify() gives the same folder for
    every one of those 561 messages),
  * the daily triage task (the same rules, written out in daily-triage-prompt.md),
  * the Make scenario "Hostinger mail listener" (listener() is its formula in Python, and
    `python3 mail_rules.py --make` prints the formulas that are pasted into the scenario).

Only the sender (address and display name) and the subject are used. Message bodies are
never needed to pick a folder, so the rules cannot be steered by text inside an email.
A forged sender address cannot be detected from these fields: that is the mail server's
job (SPF, DKIM, DMARC), and one more reason to move the DMARC policy to quarantine.

    from mail_rules import classify, destination, FOLDERS
    key = classify("noreply@business-updates.facebook.com", "Your ads were approved")
    FOLDERS[key]         # -> "INBOX.06 Ads - Approvals & Notices"
    destination(key)     # -> ("INBOX.06 Ads - Approvals & Notices", True)   (folder, mark as read)

All patterns are lower-case, are applied to lower-cased text and use ASCII word boundaries,
so the same pattern gives the same answer in Python and in Make (JavaScript).
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

OWN = "customer.care@justnow.life"            # the mailbox itself; the website sends as this address
WEBSITE_FORM = "no-reply@www.justnow.life"    # older website sender
OWNER_GMAIL = "justnow.cs@gmail.com"          # also the sender of BookingKoala system mail

# ---------------------------------------------------------------- senders, by domain
META = ("facebook.com", "facebookmail.com", "meta.com", "whatsapp.com", "instagram.com")
TIKTOK = ("tiktok.com",)
GOOGLE = ("google.com", "googlemail.com")
MICROSOFT = ("microsoft.com",)
APPLE = ("apple.com",)
TOOL_DOMAINS = (
    "bookingkoala.com", "ziina.com", "setmore.com", "respond.io", "hubspot.com", "hs-send.com",
    "bigin.com", "zoho.com", "zohobookings.com", "hostinger.com", "make.com", "github.com",
)
NEWSLETTER_DOMAINS = (
    "pushwoosh.com", "rapidr.io", "n8n.io", "wetracked.io", "uae-crif.com", "theaccountant.ae",
    "betterlifeuae.com", "farahatacademy.com", "adspirer.com",
)
OFFER_DOMAINS = ("9kmanpower.com", "800lawuae.com")
# Senders seen pretending to be Meta or a law firm.
PHISHING_DOMAINS = (
    "deped.gov.ph", "jisuniversity.ac.in", "klu.ac.in", "iedcj.edu.pe", "kts.ac.th",
    "indus.edu.pk", "sellluna.com", "morrisonfoersterlaw.com",
)


def dom_re(names):
    """Pattern for 'this domain or any subdomain of it'. Never a substring test."""
    return r"^(.*\.)?(" + "|".join(n.replace(".", r"\.") for n in names) + r")$"


AD_PLATFORM_DOM = dom_re(META + TIKTOK)
GOOGLE_DOM = dom_re(GOOGLE)
KNOWN_DOM = dom_re(GOOGLE + MICROSOFT + APPLE + TOOL_DOMAINS + NEWSLETTER_DOMAINS + OFFER_DOMAINS)
PHISHING_DOM = dom_re(PHISHING_DOMAINS)
# A platform name as a whole label of some other domain: ads-tiktok.com, accounts-google.com,
# facebook.com.evil.io. Tested only after the real domains above.
LOOKALIKE_DOM = r"(^|[.\-])(facebook|facebookmail|tiktok|whatsapp|instagram|google|microsoft)([.\-]|$)"
GOOGLE_ADS_LOCAL = r"^(ads-|googleads|adwords)"
DAEMON_LOCAL = r"^(mailer-daemon|postmaster)$|^microsoftexchange"
# No-reply style local parts: not a person. (info@, support@, contact@ are people often enough.)
AUTOMATED_LOCAL = r"no-?reply|do-?not-?reply|notification|newsletter|marketing|mailer|bounce|^news$|^updates?$|^alerts?$"

# ---------------------------------------------------------------- subjects
DSN_SUBJ = (r"^(undeliverable|undelivered mail|delivery status notification|mail delivery (failed|failure|subsystem)|"
            r"returned mail|failure notice|delivery failure|message not delivered)")
# Ad platforms. Order of the tests: login codes, problems, money, known routine notices.
# A subject that matches nothing is treated as a problem, so it is never hidden as routine.
SEC_CODE = r"security code|use code|login code|verification code|confirm your email|verify your email"
LOGIN_HELP = r"verification help"      # TikTok login codes; kept with the open TikTok access issue
ALERT = (r"disabled|declined|rejected|restricted|suspended|no longer have access|not approved|couldn.t|could not|"
         r"unable to|fail|problem|issue with|flagged|violat|removed|unpublished|deactivat|expir|overdue|past due|"
         r"\bdue\b|unpaid|outstanding|action (is )?(required|needed)|at risk|paused|n.t running|not running|"
         r"not delivering|blocked|appeal|warning|limit reached|"
         r"معطل|تعطيل|مرفوض|رفض|مقيد|تقييد|فشل|مشكلة|متأخر|إجراء مطلوب")
BILLING = r"receipt|invoice|إيصال|فاتورة"
ROUTINE = (r"\bads? (was|were) approved\b|is complete|have increased|pricing|see more of|new notifications?|"
           r"running again|business portfolio|تمت الموافقة|عرض أداء|\btips?\b|newsletter|webinar|introducing|"
           r"what.s new|summary|report is ready")
GOOGLE_SEC = r"security|sign-in|signed in|password|verification|recovery|2-step|access"

# Phishing. Seen here: fake "Meta support" on school and shop domains, fake law firms about
# copyright, TestFlight invitations to fake "ads" apps. A cleaning company has no copyright
# business, so those words from an unknown sender are junk. Everything else needs two signals,
# so that a customer called Meta, a metal trader or a "Head Accountant" is not junked.
COPYRIGHT = (r"\bcopyright|\bintellectual property\b|\btrademark (infringement|violation|complaint)|"
             r"حقوق النشر|حقوق الطبع|الملكية الفكرية")
PAGE_LURE = r"\bpages? (has been|have been|is|was|will be) (suspended|unpublished|removed|disabled|restricted)\b"
BRAND = r"\b(meta|facebook|instagram)\b|فيسبوك|ميتا"
AD_TOPIC = (r"\b(ad|ads|advertising) accounts?\b|\badvertising (policy|policies|access)\b|\bcommunity (policy|standards)\b|"
            r"حساب الإعلانات|الحساب الإعلاني|سياسة الإعلانات")
ACCOUNT_LURE = (r"\baccounts? (has been|have been|is|was|will be) (suspended|disabled|restricted|locked|removed)\b|"
                r"\baccount verification\b|\bverify your (ad |business )?(account|page|identity)\b|"
                r"\bverification (is )?(required|needed)\b|\bviolat(es|ed|ion)\b|تعليق الحساب|توثيق الحساب")
AD_WORD = r"\badvertis"
AD_APP = r"ads|gpt|open ?a[il]|\bmeta\b"   # TestFlight invitations to fake ad tools

BULK = r"\bnewsletter\b|\bwebinar\b|\bunsubscribe\b|last chance to register|special offer for"
OFFER_SUBJ = (r"\bcv\b|curriculum vitae|\bresume (attached|for)\b|\bmy resume\b|reasme|job application|"
              r"application for .*\b(position|post|role|vacancy|job)\b|\bvacanc(y|ies)\b|recruitment agenc|"
              r"manpower (supply|agency)|partnership opportunity|authorized dealer|\bseo\b|web ?design|landing page|"
              r"app idea|digital marketing|سيرة ذاتية|طلب توظيف")
REPLY_OR_REF = r"^\s*(re|fwd?):|jn-[0-9]"
REPLY_TO_US = r"^\s*re:.*jn-[0-9]"      # a reply to one of our booking emails: a customer, whatever the domain
COMPLAINT = r"complain|refund|compensat|damage|legal notice|شكوى|شكوي|استرداد|تعويض|تلف"
BOOKING = r"\bbooking\b|\bbook\b|jn-[0-9]|حجز"


def has(pattern, text):
    return re.search(pattern, text, re.ASCII) is not None


def parts(addr):
    a = (addr or "").strip().lower()
    return a, a.split("@")[0], a.rsplit("@", 1)[-1]


def phishy(name, subject):
    """Ad-account, page or copyright lure in the display name or the subject (both lower-case)."""
    text = f"{name} {subject}"
    if has(COPYRIGHT, text) or has(PAGE_LURE, text) or has(AD_TOPIC, name):
        return True
    if has(BRAND, text):
        return has(AD_TOPIC, text) or has(ACCOUNT_LURE, text)
    if has(AD_TOPIC, text):
        return has(ACCOUNT_LURE, text)
    return has(ACCOUNT_LURE, text) and has(AD_WORD, text)


def platform_mail(sl):
    if has(SEC_CODE, sl):
        return "security"
    if has(LOGIN_HELP, sl) or has(ALERT, sl):
        return "ads_alert"
    if has(BILLING, sl):
        return "billing"
    if has(ROUTINE, sl):
        return "ads_notice"
    return "ads_alert"


def classify(from_addr, subject, from_name=""):
    """Return the folder key for one message."""
    a, local, dom = parts(from_addr)
    sl = (subject or "").strip().lower()
    name = (from_name or "").strip().lower()

    # 1. The company's own website.
    if a in (OWN, WEBSITE_FORM):
        if "[test" in sl:
            return "tools"
        if "new booking request" in sl or a == WEBSITE_FORM:
            return "lead"
        return "tools" if "test" in sl else "confirmation"

    # 2. Mail system: failed deliveries. Tested before the Microsoft rule (Exchange reports).
    if has(DAEMON_LOCAL, local) or has(DSN_SUBJ, sl):
        return "junk" if phishy(name, sl) else "bounce"

    # A reply to one of our booking emails is a customer, even from a company address.
    if has(REPLY_TO_US, sl):
        return "customer"

    # 3. Ad platforms, real domains only.
    if has(AD_PLATFORM_DOM, dom) or (has(GOOGLE_DOM, dom) and has(GOOGLE_ADS_LOCAL, local)):
        return platform_mail(sl)

    # 4. Google, Microsoft and Apple accounts.
    if has(GOOGLE_DOM, dom):
        if local.startswith("googleplay"):
            return "billing" if "receipt" in sl else "tools"
        if "googlehome" in local or "newsletter" in sl:
            return "newsletter"
        if dom == "accounts.google.com" or local in ("noreply", "no-reply") or has(GOOGLE_SEC, sl):
            return "security"
        return "tools"
    if has(dom_re(MICROSOFT), dom):
        return "security"
    if has(dom_re(APPLE), dom):
        if "testflight" in a or "testflight" in name:
            return "junk" if has(AD_APP, f"{name} {sl}") else "tools"
        return "billing" if has(BILLING, sl) else "security"

    # 5. Known senders, matched on the domain and never on a part of the address.
    if has(dom_re(TOOL_DOMAINS), dom):
        return "billing" if dom == "github.com" and has(BILLING, sl) else "tools"
    if has(dom_re(NEWSLETTER_DOMAINS), dom):
        return "newsletter"
    if has(dom_re(OFFER_DOMAINS), dom):
        return "recruitment"
    if a == OWNER_GMAIL:     # system mail sent with the owner's Gmail as sender, and the owner's own notes
        if "password" in sl:
            return "security"
        return "ads_alert" if "tiktok" in sl else "tools"

    # 6. Phishing: known fake senders, look-alike platform domains, ad-account and copyright lures.
    if has(PHISHING_DOM, dom) or has(LOOKALIKE_DOM, dom) or phishy(name, sl):
        return "junk"

    # 7. Bulk mail, offers, and then people.
    if has(BULK, sl):
        return "newsletter"
    if has(OFFER_SUBJ, sl) and not has(REPLY_OR_REF, sl):
        return "recruitment"
    return "customer"


def destination(key, answered=False):
    """(folder to move to, mark as read). Folder None = leave the message in the inbox.

    Mail from a person leaves the inbox only when it was answered from this mailbox, or when
    the owner moves it by hand after handling it on WhatsApp or by phone. Age alone never
    files it, so the inbox stays the list of people who are waiting.
    """
    if key == "customer" and not answered:
        return None, False
    return FOLDERS[key], key in MARK_READ


# ---------------------------------------------------------------- the Make listener
HIGH = ("COMPLAINT", "CUSTOMER_REPLY", "PERSON", "BOUNCE", "AD_ALERT")
FROM_ADDR = r"^[\s\S]*<([^<>]*)>\s*$"                         # "$1" = the address inside <...>
FROM_NAME = r"<[^<>]*>\s*$"                                   # removed to leave the display name
FROM_DOM = r"^[\s\S]*@([^@<>\s]*)>?\s*$"                      # "$1" = the domain
FROM_LOCAL = r"^([\s\S]*[<\s])?([^<>@\s]*)@[^@<>\s]*>?\s*$"   # "$2" = the part before @


def split_from(from_header):
    """The webhook's "from" field ('Display Name <address>' or a bare address), lower-cased."""
    f = (from_header or "").lower()
    addr = re.sub(FROM_ADDR, r"\1", f).strip()
    name = re.sub(FROM_NAME, "", f).strip() if "<" in f else ""
    dom = re.sub(FROM_DOM, r"\1", f).strip()
    local = re.sub(FROM_LOCAL, r"\2", f).strip()
    return addr, name, dom, local


def listener(from_header, subject):
    """What the Make listener does with one new email: (category, priority).

    The same decisions as classify(), shortened: it only has to decide whether the owner
    gets an alert. A person the rules do not know is always HIGH, whatever the subject.
    """
    addr, name, dom, local = split_from(from_header)
    s = (subject or "").lower()
    # sender type
    if addr in (OWN, WEBSITE_FORM):
        sender = "OWN"
    elif has(DAEMON_LOCAL, local) or has(DSN_SUBJ, s):
        sender = "DAEMON"
    elif has(AD_PLATFORM_DOM, dom):
        sender = "ADS"
    elif has(GOOGLE_DOM, dom) and has(GOOGLE_ADS_LOCAL, local):
        sender = "ADS"
    elif has(KNOWN_DOM, dom):
        sender = "VENDOR"
    elif addr == OWNER_GMAIL:
        sender = "OWNER"
    elif has(PHISHING_DOM, dom) or has(LOOKALIKE_DOM, dom):
        sender = "FAKE"
    else:
        sender = "OTHER"
    phish = phishy(name, s)
    # category
    if sender == "OWN":
        if "[test" in s:
            cat = "TEST"
        elif "new booking request" in s or addr == WEBSITE_FORM:
            cat = "BOOKING_REQUEST"
        else:
            cat = "TEST" if "test" in s else "CONFIRMATION_COPY"
    elif sender == "DAEMON":
        cat = "PHISHING" if phish else "BOUNCE"
    elif has(REPLY_TO_US, s):
        cat = "COMPLAINT" if has(COMPLAINT, s) else "CUSTOMER_REPLY"
    elif sender == "ADS":
        if has(SEC_CODE, s) or has(LOGIN_HELP, s):
            cat = "AD_LOGIN_CODE"
        elif has(ALERT, s):
            cat = "AD_ALERT"
        elif has(BILLING, s):
            cat = "BILLING"
        else:
            cat = "AD_NOTICE" if has(ROUTINE, s) else "AD_OTHER"
    elif sender == "VENDOR":
        cat = "AUTOMATED"
    elif sender == "OWNER":
        cat = "OWNER_MAIL"
    elif sender == "FAKE" or phish:
        cat = "PHISHING"
    elif has(COMPLAINT, s):
        cat = "COMPLAINT"
    elif has(BOOKING, s):
        cat = "CUSTOMER_REPLY"
    elif has(BULK, s) or has(OFFER_SUBJ, s):
        cat = "BULK_OR_OFFER"
    elif has(AUTOMATED_LOCAL, local):
        cat = "AUTOMATED"
    else:
        cat = "PERSON"
    return cat, "HIGH" if cat in HIGH else "LOW"


def make_formulas():
    """The Make (IML) formulas for the scenario, built from the patterns above."""
    F = "lower(ifempty(1.data.from; emptystring))"

    def t(pattern, var):          # true when the pattern occurs in var
        assert '"' not in pattern and "{" not in pattern and "/" not in pattern, pattern
        return f'length(replace({var}; "/{pattern}/g"; emptystring)) < length({var})'

    def chain(steps, last):       # [(condition, value), ...] -> nested if()
        out = last
        for cond, val in reversed(steps):
            out = f"if({cond}; {val}; {out})"
        return out

    q = lambda v: f'"{v}"'
    text = '2.name + " " + 2.s'
    lure_and_ad = chain([(t(ACCOUNT_LURE, text), chain([(t(AD_WORD, text), q("yes"))], q("no")))], q("no"))
    phish = chain([
        (t(COPYRIGHT, text), q("yes")),
        (t(PAGE_LURE, text), q("yes")),
        (t(AD_TOPIC, "2.name"), q("yes")),
        (t(BRAND, text), chain([(t(AD_TOPIC, text), q("yes")), (t(ACCOUNT_LURE, text), q("yes"))], q("no"))),
        (t(AD_TOPIC, text), chain([(t(ACCOUNT_LURE, text), q("yes"))], q("no"))),
    ], lure_and_ad)
    sender = chain([
        (f'2.addr = "{OWN}"', q("OWN")),
        (f'2.addr = "{WEBSITE_FORM}"', q("OWN")),
        (t(DAEMON_LOCAL, "2.local"), q("DAEMON")),
        (t(DSN_SUBJ, "2.s"), q("DAEMON")),
        (t(AD_PLATFORM_DOM, "2.dom"), q("ADS")),
        (t(GOOGLE_DOM, "2.dom"), chain([(t(GOOGLE_ADS_LOCAL, "2.local"), q("ADS"))], q("VENDOR"))),
        (t(KNOWN_DOM, "2.dom"), q("VENDOR")),
        (f'2.addr = "{OWNER_GMAIL}"', q("OWNER")),
        (t(PHISHING_DOM, "2.dom"), q("FAKE")),
        (t(LOOKALIKE_DOM, "2.dom"), q("FAKE")),
    ], q("OTHER"))
    own = chain([
        ('contains(2.s; "[test")', q("TEST")),
        ('contains(2.s; "new booking request")', q("BOOKING_REQUEST")),
        (f'2.addr = "{WEBSITE_FORM}"', q("BOOKING_REQUEST")),
        ('contains(2.s; "test")', q("TEST")),
    ], q("CONFIRMATION_COPY"))
    ads = chain([
        (t(SEC_CODE, "2.s"), q("AD_LOGIN_CODE")),
        (t(LOGIN_HELP, "2.s"), q("AD_LOGIN_CODE")),
        (t(ALERT, "2.s"), q("AD_ALERT")),
        (t(BILLING, "2.s"), q("BILLING")),
        (t(ROUTINE, "2.s"), q("AD_NOTICE")),
    ], q("AD_OTHER"))
    category = chain([
        ('7.sender = "OWN"', own),
        ('7.sender = "DAEMON"', chain([('7.phish = "yes"', q("PHISHING"))], q("BOUNCE"))),
        (t(REPLY_TO_US, "2.s"), chain([(t(COMPLAINT, "2.s"), q("COMPLAINT"))], q("CUSTOMER_REPLY"))),
        ('7.sender = "ADS"', ads),
        ('7.sender = "VENDOR"', q("AUTOMATED")),
        ('7.sender = "OWNER"', q("OWNER_MAIL")),
        ('7.sender = "FAKE"', q("PHISHING")),
        ('7.phish = "yes"', q("PHISHING")),
        (t(COMPLAINT, "2.s"), q("COMPLAINT")),
        (t(BOOKING, "2.s"), q("CUSTOMER_REPLY")),
        (t(BULK, "2.s"), q("BULK_OR_OFFER")),
        (t(OFFER_SUBJ, "2.s"), q("BULK_OR_OFFER")),
        (t(AUTOMATED_LOCAL, "2.local"), q("AUTOMATED")),
    ], q("PERSON"))
    return {
        "2.addr": "{{trim(replace(" + F + f'; "/{FROM_ADDR}/"; "$1"))' + "}}",
        "2.name": "{{if(contains(" + F + '; "<"); trim(replace(' + F + f'; "/{FROM_NAME}/"; emptystring)); emptystring)' + "}}",
        "2.dom": "{{trim(replace(" + F + f'; "/{FROM_DOM}/"; "$1"))' + "}}",
        "2.local": "{{trim(replace(" + F + f'; "/{FROM_LOCAL}/"; "$2"))' + "}}",
        "7.sender": "{{" + sender + "}}",
        "7.phish": "{{" + phish + "}}",
        "3.category": "{{" + category + "}}",
        "4.priority": '{{if(length(replace(3.category; "/^(' + "|".join(HIGH) + ')$/"; emptystring)) = 0; "HIGH"; "LOW")}}',
    }


if __name__ == "__main__":
    import collections
    import json
    import sys

    if sys.argv[1:] == ["--make"]:
        print(json.dumps(make_formulas(), ensure_ascii=False, indent=1))
        sys.exit()
    # Input: JSON list of message envelopes as returned by the Hostinger Mail API
    # (uid, subject, flags, from{name,address}). Prints the folder plan and writes it to folder_plan.json.
    msgs = json.load(open(sys.argv[1]))
    plan = collections.defaultdict(list)
    for m in msgs:
        key = classify(m["from"]["address"], m.get("subject"), m["from"].get("name"))
        folder, _ = destination(key, "\\Answered" in (m.get("flags") or []))
        plan[folder or "INBOX (stays: waiting for an answer)"].append(m["uid"])
    for folder in sorted(plan):
        print(f"{folder:45s} {len(plan[folder]):4d}")
    json.dump({k: sorted(v) for k, v in plan.items()}, open("folder_plan.json", "w"), indent=1)
