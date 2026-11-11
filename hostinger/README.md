# Hostinger email setup report – Just Now For Building Cleaning Services

Date: 11 November 2026
Mailbox: customer.care@justnow.life (Hostinger Business Email, 20 GB, 28 MB used)
Reached through: the Hostinger Email connector, which covers this one mailbox (messages, folders, webhooks). hPanel was not reachable, so DNS, webmail filters, forwarders, auto-reply and hosting are untouched (section 6).

## 1. What is configured and verified

| Area | Status | Details |
|---|---|---|
| Folders | Done | 11 numbered folders under the inbox (section 3). |
| One-off sort | Done, verified | All 561 inbox messages filed. 567 messages in the mailbox before and after (561 inbox + 6 already in Junk), none deleted. Ten recent customer emails were left in the inbox on purpose. |
| Read state | Done | 135 unread ad notices, newsletters and phishing mails marked as read. No other flag was changed. |
| Live listener | Done, tested | Hostinger webhook "Make - inbox listener (CRM + alerts)" fires on every new email and calls the Make scenario "Hostinger mail listener -> email log + owner alert (customer.care inbox)". After the review its rules were rewritten and checked with 86 test events: all 86 got the expected category. Two real emails have been logged since. |
| Owner alerts | Done, tested | A complaint, a customer reply, any email from a person the rules do not know, a bounced email or an ad platform problem puts an event on the Google Calendar "Just Now – Alerts" with a pop-up and an email reminder. Test alerts were created and removed. |
| Email log | Done | Make data store "JN Email log (customer.care inbox)": one row per new email with time, sender, subject, category, priority, booking number and the first lines. Test rows removed, it starts empty. |
| Daily filing and digest | Done, test run verified | Scheduled task "Just Now inbox daily triage", every day 07:36 Asia/Dubai. The test run filed 77 of the remaining 87 messages and left the ten customer emails; every folder count matched the expected plan. It ends with a short Arabic digest of what needs the owner. |
| Lead register | Done | The 146 website booking-request emails parsed into a spreadsheet: Leads, Customers, Lost leads, Not in HubSpot, Bounced emails. Handed to the owner directly. It holds customer data, so it is not in this repository. |
| Report | Done | `REPORT-booking-requests-2026-11-11.md`: counts and outcomes, no customer data. |
| Mail authentication | Checked | SPF, DKIM and DMARC all pass on a real confirmation email. The DMARC policy itself is only `p=none` (section 6). |

## 2. How mail is handled now

1. A new email arrives. Within seconds Hostinger calls the webhook and Make logs the email. If it is a complaint, a customer reply, mail from an unknown person, a bounce or an ad platform problem, an alert appears on the Alerts calendar.
2. Every morning at 07:36 the triage task files what is in the inbox into the folders below and writes the digest.
3. Customer and personal mail stays in the inbox until it is answered from this mailbox. If you handle it on WhatsApp or by phone, drag it to folder 02 yourself. Until the new instruction is stored (section 7), the daily task still moves unanswered mail to folder 02 after 14 days. Three such emails are already there: replies about JN-147281, JN-147290 (a complaint) and JN-147328.
4. Nothing is ever sent, answered or deleted automatically.

## 3. Folders and rules

Counts on 11 November 2026 after the sort.

| Folder | Messages | What goes there |
|---|---:|---|
| Inbox | 10 | Customer and personal mail waiting for an answer |
| 01 Leads - Booking Requests | 146 | Website "New booking request JN-…" notifications |
| 02 Customers - Replies & Complaints | 4 | Customer mail once answered or handled. One of the four was answered; three are older than 14 days and unanswered |
| 03 Bookings - Confirmations | 5 | Copies of confirmations the website sent to the mailbox itself |
| 04 Bounces - Failed Delivery | 13 | "Undelivered Mail Returned to Sender" |
| 05 Ads - Alerts & Issues | 23 | Meta, TikTok and WhatsApp problems: declined payment, disabled account, rejected template, TikTok login codes |
| 06 Ads - Approvals & Notices | 161 | "Your ads were approved" and other routine platform notices (marked read) |
| 07 Billing - Receipts & Invoices | 53 | Meta receipts, TikTok invoices, GitHub and Google Play receipts |
| 08 Tools & Vendors | 25 | BookingKoala, Ziina, Setmore, respond.io, HubSpot, Bigin, Zoho, Google Play, tests |
| 09 Accounts & Security | 55 | Google and Microsoft security alerts, login codes, password changes |
| 10 Recruitment & Offers | 7 | CVs, manpower agencies, unsolicited business offers |
| 11 Newsletters & Promotions | 45 | Pushwoosh, Rapidr, n8n, wetracked, CRIF and similar (marked read) |
| Junk | 21 | The 15 phishing emails moved there by the sort (fake "Meta" notices, fake law-firm copyright notices, TestFlight "ads app" invitations) and six the mail server had put there, left as they were |

The rules use only the sender and the subject, never the text of the email. They are in `mail_rules.py` and, written out for the daily task, in `daily-triage-prompt.md`. The Make listener's formulas are generated from the same file. Senders are matched on their domain. A forged sender address cannot be seen from these fields; that is what DMARC is for (section 6). The counts are those right after the sort. New mail waits in the inbox until the next morning run.

Real Meta mail only comes from facebook.com, facebookmail.com, meta.com, whatsapp.com or instagram.com. Anything else that talks about ad accounts, page suspension, copyright or verification is treated as phishing.

## 4. What the mailbox showed

1. **Customer emails are not being answered.** 14 customer emails arrived between 23 October and 8 November and one was answered from this mailbox. Besides the formal complaint, a second complaint (a reply about JN-147290, 24 October) has no answer and now sits in folder 02. They include a formal complaint received on 7 November about a job on 6 November (3-bedroom townhouse, four cleaners for four hours). It asks for a full refund, compensation for damage, an investigation and a management answer within 48 hours. That deadline passed on 9 November. The message was read, flagged and forwarded on 8 November, but no reply to the customer was sent from this mailbox. Two other customers wrote that nobody contacted them to confirm, and one of them cancelled. Others asked to change the date, and one asked for a new booking. Whether these were handled on WhatsApp is not visible here.
2. **Why customers write here.** The "booking request received" email says the booking is final only after a WhatsApp confirmation, and the confirmation email says "or simply reply to this email". The replies land in a mailbox where 83 of the 146 request notifications are still unread: 83 of the 104 that arrived since 29 October. Every earlier one was read.
3. **The emails are the requests the website could not confirm by itself, not all bookings.** Since 18 October the website sends staff two kinds of email. Requests with no free team at the requested time, no listed price (sofa, mattress and carpet only, or a home or area not in the price list) or kitchen add-ons arrive here as "New booking request". Bookings it confirms by itself are announced as "New booking" to the company Gmail. Of 315 booking numbers, owner tests included, 139 are here and 176 are in the Gmail. Compared with the calendar, both groups are done at the same rate: 62% here, 61% there. 35% of the requests here are no longer in the calendar against 26% there, a gap that is within chance. 17 bookings the website confirmed by itself are still UNCONFIRMED in the calendar, one for a date that has passed.
4. **Where requests are lost.** Sofa, mattress and carpet requests: 16 asked, 3 done, 11 gone. Same-day requests do best (79% done). In this sample 41% of afternoon and 28% of morning requests are gone, but that gap is not reliable. 31 customers asked and have no booking in the calendar at all; 15 of them were shown a price, AED 7,605 in total. Eight requests were marked by the website as possible duplicates.
5. **Capacity.** Since 24 October at least 92 of 265 website bookings (35%) asked for a time when the website schedule had no free team. Among the bookings the check applies to it is 40%. More than half of those asked for the 12–2 slot.
6. **13 emails to customers bounced, all because of the customer's address:** two mistyped domains (gmail.cok, gmail.gom), eight addresses that do not exist or were refused (one is an obvious placeholder) and three full inboxes. None was rejected because of this domain. The website form accepts any text as an email address.
7. **Meta billing.** "Payment declined, ads paused" notices for the ad account named "jn" (ID ending 8677) ten times from 22 September to 10 November, for "justnow22" (ending 0660) on 22 October, and a declined payment for "JN" (ending 6647) on 3 November. The emails give no amount and no reason.
8. **WhatsApp.** Three message templates rejected on 3 and 9 November. The only reason given is the Commerce Policy.
9. **TikTok.** The business login is tied to a phone number the company no longer has, so balance cannot be added. The support request of 27 October has no answer in this mailbox.
10. **BookingKoala.** Their reply of 11 November: they will not load the configuration for us and offer a Zoom walkthrough. The trial-extension request is still with their developers. The question about which plan gives Google Calendar sync and Arabic texts was not answered.
11. **Google Play.** The developer account must declare trader or non-trader status by 1 February 2027, or the apps and the developer profile are removed.
12. **Zoho Bigin** reported 90% of its 500-record limit on 22 October.
13. **Phishing.** 15 phishing emails were sitting in the inbox and are now in Junk, next to the six Hostinger had already caught. Typical signs: sender on a school or unrelated domain, a 12 or 24 hour threat, a shortened link.
14. **Security noise.** 36 Google "Security alert" emails for the company Gmail between 15 September and 9 November, and Microsoft password changes on 21 September. Worth one look at the list of connected apps and devices.
15. **HubSpot.** 96 of the 129 customers in these emails are already in HubSpot. The other 33 were not added on purpose: the active Make scenario "Hubspot (On Contact Created) -> Facebook Conversions API for CRM" sends every new contact to Meta as a conversion, so a bulk import would distort ad optimisation. They are listed in the lead register.

## 5. What only you can do

1. Answer the formal complaint of 7 November. It is the flagged message in the inbox whose subject starts with "FORMAL COMPLAINT". Then the second complaint, the reply about JN-147290 in folder 02.
2. Go through the other nine customer emails in the inbox. Most dates have passed, but two customers were never contacted and one new enquiry was never answered.
3. Settle the Meta billing on the three ad accounts, then check the three rejected WhatsApp templates in WhatsApp Manager.
4. Call or WhatsApp the 31 lost leads in the lead register, starting with the sofa, mattress and carpet requests.
5. Decide on the BookingKoala Zoom walkthrough and chase the trial extension.
6. Declare the trader status in Google Play Console before 1 February 2027.
7. Check with whoever maintains the website: email validation on the booking form, the team schedule that produces "No free team", and sending the "New booking request" emails to an address that is read. They wait for a person and 83 are unread.
8. Paste the new daily instruction (section 7).

## 6. Not configured, because it needs hPanel or webmail

- **DMARC.** The record is `v=DMARC1; p=none` with no report address, so a forged email in the company's name is not blocked. First step: add `rua=mailto:` an address you read. After two weeks of clean reports move to `p=quarantine`. Check first that every tool sending as @justnow.life is signed.
- **Server-side filters.** Hostinger webmail can file mail the moment it arrives. Until then filing happens once a day through the scheduled task.
- **Forwarding and auto-reply.** A short auto-reply ("for a faster answer write to us on WhatsApp +971 50 767 7282") would cover the hours before anyone reads the inbox.
- **Other mailboxes, aliases, hosting, domain.** Not visible through the email connector.
- **The website.** Not touched.

## 7. How to change or stop things

| To do this | Do this |
|---|---|
| Stop the alerts | Make: switch off scenario 6991667. Or pause the Hostinger webhook "Make - inbox listener (CRM + alerts)". |
| Change what raises an alert | Change the patterns in `mail_rules.py`, run `python3 mail_rules.py --make` and paste the formulas into Make scenario 6991667. A copy of the scenario is in `make-listener-blueprint.json`. |
| Stop the daily filing | Claude app: pause or delete the scheduled task "Just Now inbox daily triage". |
| Change the folder rules | Write the change in the Claude conversation "Just Now inbox daily triage". The task's instruction can only be changed from there. Then update `mail_rules.py` and `daily-triage-prompt.md` to match. **Open now:** the improved instruction in `daily-triage-prompt.md` is not stored yet. Open that conversation and write: "replace this task's instruction with the following", then paste the text. Until then the task runs the first version, which files the same mail except for the points in section 2 item 3. |
| Rebuild the lead register and report | Export the booking-request emails and run `booking_requests.py` (usage at the top of the file). |
| Undo the sort | Move the messages back from the folders. Nothing was deleted. |

Identifiers: Hostinger webhook `01a1c9d9-9869-732b-aa26-5c562ae89acb`; Make team 1579313, hook 3051146, scenario 6991667, data store 198605, data structure 576435; scheduled task `trig_0131Va5py27rzYHpbeJgWfFQ` in session `session_01ESETHWs9wAdJkXgdTUmy5z`. The webhook URL and its signing secret are not stored in this repository.

Running cost: the listener uses 6 Make operations per email, 7 when it alerts. At the current volume that is about 1,800 operations a month out of 20,000. The daily task is one short Claude run per day.

## 8. Files in this folder

| File | What it is |
|---|---|
| `README.md` | This report |
| `REPORT-booking-requests-2026-11-11.md` | Booking-request numbers and outcomes, generated by `booking_requests.py` |
| `mail_rules.py` | The folder rules as code, and the source of the Make formulas. Gives every one of the 561 sorted messages the folder it was filed in |
| `daily-triage-prompt.md` | The instruction the scheduled task sends every morning |
| `make-listener-blueprint.json` | Export of the Make listener scenario |
| `booking_requests.py` | Parser for the website's booking-request emails; builds the lead register and the report |
