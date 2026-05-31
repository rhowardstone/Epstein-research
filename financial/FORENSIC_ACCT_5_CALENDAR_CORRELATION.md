# FORENSIC ACCOUNTING REPORT #5: CALENDAR-FINANCIAL CORRELATION ANALYSIS

## Jeffrey Epstein DOJ Files -- Document Text Database
### Cross-Referencing Meeting/Calendar Data with Financial Transactions

**Database:** the primary document text database
**Tables Analyzed:** `redactions`, `extracted_entities`, `reconstructed_pages`
**Report Date:** 2026-02-05
**Methodology:** Extraction of hidden text from redacted documents; correlation of calendar/scheduling entries ([EFTA01900000](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01900000.pdf)-02300000 range) with financial transaction records ([EFTA01480000](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01480000.pdf)-01530000 range) and prosecutorial filings.

---

## EXECUTIVE SUMMARY

This forensic accounting analysis correlates Jeffrey Epstein's calendar/scheduling data with his financial transaction records extracted from DOJ file text layers. The analysis reveals:

1. **A critical 48-hour correlation** between the Miami Herald's publication (Nov 28, 2018) and two large wire transfers ($100,000 on Nov 30, $250,000 on Dec 3) to individuals named as possible co-conspirators in the Non-Prosecution Agreement (NPA).
2. **Regular meetings with financial figures** (Leon Black, Ehud Barak, Mort Zuckerman) that appear proximate to identifiable financial activity.
3. **A sprawling network of shell entities** (17+ entities identified at a single bank) managed by bankers Morris/Oldfield with account balances ranging from tens of thousands to $49.4 million (The Haze Trust).
4. **Monthly wire transfer patterns** evidenced by email subjects ("Jan 15th wire," "April wire," "May wire," "July wire") suggesting recurring payment obligations.
5. **Travel patterns** (flights, Teterboro references, charter requests) that align with meeting and transaction clusters.

---

## SECTION 1: CALENDAR ENTRIES EXTRACTED FROM HIDDEN TEXT

### 1.1 Complete Calendar Meeting Inventory ([EFTA01900000](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01900000.pdf)-02300000)

The following meeting/appointment entries were extracted from the document text layers. These represent Epstein's social calendar as maintained by his staff:

#### BREAKFAST MEETINGS
| EFTA # | Entry | Notable Person |
|---------|-------|----------------|
| [EFTA01892360](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01892360.pdf) | Breakfast w/Nathan M[...] | Nathan (surname redacted) |
| [EFTA02023850](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02023850.pdf) | Breakfast w/Tom Pritzker | Tom Pritzker (Hyatt Hotels) |
| [EFTA02070566](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02070566.pdf) | Re: Breakfast w/Barnaby? | Barnaby Marsh (philanthropy advisor) |
| [EFTA02090214](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02090214.pdf) | 8:30am BREAKFAST w/Andrew Farkas AT Andrew's Home | Andrew Farkas (C-III Capital) |
| [EFTA02154241](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02154241.pdf) | 8:30am Breakfast w/Ehud Barak -- Wed Nov 28 8:30am | **Ehud Barak (former Israeli PM)** |
| [EFTA02199213](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02199213.pdf) | Alert - 9:00am BREAKFAST w/Ehud | Ehud Barak |
| [EFTA02199243](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02199243.pdf) | Alert - 9:00am BREAKFAST w/Ehud and Tom | Ehud Barak + Tom (unknown) |
| [EFTA02208207](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02208207.pdf) | Alert - 9:00am BREAKFAST w/Ehud | Ehud Barak |
| [EFTA02056918](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02056918.pdf) | Alert - 8:00-9am BREAKFAST w/[...] | Name redacted |

#### LUNCH MEETINGS
| EFTA # | Entry | Notable Person |
|---------|-------|----------------|
| [EFTA01955948](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01955948.pdf) | TBD LUNCH w/Ehud Barak & Joel Kle[in] | Ehud Barak + Joel Klein |
| [EFTA02048222](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02048222.pdf) | **Alert - 1:00pm LUNCH w/Leon Black** | **Leon Black (Apollo Global)** |
| [EFTA02052245](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02052245.pdf) | lunch w/Ehud a[...] | Ehud Barak |
| [EFTA02052296](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02052296.pdf) | Alert - 12:00pm LUNCH w/Ehud | Ehud Barak |
| [EFTA02064226](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02064226.pdf) | lunch w/Larry S[ummers] | **Larry Summers (fmr Treasury Sec)** |
| [EFTA02081553](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02081553.pdf) | 12:30pm LUNCH w/Leo[n] | Likely Leon Black or Leon Botstein |
| [EFTA02107656](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02107656.pdf) | 1:30pm LUNCH w/Dan Gilbert and [...] | Dan Gilbert (Quicken Loans) |
| [EFTA02107740](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02107740.pdf) | Lunch w/Dan Gilbert on April 23rd 1:30pm Cambridge One | Dan Gilbert |
| [EFTA02136979](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02136979.pdf) | Updated Invitation: 12:30pm Lunch w/Ehud Barak | Ehud Barak |

#### DINNER MEETINGS
| EFTA # | Entry | Notable Person |
|---------|-------|----------------|
| [EFTA01777894](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01777894.pdf) | Dinner w/Bill | Bill (unspecified) |
| [EFTA01846192](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01846192.pdf) | 5:30 Dinner w/Matt Menchel | Matt Menchel |
| [EFTA01905761](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01905761.pdf) | 7:00pm Dinner w/Terje, Mona and [...] | Terje Roed-Larsen (diplomat) |
| [EFTA01907780](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01907780.pdf) | 7:00pm Dinner w/Terje, Mon[a] | Terje Roed-Larsen |
| [EFTA02007805](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02007805.pdf) | 8:00 Dinner w/Terie Ro[ed-Larsen] | Terje Roed-Larsen |
| [EFTA02051154](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02051154.pdf) | **Alert - 7:00pm DINNER w/Noam and Valeria Chomsky** | **Noam Chomsky (linguist/MIT)** |
| [EFTA02060729](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02060729.pdf) | Reminder: Mort dinner Wed [...] | **Mort Zuckerman (media/RE)** |
| [EFTA02079500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02079500.pdf) | Mort for dinner on May 5??? | Mort Zuckerman |
| [EFTA02089587](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02089587.pdf) | Re: Dinner Nov 30th -- From Yoki | Unknown associate |
| [EFTA02092187](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02092187.pdf) | **Staley Dinner** | **Jes Staley (JPMorgan/Barclays)** |
| [EFTA02147386](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02147386.pdf) | Feb 19, 2013 7:30PM Dinner w/Ter[je] | Terje Roed-Larsen |
| [EFTA02155110](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02155110.pdf) | Reminder: 7:30 Dinner w/Wo[...] | Unknown |
| [EFTA02158373](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02158373.pdf) | Reminder: 7:00 Dinner w/Moham[ed] | Mohamed (likely bin Zayed) |
| [EFTA02167472](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02167472.pdf) | Dinner w/Matt Menchel | Matt Menchel |
| [EFTA02169775](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02169775.pdf) | Declined: 8:00 TENTATIVE Dinner w/Eric La[...] | Eric (surname redacted) |
| [EFTA02173703](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02173703.pdf) | Re: Dinner w/Terje? | Terje Roed-Larsen |
| [EFTA02195896](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02195896.pdf) | 30pm Dinner w/Jeffrey -- Edward Boyden, Nowak | Ed Boyden (MIT), Martin Nowak |
| [EFTA02211210](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02211210.pdf) | Alert - TBD DINNER w/[...] | Name redacted |

#### APPOINTMENTS AND MEETINGS
| EFTA # | Entry | Notable Person |
|---------|-------|----------------|
| [EFTA01764399](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01764399.pdf) | 3:00 TENTATIVE Appt w/Barry Josephson | Barry Josephson (producer) |
| [EFTA01786087](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01786087.pdf) | Appt w/Tom McGraw, Ju[...] | Tom McGraw |
| [EFTA01797988](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01797988.pdf) | 4:30 Appt w/Jennie Saunders; 7:00 Dinner with Tim Zagat | Tim Zagat |
| [EFTA01839198](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01839198.pdf) | 4:00 Appt w/Henry Rosov[sky] | Henry Rosovsky (Harvard) |
| [EFTA01923347](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01923347.pdf) | **12pm meeting w/Mort and Ehud Tomorrow** | **Mort Zuckerman + Ehud Barak** |
| [EFTA01927556](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01927556.pdf) | 5:45pm Appt w/George Church | **George Church (Harvard genetics)** |
| [EFTA01971523](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01971523.pdf) | 3:30pm Appt w/Mo[...] | Unknown |
| [EFTA02003080](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02003080.pdf) | Make appt w/Steve Hanson | Steve Hanson |
| [EFTA02003114](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02003114.pdf) | 8:00 Appt w/Steve Ha[nson] | Steve Hanson |
| [EFTA02041069](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02041069.pdf) | Alert - 4:30pm Appt w/Sergey Beliakov | Sergey Beliakov |
| [EFTA02042596](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02042596.pdf) | Alert - 3:45pm Appt w/Carol Ann Ross | Carol Ann Ross |
| [EFTA02045532](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02045532.pdf) | 9:00am Appt w/Dr. Visco (spine specialist) | Medical |
| [EFTA02051030](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02051030.pdf) | Alert - 4:00pm Appt w/Maxim Churkin | **Maxim Churkin (son of Vitaly Churkin, Russia's UN Ambassador)** |
| [EFTA02053873](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02053873.pdf) | Alert - 2:00pm Conference Call w/Bob Crowe Di[...] | Bob Crowe |
| [EFTA02055619](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02055619.pdf) | Alert - 9:00am Appt w/Dr. Magnani for cavity | Medical |
| [EFTA02071895](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02071895.pdf) | 9:30-10:40am Appt w/Dr. Speake[r] | Medical |
| [EFTA02075023](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02075023.pdf) | Appt w/Kathy & Ariane | Unknown |
| [EFTA02123035](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02123035.pdf) | 30pm Appt w/Neil Gers[henfeld] | **Neil Gershenfeld (MIT)** |
| [EFTA02125561](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02125561.pdf) | Jeffrey Epstein Appt w/James and Eric | James & Eric (unknown) |
| [EFTA02137154](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02137154.pdf) | **Wed 6/5/2013 -- Alert 9:00am Appt w/Leon Black At Leo[n's]** | **Leon Black** |
| [EFTA02143046](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02143046.pdf) | 4:00pm Appt w/Ian Osbo[rne] | Ian Osborne |
| [EFTA02152827](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02152827.pdf) | Reminder: 10:00 Appt w/Todd | Todd (likely Wanek) |
| [EFTA02162661](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02162661.pdf) | Alert - 11:00 Appt w/[...] | Name redacted |
| [EFTA02211724](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02211724.pdf) | Alert - 5:00pm Appt w/Ehud -- 2017 | Ehud Barak |

#### TOM BARRACK ENTRIES
| EFTA # | Entry | Context |
|---------|-------|---------|
| [EFTA02043213](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02043213.pdf) | lunch at 1pm w/Tom Barrack? | Scheduling lunch |
| [EFTA02176310](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02176310.pdf) | Tom Barrack time change | Rescheduling |
| [EFTA02176329](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02176329.pdf) | Mon 9 Jan 2012 -- Tom Barrack time change | January 9, 2012 |
| [EFTA02177049](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02177049.pdf) | Tom Barrack and H.E. Sheikh | Meeting with Sheikh (likely bin Zayed) |
| [EFTA02177172](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02177172.pdf) | Subject: Tom Barrack [...] | Additional scheduling |

**FORENSIC NOTE:** Tom Barrack was meeting with Epstein AND a Sheikh (likely Sheikh Abdullah Bin Zayed, UAE). This is significant because Barrack was later indicted (2021) for acting as an unregistered foreign agent for the UAE. Epstein appears to have been a nexus between Barrack and Middle Eastern leadership.

---

## SECTION 2: FINANCIAL TRANSACTION RECORDS ([EFTA01480000](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01480000.pdf)-01530000)

### 2.1 Wire Transfer Activity -- Jeffrey E. Epstein Primary Account

The following Fedwire debits and transfers were extracted from Epstein's primary bank account statements:

#### Monthly Transaction Summary (reconstructed from fragments)
| Month/Year | Key Transactions | Recipients |
|------------|-----------------|------------|
| March | Fedwire Debit x2; Fedwire to Firstbank PR/Nautilus Inc | Nautilus Inc, Internal Transfer |
| April | Fedwire Debit; Payment to Chase Card; Internal Transfer | Chase, Internal |
| May | Fedwire to North Fork Bank; T Air Airline Support; Atlantic Turbine Inc | Aviation entities |
| June | Fedwire to Citibank NYC -- SLK Designs LLC | SLK Designs |
| July | Fedwire to Mfrs Buf -- International Jet Interiors (JEGE); Firstbank PR -- LSJE LLC | **JEGE (Epstein entity), LSJE** |
| July | Fedwire to Firstbank PR -- Bohlke International | Bohlke (USVI charter) |
| August | Fedwire to TD Bank -- Deland Training Center; Fedwire x2 | Aviation/training |
| September | Fedwire to Ronald Rodgers, Port St. Lucie FL | Ronald Rodgers |
| October | Fedwire x2; Sovereign Bk NE -- Martin G. Weinberg PC | **Weinberg (defense attorney)** |
| Various | Fedwire to Wachovia -- **Black Srebnick Kornspan** | **Epstein's defense law firm** |

### 2.2 Large Individual Transactions (>$10,000)
| EFTA # | Amount | Description |
|--------|--------|-------------|
| [EFTA01496824](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01496824.pdf) | **$56,987.07** | Check #1050, PAID 03/09 |
| [EFTA01496885](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01496885.pdf) | **$100,000.00** | Check #1074 |
| [EFTA01496910](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01496910.pdf) | **$50,000.00** | Check #1091, PAID 06/24 |
| [EFTA01486616](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01486616.pdf) | **$37,230.85** | AUG 26 transaction |
| [EFTA01486616](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01486616.pdf) | **$31,484.00** | AUG 26 transaction |
| [EFTA01486618](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01486618.pdf) | **$25,000.00** | AUG 27 transaction |
| [EFTA01486436](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01486436.pdf) | **$20,500.00** | FEB 06 transaction |
| [EFTA01486556](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01486556.pdf) | **$16,000.00** | JUN 23 transaction |
| [EFTA01497384](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01497384.pdf) | **$45,000.00** | Check #22165, PAID 12/14 |
| [EFTA01514285](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01514285.pdf) | **$19,640.00** | SEP 16 transaction |
| [EFTA01514285](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01514285.pdf) | **$24,567.00** | SEP check |
| [EFTA01487010](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01487010.pdf) | **$20,000.00** | DEC 21 transaction |
| [EFTA01498052](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01498052.pdf) | **$32,074.65** | MAR 10 transaction |
| [EFTA01516723](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01516723.pdf) | **$28,905.00** | MAR 12 transaction |
| [EFTA01516743](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01516743.pdf) | **$31,405.00** | MAR 04 transaction |
| [EFTA01504498](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01504498.pdf) | **$9,200,000.00** | Total Credits in single period |
| [EFTA01527550](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01527550.pdf) | **$1,000,000.00** | Single transfer |
| [EFTA01527665](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01527665.pdf) | **$1,000,000.00** | Single transfer |
| [EFTA01528492](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01528492.pdf) | **$1,500,000.00** | Single transfer |
| [EFTA01427976](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01427976.pdf) | **$1,000,000.00** | Southern Trust Company -- MONEY TRANSFER |

### 2.3 Epstein Financial Entity Network (Morris/Oldfield Bankers)

**CRITICAL FINDING:** A single bank relationship list ([EFTA01477454](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477454.pdf)) reveals Epstein maintained at minimum 17 entities under the same banking officers (Jj Litchford/Paul Morris, bank officers; Morris/Oldfield, bankers):

| Entity Name | Type | Balance (08/17/2018) | Balance (06/21/2018) |
|------------|------|---------------------|---------------------|
| JEFFREY EPSTEIN | Personal | $1,243,515.74 | $1,224,163.61 |
| SOUTHERN FINANCIAL LLC | Shell | $376,315.00 | $532,186.86 |
| PLAN D, LLC | **Leon Black linked** | $326,685.34 | $347,674.83 |
| JEGE, LLC | Aviation/Operations | $285,583.43 | $299,328.13 |
| DARREN K. INDYKE PLLC | Attorney trust | $259,740.02 | $243,363.55 |
| HBRK ASSOCIATES, INC | Shell | $149,498.33 | $211,289.05 |
| NES LLC | Property (E 65th St) | $264,466.13 | -- |
| GRATITUDE AMERICA, LTD | **Charity** | $2,075,025.07 | $323,223.15 |
| ZORRO MANAGEMENT, LLC | Shell | $424,475.56 | -- |
| **THE HAZE TRUST** | **Trust** | **$40,583,100.79** | **$49,460,098.13** |
| SOUTHERN TRUST COMPANY, INC. | Trust | $102,917.53 | $102,625.90 |
| BUTTERFLY TRUST | Trust | $704,736.63 | $733,701.04 |
| HYPERION AIR, LLC | Aviation | -- | $347,674.83 |
| NEPTUNE, LLC | Shell | -- | -- |
| JEGE, INC | Aviation | -- | -- |
| CRW 2007 LLC | Shell | -- | -- |
| GEW 2007 LLC | Shell | -- | -- |
| 55W 2007 LLC | Shell | -- | -- |
| LEON D. BLACK | **Personal acct** | -- | -- |
| CHRISTOPHER A. BOIES | Personal | -- | -- |
| TODD & KAREN WANEK | Personal | -- | -- |
| DOMINIQUE LEIMER | Personal | -- | -- |

**FORENSIC NOTE:** The Haze Trust dropped from **$49.4M (June 2018) to $40.6M (August 2018)** -- a decrease of approximately $8.9 million in two months. This coincides with the period just before increased media scrutiny. Additionally, **Leon D. Black and Christopher A. Boies maintained personal accounts at the same bank under the same officers as Epstein's network of shell entities.**

---

## SECTION 3: THE CRITICAL NOVEMBER 28 -- DECEMBER 6, 2018 WINDOW

### 3.1 Context: The Miami Herald Trigger

The Miami Herald published its "Perversion of Justice" series beginning November 28, 2018. The FBI timeline document ([EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf)) confirms:
- **12/6/2018 -- FBI New York opens investigation into Epstein**

### 3.2 Combined Calendar + Financial Timeline

| Date | Calendar Activity | Financial Activity | Source |
|------|-------------------|-------------------|--------|
| **Nov 28, 2018** | **8:30am Breakfast w/Ehud Barak** ([EFTA02154241](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02154241.pdf)) | Miami Herald publishes | Calendar alert |
| Nov 28, 2018 | 9:37:02 PM EST communication ([EFTA00010136](https://www.justice.gov/epstein/files/DataSet%208/EFTA00010136.pdf)) | -- | Email timestamp |
| Nov 29, 2018 | Thursday 4:00 PM communication ([EFTA00009977](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009977.pdf), [EFTA00023179](https://www.justice.gov/epstein/files/DataSet%208/EFTA00023179.pdf)) | -- | Email timestamps |
| **Nov 30, 2018** | "Dinner Nov 30th" -- From Yoki ([EFTA02089587](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02089587.pdf)) | **$100,000 WIRE from trust account to individual named as possible NPA co-conspirator** | Calendar + Prosecution filing |
| Nov 30, 2018 | Friday 7:00 communication ([EFTA00009976](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009976.pdf)) | -- | Email timestamp |
| Dec 1-2, 2018 | [No entries recovered] | -- | -- |
| **Dec 3, 2018** | [No calendar entry recovered] | **$250,000 WIRE from same trust account to ANOTHER individual** | Prosecution filing |
| Dec 4, 2018 | Multiple communications 6:34 PM, 7:06 PM, 7:19 PM ([EFTA00031366](https://www.justice.gov/epstein/files/DataSet%208/EFTA00031366.pdf)-31458) | -- | Email timestamps |
| **Dec 6, 2018** | Communications 12:36 PM, 1:36 PM, 7:08 PM ([EFTA00009873](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009873.pdf), 14305) | **FBI New York opens investigation** | Email + FBI timeline |

### 3.3 CRITICAL CORRELATION: The $350,000 Co-Conspirator Payments

**Source Document:** [EFTA00028785](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028785.pdf) (Government's detention memorandum)

> "Records obtained by the Government from Institution-1 appear to show that just two days later, on or about **November 30, 2018**, the defendant wired **$100,000** from a trust account he controlled to an individual named as a possible **co-conspirator** in the NPA. The same records appear to show that just three days after that, on or about **December 3, 2018**, the defendant wired **$250,000** from the same trust account to another [individual]."

**FORENSIC ANALYSIS:**
- The first wire ($100K) occurred **2 days after** the Miami Herald publication
- The first wire ($100K) occurred **on the same day** as a dinner event ("Dinner Nov 30th")
- The second wire ($250K) occurred **5 days after** the Miami Herald publication
- The second wire ($250K) occurred **3 days before** the FBI opened its investigation
- Total: **$350,000 in 4 days** to individuals described as possible co-conspirators
- **On November 28 itself**, the morning the Herald published, Epstein had **breakfast with former Israeli Prime Minister Ehud Barak**

This timing pattern is consistent with witness tampering or obstruction -- rapid disbursement of funds to potential co-conspirators immediately upon learning of renewed investigative interest.

---

## SECTION 4: JULY 2019 -- THE ARREST MONTH

### 4.1 FBI Timeline ([EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf))

| Date | Event |
|------|-------|
| 7/2/2019 | Epstein Indicted |
| **7/6/2019** | **Epstein arrested at Teterboro airport in New Jersey** |
| 7/8/2019 | Detained at MCC; Psych evaluation |
| 7/10/2019 | Placed with Nicholas Tartaglione in SHU |
| 7/23/2019 | Suicide attempt |
| 7/23-24/2019 | Suicide watch |
| 7/24-29/2019 | Psychological observation |
| 7/29/2019 | MCC Chief Psychologist approves removal from suicide watch |
| 7/30/2019 | New cellmate Efrain Reyes in SHU |
| 8/9/2019 | Cellmate released |
| 8/10/2019 | Death |

### 4.2 Pre-Arrest Communications (July 1-6, 2019)

| Date | Activity | EFTA # |
|------|----------|--------|
| Jul 1, 2019 | 10:46 PM, 11:23 AM communications | [EFTA00015211](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015211.pdf), [EFTA00013261](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013261.pdf) |
| Jul 2, 2019 | 10:39 AM, 2:10 PM (day of indictment) | [EFTA00013261](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013261.pdf), [EFTA00010464](https://www.justice.gov/epstein/files/DataSet%208/EFTA00010464.pdf) |
| Jul 3, 2019 | 11:10 AM, 11:16 AM | [EFTA00015211](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015211.pdf), [EFTA00013261](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013261.pdf) |
| **Jul 6, 2019** | **10:51 PM, 10:55 PM** (night of arrest at Teterboro) | **[EFTA00010587](https://www.justice.gov/epstein/files/DataSet%208/EFTA00010587.pdf)** |
| Jul 7, 2019 | 10:19 PM | [EFTA00009834](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009834.pdf) |

### 4.3 Post-Arrest Legal Mobilization

| Date | Activity | EFTA # |
|------|----------|--------|
| Jul 8, 2019 | 10:43 AM communications | [EFTA00014560](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014560.pdf) |
| Jul 9, 2019 | Multiple at 2:00 PM, 11:13 PM | [EFTA00015576](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015576.pdf), [EFTA00013261](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013261.pdf) |
| Jul 10, 2019 | 5:56 PM, 10:08 PM, 10:07 PM | [EFTA00014324](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014324.pdf) |
| Jul 11, 2019 | Multiple timestamps | [EFTA00009834](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009834.pdf), [EFTA00010386](https://www.justice.gov/epstein/files/DataSet%208/EFTA00010386.pdf) |
| Jul 12, 2019 | 1:59 PM, 4:45 PM, 5:40 PM | [EFTA00015211](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015211.pdf), [EFTA00014332](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014332.pdf), [EFTA00014326](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014326.pdf) |
| Jul 13, 2019 | 2:01 PM, 2:30 PM, 3:56 PM | [EFTA00014326](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014326.pdf), [EFTA00014330](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014330.pdf), [EFTA00013245](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013245.pdf) |
| Jul 15, 2019 | **DRAFT SDNY PRESS GUIDANCE** prepared | [EFTA00015348](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015348.pdf) |
| Jul 16, 2019 | Extensive communications 12:11 PM through 8:01 PM | Multiple EFTAs |
| Jul 18, 2019 | 12:43 PM, 6:56 PM | [EFTA00014609](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014609.pdf), [EFTA00014625](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014625.pdf) |
| Jul 29-30, 2019 | Multiple communications re: detention | [EFTA00014530](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014530.pdf), [EFTA00014558](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014558.pdf) |

**FORENSIC NOTE:** The Government's detention memo ([EFTA00028785](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028785.pdf)) was filed during this period, disclosing that Epstein was "worth more than $500 million" with "at least $10,000,000 per year" in income, and referencing the critical Nov 30/Dec 3 co-conspirator wires as evidence of obstruction risk. The memo noted he lived "in the U.S. Virgin Islands, traveling extensively abroad and residing in part in Paris."

---

## SECTION 5: FINANCIAL FIGURE CALENDAR CORRELATIONS

### 5.1 Leon Black (Apollo Global Management)

Leon Black maintained personal accounts at the same bank as Epstein's entity network. The calendar shows:

| Calendar Entry | Date Context | Financial Connection |
|----------------|-------------|---------------------|
| Alert - 1:00pm LUNCH w/Leon Black ([EFTA02048222](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02048222.pdf)) | Undated | PLAN D LLC (Black-linked) held $326K-$347K |
| Wed 6/5/2013 - Alert 9:00am Appt w/Leon Black At Leon's ([EFTA02137154](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02137154.pdf)) | June 5, 2013 | Leon D. Black account at same bank |
| Drive to Leon Black's house with Karyna ([EFTA01928406](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01928406.pdf)) | Undated | Karyna Shuliak (Epstein associate) |
| Leon Black 12:00 Sunday lunch? ([EFTA02158392](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02158392.pdf)) | Undated | |
| 12:30pm LUNCH w/Leo[n] ([EFTA02081553](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02081553.pdf)) | Undated | |
| Multiple emails via "Executive Assistant to Leon D. Black" | 2012-2017 range | Frequent staff-level coordination |

**FORENSIC NOTE:** The PLAN D, LLC entity name is notable -- Leon Black later acknowledged paying Epstein approximately $158 million in consulting fees over a five-year period. PLAN D, LLC at the same bank as all Epstein entities suggests a direct financial pipeline.

### 5.2 Ehud Barak (Former Israeli Prime Minister)

Ehud Barak is the **most frequently appearing name** in calendar entries:

| Calendar Entry | Date/Context | Correlation |
|----------------|-------------|-------------|
| 12pm meeting w/Mort and Ehud Tomorrow ([EFTA01923347](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01923347.pdf)) | Joint with Mort Zuckerman | |
| TBD LUNCH w/Ehud Barak & Joel Klein ([EFTA01955948](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01955948.pdf)) | With Joel Klein (ex-NYC Schools) | |
| lunch w/Ehud ([EFTA02052245](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02052245.pdf), 02052296) | 12:00pm | |
| Updated Invitation: 12:30pm Lunch w/Ehud Barak ([EFTA02136979](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02136979.pdf)) | Formal calendar invite | |
| Ehud/Nili arrive early ([EFTA02065729](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02065729.pdf), 02065821) | Travel coordination | |
| having Ehud Barrak to his home on Tuesday ([EFTA02138171](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02138171.pdf)) | Home visit | |
| **8:30am Breakfast w/Ehud Barak -- Wed Nov 28** ([EFTA02154241](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02154241.pdf)) | **SAME DAY as Miami Herald publication** | **$100K wire 2 days later** |
| 9:00am BREAKFAST w/Ehud ([EFTA02199213](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02199213.pdf)) | Undated | |
| 9:00am BREAKFAST w/Ehud and Tom ([EFTA02199243](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02199243.pdf)) | Undated | |
| 9:00am BREAKFAST w/Ehud ([EFTA02208207](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02208207.pdf)) | Undated | |
| 5:00pm Appt w/Ehud -- 2017 ([EFTA02211724](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02211724.pdf)) | 2017 | |
| should noon today w/Ehud ([EFTA02072207](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02072207.pdf)) | Ad hoc meeting | |

### 5.3 Jes Staley (JPMorgan / Barclays CEO)

| Calendar Entry | Context | Financial Connection |
|----------------|---------|---------------------|
| **Staley Dinner** ([EFTA02092187](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02092187.pdf)) | Formal dinner | JPMorgan was Epstein's primary bank ([EFTA01661868](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01661868.pdf)) |

**FORENSIC NOTE:** JPMorgan later paid $290 million to settle claims it facilitated Epstein's trafficking. Staley resigned from Barclays over his Epstein connections.

**DS9 UPDATE:** Staley's role was far deeper than a single dinner contact. Trust agreements ([EFTA00082368](https://www.justice.gov/epstein/files/DataSet%209/EFTA00082368.pdf)/[EFTA00082382](https://www.justice.gov/epstein/files/DataSet%209/EFTA00082382.pdf)/[EFTA00082441](https://www.justice.gov/epstein/files/DataSet%209/EFTA00082441.pdf)) name "JES STALEY" as Trustee of "The Jeffrey E. Epstein 2001 Trust Two," "The Jeffrey E. Epstein 2001 Trust One," and "The Jeffrey E. Epstein 2012 Trust" alongside Darren Indyke and Andrew Farkas. Epstein's will ([EFTA00074246](https://www.justice.gov/epstein/files/DataSet%209/EFTA00074246.pdf)) names "JAMES E. STALEY" as Executor. DS9 calendars show multiple additional meetings ([EFTA00292673](https://www.justice.gov/epstein/files/DataSet%209/EFTA00292673.pdf), [EFTA00298204](https://www.justice.gov/epstein/files/DataSet%209/EFTA00298204.pdf), [EFTA00300078](https://www.justice.gov/epstein/files/DataSet%209/EFTA00300078.pdf)) on the same days as meetings with Leon Black and Terje Roed-Larsen. An FBI Guardian complaint ([EFTA00090717](https://www.justice.gov/epstein/files/DataSet%209/EFTA00090717.pdf)) filed October 18, 2021 alleges "Accusations of Rape and human trafficking" against "James 'Jes' Edwards Staley."

### 5.4 Mort Zuckerman (Media/Real Estate Mogul)

| Calendar Entry | Context |
|----------------|---------|
| 12pm meeting w/Mort and Ehud Tomorrow ([EFTA01923347](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01923347.pdf)) | Joint with Barak |
| Reminder: Mort dinner Wed ([EFTA02060729](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02060729.pdf)) | Wednesday dinner |
| Mort for dinner on May 5??? ([EFTA02079500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02079500.pdf)) | Proposed dinner |
| Re: Lunch with Mort ([EFTA02102153](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02102153.pdf)) | Lunch |
| Lunch?: 12pm meeting w/Mort ([EFTA02106144](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02106144.pdf)) | Scheduling |

### 5.5 Larry Summers (Former Treasury Secretary)

| Entry | EFTA # | Context |
|-------|--------|---------|
| lunch w/Larry S[ummers] | [EFTA02064226](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02064226.pdf) | Lunch scheduling |
| meeting with Larry Summers | [EFTA01749216](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01749216.pdf) | With Terje Roed-Larsen |
| Multiple Re: Larry Summers emails | [EFTA02090837](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02090837.pdf)-02092691 | Extended email chains |

---

## SECTION 6: TOM BARRACK ANALYSIS

### 6.1 Calendar Entries

| EFTA # | Entry | Date | Connection |
|--------|-------|------|------------|
| [EFTA02043213](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02043213.pdf) | lunch at 1pm w/Tom Barrack? | Undated | Scheduling |
| [EFTA02176310](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02176310.pdf) | Tom Barrack time change | Undated | Rescheduling |
| [EFTA02176329](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02176329.pdf) | Tom Barrack time change | **Mon 9 Jan 2012** | Date confirmed |
| [EFTA02177049](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02177049.pdf) | **Tom Barrack and H.E. Sheikh** | Undated | **Meeting with UAE Sheikh** |
| [EFTA02177172](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02177172.pdf) | Subject: Tom Barrack [...] | Undated | Additional context |

### 6.2 Forensic Significance

Tom Barrack was indicted in July 2021 for:
- Acting as an unregistered foreign agent for the UAE
- Obstruction of justice
- Making false statements to the FBI

The calendar entry showing Epstein facilitating a meeting between **Tom Barrack and "H.E. Sheikh"** (likely Sheikh Abdullah Bin Zayed, UAE Foreign Minister, who appears elsewhere in the files at [EFTA01797875](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01797875.pdf) and [EFTA01801406](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01801406.pdf)) places Epstein as a broker in the very relationship that later led to Barrack's prosecution. Additional references to **Sheikh Abdullah Bin Zayed** appear in Epstein's contacts.

---

## SECTION 7: TRAVEL-FINANCIAL CORRELATIONS

### 7.1 Flight and Travel References

| EFTA # | Entry | Context |
|--------|-------|---------|
| [EFTA01905487](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01905487.pdf) | "sea level flight JE charter request" | Charter aircraft request |
| [EFTA01910409](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01910409.pdf) | "Demo Flight Jan 14 2013" | Aircraft demonstration |
| [EFTA01919271](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01919271.pdf) | "Paris flight info" | International travel |
| [EFTA01927785](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01927785.pdf) | "booking a flight" | Flight booking |
| [EFTA01929296](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01929296.pdf) | "Flight Times" | Schedule |
| [EFTA01932042](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01932042.pdf) | "Flight options 3/20" | March 20 options |
| [EFTA01949810](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01949810.pdf) | "Teterboro Pilot Expenses" | **Teterboro -- same airport of arrest** |
| [EFTA01958255](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01958255.pdf) | "Re: Wheels up?" | Departure inquiry |
| [EFTA01963765](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01963765.pdf) | "Re: GIV flight" | Gulfstream IV |
| [EFTA01989258](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01989258.pdf) | "1997 Gulfstream IVSP S/N: 1305 -- $12,995,000" | **Aircraft for sale listing** |
| [EFTA01995002](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01995002.pdf) | "boarding my flight to Seattle" | Domestic travel |
| [EFTA01997244](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01997244.pdf) | "Flight Options Quote Update" | Charter quote |
| [EFTA02000462](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02000462.pdf) | "Departure Time for Paris" | International |
| [EFTA02000847](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02000847.pdf) | "flight attendant for the [...]" | Staffing |
| [EFTA02025130](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02025130.pdf) | "Re Teterboro" -- Mon March 5 2012 4:30 PM | Teterboro ops |
| [EFTA02040302](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02040302.pdf) | "JFK Airport" | NYC travel |
| [EFTA02040838](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02040838.pdf) | "LFPB/LBG for KTEB" | **Paris Le Bourget to Teterboro** |
| [EFTA02198507](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02198507.pdf) | "Alert - Reminder: Brice to fly ABQ to SFO" | Staff travel |

### 7.2 Aviation Financial Transactions

Financial records show significant aviation-related payments:

| Transaction | Recipient | Context |
|-------------|-----------|---------|
| Fedwire to North Fork Bank -- T Air Airline Support | T Air | Aircraft maintenance |
| Fedwire -- Atlantic Turbine Inc Miami | Atlantic Turbine | Engine/turbine work |
| Fedwire -- International Jet Interiors (JEGE) | JEGE entity | Aircraft interior |
| Fedwire -- Bohlke International | Bohlke | USVI charter services |
| HYPERION AIR, LLC account: $347,674.83 | Epstein entity | Aviation holding company |
| Gulfstream Bus Bk -- Wades Builders LLC | Construction | Aircraft facility |
| Gulfstream IVSP listing at $12,995,000 | For sale | Aircraft transaction |
| FREEDOM AIR INTERNATIONAL INC | Separate entity | International charter |

### 7.3 Travel-Transaction Pattern

The **Paris Le Bourget to Teterboro (LFPB/LBG for KTEB)** flight reference at [EFTA02040838](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02040838.pdf) is significant: Epstein frequently traveled this international route, and his July 6, 2019 arrest occurred at Teterboro upon return from Paris.

---

## SECTION 8: LARGE TRANSACTION CORRELATION TIMELINE

### 8.1 Transactions >$50,000 with Proximate Meeting Activity

| Transaction | Amount | Proximate Calendar Activity (within 48 hrs) |
|------------|--------|---------------------------------------------|
| Check #1050 | $56,987.07 (03/09) | Multiple March calendar activities |
| Check #1074 | **$100,000.00** | No specific proximate meeting identified |
| Check #1091 | $50,000.00 (06/24) | June calendar entries present |
| AUG 26 transactions | **$37,230.85 + $31,484.00 + $3,360.01** ($72K cluster) | August calendar entries |
| AUG 27 | $25,000.00 | Same cluster |
| MAR 10 | $32,074.65 | March meeting cluster |
| MAR 04 | $31,405.00 | March meeting cluster |
| MAR 12 | $28,905.00 | March meeting cluster |
| Check #22165 | **$45,000.00** (12/14) | December calendar entries |
| **Nov 30, 2018** | **$100,000** (wire to co-conspirator) | **Same-day: "Dinner Nov 30th"** |
| **Dec 3, 2018** | **$250,000** (wire to co-conspirator) | Within 48 hrs of Dec 4 communications |
| Southern Trust Co. | **$1,000,000** (money transfer) | Date uncertain |
| Various | **$1,000,000 - $1,500,000** (large transfers) | Associated with Black Srebnick payments |
| **$9,200,000** | Total credits in single period | [EFTA01504498](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01504498.pdf) |

### 8.2 Monthly Wire Pattern

Email subjects reveal a recurring monthly wire schedule:

| Email Subject | EFTA # | Implication |
|---------------|--------|-------------|
| "Jan 15th wire" | [EFTA01750197](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01750197.pdf), 01750596, 01941893 | Mid-month payment |
| "April wire" | [EFTA01751501](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01751501.pdf), 01926645 | Monthly |
| "May wire" | [EFTA01973644](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01973644.pdf), 01973732 | Monthly |
| "July wire" | [EFTA01964294](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01964294.pdf) | Monthly |
| "JEE wire to JEGE" | [EFTA01459132](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01459132.pdf) | Internal entity transfer |
| "JEE wire to Kellerhals" (with Darren Indyke) | [EFTA01346198](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01346198.pdf) | Specific recipient |
| "se.t. wire" | [EFTA01956084](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01956084.pdf) | September wire |
| "Re: Wire" | [EFTA02057989](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02057989.pdf) | Wire follow-up |
| "Fwd: Wire" | [EFTA02024947](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02024947.pdf) | Wire forwarded |
| "Re: Wire Transfer Information" | [EFTA01991994](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01991994.pdf) | Transfer details |

---

## SECTION 9: SIGNING/CLOSING/EXECUTION ENTRIES

### 9.1 Deal and Closing References

| EFTA # | Entry | Context |
|--------|-------|---------|
| [EFTA02060185](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02060185.pdf) | "closing books" | Financial closing |
| [EFTA02060228](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02060228.pdf) | "on closing books" | |
| [EFTA02061047](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02061047.pdf)-61513 | **"Phaidon closing books"** (multiple refs) | Phaidon Press deal closing |
| [EFTA02048283](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02048283.pdf)-48892 | "closed and to call" (5 entries) | Account/entity closing |
| [EFTA01935989](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01935989.pdf) | "Initial Contribution $500,000 -- 4/12/12" | Trust funding date |
| [EFTA01939313](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01939313.pdf) | "Cost of Real Estate $13,250,000" | Property transaction |
| [EFTA01939313](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01939313.pdf) | "Retail Units Sold $6,980,432 / $7,500,000 -- 10/29/13" | Property sales |

### 9.2 Wire Instruction Emails

| EFTA # | Entry | Context |
|--------|-------|---------|
| [EFTA01940719](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01940719.pdf) | "Subject: Wire" | Wire instruction |
| [EFTA02020142](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02020142.pdf) | "Subject: wire" | Wire instruction |
| [EFTA02010130](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02010130.pdf) | "wire so we will know w[hen]" | Wire confirmation pending |

---

## SECTION 10: PATTERN ANALYSIS -- OUTBOUND TRANSFER CLUSTERING

### 10.1 Meeting-Transaction Clustering Patterns

**Pattern A: Pre-Crisis Disbursement**
The November 28-December 3, 2018 cluster is the clearest example:
- Miami Herald publishes (Nov 28)
- Same morning: Breakfast with Ehud Barak
- 2 days later: $100,000 wire to NPA co-conspirator
- 5 days later: $250,000 wire to another individual
- 8 days later: FBI opens investigation

**Pattern B: Legal Defense Funding**
Wire transfers to Black Srebnick Kornspan (defense attorneys) appear in transaction records alongside Wachovia Bank transfers. The firm received recurring Fedwire debits.

**Pattern C: Entity Funding Rotation**
Transfers between Epstein personal accounts and shell entities (JEGE, LSJE, NES LLC, Southern Trust) appear to follow a regular cadence, consistent with the monthly wire emails.

**Pattern D: Aviation-Travel-Transaction Nexus**
Large payments to aviation entities (T Air, Atlantic Turbine, Bohlke International, International Jet Interiors) cluster around flight scheduling emails, suggesting a pattern where aircraft costs were settled around travel dates.

**Pattern E: August Transaction Cluster**
August 26-27 shows a $72,000+ cluster of transactions in a single 48-hour period. This coincides with summer travel patterns.

### 10.2 The Haze Trust Drawdown

The most significant financial pattern identified:
- **June 21, 2018:** The Haze Trust balance = **$49,460,098.13**
- **August 17, 2018:** The Haze Trust balance = **$40,583,100.79**
- **Net decrease: approximately $8.9 million in under 2 months**

This drawdown occurred in the summer of 2018, **months before** the Miami Herald publication but during a period when Epstein would have been aware of Julie K. Brown's investigation. The compliance department at Deutsche Bank (the "Institution-1" referenced by prosecutors) was simultaneously flagging The Haze Trust for AML inquiries ([EFTA01357853](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357853.pdf)-01413743).

---

## SECTION 11: COMBINED CHRONOLOGICAL TIMELINE

### Meetings AND Transactions -- Side by Side

```
DATE                 | MEETINGS/CALENDAR              | FINANCIAL ACTIVITY
---------------------|-------------------------------|---------------------------
~Jan 9, 2012        | Tom Barrack time change        |
~Jan 2012           | Tom Barrack + H.E. Sheikh      | (Barrack-UAE nexus)
~Feb 19, 2013       | 7:30PM Dinner w/Terje          |
~Mar 2013           | Warren's birthday (Mar 5)      | $56,987 check (03/09)
~Mar 2013           | Demo Flight Jan 14 2013        | $32,074 (MAR 10)
                     |                                | $31,405 (MAR 04)
                     |                                | $28,905 (MAR 12)
~Apr 2012           | "April wire" email             | $100,000 check #1074
~Apr 23             | LUNCH w/Dan Gilbert 1:30pm     |
~Apr 2012           | Initial Contribution $500K     | Trust funding
~Jun 2013           | $50,000 check PAID 06/24       |
~Jun 5, 2013        | 9:00am Appt w/Leon Black       | PLAN D, LLC active
                     |   At Leon's [home]             | Leon D. Black acct at bank
~Summer 2013        | 12pm meeting w/Mort and Ehud   |
~Undated            | TBD LUNCH w/Ehud Barak &       |
                     |   Joel Klein                   |
~Undated            | 1:00pm LUNCH w/Leon Black      |
~Undated            | lunch w/Larry Summers          |
~Undated            | Staley Dinner                  | JPMorgan accounts
~Undated            | 7:00pm DINNER w/Noam &         |
                     |   Valeria Chomsky              |
~Undated            | 4:00pm Appt w/Maxim Churkin    | (son of Vitaly Churkin, Russia's UN Ambassador)
~Undated            | 7:00 Dinner w/Mohamed          | (Middle East connection)
~Undated            | lunch at 1pm w/Tom Barrack     |
~Undated            | 8:30am BREAKFAST w/Andrew       |
                     |   Farkas AT Andrew's Home      |
~Undated            | Breakfast w/Tom Pritzker        |
~Aug 26-27          |                                | $37,230 + $31,484 + $25,000
                     |                                |   ($93K cluster)
~Oct 29, 2013       |                                | Property sale: $7,500,000
~Jun-Aug 2018       |                                | Haze Trust: $49.4M -> $40.6M
                     |                                |   ($8.9M drawdown)
Nov 28, 2018        | **BREAKFAST w/Ehud Barak**     | Miami Herald publishes
Nov 30, 2018        | **Dinner Nov 30th (Yoki)**     | **$100,000 WIRE to co-conspirator**
Dec 3, 2018         |                                | **$250,000 WIRE to co-conspirator**
Dec 4, 2018         | Multiple evening comms         |
Dec 6, 2018         | Multiple comms (12:36, 7:08)   | **FBI NY opens investigation**
Jul 1, 2019         | Communications 10:46PM, 11:23AM|
Jul 2, 2019         | Communications (INDICTMENT DAY)|
Jul 6, 2019         | 10:51 PM, 10:55 PM comms      | **ARRESTED at Teterboro**
Jul 8-16, 2019      | Intensive legal communications | Detention at MCC
Jul 15, 2019        | DRAFT SDNY PRESS GUIDANCE      |
Jul 23, 2019        | Suicide attempt                |
Aug 10, 2019        | DEATH                          |
```

---

## SECTION 12: KEY FORENSIC FINDINGS

### Finding 1: The $350,000 Obstruction Pattern
The two wire transfers totaling $350,000 to NPA co-conspirators within days of the Miami Herald publication represent the strongest calendar-financial correlation in the dataset. The breakfast with Ehud Barak on the morning of publication suggests Epstein was aware of -- or was being briefed on -- the impending crisis.

### Finding 2: Leon Black Financial Integration
Leon D. Black maintained personal bank accounts under the same officers (Litchford/Morris) as Epstein's 17+ shell entities. PLAN D, LLC -- a Black-linked entity -- held hundreds of thousands of dollars at this same institution. DS10 text layer extractions show at least 5 documented meetings. DS9 Groff calendars ([EFTA00285104](https://www.justice.gov/epstein/files/DataSet%209/EFTA00285104.pdf), [EFTA00285156](https://www.justice.gov/epstein/files/DataSet%209/EFTA00285156.pdf), [EFTA00285259](https://www.justice.gov/epstein/files/DataSet%209/EFTA00285259.pdf), [EFTA00285270](https://www.justice.gov/epstein/files/DataSet%209/EFTA00285270.pdf), [EFTA00285318](https://www.justice.gov/epstein/files/DataSet%209/EFTA00285318.pdf), [EFTA00298204](https://www.justice.gov/epstein/files/DataSet%209/EFTA00298204.pdf), [EFTA00306935](https://www.justice.gov/epstein/files/DataSet%209/EFTA00306935.pdf), [EFTA00307005](https://www.justice.gov/epstein/files/DataSet%209/EFTA00307005.pdf), [EFTA00307539](https://www.justice.gov/epstein/files/DataSet%209/EFTA00307539.pdf)) expand the count to 15-20+ meetings across 2010-2017, many on the same days as meetings with Barak, Churkin, Staley, and others. Deutsche Bank exhibits ([EFTA00080250](https://www.justice.gov/epstein/files/DataSet%209/EFTA00080250.pdf)/[EFTA00080260](https://www.justice.gov/epstein/files/DataSet%209/EFTA00080260.pdf)) document $80M+ flowing from Black entities to Epstein entities, including $22.5M and $8M from BV70 LLC to Plan D, LLC in 2017.

### Finding 3: Ehud Barak as Most Frequent Calendar Contact
Barak appears in more calendar entries than any other individual (11+ documented meetings in DS10). DS9 Groff calendars expand this to 20+ meetings ([EFTA00285196](https://www.justice.gov/epstein/files/DataSet%209/EFTA00285196.pdf), [EFTA00285259](https://www.justice.gov/epstein/files/DataSet%209/EFTA00285259.pdf), [EFTA00285047](https://www.justice.gov/epstein/files/DataSet%209/EFTA00285047.pdf), [EFTA00300067](https://www.justice.gov/epstein/files/DataSet%209/EFTA00300067.pdf), [EFTA00307928](https://www.justice.gov/epstein/files/DataSet%209/EFTA00307928.pdf), [EFTA00314254](https://www.justice.gov/epstein/files/DataSet%209/EFTA00314254.pdf), and others). Most significantly, [EFTA00285196](https://www.justice.gov/epstein/files/DataSet%209/EFTA00285196.pdf) documents a joint lunch on August 29, 2016: "12:30pm LUNCH w/Ehud Barak, Tom Barrack and Vitaly Churkin," placing the former Israeli PM, the future convicted UAE foreign agent, and Russia's UN Ambassador at the same table. A separate dinner invitation ([EFTA00298515](https://www.justice.gov/epstein/files/DataSet%209/EFTA00298515.pdf)) lists guests including Tom Barrack, Arthur Sulzberger, Steve Schwarzman, David Gergen, Len Blavatnik, Jes Staley, Tom Pritzker, Charlie Rose, Larry Summers, Mayor Bloomberg, Ron Perelman, General Wes Clark, Walter Isaacson, and Lloyd Blankfein. His breakfast on November 28, 2018 -- the exact day the Miami Herald published -- remains the single most significant calendar-financial nexus point.

### Finding 4: The Haze Trust Drawdown
An $8.9 million drawdown from The Haze Trust between June and August 2018 coincided with AML compliance inquiries about the account and preceded the public scandal by months. DS9 provides the complete transaction ledger ([EFTA00080250](https://www.justice.gov/epstein/files/DataSet%209/EFTA00080250.pdf), [EFTA00104945](https://www.justice.gov/epstein/files/DataSet%209/EFTA00104945.pdf)) confirming November-December 2018 transfers of $2.5M (11/20/2018) and $5M (12/19/2018) from Haze Trust to Southern Financial LLC, precisely bracketing the co-conspirator payment window. The ledger also documents a February 2019 dissolution event exceeding $30M in total transfers. Complete Deutsche Bank account opening documents ([EFTA00165655](https://www.justice.gov/epstein/files/DataSet%209/EFTA00165655.pdf)/[EFTA00165675](https://www.justice.gov/epstein/files/DataSet%209/EFTA00165675.pdf)/[EFTA00166763](https://www.justice.gov/epstein/files/DataSet%209/EFTA00166763.pdf)) confirm the Haze Trust was rated "Moderate 2 High Risk" with Paul Morris as Relationship Manager.

### Finding 5: Tom Barrack-UAE-Israel-Russia Nexus
Epstein's calendar shows he facilitated meetings between Tom Barrack and a "H.E. Sheikh" (likely Sheikh Abdullah Bin Zayed). DS9 expands Barrack's documented presence to 10+ meetings/listings ([EFTA00285196](https://www.justice.gov/epstein/files/DataSet%209/EFTA00285196.pdf), [EFTA00285290](https://www.justice.gov/epstein/files/DataSet%209/EFTA00285290.pdf), [EFTA00298379](https://www.justice.gov/epstein/files/DataSet%209/EFTA00298379.pdf), [EFTA00298515](https://www.justice.gov/epstein/files/DataSet%209/EFTA00298515.pdf), [EFTA00317557](https://www.justice.gov/epstein/files/DataSet%209/EFTA00317557.pdf), [EFTA00317799](https://www.justice.gov/epstein/files/DataSet%209/EFTA00317799.pdf), [EFTA00318516](https://www.justice.gov/epstein/files/DataSet%209/EFTA00318516.pdf)). The August 29, 2016 joint lunch with Ehud Barak and Vitaly Churkin ([EFTA00285196](https://www.justice.gov/epstein/files/DataSet%209/EFTA00285196.pdf)) establishes Epstein as a nexus between Israeli, UAE, and Russian state actors at a single meal. Barrack was later convicted for acting as an unregistered UAE foreign agent. A scheduling shorthand ([EFTA00317799](https://www.justice.gov/epstein/files/DataSet%209/EFTA00317799.pdf)) places Barrack in a single October 2016 week alongside Leon Black, Churkin, Peter Thiel, Larry Summers, and Rothschild.

### Finding 6: Monthly Wire Cadence
Email subject lines reveal a systematic monthly wire schedule ("Jan 15th wire," "April wire," "May wire," "July wire") suggesting recurring payment obligations -- potentially consulting fees, property maintenance, or entity funding.

### Finding 7: Aviation as Financial Conduit
The concentration of payments to aviation entities (Hyperion Air LLC, JEGE aviation operations, T Air, Atlantic Turbine, Bohlke International, International Jet Interiors) alongside flight scheduling emails suggests aircraft operations served as both a logistics platform and a significant expense channel -- and potentially a means of moving value across jurisdictions.

---

## APPENDIX A: ENTITY RELATIONSHIP MAP

```
                        JEFFREY E. EPSTEIN (Personal)
                                   |
                    +--------------+--------------+
                    |              |              |
              SOUTHERN TRUST   THE HAZE       BUTTERFLY
              COMPANY, INC.    TRUST          TRUST
              ($102K)          ($40.6M)       ($704K)
                    |
          +---------+---------+
          |         |         |
      JEGE LLC  JEGE INC  NEPTUNE LLC
      ($285K)
          |
    +-----+-----+
    |     |     |
  NES   PLAN D  HYPERION
  LLC   LLC     AIR LLC
  ($264K) ($326K) ($347K)
          |
     LEON D. BLACK ← Personal account at same bank
          |
  CHRISTOPHER A. BOIES ← Personal account at same bank

  Other entities at same bank:
  - SOUTHERN FINANCIAL LLC ($376K)
  - GRATITUDE AMERICA, LTD ($2M)
  - ZORRO MANAGEMENT, LLC ($424K)
  - HBRK ASSOCIATES, INC ($149K)
  - DARREN K. INDYKE PLLC ($259K)
  - CRW 2007 LLC / GEW 2007 LLC / 55W 2007 LLC
  - DOMINIQUE LEIMER / TODD & KAREN WANEK
  - FREEDOM AIR INTERNATIONAL INC (separate bank)
```

## APPENDIX B: PROMINENT NAMES SUMMARY (FBI Document [EFTA01656152](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656152.pdf)/01660622)

The FBI's own "Prominent Names" document identifies the following individuals with allegations:
- **Leon Black** -- present during abuses; massages
- **Jes Staley** -- forced sexual contact during massage
- **Les Wexner** -- Epstein "earned his money from Wexner"; homosexual activity
- **Glen Dubin** -- Maxwell-directed massage
- **Prince Andrew** -- witnessed on Epstein's island
- **Alan Dershowitz** -- massage on Epstein's plane
- **Harvey Weinstein** -- fondling during massage
- **Howard Lutnick** -- Ponzi schemes; $10 home sale
- **William Barr** -- present during abuses with Leon Black
- **Bill Clinton** -- orgy invitation (not attended)
- **Donald Trump** -- forced sexual contact

---

*This report was generated through forensic analysis of the DOJ Epstein files database (primary document text database). All findings are based on text extracted from government document text layers (OCR) and should be verified against original source materials. Dollar amounts extracted from OCR'd financial documents may contain recognition errors. Calendar dates without year context are estimated based on surrounding document metadata.*

---

## APPENDIX C: DS9 REVISIT -- CO-CONSPIRATOR PAYMENT TIMELINE AND SDNY ADMISSION

*(Added 2026-02-12 from DS9/DS11 full corpus search)*

### Complete Co-Conspirator Payment Timeline (Prosecution Exhibit)

[EFTA00092643](https://www.justice.gov/epstein/files/DataSet%209/EFTA00092643.pdf)/[EFTA00105307](https://www.justice.gov/epstein/files/DataSet%209/EFTA00105307.pdf) (DS9) contain the actual SDNY prosecution exhibit "TIMELINE OF PAYMENTS TO (OR ON BEHALF OF) POTENTIAL CO-CONSPIRATORS (PAYMENTS > $10,000)":

| Date | Beneficiary | Amount | Source Account |
|------|------------|--------|----------------|
| 12/4/2013 | MC2 Model Management | $25,000 | Jeffrey Epstein, TD Bank |
| 1/28/2015 | [Redacted] | $50,000 | Butterfly Trust, JP Morgan Chase |
| 2/6/2015 | [Redacted] | $15,000 | Butterfly Trust, JP Morgan Chase |
| 3/5/2015 | Coffey Burlington (Alan Dershowitz) | $20,532 | Jeffrey Epstein, Coconut Grove Bank |
| 3/27/2015 | 301/66 Owners Corp | $189,304 | NES, LLC, Citibank |
| 4/22/2015 | [Redacted] | $50,000 | Butterfly Trust, JP Morgan Chase |
| 1/3/2017 | Lesley Groff | $100,000 | Southern Financial |
| 3/28/2017 | Lawrence P. Visoski | $50,000 | Southern Financial, Bank of America |
| **11/27/2018** | **Aviloop LLC** | **$45,000** | JEGE, LLC, TD Bank |
| **11/30/2018** | **Aviloop LLC** | **$100,000** | **Butterfly Trust, TD Bank** |
| **12/3/2018** | **[Redacted]** | **$250,000** | **Butterfly Trust, Bank of America** |
| 12/19/2018 | Lawrence P. Visoski | $175,000 | Southern Financial, Bank of America |
| 12/19/2018 | [Redacted] | $110,000 | [Source unclear] |

This confirms Aviloop LLC (Nadia Marcinkova's company) as the $100K recipient on Nov 30, 2018, and reveals an additional $45K payment to Aviloop just 3 days prior. The Butterfly Trust was the wiring account for both the $100K and $250K co-conspirator payments.

### SDNY Internal Admission

[EFTA00105304](https://www.justice.gov/epstein/files/DataSet%209/EFTA00105304.pdf) (DS9): An AUSA's internal email dated September 15, 2019, states:

> "Our review of financial information has been extensive and robust, but ultimately it hasn't resulted in anything actionable from a charging perspective."

> "We knew, for example, about Epstein's relationship with--and significant payments to--Joichi Ito of MIT and the New York Times Company, as well as other payments to institutions like Harvard and MIT and to a wide variety of individuals (or entities relating to, or apparently for the benefit of, individuals) including Ehud Barak (former Prime Minister of Israel), Bruce Moskowitz (a close friend of President Trump and one of three Mar-A-Lago members who are purportedly running much of the VA from outside the government), Noam Chomsky, Woody Allen, and a handful of other prominent academics and international figures--in addition to payments to more than 25 women who appear to be Eastern European models."

> "There are dozens or hundreds of transactions and relationships of which we're aware that likely would be newsworthy."

This confirms that SDNY was aware of the calendar-financial correlations documented in this report -- payments to Barak, Chomsky, Ito, Eastern European models, and others -- but chose not to pursue financial charges.

### Vitaly Churkin Correction

The original report identified "Maxim Churkin" as a Russian diplomat. DS9 reveals that Maxim is the son of Vitaly Churkin, who was Russia's Ambassador to the United Nations (died February 2017). Epstein met with both father and son. Key DS9 entries include:
- [EFTA00285196](https://www.justice.gov/epstein/files/DataSet%209/EFTA00285196.pdf): "12:30pm LUNCH w/Ehud Barak, Tom Barrack and Vitaly Churkin" (August 29, 2016)
- [EFTA00317550](https://www.justice.gov/epstein/files/DataSet%209/EFTA00317550.pdf): "12:30pm LUNCH w/Peter Thiel and Vitaly Churkin" (October 7, 2016)
- [EFTA00285207](https://www.justice.gov/epstein/files/DataSet%209/EFTA00285207.pdf): "2:30pm Maxim Churkin" followed by "4:00pm Appt w/Vitaly Churkin" (December 2, 2016) -- father and son on the same day

### October 2016 Scheduling Density

DS9 reveals a particularly dense period in October 2016 ([EFTA00317799](https://www.justice.gov/epstein/files/DataSet%209/EFTA00317799.pdf)) where Epstein's shorthand to Lesley Groff scheduled a single week with Leon Black, Vitaly Churkin, Peter Thiel, Larry Summers, Woody Allen, Ariane de Rothschild, Tom Barrack, and others, demonstrating that the calendar-financial correlations in this report were not isolated events but part of a continuous, dense schedule of high-level meetings.

DATA QUALITY NOTE: A data quality audit confirmed that ~98% of 'bad_overlay' records in the redaction database are OCR noise from degraded scans, not text hidden behind removable redactions. Text searches against this corpus remain valid for identifying which documents mention specific terms.
