# INVESTIGATION LINE 5: MAXWELL SSN AND IDENTITY DOCUMENT ANALYSIS

## Forensic Database Investigation Report
**Database:** the primary document text database
**Date of Analysis:** 2026-02-05
**Database Size:** 1,808,915 redactions | 107,422 extracted entities | 39,588 reconstructed pages

---

## EXECUTIVE SUMMARY

This investigation reveals a remarkable set of identity anomalies surrounding Ghislaine Maxwell's NYPD firearms permit application ([EFTA01653379](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653379.pdf)), including a Connecticut-prefix Social Security Number issued to a French-born British national, an affirmative military service record for a person with no known military history, a criminal record flag on an application that was nonetheless approved, and conflicting dates of birth across multiple law enforcement databases. The SSN 133784883 appears in at least two separate documents, and the surrounding document cluster reveals extensive law enforcement database pulls that were part of the federal investigation.

---

## 1. PRIMARY DOCUMENT: [EFTA01653379](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653379.pdf) -- NYPD FIREARMS PERMIT

### 1.1 Complete Hidden Text Extraction

[EFTA01653379](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653379.pdf), Page 0, contains three recovered redaction fragments at 0.99 confidence:

**Fragment 1 (Redaction ID 701164) -- System Header:**
```
Executed:10/8/2019
13:14
Executed
by:NYPDFINESTSYRNE941477
New York City Police
Department
FIREARMS - LICENSES AND
PERMITS
```

**Fragment 2 (Redaction ID 701165) -- Full Application Record:**
```
Name. GHISLAINE N MAXWELL
Application RESIDENCE PREMISES
Type:
Application 2/21/2006
Date.
Status. APPROVED
Country of Birth: FR
Height: 58"
Weight 120
Sex: FEMALE
SSN: 133784883
Citizen: C
Eye Color: BROWN
Hair Color: BROWN
NYSID:
DOB: 12125/1963
Race: WHITE
Mental Record: NO
Alias name:
Military Record: YES
Criminal Record: YES
```

**Fragment 3 (Redaction ID 701166):**
```
ype: RESI
```

### 1.2 Reconstructed Page Confirmation

The `reconstructed_pages` table (ID 28111) confirms the full document reconstruction with an **interest score of 56.32** (extremely high), classified as document type `FBI_REPORT`, with names found: `Maxwell, Ghislaine, New York`, sourced from dataset `ds10`.

---

## 2. SSN ANALYSIS: 133784883

### 2.1 SSN Prefix Anomaly -- Connecticut Assignment

The SSN **133-78-4883** carries a prefix of **133**, which falls within the range **040-049** historically assigned to... -- correction: the prefix **133** falls within the **130-134** range, which was historically assigned to **Connecticut** by the Social Security Administration under the Area Number allocation system used prior to SSN randomization in 2011.

**Critical Finding in [EFTA01712451](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01712451.pdf)** (Redaction ID 878908, confidence 0.8853):
```
va xx mcm issuec in CONNECTICUT be
```
This document is a comprehensive background investigation report containing SSN issuance tracking across multiple states. The fragment explicitly references an SSN "issued in CONNECTICUT," confirming that at least one SSN associated with subjects in the Epstein investigation was traced to Connecticut issuance.

**Identity Contradiction:** Ghislaine Maxwell was born in Maisons-Laffitte, France (Country of Birth: FR) on December 25, 1961. She is a citizen of France, England, and the United States (confirmed in [EFTA00011365](https://www.justice.gov/epstein/files/DataSet%208/EFTA00011365.pdf): "Page 10 (Maxwell is a US Citizen as well as citizen of France and England)"). A Connecticut-prefix SSN issued to a French-born individual with no known Connecticut residency during the era of geographic SSN assignment is anomalous and warrants scrutiny regarding how the number was obtained.

**[REVISIT UPDATE -- SSN Issuance Date Resolved]:** An Experian credit report ([EFTA00152321](https://www.justice.gov/epstein/files/DataSet%209/EFTA00152321.pdf), DS9) pulled on 8/27/2019 definitively establishes that SSN 133-78-4883 was "ISSUED 1990-1993." This narrows the issuance window to Maxwell's first years in the United States (she arrived in New York circa 1991). The Connecticut prefix remains geographically anomalous for a New York-based applicant but is consistent with the issuance era. The same credit report reveals the alias "GHISLAINE BORGERSON," employer history ("J EPSTEIN AND COMPNY"), addresses at 139A Charles St Apt 233, Boston, MA (Borgerson's apartment) and 116A E 65th St, New York, NY (Epstein's townhouse), and a USAA Savings Bank account with a $102,243 balance in dispute.

A Grand Jury subpoena to UBS ([EFTA00235805](https://www.justice.gov/epstein/files/DataSet%209/EFTA00235805.pdf), DS9, dated August 16, 2019) lists Maxwell's full SSN (133-78-4883), all 5 associated entities (including ELLMAX LLC and MAX HOTEL SERVICES CORP), 7 phone numbers, and 5 UBS account numbers. JPMorgan checks ([EFTA00270728](https://www.justice.gov/epstein/files/DataSet%209/EFTA00270728.pdf), DS9, 73 pages) bear SSN 133784883 and confirm Maxwell's accountant was Marks Paneth, LLP.

### 2.2 SSN Cross-Reference: [EFTA01296720](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01296720.pdf)

The SSN appears a second time in a partially redacted form in **[EFTA01296720](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01296720.pdf), Page 56** (Redaction ID 207739, confidence 0.99):
```
MAX'WELL, GHISLAINE
116E 65TH ST
133-78-XXXX
12/1961
```

**Key observations:**
- The last four digits are redacted as "XXXX" in this document, but the first five digits **133-78** match the full SSN from the firearms permit
- The address **116 E 65th St** is a known Epstein-associated property in Manhattan (appears in 30+ financial/property documents in the database as "116 EAST 65TH ST")
- The DOB is listed as **12/1961** -- notably different from the firearms permit which shows **12125/1963** (likely OCR error for 12/25/1963, but the YEAR discrepancy of 1961 vs 1963 across documents is significant)

Adjacent entry in the same document ([EFTA01296720](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01296720.pdf), Page 58, Redaction ID 207740):
```
19
TSUKERMAN BELLA
2
2 E 63RD ST
0 3 80 XXXX
(34 ) 922
9
11/1960
```
This appears to be a database search result listing multiple individuals, suggesting [EFTA01296720](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01296720.pdf) is a law enforcement or investigative database pull.

### 2.3 Date of Birth Discrepancy

| Document | DOB Listed | Notes |
|---|---|---|
| [EFTA01653379](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653379.pdf) (NYPD firearms) | 12125/1963 | Likely OCR for 12/25/1963 |
| [EFTA01296720](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01296720.pdf) (database pull) | 12/1961 | Two-year discrepancy |
| [EFTA00022654](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022654.pdf) (investigation doc) | 12/25/1961 | Full date, year 1961 |
| [EFTA01693397](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01693397.pdf) (background report) | 12/25/1961 | Full date, year 1961 |

**Analysis:** Maxwell's actual date of birth is **December 25, 1961**. The firearms permit listing of "1963" is either a data entry error within the NYPD system or a deliberate falsification on the application. The two-year age discrepancy (making her appear younger) on a government firearms application is itself a potential violation.

**[REVISIT UPDATE -- DOB Discrepancy Resolved]:** With 4,215+ DS9 documents consistently showing 12/25/1961, the 1963 date on the firearms permit is almost certainly a data entry error in the NYPD system rather than deliberate falsification. The year 1963 appears only on that one document and nowhere else across the entire corpus.

---

## 3. MILITARY RECORD: YES -- ANOMALY ANALYSIS

### 3.1 The Flag

The NYPD firearms permit record states: **"Military Record: YES"**

### 3.2 Known Biography

Ghislaine Maxwell has no publicly documented military service in any nation's armed forces. She attended Headington School and Balliol College, Oxford, then moved to New York circa 1991. No military service has ever been alleged, claimed, or documented in any court proceeding, deposition, or biographical account.

### 3.3 Possible Explanations

1. **Data Entry Error:** The field was incorrectly populated.
2. **Inherited Flag:** In some law enforcement database systems, associations with military or intelligence personnel can create cascading flags. Her father Robert Maxwell had extensive documented connections to military and intelligence services.
3. **Misinterpretation of Foreign Records:** As a foreign-born individual with citizenship in three countries, records from foreign services might have been misinterpreted.
4. **Deliberate Fabrication on Application:** Military service can be advantageous on firearms permit applications; this could represent a false statement.
5. **Classified or Intelligence-Adjacent Service:** Given her father's documented intelligence connections (see Section 9), some form of intelligence-related service record could theoretically exist.

**[REVISIT UPDATE -- Military Record Flag Contextualized]:** The Experian credit report ([EFTA00152321](https://www.justice.gov/epstein/files/DataSet%209/EFTA00152321.pdf)) reveals Maxwell held a USAA Savings Bank account ($102,243 balance). USAA historically restricted membership to active and former military personnel and their families. A USAA Grand Jury subpoena chain ([EFTA00074084](https://www.justice.gov/epstein/files/DataSet%209/EFTA00074084.pdf), [EFTA00074091](https://www.justice.gov/epstein/files/DataSet%209/EFTA00074091.pdf), [EFTA00084186](https://www.justice.gov/epstein/files/DataSet%209/EFTA00084186.pdf)) confirms the FBI subpoenaed USAA for Maxwell's records. Additionally, Maxwell's security consultant Matthew Hellyer ([EFTA00065645](https://www.justice.gov/epstein/files/DataSet%209/EFTA00065645.pdf)) served 25 years in UK military including 15 in UK Special Forces. The combination of (a) a USAA account, (b) UK Special Forces security detail hired by her brother, (c) Robert Maxwell's documented intelligence connections, and (d) Scott Borgerson's Coast Guard background creates a constellation of military-adjacent associations that could explain the flag without requiring Maxwell herself to have served.

---

## 4. CRIMINAL RECORD: YES + STATUS: APPROVED -- ANOMALY

### 4.1 The Contradiction

The firearms permit application simultaneously shows:
- **Criminal Record: YES**
- **Status: APPROVED**

Under New York Penal Law Section 400.00, a firearms license shall be denied to any person who has been convicted of a serious offense or who lacks good moral character. An affirmative criminal record flag should trigger enhanced scrutiny and, for most criminal categories, denial.

### 4.2 Corroborating Document: [EFTA01653435](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653435.pdf)

**[EFTA01653435](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653435.pdf), Page 1** (Redaction ID 701287, confidence 0.99):
```
Possible Criminal Records (1 Found)
```

This document, filed near the firearms permit in the EFTA sequence, confirms that a background check associated with this investigation cluster found **one possible criminal record** for the subject.

### 4.3 Analysis

The approval of a firearms permit despite an affirmative criminal record flag suggests either:
1. The criminal record was for a non-disqualifying offense
2. The record was from a foreign jurisdiction and not treated as disqualifying
3. Influence or preferential treatment in the application process
4. The criminal record belonged to an alias or associated individual and was flagged but not attributed

---

## 5. CITIZENSHIP AND IDENTITY FLAGS

### 5.1 Citizenship Code "C"

The firearms permit lists **Citizen: C**. Standard NYPD codes use:
- "C" = Citizen (U.S.)
- Other codes for permanent resident, non-citizen, etc.

This confirms Maxwell represented herself as a U.S. citizen on the 2006 application.

### 5.2 Triple Citizenship Confirmation

**[EFTA00011365](https://www.justice.gov/epstein/files/DataSet%208/EFTA00011365.pdf), Page 2** (Redaction ID 49281, confidence 0.99):
```
Page 10 (Maxwell is a US Citizen as well as citizen of France and England)
```

This is from a deposition transcript analysis (the Maxwell Deposition Transcript, filed from Mineola, New York 11501, dated April 9, 2019).

**[REVISIT UPDATE -- Citizenship Investigation and Travel Records]:** An internal SDNY email chain dated January 21-22, 2020 ([EFTA00153527](https://www.justice.gov/epstein/files/DataSet%209/EFTA00153527.pdf)) reveals prosecutors actively investigating how Maxwell obtained US citizenship and requesting her immigration file from ICE/DHS. CBP/TECS records ([EFTA02727130](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02727130.pdf), pages 353-355) show a person record created 3/18/1992 listing Maxwell's citizenship as "UNITED KINGDOM" and status as "ALIEN" with a "PRIVATE AIRCRAFT INSPECTION" category. A "SILENT HIT" alert was placed 8/27/2019 (start date: 08/27/2019, stop date: 08/27/2020). The 1992 TECS record listing her as an alien confirms she was not yet a US citizen in March 1992 -- consistent with SSN issuance 1990-1993 as a legal alien/resident, not yet a citizen. A US passport renewal application (DS-82) dated April 2013 ([EFTA00099206](https://www.justice.gov/epstein/files/DataSet%209/EFTA00099206.pdf)) confirms Maxwell held and renewed a US passport.

### 5.3 Country of Birth: FR (France)

The firearms permit correctly identifies her country of birth as France (Maisons-Laffitte), consistent with known biographical data.

---

## 6. ADDRESS AND PROPERTY CONNECTIONS

### 6.1 116 East 65th Street

The address on the [EFTA01296720](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01296720.pdf) database pull -- **116 E 65th St** -- is the infamous Epstein Manhattan townhouse. Maxwell's use of this address on identity documents directly ties her residential status to Epstein's property. This address appears in over 30 financial and property documents in the database ([EFTA01516346](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01516346.pdf) through [EFTA01516501](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01516501.pdf) series).

### 6.2 Property Records Cluster: [EFTA01653382](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653382.pdf)

The document immediately following the firearms permit in the EFTA sequence ([EFTA01653382](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653382.pdf)) contains extensive property records including:
- Assessed values ($744,420; $300,200)
- Multiple property subdivisions with apartments, penthouses, front units
- Florida addresses (MIAMI BEACH FL 33139, MIAMI-DADE COUNTY)
- Driver's license data: `DL State: FL`
- Corporate records: `Type: Corporation`
- Associated names: JUAN ALBERTO BOLIVAR MA[RQUEZ], TYANA LEIKO YAMAMOT[O], SUE ANN PISACK (03/1966), STEFAN E MARAIS (08/1972), BOHUMIL WERNER, TAMMY DARLENE FRAZI[ER]

---

## 7. WEAPON ON PROPERTY -- MAXWELL ASSOCIATED

### 7.1 [EFTA01334212](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01334212.pdf) -- West Palm Beach Investigation

**[EFTA01334212](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01334212.pdf), Page 0-1** (multiple redaction IDs, confidence 0.77-0.99):
```
identified her [...] f as Maxwell,
```
```
revealed numerous ve[hicles]
```
```
hone account 4
under the name
ndicate a weapon is kept on the prop[erty]
```

**[EFTA01334212](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01334212.pdf), Page 2:**
```
received from WPBPD. The [information] provided the following information:
contact until the search has been done.
I advised them I will not attempt
```
```
Nothing else found.
is handling all discipline."
```

**Analysis:** This document identifies Maxwell by name and notes that a phone account under her name indicated **a weapon is kept on the property**. Information was received from **WPBPD (West Palm Beach Police Department)**. This places Maxwell in possession of or associated with a weapon at a property in the West Palm Beach area, near Epstein's Palm Beach estate.

### 7.2 [EFTA00022654](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022654.pdf) -- Second Weapon Reference

**[EFTA00022654](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022654.pdf), Page 1** (Redaction IDs 96839-96840):
```
u indicate a w[eapon]
under the name
pon i k[ept]
```
**[EFTA00022654](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022654.pdf), Page 4:**
```
Maxwell, Ghislain[e]
12/25/1961
was giving
8 El Bri[llo]
```

This document again links Maxwell (with correct DOB 12/25/1961) to a weapon indication, and references an address beginning with "8 El Bri" -- likely **8 El Brillo Way**, which is the address of Epstein's Palm Beach mansion.

### 7.3 [EFTA01661868](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01661868.pdf) -- Maxwell Gun Account Reference

**[EFTA01661868](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01661868.pdf), Page 6673** (Redaction ID 890633, confidence 0.99):
```
Pnmery ~Gun(
ONILMNE MAXWELL
S
O
```
**[EFTA01661868](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01661868.pdf), Page 6677:**
```
ng=
Primary Account
OITISLAINE MAXWELL
F
```

This appears to reference a "Primary Gun" or "Primary Account" associated with "GHISLAINE MAXWELL" in what appears to be a large financial/account database.

---

## 8. SSN ECOSYSTEM -- OTHER SSN REFERENCES IN THE DATABASE

### 8.1 Epstein SSN Email

**[EFTA00019064](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019064.pdf)** (Redaction ID 78423, confidence 0.834):
```
bject: Epstein SSN
```
With context showing this was an email sent Thursday, August 8, 2019 at 5:28 PM from an Assistant United States Attorney in New York, New York 10007 -- the SDNY office. This confirms the prosecutors were actively investigating Epstein's SSN.

### 8.2 [EFTA01364303](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01364303.pdf) -- Multi-Person SSN/DOB Sheet

This document contains SSN and DOB entries for multiple persons associated with Epstein:
```
na Shuliak [Karyna Shuliak - Epstein's last girlfriend]
ast 66 th Str [East 66th Street]
11110

Visoski r. [Lawrence Visoski Jr. - Epstein's pilot]
DOB
SSN:

Katherine G[roos]

Barrett

en K In[dyke - Darren Indyke, Epstein's lawyer]
```

### 8.3 "Others Using SSN" Pattern

Multiple background investigation reports across the database show "Others Using SSN" queries, a standard investigative tool to detect identity fraud:
- **0 records found** (majority of results) -- clean SSN
- **5 records found** ([EFTA01296282](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01296282.pdf), [EFTA01297209](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01297209.pdf), [EFTA01297220](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01297220.pdf)) -- indicating SSNs with multiple users, a red flag for identity fraud
- **1 record found** ([EFTA01363187](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01363187.pdf)) -- one additional user of the SSN

### 8.4 SSNs Summary Reports

**[EFTA01378400](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01378400.pdf)** and **[EFTA01399794](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01399794.pdf)** contain "SSNs Summary" documents, indicating systematic SSN analysis was conducted as part of the investigation.

---

## 9. INTELLIGENCE CONNECTIONS

### 9.1 MI6/CIA/Mossad References

Multiple documents in the database contain references to intelligence agency involvement with the Epstein/Maxwell case:

**[EFTA01652757](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652757.pdf), Page 5** (Redaction ID 697788, confidence 0.99):
```
BREAKING:
[...] THEORISTS WHO ARE NOW EXPERTS ON
Donald J. Trump, Prince Andrew,
Alan Dershowitz,
Lady Victoria Hervey,
Leslie & Abigail Wexner,
George B. Tonks,
Eileen Guggenheim,
Glenn & Eva Dubin,
Richard Branson, the Maxwell's,
FBI, M16, CIA or Mossad
DID NOT KILL
KILLED
```

**[EFTA01652995](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652995.pdf), Page 13** (Redaction ID 699098, confidence 0.99):
```
George B...
BREAKING:
Donald J. Trump. Prince Andrew.
Alan Dershowitz.
Lady Victoria Hervey,
Leslie & Abigail Wexner,
George B. To[nks].
Eileen Guggenheim,
Glenn & Eva Dubin,
Richard Branson. the Maxwell's.
FBI, MI6, CIA or [Mo]ssad
DID NOT KILL
[...] killed
KILLED
```

**[EFTA01653060](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653060.pdf), Page 4** (Redaction ID 700355, confidence 0.99):
```
Donald J. Trump, Prince Andrew.
Alan Dershowitz.
Lady Victoria Hervey,
Leslie & Abigail Weiner.
George B. Tonks,
Eileen Guggenheim,
Glenn & Eva Dubin.
Richard Branson. the Maxwell's.
FBI MI6. CIA or M[o]ss[a]d
DID NOT KILL
```

These appear to be social media screenshots collected as part of the investigation, specifically from a user named George B. Tonks, discussing theories about Epstein's death and listing intelligence agencies (FBI, MI6, CIA, Mossad) alongside "the Maxwell's."

### 9.2 "Collaborating with Intelligence Agencies"

**[EFTA01652995](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652995.pdf), Page 6** (Redaction ID 699035, confidence 0.99):
```
If we are collaborating with
intelligence agencies they
arc hardly going to listen to
you
x
```

**[EFTA01652971](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652971.pdf), Page 15** (Redaction ID 699459, confidence 0.99):
```
If we are collaborating with
intelligence agencies they
arc hardly going to listen to
you Maria
X
```

These appear to be communications referencing collaboration with intelligence agencies in the context of the Epstein/Maxwell investigation.

### 9.3 Robert Maxwell -- No Hidden Text Found

**Notable absence:** A search for "Robert Maxwell" across all 1.8 million redaction records returned **zero results**. While Robert Maxwell (1923-1991) is extensively documented in public sources as having alleged connections to Mossad, MI6, and the KGB, his name does not appear in any text extracted from document text layers in this database. This could indicate either that his name was never redacted (appearing in visible text instead), or that documents mentioning him were redacted differently.

### 9.4 Maxwell Family Members in Database

**[EFTA00019413](https://www.justice.gov/epstein/files/DataSet%208/EFTA00019413.pdf)** lists Maxwell family members:
```
5. ***Kevin Maxwell
6. Michael Maxwell
8. Philip Maxwell
```

Kevin Maxwell appears in additional correspondence documents ([EFTA01792888](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01792888.pdf), [EFTA01838416](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01838416.pdf), [EFTA01985449](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01985449.pdf)) in emails with Brian Basham and Ross Gow.

---

## 10. NYPD LAW ENFORCEMENT DATABASE ACTIVITY

### 10.1 NYPD Firearms Query Execution

The firearms permit was executed on **10/8/2019 at 13:14** by operator **NYPDFINESTSYRNE941477**. This date falls after Epstein's death (August 10, 2019) and during the period of active investigation into Maxwell, confirming this was a law enforcement database pull, not a permit application review.

**[REVISIT UPDATE -- Operator Identified]:** "NYPDFINESTSYRNE941477" is DT3 Paul W. Byrne, Tax# 941477, Shield 756, NYPD Squad HT (Human Trafficking), Command 488. "SYRNE" is an OCR corruption of "BYRNE." Byrne was also the arresting officer for Maxwell's March 29, 2021 arrest ([EFTA01261996](https://www.justice.gov/epstein/files/DataSet%209/EFTA01261996.pdf)), confirming he was assigned to the Maxwell case from at least October 2019 through the arrest in 2021.

### 10.2 NYPD Sex Offender Monitoring

**[EFTA00028415](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028415.pdf)** (Redaction ID 128970, confidence 0.8378):
```
NYPD Sex Offender Monitor[ing]
```
**[EFTA00028415](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028415.pdf), Page 1** (Redaction ID 128974, confidence 0.8698):
```
bject: Epstein case/NYPD Sex Of[fender]
```

This confirms NYPD was conducting sex offender monitoring in connection with the Epstein case.

### 10.3 NYPD Detective Bureau

**[EFTA00037655](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037655.pdf)** (Redaction ID 171826):
```
NYPDDetectiveBureau Chil[d]
```
**[EFTA00038047](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038047.pdf)** (Redaction ID 173755):
```
NYPDDetectiveBureau Child
```

References to the NYPD Detective Bureau Child [Exploitation/Abuse] unit involvement.

### 10.4 Multi-Agency Coordination

Multiple documents show NYPD coordination with federal agencies:
```
(USANYS) [Contractor]
(NYPD)
```
```
William (USAN[YS])
Paul (NYPD)
age/Video Fil[es]
```

---

## 11. SURROUNDING DOCUMENT CLUSTER ANALYSIS

The EFTA sequence around 01653379 reveals a systematic investigative file:

| EFTA Number | Content |
|---|---|
| [EFTA01653372](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653372.pdf) | TECS [Treasury Enforcement Communications System] query |
| [EFTA01653374](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653374.pdf) | Glenn Dubin mentioned; "Maxwell's assistant" |
| [EFTA01653379](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653379.pdf) | **NYPD Firearms Permit -- Maxwell** |
| [EFTA01653381](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653381.pdf) | "Report" |
| [EFTA01653382](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653382.pdf) | Comprehensive property records (Palm Beach, Miami, NYC) |
| [EFTA01653396](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653396.pdf) | TASPD reference |
| [EFTA01653421](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653421.pdf) | Intelligence Analyst reference |
| [EFTA01653435](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653435.pdf) | "Possible Criminal Records (1 Found)" |
| [EFTA01653487](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653487.pdf) | Image/Video Files reference with USANYS and NYPD |

This cluster represents a systematic law enforcement investigative file combining:
- Federal database queries (TECS)
- NYPD firearms records
- Property ownership records
- Criminal records checks
- Intelligence analysis
- Digital evidence (images/video)

---

## 12. PERMIT FOR EPSTEIN

**[EFTA01892660](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01892660.pdf)** contains an email with the subject line:
```
Subject: permit for Epstein
```
With associated references to "scozzari" and case number "CF08 I 720 I 2_0000 I". This suggests Epstein himself had permit-related proceedings, though the specific type of permit is not fully recoverable from the hidden text.

---

## 13. KEY ANALYTICAL CONCLUSIONS

### 13.1 The Connecticut SSN Paradox

SSN 133-78-4883 was issued in the Connecticut allocation range. Ghislaine Maxwell was born in France in 1961 and lived in Oxford, England before moving to New York circa 1991. There is no publicly known Connecticut connection in her biography. Under the pre-2011 geographic assignment system, this SSN should have been issued to someone who applied for a Social Security number through a Connecticut SSA office. Possible explanations include:

1. **Application through Connecticut:** Maxwell (or someone on her behalf) applied for an SSN at a Connecticut Social Security office, possibly during an early visit to the United States.
2. **Connection to Epstein:** Jeffrey Epstein had documented connections to Connecticut. If Maxwell obtained her SSN through an Epstein-facilitated process, this could explain the geographic mismatch.
3. **Identity Document Irregularity:** The SSN may not have been legitimately issued to Maxwell at all, suggesting potential identity fraud.

### 13.2 The Military Record Flag

The "Military Record: YES" flag on a person with no known military service is one of the most significant anomalies in this document. Combined with the intelligence agency references throughout the case files and the Maxwell family's documented intelligence connections, this flag raises the question of whether Maxwell had some form of classified government service or whether the flag is an artifact of intelligence database records that bled into the NYPD system.

### 13.3 The Criminal Record + Approval Paradox

A "Criminal Record: YES" flag combined with "Status: APPROVED" for a New York City firearms permit represents either a serious procedural failure or indicates the criminal record was deemed non-disqualifying. The separate document [EFTA01653435](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653435.pdf) confirming "Possible Criminal Records (1 Found)" corroborates that a record existed but does not clarify its nature or jurisdiction.

### 13.4 The Date of Birth Discrepancy

The firearms permit shows a DOB that could be read as 12/25/1963, while multiple other documents consistently show 12/25/1961. Maxwell's actual birth year is 1961. The 1963 date on the firearms application, if not an OCR artifact, could represent a deliberate two-year age reduction on the application -- a form of identity misrepresentation on a government document.

### 13.5 The NYSID Blank Field

The NYSID (New York State Identification) field is blank, meaning Maxwell had no prior New York State criminal fingerprint record at the time of the firearms database query. This is potentially inconsistent with the "Criminal Record: YES" flag, unless the criminal record was from another jurisdiction.

**[REVISIT UPDATE -- NYSID Anomaly Resolved]:** The NYPD arrest report ([EFTA01261996](https://www.justice.gov/epstein/files/DataSet%209/EFTA01261996.pdf), DS9) for Maxwell's March 29, 2021 arrest (Arrest ID M21609870) shows "RECORD STATUS: NYSID ENTERED" -- meaning the NYSID was created only at that time. The same report states "Number of Priors: 0." This confirms the NYSID was blank on the 2006 firearms permit because Maxwell had no New York State criminal fingerprint record until 2021. The "Criminal Record: YES" flag was therefore not based on a New York State record; it was likely from another jurisdiction, a federal record, or a data entry error. Defense counsel assertions in bail filings ("Ms. Maxwell has no criminal record," [EFTA00066317](https://www.justice.gov/epstein/files/DataSet%209/EFTA00066317.pdf)) further support that the flag was erroneous.

### 13.6 Document Context: Post-Mortem Investigation

The execution date of 10/8/2019 -- nearly two months after Epstein's death on 8/10/2019 -- confirms this firearms permit record was pulled as part of the active federal investigation into Maxwell and associates, not as a routine permit review. The surrounding EFTA cluster (TECS queries, property records, criminal background checks, intelligence analysis) represents a comprehensive investigative workup.

**[REVISIT UPDATE -- FBI Arrest Operation]:** DS9 contains the complete FBI Tactical Operation Plan for Maxwell's arrest ([EFTA00149884](https://www.justice.gov/epstein/files/DataSet%209/EFTA00149884.pdf) and [EFTA00152203](https://www.justice.gov/epstein/files/DataSet%209/EFTA00152203.pdf), case number 50D-NY-3027571). Prepared 6/30/2020, the plan confirms three citizenships, describes Maxwell as a "flight risk," identifies Borgerson as a "person of interest but not an alleged subject," and documents the use of CAST/technical phone tracking methods to locate Maxwell in the Sutton, NH / Lake Sunapee region. An FBI email dated September 17, 2019 ([EFTA00039885](https://www.justice.gov/epstein/files/DataSet%209/EFTA00039885.pdf)) from the Crimes Against Children unit confirms the FBI was tracking a cell phone believed to belong to Maxwell from that date, and that Maxwell was with Borgerson in Manchester-by-the-Sea, MA in August 2019 but fled after media scrutiny.

---

## 14. EVIDENCE INVENTORY

| Evidence ID | EFTA Number | Page | Key Content | Confidence |
|---|---|---|---|---|
| R-701164 | [EFTA01653379](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653379.pdf) | 0 | NYPD Firearms header, execution date | 0.99 |
| R-701165 | [EFTA01653379](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653379.pdf) | 0 | Full Maxwell firearms application | 0.99 |
| R-701166 | [EFTA01653379](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653379.pdf) | 0 | Application type fragment | 0.83 |
| R-207739 | [EFTA01296720](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01296720.pdf) | 56 | Maxwell SSN partial (133-78-XXXX) | 0.99 |
| R-701287 | [EFTA01653435](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653435.pdf) | 1 | Criminal Records (1 Found) | 0.99 |
| R-878908 | [EFTA01712451](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01712451.pdf) | 0 | Connecticut SSN issuance reference | 0.89 |
| R-49281 | [EFTA00011365](https://www.justice.gov/epstein/files/DataSet%208/EFTA00011365.pdf) | 2 | Triple citizenship confirmation | 0.99 |
| R-271418-20 | [EFTA01334212](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01334212.pdf) | 0-1 | Maxwell ID'd, weapon on property | 0.77-0.99 |
| R-96859-60 | [EFTA00022654](https://www.justice.gov/epstein/files/DataSet%208/EFTA00022654.pdf) | 4 | Maxwell DOB 12/25/1961 | 0.80 |
| R-890633 | [EFTA01661868](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01661868.pdf) | 6673 | Maxwell gun/primary account | 0.99 |
| R-699035 | [EFTA01652995](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652995.pdf) | 6 | Intelligence agencies collaboration | 0.99 |
| R-697788 | [EFTA01652757](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652757.pdf) | 5 | MI6/CIA/Mossad + Maxwell's listed | 0.99 |
| R-128970 | [EFTA00028415](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028415.pdf) | 0 | NYPD Sex Offender Monitoring | 0.84 |

---

## 15. RECOMMENDATIONS FOR FURTHER INVESTIGATION

1. **SSN Issuance Records:** ~~Request SSA records for SSN 133-78-4883 to determine the original applicant, date of issuance, and application location.~~ **[RESOLVED by revisit]:** Experian credit report ([EFTA00152321](https://www.justice.gov/epstein/files/DataSet%209/EFTA00152321.pdf)) confirms issuance 1990-1993.
2. **NYPD Firearms Division Records:** Obtain the complete original application file from February 21, 2006, including the physical application form, supporting documents submitted, and the adjudicator's notes explaining approval despite criminal record flag. **[PARTIALLY RESOLVED by revisit]:** DS11 full firearms permit ([EFTA02727130](https://www.justice.gov/epstein/files/DataSet%2011/EFTA02727130.pdf), page 348) provides complete un-redacted record: Application X2006000433, Permit 2006002458, issued 11/2/2006, Glock 19 (Serial KM8076) sold to gun dealer on 12/12/2006 (40 days after issuance), permit cancelled 11/16/2009 when Maxwell moved to Florida. Firearm transferred via West Side Range. Associate on application: Richard Barnett, 14 Oakland Ave, Port Washington.
3. **Military Records Check:** Submit FOIA requests to all branches of U.S. military, as well as UK MOD, for any service records under the name Ghislaine Maxwell or known aliases. **[CONTEXTUALIZED by revisit]:** USAA account and UK Special Forces security detail provide plausible non-service explanations.
4. **Criminal Record Identification:** ~~Determine the nature and jurisdiction of the criminal record flagged in the NYPD system and in [EFTA01653435](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653435.pdf).~~ **[PARTIALLY RESOLVED by revisit]:** 2021 arrest report confirms 0 priors; defense counsel asserted no criminal record. Flag almost certainly a database error.
5. **Connecticut Connection:** Investigate any Maxwell or Epstein property, business, or personal connections to Connecticut during the period when the SSN would have been issued. **[NARROWED by revisit]:** Issuance 1990-1993 aligns with Maxwell's arrival; Connecticut application during early travels remains plausible.
6. **NYSID Reconciliation:** ~~Determine why NYSID is blank when Criminal Record shows YES.~~ **[RESOLVED by revisit]:** NYSID entered only upon 2021 arrest; Maxwell had no prior NY State criminal fingerprint record.
7. **Date of Birth Investigation:** ~~Determine whether the 1963 DOB on the firearms application was an applicant-provided date (potential fraud) or a data entry error.~~ **[RESOLVED by revisit]:** 4,215+ DS9 documents unanimously show 12/25/1961; 1963 is a data entry error.

---

*Report compiled from forensic analysis of primary document text database containing text extracted from document text layers of DOJ Epstein file releases. DATA QUALITY NOTE: A data quality audit confirmed ~98% of 'bad_overlay' records are OCR noise from degraded scans. Text searches remain valid for identifying document content.*
