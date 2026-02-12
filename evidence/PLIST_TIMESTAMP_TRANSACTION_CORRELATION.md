# PLIST Timestamp-Transaction Correlation Analysis

## Epstein DOJ Files: Apple Mail Metadata Forensic Timeline

**Analysis Date:** 2026-02-07
**Source:** the OCR text extraction database -- `ocr_results` table
**Method:** Extracted Unix timestamps from Apple Mail PLIST `date-received` fields embedded in OCR text, converted to human-readable dates, cross-referenced with known financial transaction dates.

---

## Executive Summary

420 emails with parseable Apple Mail PLIST timestamps were extracted from the DS11 OCR text records, spanning **September 1, 2009 through April 9, 2019**. DS9 contains an additional **571 documents** with PLIST `date-received` fields and **614 with full PLIST XML blocks**, representing the raw email source files from which the DS11 OCR data was derived. Cross-referencing these timestamps with critical financial transaction dates reveals:

1. **The Aug 2014 spike (23 emails) directly overlaps the $13.5M Tudor Futures transfer** -- the single highest-activity month in 2014. DS9 Exhibit B ([EFTA00080260](https://www.justice.gov/epstein/files/DataSet%209/EFTA00080260.pdf)) clarifies the transfer occurred in two tranches: $12,826,541 on Aug 4, 2014 and $673,459 on Aug 8, 2014 (not Aug 15 as originally cited).
2. **Dec 2016-Jan 2017 spike (39 emails in 2 weeks) coincides with the $30.5M Sotheby's/Christie's to Haze Trust period** -- includes a JE-to-Leon Black email about liquidating trusts and "sensitive accounts." DS9 also contains a second Leon Black liquidation email ([EFTA01057105](https://www.justice.gov/epstein/files/DataSet%209/EFTA01057105.pdf), Jan 12, 2017) referencing IRS Form 8865 and "fire castrucci."
3. **Nov 2017 spike (18 emails) contains direct financial communications** -- JE to David Mitchell about "cascade" payments and to Richard Kahn about trustee changes and "account statements." **Correction:** "cascade" refers to Crescendo Real Estate Partners Ltd. (a Guernsey lender in Mitchell's Life Hotel deal), not to cascading fund transfers (see Section III correction below). Separately, "Cascade Investments LLC" is Bill Gates's private holding company ([EFTA00628797](https://www.justice.gov/epstein/files/DataSet%209/EFTA00628797.pdf)).
4. **A gap in the DS11 PLIST-timestamped subset (Nov 14, 2018 - Feb 21, 2019) does not reflect a gap in actual email activity.** DS9 contains 40+ emails from jeevacation@gmail.com during this period, including conversations with Larry Summers, Ehud Barak, Richard Kahn, Nicole Junkermann, John Brockman, and Noam Chomsky. The gap reflects a device/export discontinuity in the DS11 Apple Mail export, not a communication shutdown. See Section F correction below.
5. **The email collection in the DS11 PLIST subset effectively ends Nov 14, 2018** with only 6 straggler emails in 2019 -- this reflects the Apple Mail device or export stopping its sync around mid-November 2018, while the underlying jeevacation@gmail.com account remained fully active via other means (likely web or another device)

---

## I. Email Volume Statistics

### Yearly Distribution
| Year | Count | Notes |
|------|-------|-------|
| 2009 | 1 | Single email |
| 2010 | 28 | Post-plea period |
| 2011 | 22 | |
| 2012 | 24 | |
| 2013 | 71 | Major spike year |
| 2014 | 80 | **Highest year -- Tudor Futures period** |
| 2015 | 18 | Sharp decline |
| 2016 | 42 | Recovery |
| 2017 | 76 | Second highest -- Sotheby's/trust period |
| 2018 | 52 | Truncated Nov 14 |
| 2019 | 6 | Collection effectively ends |

**Average monthly volume:** 5.5 emails/month

### Activity Spikes (>= 2x monthly average)
| Month | Count | Multiple | Correlating Event |
|-------|-------|----------|-------------------|
| 2010-12 | 12 | 2.2x | Unknown |
| 2013-06 | 39 | **7.1x** | **Largest spike in entire collection** |
| 2014-02 | 16 | 2.9x | Pre-Tudor period |
| 2014-08 | 23 | **4.2x** | **$13.5M Tudor Futures to Southern Financial** |
| 2014-09 | 16 | 2.9x | Post-Tudor continuation |
| 2016-01 | 13 | 2.4x | Unknown |
| 2016-12 | 18 | 3.3x | **Pre-Sotheby's/Haze Trust activity** |
| 2017-01 | 21 | **3.8x** | **$30.5M Sotheby's/Christie's to Haze Trust period** |
| 2017-11 | 18 | 3.3x | **"Cascade" payments + trustee changes** |

---

## II. Critical Transaction Cross-Reference

### A. $13.5M Tudor Futures to Southern Financial (Aug 2014)

**Window: +/- 14 days of Aug 4-8, 2014 (two-tranche transfer)**
**Emails found: 21** -- This is the densest cluster relative to a specific transaction date.

> **Correction (2026-02-12):** DS9 Exhibit B ([EFTA00080260](https://www.justice.gov/epstein/files/DataSet%209/EFTA00080260.pdf)) shows the Tudor transfer was executed in two tranches: **$12,826,541 on Aug 4, 2014** and **$673,459 on Aug 8, 2014**, totaling $13,500,000. Monthly portfolio valuations ([EFTA01194336](https://www.justice.gov/epstein/files/DataSet%209/EFTA01194336.pdf)) confirm Tudor Futures went from $13,501,622 to $0 between July 31 and August 31, 2014. The Aug 15 date originally cited was the date of the "tomorw?" email, not the transfer itself.

| Days | Date | EFTA | Content |
|------|------|------|---------|
| -5 | Aug 10 | [EFTA02588549](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02588549.pdf) | (metadata only) |
| -5 | Aug 10 | [EFTA02588573](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02588573.pdf) | Paula Heil Fisher - "ps." |
| -3 | Aug 12 | [EFTA02588546](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02588546.pdf) | (metadata only) |
| **0** | **Aug 15** | **[EFTA02589073](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589073.pdf)** | **JE to "President" -- "tomorw ?"** |
| +2 | Aug 17 | [EFTA02588569](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02588569.pdf) | **JE to Erika Kellerhals** -- "Upon reflection I see little upside in having stacy and I meet, prior to her winning, we dont need any funny press. I trust her as she is your friend." |
| +3 | Aug 18 | [EFTA02589105](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589105.pdf) | JE to Ann Rodriquez re: "Chris" -- scheduling meeting at 11:45 |
| +4 | Aug 19 | [EFTA02589074](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589074.pdf) | Reply to JE -- "telepathy" + "grand Canyon rafting trip" |
| +6 | Aug 21 | [EFTA02589071](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589071.pdf) | Subject: "Alma" |
| +7 | Aug 22 | [EFTA02589066](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589066.pdf) | (metadata only) |
| +8 | Aug 23 | [EFTA02589094](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589094.pdf) | (metadata only) |
| +9 | Aug 24 | [EFTA02589075](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589075.pdf) | JE to COLOM (Olivier Colom - Edmond de Rothschild) |
| +13 | Aug 28 | [EFTA02518352](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518352.pdf) | **JE to Ann Rodriquez** -- "Schedule I leave sat morning 7 arrive back Monday 3, leave sun 7 for week noisy work best done week of 8th" |
| +14 | Aug 29 | [EFTA02518861](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518861.pdf) | (metadata only) |
| +14 | Aug 29 | [EFTA02518872](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518872.pdf) | **Ann Rodriquez to JE** -- Subject: "Lunch" |
| +14 | Aug 29 | [EFTA02518879](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518879.pdf) | JE to Ann Rodriquez |
| +14 | Aug 29 | [EFTA02518908](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518908.pdf) | (metadata only) |
| +14 | Aug 29 | [EFTA02518917](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518917.pdf) | (metadata only) |
| +14 | Aug 29 | [EFTA02518924](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518924.pdf) | (metadata only) |

**Key Finding:** On Aug 15, 2014 (approximately one week after the two-tranche Tudor Futures transfer of Aug 4/8, 2014), JE sent a one-word email to someone identified as "President" asking "tomorw ?" -- suggesting a next-day meeting or action. Two days later, he emailed Erika Kellerhals about avoiding "funny press" around someone named "Stacy." The Aug 24 email to COLOM connects to Olivier Colom of Edmond de Rothschild (France), whose disclaimer appears in the same document set.

### B. $30.5M Sotheby's/Christie's to Haze Trust (2017)

**Window: Dec 19, 2016 - Jan 13, 2017 (the dense cluster)**
**Emails found: 31 in this 25-day window**

**Critical emails in this cluster:**

| Date | EFTA | Content |
|------|------|---------|
| **Dec 21, 2016** | **[EFTA02664953](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664953.pdf)** | **JE to Leon Black**: "lets liquidate the J BLACK trust. the reason is that judy has passed. .2 deal with wechsler telling at least joe, and probably others that there are 'sensitive accounts' why he would do that is beyond me. .3 we should mock up this years gift tax to verify. all in order." |
| Dec 25, 2016 | [EFTA02664943](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664943.pdf) | JE to Jabor Y. (content redacted/confidential notice only) |
| Dec 30, 2016 | [EFTA02664901](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664901.pdf) | JE to Jermaine Ruan re: "Google wifi" -- "you can test in main compound after i leave" |
| **Dec 31, 2016** | **[EFTA02664963](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664963.pdf)** | **JE to Larry Visoski re: "GV"** -- "Thanks Susan we are definitely getting a5, The market is what it is, and I couldn't get more than a 8.5 bid for yours and then sell mine" -- **Aircraft/asset sale negotiation** |
| Dec 31, 2016 | [EFTA02664928](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664928.pdf) | Reply re: "Happy New Year !!!" -- "haappy times ahead" |
| Jan 1, 2017 | [EFTA02664888](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664888.pdf) | "Lf" to JE -- "you already have everything success, money, fame, joyful life" |
| Jan 1, 2017 | [EFTA02664920](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664920.pdf) | JE re: "COO" -- links to Wikipedia, "We visited hom party!!!! Great time" |
| Jan 2, 2017 | [EFTA02664937](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664937.pdf) | JE fwd: "Ok to book flight for TOMORROW?" via Lesley Groft |
| Jan 4, 2017 | [EFTA02664913](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664913.pdf) | Lesley Croft to JE -- Subject: "Dangene and Jennie" |
| **Jan 12, 2017** | **[EFTA02663622](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02663622.pdf)** | **JE to Ann Rodriquez re: "PRD to BVI"** -- "yes delay until next wed" / Ann: "Should I cancel PRD going to the BVI tomorrow afternoon? Carlos was taking PRD down tomorrow at 12pm and Randy was following him in little C to pick him back up." |

**Key Findings:**
1. The **Leon Black "liquidate the J BLACK trust" email (Dec 21, 2016)** is sent 10 days before the Sotheby's/Christie's transaction window opens. Epstein explicitly references "sensitive accounts" being disclosed by someone named Wechsler.
2. The **GV negotiation** (Dec 31) suggests active asset sales -- "couldn't get more than a 8.5 bid" -- possible aircraft (Gulfstream V) trade.
3. **BVI logistics email** (Jan 12) shows active movement to the British Virgin Islands -- a key offshore jurisdiction -- with "PRD" being transported.

### C. $25M Rothschild to Southern Trust (Dec 2015)

**Window: +/- 14 days of Dec 15, 2015**
**Emails found: 1**

| Date | EFTA | Content |
|------|------|---------|
| Dec 22, 2015 | [EFTA02477179](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02477179.pdf) | **Larry Visoski to JE** -- "Jeffrey Do you have estimated departure time Friday to Marrakesh? Flight time 7+10min LSJ to GMMX (Marrakesh). Passengers: you and Karyna only?" |

**Key Finding:** One week after the $25M Rothschild transfer, Epstein is flying from Little St. James (LSJ) to Marrakesh, Morocco with Karyna (Shuliak). Private jet logistics for international travel immediately following a massive financial transfer.

**Related Rothschild correspondence found elsewhere:**
- **[EFTA02502971](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02502971.pdf)** (Apr 19, 2015): "Ariane de Rothschild" (signed as "Ade Rothschid") to JE -- discusses personal matters, mentions "michael Douglas's house in Palma de Mallorca is for sale at Sothebys" and states "this is my new email address that nobody can access"
- **[EFTA02518347](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518347.pdf)**: Olivier Colom (Edmond de Rothschild France employee disclaimer) in correspondence with JE (Jul 27, 2014)

> **Revisit addition (2026-02-12):** DS9 contains the full Rothschild email thread (7+ messages over Apr 19-22, 2015) showing Epstein was actively advising Ariane de Rothschild on her separation/divorce from Benjamin de Rothschild, discussing "board vote, custodianship, regulators" ([EFTA00858979](https://www.justice.gov/epstein/files/DataSet%209/EFTA00858979.pdf)). Epstein was not merely receiving a secret communication channel -- he was providing strategic advice on corporate governance and marital separation to the wife of the man whose bank sent $25M to Epstein's Southern Trust eight months later.

### D. Haze Trust "Great Drain" -- $48.3M to Southern Financial (Jun-Jul 2018)

**Window: May 16 - Jul 15, 2018**
**Emails found: 12**

| Days | Date | EFTA | Content |
|------|------|------|---------|
| -30 | May 16 | [EFTA02664984](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664984.pdf) | (metadata only) |
| **-29** | **May 16** | **[EFTA02663611](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02663611.pdf)** | **JE to Richard Kahn re: "price Maybach berline"** -- "im goimg to exchnage my current one for this, sould reduce the vat charge as well" + link to Mercedes-Benz Maybach pricing |
| -29 | May 17 | [EFTA02664954](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664954.pdf) | (metadata only) |
| -29 | May 17 | [EFTA02664915](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664915.pdf) | (metadata only) |
| **-29** | **May 17** | **[EFTA02664945](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664945.pdf)** | **Richard Kahn to JE** -- "another christies disaster" + link to Steve Wynn Picasso damage story. Richard Kahn, HBRK Associates Inc., 575 Lexington Avenue, NY |
| -29 | May 17 | [EFTA02664929](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664929.pdf) | (metadata only) |
| -29 | May 17 | [EFTA02664988](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664988.pdf) | (metadata only) |
| +6 | Jun 21 | [EFTA02571051](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02571051.pdf) | Reference to "St Thomas USVI 00802" |
| +6 | Jun 21 | [EFTA02570995](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570995.pdf) | JE re: "LSJ GSJ" furniture package -- "yes. you should have exactly what you guys want" -- Karen requesting furniture purchase approval for LSI Staff Cottage |
| +6 | Jun 21 | [EFTA02571042](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02571042.pdf) | Anti-aging researcher article shared |
| **+11** | **Jun 26** | **[EFTA02518838](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518838.pdf)** | **Lesley Croft to JE** -- "HHI requesting tickets to World Cup France vs Argentina on June 30 - Tickets about $900 each...she would like 2 of them...know you have said OK to her going to some games" |
| +27 | Jul 12 | [EFTA02602608](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02602608.pdf) | (metadata only) |

**Key Findings:**
1. Richard Kahn (HBRK Associates) appears twice in May 2018 -- both in a **Maybach luxury car exchange** email and a **Christie's art damage** discussion. Kahn is a key financial intermediary.
2. The May 16 Maybach email is notable: Epstein is exchanging luxury vehicles while $48.3M is about to begin flowing from Haze Trust to Southern Financial. He instructs Kahn to handle the VAT implications.
3. Furniture purchases for "LSI Staff Cottage" and World Cup tickets suggest business-as-usual spending during the drain period.

### E. KYC Breach (Apr 16, 2018)

**Window: +/- 7 days**
**Emails found: 8**

| Days | Date | EFTA | Content |
|------|------|------|---------|
| **-5** | **Apr 11** | **[EFTA02474953](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02474953.pdf)** | **"Greg" to JE** -- "Please introduce me to the lawyer/accountant team and I will have my guy deal with them on paperwork. Great to see you!" |
| -4 | Apr 12 | [EFTA02474967](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02474967.pdf) | JE -- Re: "Nyc trip" -- "do you have time today to come and say hello" (visiting guest using JE NYC property) |
| -4 | Apr 12 | [EFTA02474970](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02474970.pdf) | JE seeking "a person to work with me on all houses. full time. girl up to 30 that can travel that has great taste. does not have to be pretty. but must be responsible" |
| -4 | Apr 12 | [EFTA02474932](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02474932.pdf) | (metadata only) |
| -4 | Apr 12 | [EFTA02474939](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02474939.pdf) | (metadata only) |
| -4 | Apr 12 | [EFTA02474938](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02474938.pdf) | (metadata only) |
| +1 | Apr 17 | [EFTA02469746](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02469746.pdf) | (JEE confidential notice only) |
| +6 | Apr 22 | [EFTA02462586](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02462586.pdf) | **JE to David Mitchell** -- "steven hanson wants to see me this morning at 8 am, what should i know?" / Mitchell responds about restaurant, borough commissioner, TCO (Temporary Certificate of Occupancy), expediter, third-party inspector, "$22,500 to pay the inspectors for the compressed time" |

**Key Findings:**
1. Five days before the KYC breach documentation, someone named **"Greg" asks JE for an introduction to his "lawyer/accountant team"** for "paperwork" -- potentially related to compliance/KYC matters.
2. Six days after KYC breach, JE is discussing **inspection expediting** with David Mitchell (Mitchell Holdings LLC, 745 Fifth Avenue -> later 801 Madison Avenue) -- potentially related to property compliance.

### F. $100K Aviloop/Marcinkova + Miami Herald + Emergency Wires + Dissolution (Nov 2018 - Feb 2019)

**DS11 PLIST GAP: Nov 14, 2018 through Feb 21, 2019 -- 99 days with zero DS11 PLIST-timestamped emails**

> **Correction (2026-02-12):** This section originally characterized the gap as the "most significant finding" and proposed four explanations (channel switch, device wipe, evidence destruction, device separation). **The 99-day gap does not exist in DS9.** DS9 contains 40+ emails from jeevacation@gmail.com during this period, demonstrating continuous email activity. The gap is an artifact of the DS11 PLIST extraction methodology -- the Apple Mail export that produced the DS11 PLIST metadata stopped updating around mid-November 2018, while the underlying email account remained fully active via other means (likely web or another device).
>
> Key DS9 emails during the supposed gap:
> - **Nov 14-15, 2018**: 15+ emails including architect travel, Apple Watch orders, Joscha Bach island trip
> - **Dec 17, 2018**: Barak to Epstein: "you should make clear that i dont work for mossad :)" / Epstein: "unfortunately, not" ([EFTA01013272](https://www.justice.gov/epstein/files/DataSet%209/EFTA01013272.pdf))
> - **Dec 21-26, 2018**: Summers-Epstein exchange: "Want to discuss the Donald...Curious re Dersh" ([EFTA01009424](https://www.justice.gov/epstein/files/DataSet%209/EFTA01009424.pdf)); Moscow flight rescheduling ([EFTA00488235](https://www.justice.gov/epstein/files/DataSet%209/EFTA00488235.pdf)); fund transfers ([EFTA01010835](https://www.justice.gov/epstein/files/DataSet%209/EFTA01010835.pdf))
> - **Jan 2-9, 2019**: Kahn to Epstein re Honeycomb Partners, Scott Link invoices, Boothbay fund returns ([EFTA01009628](https://www.justice.gov/epstein/files/DataSet%209/EFTA01009628.pdf), [EFTA01009503](https://www.justice.gov/epstein/files/DataSet%209/EFTA01009503.pdf), [EFTA01009065](https://www.justice.gov/epstein/files/DataSet%209/EFTA01009065.pdf))
>
> The correct explanation is simpler than the four originally proposed: the Apple Mail device or export stopped syncing/updating after approximately Nov 14, 2018, while Epstein continued using jeevacation@gmail.com via web or other clients. The original Section F interpretation should be disregarded.

The DS11 PLIST subset shows the following gap pattern:

The last DS11 PLIST email before the gap: **Nov 14, 2018 ([EFTA02616241](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02616241.pdf))**
The first DS11 PLIST email after the gap: **Feb 21, 2019 ([EFTA02633608](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02633608.pdf))** -- "George is here, thank you" from Carluz & Arline Toylo

The 6 DS11 PLIST emails that appear in 2019 (Feb 21 - Apr 9) are sparse:
| Date | EFTA | Content |
|------|------|---------|
| Feb 21 | [EFTA02633608](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02633608.pdf) | "George is here, thank you" -- household staff |
| Feb 25 | [EFTA02633609](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02633609.pdf) | JEE confidential notice only |
| Mar 1 | [EFTA02633143](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02633143.pdf) | JE to David Mitchell -- Martha Stewart cannabis article |
| Mar 1 | [EFTA02633134](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02633134.pdf) | Quantum Vision Construction LLC correspondence |
| Mar 2 | [EFTA02633147](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02633147.pdf) | (metadata only) |
| Apr 9 | [EFTA02633606](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02633606.pdf) | (metadata only) -- **LAST EMAIL IN DS11 PLIST SUBSET** |

These 6 emails likely represent emails that were coincidentally present in the DS11 export through a different mechanism (e.g., forwarded chains that re-appeared in the Apple Mail client), not a resumption of the Apple Mail sync.

---

## III. November 2017 Spike: The Financial Operations Cluster

November 2017 (18 emails, 3.3x average) contains the most explicitly financial operational communications:

### [EFTA02664953](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664953.pdf) -- JE to Leon Black (Dec 21, 2016)
> "lets liquidate the J BLACK trust. the reason is that judy has passed. .2 deal with wechsler telling at least joe, and probably others that there are **'sensitive accounts'** why he would do that is beyond me. .3. we should mock up this years gift tax to verify. all in order."

### [EFTA02570991](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570991.pdf) -- JE to David Mitchell (Nov 7, 2017)
> "tomorow you must make **money**. clear that **cascade** will au[thorize?] the **payments**. do you have another idea for who can hold the..."
> *(Message truncated by OCR/encoding)*

### [EFTA02570951](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570951.pdf) -- JE to Richard Kahn (Nov 7, 2017)
> "deborah, Noam has decided to replace max with Lawrence Krauss, a friend and highly respected scientist as **Trustee**. as we discussed if harry agrees, this should put the current issue to rest. he would like gene landy to recommend person re a **lawsuit against bain**, but I thought the first step and noam agreed would be a call to bain from you in the hopes of a **settlement**. If he has to file a lawsuit he understands he will need a different firm as Gene said he thought your firm had a conflict. I certainly want none of these steps to impede the delivery of the **account statements**."

**Analysis:** On the same day (Nov 7, 2017), Epstein sent two financial operations emails:
1. To Mitchell: Instructions about **"cascade" authorizing payments** and finding someone to "hold" something
2. To Kahn: **Trustee replacement**, potential **lawsuit**, need for **account statements** delivery, conflict of interest concerns

~~The term "cascade" in a payment context may refer to cascading fund transfers -- a structure where money flows through multiple entities sequentially, consistent with the multi-entity financial architecture (Haze Trust -> Southern Financial -> etc.).~~

> **Correction (2026-02-12):** This interpretation is incorrect. DS9 reveals "cascade" in the Mitchell emails refers to **Crescendo Real Estate Partners Ltd.**, a Guernsey-based lender in Mitchell's Life Hotel real estate deal. Mitchell's reply ([EFTA00960874](https://www.justice.gov/epstein/files/DataSet%209/EFTA00960874.pdf)) explicitly states "all the crescendo money went to DB" and discusses the lender's control over funds as a condition for a preferred equity position. The payments being "audited" are construction payables for Mitchell's Life Hotel project.
>
> Separately, DS9 identifies two other distinct "Cascade" entities: (1) **Cascade Investments LLC** = Bill Gates's private holding company, confirmed by Boris Nikolic ([EFTA00628797](https://www.justice.gov/epstein/files/DataSet%209/EFTA00628797.pdf)); and (2) **"Loan Cascade"** in Leon Black financial documents ([EFTA00716362](https://www.justice.gov/epstein/files/DataSet%209/EFTA00716362.pdf): "BFP can give notice by May 31 to withdraw $25mm from Loan Cascade"), a named investment vehicle within the Black Family Partners structure. None of these meanings support the "cascading fund transfer" interpretation.

---

## IV. Key Financial Correspondents in PLIST Emails

### Richard Kahn (HBRK Associates Inc.)
- 575 Lexington Avenue, 4th Floor, New York, NY 10022
- 7 emails in PLIST collection
- Topics: Trust liquidation, Christie's art, Maybach purchase, Jawbone investment, trustee changes, account statements, holiday scheduling
- **Role:** Financial advisor/associate handling trust operations, art transactions, investment tracking

### David Mitchell (Mitchell Holdings LLC)
- 745 Fifth Avenue -> 801 Madison Avenue, New York, NY 10065
- 4 emails in PLIST collection
- Topics: "cascade" payments, investor letters on 82nd St property, restaurant/property inspections, Martha Stewart
- **Role:** Real estate/property operations, payment processing

### Leon Black
- 1 email in DS11 PLIST collection (but highly significant); DS9 contains a second liquidation directive
- Topic: Trust liquidation, "sensitive accounts," gift tax verification
- **Role:** Apollo Global Management founder; trust relationship with Epstein

> **Revisit addition (2026-02-12):** DS9 contains [EFTA01057105](https://www.justice.gov/epstein/files/DataSet%209/EFTA01057105.pdf) (Jan 12, 2017) -- a second, more detailed liquidation directive: "lets begin, preparation.- taking steps.. 1 liquidate trust 2, liquidate artspace regan. talk to me about phaidon. fire castrucci.. 3 prepare financials. recall DB is a bene...talk to me .4. re 8865 issues.. you are no more than 25% done. now comes the real work." The IRS Form 8865 reference (Return of U.S. Persons With Respect to Certain Foreign Partnerships) indicates Epstein was directing Black's tax compliance and partnership restructuring.

### Larry Visoski
- 7 emails in PLIST collection
- Topics: Flight logistics, aircraft/asset negotiations ("GV" offer), furniture, electronics
- **Role:** Chief pilot, logistics coordinator

### Lesley Groff/Croft
- 5+ emails in PLIST collection
- Topics: Staff scheduling, flight bookings, Richard Kahn holiday, World Cup tickets
- **Role:** Executive assistant, scheduling

### Ann Rodriquez
- 5+ emails in PLIST collection
- Topics: BVI logistics, scheduling, household management, WAPA (power utility)
- **Role:** Island operations manager

### Ariane de Rothschild
- 1 email in PLIST collection
- Signed "Ade Rothschid" -- "this is my new email address that nobody can access"
- Mentions Sotheby's (Michael Douglas Mallorca property)
- **Connection to $25M Rothschild transfer to Southern Trust (Dec 2015)**

---

## V. Financial Terms Found in PLIST Email Collection

| Term | Hits | Key Documents |
|------|------|---------------|
| trust | 4 | JE-Leon Black "liquidate J BLACK trust" + "sensitive accounts"; JE-Kahn trustee replacement; JE re Zuckerman "All trusts" |
| account | 4 | "sensitive accounts" (Leon Black); "lawyer/accountant team" (Greg); "account statements" (Kahn) |
| payment | 2 | "cascade will au[thorize] the payments" (Mitchell); Bombardier $5mm payment (Lyndon Lea) |
| money | 4 | "you must make money" (Mitchell); phone bill request; New Year greeting; modeling |
| Sotheby | 1 | Ariane de Rothschild -- Mallorca property |
| Christie | 1 | Richard Kahn -- "another christies disaster" (Steve Wynn Picasso) |
| Rothschild | 2 | Ariane de Rothschild; Edmond de Rothschild (France) disclaimer |
| Kahn | 7 | Financial operations, trust, art, investments |
| BVI | 1 | JE-Rodriquez: "PRD to BVI" logistics |
| wire | 1 | "Verizon Wireless BlackBerry" (false positive) |
| bank | 2 | "Transplant Bank" article; "Euromoney" newsletter |
| lawyer | 3 | SingularityNET lawyer; immigration permit; "lawyer/accountant team" |
| Maybach | 1 | JE-Kahn: vehicle exchange with VAT reduction |
| GV | 1 | JE-Visoski: aircraft/asset sale negotiation |

---

## VI. Gap Analysis: Suspicious Silences

### Major Gaps Correlating with Financial Events

| Gap Period | Days | Correlating Financial Event |
|-----------|------|---------------------------|
| Sep 6, 2016 - Dec 19, 2016 | **104 days** | Pre-Sotheby's/Haze Trust setup period |
| Feb 11, 2017 - Jun 22, 2017 | **131 days** | Post-Sotheby's transaction completion |
| **Nov 14, 2018 - Feb 21, 2019** | **99 days** | **DS11 PLIST subset gap only; DS9 shows continuous email activity** |
| Aug 6, 2018 - Oct 5, 2018 | **60 days** | Unknown -- pre-Herald investigation period |

The 131-day gap (Feb-Jun 2017) after the Sotheby's/Haze Trust cluster is notable: after 39 emails in the Dec 2016-Jan 2017 period, activity drops to a single email in February and then nothing until June.

---

## VII. Timeline Correlation Matrix

```
Transaction                          Email Activity    Correlation
-----------                          --------------    -----------
$13.5M Tudor (Aug 2014)              23 emails/month   STRONG - same-day email, 21 in window
$25M Rothschild (Dec 2015)           1 email           WEAK - but flight to Marrakesh +7d
$30.5M Sotheby's/Haze (Jan 2017)    39 emails/2 weeks STRONG - Leon Black trust email -10d
KYC Breach (Apr 16, 2018)            8 emails          MODERATE - lawyer/accountant intro -5d
Haze Drain Start (Jun 2018)          12 emails          MODERATE - Kahn/Christie's, Maybach
$100K Aviloop (Nov 30, 2018)         0 DS11 PLIST      DS9: 40+ emails active (gap is DS11 artifact)
Emergency Wires (Dec 2018)           0 DS11 PLIST      DS9: Barak, Summers, Kahn correspondence
$31.5M Dissolution (Feb 2019)        2 DS11 PLIST      DS9: continuous activity through Jan 2019
Arrest (Jul 6, 2019)                 0 emails          Collection ends Apr 9, 2019
```

---

## VIII. Critical Document Index

### Highest-Priority Financial Documents
1. **[EFTA02664953](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664953.pdf)** -- JE to Leon Black: Trust liquidation + "sensitive accounts" (Dec 21, 2016)
2. **[EFTA02570991](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570991.pdf)** -- JE to David Mitchell: "cascade" payments authorization (Nov 7, 2017)
3. **[EFTA02570951](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570951.pdf)** -- JE to Richard Kahn: Trustee replacement + lawsuit + account statements (Nov 7, 2017)
4. **[EFTA02518881](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518881.pdf)** -- JE to Mortimer Zuckerman + Clare Probert: "All trusts, past three year tax returns, latest will, grats, crts, pledges, art inventory, bxp filings, daily news financial statements, phone contact for Ellen, all tax preparers, Morgan Stanley last report" (Dec 15, 2013)
5. **[EFTA02502971](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02502971.pdf)** -- Ariane de Rothschild to JE: "this is my new email address that nobody can access" + Sotheby's mention (Apr 19, 2015)
6. **[EFTA02663611](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02663611.pdf)** -- JE to Richard Kahn: Maybach exchange + VAT reduction (May 16, 2018)
7. **[EFTA02589073](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589073.pdf)** -- JE to "President": "tomorw?" on day of $13.5M Tudor transfer (Aug 15, 2014)
8. **[EFTA02663622](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02663622.pdf)** -- JE to Ann Rodriquez: BVI logistics (Jan 12, 2017)
9. **[EFTA02664963](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664963.pdf)** -- JE to Larry Visoski: GV (Gulfstream V?) price negotiation (Dec 31, 2016)
10. **[EFTA02474953](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02474953.pdf)** -- "Greg" to JE: "lawyer/accountant team" introduction (Apr 11, 2018)

---

## IX. Conclusions

### 1. The Aug 2014 Tudor Correlation is the Strongest
21 emails within 14 days of the $13.5M transfer, including a same-day email from Epstein to someone identified only as "President." The Edmond de Rothschild connection (Olivier Colom correspondence 3 weeks earlier) and subsequent travel scheduling suggest coordinated financial operations.

### 2. The Leon Black "Sensitive Accounts" Email is Significant
Sent Dec 21, 2016 -- just days before the $30.5M Sotheby's/Haze Trust period -- Epstein instructs Leon Black to liquidate a trust while expressing frustration that someone named Wechsler has been telling others about "sensitive accounts." This directly connects Epstein's email activity to trust restructuring concurrent with major art-transaction financial flows.

### 3. ~~The Nov 7, 2017 "Cascade" Payment Email Suggests Structured Transfers~~ (Corrected)
~~Epstein's instruction to David Mitchell about "cascade" authorizing "payments" and finding someone to "hold" an unspecified asset, on the same day he discusses trustee replacements and settlement strategy with Richard Kahn, reveals a coordinated financial operations day.~~

> **Correction (2026-02-12):** "Cascade" in the Mitchell emails refers to Crescendo Real Estate Partners Ltd. (a Guernsey lender), not a structured transfer mechanism. The Nov 7, 2017 email thread concerns construction payables for Mitchell's Life Hotel project, not illicit cascading transfers. The simultaneous Kahn email about trustees and lawsuits remains significant as evidence of a coordinated financial operations day, but the "cascade" = "structured transfers" interpretation is withdrawn.

### 4. ~~The Nov 2018 - Feb 2019 Blackout is Forensically Significant~~ (Withdrawn)
~~The total absence of PLIST emails during the most critical financial crisis period -- when the Miami Herald story broke, emergency wires were sent, and the $31.5M dissolution occurred -- represents either evidence destruction, a communication channel switch, or device separation. This 99-day gap demands investigation into alternative communication records.~~

> **Correction (2026-02-12):** DS9 demonstrates that jeevacation@gmail.com was continuously active throughout this period. Epstein was corresponding with Larry Summers, Ehud Barak, Richard Kahn, Nicole Junkermann, John Brockman, Noam Chomsky, and construction staff during the supposed blackout. The gap exists only in the DS11 PLIST-timestamped subset and reflects a device/export discontinuity, not a communication shutdown. The four proposed explanations (channel switch, device wipe, evidence destruction, device separation) are not supported by the DS9 evidence. This conclusion is withdrawn.

### 5. Ariane de Rothschild's "Secure Email" is Notable
Her April 2015 email states "this is my new email address that nobody can access" -- indicating conscious efforts to create untraceable communication channels within Epstein's network, months before the $25M Rothschild-to-Southern Trust transfer.

---

*Generated from 420 PLIST-timestamped emails in the DS11 OCR subset. 4 additional records contained date-received fields but timestamps could not be parsed due to OCR artifacts. DS9 contains 571+ additional documents with PLIST date-received fields and 614 with full PLIST XML blocks.*

---

**REVISIT INTEGRATION (2026-02-12):** Seven corrections integrated from full corpus review (1,380,937 documents across all 12 datasets). Three corrections are classified as major: (1) The "99-day email blackout" does not exist in DS9 -- continuous email activity from jeevacation@gmail.com is documented throughout the supposed gap period; (2) The "cascade" interpretation as structured transfers is incorrect -- it refers to Crescendo Real Estate Partners Ltd.; (3) The claim that Epstein "switched communication channels" or that "evidence was destroyed" during Nov-Feb is unsupported by DS9 evidence. Two corrections are moderate: (4) Tudor transfer date corrected from Aug 15 to two tranches on Aug 4/8, 2014; (5) A second Leon Black liquidation email identified ([EFTA01057105](https://www.justice.gov/epstein/files/DataSet%209/EFTA01057105.pdf)). The PLIST email corpus is approximately 50% larger in DS9 than the 420 reported from DS11 OCR extraction. What remains valid: the Leon Black "sensitive accounts" email, the Rothschild correspondence, the Sotheby's/Haze Trust transaction correlation, the email-to-transaction spike methodology, and the identification of key financial correspondents. Cross-referenced with revisits #44, #45.
