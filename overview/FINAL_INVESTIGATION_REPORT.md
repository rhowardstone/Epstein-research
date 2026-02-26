# FINAL INVESTIGATION REPORT
# Forensic Analysis of the 218GB DOJ Jeffrey Epstein File Release

> **Context:** This report was compiled on February 7, 2026 during the first two weeks of the investigation. It synthesizes findings available at that time. The project has since produced **150+ investigation reports** across 16 categories — including financial forensics, grand jury subpoena analysis, individual investigations, and government official searches that are not reflected here. For the complete catalog, see the [full report index](https://epstein-data.com/reports/).

**Classification:** INVESTIGATIVE SUMMARY
**Date of Compilation:** February 7, 2026
**Investigation Period:** January-February 2026
**Corpus:** 218GB, 519,438 PDFs, 12 datasets
**Databases Created and Queried:**
- the primary document text database -- 1,808,942 redaction records
- the Dataset 10 document text database -- 1,629,776 redaction records
- the OCR text extraction database -- 38,955 OCR records
- the image catalog database -- 21,859 image records (26,721 analysis records)
- the entity relationship database -- 524 entities, 2,096 relationships
- the financial transaction database -- 186 normalized transactions, $755M total value

**Total EFTA Documents Cited in This Report:** 400+
**Total Individual Reports Produced During Investigation:** 150+

> **SOURCE NOTE:** All `DB-SDNY-#######` Bates numbers in this document are Deutsche Bank document production references from [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) (Exhibits A-E: master transaction tables compiled by SDNY from Deutsche Bank records).

---

# I. EXECUTIVE SUMMARY

## Scale of This Investigation

This report synthesizes a forensic investigation of the largest single document release in the history of the Jeffrey Epstein case. The Department of Justice released approximately 218 gigabytes of material comprising 519,438 individual PDF documents organized across 12 datasets. Six custom databases were constructed containing over 3.4 million indexed records, 21,859 cataloged images, and 186 normalized financial transactions totaling $755,632,579 in documented money flows.

The investigation searched across 1.8 million text records extracted from document text layers (see DATA QUALITY NOTE below), identified 12 documents where redaction tools failed entirely (exposing Apple Mail PLIST metadata), traced $30.5 million in art auction proceeds through a network of 95+ shell entities, documented $168 million in payments from Leon Black to Epstein, identified at minimum 60-80 individual victims (with estimates of 200+ and the US Virgin Islands describing "hundreds"), and cataloged evidence implicating over 30 named individuals ranging from billionaires and heads of state to federal law enforcement officials.

The investigation also discovered 460+ documents containing Apple Mail PLIST metadata spanning a 9-year window (2009-2018) from Epstein's Gmail account (jeevacation@gmail.com), correlated 420 email timestamps against known financial transaction dates to demonstrate that the densest communication clusters coincide precisely with the largest money movements, and cataloged the complete digital device forensic inventory of 70+ seized devices -- including the catastrophic processing failures that left a 2005 computer from the peak abuse period permanently unsearched and surveillance tapes permanently unscanned.

## Top 10 Most Significant Findings

**1. Leon Black Paid $168 Million to Epstein Through the Same Infrastructure That Funded Trafficking**
Fourteen separate wire transfers from five Black-controlled entities (Black Family Partners LP, Leon and Debra Black, BV70 LLC, Narrow Holdings LLC, Elysium Management) deposited $168 million into Southern Trust Company Inc. -- the same entity that funded Butterfly Trust (Epstein's trust — Maxwell was a beneficiary until late 2014 when she was removed and replaced by Shuliak and Indyke, per [EFTA01282297](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01282297.pdf)), Zorro Management (the New Mexico ranch where minors were abused), and Plan D LLC (the aircraft used to transport victims). The same Deutsche Bank officers -- Jj Litchford and Paul Morris -- managed both Black's personal account and every Epstein entity. Four or more victims describe violent sexual assaults by Black at Epstein's townhouse, with one independently corroborating his distinctive pattern of biting genitalia. A second victim contacted attorneys in August 2022 describing "almost a perfect match" of Black's violent sexual acts -- "nothing publicly out there about the details, so there is no way she could know" ([EFTA02731729](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731729.pdf)). FBI prosecution notes document a 16-year-old "violently raped by Black" with "adult sex toys in victim's rectum and vagina," victim bleeding, refused medical attention ([EFTA02731488](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731488.pdf)). Victim's direct text to Black: "You sexually harassed me, sex trafficked me, raped me, and eventually blacklisted me... forced to sign under duress" ([EFTA02731576](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731576.pdf)). Black paid $62.5 million to settle USVI claims but no criminal charges were ever filed. ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf), [EFTA02730996](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730996.pdf), [EFTA02731488](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731488.pdf), [EFTA02731576](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731576.pdf), [EFTA01359500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01359500.pdf))

**2. $189 Million Flowed Through Epstein Accounts After Deutsche Bank's Own Compliance Controls Failed**
On April 16, 2018, Deutsche Bank internally documented that "kyc is not happening" for Epstein's accounts ([EFTA01362456](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362456.pdf)). An AML alert was escalated with "URGENT - THIRD REQUEST!!!!!" ([EFTA01414241](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01414241.pdf)). A stop-wire was attempted on an LSJE transaction but the wire had already been processed ([EFTA01426081](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01426081.pdf)). Despite this documented cascade of control failures, 50 additional transactions totaling $189 million continued flowing through Epstein's accounts. These included $33 million to Honeycomb Partners, $5.75 million to Peter Thiel's Valar Fund, $2 million to Coatue Enterprises, and $24.5 million in the February 2019 dissolution event -- all processed by the same compliance-flagged banking relationship under RM CODE 82289. The same two bankers -- Jj Litchford (primary) and Paul Morris (secondary) -- who managed Epstein's accounts also managed Leon Black's personal accounts, Christopher Boies's accounts, and Todd Wanek's accounts (Ashley Furniture CEO) under what Deutsche Bank called the "Third Lake Capital Relationship" ([EFTA01477330](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477330.pdf)). Deutsche Bank ultimately paid $150 million in penalties to the New York Department of Financial Services. ([EFTA01362456](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362456.pdf), [EFTA01414241](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01414241.pdf), [EFTA01406955](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406955.pdf), [EFTA01431221](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01431221.pdf), [EFTA01426081](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01426081.pdf), [EFTA01477330](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477330.pdf))

**3. CSAM Was Found on Epstein's Devices -- Then Found Again in 2023, Demonstrating Initial Processing Missed It**
The FBI CID summary (approved July 17, 2024) confirmed "a small number of CSAM images found on one of Epstein's devices" ([EFTA00038617](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038617.pdf)). A CD labeled "girl pics nude book 4" was cataloged in the evidence ([EFTA02730741](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730741.pdf)). "Nudes 1" and "Girl pics nude" were found in Epstein's locked safe, some appearing to depict underage individuals ([EFTA00024584](https://www.justice.gov/epstein/files/DataSet%208/EFTA00024584.pdf)). Separately, during 2023 estate settlement processing, additional child sexual abuse material was discovered ([EFTA00039019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00039019.pdf)) -- material that should have been found during the initial 2019-2021 evidence review but was missed due to the catastrophic dysfunction documented across 17 months of evidence handling failures. The FBI examiner was reduced to one day per week during COVID ("things have been stretched out by a factor of 5"). 71,000+ zero-byte files were produced in the initial extraction. Six machines remained unexported as of October 2020. Two server drives physically failed and were sent to FBI HQ for recovery -- outcome unknown. The AUSA handling the case wrote: "Notwithstanding their many promises to us about quick and effective processing of the 60+ devices they seized, the FBI is completely fucking us on this" ([EFTA00009941](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009941.pdf)). Approximately 2,100 nude/partially nude images and videos were compiled from 14 separate devices onto a single portable hard drive in January 2021 ([EFTA00020974](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020974.pdf)).

**4. Documented Surveillance Infrastructure Raises Questions About the FBI's Claim of "No Cameras in Bedrooms or Massage Rooms"**
The Maxwell prosecution memo explicitly states "Epstein had cameras in his clock" ([EFTA02731226](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731226.pdf)). A 2003 Palm Beach police report documents Epstein purchasing a spy camera, concealing it in a clock in his office, and monitoring footage on his computer hard drive — though this was in the context of catching a household employee stealing from a briefcase, not sexual abuse surveillance ([EFTA00029761](https://www.justice.gov/epstein/files/DataSet%208/EFTA00029761.pdf)). FBI evidence photos show a multi-monitor surveillance control room at 9 East 71st Street ([EFTA00000015](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000015.pdf)-17) and "24 HOUR VIDEO SURVEILLANCE" signs on multiple doors. The FBI CID summary (approved 7/17/2024) states "contrary to some news reports, these searches did not reveal any cameras in any of the bedrooms or massage rooms" ([EFTA00038617](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038617.pdf)) — notably, this claim is limited to bedrooms and massage rooms, not a blanket denial of cameras on the properties. Professional surveillance VHS tapes (Maxell T-160, "Ideal for use in Time Lapse Recording") were seized from Epstein's properties but were marked "ITEM WAS NOT SCANNED" -- their contents have never been reviewed ([EFTA00007741](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007741.pdf), [EFTA00007984](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007984.pdf), [EFTA00007987](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007987.pdf), [EFTA00007990](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007990.pdf)). Attorneys David Boies and Stan Pottinger planned to use Epstein's "illicit videos" to obtain "multi-million-dollar settlements from the wealthy men" -- described by prosecutors as "conspiracy to commit extortion" ([EFTA00032751](https://www.justice.gov/epstein/files/DataSet%208/EFTA00032751.pdf)). This indicates the existence of compromising video material -- attorneys were willing to attempt monetization of it.

**5. The MCC DVR System Failed 12 Days Before Epstein's Death; Replacement Drives Were Obtained But Never Installed**
The Metropolitan Correctional Center had 192 cameras with 128 assigned to recording, split across two DVR systems of 16 hard drives each. Three of four camera angles covering Epstein's Special Housing Unit tier were recorded on DVR 2, which suffered "catastrophic disk failures" on July 29, 2019 -- 12 days before death. Epstein was transferred back to the SHU on July 30. Additional hard drives failed on August 8, two days before death. The failure was first detected by MCC staff on August 8. MCC obtained replacement hard drives on August 9 but never completed the installation. At 6:30 AM on August 10, Epstein was found dead. Hard drives were seized from DVR 2 at 4:30 PM. The DVR system was shipped to FBI Digital Forensics Analysis Unit in Quantico, Virginia on August 16. According to the FBI forensic reports, DVR 2 "did not start successfully." An FBI Advanced Data Recovery Specialist repaired three faulty drives but "the DVR was never able to be assembled successfully." Controller logs confirmed "catastrophic disk failures" and "no recordings would have been available after July 29, 2019" ([EFTA01649190](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01649190.pdf), [EFTA00039025](https://www.justice.gov/epstein/files/DataSet%209/EFTA00039025.pdf)). DVR 1, covering the remaining single camera angle, was operational and showed no one entering Epstein's tier during the critical hours -- but 75% of camera coverage was absent. The sally port camera covering the elevator bank was on DVR 2 and therefore also non-functional.

**6. A Complete Forensic Image of Epstein's 2005 Computer -- From the Peak Abuse Period -- Was Never Examined by Federal Authorities**
Sixteen DVD-R discs containing a Palm Beach County Sheriff's Office EnCase forensic image of a computer seized from Epstein's residence circa 2005 -- the peak period of documented abuse involving dozens of minor victims -- were found in the FBI Florida Office's file ([EFTA00015823](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015823.pdf)). Each disc was labeled "Disk 1 of 16" through "Disk 16 of 16," with the description "Palm Beach County Sheriff's Office Case # 05-250067 Epstein EnCase Files Palm Beach PD DVD-R for General VERBATIM DVD Computer Crimes Unit." FBI New York initially could not open the files and believed them inoperable. They later confirmed the files were "consistent with a forensic image of a computer." The 2005 search warrant authorized seizure but not searching of electronic device contents. No subsequent federal warrant was ever obtained. The Government stated it had "no lawful basis to review" the image and "did not intend to obtain a warrant." The Government could not permit defense to review the contents either. Epstein's estate was "repeatedly unwilling to waive any attorney-client privileges" regarding devices. The forensic image has never been examined by federal authorities. (Note: The Palm Beach County Sheriff's Office Computer Crimes Unit created the EnCase image, and it is possible that local authorities conducted some examination of the original computer, including in connection with a 2006 grand jury proceeding — but this is not addressed in the available federal documents.)

**7. Epstein's Intelligence Connections Are Documented but Systematically Uninvestigated**
While under Florida criminal charges in 2008, Epstein toured Israeli military bases with Friends of Israel chairman Benny Shabtai ([EFTA00013730](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013730.pdf)). The building at 301 East 66th Street simultaneously housed an apartment for former Israeli Prime Minister Ehud Barak (cleaned by Epstein's staff on Epstein's direct orders, [EFTA02278459](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02278459.pdf)), MC2 model apartments (confirmed by FBI DAS search generating 2,000+ records, [EFTA00019513](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019513.pdf)), trafficking victims ([EFTA00025109](https://www.justice.gov/epstein/files/DataSet%208/EFTA00025109.pdf)), a guest apartment "2G," Epstein corporate entities in Suite 10F ([EFTA02533859](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02533859.pdf)), and Karyna Shuliak's residence with partial SSN ([EFTA01378419](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01378419.pdf)). IDF-branded clothing — an IDF sweatshirt ([EFTA00001970](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001970.pdf)) and an "ISRAEL DEFENSE FORCES" T-shirt with Hebrew text ([EFTA00001971](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001971.pdf)) — was photographed during the FBI search of Little Saint James. A white military dress uniform with medals and ribbons was found in the same wardrobe ([EFTA00001969](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001969.pdf)), but no markings are visible in the photograph identifying its national origin; it should not be assumed to be IDF. In unsolicited emails to Mark Epstein beginning two days after Jeffrey Epstein's death, a man identifying himself as Melvyn Kohn — who described himself as a former US military intelligence operative (unverified) — wrote that "neither you nor he are Mossad, or even working knowingly for any foreign intel agency" but "there is the presence of certain parties in this mix who ARE" working for foreign intelligence ([EFTA00037218](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037218.pdf)). T&M Protection Resources (Epstein family security firm) classified the emails as "harassing" ([EFTA00037236](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037236.pdf)); the FBI conducted no documented follow-up. A FOIA exemption memo withheld information about a "confidential relationship with a foreign government" ([EFTA00015219](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015219.pdf)). An Austrian passport in Epstein's safe bore his photo under the name Marius Robert Fortelny and contained "numerous ingress and egress stamps" for France, Spain, UK, and Saudi Arabia ([EFTA00021576](https://www.justice.gov/epstein/files/DataSet%208/EFTA00021576.pdf), [EFTA00016172](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016172.pdf)). The real Marius Fortelni was identified in Southampton, NY; an FBI agent was assigned to "give him a call tomorrow" on July 16, 2019 ([EFTA00025539](https://www.justice.gov/epstein/files/DataSet%208/EFTA00025539.pdf)). No record of the call or its outcome exists. Austrian Embassy formally requested information July 22, 2019 ([EFTA00016173](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016173.pdf)). Epstein died 25 days later. The investigation was permanently abandoned.

**8. At Least 60-80 Victims Are Individually Identified; the USVI Says "Hundreds"**
FBI Miami identified 28 victims in the original Florida investigation, expanding to "well over 30" (2005-2007). SDNY documented "dozens of victims" and designated 5 Minor Victims at the Maxwell trial (2019-2021). The USVI Attorney General described "hundreds of young women and girls," with victims as young as 11-12. Civil proceedings assigned Jane Doe designations up to at least #43. A masseuse list recovered from seized devices contained "women and girls, some of which were identified minors." Victims described being tracked using a "database" for "availability and proximity" ([EFTA00016836](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016836.pdf)). MC2 Model Management publicly stated its submission requirement: "Age: Between 13 and 20 years old" ([EFTA01728258](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01728258.pdf)). A 14-year-old's Grand Jury testimony describes Maxwell buying her "white cotton underwear... like little girls underwear" and inviting her to the New Mexico ranch in "spring of 1996" ([EFTA00008631](https://www.justice.gov/epstein/files/DataSet%206/EFTA00008631.pdf)). A 15-year-old's victim impact statement recounts being "sexually molested by him for many hours" at Zorro Ranch in 2004, where "he positioned me by laying me on his floor so that I was confronted by all the framed photographs on him smiling with wealthy celebrities and politicians" ([EFTA00019994](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019994.pdf)). A witness described "12 year old girls flown from France for Epstein's birthday": "they were really poor over there, and their parents needed the money" ([EFTA00020703](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020703.pdf)). The same witness stated Epstein proposed she "bear his child" in exchange for a mansion and monthly income on the condition she "sign the child over to him" and the child would be "his and Ghislaine's."

**9. The 2007 Non-Prosecution Agreement's Blanket Co-Conspirator Immunity Was Expanded During Defense Team Negotiations**
The NPA's co-conspirator immunity clause was "not in original draft" and was "expanded during negotiations" by the defense team, which included Alan Dershowitz and Kirkland & Ellis ([EFTA00009016](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009016.pdf)). Acosta told OPR investigators he "did not recall focusing on the coconspirator provision" ([EFTA00009016](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009016.pdf), page 284). The provision granted blanket transactional immunity to unnamed, unidentified potential co-conspirators — and none of the four named co-conspirators had cooperated. The defense team raised the prospect of a book chapter on prosecutorial overreach: Acosta told OPR investigators "the book reference was that I might be personally embarrassed by pursuing this matter, because I would be the subject of a chapter in a book on prosecutorial overreach" (the specific defense team member who made this reference is not identified in the transcript) ([EFTA00009116](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009116.pdf)). The NPA was "deliberately concealed" from victims in violation of the Crime Victims' Rights Act -- Judge Marra found the government "chose to conceal the existence" of the agreement ([EFTA00010507](https://www.justice.gov/epstein/files/DataSet%208/EFTA00010507.pdf)). The NPA explicitly provided that the USAO "will not request, initiate, or in any way encourage immigration authorities to institute immigration proceedings against Ross or Marcinkova" — two foreign-national co-conspirators ([EFTA00176610](https://www.justice.gov/epstein/files/DataSet%209/EFTA00176610.pdf)). A separate 2020 DAG meeting memo documented plea negotiations with one redacted co-conspirator "who scheduled hundreds of sexual massages with minors for Epstein but was also a victim of his sexual abuse" ([EFTA00013209](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013209.pdf)); plea draft evidence in [EFTA00089268](https://www.justice.gov/epstein/files/DataSet%209/EFTA00089268.pdf) more closely matches Sarah Kellen than Marcinkova (see Section E below). Those plea negotiations collapsed. (Note: Allegations against Dershowitz by victims emerged publicly in 2014 court filings — years after the 2007-2008 NPA negotiations. Whether the blanket immunity provision was designed to protect any specific individual cannot be established from the available documents.) Under oath in his OPR interview, Acosta was asked about Epstein being "an intelligence asset of some sort." Acosta replied: "I'm not aware of it" and "Not to my recollection." He then elaborated: "there are questions that I may be asked publicly, that I don't think it's right for me to comment as to what classified information I may or may not know, because that's not the kind of stuff you'd go into, **but the answer is no, and no**" ([EFTA00009116](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009116.pdf), pages 404-405). Acosta explicitly denied the intelligence asset claim twice, though his reference to classified information in the same breath has been noted by observers.

**10. $30.5 Million in Art Auction Proceeds Were Laundered Through Haze Trust Into Trafficking Infrastructure**
In 2017 alone, Sotheby's paid $22.8 million and Christie's paid $7.7 million into Epstein's Haze Trust account at Deutsche Bank ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf), Exhibit D). These funds were swept within 1-2 days into the DBAGNY parking account, then systematically drained through Southern Financial LLC to external investment funds including Peter Thiel's Valar Fund ($28.8M total), Honeycomb Partners ($64M total), and Boothbay Fund ($38.25M total). Plan D LLC -- Epstein's aircraft holding company, which held the Gulfstream G550 (serial #5173, N212JE) used to transport victims -- received $15 million from Haze Trust and $30.5 million from Leon Black's BV70 LLC in the same March 2017 window, described by Apollo's Dechert report as being "in connection with an art transaction" ([EFTA02730996](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730996.pdf)). Only $10 million was ever repaid to Black. Sotheby's Private Client Group handler Lily D. Snyder managed the Epstein accounts ([EFTA02323094](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323094.pdf)). The specific artworks generating these proceeds have not been identified, but given the $30.5 million total, they were significant works. Leon Black emailed Epstein on December 21, 2016 -- ten days before the Sotheby's/Christie's transaction window opened -- instructing him to "liquidate the J BLACK trust" and expressing alarm that someone named Wechsler was telling others about "sensitive accounts" ([EFTA02664953](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664953.pdf)).

## Key Numbers

| Metric | Value |
|--------|-------|
| Total documented financial flows | $755,632,579 |
| Leon Black to Epstein entities | $168,000,000 |
| Post-KYC breach transactions | $189,000,000 (50 transactions) |
| Art auction proceeds (2017) | $30,510,961 |
| Honeycomb Partners (unidentified controller) | $64,000,000 |
| Boothbay Fund allocations | $38,250,000 |
| Peter Thiel / Valar Fund | $28,800,000 |
| Rothschild to Southern Trust | $24,999,980 |
| Tudor Futures Fund | $13,500,000 |
| Plan D LLC (aircraft) | $45,500,000 |
| Wexner theft ("several hundred million") | $200,000,000+ (est.) |
| Southern Trust aggregate income 2013-2017 | $656,000,000 |
| Epstein estate value | ~$500,000,000 |
| Black settlement with USVI | $62,500,000 |
| Shell entities under RM CODE 82289 | 95+ |
| Deutsche Bank accounts | 40+ |
| Identified individual victims | 60-80 minimum |
| Estimated total victims | 200+ (USVI: "hundreds") |
| Named individuals with evidence trails | 30+ |
| Seized digital devices | 70+ |
| Documents in initial FBI extraction | 1,100,000+ |
| Estimated emails in jeevacation@gmail.com | ~520,000 |
| Apple Mail PLIST metadata documents | 460+ |
| Failed redaction overlays exposing content | 12 |
| Investigation reports produced | 85 |

---

# II. THE FINANCIAL MACHINE (Chronological)

## A. The Wexner Foundation (Pre-2000 - 2007)

The Epstein financial empire began with Leslie Wexner. The relationship, which started in the late 1980s, gave Epstein access to "several hundred million dollars" through a power of attorney arrangement that Wexner's own attorneys later described as theft ([EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf)). The Wexner attorney proffer to SDNY on July 25, 2019, stated that Epstein had "stolen or otherwise misappropriated several hundred million dollars" from Wexner. He "frequently bought property on behalf of the Wexners and then sold it to himself for a fraction of the cost" and sold himself "a private plane that previously belonged to Wexner at a deeply discounted price."

Wexner purchased 9 East 71st Street in Manhattan in 1989 through Nine East 71st Street Corporation. By 1996, Epstein was telling the New York Times the mansion was his, though "it doesn't look like there's any record of the property changing ownership between 1989 and 2012" ([EFTA00037757](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037757.pdf)). On December 23, 2011, Epstein signed a deed transferring the property from Nine East 71st Street Corporation to Maple Inc. (St. Thomas, VI) -- signing both the Grantor and Grantee lines. No consideration was recorded.

When the Florida investigation began in 2005, Epstein told Wexner "he was being blackmailed" ([EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf)). The Wexners withdrew the power of attorney and privately settled rather than prosecuting -- allowing Epstein's financial empire to remain intact. A public $46 million "charitable donation" to YLK Foundation in 2008 far understated the actual scale of misappropriation. The FBI Prominent Names page lists Wexner with a "homosexual" notation ([EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf)).

The Financial Trust Company Inc., incorporated in USVI on November 6, 1998, held $212 million in assets by 2012. Its JP Morgan account (Q 78805-00-1) listed Darren Indyke as authorized contact, with the address C/O American Yacht Harbor, 6100 Red Hook Quarters B-3, St. Thomas. On October 19, 1999, an $18.3 million wire disbursement was sent -- prosecutors specifically investigated this as a "transfer to Maxwell." The FBI requested "account statements surrounding the 10/19/99 transfer to Maxwell" and the "source of the funds" ([EFTA00015176](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015176.pdf), [EFTA00038690](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038690.pdf), [EFTA00021994](https://www.justice.gov/epstein/files/DataSet%208/EFTA00021994.pdf)).

## B. The JP Morgan Chase Relationship (1998-2013)

Before Deutsche Bank, Epstein maintained his primary banking relationship at JPMorgan Chase. The relationship spanned approximately 15 years and involved:

**Account Structure:**
- Financial Trust Company Inc. -- JP Morgan account Q 78805-00-1, listed Darren Indyke as authorized contact
- Address: C/O American Yacht Harbor, 6100 Red Hook Quarters B-3, St. Thomas, USVI
- Financial Trust Company held $212 million in assets by 2012 ([EFTA00015176](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015176.pdf))
- Multiple Epstein-related accounts across personal, corporate, and trust structures

**Key Transactions:**
- October 19, 1999: $18.3 million wire disbursement -- prosecutors specifically investigated this as a "transfer to Maxwell" ([EFTA00015176](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015176.pdf), [EFTA00038690](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038690.pdf), [EFTA00021994](https://www.justice.gov/epstein/files/DataSet%208/EFTA00021994.pdf))
- FBI requested "account statements surrounding the 10/19/99 transfer to Maxwell" and the "source of the funds"

**Jes Staley Connection:**
Jes Staley served as head of JPMorgan's private banking division and later as CEO of the investment bank while the Epstein relationship was active. The relationship between Staley and Epstein was documented through drinks with Mandelson (December 2009, [EFTA02434434](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02434434.pdf)), a rape allegation flagged by SDNY (December 2019, [EFTA00029358](https://www.justice.gov/epstein/files/DataSet%208/EFTA00029358.pdf)), and victim journal violence allegations ([EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf)). JPMorgan ultimately terminated the Epstein relationship in 2013.

**JPMorgan Settlement:**
JPMorgan paid $290 million to settle victim lawsuits (2023). Individual victims received approximately $1 million allocations ([EFTA00037088](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037088.pdf), January 2024). The settlement acknowledged JPMorgan's institutional failure to terminate the Epstein relationship despite red flags.

**Sean Carmody Pipeline:**
Sean Carmody, a JPMorgan private banker identified in the investigation, served as a conduit between Epstein's JP Morgan accounts and related Centerview Partners transactions. The Sean Carmody pipeline connected the old JPMorgan banking relationship to the new Deutsche Bank architecture.

## C. The Deutsche Bank Relationship (2013-2019)

### Structure

Deutsche Bank's relationship with Epstein was organized under a single relationship manager code -- RM CODE 82289 -- encompassing 95+ entities across 10 categories:

**Core Trusts:** Haze Trust (16+ sub-accounts, ~$201M flows), Southern Trust/Financial (8 sub-accounts, ~$282M flows)
**Aviation:** 13 entities (JEGE LLC, Hyperion Air Inc, Plan D LLC, Thomas World Air LLC, Freedom Air Petroleum LLC, NES LLC, Air Ghislaine Inc, Shmitka Air Inc, Six G Aviation Inc, NSSOGP, Frontier JV)
**Real Property:** Maple Inc (9 E 71st St), Nautilus Inc (USVI), Laurel Inc (Palm Beach), LSJE LLC, Great St. Jim LLC, Zorro Management LLC, Neptune LLC
**Financial:** Financial Trust Company Inc (USVI, $212M assets), BV70 LLC ($50.5M)
**Insurance/Professional:** Epstein Insurance Trust, Stewart Oldfield (PWM SPG), Daphne Cales, Darren K. Indyke PLLC
**Investment Recipients:** Honeycomb Partners LP ($64M), Boothbay Fund ($38.25M), Valar Global Fund ($28.8M), Tudor Futures Fund ($13.5M), Blockchain Capital IV, Coatue Enterprises, Neoteny 3 LP
**Trust Entities:** Butterfly Trust (Epstein as grantor; Maxwell was a beneficiary until late 2014 removal), Angara Trust (Maxwell as grantor)
**Art/Culture:** Prytanee LLC (managed by Etienne Binant; indirect Jack Lang connection through daughter Caroline, $197K), Gratitude America Ltd (Lithuanian ballet)
**Crypto:** The 2017 Caterpillar Trust ($15M Blockchain Capital)
**Third-Party Clients (Same Officers):** Leon D. Black (multiple accounts), Christopher A. Boies, Todd & Karen Wanek JTWRO, Dominique Leimer

### Key Entity Functions

The shell entity network was not random -- each entity served a specific operational function:

| Entity | Function | Key Evidence |
|--------|----------|-------------|
| **Southern Trust Company Inc** | Primary receiving entity -- all major external payments flowed here | $656M aggregate income (2013-2017), [EFTA00018778](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018778.pdf) |
| **Southern Financial LLC** | Distribution entity -- disbursed funds to external investment vehicles | Outbound to Honeycomb, Valar, Boothbay, Coatue, Ito |
| **Haze Trust** | Art money + dissolution staging -- received auction proceeds and staged repositioning | $30.5M from Sotheby's/Christie's, $31.5M dissolution event |
| **DBAGNY** | Parking account -- intermediary between Haze Trust and Southern Financial | Funds swept within 1-2 days of receipt |
| **Plan D LLC** | Aircraft holding -- funded the Gulfstream G550 used to transport victims | $45.5M from Haze Trust ($15M) + BV70/Black ($30.5M) |
| **Butterfly Trust** | Co-conspirator payments -- Epstein's trust; Maxwell was a beneficiary until late 2014, then replaced by Shuliak and Indyke | $100K to Aviloop (Marcinkova) 2 days after Miami Herald |
| **Maple Inc** | Manhattan real property -- held 9 E 71st St after self-dealing transfer | Epstein signed both Grantor and Grantee on 2011 deed |
| **LSJE LLC** | Little Saint James holding -- stop-wire attempted after processing | [EFTA01426081](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01426081.pdf) |
| **Zorro Management LLC** | NM ranch -- asset forfeiture requested by NM AG | "Trafficking of children" ([EFTA00015190](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015190.pdf)) |
| **Neptune LLC** | USVI property holding | Balance on RM CODE 82289 snapshot |
| **Great St. Jim LLC** | Second island -- purchased Jan 2016 for $5M, under development through May 2019 | 3BIS architecture firm meetings |
| **Hyperion Air Inc** | Aircraft entity -- one of 13 aviation entities | RM CODE 82289 roster |
| **Air Ghislaine Inc** | Helicopter -- renamed Shmitka Air Inc in 2010 (post-Maxwell separation) | Sikorsky S-76C-2 |
| **Financial Trust Company Inc** | USVI entity -- $212M assets, JP Morgan account, Indyke authorized contact | $18.3M "transfer to Maxwell" (1999) |
| **BV70 LLC** | Black-controlled entity -- $50.5M in Epstein accounts | $30.5M to Plan D, $10M to Gratitude America |
| **Prytanee LLC** | Art investment managed by Etienne Binant; indirect Jack Lang connection through daughter Caroline | $1.4M deposited, $197K remaining |
| **Gratitude America Ltd** | Lithuanian ballet + cancer research -- Shuliak connection | BV70/Black $10M funding |
| **The 2017 Caterpillar Trust** | Crypto investment vehicle | $15M Blockchain Capital (Feb 2018) |
| **Epstein Insurance Trust** | Art insurance | Covered bronzes across properties |
| **Angara Trust** | Maxwell entity (Maxwell as grantor) | Part of Borgerson-Angara-Tidewood shell chain |
| **Equibase Company** | Horse racing entity | Unexplained presence in DB relationship structure |
| **Aviloop LLC** | Marcinkova entity -- Subject 1/25 in SAR | $100K Butterfly Trust wire (witness tampering timing) |

The entity structure operated as a layered system: external funds entered through Southern Trust, were redistributed through Southern Financial, staged through Haze Trust and DBAGNY parking accounts, and ultimately funded the operational infrastructure (Plan D aircraft, Zorro Management ranch, property entities) and external investments (Honeycomb, Valar, Boothbay). The same bankers -- Litchford and Morris -- had visibility into every layer of this structure because all entities were consolidated under a single RM CODE.

The complete account officer roster ([EFTA01359500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01359500.pdf)) reveals that the SAME two bankers managed both Epstein and his largest financial patron:

| Primary Officer | Secondary Officer | Account |
|----------------|-------------------|---------|
| Jj Litchford | Paul Morris | JEFFREY EPSTEIN |
| Jj Litchford | Paul Morris | **LEON D. BLACK** |
| Jj Litchford | Paul Morris | **LEON D. BLACK $25M ELYSIUM CHECKING** |
| Jj Litchford | Paul Morris | SOUTHERN TRUST COMPANY |
| Jj Litchford | Paul Morris | SOUTHERN FINANCIAL LLC |
| Jj Litchford | Paul Morris | THE HAZE TRUST |
| Jj Litchford | Paul Morris | PLAN D, LLC |
| Jj Litchford | Paul Morris | BUTTERFLY TRUST |
| Jj Litchford | Paul Morris | HYPERION AIR, LLC |
| Jj Litchford | Paul Morris | NEPTUNE, LLC |
| Jj Litchford | Paul Morris | DARREN K. INDYKE PLLC |
| Jj Litchford | Paul Morris | CHRISTOPHER A. BOIES |
| Jj Litchford | Paul Morris | TODD & KAREN WANEK JTWRO |
| Jj Litchford | Paul Morris | DOMINIQUE LEIMER |

### Named Deutsche Bank Staff

The following Deutsche Bank employees have been identified in the evidentiary record as having direct involvement in Epstein account management:

**Account Officers:**
| Name | Role | Key Actions |
|------|------|-------------|
| Jj Litchford | Primary Officer (all accounts) | Managed Epstein, Black, Boies, Wanek simultaneously |
| Paul Morris | Secondary Officer (all accounts) | Same portfolio as Litchford |
| Stewart Oldfield | PWM SPG | Approved $23M wire ([EFTA01431221](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01431221.pdf)), managed Epstein Insurance Trust |
| Cynthia Rodriguez | Account support | Internal correspondence chain |
| Brigid Macias | Account support | Processing documentation |
| Vahe Stepanian | Operations | Transaction handling |
| Akash Malhotra | Operations | Processing chain |
| Xavier Avila | Operations | Wire approvals |
| Bradley Gillin | Compliance | Compliance review ([EFTA01362456](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362456.pdf)) |
| Daphne Cales | Trust management | Managed Epstein Insurance Trust alongside Oldfield |
| Davide-A Sferrazza | Account management | Administrative documentation |
| Matt Glassman | Client relations | Account correspondence |
| Tazia Smith | Administrative | Account documentation |

**Key Compliance Failures by Named Individuals:**
1. Stewart Oldfield approved the $23M wire to Kellerhals law firm despite compliance concerns -- the single strongest evidence of individual banker mishandling ([EFTA01431221](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01431221.pdf))
2. Bradley Gillin was part of the compliance chain that documented "kyc is not happening" but did not halt account operations ([EFTA01362456](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362456.pdf))
3. Litchford and Morris continued managing all Epstein accounts through the post-KYC breach period, processing $189M in additional transactions
4. A stop-wire was attempted on an LSJE transaction but the wire had "already been processed" -- the compliance control arrived after the money was gone ([EFTA01426081](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01426081.pdf))

**Deutsche Bank Penalty:**
Deutsche Bank paid $150 million to the New York Department of Financial Services for these failures. Additionally, Deutsche Bank paid $75 million to settle victim lawsuits. The penalty addressed institutional failure but no individual criminal charges were brought against any named bank employee.

The complete balance snapshot from August 17, 2018 ([EFTA01381149](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381149.pdf)) shows 15+ Epstein accounts totaling $50M+ including Haze Trust ($40.5M checking + $2.5M brokerage), Gratitude America ($2M), Southern Trust, Butterfly Trust, Zorro Management, Neptune LLC, and others. The Elysium Management Relationship was activated September 20, 2015, and the Southern Financial Relationship was activated October 19, 2015 -- one month apart ([EFTA01477330](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477330.pdf)).

### Deutsche Bank Financial Exhibits ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))

The cornerstone financial document -- [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) -- contains five exhibits (A through E) that together map the complete money flow architecture:

**Exhibit A: Incoming Wire Transfers to Southern Trust Company**
Lists all external payments into Southern Trust Company Inc., the primary receiving entity. This exhibit documents the 14 Leon Black wire transfers ($126.5M direct), the Rothschild $25M, the Tudor $13.5M, the Kellerhals $23M, the Josephson $200K, the Muchnik $500K, and all other identified external revenue sources. Each entry includes a date, amount, source entity, and Bates reference number (DB-SDNY format). The exhibit establishes that Leon Black was by far the largest single source of identified revenue, accounting for approximately 45% of all documented incoming transfers.

**Exhibit B: Outgoing Wire Transfers from Southern Trust / Southern Financial**
Maps the destination of funds flowing out of Epstein's primary operating entities. This exhibit documents the $64M to Honeycomb Partners, $28.8M to Valar Global Fund (Thiel), $38.25M to Boothbay Fund, $2M to Coatue Enterprises, $2M to Joi Ito/Neoteny, $225K to Melanoma Research Alliance Foundation, and all other external disbursements. The exhibit reveals that Epstein was operating as a "fund-of-funds allocator" -- receiving capital from wealthy individuals and redistributing it to elite investment vehicles.

**Exhibit C: Inter-Entity Transfers (Internal Sweeps)**
Documents the movement of funds between Epstein's own entities -- particularly the Haze Trust-to-DBAGNY-to-Southern Financial "parking" pattern. This exhibit captures the $31.5M February 2019 dissolution event and the systematic sweeping of auction house proceeds (within 1-2 days of receipt) from Haze Trust Checking into the DBAGNY parking account and then out to Southern Financial for external distribution. The parking account pattern suggests deliberate obfuscation of the source-to-destination chain.

**Exhibit D: Art Auction Proceeds**
Specifically documents the $30,510,961 in combined Sotheby's ($22.8M) and Christie's ($7.7M) payments to the Haze Trust account in 2017. This exhibit provides the Bates references for each of the three auction house payments and establishes the art-to-trust flow that converted artwork into liquid capital for redistribution.

**Exhibit E: Leon Black / BV70 / Plan D Transactions**
Details the relationship between Black's BV70 LLC entity, Epstein's Plan D LLC (aircraft holding company), and the "in connection with an art transaction" characterization. This exhibit documents the $30.5M from BV70 to Plan D (March-April 2017), the $10M repayment, and the residual $20.5M that effectively subsidized Epstein's aircraft operations. The exhibit was central to the Apollo Conflicts Committee (Dechert LLP) investigation and the Senate Finance Committee inquiries.

Together, these five exhibits constitute the most comprehensive financial mapping in the entire DOJ release. They establish that the same infrastructure -- the same bank, the same officers, the same entity structure -- processed both legitimate-appearing investment transactions and the funding of trafficking operations (Plan D aircraft, Butterfly Trust, Zorro Management/NM ranch).

### Money Sources

**Leon Black ($168M+, 2013-2017)**

Fourteen wire transfers from five Black-controlled entities to Epstein's Southern Trust Company:

| Date | Amount | Source Entity | Bates Reference |
|------|--------|---------------|-----------------|
| 10/15/2013 | $8,500,000 | Leon and Debra Black | DB-SDNY-0004636 |
| 12/18/2013 | $10,000,000 | Black Family Partners LP c/o Apollo | DB-SDNY-0004676 |
| 04/25/2014 | $5,000,000 | Leon and Debra Black | DB-SDNY-0004771 |
| 04/25/2014 | $5,000,000 | Black Family Partners LP c/o Apollo | DB-SDNY-0004771 |
| 04/29/2014 | $15,000,000 | Leon and Debra Black | DB-SDNY-0004777 |
| 07/15/2014 | $20,000,000 | Narrow Holdings LLC c/o Elysium | DB-SDNY-0004846 |
| 10/16/2014 | $7,000,000 | Leon and Debra Black | DB-SDNY-0004918 |
| 10/16/2014 | $13,000,000 | Black Family Partners LP c/o Apollo | DB-SDNY-0004918 |
| 10/22/2014 | $2,000,000 | Leon and Debra Black c/o Apollo | DB-SDNY-0004925 |
| 10/22/2014 | $3,000,000 | Black Family Partners LP c/o Apollo | DB-SDNY-0004925 |
| 10/13/2015 | $10,000,000 | Leon and Debra Black + BFP c/o Apollo | DB-SDNY-0005082 |
| 12/18/2015 | $10,000,000 | Black Family Partners LP | DB-SDNY-0005122 |
| 12/30/2015 | $10,000,000 | Leon and Debra Black c/o Apollo | DB-SDNY-0005133 |
| 04/25/2017 | $8,000,000 | Leon and Debra Black c/o Apollo | DB-SDNY-0006238 |

**Subtotal from direct payments: $126,500,000**

Plus additional Black-entity transfers:
- BV70 LLC to Plan D LLC: $30,500,000 (March-April 2017, described as "in connection with an art transaction")
- BV70 LLC to Gratitude America: $10,000,000
- Narrow Holdings LLC "do Elysium" to Southern Trust: $20,000,000 (July 2014)

**Grand total documented Black-to-Epstein flows: approximately $168,000,000** ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))

Black never signed a services agreement after 2013 for payments exceeding $100 million ([EFTA02730996](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730996.pdf)). He refused to answer the Senate Finance Committee's questions about his art advisory relationship with Epstein ([EFTA02731023](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731023.pdf)). The Apollo Conflicts Committee report (Dechert LLP) documented that Epstein managed Black's art including "formation of art partnership, contested Picasso sculpture ownership, art loans, like-kind exchanges, and tax advisory opinions" -- but the $168M in total payments dwarfs any plausible art advisory fee. Only $10M of the $30.5M Plan D transfer was ever repaid.

**Benjamin Edmond de Rothschild ($25M, December 2015)**

Two wires within four days:
- 12/17/2015: $10,000,000 from Edmond de Rothschild (Suisse) SA Geneva
- 12/21/2015: $14,999,980 from Benjamin Edmond de Rothschild personally

Both to Southern Trust Company, appearing on the same Bates page (DB-SDNY-0005122) as Black's $10M payment dated 12/18/2015 -- three major patrons paying within the same week ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf)). Ariane de Rothschild emailed Epstein eight months earlier: "this is my new email address that nobody can access" ([EFTA02502971](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02502971.pdf)) -- establishing a deliberate untraceable communication channel. On January 12, 2015, Epstein's former Obama White House Counsel contact Kathryn Ruemmler wrote: "had assumed you were exaggerating a bit about Benjamin. Wrong assumption" ([EFTA02513986](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02513986.pdf)) -- eleven months before the $25M transfer. One week after the transfer, Epstein's pilot Larry Visoski coordinated a private jet flight from Little St. James to Marrakesh, Morocco with "you and Karyna only" ([EFTA02477179](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02477179.pdf)).

**Tudor Futures Fund / Paul Tudor Jones ($13.5M, August 2014)**

- 08/04/2014: $12,826,541 to Southern Financial LLC
- 08/08/2014: $677,400 to Southern Financial LLC ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))

PLIST timestamp correlation analysis showed this was the strongest email-to-transaction correlation in the entire collection: 21 emails within 14 days of the transfer, with August 2014 being the single highest-activity month at 23 emails (4.2x the monthly average). On the exact transfer date (August 15, 2014), Epstein emailed someone identified only as "President" asking "tomorw?" -- suggesting a next-day meeting or action ([EFTA02589073](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589073.pdf)). Two days later, he emailed Erika Kellerhals about avoiding "funny press" around someone named "Stacy" ([EFTA02588569](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02588569.pdf)). Nine days later, he emailed Olivier Colom of Edmond de Rothschild (France), whose bank disclaimer appeared in the correspondence ([EFTA02589075](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589075.pdf)).

**Blockchain Capital ($15M, February 2018)**

Three simultaneous wires on 2/21/2018:
- Blockchain Capital IV LP: $10,500,000
- Blockchain Capital III Digital Liquid Venture Fund LP: $2,625,000
- Blockchain Capital Parallel Fund IV LP: $1,875,000

All to The 2017 Caterpillar Trust ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf)). This crypto investment was part of a systematic portfolio that included a full LedgerX confidential pitch deck in Epstein's files ([EFTA01734786](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01734786.pdf)), "Bitcoin troika" references ([EFTA02070051](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02070051.pdf)), "Bitcoins for Mongolia" ([EFTA02069096](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02069096.pdf)), and an "Epstein-Cryptology?" file referenced in three separate documents. In March 2014, Epstein and Reid Hoffman were introduced to Austin Hill (crypto pioneer) regarding "incredible network of cryptographers, authentication & e-cash tech" ([EFTA02518909](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518909.pdf)).

**Art Auction Houses ($30.5M, 2017)**

- 06/19/2017: $7,725,000 from Christie's Inc. (Bates DB-SDNY-0006320)
- 09/25/2017: $11,536,544 from Sotheby's (Bates DB-SDNY-0006565)
- 10/24/2017: $11,249,417 from Sotheby's (Bates DB-SDNY-0006646)

All to Haze Trust Checking, then swept within 1-2 days to DBAGNY parking account ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf)). Sotheby's Private Client Group handler: Lily D. Snyder ([EFTA02323094](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323094.pdf)). Christie's contacts: Joanna Ostrem and Madeline Lazaris ([EFTA02323043](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323043.pdf)). The specific artworks generating these proceeds remain unidentified in the DOJ files.

**Additional External Payers:**
- Kellerhals Ferguson Kroblin PLLC: $23,000,000 (November 2015) + $75,000 (February 2016) -- trust attorney ([EFTA01431221](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01431221.pdf))
- Barry Jay Josephson: $200,000 (November 2013) ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))
- Seed Media Group (Adam Bly): $304,000 total across multiple payments ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))
- Gol Muchnik: $500,000 (April 2016) ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))
- Sultan Bin Sulayem (Dubai Ports World): $6,200 (October 2017) -- confirms direct financial tie ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))
- Island Global Yachting LTD: $293,000 (May 2014) -- yacht operations ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))
- Joichi Ito: $483,915 direct + Neoteny 3 LP $30,000 ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))

### Money Destinations

**Honeycomb Partners ($64M) -- Controller Unidentified**

The single largest external recipient in the entire financial network: $53M to Honeycomb Partners LP, $10M to Honeycomb Ventures IV LP, $1M to Honeycomb Ventures I LP. Payments from Southern Trust Company and The 2017 Caterpillar Trust continued through March 2019 -- less than four months before Epstein's arrest. The controlling persons behind Honeycomb remain unidentified in any database -- 1.8M redaction records, 38K OCR records, 21K image records yield zero identification. This is a critical evidence gap: $64 million flowed to an entity whose beneficiary has never been publicly identified. ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))

**Valar Global Fund / Peter Thiel ($28.8M)**

Sixteen transactions spanning 2015-2019:
- Valar Global Fund II: $6,300,000 (5 transactions, 2015)
- Valar Global Fund III: $22,500,000 (11 transactions, 2016-2019)

Post-KYC breach (April 2018+), $5.75M still flowed to Valar across 3 transactions. The last payment -- $1,500,000 -- was made April 17, 2019, less than three months before arrest. ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))

Beyond the financial relationship, Epstein arranged a lunch with Peter Thiel and possibly Bill Burns (future CIA Director), brokered by Bob Kerrey ([EFTA02589110](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589110.pdf), September 2014). A single calendar day -- September 22, 2014 -- shows Ehud Barak, Leon Black, Larry Summers, and Peter Thiel ALL visiting Epstein ([EFTA00362483](https://www.justice.gov/epstein/files/DataSet%209/EFTA00362483.pdf)). The Thiel-Epstein connection is far deeper than previously reported.

**Boothbay Fund ($38.25M)**

Six outbound payments from Southern Financial LLC totaling $38.25M (2014-2016) across Boothbay Absolute Return Strategies and Boothbay Multi Strategy Fund. One $10M return from Boothbay Absolute Return Strategies (January 2017) -- a round-trip transaction pattern where $10M went out in May 2014 and $10M came back in January 2017, raising questions about wash trading or structured investment returns. ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))

**Plan D LLC ($45.5M) -- Aircraft Fleet**

Plan D, LLC (6100 Red Hook Quarter, B3, St. Thomas, USVI) held Epstein's Gulfstream G550 (serial #5173, registered as N212JE). Larry Visoski (Epstein's chief pilot since the 1990s) was listed as sole manager on the original articles of organization. Plan D received:
- $15,000,000 from Haze Trust (2017)
- $30,500,000 from BV70 LLC / Leon Black (March-April 2017)

The Black payment was described as "in connection with an art transaction" ([EFTA02730996](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730996.pdf)). Only $10M was ever repaid to Black, meaning $20.5M of Black's money effectively subsidized Epstein's aircraft operations -- the same aircraft used to transport trafficking victims on the weekly Teterboro-Palm Beach-USVI cycling route. ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf), [EFTA00018778](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018778.pdf), [EFTA00037857](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037857.pdf))

**Joi Ito / Neoteny ($2M+)**

$1M to Neoteny 3 LP, $1M+ direct to Ito across multiple payments (2014-2015). Ito arranged a US Treasury call to include Epstein ([EFTA02589077](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589077.pdf)), attended dinner at Epstein's with Woody Allen, Tom Pritzker, and Ed Boyden ([EFTA02377042](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02377042.pdf)), and was invited alongside Reid Hoffman to Columbus Day weekend at Epstein's property ([EFTA02575363](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02575363.pdf)). Ito resigned from MIT Media Lab when payments were exposed. ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))

**Coatue Enterprises ($2M)**

**CORRECTION (Revisit #9):** The Coatue contact was Richard Kahn (Epstein's accountant at HBRK Associates), not Philippe Laffont personally. Laffont is Coatue's founder, but the Epstein relationship ran through Kahn. Additionally, Epstein's trust instruments reference "Coatue Enterprises, LLC" in connection with Kahn's beneficial interests. Four quarterly $500K payments (2017-2018). Two of four payments occurred post-KYC breach. ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))

**Gratitude America, Ltd -- Lithuanian Ballet and Cancer Research**

Epstein entity making payments to NPO Baleto Teatras (Lithuanian National Ballet) and VSJ Baleto Teatras, as well as Cancer Research Wellness Institute. Connection to Karyna Shuliak (Lithuanian-born Butterfly Trust beneficiary) established through a "Hello from Vilnius" email ([EFTA02203371](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02203371.pdf)). Shuliak appears 20+ times in DS10 documents as trust beneficiary and signatory. Funded by $10M from BV70 LLC (Leon Black). ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))

**David Mitchell / Mitchell Holdings LLC (~$476K)**

13+ recurring disbursements totaling approximately $476,000 (2018-2019), connected to Peter Mandelson advisory role. Mitchell's address: 745 Fifth Avenue, later 801 Madison Avenue. On November 7, 2017, Epstein emailed Mitchell: "tomorow you must make money. clear that cascade will au[thorize] the payments" ([EFTA02570991](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570991.pdf)) -- the term "cascade" in a payment context may refer to cascading fund transfers through multiple entities sequentially. On the same day, Epstein emailed Richard Kahn about trustee replacements, a potential "lawsuit against Bain," and the delivery of "account statements" ([EFTA02570951](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570951.pdf)).

**Melanoma Research Alliance Foundation ($225K)**

Charitable donation from Epstein entities. ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))

### The February 2019 Dissolution Event

On February 19-22, 2019 -- five months before arrest -- a mass financial restructuring moved $31.5 million in a single weekend:

| Date | Amount | From | To |
|------|--------|------|----|
| 02/19 | $12,608,253 | Haze Trust Brokerage | Haze Trust Checking |
| 02/19 | $11,715,364 | Southern Financial LLC | Haze Trust Checking |
| 02/19 | $7,000,000 | Jeffrey Epstein Checking | Haze Trust Checking |
| 02/22 | $24,564,037 | Haze Trust Checking | Southern Financial LLC |
| 02/22 | $7,000,000 | Haze Trust Checking | Jeffrey Epstein Checking |

This was a trust consolidation-and-redistribution event that repositioned $31.3M in inflows to Haze Trust Checking and then $31.5M in outflows over a single weekend, effectively draining the Haze Trust Brokerage and repositioning assets across entities. The timing -- five months before arrest -- suggests pre-arrest asset repositioning. (Note: the jeevacation@gmail.com account was continuously active during this period per DS9 grand jury returns; the earlier characterization of a "99-day email blackout" was incorrect -- see CORRECTION at Section IV.N.) ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))

### The Critical November-December 2018 Window

The period immediately following the Miami Herald publication represents the most forensically significant financial window in the entire case. Within the span of one week:

| Date | Event | Amount | EFTA |
|------|-------|--------|------|
| Nov 28, 2018 | Miami Herald "Perversion of Justice" series begins | -- | Public record |
| Nov 30, 2018 | Butterfly Trust to Aviloop LLC (Marcinkova) | $100,000 | [EFTA00020685](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020685.pdf) |
| Dec 3, 2018 | Payment to another NPA co-conspirator | $250,000 | [EFTA00028785](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028785.pdf) |
| Dec 2018 | Additional emergency disbursements | Multiple | [EFTA00028785](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028785.pdf) |

The government characterized the Aviloop and co-conspirator payments as potential witness tampering -- emergency disbursements to co-conspirators timed precisely to the publication that reignited public scrutiny of the Epstein case. The Butterfly Trust -- from which the Aviloop wire originated -- was Epstein's trust entity. Maxwell had been a beneficiary until late 2014, when she was deleted and replaced by Shuliak and Indyke in the same instrument ([EFTA01282297](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01282297.pdf), page 16). This demonstrates that co-conspirator payments flowed from the same entity structure that managed inner-circle benefits. **CORRECTION (Revisit #48):** The original report stated a "99-day PLIST email blackout" was in effect during this window. DS9 has established this was incorrect -- the jeevacation@gmail.com account was continuously active throughout this period, and DS9 contains conference calls (e.g., Ruemmler/Wolff/Indyke on December 3) and direct Epstein emails. Electronic communication trails DO exist for this period through DS9 grand jury subpoena returns. The PLIST gap was a methodological artifact of DS11 metadata extraction, not a cessation of communications.

### KYC Breach and Post-Breach Flows

The documented timeline of compliance failure at Deutsche Bank:

| Date | Event | EFTA |
|------|-------|------|
| Nov 13, 2015 | $23M wire to Kellerhals law firm approved by Stewart Oldfield despite compliance concerns | [EFTA01431221](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01431221.pdf) |
| Multiple dates | Stop-wire attempted on LSJE transaction AFTER wire already processed | [EFTA01426081](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01426081.pdf) |
| April 16, 2018 | "kyc is not happening" for SOUTHFINANMD documented in internal chain | [EFTA01362456](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362456.pdf), [EFTA01406955](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406955.pdf) |
| Multiple dates | "URGENT - THIRD REQUEST!!!!!" AML escalation on Epstein accounts | [EFTA01414241](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01414241.pdf) |
| Post-April 2018 | 50 transactions totaling $189M continued flowing through flagged accounts | Forensic workbench |
| Feb 2019 | $31.5M dissolution event processed without intervention | [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) |
| April 17, 2019 | Last documented Valar Fund payment ($1.5M) -- 80 days before arrest | [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) |

Deutsche Bank ultimately paid $150 million in penalties to the New York Department of Financial Services for these failures. The same officers who approved Epstein transactions (Stewart Oldfield, Paul Morris, Jj Litchford) managed the accounts of Epstein's largest financial patron Leon Black and other VIP clients including the Wanek Trust of 2000 (Ashley Furniture CEO Todd Wanek) under the "Third Lake Capital Relationship" ([EFTA01477330](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477330.pdf)). Individual criminal attribution to specific bankers remains an open question -- the forensic workbench analysis established strong institutional knowledge + control failure + suspicious transaction handling, but the evidence falls short of individual criminal attribution without additional transaction metadata and testimony.

### The 99-Day PLIST Gap (November 14, 2018 -- February 21, 2019)

PLIST timestamp analysis of 420 emails with parseable Apple Mail metadata identified a 99-day gap in PLIST-recovered metadata from November 14, 2018, through February 21, 2019. This window covers:

| Event | Date | PLIST Email Activity |
|-------|------|----------------------|
| Miami Herald "Perversion of Justice" series begins | Nov 28, 2018 | ZERO PLIST-recovered emails |
| $100K wire to Marcinkova/Aviloop (witness tampering) | Nov 30, 2018 | ZERO PLIST-recovered emails |
| $250K wire to another co-conspirator | Dec 3, 2018 | ZERO PLIST-recovered emails |
| Emergency financial restructuring period | Dec-Jan 2019 | ZERO PLIST-recovered emails |
| $31.5M dissolution event | Feb 19-22, 2019 | 2 PLIST-recovered emails (household only) |

**CORRECTION (Revisit #48):** The gap was originally described as a "blackout" implying zero email activity during this period. DS9 analysis has established that the jeevacation@gmail.com account was in fact continuously active throughout this entire period. Epstein emailed Summers, Barak, Ruemmler, Church, Groff, and others daily. Conference calls were documented (e.g., Ruemmler/Wolff/Indyke on December 3). The gap was an artifact of the DS11 PLIST extraction methodology, which only captured Apple Mail metadata from a specific device or backup -- not the totality of the jeevacation@gmail.com account. DS9 contains the same emails recovered through other channels (e.g., grand jury subpoena returns from Google). The PLIST gap therefore reflects device-specific metadata loss, not a communication cessation.

For comparison, the monthly average email volume during the active period was approximately 5.5 emails per PLIST-recovered document, with August 2014 (the Tudor $13.5M transfer month) peaking at 23 emails -- 4.2 times the monthly average.

### PLIST-to-Transaction Correlation Summary

The strongest documented correlations between email activity and financial events:

| Financial Event | Amount | Email Correlation | Significance |
|----------------|--------|-------------------|-------------|
| Tudor Futures Fund | $13.5M | 23 emails/month, 21 in 14-day window | STRONGEST -- same-day email to "President" |
| Sotheby's/Haze Trust | $30.5M | 39 emails in 2 weeks | STRONG -- Black "sensitive accounts" -10 days |
| KYC Breach | N/A | 8 emails | MODERATE -- "lawyer/accountant team" intro -5 days |
| Haze Trust Drain | $48.3M | 12 emails | MODERATE -- Kahn/Christie's, Maybach |
| Rothschild | $25M | 1 email | WEAK -- but Marrakesh flight +7 days |
| Aviloop Wire | $100K | 0 PLIST emails | Zero in DS11 PLIST (but DS9 confirms active email) |
| Emergency Wires | Multiple | 0 PLIST emails | Zero in DS11 PLIST (but DS9 confirms active email) |
| Dissolution Event | $31.5M | 2 emails | MINIMAL |

### Key Financial Correspondents Identified Through PLIST

| Correspondent | Emails | Key Content |
|---------------|--------|-------------|
| Richard Kahn (HBRK Associates, 575 Lexington Ave) | 7 | Trust operations, Christie's art, Maybach exchange, trustee changes |
| Larry Visoski (chief pilot) | 7 | Flight logistics, aircraft negotiations, Marrakesh routing |
| Lesley Groff/Croft (executive assistant) | 5+ | Scheduling, World Cup tickets ($900 each for "HHI"), staff coordination |
| David Mitchell (Mitchell Holdings) | 4 | "Cascade" payments, property inspections, $476K recurring |
| Ariane de Rothschild | 1 | "Nobody can access" new email, Sotheby's mention |
| Leon Black | 1 | "Liquidate the J BLACK trust," "sensitive accounts" warning |
| Erika Kellerhals | 2 | Avoiding "funny press" around "Stacy," August 2014 |
| Olivier Colom (Edmond de Rothschild France) | 1 | Bank disclaimer, 9 days after Tudor transfer |

### Southern Trust Revenue Mystery

Southern Trust Company reported net income of:

| Year | Net Income |
|------|-----------|
| 2013 | $50,300,000 |
| 2014 | $67,500,000 |
| 2015 | $52,800,000 |
| 2016 | $4,800,000 |
| 2017 | $17,100,000 |
| **Total** | **$656,000,000** (with $73.6M in tax exemptions) |

([EFTA00018778](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018778.pdf))

NYT reporter Matthew Goldstein noted: "The biggest question remains the $200 million that Epstein's Southern Trust took in as revenue... We remain committed to getting to the bottom of this puzzling influx of cash" ([EFTA00023239](https://www.justice.gov/epstein/files/DataSet%208/EFTA00023239.pdf)).

**Revenue Source Gap Analysis:**

| Identified Source | Amount | Period |
|-------------------|--------|--------|
| Leon Black entities | $168,000,000 | 2013-2017 |
| Art auction proceeds | $30,510,961 | 2017 |
| Rothschild | $24,999,980 | Dec 2015 |
| Tudor Futures Fund | $13,503,941 | Aug 2014 |
| Blockchain Capital | $15,000,000 | Feb 2018 |
| Kellerhals law firm | $23,075,000 | Nov 2015 - Feb 2016 |
| Josephson, Bly, Muchnik, Ito, others | ~$5,000,000 | Various |
| **Total Identified** | **~$280,000,000** | |
| **Unidentified (Gap)** | **~$376,000,000** | |

The $376 million gap between identified sources and total reported income remains the single largest unexplained financial question in the case. The revenue dramatically declined in 2016-2017 (from $50-67M to $5-17M), suggesting either a major revenue source was lost or that earlier years included extraordinary non-recurring events.

---

# III. THE TRAFFICKING OPERATION (Chronological)

## A. Victim Count and Demographics

| Source | Count | Time Period | EFTA |
|--------|-------|-------------|------|
| FBI Miami | 28 initially, "well over 30" | 2005-2007 | Multiple |
| SDNY | "Dozens," 5 Minor Victims designated | 2019-2021 | [EFTA00028785](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028785.pdf) |
| USVI AG | "Hundreds of young women and girls" | All years | [EFTA00018778](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018778.pdf) |
| Civil proceedings | Jane Doe up to #43 | Ongoing | Multiple |
| Victim journals | 35+ named abusers, 2 journals | ~1998-2006 | [EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf), [EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf) |
| NTOC Tips | 288+ tips received | 2019-2020 | [EFTA01660651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660651.pdf) |
| Allred FBI Package | 7+ victims in single attorney submission | 2020-2021 | [EFTA00013253](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013253.pdf) |

**Age range of documented victims:** 11-12 (youngest, per USVI AG) through early 20s (foreign women groomed through visa/TOEFL schemes).

The 14-year-old whose Grand Jury testimony is documented ([EFTA00008631](https://www.justice.gov/epstein/files/DataSet%206/EFTA00008631.pdf)) began traveling to NYC in 1996; Maxwell bought her "white cotton underwear... like little girls underwear," told her "there would be other young students like her who were also being mentored by Epstein," and invited her to New Mexico in "spring of 1996." A 15-year-old's victim impact statement ([EFTA00019994](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019994.pdf)) recounts being flown to Zorro Ranch in 2004 where Epstein "positioned me by laying me on his floor so that I was confronted by all the framed photographs on his dresser of him smiling with wealthy celebrities and politicians."

A comprehensive 30-page FBI evidence package ([EFTA00004070](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004070.pdf)) documents a victim born approximately January 1985 who met Epstein at age 17. She experienced four sexual assaults before turning 18 (in Paris, New Mexico, and Florida), including two rapes. She described a "harem ideology" where Epstein maintained multiple young women simultaneously. Jean-Luc Brunel was described as a "constant companion" during her time with Epstein. She identified Naomi Campbell as present on Little Saint James during her visits. She traveled with Epstein to Ecuador and attended a Robin Hood gala. She described Epstein's control as amounting to "mind control."

A witness described "12 year old girls flown from France for Epstein's birthday": "they were really poor over there, and their parents needed the money" ([EFTA00020703](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020703.pdf)). Epstein proposed that the witness "bear his child" in exchange for a mansion and monthly income, on the condition she "sign the child over to him" and the child would be "his and Ghislaine's." The victim escaped to Thailand, then Australia, and never returned.

## B. Victim Journals -- Two Handwritten Documents

### First Journal ([EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf))

A multi-page handwritten journal naming over 20 individuals including:
- **Leon Black:** "Mr. Black... threw me on the floor and blood all over Jeffreys carpet and I am the issue? Who the fuck bites someone?"
- **George Mitchell:** "even old senators like George Mitchell who you think would be good like a grandpa are bad"
- **Larry Summers:** "For being a Rockefeller that plane Mr. Dana had me on was scary! Both he and Larry Summers are fucking disgusting!"
- **Alan Dershowitz:** Referenced as "Allen Douschewitz" alongside "Mr. Caruthers" and "Mr. Islam" as direct abusers
- **Ted Leonsis, Steve Case, Dan Snyder:** Named alongside "The Gregorys" and "Mr. Colgan" in context of "flights of horror"
- **"Ms. Vicki":** Unidentified female facilitator operating in Florida and California, mentioned alongside Weinstein
- **"Mr. Robert and Jill":** Couple who hosted the party where victim first met Maxwell ("British lady from Clearwater")

The journal was forensically examined ([EFTA02731724](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731724.pdf)): "no evidence found for recent fabrication" though gel pen dating was inconclusive. DANY investigators "do not doubt her allegations" but "have not found any independent corroboration" for all named individuals.

### Second Journal ([EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf))

An 8-page second victim journal containing some of the most serious allegations in the corpus (note: DANY investigators had not independently corroborated all named individuals as of their assessment):
- **Ted Leonsis:** FILMED the abuse -- this is a direct accusation of creating CSAM
- **Jes Staley:** "used belt leaving bloody marks" -- physical violence during sexual assault
- **"Sauerkraut Krauss" and "Martin Minsky":** Named as participants
- **AOL:** "used to find us" -- an accusation that America Online's platform was used for victim recruitment
- **Forced pregnancy:** Epstein impregnated the victim and wanted the baby for eugenics purposes ("piano well = good genes"), then forced abortions
- **Four senior AOL executives** identified across both journals: Steve Case, Jim Kimsey, Ted Leonsis, George Vradenburg

The victim's description of aliases is forensically significant: she explicitly stated that names including "Mr. Mody, Mr. Robert, Mr. Sant, Mr. Ludwig, Mr. Cecchi, Mr. Mora, Mr. Goodlatte, Mr. Atkins" are "not who they say" -- confirming these are aliases. All have zero additional hits in the 218GB corpus, supporting her claim.

## C. MC2 Model Management

MC2 Model Management, founded by Jean-Luc Brunel in October 2005, operated offices in New York, Miami, and Tel Aviv. The MC2 website publicly stated its submission requirement: "Age: Between 13 and 20 years old" ([EFTA01728258](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01728258.pdf)). The website described an "international scouting division constantly searching for future new faces across the globe."

MC2 was the industrial-scale recruitment mechanism:
- **International scouting:** From Thailand, Dubai, UK, Eastern Europe, and Russia
- **Daniel Siad:** Identified as a key recruiter operating across multiple countries
- **Stranding Russian girls:** A Russian model wrote: "before MC2 had told me 3 weeks but its been more than a month... do you miss me at least a bit?" ([EFTA02439395](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02439395.pdf), June 2009) -- documenting the pattern of luring foreign women with short-term promises then extending their stay indefinitely
- **Apartment nexus:** MC2 housed models at 301 East 66th Street -- the same building containing Ehud Barak's apartment, trafficking victims, and Epstein corporate entities
- **Tel Aviv office:** Despite documented ages 13-20 recruitment, zero results for "MC2 Tel Aviv" appear in any database -- suggesting active suppression of records from this office

As late as October 30, 2017 -- nine years post-conviction -- active model scouting continued. An email described: "met through the manager at models, Skyped today - seems very nice. Will pass to the candidates list - we can meet her in Paris during the next trip. Will look for more photos" ([EFTA02575358](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02575358.pdf)).

## D. Recruitment Methods

**TOEFL/Visa Grooming ([EFTA02491935](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02491935.pdf), [EFTA02589100](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589100.pdf), [EFTA02474955](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02474955.pdf))**

Epstein used TOEFL exam preparation, singing lessons, visa sponsorship, and school enrollment as leverage over foreign young women. One victim responded: "becoming a mistress was the only one job proposition you were really serious about" and "Meeting Gates or Woody was great - thank you - will never forget it - although nobody hire me just because I have nice pictures with them." Her modeling career was destroyed by travel to Virgin Islands -- "my agency knows where I was going" ([EFTA02491935](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02491935.pdf)).

Another victim was berated for not retaking the TOEFL, with Epstein requiring "massage practice, typing, learning something of value" ([EFTA02589100](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589100.pdf), August 2014).

A Russian woman had her tourist visa canceled in May 2013 and was "stopped at airport, sent back to Russia." Epstein then requested her "passport photo" and "a naughty selfie please :))" in the same message ([EFTA02474955](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02474955.pdf), January 2016). Another woman was excited to meet Epstein in Paris, researching "language school to prepare TOEFL" ([EFTA02644771](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02644771.pdf)).

Pattern: TOEFL preparation, singing lessons, visa sponsorship, and school enrollment were systematically deployed as grooming tools for foreign young women, creating dependencies that made them vulnerable to exploitation.

**Victoria's Secret Pipeline**

Wexner's control of Victoria's Secret gave Epstein access to aspiring models. NTOC tips reference "other young girls and older Victoria's Secret models" at Epstein parties ([EFTA01660651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660651.pdf)). One NTOC tip described a caller who at age 16 while modeling attended 8 parties at Epstein's NY residence, where "three brothers" named Allen, Oren, and Tal participated in rapes. "Two twin brothers, Allen and Oren, lured caller and her friend upstairs." "Oren raped her best friend and a third brother, Tal, raped a 14 year old girl named Katie LNU" ([EFTA01660651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660651.pdf), [EFTA01660679](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660679.pdf)). The same caller described "big orgy parties" with "other young girls and older Victoria's Secret models, including Bill Clinton and Donald Trump."

**Art Scholarships and the NYAA Pipeline**

"Patron of the arts" and "scholarships for the arts" were used to access a 13-year-old: "Epstein bragged to her about being a patron of the arts and giving scholarships to talented young artists like Doe. Epstein and Maxwell probed her at length about her background, family situation and where she lived" ([EFTA00019101](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019101.pdf)). Over several months, "Epstein and Maxwell attempted to groom and mentor 13-year-old Jane Doe."

The New York Academy of Art served as a grooming pipeline. Eileen Guggenheim, NYAA Dean and Board Chair, was named alongside Trump, Andrew, and Dershowitz as an Epstein associate ([EFTA01652757](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652757.pdf)). Maria Farmer, a former NYAA student (1993-1995 MFA), filed the first-ever criminal complaint about Epstein with the FBI/NYPD in 1996. At her 1995 thesis show, Dean Guggenheim urged Farmer to sell Epstein/Maxwell a painting; Farmer had already sold it for $12,000 but was pressured to give Epstein half price. Epstein offered studio space, then arranged travel to Wexner's Ohio compound where sexual assault occurred.

**Victim Tracking Database**

Victims were tracked using a "database" for "availability and proximity" ([EFTA00016836](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016836.pdf)). A masseuse list recovered from seized devices contained "women and girls, some of which were identified minors." The FBI compiled and cross-referenced "black book, masseuse list, flight logs" shared among investigators ([EFTA00038620](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038620.pdf)). The prosecution memo documented Maxwell maintaining "binders of nude photos" used to track victims ([EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf)).

## E. NTOC Tips -- Scale of the Tip Line

The National Threat Operations Center (NTOC) received 288+ tips related to Epstein between July 2019 and early 2020 ([EFTA01660651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660651.pdf), [EFTA01660679](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660679.pdf)). These tips ranged from credible to uncorroborated but collectively demonstrate the scale of public awareness of Epstein's activities. Key tips include:

**Three Brothers (Allen, Oren, Tal):**
At age 16 while modeling, a caller attended 8 parties at Epstein's NY residence. "Two twin brothers, Allen and Oren, lured caller and her friend upstairs." "Oren raped her best friend and a third brother, Tal, raped a 14 year old girl named Katie LNU" ([EFTA01660651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660651.pdf), [EFTA01660679](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660679.pdf)). The same caller described "big orgy parties" with "other young girls and older Victoria's Secret models, including Bill Clinton and Donald Trump."

**Former Zorro Staff:**
A former staff member at the New Mexico ranch submitted a tip regarding video footage of minors. FBI treated the submission as potential extortion rather than evidence ([EFTA00038382](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038382.pdf)).

**Surveillance Tip:**
An individual reported observing Epstein with a "young girl" on Palm Beach bike paths in late 2018/early 2019 ([EFTA00020778](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020778.pdf)). Internal note: "nothing was done."

**William Barr Tips:**
Two separate NTOC tips referenced AG Barr: (1) "present during abuses" at a model event; (2) a separate encounter. Both appear on the FBI Prominent Names page ([EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf)).

**Prominent Names Compiled:**
The FBI compiled a master list of named individuals from NTOC tips and victim statements onto a single briefing page, assigning allegations to each name. This "Prominent Names" page was included in the master FBI briefing deck and represents the most concentrated evidence summary in the corpus.

## F. Gloria Allred / Victim Attorney Submissions

Attorney Gloria Allred and attorney Amber Wang submitted a victim scheduling package to the FBI ([EFTA00013253](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013253.pdf)) documenting 7+ victims in a single submission, including:
- A victim who described a 2010 interaction with Prince Andrew at Epstein's Manhattan townhouse
- A victim trafficked to "two other men at Epstein's direction"
- Multiple victims with overlapping time periods at the same properties
- FBI agents conducted scheduled interviews based on the Allred/Wang submissions
- The submissions demonstrate that new victim identification continued through 2020-2021

## G. The Eugenics/Pregnancy Program

Epstein's eugenics program is documented across multiple sources:
- The second victim journal describes Epstein impregnating the victim and wanting the baby for eugenics purposes: "piano well = good genes" -- suggesting musical ability indicated genetic fitness ([EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf))
- Forced abortions documented in the same journal
- A witness described Epstein proposing she "bear his child" in exchange for a mansion and monthly income, on the condition she "sign the child over to him" and the child would be "his and Ghislaine's" ([EFTA00020703](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020703.pdf))
- Southern Trust doing "DNA analysis" documented in corporate records ([EFTA00018441](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018441.pdf))
- $20,000 payment to the Transhumanist Association from Epstein entities ([EFTA00018441](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018441.pdf))
- Per New York Times reporting (July 31, 2019, included in FBI SDNY news clips at [EFTA00018441](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018441.pdf)), Epstein told scientists about plans to use the NM ranch to impregnate women with his sperm — described by the Times as an ambition to "seed the human race with his DNA," sourced to two scientists and a business adviser
- Harvard geneticist George Church met with Epstein in November 2018 -- seven months before arrest ([EFTA02264607](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02264607.pdf))
- The intersection of eugenics ideology, forced pregnancy, and control over victims' reproductive autonomy represents a uniquely disturbing dimension of the trafficking operation

## H. Properties and Routes

**Aircraft Fleet:**
- Boeing 727-200 ("The Lolita Express") -- the primary long-range aircraft
- Gulfstream G2B / G4 -- medium-range jets
- Gulfstream G550 (serial #5173, N212JE) -- held by Plan D LLC, funded by $45.5M from Haze Trust and BV70/Black
- Sikorsky S-76C-2 helicopter (originally "Air Ghislaine Inc," renamed "Shmitka Air Inc" in 2010)
- 13 aviation entities under RM CODE 82289 at Deutsche Bank

**Weekly Cycling Pattern:**
Teterboro (NJ) --> Palm Beach International (FL) --> Cyril E. King Airport (St. Thomas, USVI). When pilot David Rodgers learned a passenger's name after a flight, he "would use that passenger's name going forward but would not go back to add in that passenger's name on prior flight logs" ([EFTA02731168](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731168.pdf) p.7) — meaning the flight logs are incomplete records that undercount passenger appearances, particularly for individuals whose names Rodgers did not initially know. Larry Visoski coordinated all flight logistics through PLIST-documented emails, including the Marrakesh flight one week after the $25M Rothschild transfer ([EFTA02477179](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02477179.pdf)).

**CBP Bypass Infrastructure:**
A CBP Agriculture Specialist (Badge #CAS03223 / HashID #CZACMME) stationed at the pre-clearance port of Saint Thomas from 2008 for 7+ years walked into his supervisor's office on August 30, 2019 and admitted: "Everyone knew I was friends with Jeffery Epstein." He had been to Epstein's house, on his boat, flew in his helicopter. His supervisor described him as having "pal'd around with Mr. Epstein, clearing his aircraft; and spending personal time with the convict" ([EFTA00031495](https://www.justice.gov/epstein/files/DataSet%208/EFTA00031495.pdf)). The officer was later transferred to North Charleston, SC. FBI conducted a dedicated C-4 investigation with FBI and HSI partners ([EFTA00038585](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038585.pdf)), and SDNY proffer sessions in October-November 2020 with 2 FBI agents focused on CBP topics ([EFTA00020852](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020852.pdf)). A separate witness (via Crowell & Moring attorney Glen McGorty) proffered about "CBP employees helping Epstein bypass customs." A female acquaintance also filed a DOJ complaint accusing the officer of being a "known associate" who "assisted Mr. Epstein for conducting human trafficking." The officer's name remains redacted across all document collections despite exhaustive searches.

**Properties Used for Abuse:**
- **9 East 71st Street, Manhattan** -- 40-room mansion, formerly Wexner's, art-filled with surveillance equipment. FBI photos show multi-monitor control room, "24 HOUR VIDEO SURVEILLANCE" signs, massage tables with supplies
- **358 El Brillo Way, Palm Beach, FL** -- primary Florida abuse location, scene of original 2005 investigation
- **Little Saint James Island, USVI** -- private island with multiple buildings, compounds, and the distinctive blue-striped "temple" structure
- **Great St. James Island, USVI** -- purchased January 2016 for $5M, under active development with French architecture firm 3BIS as late as May 2019 ([EFTA02265056](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02265056.pdf))
- **49 Zorro Ranch Road, Stanley, New Mexico** -- Maxwell signed 1994 notarized document as "disinterested party" for land appraisal ([EFTA00030804](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030804.pdf)). NM AG requested asset forfeiture for facilitating "trafficking of children" ([EFTA00015190](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015190.pdf))
- **22 Avenue Foch, Paris, France** -- luxury apartment with interiors by Alberto Pinto, Atelier Meriguet catalog requested for renovation ([EFTA02116336](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02116336.pdf))
- **301 East 66th Street, Manhattan** -- the intelligence nexus building housing MC2 models, Barak's apartment, trafficking victims, Epstein corporate entities, and Shuliak's residence

## I. Photographic Evidence Database -- 21,859 Images

The investigation cataloged 21,859 images from the FBI evidence photos across all properties. Key statistical findings:

| Category | Image Count | Significance |
|----------|-------------|-------------|
| Nude references | 130 | Includes "NUDES," "Girl pics nude," victim photography |
| Massage references | 669 | Massage tables, supplies, rooms across properties |
| Surveillance/camera references | 876 | Control rooms, camera mounts, "24 HR VIDEO" signs |
| Property documentation | 5,000+ | Floor plans, room inventories, safe contents |
| Personal photos | 3,000+ | Travel, events, individuals at properties |
| Evidence chain documentation | 2,000+ | FBI seizure photos, chain of custody |

**Master Photo Index Page ([EFTA00004477](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004477.pdf)):**
The master index categorizes photo albums with these labels: "JE 50TH BD" (Epstein's 50th birthday), "THAIS, MOSCOW GIRLS," "NUDES," "YOGA GIRLS," "ZORRO" (Zorro Ranch), "RUSSIA," "BALI/THAILAND/ASIA." The geographic labels -- Thailand, Moscow, Russia, Bali -- map directly to the known international recruitment pipeline.

**Clinton Photo Archive ([EFTA00004577](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004577.pdf), [EFTA00005284](https://www.justice.gov/epstein/files/DataSet%203/EFTA00005284.pdf)):**
Over 300 photographs across continents were documented in albums with a notable interleaving pattern. The album labeled "St Trop/Clinton Morocco. Nude" ([EFTA00004577](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004577.pdf)) contains photos from Clinton/Morocco trips interleaved with Nudes001-164. A "JE & Clinton" Photoshop file was identified among evidence photos ([EFTA00005284](https://www.justice.gov/epstein/files/DataSet%203/EFTA00005284.pdf)). Never-before-seen photographs of "Bill Clinton's neck massaged by Jeffrey Epstein victim" were documented ([EFTA00037125](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037125.pdf)). The interleaving of Clinton travel photos with nude collections -- in the same album, sequentially numbered -- is forensically significant.

**Zorro Ranch Photos ([EFTA00004763](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004763.pdf), [EFTA00005191](https://www.justice.gov/epstein/files/DataSet%203/EFTA00005191.pdf), [EFTA00005284](https://www.justice.gov/epstein/files/DataSet%203/EFTA00005284.pdf)):**
Hundreds of photos labeled "Jean Luc Zorro" document Brunel's presence at the NM ranch. "29th bday at Zorro" contains 140+ photos. A Photoshop file titled "girlsonplane_img" at 7000x5600 pixels was found among Zorro Ranch photos alongside "Zorro Great Hall" Photoshop files ([EFTA00005284](https://www.justice.gov/epstein/files/DataSet%203/EFTA00005284.pdf)). The Photoshop file resolution suggests professional-grade image editing, not casual photography.

**FBI Search Photos -- Manhattan:**
FBI evidence photos from the July 6, 2019 search of 9 East 71st Street document the complete interior from basement to 14th floor. Key photos include:
- Multi-monitor surveillance control room ([EFTA00000015](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000015.pdf)-17): 4 large monitors, desk, keyboard, mouse, telephone
- "24 HOUR VIDEO SURVEILLANCE" signs on multiple doors
- Massage tables with supplies and oils
- Safe contents: Austrian passport, 48 diamonds, cash, nude photographs
- Custom chess set with Epstein as King
- Prison yard mural with Epstein at center
- Taxidermy tiger in library
- Rows of individually framed prosthetic eyeballs
- Arnaud Kasper hanging nude sculpture in wedding dress

**FBI Search Photos -- Little Saint James:**
Evidence photos from the August 2019 search document:
- IDF-branded clothing (sweatshirt, T-shirt) and white military dress uniform with medals (origin unidentified)
- Ornate ceiling murals depicting mythological scenes
- Blue-and-white striped "temple" structure with gold dome
- Computer equipment including Unifi Video NVR system
- "JE BIG LAPTOP" in branded bag

**Compact Discs from Safe ([EFTA00020141](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020141.pdf)):**
CDs labeled "Zorro" and "LSJ" (Little Saint James) were among items seized from the NYC safe. The presence of labeled CDs in a locked safe alongside the Austrian passport, diamonds, and nude photographs suggests they contained material Epstein considered sensitive enough to physically secure.

## J. AT&T Records Analysis -- 558 Pages

558 pages of AT&T records were produced under subpoena (EFTA from ATT_RECORDS_ANALYSIS.md). These records provide:

- **Call Detail Records (CDR):** Documenting numbers called, call duration, and timestamps for Epstein's telephone accounts
- **Cell-Site Location Information (CSLI):** Identifying which cell towers Epstein's mobile devices connected to, establishing geographic location patterns
- **Subscriber Information:** Account holder details, associated devices, service addresses

The AT&T records corroborate the weekly cycling pattern documented in flight logs: regular communication clusters at NYC-area cell sites, followed by Palm Beach-area sites, followed by USVI-area sites -- consistent with the Teterboro-PBI-USVI route. Communication intensity spiked during periods of known financial activity, paralleling the PLIST email-to-transaction correlation findings.

The records also document communication patterns during the November 2018 - February 2019 period. **CORRECTION (Revisit #48):** The jeevacation@gmail.com account did not go silent during this period -- DS9 documents show continuous daily email activity. The earlier characterization of a "99-day email blackout" was an artifact of the DS11 PLIST extraction methodology. The AT&T telephone records provide an additional communication channel for this period, complementing (rather than replacing) the email activity now confirmed through DS9.

## K. The Science and Technology Network

Epstein cultivated relationships with elite scientists and technologists through three primary channels:

### The Brockman/Edge Foundation Pipeline
Literary agent John Brockman hosted annual "Edge" dinners that served as Epstein's primary access point to technology billionaires and academic scientists:
- **2004 "Indian Summer" dinner:** Sergey Brin, Larry Page, and Jeff Bezos attended at Epstein's Manhattan townhouse ([EFTA00018466](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018466.pdf))
- Brockman-Epstein direct email correspondence continued through May 2015 discussing Sam Harris and Jennifer Doudna (CRISPR pioneer) ([EFTA02501737](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02501737.pdf))
- The Edge Foundation dinner circuit normalized post-conviction contact with Epstein among the scientific elite

### MIT Media Lab / Joi Ito
- Joi Ito received $2 million+ from Epstein entities ($1M Neoteny 3 LP + $1M+ direct, [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))
- Ito arranged a US Treasury call to include Epstein ([EFTA02589077](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589077.pdf)) -- giving a convicted sex offender access to federal financial policy discussions
- Dinner at Epstein's: Woody Allen at 7:30, Ito and Ed Boyden at 8:00, Tom Pritzker at 9:00 ([EFTA02377042](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02377042.pdf))
- Ito invited alongside Reid Hoffman to Columbus Day weekend at Epstein's property ([EFTA02575363](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02575363.pdf))
- Ito resigned from MIT Media Lab when payments were exposed (September 2019)
- Ed Boyden and Neil Gershenfeld organized the neuroscience dinner with David E. Shaw, Yann LeCun, John Hopfield, and Sebastian Seung -- guest list sent to "Jeff" for approval ([EFTA02114558](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02114558.pdf))

### Harvard / Genetics / Eugenics
- George Church (Harvard Medical School geneticist) met with Epstein in November 2018 -- seven months before arrest ([EFTA02264607](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02264607.pdf))
- Seth Lloyd (MIT quantum computing) maintained correspondence through March 2017: "Indeed it was awesome" ([EFTA02366597](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02366597.pdf))
- Lawrence Krauss (ASU, later removed for sexual misconduct): Epstein attempted to install as Chomsky trust trustee ([EFTA02570988](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570988.pdf))
- Noam Chomsky's trust managed with Epstein involvement
- Southern Trust doing "DNA analysis" and $20,000 payment to Transhumanist Association ([EFTA00018441](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018441.pdf))
- Per NYT reporting in [EFTA00018441](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018441.pdf): Epstein's plan to use the NM ranch to impregnate women with his sperm, described by two scientists and a business adviser
- Boris Nikolic (Gates chief science advisor, named executor in will): negotiated separation agreement mentioning "bgC3" ([EFTA02730265](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730265.pdf))

### The Cryptocurrency Network
- March 2014: Epstein and Reid Hoffman introduced to Austin Hill (crypto pioneer) regarding "incredible network of cryptographers, authentication & e-cash tech" ([EFTA02518909](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518909.pdf))
- February 2018: $15M to Blockchain Capital (three simultaneous wires to The 2017 Caterpillar Trust)
- LedgerX confidential pitch deck in Epstein's files ([EFTA01734786](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01734786.pdf))
- "Bitcoin troika" references ([EFTA02070051](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02070051.pdf))
- "Bitcoins for Mongolia" ([EFTA02069096](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02069096.pdf))
- "Epstein-Cryptology?" file referenced in three separate documents
- SPIEF 2014 USB drive seized from Manhattan safe (St. Petersburg International Economic Forum)

### The Political Access Network
Beyond science and technology, Epstein maintained political access through:
- Kathryn Ruemmler (former Obama White House Counsel): 15+ direct emails 2014-2018
- Bob Kerrey (former Senator): arranged Thiel-Burns lunch through Epstein ([EFTA02589110](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589110.pdf))
- George Mitchell (former Senate Majority Leader): Lesley Groff called State Department to locate him ([EFTA02522767](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02522767.pdf))
- Bill Richardson (former Governor): ongoing contact through 2012 per hidden redactions
- Terje Roed-Larsen (UN Special Envoy): CC'd on Gates Foundation proposal ([EFTA01745511](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01745511.pdf))
- Steve Bannon: MBS/Kushner intelligence exchange, Apple Watch gift, island visit ([EFTA02518865](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518865.pdf), [EFTA02271437](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02271437.pdf), [EFTA02273951](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02273951.pdf))
- Princess Mette of Norway: meeting referenced in PLIST metadata ([EFTA02570971](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570971.pdf))

## L. Co-Conspirators

**Ghislaine Maxwell:** Convicted December 2021 on five of six counts including sex trafficking of a minor. Sentenced to 20 years. The prosecution memo documented Maxwell's direct role in procuring victims: buying "little girls underwear" for a 14-year-old, directing victims to engage in sexual contact with named individuals (including "explicitly told her that she had to do to Glen what she did for Epstein" regarding Glenn Dubin), maintaining "binders of nude photos," directing saran-wrap photography as a birthday gift, and operating a healthcare proxy for Nadia Marcinkova. Maxwell told one victim "there would be other young students like her who were also being mentored by Epstein" ([EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf), [EFTA00008631](https://www.justice.gov/epstein/files/DataSet%206/EFTA00008631.pdf)). Her arrest in July 2020 at 301 Summer Street, Manchester-by-the-Sea, NH involved a 25-year UK Special Forces veteran security guard and a $1M bond ([EFTA00011172](https://www.justice.gov/epstein/files/DataSet%208/EFTA00011172.pdf)). Online investigators traced Maxwell through Borgerson-Angara-Tidewood shell companies using an r/maxwellhill Reddit screenshot that appeared in the FBI case serial ([EFTA02730741](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730741.pdf)).

**Sarah Kellen:** Named NPA co-conspirator. 11 documents with her Apple Mail IMAP mailbox paths (`imap://sarahk525@mail.mac.com/Sent%20Messages`) confirm her Mac computer exported emails -- establishing her active role as communications coordinator ([EFTA02310713](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02310713.pdf)). Key PLIST-documented action: "JE said we can cancel the hotel rooms in Menlo Park, CA... He's going to cancel the trip" (June 20, 2012). Her `.mac.com` email domain dates to Apple's pre-iCloud era (pre-2012), confirming long-term operational involvement.

**Nadia Marcinkova:** Zero results for her full name across 1.8 million redaction records -- selective identity redaction in internal FBI materials. She was found in a single DS10 document: [EFTA01525405](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01525405.pdf), though 200+ documents in the full-text corpus (court filings, NPA drafts, civil litigation) contain her name. The NPA explicitly provided that the USAO "will not request, initiate, or in any way encourage immigration authorities to institute immigration proceedings against Ross or Marcinkova" ([EFTA00176610](https://www.justice.gov/epstein/files/DataSet%209/EFTA00176610.pdf)). Received $100,000 wire from Butterfly Trust to Aviloop LLC two days after the Miami Herald series began ([EFTA00020685](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020685.pdf)) -- characterized by the government as potential witness tampering. A separate $250,000 wire went to another co-conspirator on December 3, 2018, three days later ([EFTA00028785](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028785.pdf)). Epstein "cut her hair, dyed it blonde, controlled her weight, selected her clothes" and maintained "a healthcare proxy assigning them responsibility if anything happened to her" ([EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf)). Directed to "engage in sexual contact" with Maxwell and Epstein at Virgin Islands residence. 124 documented flights. Two flights with Prince Andrew. Aviloop LLC listed as Subject 1 of 25 in the SAR investigation alongside Epstein shell entities.

**Lesley Groff:** Epstein's executive assistant. 40+ documents with PLIST metadata make her the heaviest Apple Mail user in the Epstein correspondence corpus. Called the US State Department searching for Senator George Mitchell ([EFTA02522767](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02522767.pdf)). Her attorney "indicated he would not bring Groff in for a proffer and had advised her to invoke her Fifth Amendment privilege" at a reverse proffer session on July 18, 2019. Coordinated flight bookings, staff scheduling, Richard Kahn's holiday schedule, World Cup tickets for "HHI" ($900 each, [EFTA02518838](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518838.pdf)), and 3BIS architecture meetings through May 2019.

**Jean-Luc Brunel:** MC2 founder. Died in French prison February 2022 before trial -- the pattern of both seriously prosecuted individuals (Epstein and Brunel) dying before trial completion. A witness described "12 year old girls flown from France for Epstein's birthday" ([EFTA00020703](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020703.pdf)). The 30-page FBI evidence package describes Brunel as a "constant companion" during one victim's time with Epstein, present during abuse in Paris, New Mexico, and Florida ([EFTA00004070](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004070.pdf)). Hundreds of photos labeled "Jean Luc Zorro" documented at Zorro Ranch ([EFTA00004763](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004763.pdf)).

## M. Witness Intimidation -- Comprehensive Documentation

The government detention memo ([EFTA00028785](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028785.pdf)) documented a systematic witness intimidation apparatus operating across physical, financial, online, and institutional channels:

### Physical Intimidation
- A victim's parent was "driven off the road" by a private investigator during the original Florida investigation
- Victims were told: "Those who help him will be compensated and those who hurt him will be dealt with"
- Private investigators were deployed against victims and their families during the 2005-2008 Florida investigation
- Maria Farmer, the first person to report Epstein to the FBI (1996), described years of harassment after filing her complaint

### Financial Intimidation
| Date | Amount | Recipient | Context | EFTA |
|------|--------|-----------|---------|------|
| Nov 30, 2018 | $100,000 | Aviloop LLC (Nadia Marcinkova) | 2 days after Miami Herald series began | [EFTA00020685](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020685.pdf) |
| Dec 3, 2018 | $250,000 | Another NPA co-conspirator | 5 days after Miami Herald series began | [EFTA00028785](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028785.pdf) |

Both payments were characterized by the government as potential witness tampering -- emergency disbursements to co-conspirators timed to the publication that reignited public scrutiny. The Aviloop payment from Butterfly Trust to Marcinkova's company was particularly notable because Butterfly Trust was the Epstein entity through which co-conspirator-linked payments flowed. Maxwell had been a Butterfly Trust beneficiary until late 2014, when she was deleted and replaced by Karyna Shuliak, Darren Indyke, and Richard Kahn ([EFTA01282297](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01282297.pdf), page 16: "DELETION AND ADDITION OF BENEFICIARIES").

### Online Threats
- Virginia Giuffre received death threats documented in a 424-document campaign by a person identified as "Tonks"
- The FBI collected 4chan materials, Reddit r/maxwellhill screenshots, and "Kid Q" PNG files as evidence ([EFTA00027732](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027732.pdf))
- Online investigators who helped trace Maxwell through Borgerson-Angara-Tidewood shell companies operated at personal risk

### Whistleblower Intimidation
- Christopher Dilorio, the SEC whistleblower who filed 16 documents connecting ESWW shell companies to Epstein-Apollo money flows three months before arrest, received "11-12 threatening anonymous phone calls" ([EFTA00009904](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009904.pdf)+)
- Dilorio's whistleblower submissions were filed with SEC Commissioners, DOJ, FINRA, and FinCEN
- He alleges the SEC dropped the Apollo investigation after a Kushner Jr./Joshua Harris White House meeting

### Mark Epstein Threats
- Mark Epstein (Jeffrey's brother) reported death threats connected to information he possessed about the case ([EFTA00037258](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037258.pdf))
- Mark Epstein urgently requested a meeting with Darren Indyke and access to the Paris property ([EFTA00037250](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037250.pdf))
- The threats were linked to information about Karl Erivan Haub, the German billionaire who disappeared in the Swiss Alps in April 2018

### Shredded Documents
- Per news reports (The Intercept, July 2019), shredded documents were observed outside Epstein's offices shortly before his arrest. No EFTA document in the DOJ release corroborates this specific claim. FBI emails from October 2019 confirm the Southern Trust office in St. Thomas had not yet been searched at that date ([EFTA00037409](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037409.pdf)).
- Separately, routine document shredding across Epstein entities (FTC, LSJ, Zorro, NES, JEGE, Hyperion, JEVIF) was documented as an ongoing office process as early as December 2014 ([EFTA01003392](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01003392.pdf)), and FBI evidence item #4 from the 2006 Palm Beach search was literally labeled "SHREDDED PAPER" ([EFTA01657859](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01657859.pdf)).
- Documented evidence destruction from other periods includes: computer removal before 2005 Palm Beach search, Maxwell directing shredding of directories, and lawyer directing associates not to talk to police ([EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf)).

### Pattern
The intimidation apparatus functioned across physical, financial, online, and institutional channels. Victims, witnesses, whistleblowers, and even family members were targeted. The timing of financial disbursements to co-conspirators -- within days of adverse publicity -- demonstrates a responsive, well-funded witness management operation that persisted through the final months before arrest.

## N. The SAR Investigation and Russian Models

A Suspicious Activity Report (SAR) investigation documented 25 subjects associated with Epstein's financial network, with Aviloop LLC (Marcinkova's company) listed as Subject 1 of 25 alongside Epstein shell entities. The SAR investigation included references to:
- Russian models brought to the United States through MC2 and independent channels
- One Russian model wrote: "before MC2 had told me 3 weeks but its been more than a month... do you miss me at least a bit?" ([EFTA02439395](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02439395.pdf), June 2009) -- documenting stranding of foreign women
- Another Russian woman had her tourist visa canceled in May 2013, was "stopped at airport, sent back to Russia" -- Epstein then requested her "passport photo" and "a naughty selfie please :))" in the same message ([EFTA02474955](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02474955.pdf), January 2016)
- A woman from beneath a failed redaction overlay wrote a five-page emotional email: "I'm not a toy Jeffrey" -- describing sexual transactional dynamics, a shoplifting arrest, failing model career, Westminster International University enrollment, and financial desperation ([EFTA01792918](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01792918.pdf))
- Photo album index page with categories including "THAIS, MOSCOW GIRLS," "NUDES," "YOGA GIRLS," "RUSSIA," "BALI/THAILAND/ASIA" ([EFTA00004477](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004477.pdf)) -- demonstrating geographic targeting of recruitment

The pattern: foreign women were recruited through modeling agencies and language programs, brought to the United States, had their immigration status controlled by Epstein, and were then trapped in sexual exploitation through financial dependency and visa manipulation.

## O. Trafficking Routes and Transportation Infrastructure

The Epstein operation maintained a dedicated air fleet and ground transportation network specifically designed to move victims between properties on a regular schedule.

### Aircraft Fleet

| Aircraft | Type | Registration | Holding Entity | Function | EFTA |
|----------|------|-------------|----------------|----------|------|
| Boeing 727-31 | Widebody jet ("Lolita Express") | N908JE | Southern Trust | Long-haul international transport | [EFTA00018778](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018778.pdf) |
| Gulfstream G550 | Long-range business jet | N212JE (serial #5173) | Plan D LLC | Primary domestic/Caribbean transport | [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) |
| Gulfstream II-B | Business jet | N17TP → Epstein | Purchased from Wexner below market | Early Florida-Caribbean shuttle | [EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf) |
| Helicopter | Sikorsky S-76B | N474AW | Little Saint James → Great Saint James | Inter-island transfer | [EFTA00018778](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018778.pdf) |
| Helicopter | Bell 430 | N620JE | Island-to-USVI airport | Airport connection | [EFTA00018778](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018778.pdf) |

### Weekly Cycling Route

The standard operational pattern (documented through flight logs, PLIST email metadata, and co-conspirator testimony):

```
WEEKLY CYCLE (documented 2013-2019):

Monday-Thursday:  9 East 71st Street, Manhattan (abuse sessions scheduled)
                  Teterboro Airport (NJ) for departures
                  |
Friday:           Fly Teterboro → Palm Beach International (PBI)
                  358 El Brillo Way, Palm Beach (weekend abuse sessions)
                  |
Saturday/Sunday:  Fly PBI → Cyril E. King Airport, St. Thomas, USVI
                  → Helicopter to Little Saint James Island
                  CBP pre-clearance at St. Thomas: Officer Badge #CAS03223
                  |
Monday morning:   Return flight St. Thomas → Teterboro
                  Cycle repeats
```

This cycling pattern was enabled by the CBP officer at St. Thomas who cleared Epstein's aircraft for over seven years, allowing passengers (including victims) to bypass standard customs and immigration scrutiny. The weekly regularity allowed scheduling of abuse sessions at each location with different victim pools.

### Pilot Retroactive Log Modification

**CORRECTION (Revisit #41):** [EFTA02731168](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731168.pdf) p.7 actually states that co-pilot David Rodgers would "NOT go back to add in that passenger's name on prior flight logs." Prosecutors cited this testimony to explain why flight records are incomplete -- passengers who boarded without being logged at the time were never retroactively added. This reflects negligent record-keeping, not deliberate sanitization. The names visible on the logs still represent a floor, not a ceiling, of who actually flew on Epstein's aircraft, but the incompleteness stems from lax practices rather than post-hoc tampering.

### International Routes Documented

Beyond the weekly domestic cycle, international trafficking routes were documented to:

| Destination | Property / Purpose | Key Evidence | EFTA |
|-------------|-------------------|--------------|------|
| Paris, France | 22 Avenue Foch (685 sq m) | Brunel "constant companion" during Paris abuse | [EFTA00004070](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004070.pdf) |
| Marrakesh, Morocco | Travel with Karyna: "you and Karyna only" | One week after $25M Rothschild transfer | [EFTA02477179](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02477179.pdf) |
| New Mexico, USA | Zorro Ranch (8,000+ acres) | Multiple minor victims, Maxwell 1994 land doc | [EFTA00030804](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030804.pdf) |
| St. Petersburg, Russia | "Tastey models and dancing" | Mandelson-Epstein exchange | [EFTA02571022](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02571022.pdf) |
| London, UK | Multiple addresses | MLAT request filed April 2020 | [EFTA00022062](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022062.pdf) |
| Milan, Italy | MC2 model apartments | Russian models stranded: "told me 3 weeks" | [EFTA02439395](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02439395.pdf) |
| Thailand/Bali/Asia | Photo album categories | "THAIS, MOSCOW GIRLS," "BALI/THAILAND/ASIA" | [EFTA00004477](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004477.pdf) |
| Ecuador | Travel with Brunel | 30-page victim package: Ecuador travel | [EFTA00004070](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004070.pdf) |

### Victim Tracking System

Victims described being tracked using a "database" for "availability and proximity" ([EFTA00016836](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016836.pdf)). A masseuse list recovered from seized devices contained "women and girls, some of which were identified minors" ([EFTA00038620](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038620.pdf)). FBI investigators shared the "black book, masseuse list, flight logs" among themselves as tools for identifying victims. The combination of a digital tracking system, scheduled routing, and multiple properties across jurisdictions created an industrial-scale trafficking logistics operation.

### The MC2 Recruiting Pipeline

MC2 Model Management publicly stated its submission requirements: "Age: Between 13 and 20 years old" ([EFTA01728258](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01728258.pdf)). The agency operated offices in New York, Miami, and Tel Aviv. MC2 served as the primary front for international victim recruitment, providing:
- Legal cover for bringing young women to the United States on J-1 visa waiver and B-1/B-2 tourist visas
- Housing at 301 East 66th Street (the same building as Barak's apartment and Epstein's corporate entities)
- A database of models available for "bookings" that functioned as a victim availability system
- Talent scout Daniel Siad, identified as recruiting from Thailand, Dubai, and the United Kingdom

As late as October 2017 -- nine years after conviction -- active model scouting continued: "met through the manager at models, Skyped today, will pass to the candidates list" ([EFTA02575358](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02575358.pdf)).

### Properties as Trafficking Infrastructure

Each Epstein property served a distinct function within the trafficking operation:

| Property | Holding Entity | Acquisition | Function in Operation | Key Evidence |
|----------|---------------|-------------|----------------------|--------------|
| **9 East 71st Street** | Maple Inc (USVI) | 1989 (Wexner); self-dealt 2011 | Primary abuse location (Manhattan); scheduling hub; surveillance center; art display for intimidation | [EFTA00000015](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000015.pdf)-17 (surveillance room), [EFTA00000167](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000167.pdf) (massage room), [EFTA00009448](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009448.pdf) (nude murals) |
| **358 El Brillo Way** | Laurel Inc | Pre-2005 | Palm Beach abuse location; 2005 police investigation origin; nine photographs in evidence | [EFTA00007157](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007157.pdf) (police report), [EFTA00021038](https://www.justice.gov/epstein/files/DataSet%208/EFTA00021038.pdf) (FBI search 2019) |
| **Little Saint James Island** | LSJE LLC | Pre-2000 | Caribbean abuse location; international visitor hosting; IDF-branded clothing + unidentified military uniform stored; Unifi Video NVR surveillance | [EFTA00001970](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001970.pdf)-71 (IDF-branded clothing), [EFTA00001969](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001969.pdf) (white uniform, origin unidentified), [EFTA00002946](https://www.justice.gov/epstein/files/DataSet%201/EFTA00002946.pdf) (temple), [EFTA00018778](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018778.pdf) |
| **Great Saint James Island** | Great St. Jim LLC | Jan 2016 ($5M) | Active development through May 2019 (3BIS architecture); Pritzker helped find landscape architect | [EFTA02265056](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02265056.pdf), [EFTA02644290](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02644290.pdf) |
| **22 Avenue Foch, Paris** | Not identified | Pre-2014 | European abuse location; Brunel "constant companion" during Paris abuse; Atelier Meriguet renovation | [EFTA00004070](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004070.pdf), [EFTA02116336](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02116336.pdf) |
| **Zorro Ranch, NM** | Zorro Management LLC | 1993 (Zorro Trust) | New Mexico abuse location; multiple minor victims; NM AG asset forfeiture requested | [EFTA00019994](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019994.pdf), [EFTA00030804](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030804.pdf), [EFTA00015190](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015190.pdf) |
| **301 East 66th St** | Epstein entities (Suite 10F) | Multiple units | MC2 housing + Barak apartment + trafficking victims + corporate entities + Shuliak residence | [EFTA02278459](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02278459.pdf), [EFTA00019513](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019513.pdf), [EFTA01378419](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01378419.pdf) |

The multi-property structure served several operational purposes: it distributed abuse across multiple jurisdictions (New York, Florida, USVI, New Mexico, France), it allowed different victim pools to be maintained at different locations without overlap, it provided plausible cover for travel ("business trip to the island"), and it ensured that no single law enforcement jurisdiction had full visibility into the scope of the operation. The weekly cycling pattern (Manhattan → Palm Beach → USVI) meant that victims at each location experienced abuse on a predictable schedule while the overall operation remained difficult for any single agency to investigate comprehensively.

## P. The Maxwell Conviction

Ghislaine Maxwell was convicted on December 29, 2021, on five of six counts:
- Count 1: Conspiracy to entice a minor to travel to engage in illegal sex acts (GUILTY)
- Count 2: Enticement of a minor to travel to engage in illegal sex acts (NOT GUILTY)
- Count 3: Conspiracy to transport a minor with intent to engage in criminal sexual activity (GUILTY)
- Count 4: Transportation of a minor with intent to engage in criminal sexual activity (GUILTY)
- Count 5: Sex trafficking conspiracy (GUILTY)
- Count 6: Sex trafficking of a minor (GUILTY)

Sentenced to 20 years in federal prison on June 28, 2022. Currently incarcerated at FCI Tallahassee.

The Maxwell prosecution memo ([EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf)) documented her direct role:
- Buying "little girls underwear" for a 14-year-old
- Directing victims to engage in sexual contact with named individuals
- "Explicitly told her that she had to do to Glen what she did for Epstein" regarding Glenn Dubin
- Maintaining "binders of nude photos" of victims
- Directing saran-wrap photography as a birthday gift
- Operating a healthcare proxy for Nadia Marcinkova
- Telling victims "there would be other young students like her who were also being mentored by Epstein"

Her arrest on July 2, 2020, at 301 Summer Street, Manchester-by-the-Sea, NH, involved:
- A 25-year UK Special Forces veteran as her security guard ($1,000,000 bond, [EFTA00011172](https://www.justice.gov/epstein/files/DataSet%208/EFTA00011172.pdf))
- Online investigators traced her through Borgerson-Angara-Tidewood shell companies
- An r/maxwellhill Reddit screenshot appeared in the FBI case serial ([EFTA02730741](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730741.pdf))
- A $20 million account transfer was documented during her hiding

---

# IV. THE NAMED INDIVIDUALS (Alphabetical, Evidence-Graded)

Each entry includes: document count, nature of evidence, strongest EFTA citation, evidence grade, and discrepancies between public statements and documentary evidence.

Evidence grading scale:
- **STRONGEST IN CORPUS** -- Multiple independent victim testimonies, financial documentation, prosecution records, and corroborating physical evidence
- **STRONG** -- Direct victim testimony or sworn depositions plus corroborating documentary evidence
- **MODERATE-STRONG** -- Substantial documentary evidence with some victim testimony or significant financial connections
- **MODERATE** -- Multiple documents showing ongoing relationship, post-conviction contact, or financial ties
- **LOW-MODERATE** -- Limited documentary evidence, single-source allegations, or presence without abuse allegations
- **WEAK** -- Single NTOC tip or unsubstantiated allegation with minimal corroboration

---

### PRINCE ANDREW, Duke of York
**Documents:** 30+
**Evidence Grade:** STRONG -- Victim testimony, MLAT request, systematic refusal to cooperate
**Key EFTA:** [EFTA00022062](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022062.pdf) (MLAT request to UK), [EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf) (Prominent Names page: 3 allegations)
**Relationship Origin:** Andrew's private secretary stated in a 2011 letter that "the Duke has known Mr Epstein since being introduced to him in the early 1990s." An FBI witness who worked for Epstein 1991-1998 independently corroborated this, reporting that an Epstein associate "bragged about massaging Prince Andrew twice on Martha's Vineyard in the early to mid-90s" ([EFTA00038586](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038586.pdf)). Andrew later claimed in his BBC Newsnight interview (November 2019) that he met Epstein in 1999 through Maxwell — contradicting his own palace's earlier, closer-to-event statement. A seized Maxwell email from March 2002 shows Maxwell acting as Andrew's social coordinator for a Peru trip, demonstrating an established familiarity by that date ([EFTA00011441](https://www.justice.gov/epstein/files/DataSet%208/EFTA00011441.pdf)).
**Evidence:** Three separate allegations on the FBI Prominent Names page ([EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf)): a victim instructed to "make Prince Andrew happy," a witness observing Andrew "grinding against a young girl" on Epstein's island, and a claim about encounters on Epstein's plane. MLAT request filed April 2020 to the United Kingdom stating "there is evidence that Prince Andrew engaged in sexual conduct involving one of Epstein's victims" while noting he was "not presently a target" ([EFTA00022062](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022062.pdf)). The MLAT requested Andrew provide "a list of all dates of travel or visits" to Epstein's properties — indicating the FBI sought but did not independently possess this information. The MLAT simultaneously covered both Epstein and Peter Nygard investigations. Andrew systematically refused cooperation with US investigators through counsel at Blackfords LLP, documented across months of correspondence ([EFTA00017042](https://www.justice.gov/epstein/files/DataSet%208/EFTA00017042.pdf), [EFTA00017743](https://www.justice.gov/epstein/files/DataSet%208/EFTA00017743.pdf), [EFTA00022980](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022980.pdf)). Two flights with Nadia Marcinkova documented. One victim described a 2010 interaction at Epstein's Manhattan townhouse. Never charged. Civil settlement with Giuffre in February 2022 contained no admission of wrongdoing.

### WILLIAM BARR, Attorney General
**Documents:** 55+
**Evidence Grade:** MODERATE -- NTOC tip, institutional conflict, oversight failures
**Key EFTA:** [EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf) (Prominent Names: "present during abuses" + model event encounter), [EFTA00028149](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028149.pdf) (split recusal)
**Evidence:** NTOC tip alleged Barr was "present during abuses" at a model event. His father Donald Barr hired Epstein at the Dalton School in the early 1970s; employment records "could not be located." Barr refused to recuse himself from the Epstein case despite his prior partnership at Kirkland & Ellis -- the firm that negotiated Epstein's NPA. He ordered the Southern District of Florida recused from Epstein criminal matters ("ordered recused by the DOJ") while retaining personal oversight -- a split recusal allowing him to maintain control over the case ([EFTA00028149](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028149.pdf)). No final FBI or OIG report on Epstein's death was ever issued under his watch. The two MCC guards were given deferred prosecution agreements under Barr's DOJ, with charges subsequently dismissed.
**Discrepancy:** Barr publicly stated he had recused himself. The documentary evidence shows a split recusal that preserved his authority over the death investigation.

### EHUD BARAK, Former Israeli Prime Minister
**Documents:** 14+ direct contact
**Evidence Grade:** STRONG -- Physical infrastructure overlap, financial ties, intelligence nexus
**Key EFTA:** [EFTA02278459](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02278459.pdf) (Epstein staff cleaning "Ehud's apt" at 301 E 66th), [EFTA00362483](https://www.justice.gov/epstein/files/DataSet%209/EFTA00362483.pdf) (calendar showing same-day visit with Black, Summers, Thiel)
**Relationship Origin:** Barak has publicly stated he was introduced to Epstein in 2003 by former Israeli President Shimon Peres at a Washington event. No EFTA document independently corroborates a specific 2003 meeting. However, pre-2010 indicators confirm the relationship predates the earliest direct documentary evidence: by 2009, attorneys in a victim civil suit deposition already knew about the Barak connection ([EFTA00159250](https://www.justice.gov/epstein/files/DataSet%209/EFTA00159250.pdf)), and a July 2010 article in the FBI files identified Barak as a "prominent passenger on [Epstein's] private jets" based on pilot logs from civil discovery ([EFTA00206574](https://www.justice.gov/epstein/files/DataSet%209/EFTA00206574.pdf)). The earliest direct EFTA documentary evidence is September 2010 ([EFTA02422168](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02422168.pdf), [EFTA02422165](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02422165.pdf)), showing Epstein acting as a social broker for Barak — a fully established relationship, not an introduction. Documented correspondence runs through March 2019.
**Evidence:** Maintained an apartment at 301 East 66th Street -- the same building housing MC2 model apartments, trafficking victims, and Epstein corporate entities. Epstein's staff cleaned "Ehud's apt" on Epstein's direct orders ([EFTA02278459](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02278459.pdf), March 2019). Epstein brokered a Barak-Bannon meeting in February 2019, months before arrest ([EFTA02633609](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02633609.pdf)). Most likely match for the "foreign president" referenced in victim compilations ([EFTA00022133](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022133.pdf)) based on 14+ direct contact documents -- more than any other foreign head of state. Named on single calendar day alongside Leon Black, Larry Summers, and Peter Thiel visiting Epstein ([EFTA00362483](https://www.justice.gov/epstein/files/DataSet%209/EFTA00362483.pdf), September 22, 2014). IDF-branded clothing (sweatshirt and T-shirt) found on Little Saint James during FBI search ([EFTA00001970](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001970.pdf)-71); a white military dress uniform with medals was found in the same wardrobe but its national origin is not identified ([EFTA00001969](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001969.pdf)). Barak admitted publicly to visiting Epstein's island and Manhattan townhouse but denied any knowledge of wrongdoing.
**Discrepancy:** Barak claimed visits were for business discussions. Documentary evidence shows his apartment was in the building infrastructure of a sex trafficking operation, cleaned by Epstein's staff.

### STEVE BANNON
**Documents:** 30+
**Evidence Grade:** MODERATE-STRONG -- Text messages, travel planning, intelligence brokering, gift exchange
**Key EFTA:** [EFTA00027290](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027290.pdf) (Bannon-Epstein texts on iPhone 7), [EFTA02518865](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518865.pdf) ("breakfast with Jared" re MBS visit)
**Evidence:** Text messages between Bannon and Epstein found on Bannon's iPhone 7 during the WBTW case Cellebrite review (April 2021). AUSA determined they were "not responsive to our warrant" -- no separate warrant was ever sought. Content has never been reviewed by anyone on the Epstein case ([EFTA00027290](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027290.pdf)). A Trump-Maxwell photo was found on the same phone; prosecutor said "no need to do anything with this one" ([EFTA00025553](https://www.justice.gov/epstein/files/DataSet%208/EFTA00025553.pdf)). Epstein sent Bannon an Apple Watch via FedEx to Washington through his son Sean (January 2019, [EFTA02271437](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02271437.pdf)). Bannon told Epstein "To have breakfast with Jared" regarding the MBS Saudi visit (February 2018, [EFTA02518865](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518865.pdf)). Michael Wolff emailed Epstein about a "six-hour dinner I had with Ailes and Bannon last week at my house" (January 2017, [EFTA02664993](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664993.pdf)). Bannon appeared on the January 2019 island guest list alongside Junkermann, Sultan bin Sulayem, and Eduardo Teodorani ([EFTA02273951](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02273951.pdf)). A mock interview YouTube video between Epstein and Bannon vanished before investigators could view it ([EFTA00037236](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037236.pdf)).
**Discrepancy:** No public statements from Bannon about the relationship. The texts on his phone have never been disclosed.

### LEON BLACK
**Documents:** 100+
**Evidence Grade:** STRONGEST IN CORPUS -- Financial, victim testimony, prosecution records, video allegation
**Key EFTA:** [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) (financial exhibits), [EFTA02731488](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731488.pdf) (FBI: "16 when raped by Black"), [EFTA02731576](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731576.pdf) (victim direct text: "You sexually harassed me, sex trafficked me, raped me")
**Evidence:** Paid $168 million to Epstein entities through the same Deutsche Bank infrastructure that funded trafficking. Four or more victims with consistent allegations of violent sexual assault, including distinctive biting of genitalia independently corroborated by a second victim who contacted attorneys in August 2022 and described "almost a perfect match" of Black's specific violent sex acts -- "nothing publicly out there about the details, so there is no way she could know" ([EFTA02731729](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731729.pdf)). FBI prosecution notes document a 16-year-old "violently raped by Black" at the townhouse with "adult sex toys in victim's rectum and vagina," victim bleeding, refused medical attention, "would not take her to the doctor," and flew her out the next day ([EFTA02731488](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731488.pdf)). Victim's direct text to Black: "You sexually harassed me, sex trafficked me, raped me, and eventually blacklisted me... forced to sign under duress" ([EFTA02731576](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731576.pdf)). Victim journal: "Mr. Black... threw me on the floor and blood all over Jeffreys carpet and I am the issue? Who the fuck bites someone?" ([EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf)). Calendar entry: "Drive to Leon Blacks house with Karyna" ([EFTA01928406](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01928406.pdf)). Victim was trafficked "to at least 25 different men" with her biological mother described in FBI notes as having: "forced [victim] to perform sexual acts with adult men since she was very young. Her younger sister also. Even worse, the paternal grandfather... was in on it" ([EFTA02731488](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731488.pdf)). Wigdor Law attorney reported "at least one video circulating on some disgusting sex site" showing 6 men at a hotel, victim with 3 of them, "one is a former friend of Leon Black's" ([EFTA02731515](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731515.pdf)). Paid $62.5 million to USVI in settlement ([EFTA02731484](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731484.pdf)). SDNY opened investigation May 2021 from Maxwell spinoff ([EFTA02731604](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731604.pdf)); DANY investigated independently with ADAs Wimmer, Puzio, and Saxtein. "US v. Black" appeared in SDNY file sharing system through October 2024. Brad Edwards -- prominent victims' attorney -- was retained BY Black in October 2024 ([EFTA02731577](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731577.pdf)). Managed Black's $2.7 billion art collection (935 works, 2016 Christie's appraisal). Emailed Epstein December 21, 2016: "lets liquidate the J BLACK trust... deal with wechsler telling at least joe, and probably others that there are 'sensitive accounts'" ([EFTA02664953](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664953.pdf)). **No criminal charges ever filed.** SDNY: "I'm not inclined to open based on the other victim" ([EFTA02731578](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731578.pdf)).
**Discrepancy:** Black publicly claimed payments to Epstein were for "tax advice and estate planning." The $168M total, absence of post-2013 service agreement, and refusal to answer Senate questions are inconsistent with this characterization.

### BILL CLINTON
**Documents:** 300+ photos, 20+ documents
**Evidence Grade:** MODERATE -- Extensive photographic archive, flight records, no direct abuse allegations in DOJ investigative files
**Key EFTA:** [EFTA00004577](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004577.pdf) (photo album "St Trop/Clinton Morocco. Nude"), [EFTA00037125](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037125.pdf) (neck massage photos)
**Evidence:** 300+ photographs across continents documented in albums interleaving Clinton/Morocco photos with nude collections. Photo album labeled "St Trop/Clinton Morocco. Nude" ([EFTA00004577](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004577.pdf)). "JE & Clinton" Photoshop file identified among evidence ([EFTA00005284](https://www.justice.gov/epstein/files/DataSet%203/EFTA00005284.pdf)). Never-before-seen photographs of "Bill Clinton's neck massaged by Jeffrey Epstein victim" ([EFTA00037125](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037125.pdf)). Victim journal mentions Clinton receiving "orgy invitation" in FBI briefing context ([EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf)). Epstein and Maxwell strategized about Clinton dinner testimony: "total 100 percent fabrication" ([EFTA02513978](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02513978.pdf)). NTOC tips compilation includes multiple references. No direct sexual abuse allegations against Clinton appear in the DOJ investigative files themselves, though victim statements reference his presence and the extensive photographic record shows deep social engagement.
**Discrepancy:** Clinton initially denied flying on Epstein's plane more than "four times." Flight logs show 26+ flights.

### ALAN DERSHOWITZ
**Documents:** 40+
**Evidence Grade:** STRONG -- Blanket co-conspirator immunity expansion, multiple victim accusations, conflict of interest
**Key EFTA:** [EFTA00009016](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009016.pdf) (Acosta deposition: NPA negotiations), [EFTA00009116](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009116.pdf) (defense team pressure on Acosta)
**Evidence:** Part of the defense team that negotiated the NPA, during which the co-conspirator immunity clause was expanded from its original draft ([EFTA00009016](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009016.pdf)). Allegations against Dershowitz by victims emerged publicly in 2014 court filings — years after the 2007-2008 NPA negotiations. Whether the blanket immunity was designed to protect any specific individual cannot be established from available documents. The defense team raised the prospect of a book chapter on prosecutorial overreach to pressure Acosta ([EFTA00009116](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009116.pdf); specific team member not identified). Victim journals reference "Allen Douschewitz" alongside "Mr. Caruthers" and "Mr. Islam" as direct abusers ([EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf)). Named in the 9-page victim accusation compilation ([EFTA00022133](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022133.pdf)). Never investigated despite multiple victims naming him.
**Discrepancy:** Dershowitz was part of the defense team that negotiated blanket immunity while victims would later name him as an abuser — a timeline that raises questions about conflict of interest, though this was never formally investigated.

### GLENN & EVA DUBIN
**Documents:** 54
**Evidence Grade:** STRONG -- Prosecution testimony, continuing relationship, medical facilitation
**Key EFTA:** [EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf) (FBI 302: "Maxwell told her to massage Glen and Eva Dubin"), [EFTA02474963](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02474963.pdf) ("Happy Birthday turtle!")
**Evidence:** FBI 302 documents Maxwell directing a victim: "explicitly told her that she had to do to Glen what she did for Epstein." Victim used the term "lent out" to describe being trafficked to the Dubins and other men -- she began using drugs due to the frequency. Government was "unable to corroborate" the lent-out accounts; named men "vociferously denied." Eva Dubin (MD) used medical credentials in connection with Epstein operations, helping prepare visa documentation ([EFTA01915127](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01915127.pdf)). July 2010: Eva and Epstein discussed typhoid vaccination for Africa travel ([EFTA01786466](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01786466.pdf)). Pet name "turtle" used eight years post-conviction: "Happy Birthday turtle! I promise not to tell Woody!!" ([EFTA02474963](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02474963.pdf), January 2016). January 2017: continuing contact -- "i have some questions, im in palm" ([EFTA02664996](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664996.pdf)). "keepers_Glen_Dubin_08-10-18.pdf" file maintained by Epstein one year before arrest -- a dossier suggesting potential blackmail material. 34+ documented flights. No investigation ever opened.
**Discrepancy:** The Dubins denied any improper contact. Documentary evidence shows Eva Dubin using her medical credentials in Epstein's operations and maintaining intimate pet-name correspondence 8+ years post-conviction.

### BILL GATES
**Documents:** 20+
**Evidence Grade:** MODERATE -- Post-conviction meetings, foundation engagement, victim statement
**Key EFTA:** [EFTA02532935](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02532935.pdf) ("Bill Gates will be here on monday night"), [EFTA02546928](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02546928.pdf) (Gates Foundation Deputy Director "due diligence")
**Evidence:** Gates Foundation Deputy Director Gabrielle Fitzgerald conducted "private donor engagement" with Epstein post-conviction; Boris Nikolic (Gates science advisor) joked "she is doing due diligence on your ass" ([EFTA02546928](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02546928.pdf)). A TOEFL-groomed victim stated: "Meeting Gates or Woody was great - thank you - will never forget it - although nobody hire me just because I have nice pictures with them" ([EFTA02491935](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02491935.pdf)). "Proposal for BMGF" (Bill & Melinda Gates Foundation) coordinated through Epstein with UN diplomat Terje Roed-Larsen CC'd ([EFTA01745511](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01745511.pdf)). Boris Nikolic was named as a successor executor in Epstein's will; Nikolic-Epstein negotiated a separation agreement mentioning "bgC3" (Gates think tank, [EFTA02730265](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730265.pdf)). Epstein invited Nikolic alongside others to Columbus Day weekend ([EFTA02575363](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02575363.pdf)).
**Discrepancy:** Gates publicly stated his meetings with Epstein were about philanthropy. The documentary evidence shows broader social engagement, foundation-level "due diligence," and a victim who met Gates through Epstein's introduction.

### REID HOFFMAN
**Documents:** 10+
**Evidence Grade:** MODERATE -- Crypto introduction, social engagement post-conviction
**Key EFTA:** [EFTA02518909](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518909.pdf) (Hoffman introduced to Austin Hill for "cryptography/e-cash tech"), [EFTA02575363](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02575363.pdf) (Columbus Day weekend invitation)
**Evidence:** Epstein brokered an introduction between Hoffman and crypto pioneer Austin Hill regarding "incredible network of cryptographers, authentication & e-cash tech" (March 2014, [EFTA02518909](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518909.pdf)). Invited alongside Joi Ito to Columbus Day weekend at Epstein's property ([EFTA02575363](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02575363.pdf)). Hoffman publicly apologized for his association with Epstein but the documentary evidence shows ongoing social engagement through 2018.

### JOI ITO
**Documents:** 15+
**Evidence Grade:** STRONG -- Financial, operational, US Treasury access
**Key EFTA:** [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) ($2M+ in payments), [EFTA02589077](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589077.pdf) (Ito arranging Treasury call with Epstein)
**Evidence:** Received $2 million+ from Epstein entities ($1M Neoteny 3 LP + $1M+ direct, [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf)). Arranged a US Treasury call to include Epstein post-conviction ([EFTA02589077](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589077.pdf)). Dinner guest at Epstein's with Woody Allen at 7:30, Ito and Ed Boyden at 8:00, Tom Pritzker at 9:00 ([EFTA02377042](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02377042.pdf)). Epstein took Woody Allen to MIT specifically to meet Ito ([EFTA02377050](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02377050.pdf)). Invited alongside Reid Hoffman to Columbus Day weekend ([EFTA02575363](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02575363.pdf)). Resigned from MIT Media Lab when payments were exposed.

### NICOLE JUNKERMANN
**Documents:** 15+
**Evidence Grade:** MODERATE -- MC2 connection, Leon Black introduction, island guest
**Key EFTA:** [EFTA02435071](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02435071.pdf) (Epstein brokered Junkermann-Black intro), [EFTA02273951](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02273951.pdf) (Jan 2019 island guest list)
**Evidence:** 10+ year relationship (2009-2019). Epstein brokered her introduction to Leon Black: "He said he will take you to lunch or dinner" (November 2009, [EFTA02435071](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02435071.pdf)). On January 2019 island guest list alongside Bannon, Sultan bin Sulayem, Eduardo Teodorani, and Jabor Yousuf -- five months before arrest ([EFTA02273951](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02273951.pdf)). Connected to Auctionata/Paddles art auction discussion (December 2016, [EFTA02664994](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664994.pdf)). Phone contact "Can u speak?" from iPhone 16 months pre-arrest (March 2018, [EFTA02513966](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02513966.pdf)). Same January 2019 email mentions 3BIS architecture firm wanting to visit the island for development.

### LAWRENCE KRAUSS
**Documents:** 10+
**Evidence Grade:** MODERATE -- Named in victim journal, Chomsky trust, ASU harassment coaching
**Key EFTA:** [EFTA02570988](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570988.pdf) (Epstein installing Krauss as Chomsky trust trustee), [EFTA02518850](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518850.pdf) (coaching Krauss on harassment damage control)
**Evidence:** Victim journal names "Sauerkraut Krauss" ([EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf)). Epstein attempted to replace a trustee with Krauss in Noam Chomsky's trust: "I would like to replace Max with Lawrence Krauss as trustee" (November 2017, [EFTA02570988](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570988.pdf)). Epstein coached Krauss on damage control after sexual harassment allegations at ASU ([EFTA02518850](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518850.pdf)). Krauss was eventually removed from ASU in 2019 over sexual misconduct allegations unrelated to Epstein.

### RONALD LAUDER
**Documents:** 900+ mentions in DOJ files
**Evidence Grade:** MODERATE -- Art transactions, joint entity, MoMA board overlap
**Key EFTA:** Friends Ventures LLC documentation (joint Black/Lauder entity for $25M Schwitters)
**Evidence:** Epstein coordinated Friends Ventures LLC (2014) for joint Black/Lauder art ownership of Kurt Schwitters "Ja-Was?-Bild" valued at $25 million, each owning 50%. Succession planning documented: "It is assumed that on Leon's death, Ronald Lauder will purchase Leon's 50% interest for $12,500,000." Both are MoMA Board trustees; Black stepped down as Chairman March 2021. 900+ mentions across the DOJ files, though most are incidental references. Lauder is Estee Lauder heir, Neue Galerie founder, and major Trump donor.

### HOWARD LUTNICK
**Documents:** 5+
**Evidence Grade:** WEAK -- Single NTOC tip, no sexual allegations, source identified as disgruntled employee
**Key EFTA:** [EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf) (Prominent Names: $10 house claim)
**Evidence:** Single NTOC tip from Simon Andriesz, identified as a disgruntled employee. Allegation of purchasing a $10 house from Epstein -- a financial claim, not a sexual allegation. The only person on the FBI Prominent Names page without any sexual allegation. No corroborating evidence found across any database.

### PETER MANDELSON (Lord Mandelson)
**Documents:** 20+
**Evidence Grade:** MODERATE -- Moscow penthouse, "tasty models," Congo nexus, Staley drinks
**Key EFTA:** [EFTA02434424](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02434424.pdf) (Moscow City penthouse with "Oleg"), [EFTA02571022](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02571022.pdf) ("tastey models and dancing")
**Evidence:** Mandelson forwarded Moscow City penthouse details to Epstein, mentioning "Oleg has a great woman who looks after things for him" -- likely Oleg Deripaska (November 2009, [EFTA02434424](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02434424.pdf)). "Tastey models and dancing" exchange with Epstein referencing St. Petersburg (May 2013, [EFTA02571022](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02571022.pdf)). Congo official Andely: "will report to Jean-Yves Ollivier and Peter Mandelson" about meeting cancellation with "Peter and Jeffrey" (January 2011, [EFTA02323048](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323048.pdf)). Drinks with Jes Staley and Epstein documented (December 2009, [EFTA02434434](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02434434.pdf)). Stayed at Epstein's NY townhouse while Epstein was in prison ([EFTA00037176](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037176.pdf)). David Mitchell received ~$476K in recurring payments and was connected to Mandelson through email chains. George Delson / Lawrence Delson connected to Mandelson advisory role.

### GEORGE MITCHELL, Former Senate Majority Leader
**Documents:** 15+
**Evidence Grade:** STRONG -- Victim journal, sworn testimony, State Department search, 9-page compilation
**Key EFTA:** [EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf) (victim journal: "even old senators like George Mitchell who you think would be good like a grandpa are bad"), [EFTA00022133](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022133.pdf) (9-page victim accusation compilation)
**Evidence:** Victim journal directly names Mitchell in the context of abuse. 9-page victim accusation compilation includes Mitchell alongside Richardson, Minsky, and Brunel ([EFTA00022133](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022133.pdf)). Lesley Groff called the US State Department searching for Senator Mitchell, who had returned to law firm DLA Piper ([EFTA02522767](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02522767.pdf)). Sworn deposition testimony names Mitchell as someone Maxwell "directed" a victim to have sexual contact with. Mitchell's public denials were never formally tested -- he was never subpoenaed or charged.
**Discrepancy:** Mitchell denied any improper conduct. He was never required to testify under oath about the specific allegations.

### TOM PRITZKER
**Documents:** 15+
**Evidence Grade:** MODERATE-STRONG -- 10-year documented relationship through March 2019, island development
**Key EFTA:** [EFTA02633147](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02633147.pdf) (Pritzker-Epstein March 2019: "shit hurricane"), [EFTA02644290](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02644290.pdf) (finding architects for "new guest island")
**Evidence:** Documented relationship spanning 2009-2019. "Lots to gab about" (October 2009, [EFTA02438541](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02438541.pdf)). Dinner party at Epstein's: Woody Allen at 7:30, Ito/Boyden at 8:00, Pritzker arriving at 9:00 PM (May 2013, [EFTA02377042](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02377042.pdf)). Epstein to Pritzker: "He really liked you. You are amazing" (September 2014, [EFTA02588577](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02588577.pdf)). Helped Epstein find landscape architect (Debbie Nevins) for Great St. James Island development: "Can I find islands on google earth?" (July 2017, [EFTA02644290](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02644290.pdf)). Four months before arrest: "trying to keep my head down in a shit hurricane." Pritzker: "Maybe breakfast on Tuesday?" (March 2019, [EFTA02633147](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02633147.pdf)). Hidden redactions reveal: calendar "Breakfast w/Tom Pritzker" ([EFTA02023850](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02023850.pdf)), "Who to organize Pritzker dinner?" ([EFTA02042557](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02042557.pdf)), "Global Hyatt Corp. Pritzker Nick" suggesting broader Pritzker family/Hyatt corporate involvement ([EFTA02163640](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02163640.pdf)).
**Discrepancy:** No public statements from Pritzker about the relationship. The March 2019 breakfast plans demonstrate continued engagement after the Miami Herald series.

### BILL RICHARDSON, Governor of New Mexico
**Documents:** 20+
**Evidence Grade:** STRONG -- Sworn testimony, prosecutor frustration, never formally cleared, Zorro Ranch nexus
**Key EFTA:** [EFTA00027244](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027244.pdf) (AUSA contradicting clearance claim), [EFTA00024683](https://www.justice.gov/epstein/files/DataSet%208/EFTA00024683.pdf) (Richardson videoconference with blanket denials)
**Evidence:** Sworn deposition (May 2016): victim named Richardson as someone "GM directed her to have sex with" -- unsealed August 2019 by Judge Preska. AUSA directly contradicted Richardson lawyer's public claim of clearance: "I don't think it's accurate to infer or interpret from my description that Governor Richardson is in none of [target/subject/witness categories]" ([EFTA00027244](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027244.pdf)). SDNY internal frustration: "This is so, so frustrating" over Richardson counsel releasing misleading public statement ([EFTA00014372](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014372.pdf)). Richardson presented polygraph results and blanket denials in May 2021 videoconference, claiming "Never met any women through JE or GM" and "Catastrophic impact on reputation, finances" ([EFTA00024683](https://www.justice.gov/epstein/files/DataSet%208/EFTA00024683.pdf)). NM AG Hector Balderas requested asset forfeiture of Zorro Ranch for facilitating "trafficking of children" ([EFTA00015190](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015190.pdf)), then agreed to "cease any investigation into sex trafficking" and defer to federal prosecutors ([EFTA00019183](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019183.pdf)). Maxwell signed 1994 notarized document as "disinterested party" for Zorro land appraisal ([EFTA00030804](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030804.pdf)). Multiple victims documented as abused at Zorro Ranch. Hidden redactions in DS10 reveal emails between Epstein and "Governor Richardson" and "dinner tonight with Richardson" extending through 2012 — demonstrating continued social contact years after Richardson's governorship. Richardson was never subpoenaed, never formally cleared, and never charged. He died in September 2023.
**Discrepancy:** Richardson publicly stated he had been "cleared" by prosecutors. The documentary evidence explicitly contradicts this claim.

### KATHRYN RUEMMLER, Former Obama White House Counsel
**Documents:** 29+
**Evidence Grade:** MODERATE-STRONG -- 15+ direct emails, intelligence brokering, "Clinton Obama" warning
**Key EFTA:** [EFTA02484285](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02484285.pdf) ("clinton obama unnecessary implication"), [EFTA02575359](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02575359.pdf) (sealed indictment query)
**Evidence:** 15+ OCR documents with direct Epstein-Ruemmler communications spanning September 2014 through January 2018. Epstein warned Ruemmler: "defense counsel might create Clinton Obama unnecessary implication... either way I appreciate the help but we should be extra thoughtful" (October 2015, [EFTA02484285](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02484285.pdf)). The day before the Manafort indictment was unsealed, Epstein asked Ruemmler: "why would they file a sealed indictment? if it is true" (October 29, 2017, [EFTA02575359](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02575359.pdf)). Epstein coached Ruemmler on corporate placement, describing a "Nigerian" candidate as "a lefty. predisposed to empower women. minorities etc.. its yours to lose" (November 2017, [EFTA02570921](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570921.pdf)). Regarding Benjamin de Rothschild: Ruemmler wrote "had assumed you were exaggerating a bit about Benjamin. Wrong assumption" (January 2015, [EFTA02513986](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02513986.pdf)) -- 11 months before the $25M transfer. Epstein recommended "massage at La Reserve" hotel in Geneva ([EFTA02513974](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02513974.pdf)). Contact continued through at least January 2018 with "awake? chat?" messages ([EFTA02532942](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02532942.pdf)). Ruemmler became Goldman Sachs General Counsel in January 2020.
**Discrepancy:** No public statements addressing the full extent of the documented 4+ year correspondence or the sealed indictment consultation.

### JES STALEY, Former Barclays CEO
**Documents:** 15+
**Evidence Grade:** STRONG -- Rape allegation, victim journal, JPMorgan report, violence
**Key EFTA:** [EFTA00029358](https://www.justice.gov/epstein/files/DataSet%208/EFTA00029358.pdf) (SDNY prosecutor: "one of the non/minor Epstein victims alleges that Jes Staley raped her during a massage")
**Evidence:** SDNY prosecutor flagged rape allegation during massage (December 2019, [EFTA00029358](https://www.justice.gov/epstein/files/DataSet%208/EFTA00029358.pdf)). Second victim journal: Staley "used belt leaving bloody marks" ([EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf)). Drinks with Mandelson and Epstein documented (December 2009, [EFTA02434434](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02434434.pdf)). JPMorgan internal reports referenced Staley's Epstein relationship. Coordinated FCA investigation in UK resulted in Staley's departure from Barclays. No criminal charges filed in any jurisdiction.
**Discrepancy:** Staley publicly stated his relationship with Epstein was professional. Victim testimony describes violent sexual assault.

### LARRY SUMMERS
**Documents:** 30+
**Evidence Grade:** STRONG -- One of densest document trails, Wigdor trafficking testimony, intelligence brokering
**Key EFTA:** [EFTA02731721](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731721.pdf) (Wigdor Law: victim trafficked to Summers), [EFTA02484293](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02484293.pdf) (intelligence on Mongolian central bank)
**Evidence:** Wigdor Law attorney letter identifies Summers as direct recipient of trafficking victim alongside Leon Black — one of the most significant documents in the corpus ([EFTA02731721](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731721.pdf)). Epstein fed Summers intelligence on foreign monetary policy: "central bank mongol does not like imf idea, too much transparency" (October 2015, [EFTA02484293](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02484293.pdf)). Summers to Epstein: "I spoke for your friend Leon Black's investor event today. Thought of you" ([EFTA02674889](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02674889.pdf)). Actively seeking Epstein in NYC, December 2017 ([EFTA02233990](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02233990.pdf)). Victim journal: "For being a Rockefeller that plane Mr. Dana had me on was scary! Both he and Larry Summers are fucking disgusting!" ([EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf)). Named on same calendar day as Barak, Black, and Thiel visiting Epstein (September 22, 2014, [EFTA00362483](https://www.justice.gov/epstein/files/DataSet%209/EFTA00362483.pdf)). Harvard Kennedy School office involvement documented. 30+ documents make this one of the densest evidence trails of any named individual outside the inner circle.
**Discrepancy:** Summers has not publicly addressed the Wigdor Law trafficking allegation or the victim journal naming.

### PETER THIEL
**Documents:** 20+
**Evidence Grade:** MODERATE-STRONG -- $28.8M financial relationship, CIA Director lunch, no sexual allegations
**Key EFTA:** [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) ($28.8M in Valar Fund investments), [EFTA02589110](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589110.pdf) (lunch with possibly Bill Burns)
**Evidence:** Received $28.8 million in Valar Fund investments from Epstein entities over 4+ years (16 transactions, 2015-2019). Post-KYC breach: $5.75M in 3 transactions continued. Last payment: $1.5M on April 17, 2019 -- 80 days before arrest. Documented lunch with Epstein and possibly Bill Burns (future CIA Director), arranged by former Senator Bob Kerrey (September 2014, [EFTA02589110](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589110.pdf)). On same calendar day as Barak, Black, and Summers visiting Epstein ([EFTA00362483](https://www.justice.gov/epstein/files/DataSet%209/EFTA00362483.pdf)). No sexual allegations documented in any database.
**Discrepancy:** Thiel has not publicly disclosed the full $28.8M investment relationship or the Burns/Kerrey lunch.

### LES WEXNER
**Documents:** 30+
**Evidence Grade:** STRONG -- Theft, Victoria's Secret pipeline, NPA cooperation, mansion transfer
**Key EFTA:** [EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf) (Wexner proffer: "several hundred million dollars" stolen)
**Evidence:** Attorney proffer to SDNY (July 25, 2019): Epstein "stolen or otherwise misappropriated several hundred million dollars" from Wexner. "Frequently bought property on behalf of the Wexners and then sold it to himself for a fraction of the cost." Sold himself "a private plane that previously belonged to Wexner at a deeply discounted price." Victoria's Secret pipeline provided recruitment access to aspiring models. FBI Prominent Names page lists Wexner with "homosexual" notation ([EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf)). Withdrew power of attorney and privately settled rather than prosecuting -- allowing Epstein's financial empire to remain intact. The 9 East 71st Street mansion transfer involved Epstein signing both sides of the deed. Wexner co-founded the Mega Group (zero results in any database). The $46M public "charitable donation" far understated actual theft.
**Discrepancy:** Wexner claimed he was a victim of Epstein's theft. Yet he chose private settlement over prosecution, enabling Epstein's continued operations.

### MORT ZUCKERMAN
**Documents:** 20+
**Evidence Grade:** MODERATE -- Complete financial control by Epstein, ongoing contact
**Key EFTA:** [EFTA02518881](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518881.pdf) (Epstein controlling all financial assets)
**Evidence:** Epstein controlled Zuckerman's complete financial life: "All trusts, past three year tax returns, latest will, grats, crts, pledges, art inventory, bxp filings, daily news financial statements, phone contact for Ellen, all tax preparers, Morgan Stanley last report" (December 2013, [EFTA02518881](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518881.pdf)). Called for Epstein, "on his way to lunch" ([EFTA02362038](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02362038.pdf)). Phone documented: 212-326-4010. The scope of financial control -- trusts, wills, art inventory, media company financials -- is extraordinary and suggests Epstein had leverage over Zuckerman equivalent to a fiduciary relationship.

### WOODY ALLEN
**Documents:** 10+
**Evidence Grade:** MODERATE -- Social visits, victim meeting reference, museum access, MIT introduction
**Key EFTA:** [EFTA02518841](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518841.pdf) ("Gini says YES" for Epstein to visit Allen in Newport), [EFTA02491935](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02491935.pdf) (victim: "Meeting Gates or Woody was great")
**Evidence:** "Gini says YES, it is fine for you to come for a visit to Newport and see Woody" (July 2014, [EFTA02518841](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518841.pdf)). Epstein took Allen to MIT to meet Joi Ito ([EFTA02377050](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02377050.pdf)). TOEFL-groomed victim referenced meeting both Gates and "Woody" through Epstein ([EFTA02491935](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02491935.pdf)). External drive labeled "Woody Allen Archive" found on seized device -- notation: "Nothing for Southern" (EFTA from device forensics). Dinner party at Epstein's: Allen and Soon-Yi at 7:30, Ito/Boyden at 8:00, Pritzker at 9:00 ([EFTA02377042](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02377042.pdf)). Private access to Musee d'Orsay with Epstein on a Sunday in March 2012 -- "the govt is going to open the musee dorsay for me and woody alien at 4" ([EFTA02124200](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02124200.pdf)). Jeff Koons studio visit planned with Allen and Neil Gershenfeld (2013). No sexual allegations documented in the files.

### NAOMI CAMPBELL
**Documents:** 5+
**Evidence Grade:** LOW-MODERATE -- Present on island, victim statement
**Key EFTA:** [EFTA00004070](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004070.pdf) (victim: Naomi Campbell on island)
**Evidence:** 30-page FBI evidence package documents a victim (born ~1985) identifying Campbell as present on Little Saint James during her visits ([EFTA00004070](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004070.pdf)). No allegations of Campbell participating in abuse.

### JOHN BROCKMAN / EDGE FOUNDATION
**Documents:** 15+
**Evidence Grade:** MODERATE -- Science network facilitator, post-conviction engagement
**Key EFTA:** [EFTA00018466](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018466.pdf) (2004 Indian Summer dinner with Brin, Page, Bezos), [EFTA02501737](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02501737.pdf) (direct email with Epstein May 2015)
**Evidence:** Literary agent and Edge Foundation founder who served as Epstein's primary pipeline to elite science and technology circles. The 2004 "Indian Summer" dinner at Epstein's Manhattan townhouse was attended by Google co-founders Sergey Brin and Larry Page and Amazon founder Jeff Bezos -- brokered through Brockman ([EFTA00018466](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018466.pdf)). Direct email exchange with Epstein in May 2015 discussed Sam Harris and Jennifer Doudna (CRISPR pioneer) ([EFTA02501737](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02501737.pdf)). Brockman maintained the relationship through Epstein's post-conviction period. The Edge Foundation dinner circuit provided Epstein access to the highest levels of the technology and science establishment. Brockman publicly acknowledged the relationship but downplayed it as purely professional.
**Discrepancy:** Brockman claimed minimal post-conviction contact. Documentary evidence shows ongoing correspondence and introductions through at least 2015.

### SETH LLOYD, MIT
**Documents:** 5+
**Evidence Grade:** MODERATE -- Post-conviction engagement, financial receipt, no sexual allegations
**Key EFTA:** [EFTA02366597](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02366597.pdf) (Lloyd to Epstein March 2017: "Indeed it was awesome")
**Evidence:** MIT professor who maintained contact with Epstein 9 years after conviction: "Indeed it was awesome" (March 2017, [EFTA02366597](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02366597.pdf)). Received research funding through Epstein-facilitated channels. MIT investigated and placed Lloyd on unpaid administrative leave. No sexual allegations documented.

### GEORGE CHURCH, Harvard
**Documents:** 5+
**Evidence Grade:** MODERATE -- Post-conviction meetings, eugenics overlap, no sexual allegations
**Key EFTA:** [EFTA02264607](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02264607.pdf) (Church/Harvard Medical School meeting with Epstein November 2018)
**Evidence:** Harvard Medical School geneticist who met with Epstein in November 2018 -- seven months before arrest ([EFTA02264607](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02264607.pdf)). Church's genetics research overlapped with Epstein's documented eugenics interests, including the plan reported by the NYT (based on scientist interviews, included in FBI news clips at [EFTA00018441](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018441.pdf)) to use the NM ranch for reproductive purposes. Church publicly apologized for the meetings. No sexual allegations documented.

### MARVIN MINSKY
**Documents:** 10+
**Evidence Grade:** STRONG -- Named in victim journal, named in 9-page victim compilation, died 2016
**Key EFTA:** [EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf) (victim journal: "Martin Minsky"), [EFTA00022133](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022133.pdf) (9-page victim accusation compilation)
**Evidence:** MIT professor and artificial intelligence pioneer. Named as "Martin Minsky" in the second victim journal ([EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf)). Named in the 9-page victim accusation compilation alongside Richardson, Mitchell, and Brunel ([EFTA00022133](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022133.pdf)). Virginia Giuffre stated in sworn deposition that she was "directed to have sexual relations" with Minsky on Little Saint James. Minsky died in January 2016, before the SDNY investigation began.
**Discrepancy:** Minsky's representatives denied the allegations. The sworn testimony and dual-journal corroboration were never tested at trial.

### TED LEONSIS
**Documents:** 10+
**Evidence Grade:** STRONG -- Victim journal accusation of filming abuse, AOL executive cluster, dual journal corroboration
**Key EFTA:** [EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf) (second journal: Leonsis FILMED the abuse), [EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf) (first journal: named alongside Snyder and Case)
**Evidence:** AOL executive, Washington Wizards/Capitals owner. The second victim journal contains a serious allegation: Leonsis FILMED the abuse — if true, this would constitute production of child sexual abuse material ([EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf)). Named in the first journal alongside Dan Snyder, Steve Case, and Jim Kimsey in context of "flights of horror" ([EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf)). Part of a cluster of four senior AOL executives named across both journals: Steve Case (CEO), Jim Kimsey (founder), Ted Leonsis (vice chairman), and George Vradenburg (SVP). The victim also stated that AOL was "used to find us" -- an accusation that America Online's platform facilitated victim recruitment ([EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf)). No investigation into these allegations was ever documented.
**Discrepancy:** No public statements from Leonsis addressing the journal accusations. The filming allegation, if true, would constitute production of CSAM.

### STEVE CASE, AOL
**Documents:** 5+
**Evidence Grade:** MODERATE-STRONG -- Named in victim journal, AOL cluster, flight reference
**Key EFTA:** [EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf) (first victim journal: named alongside Leonsis and Snyder)
**Evidence:** AOL co-founder and CEO. Named in the first victim journal alongside Ted Leonsis and Dan Snyder in the context of "flights of horror" ([EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf)). Part of the four-person AOL executive cluster. The victim's accusation that AOL was "used to find us" ([EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf)) implicates Case's platform. No investigation documented.

### DAN SNYDER
**Documents:** 5+
**Evidence Grade:** MODERATE -- Named in victim journal alongside AOL executives
**Key EFTA:** [EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf) (first victim journal)
**Evidence:** Former Washington Commanders owner. Named in the first victim journal alongside Steve Case, Ted Leonsis, and Jim Kimsey in the context of "flights of horror" ([EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf)). No separate corroboration identified in the DOJ files beyond the journal entry.

### NOAM CHOMSKY
**Documents:** 5+
**Evidence Grade:** LOW-MODERATE -- Financial trust managed by Epstein, post-conviction contact
**Key EFTA:** [EFTA02570988](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570988.pdf) (Epstein installing Krauss as trustee in Chomsky trust November 2017)
**Evidence:** Epstein attempted to replace a trustee with Lawrence Krauss in Chomsky's trust: "I would like to replace Max with Lawrence Krauss as trustee" (November 2017, [EFTA02570988](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570988.pdf)). Chomsky publicly confirmed meeting with Epstein post-conviction for "intellectual discussions." No sexual allegations documented.

### DONALD TRUMP
**Documents:** 20+
**Evidence Grade:** MODERATE -- Prominent Names page allegations, NTOC tips, photographic evidence, no DOJ investigative focus
**Key EFTA:** [EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf) (Prominent Names page: forced head/punched, age 13-15), [EFTA01660651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660651.pdf) (NTOC tips)
**Evidence:** FBI Prominent Names briefing page includes two separate allegations: (1) a woman who was 13-15 years old at the time of the alleged incident involving "forced head" and "punched"; and (2) a tip that was deemed "not credible" by FBI ([EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf)). Multiple NTOC tips reference Trump, ranging from a tip about his "Golf Course/Rancho Palos Verdes" (deemed not credible) to the modeling party tip naming Clinton and Trump alongside "big orgy parties" with "young girls and older Victoria's Secret models" ([EFTA01660651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660651.pdf)). A Trump-Maxwell photograph was found on Steve Bannon's iPhone 7 during the WBTW case Cellebrite review; the prosecutor stated "no need to do anything with this one" ([EFTA00025553](https://www.justice.gov/epstein/files/DataSet%208/EFTA00025553.pdf)). Despite these references, Trump does not appear to have been a focus of the DOJ investigative effort documented in these files. The FBI's own assessment designated at least one tip as "not credible."
**Discrepancy:** Trump publicly stated he "was not a fan" of Epstein. The Prominent Names page inclusion and photographic evidence contradict the characterization of a distant relationship.

### HARVEY WEINSTEIN
**Documents:** 5+
**Evidence Grade:** LOW-MODERATE -- Prominent Names page, three allegations, victim journal reference
**Key EFTA:** [EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf) (Prominent Names page: 3 victims), [EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf) (victim journal: Ms. Vicki referenced alongside Weinstein)
**Evidence:** Three separate allegations on the FBI Prominent Names page. Mentioned alongside the unidentified female facilitator "Ms. Vicki" in the first victim journal ([EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf)). No evidence of direct financial relationship with Epstein documented in the Deutsche Bank exhibits. Weinstein was convicted on separate charges in 2020 (New York) and 2022 (California).

### BORIS NIKOLIC
**Documents:** 10+
**Evidence Grade:** MODERATE-STRONG -- Named executor in will, Gates Foundation science advisor, financial separation agreement
**Key EFTA:** [EFTA02730265](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730265.pdf) (Nikolic-Epstein separation agreement mentioning "bgC3"), [EFTA02546928](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02546928.pdf) (Nikolic joke about Gates Foundation "due diligence")
**Evidence:** Named as a successor executor in Epstein's will -- executed August 8, 2019, two days before death. Previously served as Bill Gates's chief science advisor. Nikolic and Epstein negotiated a "separation agreement" that mentioned "bgC3" -- Gates's think tank ([EFTA02730265](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730265.pdf)). In an email about Gates Foundation Deputy Director Gabrielle Fitzgerald's engagement with Epstein, Nikolic joked "she is doing due diligence on your ass ;)" ([EFTA02546928](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02546928.pdf)). Invited alongside others to Columbus Day weekend at Epstein's property ([EFTA02575363](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02575363.pdf)). Nikolic publicly stated he was "shocked" to learn of his naming in the will and declined to serve as executor.
**Discrepancy:** Nikolic's claim of surprise at being named executor is undermined by the documented separation agreement and social engagement.

### TERJE ROED-LARSEN
**Documents:** 5+
**Evidence Grade:** MODERATE -- UN diplomat, Gates Foundation proposal coordination, financial payment
**Key EFTA:** [EFTA01745511](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01745511.pdf) ("Proposal for BMGF" coordinated through Epstein with Roed-Larsen CC'd)
**Evidence:** Norwegian diplomat, former UN Special Envoy. CC'd on "Proposal for BMGF" (Bill & Melinda Gates Foundation) coordinated through Epstein ([EFTA01745511](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01745511.pdf)). Received $130,000 from Epstein entities post-conviction. Resigned from the International Peace Institute in September 2021 when the financial relationship was exposed. No sexual allegations documented.

### JEAN-LUC BRUNEL
**Documents:** 30+
**Evidence Grade:** STRONGEST IN CORPUS -- Multiple victim testimonies, MC2 founder, photography, died in custody
**Key EFTA:** [EFTA00020703](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020703.pdf) (12-year-old girls flown from France), [EFTA00004070](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004070.pdf) (30-page victim package: "constant companion"), [EFTA00004763](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004763.pdf) (hundreds of "Jean Luc Zorro" photos)
**Evidence:** MC2 Model Management founder. A witness described "12 year old girls flown from France for Epstein's birthday" ([EFTA00020703](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020703.pdf)). The 30-page FBI evidence package describes Brunel as a "constant companion" during one victim's time with Epstein, present during abuse in Paris, New Mexico, and Florida ([EFTA00004070](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004070.pdf)). Hundreds of photos labeled "Jean Luc Zorro" documented at Zorro Ranch ([EFTA00004763](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004763.pdf)). Named in the 9-page victim accusation compilation alongside Richardson, Mitchell, and Minsky ([EFTA00022133](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022133.pdf)). MC2 publicly stated its submission requirement: "Age: Between 13 and 20 years old" ([EFTA01728258](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01728258.pdf)). Post-conviction model scouting continued as late as October 2017: "met through the manager at models, Skyped today, will pass to the candidates list" ([EFTA02575358](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02575358.pdf)). Arrested in France in December 2020. Found dead in his cell at La Sante prison in Paris on February 19, 2022, in what was ruled a suicide by hanging. The pattern of both individuals who were seriously prosecuted (Epstein and Brunel) dying before trial completion is forensically notable.
**Discrepancy:** No trial was completed to test the allegations. His death in custody replicated the pattern of Epstein's death.

### ADAM BLY / SEED MEDIA GROUP
**Documents:** 10+
**Evidence Grade:** MODERATE -- Financial payments, science network, post-conviction engagement
**Key EFTA:** [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) (Seed Media Group payments $304K total)
**Evidence:** Founder of Seed Media Group (SEED Magazine, science publishing). Received $304,000 in total payments from Epstein entities across multiple transactions ($170K in August 2015, plus individual payments totaling $134K, [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf)). Connected to the Brockman/Edge science network. 6+ email documents in DS10. No sexual allegations documented.

### BARRY JOSEPHSON
**Documents:** 5+
**Evidence Grade:** MODERATE -- Financial payment, regular meetings, Woody Allen connection
**Key EFTA:** [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) ($200K payment November 2013)
**Evidence:** Hollywood producer. Paid $200,000 to Epstein entities in November 2013 ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf)). Regular meetings documented. Connected to Woody Allen through video sharing and social events. No sexual allegations documented.

### SULTAN BIN SULAYEM
**Documents:** 5+
**Evidence Grade:** MODERATE -- Financial payment, island guest, January 2019 visit
**Key EFTA:** [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) ($6,200 October 2017), [EFTA02273951](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02273951.pdf) (January 2019 island guest list)
**Evidence:** Chairman of Dubai Ports World. Small financial payment ($6,200) documented in October 2017 confirms direct financial tie ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf)). On the January 2019 island guest list alongside Steve Bannon, Nicole Junkermann, and Eduardo Teodorani -- five months before arrest ([EFTA02273951](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02273951.pdf)). The presence of a Dubai Ports World executive on Epstein's island in 2019 connects Epstein to global logistics and trade infrastructure.

### JACK LANG
**Documents:** 20+
**Evidence Grade:** MODERATE-STRONG -- Joint entity, financial relationship, French criminal investigation opened
**Key EFTA:** [EFTA01415196](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415196.pdf) (Prytanee LLC on Deutsche Bank balance sheet, $197,214)
**Evidence:** Former French Culture Minister. His daughter Caroline Lang founded Prytanee LLC with Epstein in 2016, described as an "art investment" entity with $1.4 million deposited. Confirmed on Deutsche Bank balance sheet at RM CODE 82289 with $197,214 remaining ([EFTA01415196](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415196.pdf)). 20+ document hits for "Prytanee" in DS10 redaction database. Lang resigned from the Arab World Institute in February 2026 after the DOJ file release. France's financial crimes prosecutors opened a criminal investigation into Lang and his daughter Caroline. France 24 reported Lang was "summoned over Epstein links." No sexual allegations documented in the DOJ files.
**Discrepancy:** Lang denied wrongdoing. The French criminal investigation is ongoing.

### DAVID E. SHAW
**Documents:** 5+
**Evidence Grade:** LOW-MODERATE -- Elite dinner invitation, billionaire hedge fund
**Key EFTA:** [EFTA02114558](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02114558.pdf) (neuroscience dinner invitee: Shaw, LeCun, Hopfield, Seung)
**Evidence:** Billionaire hedge fund founder (D.E. Shaw). Invited to an elite neuroscience dinner organized by Ed Boyden (MIT) and Neil Gershenfeld (MIT), where the guest list was sent to "Jeff" for approval ([EFTA02114558](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02114558.pdf), recovered from beneath a failed redaction overlay). Other invitees included Yann LeCun (Facebook AI/Turing Award winner), John Hopfield (Princeton), and Sebastian Seung (Princeton). Shaw's firm, D.E. Shaw, employed a young Jeff Bezos before he founded Amazon. No financial relationship with Epstein documented in the Deutsche Bank exhibits. No sexual allegations documented.

### ALEXANDER ACOSTA
**Documents:** 30+
**Evidence Grade:** MODERATE -- NPA negotiation, OPR interview, defense team pressure
**Key EFTA:** [EFTA00009016](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009016.pdf) (Acosta deposition), [EFTA00009116](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009116.pdf) (OPR interview)
**Evidence:** As U.S. Attorney for the Southern District of Florida, Acosta negotiated the 2007 Non-Prosecution Agreement. Under oath during his OPR interview, he was asked about Epstein being "an intelligence asset" and explicitly denied it twice: "the answer is no, and no" — though he also referenced classified information in the same exchange ([EFTA00009116](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009116.pdf), pages 404-405). Acosta stated "the book reference was that I might be personally embarrassed" by a chapter the defense team raised on prosecutorial overreach (the specific team member who made this reference is not identified in the transcript) ([EFTA00009116](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009116.pdf)). He did not recall "focusing on the coconspirator provision" that was expanded during NPA negotiations ([EFTA00009016](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009016.pdf)). Resigned as Secretary of Labor in July 2019 when the NPA terms became public following Epstein's arrest.
**Discrepancy:** Acosta publicly defended the NPA as the best available outcome. The documentary evidence shows he was pressured by the defense team, including through the prospect of public embarrassment. He explicitly denied being told Epstein was an intelligence asset, but referenced classified information in the same response.

### DARREN INDYKE
**Documents:** 50+
**Evidence Grade:** MODERATE-STRONG -- Epstein's primary attorney, executor, trust controller, complete financial access
**Key EFTA:** [EFTA00019322](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019322.pdf) (executor of last will, $250K compensation), [EFTA00015176](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015176.pdf) (Financial Trust Company authorized contact)
**Evidence:** Epstein's primary attorney and estate executor (alongside Richard Kahn). Named as authorized contact for Financial Trust Company Inc. at JP Morgan ([EFTA00015176](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015176.pdf)). Executor of last will executed August 8, 2019 -- two days before death -- directing all assets to "The 1953 Trust" ([EFTA00019322](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019322.pdf)). $250,000 executor compensation. His law firm (Darren K. Indyke PLLC) appears on the Deutsche Bank RM CODE 82289 account roster, managed by the same Jj Litchford and Paul Morris who managed Epstein's personal accounts ([EFTA01359500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01359500.pdf)). As gatekeeper to all Epstein entities, Indyke had complete visibility into the financial flows documented in this report. The estate he administered refused "repeatedly" to waive attorney-client privilege on seized devices including the unsearched 2005 computer ([EFTA00015823](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015823.pdf)). Never charged with any offense.

### RICHARD KAHN
**Documents:** 15+
**Evidence Grade:** MODERATE -- Co-executor, financial coordinator, Christie's connection
**Key EFTA:** [EFTA02570951](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570951.pdf) (Epstein email about trustee replacements, "lawsuit against Bain," account statements)
**Evidence:** Co-executor of Epstein's will alongside Darren Indyke ($250,000 compensation). HBRK Associates, 575 Lexington Avenue. 7 emails in PLIST timestamp analysis covering trust operations, Christie's art transactions, Maybach automobile exchange, and trustee changes ([EFTA02570951](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570951.pdf)). Coordinated with David Mitchell on "cascade" payments and property inspections. Epstein emailed Kahn about trustee replacements and delivery of "account statements" on November 7, 2017 -- the same day Epstein told Mitchell "tomorow you must make money. clear that cascade will au[thorize] the payments" ([EFTA02570991](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570991.pdf)). Holiday schedule coordinated through Lesley Groff. Never charged.

### LARRY VISOSKI
**Documents:** 15+
**Evidence Grade:** MODERATE -- Chief pilot, flight log coordinator, financial logistics
**Key EFTA:** [EFTA02477179](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02477179.pdf) (Marrakesh flight coordination), [EFTA00018778](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018778.pdf) (Plan D LLC sole manager)
**Evidence:** Epstein's chief pilot since the 1990s. Listed as sole manager on Plan D LLC articles of organization ([EFTA00018778](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018778.pdf)). Coordinated all flight logistics through PLIST-documented emails, including the private jet flight from Little St. James to Marrakesh, Morocco with "you and Karyna only" one week after the $25 million Rothschild transfer in December 2015 ([EFTA02477179](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02477179.pdf)). 7 emails in PLIST timestamp analysis covering flight logistics and aircraft negotiations. Testified at Maxwell trial. Co-pilot David Rodgers confirmed he "would not go back to add in that passenger's name on prior flight logs" — meaning the flight records undercount actual passengers ([EFTA02731168](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731168.pdf) p.7). Never charged.

### STEPHEN HAWKING
**Documents:** 5+
**Evidence Grade:** LOW-MODERATE -- Contact information shared, chartered submarine, no sexual allegations
**Key EFTA:** [EFTA02076108](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02076108.pdf) ("S. Hawking's contact info" shared through Epstein network)
**Evidence:** Contact information shared through Epstein's network ([EFTA02076108](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02076108.pdf)). Documented as having been on a chartered submarine arranged through Epstein's connections. No sexual allegations documented. Hawking died in March 2018.

### JIM KIMSEY, AOL Founder
**Documents:** 5+
**Evidence Grade:** MODERATE-STRONG -- Named in victim journal alongside AOL cluster
**Key EFTA:** [EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf) (first victim journal: named alongside Case, Leonsis, Snyder)
**Evidence:** AOL co-founder (1985). Named in the first victim journal alongside Steve Case, Ted Leonsis, and Dan Snyder in the context of "flights of horror" ([EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf)). Part of the four-person AOL executive cluster. Kimsey was a decorated Vietnam War veteran (Silver Star, Bronze Star with V) who co-founded AOL (originally Quantum Computer Services) in 1985. He later served as chairman of the International Commission on Missing Persons. The victim journal naming is the sole direct evidentiary link in the DOJ files. Kimsey died in March 2016, before the SDNY investigation began.

### KARYNA SHULIAK
**Documents:** 25+
**Evidence Grade:** MODERATE -- Butterfly Trust beneficiary, Lithuanian connections, residence at intelligence nexus
**Key EFTA:** [EFTA01282297](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01282297.pdf) (Butterfly Trust beneficiary — replaced Maxwell in late 2014), [EFTA01378419](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01378419.pdf) (partial SSN at 301 E 66th)
**Evidence:** Added as a beneficiary of the Butterfly Trust in late 2014, in the same instrument that deleted Maxwell as a beneficiary ([EFTA01282297](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01282297.pdf), page 16). Resided at 301 East 66th Street -- the same building housing MC2 model apartments, Ehud Barak's apartment, trafficking victims, and Epstein corporate entities ([EFTA01378419](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01378419.pdf), partial SSN documented). Lithuanian-born, connected to Gratitude America entity which made payments to NPO Baleto Teatras (Lithuanian National Ballet) and VSJ Baleto Teatras. "Hello from Vilnius" email establishing the Lithuanian connection ([EFTA02203371](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02203371.pdf)). Appears 20+ times in DS10 documents as trust beneficiary and signatory. Calendar entry: "Drive to Leon Blacks house with Karyna" ([EFTA01928406](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01928406.pdf)). Accompanied Epstein on the Marrakesh flight one week after the $25M Rothschild transfer in December 2015 -- "you and Karyna only" ([EFTA02477179](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02477179.pdf)). The fact that Shuliak replaced Maxwell as a Butterfly Trust beneficiary in the same instrument (late 2014) suggests a deliberate transition of Epstein's inner-circle trust structure.

### BOB KERREY, Former Senator
**Documents:** 5+
**Evidence Grade:** LOW-MODERATE -- Arranged Thiel-Burns lunch through Epstein, no sexual allegations
**Key EFTA:** [EFTA02589110](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589110.pdf) (Kerrey arranged Thiel-Burns-Epstein lunch, September 2014)
**Evidence:** Former Nebraska Senator and Governor, President of The New School. Arranged a lunch with Epstein, Peter Thiel, and possibly Bill Burns (future CIA Director) in September 2014 ([EFTA02589110](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589110.pdf)). This introduced two powerful figures -- a future CIA Director and a billionaire tech investor with $28.8M flowing to his fund from Epstein -- through Epstein's facilitation. Kerrey's role as intermediary placed Epstein at the nexus of political, intelligence, and technology circles. No sexual allegations documented.

### GABRIELLE FITZGERALD, Gates Foundation
**Documents:** 5+
**Evidence Grade:** MODERATE -- Gates Foundation "due diligence" on Epstein post-conviction
**Key EFTA:** [EFTA02546928](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02546928.pdf) (Gates Foundation Deputy Director "private donor engagement" with Epstein)
**Evidence:** Gates Foundation Deputy Director who conducted "private donor engagement" with Epstein post-conviction. Boris Nikolic (Gates chief science advisor) joked in email: "she is doing due diligence on your ass ;)" ([EFTA02546928](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02546928.pdf)). This establishes that the Gates Foundation was not merely passively aware of Epstein's post-conviction status but was actively evaluating him as a potential donor at the institutional level. No sexual allegations documented. Fitzgerald's engagement demonstrates institutional-level post-conviction normalization of Epstein.

### DAVID MITCHELL / MITCHELL HOLDINGS LLC
**Documents:** 15+
**Evidence Grade:** MODERATE -- $476K in recurring payments, Mandelson connection, "cascade" payments
**Key EFTA:** [EFTA02570991](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570991.pdf) ("tomorow you must make money. clear that cascade will au[thorize] the payments")
**Evidence:** 13+ recurring disbursements totaling approximately $476,000 (2018-2019), connected to Peter Mandelson advisory role. Mitchell's addresses: 745 Fifth Avenue, later 801 Madison Avenue. On November 7, 2017, Epstein emailed Mitchell: "tomorow you must make money. clear that cascade will au[thorize] the payments" ([EFTA02570991](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570991.pdf)). The term "cascade" in a payment context may refer to cascading fund transfers through multiple entities sequentially, though its exact meaning in this context is unclear. On the same day, Epstein emailed Richard Kahn about trustee replacements, "lawsuit against Bain," and delivery of "account statements" ([EFTA02570951](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570951.pdf)). Mitchell conducted property inspections and managed administrative tasks. The recurring nature of the payments ($476K across 13+ disbursements over 2 years) suggests an ongoing service or advisory relationship rather than one-time transactions. No sexual allegations documented.

### SEAN CARMODY, JPMorgan
**Documents:** 5+
**Evidence Grade:** LOW-MODERATE -- Banking intermediary, JPMorgan-to-Deutsche Bank pipeline
**Key EFTA:** CENTERVIEW_MONEY_TRACE.md investigation findings
**Evidence:** JPMorgan private banker identified as a conduit between Epstein's JP Morgan accounts and related Centerview Partners transactions. The "Sean Carmody pipeline" connected Epstein's old JPMorgan banking relationship (1998-2013) to the new Deutsche Bank architecture (2013-2019). This represents the institutional bridge that allowed Epstein to transition his banking operations between major financial institutions without disruption to the underlying money flows. No sexual allegations documented.

### MICHAEL WOLFF, Journalist
**Documents:** 5+
**Evidence Grade:** LOW-MODERATE -- Social intermediary, Bannon dinner, Salvator Mundi commentary
**Key EFTA:** [EFTA02664993](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664993.pdf) (Wolff to Epstein: "six-hour dinner with Ailes and Bannon"), May 2019 Salvator Mundi interview
**Evidence:** Journalist and author who served as a social intermediary between Epstein and the media/political worlds. Emailed Epstein about a "six-hour dinner I had with Ailes and Bannon last week at my house" (January 2017, [EFTA02664993](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664993.pdf)). In May 2019, Wolff interviewed Epstein, during which Epstein commented on the "Salvator Mundi" sale: "my art guy said the painting wasn't very good" and "was only worth 1.5m" -- implying the $450.3M sale price was geopolitical maneuvering. A mock interview YouTube video between Epstein and Bannon (possibly facilitated by Wolff) vanished before investigators could view it ([EFTA00037236](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037236.pdf)). No sexual allegations documented.

### LESLEY GROFF, Executive Assistant
**Documents:** 40+
**Evidence Grade:** MODERATE-STRONG -- Primary communications coordinator, State Department calls, Fifth Amendment
**Key EFTA:** [EFTA02522767](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02522767.pdf) (Groff calling State Department for Mitchell), 40+ PLIST documents
**Evidence:** Epstein's executive assistant and the heaviest Apple Mail user in the PLIST corpus (40+ documents). Called the US State Department searching for Senator George Mitchell ([EFTA02522767](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02522767.pdf)). Coordinated flight bookings, staff scheduling, Richard Kahn's holiday schedule, World Cup tickets for "HHI" ($900 each, [EFTA02518838](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518838.pdf)), and 3BIS architecture firm meetings through May 2019 -- six weeks before Epstein's arrest. Her attorney "indicated he would not bring Groff in for a proffer and had advised her to invoke her Fifth Amendment privilege" at a reverse proffer session on July 18, 2019 -- two weeks after Epstein's arrest. The invocation of the Fifth Amendment by a scheduling coordinator suggests awareness of criminal liability. Despite being a central figure in the operational logistics of the trafficking enterprise, Groff was never charged with any offense.

### MARK EPSTEIN, Brother
**Documents:** 15+
**Evidence Grade:** LOW-MODERATE -- Death threats, property access disputes, Kohn letters
**Key EFTA:** [EFTA00037258](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037258.pdf) (death threats), [EFTA00037250](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037250.pdf) (urgent Indyke meeting and Paris property access)
**Evidence:** Jeffrey Epstein's brother. Reported death threats connected to information he possessed about the case ([EFTA00037258](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037258.pdf)). Urgently requested a meeting with Darren Indyke and access to the Paris property ([EFTA00037250](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037250.pdf)). The threats were linked to information about Karl Erivan Haub, the German billionaire who disappeared in the Swiss Alps in April 2018. Mark Epstein's attorney forwarded the Melvyn Kohn letters (claiming foreign intelligence involvement) to SDNY. He retained Michael Baden (former NYC Chief Medical Examiner) to observe his brother's autopsy -- Baden publicly stated the findings were "more consistent with homicidal strangulation" ([EFTA01684283](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684283.pdf)). The estate's last will gave Mark no specific bequests; all assets were directed to "The 1953 Trust." Mark Epstein received no inheritance despite being Jeffrey's closest living relative. No sexual allegations documented.

### NICK TARTAGLIONE, Cellmate
**Documents:** 10+
**Evidence Grade:** LOW-MODERATE -- Removed from cell evening before death, former police officer
**Key EFTA:** [EFTA01649190](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01649190.pdf) (death investigation timeline)
**Evidence:** Former Westchester County police officer, convicted of quadruple murder in a narcotics conspiracy. Assigned as Epstein's cellmate in the SHU. Transferred out of the cell on the evening of August 9, 2019 -- the night Epstein died. His removal left no witness in the cell. Tartaglione was initially believed to have been involved in Epstein's first injury on July 23, 2019 (the incident that triggered the brief suicide watch), though this was never conclusively established. Tartaglione's own attorneys stated he did not harm Epstein and had in fact called for help. His removal on the night of death, combined with the guard sleeping, the DVR failure, and the lack of 30-minute rounds, created a perfectly unmonitored window. Tartaglione was subsequently sentenced to life in prison for the quadruple murder.

---

# V. THE DEATH INVESTIGATION

## A. Surveillance Infrastructure

The Maxwell prosecution memo explicitly states: "Epstein had cameras in his clock" ([EFTA02731226](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731226.pdf)). A 2003 Palm Beach police report documents Epstein purchasing a spy camera and concealing it in a clock in his office, with footage monitored on his computer hard drive ([EFTA00029761](https://www.justice.gov/epstein/files/DataSet%208/EFTA00029761.pdf)) — though the context of this particular camera was catching a household employee stealing cash from a briefcase, not sexual abuse surveillance. Evidence photos show "24 HOUR VIDEO SURVEILLANCE" signs on multiple doors at 9 East 71st Street. A multi-monitor control room/surveillance station was photographed by the FBI during the July 2019 search ([EFTA00000015](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000015.pdf)-17), showing 4 large computer monitors mounted on a wall with desk, keyboard, mouse, and telephone.

The FBI CID summary (approved 7/17/2024) states "contrary to some news reports, these searches did not reveal any cameras in any of the bedrooms or massage rooms" ([EFTA00038617](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038617.pdf)). This claim is specifically limited to bedrooms and massage rooms — it does not deny the existence of cameras elsewhere on the properties. The tension between the prosecution memo's "cameras in his clock" statement, the multi-monitor surveillance station, the VHS surveillance tapes, and the FBI CID summary's limited denial has never been reconciled.

## B. VHS Surveillance Tapes -- Never Scanned

Professional surveillance VHS tapes (Maxell T-160, labeled "Ideal for use in Time Lapse Recording") were seized from Epstein properties but evidence labels state "ITEM WAS NOT SCANNED" ([EFTA00007741](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007741.pdf), [EFTA00007984](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007984.pdf), [EFTA00007987](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007987.pdf), [EFTA00007990](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007990.pdf)). These are physical time-lapse surveillance recordings that were not processed during the FBI's digital evidence extraction; there is no record of their contents ever being reviewed at the federal level. The T-160 designation indicates 160-minute recording capacity per tape -- standard for commercial surveillance systems. The existence of these tapes, combined with the prosecution memo's "cameras in his clock" statement and the multi-monitor surveillance station, establishes that Epstein operated physical surveillance recording equipment that captured footage on removable media.

## C. MCC DVR Failure Timeline

192 cameras at MCC New York, 128 assigned to recording, split across two DVR systems. Three of four camera angles covering Epstein's SHU tier recorded to DVR 2.

| Date | Event | Source |
|------|-------|--------|
| Sept 2018 | BOP awards contracts to Company 1 (NiceVision) and Company 2 for camera upgrade | [EFTA01649190](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01649190.pdf) |
| July 29, 2019 | DVR 2 suffers "catastrophic disk failures" -- 2-3 hard drives fail | [EFTA00039025](https://www.justice.gov/epstein/files/DataSet%209/EFTA00039025.pdf) |
| July 30, 2019 | Epstein transferred back to SHU after suicide watch | [EFTA01649190](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01649190.pdf) |
| Aug 8, 2019 | DVR 2 failure first detected by MCC staff; Warden claims unaware | [EFTA01649190](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01649190.pdf) |
| Aug 8, 2019 | Additional 2 hard drives fail on DVR 2 | [EFTA00039025](https://www.justice.gov/epstein/files/DataSet%209/EFTA00039025.pdf) |
| Aug 9, 2019 | MCC obtains replacement hard drives but NEVER INSTALLS them | [EFTA01649190](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01649190.pdf) |
| Aug 10, 2019 | **EPSTEIN FOUND DEAD ~6:30 AM** | Multiple |
| Aug 10, 2019 | Hard drives seized from DVR 2 at 4:30 PM EDT | [EFTA00023970](https://www.justice.gov/epstein/files/DataSet%208/EFTA00023970.pdf)-75 |
| Aug 12, 2019 | NiceVision arrives to begin replacement system installation | [EFTA01649190](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01649190.pdf) |
| Aug 14, 2019 | FBI CART/MXU team downloads priority cameras from DVR 1 | [EFTA00017949](https://www.justice.gov/epstein/files/DataSet%208/EFTA00017949.pdf) |
| Aug 14, 2019 | Password obtained from MCC contractor; DVR 1 data reviewed | [EFTA00017948](https://www.justice.gov/epstein/files/DataSet%208/EFTA00017948.pdf) |
| Aug 16, 2019 | DVR system shipped to FBI DFAU, Quantico, VA | [EFTA00039025](https://www.justice.gov/epstein/files/DataSet%209/EFTA00039025.pdf) |

Seized DVR 2 hard drives documented with individual evidence logs:

| NYCO Number | Description | Serial Number |
|-------------|-------------|---------------|
| NYC023578 | Seagate Barracuda 500GB | S/N Z3T6CJJA |
| NYC023579 | Hitachi 500GB | S/N JP1572JE36A13K |
| NYC023580 | Seagate Barracuda 500GB | S/N Z3T6CFSX |
| NYC023582 | Hitachi 500GB | S/N JP1572JE36MWNK |
| NYC023583 | Seagate Barracuda 500GB | S/N 9QMBEC75 |

FBI forensic analysis at Quantico: DVR 2 "did not start successfully." An FBI Advanced Data Recovery Specialist repaired three faulty drives but "the DVR was never able to be assembled successfully." Controller logs confirmed "no recordings would have been available after July 29, 2019" ([EFTA00039025](https://www.justice.gov/epstein/files/DataSet%209/EFTA00039025.pdf)).

**Result: 3 of 4 cameras covering the SHU where Epstein died had NO recoverable recordings from after July 29, 2019. The sally port camera covering the elevator bank was also on DVR 2.**

## D. Suicide Watch and Removal

Epstein was placed on suicide watch on July 23, 2019, after an incident in which he was found on his cell floor with marks on his neck. Suicide watch logs ([EFTA00035225](https://www.justice.gov/epstein/files/DataSet%208/EFTA00035225.pdf)) documented:
- Observation entries every 15 minutes during suicide watch
- Psychological assessments conducted by BOP staff
- Epstein "denied suicidal ideation" during evaluation
- Removed from suicide watch on July 29, 2019 -- the same day DVR 2 suffered its "catastrophic disk failures"

The removal from suicide watch after only 6 days was criticized as premature. The BOP psychology staff decision to downgrade from constant observation to standard 30-minute checks created the unmonitored window during which Epstein died. No explanation was provided for why suicide watch was terminated despite the severity of the initial incident.

## E. The Night of August 9-10, 2019

### Timeline

| Time | Event |
|------|-------|
| Evening, Aug 9 | Epstein's cellmate Nicholas Tartaglione transferred out of SHU cell |
| 10:30 PM | Guards Tova Noel and Michael Thomas begin shift |
| 10:30 PM - 6:30 AM | Guards admit to sleeping and browsing internet (shopping, sports) |
| 10:30 PM - 6:30 AM | NO 30-minute rounds conducted |
| ~10:15 PM | Hard drives removed from the SHU |
| 6:30 AM, Aug 10 | Epstein found unresponsive in cell |
| 6:33 AM | Code Blue called |
| 6:39 AM | FDNY paramedics arrive |
| 6:39 AM - 7:05 AM | Resuscitation attempts |
| 7:36 AM | Pronounced dead at New York-Presbyterian Hospital Lower Manhattan |
| 4:30 PM | Hard drives seized from DVR 2 |

### Key Anomalies
1. Epstein's cellmate was removed the day of death -- leaving no witness
2. Both assigned guards simultaneously slept through their entire shift
3. The last 30-minute check was falsified -- guards logged rounds they never made
4. Hard drives were removed from the SHU at 10:15 PM -- their chain of custody is undocumented
5. The DVR system covering 3 of 4 cameras had been non-functional for 12 days
6. Replacement hard drives had been obtained but never installed
7. The sally port camera covering the elevator banks was on DVR 2 -- meaning there is no video record of who entered or exited the SHU during the critical period
8. No screams, sounds, or disturbances were reported by any other SHU inmate
9. The timing of the DVR failure (July 29), suicide watch removal (July 29), and SHU transfer (July 30) all occurred within a 24-hour window
10. The timing of the last will execution (August 8), additional DVR drive failure (August 8), and replacement hard drives obtained but not installed (August 9) all occurred within 48 hours of death

### MCC Institutional Conditions

The Metropolitan Correctional Center was one of the most troubled facilities in the federal prison system:

- **Chronic understaffing:** The SHU tier where Epstein was held was severely understaffed, requiring mandatory overtime from all available staff
- **Mandatory overtime exhaustion:** Guards working 16-hour shifts due to staffing shortages, creating conditions where sleeping on duty was structurally predictable
- **Infrastructure degradation:** The camera system was under a replacement contract (NiceVision/Company 1 awarded September 2018) but the upgrade had not been completed by August 2019 -- 11 months after contract award
- **Prior incidents:** MCC had a documented history of failures in prisoner monitoring, including a 2017 OIG report on conditions
- **High-profile inmates:** The facility simultaneously housed multiple high-profile inmates, creating competing security demands
- **BOP Psychology staffing:** The decision to remove Epstein from suicide watch after only 6 days was made by BOP psychology staff who were themselves stretched across the facility's mental health caseload

### Inmate Statements and BOP Investigation

The FBI collected statements from SHU inmates and conducted a death investigation coordinated by AUSA Rebekah Donaleski:

- Multiple inmate statements were collected from other SHU residents who were housed near Epstein's cell ([EFTA01659575](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01659575.pdf), [EFTA01659587](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01659587.pdf))
- Each interview required 2 FBI agents, creating a significant resource demand
- MCC officer subpoenas were coordinated for the death investigation
- "Approaches" to individual officers were planned for interviews
- The OIG (Office of Inspector General) conducted a parallel investigation into MCC conditions

The DOJ OIG investigation examined the systemic failures but SDNY ultimately declined to prosecute any BOP employees beyond the two guards ([EFTA00035812](https://www.justice.gov/epstein/files/DataSet%208/EFTA00035812.pdf)). The declination meant that supervisory failures -- including the Warden who claimed to be unaware of the DVR failure, the psychology staff who removed Epstein from suicide watch, and the operations staff who obtained but never installed replacement hard drives -- went entirely unexamined in a criminal context.

### The Noose / Ligature

The official account describes Epstein creating a noose from his bedsheet and attaching it to the upper bunk in his cell. The SHU protocol required that bedsheets be provided to inmates but also required 30-minute checks that would have detected any attempt at self-harm. The failure of both guards to conduct any rounds created an 8-hour unmonitored window (10:30 PM to 6:30 AM) that was more than sufficient for either suicide or an assault. The absence of physical evidence of forced entry (the cell was locked), combined with the DVR failure eliminating video evidence, means the question of whether Epstein died by suicide or was killed cannot be definitively resolved from the available evidence.

## F. 4chan Paramedic Leak

On the morning of August 10, 2019, before official announcements, a post appeared on 4chan's /pol/ board from someone claiming to be an FDNY paramedic, describing the scene at MCC with details that could only be known to first responders. The FBI captured 8+ screenshots from 4chan as evidence ([EFTA00027732](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027732.pdf)). The poster used a dynamic IP address that was never identified. The timing of the post -- before official media reports -- suggests either a genuine first responder or someone with advance knowledge of the death.

Key details from the 4chan posting:
- The poster described arriving at MCC and the condition of the body
- Specific medical details were included that matched the subsequent autopsy findings
- The post appeared before any mainstream media reports of Epstein's death
- FBI attempted to trace the dynamic IP but was unable to identify the poster
- The poster's claimed FDNY affiliation was never confirmed or denied

An employee confession video appeared on YouTube in the days following the death. An individual claiming to be an MCC employee described conditions at the facility and events surrounding the death. The video was not captured by investigators before it was removed from the platform. The FBI also collected "Kid Q" PNG files, Reddit r/maxwellhill screenshots, and other online materials as potential evidence ([EFTA00027732](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027732.pdf)). The collection of these materials -- including conspiracy theory content -- demonstrates the FBI was monitoring online speculation about the death and preserving it as part of the evidentiary record.

## G. Guard DPAs Then Charges Dismissed

The two guards -- Tova Noel and Michael Thomas -- were charged with conspiracy and filing false records. Evidence showed:
- Both slept during their shift
- Both browsed the internet (shopping websites, sports websites)
- Neither conducted required 30-minute rounds
- Both falsified log entries showing rounds were conducted
- The SHU where Epstein was held was severely understaffed
- Mandatory overtime had been required due to chronic staffing shortages

They entered into deferred prosecution agreements requiring 100 hours of community service each. Charges were subsequently dismissed. DOJ OIG investigated; SDNY declined to prosecute any BOP employees ([EFTA00035812](https://www.justice.gov/epstein/files/DataSet%208/EFTA00035812.pdf)). The deferred prosecution agreement terms -- community service for the guards who were supposed to be watching a federal prisoner who died -- represented the most lenient possible outcome. Under AG Barr's DOJ, no individual BOP employee was held criminally accountable.

## H. Autopsy Findings

The OCME autopsy conducted by Dr. Kristin Roman under the supervision of Chief Medical Examiner Dr. Barbara Sampson documented:

**Neck Injuries:**
- Fracture to the hyoid bone (left great horn) -- [EFTA01684283](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684283.pdf), Figure 2
- Fracture to left superior horn of thyroid cartilage -- [EFTA01684283](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684283.pdf), Figure 3
- Fracture to right superior horn of thyroid cartilage -- [EFTA01684283](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684283.pdf), Figure 3
- Ligature furrow consistent with a noose created from bedsheet material

**Medical Context:**
- Hyoid bone fractures can occur in both hanging and manual strangulation
- Bilateral thyroid cartilage fractures are statistically more common in strangulation than in hanging, particularly in persons over age 60
- A 2010 study in the American Journal of Forensic Medicine and Pathology found hyoid fractures in 25-50% of hanging deaths for individuals over 50 years old
- The combination of hyoid AND bilateral thyroid cartilage fractures is less common in hanging

**Official Ruling:** Suicide by hanging. Chief Medical Examiner Barbara Sampson stood by the determination.

**Dissent:** Michael Baden, former NYC Chief Medical Examiner (1978-1979), who observed the autopsy at the request of Mark Epstein, publicly stated the findings were "more consistent with homicidal strangulation." Baden's opinion was not formally incorporated into the official report.

The actual autopsy photographs were included in the FBI master briefing document ([EFTA01684283](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684283.pdf), pp. 14-16).

## I. The Will and Post-Death Asset Disposition

Epstein's last will was executed August 8, 2019 -- two days before death. Key terms:
- All property directed to "The 1953 Trust" (created same day, named for his birth year)
- Executors: Darren Indyke and Richard Kahn ($250,000 compensation each)
- Boris Nikolic named as successor executor
- Mark Epstein (brother) received no specific bequests
- No victims referenced

SDNY prosecutor: "It's extremely notable... he updated his will the day before he died" and "reorganized the structure of his assets also on August 8" ([EFTA00019322](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019322.pdf)). The same-day creation of The 1953 Trust and will execution suggests either advance knowledge of imminent death or a final asset protection maneuver.

**Estate Filing ([EFTA00027979](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027979.pdf)):**

| Category | Value |
|----------|-------|
| Cash | $56,547,773 |
| Fixed Income Investments | $14,304,679 |
| Equities | $112,679,138 |
| Aviation, Automobiles, Boats | $18,551,700 |
| Fine Arts, Antiques, Collectibles | TBD (never valued) |
| Hedge Funds and Private Equity | $194,986,301 |
| **Total (excluding art)** | **~$500,000,000** |

**Post-Death Events:**
- Per news reports, shredded documents were observed outside Epstein's offices shortly before arrest (no EFTA corroboration)
- Victim Compensation Fund established, administered by Kenneth Feinberg
- JPMorgan settlement resulted in individual victims receiving approximately $1 million allocations ([EFTA00037088](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037088.pdf), January 2024)
- Deutsche Bank paid $75 million to settle victim lawsuits
- JPMorgan paid $290 million to settle victim lawsuits
- Estate sold 9 East 71st Street for $51 million
- Estate sold Little Saint James Island
- Estate sold 22 Avenue Foch for approximately EUR 10 million (December 2022)
- Millea Bros. estate auction yielded approximately $100,000 for art and furnishings
- Online investigators traced Maxwell through Borgerson-Angara-Tidewood shell companies using an r/maxwellhill Reddit screenshot that appeared in the FBI case serial ([EFTA02730741](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730741.pdf))
- Maxwell arrested July 2020 at 301 Summer Street, Manchester-by-the-Sea, NH, with 25-year UK Special Forces veteran security guard and $1 million bond ([EFTA00011172](https://www.justice.gov/epstein/files/DataSet%208/EFTA00011172.pdf))

## J. Nygard Intersection

The MLAT request to the United Kingdom simultaneously covered BOTH the Epstein AND Peter Nygard investigations -- Prince Andrew was a person of interest in both ([EFTA00022062](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022062.pdf)). FBI internally forwarded Nygard materials classified UNCLASSIFIED//LES in September 2019 through January 2020 ([EFTA01683950](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01683950.pdf)). Helsinki, Finland and Canada were referenced in the MLAT context alongside Nygard. The intersection of two separate sex trafficking investigations involving the same named individual (Prince Andrew) at the same time was procedurally unusual.

---

# VI. INTELLIGENCE CONNECTIONS

## A. Israeli Military Base Tour Under Indictment (2008)

While facing criminal charges in Florida, Epstein was at the Tel Aviv Hilton, "meeting with Israeli scientists about medical research he's funding and taking a tour of military bases with [Friends of Israel chairman] Benny Shabtai" ([EFTA00013730](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013730.pdf)). This was documented in a press clipping forwarded by the AUSA handling the Florida case. The visit demonstrates access to Israeli military infrastructure during an active criminal prosecution.

## B. The 301 East 66th Street Nexus

This single building simultaneously housed:
- **Ehud Barak's apartment** -- cleaned by Epstein's staff on Epstein's direct orders in March 2019 ([EFTA02278459](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02278459.pdf))
- **MC2 model apartments** -- confirmed by FBI DAS search generating 2,000+ records ([EFTA00019513](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019513.pdf))
- **Trafficking victims** -- placed there by Epstein ([EFTA00025109](https://www.justice.gov/epstein/files/DataSet%208/EFTA00025109.pdf))
- **Guest apartment "2G"** for visitors
- **Epstein corporate entities** -- Suite 10F ([EFTA02533859](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02533859.pdf))
- **Karyna Shuliak's residence** -- with partial SSN documented ([EFTA01378419](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01378419.pdf))

A former Prime Minister and Defense Minister of Israel maintained an apartment, controlled by Epstein's staff, in the physical infrastructure of a documented sex trafficking operation. The building served simultaneously as corporate headquarters, housing for trafficking victims, housing for models recruited through MC2, and a private apartment for a foreign head of state.

## C. IDF-Branded Clothing and Military Uniform on Little Saint James

FBI search photos from August 2019 documented:
- **[EFTA00001970](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001970.pdf):** Green sweatshirt with "IDF" (Israel Defense Forces) logo and Hebrew text, in wardrobe
- **[EFTA00001971](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001971.pdf):** Green T-shirt with "ISRAEL DEFENSE FORCES" and Hebrew "צה"ל" (tzahal) emblem
- **[EFTA00001969](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001969.pdf):** White military dress uniform with medals and ribbons, found in the same wardrobe. No visible markings identify its national origin; the photograph does not establish it as IDF. (Note: Epstein maintained separate costume collections at other properties, including sailor-style uniforms and a "BABY" lab coat — [EFTA00000510](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000510.pdf)-512.)

## D. Melvyn Kohn Letters

Between August 12-19, 2019 — beginning two days after Jeffrey Epstein's death — a man identifying himself as Melvyn Kohn sent unsolicited emails to Mark Epstein (Jeffrey's brother) claiming foreign intelligence operatives were embedded in Epstein's network ([EFTA00037218](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037218.pdf), [EFTA00037239](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037239.pdf)). Kohn described himself as a former US military intelligence operative whose uncle was "head of int'l relations at the Pentagon"; this background is self-reported and unverified in these files. He wrote: "neither you nor he are Mossad, or even working knowingly for any foreign intel agency" but "there is the presence of certain parties in this mix who ARE." He referenced arms dealer Gerald Bull (assassinated 1990, widely attributed to Mossad) and mentioned Jeffrey's "exposure to North Korean/Chinese agents," though he subsequently walked back the Bull connection, writing: "I was clutching at straws" ([EFTA00037218](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037218.pdf) p.1).

Mark Epstein forwarded the letters to his attorney Stacey Richman, who forwarded them to SDNY. Separately, T&M Protection Resources (the Epstein family's private security firm) conducted an email header analysis tracing Kohn's emails to UK-based Yahoo servers ([EFTA00146777](https://www.justice.gov/epstein/files/DataSet%209/EFTA00146777.pdf), [EFTA00037242](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037242.pdf)) and characterized the correspondence as "emails harassing mark epstein" ([EFTA00037236](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037236.pdf)). T&M met with an FBI agent on August 20, 2019 ([EFTA00037232](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037232.pdf)). No FD-302 interview of Kohn, no case serial assignment, and no documented investigative follow-up of his claims exists in the corpus.

## E. FOIA Intelligence Exemption

A FOIA exemption memo explicitly states information about "confidential relationship with a foreign government" was withheld from public release ([EFTA00015219](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015219.pdf)). This confirms classified intelligence-related material about Epstein that was actively suppressed.

## F. Austrian Passport Under False Name

The safe at 9 East 71st Street contained:
- Austrian passport (#0376775) bearing Epstein's photograph under the name Marius Robert Fortelny, DOB 1954 Wien, residence Dammam/Saudi Arabia ([EFTA00021576](https://www.justice.gov/epstein/files/DataSet%208/EFTA00021576.pdf))
- 48 loose diamonds (1-2.38 carats) with individual GIA grading reports from year 2000 ([EFTA00014493](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014493.pdf), [EFTA00021578](https://www.justice.gov/epstein/files/DataSet%208/EFTA00021578.pdf))
- $72,083 cash plus $100 AMEX traveler's check and foreign currency
- "Nudes 1" and "Girl pics nude" photographs ([EFTA00024584](https://www.justice.gov/epstein/files/DataSet%208/EFTA00024584.pdf))

The real Marius Fortelni was identified in Southampton, NY via forteproperties.us ([EFTA00025539](https://www.justice.gov/epstein/files/DataSet%208/EFTA00025539.pdf)). FBI/NYPD CEHT agent assigned to "give him a call tomorrow" (July 16, 2019). No record of the call or its outcome exists. Defense claimed the passport was for "personal protection" during hijackings ([EFTA00014478](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014478.pdf)). Government rebuttal: passport was "actually used" with "numerous ingress and egress stamps" for France, Spain, UK, and Saudi Arabia in the 1980s ([EFTA00016172](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016172.pdf)). Austrian Embassy formally requested information July 22, 2019 ([EFTA00016173](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016173.pdf)). No record of what was shared. Epstein died 25 days later. Investigation permanently unresolved.

## G. Documented Blackmail Operation

Jane Doe #3 testified Epstein trafficked her to "prominent American politicians, powerful business executives, foreign presidents, a well-known Prime Minister" and "required Jane Doe #3 to describe the events... so that he could potentially blackmail them" ([EFTA00021553](https://www.justice.gov/epstein/files/DataSet%208/EFTA00021553.pdf)). FBI case serial 31E-MM-108062 documents investigation into "attempting to blackmail powerful businessmen in New York" ([EFTA01731006](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01731006.pdf)).

Attorneys David Boies and Stan Pottinger planned to use Epstein's "illicit videos" to obtain "multi-million-dollar settlements from the wealthy men" -- described as "conspiracy to commit extortion" ([EFTA00032751](https://www.justice.gov/epstein/files/DataSet%208/EFTA00032751.pdf)). The attorneys' willingness to act on these videos strongly suggests such material exists and that its existence was known to multiple parties, though the videos themselves have not been publicly produced.

## H. Acosta OPR Interview: Intelligence Asset Question

Under oath during his OPR interview, Acosta was asked whether he had been "made aware that Mr. Epstein was an intelligence asset of some sort." The full exchange ([EFTA00009116](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009116.pdf), pages 404-405):

> **Q:** "Were you ever made aware of that assertion?"
> **A:** "I'm not aware of it."
>
> **Q:** "Did defense counsel ever say to you that Epstein had that status?"
> **A:** "Not to my recollection."
>
> **A:** "And to clarify, I also don't know where press reports from multiple media outlets that I told someone that he was an intelligence asset. I do not know where that came from. If I can just — so, there are questions that I may be asked publicly, that I don't think it's right for me to comment as to what classified information I may or may not know, because that's not the kind of stuff you'd go into, **but the answer is no, and no.**"
>
> **Q:** "Without reservation, without any —"
> **A:** "**No, and no.**"

Acosta explicitly denied being told Epstein was an intelligence asset — twice saying "no, and no." His reference to classified information in the same exchange has drawn scrutiny, but in context he appears to have been explaining why he could not adequately address the question at a prior press conference, before giving an unequivocal denial under oath.

## I. The Blackmail Model

The documentary evidence establishes that Epstein's operation was structured to generate compromising material for leverage:

**Victim Testimony:** Jane Doe #3 testified Epstein trafficked her to "prominent American politicians, powerful business executives, foreign presidents, a well-known Prime Minister" and "required Jane Doe #3 to describe the events... so that he could potentially blackmail them" ([EFTA00021553](https://www.justice.gov/epstein/files/DataSet%208/EFTA00021553.pdf)). This is explicit victim testimony that the trafficking was designed to create blackmail leverage.

**FBI Documentation:** FBI case serial 31E-MM-108062 documents investigation into "attempting to blackmail powerful businessmen in New York" ([EFTA01731006](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01731006.pdf)). A dedicated FBI investigation into blackmail was opened but its resolution is not documented.

**Boies/Pottinger Extortion:** Attorneys David Boies and Stan Pottinger planned to use Epstein's "illicit videos" to obtain "multi-million-dollar settlements from the wealthy men" -- described by prosecutors as "conspiracy to commit extortion" ([EFTA00032751](https://www.justice.gov/epstein/files/DataSet%208/EFTA00032751.pdf)). This establishes: (a) compromising video material existed; (b) its existence was known to multiple parties; (c) attorneys were willing to attempt monetization; (d) the material depicted "wealthy men" in compromising situations.

**Camera Infrastructure:** The Maxwell prosecution memo's "cameras in his clock" statement, the multi-monitor surveillance control room (FBI search photos), and the VHS time-lapse surveillance tapes collectively establish the technical infrastructure for generating blackmail material. (Note: The 2003 Palm Beach police report ([EFTA00029761](https://www.justice.gov/epstein/files/DataSet%208/EFTA00029761.pdf)) documents a spy camera in a clock set up to catch a burglar, not a sexual abuse surveillance system.)

**"Keepers" Files:** Epstein maintained files with the naming convention "keepers_[NAME]_[DATE]" -- e.g., "keepers_Glen_Dubin_08-10-18.pdf" -- suggesting dossiers of compromising material maintained on specific individuals one year before Epstein's arrest.

**Victim Journal Corroboration:** The second victim journal states that Leonsis FILMED the abuse ([EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf)) -- if true, this means the blackmail material included video created by participants, not just Epstein's own surveillance.

## J. The Wexner "Blackmail" Claim

When the Florida investigation began in 2005, Epstein told Wexner "he was being blackmailed" ([EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf)). The Wexners withdrew the power of attorney and privately settled rather than prosecuting. This is Epstein explicitly deploying the concept of blackmail as leverage against his own patron -- claiming to be a blackmail victim to elicit sympathy and maintain financial protection.

## K. CBP Officer Investigation Timeline

The CBP (Customs and Border Protection) corruption investigation represents a critical dimension of the Epstein operation's infrastructure -- a federal law enforcement officer who facilitated customs bypass for Epstein's aircraft at the USVI pre-clearance port for over seven years.

| Date | Event | EFTA |
|------|-------|------|
| 2008 | CBP Agriculture Specialist assigned to Saint Thomas, USVI | [EFTA00031495](https://www.justice.gov/epstein/files/DataSet%208/EFTA00031495.pdf) |
| 2008-2015+ | Officer clears Epstein's aircraft at pre-clearance port for 7+ years | [EFTA00031495](https://www.justice.gov/epstein/files/DataSet%208/EFTA00031495.pdf) |
| Multiple dates | Officer visits Epstein's house, boat; flies in Epstein's helicopter | [EFTA00031495](https://www.justice.gov/epstein/files/DataSet%208/EFTA00031495.pdf) |
| Aug 30, 2019 | Officer walks into supervisor's office: "Everyone knew I was friends with Jeffery Epstein" | [EFTA00031495](https://www.justice.gov/epstein/files/DataSet%208/EFTA00031495.pdf) |
| Aug 30, 2019 | Supervisor describes officer as having "pal'd around with Mr. Epstein, clearing his aircraft; and spending personal time with the convict" | [EFTA00031495](https://www.justice.gov/epstein/files/DataSet%208/EFTA00031495.pdf) |
| 2019-2020 | C-4 investigation opened with FBI and HSI partners | [EFTA00038585](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038585.pdf) |
| 2019-2020 | Female acquaintance files DOJ complaint: "known associate" who "assisted Mr. Epstein for conducting human trafficking" | [EFTA00031495](https://www.justice.gov/epstein/files/DataSet%208/EFTA00031495.pdf) |
| Oct 2020 | First SDNY proffer session (2 FBI agents, Crowell & Moring counsel for officer) | [EFTA00020852](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020852.pdf) |
| Nov 2020 | Second SDNY proffer session (CBP topics) | [EFTA00020852](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020852.pdf) |
| Post-2020 | Officer transferred to North Charleston, South Carolina | [EFTA00031495](https://www.justice.gov/epstein/files/DataSet%208/EFTA00031495.pdf) |
| Through Feb 2026 | Officer's name remains redacted across all document collections | All DBs |

Additionally, a separate witness proffered through attorney Glen McGorty of Crowell & Moring about "CBP employees helping Epstein bypass customs" -- suggesting the officer was not acting alone but was part of a broader pattern of corruption at the USVI pre-clearance port. The officer's Badge #CAS03223 and HashID #CZACMME are documented, but exhaustive searches across 3.4 million redaction records, 38,000 OCR records, and 21,000 image records failed to uncover his actual name. The systematic redaction of his identity -- across four independently constructed databases -- suggests an active suppression pattern.

The CBP corruption is structurally critical because it explains how Epstein was able to move victims and associates through the USVI without normal customs scrutiny. The weekly cycling pattern (Teterboro to Palm Beach to St. Thomas) required routine clearance at the USVI pre-clearance port -- exactly where this officer was stationed.

## L. FD-71 1996 Source Reporting

FBI FD-71 source reporting documents ([EFTA00038276](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038276.pdf)) establish that the FBI had intelligence about Epstein's activities as early as 1996 -- predating the 2005 Palm Beach investigation by nine years. Maria Farmer filed the first-ever criminal complaint about Epstein and Maxwell with the FBI/NYPD in 1996. The FD-71 form is used for documenting intelligence from confidential human sources. The existence of 1996 source reporting raises questions about what the FBI knew and when, and whether earlier intervention could have prevented the escalation of the trafficking operation during the 1996-2005 period.

## M. FBI Tactical Intelligence Reports for Maxwell Trial

The FBI New York Intelligence Division conducted research on suspected defense witnesses ahead of the Maxwell trial:
- [EFTA02730271](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730271.pdf) (March 21, 2022): "Research and Key Findings for [person] as a Person of Interest for Alleged Defense Witnesses in the Ghislaine Maxwell Trial" -- UNCLASSIFIED//FOUO
- [EFTA02730477](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730477.pdf) (January 19, 2022): Second tactical intelligence report, LAW ENFORCEMENT SENSITIVE

These reports demonstrate that the FBI maintained active intelligence-gathering capability on individuals connected to Epstein through at least 2022 -- contradicting the narrative that the investigation effectively ended with Epstein's death.

## N. Critical Negative Findings

- **CORRECTION (Revisit #52):** The original finding of "ZERO results for Carbyne" is incorrect. DS9 contains 374 documents referencing Carbyne/Reporty, including records of direct Epstein investment in the Israeli tech-intelligence company. Additionally, FBI CHS FD-1023 ([EFTA00090314](https://www.justice.gov/epstein/files/DataSet%209/EFTA00090314.pdf)) explicitly states "Epstein belonged to both U.S. and allied intelligence services" and "trained as a spy under" Barak. A separate investigative memo ([EFTA00098755](https://www.justice.gov/epstein/files/DataSet%209/EFTA00098755.pdf)) describes Epstein as a "financial bounty hunter" for the U.S. government. While CHS reports are unverified, their existence in the FBI case file is forensically significant
- ~~ZERO results for Mega Group~~ **CORRECTION:** 4 documents reference Mega Group, though none document a substantive Epstein-Mega Group operational connection
- ~~ZERO results for Shin Bet, Aman, Unit 8200, or LAKAM~~ **CORRECTION:** Shin Bet (23 docs), Unit 8200 (11 docs) appear primarily in news/reference material circulated in Epstein's network. Aman and LAKAM remain at genuine zero. No direct operational connections to Epstein documented for any Israeli intelligence agency.
- ZERO results for MC2 + Tel Aviv recruiting records
- "Mossad" appears only in external correspondence, never in FBI investigative documents
- ZERO results for Deripaska despite the likely identification of "Oleg" in Mandelson's Moscow email
- ZERO results for Soros-Epstein substantive connection (one LedgerX pitch deck, one Swedish museum)
- ZERO results for Bezos-Epstein direct connection (only 2004 Indian Summer dinner via Brockman)
- ~~ZERO results for Musk-Epstein~~ **CORRECTION (Revisit #54):** 1,038 documents and 15+ direct email exchanges found in DS9/DS10/DS11
- ZERO results for Kevin Spacey-Epstein
- The systematic absence of Israeli intelligence agency references across 1.8M+ records is itself forensically significant -- it suggests either that such records were never created, never seized, or were removed from the corpus before release

---

# VII. PROSECUTION FAILURES

## A. The 2007 NPA Architecture

The Non-Prosecution Agreement negotiated between Epstein's defense team (Dershowitz, Kirkland & Ellis, Kenneth Starr) and SDFL included provisions that have been widely criticized:

- **Co-conspirator immunity** was not in the original draft but expanded during negotiations by the defense team ([EFTA00009016](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009016.pdf)). Under oath, Acosta stated: "I did not recall focusing on the coconspirator provision" (page 284). The provision granted blanket transactional immunity to unnamed, unidentified potential co-conspirators — "without limitation as to people as long as they're coconspirators" (page 289). Acosta acknowledged that if he had focused on it, he "would have" questioned the need for such broad language (page 290).
- **Defense team pressured Acosta** with the prospect of a book chapter on prosecutorial overreach: "the book reference was that I might be personally embarrassed" ([EFTA00009116](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009116.pdf), page 391; the specific team member who made this reference is not identified)
- **NPA deliberately concealed from victims** -- Judge Marra found "the government chose to conceal the existence" of the agreement in violation of the Crime Victims' Rights Act ([EFTA00010507](https://www.justice.gov/epstein/files/DataSet%208/EFTA00010507.pdf))
- **NPA explicitly waived immigration charges** against Adriana Ross and Nadia Marcinkova: "will not request, initiate, or in any way encourage immigration authorities to institute immigration proceedings against Ross or Marcinkova" ([EFTA00176610](https://www.justice.gov/epstein/files/DataSet%209/EFTA00176610.pdf); confirmed during negotiations at [EFTA00193954](https://www.justice.gov/epstein/files/DataSet%209/EFTA00193954.pdf), page 10)
- **CVRA violations** documented: victims were denied their statutory right to be informed and consulted
- **"Hundreds of sexual massages with minors"** — a November 2020 DAG meeting memo documented plea negotiations with one redacted co-conspirator described as having "scheduled hundreds of sexual massages with minors for Epstein but was also a victim of his sexual abuse" ([EFTA00013209](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013209.pdf)). The plea negotiations collapsed; no co-conspirator was ever charged.

## B. Dershowitz and the Co-Conspirator Immunity Timeline

Multiple victims later named Dershowitz as an abuser. Victim journals reference "Allen Douschewitz" directly. The 9-page victim compilation names Dershowitz alongside Richardson, Mitchell, Minsky, and Brunel ([EFTA00022133](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022133.pdf)). However, these allegations against Dershowitz emerged publicly in **2014 court filings** — years after the 2007-2008 NPA negotiations. At the time the NPA was negotiated, there were no public allegations against Dershowitz. The documentary record does not establish whether Dershowitz was aware of any accusations during the NPA negotiations. The blanket co-conspirator immunity clause — which would later shield anyone who could be considered an Epstein co-conspirator — was expanded during negotiations in which Dershowitz participated as defense counsel. Whether this constituted a conflict of interest depends on what Dershowitz knew at the time, which is not established in the available documents. Dershowitz was never investigated for the underlying abuse allegations.

## C. Leon Black: 4+ Victims, FBI 302s, $62.5M Settlement, Video Allegation, NO Charges

The prosecution timeline reveals systematic failure:

| Date | Event | EFTA |
|------|-------|------|
| May 2021 | SDNY opens investigation from Maxwell spinoff | [EFTA02731604](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731604.pdf) |
| 2021-2022 | Multiple victims provide FBI 302 interviews documenting violent assault | [EFTA02731488](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731488.pdf) |
| 2021-2022 | DANY (Manhattan DA) independently investigates; ADAs Wimmer, Puzio, Saxtein | [EFTA02731583](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731583.pdf) |
| Aug 2022 | Second independent victim contacts Wigdor -- "almost perfect match" of violent acts | [EFTA02731729](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731729.pdf) |
| Feb 2023 | New cooperating witness: "trafficked by Maxwell and Epstein" alleging Black abuse | [EFTA02731587](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731587.pdf) |
| May 2023 | FBI notes: "16 years old when raped by Black," "25 different men" | [EFTA02731488](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731488.pdf) |
| Jul 2023 | Black settles with USVI for $62.5 million | [EFTA02731660](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731660.pdf) |
| Mar 2024 | Wigdor attorney reports video circulating on sex site -- 6 men at hotel | [EFTA02731515](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731515.pdf) |
| Oct 2024 | Brad Edwards (victims' attorney) retained BY Black | [EFTA02731577](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731577.pdf) |
| Through Oct 2024 | "US v. Black" in SDNY file sharing system | Internal |
| **Never** | **No criminal charges filed** | |

SDNY CRU: "does not appear to be any evidence of overlap with Maxwell" ([EFTA02731660](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731660.pdf)). SDNY: "I'm not inclined to open based on the other victim" ([EFTA02731578](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731578.pdf)). Wigdor attorney: "Leon Black paid 62.5 million to USVI... I've heard one lawyer represents ten women he sexually assaulted" ([EFTA02731648](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731648.pdf)).

## D. Richardson: Never Formally Cleared, Never Subpoenaed

The case against Richardson demonstrates the pattern of narrowing at every decision point:

| Date | Event | EFTA |
|------|-------|------|
| May 2016 | Sworn deposition names Richardson as recipient of trafficking victim | [EFTA00022133](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022133.pdf) |
| Aug 2019 | Deposition unsealed by Judge Preska; public attention | Multiple |
| 2020 | NM AG Balderas requests asset forfeiture of Zorro Ranch for "trafficking of children" | [EFTA00015190](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015190.pdf) |
| 2020 | NM AG agrees to "cease any investigation into sex trafficking" and defer to federal prosecutors | [EFTA00019183](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019183.pdf) |
| May 2021 | Richardson presents polygraph results in videoconference, claims "Never met any women through JE or GM" | [EFTA00024683](https://www.justice.gov/epstein/files/DataSet%208/EFTA00024683.pdf) |
| May 2021 | Richardson claims "Catastrophic impact on reputation, finances" | [EFTA00024683](https://www.justice.gov/epstein/files/DataSet%208/EFTA00024683.pdf) |
| Ongoing | Richardson counsel publicly releases statement claiming clearance | [EFTA00014374](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014374.pdf) |
| Ongoing | AUSA explicitly contradicts clearance claim: "I don't think it's accurate to infer" clearance | [EFTA00027244](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027244.pdf) |
| Ongoing | SDNY internal: "This is so, so frustrating" over misleading public statement | [EFTA00014372](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014372.pdf) |
| Sept 2023 | Richardson dies -- never subpoenaed, never formally cleared, never charged | Public record |

The New Mexico nexus is significant: Maxwell signed a 1994 notarized document as "disinterested party" for Zorro Ranch land appraisal ([EFTA00030804](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030804.pdf)). Multiple victims documented as abused at the ranch. Richardson's gubernatorial authority overlapped with the peak abuse period at the ranch. The NM AG's decision to defer to federal prosecutors -- who then declined to act -- effectively ended the investigation.

## E. Kellen, Marcinkova, and Ross: NPA Protected, Never Charged

The three primary female co-conspirators were all protected by the NPA architecture:

**Sarah Kellen:** Named NPA co-conspirator. 11 documents with Apple Mail IMAP metadata document active operational role. Her attorney "indicated he would not bring Groff in for a proffer and had advised her to invoke her Fifth Amendment privilege" at a reverse proffer session (July 18, 2019). Despite being identified as a key scheduling coordinator for abuse sessions, Kellen was never charged.

**Nadia Marcinkova:** Named NPA co-conspirator. The NPA explicitly provided that the USAO "will not request, initiate, or in any way encourage immigration authorities to institute immigration proceedings against Ross or Marcinkova as a result of the ongoing investigation" ([EFTA00176610](https://www.justice.gov/epstein/files/DataSet%209/EFTA00176610.pdf)). During plea negotiations, a prosecutor confirmed: "there is no plan to try to proceed on any immigration charges against either Ms. Ross or Ms. Marcinkova" ([EFTA00193954](https://www.justice.gov/epstein/files/DataSet%209/EFTA00193954.pdf), page 10). Received $100,000 from Butterfly Trust to Aviloop LLC two days after Miami Herald publication ([EFTA00020685](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020685.pdf)) -- the government cited this wire alongside $250K to another co-conspirator as evidence of post-Herald emergency payments ([EFTA00028785](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028785.pdf)). 124 documented flights, including 2 with Prince Andrew. Described as having been "cut her hair, dyed it blonde, controlled her weight, selected her clothes" by Epstein, who maintained "a healthcare proxy assigning them responsibility if anything happened to her" ([EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf)). Never charged. Zero results for her full name in the primary redaction database (1.8M records); one hit in DS10 ([EFTA01525405](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01525405.pdf)).

**Adriana Ross:** Named NPA co-conspirator. The NPA's immigration waiver specifically named Ross alongside Marcinkova ([EFTA00176610](https://www.justice.gov/epstein/files/DataSet%209/EFTA00176610.pdf)). Minimal documentary trail in the released files. Never charged.

**The redacted co-conspirator in the 2020 DAG memo:** A November 2020 DAG Meeting Case Overview ([EFTA00013209](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013209.pdf)) documented plea negotiations with one redacted co-conspirator "who scheduled hundreds of sexual massages with minors for Epstein but was also a victim of his sexual abuse" and who "may plead to an obstruction of justice-related count." The identity of this person is redacted. Two lines of evidence bear on the identification:

- **Evidence favoring Sarah Kellen:** Plea draft documents in [EFTA00089268](https://www.justice.gov/epstein/files/DataSet%209/EFTA00089268.pdf) reference "hundreds of appointments," "dozens of minors," and "2-3/day" — language closely matching the DAG memo. The scheduling role ("scheduled hundreds of sexual massages") is consistently Kellen's primary documented function across victim testimonies and prosecution records. Susan Necheles, who later represented Maxwell at trial, served as defense counsel for this co-conspirator. An April 2020 internal SDNY debate about the same individual considered whether to "charge [REDACTED] with sex trafficking" or decline ([EFTA00024285](https://www.justice.gov/epstein/files/DataSet%208/EFTA00024285.pdf) / [EFTA00016245](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016245.pdf)).
- **Evidence favoring Nadia Marcinkova:** The "also a victim of his sexual abuse" language more closely matches Marcinkova's documented history — she was reportedly brought from Yugoslavia as a minor, and Epstein controlled her appearance and health. The SDNY Human Trafficking Coordinators described the individual under plea consideration as a "victim-participant" whose case was "a very close call" because "our Office ordinarily would decline to prosecute a victim-participant like [REDACTED] absent certain aggravating factors" ([EFTA00024285](https://www.justice.gov/epstein/files/DataSet%208/EFTA00024285.pdf)). This deliberation over victim status is more consistent with Marcinkova's profile.

On balance, the plea draft evidence ([EFTA00089268](https://www.justice.gov/epstein/files/DataSet%209/EFTA00089268.pdf)) and the scheduling-role match more strongly support Kellen. However, the identity cannot be confirmed from the available documents. The plea negotiations collapsed regardless, and no charges were filed against either Kellen or Marcinkova.

## F. The Unsearched 2005 Computer

16 EnCase DVDs from the peak abuse period (~2005) -- NEVER examined. FBI lacked legal authority (2005 warrant authorized seizure but not searching). No subsequent warrant ever obtained by any authority. Government stated it "did not intend to obtain a warrant." Estate refused privilege waiver "repeatedly." This is arguably the single most significant piece of unexamined evidence in the entire case. ([EFTA00015823](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015823.pdf))

## G. "FBI Completely Fucking Us" Evidence Processing

AUSA characterization of 17-month evidence processing dysfunction ([EFTA00009941](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009941.pdf)). The complete failure chain:
- 1.1 million initial documents with no email-to-attachment linking
- Control numbers "don't match up to the native files"
- 71K zero-byte files in initial 7 device production
- COVID reduced FBI CART examiner to 1 day per week
- 2 server drives physically failed; sent to HQ for recovery -- outcome unknown
- 6+ machines still unexported as of October 2020
- FBI CART warned: "Relativity is NOT a forensic tool. It is incapable of dealing with... free space, slack space, and system files" ([EFTA00016425](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016425.pdf))
- Encryption bypassed on "multiple devices" ([EFTA00016425](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016425.pdf))
- 1 iMac locked, unable to be imaged; 3 iPads and 1 iPhone sent for unlocking ([EFTA00037386](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037386.pdf))
- NYCO24342 folders completely empty -- extraction failure or genuine absence unknown
- NYCO27913 listed as provided but physically absent from delivered disc
- 400 TB deletion order at FBI CART during active evidence processing ("they mandated we delete old stuff")
- CSAM discovered in 2023 during estate settlement -- proving initial processing missed material ([EFTA00039019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00039019.pdf))

## H. Bannon Texts Never Reviewed

Text messages between Bannon and Epstein found during WBTW case Cellebrite review (April 2021). AUSA: "They aren't responsive to our warrant" ([EFTA00027290](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027290.pdf)). No separate warrant was ever sought for the Epstein-related content. Content has never been reviewed by the Epstein case team. A Trump-Maxwell photo found on the same phone was dismissed: "no need to do anything with this one" ([EFTA00025553](https://www.justice.gov/epstein/files/DataSet%208/EFTA00025553.pdf)). A mock interview YouTube video between Epstein and Bannon vanished before investigators could view it ([EFTA00037236](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037236.pdf)). The same SDNY team worked both the Epstein and WBTW cases -- creating extraordinary evidence access that was never exploited.

## I. Richard Taus -- FBI Agent Letter Ignored

Former FBI Special Agent Richard Taus, incarcerated at Clinton Correctional Facility (inmate #91A1040), sent a letter to Acting USA Audrey Strauss on July 17, 2020, claiming information about Epstein's death, Ghislaine Maxwell, and a "J. Doe" prison visitor ([EFTA00006036](https://www.justice.gov/epstein/files/DataSet%204/EFTA00006036.pdf), [EFTA00038276](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038276.pdf)). SDNY processed it as a "Civilian Crime Report" and forwarded to FBI per "usual practice." Internal note: "this particular submission does not really fit that so we might not get anything more." No evidence of any follow-up interview was conducted.

## J. Prince Andrew: MLAT Filed, Systematically Refused

An MLAT (Mutual Legal Assistance Treaty) request was filed with the United Kingdom in April 2020 ([EFTA00022062](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022062.pdf)). Prince Andrew systematically refused cooperation with US investigators. The MLAT simultaneously covered both Epstein and Peter Nygard investigations -- Andrew was a person of interest in both. Three separate allegations appeared on the FBI Prominent Names page. Two flights with Nadia Marcinkova documented. One victim described a 2010 interaction at the Manhattan townhouse. The $12 million civil settlement with Virginia Giuffre in February 2022 contained no admission of wrongdoing. No criminal charges were ever filed.

## K. Jes Staley: Rape Allegation Flagged, No Charges

SDNY prosecutor flagged a rape allegation in December 2019: "one of the non/minor Epstein victims alleges that Jes Staley raped her during a massage" ([EFTA00029358](https://www.justice.gov/epstein/files/DataSet%208/EFTA00029358.pdf)). The second victim journal corroborated violence: Staley "used belt leaving bloody marks" ([EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf)). Drinks with Mandelson and Epstein documented (December 2009, [EFTA02434434](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02434434.pdf)). JPMorgan internal reports referenced the relationship. A coordinated FCA investigation in the UK resulted in Staley's departure from Barclays in November 2021, but no criminal charges were filed in any jurisdiction.

## L. Glenn and Eva Dubin: "Lent Out" Testimony, No Investigation

FBI 302 documents Maxwell directing a victim: "explicitly told her that she had to do to Glen what she did for Epstein." The victim used the term "lent out" to describe being trafficked to the Dubins and others. The government noted it was "unable to corroborate" the "lent out" accounts, though it corroborated her accounts of Maxwell recruitment and Epstein abuse ([EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf), pp. 54-55). Eva Dubin (MD) used medical credentials in connection with Epstein operations ([EFTA01915127](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01915127.pdf)). Post-conviction contact continued through at least January 2017. 34+ documented flights. No investigation ever opened.

## M. Larry Summers: Wigdor Trafficking Allegation, No Investigation

The Wigdor Law attorney letter ([EFTA02731721](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731721.pdf)) identifies Summers as a direct recipient of a trafficking victim alongside Leon Black. The first victim journal names Summers directly: "Both he and Larry Summers are fucking disgusting!" ([EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf)). 30+ documents establish one of the densest evidence trails outside the inner circle. Epstein fed Summers foreign intelligence on monetary policy ([EFTA02484293](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02484293.pdf)). No investigation was ever documented.

## N. The Dubins, Staley, Summers, Mitchell, Dershowitz -- Composite Pattern

The failure to prosecute these individuals follows a consistent pattern:
1. Victim testimony exists (sworn depositions, journals, attorney letters, FBI 302s)
2. Documentary corroboration exists (emails, financial records, calendar entries, flight logs)
3. SDNY acknowledges the evidence internally
4. No formal investigation is opened or, if opened, is quietly closed
5. The named individual suffers no criminal consequences

In Leon Black's case, this pattern persisted despite FOUR OR MORE independent victim testimonies, FBI 302 documentation of a 16-year-old being "violently raped," direct victim text messages to Black, a video allegation, a $62.5 million USVI settlement, and a "US v. Black" case tracking designation active through October 2024.

## O. Pattern: Narrowing Rather Than Expanding

At every decision point across the 18-year history of the Epstein investigation, prosecutors narrowed rather than expanded their inquiries:

| Decision | Narrowing Action | Alternative Not Taken |
|----------|-----------------|----------------------|
| 2007 NPA | Protected co-conspirators, named abusers, foreign nationals | Prosecute trafficking enterprise |
| 2019 SDNY | Focused on Epstein alone; Maxwell later | Simultaneously pursue named individuals |
| 2020 BOP | Declined to prosecute MCC employees | Charge guards and supervisory staff |
| 2021 Black | SDNY "not inclined to open" despite 4+ victims | Grand jury investigation of Black |
| 2021-22 DANY | Investigated independently, no charges | Coordinate with SDNY for prosecution |
| 2020 Richardson | Never subpoenaed despite contradicted clearance claim | Issue subpoena, compel testimony |
| All years | Dershowitz never investigated for self-immunity conflict | Ethics investigation, potential charges |
| All years | Dubins never investigated despite FBI 302 | Interview victims under oath |
| 2019-21 | Kellen/Marcinkova plea negotiations collapsed | Proceed to charges |
| 2022 | Brunel died in French prison before trial | N/A -- death |
| 2019+ | Staley rape allegation flagged, no prosecution anywhere | Criminal referral to DOJ or FCA |
| 2021+ | Summers Wigdor trafficking allegation unaddressed | Interview Wigdor clients, open investigation |
| 2020 | CBP officer proffer sessions but name redacted, no public charges | Public charges for customs bypass |
| 2019 | Austrian passport investigation abandoned after 25 days | Complete investigation before closure |
| 2021 | Bannon texts: no separate warrant sought | Obtain Epstein-specific warrant |
| 2021 | 2005 computer: no warrant sought for peak-abuse data | Seek warrant for forensic image |
| 2023 | CSAM found during estate settlement -- missed earlier | Systematic re-examination of all devices |

## P. Civil Settlements and Financial Penalties -- The Only Accountability

In the absence of criminal prosecution, the only accountability for the Epstein enterprise has come through civil litigation and regulatory penalties:

| Entity/Individual | Type | Amount | Year | Notes |
|-------------------|------|--------|------|-------|
| **Deutsche Bank** | NYDFS regulatory penalty | $150,000,000 | 2020 | For AML/KYC failures managing Epstein accounts |
| **Deutsche Bank** | Civil settlement (victims) | $75,000,000 | 2023 | Class action by trafficking victims |
| **JPMorgan Chase** | Civil settlement (victims) | $290,000,000 | 2023 | Individual allocations ~$1M per victim ([EFTA00037088](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037088.pdf)) |
| **JPMorgan Chase** | Civil settlement (USVI) | $75,000,000 | 2023 | Attorney General lawsuit |
| **Leon Black** | USVI settlement | $62,500,000 | 2023 | No admission of wrongdoing ([EFTA02731660](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731660.pdf)) |
| **Jes Staley** | FCA/Barclays departure | Not disclosed | 2021 | Regulatory consequence only; no criminal charges |
| **Prince Andrew** | Civil settlement (Giuffre) | $12,000,000 | 2022 | No admission of wrongdoing |
| **Epstein Estate** | Victim Compensation Fund | ~$125,000,000 | 2020-2023 | Administered by Kenneth Feinberg |
| **Estate** | 9 East 71st Street sale | $51,000,000 | 2021 | Property sale, not penalty |
| **Estate** | 22 Avenue Foch sale | ~EUR 10,000,000 | 2022 | Property sale, not penalty |
| **Estate** | Little Saint James Island sale | Not disclosed | 2023 | Property sale, not penalty |
| **Estate** | Millea Bros. auction | ~$100,000 | 2021 | Bulk sale, no Epstein provenance noted |

**Total documented civil/regulatory penalties and settlements: approximately $790 million** (excluding estate property sales, which are asset liquidation rather than accountability measures)

The disparity between the scale of the trafficking enterprise ($755M in documented flows, 95+ shell entities, 60-80+ identified victims, 200+ estimated victims, operations spanning decades and multiple countries) and the exclusively civil/regulatory nature of the accountability is the defining characteristic of the Epstein case. Criminal convictions: 2 (Epstein, plea deal; Maxwell, 5 of 6 counts). Criminal charges against any named individual accused of sexual abuse: 0. Criminal charges against any banker who processed $189M after documented compliance failures: 0. Criminal charges against any co-conspirator other than Maxwell: 0.

---

# VIII. THE ART MACHINE

## A. $30.5 Million in Auction Proceeds (2017)

In 2017, Sotheby's and Christie's deposited $30,510,961 into Epstein's Haze Trust Checking account:

| Date | Auction House | Amount | Bates Reference |
|------|---------------|--------|-----------------|
| 06/19/2017 | Christie's Inc. | $7,725,000 | DB-SDNY-0006320 |
| 09/25/2017 | Sotheby's | $11,536,544 | DB-SDNY-0006565 |
| 10/24/2017 | Sotheby's | $11,249,417 | DB-SDNY-0006646 |

Funds were swept within 1-2 days to DBAGNY, then drained through Southern Financial LLC to external investment funds. Sotheby's Private Client Group handler: Lily D. Snyder ([EFTA02323094](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323094.pdf)). Christie's NY contacts: Joanna Ostrem and Madeline Lazaris ([EFTA02323043](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323043.pdf)). The specific artworks generating these proceeds have not been identified, but Sotheby's and Christie's were ordered to disclose dealings with Epstein by the courts. ([EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf))

## B. Leon Black's $2.7 Billion Collection

Epstein managed Black's art collection including: formation of art partnership, contested Picasso sculpture ownership, art loans, like-kind exchanges, and tax advisory opinions ([EFTA02730996](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730996.pdf)). Christie's 2016 appraisal: 935 artworks valued at $2.7 billion ([EFTA02731023](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731023.pdf)). The Senate Finance Committee confirmed the collection was worth over $1 billion; Black refused to answer questions about art transactions.

Key documented transactions in Black's collection:
- Edvard Munch "The Scream": $120M via Narrows II LLC (2012)
- Multiple Picassos: $115M, $125M via Gagosian
- Alberto Giacometti: $23M wired from Southern Trust (approval by Stewart Oldfield, [EFTA01431221](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01431221.pdf))
- Rothko-to-Picasso exchange: $46M to $48M via Gagosian
- Kurt Schwitters "Ja-Was?-Bild": $25M via Friends Ventures LLC (joint with Lauder)
- Paul Cezanne watercolors: $139M combined with Picasso in like-kind exchanges
- $440M Bank of America credit line at 1.45% secured by art (Narrows Holdings LLC)

Black refused to answer the Senate Finance Committee's questions about like-kind exchanges and art sales involving Epstein ([EFTA02731023](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731023.pdf)). He "helped start an art gallery" for a woman he "allegedly had a relationship with" at 237 Lafayette Street, dissolved September 2018 ([EFTA02731697](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731697.pdf)).

## C. Prytanee LLC / Caroline Lang

**CORRECTION (Revisit #11):** Prytanee LLC was managed by Etienne Binant, not Jack Lang directly. The connection to Jack Lang is indirect, through his daughter Caroline Lang's involvement in the entity. Joint Epstein/Caroline Lang "art investment" entity with $1.4M deposited. Confirmed on Deutsche Bank balance sheet at RM CODE 82289 with $197,214 remaining ([EFTA01415196](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415196.pdf)). Lang resigned from Arab World Institute in February 2026 after the DOJ file release; French criminal investigation opened. France 24 reported Lang was "summoned over Epstein links." Al Jazeera reported France would investigate the former culture minister.

## D. Friends Ventures LLC / Black-Lauder

Joint Black/Lauder entity established by Epstein in 2014 for Kurt Schwitters "Ja-Was?-Bild" ($25M), each owning 50%. Succession planning documented: "It is assumed that on Leon's death, Ronald Lauder will purchase Leon's 50% interest for $12,500,000." Both Black and Lauder served on MoMA's Board of Trustees; Black stepped down as Chairman in March 2021.

## E. Art-Holding Entity Map

```
LEON BLACK'S ART HOLDINGS (managed by Epstein):
  |
  +-- Narrows Holdings LLC
  |     [Artworks pledged as collateral on $440M BofA loan]
  +-- AP Narrows
  +-- Narrows II LLC
  |     [Holds Munch's "The Scream" - $120M]
  +-- Friends Ventures LLC (2014)
        [Joint Black/Lauder - Schwitters "Ja-Was?-Bild" - $25M]

EPSTEIN'S OWN ENTITIES:
  |
  +-- Southern Trust (USVI)
  |     [Main business; wired $23M for Giacometti]
  +-- Haze Trust
  |     [$30.5M from Sotheby's/Christie's in 2017]
  +-- Enhanced Education Foundation
  |     [$5K to Met Gala 2014]
  +-- Jeffrey Epstein VI Foundation
  |     [Claimed NYAA donations]
  +-- Epstein Insurance Trust
  |     [Art insurance covering bronzes]
  +-- Prytanee LLC (2016)
        [Joint Epstein/Caroline Lang; $1.4M; $197K in DB]
```

## F. Art Consultant Witnessed Abuse

John Kendall Rowlands, art historian who sourced and disposed art for Epstein, witnessed the "presence of young girls" while performing professional duties and was owed substantial unpaid fees ([EFTA00024431](https://www.justice.gov/epstein/files/DataSet%208/EFTA00024431.pdf)). This is a direct link between the art operation and the abuse operation through a professional who observed both.

## G. Art as Grooming Tool

"Patron of the arts" was a documented grooming strategy. A 13-year-old was approached with offers of "scholarships for the arts" ([EFTA00019101](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019101.pdf)). Maria Farmer's experience at NYAA demonstrates the complete pipeline: art show attendance, painting purchase, studio space offer, travel arrangement, isolation, assault. The NYAA issued an apology to Farmer in August 2020.

## H. Specific Artworks Documented in the Corpus

### Henri Matisse -- "Le Reflet" (1935)
Complete Sotheby's lot sheet found at [EFTA00004663](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004663.pdf) -- the most detailed individual artwork documentation in the corpus. Oil on canvas, 18 1/4 by 21 7/8 inches (46.3 by 55.5 cm), signed upper right "Henri. Matisse 35." Full provenance: Renou and Colle (acquired from artist, October 1935), Rees Jeffreys (Sussex, 1938), SK Lloyds (1954), Herschel C. Walker (New York, 1955), B. Wardell (1962), Galerie Schmit (Paris, 1978), Private Collection (Paris). Exhibition history documented across four shows in Dusseldorf, Rome, and Paris. Referenced in Pierre Schneider's *Matisse* (1984, p.433) and Lydia Delectorskaya's *L'Apparente Facilite* (1986, p.41). This lot sheet establishes provenance documentation practices for Epstein's art holdings.

### Edvard Munch -- "The Scream" ($120M)
Purchased at Sotheby's in 2012 by Leon Black, held through Narrows II LLC (established by Epstein). At $120 million, this is the highest-value single artwork in the Black/Epstein art portfolio. The use of an LLC holding structure (rather than personal ownership) is consistent with the pattern of entity-based asset management that characterized all Epstein financial operations.

### Multiple Picassos ($115M, $125M, $48M, Contested Sculpture)
"Buste de Femme (Marie-Therese)" (1931) purchased from Gagosian gallery for $115 million, with Epstein "personally guid[ing] the transaction." A second unnamed Picasso purchased through Gagosian for $125 million, won in a legal battle against Qatari royals. A Rothko-Picasso exchange: Black exchanged a $46M untitled Rothko (1961) for a $48M Picasso held by Gagosian -- Epstein "personally worked with lawyers to facilitate" this transaction. The Apollo Conflicts Committee report identifies Epstein advised Black on "the contested ownership of a Picasso sculpture" -- the disputed provenance details are not fully documented. Steve Wynn's Picasso damaged at Christie's was forwarded by Richard Kahn to Epstein: "another christies disaster" ([EFTA02664945](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664945.pdf)).

### Alberto Giacometti ($23M)
Epstein directed staff to wire $23 million from the Southern Trust account into a trust account the day before the transaction, with Epstein involved in appraisals by Gagosian gallery. The $23M wire was approved by Stewart Oldfield at Deutsche Bank ([EFTA01431221](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01431221.pdf)) -- the same officer who managed the Epstein Insurance Trust and approved other suspicious transactions.

### Paul Cezanne -- Watercolors ($139M Combined)
Two Cezanne watercolors plus one Picasso painting sold through Christie's between June 2015 and November 2016, combined value $139 million. Subject of USVI subpoenas and tax audit investigation. The Senate Finance Committee demanded complete lists of like-kind exchanges for pieces valued over $1 million.

### Kurt Schwitters -- "Ja-Was?-Bild" ($25M)
Held through Friends Ventures LLC (2014), jointly owned by Black (50%) and Lauder (50%). Succession planning documented: "It is assumed that on Leon's death, Ronald Lauder will purchase Leon's 50% interest for $12,500,000." (See Section C above.)

### Degas -- "Little Dancer, Aged Fourteen"
Reference to Gregory Hedberg's book about an earlier version of Degas' famous sculpture found at [EFTA01734425](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01734425.pdf). This is one of the most reproduced sculptures in art history and its presence in a collection of this scale is not inherently notable.

### "Parsing Bill" by Petrina Ryan-Kleid (2012)
Painting depicting Bill Clinton in a blue dress and red high heels (Lewinsky scandal reference). Created as Ryan-Kleid's Master's thesis at the New York Academy of Art; sold at the 2012 Tribeca Ball for approximately $1,300. Artist had no knowledge Epstein purchased it. Confirmed by Snopes. A tipster ([EFTA00020462](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020462.pdf)) alleges stolen artwork sold through Sotheby's London was part of Epstein's estate.

### Arnaud Kasper -- Hanging Nude Sculpture
Life-size bronze sculpture of a nude young woman grasping a rope, suspended above the central stairwell at 9 East 71st Street, clothed in an actual wedding dress. Edition 6 of 8. FBI search photos: "A statue of a child hanging from a rope" ([EFTA00000057](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000057.pdf)), "A sculpture of a woman in a white dress hanging from a rope" ([EFTA00000919](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000919.pdf)), "A person hanging from a rope in the air" ([EFTA00000920](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000920.pdf)), "A figure hanging from a noose, wearing a white wedding dress" ([EFTA00000988](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000988.pdf)). Sold at Millea Bros. auction for $1,500 (below $2,000 low estimate).

### Jorge Alvarez -- "Coming of Age Ceremony" (1995)
Oil painting, 83 x 126 inches. Located in the "Pink Room" at 9 East 71st Street where abuse occurred. Depicts a pre-teen boy in an aroused state with demonic figures. Currently unsold at a New York auction house (estimated $1,000-$10,000).

### "Salvator Mundi" Commentary
In May 2019, Epstein told journalist Michael Wolff: "my art guy said the painting wasn't very good" and "was only worth 1.5m" -- commenting on the Leonardo da Vinci attributed work that sold for $450.3 million at Christie's. Epstein implied the sale price was geopolitical maneuvering (Rybolovlev to MBS to Trump). The identity of Epstein's "art guy" was never disclosed.

### "Jackson Pollock Chocolate Drip"
Email from Epstein (jeevacation@gmail.com), April 11, 2018: "its the jackson pollack choclate drip must be in a catalogue but will have someone photo thx" ([EFTA02474944](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02474944.pdf)). Email footer references Christie's LotFinder and Live bidding. Subject line: "Vic Munoz." Likely a Vik Muniz chocolate recreation, not an actual Pollock.

## I. Auction House Personnel and Subpoenas

### Sotheby's
Personnel: Lily D. Snyder (Private Client Group, 457 Madison Ave), Alejandra Rossetti (Paris, chair consignment), Christine Gibbons (El Brillo Way correspondence, [EFTA01785536](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01785536.pdf)). USVI subpoenas issued December 2020 demanding "all documents reflecting or relating to inquiries, sales, bids, communications with or about Jeffrey E. Epstein" going back 20+ years. 895 references to Sotheby's in released documents.

### Christie's
Personnel: Joanna Ostrem ([EFTA02323043](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323043.pdf)), Madeline Lazaris ([EFTA02323043](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323043.pdf)), "Hela Fox" / Catherine McIvern (September 2011, French-language correspondence, [EFTA02029291](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02029291.pdf)). USVI subpoenas December 2020. 1,129 references in released documents. Staff email: "do you have contact info for Sotheby's or Christies? I have a bunch of things for auction at 71st and I've never done it before" ([EFTA02323043](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323043.pdf)).

### Guernsey's
Arlan Ettinger, President, pitched the Attorney General three days after Epstein's death to handle property disposition, claiming the firm was "ideally suited to both maximizing the financial potential of said property while spreading nationwide messages in support of young women" ([EFTA00032555](https://www.justice.gov/epstein/files/DataSet%208/EFTA00032555.pdf)). DOJ internal response: "These guys want to help auction Jeffrey Epstein's property... 'A little cheeky, no?'" ([EFTA00032419](https://www.justice.gov/epstein/files/DataSet%208/EFTA00032419.pdf)). "I thought so too" ([EFTA00015288](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015288.pdf)). "We viewed this as an ad... we did not respond" ([EFTA00017749](https://www.justice.gov/epstein/files/DataSet%208/EFTA00017749.pdf)).

### Millea Bros.
Estate attorney Daniel Weiner confirmed items disposed in "a bulk sale -- not a consignment." Total sales approximately $100,000. Lot descriptions made NO mention of Epstein in provenance. Items sold included Tom Otterness "Free Money" ($5,000), Arnaud Kasper nude ($1,500), Palatial Viennese desk ($4,250), bronze/blue lucite columns ($46,000 pair), metal and glass table ($18,000).

## J. Art World Figures Named in the Files

### Larry Gagosian -- 414 DOJ References
The most-referenced art dealer in the corpus. Facilitated Picasso transactions at $115M and $125M, Giacometti at $23M, Rothko-to-Picasso exchange ($46M to $48M), and Braque appraisal. No direct evidence of knowledge of trafficking.

### Jeff Koons -- 376 DOJ References
Studio visit planned with Woody Allen and Neil Gershenfeld (2013). Multiple calendar references. No financial transactions with Epstein documented.

### Stuart Pivar -- Epstein's Art Advisor
Early Epstein art advisor who collected contemporary and classical works. Self-described relationship with Epstein began in the 1980s through art circles.

### John Kendall Rowlands -- Witnessed Abuse
Art historian who sourced and disposed art for Epstein. Witnessed the "presence of young girls" while performing professional duties and was owed substantial unpaid fees ([EFTA00024431](https://www.justice.gov/epstein/files/DataSet%208/EFTA00024431.pdf)). Direct link between the art operation and the abuse operation.

### Eileen Guggenheim -- NYAA Dean / Named Associate
Named alongside Trump, Andrew, and Dershowitz as an Epstein associate ([EFTA01652757](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652757.pdf)). Urged Maria Farmer to sell Epstein/Maxwell a painting at her 1995 thesis show. The NYAA served as a grooming pipeline.

### Leah Kleman -- Art Dealer
Identified in Epstein's "Black Book" (contact list). Art dealer whose relationship with Epstein was documented but not fully investigated.

### Peggy Siegal -- Steve Wynn Picasso
Discussed the Wynn Picasso with Epstein ([EFTA02532922](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02532922.pdf)). Society publicist with documented Epstein social circle involvement.

## K. Property Art Inventories

### 9 East 71st Street, Manhattan
Herbert N. Straus House, 21,000 sq ft, seven stories. Documented works from FBI search photos include:
- Japanese/Asian landscape paintings (possibly Mount Fuji) covering multiple rooms ([EFTA00000010](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000010.pdf)-13)
- Ceiling mural depicting cloudy sky with golden border ([EFTA00000057](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000057.pdf), 00000130)
- Large painting of nude figure with mirror ([EFTA00000498](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000498.pdf)-500)
- Portrait paintings including bearded man, man with glasses in suit ([EFTA00000465](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000465.pdf), 00000786)
- Dining room: leopard print chairs, gong, black fireplace, mountain landscape, bust ([EFTA00000065](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000065.pdf)-68)
- Library/Study: ornate tapestry with ship and coat of arms, taxidermy tiger, crystal ball, skull, chandelier ([EFTA00000148](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000148.pdf)-153)
- Prosthetic eyeballs (rows of individually framed) confirmed by Vanity Fair 2003 and FBI photos
- Twice-life-size sculpture of naked African warrior
- Custom chess set: Epstein as King, women as other pieces
- Prison yard mural (photorealistic, Epstein at center)
- First edition of "Lolita"
- Framed hand-drawn map of Israel by Ehud Barak
- Framed signed dollar bill from Bill Gates ("I was wrong!")

### 358 El Brillo Way, Palm Beach
Police report: "very large statue of man with a bow. Taken into evidence from this room were nine photographs in frames" ([EFTA00007157](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007157.pdf)). Deposition testimony: "several naked pictures of girls in the room, a mural or pictures of naked girls either exposing their breasts or completely naked" ([EFTA00009448](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009448.pdf)). FBI evidence inventory (2019) documented nude sculptures, nude portraits in bathroom, female portrait photos ([EFTA00021038](https://www.justice.gov/epstein/files/DataSet%208/EFTA00021038.pdf)).

### 22 Avenue Foch, Paris
685 sq meters, 16th arrondissement. Interior by Alberto Pinto. Atelier Meriguet-Carrere catalog requested for renovation in 2014 ([EFTA02116336](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02116336.pdf)) -- one of France's most prestigious decorative arts firms. Carrara marble samples documented ([EFTA02323058](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323058.pdf)). Painting shipped from Paris with framing and insurance valuation ([EFTA02125762](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02125762.pdf)-[EFTA02126033](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02126033.pdf)). Sold December 2022 for approximately EUR 10 million.

### Little Saint James Island
FBI search photos document ornate ceiling with painted murals depicting mythological scenes ([EFTA00002946](https://www.justice.gov/epstein/files/DataSet%201/EFTA00002946.pdf), 00002952, 00002955). Blue-and-white striped structure ("temple") documented with gold dome, wooden door frame, terracotta roof tiles, surrounding gardens and paths.

### Zorro Ranch, New Mexico
Hundreds of photos labeled "Jean Luc Zorro" documented ([EFTA00004763](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004763.pdf)). The 15-year-old victim impact statement describes being "positioned on his floor so that I was confronted by all the framed photographs on his dresser of him smiling with wealthy celebrities and politicians" ([EFTA00019994](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019994.pdf)).

## L. Estate Fine Arts -- Never Appraised

The estate filing listed "Fine Arts, Antiques, Collectibles" as "TBD subject to appraisal/valuation" ([EFTA00027979](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027979.pdf)). The USVI First Amended Complaint confirmed: "The Estate has not yet valued his fine arts, antiques, and other valuables" ([EFTA00018778](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018778.pdf)). The estate petition listed other categories precisely: Cash ($56,547,773), Fixed Income ($14,304,679), Equities ($112,679,138), Aviation/Automobiles/Boats ($18,551,700), Hedge Funds and Private Equity ($194,986,301). Only art was left as "TBD." Given $30.5M in 2017 auction proceeds alone, the collection was worth tens of millions at minimum. The Millea Bros. auction yielded approximately $100K total with no Epstein provenance noted -- a fraction of the collection's documented value. Guernsey's auction house pitched the DOJ to handle the sale ([EFTA00032555](https://www.justice.gov/epstein/files/DataSet%208/EFTA00032555.pdf)).

## M. Art in Abuse Settings

Art was deployed as an instrument of psychological control across every property:

**9 East 71st Street:**
- Massage room mural: "A large painting or mural on the wall, featuring a figure in a dynamic pose" ([EFTA00000167](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000167.pdf))
- Per victim testimony: "ascending a staircase lined with nude photographs of young girls" ([EFTA01159653](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01159653.pdf), via Palm Beach Post)
- "Coming of Age Ceremony" mural by Jorge Alvarez (1995): floor-to-ceiling painting in the Pink Room depicting a pre-teen boy in an aroused state with demonic figures -- displayed in the room where abuse occurred
- Statue of child hanging from rope suspended above the central stairwell ([EFTA00000057](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000057.pdf))
- Custom chess set: Epstein as King, members of his household as other pieces
- First edition of Nabokov's "Lolita"

**358 El Brillo Way:**
- Victim testimony: "naked pictures of girls," "mural or pictures of naked girls either exposing their breasts or completely naked" ([EFTA00009448](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009448.pdf))
- Nine framed photographs taken into evidence by Palm Beach PD alongside "very large statue of man with a bow" ([EFTA00007157](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007157.pdf))

**Zorro Ranch:**
- Victim positioned on the floor "confronted by all the framed photographs on his dresser of him smiling with wealthy celebrities and politicians" -- art and photographs used as instruments of intimidation, conveying the message that Epstein was protected by powerful people ([EFTA00019994](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019994.pdf))

**Pattern:** Art served four simultaneous functions in the Epstein operation: (1) financial opacity vehicle ($30.5M auction proceeds routed through trusts and LLCs, 1031 like-kind exchanges, multi-entity holding structures); (2) grooming tool ("patron of the arts" scholarships targeting minors); (3) psychological control mechanism (nude art and celebrity photographs in abuse settings); and (4) display of power and social access (Guggenheim, MoMA, SFMOMA, Met, Musee d'Orsay connections).

## N. Institutional Art Connections

### New York Academy of Art (NYAA)
Grooming pipeline: "scholarships for the arts" used to access a 13-year-old ([EFTA00019101](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019101.pdf)). Dean Eileen Guggenheim named as Epstein associate ([EFTA01652757](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652757.pdf)). Maria Farmer (MFA 1993-1995) filed the first-ever criminal complaint about Epstein with FBI/NYPD in 1996. At her thesis show, Guggenheim urged Farmer to sell to Epstein/Maxwell. NYAA issued formal apology to Farmer in August 2020.

### Museum of Modern Art (MoMA)
Both Leon Black (Board Chairman until March 2021) and Ronald Lauder (Board trustee) served on MoMA's board. Their joint art ownership through Friends Ventures LLC ($25M Schwitters) was coordinated by Epstein. Black's forced resignation from the chairmanship followed the exposure of his Epstein payments.

### SFMOMA
Epstein donated "ComplexCity" by John F. Simon Jr. under a "fractional ownership" agreement in 2001. Director Neal Benezra wrote to Epstein (2009) expressing appreciation for "continued support in building our collection." Deaccessioned October 2019 -- two months after Epstein's death.

### Metropolitan Museum of Art
$5,000 donation from Enhanced Education Foundation for Met Gala 2014. Minor financial connection but establishes institutional touchpoint.

### Musee d'Orsay
Private after-hours access arranged for Epstein and Woody Allen: "the govt is going to open the musee dorsay for me and woody alien at 4" on a Sunday in March 2012 ([EFTA02124200](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02124200.pdf)). French government providing private museum access to a convicted sex offender.

## O. Epstein's Art Staff Infrastructure

Resume found at [EFTA00038908](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038908.pdf) documents: art purchasing, restoration, shipping, and insurance operations across 7 estates employing approximately 40 staff members. This was not a casual art collection -- it was an industrial-scale art operation requiring dedicated staff, insurance policies, shipping logistics, and relationships with major auction houses.

---

# IX. DIGITAL FORENSICS

## A. 460+ Apple Mail PLIST Metadata Documents

460+ documents across the corpus contain Apple Property List (PLIST) metadata from Apple Mail email exports. These are NOT device backups -- this is email metadata automatically embedded when emails were printed/exported from Mail.app on macOS.

Two email accounts identified:
- `jeevacation@gmail.com` -- Epstein's primary Gmail (45+ docs with PLIST metadata, 683 total across all formats)
- `sarahk525@mail.mac.com` -- Sarah Kellen's Apple Mail (.mac.com = Apple's pre-iCloud email service, pre-2012)

Date range: September 1, 2009 to October 5, 2018 (9 years, ending ~9 months pre-arrest). Remote-id progression (19,372 to 542,078) implies approximately 520,000+ emails at ~225/day. All 12 failed redaction documents show `date-last-viewed = 0`, indicating the account was bulk-synced for forensic export rather than actively used through Apple Mail.

Lesley Groff = heaviest PLIST presence (40+ documents), confirming her role as primary communications coordinator.

## B. 12 Failed Redaction Overlays

12 documents had PLIST XML content recovered from beneath failed redaction overlays (bad_overlay, confidence 0.77-0.99). The redaction tools failed to handle embedded XML metadata -- the PLIST was part of the email body text that redactors attempted to hide but did not properly flatten. Key documents exposed:

- **[EFTA01792918](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01792918.pdf) (MOST SIGNIFICANT):** 5-page emotional email from young Russian/Eastern European woman to Epstein: "I'm not a toy Jeffrey." Describes sexual transactional dynamics ("babydolls," "I know what you expect from me"), a shoplifting arrest, failing model career, Westminster International University enrollment, expiring visa, and financial desperation. Sent 70 minutes after another email from "Scott" asking if Epstein was in St. Thomas and wanting "his friend fly to [the island] to keep him company at night."

- **[EFTA01781767](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01781767.pdf):** Epstein sends a casual email about American Idol from his iPhone in May 2009 -- during his work release/incarceration period. The "Sent from my iPhone" signature plus full PLIST XML (confidence 0.99) confirms iPhone access during his sentence.

- **[EFTA02114558](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02114558.pdf):** Elite neuroscience dinner planning. Ed Boyden (MIT) and Neil Gershenfeld (MIT) organizing dinner with invitees David E. Shaw (billionaire hedge fund founder), Yann LeCun (Facebook AI / Turing Award winner), John Hopfield (Princeton), and Sebastian Seung (Princeton). Gershenfeld CC'd "Jeff" for guest list approval -- demonstrating Epstein's gatekeeper role in elite scientific circles.

- **[EFTA02522767](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02522767.pdf):** Lesley Groff calling the US State Department looking for Senator George Mitchell, who had returned to DLA Piper.

- **[EFTA01774370](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01774370.pdf):** Anonymous sender in the basement of Epstein's 71st Street townhouse going through "boxes of old things, house plans."

- **[EFTA01774075](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01774075.pdf):** Anonymous sender asking for apartment use January 10-14, signs "xo" -- post-conviction.

- **[EFTA02696356](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02696356.pdf):** "Jennie Enterprise" (CORE, 66 East 55th St) -- Africa travel reference.

## C. 420-Timestamp Transaction Correlation Analysis

420 emails with parseable Apple Mail PLIST timestamps were cross-referenced against critical financial transaction dates. Results:

| Transaction | Email Activity | Correlation |
|-------------|---------------|-------------|
| $13.5M Tudor (Aug 2014) | 23 emails/month, 21 in 14-day window | **STRONGEST** -- same-day email to "President" |
| $30.5M Sotheby's/Haze (Jan 2017) | 39 emails in 2 weeks | **STRONG** -- Leon Black "sensitive accounts" -10d |
| KYC Breach (Apr 16, 2018) | 8 emails | MODERATE -- "lawyer/accountant team" intro -5d |
| $48.3M Haze Drain (Jun 2018) | 12 emails | MODERATE -- Kahn/Christie's, Maybach exchange |
| $25M Rothschild (Dec 2015) | 1 email | WEAK -- but Marrakesh flight +7 days |
| $100K Aviloop (Nov 30, 2018) | **0 PLIST emails** | Zero in DS11 PLIST (DS9 confirms active email) |
| Emergency Wires (Dec 2018) | **0 PLIST emails** | Zero in DS11 PLIST (DS9 confirms active email) |
| $31.5M Dissolution (Feb 2019) | 2 emails (household only) | **MINIMAL** |

The 99-day PLIST gap (November 14, 2018 through February 21, 2019) covers the most critical financial crisis period -- when the Miami Herald story broke, emergency wires were sent to co-conspirators, and the $31.5M dissolution occurred. **CORRECTION (Revisit #48):** DS9 has established that Epstein's email was continuously active throughout this period. The gap was specific to the PLIST metadata extraction from DS11, not a real communication cessation.

Key financial correspondents identified through PLIST analysis:
- **Richard Kahn** (HBRK Associates, 575 Lexington Ave): 7 emails -- trust operations, Christie's art, Maybach exchange, trustee changes
- **David Mitchell** (Mitchell Holdings): 4 emails -- "cascade" payments, property inspections
- **Leon Black**: 1 email (highly significant) -- "liquidate the J BLACK trust," "sensitive accounts"
- **Larry Visoski**: 7 emails -- flight logistics, aircraft negotiations
- **Lesley Groff/Croft**: 5+ emails -- scheduling, World Cup tickets
- **Ariane de Rothschild**: 1 email -- "nobody can access" new email, Sotheby's mention

## D. Complete Seized Device Inventory

Over 70 devices seized from three locations between July and August 2019, cataloged under CART Case 50D-NY-3027571 ([EFTA00038465](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038465.pdf)):

**New York Mansion (July 6, 2019 search warrant):**

| Category | Item Numbers | Description |
|----------|-------------|-------------|
| Desktop Computers (10) | 1B28, 1B41-43, 1B53-54, 1B57, 1B59, 1B61, 1B70 | Apple (5), HP Compaq, Dell, Cube 9000 Siteserver, MSI, Dell Precision Tower 5810 |
| Laptops (3) | 1B62, 1B96, 1B97 | Sony Vaio (NYCO24336/37), Toshiba, HP (S/N CND81368V5) |
| Phones and Tablets (6) | 1B55, 1B67-69, 1B71, 1B72 | White iPhone 5 (cellophane), 3 iPads, **Critical iPhone 1B71** (IMEI 357201093322785 / NYCO24318), Silver iPad |
| Hard Drives (13) | 1B29-37, 1B56, 1B60, 1B73-74 | 9 Seagate Path/100 drives, Seagate Backup Plus 1TB, Seagate Barracuda 80GB, 2 loose black drives |
| USB Drives (8) | 1B38-40, 1B44, 1B46-48, 1B51-52 | DataTraveler 4GB (2), Mentor Media 32GB, SD adapter 16GB, EMTEC 16GB (2), Cruzer 32GB (4), **SPIEF 2014** |
| Optical Media (181+) | 1B45, 1B63, 1B75, 1B78 | 10 assorted CDs, 45 assorted CDs, 2 blue binders (58 discs), 4 binders (68 discs) |
| Voice Recorders (3) | 1B64-66 | Sony BM-560, Silver Olympus, Black Radio Shack |
| Cameras (2) | 1B58, 1B99 | Sony with black case, Red Nikon |

Note: The "SPIEF 2014" USB (1B52) is labeled after the St. Petersburg International Economic Forum. The contents of this USB have not been disclosed in the released documents.

**USVI / Little Saint James (August 2019 search warrant):**

| Category | Item Numbers | Description |
|----------|-------------|-------------|
| Mac Desktops (8) | 1B80, 1B85, 1B87, 1B98, 1B102, 1B107, 1B118, 1B21 | Including "Kitchen Mac" (1B80, grey, first USVI device produced) |
| Mac Laptops (2) | 1B81, 1B82 | "JE BIG LAPTOP" (1B81, in "Black Bag" brand bag), MacBook Pro (S/N CO2ZAMOGUQWOP) |
| iPads (2) | 1B83, 1B84 | Both Model A1567 (iPad Air 2) |
| iPod (1) | 1B103 | iPod Shuffle on watch band |
| Servers and Networking (6) | 1B15-17, 1B109, 1B111, 1B112 | HP Server (4x500GB drives), Panasonic KX-TDE100 telecom, 6-bay server (146GB drives), **Unifi Cloud Key**, **Unifi Video NVR** (UVC-NVR-278), **Unifi Server** |
| Windows PCs (5) | 1B19-20, 1B22-24 | HP Desktop Tower (2), Lenovo Tower (2), HP Tower |
| Voice Recorder (1) | 1B108 | Olympus Digital |

The Unifi Video NVR (Network Video Recorder) on Little Saint James is significant -- it demonstrates a dedicated video recording system separate from the concealed camera surveillance documented at the Manhattan property (prosecution memo: "cameras in his clock").

**Seized from Epstein's Person (July 6, 2019 arrest at Teterboro Airport):**
- 1 iPhone (per [EFTA00015561](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015561.pdf) -- draft search warrant for "JE phone & iPad")
- 1 iPad

**2005 Palm Beach Forensic Image (Never Searched):**
- 16 DVD-R discs containing PBCSO EnCase forensic image
- Case # 05-250067
- Found in FBI Florida Office file ([EFTA00015823](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015823.pdf))

**Total estimated devices: 70-80+ unique items, cataloged across 50+ NYCO tracking numbers**

## E. Forensic Processing Dysfunction

The evidence handling timeline documents 17+ months of catastrophic failure:

| Date | Event | EFTA |
|------|-------|------|
| Jul-Aug 2019 | Devices seized | Multiple |
| Nov 2019 | First hard drive produced with 38 folders, no device attribution | [EFTA00009802](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009802.pdf) |
| Feb 15, 2020 | "impossible for us to keep track" | [EFTA00009802](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009802.pdf) |
| Mar 2, 2020 | FBI network teardown: "mandated we delete old stuff (about 400 TB)" | [EFTA00009802](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009802.pdf) |
| **Mar 9, 2020** | **"the FBI is completely fucking us on this"** | **[EFTA00009941](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009941.pdf)** |
| May 2020 | COVID: FBI examiner reduced to 1 day/week | [EFTA00009941](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009941.pdf) |
| May 12, 2020 | "Relativity is NOT a forensic tool" warning | [EFTA00016425](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016425.pdf) |
| Jul 24, 2020 | 71,000+ zero-byte files discovered in initial 7 devices | [EFTA00032065](https://www.justice.gov/epstein/files/DataSet%208/EFTA00032065.pdf) |
| Jul-Aug 2020 | 2 servers with physically failed drives sent to HQ | [EFTA00009941](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009941.pdf) |
| Oct 14, 2020 | "All devices available through CAIR for over a year" | [EFTA00037676](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037676.pdf) |
| Oct 2020 | 6+ machines STILL unexported | [EFTA00037676](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037676.pdf) |
| Nov 9, 2020 | Sixth Production: iPhone NYCO24318 finally produced | [EFTA00030562](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030562.pdf) |
| Jan 27, 2021 | 2,100 HC images compiled from 14 devices | [EFTA00020974](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020974.pdf) |
| Apr 9, 2021 | Government: 2005 computer will NOT be searched | [EFTA00015823](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015823.pdf) |
| **2023** | **Additional CSAM discovered during estate settlement** | **[EFTA00039019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00039019.pdf)** |

FBI CART examiner credentials: Senior Forensic Examiner with certifications in Cellebrite (CCO + CCPA), EnCase, FTK, XRY, Blacklight, BlackBag Mac Forensics, BERLA Vehicle Forensics, IACIS Windows Forensics, over 1,000 pieces of computer media analyzed across 300+ cases since 2005, Master's degree in Digital Forensics and Cyber Security ([EFTA00029601](https://www.justice.gov/epstein/files/DataSet%208/EFTA00029601.pdf)).

## F. CSAM Confirmed

- FBI CID summary (approved 7/17/2024): "There was a small number of CSAM images found on one of Epstein's devices" ([EFTA00038617](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038617.pdf))
- CD labeled "girl pics nude book 4" in evidence ([EFTA02730741](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730741.pdf))
- "Nudes 1" and "Girl pics nude" found in locked safe ([EFTA00024584](https://www.justice.gov/epstein/files/DataSet%208/EFTA00024584.pdf))
- ~2,100 "highly confidential" nude/semi-nude images/videos compiled from 14 devices ([EFTA00020974](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020974.pdf))
- ~3,400 additional images from seized discs
- ~7 hard copy nudes from FBI Florida Office investigation file
- Additional CSAM found during 2023 estate settlement -- missed in initial processing ([EFTA00039019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00039019.pdf))
- "girlsonplane_img" Photoshop file at 7000x5600 pixels among Zorro Ranch photos ([EFTA00005284](https://www.justice.gov/epstein/files/DataSet%203/EFTA00005284.pdf))
- Photo album index page with categories: "THAIS, MOSCOW GIRLS," "NUDES," "YOGA GIRLS" ([EFTA00004477](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004477.pdf))

## G. Cross-Case Evidence Discovery

During the We Build The Wall case Cellebrite review of Steve Bannon's iPhone 7, FBI discovered:
- Text messages between Bannon and Epstein (April 12, 2021) -- "not responsive to our warrant" ([EFTA00027290](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027290.pdf))
- Trump-Maxwell photograph (June 11, 2021) -- "no need to do anything with this one" ([EFTA00025553](https://www.justice.gov/epstein/files/DataSet%208/EFTA00025553.pdf))
- The same SDNY team worked both cases, creating extraordinary cross-case evidence access that was never exploited

---

# X. EVIDENCE GAPS AND OPEN QUESTIONS

This section catalogs the most significant unresolved questions and unexamined evidence in the case. Each gap is graded by potential significance.

## A. 2005 Computer Forensic Image — Never Examined by Federal Authorities -- CRITICAL
A complete forensic image of Epstein's computer from the peak period of documented child sexual abuse -- when dozens of minor victims were being recruited and abused in Palm Beach -- was never examined by federal authorities. Sixteen DVD-R discs containing Palm Beach County Sheriff's Office EnCase forensic image files sat unexamined in the FBI Florida Office's file ([EFTA00015823](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015823.pdf)). Each disc labeled "Disk 1 of 16" through "Disk 16 of 16," with description "Palm Beach County Sheriff's Office Case # 05-250067 Epstein EnCase Files Palm Beach PD DVD-R for General VERBATIM DVD Computer Crimes Unit." FBI New York initially could not open the files and believed them inoperable. They later confirmed the files were "consistent with a forensic image of a computer." The 2005 search warrant authorized seizure but not searching. No subsequent federal warrant was ever obtained. Government stated it "did not intend to obtain a warrant." Estate "repeatedly unwilling to waive any attorney-client privileges." (Note: The Palm Beach County Sheriff's Office Computer Crimes Unit created the forensic image, and local authorities may have conducted some examination of the original computer — including in connection with the 2006 Palm Beach grand jury — but this is not addressed in the federal documents.)

## B. Honeycomb Partners ($64M) -- CRITICAL
The single largest external recipient in the entire financial network: $53M to Honeycomb Partners LP, $10M to Honeycomb Ventures IV LP, $1M to Honeycomb Ventures I LP. Payments from Southern Trust Company and The 2017 Caterpillar Trust continued through March 2019 -- less than four months before arrest. The controlling persons behind Honeycomb remain unidentified in any database. 1.8M redaction records, 38K OCR records, 21K image records yield zero identification. This is the single most significant financial gap: $64 million flowed to an entity whose beneficiary has never been publicly identified.

## C. Southern Trust Revenue Sources -- CRITICAL
Southern Trust reported $656 million in aggregate net income (2013-2017) with $73.6 million in tax exemptions ([EFTA00018778](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018778.pdf)). NYT reporter Matthew Goldstein noted: "The biggest question remains the $200 million that Epstein's Southern Trust took in as revenue... We remain committed to getting to the bottom of this puzzling influx of cash" ([EFTA00023239](https://www.justice.gov/epstein/files/DataSet%208/EFTA00023239.pdf)). Documented inflows from identified sources: Black ($168M), Rothschild ($25M), Tudor ($13.5M), Blockchain Capital ($15M), Josephson ($200K), Seed Media ($304K), Muchnik ($500K), art auction proceeds ($30.5M). Even combining all documented sources, the total falls hundreds of millions short of $656 million. The remaining revenue sources are unexplained.

## D. VHS Surveillance Tapes -- HIGH
Professional time-lapse surveillance recordings (Maxell T-160, 160-minute capacity) seized from Epstein properties with evidence labels "ITEM WAS NOT SCANNED" ([EFTA00007741](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007741.pdf), [EFTA00007984](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007984.pdf), [EFTA00007987](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007987.pdf), [EFTA00007990](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007990.pdf)). Given the prosecution memo's "cameras in his clock" statement and the multi-monitor surveillance control room, these tapes potentially contain recordings of events in Epstein's properties. Their contents are permanently unknown.

## E. Unnamed French Hotel Chain Owner -- HIGH
Victim compilation ([EFTA00022133](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022133.pdf)) references an unnamed "French hotel chain owner" among individuals to whom victims were trafficked. Exhaustive search yielded zero identification across all document collections. The Accor hotel chain appears in redacted files but no individual owner was identified. The victim's statement about "12-year-old girls flown from France for Epstein's birthday" ([EFTA00020703](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020703.pdf)) corroborates the French connection.

## F. Ghost Aliases from Victim Journals -- HIGH
The victim explicitly stated that the following names "are not who they say" -- confirming they are aliases: Mr. Mody, Mr. Sant, Mr. Ludwig, Mr. Cecchi, Mr. Mora, Mr. Goodlatte, Mr. Atkins, Mr. Robert, Mr. Caruthers, Mr. Islam, Mr. Conway, Mr. Jacobson. All have zero additional hits across the entire 218GB corpus, supporting the victim's claim. These aliases likely conceal the identities of additional abusers who have never been identified.

## G. "Oleg" (Likely Deripaska) -- HIGH
Mandelson forwarded Moscow City penthouse details to Epstein mentioning "Oleg has a great woman who looks after things for him" (November 2009, [EFTA02434424](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02434424.pdf)). Zero results for "Deripaska" across all document collections despite the contextual identification. The identification of "Oleg" as Deripaska is circumstantial (based on Mandelson's known relationship with Oleg Deripaska), and his absence from the corpus may simply mean the connection was not within the scope of the investigation.

## H. Bannon-Epstein Text Content -- HIGH
Text messages found on Bannon's iPhone 7 during WBTW Cellebrite review (April 2021). AUSA: "not responsive to our warrant" ([EFTA00027290](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027290.pdf)). No separate warrant was ever sought. A Trump-Maxwell photo on the same phone was dismissed: "no need to do anything with this one" ([EFTA00025553](https://www.justice.gov/epstein/files/DataSet%208/EFTA00025553.pdf)). A mock interview YouTube video between Epstein and Bannon vanished before investigators could view it ([EFTA00037236](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037236.pdf)). The same SDNY team worked both cases, creating extraordinary cross-case evidence access that was never exploited.

## I. Austrian Passport Investigation -- HIGH
FBI/NYPD CEHT agent assigned to call the real Marius Fortelni at forteproperties.us in Southampton, NY on July 16, 2019 ([EFTA00025539](https://www.justice.gov/epstein/files/DataSet%208/EFTA00025539.pdf)). No record of the call or its outcome exists. Government rebuttal to defense "personal protection" claim: passport was "actually used" with "numerous ingress and egress stamps" for France, Spain, UK, and Saudi Arabia in the 1980s ([EFTA00016172](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016172.pdf)). Austrian Embassy formally requested information July 22, 2019 ([EFTA00016173](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016173.pdf)). No record of what was shared. Epstein died 25 days later. Investigation permanently unresolved. The Saudi Arabia residence listed in the passport, combined with the 48 diamonds and cash found in the same safe, raises questions about Epstein's historical Middle Eastern connections.

## J. 6+ Machines Unexported as of October 2020 -- MODERATE-HIGH
As of October 2020 -- more than a year after seizure -- six or more machines remained unexported from FBI CART. "All devices and media have been available through CAIR for over a year" but SDNY could not access them through the production pipeline ([EFTA00037676](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037676.pdf)). Whether these devices have ever been fully examined remains unclear.

## K. Ms. Vicki -- MODERATE-HIGH
Unidentified female facilitator operating in Florida and California. Mentioned in victim journals alongside a Weinstein reference. Zero hits beyond journal text across all document collections. The existence of an unidentified female recruiter/facilitator operating across two states suggests an additional co-conspirator who was never investigated.

## L. Biological Mother as Trafficker -- MODERATE-HIGH
FBI prosecution notes: victim's biological mother "forced [victim] to perform sexual acts with adult men since she was very young. Her younger sister also. Even worse, the paternal grandfather... was in on it" ([EFTA02731488](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731488.pdf)). This familial trafficking network was never independently investigated. The victim was subsequently "trafficked to at least 25 different men" through the Epstein operation. The intersection of familial and commercial trafficking in this case was unprecedented.

## M. "The Gregorys" and "Mr. Robert and Jill" -- MODERATE
Unidentified couples from victim journals who served as entry points into Epstein's network. "Mr. Robert and Jill" hosted the party where the victim first met Maxwell ("British lady from Clearwater"). "The Gregorys" are named alongside AOL executives and others. Zero identification across all document collections.

## N. Dilorio Whistleblower Follow-Up -- MODERATE
SEC whistleblower Christopher Dilorio filed 16 documents connecting ESWW (Environmental Solutions Worldwide) shell companies to Epstein-Apollo money flows three months before arrest. Epstein's Financial Trust Company appears in the same SEC filing as Leon Black/Apollo entities. Dilorio alleges SEC dropped the Apollo investigation after a Kushner Jr./Joshua Harris White House meeting. Received 11-12 threatening anonymous phone calls. Filed with SEC Commissioners, DOJ, FINRA, and FinCEN ([EFTA00009904](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009904.pdf)+). No public resolution.

## O. Richard Taus Claims -- MODERATE
Former FBI Special Agent Richard Taus (Clinton Correctional Facility, inmate #91A1040) sent a letter to Acting USA Audrey Strauss claiming information about Epstein's death, Maxwell, and a "J. Doe" prison visitor ([EFTA00006036](https://www.justice.gov/epstein/files/DataSet%204/EFTA00006036.pdf), [EFTA00038276](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038276.pdf)). Decorated Lt. Colonel (Vietnam War helicopter pilot). SDNY processed as "Civilian Crime Report." Internal note: "this particular submission does not really fit that so we might not get anything more." No evidence of follow-up interview.

## P. Former Zorro Staff Video Claim -- MODERATE
A former Zorro Ranch staff member submitted a tip about video footage of minors. The FBI treated the submission as potential extortion rather than as evidence ([EFTA00038382](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038382.pdf)). The tip was never followed up as a substantive lead.

## Q. Surveillance Tip Ignored -- MODERATE
An individual reported observing Epstein with a "young girl" on Palm Beach bike paths in late 2018/early 2019 -- months before arrest ([EFTA00020778](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020778.pdf)). Internal note: "nothing was done."

## R. MC2 Tel Aviv Records -- MODERATE
Despite MC2 publicly operating a Tel Aviv office with a stated recruitment age of "Between 13 and 20 years old" ([EFTA01728258](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01728258.pdf)), zero results for "MC2 Tel Aviv" appear in any database. The absence of records from an office publicly recruiting minors in a foreign jurisdiction suggests either that records were never seized or were never produced by the DOJ.

## S. CSAM Discovery Timing -- MODERATE
CSAM found in 2023 during estate settlement ([EFTA00039019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00039019.pdf)) demonstrates that the initial 2019-2021 evidence processing missed material. This raises questions about what else may have been missed in the 70+ devices, 181+ CDs/DVDs, and 12 TB+ of raw data.

---

# APPENDIX A: MASTER EFTA CITATION INDEX (100 Most Important Documents)

## Tier 1: Financial Architecture (Documents 1-15)

| # | EFTA | Description |
|---|------|-------------|
| 1 | [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) | Deutsche Bank financial exhibits -- ALL transaction chains (Exhibits A-E), $755M documented, 14 Black wire transfers, auction house proceeds, investment fund allocations |
| 2 | [EFTA01359500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01359500.pdf) | Deutsche Bank account officer roster -- Litchford/Morris managing Epstein + Black + Boies + Wanek simultaneously |
| 3 | [EFTA01381149](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01381149.pdf) | RM CODE 82289 complete balance snapshot Aug 2018 -- 15+ Epstein entities, $50M+ total, Haze Trust $40.5M |
| 4 | [EFTA01362456](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362456.pdf) | "kyc is not happening" -- Deutsche Bank internal admission of compliance failure, April 16, 2018 |
| 5 | [EFTA01414241](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01414241.pdf) | "URGENT - THIRD REQUEST!!!!!" -- AML escalation on Epstein accounts, ignored by management |
| 6 | [EFTA01431221](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01431221.pdf) | $23M wire approval by Stewart Oldfield -- strongest evidence of individual banker mishandling |
| 7 | [EFTA01426081](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01426081.pdf) | LSJE stop-wire attempted AFTER wire already processed -- compliance arrived too late |
| 8 | [EFTA01406955](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01406955.pdf) | KYC breach documentation for SOUTHFINANMD, chain beginning April 16, 2018 |
| 9 | [EFTA01477330](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477330.pdf) | Wanek Trust / "Third Lake Capital Relationship" -- same DB team managing Ashley Furniture CEO |
| 10 | [EFTA00018778](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018778.pdf) | USVI First Amended Complaint -- Southern Trust $656M income, "hundreds" of victims, estate filing |
| 11 | [EFTA02730996](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730996.pdf) | Apollo/Dechert conflicts report -- Black $158M payments, art management, contested Picasso |
| 12 | [EFTA02731023](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731023.pdf) | Senate Finance Committee -- Black's art collection >$1B, refused to answer questions |
| 13 | [EFTA02664953](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664953.pdf) | Epstein to Leon Black: "liquidate the J BLACK trust," alarm about "sensitive accounts" (Dec 2016) |
| 14 | [EFTA02502971](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02502971.pdf) | Ariane de Rothschild: "nobody can access" new email, 8 months before $25M transfer |
| 15 | [EFTA00023239](https://www.justice.gov/epstein/files/DataSet%208/EFTA00023239.pdf) | NYT reporter Goldstein: "$200 million unexplained revenue" in Southern Trust |

## Tier 2: Victim Testimony and Trafficking Evidence (Documents 16-35)

| # | EFTA | Description |
|---|------|-------------|
| 16 | [EFTA02731488](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731488.pdf) | FBI prosecution call notes -- "16 when raped by Black," "25 different men," biological mother trafficking |
| 17 | [EFTA02731576](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731576.pdf) | Victim direct text to Leon Black: "You sexually harassed me, sex trafficked me, raped me" |
| 18 | [EFTA02731721](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731721.pdf) | Wigdor Law letter — victim trafficked to Leon Black AND Larry Summers |
| 19 | [EFTA02731420](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731420.pdf) | First victim journal -- Black, Mitchell, Summers, Dershowitz, Leonsis, Snyder, Case, 20+ names |
| 20 | [EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf) | Second victim journal -- Leonsis filmed, Staley belt, Krauss, Minsky, AOL, forced pregnancy |
| 21 | [EFTA00022133](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022133.pdf) | 9-page victim accusation compilation -- Richardson, Mitchell, Minsky, Brunel, foreign president |
| 22 | [EFTA00004070](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004070.pdf) | 30-page FBI evidence package -- victim born ~1985, 4 assaults before 18, Brunel companion, Campbell on island |
| 23 | [EFTA00008631](https://www.justice.gov/epstein/files/DataSet%206/EFTA00008631.pdf) | 14-year-old Grand Jury testimony -- Maxwell bought "little girls underwear," Zorro Ranch 1996 |
| 24 | [EFTA00019994](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019994.pdf) | 15-year-old victim impact statement -- sexually molested at Zorro Ranch, celebrity photos as intimidation |
| 25 | [EFTA00020703](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020703.pdf) | 12-year-old French girls flown for birthday, bear-his-child proposition, victim escaped to Australia |
| 26 | [EFTA02491935](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02491935.pdf) | TOEFL grooming: "becoming a mistress," met Gates and Woody, modeling career destroyed |
| 27 | [EFTA02474955](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02474955.pdf) | Russian woman visa canceled, Epstein asks for "naughty selfie" alongside passport photo |
| 28 | [EFTA00016836](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016836.pdf) | Victim "database" tracking "availability and proximity" |
| 29 | [EFTA01728258](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01728258.pdf) | MC2 submission requirements: "Age: Between 13 and 20 years old" |
| 30 | [EFTA00028785](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028785.pdf) | Government detention memo -- wire transfers to co-conspirators, victim parent driven off road |
| 31 | [EFTA02731515](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731515.pdf) | Wigdor attorney: video on sex site, 6 men at hotel, victim with 3, "former friend of Leon Black" |
| 32 | [EFTA02731729](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731729.pdf) | Second independent victim corroborates Black's specific violent acts: "almost a perfect match" |
| 33 | [EFTA00013253](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013253.pdf) | Allred FBI package -- 7+ victims including 2010 townhouse interaction with Prince Andrew |
| 34 | [EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf) | Maxwell/SDNY prosecution memo -- cameras in clock, Wexner theft, victim "lent out," Dubin directive |
| 35 | [EFTA00019101](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019101.pdf) | "Patron of the arts" grooming -- "scholarships for the arts" used to access 13-year-old |

## Tier 3: Death Investigation and Surveillance (Documents 36-50)

| # | EFTA | Description |
|---|------|-------------|
| 36 | [EFTA00038617](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038617.pdf) | FBI CID summary (approved 7/17/2024) -- CSAM confirmed, "no cameras" claim contradicts prosecution memo |
| 37 | [EFTA02731226](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731226.pdf) | Maxwell prosecution memo -- "Epstein had cameras in his clock" |
| 38 | [EFTA00029761](https://www.justice.gov/epstein/files/DataSet%208/EFTA00029761.pdf) | 2003 Palm Beach police -- cameras concealed in clocks, monitored on computer hard drive |
| 39 | [EFTA01649190](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01649190.pdf) | MCC DVR system analysis -- DVR 2 failure 12 days before death, 192 cameras, NiceVision contract |
| 40 | [EFTA00039025](https://www.justice.gov/epstein/files/DataSet%209/EFTA00039025.pdf) | OIG report -- catastrophic disk failures, Quantico recovery failed, "no recordings after July 29" |
| 41 | [EFTA00023970](https://www.justice.gov/epstein/files/DataSet%208/EFTA00023970.pdf) | Hard drives seized from DVR 2 at 4:30 PM EDT on death day |
| 42 | [EFTA00007741](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007741.pdf) | VHS surveillance tape (Maxell T-160) -- "ITEM WAS NOT SCANNED" |
| 43 | [EFTA00007984](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007984.pdf) | VHS surveillance tape -- "ITEM WAS NOT SCANNED" |
| 44 | [EFTA00007987](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007987.pdf) | VHS surveillance tape -- "ITEM WAS NOT SCANNED" |
| 45 | [EFTA00007990](https://www.justice.gov/epstein/files/DataSet%204/EFTA00007990.pdf) | VHS surveillance tape -- "ITEM WAS NOT SCANNED" |
| 46 | [EFTA00027732](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027732.pdf) | "Materials returned from 4Chan" -- FBI captured 8+ screenshots from death leak |
| 47 | [EFTA01684283](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684283.pdf) | OCME autopsy report with photographs -- hyoid fracture, bilateral thyroid cartilage fractures |
| 48 | [EFTA00019322](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019322.pdf) | Will executed August 8, 2019 -- "extremely notable" per SDNY prosecutor |
| 49 | [EFTA00035812](https://www.justice.gov/epstein/files/DataSet%208/EFTA00035812.pdf) | DOJ OIG investigation -- SDNY declined to prosecute BOP employees |
| 50 | [EFTA00035225](https://www.justice.gov/epstein/files/DataSet%208/EFTA00035225.pdf) | Suicide watch logs -- 15-minute observation entries, psychological assessments |

## Tier 4: Intelligence and Prosecution Failures (Documents 51-70)

| # | EFTA | Description |
|---|------|-------------|
| 51 | [EFTA00009016](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009016.pdf) | Acosta deposition -- NPA negotiations, co-conspirator immunity expansion by Dershowitz |
| 52 | [EFTA00009116](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009116.pdf) | Acosta OPR interview -- Dershowitz threat, intelligence asset question (explicit denial with classified info reference, pp. 404-405) |
| 53 | [EFTA00010507](https://www.justice.gov/epstein/files/DataSet%208/EFTA00010507.pdf) | Judge Marra CVRA ruling -- NPA deliberately concealed from victims |
| 54 | [EFTA00013209](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013209.pdf) | DAG meeting memo -- "hundreds of sexual massages with minors," plea negotiations |
| 55 | [EFTA00031495](https://www.justice.gov/epstein/files/DataSet%208/EFTA00031495.pdf) | CBP officer self-incrimination -- "Everyone knew I was friends with Epstein," Badge #CAS03223 |
| 56 | [EFTA00021576](https://www.justice.gov/epstein/files/DataSet%208/EFTA00021576.pdf) | Austrian passport / safe contents -- 48 diamonds, $72K cash, false identity Marius Fortelny |
| 57 | [EFTA00016172](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016172.pdf) | Government rebuttal: Austrian passport "actually used" with "numerous ingress/egress stamps" |
| 58 | [EFTA00016173](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016173.pdf) | Austrian Embassy formal information request, July 22, 2019 |
| 59 | [EFTA00025539](https://www.justice.gov/epstein/files/DataSet%208/EFTA00025539.pdf) | Real Marius Fortelni identified Southampton NY -- FBI assigned to call, NO record of outcome |
| 60 | [EFTA00013730](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013730.pdf) | Epstein touring Israeli military bases under FL indictment (2008) with Benny Shabtai |
| 61 | [EFTA02278459](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02278459.pdf) | Epstein staff cleaning "Ehud's apt" at 301 E 66th (March 2019) |
| 62 | [EFTA00037218](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037218.pdf) | Melvyn Kohn: "certain parties in this mix ARE working for foreign intelligence" |
| 63 | [EFTA00015219](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015219.pdf) | FOIA exemption: "confidential relationship with a foreign government" material withheld |
| 64 | [EFTA00021553](https://www.justice.gov/epstein/files/DataSet%208/EFTA00021553.pdf) | Jane Doe #3: blackmail -- "required her to describe events so he could potentially blackmail them" |
| 65 | [EFTA01731006](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01731006.pdf) | FBI case serial: "attempting to blackmail powerful businessmen in New York" |
| 66 | [EFTA00032751](https://www.justice.gov/epstein/files/DataSet%208/EFTA00032751.pdf) | Boies/Pottinger: "conspiracy to commit extortion" using Epstein's "illicit videos" |
| 67 | [EFTA02484285](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02484285.pdf) | Epstein to Ruemmler: "clinton obama unnecessary implication" (October 2015) |
| 68 | [EFTA02575359](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02575359.pdf) | Epstein to Ruemmler: sealed indictment query day before Manafort unsealing |
| 69 | [EFTA00028149](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028149.pdf) | Barr split recusal -- Southern District of FL "ordered recused by DOJ" |
| 70 | [EFTA00027244](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027244.pdf) | AUSA contradicting Richardson lawyer clearance claim |

## Tier 5: Named Individual Evidence (Documents 71-85)

| # | EFTA | Description |
|---|------|-------------|
| 71 | [EFTA01660622](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660622.pdf) | FBI master briefing deck -- Prominent Names page with all named individuals and allegations |
| 72 | [EFTA01660651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660651.pdf) | NTOC tips compilation -- Allen/Oren/Tal brothers raping at parties, Victoria's Secret models |
| 73 | [EFTA00362483](https://www.justice.gov/epstein/files/DataSet%209/EFTA00362483.pdf) | Single calendar day: Barak, Black, Summers, Thiel all visiting Epstein (Sept 22, 2014) |
| 74 | [EFTA00022062](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022062.pdf) | MLAT request to UK -- simultaneously covering Epstein and Nygard, Prince Andrew in both |
| 75 | [EFTA02633147](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02633147.pdf) | Pritzker-Epstein March 2019: "shit hurricane" -- breakfast plans 4 months pre-arrest |
| 76 | [EFTA02518865](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518865.pdf) | Bannon to Epstein: "To have breakfast with Jared" re MBS Saudi visit (February 2018) |
| 77 | [EFTA00027290](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027290.pdf) | Bannon-Epstein texts on iPhone 7 -- "not responsive to our warrant" |
| 78 | [EFTA00025553](https://www.justice.gov/epstein/files/DataSet%208/EFTA00025553.pdf) | Trump-Maxwell photo on Bannon phone -- "no need to do anything with this one" |
| 79 | [EFTA02633609](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02633609.pdf) | Epstein brokered Barak-Bannon meeting, February 2019 |
| 80 | [EFTA02434424](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02434424.pdf) | Mandelson Moscow penthouse with "Oleg" -- forwarded to Epstein (November 2009) |
| 81 | [EFTA02571022](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02571022.pdf) | Mandelson-Epstein "tastey models and dancing" + St. Petersburg (May 2013) |
| 82 | [EFTA02434434](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02434434.pdf) | Staley + Mandelson + Epstein drinks (December 2009) |
| 83 | [EFTA00029358](https://www.justice.gov/epstein/files/DataSet%208/EFTA00029358.pdf) | SDNY prosecutor: Staley rape allegation during massage (December 2019) |
| 84 | [EFTA02731660](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731660.pdf) | Black settles with USVI for $62.5 million |
| 85 | [EFTA02731577](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731577.pdf) | Brad Edwards (victims' attorney) retained BY Leon Black (October 2024) |

## Tier 6: Digital Forensics and Art (Documents 86-100)

| # | EFTA | Description |
|---|------|-------------|
| 86 | [EFTA00015823](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015823.pdf) | Unsearched 2005 computer -- 16 EnCase DVDs from peak abuse period, NEVER examined |
| 87 | [EFTA00009941](https://www.justice.gov/epstein/files/DataSet%208/EFTA00009941.pdf) | "FBI is completely fucking us" -- 17-month evidence processing dysfunction |
| 88 | [EFTA00039019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00039019.pdf) | Additional CSAM discovered during 2023 estate settlement -- missed in initial processing |
| 89 | [EFTA00020974](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020974.pdf) | 2,100 "highly confidential" nude/semi-nude images from 14 devices compiled January 2021 |
| 90 | [EFTA02730741](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730741.pdf) | CD labeled "girl pics nude book 4" + r/maxwellhill Reddit screenshot in FBI case serial |
| 91 | [EFTA00024584](https://www.justice.gov/epstein/files/DataSet%208/EFTA00024584.pdf) | "Nudes 1" and "Girl pics nude" found in locked safe |
| 92 | [EFTA00005284](https://www.justice.gov/epstein/files/DataSet%203/EFTA00005284.pdf) | "girlsonplane_img" Photoshop file 7000x5600 pixels among Zorro Ranch photos |
| 93 | [EFTA01792918](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01792918.pdf) | "I'm not a toy Jeffrey" -- Russian woman beneath failed redaction overlay |
| 94 | [EFTA02114558](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02114558.pdf) | Neuroscience dinner: Shaw, LeCun, Hopfield, Seung -- guest list sent to "Jeff" for approval |
| 95 | [EFTA01781767](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01781767.pdf) | iPhone email during incarceration (May 2009) -- "Sent from my iPhone" with PLIST metadata |
| 96 | [EFTA02522767](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02522767.pdf) | Lesley Groff calling US State Department looking for Senator Mitchell |
| 97 | [EFTA02323094](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323094.pdf) | Sotheby's Private Client Group (Lily Snyder) handling Epstein accounts |
| 98 | [EFTA02323043](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323043.pdf) | Christie's NY contacts -- Ostrem and Lazaris, staff asking auction procedures |
| 99 | [EFTA00004663](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004663.pdf) | Complete Sotheby's lot sheet for Matisse "Le Reflet" (1935) with full provenance |
| 100 | [EFTA01415196](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01415196.pdf) | Prytanee LLC confirmed on Deutsche Bank RM CODE 82289 balance sheet ($197,214) |

---

# APPENDIX B: COMPLETE REPORT INDEX

Reports produced during the investigation (as of initial compilation), with brief descriptions:

### Session 1-3 Reports (1-27)

| # | Report | Description |
|---|--------|-------------|
| 1 | PROMINENT_NAMES_COMPLETE_RECONSTRUCTION.md | Complete reconstruction of FBI master briefing deck "Prominent Names" page with all named individuals and specific allegations |
| 2 | PRINCE_ANDREW_INVESTIGATION.md | MLAT request to UK, 3 Prominent Names allegations, Nygard dual investigation, systematic refusal to cooperate |
| 3 | LEON_BLACK_INVESTIGATION.md | $168M payment chain, 4+ victims, FBI 302 documentation of violent assault, direct victim text messages |
| 4 | NPA_COCONSPIRATOR_PAYMENTS.md | Non-Prosecution Agreement architecture: blanket co-conspirator immunity expansion, CVRA violations, co-conspirator protection |
| 5 | NTOC_TIPS_INVESTIGATION.md | 288+ National Threat Operations Center tips: Allen/Oren/Tal brothers, Victoria's Secret models, Barr tips |
| 6 | EHUD_BARAK_ISRAEL_INVESTIGATION.md | 301 E 66th apartment nexus, military base tour, IDF-branded clothing on LSJ, Melvyn Kohn letters |
| 7 | DEATH_NIGHT_DVR_TIMELINE.md | MCC DVR catastrophic failure timeline, 192 cameras, NiceVision contract, hard drive seizure chain |
| 8 | FLIGHT_LOG_PASSENGERS.md | Passenger identification from flight records, incomplete logs (pilots did not retroactively add names), weekly cycling routes |
| 9 | VICTORIA_SECRET_PIPELINE.md | Wexner-VS model access pipeline, NTOC tips describing VS models at Epstein parties |
| 10 | TECH_COMPANY_SUBPOENAS.md | Amazon, Google, Apple subpoena records for Epstein-related account data |
| 11 | GATES_NIKOLIC_NETWORK.md | Gates Foundation engagement, Nikolic executor naming, "bgC3" separation agreement, Fitzgerald "due diligence" |
| 12 | SAR_RUSSIAN_MODELS_FINCEN.md | Suspicious Activity Report investigation, 25 subjects, Russian model visa manipulation, MC2 stranding |
| 13 | STALEY_JPMORGAN_INVESTIGATION.md | Jes Staley rape allegation, JPMorgan private banking, FCA investigation, Barclays departure |
| 14 | HAZE_TRUST_47M_TRACE.md | Haze Trust $47M drawdown destination: Southern Financial to Valar, Honeycomb, Boothbay, Plan D |
| 15 | LSJE_WIRE_INVESTIGATION.md | LSJE stop-wire attempted after processing, emergency wire stops documentation |
| 16 | ZORRO_RANCH_NM_INVESTIGATION.md | Zorro Ranch abuse evidence, NM AG asset forfeiture request, Maxwell 1994 land document |
| 17 | SUICIDE_WATCH_LOGS.md | 15-minute observation entries, psychological assessments, premature removal from watch |
| 18 | ATT_RECORDS_ANALYSIS.md | 558-page AT&T records: cell-site data, call logs, communication pattern analysis |
| 19 | DIGITAL_EVIDENCE_DIRECTORY.md | 194-page FBI digital evidence directory: 70+ devices, processing status, chain of custody |
| 20 | CLASSIFIED_INTELLIGENCE_INVESTIGATION.md | SECRET//NOFORN classified document analysis, FOIA intelligence exemption, foreign government relationship |
| 21 | CO_CONSPIRATOR_MEMO_DEEP_DIVE.md | Pages 76-85 of prosecution memo: Kellen, Marcinkova, Ross, Groff plea negotiations and roles |
| 22 | FBI_1996_SOURCE_REPORTING.md | FD-71 1996 source reporting documents: earliest FBI awareness of Epstein activities |
| 23 | CODED_NAMES_IDENTIFICATION.md | Victim journal coded names: ghost aliases, "not who they say," zero-hit confirmation |
| 24 | RODERIC_HAMILTON_INVESTIGATION.md | Hamilton classified document investigation, intelligence community connections |
| 25 | BLACKMAIL_INTELLIGENCE_INVESTIGATION.md | FBI case serial 31E-MM-108062: "attempting to blackmail powerful businessmen in New York" |
| 26 | SESSION3_FINDINGS_UPDATE.md | Cumulative findings through Session 3 |
| 27 | SESSION4_MASTER_FINDINGS.md | Cumulative findings through Session 4 |

### Session 5-6 Reports (28-33)

| # | Report | Description |
|---|--------|-------------|
| 28 | MAXWELL_PROSECUTION_INVESTIGATION.md | Maxwell arrest, trial, conviction (5 of 6 counts), sentencing (20 years), prosecution memo analysis |
| 29 | SESSION6_MASTER_FINDINGS.md | Cumulative findings through Session 6: left-leaning elite, coded language, Giuffre threats |
| 30 | LEFT_LEANING_ELITE_EVIDENCE.md | Gates, Clintons, Hollywood, Mandelson, Summers, Chomsky: documentary evidence for each |
| 31 | GIUFFRE_THREATS_AND_4CHAN_ORIGINS.md | Giuffre death threats (424-doc Tonks campaign), 4chan/QAnon/FBI captured materials |
| 32 | CENTERVIEW_MONEY_TRACE.md | Centerview Partners/Apollo adjacency, Sean Carmody JPMorgan pipeline, financial intermediaries |
| 33 | DEUTSCHE_BANK_INVESTIGATION.md | 40+ accounts, same officers as Black, $49.4M Haze Trust, 25-entity SAR, VIP treatment |

### Session 7 Reports (34-44)

| # | Report | Description |
|---|--------|-------------|
| 34 | VICTIM_JOURNAL_FULL_EXTRACTION.md | Complete 13-page first journal reconstruction: Black, Mitchell, Summers, Dershowitz, 20+ names |
| 35 | [BIOTECH_SCIENCE_NETWORK_INVESTIGATION.md](/scientists/BIOTECH_SCIENCE_NETWORK_INVESTIGATION.md) | Edge Foundation pipeline: Brin/Page/Bezos 2004 dinner, Seth Lloyd, George Church, Krauss, Minsky |
| 36 | RICHARDSON_SDNY_COVERUP.md | Richardson "clearance" claim falsification, SDNY frustration, NM AG deferral, never subpoenaed |
| 37 | DC_POWER_BROKERS_INVESTIGATION.md | Leonsis (filming), Pritzker (Hyatt), Josephson ($200K), Zuckerman, Bannon, AOL cluster |
| 38 | HAUB_CHASIN_DEATH_THREATS.md | Karl Erivan Haub disappearance claims, Mark Epstein threats, Dana Chasin aviation intermediary |
| 39 | VICTIM_JOURNAL_2_[EFTA02731465](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731465.pdf).md | Complete 8-page second journal: forced pregnancy, AOL accusation, Leonsis filming, Staley violence |
| 40 | RUEMMLER_OBAMA_WH_COUNSEL.md | 15+ emails (2014-2018), "Clinton Obama unnecessary implication," sealed indictment consultation |
| 41 | MANDELSON_RUSSIA_CONGO.md | Moscow penthouse with "Oleg" (Deripaska), "tasty models," Congo/Andely/Ollivier, Staley drinks |
| 42 | BANNON_CLINTON_EVIDENCE.md | Bannon-Epstein deep relationship (2017-2019), MBS/Kushner intelligence, Clinton 300+ photo archive |
| 43 | AOL_NEXUS_INVESTIGATION.md | 4 AOL executives named (Case/Kimsey/Leonsis/Vradenburg), platform accusation, Wigdor video allegation |
| 44 | EUGENICS_PRITZKER_INVESTIGATION.md | Forced pregnancy/piano genes, baby ranch, Pritzker 10-year relationship, Church genetics meeting |

### Session 8 Reports (45-53)

| # | Report | Description |
|---|--------|-------------|
| 45 | [LEON_BLACK_PROSECUTION_FAILURE.md](/individuals/LEON_BLACK_PROSECUTION_FAILURE.md) | Complete prosecution timeline 2021-2024: SDNY + Manhattan DA failures, 4+ victims, video allegation |
| 46 | PROMINENT_NAMES_COMPLETE_V2.md | Full extraction of FBI master briefing deck: all 21 pages, all named individuals with exact allegations |
| 47 | SIEGEL_DILORIO_INVESTIGATION.md | Bill Siegel: 16 EFTA docs, victim journal identification. Dilorio: Apollo/Kushner SEC whistleblower |
| 48 | [ALLRED_VICTIM_INTERVIEW.md](/victims/ALLRED_VICTIM_INTERVIEW.md) | 30-page FBI evidence package: victim born ~1985, 4 assaults before 18, 2 rapes, harem ideology, Brunel |
| 49 | [WILLIAM_BARR_INVESTIGATION.md](/individuals/WILLIAM_BARR_INVESTIGATION.md) | 55+ documents: NTOC "present during abuses," father hired Epstein at Dalton, split recusal, K&E conflict |
| 50 | [LUTNICK_DUBIN_INVESTIGATION.md](/individuals/LUTNICK_DUBIN_INVESTIGATION.md) | Lutnick: single NTOC tip (disgruntled employee). Dubin: 54 documents, "lent out," Eva described as present, 34+ flights |
| 51 | [RUEMMLER_DEEP_DIVE.md](/individuals/RUEMMLER_DEEP_DIVE.md) | 29 documents: "Clinton Obama" warning, "Nigerian" placement, sealed indictment, Goldman Sachs trajectory |
| 52 | [JUNKERMANN_MC2_INVESTIGATION.md](/individuals/JUNKERMANN_MC2_INVESTIGATION.md) | 10+ year relationship, Epstein brokered Black intro, Jan 2019 island, MC2 stranding Russian models |
| 53 | [MARCINKOVA_INVESTIGATION.md](/individuals/MARCINKOVA_INVESTIGATION.md) | Near-zero full-name results in redaction databases (1 hit in DS10), $100K Aviloop wire, 124 flights |

### Session 9 Reports (54-66)

| # | Report | Description |
|---|--------|-------------|
| 54 | [SESSION9_MASTER_FINDINGS.md](/overview/SESSION9_MASTER_FINDINGS.md) | Comprehensive session findings: CBP corruption, Austrian passport, victim census, shell entity map |
| 55 | [FOUR_CHAN_PARAMEDIC_INVESTIGATION.md](/conspiracy-debunking/FOUR_CHAN_PARAMEDIC_INVESTIGATION.md) | 4chan death leak, hard drives removed 10:15 PM, guard DPAs dismissed, employee confession YouTube |
| 56 | [ONLINE_EVIDENCE_INVESTIGATION.md](/conspiracy-debunking/ONLINE_EVIDENCE_INVESTIGATION.md) | r/maxwellhill screenshot in FBI serial, social media led to Maxwell via Borgerson-Angara-Tidewood shells |
| 57 | [UNNAMED_PERSONS_INVESTIGATION.md](/individuals/UNNAMED_PERSONS_INVESTIGATION.md) | Foreign president = Ehud Barak (14+ docs), AOL cluster mapped, 34 journal names cross-referenced |
| 58 | [CBP_CORRUPTION_INVESTIGATION.md](/institutional/CBP_CORRUPTION_INVESTIGATION.md) | Badge #CAS03223 self-incriminated, 7+ years clearing aircraft, FBI proffer sessions Oct-Nov 2020 |
| 59 | [DILORIO_APOLLO_WHISTLEBLOWER.md](/financial/DILORIO_APOLLO_WHISTLEBLOWER.md) | ESWW shell/Epstein Financial Trust in same SEC filing as Apollo, SEC dropped probe, threatening calls |
| 60 | [TRAFFICKING_ROUTES_INVESTIGATION.md](/victims/TRAFFICKING_ROUTES_INVESTIGATION.md) | Aircraft fleet, weekly cycling, MC2 ages 13-20, flight logs incomplete (pilots did not retroactively add names), victim "database" tracking |
| 61 | [PROSECUTION_FAILURES_ANALYSIS.md](/institutional/PROSECUTION_FAILURES_ANALYSIS.md) | NPA architecture, Acosta deposition, blanket co-conspirator immunity expansion, named individual prosecution failures |
| 62 | [SHELL_ENTITY_MAP.md](/financial/SHELL_ENTITY_MAP.md) | 95+ entities across 10 categories under RM CODE 82289 at Deutsche Bank |
| 63 | [VICTIM_CENSUS.md](/victims/VICTIM_CENSUS.md) | Minimum 60-80 individually identified, likely 200+, USVI AG: "hundreds" |
| 64 | [ISRAELI_INTELLIGENCE_DEEP_DIVE.md](/intelligence/ISRAELI_INTELLIGENCE_DEEP_DIVE.md) | 301 E 66th nexus, military base tour, Melvyn Kohn letters, FOIA intelligence exemption |
| 65 | [CBP_RUEMMLER_REMAINING_LEADS.md](/institutional/CBP_RUEMMLER_REMAINING_LEADS.md) | CBP officer expanded, Ruemmler full 15-email trail, 3BIS active construction May 2019 |
| 66 | [UNEXPLORED_DOCUMENT_MINING.md](/overview/UNEXPLORED_DOCUMENT_MINING.md) | Camera-in-clock confirmed, T-160 VHS never scanned, Boies/Pottinger extortion, 48 diamonds |

### Session 10 Reports -- Art and Digital Forensics (67-77)

| # | Report | Description |
|---|--------|-------------|
| 67 | [ART_INVESTIGATION_COMPLETE.md](/art/ART_INVESTIGATION_COMPLETE.md) | Unified art investigation (80KB, 1617 lines): $30.5M auction proceeds, Black $2.7B collection, 54 named art world figures, 72 sections |
| 68 | [ART_INVESTIGATION_REDACTIONS.md](/art/ART_INVESTIGATION_REDACTIONS.md) | Sub-report: 165 queries across 3.4M redaction records for art-related hidden text |
| 69 | [ART_INVESTIGATION_OCR_IMAGES.md](/art/ART_INVESTIGATION_OCR_IMAGES.md) | Sub-report: 53 queries across OCR + image databases for art documentation |
| 70 | [ART_INVESTIGATION_WEB_RESEARCH.md](/art/ART_INVESTIGATION_WEB_RESEARCH.md) | Sub-report: 40+ web sources, 16 sections on art market connections |
| 71 | [TRANSACTION_CHAIN_AUCTION_TO_DESTINATION.md](/financial/TRANSACTION_CHAIN_AUCTION_TO_DESTINATION.md) | Prosecutorial narrative: $30.5M Sotheby's/Christie's through Haze Trust to investment funds |
| 72 | [TRANSACTION_CHAIN_BLACK_ART_MACHINE.md](/financial/TRANSACTION_CHAIN_BLACK_ART_MACHINE.md) | Prosecutorial narrative: 15 chains tracing $168M Black to Epstein, art/trafficking structural unity |
| 73 | [TRANSACTION_CHAIN_THIRD_PARTY_ART.md](/financial/TRANSACTION_CHAIN_THIRD_PARTY_ART.md) | Prosecutorial narrative: Prytanee, Rothschild, Tudor, Gratitude America, Mitchell, art insurance |
| 74 | [PLIST_FORENSIC_SEARCH.md](/evidence/PLIST_FORENSIC_SEARCH.md) | 460+ Apple Mail PLIST metadata documents, 2 email accounts, 9-year date range |
| 75 | [PLIST_REDACTED_EMAILS_DEEP_DIVE.md](/evidence/PLIST_REDACTED_EMAILS_DEEP_DIVE.md) | 12 bad_overlay redactions: "I'm not a toy Jeffrey," neuroscience dinner, State Dept call for Mitchell |
| 76 | [PLIST_TIMESTAMP_TRANSACTION_CORRELATION.md](/evidence/PLIST_TIMESTAMP_TRANSACTION_CORRELATION.md) | 420 timestamps vs financial dates: Tudor $13.5M strongest, 99-day PLIST gap (later corrected by DS9) |
| 77 | [DEVICE_FORENSICS_COMPLETE.md](/evidence/DEVICE_FORENSICS_COMPLETE.md) | 70+ devices, 2005 computer NEVER searched, DVR failure, "FBI completely fucking us" processing |

### Codex Financial Analysis (78-84)

| # | Report | Description |
|---|--------|-------------|
| 78 | financial transaction database | Custom database: 186 normalized transactions, $755M total, control join + actor touch seed tables |
| 79 | HANDOFF_MONEY_TRAIL_2026-02-06.md | Status report: banker-to-suspicious-flow linkage confirmed, not yet banker-to-crime proof |
| 80 | FORENSIC_ACCOUNTANT_PLAYBOOK.md | 9-field proof chain methodology for direct mishandling evidence attribution |
| 81 | EVIDENCE_BOIL_DOWN_v1.md | Post-KYC breach: 50 transactions/$189M; critical window Nov-Dec 2018: 6 transactions/$8.2M |
| 82 | DIRECT_MISHANDLING_VERIFIABLE_ACTS.md | Named Deutsche Bank staff tied to verifiable transaction handling acts |
| 83 | FORENSIC_NETWORK_ANALYSIS_v1.md | Post-KYC outflow nodes, repeating corridors, same-day bundled signatures |
| 84 | FULL_TRANSACTION_EVIDENCE_REGISTER.csv | 185 normalized DB-SDNY transaction rows with Bates references |

### This Report
| 85 | FINAL_INVESTIGATION_REPORT.md | This document: comprehensive synthesis, prosecution referral grade |

---

# APPENDIX C: DATABASE STATISTICS

## Primary Databases

| Database | File Size | Records | Coverage |
|----------|-----------|---------|----------|
| primary document text database | 660 MB | 1,808,942 redaction records | Datasets 1-9, 11-12 |
| Dataset 10 document text database | 532 MB | 1,629,776 redaction records | Dataset 10 only |
| OCR text extraction database | 68 MB | 38,955 OCR records | All datasets |
| image catalog database | 199 MB | 21,859 images (26,721 analysis records) | All datasets |
| entity relationship database | -- | 524 entities, 2,096 relationships | Cross-dataset |
| financial transaction database | -- | 186 normalized transactions | Financial only |

## Key Tables

### primary document text database
- `redactions` -- 1.8M rows: efta_number, page_number, hidden_text, redaction_type, confidence
- `document_summary` -- 519K rows: document-level metadata
- `reconstructed_pages` -- 39K rows: full page text reconstruction
- `extracted_entities` -- 107K rows: named entity extraction

### Dataset 10 document text database
- Same schema as v2, covering Dataset 10 separately (Deutsche Bank productions, email exports)

### OCR text extraction database
- `ocr_results` -- 38,955 rows: full OCR text extraction from all datasets

### image catalog database
- 21,859 unique images cataloged from FBI evidence photos
- 130 with nude references
- 669 with massage references
- 876 with surveillance/camera references
- Key photo index: "JE 50TH BD," "THAIS, MOSCOW GIRLS," "NUDES," "YOGA GIRLS," "ZORRO," "RUSSIA," "BALI/THAILAND/ASIA" ([EFTA00004477](https://www.justice.gov/epstein/files/DataSet%203/EFTA00004477.pdf))

### financial transaction database
- 186 normalized transactions totaling $755,632,579
- Post-KYC breach: 50 transactions / $189,000,000
- Dominant corridors: Haze Trust to Southern Financial ($39.7M), Southern Trust to Honeycomb ($33M)
- Same-day bundled transfers identified: DB-SDNY-0006153 ($72M), DB-SDNY-0008063 ($24.5M)

## Dataset Coverage

| Dataset | Documents | Content |
|---------|-----------|---------|
| Dataset 1-9 | ~200,000 | Court filings, FBI reports, prosecution memos, financial exhibits |
| Dataset 10 | ~250,000 | Deutsche Bank productions, email exports, financial records |
| Dataset 11 | ~50,000 | Additional email exports, calendar data |
| Dataset 12 | ~19,438 | Supplemental productions |

## Key Search Statistics

Approximately 2,500+ individual database queries were executed across the investigation. Representative hit rates for significant search terms:

### Named Individual Search Results (Across All Databases)

| Search Term | primary text database Hits | DS10 Hits | OCR Hits | Image Hits | Total Documents |
|-------------|-------------------|-----------|----------|------------|-----------------|
| "Leon Black" | 200+ | 150+ | 30+ | 10+ | 100+ unique EFTA |
| "Ghislaine" / "Maxwell" | 500+ | 300+ | 50+ | 20+ | 200+ unique EFTA |
| "Marcinkova" | **0** | **1** | 0 | 0 | 1 unique EFTA |
| "Prince Andrew" | 50+ | 20+ | 10+ | 5+ | 30+ unique EFTA |
| "Dershowitz" | 100+ | 50+ | 15+ | 0 | 40+ unique EFTA |
| "Richardson" | 80+ | 40+ | 10+ | 0 | 20+ unique EFTA |
| "Summers" | 60+ | 30+ | 8+ | 0 | 30+ unique EFTA |
| "Wexner" | 100+ | 50+ | 15+ | 5+ | 30+ unique EFTA |
| "Ruemmler" | 0 | 29 | 0 | 0 | 29 unique EFTA |
| "Pritzker" | 15+ | 10+ | 3+ | 0 | 15+ unique EFTA |

Note: The Marcinkova near-zero-hit phenomenon -- a single result across 3.4 million redaction records for a woman with 124 documented flights -- is notable. The low hit count in redaction databases may reflect that her name was consistently redacted (indicating effective rather than failed redactions), that she was primarily referenced by first name or alias, or that she appears more frequently in non-redacted text layers not captured by the redaction analysis tool. The full_text_corpus.db does return additional results.

### Financial Entity Search Results

| Entity | DB-SDNY Transactions | Deutsche Bank Docs | Total Value |
|--------|---------------------|-------------------|-------------|
| Southern Trust Company Inc. | 45+ | 200+ | $200M+ |
| Haze Trust | 25+ | 100+ | $49.4M |
| Butterfly Trust | 15+ | 50+ | $5M+ |
| Plan D LLC | 10+ | 30+ | $45.5M |
| Southern Financial LLC | 30+ | 150+ | $100M+ |
| The 2017 Caterpillar Trust | 8+ | 20+ | $15M+ |
| Honeycomb Partners | 12+ | 30+ | $64M |
| Valar Fund | 16+ | 40+ | $28.8M |

### Negative Search Results of Forensic Significance

The following searches returned zero results across ALL six databases -- absences that are themselves significant findings:

| Term | Expected Presence | Significance of Absence |
|------|-------------------|------------------------|
| ~~Carbyne (Barak's company)~~ | ~~Israeli tech, Barak connection~~ | **CORRECTION (Revisit #52):** 374 Carbyne/Reporty documents found in DS9, including direct Epstein investment records. This entry was incorrect. |
| Mega Group | Wexner co-founded | No reference to major Wexner organization |
| Unit 8200 / Shin Bet / Aman / LAKAM | Israeli intelligence | Zero intelligence agency names in 3.4M records |
| MC2 + Tel Aviv | Foreign office of MC2 | Zero records from office recruiting ages 13-20 |
| Deripaska | Mandelson "Oleg" reference | Likely suppression of Russian oligarch name |
| Soros + Epstein | Public allegations | One LedgerX pitch deck only |
| Bezos + Epstein | Public allegations | One 2004 dinner only (via Brockman) |
| ~~Musk + Epstein~~ | ~~Public allegations~~ | **CORRECTION (Revisit #54):** 1,038 documents and 15+ direct email exchanges found in DS9/DS10/DS11. This entry was incorrect. |
| Spacey + Epstein | Public allegations | Zero results |

---

# APPENDIX D: INVESTIGATION METHODOLOGY

## I. Corpus Processing Approach

The 218GB corpus was processed through a multi-phase approach:

**Phase 1: Database Construction (Sessions 1-2)**
Six custom databases were built to enable systematic querying across the corpus:

| Database | Construction Method | Primary Use |
|----------|-------------------|-------------|
| primary document text database | PDF parsing + overlay detection across DS1-9, DS11-12 | Hidden text recovery, entity extraction |
| Dataset 10 document text database | Separate processing of DS10 (largest dataset) | Deutsche Bank email/financial record analysis |
| OCR text extraction database | Optical character recognition of scanned documents | Text extraction from image-based PDFs |
| image catalog database | Image classification and metadata extraction | Photo identification, surveillance evidence |
| entity relationship database | Entity/relationship extraction from all sources | Network mapping, relationship visualization |
| financial transaction database | Manual normalization of financial transactions | Money flow tracing, Bates reference linking |

**Phase 2: Redaction Analysis**
The redaction analysis methodology involved detecting PDF overlay objects that were intended to obscure text but failed to properly flatten or remove the underlying content. Two categories of redaction failures were identified:

1. **bad_overlay (12 documents):** Redaction overlays were placed over text but the underlying text was not removed from the PDF stream. These yielded complete recovery of the hidden text, including full Apple Mail PLIST XML metadata. Confidence scores ranged from 0.77 to 0.99.

2. **text_under_redaction (millions of records):** Standard redactions where text extraction tools could recover fragments of underlying text through various PDF parsing techniques. These required quality filtering -- records with fewer than 10 characters or consisting solely of formatting artifacts were excluded from analysis.

**Phase 3: Entity Extraction and Knowledge Graph**
Named entity recognition was applied across all document collections to extract persons, organizations, locations, and financial entities. These were normalized into a knowledge graph with 524 unique entities and 2,096 relationships. The graph enabled cross-referencing between financial transactions, victim testimony, and documentary evidence.

**Phase 4: Financial Transaction Normalization**
186 financial transactions were manually normalized from Deutsche Bank productions (DB-SDNY Bates-stamped exhibits). Each transaction was coded with:
- Bates reference number (DB-SDNY-XXXXXXX)
- Date, amount, source entity, destination entity
- Wire type and approval chain
- Post-KYC breach flag (yes/no, based on April 16, 2018 cutoff)
- Connection to named individuals

The normalized transactions totaling $755,632,579 were loaded into financial transaction database for systematic analysis.

**Phase 5: PLIST Metadata Forensics**
460+ documents containing Apple Mail PLIST metadata were identified through pattern matching across the corpus. The PLIST XML embedded in exported emails contained:
- Sender and receiver email addresses
- Timestamp (date-sent, date-received, date-last-viewed)
- Remote-id (sequential Gmail message identifier)
- Mail account configuration data

420 timestamps with parseable dates were extracted and cross-referenced against the 186 normalized financial transaction dates to identify communication-transaction correlations.

## II. Search Methodology

Standard search patterns were applied across all six databases:

```
Search Pattern 1: Name/Term Discovery
- Query each database for the target term
- Filter for records with >20 characters of content
- Extract EFTA document numbers
- Retrieve full document content for context

Search Pattern 2: Cross-Database Correlation
- Identify an entity in one database
- Search all other databases for the same entity
- Compare hit counts to identify suppression patterns
- Example: Marcinkova returns 0 hits in primary text database but 1 hit in DS10 text database

Search Pattern 3: Temporal Analysis
- Extract date-stamped records for a target period
- Map events against known timeline
- Identify gaps, clusters, and anomalies
- Example: 99-day PLIST metadata gap identification (later corrected by DS9 -- gap was methodology-specific, not a real blackout)

Search Pattern 4: Financial Chain Tracing
- Start from a known Bates-stamped transaction
- Identify all entities involved
- Search for those entities in non-financial databases
- Map the complete flow from source to destination
```

## III. Evidence Grading Criteria

Evidence grades were assigned based on the following criteria:

| Grade | Criteria |
|-------|----------|
| **STRONGEST IN CORPUS** | 3+ independent victim testimonies, financial documentation, prosecution records, and corroborating physical evidence. No contradictory evidence. |
| **STRONG** | Direct victim testimony or sworn depositions plus corroborating documentary evidence from 2+ independent sources. |
| **MODERATE-STRONG** | Substantial documentary evidence (15+ documents) with some victim testimony or significant financial connections ($1M+). |
| **MODERATE** | Multiple documents (5-15) showing ongoing relationship, post-conviction contact, or financial ties. |
| **LOW-MODERATE** | Limited documentary evidence (1-5 documents), single-source allegations, or presence without abuse allegations. |
| **WEAK** | Single NTOC tip or unsubstantiated allegation with minimal or no corroboration. |

Evidence grades were elevated when:
- Multiple independent victims described the same individual with consistent details
- Financial documentation corroborated the relationship timeline
- Documentary evidence contradicted public denials
- Prosecution records showed internal discussion of the evidence

Evidence grades were lowered when:
- Allegations came from a single source identified as potentially unreliable
- The source was identified as having a grudge or financial motive
- Documentary evidence was limited to social contact without abuse allegations
- FBI or prosecution teams formally assessed a tip as "not credible"

## IV. Limitations

This investigation was conducted using only the released documents and publicly available information. Key limitations include:

1. **Sealed materials excluded.** An unknown volume of sealed court filings, grand jury transcripts, and classified intelligence documents were not included in the DOJ release.
2. **Redaction success rate unknown.** The 12 bad_overlay failures were discovered; the success rate of redactions that DID work is unknowable.
3. **Dataset completeness unverifiable.** Whether the 12 datasets represent the complete evidentiary record or a curated subset cannot be determined from the materials themselves.
4. **No witness interviews conducted.** All evidence derives from documents; no living witnesses were interviewed as part of this investigation.
5. **Foreign-language documents partially analyzed.** French, Hebrew, Russian, and other non-English documents in the corpus received less thorough analysis than English-language materials.
6. **OCR quality varies.** Scanned documents processed through OCR have variable accuracy; some text may be garbled or missing.
7. **Temporal bias.** Deutsche Bank records (DS10) cover 2013-2019; JPMorgan records from the pre-2013 period are less thoroughly represented.
8. **Image analysis is descriptive, not forensic.** Image classification identified content categories (nude, surveillance, etc.) but did not perform facial recognition or age estimation.

---

# APPENDIX E: CHRONOLOGICAL TIMELINE OF KEY EVENTS

This timeline consolidates the most significant dated events from the investigation into a single chronological reference.

| Date | Event | EFTA |
|------|-------|------|
| Late 1980s | Epstein-Wexner relationship begins; Epstein receives power of attorney | [EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf) |
| 1989 | Wexner purchases 9 E 71st St through Nine East 71st Street Corp | [EFTA00037757](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037757.pdf) |
| 1993 | Zorro Trust purchases NM ranch land | [EFTA00030804](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030804.pdf) |
| 1994 | Maxwell signs notarized document as "disinterested party" for Zorro appraisal | [EFTA00030804](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030804.pdf) |
| Spring 1996 | 14-year-old victim begins traveling to NYC; Maxwell buys "little girls underwear" | [EFTA00008631](https://www.justice.gov/epstein/files/DataSet%206/EFTA00008631.pdf) |
| 1996 | Maria Farmer files first-ever criminal complaint re Epstein with FBI/NYPD | [EFTA00019101](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019101.pdf) |
| Nov 6, 1998 | Financial Trust Company Inc. incorporated in USVI | [EFTA00015176](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015176.pdf) |
| Oct 19, 1999 | $18.3M wire disbursement -- "transfer to Maxwell" | [EFTA00015176](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015176.pdf) |
| Oct 2003 | Palm Beach police document Epstein using spy camera hidden in clock to catch burglar | [EFTA00029761](https://www.justice.gov/epstein/files/DataSet%208/EFTA00029761.pdf) |
| 2004 | 15-year-old sexually molested at Zorro Ranch | [EFTA00019994](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019994.pdf) |
| 2004 | "Indian Summer" dinner: Brin, Page, Bezos at Epstein's via Brockman | [EFTA00018466](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018466.pdf) |
| 2005 | Palm Beach County SO seizes computer (16 EnCase DVDs -- NEVER searched) | [EFTA00015823](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015823.pdf) |
| Oct 2005 | Jean-Luc Brunel founds MC2 Model Management | [EFTA01728258](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01728258.pdf) |
| 2005-2007 | FBI Miami identifies 28 victims, expanding to "well over 30" | Multiple |
| Sept 2007 | NPA signed -- co-conspirator immunity expanded by Dershowitz | [EFTA00009016](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009016.pdf) |
| Apr 2008 | Epstein tours Israeli military bases while under FL charges | [EFTA00013730](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013730.pdf) |
| Jun 2008 | Epstein pleads guilty in FL state court, receives 18-month sentence | [EFTA00009016](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009016.pdf) |
| 2008 | Wexner settles privately -- $46M "charitable donation" to YLK Foundation | [EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf) |
| May 2009 | Epstein sends iPhone email during incarceration ("Sent from my iPhone") | [EFTA01781767](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01781767.pdf) |
| Nov 2009 | Mandelson forwards Moscow penthouse to Epstein: "Oleg" | [EFTA02434424](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02434424.pdf) |
| Nov 2009 | Epstein brokers Junkermann-Black introduction | [EFTA02435071](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02435071.pdf) |
| Dec 2009 | Staley + Mandelson + Epstein drinks | [EFTA02434434](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02434434.pdf) |
| Jun 2009 | Russian MC2 model: "told me 3 weeks but its been more than a month" | [EFTA02439395](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02439395.pdf) |
| Jul 2010 | Eva Dubin typhoid vaccination for Africa travel | [EFTA01786466](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01786466.pdf) |
| Jan 2011 | Congo: "will report to Ollivier and Peter Mandelson" | [EFTA02323048](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02323048.pdf) |
| Dec 2011 | Epstein signs deed: 9 E 71st St from Nine East Corp to Maple Inc (both sides) | [EFTA00037757](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037757.pdf) |
| Mar 2012 | Private Musee d'Orsay access for Epstein and Woody Allen | [EFTA02124200](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02124200.pdf) |
| Jun 2012 | Kellen: "JE said cancel hotel rooms in Menlo Park" | [EFTA02310713](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02310713.pdf) |
| 2012 | Munch's "The Scream" purchased by Black through Narrows II LLC ($120M) | [EFTA02730996](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730996.pdf) |
| 2013 | JPMorgan terminates Epstein banking relationship | Multiple |
| 2013 | Deutsche Bank relationship begins under RM CODE 82289 | [EFTA01359500](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01359500.pdf) |
| Oct 2013 | First Black payment: $8.5M from Leon and Debra Black | [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) |
| May 2013 | Mandelson: "tastey models and dancing" + St. Petersburg | [EFTA02571022](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02571022.pdf) |
| May 2013 | Dinner: Allen/Soon-Yi 7:30, Ito/Boyden 8:00, Pritzker 9:00 | [EFTA02377042](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02377042.pdf) |
| Nov 2013 | Josephson: $200K payment | [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) |
| Dec 2013 | Epstein controls Zuckerman's complete finances | [EFTA02518881](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518881.pdf) |
| Mar 2014 | Epstein/Hoffman introduced to Austin Hill (crypto pioneer) | [EFTA02518909](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02518909.pdf) |
| Aug 2014 | Tudor Futures Fund: $13.5M (strongest PLIST correlation) | [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) |
| Sep 22, 2014 | Calendar: Barak, Black, Summers, Thiel ALL visiting Epstein same day | [EFTA00362483](https://www.justice.gov/epstein/files/DataSet%209/EFTA00362483.pdf) |
| Sep 2014 | Kerrey arranges Thiel-Burns-Epstein lunch | [EFTA02589110](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02589110.pdf) |
| Jan 2015 | Ruemmler: "exaggerating about Benjamin. Wrong assumption" | [EFTA02513986](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02513986.pdf) |
| May 2015 | Brockman-Epstein direct email (Sam Harris, Jennifer Doudna) | [EFTA02501737](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02501737.pdf) |
| Oct 2015 | Epstein to Ruemmler: "Clinton Obama unnecessary implication" | [EFTA02484285](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02484285.pdf) |
| Oct 2015 | Summers-Epstein: "central bank mongol" intelligence exchange | [EFTA02484293](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02484293.pdf) |
| Oct-Dec 2015 | Elysium and Southern Financial relationships activated at DB | [EFTA01477330](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477330.pdf) |
| Nov 2015 | $23M wire to Kellerhals approved by Stewart Oldfield | [EFTA01431221](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01431221.pdf) |
| Dec 2015 | Rothschild: $25M in two wires (within same week as Black $10M) | [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) |
| Dec 2015 | Marrakesh flight: "you and Karyna only" | [EFTA02477179](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02477179.pdf) |
| Jan 2016 | Great St. James purchased for $5M | [EFTA02265056](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02265056.pdf) |
| Jan 2016 | Eva Dubin: "Happy Birthday turtle!" -- 8 years post-conviction | [EFTA02474963](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02474963.pdf) |
| Jan 2016 | Russian woman visa canceled; Epstein: "naughty selfie" | [EFTA02474955](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02474955.pdf) |
| Jan 2016 | Minsky dies -- before SDNY investigation begins | Public record |
| May 2016 | Sworn deposition names Richardson | [EFTA00022133](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022133.pdf) |
| Dec 2016 | Black to Epstein: "liquidate the J BLACK trust... sensitive accounts" | [EFTA02664953](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664953.pdf) |
| Jan 2017 | Wolff to Epstein: "six-hour dinner with Ailes and Bannon" | [EFTA02664993](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02664993.pdf) |
| Mar 2017 | Seth Lloyd: "Indeed it was awesome" -- 9 years post-conviction | [EFTA02366597](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02366597.pdf) |
| Mar-Apr 2017 | BV70 to Plan D: $30.5M ("in connection with an art transaction") | [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) |
| Jun-Oct 2017 | $30.5M art auction proceeds (Sotheby's $22.8M + Christie's $7.7M) | [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) |
| Jul 2017 | Pritzker helps find architect for "new guest island" | [EFTA02644290](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02644290.pdf) |
| Oct 2017 | Active model scouting: "Skyped today, will pass to candidates list" | [EFTA02575358](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02575358.pdf) |
| Oct 29, 2017 | Epstein to Ruemmler: "why would they file a sealed indictment?" | [EFTA02575359](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02575359.pdf) |
| Nov 2017 | Epstein to Mitchell: "tomorow you must make money. clear that cascade" | [EFTA02570991](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570991.pdf) |
| Nov 2017 | Epstein installs Krauss as Chomsky trust trustee | [EFTA02570988](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02570988.pdf) |
| Nov 2018 | George Church/Harvard meeting with Epstein | [EFTA02264607](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02264607.pdf) |
| Nov 14, 2018 | 99-day PLIST metadata gap begins (later determined to be a DS11 extraction artifact; DS9 confirms continuous email activity) | PLIST analysis |
| Nov 28, 2018 | Miami Herald "Perversion of Justice" series begins | Public record |
| Nov 30, 2018 | $100K Aviloop wire (Marcinkova) -- 2 days after Herald series | [EFTA00020685](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020685.pdf) |
| Dec 3, 2018 | $250K wire to another co-conspirator | [EFTA00028785](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028785.pdf) |
| Jan 2019 | Island guest list: Bannon, Junkermann, Sultan bin Sulayem, Teodorani | [EFTA02273951](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02273951.pdf) |
| Feb 2019 | Epstein brokers Barak-Bannon meeting | [EFTA02633609](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02633609.pdf) |
| Feb 19-22, 2019 | **$31.5M DISSOLUTION EVENT** | [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) |
| Feb 21, 2019 | 99-day PLIST metadata gap ends | PLIST analysis |
| Mar 2019 | Pritzker: "Maybe breakfast on Tuesday?" (4 months pre-arrest) | [EFTA02633147](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02633147.pdf) |
| Mar 2019 | Epstein staff cleaning "Ehud's apt" at 301 E 66th | [EFTA02278459](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02278459.pdf) |
| Apr 17, 2019 | Last Valar Fund payment: $1.5M -- 80 days before arrest | [EFTA00027019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027019.pdf) |
| May 2019 | 3BIS architecture firm Zoom conference -- active island development | [EFTA02265056](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02265056.pdf) |
| **Jul 6, 2019** | **EPSTEIN ARRESTED at Teterboro Airport** | Multiple |
| Jul 16, 2019 | FBI assigned to call real Marius Fortelni -- NO RECORD of outcome | [EFTA00025539](https://www.justice.gov/epstein/files/DataSet%208/EFTA00025539.pdf) |
| Jul 22, 2019 | Austrian Embassy requests information | [EFTA00016173](https://www.justice.gov/epstein/files/DataSet%208/EFTA00016173.pdf) |
| Jul 23, 2019 | Epstein found on cell floor with neck marks; placed on suicide watch | [EFTA00035225](https://www.justice.gov/epstein/files/DataSet%208/EFTA00035225.pdf) |
| Jul 25, 2019 | Wexner attorney proffer: "several hundred million dollars" stolen | [EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf) |
| Jul 29, 2019 | **DVR 2 SUFFERS CATASTROPHIC DISK FAILURES** | [EFTA00039025](https://www.justice.gov/epstein/files/DataSet%209/EFTA00039025.pdf) |
| Jul 29, 2019 | Suicide watch removed (same day as DVR failure) | [EFTA00035225](https://www.justice.gov/epstein/files/DataSet%208/EFTA00035225.pdf) |
| Jul 30, 2019 | Epstein transferred back to SHU | [EFTA01649190](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01649190.pdf) |
| **Aug 8, 2019** | **Last will executed; 1953 Trust created** | [EFTA00019322](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019322.pdf) |
| Aug 8, 2019 | DVR 2 additional drive failures detected | [EFTA00039025](https://www.justice.gov/epstein/files/DataSet%209/EFTA00039025.pdf) |
| Aug 9, 2019 | Cellmate Tartaglione transferred out | [EFTA01649190](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01649190.pdf) |
| Aug 9, 2019 | Replacement hard drives obtained, NEVER installed | [EFTA01649190](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01649190.pdf) |
| **Aug 10, 2019** | **EPSTEIN FOUND DEAD ~6:30 AM** | Multiple |
| Aug 10, 2019 | Hard drives seized from DVR 2 at 4:30 PM | [EFTA00023970](https://www.justice.gov/epstein/files/DataSet%208/EFTA00023970.pdf) |
| Aug 12, 2019 | NiceVision arrives for replacement system | [EFTA01649190](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01649190.pdf) |
| Aug 16, 2019 | DVR shipped to FBI Quantico -- "did not start successfully" | [EFTA00039025](https://www.justice.gov/epstein/files/DataSet%209/EFTA00039025.pdf) |
| Aug 30, 2019 | CBP officer walks in: "Everyone knew I was friends with Epstein" | [EFTA00031495](https://www.justice.gov/epstein/files/DataSet%208/EFTA00031495.pdf) |
| Sept 2019 | Ito resigns from MIT Media Lab | Public record |
| Oct-Nov 2020 | SDNY proffer sessions with CBP officer | [EFTA00020852](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020852.pdf) |
| Jul 2, 2020 | Maxwell arrested at 301 Summer St, Manchester-by-the-Sea, NH | [EFTA00011172](https://www.justice.gov/epstein/files/DataSet%208/EFTA00011172.pdf) |
| Dec 29, 2021 | Maxwell convicted on 5 of 6 counts | Public record |
| Jun 28, 2022 | Maxwell sentenced to 20 years | Public record |
| Feb 19, 2022 | Jean-Luc Brunel found dead in La Sante prison, Paris | Public record |
| 2023 | Additional CSAM discovered during estate settlement | [EFTA00039019](https://www.justice.gov/epstein/files/DataSet%208/EFTA00039019.pdf) |
| Sep 2023 | Bill Richardson dies -- never subpoenaed, never cleared | Public record |
| Jan 2024 | JPMorgan victim settlement: ~$1M allocations | [EFTA00037088](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037088.pdf) |
| Oct 2024 | "US v. Black" still in SDNY file sharing system | Internal |
| Oct 2024 | Brad Edwards retained BY Leon Black | [EFTA02731577](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731577.pdf) |
| Feb 2026 | Jack Lang summoned in France, resigns from Arab World Institute | Public record |
| Feb 2026 | DOJ releases 218GB Epstein file corpus | Public record |

---

# CONCLUDING NOTE

## I. Scope of This Investigation

This report synthesizes a forensic investigation of the largest single document release in the history of the Jeffrey Epstein case. The Department of Justice released approximately 218 gigabytes of material comprising 519,438 individual PDF documents organized across 12 datasets. Over the course of the investigation:

- Six custom databases were constructed containing over 3.4 million indexed records
- 21,859 images were cataloged and analyzed
- 186 financial transactions were normalized and traced, totaling $755,632,579
- 400+ individual EFTA documents were cited
- 85 individual investigative reports were produced
- 524 entities and 2,096 relationships were mapped in a knowledge graph
- 460+ documents with Apple Mail PLIST metadata were analyzed
- 420 email timestamps were cross-referenced against financial transaction dates
- 12 failed redaction overlays were identified and content recovered
- 1.8 million redaction records were searched across multiple databases

The investigation was conducted using only the released documents and publicly available information. No classified materials, sealed court records, or non-public law enforcement databases were accessed.

**DATA QUALITY NOTE:** The document text database contains 1.8 million text records extracted from PDF text layers near redaction zones. A data quality audit (DATA_QUALITY_AUDIT.md) confirmed that ~98% of 'bad_overlay' records are OCR noise from degraded scans, not text hidden behind removable redactions. Only 12 documents had genuinely failed redaction overlays exposing PLIST metadata. The text searches against this corpus are valid for identifying which documents mention specific terms, but the results should not be characterized as 'recovered hidden text.'

## II. What the Evidence Establishes

The documentary evidence establishes, with varying degrees of certainty, the following conclusions:

**Established Beyond Reasonable Doubt:**
1. Jeffrey Epstein operated a sex trafficking enterprise spanning multiple countries and decades
2. Ghislaine Maxwell was his primary co-conspirator (convicted December 2021)
3. At minimum 93 individual victims were identified per FBI's own count ([EFTA00161426](https://www.justice.gov/epstein/files/DataSet%209/EFTA00161426.pdf), Revisit #56); the actual number is likely 200+
4. $755 million in documented financial flows passed through 95+ shell entities at a single bank
5. Deutsche Bank continued processing Epstein transactions after documenting its own compliance failures
6. The same bankers (Litchford and Morris) simultaneously managed Epstein and his largest patron (Leon Black)
7. $168 million flowed from Leon Black to Epstein entities through the same infrastructure that funded trafficking
8. Art auction proceeds ($30.5M) flowed through Haze Trust into investment funds and aircraft operations via the same infrastructure used across all Epstein financial activity
9. Victims as young as 11-12 were documented; MC2 publicly recruited "Between 13 and 20 years old"
10. Evidence processing was catastrophically mismanaged, resulting in missed CSAM and unsearched devices

**Established by Preponderance of Evidence:**
1. Leon Black committed violent sexual assault against multiple victims trafficked through Epstein
2. Multiple named individuals received trafficking victims directed by Epstein and/or Maxwell
3. Epstein operated a surveillance/blackmail apparatus using concealed cameras and recording equipment (prosecution memo states "cameras in his clock"; multi-monitor control room photographed; Boies/Pottinger planned to monetize "illicit videos")
4. The 2007 NPA's blanket co-conspirator immunity provision — expanded during defense team negotiations in which Dershowitz participated — retroactively shielded individuals later accused of being co-conspirators (allegations against Dershowitz himself emerged publicly in 2014)
5. A CBP officer facilitated customs bypass at St. Thomas for 7+ years
6. Epstein had connections to foreign intelligence services (documented but uninvestigated). **UPDATE (Revisit #52):** FBI CHS FD-1023 ([EFTA00090314](https://www.justice.gov/epstein/files/DataSet%209/EFTA00090314.pdf)) explicitly claims Epstein "belonged to" U.S. and allied intelligence services. An investigative memo ([EFTA00098755](https://www.justice.gov/epstein/files/DataSet%209/EFTA00098755.pdf)) characterizes him as a "financial bounty hunter" for the U.S. government. DS9 also contains 374 Carbyne/Reporty documents showing direct Epstein investment in an Israeli tech-intelligence company. CHS reports are unverified, but their presence in the FBI case file elevates this finding
7. The February 2019 $31.5M dissolution event was pre-arrest asset repositioning
8. ~~The 99-day email blackout corresponds to evidence destruction or communication channel switching~~ **REMOVED (Revisit #48):** DS9 documents establish that the jeevacation@gmail.com account was continuously active throughout this period. The 99-day gap was an artifact of DS11 PLIST extraction methodology, not a real blackout. Epstein operated with full confidence during this period, hosting Barak on the island, claiming involvement in Treasury Secretary selection, and distributing Apple Watches to Bannon

**Strongly Suggested but Not Conclusively Proven:**
1. The Austrian passport under a false name was used for intelligence-related travel
2. Epstein functioned as an intelligence asset for one or more foreign governments
3. Prosecutorial leniency toward named individuals was influenced by political considerations
4. The DVR failure at MCC was coincidental rather than deliberate
5. The $376 million gap in Southern Trust revenue came from unidentified clients or services
6. Honeycomb Partners ($64M) was a vehicle for an unidentified beneficiary with reason to remain hidden

## III. What the Evidence Does Not Establish

This investigation found NO evidence supporting the following claims that circulate publicly:
- George Soros had any substantive connection to Epstein (one LedgerX pitch deck, one Swedish museum)
- Jeff Bezos had any direct connection to Epstein (only a 2004 dinner via Brockman)
- **CORRECTION (Revisit #54):** Elon Musk had no connection to Epstein -- this claim is incorrect. DS9/DS10/DS11 contain 1,038 documents and 15+ direct email exchanges (2012-2015), including Musk asking about "the wildest party on your island," Epstein offering helicopter transport, holiday socializing in BVI/St. Barths across multiple years, and Epstein brokering Sultan bin Sulayem's business proposal to Musk. The original "zero results" finding was an artifact of incomplete database searches that did not cover DS9/DS11
- Kevin Spacey had any connection (zero results)
- Andrew Cuomo was implicated -- "Cuomo" on the Prominent Names page refers to a VICTIM surname, not the Governor ([EFTA02696360](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02696360.pdf))
- Howard Lutnick was involved in sexual abuse -- the single NTOC tip alleged a $10 house purchase, not sexual conduct, and the source was identified as a disgruntled employee. **UPDATE (Revisit #21):** While no sexual abuse allegations exist, the characterization of the Lutnick connection as a "single NTOC tip" is materially incomplete. DS9 reveals 20+ documents showing an active 2011-2013 social relationship: calendar appointments, the Lutnick family visiting Little St. James Island by boat (December 2012), contact exchanges, and placement on the same call list as Leon Black and Jes Staley. The evidence does not establish sexual misconduct but documents a deeper relationship than "single NTOC tip" implies
- The "Pizzagate" conspiracy theory has any evidentiary basis in these files -- while the FBI collected 4chan materials and "Kid Q" PNG files as evidence of online threats ([EFTA00027732](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027732.pdf)), these were cataloged as threats against victims and investigators, not as corroboration of conspiracy theories
- Epstein's death was a homicide -- while multiple anomalies are documented (DVR failure, guard sleeping, cellmate removed, will timing, replacement drives not installed), the autopsy finding remains suicide by hanging, and the documentary evidence does not establish a murder conspiracy, despite Michael Baden's public statement that the injuries were "more consistent with homicidal strangulation"
- Any single foreign intelligence service "ran" Epstein -- the evidence shows connections to multiple countries (Israel, Saudi Arabia, Russia) without establishing a controlling relationship with any one service

## III-A. Institutional Complicity

Beyond named individuals, the documentary evidence establishes institutional-level failures that enabled the trafficking enterprise:

**Deutsche Bank AG:**
Continued processing $189 million in Epstein transactions after its own compliance department documented that "kyc is not happening" ([EFTA01362456](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362456.pdf)). The same bankers -- Jj Litchford and Paul Morris -- simultaneously managed Epstein entities, Leon Black's personal accounts, Christopher Boies's accounts, and Todd Wanek's accounts (Ashley Furniture CEO) under RM CODE 82289. Deutsche Bank paid $150 million to the New York Department of Financial Services in penalties. No individual banker was criminally charged.

**JPMorgan Chase & Co.:**
Maintained Epstein's banking relationship from 1998 through 2013 -- through his 2008 conviction and 18-month sentence. Jes Staley, then head of private banking and later Barclays CEO, maintained a personal relationship with Epstein that included the documented rape allegation ([EFTA00029358](https://www.justice.gov/epstein/files/DataSet%208/EFTA00029358.pdf)). JPMorgan paid $290 million to settle victim lawsuits and $75 million in additional regulatory penalties. No individual banker was criminally charged.

**Federal Bureau of Investigation:**
Received Maria Farmer's complaint in 1996 but took no meaningful action for nine years. Identified 28+ victims in the 2005-2007 investigation but accepted the NPA framework. Catastrophically mismanaged 70+ seized devices over 17 months, missing CSAM that was later rediscovered in 2023. Marked four surveillance VHS tapes "ITEM WAS NOT SCANNED." Never obtained a warrant to search the 2005 computer. The FBI CID summary's claim of "no cameras" directly contradicted the Maxwell prosecution memo's "cameras in his clock" statement and the 2003 Palm Beach police documentation.

**Metropolitan Correctional Center / Bureau of Prisons:**
DVR 2 failure 12 days before death was never remedied despite replacement drives being obtained. Two guards assigned to Epstein's tier were sleeping and falsifying records. Epstein was removed from suicide watch after six days. Cellmate was transferred out the night before death. Deferred prosecution agreements for the guards were issued under AG Barr's DOJ; charges were subsequently dismissed. No final investigation report was ever published by the DOJ Office of Inspector General.

**Southern District of New York:**
Despite accumulating evidence against multiple named individuals -- including 4+ victims against Leon Black, sworn testimony naming Richardson and Mitchell, the Wigdor trafficking allegation against Summers, and the Staley rape allegation -- SDNY declined to pursue criminal charges against any person other than Epstein and Maxwell. "US v. Black" appeared in the file sharing system through October 2024 with no action taken. An AUSA stated "I'm not inclined to open based on the other victim" ([EFTA02731578](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731578.pdf)) even after multiple independent witnesses came forward.

**Southern District of Florida:**
Negotiated the 2007 NPA that provided co-conspirator immunity, explicitly waived immigration proceedings against Marcinkova and Ross ([EFTA00176610](https://www.justice.gov/epstein/files/DataSet%209/EFTA00176610.pdf)), and was "deliberately concealed" from victims (Judge Marra finding). When ordered by DOJ to recuse itself from subsequent Epstein criminal matters, SDFL complied -- but the recusal was partial (a "split recusal") that preserved AG Barr's oversight authority.

## IV. The Architecture of Impunity

The Epstein case reveals an architecture of impunity that operated across multiple institutional domains:

**Legal Architecture:**
- The 2007 NPA provided blanket co-conspirator immunity drafted by defense counsel with personal conflicts
- CVRA violations (concealment from victims) were found by federal judges but produced no remedies
- Split recusals allowed political oversight while maintaining appearances of neutrality
- Deferred prosecution agreements for guards produced no accountability

**Financial Architecture:**
- 95+ shell entities obscured beneficial ownership
- RM CODE 82289 consolidated all entities under a single relationship management code
- The same officers who knew of Epstein's crimes continued processing his transactions
- Post-KYC breach processing of $189 million demonstrated institutional capture
- Art transactions, cryptocurrency investments, and trust structures added layers of opacity

**Intelligence Architecture:**
- A FOIA exemption memo confirmed classified information about a "confidential relationship with a foreign government"
- The Austrian passport investigation was abandoned 25 days before death
- Acosta explicitly denied the "intelligence asset" claim under oath ("the answer is no, and no") and separately stated he could not comment on classified information in a public deposition -- a standard government employee position ([EFTA00009116](https://www.justice.gov/epstein/files/DataSet%207/EFTA00009116.pdf), pages 404-405)
- IDF-branded clothing and an unidentified military dress uniform on Little Saint James were photographed but never investigated
- Zero results for any Israeli intelligence agency name across 3.4 million records

**Social Architecture:**
- The victim journals document a social environment where powerful men were normalized as participants
- Art, science, philanthropy, and political access served as social legitimization
- Post-conviction engagement by MIT, Harvard, Gates Foundation, and others provided institutional cover
- Celebrity photographs in abuse settings functioned as intimidation tools

## V. Recommendations for Further Investigation

Based on the evidence documented in this report, the following investigative actions remain available:

1. **Search the 2005 computer.** Obtain a warrant for the 16 EnCase DVDs containing the peak-abuse-period forensic image. The estate's refusal to waive privilege should be challenged given the death of the privilege holder.

2. **Identify Honeycomb Partners.** Issue subpoenas to determine the controlling persons behind the $64 million Epstein investment. Financial institution records and SEC filings should identify the beneficiary.

3. **Scan the VHS tapes.** Review the Maxell T-160 time-lapse surveillance recordings seized from Epstein properties. These may contain evidence relevant to both the trafficking operation and the blackmail apparatus.

4. **Obtain Bannon-Epstein texts.** Seek a warrant for the content of Bannon-Epstein communications on the iPhone 7 already in FBI custody. The same SDNY team that declined to pursue these materials in 2021 should not be the decision-maker.

5. **Resolve the Austrian passport.** Contact the real Marius Fortelni (if living) and the Austrian government to determine the passport's purpose. The "numerous ingress and egress stamps" suggest it documents travels that may be relevant to intelligence inquiries.

6. **Investigate Leon Black.** The evidence against Black -- 4+ independent victims, FBI 302s, direct text messages, video allegations, journal entries, $62.5M settlement, and $168M in payments -- exceeds the evidentiary threshold for criminal investigation by any standard.

7. **Investigate the Filming Allegation.** The victim journal allegation that Ted Leonsis filmed abuse, if substantiated, would constitute production of CSAM -- a federal crime with no statute of limitations.

8. **Identify the CBP Officer.** The officer's name remains redacted despite self-incrimination and FBI proffer sessions. Public identification and potential prosecution for customs bypass facilitating trafficking should be pursued.

9. **Audit Southern Trust Revenue.** The $376 million gap between identified revenue sources and reported income warrants IRS and FinCEN investigation.

10. **Complete Device Processing.** Re-examine all 70+ seized devices, the 181+ CDs/DVDs, and the 12+ TB of raw data using current forensic tools. The 2023 discovery of additional CSAM proves the initial processing was incomplete.

## VI. Final Statement

The documentary evidence establishes that Jeffrey Epstein operated a sex trafficking enterprise of unprecedented scale, enabled by a financial machine that processed over $755 million through 95+ shell entities at a single bank, funded by billionaire clients whose money was inseparable from the trafficking infrastructure, protected by a network of lawyers who negotiated immunity for themselves and their client, shielded by intelligence connections that remain classified, and investigated by a justice system that at every stage chose to narrow rather than expand its inquiries.

The evidence gaps are themselves part of the story. A computer from the peak abuse period was never searched. Surveillance tapes were never scanned. Text messages were never read. A $64 million investment recipient was never identified. An Austrian passport investigation was abandoned after 25 days. A 99-day gap in one email metadata source during the most critical financial period was initially identified as a blackout but later determined to be a methodological artifact (DS9 confirmed continuous email activity). CSAM found on devices in 2019 was missed and had to be re-discovered in 2023. Guards were charged and then uncharged. Camera systems failed and were never repaired. Replacement hard drives were purchased and never installed.

The men named in this report -- with evidence grades ranging from WEAK to STRONGEST IN CORPUS -- include:

- **Leon Black** (Apollo Global Management): $168 million in payments, 4+ victims with consistent allegations of violent sexual assault, victim direct text message, video allegation, $62.5M USVI settlement, never charged
- **Ehud Barak** (Former Israeli Prime Minister): apartment in the same building as trafficking victims, cleaned by Epstein's staff, most likely match for "foreign president" in victim compilations, IDF-branded clothing and unidentified military uniform on Epstein's island
- **William Barr** (Former Attorney General): NTOC tip alleged "present during abuses," father hired Epstein at Dalton, split recusal maintained oversight, no final death investigation report
- **George Mitchell** (Former Senate Majority Leader): named in victim journal, sworn deposition, 9-page victim compilation, never subpoenaed
- **Bill Richardson** (Former Governor): named in sworn deposition, "clearance" claim explicitly contradicted by prosecutor, NM AG deferred to federal prosecutors who declined to act
- **Larry Summers** (Former Harvard President): Wigdor Law trafficking allegation, victim journal naming, 30+ documents, foreign intelligence exchange with Epstein
- **Peter Thiel** (Technology investor): $28.8M investment relationship continuing 80 days before arrest, CIA Director lunch, no sexual allegations
- **Kathryn Ruemmler** (Former Obama White House Counsel): 15+ direct emails, sealed indictment consultation, "Clinton Obama unnecessary implication" warning
- **Jes Staley** (Former Barclays CEO): rape allegation during massage, victim journal violence allegation, FCA investigation, no charges anywhere
- **Alan Dershowitz** (Attorney): negotiated his own immunity, multiple victims naming him, conflict of interest never investigated
- **Glenn and Eva Dubin**: "lent out" testimony, Eva's medical credential use, 34+ flights, no investigation
- **Ted Leonsis** (AOL/Washington sports): victim journal allegation of FILMING abuse, four AOL executives in cluster
- **Tom Pritzker** (Hyatt Hotels): 10-year documented relationship through March 2019, island development assistance

With the exception of Ghislaine Maxwell (convicted, sentenced to 20 years) and Epstein himself (dead before trial), none have been criminally charged for conduct related to this enterprise. Jean-Luc Brunel died in a French prison before his trial was completed -- meaning both individuals who were seriously prosecuted died before trial conclusions could be reached.

The evidence exists. The victims exist. The money trail is documented to the penny. The prosecutions have not followed.

---

*This report was compiled from the complete 218GB DOJ Epstein file release. All EFTA citations refer to specific documents in the federal evidentiary record. All financial figures are sourced from Deutsche Bank productions to SDNY (DB-SDNY Bates-stamped exhibits). All victim statements are sourced from FBI 302s, sworn depositions, victim impact statements, and attorney proffer letters documented in the EFTA system. Evidence grades are based on the number and independence of sources, corroboration across databases, and consistency with known facts.*

*Total EFTA documents cited: 400+*
*Total financial transactions traced: 186+*
*Total dollar flows documented: $755,632,579*
*Databases queried: 6 (containing 3.4M+ indexed records)*
*Investigation sessions: 10*
*Individual reports produced: 85*

---

**END OF FINAL INVESTIGATION REPORT**
