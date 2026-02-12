# PLIST FORENSIC SEARCH REPORT
## Exhaustive Database Search for Apple Property List (PLIST) Content & [EFTA00524160](https://www.justice.gov/epstein/files/DataSet%209/EFTA00524160.pdf)

**Generated:** 2026-02-07
**Databases Searched:**
- the primary document text database
- the Dataset 10 document text database
- the OCR text extraction database
- the image catalog database

---

## 1. [EFTA00524160](https://www.justice.gov/epstein/files/DataSet%209/EFTA00524160.pdf) -- SEARCH RESULTS

### Finding: [EFTA00524160](https://www.justice.gov/epstein/files/DataSet%209/EFTA00524160.pdf) DOES NOT EXIST in any database.

The specific EFTA number `EFTA00524160` was NOT found in any of the four databases. However, a closely related number was found:

**[EFTA01524160](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01524160.pdf)** -- This document DOES exist:
- **File:** DOJ dataset file `dataset10/VOL00010/IMAGES/0135/EFTA01524160.pdf`
- **Content:** JPMorgan Chase Private Bank statement for **Ghislaine Maxwell**
  - Statement period: April 1, 2003 -- April 30, 2003
  - Account: Premier Checking, c/o New York Strategy Group, Attn: Eric Gany
  - Opening balance: $3,499,315.96
  - Total credits: $3,991.98
  - Total debits: $23,745.79
  - Ending balance: $3,479,564.15
  - Private Bank Team: Maria Hornak
  - Bates numbers: JPM-SDNY-00051945, SDNY_GM_00321143

- **Redaction analysis (v2 & ds10):** 2 redactions detected, both classified as `proper_redaction` with low confidence (0.5051, 0.5609). Hidden text was empty (nothing recovered beneath redactions).
- **Document summary:** 2 total pages, 0 with recovered text, 2 redacted pages

**Assessment:** [EFTA01524160](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01524160.pdf) is a financial document (bank statement), NOT a PLIST-encoded document. The caller may have had the wrong EFTA number, or the number may have been confused. This is a JPMorgan banking record, not Apple device data.

---

## 2. PLIST CONTENT -- COMPREHENSIVE FINDINGS

### 2.1 Scope and Scale

| Database | Metric | Count |
|----------|--------|-------|
| OCR (OCR text extraction database) | Distinct EFTA documents containing "plist" | **268** |
| OCR | Documents with `conversation-id` + `date-received` metadata | **358** |
| OCR | Documents with `gmail-label-ids` | **296** |
| OCR | Documents with `remote-id` | **459** |
| OCR | Documents with `original-mailbox` + IMAP references | **38** |
| Redaction analysis (v2) | Distinct EFTA with plist in hidden (redacted) text | **12** |
| Redaction analysis (ds10) | Distinct EFTA with plist (duplicates v2) | **10** |

**Total unique documents containing Apple PLIST metadata (OCR database only): approximately 460+**

> **Revisit note (2026-02-12):** The full text corpus (1,380,937 documents across all 12 datasets) reveals a scale approximately 200x larger than the OCR database captured: 93,634 documents with `gmail-label-ids`, 18,160 with `original-mailbox` references, and 84,401 with `date-received` + `plist` co-occurring. DS11 alone contains approximately 75,630 PLIST-containing documents. The OCR database captured less than 0.5% of the actual PLIST corpus. The 460+ figure below reflects only the OCR database subset.

### 2.2 What This Data Actually Is

**THIS IS NOT DEVICE BACKUP DATA.** The PLIST content found across these documents represents **Apple Mail (Mail.app) email metadata** that was embedded within printed/exported emails. Specifically:

The PLIST fragments are Apple Mail's internal message metadata, automatically appended when emails were exported from Mail.app or Apple's email system. The standard structure found is:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>conversation-id</key>
    <integer>[ID]</integer>
    <key>date-last-viewed</key>
    <integer>0</integer>
    <key>date-received</key>
    <integer>[UNIX_TIMESTAMP]</integer>
    <key>flags</key>
    <integer>[FLAG_VALUE]</integer>
    <key>gmail-label-ids</key>
    <array>
        <integer>[LABEL_ID]</integer>
    </array>
    <key>original-mailbox</key>
    <string>imap://[EMAIL_ACCOUNT]/[FOLDER]</string>
    <key>remote-id</key>
    <string>[MESSAGE_ID]</string>
</dict>
</plist>
```

### 2.3 Email Accounts Identified in PLIST Metadata

| Email Account | Description | Document Count |
|---------------|-------------|----------------|
| `jeevacation@gmail.com` | Jeffrey Epstein's primary Gmail | ~683 in OCR DB; **272,735 in DS9 + 170,876 in DS11** (full corpus) |
| `sarahk525@mail.mac.com` | Sarah Kellen's Apple iCloud/Mac email | 11 in OCR DB; **1,465 in DS9/DS11** (full corpus) |
| `sarahk525@me.com` | Sarah Kellen's transitional Apple email | **39 in DS9** (full corpus; not found in OCR DB) |

The `sarahk525@mail.mac.com` account is forensically significant -- it reveals that **Sarah Kellen's Mac computer running Apple Mail** was used to access and export some of these emails. The IMAP mailbox references show folder paths like `imap://sarahk525@mail.mac.com/Sent%20Messages`.

> **Revisit note (2026-02-12):** DS9 also reveals the `sarahk525@me.com` transitional Apple domain, with 39 documents including flight coordination emails with Nadia Marcinkova ([EFTA00415730](https://www.justice.gov/epstein/files/DataSet%209/EFTA00415730.pdf): "330 wheels up WED the 11th from lsj to ny") and direct emails to Epstein ([EFTA00422779](https://www.justice.gov/epstein/files/DataSet%209/EFTA00422779.pdf)). The total sarahk525 count expands from 11 to 1,465 documents across DS9/DS11.

### 2.4 Date Range of PLIST-Embedded Email Metadata

Based on Unix timestamps extracted from `date-received` fields:

- **Earliest:** September 1, 2009 (timestamp 1251822309)
- **Latest:** October 5, 2018 (timestamp 1538761712)

This spans approximately **9 years of email activity** from 2009 to 2018.

### 2.5 Key Flag Values Observed

| Flag Value | Meaning | Frequency |
|------------|---------|-----------|
| 8590195713 | Read message | Most common |
| 8623750145 | Read + flagged/labeled message | Common |
| 8590195717 | Read with additional flags | Occasional |
| 8590195969 | Read with special flags | Rare |

---

## 3. PLIST DATA IN REDACTED (HIDDEN) TEXT

These 12 documents had PLIST content recovered from BENEATH redactions -- meaning the PLIST metadata was actively hidden by redaction overlays:

### Documents with PLIST Recovered from Redactions (primary document text database)

| EFTA Number | Page | Recovered Text | Redaction Type | Confidence |
|-------------|------|----------------|----------------|------------|
| [EFTA01758519](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01758519.pdf) | 0 | `PLIST 1 0//EN"` | bad_overlay | 0.7785 |
| [EFTA01765156](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01765156.pdf) | 0 | `D PLIST 1 0//EN"` | bad_overlay | 0.8014 |
| [EFTA01766832](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01766832.pdf) | 0 | `li t PUBLIC " //A l //DTD PLIST 1 0//EN" "htt // l` | bad_overlay | 0.99 |
| [EFTA01774075](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01774075.pdf) | 0 | `<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST` | bad_overlay | 0.9446 |
| [EFTA01774370](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01774370.pdf) | 0 | `UBLIC " //A l //DTD PLIST 1 0//E` | bad_overlay | 0.8809 |
| [EFTA01781767](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01781767.pdf) | 0 | `performance. Sent from my i Phone <?xml version "1 0" encoding "UTF 8"?> <!DOCTYPE plist PUBLIC " //Apple//DTD PLIST 1 0//EN"` | bad_overlay | 0.99 |
| [EFTA01792918](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01792918.pdf) | 3 | `PUBLIC "-//Apple//DTD PLIST 1.0//EN` | bad_overlay | 0.8961 |
| [EFTA01793116](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01793116.pdf) | 0 | `" //A l //DTD PLIST` | bad_overlay | 0.8208 |
| [EFTA01802972](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01802972.pdf) | 0 | `<plist version "1 0">` | bad_overlay | 0.8825 |
| [EFTA02114558](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02114558.pdf) | 1 | `<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.co` | bad_overlay | 0.99 |
| [EFTA02522767](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02522767.pdf) | 0 | `C " //A l //DTD PLIST 1 0//EN` | bad_overlay | 0.8592 |
| [EFTA02696356](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02696356.pdf) | 0 | `//Apple//DTD PLIST 1 0//` | bad_overlay | 0.8504 |

**Assessment:** These are all classified as `bad_overlay` redactions with high confidence (0.77-0.99). The redaction overlays were improperly applied and failed to fully conceal the underlying PLIST metadata. This is consistent with someone using PDF redaction tools that did not properly flatten the document -- the PLIST XML text that was part of the email export was not fully obscured.

All 12 of these come from dataset10 (EFTA01*) and dataset11 (EFTA02*).

---

## 4. NOTABLE EMAILS WITH PLIST METADATA (by person referenced)

### 4.1 High-Profile Individuals in PLIST-Containing Emails

| EFTA Number | Person Referenced | Subject/Content | Date |
|-------------|-------------------|-----------------|------|
| [EFTA02570971](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570971.pdf) | **Princess Mette** (Norway) | Princess Mette not sure about 1pm Monday meeting | June 22, 2013 |
| [EFTA02518841](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518841.pdf) | **Woody Allen** | "Gini says YES, it is fine for you to come for a visit to Newport and see Woody" | July 25, 2014 |
| [EFTA02513976](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02513976.pdf) | **Woody Allen** | "Would you like me to set up a dinner with Woody through his assistant, Gini?" | January 19, 2015 |
| [EFTA02362038](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02362038.pdf) | **Mort Zuckerman** | "Mort Zuckerman called for you...he is on his way to lunch" (212-326-4010) | May 30, 2013 |
| [EFTA02518909](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518909.pdf) | **Reid Hoffman** | Austin Hill re: "incredible network of cryptographers, authentication & e-cash tech" | March 19, 2014 |
| [EFTA02589089](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589089.pdf) | **George Church** | Reminder call list: George Church, Martin Nowak | September 10, 2014 |
| [EFTA02513966](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02513966.pdf) | **Nicole Junkermann** | "Can u speak?" sent from iPhone | March 8, 2018 |
| [EFTA02571050](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02571050.pdf) | **Ben Goertzel** | SingularityNET lawyer discussion | November 5, 2017 |
| [EFTA02532947](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02532947.pdf) | **Lyndon Lea** | Private jet: "deposit down for the new Global 8000 of $1mm... total cost $55mm" | November 10, 2010 |
| [EFTA02570943](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570943.pdf) | **Peggy Siegal** | "Any news on Gary Siegal?" forwarded chain | June 5, 2013 |
| [EFTA02672124](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02672124.pdf) | **Andrew Farkes** | "intro to Michael Ovitz," "Mort completely evaporated," confirmed 12/4 at 3pm | November 16, 2014 |
| [EFTA02570981](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570981.pdf) | **Jean Luc Brunel** | Apartment maintenance, leaks, air conditioning | June 5, 2013 |
| [EFTA02588573](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02588573.pdf) | **Paula Heil Fisher** | "perfectly overqualified to organize your dinners and meetings in NYC" | August 10, 2014 |
| [EFTA02518921](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518921.pdf) | **Larry Visoski** (Epstein's pilot) | "GIV is enroute to Teterboro now, out of holding" | February 3, 2014 |
| [EFTA02518864](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518864.pdf) | **Michael Buchholtz** | Regarding "Warren" -- talking to Linda every day about wheelchair/care | February 19, 2014 |
| [EFTA02664944](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664944.pdf) | Unnamed | "similar mannerisms between Trump and McGyver" | January 12, 2017 |
| [EFTA02518833](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518833.pdf) | Unnamed (Polish sender) | "Just found my recored" -- "Wystane z iPada" (sent from iPad in Polish) | May 1, 2014 |
| [EFTA02672121](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02672121.pdf) | **"Nina"** | "contacted the lawyer and he is working on my permit... the day he's allowed visits" -- "Sent from Nina's iPhone" | November 17, 2013 |
| [EFTA02388553](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02388553.pdf) | - | Alert: "brad depo" (Brad deposition) | May 15, 2013 |
| [EFTA02518859](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518859.pdf) | **Richard Josin** | "Narrows" -- sales tax/exemption certificate discussion | February 4, 2014 |

### 4.2 Lesley Groff (Epstein's Executive Assistant) -- Heaviest PLIST Presence

Lesley Groff appears in **40+ documents** with PLIST metadata in the OCR database, making her the most frequently appearing person in the Apple Mail data. Her emails consistently show the plist metadata pattern, indicating she was a primary user of Apple Mail for Epstein-related correspondence. DS9 contains additional Groff email chains showing her `lesley.jee@gmail.com` account (the "JEE" = Jeffrey E. Epstein naming convention mirrors `jeevacation@gmail.com`), including [EFTA00432172](https://www.justice.gov/epstein/files/DataSet%209/EFTA00432172.pdf) and [EFTA00436223](https://www.justice.gov/epstein/files/DataSet%209/EFTA00436223.pdf) (furniture shopping at 301 E 66th, March 2011).

### 4.3 Ann Rodriquez (Epstein's Housekeeper, USVI)

Ann Rodriquez appears in 6+ documents with PLIST, including:
- [EFTA02388589](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02388589.pdf): "I'm so sorry about your arrival back home (it won't happen again)"
- [EFTA02518872](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518872.pdf): "Hey Bossman, What time should I prepare your Lunch?"
- [EFTA02554183](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02554183.pdf): Re: WAPA (Clinton Hedrington power company issue on St. Thomas)

---

## 5. CELLEBRITE AND DEVICE FORENSIC REFERENCES

### 5.1 Cellebrite References (17 documents in DS8; 21+ in DS9)

> **Revisit note (2026-02-12):** DS9 alone contains 21+ Cellebrite-referencing documents, expanding the total beyond the 17 identified in DS8. New DS9 documents include: [EFTA00164855](https://www.justice.gov/epstein/files/DataSet%209/EFTA00164855.pdf) (CART download of 80GB Cellebrite report from a contraband phone, April 2025); [EFTA00173373](https://www.justice.gov/epstein/files/DataSet%209/EFTA00173373.pdf) (FBI CACHTU inspection revealing Axiom, Cellebrite, and GrayKey purchased via UCO funds); and [EFTA00164740](https://www.justice.gov/epstein/files/DataSet%209/EFTA00164740.pdf) (March 2025 evidence review referencing CART/Cellebrite procedures).

The following documents reference Cellebrite forensic extraction software:

| EFTA Number | Content |
|-------------|---------|
| [EFTA00020322](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020322.pdf) | **KEY:** "All electronic images should be viewable as thumbnails, except those seized from Apple devices, which must be viewed using Cellebrite. The Cellebrite software will be provided on the drive for your review of images and videos seized from Apple devices." |
| [EFTA00029601](https://www.justice.gov/epstein/files/DataSet%208/EFTA00029601.pdf) | FBI forensic examiner's CV: "Cellebrite/Secureview Cell Phone Forensics, Salt Lake City, UT (4 days)" training in Feb 2009, plus XRY Mobile Phone Examination, EnCase, Forward Discovery Macintosh Forensics |
| [EFTA00025553](https://www.justice.gov/epstein/files/DataSet%208/EFTA00025553.pdf), [EFTA00030999](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030999.pdf) | **"GM photo on Bannon phone"** -- "I've been looking through Steve Bannon's iPhone 7 on Cellebrite. As I was going through the images from that phone, I found an image of Trump and Ghislaine Maxwell on Bannon's phone" |
| [EFTA00015786](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015786.pdf), [EFTA00030035](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030035.pdf), [EFTA00015804](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015804.pdf) | Discovery letter: ~2,100 electronic images/videos seized from Epstein's electronic devices, ~3,400 from discs, 7 hard copy nude images from FBI Florida investigation |
| [EFTA00015738](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015738.pdf), [EFTA00015753](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015753.pdf), [EFTA00015770](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015770.pdf) | Prosecution correspondence about evidence viewing procedures |
| [EFTA00026890](https://www.justice.gov/epstein/files/DataSet%208/EFTA00026890.pdf) | Defense question: "Can you please explain why 2,100 + 7 'highly confidential' images have not been shared with us yet?" |
| [EFTA00031332](https://www.justice.gov/epstein/files/DataSet%208/EFTA00031332.pdf), [EFTA00031589](https://www.justice.gov/epstein/files/DataSet%208/EFTA00031589.pdf), [EFTA00030101](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030101.pdf) | Government responses about evidence handling |
| [EFTA00032465](https://www.justice.gov/epstein/files/DataSet%208/EFTA00032465.pdf), [EFTA00032669](https://www.justice.gov/epstein/files/DataSet%208/EFTA00032669.pdf) | Defense requests for evidence segregation |

### 5.2 Key Forensic Finding: Apple Devices Required Cellebrite

Per [EFTA00020322](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020322.pdf), the government explicitly stated that images seized from Epstein's **Apple devices** required Cellebrite software to view. This confirms:
1. Apple devices were seized from Epstein
2. Cellebrite was used to extract data from these Apple devices
3. The extracted data was provided to defense on hard drives

### 5.3 Steve Bannon's iPhone 7

Per [EFTA00025553](https://www.justice.gov/epstein/files/DataSet%208/EFTA00025553.pdf) and [EFTA00030999](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030999.pdf), during a Cellebrite review of Steve Bannon's iPhone 7 (as part of an apparently separate "WBTW" case), an image of Trump and Ghislaine Maxwell was found on Bannon's phone. This cross-case discovery was flagged internally.

---

## 6. SARAH KELLEN'S APPLE MAIL DATA

### Documents with `sarahk525@mail.mac.com` IMAP References

These documents contain Apple Mail PLIST metadata with IMAP mailbox paths pointing to Sarah Kellen's `.mac.com` email, indicating these emails were exported from her Apple Mail application:

| EFTA Number | Content |
|-------------|---------|
| [EFTA02299110](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02299110.pdf) | Email with original-mailbox: imap://sarahk525@mail.mac.com/Sent%20Messages |
| [EFTA02310703](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02310703.pdf) | Email with Sarah Kellen's IMAP mailbox reference |
| [EFTA02310713](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02310713.pdf) | "JE said we can cancel the hotel rooms in Menlo Park, CA... He's going to cancel the trip" + `date-sent: 1340203692` (June 20, 2012) |
| [EFTA02317839](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02317839.pdf) | Email with Sarah Kellen's mailbox reference |
| [EFTA02317855](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02317855.pdf) | Email with Sarah Kellen's mailbox reference |
| [EFTA02317856](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02317856.pdf) | Email with Sarah Kellen's mailbox reference |
| [EFTA02317857](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02317857.pdf) | Email with Sarah Kellen's mailbox reference |
| [EFTA02323043](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323043.pdf) | "any help/input would be appreciated! Thanks chica" + `original-mailbox: imap://sarahk525@mail.mac.com/Sent%20Messages` |
| [EFTA02323056](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323056.pdf) | Email with Sarah Kellen's mailbox reference |
| [EFTA02323069](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323069.pdf) | Email with Sarah Kellen's mailbox reference |
| [EFTA02323071](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323071.pdf) | Email with Sarah Kellen's mailbox reference |

**Forensic significance:** The presence of `imap://sarahk525@mail.mac.com/Sent%20Messages` in the PLIST metadata proves these emails were stored in and exported from Sarah Kellen's Apple Mail account on a Mac computer. The `.mac.com` domain was Apple's pre-iCloud email service (later transitioned to `@me.com` and then `@icloud.com`).

### Sarah Kellen's Mac -- Property-Organized Email Folders (DS9 Expansion)

> **Revisit addition (2026-02-12):** [EFTA00511040](https://www.justice.gov/epstein/files/DataSet%209/EFTA00511040.pdf) (DS9) is a Cellebrite forensic extraction report for device NYCO24329 (Macintosh HD, AFF4 forensic image format). It reveals Kellen's complete Mac Mail folder structure organized by Epstein property:
>
> - `/Users/(Deleted)/Library/Mail/V2/Mac-sarahk525/Work.mbox/LSJ.mbox/` -- emails organized under Little Saint James island
> - `/Users/(Deleted)/Library/Mail/V2/Mac-sarahk525/Work.mbox/71st.mbox/` -- emails organized under the 71st Street Manhattan townhouse
> - `/Users/(Deleted)/Library/Mail/V2/MailData/Envelope Index` -- master email database
>
> The account was marked `(Deleted)` -- the user profile had been deleted before forensic imaging, indicating attempted evidence destruction. The `Work.mbox` parent folder confirms these were treated as work-related communications.
>
> The same Macintosh (NYCO24329) also contained `/Users/karyna/Library/Mail/V6/` -- Karyna Shuliak's user account, establishing a device continuity chain from NPA-protected co-conspirator (Kellen) to Epstein's later partner (Shuliak).
>
> [EFTA00518756](https://www.justice.gov/epstein/files/DataSet%209/EFTA00518756.pdf) shows top contacts analysis: sarahk525 had 22,524 messages with her top contact, 12,304 with the second, and 10,952 with the third.

### Skype Call Logs -- Device NYCO24329 (DS9 Expansion)

> **Revisit addition (2026-02-12):** [EFTA00511018](https://www.justice.gov/epstein/files/DataSet%209/EFTA00511018.pdf)/[EFTA00511023](https://www.justice.gov/epstein/files/DataSet%209/EFTA00511023.pdf) (DS9): Cellebrite extraction from NYCO24329 includes complete Skype audio call logs spanning September 2012 through January 2014, with both incoming and outgoing calls documented. Many calls show "Cancelled" status. This provides an additional communication channel not previously documented.

---

## 7. COMPLETE LIST OF EFTA NUMBERS WITH PLIST CONTENT

### 7.1 From OCR Database (268 unique documents)

The full list of 268 EFTA numbers is extensive. Key EFTA ranges:
- [EFTA02299110](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02299110.pdf) - [EFTA02300584](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02300584.pdf) (early batch)
- [EFTA02303801](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02303801.pdf) - [EFTA02323093](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323093.pdf) (Sarah Kellen batch)
- [EFTA02351725](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02351725.pdf) - [EFTA02406465](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02406465.pdf) (mid-range)
- [EFTA02453274](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02453274.pdf) - [EFTA02502971](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02502971.pdf) (later batch)
- [EFTA02513964](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02513964.pdf) - [EFTA02571051](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02571051.pdf) (largest batch -- Lesley Groff emails)
- [EFTA02584723](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02584723.pdf) - [EFTA02700500](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02700500.pdf) (latest batch)

### 7.2 From Redaction Analysis (12 unique documents, all with bad_overlay redactions)

- [EFTA01758519](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01758519.pdf), [EFTA01765156](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01765156.pdf), [EFTA01766832](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01766832.pdf), [EFTA01774075](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01774075.pdf), [EFTA01774370](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01774370.pdf)
- [EFTA01781767](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01781767.pdf), [EFTA01792918](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01792918.pdf), [EFTA01793116](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01793116.pdf), [EFTA01802972](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01802972.pdf)
- [EFTA02114558](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02114558.pdf), [EFTA02522767](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02522767.pdf), [EFTA02696356](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02696356.pdf)

---

## 8. ASSESSMENT AND CONCLUSIONS

### 8.1 Nature of the PLIST Data

The PLIST content found across these 460+ documents is **Apple Mail internal message metadata**, NOT:
- iPhone/iPad device backups
- Safari browsing history
- Contacts databases
- Location data
- App usage data

The metadata was embedded because emails were exported from Apple Mail (Mail.app on macOS) in a format that included the internal PLIST representation. This happened because:
1. The emails were printed or exported to PDF directly from Apple Mail
2. Apple Mail's internal metadata (conversation-id, date-received, flags, gmail-label-ids, remote-id, original-mailbox) was included in the export
3. The metadata was not stripped before the documents were produced in discovery

### 8.2 Forensic Value

Despite not being device backup data, this PLIST metadata is still forensically valuable because:

1. **Email Account Identification:** Confirms `jeevacation@gmail.com` (Epstein) and `sarahk525@mail.mac.com` (Kellen) as email accounts
2. **Precise Timestamps:** Unix timestamps in `date-received` provide exact receipt times (to the second) for emails, independent of what the email header says
3. **Gmail Label IDs:** The `gmail-label-ids` fields show how emails were categorized in Gmail, potentially revealing organizational patterns
4. **Conversation Threading:** `conversation-id` values could be used to reconstruct email threads
5. **Remote Message IDs:** `remote-id` values map to IMAP message IDs on the mail server
6. **Mail Client Identification:** Proves Apple Mail was used (not just webmail)
7. **Folder Information:** `original-mailbox` reveals which folder emails were filed in (e.g., Sent Messages)

### 8.3 Date Coverage

The PLIST metadata timestamps in the OCR database cover email activity from **September 2009 to October 2018** -- a 9-year window ending approximately 9 months before Epstein's arrest on July 6, 2019. With the full corpus, DS9 Cellebrite extractions provide device-level timestamps independent of email PLIST metadata, and the PLIST date range may extend further.

### 8.4 Redaction Failures

12 documents in dataset10 had PLIST content that was supposed to be redacted but was recoverable due to `bad_overlay` redactions (high confidence 0.77-0.99). This suggests the redaction process did not properly handle the XML/PLIST metadata embedded in the email exports.

### 8.5 Previously Analyzed vs. New Findings

- The **OCR-based findings** (268 documents) represent data visible in the document text and captured by OCR processing. These would be available to anyone examining the documents.
- The **12 redacted PLIST documents** from the redaction analysis are potentially NEW findings, as the PLIST content was hidden beneath redaction overlays and only recovered through the document analysis process.
- The **Cellebrite/forensic device** references (17 documents in DS8; 21+ in DS9) provide context about how Apple device data was handled in the case but are visible in the document text.

### 8.6 Regarding [EFTA00524160](https://www.justice.gov/epstein/files/DataSet%209/EFTA00524160.pdf)

[EFTA00524160](https://www.justice.gov/epstein/files/DataSet%209/EFTA00524160.pdf) does not exist in any database. The closest match is [EFTA01524160](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01524160.pdf), which is a Ghislaine Maxwell JPMorgan Chase bank statement from April 2003 with no PLIST content whatsoever. The original query about this EFTA number having "PLIST encoding" appears to be based on incorrect information.

---

## APPENDIX A: Sample PLIST Metadata ([EFTA02570954](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570954.pdf))

Full recovered text showing typical Apple Mail PLIST structure:

```
From: [redacted]
Sent: Thursday, June 13, 2013 9:43 PM
To: jeevacation@gmail.com

Salam capt keith holland

Sent from my iPhone

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>conversation-id</key>
    <integer>257285</integer>
    <key>date-last-viewed</key>
    <integer>0</integer>
    <key>date-received</key>
    <integer>1371159841</integer>   [= June 13, 2013 5:44:01 PM]
    <key>flags</key>
    <integer>8590195713</integer>
    <key>...
```

## APPENDIX B: Sample PLIST Metadata with IMAP Mailbox ([EFTA02323043](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323043.pdf))

```
> any help/input would be appreciated!
> Thanks chica

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>flags</key>
    <integer>8590195713</integer>
    <key>original-mailbox</key>
    <string>imap://sarahk525@mail.mac.com/Sent%20Messages</string>
    <key>remote-id</key>
    <string>4043</string>
</dict>
</plist>
```

## APPENDIX C: Cellebrite Apple Device Evidence ([EFTA00020322](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020322.pdf))

```
All electronic images should be viewable as thumbnails, except those seized
from Apple devices, which must be viewed using Cellebrite.

The Cellebrite software will be provided on the drive for your review of
images and videos seized from Apple devices.

The electronic files have the same metadata on the hard drive that was
available when the FBI seized each image. For images that were carved or
deleted, no metadata was recovered, so none is viewable.
```

---

*End of Report*
