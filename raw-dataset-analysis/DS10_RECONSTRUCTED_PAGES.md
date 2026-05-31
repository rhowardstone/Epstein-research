# Epstein Files: Reconstructed Redacted Pages

**Generated:** 2026-02-05 20:30:48

## Methodology

**Data Source Note:** Per REDACTION_TEXT_LAYER_ANALYSIS (Report #93), DS10's "hidden text under redaction bars" is predominantly garbled OCR from an invisible Tr=3 text rendering layer placed over scanned document images, not content genuinely concealed beneath PDF redaction annotations. The black boxes visible in these PDFs are baked JPEG pixels in the scanned images, not PDF overlay objects. The full_text_corpus.db (PyMuPDF extraction) captures the same underlying text more cleanly. The reconstructed pages below reflect OCR of page content, and while the extracted text is real, the recovery mechanism is OCR-based, not redaction-defeat.

Each entry in the redaction database represents text extracted from under a single
black rectangle region in court documents. Multiple rectangles on the
same page, when read in spatial order (top-to-bottom, left-to-right), reconstruct
page content.

This analysis groups fragments by EFTA number and page number, orders them by
spatial coordinates (rect_y0 then rect_x0), and concatenates them to produce
readable page reconstructions.

## Summary Statistics

- **Total redaction entries in database:** 1,808,915
- **Entries with meaningful hidden text (>5 chars):** 427,604
- **Reconstructed pages (3+ fragments):** 39588
- **Total reconstructed text:** 4,076,924 characters
- **Pages containing email addresses:** 176
- **Pages containing dollar amounts:** 1076

### Document Type Distribution

| Document Type | Count | Percentage |
|---|---|---|
| OTHER | 28311 | 71.5% |
| CALENDAR_SCHEDULE | 4385 | 11.1% |
| EMAIL | 2904 | 7.3% |
| FINANCIAL | 1482 | 3.7% |
| PHONE_RECORD | 1005 | 2.5% |
| VICTIM_STATEMENT | 883 | 2.2% |
| FLIGHT_LOG | 255 | 0.6% |
| FBI_REPORT | 205 | 0.5% |
| LEGAL | 119 | 0.3% |
| PROPERTY | 35 | 0.1% |
| ADDRESS_BOOK | 4 | 0.0% |

### Most Frequently Referenced Names (across all reconstructed pages)

| Name | Pages |
|---|---|
| Epstein | 4099 |
| Jeffrey | 1644 |
| Les | 960 |
| New York | 821 |
| Maxwell | 597 |
| Palm Beach | 376 |
| Groff | 341 |
| Ghislaine | 302 |
| Black | 274 |
| Bill | 222 |
| Paul | 220 |
| Leon | 153 |
| Ross | 136 |
| Bradley | 134 |
| Andrew | 121 |
| Chris | 117 |

**Name Disambiguation Notes:**
- **"Les" (960 pages)** — Likely includes Les Wexner references, other uses of "Les" as a first name, and word fragments
- **"Ross" (136 pages)** — Multiple individuals: Adriana Ross (co-conspirator), other Rosses in legal filings
- **"Bradley" (134 pages)** — Predominantly Bradley Gillin (Deutsche Bank) in account management emails
- **"Mitchell" (54 pages, if present below)** — Both Senator George Mitchell and David Mitchell (estate co-executor) are separate individuals who appear in the corpus
| Darren | 114 |
| Indyke | 99 |
| Larry | 73 |
| Edwards | 63 |
| Rodriguez | 63 |
| Maria | 58 |
| Alan | 56 |
| Mitchell | 54 |
| Jay | 53 |
| Visoski | 52 |
| Sarah | 45 |
| Manhattan | 44 |
| Kevin | 40 |
| Janusz | 33 |
| Donald | 31 |
| Richardson | 26 |
| Prince | 21 |
| Barak | 21 |
| Alexander | 18 |
| Zorro Ranch | 18 |
| Trump | 17 |
| Brunel | 17 |
| Stephen | 16 |
| Dubin | 15 |
| Scarola | 14 |
| Summers | 13 |
| Virginia | 12 |
| Acosta | 12 |
| Banasiak | 12 |
| Roberts | 11 |
| Clinton | 9 |
| Marvin | 8 |
| Staley | 7 |
| Lefkowitz | 7 |

### Email Addresses Found Under Redactions

| Email Address | Occurrences |
|---|---|
| jeevacation@gmail.com | 21 |
| Kelly.Eldred@fca.org.uk | 7 |
| evacation@gmail.com | 3 |
| thebranch.staff@db.com | 3 |
| oevacation@gmail.com | 3 |
| decott@fca.org.ulc | 2 |
| CEverdell@CohenGresser.com | 2 |
| 6385257@projects.filevine | 2 |
| victimservices@fbi.gov | 2 |
| dred@fca.org.uk | 2 |
| er@hmflaw.com | 2 |
| bcsternheim@mac.com | 2 |
| leevacation@gmail.com | 2 |
| dor@podhurst.com | 2 |
| o@db.com | 2 |
| cation@gmail.com | 2 |
| ate.Tuckley@fca.org.uk | 2 |
| tion@gmail.com | 2 |
| Tammy_Torres@ca2.uscourts.gov | 2 |
| jpagliuca@hmflaw.co | 2 |
| y@db.co | 1 |
| ecf@eplIc.com | 1 |
| Renelltile@fisglobal.com | 1 |
| eckprocessing@list.db.com | 1 |
| v@db.com | 1 |
| brad@eplIc.corn | 1 |
| janusz53@me.com | 1 |
| pbrd_admin@list.db.com | 1 |
| owlmgw@att.net | 1 |
| KateTuckley@fca.org.uk | 1 |

### Notable Dollar Amounts Found Under Redactions

| Amount | EFTA | Page |
|---|---|---|
| $13,000,000.00 | [EFTA02730486](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730486.pdf) | 145 |
| $13,000,000.00 | [EFTA01684466](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684466.pdf) | 133 |
| $10194682 | [EFTA01378580](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01378580.pdf) | 0 |
| $3,280,074.47 | [EFTA01365914](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01365914.pdf) | 0 |
| $2,000,000 | [EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf) | 3 |
| $2,000,000 | [EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf) | 2 |
| $2,000,000 | [EFTA01266134](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266134.pdf) | 3 |
| $2,000,000 | [EFTA01266134](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266134.pdf) | 3 |
| $126,714,2 | [EFTA01361658](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01361658.pdf) | 0 |
| $1122000 | [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) | 1009 |
| $1000000 | [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) | 998 |
| $750,000 | [EFTA01656173](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656173.pdf) | 14 |
| $750,000 | [EFTA01656152](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656152.pdf) | 14 |
| $749,347. | [EFTA01437262](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01437262.pdf) | 3 |
| $700000 | [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) | 404 |
| $600,000 | [EFTA01377043](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01377043.pdf) | 0 |
| $562,976. | [EFTA01437262](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01437262.pdf) | 3 |
| $500,000 | [EFTA01269520](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01269520.pdf) | 6 |
| $497,882. | [EFTA01437262](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01437262.pdf) | 6 |
| $483882 | [EFTA01362825](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01362825.pdf) | 0 |
| $475,000.0 | [EFTA01561305](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01561305.pdf) | 10 |
| $4,000,00 | [EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf) | 3 |
| $2,42400 | [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) | 758 |
| $188,000 | [EFTA01693046](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01693046.pdf) | 71 |
| $167500 | [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) | 310 |
| $1,36500 | [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) | 894 |
| $1,28750 | [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) | 405 |
| $1,23200 | [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) | 565 |
| $1,20060 | [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) | 849 |
| $1,20000 | [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) | 925 |

---

## Top 200 Most Significant Reconstructed Pages

Pages are ranked by an interest score based on: text length, number of fragments,
named individuals mentioned, financial amounts, email addresses, phone numbers,
dates, and high-value investigative keywords.

---

### EMAIL (8 pages)

#### [1] [EFTA01652971](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652971.pdf) -- Page 15

- **Interest Score:** 115.3
- **Fragments:** 8
- **Document Type:** EMAIL
- **Dataset:** ds10
- **Names Found:** Andrew, Prince, Les, Sarah, Virginia, Giuffre, Farmer, Maria, Edwards

**Reconstructed Text:**

```
Jule-29;2O2Z-
WOV(10r.ht,ey • 
IP.,  Con,. MOP* 5
Just like I said a few days ago Km 
Edwards is your guy. I believe Virginia 
giuf fre and Maria Farmer are con 
artists and we have the proof. 
I only use credible sources. 
I don'tgive labelsunless there's If we are collaborating with 
intelligence agencies they 
arc hardly going to listen to 
you Maria 
X
indisputable proof A A A 
Send moisp.is 
Q V 
L d Vi
i H n. \ I inA 
What ease were you a 
witness on and what 
governmental agency 
granted you whotleblower 
status. No one can find it. 
If Geroge R. Mat lied 
b
i i
h
about =rising the attorneys 
ld h
dhi
d h
C.orsr no et inns< held him if he felt George 
submitted a fraudulent 
document to the court.
None of that happened...
George B. Tonks fti @GeorgeBTonks • 13m 
••• 
Sarah, yes Maria Farmer & Virginia Giuffre are 
liars. No Sarah, it's not over yet, but will be 
soon! 
a, Sarah Ransome @SarahRa... • 10/16/23 
Replying to @VRSVirginia and 
@pinkPeptobismot 
And Virginia if you think this Prince Andrew 
matter is over I've got news for YOU little 
girl. It's ain't over and yes I'm going to make 
sure you return every cent back to the 
British Monarchy. You are a disgrace to tt r& 
12:26 .` j.
```

#### [2] [EFTA01652995](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652995.pdf) -- Page 6

- **Interest Score:** 95.4
- **Fragments:** 10
- **Document Type:** EMAIL
- **Dataset:** ds10
- **Names Found:** Andrew, Prince, Les, Sarah, Edwards

**Reconstructed Text:**

```
July 79,1-023. 
s 
Wen: t ninnies. • 2;,
Just like I said a few days ago Huw 
Edwards is your guy. I believe 
are con 
artists and we have the proof. 
I only use credible sources. 
I don't give labels unless there's If we are collaborating with 
intelligence agencies they 
arc hardly going to listen to 
you 
x
indisputable proof A A A VC. hat Caw were toil a 
\Slim:, on and what 
govetnnwnt:d agency 
granted you whistIt-blower 
%taw,. Nu one tan find it. 
111(1corge N. Total ha 
b
about anything the attorney. 
ld h
dhi
d h
would hate wed him and the 
f d
l l d
ldh t
federal lodge would hate 
h ld hi
if h
f lt li
Gnome It Tanks 7-13 
I appreciate Lady victoria Hervey's honesty. held him if he felt licorgr 
submitted a fraudulent 
tkwunwnt to the cowl 
None of that hapiwned
George B. Tonks 
@GeorgeBTonks • 13m 
••• 
,yes 
are 
liars. No 
, it's not over yet, but will be 
soon! 
@SarahRa... • 10/16/23 
Replying to 
@oinkPeptobismot 
And 
if you think this Prince Andrew 
matter is over I've got news for YOU little 
girl- t's ain't over and yes I'm going to make 
sure you return every cent back to the 
British Monarchy. You are a disgrace to ti r& 
12:26 ` .J
```

#### [3] [EFTA01951455](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01951455.pdf) -- Page 0

- **Interest Score:** 73.4
- **Fragments:** 3
- **Document Type:** EMAIL
- **Dataset:** ds10
- **Names Found:** Epstein, Jeffrey, Andrew, Staley, Chris

**Reconstructed Text:**

```
To: 
Jes Staley 
Cc: 
alex von bidder 
bi he s masters 
clayton s. rose 
debora stale 
sloane 
andrew I cohen 
christo• er 
(brother) staley 
I cla ton 
rose 
debora stale 
emilio saracho 
Janet Staley 
geevacation@gmail com)[jeffrey e epstein geevacationggmail c
[alex von b • 
s 
- 
bl 
m te
killian staley 
• christo • er
• 
s orn
s 
p 
1* 
brother 
rik ortel 
)1; 
oane 
staff 
James
)
barrett 
Shah 
Waring 
stale 
iT 
uinc smith 
Silva 
bernstein 
white 
h.m. whi.d 
collins 
Vic 
Fran: 
Sent:
-in- w nitzan 
• jose 
h 
w I r 
'udson c. 'ud linville 
rk 
iratunnii 
uinc smith 
h a. walker 
Rosa da 
seth p. bernstein 
Jes Staley 
Wed 10/30/2013 9:05:45 PM
barre
c.
n
 
!
 
d
k
a
t
a
4
7
1
 
it 
sophia s
h m 
whidden 
; timoth c. collins
```

#### [4] [EFTA00027912](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027912.pdf) -- Page 0

- **Interest Score:** 59.6
- **Fragments:** 17
- **Document Type:** EMAIL
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Andrew, Edwards

**Reconstructed Text:**

```
Roberta Kaplan  
fr-" 
)"
er 9 2019 4:55:53 PM
<->; 
; Brad Edwards >; Sigrid McCawley
sa Bloom < Brittany Henderson < >; ECF <ecf@epl com>; Laura Starr
; Andrew Benjamin Margulis <
Villacastin oria Allred < Mullen
c: 
<a>
<a> 
ubject: FW: Epstein Victims'
Rachel Harris <rh
Subject: RE: Epstein Victims' Co
```

#### [5] [EFTA00027107](https://www.justice.gov/epstein/files/DataSet%208/EFTA00027107.pdf) -- Page 0

- **Interest Score:** 58.5
- **Fragments:** 6
- **Document Type:** EMAIL
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Jeffrey

**Reconstructed Text:**

```
T
d
A
t 13 2019 5 38 PM
To: 
Cc: 
Subject: FW: CONFIDENTIAL: Coordinating Victim Interviews Against Jeffrey Epstein 19 Cr 490 (RMB)
t 13, 2019 5:20 PM
Teri Gibbs 
Arick Fuda
bject: CONFIDENTIAL: Coordinating Victim Intervie
ws Against Jeffrey Epstein, 19
Please let me know
```

#### [6] [EFTA01380778](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01380778.pdf) -- Page 0

- **Interest Score:** 53.9
- **Fragments:** 6
- **Document Type:** EMAIL
- **Dataset:** ds10
- **Names Found:** Rodriguez, Mitchell, Bradley

**Reconstructed Text:**

```
Bradley Gillin 
Divya Rajawat 
Cynthia Rodriguez 
INV 
; Mariela Lopez 
Raphael A Mann 
Mitchell 
; Stewart Oldfield 
Gail F Mahabir 
j; Norma A Kenney 
; Muhammod 1 Uddin 
; Hemant-Kumar Rathore 
; Sara Castro 
l; Theresa Coleman 
RE D
it R t
A/ tl
Q
f
t
It
[C]
; William-M Finn 
; CUST 
; Evon A Lawrenc
; Ema Menniti 
; Joy E
>; Cynthia Rodriguez ; Gail F Mahabir
y@db.co ; orm
uhammod J Uddin 
Kumar Rathore a; 
Evon A Lawrence 
>; Ema Menniti
```

#### [7] [EFTA00028682](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028682.pdf) -- Page 4

- **Interest Score:** 53.4
- **Fragments:** 9
- **Document Type:** EMAIL
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Les, Maria

**Reconstructed Text:**

```
L
A
l
CA
Tuesday August 11 2020 1
Cc: Maria n Wang < 
: New potential victims of Epstein
From: Gloria Allred
st 10, 2020 7:31 PM
Cc: Mariann Wang < tial victims of Epstein and so
Los Angeles, CA
```

#### [8] [EFTA00021776](https://www.justice.gov/epstein/files/DataSet%208/EFTA00021776.pdf) -- Page 0

- **Interest Score:** 53.2
- **Fragments:** 6
- **Document Type:** EMAIL
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Maxwell, Ghislaine, Jeffrey, Manhattan

**Reconstructed Text:**

```
RE GHISLAINE MAXWELL CHARGED IN MANHATTAN FE
Thursday July 2 2020 5:11PM
bject: RE: GHISLAINE MAXWELL CHARGED IN MANHATT
urs ay, uy ,
:
To: 
Subject: FW: GHISLAINE MAXWELL CHARGED IN MANHATTAN FEDERAL COURT FOR CONSPIRING WITH JEFFREY EPSTEIN
urs ay, uy , 
:
```

---

### FINANCIAL (57 pages)

#### [9] [EFTA01357833](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357833.pdf) -- Page 0

- **Interest Score:** 154.0
- **Fragments:** 10
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
11 75
FY 1TE EBITDA (1 Mithr.n) 
1225
2215
13 25
1175
1425
1110 FY 13E FCFC/Mtlkon 
$1 76
$2215
1275
1315
$3 75
$4 2
$4 75
FY 16E EBITDA IS Marconi 
$1 11
$125
$275
Sin
2176
1425
SUS FY 16E FCF IS I dirwmi 
11 75
1225
$276
$11 25
$176
$4 25
$411
$1.73 
$224 
$.75 
$321 
San 
1425 
1476 NifIVEX Gan IS., 
61 .75 
$22 $273 
SSM 
13.7$ 
1416
$1.71 
San 
12.75 
lin 
015 
P
66c
10
614
474
ell
$4.25 
1075 
41*
3* NYISEX Gan IS 90
$1 I) 
12
130 0
31e
SI 12.1, 
13 
fin 
$4.26 
4271 
510
SI 5
$1 5
$16
$16
```

#### [10] [EFTA01357828](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357828.pdf) -- Page 0

- **Interest Score:** 145.8
- **Fragments:** 9
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
FY 15E EFII/DA (5. 
11111
1126
Sin
112
VI
$4 21
1415 FY 15E FCF 
NIMEC Car rS.Jm, 
51 13
$2 77
$i rs
$3 2$
$375
$4 26
14 15
FY 15E ESITEIA (S Million) 
ro' VEY G.r. 3-
$1 75
52
UM
$12$
137$
$4 2$
$4 75 FY 16E FCC IS Million) 
N !MP( Gas 
SI 75
$2 25
32 7>
$3 23
$675
San
14 7$
rn VIC( C.. , Sanc.e) 
SI 7$ 
1126 
TS 
13.25 
13.75 
5415 
14.75 (simo
St /5 
/2.25 52.75 
$3.25 
517$ 
14.25 
54.75
%IF • 
3 r l 
$1.715 
26 
$275 
1115 
079 
atm 
$4.75 
1360
36 9
201
2515
211
169$
161
15 I $1.75 
12.25 
12.75 
$3.25 
477 
14.25 
14.75 
1310
133
$33
$33
532
132
$32
$31
```

#### [11] [EFTA01266134](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266134.pdf) -- Page 3

- **Interest Score:** 140.5
- **Fragments:** 5
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
i
D ll
with a lum sum in the amou
lance payable to the estate of
if she sur
llars ($4 000 000) which
if she su
rs ($2,000,000), which a
($2,000,000)
```

#### [12] [EFTA01357835](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357835.pdf) -- Page 0

- **Interest Score:** 130.3
- **Fragments:** 9
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
FY ISE EBITDA(.5 NItlion) 
$375
1225
1175
$3 25
1325
SLSS
$4 23 FY 15E FCF IS Million) 
NV 
x 618 I Sin< It 
5375
P 25
$2 75
13 25
1175
14 25
14 75
FY ISE ESITDA (5 Million) 
$1 76
12215
12 75
6/26
5125
$425
14 26 44 r SSinn
Sinn
FY 16E FCF IS Million  
$1 75
12 25
17 75
$3 25
$375
$1 25
/4 75
11.7$ 
53.25 
1225 
$125 
Sin 
14.26 
11.25 51.75 
12.25 
112.75 
1325 
$175 
14.25 
$4.75
11.7$ 
1175 
$2.0 
$.3.25 
St 
5300
430
401
308
346
326
14.26
14.15 
174
30 1175 
1360
$I 4
12.2
$1 /2.76 
$3.25 
$175 
14.24 
34.75 
$1 4
$1 4
$I 4
$14
$14
```

#### [13] [EFTA01357836](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357836.pdf) -- Page 0

- **Interest Score:** 129.8
- **Fragments:** 9
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
FY ISE EMMA (.5 Million) 
51 75
$225
52 75
1125
13 75
14 25
$ 75 F9 150 FCF (1 Million) 
$175
1225
12 75
2325
5175
$4 26
$4 75
F Y 160 EBITDA (S Million) 
In 
c...:3 
$1.71
$2.4
22-75
1123
237$
1 425
14.73 FY 16E FCF (5 Million( 
11 75
12 23
52 75
53 25
5175
$426
1415
g
$1 74 
$225 
12.6 
$3.22 
$276 
11.25 
14.75 (
NYMEX Gas (tingle) 
Sin 
1171 
$2.15 
S3.4 
$1 IS 
6 72 
54.75
311). 0.45 µlmere) 
51 
122$ 
1275 
$3.23 
117$
5425 
2475 
13110
114$
748
1
4344
1311
9174
246 NYMEX Gt. si
11.75 
4
$30 0
$2 0 o 
12.73 
13.25 
1215 
5125 
14.75 
$28
123
$23
$24
$27
```

#### [14] [EFTA01357813](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357813.pdf) -- Page 0

- **Interest Score:** 114.9
- **Fragments:** 9
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
FY 15E EBITDA (5 111.1106) 
11 71
$129
1221
11 25
AR
$42$
14 75 FY 13E F CF CS 'litham] 
orlAtx Gac r3.90 
51 73
12 25
12 71
MO
1275
$1 25
$4 1$
FY IFE EBITDA (5 M119.6.11 
* 
11 75
3226
12 71
1121
13 76
$126
14 75 FY 16E FCF IS Milton) 
eiltAEx Cas 0.9/1/1 
$1 is
$2]>
32 75
1 26
31/5
14 25
14 75
NYME X On Oimec.) 
SI /6 
$226 
/3 
3123 
117$ 
S4-29 
14.75 NOI4Ex Gac .197.e) 
$1.73 
2.26 
1.7> 
1125 
$313 
an 
14.75
NYI1EX Ga/ (9mcle) 
117s 
se n 
1175 
$123 
11175 
$4.29 
1175 
134 0
79 PI'
1174
191á
2573
31 2 $6
430 * NYMEx Gas 0970
s1 zs 
$2 2
510
115
SI S 12.71 
$3.21 
3175 
1.4.13 
1175 
515
115
S15
$16
SIS
```

#### [15] [EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf) -- Page 3

- **Interest Score:** 109.3
- **Fragments:** 8
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
i
d i t
ti
th t
ees for the benefit of 
he amount of Two Million Dol
lance payable to the estate of
benefit of 
Million Dollars ($4,000,00
with a lum sum in th
ayable to the estate of
payable to the estate
enefit of 
ion Dollars ($2,000,000
e payable to the estate o
```

#### [16] [EFTA01357838](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357838.pdf) -- Page 0

- **Interest Score:** 103.5
- **Fragments:** 9
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
FY ISE EBITDA (5 
31 71
1276
1276
3125
13 73
1 12$
14 75 FY 15E FCF (S Million) 
NYMEx Gan (Simile) 
1175
5225
12 75
13 23
5516
14 25
14 75
FY 16E EBITDA (S litill0m) 
NYMEX Gas IAm93e1 
21 75
$2 25
$2 75
$3 25
13 73
1142$
$4 75 7. ISE FCF IS 
1375
32 25
0 75
0 26
$176
14 25
1175
NYNEX Gas (timcce) 
SA 7 S 
$2h 
1276 
1126 
$375 
1126 
11.75 NYMEX GAS (Linde) 
1113 
$2 .25 
$x75 
13.2$ 
23 75 
14.26 
14.75
W“11). Gas µ176c4) 
$1.75 
5225 
12.75 
$3.25 
$130
209
260
220*
205
13.75
54.25 
14.75 
163
145
154 NYMEX 04, ! sm
11375 
230 0
232
1 ) 
13.23 
$175 
11.25 
11.75 
132
$31
$31
$31
131
1235
```

#### [17] [EFTA01357810](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357810.pdf) -- Page 0

- **Interest Score:** 100.9
- **Fragments:** 8
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
FY 15€ EFITTDA (5 M.lhon) 
1175
$120
%A
33 21
$3 73
14 75
5475 FY 15E FCF (5 hlillsoni 
«I /ME« Ca« ii.Jrne 
11 73
57 21
$2 73
$3 21
5175
54 25
1175
12175
9254
FY 16E 8ITDA (S. Milbon) 
53 21
an
$425
54% /V 16E FCF (5 ,Whorl) 
1175
an
52 75
33 23
3171
$4 25
54 75
11.7$ 
12.25 
1235 
5125 
14.70 
14.25 
14.75 5471 
an 
$2.73 
5171 
3175 
$4.25 
34.75
stil
a 
5475
$125 
5110
128
133
e1
47x
nn 
$4.15 
14.75 
382
3h
20 5171 
an 
Ian 
$3.26 
nis 
14.2$ 
$30 0
114
$14
$13
313
112
II 1
$1.75 
311
```

#### [18] [EFTA01357843](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357843.pdf) -- Page 0

- **Interest Score:** 100.0
- **Fragments:** 9
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
11 73
1225
FY 15E EMMA (5 Million) 
1225
1125
1175
$4 25
14 75 FY 15E FCF (S Million) 
NT roiEK Gini 
11 75
1225
12 75
131
1175
$
v %IF 
FY 16E EBITDA (5 1117ilion) 
11 75
$229
1275
1125
11 75
$4 21
14 Fl 17.E FCF IS Mil:ion) 
1175
12.25
71
a
$175
75
14 75
NYNEX Gas (timefe) 
Si 7, 
S7 1 
g
1? IN 
SAP. 
1375 
14 / 
14.75 p
NYME x Gas (SEncle) 
11.m 
32.25 
17.79 
13 23 
$375 
14.25 
$4.75
In11112.0.s µ,nie re) 
11.75 
1300
31I
$2
12.73 
172
114.25 
$3.25 
$4.75 
12 44
1071
934
i
13.73 .1
2272 0.6 
075 
1
$10 0
$17 c) 
1775
$3.26 
1173 
14.25 
14.75 
III
$16
$15
115
315
```

#### [19] [EFTA01437262](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01437262.pdf) -- Page 3

- **Interest Score:** 94.1
- **Fragments:** 7
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
PREAUTHORIZED ACH DEB
WAGE PAY
PAYROLL FEES
$749,347.
$562,976.
No items
$15,000.0
```

#### [20] [EFTA01357840](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357840.pdf) -- Page 0

- **Interest Score:** 88.3
- **Fragments:** 9
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
$1 5
25
FY ISE ESITDA (1 NItitron I 
12 5
$3 5
14 21
11 11 FY ISE FCF (1, Million) 
NV ME X .63, Sin< le I 
14 5
5225
52 5
11 25
1125
54 5
FY ISE EBITDA(S Nblhon) 
6 75
3223
1275
1125
5375
51 25
11 75 FY 16E FCF (S Millionl 
NYMEN G..75 (1107 
11 is
0 26
12 75
UM
$175
25
54 75
NYNEX Gas(/Mich) 
1/ 
g
17 78 
II 78 
13 75 
IL» 
11.75 NYMEX Gas (Vmcit) 
II .O 
v.93 
i2.75 
11.25 
$175 
14.25 
14.71
7•8 811-). Das If mere) 
11.75 
13{10
22
52
13.75 
31 47
001
$3.25
53.75 
54-25 
1.75 
104
161
1141
164 ISYNNESCes!s
0.95 
5
5300
$33 ) 
52.75 
13.25 
1175 
11.25 
1475 
$21
$23
$23
$23
$23
```

#### [21] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 1009

- **Interest Score:** 88.1
- **Fragments:** 4
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
eck: 2102 
Amount: $1122000 
Date: 03101/20 .00 
Date: 03,01/20
Check: 5389 
Amount: $3,040.00 
Date: 03/05/20 Check 5392 
Amount: $4,431.00 
Date: 0305,201
```

#### [22] [EFTA01477454](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477454.pdf) -- Page 0

- **Interest Score:** 86.0
- **Fragments:** 22
- **Document Type:** FINANCIAL
- **Dataset:** ds10
- **Names Found:** Jeffrey, Black, Leon, Darren, New York

**Reconstructed Text:**

```
.
s
-
Mrra
ldfaldBank c.
7LL
1.1...........
Morris/Oldfield Banker SOUTHERN FIN
Morris/Oldfield Banker
GRATITUDE AM
Morris/Oldfield Banker
CRW 2007 LLC
ldfield Banker
NEW YORK STRATEGY GR
ldfield Banker LEON D. BLACK
Oldfield Banker PLAN D LLC
Oldfield Banker LEON D. BLACK
0 
e 
Ban er MARK F. DZIALGA 
Oldfield Banker
Morris/Oldfield Banker JEGE INC
Oldfield Banker THE NATIONAL ORGANIZ
Oldfield Banker DOMINIQUE LEIMER
Morris/Oldfield Banker 55W 2007 LLC
PMENT COR
PWPIPM!
Ier
llRrg
ll
Morris/Oldfield Banker JEFFREY EPST
Morris/Oldfield Banker SOUTHERN TRU
Morris/Oldfield Banker WANEK TRUST
DYKE PLLC bLMIN..
/M
er
SSW
LLC 
Morris/Oldfield Banker DARREN K. IN
Morris/Oldfield Banker HYPERION AIR
```

#### [23] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 998

- **Interest Score:** 85.4
- **Fragments:** 6
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
t $1000000
D t
0211120 k 5440
Amount $840 00
D t
02/11/20
ck 1658 
Amount. $4,000.00 
Date: 02/11/20 Check: 5448 
Amount. $2.227.40 
Da
Check
5450
Amount: $3 294 00
Date 02 12 201 Check
5454
Amount $54000
Date 02 12 20
```

#### [24] [EFTA01266168](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01266168.pdf) -- Page 2

- **Interest Score:** 85.2
- **Fragments:** 8
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
if she 
efit of 
D ll
($4 000 000) which
with a lump sum in 
yable to the estate of I
o be purchased by the T
institution in the amou if she
the benefit of 
Million Dollars ($10 000 000) which
payable to the estate o with a lum sum in the
enefit o 
ion Dollars ($2,000,000), which a
e payable to the estate of
```

#### [25] [EFTA01357837](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357837.pdf) -- Page 0

- **Interest Score:** 84.4
- **Fragments:** 9
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
FY ISE EB1TDA 
Mfllron) FY ISE FCF 74 Million) 
ens le) 
Si I
52
FY 16E EBITDA(S N141144) 
N 
r G. 
11 7$
5221
12 75
53 25
1321
$4 23
14 75 El ICE EC? (S JJlnni 
1175
MI6
52.15
53 8
$3.71
54 25
1175
g
NYMEX Gas (Prricie) 
11 73 
17 77
1277 
5125 
An 
1126 
MTh NYMEX Gas (14cle) 
3117 
$2.75 
53.2$ 
53/5 
$4.21 
14.15
W“11). 04 µ!mere) 
11.75 
5221 
14.75 
$3.23 
UPS 
$425 
$300
732
348
1127
01
302
217
161 NYMEX 
isi
5125 
1
130 0
13 0 o 
12.75 
13.4 
1115 
14.25 
14.75 
$30
$30
130
$30
$30
```

#### [26] [EFTA01684466](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01684466.pdf) -- Page 133

- **Interest Score:** 83.2
- **Fragments:** 5
- **Document Type:** FINANCIAL
- **Dataset:** ds10
- **Names Found:** New York

**Reconstructed Text:**

```
aisal fo 
roperty.
J
2016
Titl
t
d
A urchased b' 
n January 2016. 
report and an Appraisal fo 
$13,000,000.00, dated 07/24/2019. 
y Subpoena fo 
ena to serve o 
d
f
9 E
t 71 t St
t N
Y
k NY 10021
o-
fo 
or 9 E 71st St New York NY 10021
```

#### [27] [EFTA01577747](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01577747.pdf) -- Page 6

- **Interest Score:** 79.7
- **Fragments:** 12
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
400
CA
$30 00
$21 28
$225 00
$35 00
$99 00
$278 40
$111 55
$34.60
$28.52
8939 CA 
200.00
$10.00
$170.14 
1/8/14 
415-4264400 CA $34.57
```

#### [28] [EFTA01577747](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01577747.pdf) -- Page 8

- **Interest Score:** 77.2
- **Fragments:** 17
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
$75.00
511 57
WA
57 67
$28 87
400
$60 33
21
11 1
NY
11 99
11.111. 
Am.,
400
CA $70.00
f25.06
CO
5268 90
2/28/14 
$5,329.11
400 CA $56.64
zon.coWA $244.61
8939 CA $200.00
WA $174.23
3/5/14
```

#### [29] [EFTA01653060](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653060.pdf) -- Page 14

- **Interest Score:** 77.0
- **Fragments:** 13
- **Document Type:** FINANCIAL
- **Dataset:** ds10
- **Names Found:** Andrew, Prince, Wexner, Les

**Reconstructed Text:**

```
oria H
co-c
orge
out in our late n
about how they
the big lawsuit be
made videos &
lawsuit. 
o
famous artist & nned everyt
ne convers3
ing to pro
eslie & Me. 
s to launch t
ed to beco
 that this w
Wbryonvoordon can you find out the grand
total of MONEY that the gdaiNmail paid
throughout the years.
told me that she received
hundreds of thousands for the fake Prince
Andrew photo. Both 
d
h
h D il M ilwoue
guaranteed me that the Daily Mail woue 
pay
t
h
d f k
pay me martens once they created a fake 
i
fL
li W
&
h P
picture of Leslie Wexner & me togetheP
h
I
d
D
idB i
ld
when I was underage, so David Boies cou
L
li f
dli
```

#### [30] [EFTA01577747](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01577747.pdf) -- Page 1

- **Interest Score:** 75.2
- **Fragments:** 13
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
4/23/13 
5501.50 
4/23/13
iiiiiIIIIIIIIII
855
AZ $50 86
4400
CA $48 00
855
AZ
399 71
5/3/13 
gillOigniggi CA 31.00 
5/4/13 
YORK
NY
$17 65
5 4 13 
5/9/13
NY $97.98
TI
M
AR.
4400
CA
$17 80
$15.00
NY $161.94
6/3/13
400
CA
52.92
6/10/13 
6 11 13 
75.00 
5503.20 
6 11 13 
5501.30 
6/15/13
```

#### [31] [EFTA01361658](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01361658.pdf) -- Page 0

- **Interest Score:** 72.8
- **Fragments:** 3
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
Accou
ted Annua nt Value 
5126 714 
l Income
$3 85 $126,714,2
4
```

#### [32] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 404

- **Interest Score:** 72.0
- **Fragments:** 6
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
Cheek: 2278
Amount: $2 474 50
Date: 11:05201 Check: 2263
Amount: 52 535 00
Date: 11 0
Check: 2269 
Amount: 54,415 85 
Date 11.06,2 Check 1116 
Amount $700000 
Date 1
F
Chedc 2262 
Amount $10.600.00 
Date: 1103201 Check 2261 
Amount $30669 
Date: 110920
```

#### [33] [EFTA01365914](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01365914.pdf) -- Page 0

- **Interest Score:** 69.7
- **Fragments:** 3
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
Accou
ted Annua nt Value 
Income 074.47 
$3,280,074.47 
4 '
```

#### [34] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 390

- **Interest Score:** 68.7
- **Fragments:** 6
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
2199
A
t $500 00
D t
1009/20 Ch
k
2213
A
t $787 50
D t
10 09/20
Check
2214
Amount 5900 00
Date 10 C9 20 Check
2215
Amount $1,08000
Date: latoczo
Check
2217 
Amount. $1,100.00 
Date: 1009/201 Check: 2212
Amount $1.200 00 
Date. 1009:20
```

#### [35] [EFTA02730486](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730486.pdf) -- Page 145

- **Interest Score:** 68.4
- **Fragments:** 3
- **Document Type:** FINANCIAL
- **Dataset:** ds1-9_11-12

**Reconstructed Text:**

```
sal for
n 
• 
y 
$13,000,000.00, dated 07/24/2
Di
f C
i
d f
L SJ L
e on 
ents • r 
f
d f
USVI
ti
```

#### [36] [EFTA01720603](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01720603.pdf) -- Page 7

- **Interest Score:** 68.3
- **Fragments:** 8
- **Document Type:** FINANCIAL
- **Dataset:** ds10
- **Names Found:** Les

**Reconstructed Text:**

```
In/Out Bottle, $111081bS Upscale Cent
hi BiAppi oN[y!!
19vo IN/OUT 
XCITEMENT
VA OUS POSITIONS Island Beauty
EEE 
y.iile 
Upscale Service, Female owned 
and operated hiring top model typ( 
males and females. No exp 
seeded For outcalls and travel. To; 
pay. Hiring in the tri county area. 
Only serious, reliable model type 
need apply.Day And night shift 
avail for upscale clientel. 
Call Tia 
private
High class
```

#### [37] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 894

- **Interest Score:** 68.1
- **Fragments:** 6
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
D t
08/10/20 D t
08/10/20
Check: 4939 
Amount $1,36500 
Date 08.1020 Check: 4955 
Amount: $4850.00 
Date: 08/10/201
heck' 4941 
Amount: 52.122.00 
Date: 08/10/201 Check: 4913 
Amount $540.00 
Date: oesin
```

#### [38] [EFTA01378580](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01378580.pdf) -- Page 0

- **Interest Score:** 67.6
- **Fragments:** 3
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
29 41AM
ance Required in solving n KYC Case$10194682S [I]
```

#### [39] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 471

- **Interest Score:** 66.7
- **Fragments:** 6
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
Amount 5700 00
D t
04'08/20 Amount $700 00
D t
040820
Ch
k 2585
Check: 2586 
Amount: 5720.00 
Date: 0408 2 Check 2584 
Amount $92500 
Date 0408 2
Check: 2591 
Amount: 51.036.03 
Date: 04,08/201 Check 2982 
Amount $1,11000 
Date 0408 20
```

#### [40] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 702

- **Interest Score:** 64.6
- **Fragments:** 6
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
Ch
k
3912
A
t $1 080 00
D t
100620 Ch
k
3933
Amour*: $500 00
D t
10106/20
Chect 3918
Amount $400 00
Date 1000 20 Check
3934
Amount $0000
Date 10 06/201
Check 3919 
Amount 5500.00 
Date: 1006/2 heck 3910 
Amount $1,08000 
Date: 10,0
```

#### [41] [EFTA01269520](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01269520.pdf) -- Page 6

- **Interest Score:** 63.9
- **Fragments:** 14
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
Information 
( D
i
)
hi O P
t
hi
O C
ti
O Non Profs O LLP 0 LLC O Other
Authorize
i
d S uth ri r.)
Member
n 
pat -
Type 
tification
3 N vers License
Depositor he
Client Inform of the depositor and that it has reviewed the information oontaned in 
as received and agrees to the Terms and Agreements for Commercial
ype: 
Cash Mgr CM/ 
O Other' 
Amount 'Mai 
• 
If the initial deposit is over $500,000 
Money Order/
please document source of funds or source
t rAein ma 
re 
Il 
' 
FirstBankPR000879
```

#### [42] [EFTA01450739](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01450739.pdf) -- Page 0

- **Interest Score:** 62.5
- **Fragments:** 6
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
YA 
96
Yi ld
d S
d A
l
i
'Nat-, 
I: 
I:: r" 
Price 
DM (bp) 
Viorkout 
05/21/2014 Q 
10
Neutral Price 
Adjusted Price 
to 
Adjusted Simple Margin 
(bp) 
Adjusted Total Margin 
(bp: 
c7read For life 
(bp)  
Floater Information "IlniMill• At i J60 
Price at Refix 
on 05/21/14 
Mmict 
  
ro
Mod Duration 
Risk 
Convexity 
DV In  on 11414 
Invoice 100
?
ts 05/2
0
0.00 Date 
R
, 6.1
/14 
M
 
0.4
 
0.3
0.0054
Benchmark 
EUR006M Assumed Rate 
- 4 
t1 
Quoted Margin 
130.00 Coupon 
1.61900 Principal 
983.200.00 
Next Pay 
05/21/14 Coupon Freq Semi-An... Accrued (26 Days) 
1,169.28 
Index to 
05/21/14 
Refix Iceg 
EOM 
Semi-An... Total (EUR) 
Australia 61 2 v.77 $600 Brazil 5511 3048 4500 Euroszte 44 20 ?330 7500 Cfraany 49 69 9204 1210 Nang Kona $52 2977 6000 
Japan 81 3 3201 8900 
Singapore, 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2013 Blooadoerg Finance L.P. 
SN 622439 CPIT 00+0.00 H465-2561-2 12-04c-2012 15:00t05
```

#### [43] [EFTA01454551](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01454551.pdf) -- Page 0

- **Interest Score:** 62.3
- **Fragments:** 4
- **Document Type:** FINANCIAL
- **Dataset:** ds10
- **Names Found:** Paul

**Reconstructed Text:**

```
ES 
CO ESPIRITO 
BE SPL 
Var 11/23 
94.2460/95.4850 
(8.735/8.374) 
BGN 
010:22
SANTO SA 
:ter-
E39445499 
PTBEQ30)40012 
\a --The: 
BANCO ESPIRITO 
:tc_5try 
Banking 
4acurtty Information 
EFS:: 
BBGOOSMOK D32 
s 
'At 
aro MTN 
Bahr Ratings 
<bu-t, , 
PT 
Rank 
Subordinated 
renzy 
Series 
BJR 
B‘TrN 
82 
5S.= 
B 
ct 
Coupon 
7.125 
T &PR 
Variable 
BEN 
Con Freq Annual 
B. 
Day CM 
ACT/ACT 
I ss Price 
100.00000 Issuance 8 Trading 
Maturity 11/28/2023 
Reoffer 
100 
ant: I Fs.ed/Outst and i r.g 
s 
Pecs: 
CALL 11/28/186100.00 
Iss Sprd 
645.40bp vs OBL 1 10/12/18  
B/R 
 
EUR 
750,000.00 (T.1) / 
750,000.00 (M) 
ost 
Act,c,
Calc Type 
(1469) FD(-TO-VARIABLE BD 
Min Piece/Increment 
ect.ts 
Announcement Date 
11/21/2013 
100,000.0D / 100,000.0) 
ews 
Interest Accri.a. 03TE 
11/28/2013 
Par Amount 
100,000.00 
s 
Date 
11/28/2013 
Book Runner 
BESI,BAML,C, MS 
!•.'t 
..st 
Da:e 
11/28/2014 
Exchange 
Multiple
Paul Moms Nay GtlIttl
07/01/2014 08:22 AM
```

#### [44] [EFTA01357846](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357846.pdf) -- Page 0

- **Interest Score:** 60.8
- **Fragments:** 16
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
FY 15
NIPS, N. 11, Ge, Ilene.' 'th
51103
52300
5 ITDA IS hlillion) 
,
14600
365 00
NM
171 00 FY IS
NBD N3urel Gas (pence l th
12000
$3 E Per FS Million) 
rm) 
03
54300
15400
105 00
S75 0)
Y 16
Nap 1...e.aal 
IF,/ nee i 
11500
1:300
5 ITDA (S Million) 
m) 
14300
16510
10600
$7100 FY 16
10 00
321 00
53 FCF 
1,1 bon) 
00
$4603
10100
MOO
9740)
NOP Nature}Gm IFe rice i the
315 00 
1:30a 
135 g
54500 
36530 
MVO 
57100 NAP Naluisl Gas I pe
$1500 
a erm) 
Sn 
26 600 
MOO 
MOO 
17800
?IRO N owe, Gm (pence(the
115 
1310
?
co 
12500 
133
S rm) 
00 
4300 
1.55() 
165 00 
MOO 
l
Id
07
034 NMI Natural Gan (pe
115 00 
125 .00
536 0
121
321 erm) 
3.0) 
14500 
13400 
IRLOO 
Stia 
21
320
120
$20
120
```

#### [45] [EFTA01459860](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01459860.pdf) -- Page 0

- **Interest Score:** 60.6
- **Fragments:** 17
- **Document Type:** FINANCIAL
- **Dataset:** ds10
- **Names Found:** Les, Edwards, Bradley, Paul, Jay

**Reconstructed Text:**

```
Anna-Sofiya Lupolover 
Elizabeth Payne 
C d L R
D tt Proko Michele-M Qu
Liles 
L sen-Cosby 
; Bradley Anu Barua
; Anh H Parisi ; Terri Sohrab
S l
t
M
Russell D
Susan Burnett 
; Paul Morr oore 
Ma
Dan Gray
Jay Harley 
Margie Edwards 
Lis Dan 
M
nthony Western 
Cath MacGuire 
n 
; Ter
RE: Feb 2016 Return Mail m Banking Money Mark crow and OBAG CD Accounts
```

#### [46] [EFTA01577747](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01577747.pdf) -- Page 0

- **Interest Score:** 59.9
- **Fragments:** 14
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
MENIMONON
347
NJ
1 763 77
7733 CA
$1 125 00
ii
ii
iiiiiill
855
AZ
544 86
P COMGA
75 00
$15 00
CA
$2 075 0
4/18/13 
480-5058855 AZ 5.99
NY 
$139.49
NY $17.50
NY 
$5.71
NY 
8.54
CA 532.00
4/22/13
```

#### [47] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 502

- **Interest Score:** 59.8
- **Fragments:** 5
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
Ch
k 2730
A
t $126 00
D t
06f17/20
Check: 2728 
Amount: 5962.50 
Date. 06'17201 cheek 
lilt, 
Amount §1,020 DU 
Da te u 
4u
Check: 2731 
Amount: $1.060.50 
Date: 06/17/201 Check 2733 
Amount $1,10000 
Date 0&17201
```

#### [48] [EFTA02188376](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02188376.pdf) -- Page 0

- **Interest Score:** 59.5
- **Fragments:** 6
- **Document Type:** FINANCIAL
- **Dataset:** ds10
- **Names Found:** Epstein, Jeffrey, Les

**Reconstructed Text:**

```
F
L
l
G
ff
1 AM EDT
bject The Charles Hot
Number 
Guest Name 
Arrival Date 
Departure Date 
1802350 
Jeffrey Epstein 
June 16, 2011 
June 18, 2011
Cancellation without penalty is required by 4:00 PM EST on 
Tuesday, lune 14, 2011 
Check•in time 
3:00 PM 
Check-out time 
12:00 noon 
Room Tax 
14.45% 
Overnight & Valet $34.00 per day 
Parking 
‘,. 
n 
ACE INFORMATION`':';.
Reservations 
Number 
Concierge Number 
Hotel Website
```

#### [49] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 849

- **Interest Score:** 59.2
- **Fragments:** 5
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
4684
$
heck 4692 
Amount: $1,20060 
Date: 05/18/201 heck 4095 
Amount $1,320.00 
Date 05,18,201
Check: 4883 
Amount: $1.200.00 
Date: 0518 20 Check: 4674 
Amount: 32110.00 
Date: 05/21/
```

#### [50] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 565

- **Interest Score:** 59.2
- **Fragments:** 5
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
11/04/20
Check: 3319 
Amount $I .050 00 
Date 11,04:201 Check 3317 
Amount $1,23200 
Date: 
i0420
Check 3313 
Amount $1.260.00 
Date 11:04:2 Check 3315 
Amount $1.260 00 
Date 1104201
```

#### [51] [EFTA01688396](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01688396.pdf) -- Page 20

- **Interest Score:** 58.1
- **Fragments:** 12
- **Document Type:** FINANCIAL
- **Dataset:** ds10
- **Names Found:** Epstein, Palm Beach

**Reconstructed Text:**

```
s concerning m ages and
l
uring the visit Epstein's
e.
s t e victims corn lied and 
vided the masse es E stein would 
At the conclusion ofthe massages the victims were paid sums of money ranging front $200 $1 00
ful sexual activity he Tow f Palm Beach.
rough a photo line up.
,
an opp
Sunday was a Sunday.
```

#### [52] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 405

- **Interest Score:** 56.8
- **Fragments:** 4
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
Ch
k
2270
A
t $3 127 75
D t
11 09 2 Ch
k 2268
A
t $620 00
D t
11110/20
Amount: $299.70 
Date: Check 2276 
Amount $1,28750 
Date: 11/12:201
```

#### [53] [EFTA02188365](https://www.justice.gov/epstein/files/DataSet%2010/EFTA02188365.pdf) -- Page 0

- **Interest Score:** 56.2
- **Fragments:** 7
- **Document Type:** FINANCIAL
- **Dataset:** ds10
- **Names Found:** Epstein, Jeffrey, Les

**Reconstructed Text:**

```
L
l
G
ff
0 AM EDT
ject: The Charles Ho
Number 
Guest Name 
Arrival Date 
Departure Date 
1602349 
Jeffrey Epstein 
June 16, 2011 
June 18, 2011 
• 
king bed
POLICIES
Cancellation without penalty is required by 4:00 PM EST on 
Tuesday, June 14, 2011 
Check-in time 
3:00 PM 
Check-out time 
12:00 noon 
Room Tax 
14.45% 
Overnight & Valet $34.00 per day 
Parking
Reservations 
Number 
Concierge Number 
Hotel Website 
WWW ChaLlgslapAls_gm
```

#### [54] [EFTA01357847](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357847.pdf) -- Page 0

- **Interest Score:** 55.3
- **Fragments:** 8
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
FY 15E EB1TDA (5 51dhon) 
to 51r* 
$ FY 15E FCF (5 111ilhon1
FY 16E EBI1DA (5 151.11ron) 
NYMEX Gas ($/mele ) 
S11>
57 75
5275
53 25
52
R 25
14 75 FY 15E ;CE (5 1.1i1For 
51 75
1225
12 15
13 25
53 715
1425
51.75 
5225 
$2.75 
53.25 
5175 
14.25 
14.75 11.75 
52.25 
52.75 
53.25 
1175 
1425
14.75
NYMEX Ga (time(*) 
5270 
5825 
9 00
7924
2134
1182
14.75 
80
5 94 V  rmeM Gas 4.-viri 
51.75 
12.25 
12.75 
13.23 
SIJS 
NIS 
54.75 
530 0
$0 7
$07
107
$06
$0 6
soe
$06
```

#### [55] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 925

- **Interest Score:** 55.2
- **Fragments:** 4
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
Check: 5053
Amount $3 130 00
Date 10 03 2 Check
5037
Amount $0312 50
Date: 1002
Check 5073 
Amount $540 00 
Date 1004 20 Check 5086 
Amount $1,20000 
Date: 100520
```

#### [56] [EFTA01357818](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357818.pdf) -- Page 0

- **Interest Score:** 55.2
- **Fragments:** 9
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
FY 15E EBITDA (5 Million) 
1115
$125
12 4
51 25
16 5
5425
1475 FY 151 FCF l5 Mahon] 
7108.17G.77,547sr 
1175
5125
$7 15
$135
LIM
14 15
FY 16E ESITDA(S 
4/4117. On rVeor7) 
51 75
5775
TO
5325
SIM
$42$
14776 FY 16E FCF (S Mil lion) 
5175
11 75
52 75
11 5
535
an
1111
NYMEX Gas 15(mere) 
11.71 
5225 
524 
5125 
5175 
5425 
44.75 NYMEX Gas Itmerol 
51.75 
51.25 
$2.75 
13.25 
5175 
5516 
15. 76
NYMEx On (318171e) 
51 75 
525 
57.5 
13.25 
55.5 
14.25 
1175 
5300
677
67
64
11677
65
441
At NYMEX Oer itorne
11 15 
31.2
530 0
549
54 e) 
1215 
9.5 
1115 
11.15 
14.73 
149
3 9
149
14 9
24 9
```

#### [57] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 758

- **Interest Score:** 55.2
- **Fragments:** 4
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
eck: 4262 
Amount $2,42400 
Date: 12)15/20 $1.000 03 
Date: 12/1520
12/15/20 k
4255
A
t $1030 CO
D t
12/15/201
```

#### [58] [EFTA00026723](https://www.justice.gov/epstein/files/DataSet%208/EFTA00026723.pdf) -- Page 0

- **Interest Score:** 54.6
- **Fragments:** 3
- **Document Type:** FINANCIAL
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Jeffrey, Bill, Wexner, Les

**Reconstructed Text:**

```
om: " 
To:
Thursday July 11 2019 2:5
Subject: CNBC; Jeffrey Epstein used $46 million charitable donation to keep alive his ties with billionaire Les Wexner
```

#### [59] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 965

- **Interest Score:** 54.4
- **Fragments:** 5
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
1653
$
Check
5249
Amount: $1 856 85
Date: 12/11/20 1/2018
Check 5279 
Amount. $2.900.00 
Date: 12/12/2 Check 5285 
Amount $1,05000 
Date 12'12201
```

#### [60] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 500

- **Interest Score:** 54.4
- **Fragments:** 6
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
Check
2711
Amount $1 560 00
Date: 0606/201 Check
2705
Amount 51 760 00
Date 06062016
A
Check
2692
Amount $20,100 00
Date: 0606 201 Check
2690
 
 
Amount $11255 67
Date 06,07:20
Check 2718 
Amount. $1.500.00 
Date: 0608/20 Check: 2698 
Amount: 83.030.00 
Date: 06/08/20
```

#### [61] [EFTA01357823](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01357823.pdf) -- Page 0

- **Interest Score:** 54.2
- **Fragments:** 9
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
FT ISO EFITTDA (5 IIIllhon) 
tenth,. 
(Vnicfe) 
ST 4
17 71
$3 21
00
142$
91 75 El 150 EGO 4.5 
1110
5 75
52 75
S116
14 75
FY ISE EelIDA(S 11101,5n) 
an
tus
/2 75
$24$
13 715
14 10
am FY 16E EGO (S 1.1,150n) 
sirs
an
an
53 n
075
Kn
ass
NYMEX Gar (Stine,/ 
Si 15
75 
51 .4 
1125 
31 
$4.21 
54.75 0.75 
370 
32.75 
1.3.8 
5375 
54.25 
54.75
117 VIE Gn515.1^net) 
51.7>
1323 
1275 
5125 
11176 
1.1.20 
14.75 
$100
ISO*
4 In
3 3
420
469
404
3 14 F/F X CAA I SI,C'
0.75 
130 0
07
5225
107 $2.75 
TO 7
13.8 
306
1175 
10
14.25 
106
075 
SO
```

#### [62] [EFTA01729237](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01729237.pdf) -- Page 0

- **Interest Score:** 54.1
- **Fragments:** 12
- **Document Type:** FINANCIAL
- **Dataset:** ds10
- **Names Found:** Epstein, Palm Beach

**Reconstructed Text:**

```
uring the visit Epstein's
stein would 
s they provided the
sums of money ranging from $200 - $1 0
he Tow Palm Beach
y Epstein through a photo line up.
ed
te v ew,
stated
at 
had o ered her an oppo
Sunday t sure o t was a Sunday.
Det 
whoa personally k
Signature of Police Officer (F.S.S. 1 Date: 05/01/2006
```

#### [63] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 310

- **Interest Score:** 53.9
- **Fragments:** 6
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
Check: 1871
Amount: $350 00
Date: 02 27/2 Amount 51 000 00
Date: 0227/201
Check
1868
Amount: 51080 00
Date 0227 Check
1874
Amount $167500
Date 0227 2
Check 1869 
Amount 52.095.75 
Date: 02/27/20 • 
Check: 1872 
Amount: 52.250.00 
Date: 0227/20
```

#### [64] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 640

- **Interest Score:** 53.6
- **Fragments:** 6
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
Ch
k 3658
A
d $96003
D t
05/05/201 Ch
k 3661
A
t $960 00
D t
0505 2
Ch
k
3657
Amo nt $1 406 00
D t
050520 eck
3662
Amount $1 616 00
Date: 05052
Chedc 3663 
Amount: $600.00 
Date: 0508/20 Check: 3626 
Amount $4.760 50 
Date 0508 20
```

#### [65] [EFTA01670642](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01670642.pdf) -- Page 808

- **Interest Score:** 53.5
- **Fragments:** 6
- **Document Type:** FINANCIAL
- **Dataset:** ds10

**Reconstructed Text:**

```
Ch
k
4508
A
t 51 818 00
Date: 03/09/20 Check 4497
Amount 51 080 CO
Date: oaostensa
Check: 4503
Amount. $108000
Date 03 09 20 Check
4500 
Amount 51.080 CO
Date: 0309/201
Ch
k 4496
A
$1 080 00
D
0309 20 Ch
k 4495
D t
03092018
```

---

### FBI_REPORT (5 pages)

#### [66] [EFTA01652971](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652971.pdf) -- Page 2

- **Interest Score:** 85.9
- **Fragments:** 5
- **Document Type:** FBI_REPORT
- **Dataset:** ds10
- **Names Found:** Les, Virginia, Giuffre, Farmer, Maria, Edwards

**Reconstructed Text:**

```
leclyvictonabrver * 
From Create P., ,de 
Just like I said a few days ago Huw 
Edwards is your guy. I believe Virginia 
giuffre and Maria Farmer are con 
artists and we have the proof. 
I only use credible sources. 
I don't give labels unless there's 
indisputable proof AAA 
Send message 
r. 
Q V
George ite 
Ceorgii forikf. 13m 
 
Lady Victoria communicates with Ghigaine& I 
can only say that there is a lot gcing on behind 
the scenes. el M illt
ey C. It 
don OW vele • menne wenn 
s doe, I don't Worn t Keen for J the sea
The FBI, Department of Justice, Joe Biden & 
the du Pont family. 
George B 
Tonks 
R 1 views • 2 months age 
1: WM 
Ws. rsoLos 010 
0 
V 
71.4%
```

#### [67] [EFTA01652143](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652143.pdf) -- Page 27

- **Interest Score:** 72.0
- **Fragments:** 4
- **Document Type:** FBI_REPORT
- **Dataset:** ds10
- **Names Found:** Farmer, Maria

**Reconstructed Text:**

```
George B. Tonks 
@Geot, 
I want to make it very clear to everyone that I 
have always supported 
. After 
speaking with her, I can honestly say that she 
is focused on exposing the truth & will go out 
of her way as a trained lawyer to thoroughly 
investigate her sources. 
IC) Lucia Osborne-Crowley 
Oh wow thank you so, so much George — I 
can't tell you how much this means to me 
@GeorgeBTonks twitter.com/ 
GeorgeBTonks/s... 
ItC1 
L—J isayvicionahervey• Dm 
From Create Mode , 
I I i 
itMARIAFARMER 
What case were you a 
witness on and what 
governmental agency 
granted you whistleblower 
status. No one can find it. 
If George B. Tonks lied 
about anything the attorneys 
ould have sued him and the 
federal judge would have 
held him if he felt George 
submitted a fraudulent 
document to the court. 
None of that happened...
From Create Mode ) 
Cr 
What case were you a 
witness on and what 
governmental agency 
granted you whistleblower 
status. No one can find it. 
If George B. Tonks lied 
about anything the attorneys 
would have sued him and the 
federal judge would have 
held him if he felt George 
submitted a fraudulent 
document to the court. 
None of that happened... 
;M: Freencr•ate mode 
What case were you a 
witness on and what 
governmental agency 
granted you whistleblower 
status. No one can find it. 
If George B. Tonks lied 
about anything the attorneys 
would have sued him and the 
federal judge would have 
held him if he felt George 
submitted a fraudulent 
document to the court. 
None of that happened...
```

#### [68] [EFTA01731021](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01731021.pdf) -- Page 95

- **Interest Score:** 63.1
- **Fragments:** 4
- **Document Type:** FBI_REPORT
- **Dataset:** ds10
- **Names Found:** Epstein, Maxwell, Ghislaine, Jeffrey

**Reconstructed Text:**

```
(U) Search Warrant Executed a 
(U) Search Warrant Executed a 
(U)Items seized from JEFFREY EPSTEIN duringhis (U)Items seized from JEFFREY EPSTEIN duringhis
(U) Attempted Interview of GHISLAINE MAXWELL (U) On July 7, 2019, FBI S 
(U) Attempted Interview of GHISLAINE MAXWELL (U) On July 7, 2019, FBI S • 
(U) 20190709maxwell docs0751317 pdf
(U) 201907O9maxwell docs075817.pdf
)
) Interivew o 
otes075835.pdf 
 Search Warrant Executed 
) Search Warrant Executed 
) Epstein Search Docs.pdf 
(U) Epstein Search Docs.pdf
(U//FOUO) jarnocan.PNG 
(U//FOUO) j 
PNG
```

#### [69] [EFTA01653379](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01653379.pdf) -- Page 0

- **Interest Score:** 56.3
- **Fragments:** 3
- **Document Type:** FBI_REPORT
- **Dataset:** ds10
- **Names Found:** Maxwell, Ghislaine, New York

**Reconstructed Text:**

```
Executed:10/8/2019 
13:14 
Executed 
by:NYPDFINESTSYRNE941477 
New York City Police 
Department 
FIREARMS - LICENSES AND 
PERMITS
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
ype: RESI
```

#### [70] [EFTA01731021](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01731021.pdf) -- Page 102

- **Interest Score:** 55.2
- **Fragments:** 6
- **Document Type:** FBI_REPORT
- **Dataset:** ds10
- **Names Found:** Epstein, Jeffrey, New York

**Reconstructed Text:**

```
(U) 0S0D-NY-3027571 0000269 1A0000060 000(U)Interview notes
(U
nterview notes141028.pdf
(U
nterview notes141028.pdf
latives141 latives141
(U) Cranston RI police records140826.pdf 
(U) Cranston RI police records140826.pdf
(U) FBI New York - Jeffrey Epstein - Child Sex Traff (U) Case Enhancement; AM #190904-1
```

---

### VICTIM_STATEMENT (42 pages)

#### [71] [EFTA01660651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660651.pdf) -- Page 3

- **Interest Score:** 162.5
- **Fragments:** 5
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Maxwell, Ghislaine, Jeffrey, Clinton, Bill, Trump, Donald, Les, Katie, Alexander, New York

**Reconstructed Text:**

```
W d
d
A
t 6 2025 4 0OPM
S bj
t FW NTOC N
reported an unidentified female friend who was forced to perform 
• . -, • President Trump approximately 35 years ago in NJ. The friend told 
Alexis that she was approximately 13.14 years old when this occurred and the 
friend allegedly bit President Trump while performing oral sex. The friend was 
allegedly hit in the face after she laughed about biting President Trump. The 
friend said she was also abused by Epstein. 
Donald Trump 
Jeffrey Epstein 
ported she has a friend, Leslie McMichael. who was a 
persona ass's an to Epstein in Florida from 1986 until 1991 or 1992. This 
friend shared names of some of the guests at Epstein's parties to include Bill
Jeffrey Epstein 
Jeffrey Epstein's Wife 
Donald Trump
At age 16, while modeling, caller attended 8 parties at Epstein s New York 
residence. On one occasion, caller reported she was sexually assaulted by 
Epstein. On another occasion, two twin brothers, Allen and Oren, lured caller 
and her friend upstairs but they escaped back downstairs. Caller stated Oren 
raped her best friend and a third brother. Tal. raped a 14 year old girl named 
Katie LNU. Caller named other individuals involved in -big orgy parties" with 
her, other young girls, and older Victoria's Secret models, including Bill Clinton 
and Donald Trump. 
Allen. Oren, Tal (LNU. 
possibly identifiable as 
Alexander brothers) 
Epstein's 'British Socialite" 
Bil Clinton 
Donald Trump 
Jeffrey Epstein 
Online complainant reported she was a victim and witness to a sex trafficking 
ring at the Trump Golf Course in Rancho Palos Verdes. CA between 1995- 
1996. Complainant reported Ghislaine Maxwell as the madam and broker for 
sex parties, clients of whom included Epstein. Robin Leach, and Donald 
Trump. Complainant reported participating in orgies and that some girls went 
missing, rumored to have been murdered and buried at the facility. 
Complainant reported being threatened by Trump's then head of security that. 
if she ever talked of what went on there or who she saw, he would 'end up as 
fertilizer for the back nine holes like the other punts.' 
Donald Trump 
Ghislaine Maxwell 
Jeffrey Epstein 
Robin Leach 
Complainant claims to have video of high-profile sex parties, dealings with 
cartels, and having witnessed Robin Leach strangle a young girl to death at a 
party 
Donald Trump 
Jeffrey Epstein 
Ghislaine Maxwell 
Robin Leach 
Sinaloa Cartel 
Claims he was contacted by a female victim of Epstein's who wants to publish 
Bil Clinton
and one was murdered. While working as a limousine driver, complainant 
recalled picking up Donald Trump in 1995 to take him to Dallas Fort Worth 
Airport. During that ride, complainant recalled some of the things Trump spoke 
about on his cell phone were very concerning and described being "a few 
seconds from pulling the limousine over on the median and within a few 
seconds of pulling him out of the car and hurting him due to some of the things 
he was saying." Complainant noted Trump repeatedly stated the name 
'Jeffrey" while on the phone. One of complainant's ex-girlfriend's daughters 
told complainant Trump raped her, as did Epstein. 
Donald Trump 
John W. Nichols 
Bill Clinton 
Hillary Clinton 
Caller is talking about crimes committed against her. She claims to be a 
prisoner. She references Lisa Marie Presley, the British Royal Family, 
Lisa Marie Presley. British 
Royal Family. Donald Trump.
```

#### [72] [EFTA01660679](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660679.pdf) -- Page 3

- **Interest Score:** 159.0
- **Fragments:** 8
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Maxwell, Ghislaine, Jeffrey, Dershowitz, Clinton, Bill, Trump, Donald, Les, Alexander

**Reconstructed Text:**

```
and Eric Trump were there. Attorney Allan 
Dershowitz was also there with Attorney Bob 
Shapiro. We were taken in rooms. forced to give oral 
sex to Donald J Trump. Forced to allow them to 
penetrate us. I was 13 years old when Donald J 
Trump raped me. Ghislaine Maxwell was also 
present.
Wednesday August 6 20258:12 PM
Wediwul
‘VM43
ust
PM
ubject: RE: NTOCNames
Wednesday, August 6,2025 4:00 PM
iecr-rw. mot. mimes
p
p
President Trump approximately 35 years ago in NJ. The friend told 
Alexis that she was approximately 13.14 years old when this occurred and the 
friend allegedly bit President Trump while performing oral sex. The friend was 
allegedly hit in the face after she laughed about biting President Trump. The 
f ' 
s also abused by Epstein. 
p
Jeffrey Epstein 
reported she has a friendn
 who was a 
persona assistant to Epstein in Florida fro 
r 1992. This 
friend shared names of some of the guests at Epstein's parties. to include Bill 
Jeffrey Epstein 
Jeffrey Epstein's Wife 
Donald Trump
residence. On one occasion, caller reported she was sexually assaulted by 
Epstein. On another occasion, two twin brothers. Allen and Oren. lured caller 
and her friend upstairs but they escaped back downstairs. Caller stated Oren 
ra 
her best friend and a third brother, Tal. raped a 14 year old gid named 
Ile( named other individuals involved in 'big orgy parties" with 
her, other young girls. and older Victoria's Secret models, including Bill Clinton 
and Donald Trump. 
possibly identifiable as 
Alexander brothers) 
Epstein's "British Socialite" 
Bil Clinton 
Donald Trump 
Jeffrey Epstein 
Online complainant reported she was a victim and witness to a sex trafficking 
ring at the Trump Golf Course in Rancho Palos Verdes, CA between 1995- 
1996. Complainant reported Ghislaine Maxwell as the madam and broker for 
sex parties, clients of whom included Epstein. Robin Leach, and Donald 
Trump. Complainant reported participating in orgies and that some girls went 
missing, rumored to have been murdered and buried at the facility. 
Complainant reported being threatened by Trump's then head of security that. 
if she ever talked of what went on there or who she saw, he would 'end up as 
fertilizer for the back nine holes like the other cunts." 
Donald Trump 
Ghislaine Maxwell 
Jeffrey Epstein 
Robin Leach 
Complainant claims to have video of high-profile sex parties, dealings with 
cartels, and having witnessed Robin Leach strangle a young girl to death at a 
party 
Donald Trump 
Jeffrey Epstein 
Ghislaine Maxwell 
Robin Leach 
Sinaloa Cartel 
Claims he was contacted by a female victim of Epstein's who wants to publish 
a book. Complainant provided background for himself, such as working with
Bil Clinton 
Donald Trump
```

#### [73] [EFTA01660679](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660679.pdf) -- Page 4

- **Interest Score:** 151.5
- **Fragments:** 3
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Maxwell, Ghislaine, Jeffrey, Clinton, Bill, Trump, Donald, Andrew, Les, New York

**Reconstructed Text:**

```
Ghi l i
Complainant reported his ex-girlfriend' 
re victims of Epstein's 
and one was murdered. While workin 
e driver, complainant 
recalled picking up Donald Trump in 1995 to take him to Dallas Fort Worth 
Airport. During that ride. complainant recalled some of the things Trump spoke 
about on his cell phone were very concerning and described being "a few 
seconds from pulling the limousine over on the median and within a few 
seconds of pulling him out of the car and hurting him due to some of the things 
he was saying." Complainant noted Trump repeatedly stated th 
'Jeffrey" while on the phone. One of complainant's ex-girlfriendilii. 
told complainant Trump raped her, as did Epstein. 
Ghislaine Maxwell 
Donald Trump 
John W. Nichols 
Bill Clinton 
Hillary Clinton 
Cheryl Rene Duke
Caller is talking about crimes committed against her. She claims to be a 
prisoner. She references Lisa Marie Presley, the British Royal Family, 
President Trump, and Jeffrey Epstein. 
Lisa Marie Presley. British 
Royal Family, Donald Trump. 
Jeffrey Epstein 
Complainant reported her neighbor sought modeling gigs at the Trump
Jeffrey Epstein
p
g p
g
g
p
tip, reporting that she was forced to perform sex acts when she was 13 years 
old and pregnant in 1984. Complainant also reported there were high profile 
individuals involved in her sex trafficking and the murder and disposal of her 
newborn daughter. Complainant reported Donald Trump participated regularly 
in paying money to force her to perform sex acts with him and alleged Trump 
was present when her uncle murdered her newborn child. 
p
Jeffrey Epstein 
Caller was taken by boat to Epstein's Island. Caller said it was complicated 
and involved Jeffery Epstein and Ghislaine Maxwell. Caller became a school 
counselor and had a meeting with the school principal, Linda Kitts, and a 
police officer where the caller was informed there were pictures of herself with 
Epstein. Caller reported the school was mad at her for not being a Trump 
person and that the school wanted her to testify and say things against Andrew 
Cuomo. The FBI and Donald Trump were on the phone during the meeting. 
Caller believes the FBI has baby pictures of her with Epstein. 
Jeffrey Epstein. Ghislaine 
Maxwell, Linda Kitts, Donald 
Trump. Andrew Cuomo 
Caller reported that in 1987 a friend (Victim 1) was out drinking and ended up 
at Trump Plaza. Victim 1 saw Donald Trump and wanted to meet him. A 
unknown man approached her and offered to introduce her to Trump. The 
unknown man gave Victim 1 a drink and Victim 1 woke up naked and sore with 
$300 on the bed. Victim 1 didn't remember how she got to the room. She 
remembered seeing 'a flash' of Trump's face. Victim 1 called the Caller and 
told her she thought she had been raped. Victim 1 did not go to a hospital to 
have a rape kit performed because she didn't think anyone would believe her 
especially because she was drunk. Victim Vs husband's business had 
problems with suppliers and Victim 1 believed Trump was behind it. Victim 1 
also started dating a lawyer, identifier's unknown, who was married. Victim 1 
had a fight with her lawyer boyfriend and went to a bar. Victim 1 left a bar with 
a man who no one in the bar recognized but who seemed familiar with Victim 
1. Victim 1 was never seen again. A few years ago, remains were discovered 
that matched the description of what Victim 1 was wearing when she went 
missing. DNA tests at the time were inconclusive. 
Two unknown males; Donald 
Trump 
In 2004 or 2005, Sir Ivan Wilzig, hosted a party where Jeffrey Epstein, Sammy 
Sosa. and Donald Trump were in attendance. Patti LaBelle's PR agent stood at 
the door. At the patty. caller met an individual who was approximately 18 to 23 
years of age, who was brought from Oklahoma for a modeling job but then 
sold to a man in France. Several women were being auctioned, and a woman 
possibly known as Colette LNU was the madam. A couple of years later, caller 
saw Colette at the Cheetah Club in New York, NY, and she told one of Santos 
friends that Jamie Foxx was interested in spending a night with her, and that 
he could pay her a lot money. 
Sir Ivan Wilzig 
Jeffrey Epstein 
Sammy Sosa 
Patti LaBelle 
Donald Trump 
Jamie Foxx 
Donald Trump, the president, had parties at Maralago called "calendar girls' 
Jeffrey Epstein would bring the children in and trump would auction them 
Jeffrey Epstein. Elon Musk. 
Donald Trump, Donald Trump
```

#### [74] [EFTA01660651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660651.pdf) -- Page 4

- **Interest Score:** 147.0
- **Fragments:** 4
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Maxwell, Ghislaine, Jeffrey, Dershowitz, Trump, Donald, Andrew, Les, New York

**Reconstructed Text:**

```
President Trump, and Jeffrey Epstein. 
Jeffrey Epstein
Complainant following up after a call with NYPD officer regarding her previous 
tip, reporting that she was forced to perform sex acts when she was 13 years 
old and pregnant in 1984. Complainant also reported there were high profile 
individuals involved in her sex trafficking and the murder and disposal of her 
newborn daughter. Complainant reported Donald Trump participated regularly 
in paying money to force her to perfomi sex acts with him and alleged Trump 
was present when her uncle murdered her newborn child. 
Donald Trump 
Jeffrey Epstein 
Caller was taken by boat to Epstein's Island. Caller said it was complicated 
and involved Jeffery Epstein and Ghislaine Maxwell. Caller became a school 
counselor and had a meeting with the school principal, Linda Kitts, and a 
police officer where the caller was informed there were pictures of herself with 
Epstein. Caller reported the school was mad at her for not being a Trump 
person and that the school wanted her to testify and say things against Andrew 
Cuomo. The FBI and Donald Trump were on the phone during the meeting. 
Caller believes the FBI has baby pictures of her with Epstein. 
Jeffrey Epstein, Ghislaine 
Maxwell. Linda Kitts. Donald 
Trump, Andrew Cuomo 
Caller reported that in 1987 a friend (Victim 1) was out drinking and ended up 
at Trump Plaza. Victim 1 saw Donald Trump and wanted to meet him. A 
unknown man approached her and offered to introduce her to Trump. The 
unknown man gave Victim 1 a drink and Victim  1 woke up naked and sore with 
$300 on the bed. Victim 1 didn't remember how she got to the room. She 
remembered seeing 'a flash' of Trump's face. Victim 1 called the Caller and 
told her she thought she had been raped. Victim 1 did not go to a hospital to 
have a rape kit performed because she didn't think anyone would believe her 
especially because she was drunk. Victim 1's husbands business had 
problems with suppliers and Victim 1 believed Trump was behind it. Victim 1 
also started dating a lawyer, identifier's unknown, who was married. Victim 1 
had a fight with her lawyer boyfriend and went to a bar. Victim 1 left a bar with 
a man who no one in the bar recognized but who seemed familiar with Victim 
1. Victim 1 was never seen again. A few years ago. remains were discovered 
that matched the description of what Victim 1 was wearing when she went 
missing. DNA tests at the time were inconclusive. 
Two unknown males; Donald 
Trump 
In 2004 or 2005, Sir Ivan Wilzig, hosted a party where Jeffrey Epstein, Sammy 
Sosa, and Donald Trump were in attendance. Patti LaBelle's PR agent stood at 
the door. At the party. caller met an individual who was approximately 18 to 23 
years of age, who was brought from Oklahoma for a modeling job but then 
Sold to a man in France. Several women were being auctioned, and a woman 
possibly known as Colette LNU was the madam. A couple of years lat 
saw Colette at the Cheetah Club in New York. NY, and she told one o 
friends that Jamie Foxx was interested in spending a night with her, an 
at 
he could pay her a lot money. 
Sir Ivan Wilzig 
Jeffrey Epstein 
Sammy Sosa 
Patti LaBelle 
Donald Trump 
Jamie Foxx 
Donald Trump, the president, had parties at Maralago called "calendar girls' 
Jeffrey Epstein would bring the children in and trump would auction them 
off.He measured the children's vulva and vaginas by entering a finger and 
rated the children on tightness. The guests were elder men and included Elon 
Musk. Don jr. Trump, Ivanka Trump. and Eric Trump were there. Attorney Allan 
Dershowitz was also there with Attorney Bob Shapiro. We were taken in 
rooms, forced to give oral sex to Donald J Trump. Forced to allow them to 
penitrate us. I was 13 years old when Donald J Trump raped me. Ghislaine 
Maxwell was also present. 
Jeffrey Epstein, Elon Musk, 
Donald Trump, Donald Trump 
Jr., Ivanka Trump, Eric 
Trump. Allan Dershowitz, Bob 
Shapiro, Ghislaine Maxwell
y,
g
,
t. We ne5 ay, August , 
. .
```

#### [75] [EFTA01660679](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660679.pdf) -- Page 0

- **Interest Score:** 142.5
- **Fragments:** 5
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Maxwell, Ghislaine, Clinton, Bill, Trump, Donald, New York

**Reconstructed Text:**

```
Thursda
7 202S 11:48AM
Thursday, August 7, 202511:41:01 AM
bject: RE: NTOC Names
eported an unidentified female friend 
who was forced to perform oral sex on President 
Trump approximately 35 years ago in NJ. The friend 
told Alexis that she was approximately 1314 years 
old when this occurred, and the friend allegedly bit 
President Trump while performing oral sex. The 
friend was allegedly hit in the face after she laughed 
about biting President Trump. The friend said she 
was also abused by Epstein. 
S oke with caller who identified 
s friend. Lead was 
sect o as ington Office to conduct 
interview. 
sported she has a friend, 
. w 
was a personal assistant to Epstein 
IIIII. 
rom 1986 until 1991 or 1992. This friend 
shared names of some of the guests at Epstein's 
parties, to include Bill Clinton and Donald Trump. 
2 voicemails left, no response 
received.
at Epstein's New York residence. On one occasion, 
caller reported she was sexually assaulted by 
Epstein. On another occasion, two twin brothers, 
Allen and Oren, lured caller and her friend upstairs 
but they escaped back downstairs. Caller stated 
Oren raped her best friend and a third brother, Tal, 
raped a 14 year old girl named 
Caller 
named other individuals involved in "big orgy 
parties' with her, other young girls, and older 
Victoria's Secret models, including Bill Clinton and 
Donald Trump. 
Online complainant reported she was a victim and 
witness to a sex trafficking ring at the Trump Golf 
Course in Rancho Palos Verdes, CA between 1995- 
1996. Complainant reported Ghislaine Maxwell as 
the madam and broker for sex parties, clients of 
whom included Epstein. Robin Leach, and Donald 
Complainant was spoken to and 
deemed not credible. Additional 
research showed 3 se• . rate
```

#### [76] [EFTA01660651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660651.pdf) -- Page 2

- **Interest Score:** 138.5
- **Fragments:** 3
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Maxwell, Ghislaine, Jeffrey, Dershowitz, Trump, Donald, Andrew, New York

**Reconstructed Text:**

```
with Epstein. Caller reported the school was mad at 
her for not being a Trump person and that the school 
wanted her to testify and say things against Andrew 
Cuomo. The FBI and Donald Trump were on the 
phone during the meeting. Caller believes the FBI 
has baby pictures of her with Epstein. 
ell 
Caller reported that in 1987 a friend (Victim 1) was 
out drinking and ended up at Trump Plaza. Victim 1 
saw Donald Trump and wanted to meet him. A 
unknown man approached her and offered to 
introduce her to Trump. The unknown man gave 
Victim 1 a drink and Victim 1 woke up naked and 
sore with 5300 on the bed. Victim 1 didn't remember 
how she got to the room. She remembered seeing 
'a flash' of Trump's face. Victim 1 called the Caller 
and told her she thought she had been raped. Victim 
1 did not go to a hospital to have a rape kit 
performed because she didn't think anyone would 
believe her especially because she was drunk. 
Victim l's husband's business had problems with 
suppliers and Victim 1 believed Trump was behind it. 
Victim 1 also started dating a lawyer, identifier's 
unknown, who was married. Victim 1 had a fight with 
her lawyer boyfriend and went to a bar. Victim 1 left 
a bar with a man who no one in the bar recognized 
but who seemed familiar with Victim 1. Victim 1 was 
never seen again. A few years ago, remains were 
discovered that matched the description of what 
Victim 1 was wearing when she went missing. DNA 
tests at the time were inconclusive. 
contact made, victim identified is 
deceased and complainant did not 
have confirmed information
Possible order of protection matching the 
name and DOB. 
Results matching name 
and DOB for criminal history in New
No 
Jersey: 
Date of Arrest8/2/1986 for shoplifting: 
4/14/1989 for shoplifting: 5/21/1992 for 
shoplifting; 6/28/1993 for shoplifting; 
4/22/1996 for violate domestic 
violence/harassment; 9/16/2021 for shoplifting 
In 2004 or 2005, Sir Ivan Wilzig, hosted a party 
where Jeffrey Epstein, Sammy Sosa, and Donald 
Trump were in attendance. Patti LaBelle's PR agent 
stood at the door. At the party, caller met an 
individual who was approximately 18 to 23 years of 
age, who was brought from Oklahoma for a 
modeling job but then sold to a man in France. 
Several women were being auctioned. and a woman 
possibly known as Colette LNU was the madam. A 
couple of years later, caller saw Colette at the 
Cheetah Club in New York, NY. and she told one of 
Santos friends that Jamie Foxx was interested in 
spending a night with her, and that he could pay her 
a lot money. 
Phone number provided was bad. 
could not identify a valid number 
None 
Donald Trump, the president, had parties at 
Maralago called *calendar girls' Jeffrey Epstein 
would bring the children in and trump would auction 
them off. He measured the children's vulva and 
vaginas by entering a finger and rated the children 
on tightness. The guests were elder men and 
included Elon Musk. Don jr. Trump. Ivanka Trump, 
and Eric Trump were there. Attorney Allan 
Dershowitz was also there with Attorney Bob 
Shapiro. We were taken in rooms. forced to give oral 
sex to Donald J Trump. Forced to allow them to 
penetrate us. I was 13 years old wren Donald J 
Trump raped me. Ghislaine Maxwell was also 
present 
No contact information provided 
no DOB
t: Wednesday, August 6, 20258:12 PM
ednesday, August 6, 2025 4:49 PM
```

#### [77] [EFTA01656152](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656152.pdf) -- Page 14

- **Interest Score:** 124.8
- **Fragments:** 3
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Maxwell

**Reconstructed Text:**

```
MAXW
TRI
• 
Trial - 11/29/2021 - 12/29/2021 
Charges: 
• 
Count 1- Conspiracy to Entice Minors to Travel to Engage in Illega
• 
Count 2- Enticement of a Minor to Travel to Engage in Illegal Sex A
• 
Count 3- Conspiracy to transport Minors with Intent to Engage in C
• 
Count 4 -Transportation of a Minor with Intent to Engage in Crimin
• 
Count 5- Sex Trafficking Conspiracy - Guilty ( December 29,2021)
• 
Count 6- Sex Trafficking of a Minor — Guilty ( December 29,2021) 
• 2 Perjury charges were intended to be litig
pursue after initial trial. 
• The defense presented focused on discred
recall activities from decades prior, and aim
circumstances and Epstein's scapegoat. Cl
was unaware of abuse due to secrets kept b
• 6/28/2022 Sentencing - 20 years in prison
fine. WE
IA
Sex A
ts - N
imina
 Sexu
ated
ting
med
im
y E
with ELL 
L 
cts - Guilty ( December 29,2021) 
ot Guilty ( December 29,2021) 
Sexual Activity- Guilty ( December 29,2021) 
al Activity - Guilty ( December 29,2021) 
d at a later time, SDNY chose not to 
g witnesses, questioning their ability to 
to portray Maxwell as a victim of 
ed Maxwell was targeted by Epstein and 
pstein. 
h 5 years supervised release and $750,000 
15 
EFTA01656166
```

#### [78] [EFTA01656173](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01656173.pdf) -- Page 14

- **Interest Score:** 124.7
- **Fragments:** 3
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Maxwell

**Reconstructed Text:**

```
MAXW
TRI
• 
Trial - 11/29/2021 - 12/29/2021 
Charges: 
• 
Count 1- Conspiracy to Entice Minors to Travel to Engage in Illega
• 
Count 2- Enticement of a Minor to Travel to Engage in Illegal Sex A
• 
Count 3- Conspiracy to transport Minors with Intent to Engage in C
• 
Count 4 -Transportation of a Minor with Intent to Engage in Crimin
• 
Count 5- Sex Trafficking Conspiracy - Guilty ( December 29,2021)
• 
Count 6- Sex Trafficking of a Minor — Guilty ( December 29,2021) 
• 2 Perjury charges were intended to be litig
pursue after initial trial. 
• The defense presented focused on discred
recall activities from decades prior, and aim
circumstances and Epstein's scapegoat. Cl
was unaware of abuse due to secrets kept b
• 6/28/2022 Sentencing - 20 years in prison
fine. WE
IA
Sex A
ts - N
imina
 Sexu
ated
ting
med
im
y E
with ELL 
L 
cts - Guilty ( December 29,2021) 
ot Guilty ( December 29,2021) 
Sexual Activity- Guilty ( December 29,2021) 
al Activity - Guilty ( December 29,2021) 
d at a later time, SDNY chose not to 
g witnesses, questioning their ability to 
to portray Maxwell as a victim of 
ed Maxwell was targeted by Epstein and 
pstein. 
h 5 years supervised release and $750,000 
EFTA01656187
```

#### [79] [EFTA01652016](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652016.pdf) -- Page 2

- **Interest Score:** 97.9
- **Fragments:** 3
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Wexner, Les

**Reconstructed Text:**

```
ladyvictoriaheryey e 20 
From Create Mode 
X 
I don't think I'm the only one who is so 
sick of these pretenders . They a ri 
mostly paid escorts and rent boyr,
extorting money. It's just about 
money. 
Watch gsoundoffreedommovie 
If you have not yet seen it. 
This is REAL trafficking and shows 
what a joke these con artists really 
are. Also the media is responsible for 0 
using the word 'trafficking' so loosely ° 
in order to dramatize the story of the • 
epstein fake survivors. 
5INtotolog 
George B. Tooke 
RENT GIRLS 3 BOYS LIVING THE KC- . 
LIFE IS NOT SEX TRAFFICKING! 
9 
2 
4 ladyvictoriahervey O 33m 
Dole & Korn Phara Oh'
X 
, it's not too late for you to 
come forward to the authorities and 
save yourself. The FBI has all the 
evidence of the fraud. It will be a long 
jail sentence. Think about it. Please 
feel free to reach out. 
b e, George Ist. Ionics a 
^t,eorg. 
BREAKING 
3d ••• 
I.
so t. George B. Tonks 0 @GeorgeBTonks • 26m 
There is nothing wrong with me for forgiving 
Leslie Wexner. I have moved on from what 
happened over 40 years ago.
```

#### [80] [EFTA01652016](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652016.pdf) -- Page 8

- **Interest Score:** 93.1
- **Fragments:** 4
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Maxwell, Ghislaine

**Reconstructed Text:**

```
g
Top 
Latest 
People 
Photos 
Videos 
fie
George B. Tont; 
• 
After talking with award-winning journalist &
fie writer 
for over an hour on Sunday, I 
know that she sincerely cares about victims of 
rape. I encourage everyone to preorder her 
book about 
& support her 
future projects. 
fer Lucia Osborne-Crowley 
I have a book coming out in 2023 and it 
means everything to me. It's about the 
eGhislaineMaxwell trial, but it's mostly 
about the Maxwell & Epstein victims who 
trusted me with their stories & their hearts. 
There'll be a preorder link soon & your 
support would mean the world to me 
air 
CeN
Toitte Geocg
ria communicates
ay that there is a lo
. JD it 
one 
aspects= mops in
oamy bib au lot
rasfehis PT Inane P
nts stilsciva Cm e
for big ttewaxlerf
emand milk. do
y • How GM ww or. 
door I doll Show *. 
s George B. 
GeorgeBW 
Everyone must follow my OnlyFans page. 
People need to realize that the content on 
OnlyFans is not all sexual. When everyone was 
being suspended from Twitter a lot of people 
opened up OnlyFans accounts to get their 
information out. All my free content has always 
focused on corruption. 
onlyfan 
-gebtonks 
5:17 PM • 8/19/23 from Earth • 34 views 
CI 
V
```

#### [81] [EFTA01652431](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652431.pdf) -- Page 6

- **Interest Score:** 91.4
- **Fragments:** 5
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Jeffrey, Edwards, New York

**Reconstructed Text:**

```
Empowering. 
Compassionate. 
Trustworthy. 
•--nr• 
' ,gib°n hIm dridatod a proncing 
[WOES We' me Non magi god te•R*1 ant a 
Ps to
 tag m gott, sutolinhalpositrn dun?* 
rot the connect gas 
We w 0.4• 3 °gam end mgmisrced bkl 
moms. Who Na intsilintif posed as Innunt 
earn some oleo ro il poorolul Inetriduel 
cramons and ism litalnegel On Inns/ ot peon*. 
rg tont end ;ma bonaninsin. bit tact. Po swing 
n 
mama fates wring the corn. Ortlentnhe n 
genet, and at can int 00 toper-mai pin 
resoncot to Mn Ow ammo Ing Ore recent tin 
resin genii gm mengews 
'INFACT WE SPECIALIZE IN HANDLING CASES EDWARDS HENDERSON 
V 
CRIME VICTIM 
COME AS A VICTIM, 
LEAVE AS A SURVIVOR. 
Gut roue ve 
Sent frommyintone
EDWARDS HENDERSON 
if 
CRIME VICTIM 
• 
FEATURED ON 
Netflix 
Jeffrey Epstein: Filthy Rich 
ABC 20/20 
Truth & Lies: The Jeffrey Epstein 
Story 
Lifetin,
Surviving Jeffrey 
the 
Nett; Bark 
CCitn C5 
NI eft, represente
ey Epstein, inc
him and anoth
, in a news con
tty Image survivors of 
who 
m er o er egal team, 
 in New York City in 2019.
```

#### [82] [EFTA01652061](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652061.pdf) -- Page 35

- **Interest Score:** 80.1
- **Fragments:** 4
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Maxwell, Ghislaine, Jeffrey

**Reconstructed Text:**

```
ng= 
ibl i
Top 
Latest 
People 
Photos 
Videos 
George B. TOMS 
-GeorgeBTo • • 1/18/23 ••• 
After talking with award-winning journalist & 
it
f
h
S
d
I
y
know that she sincerely cares about victims of 
rape. I encourage everyone to preorder her 
book about 
=ism. 
& support her 
future projects. 
Lucia Osborne-Crowley • 12/31/22 
I have a book coming out in 2023 and it 
means everything to me. It's about the 
aGhislaineMaxwell trial, but it's mostly 
about the Maxwell & Epstein victims who 
trusted me with their stories & their hearts. 
There'll be a preorder link soon & your 
support would mean the world to me 
717
BREAKIN
Jeffrey Epstein accu
says she hasju
live atter getting hit b
ea fr -
 Pap
•
```

#### [83] [EFTA01660679](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660679.pdf) -- Page 5

- **Interest Score:** 79.8
- **Fragments:** 4
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Maxwell, Ghislaine, Dershowitz, Trump, Donald

**Reconstructed Text:**

```
off.He measured the children's vulva and vaginas by entering a finger and 
rated the children on tightness. The guests were elder men and included Elon 
Musk. Don jr. Trump, Ivanka Trump. and Eric Trump were there. Attorney Allan 
Dershowitz was also there with Attorney Bob Shapiro. We were taken in 
rooms, forced to give oral sex to Donald J Trump. Forced to allow them to 
penitrate us. I was 13 years old when Donald J Trump raped me. Ghislaine 
Maxwell was also present. 
Jr., Ivanka Trump, Eric 
Trump. Allan Dershowitz. Bob 
Shapiro, Ghislaine Maxwell
Wednesday, August 6,2025 1:48PM
Lreaneaaay. AuguSI 
4Liza we.
bject: NTOC Names
```

#### [84] [EFTA01652864](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652864.pdf) -- Page 11

- **Interest Score:** 78.3
- **Fragments:** 7
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Jeffrey, Les, Edwards, Bradley

**Reconstructed Text:**

```
:DWARDS HENDERSON 
CRIME Willa 
V 
111M1 
Authors Of 
Relentless Pursuit
Relentless Pursuit 
The Firm who has Fought for Survivors of Jeffrey 
Epstein since 2008 
In June 2008. Florida based victims' rights attorney 
Bradley J. Edwards was lhirty.two years old and 
had just started his own 
firm when a young 
woman named 
came to see him. 
afi fivriE
PS...1s it IRONY that Bedw s dedicated a chapter
DWARDS HENDERSON
of 
CRIME VirTIM 
Advocates for 
victims.
Brad Edwards 
Partner 
OUR TEAM
```

#### [85] [EFTA01651658](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01651658.pdf) -- Page 1

- **Interest Score:** 78.2
- **Fragments:** 7
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Jeffrey, Edwards, Bradley

**Reconstructed Text:**

```
Breakout Session I 10:10 am — 10:50 am 
Assessment and Intervention of 
Post-Traumatic Stress Disorder 
Daniel Sullivan, MA, MSW & Stephanie Grimaldi, MA, 
MSW Clinical Psychology Doctoral Students 
The Phobia and Trauma Clinic at Hofstra University's Joan 
and Arnold Saltzman Community Services Center
Breakout Session II 11:10 am - 12:00 pm
The Intersection of Trauma, Addiction, 
and Eating Disorders
Breakout Session III 12:10 pm - 1:00 pm 
An Overview of Sex Crimes and Consent 
Eric Aboulafia & Melissa Grier, I Assistant District Attorneys 
The Suffolk County District Attorney's Office
Breakout Session IV 1:10 pm - 2:00 pm 
Civil Litigation of Sexual Abuse Claims —
Jeffrey Epstein 
Bradley J. Edwards, Esq. I Founding Partner at Edwards 
Pottinger LLC & 
Brittany Henderson, Esq. I Partner at Edwards Pottinger LLC 
Thi
k h
ill
h J ff
E
i
l i
i il
di
il bl
i
f
l b
d h
ffi ki
i
b
h
d f d
l
24/7 Crisis Hotlines:
t Victims Unit
```

#### [86] [EFTA00030006](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030006.pdf) -- Page 1

- **Interest Score:** 76.3
- **Fragments:** 7
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Maxwell, Ghislaine, Palm Beach, New York

**Reconstructed Text:**

```
U.S. v. Ghislaine Maxwell 
Properties Owned by Epstein Where Alleged 
Grooming and/or Abuse of Minor Victims Occurred:
New Yo ork, New York 
Palm Beach , Florida 
S nta Fe, Ne w Mexic o 
EFTA
```

#### [87] [EFTA00030009](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030009.pdf) -- Page 1

- **Interest Score:** 76.3
- **Fragments:** 7
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Maxwell, Ghislaine, Palm Beach, New York

**Reconstructed Text:**

```
U.S. v. Ghislaine Maxwell 
Properties Owned by Epstein Where Alleged 
Grooming and/or Abuse of Minor Victims Occurred:
New Yo ork, New York 
Palm Beach , Florida 
S nta Fe, Ne w Mexic o 
EFTA
```

#### [88] [EFTA00030812](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030812.pdf) -- Page 1

- **Interest Score:** 76.3
- **Fragments:** 7
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Maxwell, Ghislaine, Palm Beach, New York

**Reconstructed Text:**

```
U.S. v. Ghislaine Maxwell 
Properties Owned by Epstein Where Alleged 
Grooming and/or Abuse of Minor Victims Occurred:
New Yo ork, New York 
Palm Beach , Florida 
S nta Fe, Ne w Mexic o 
EFTA
```

#### [89] [EFTA00031903](https://www.justice.gov/epstein/files/DataSet%208/EFTA00031903.pdf) -- Page 1

- **Interest Score:** 76.3
- **Fragments:** 7
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Maxwell, Ghislaine, Palm Beach, New York

**Reconstructed Text:**

```
U.S. v. Ghislaine Maxwell 
Properties Owned by Epstein Where Alleged 
Grooming and/or Abuse of Minor Victims Occurred:
New Yo ork, New York 
Palm Beach , Florida 
S nta Fe, Ne w Mexic o 
EFTA
```

#### [90] [EFTA01652143](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652143.pdf) -- Page 23

- **Interest Score:** 70.5
- **Fragments:** 4
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Les

**Reconstructed Text:**

```
Lammed Albertus #ElonMuskl
0 
4 
q
•- • 1.day:teed...el. • . 
meta 
X 
Just like I said a few days ago Huw 
Fde. ards is your guy. I believe 
and 
i 
are con 
artists and we have the proof. 
I only use credible sources. 
I don't give labels unless there's 
indisputable proof A A A 
,c, 
-LadyVictoriaHervey 
41) 
3 ladyyittoriahervey e 
From Create Mode
X 
I don't think I'm the only one who is so 
sick of these pretenders . They are 
mostly paid escorts and rent boys 
extorting money. It's just about 
money. 
(4.1)
Watch @soundoffreedommovie 
< 
If you have not yet seen it. 
This is REAL trafficking and shows 
what a joke these con artists really 
9
are. Also the media is responsible for 
using the word 'trafficking' so loosely 
in order to dramatize the story of the 
epstein fake survivors. 
IThotolog 
George B. Tooke 2d act, 
RENT GIRLS & BOYS LIVING THE HIGH 
LIFE IS NOT SEX TRAFFICKING! 
• 0 
U 
2 
0*
Snare
```

#### [91] [EFTA01652337](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652337.pdf) -- Page 64

- **Interest Score:** 69.6
- **Fragments:** 5
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Maxwell, Ghislaine

**Reconstructed Text:**

```
;
Top 
Latest 
People 
Photos 
Videos 
George B Teaks 0
c
•
I:
• IF
After talkin award-winning journalist &
writer 
for over an hour on Sunday. I 
know that she sincerely cares about victims of
rape. I encourage everyone to preorder her 
book about 
1I & support her 
future project,. 
Lucia Osborne-Crowley • 12:31/22 
I have a book coming out in 2023 and it 
means everything to me. It's about the 
#GhislaineMaxwelt trial, but its mostly 
about the Maxwell & Epstein victims who 
trusted me with their stories & their hearts. 
There'll be a preorder link soon & your 
support would mean the world to me
```

#### [92] [EFTA01652846](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652846.pdf) -- Page 10

- **Interest Score:** 69.4
- **Fragments:** 5
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Jeffrey, Les, Edwards, Bradley

**Reconstructed Text:**

```
DWARDS HENDERSON 
CRIME VICTIM 
Authors Of 
Relentless Pursuit
The Firm who has Fought for Survivors of Jeffrey 
Epstein since 2008 
In June 2008, Floridataased victims' rights attorney 
Bradley J Edwards was thirtytwo years old and
nao past stoned his own 
twin when a young 
woman named 
came to see huh.
PS...Is it IRONY that Bedw
CHAPTER IN HIS BOOK s dedicated a chapter
he declared I'm simp
```

#### [93] [EFTA01652337](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652337.pdf) -- Page 44

- **Interest Score:** 69.4
- **Fragments:** 4
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Maxwell, Ghislaine

**Reconstructed Text:**

```
- CLANDESTINE 
@FACIES
Top 
Latest 
People 
Photos 
Vide:
.
George e Tanks 
Aft
I
know that she sincerely cares about 
I
t
d
h
p
g
y
p
book about .c.hiclaineleCrIVIPII & support n. 
future projects. 
es Lucia Osbome-Crowley 
-.I 22 
I have a book coming out in 2O23 and it 
means everything to me. It's about the 
RiGhislaineMaxwell trial, but it's mostly 
about the Maxwell & Epstein victims who 
trusted me with their stories & their hearts. 
There'll be a preorder link soon & your 
support would mean the world to me
```

#### [94] [EFTA01652061](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652061.pdf) -- Page 55

- **Interest Score:** 67.7
- **Fragments:** 5
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Maxwell, Ghislaine

**Reconstructed Text:**

```
g
Top 
Latest 
People 
Photos 
Videos 
fil
^
GeorgeB Tat
0
(ii
•p Tr
I:15
:i
After talkin award winningjournalist &
file
VV 
writer 
for over an hour on Sunday, I 
know that she sincerely cares about victims of
rape. I encourage everyone to preorder her 
book about 
& support her 
future projects. 
Lucia Osborne-Crowley 
I have a book coming out in 2O23 and it 
means everything to me. It's about the 
eGhislaineMaxwell trial, but it's mostly 
about the Maxwell & Epstein victims who 
trusted me with their stories & their hearts. 
There'll be a preorder link soon & your 
support would mean the world to me
```

#### [95] [EFTA01652337](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652337.pdf) -- Page 25

- **Interest Score:** 67.6
- **Fragments:** 5
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Maxwell, Ghislaine

**Reconstructed Text:**

```
Top 
Latest 
People 
Photos 
Videos 
GeorgeB Tkmks
CUOIglrBTo
1 18/23
•
After talkin award-winningjournalist&
writer 
for over an hour on Sunday. I 
know that she sincerely cares about victims of
rape. I encourage everyone to preorder her 
book about 
& support her 
future projects 
erg Lucia Osborne-Crowley 
I have a book coming out in 2023 and it 
means everything to me. It's about the 
#GhislaineMaxwell trial, but it's mostly 
about the Maxwell & Epstein victims who 
trusted me with their stories & their hearts. 
There'll be a preorder link soon & your 
support would mean the world to me 
"jr7Z4
```

#### [96] [EFTA01652061](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652061.pdf) -- Page 15

- **Interest Score:** 67.3
- **Fragments:** 5
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Maxwell, Ghislaine

**Reconstructed Text:**

```
Top 
Latest 
People 
Photos 
Videos 
fi
GO01110EtTomili
Tr
1
After talkin award-winningjournalist &
fit writer 
for over an hour on Sunday, I 
know that she sincerely cares about victims of
rape. I encourage everyone to preorder her 
book about 
& support her 
future projects. 
Lucia Osborne-Crowley 
I have a book Coming out in 2O23 and it 
means everything to me. It's about the 
#GhislaineMaxwell trial, but it's mostly 
about the Maxwell & Epstein victims who 
trusted me with their stories & their hearts. 
There'll be a preorder link soon & your 
support would mean the world to me
```

#### [97] [EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf) -- Page 54

- **Interest Score:** 66.0
- **Fragments:** 10
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Maxwell, Palm Beach, New York

**Reconstructed Text:**

```
h
j b
ibili i
h
h
ld
h
On September 9, 2019. we interviewed 
in New York. 
. During this interview, we discussed with
the process of her recruitment
intera at a high l
t t e be
o
referenced what s o describ
raining p ame into contact with Ep
ein and Maxwell, which
l but t he "reco
d her to come to Epstein's Palm Beach residence to massage Epstein
```

#### [98] [EFTA01651292](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01651292.pdf) -- Page 4

- **Interest Score:** 65.1
- **Fragments:** 6
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein

**Reconstructed Text:**

```
M
d
J
1 2020 8 04 AM
t FW VI D il N
AG
E
t i l
h
In January, George filed a civil enforcement action under the territory s Criminally Influenced and Corrupt 
Organizations Act against Epstein's estate and six of his companies, claiming that Epstein and his attorneys
the Economic Development Commission's tax benefit program to save millions of dollars that helped fund
criminal sex trafficking operation. 
A
f h
i
G
l
d li
h
h
$600
illi
h
h
i
d hi
p
,
g p
from paying settlements to victims, and argued that the terms of the compensation fund are illegal and help 
protect others who conspired with Epstein to abuse dozens of women over the last two decades. 
V I S
i
C
t J d
C
l
H
P
ll h
id h
t
f
d
ith
b t
til G
p
g
y
and Epstein's attorneys resolved their differences, and George lifts the liens.
George said in the statement Frida that she's no
illing to do that and "th
working closely with Epstein's victims and their counsel, have now reached an agreement upon the terms of the
fund, which include a set of reforms that provide a process that will be more fair, credible, and victim-oriented."
George said she's always supported the existence of such a fund which "would allow victims to avoid the
```

#### [99] [EFTA00037526](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037526.pdf) -- Page 1

- **Interest Score:** 64.9
- **Fragments:** 6
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein

**Reconstructed Text:**

```
Monday June 1 2020 8:04 AM
bject: FW: VI Daily News: AG says Epstein lawyers h
y,
g
y
y
p
Organizations Act against Epstein's estate and six of his companies, claiming that Epstein and his attorneys
the Economic Development Commission's tax benefit program to save millions of dollars that helped fund
criminal sex trafficking operation. 
A
t f th t
ti
G
l
d li
th
th
$600
illi
t t th t h
t i t d hi
tt
from paying settlements to victims, and argued that the terms of the compensation fund are illegal and help 
protect others who conspired with Epstein to abuse dozens of women over the last two decades. 
V I Superior Court Judge Carolyn Hermon Purcell has said she cannot move forward with probate until Ge
and Epstein's attorneys resolved their differences, and George lifts the liens.
George said in the statement Friday that she's now willing to do that and "th
working closely with Epstein's victims and their counsel, have now reached an agreement upon the terms of the
fund, which include a set of reforms that provide a process that will be more fair, credible, and victim-oriented."
George said she's always supported the existence of such a fund which "would allow victims to avoid the
```

#### [100] [EFTA01652971](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652971.pdf) -- Page 4

- **Interest Score:** 63.8
- **Fragments:** 4
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Courtney, Wild, Edwards, Bradley

**Reconstructed Text:**

```
a cancer article to defame me and
Sigrid never cared, giggled when I
sobbed. She was busy building
In June 2008, Florida-based victims' rights attorney 
Bradley J. Edwards was thirty-two years old and 
had just started his own law firm when a young 
woman named Courtney Wild came to see him.
```

#### [101] [EFTA00015287](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015287.pdf) -- Page 0

- **Interest Score:** 63.2
- **Fragments:** 4
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Maxwell, Ghislaine, Jeffrey, New York

**Reconstructed Text:**

```
SDNY NEWS CLIPS THURSDAY JANUARY 28 2021
SDNY PRESS CLIPPINGS
New York Post Ghislaine Maxwell forced  girls into lurid  performances for Jeffrey Epstein, court docs reveal Accused madam Ghislaine Maxwell once directed a room of underage girls to "kiss, dance and touch one 
h
i
l
" f
l
Whil
b
5 h
i
)
Spokesman
```

#### [102] [EFTA00010111](https://www.justice.gov/epstein/files/DataSet%208/EFTA00010111.pdf) -- Page 3

- **Interest Score:** 61.2
- **Fragments:** 15
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds1-9_11-12
- **Names Found:** New York

**Reconstructed Text:**

```
• 
The Registrar of Rhode Island Department of Health has signed and certified that
Government Exhibit 12, Minor Victim-I's birth certificate, is a "true and exact copy ofthi
document officially registered and placed on file in the issuing office."
• 
The Registrar of the Missouri Department of Health and Senior Services has signed and
certified that Government Exhibit 13, Minor Victim-2's birth certificate, is an "exacj
reproduction of the certificate for the person named therein as it now appears in the
permanent records of the Bureau of Vital Records of the Missouri Department of Health
and Senior Services."
• 
The Registrar of the Town of North Hempstead, Nassau County, New York, has signed
kd certified that Government Exhibit 11, Minor Victim-4 s birth certificate, is a true ani
correct copy of the original Certificate of Birth on file in the Office of the Registrar.
The County Clerk/Recorder of Sacramento County, California, has signed and certified
that Government Exhibit 14, Minor Victim 5 s birth certificate, is a true and exact
a 
the document officially registered and placed on file in the office of
Ea s 
y
```

#### [103] [EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf) -- Page 59

- **Interest Score:** 59.8
- **Fragments:** 13
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds1-9_11-12
- **Names Found:** Maxwell, Andrew, Prince, Les

**Reconstructed Text:**

```
t i ti ll
fi ti
li
d
t f h
i
d
ith E
t i
d M
As for 
well as 
account o
recollect
Prince Andrew. who has publicly s with Pr
f= 
l also int
ations Andrew and Maxwell. 
o Prince Andrew.
r she recalled any other females who ma have been present with her during thes
ose name could not recall, had all participated with
sexual
meetin pstein or
y with Howeve een unable
```

#### [104] [EFTA01650456](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01650456.pdf) -- Page 0

- **Interest Score:** 59.6
- **Fragments:** 6
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein, Jeffrey

**Reconstructed Text:**

```
RE 
claim
BudgetAnalyst Trainee
Wednesda November 6 2019 1:16 PM
UMW )4.'4'1M (WHIM. 
it was great speaking to you! As we discussed this victim and the othel 
Epstein. It is a sex trafficking case. I will send over of FBI victim form soon as the Agent signs it. 
re victims of Jeffrey
Tuesda October 22 2019 9:15 PM
bject: 
laim
```

#### [105] [EFTA00020917](https://www.justice.gov/epstein/files/DataSet%208/EFTA00020917.pdf) -- Page 0

- **Interest Score:** 58.3
- **Fragments:** 14
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Jeffrey

**Reconstructed Text:**

```
F id
N
b
22 2019 13 37
bject: RE: Jeffrey Epstein Victim; Ms
17 years old
sex traffick our 800 line
Friday November 22 2019 1:24 PM
bject: RE: Jeffrey Epstein Victim; Ms
17 years old
Friday, November 22, 2019 13:17
Subject: FW: Jeffrey Epstein Victim; Ms
Thursday, November 21, 2019 8:12
bject: Jeffrey Epstein Victim; Ms 
1 years old
very
Eps exico.
ccasio Ms.
ns a
```

#### [106] [EFTA01652061](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652061.pdf) -- Page 64

- **Interest Score:** 57.4
- **Fragments:** 6
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein

**Reconstructed Text:**

```
ladyvictoriahervey • 2I1 
From Create Mode t 
I don't think I'm the only one who is so 
sick of these pretenders. They are 
mostly paid escorts and rent boys 
extorting money. It's just about 
money. 
Watch gsoundoffreedommovie
+
If you have not yet seen it. 
This is REAL traffickingand shows
what a joke these con artists really 
9
are. Also the media is responsible for •
using the word 'trafficking' so loosely ° 
In order to dramatize the story of the •
epstein fake survivors. 
2
Photolog 
George B. Tonics 
RENT GIRLS & BOYS LIVING THE HIGH 
LIFE IS NOT SEX TRAFFICKING! 
100
iadyvictorialservey 0 bin 
From Create Mode 
Iii 
I 
I 
What case were you a 
witness on and what 
governmental agency 
granted you whistleblower 
status. No one can find it. 
If George B. Tonks lied 
About anything the attorneys 
would have sued him and the 
federal judge would have 
held him if he felt George 
submitted a fraudulent 
document to the court. 
None of that happened...
```

#### [107] [EFTA01652337](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652337.pdf) -- Page 73

- **Interest Score:** 57.2
- **Fragments:** 6
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Epstein

**Reconstructed Text:**

```
ydyyietoriahervey • 
2h 
orn Create mode
I don't think I'm the only one who is so 
sick of these pretenders. They are 
mostly paid escorts and rent boys 
extorting money. It's just about 
money. 
Watch @soundoffreedommovie
()
If you have not yet seen it. 
This isREAL traffickingand shows
111P
what a joke these con artists really 
are. Also themedia is responsible for 0
using the word 'trafficking' so loosely 
In order to dramatize the story of the 
0 
N
epstein fake survivors. 
Photolog 
George B. Tonics 
RENT GIRL S ;L: BOYS LIVING THE HIGH 
F IS NOT SEX TRAFFiGKING,
I.
Iaayvrctonanervey0 bm 
From Croato Mort. 
I ii 
X 
What case were you a 
witness on and what 
governmental agency 
granted you whistleblower 
status. No one can find it. 
If George B. Tonics lied 
ibout anything the attorneys 
ould have sued him and the 
federal judge would have 
held him if he felt George 
submitted a fraudulent 
document to the court. 
None of that happened...
```

#### [108] [EFTA01305714](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01305714.pdf) -- Page 24

- **Interest Score:** 56.5
- **Fragments:** 6
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds10
- **Names Found:** Black, New York, Manhattan

**Reconstructed Text:**

```
S 167 ROBERT F WAGNER
MANHATTAN INTERNATIONAL HIGH SCHOOL 
EAST
N ST
SCHOOL DISTRICTS 
NEW YORK CITY GEOGRAPHIC DISTRICT # 2
About 
Public Schools
THIS REPORT IS PROVIDED "AS IS" AND ALL USES ARE AT THE USER'S SOLE RISK. ALL WARRANTIES CONCERNING THE REPORT BOTH EXPRESS
TM SKI 0 Trademarks) of Black Knight IP Holding Company, LLC, or an affiliate. m 2019 Black Knight Financial Technology Solutions. LLC. All Rights Reserved.
```

#### [109] [EFTA02731200](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731200.pdf) -- Page 7

- **Interest Score:** 55.8
- **Fragments:** 11
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds1-9_11-12
- **Names Found:** New York

**Reconstructed Text:**

```
same for masse es atth New York Resi ence.
conversations some victimsrecall having
Regarding the relevant
ut topicssuch as living with
of a massage: recounts that 
reca 
u emt e massage r
ia
m at
w t ence
ges t at E stem ultimately d
ventua y
ere was
ledged
that s to t not re
b li
th
h
l sexua contact wt 
a ize at i e victims were underage. Both 
and 
d have known that some of the girls were minors, given a 
un erage victims. 
states
now say they
e circumstances.
```

#### [110] [EFTA00037511](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037511.pdf) -- Page 1

- **Interest Score:** 54.2
- **Fragments:** 5
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein

**Reconstructed Text:**

```
I 2020 5 36 PM
Monday June 1 2020 8:04 AM
Organizations Act against Epstein's estate and six of his companies, claiming that Epstein and his attorneys
the Economic Development Commission's tax benefit program to save millions of dollars that helped fund
criminal sex trafficking operation. 
As pan of that action George placed liens on the more than $600 million estate that have restricted his atto
from paying settlements to victims, and argued that the terms of the compensation fund are illegal and help 
protect others who conspired with Epstein to abuse dozens of women over the last two decades. 
V I Superior Court Judge Carolyn Hermon-Purcell has said she cannot move forward with probate until Ge
and Epstein's attorneys resolved their differences, and George lifts the liens.
```

#### [111] [EFTA02731082](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731082.pdf) -- Page 58

- **Interest Score:** 54.1
- **Fragments:** 8
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Maxwell

**Reconstructed Text:**

```
ld
hi k
did
k
h
account of being recruited by Maxwell, abused by Maxw
and Epstein engaging in paid sexualized massages with Epstein as a minor recruiting othe
nces
remar the expe
men
has publicly identified as people to whom she was"lent out" have
either Maxwell or Epstein to engage in sexual activitsithinith
recalled E stein asking her to massage Harve Weinstein and that men. 
ng the massage Weinstein
```

#### [112] [EFTA00029640](https://www.justice.gov/epstein/files/DataSet%208/EFTA00029640.pdf) -- Page 0

- **Interest Score:** 52.5
- **Fragments:** 11
- **Document Type:** VICTIM_STATEMENT
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Jeffrey

**Reconstructed Text:**

```
Friday November 22 2019 13:37
bject: RE: Jeffrey Epstein Victim; Ms
> 
>; 
17 years old
sex traffick our 800 line
Friday, November 22, 2019 1:24 PM
bject: RE: Jeffrey Epstein Victim; Ms 
17 years old
Friday, November 22, 2019 13:17
Subject: FW: Jeffrey Epstein Victim; Ms
Thursday, November 21, 2019 8:12
bject: Jeffrey Epstein Victim; Ms 
1 years old
```

---

### LEGAL (18 pages)

#### [113] [EFTA01652864](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652864.pdf) -- Page 12

- **Interest Score:** 77.0
- **Fragments:** 3
- **Document Type:** LEGAL
- **Dataset:** ds10
- **Names Found:** Epstein, Jeffrey, Edwards

**Reconstructed Text:**

```
ABC 20/20 
Truth & Lies: The Jeffrey Epstein
Story 
Lifei iii. 
Surviving Jeffrey 
:DWARDS HENDERSON 
) \ it 
CRIME VICTIM 
Empowering. 
Compassionate. 
Trustworthy. 
Edwards Henderson is a nationally-recognized 
powerhouse litigation firm, dedicated to providing its 
clients with the highest quality legal services and, at 
the same time, making substantial, positive changes 
for the common good. 
We are skilled litigators and experienced trial 
attorneys who have effectively pursued civil lawsuits 
against some of the most powerful individuals, 
organizations and big businesses on behalf of people, 
victims and small businesses In fact we specialize in
handling cases where the power differential is 
greatest and we can use our experience and 
/lien the playing held. Our recent Trial 
results speak for themselves.
```

#### [114] [EFTA00037515](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037515.pdf) -- Page 2

- **Interest Score:** 72.9
- **Fragments:** 6
- **Document Type:** LEGAL
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein

**Reconstructed Text:**

```
In January, George filed a civil enforcement action under the territory's Criminally Influenced and Corrupt 
Organizations Act against Epstein's estate and six of his companies, claiming that Epstein and his attorneys
the Economic Development Commission's tax benefit program to save millions of dollars that helped fund
criminal sex trafficking operation.
As pan of that action, George placed liens on the more than $600 million estate that have restricted his attor
from paying settlements to victims, and argued that the terms of the compensation fund are illegal and help 
protect others who conspired with Epstein to abuse dozens of women over the last two decades.
V.I. Superior Court Judge Carolyn Hermon-Purcell has said she cannot move
and Epstein's attorneys resolved their differences, and George lifts the liens.
George said in the statement Friday that she's now willing to do that, and "the Attorney General's Office, 
working closely with Epstein's victims and their counsel, have now reached an agreement upon the terms of the
fund, which include a set of reforms that provide a process that will be more fair, credible, and victim-oriented."
sues This will help ensure that the de
Access to counseling and referral services through the FBI Victim Services program and Child USA.
```

#### [115] [EFTA00037532](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037532.pdf) -- Page 1

- **Interest Score:** 71.0
- **Fragments:** 6
- **Document Type:** LEGAL
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein

**Reconstructed Text:**

```
In January, George filed a civil enforcement action under the territory s Criminally Influenced and Corrupt 
Organizations Act against Epstein's estate and six of his companies, claiming that Epstein and his attorneys
the Economic Development Commission's tax benefit program to save millions of dollars that helped fund
criminal sex trafficking operation.
As part of that action, George placed liens on the more than $600 million estate that have restricted his attor
from paying settlements to victims, and argued that the terms of the compensation fund are illegal and help 
protect others who conspired with Epstein to abuse dozens of women over the last two decades.
V.I. Superior Court Judge Carolyn Hermon Purcell has said she cannot move
and Epstein's attorneys resolved their differences, and George lifts the liens.
George said in the statement Friday that she s now willing to do that, and the Attorney General s Office, 
working closely with Epstein's victims and their counsel, have now reached an agreement upon the terms of the
fund, which include a set of reforms that provide a process that will be more fair, credible, and victim-oriented."
sues. This will help ensure that the de
• Approval of the program's administrative budget by the Probate Court and monthly reporting to the A
```

#### [116] [EFTA00037535](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037535.pdf) -- Page 1

- **Interest Score:** 71.0
- **Fragments:** 6
- **Document Type:** LEGAL
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein

**Reconstructed Text:**

```
In January, George filed a civil enforcement action under the territory s Criminally Influenced and Corrupt 
Organizations Act against Epstein's estate and six of his companies, claiming that Epstein and his attorneys
the Economic Development Commission's tax benefit program to save millions of dollars that helped fund
criminal sex trafficking operation.
As part of that action, George placed liens on the more than $600 million estate that have restricted his attor
from paying settlements to victims, and argued that the terms of the compensation fund are illegal and help 
protect others who conspired with Epstein to abuse dozens of women over the last two decades.
V.I. Superior Court Judge Carolyn Hermon Purcell has said she cannot move
and Epstein's attorneys resolved their differences, and George lifts the liens.
George said in the statement Friday that she s now willing to do that, and the Attorney General s Office, 
working closely with Epstein's victims and their counsel, have now reached an agreement upon the terms of the
fund, which include a set of reforms that provide a process that will be more fair, credible, and victim-oriented."
sues. This will help ensure that the de
• Approval of the program's administrative budget by the Probate Court and monthly reporting to the A
```

#### [117] [EFTA00037519](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037519.pdf) -- Page 1

- **Interest Score:** 71.0
- **Fragments:** 6
- **Document Type:** LEGAL
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein

**Reconstructed Text:**

```
In January, George filed a civil enforcement action under the territory's Criminally Influenced and Corrupt 
Organizations Act against Epstein's estate and six of his companies, claiming that Epstein and his attorneys
the Economic Development Commission's tax benefit program to save millions of dollars that helped fund
criminal sex trafficking operation.
As pan of that action, George placed liens on the more than $600 million estate that have restricted his attor
from paying settlements to victims, and argued that the terms of the compensation fund are illegal and help 
protect others who conspired with Epstein to abuse dozens of women over the last two decades.
V.I. Superior Court Judge Carolyn Hermon-Purcell has said she cannot move
and Epstein's attorneys resolved their differences, and George lifts the liens.
George said in the statement Friday that she s now willing to do that, and the Attorney General s Office, 
working closely with Epstein's victims and their counsel, have now reached an agreement upon the terms of the
fund, which include a set of reforms that provide a process that will be more fair, credible, and victim-oriented."
sues. This will help ensure that the de
• Approval of the program's administrative budget by the Probate Court and monthly reporting to the A
```

#### [118] [EFTA01651272](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01651272.pdf) -- Page 3

- **Interest Score:** 70.6
- **Fragments:** 5
- **Document Type:** LEGAL
- **Dataset:** ds10
- **Names Found:** Epstein

**Reconstructed Text:**

```
In January, George filed a civil enforcement action under the territory s Criminally Influenced and Corrupt 
Organizations Act against Epstein's estate and six of his companies, claiming that Epstein and his attorneys
the Economic Development Commission's tax benefit program to save millions of dollars that helped fund
criminal sex trafficking operation.
As pan of that action, George placed liens on the more than $600 million estate that have restricted his attor
from paying settlements to victims, and argued that the terms of the compensation fund are illegal and help 
protect others who conspired with Epstein to abuse dozens of women over the last two decades.
V.I. Superior Court Judge Carolyn Hermon Purcell has said she cannot move
and Epstein's attorneys resolved their differences, and George lifts the liens.
George said in the statement Friday that she s now willing to do that, and the Attorney General s Office, 
working closely with Epstein's victims and their counsel, have now reached an agreement upon the terms of the
fund, which include a set of reforms that provide a process that will be more fair, credible, and victim-oriented."
G
id h '
l
d h
i
f
h
f
d
hi h "
ld ll
i i
id h
• Approval of the program's administrative budget by the Probate Court and monthly reporting to the A
```

#### [119] [EFTA01651264](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01651264.pdf) -- Page 2

- **Interest Score:** 69.7
- **Fragments:** 5
- **Document Type:** LEGAL
- **Dataset:** ds10
- **Names Found:** Epstein

**Reconstructed Text:**

```
In January, George filed a civil enforcement action under the territory's Criminally Influenced and Corrupt 
Organizations Act against Epstein's estate and six of his companies, claiming that Epstein and his attorneys
the Economic Development Commission's tax benefit program to save millions of dollars that helped fund
criminal sex trafficking operation.
As part of that action, George placed liens on the more than $600 million estate that have restricted his attor
from paying settlements to victims, and argued that the terms of the compensation fund are illegal and help 
protect others who conspired with Epstein to abuse dozens of women over the last two decades.
V.I. Superior Court Judge Carolyn Hermon-Purcell has said she cannot move
and Epstein's attorneys resolved their differences, and George lifts the liens.
George said in the statement Friday that she s now willing to do that, and the Attorney General s Office, 
working closely with Epstein's victims and their counsel, have now reached an agreement upon the terms of the
fund, which include a set of reforms that provide a process that will be more fair, credible, and victim-oriented."
• Approval of the program's administrative budget by the Probate Court and monthly reporting to the A
```

#### [120] [EFTA01651279](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01651279.pdf) -- Page 2

- **Interest Score:** 69.7
- **Fragments:** 5
- **Document Type:** LEGAL
- **Dataset:** ds10
- **Names Found:** Epstein

**Reconstructed Text:**

```
In January, George filed a civil enforcement action under the territory's Criminally Influenced and Corrupt 
Organizations Act against Epstein's estate and six of his companies, claiming that Epstein and his attorneys
the Economic Development Commission's tax benefit program to save millions of dollars that helped fund
criminal sex trafficking operation.
As part of that action, George placed liens on the more than $600 million estate that have restricted his attor
from paying settlements to victims, and argued that the terms of the compensation fund are illegal and help 
protect others who conspired with Epstein to abuse dozens of women over the last two decades.
V.I. Superior Court Judge Carolyn Hermon-Purcell has said she cannot move
and Epstein's attorneys resolved their differences, and George lifts the liens.
George said in the statement Friday that she s now willing to do that, and the Attorney General s Office, 
working closely with Epstein's victims and their counsel, have now reached an agreement upon the terms of the
fund, which include a set of reforms that provide a process that will be more fair, credible, and victim-oriented."
• Approval of the program's administrative budget by the Probate Court and monthly reporting to the A
```

#### [121] [EFTA00037538](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037538.pdf) -- Page 1

- **Interest Score:** 69.0
- **Fragments:** 5
- **Document Type:** LEGAL
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein

**Reconstructed Text:**

```
In January, George filed a civil enforcement action under the territory's Criminally Influenced and Corrupt 
Organizations Act against Epstein's estate and six of his companies, claiming that Epstein and his attorneys
the Economic Development Commission's tax benefit program to save millions of dollars that helped fund
criminal sex trafficking operation.
As part of that action, George placed liens on the more than $600 million estate that have restricted his attor
from paying settlements to victims, and argued that the terms of the compensation fund are illegal and help 
protect others who conspired with Epstein to abuse dozens of women over the last two decades.
V.I. Superior Court Judge Carolyn Hermon-Purcell has said she cannot move
and Epstein's attorneys resolved their differences, and George lifts the liens.
George said in the statement Friday that she s now willing to do that, and the Attorney General s Office, 
working closely with Epstein's victims and their counsel, have now reached an agreement upon the terms of the
fund, which include a set of reforms that provide a process that will be more fair, credible, and victim-oriented."
g
g
p
g
A
l f th
'
d i i t ti
b d
t b th P
b t C
t
d
thl
ti
t
th A
```

#### [122] [EFTA01651283](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01651283.pdf) -- Page 2

- **Interest Score:** 69.0
- **Fragments:** 5
- **Document Type:** LEGAL
- **Dataset:** ds10
- **Names Found:** Epstein

**Reconstructed Text:**

```
In January, George filed a civil enforcement action under the territory's Criminally Influenced and Corrupt 
Organizations Act against Epstein's estate and six of his companies, claiming that Epstein and his attorneys
the Economic Development Commission's tax benefit program to save millions of dollars that helped fund
criminal sex trafficking operation.
As pan of that action, George placed liens on the more than $600 million estate that have restricted his attor
from paying settlements to victims, and argued that the terms of the compensation fund are illegal and help 
protect others who conspired with Epstein to abuse dozens of women over the last two decades.
V.I. Superior Court Judge Carolyn Hermon-Purcell has said she cannot move
and Epstein's attorneys resolved their differences, and George lifts the liens.
George said in the statement Friday that she s now willing to do that, and the Attorney General s Office, 
working closely with Epstein's victims and their counsel, have now reached an agreement upon the terms of the
fund, which include a set of reforms that provide a process that will be more fair, credible, and victim-oriented."
g
g
p
g
A
l f th
'
d i i t ti
b d
t b th P
b t C
t
d
thl
ti
t th A
```

#### [123] [EFTA01651298](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01651298.pdf) -- Page 4

- **Interest Score:** 68.7
- **Fragments:** 5
- **Document Type:** LEGAL
- **Dataset:** ds10
- **Names Found:** Epstein

**Reconstructed Text:**

```
In January, George filed a civil enforcement action under the territory's Criminally Influenced and Corrupt 
Organizations Act against Epstein's estate and six of his companies, claiming that Epstein and his attorneys
the Economic Development Commission's tax benefit program to save millions of dollars that helped fund
criminal sex trafficking operation.
As pan of that action, George placed liens on the more than $600 million estate that have restricted his attor
from paying settlements to victims, and argued that the terms of the compensation fund are illegal and help 
protect others who conspired with Epstein to abuse dozens of women over the last two decades.
V.I. Superior Court Judge Carolyn Hermon-Purcell has said she cannot move
and Epstein's attorneys resolved their differences, and George lifts the liens.
George said in the statement Friday that she s now willing to do that, and the Attorney General s Office, 
working closely with Epstein's victims and their counsel, have now reached an agreement upon the terms of the
find, which include a set of reforms that provide a process that will be more fair, credible, and victim-oriented."
g
g
p
g
A
l f h
'
d i i
i
b d
b
h P
b
C
d
hl
i
h A
```

#### [124] [EFTA01651648](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01651648.pdf) -- Page 1

- **Interest Score:** 68.2
- **Fragments:** 6
- **Document Type:** LEGAL
- **Dataset:** ds10
- **Names Found:** Epstein, Jeffrey, Edwards, Bradley

**Reconstructed Text:**

```
Breakout Session I 10:10 am - 10:50 am 
Assessment and Intervention of 
Post-Traumatic Stress Disorder 
Daniel Sullivan, MA, MSW & Stephanie Grimaldi, MA, 
MSW Clinical Psychology Doctoral Students 
The Phobia and Trauma Clinic at Hofstra University's Joan 
and Arnold Saltzman Community Services Center
Breakout Session II 11:10 am — 12:00 pm
The Intersection of Trauma, Addiction, 
and Eating Disorders 
Thi
k h
ill f
h
i
b
Breakout Session III 12:10 pm — 1:00 pm 
An Overview of Sex Crimes and Consent 
Eric Aboulafia & Melissa Grier, I Assistant District Attorneys 
The Suffolk County District Attorney's Office
Breakout Session IV 1:10 pm - 2:00 pm 
Civil Litigation of Sexual Abuse Claims —
Jeffrey Epstein 
Bradley). Edwards, Esq. I Founding Partner at Edwards 
Pottinger LLC & 
Brittany Henderson, Esq. I Partner at Edwards Pottinger LLC 
Thi
k h
ill
th J ff
E
t i
t
l i
i il
di
il bl t
i
f
l b
d h
t
ffi ki
i
b th t t
d f d
l
t
24/7 Crisis Hotlines:
```

#### [125] [EFTA00037529](https://www.justice.gov/epstein/files/DataSet%208/EFTA00037529.pdf) -- Page 1

- **Interest Score:** 68.2
- **Fragments:** 5
- **Document Type:** LEGAL
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein

**Reconstructed Text:**

```
In January, George filed a civil enforcement action under the territory s Criminally Influenced and Corrupt 
Organizations Act against Epstein's estate and six of his companies, claiming that Epstein and his attorneys
the Economic Development Commission's tax benefit program to save millions of dollars that helped fund
criminal sex trafficking operation.
As part of that action, George placed liens on the more than $600 million estate that have restricted his attor
from paying settlements to victims, and argued that the terms of the compensation fund are illegal and help 
protect others who conspired with Epstein to abuse dozens of women over the last two decades.
V. . Supe o Cou t Judge Ca o y
e
o
u ce
as sa d s e ca
ot
ove
and Epstein's attorneys resolved their differences, and George lifts the liens.
G
id i
h
F id
h
h '
illi
d
h
d " h
g
y
g
,
y
,
working closely with Epstein's victims and their counsel, have now reached an agreement upon the terms of the
fund, which include a set of reforms that provide a process that will be more fair, credible, and victim-oriented."
G
id h '
l
t d th
i t
f
h
f
d
hi h "
ld ll
i ti
t
id th
sues. This will help ensure that the dec
```

#### [126] [EFTA00038491](https://www.justice.gov/epstein/files/DataSet%208/EFTA00038491.pdf) -- Page 2

- **Interest Score:** 68.1
- **Fragments:** 5
- **Document Type:** LEGAL
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein

**Reconstructed Text:**

```
In January, George filed a civil enforcement action under the territory s Criminally Influenced and Corrupt 
Organizations Act against Epstein's estate and six of his companies, claiming that Epstein and his attorneys
the Economic Development Commission's tax benefit program to save millions of dollars that helped fund
criminal sex trafficking operation.
As part of that action, George placed liens on the more than $600 million estate that have restricted his attor
from paying settlements to victims, and argued that the terms of the compensation fund are illegal and help 
protect others who conspired with Epstein to abuse dozens of women over the last two decades.
V. . Supe o Cou t Judge Ca o y
e
o
u ce
as sa d s e ca
ot
ove
and Epstein's attorneys resolved their differences, and George lifts the liens.
G
id i
h
id
h
h '
illi
d
h
d " h
g
y
g
,
y
,
working closely with Epstein's victims and their counsel, have now reached an agreement upon the terms of the
fund, which include a set of reforms that provide a process that will be more fair, credible, and victim-oriented."
G
id h '
l
t d th
i t
f
h
f
d
hi h "
ld ll
i ti
t
id th
sues. This will help ensure that the de
```

#### [127] [EFTA01651648](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01651648.pdf) -- Page 0

- **Interest Score:** 59.3
- **Fragments:** 7
- **Document Type:** LEGAL
- **Dataset:** ds10
- **Names Found:** Epstein, Jeffrey, Edwards, Bradley

**Reconstructed Text:**

```
9:0
1
0
10:00
Assessment and Intervention of PTSD 
P
t d b D
i l S lli
MA M S W & St
h
i G i
ldi MA I Cli i
lP
h l
D
t
lSt d
t
The Intersection of Trauma, Addiction, and Eating Disorders: From Isolation to Re-Attachment 
Presented by Dr Valentina Stoycheva Ph D I Co Founder and Director
An Overview of NY State Sex Crimes and Consent 
Presented by Eric Aboulafia & Melissa Grier Assistant District Attorneys
Civil Litigation of Sexual Abuse Claims —Jeffrey Epstein Case Study 
Presented by Bradley J. Edwards, Esq.,FoundingPartner at Edwards Pottinger LLC
CRIME V
Parents CLN I LI
n's Law
```

#### [128] [EFTA01651658](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01651658.pdf) -- Page 0

- **Interest Score:** 59.3
- **Fragments:** 7
- **Document Type:** LEGAL
- **Dataset:** ds10
- **Names Found:** Epstein, Jeffrey, Edwards, Bradley

**Reconstructed Text:**

```
9:0
1
0
10:00
Assessment and Intervention of PTSD 
P
t d b D
i l S lli
MA M S W & St
h
i G i
ldi MA I Cli i
lP
h l
D
t
lSt d
t
The Intersection of Trauma, Addiction, and Eating Disorders: From Isolation to Re-Attachment 
Presented by Dr Valentina Stoycheva Ph D I Co Founder and Director
An Overview of NY State Sex Crimes and Consent 
Presented by Eric Aboulafia & Melissa Grier Assistant District Attorneys
Civil Litigation of Sexual Abuse Claims —Jeffrey Epstein Case Study 
Presented by Bradley J. Edwards, Esq.,FoundingPartner at Edwards Pottinger LLC
CRIME V
Parents CLN I LI
n's Law
```

#### [129] [EFTA01651639](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01651639.pdf) -- Page 0

- **Interest Score:** 58.1
- **Fragments:** 5
- **Document Type:** LEGAL
- **Dataset:** ds10
- **Names Found:** Epstein, Jeffrey, Edwards, Bradley

**Reconstructed Text:**

```
9:00.10:00 ■
Assessment and Intervention of PTSD 
Presented b Daniel S lli an MA M S W & Stephanie Grimaldi MA I ClinicalPs cholog Doctoral St dents
The Intersection of Trauma, Addiction, and Eating Disorders: From Isolation to Re-Attachment 
Presented by Dr Valentina Stoycheva Ph D I Co Founder and Director
An Overview of NY State Sex Crimes and Consent 
Presented by Eric Aboulafia & Melissa Grier Assistant District Attorneys
Civil Litigation of Sexual Abuse Claims —Jeffrey Epstein Case Study 
Presented by Bradley 1. Edwards, Esq., FoundingPartner at Edwards Pottinger LLC
```

#### [130] [EFTA01651641](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01651641.pdf) -- Page 0

- **Interest Score:** 58.1
- **Fragments:** 5
- **Document Type:** LEGAL
- **Dataset:** ds10
- **Names Found:** Epstein, Jeffrey, Edwards, Bradley

**Reconstructed Text:**

```
9:00.10:00 ■
Assessment and Intervention of PTSD 
Presented b Daniel S lli an MA M S W & Stephanie Grimaldi MA I ClinicalPs cholog Doctoral St dents
The Intersection of Trauma, Addiction, and Eating Disorders: From Isolation to Re-Attachment 
Presented by Dr Valentina Stoycheva Ph D I Co Founder and Director
An Overview of NY State Sex Crimes and Consent 
Presented by Eric Aboulafia & Melissa Grier Assistant District Attorneys
Civil Litigation of Sexual Abuse Claims —Jeffrey Epstein Case Study 
Presented by Bradley 1. Edwards, Esq., FoundingPartner at Edwards Pottinger LLC
```

---

### CALENDAR_SCHEDULE (7 pages)

#### [131] [EFTA01376719](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01376719.pdf) -- Page 0

- **Interest Score:** 68.7
- **Fragments:** 24
- **Document Type:** CALENDAR_SCHEDULE
- **Dataset:** ds10

**Reconstructed Text:**

```
763 H
763 K HKI) Suspender 
At 4:08 d 
Prey 25.60 
90 Export
911 Settings 
Page 1/6 
Historical Price Table
IT Corp 
taw. 
D • 
Low 
Averace 
PIJA (kJ 
Volume
• 
Price
37.30 
16.98 
on 
25.028 
8.17 
Date
Last Price
11/21/17 
06/13/17 
14.628,298 
46.45% 
Volume
2
2
2
2
2 2
2
2
2
2 0 
0 
0 
0 
0
FIc 06/04/18 
25 0 
)1,3 05/14/18 0 
04/23/18 
25.60
2
2
2
2
2 2
2
2
2
2 0 
0 
0 
0 
0 4 983 000
Fr
05/25/18
25 60
h
05/04/18 25 60
04/13/18
26 10
,
,
4 728 042
Fr 
05/25/18 
25.60 
lb 05/24/18 
25.60 
);,- 05/23/18 
25.60 
Tu 05/22/18 
25.60 
h 05/0
Th 05/0
W.T, 05/0
Tu 05/0
ft, 04/3 25.
25.
25.
25.6 0 
0 
0 
0 04/13
04/12
04/1
04/1
CA/0 3/18 
2/18 
/18 
0/18 
9/18 
2
2
2
2
2 4,728
6,069
12,204
10,166
13,373
8 3:48 PM
VWAP on Monday
```

#### [132] [EFTA00028355](https://www.justice.gov/epstein/files/DataSet%208/EFTA00028355.pdf) -- Page 0

- **Interest Score:** 58.7
- **Fragments:** 18
- **Document Type:** CALENDAR_SCHEDULE
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, New York

**Reconstructed Text:**

```
W d
d
J l 10 2019 10 09
bj
t RE U S
E
t i
19 490
i ti
' i ht b il h
i
Wednesday July 10 2019 2
bject: FW: U S v Epstein 19 Cr 90
victims' rights re: bail earing
0 2019 10:06 PM
; Alex ndra Elenowitz-Hess
bject: Re: U.S. v. Epste 19 Cr. 490 — victims ghts re: bail hearing
New York New York 10118
Wednesday, July 10, 2019 5:56:3
bject: RE: U.S. v. Epste , 19 Cr. 490 — victims' rights
```

#### [133] [EFTA00018732](https://www.justice.gov/epstein/files/DataSet%208/EFTA00018732.pdf) -- Page 0

- **Interest Score:** 55.7
- **Fragments:** 14
- **Document Type:** CALENDAR_SCHEDULE
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Maxwell, Ghislaine, Jeffrey

**Reconstructed Text:**

```
Wednesday March 10 0215:45 PM
bject: RE: Jeffrey Epstein/Gh laine Maxwell/FOIA
Wednesday, March 10, 2021 5:44 PM
) < 
< 
; 
bject: RE: Jeffrey Epstein/Ghislaine Maxwell/FOIA
agilagida6 021 5:40 PM
bject: RE: Jeffrey Epstein/Gh laine Maxwell/FOIA
east on
Wednesday, March 10, 2021 5.23 PM
bject: RE: Jeffrey Epstein/Gh laine Maxwell/FOIA
```

#### [134] [EFTA00030537](https://www.justice.gov/epstein/files/DataSet%208/EFTA00030537.pdf) -- Page 0

- **Interest Score:** 53.7
- **Fragments:** 6
- **Document Type:** CALENDAR_SCHEDULE
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Jeffrey

**Reconstructed Text:**

```
Tuesday August 6 2019 4:40 PM
bject: Re: CONFIDENTIAL: Victim Reports Against Jeffrey Epstein 19 Cr 490 (RMB)
Tuesday, August 6, 2019 4:21:29 PM
bject: RE: CONFIDENTIAL: Victim Reports Against Jeffrey Epstein, 19 Cr. 490 (RMB)
Monday, August 5, 2019 7
e ject: FW: CONFIDENTIAL: Victim Reports Against Jeffrey Epstein, 19 Cr. 490 (RMB)
```

#### [135] [EFTA02731486](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02731486.pdf) -- Page 0

- **Interest Score:** 53.2
- **Fragments:** 10
- **Document Type:** CALENDAR_SCHEDULE
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Maxwell, Black, Leon

**Reconstructed Text:**

```
T
d
M
30 2023 10 20 AM
RE Epstein/Ma
ell/Leon Black/Additional S bject
Tuesday May 30 2023 9:50 AM
bject: RE: Epstein/Maxwell/Leon Black/Additional Subject
Tuesday May 30 2023 9:47 AM
bject: RE: Epstein/Maxwell/Leon Black/Additional Subject
Tuesday, May 30, 2023 9:35 AM
bject: RE: Epstein/Maxwell/Leon Black/Additional Subject
Tuesday, May 30, 2023 9:16 AM
bject: Epstein Maxwell Leon Blac Additional Subject
```

#### [136] [EFTA00013253](https://www.justice.gov/epstein/files/DataSet%208/EFTA00013253.pdf) -- Page 2

- **Interest Score:** 53.2
- **Fragments:** 8
- **Document Type:** CALENDAR_SCHEDULE
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Les, Maria

**Reconstructed Text:**

```
f
li k f
W
11 2020 5 16 PM
Mariann Wang 
ject: Zoom conference link fo Wednesday at 2 pm ET
Los Angeles, CA 90048
Mariann Wang 
ject: RE: New potential victim s of Epstein and some of Max
Los Angeles, CA 90048
```

#### [137] [EFTA00021787](https://www.justice.gov/epstein/files/DataSet%208/EFTA00021787.pdf) -- Page 0

- **Interest Score:** 52.9
- **Fragments:** 5
- **Document Type:** CALENDAR_SCHEDULE
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Maxwell, Ghislaine, Jeffrey, Manhattan

**Reconstructed Text:**

```
atur ay uy
Subject: FW: GHISLAINE MAXWELL CHARGED IN MANHATTAN FEDERAL COURT FOR CONSPIRING WITH JEFFREY EPSTEIN
Thursday July 02 2020 1:22 PM
ey Jr., the Assist
E MAXWEL
```

---

### PHONE_RECORD (24 pages)

#### [138] [EFTA01461896](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01461896.pdf) -- Page 0

- **Interest Score:** 141.0
- **Fragments:** 4
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10

**Reconstructed Text:**

```
j
3PHorgan Cha
Range 
Market 
Vie. p
2014 
Perloc 
Currency )
High 
Low 
Avg 
Net (hg 
61.07 
03/24/14 
50.32 
09/24/13 
55.691 
17,850,442 
3.95 
7.18% 
L
P i
F 07/18/14 
F 06/27/14 
57.53 
10,178,566 F 06/06/14 
56.97 
15,399,844 
T 07/17/14 
T 06/26/14 
57.39 
11,854,621 T 06/05/14 
56.63 
16,804,644 
.4 07/16/14 
58.96 
10,865,787 
06/25/1-i 
57.53 
14,843,900'w 06.104/14 
55.68 
9,728,053 
T 07/15/14 
58.27 
36,219,126!T 06/24/14 
57.42 
12,323,320 T 06/03/14 
55.60 
9,132,297 
M 07/14/1.4 
56.29 
14,011,991 Ni 06/23/14 
58.19 
16,009,479 M 06/02/14 
55.35 
9,440,042 
F ('7/11/14 
55.80 
10,236,860 F 06/20/14 
57.55 
17,126,425 F 05/30/14 
55.57 
11,991,312 
T 07/10/14 
55.56 
12,436,589 T 06/19/14 
57.30 
11,624,383 T 05/29/14 
55.72 
11,741,707 
W 07/09/14 
56.02 
10,914,251'5.1 06/18/14 
57.78 
13,737,143 W 05/28/14 
55.45 
11,374,958 
T 07/08/14 
55.76 
18,345,729 T 06/17/14 
57.42 
11,200,522 T 05/27/14 
55.14 
14,503,732 
07/07/14 
56.67 
13,918,743 Ni 06/16/14 
56.87 
11,199,075 
05/26/14 
F 07/04/14 
F 06/13/14 
57.04 
12,044,435 F 05/23/14 
54.53 
10,878,697 
T 07/03/14 
57.05 
12,599,842 T 06/12/14 
57.04 
11,677,911 T 05/22/14 
54.55 
11,801,568 
W 07/02/14 
56.97 
19,199,260'W 06/11/14 
57.27 
14,232,17114 “5/21/14 
54.12 
13,210,922 
T 07/01/14 
57.57 
14,472,160 1. 06/10/14 
57.90 
11,609,169 T 05/20/14 
53.72 
16,888,227 
tri 06/30/14 
57.62 
11,549,859 
06/09/14 
57.42 
12,000,038 II 05/19/1-1 
53.83 
12,068,854 
ta 
Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 6000 
Japan 81 3 3201 8900 
Singapore 65 6212 WOO 
U.S. 1 212 318 2000 
Copyright 2014 Bloomberg Finance L.P. 
SH 264224 EDT 
GMT-4:00 H653-5263-2 16-Jul-2014 13:14:47
```

#### [139] [EFTA01461921](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01461921.pdf) -- Page 0

- **Interest Score:** 137.0
- **Fragments:** 4
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10

**Reconstructed Text:**

```
q
3PHorgan Cha
Range 
Market W1Wifflatiar
2014 
Renee 
Currency 
Da
LiS
E
a
P High 
Low 
Aug 
Net Chg 
61.07 
50.32 
55.691 
3.95 
03/24/14 
09/24/13 
17,850,442 
7.18% 
l
i
V l
F 07/18/14 
F k56/27/14 
57.53 
10,178,566 F 06/06/14 
56.97 
15,399,844 
T 07/17/14 
T 06/26/14 
57.39 
11,854,621 T 06/05/14 
56.63 
16,804,644 
07)16/1.1 
58.96 
10,865,787',•1 06/25/1.1 
57.53 
14,843,900W 06704/14 
55.68 
9,728,053 
T 07/15/14 
58.27 
36,219,126 T 06/24/14 
57.42 
12,323,320 T 06/03/14 
55.60 
9,132,297 
M 07/14/14 
56.29 
14,011,991 M 06/23/14 
58.19 
16,009,479 M 06/02/14 
55.35 
9,440,042 
F 07/11/14 
55.80 
10,236,860E 06/20/14 
57.55 
17,126,425 F 05/30/14 
55.57 
11,991,312 
T 07/10/14 
55.56 
12,436,589 T 06/19/14 
57.30 
11,624,383 T, 05/29/14 
55.72 
11,741,707 
07/09/14 
56.02 
10,914,251 
06/18/14 
57.78 
13,737,143W 05/26/14 
55.45 
11,374,958 
T 07/08/14 
55.76 
18,345,729 T 06/17/14 
57.42 
11,200,522 T 05/27/14 
55.14 
14,503,732 
N 07/07/14 
56.67 
13,918,743 M 06/16/14 
56.87 
11,199,075 lot 05/26/14 
F 07704/14 
F 06/13/14 
57.04 
12,044,435 F 05/ 23/14 
54.53 
10,878,697 i• 
T 07/03/14 
57.05 
12,599,842 T 06/12/14 
57.04 
11,677,911 T 05/22/14 
54.55 
11,801,5681 
W 07/02/14 
56.97 
19,199,260'W 06/11/14 
57.27 
14,232,171 W -T./21/1.4 
54.12 
13,210,922 
T 07/01/14 
57.57 
14,472,160.7 06/10/14 
57.90 
11,609,169 T 05/20/14 
53.72 
16,888,227 
06/30/14 
57.62 
11,549,859 N 06/09/14 
57.42 
12,000,038 N 05/19/14 
53.83 
12,068,854 
Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 6°00 
Japan 81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2014 Bloomberg Finance L P 
SN 264224 EDT GMT-4,00 H653-5263-2 16-Jul-2014 13.14 47
```

#### [140] [EFTA01461913](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01461913.pdf) -- Page 0

- **Interest Score:** 135.5
- **Fragments:** 5
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10

**Reconstructed Text:**

```
q
3Pflorgan Cha
Range 
Market W1Wifflatiar
2014 
?e nod 
Currency 
Da
LIS
E
p a High 
Low 
Aug 
Net Chg 
61.07 
50.32 
55.691 
3.95 
03/24/14 
09/24/13 
17,850,442 
7.18% 
i
V l
F 07/18/14 
F k56/27/14 
57.53 
10,178,566 F 06/06/14 
56.97 
15,399,844 
T 07/17/14 
T 06/26/14 
57.39 
11,854,621 T 06/05/14 
56.63 
16,804,644 
07)16/1.1 
58.96 
10,865,787',ri 06/2S/L1 
57.53 
14,843,900W 06704/14 
55.68 
9,728,053 
T 07/15/14 
58.27 
36,219,126 T 06/24/14 
57.42 
12,323,320 T 06/03/14 
55.60 
9,132,297 
M 07/14/14 
56.29 
14,011,991 M 06/23/14 
58.19 
16,009,479 M 06/02/14 
55.35 
9,440,042 
F Y17/11/14 
55.80 
10,236,860E 06/20/14 
57.55 
17,126,425 F 05/30/14 
55.57 
11,991,312 
T 07/10/14 
55.56 
12,436,589 T 06/19/14 
57.30 
11,624,383 T, 05/29/14 
55.72 
11,741,707 
)7/09/14 
56.02 
10,914,251 
06/18/14 
57.78 
13,737,143W 05/26/14 
55.45 
11,374,958 
07/08/14 
55.76 
18,345,729 T 06/17/14 
57.42 
11,200,522 T 05/27/14 
55.14 
14,503,732 
M 07/07/14 
56.67 
13,918,743 M 06/16/14 
56.87 
11,199,075 Dt 05/26/14 
F U7/ u4/14 
F 06/13/14 
57.04 
12,044,435 1 051 23/ 14 
54.53 
10,878,697 i• 
T 07/03/14 
57.05 
12,599,842 T 06/12/14 
57.04 
11,677,911 T 05/22/14 
54.55 
11,801,5681 
W 07/02/14 
56.97 
19,199,260'W 06/11/14 
57.27 
14,232,171 W -T./21/1.4 
54.12 
13,210,922 
T 07/01/14 
57.57 
14,472,160.7 06/10/14 
57.90 
11,609,169 T 05120/14 
53.72 
16,888,227 
El 06/30/14 
57.62 
11,549,859 rl 06/09/14 
57.42 
12,000,038 lit 05/19/14 
53.83 
12,068,854 
Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 6°00 
Japan 81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2014 Bloomberg Finance L P 
SN 264224 EDT 
GMT-4,00 H653-5263-2 16-Jul-2014 13. 14 47
All trade execution informationc
```

#### [141] [EFTA01447604](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01447604.pdf) -- Page 0

- **Interest Score:** 121.5
- **Fragments:** 29
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10

**Reconstructed Text:**

```
:1Phl US Eq
3PHorgan Cha
RaTge 
rarket 
D t rt to Excel 
Period 
Currency 
D t ' L
t P 4.Fetliback 
Historical Price 
High 
61.07 
03/24/14 
Low 
50.32 
09/24/13 
Avg 
55.691 
17,850,442 
Net C fig 
3.95 
7.18% 
V l
7!! D t P
ol me !
F 07
T 07
W u7
T 07
M 07 4 
0
4 
Ti06
4 
58.96 
10,865,787 WE 0
4 
58.27 
36,219,126,TI 0
4 
56.29 
14,011,991 MI 0 6/27/14 
6/26/14 
6/25/14 
6/24/14 
5
6/23/14 F 0
 T 0
to 0
T 0
H 0 4 
4 
4 
4 
4 7 
15,
3 
16,8
8 
9,7
0 
9,1
5 
9,4
F 07/1
T 07/1 1/14 
5
0/14
5 5.80 
10,2
5.56
12,4 236,860 F 06/20/14 
57.55 
17,1
436,589 T 06/19/14
57,30
11,6
4 5 F 0
3 T 0 4 
5
4
5 7 
11,991,31
2
11,741,70
4 
5
4 
5 8/14 
7/14 8 
1
2 
1 5 
11
4 
14
T1 07/0
F 07/0
T 07/0
07/0
T 07/0 T1 07/07/14 
56.67 
13,918,743 [1 06/16/14 
56.87 
11,199,075 M 05/26/14 
F 07/04/14 
F 06/13/14 
57.04 
12,044,435 F 05/23/14 
54.53 
10,878,697 
T 07/03/14 
57.05 
12,599,842,T1 06/12/14 
57.04 
11,677,911 T 05/22/14 
54,55 
11,801,568 
07/02/14 
56.97 
19,199,260'I'! 06/11/14 
57.27 
14,232,171 
05/21/14 
54.12 
13,210,922 
T 07/01/14 
57.57 
14,472,160 T 06/10/14 
57.90 
11,609,169 T 05/20/14 
53.72 
16,888,227 
M 06/30/14 
57.62 
11,549,859.M1 06/09/14 
57.42 
12,000,038 M 05/19/14 
53.83 
12,068,854 
Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 6000 
Japan 81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2014 Bloomberg Finance L.P. 
SH 264224 EDT GMT-4;00 H653-5263-2 16-Jul-2014 13;14.47 4 
56.67 
13,9
4 
4 
57.05 
12,5
4 
56.97 
19,
4 
57.57 
14,4 918,743 [1 0
F 0
599,842,T1 0
99,260'I'! 0
472,160 T 0 6/14 
3/14 
2/14 
5
/14 
0/14 7 
1
4 
1
4 
1
7 
1
0 
1 5 M 0
5 F 0
1 T 0
71 
0
9 T 0 4 
4 
5
4 
5
4 
5
4 
5 54.53 
10,878
54,55 
11,80
54.12 
13,21
53.72 
16,888
```

#### [142] [EFTA01461894](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01461894.pdf) -- Page 0

- **Interest Score:** 121.5
- **Fragments:** 29
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10

**Reconstructed Text:**

```
:1Phl US Eq
3PHorgan Cha
RaTge 
rarket 
D t rt to Excel 
Period 
Currency 
D t ' L
t P 4.Fetliback 
Historical Price 
High 
61.07 
03/24/14 
Low 
50.32 
09/24/13 
Avg 
55.691 
17,850,442 
Net C fig 
3.95 
7.18% 
V l
7!! D t P
ol me !
F 07
T 07
W u7
T 07
M 07 4 
0
4 
Ti06
4 
58.96 
10,865,787 WE 0
4 
58.27 
36,219,126,TI 0
4 
56.29 
14,011,991 MI 0 6/27/14 
6/26/14 
6/25/14 
6/24/14 
5
6/23/14 F 0
 T 0
to 0
T 0
H 0 4 
4 
4 
4 
4 7 
15,
3 
16,8
8 
9,7
0 
9,1
5 
9,4
F 07/1
T 07/1 1/14 
5
0/14
5 5.80 
10,2
5.56
12,4 236,860 F 06/20/14 
57.55 
17,1
436,589 T 06/19/14
57,30
11,6
4 5 F 0
3 T 0 4 
5
4
5 7 
11,991,31
2
11,741,70
4 
5
4 
5 8/14 
7/14 8 
1
2 
1 5 
11
4 
14
T1 07/0
F 07/0
T 07/0
07/0
T 07/0 T1 07/07/14 
56.67 
13,918,743 [1 06/16/14 
56.87 
11,199,075 M 05/26/14 
F 07/04/14 
F 06/13/14 
57.04 
12,044,435 F 05/23/14 
54.53 
10,878,697 
T 07/03/14 
57.05 
12,599,842,T1 06/12/14 
57.04 
11,677,911 T 05/22/14 
54,55 
11,801,568 
07/02/14 
56.97 
19,199,260'I'! 06/11/14 
57.27 
14,232,171 
05/21/14 
54.12 
13,210,922 
T 07/01/14 
57.57 
14,472,160 T 06/10/14 
57.90 
11,609,169 T 05/20/14 
53.72 
16,888,227 
M 06/30/14 
57.62 
11,549,859.M1 06/09/14 
57.42 
12,000,038 M 05/19/14 
53.83 
12,068,854 
Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 6000 
Japan 81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2014 Bloomberg Finance L.P. 
SH 264224 EDT GMT-4;00 H653-5263-2 16-Jul-2014 13;14.47 4 
56.67 
13,9
4 
4 
57.05 
12,5
4 
56.97 
19,
4 
57.57 
14,4 918,743 [1 0
F 0
599,842,T1 0
99,260'I'! 0
472,160 T 0 6/14 
3/14 
2/14 
5
/14 
0/14 7 
1
4 
1
4 
1
7 
1
0 
1 5 M 0
5 F 0
1 T 0
71 
0
9 T 0 4 
4 
5
4 
5
4 
5
4 
5 54.53 
10,878
54,55 
11,80
54.12 
13,21
53.72 
16,888
```

#### [143] [EFTA01461918](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01461918.pdf) -- Page 0

- **Interest Score:** 121.5
- **Fragments:** 29
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10

**Reconstructed Text:**

```
:1Phl US Eq
3PHorgan Cha
RaTge 
rarket 
D t rt to Excel 
Period 
Currency 
D t ' L
t P 4.Fetliback 
Historical Price 
High 
61.07 
03/24/14 
Low 
50.32 
09/24/13 
Avg 
55.691 
17,850,442 
Net C fig 
3.95 
7.18% 
V l
7!! D t P
ol me !
F 07
T 07
W u7
T 07
M 07 4 
0
4 
Ti06
4 
58.96 
10,865,787 WE 0
4 
58.27 
36,219,126,TI 0
4 
56.29 
14,011,991 MI 0 6/27/14 
6/26/14 
6/25/14 
6/24/14 
5
6/23/14 F 0
 T 0
to 0
T 0
H 0 4 
4 
4 
4 
4 7 
15,
3 
16,8
8 
9,7
0 
9,1
5 
9,4
F 07/1
T 07/1 1/14 
5
0/14
5 5.80 
10,2
5.56
12,4 236,860 F 06/20/14 
57.55 
17,1
436,589 T 06/19/14
57,30
11,6
4 5 F 0
3 T 0 4 
5
4
5 7 
11,991,31
2
11,741,70
4 
5
4 
5 8/14 
7/14 8 
1
2 
1 5 
11
4 
14
T1 07/0
F 07/0
T 07/0
07/0
T 07/0 T1 07/07/14 
56.67 
13,918,743 [1 06/16/14 
56.87 
11,199,075 M 05/26/14 
F 07/04/14 
F 06/13/14 
57.04 
12,044,435 F 05/23/14 
54.53 
10,878,697 
T 07/03/14 
57.05 
12,599,842,T1 06/12/14 
57.04 
11,677,911 T 05/22/14 
54,55 
11,801,568 
07/02/14 
56.97 
19,199,260'I'! 06/11/14 
57.27 
14,232,171 
05/21/14 
54.12 
13,210,922 
T 07/01/14 
57.57 
14,472,160 T 06/10/14 
57.90 
11,609,169 T 05/20/14 
53.72 
16,888,227 
M 06/30/14 
57.62 
11,549,859.M1 06/09/14 
57.42 
12,000,038 M 05/19/14 
53.83 
12,068,854 
Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 6000 
Japan 81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2014 Bloomberg Finance L.P. 
SH 264224 EDT GMT-4;00 H653-5263-2 16-Jul-2014 13;14.47 4 
56.67 
13,9
4 
4 
57.05 
12,5
4 
56.97 
19,
4 
57.57 
14,4 918,743 [1 0
F 0
599,842,T1 0
99,260'I'! 0
472,160 T 0 6/14 
3/14 
2/14 
5
/14 
0/14 7 
1
4 
1
4 
1
7 
1
0 
1 5 M 0
5 F 0
1 T 0
71 
0
9 T 0 4 
4 
5
4 
5
4 
5
4 
5 54.53 
10,878
54,55 
11,80
54.12 
13,21
53.72 
16,888
```

#### [144] [EFTA01457144](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01457144.pdf) -- Page 0

- **Interest Score:** 104.5
- **Fragments:** 7
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10

**Reconstructed Text:**

```
DBCMWSV2 
At 4/6 
,,1.., 019'3 
--
242.0493  
  242 0493 
242. 0493 
Prey 242 . 8579 Vol 0
dlaConymo
Range 
1134et 
V'em Mid Li
High 
Low 
Average 
'1H 
D
298.3815 
on 
226.1317 
on 
274.2436 
-40.3578 
L
P i
07/08/14 
02/05/15 
274.2436 
-14.29% 
P i
5 
5 
5 
5
T, 3/1
le/ 03/18
T 03/17 5 
 
5
II 04/06/15 
F 04/x:/15 
,T 04/02/15 
W 04/01/15 
T 03/31/15 
o3/3;ins 
F 03/27/15 
,T 03/26/15 
W 03/2S/15 
'T 03/24/15 
Pt 03/23/15 
242.0493 
242.8579 
242.6625 
243.5748 
243.6486 
243.9423 
246.3612 
251.4470 
253.5129 
251.7034 
242.0493 
03/16/15 
,,V13/15 
242.8579 T 03/12/15 
242.6625 W 03/11/15 
243.5748'T 03/10/15 
243.6486 II 03/09/15 
243.9423 
0:1/06/15 
246.3612 T 
VO5/15 
251.4470 W 03/04/15 
253.51291 03/03/15 
251.7034 II 03/02/1S 
244.5564! 
244.5564 
01723,71E-, 
236.8645 
236.8645 
244.0326 
244.0326 
n2i20/15 
239.5116 
239.5116 
248.1542 
248.1542 T 02/19/15 
237.9376 
237.9376 
247.2000 
247.2000 , 1 02/18/15 
239.0979 
239.0979 
244.3136 
244.3136 T 02/17/15 
248.1189 
248.1189 
0.1/16,15 
246.5216 
246.5216 F 02/1 
232.6301 
232.6301 
247.1434 
247.1434 T 02/12/15 
230.6760 
230.6760 
244.1153 
244.11534 02/11/15 
232.1317 
232.1317 
241.4693 
241.4693 T 02/10/15 
232.9251 
232.9251 
239.6651 
239.6651],l i'.109115 
235.6331 
235.6331 
Australia 61 2 9777 8600 Brazil 5511 2395 9000 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 6000 
Japan 81 3 3201 8900 
Singapore 65 6212 1000 
V.S. 1 212 318 2000 
Copyright 2015 Bloomberg Finance L.P. 
Stt 834224 EDT 
GMT-41;00 P703-5975-3 07 -Apr -2015 09;43;11 
'Used with Permission of Bloomberg Finance LP
07, 2015 9:15 AM
```

#### [145] [EFTA01447509](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01447509.pdf) -- Page 0

- **Interest Score:** 102.5
- **Fragments:** 7
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10
- **Names Found:** Maria, Jay

**Reconstructed Text:**

```
o• Last Price 
0.69 
T High on 10/23/09 4.6085 
-0- Average 
1.2225 
Low on 01/10/12 0.1498 
4.00 
3.00 
2.00 
nn 
0.69 
0.00
• Volume 
15.089M 
I ■ SMAVG (15) 33.801M 
200M 
100M 
5.08914 
2009 
2010 
2011 
203.2 
2013 
2014 
4,-"M!, GA ecJity (Alpha Sark At) Paily 27)VH2079-24XAZ014 
; 
-;; e 
1
 (15) 3
GRAB 
n Actions
99 Alert
Analyst Recommendations
55.12 
3.9 
13 
ho:xs 
27.34 
6 
Sells 
13.64 
3 
1214 Tgt Pi( 
17/23 
0.84 
last Price 
0.69 
Return Potential 
21.71 
LTH Return 
80.2% 
Show In-riouse Data 
on
10(- 
 
S0 ..
0 
0'00 
-0. So 4..
J 26! 14 
N. 0.80 
►0.60 
0.40 
0.20 
'
p
y
g
y
Euroxx Securities 
Maria Kanellopoulo 
overweight 
0.90 06/19/14 15.00% 1st 
1st 
Alpha Finance 
Nikolaos Lianeris 
restricted 
06/17/14 
I
Natixis 
Alex Koagne 
0.75 06/16/14 
I
Pantelakis Securities 
Paris Mantzavras 
overweight 
0.90 06/13/14 
Nomura 
Daragh Quinn 
buy 
0.75 06/12/14 
0.20% 2nd 
Credit Suisse 
Hugo Swann 
• neutral 
0.80 E;6/11/14 
I
Barclays 
Kid Vijayarajah 
• overweight 
0.92 06/10/14 
I
Goldman Sachs 
Pawel Dziedzic 
Buy/Neutral 
0.80 06/06/14 
l
mS8C 
Tamer Sengun 
t overweight 
0.87 06/06/14 
I
IBG Research (ESN) 
Konstantinos Man ol 
buy 
1.10 06/06/14 
Deutsche Bank 
Rahul Shah 
t buy 
0,90 06/04/14 
alia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 60
81 3 3201 13900 
Singapore 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2014 Bloomberg Finance L.
SN 622439 H622-433-3 26-Jun-14 14:11 .47 BST GAT41 ,
```

#### [146] [EFTA01447576](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01447576.pdf) -- Page 0

- **Interest Score:** 93.4
- **Fragments:** 5
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10
- **Names Found:** Maria, Jay

**Reconstructed Text:**

```
,
q
y
Alpha Bank AL 
FEE1989f74774,774-717477-71la 
611
Consensus Rating 
3.95 
Buys 
59.11 
13 
1 O) 4 
Holds 
27.34 
Setts 
13.69 
6 
3 
12M Tgt Px 
17/23 
0.84 
Last Price 
Return Potential 
0.69 
21.7% 
°Me l■
-0.50 
LTH Return 
80.2% 
J
Sh,p, 1r ,ss...se Data 
if
!Analyst Se
3 
gt Px y
Dec
153651 6/14 
'.'L
tt
lA• 0.60 
ie 0,40 
Ii• 0,20 
n 
nk!—
NO 00 & Company 
Alexandros Bouloug 
t . 
: :120/14 
Euroxx Securities 
Maria Kanellopoulo 
ovelwelght 
06/19/14 15.00% 1: t. 
1:4 L
Alpha Finance 
Nikolaos Lianeris 
restricted 
06/17/14 
k
Natixis 
Alex Koagne 
• 
0.75 06/16/14 
Pantelakis Securities 
Paris Mantzavras 
overaight 
0.90 06/13/14 
Nomura 
Daragh Quinn 
buy 
0.79 06/12/14 
0.20% 
t
Credit Suisse 
Hugo Swann 
• neutral 
0.80 06/11/14 
Barclays 
Kiri Vijayarajah 
• overweight 
0,92 06/10/14 
t
Goldman Sachs 
Paws'. Dziedzic 
Buy/Neutral 
0.80 06/06/14 
HSBC 
Tamer Sengun 
*overweight 
0.87 06/06/14 
L
IBri Research (ESN) 
Konstantinos Manol 
buy 
1.10 06/06/14 
Deutsche Bank 
Rahul Shah 
* buy 
0.90 06/04/14 
I
alia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 60
81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2014 Bloomberg Finance L.
SN 622439 H622-433-3 26-Jun-14 14,11 .47 BST 07+1,
```

#### [147] [EFTA01447501](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01447501.pdf) -- Page 0

- **Interest Score:** 92.6
- **Fragments:** 4
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10
- **Names Found:** Maria, Jay

**Reconstructed Text:**

```
Alpha Bank AE 
Consensus Rating 
3.95 
100 
Buys 
59.1% 
13 
Holds 
27.3% 
6 
50 
Sells 
13.6% 
3 
12M Tgt Px 
17/23 
0.84 
0 
Last Price 
0.69 
0.00
Return Potential 
21.7% 
- 0,S0 
LTM Return 
80.2% 
Show In-House Data 
J
Analyst 6/14 
x0.80 
►0,60 
0,40 
0,20 
•
 
nk
I) 
2) 
:3) 
4) 
5) 
6;
1) 
8) 
9) 
10) 
11) 
12) 
Aus
Jap Wood & Company 
Alexandros Bouloug 
buy 
U. yu OW 20/14 
 Euroxx Securities 
Maria Kanellopouto 
ovenAteight 
0.90 06/19/14 15.00% 
1st 
Alpha Finance 
Nikolaos Lianeris 
restricted 
06/17/14 
Natixis 
Alex Koagne 
• 
0.75 06/16/14 
Pantel.akis Securities 
Paris Mantzavras 
0veRveight 
0.90 06/13/14 
 Nomura 
Daragh Quinn 
buy 
0.75 06/12/14 
0.20% 
Credit Suisse 
Hugo Swann 
• neutral 
0.80 06/11/14 
Barclays 
Kiri Vijayarajah 
• overweight 
0.92 06/10/14 
Goldman Sachs 
Pawel Dziedzic 
Buy/Neutral 
0.80 06/06/14 
HSBC 
 IBG Research (ESN) 
Tamer Sengun 
Konstantinos Manol 
overweight 
buy 
0.87 
1.10 
06/06/14 
06/06/14 
E
k
Deutsche Bank 
Rahul Shah 
t buy 
0.90 06/04/14 
ralia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 60
n 81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2014 Bloomberg Finance L.
SN 622439 H622-433-3 26-Jun-14 14, 11 ,47 BST GMT+1 ,
```

#### [148] [EFTA01447518](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01447518.pdf) -- Page 0

- **Interest Score:** 92.6
- **Fragments:** 4
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10
- **Names Found:** Maria, Jay

**Reconstructed Text:**

```
Alpha Bank AE 
Consensus Rating 
3.95 
100 
Buys 
59.1% 
13 
Holds 
27.3% 
6 
50 
Sells 
13.6% 
3 
12M Tgt Px 
17/23 
0.84 
0 
Last Price 
0.69 
0.00
Return Potential 
21.7% 
- 0,S0 
LTM Return 
80.2% 
Show In-House Data 
J
Analyst 6/14 
x0.80 
►0,60 
0,40 
0,20 
•
 
nk
I) 
2) 
:3) 
4) 
5) 
6;
1) 
8) 
9) 
10) 
11) 
12) 
Aus
Jap Wood & Company 
Alexandros Bouloug 
buy 
U. yu OW 20/14 
 Euroxx Securities 
Maria Kanellopouto 
ovenAteight 
0.90 06/19/14 15.00% 
1st 
Alpha Finance 
Nikolaos Lianeris 
restricted 
06/17/14 
Natixis 
Alex Koagne 
• 
0.75 06/16/14 
Pantel.akis Securities 
Paris Mantzavras 
0veRveight 
0.90 06/13/14 
 Nomura 
Daragh Quinn 
buy 
0.75 06/12/14 
0.20% 
Credit Suisse 
Hugo Swann 
• neutral 
0.80 06/11/14 
Barclays 
Kiri Vijayarajah 
• overweight 
0.92 06/10/14 
Goldman Sachs 
Pawel Dziedzic 
Buy/Neutral 
0.80 06/06/14 
HSBC 
 IBG Research (ESN) 
Tamer Sengun 
Konstantinos Manol 
overweight 
buy 
0.87 
1.10 
06/06/14 
06/06/14 
E
k
Deutsche Bank 
Rahul Shah 
t buy 
0.90 06/04/14 
ralia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 60
n 81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2014 Bloomberg Finance L.
SN 622439 H622-433-3 26-Jun-14 14, 11 ,47 BST GMT-4-1
```

#### [149] [EFTA01447526](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01447526.pdf) -- Page 0

- **Interest Score:** 92.6
- **Fragments:** 4
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10
- **Names Found:** Maria, Jay

**Reconstructed Text:**

```
Alpha Bank AE 
Consensus Rating 
3.95 
100 
Buys 
59.1% 
13 
Holds 
27.3% 
6 
50 
Sells 
13.6% 
3 
12M Tgt Px 
17/23 
0.84 
0 
Last Price 
0.69 
0.00
Return Potential 
21.7% 
- 0,S0 
LTM Return 
80.2% 
Show In-House Data 
J
Analyst 6/14 
x0.80 
►0,60 
0,40 
0,20 
•
 
nk
I) 
2) 
:3) 
4) 
5) 
6;
1) 
8) 
9) 
10) 
11) 
12) 
Aus
Jap Wood & Company 
Alexandros Bouloug 
buy 
U. yu OW 20/14 
 Euroxx Securities 
Maria Kanellopouto 
ovenAteight 
0.90 06/19/14 15.00% 
1st 
Alpha Finance 
Nikolaos Lianeris 
restricted 
06/17/14 
Natixis 
Alex Koagne 
• 
0.75 06/16/14 
Pantel.akis Securities 
Paris Mantzavras 
0veRveight 
0.90 06/13/14 
 Nomura 
Daragh Quinn 
buy 
0.75 06/12/14 
0.20% 
Credit Suisse 
Hugo Swann 
• neutral 
0.80 06/11/14 
Barclays 
Kiri Vijayarajah 
• overweight 
0.92 06/10/14 
Goldman Sachs 
Pawel Dziedzic 
Buy/Neutral 
0.80 06/06/14 
HSBC 
 IBG Research (ESN) 
Tamer Sengun 
Konstantinos Manol 
overweight 
buy 
0.87 
1.10 
06/06/14 
06/06/14 
E
k
Deutsche Bank 
Rahul Shah 
t buy 
0.90 06/04/14 
ralia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 60
n 81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2014 Bloomberg Finance L.
SN 622439 H622-433-3 26-Jun-14 14, 11 ,47 BST GMT-4-1
```

#### [150] [EFTA01447570](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01447570.pdf) -- Page 0

- **Interest Score:** 92.6
- **Fragments:** 4
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10
- **Names Found:** Maria, Jay

**Reconstructed Text:**

```
Alpha Bank AE 
Consensus Rating 
3.95 
100 
Buys 
59.1% 
13 
Holds 
27.3% 
6 
50 
Sells 
13.6% 
3 
12M Tgt Px 
17/23 
0.84 
0 
Last Price 
0.69 
0.00
Return Potential 
21.7% 
- 0,S0 
LTM Return 
80.2% 
Show In-House Data 
J
Analyst 6/14 
x0.80 
►0,60 
0,40 
0,20 
•
 
nk
I) 
2) 
:3) 
4) 
5) 
6;
1) 
8) 
9) 
10) 
11) 
12) 
Aus
Jap Wood & Company 
Alexandros Bouloug 
buy 
U. yu OW 20/14 
 Euroxx Securities 
Maria Kanellopouto 
ovenAteight 
0.90 06/19/14 15.00% 
1st 
Alpha Finance 
Nikolaos Lianeris 
restricted 
06/17/14 
Natixis 
Alex Koagne 
• 
0.75 06/16/14 
Pantel.akis Securities 
Paris Mantzavras 
0veRveight 
0.90 06/13/14 
 Nomura 
Daragh Quinn 
buy 
0.75 06/12/14 
0.20% 
Credit Suisse 
Hugo Swann 
• neutral 
0.80 06/11/14 
Barclays 
Kiri Vijayarajah 
• overweight 
0.92 06/10/14 
Goldman Sachs 
Pawel Dziedzic 
Buy/Neutral 
0.80 06/06/14 
HSBC 
 IBG Research (ESN) 
Tamer Sengun 
Konstantinos Manol 
overweight 
buy 
0.87 
1.10 
06/06/14 
06/06/14 
E
k
Deutsche Bank 
Rahul Shah 
t buy 
0.90 06/04/14 
ralia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 60
n 81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2014 Bloomberg Finance L.
SN 622439 H622-433-3 26-Jun-14 14, 11 ,47 BST GMT+1 ,
```

#### [151] [EFTA01454578](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01454578.pdf) -- Page 0

- **Interest Score:** 92.6
- **Fragments:** 4
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10
- **Names Found:** Maria, Jay

**Reconstructed Text:**

```
Alpha Bank AE 
Consensus Rating 
3.95 
100 
Buys 
59.1% 
13 
Holds 
27.3% 
6 
50 
Sells 
13.6% 
3 
12M Tgt Px 
17/23 
0.84 
0 
Last Price 
0.69 
0.00
Return Potential 
21.7% 
- 0,S0 
LTM Return 
80.2% 
Show In-House Data 
J
Analyst 6/14 
x0.80 
►0,60 
0,40 
0,20 
•
 
nk
I) 
2) 
:3) 
4) 
5) 
6;
1) 
8) 
9) 
10) 
11) 
12) 
Aus
Jap Wood & Company 
Alexandros Bouloug 
buy 
U. yu OW 20/14 
 Euroxx Securities 
Maria Kanellopouto 
ovenAteight 
0.90 06/19/14 15.00% 
1st 
Alpha Finance 
Nikolaos Lianeris 
restricted 
06/17/14 
Natixis 
Alex Koagne 
• 
0.75 06/16/14 
Pantel.akis Securities 
Paris Mantzavras 
0veRveight 
0.90 06/13/14 
 Nomura 
Daragh Quinn 
buy 
0.75 06/12/14 
0.20% 
Credit Suisse 
Hugo Swann 
• neutral 
0.80 06/11/14 
Barclays 
Kiri Vijayarajah 
• overweight 
0.92 06/10/14 
Goldman Sachs 
Pawel Dziedzic 
Buy/Neutral 
0.80 06/06/14 
HSBC 
 IBG Research (ESN) 
Tamer Sengun 
Konstantinos Manol 
overweight 
buy 
0.87 
1.10 
06/06/14 
06/06/14 
E
k
Deutsche Bank 
Rahul Shah 
t buy 
0.90 06/04/14 
ralia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 60
n 81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2014 Bloomberg Finance L.
SN 622439 H622-433-3 26-Jun-14 14, 11 ,47 BST GMT+1 ,
```

#### [152] [EFTA01447505](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01447505.pdf) -- Page 0

- **Interest Score:** 92.3
- **Fragments:** 6
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10
- **Names Found:** Maria, Jay

**Reconstructed Text:**

```
GRAB 
99 A i
99 Al
611
q
y
Alpha Bank AL 
FRESSOlf74-777-4,777-4-7174-7-71W 
Consensus Rating 
3.95 
100 4 
Buys 
59.11 
13 
Holgs 
27.34 
6 
Setts 
13.69 
3 
12M Tgt Px 
17/23 
0.84 
Last Price 
0.69 
Return Potential 
21.7% 
°Me l■
-0.50 At._
MI Return 
80.2% 
J
Sh,p, 1r- 
a4ta 
if
1 '
Analyst Se
3 
gt Px y
Dec
15arrb 6/14 
'.'L
tt
l! 0.60 
0,40 
0,20 
n 
nk!—
Od & Company 
Euroxx 
Alexandros Bouloug 
t . 
: :120/14 
Securities 
Maria Kanellopoulo 
overweight 
06/19/14 15.00% 1:t. 
1st L
Alpha Finance 
Nikolaos Lianeris 
restricted 
06/17/14 
Natixis 
Alex Koagne 
• r,: i,i;oe 
0.75 06/16/14 
Pantelakis Securities 
Paris Mantzavras 
overweight 
0.90 06/13/14 
jr
Nomura 
Daragh Quinn 
buy 
0.79 06/12/14 
0.20% 
t
Credit Suisse 
Hugo Swann 
• neutral 
0.80 06/11/14 
Barclays 
Kiri Vijayarajah 
• overweight 
0,92 06/10/1a 
Goldman Sachs 
Pawel Dziedzic 
Buy/Neutral 
0.80 .6/06/14 
L
HSBC 
Tamer Sengun 
*overweight 
0.87 06/06/14 
L
I8G Research (ESN) 
Konstantinos Manol 
buy 
1.10 06/06/14 
Deutsche Bank 
Rahul. Shah 
't buy 
0.90 06/04/14 
I
alia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 60
81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2014 Bloomberg Finance L.
SN 622439 H622-433-3 26-Jun-14 14'1147 BST 07+1,
```

#### [153] [EFTA01461891](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01461891.pdf) -- Page 0

- **Interest Score:** 90.8
- **Fragments:** 25
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10

**Reconstructed Text:**

```
tiorgan Cha
D port to Excel 
I^ 
D
D
l ligEr 
High 
r 
low 
Net Chg 
61.07 
50.32 
55.691 
3.95 
Historical Price 
03/24/14 
09/24/13 
17,850,442 
7.18%
T 07/17/14
T 0 i 
6/14 10,178,5
11 854 66 F 06/06/14 
56
621 T 06/05/14
56 97 
63
15,399,844 
16 804 644
W 07
T 07
H 07
F 07
T 07 4 
58
4 
58
4 
56
4 
55
4
55 96 
1
7 
3
29 
1
80 
1
56
1 4/i4 
3/14 
2/14 
/1.4 
9/14 8 
0 
5 
7 
2
9,7
9,1
9,4
11,9
11,7
07/09/14 
56.02 
10
T 07/08/14
55 76
18 51:.d o6/18/14 
729: T 06/17/14 57.78 
13,737,14314 0
57 42
11 200 522 T 0 8/14 
7/14
5 5 
11,374,9
14 503 7
T 07
M 07
F 07
T 07 4 
55.76 
1
4 
56.67 
1
4 
4 
57.05 
1 ,729: T 
,743 H 
,842 2 
11
11
12
11 /14 
55.14 
/14 
/14 
54.53 
/14 
54.55 4,503,732 
0,878,697 
1,801,568
56.97 
19,199,260 
06/11/14 
57.27 
14,232,171 W OS/ 21/14 
54.12 
T 07/01/14 
57.57 
14,472,160 T 06/10/14 
57.90 
11,609,169 T 05/20/14 
53.72 
M 06/'O/14 
57.62 
11,549,859 M 06/09/14 
57.42 
12,000,038 N 05/19/14 
53.83 
13,210,922 
16,888,227 
12,068,854 
Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 6000 
Japan 81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2014 Bloomberg Finance L.P. 
SN 264224 EDT 
GMT-4;00 H653-5263-2 16-Jul-2014 13,14.47
```

#### [154] [EFTA01457132](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01457132.pdf) -- Page 0

- **Interest Score:** 90.2
- **Fragments:** 20
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10

**Reconstructed Text:**

```
DBC(144.5V7 
At 4/6 
-242 -J-It,•3 
24. 0493 
illr'0 11 721711111'7111111
9
E P
t tO Excel
242.8579 
Page 1/6
Historical Price Table"
ange 
arket L
High 
298.3815 
on 07/08/14 
Low 
226.1317 
on 02/05/15 
Average 
274.2436 
274.2436 
Net Ch 
-40.3578 
-14.29% 
Price
Hid
MI
L
F 04/10/15 
04/09/15 
T 03/1
04/
W 2
/27/15 
3
2/26/15 
23
_.
5 
T 03
5 
242.0493 
242.0493 M 03
5 
F 03
5 
242.8579 
242.8579'T 03
5
242 6625
242 6625W 03 5 
 
 
5 
5 , 
5 
5 
5
w 04/ 1j1/15 
242.662
T 03/31/15 
243.574 5 
242
8 
243 25W 03/11/15 
247.2
48 T 03/10/15 
244.3 0 
247.2
6 
244.3 0 2J 02112/15 
239.0979
6 T 02117/15 39.0979
M 03
F 03
03
w 03 5 
2
2
5 
2
5
2 m 03/
3 F 03/
2'T 03/
0 W03/ 232.6301 
232.6301 
230.6760 
230.6760 
232 1317
232 1317
T 03/24/16 
253.5129 
253.5129 T 03/03/15 
241.4693 
241.4693 
02/10/15 
232.9251 
232.9251 
03/23/15 
251.7034 
251.7034 N u3/02/15.; 
239.6651 
239.6651 
027.)9/15 
235.6331 
235.6331 
Australia 61 2 9777 8600 Brazil 5511 2395 9000 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 6000 
Japan 81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2015 Bloomberg Finance L.P. 
Sn 834224 EDT GMT-4,00 N703-5975-3 07-Apr-2015 09,43, 11 
*Used with Permission of Bloomberg Finance LP
5 9:15 AM
```

#### [155] [EFTA01455007](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01455007.pdf) -- Page 0

- **Interest Score:** 88.4
- **Fragments:** 32
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10

**Reconstructed Text:**

```
CL1 197.87 
+.49 
At 9:28 
d Val 44081 
ic97.86 /97.87 is 
4x7 
97.38 
97.62 
97.88 
97.33 
243837 
96) E
E
l
Generic 1st 'C
D t Period 
Currercv 
D t
L
t High 
110.53 
09/06/13 
Low 
91.66 
01/09/14 
Avg 
100.96 
100.86 
Net Chg 
-7.45 
-7.08% 
Bid P i
'
D t
L
t P i
Bid P i
F 
103
7/14
T 07/17/14
103 102.82 
105.74 
9
103 71
06/26/14
105 84
4 
4 
97
4
97 .85 
.38 4 
1
4 
1
4 14 
1
14 
14
1 4 
0 
3
4/14 
9
/14 
9
/14 
9
0/14
10 4 
10
4 
100
4 
102
4
102 1
1
1
1 3/14 
1
0/14 
10
9/14 
1
8/14
1 7 
10
6 
3 
106
7
106 6.01 
6.20 
6 02
1.4 0
T 0
M 0
F 0
T 0 0/14 
100
9/14 
100
/14 
101
5;14 
102
4/14 
102 7 
7 
10
7 
10
 
10
7 
10 ! 07/0
T 07/0
M 07/0
07/0
T 07/0 9/14 
102.29 
101.8714 06/18/14 
10
8/14 
103.40 
103.36 T 06/17/14 
10
7/14 
103.53 
103.31 Ni 06/16/14 
10
4/14 
F 06/13/14 
10
3/14 
104.06 
103.93 "T 06/12/14 
10 7 
106
6 
106
0 
106
1 
106
3 
106
3/14 
1
2/14 
1
/14
1 4 
1
4 
1
4
1 1
 
1
1 0 
5 
1
M 07/21/14 
104.59 
104.53 M 06/30/14 
105.37 
105.50 Ni 06/09/14 
104.41 
104.47 
Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 7500 Germany 49 69 9204 1210 Hong Kong 852 2977 6000 
Japan 81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 318 2000 
Copyright 2014 Bloomberg Finance L.P. 
SN 264224 EDT GMT-4,00 H705-2594-1 06-Aug-2014 09,2.8,2S /14 
104 .59 
10 0/14 
10 /09/14
```

#### [156] [EFTA01655769](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01655769.pdf) -- Page 1

- **Interest Score:** 74.7
- **Fragments:** 5
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10
- **Names Found:** Les, Kevin, New York

**Reconstructed Text:**

```
molested ue to the recent unsea
UP3 Letters: 
14466832-0 sent to Mark Niquette of Bloomberg News on 09/18/2019 
1445706-0 sent to Jake Morphonios on 08/30/2019 
1445379-0 sent to The New York Times' Mike Baker on 08/29/2019 
1445138-0 sent to ABC New's Halley Frequer on 08/23/2019 
1443697-0 sent to Radical Media's Kevin Garnett on 08/06/2019 
1434434-0 sent to Radical Media's Kevin Garnett on 04/23/2019 
1469049-0 sent to Walden, Macht & Haran LLP's Marc Armas on 
07/08/2020 
1471456-0 sent to Mary Arnold on 07/28/2020 
1434521-0 sent to Thomas Volscho on 04/16/2019
1476604-0 sent to Thomas McCawley of Boies, Schiller and Flexner 
LLP re•resentin• 
on 09/25/2020 
SIOC, The Independent
Why didn't the
```

#### [157] [EFTA01368602](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01368602.pdf) -- Page 0

- **Interest Score:** 63.2
- **Fragments:** 4
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10

**Reconstructed Text:**

```
Reference: 
FEDERATIVE REPUBLIC OF BRAZIL 
Counterparty: 
SOUTHERN FINANCIAL LLC 
Business days: 
LDN,NYC 
Business days adj: 
Following 
Buy,Siff I: 
Sell 
Notional: 
USD 10mm 
Effective date: 
14-Jan-2015 
Maturity date: 
20-Mar-2020 
Day count: 
Af360 
Payment lreq: 
Quarterly 
Pay accrued: 
True 
Curve recovery: 
True 
Recovery rate: 
0.25 
Deal rate. 
100 
Calculator 
Valuation date: 
13-Jan-2015 
Cash settled on: 
16-Jan-2015 
Price: 
Principal: 
Accrued: 
Market Val: 
Curve date: 
13-Jan.2015 
Benchmark: 
USD 
0 
Use flat curve 
Date 
20-Sep-2015 
Spread (bps) 
205.00 
20-Mar-2016 
205.00 
20-Mar-2017 
205.00 
20-Mar-2018 
205.00 
20-Mar-2019 
205.00 
20-Mar-2020 
205.00 
20-Mar-2022 
205.00 
20-Mar-2025 
205.00 
95.01670000 
Repl sprd: 
205 
498.330.00 
Sprd DV01: 
-4.576.8268824283 
Frequency: 
O 
-6.389.00 
Days: 
23 
Day count: 
A/360 
491,941 
IR DV01: 
-129.8125752157 
Recovery rate: 
0.4 FE
ty: 
SO
ays: 
LD
ays adj: 
Fo
US
ate: 
14
te: 
20
eq: 
Qu
d: 
Tr
very: 
Tr
ate: 
0.2
10
ator 
ate: 
13-Jan
d on: 
16-Ja
95.016
498.33
-6.389
491,94 ATIVE REPUBLIC OF BRAZIL 
ERN FINANCIAL LLC 
C 
ng 
Buy,Siff I: 
Sell 
mm 
2015 
2020 
Day count: 
Af360 
ly 
5 
5 
Curv
Ben
0 
0 
Repl sprd: 
205 
Sprd DV01: 
-4.576.8268824283 
Freq
Days: 
23 
Day
IR DV01: 
-129.8125752157 
Rec te: 
13-Jan.20
rk: 
USD 
flat curve 
ate 
p-2015 
Sprea
20
r-2016 
20
r-2017 
20
r-2018 
20
r-2019 
20
r-2020 
20
r-2022 
20
r-2025 
20
y: 
O 
t: 
A/360 
rate: 
0.4
```

#### [158] [EFTA01477029](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01477029.pdf) -- Page 0

- **Interest Score:** 62.9
- **Fragments:** 17
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10
- **Names Found:** Paul, New York

**Reconstructed Text:**

```
Classi
v sory 
Depos is 
0 01089 0 01248 49 98
y 
Depos is 
1.6E-4
47.64386213
Adv 
DPWGP 
1.839
Adv 
DPWGP 
67.86186973
Adv 
DPBIA 
1.83
0 
72058 
0
0 
0 
DPWGP
. 
US O
h
1420972.07273 
0 
h Ivtmt
‘.
.
x 
496 
85.3490 3502 
k
.34742 
C ass 
A visory 
0 
0
. 
Americas
isory 
epos 
4.0E-5 48.96959804 
East Coast
USO N
ast
13 0:00 1438785.5893
USO New York
3 0:00 1742138.46
US Onshore y
o e age
0 
0 
USO New York 
Paul
```

#### [159] [EFTA01731006](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01731006.pdf) -- Page 3

- **Interest Score:** 57.4
- **Fragments:** 20
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10
- **Names Found:** Epstein, Black, New York

**Reconstructed Text:**

```
31E-MM-108062 SERIAL 230 --
he pa
Her Florida driver' xpires on 
e
porary driver's license, a references 
es the address of 
expired
one numbe mployed
-
telephone number
flE/FOUt/
2015
t
t
mpting to blackmail powerful businessmen in New York. O 5, EPSTEIN replies to
that he ha re 
and that he 
d to contact
e
name of
interested meet wit 
uring is upcoming trip a
STEIN offers to provide contacts, presumably f
s
STEIN suggests names of individu
PSTEIN& has a contact t
ONS 2014
e interactions from
eeting with In respo
```

#### [160] [EFTA02730741](https://www.justice.gov/epstein/files/DataSet%2012/EFTA02730741.pdf) -- Page 127

- **Interest Score:** 53.9
- **Fragments:** 11
- **Document Type:** PHONE_RECORD
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, New York

**Reconstructed Text:**

```
e 
date of birth 
e 
me
f
l i h
60' (A
H
T
ffi ki
(NY) O 07/09/2019
e 
e 
PROTECT IDENTITY 
e 
e 
mes 
cellular telephone 
me an anonymous male caller (Anonymous)
or EpsteinOn 07/08/2019 at 12:0
e Anonymous Internet ddress
e 
PROTECTIDENTITY] date of
n Trafficking(NY)On07/08/2019,at 6:23 p.m
, an Anonymous malecaller called the
e 
e 
date of birth 
e 
m. Eastern Time 
e 
e 
hone 
me 
e 
eet, New York, New York 10021
```

#### [161] [EFTA01365753](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01365753.pdf) -- Page 0

- **Interest Score:** 53.9
- **Fragments:** 10
- **Document Type:** PHONE_RECORD
- **Dataset:** ds10

**Reconstructed Text:**

```
formation
ty: 
ays: 
ays adj: 
te: 
e.
eq: 
d: 
very: 
ate: 
ator
FE
SO
L0
Fo
US
14
20
Qu
Tr
Tr
0.2
10 ATIVE REPUBLIC OF BRAZIL 
ERN FINANCIAL LLC 
C 
g 
mm 
2015 
2020 
y 
Buy/Sell: 
Sell 
Day count: 
A1300 
Spr
Curv
Ben
D 13,Rin-201
USD 
curve 
Sprea
5 
20
i 
20
7 
20
8 
20
20
20
20
0 
9 
2 
5 
20 5 
(bps) 
.00 
.00 
.00 
.00 
.00 
.00 
.00 
.00
(Calculator 
Valuation date: 
13-Jan-2015 
Cash settled on: 
16-Jan-2015 
Price: 
95.01670000 
Principal: 
498.330.00 
Accrued: 
-6,389.00 
Market Val: 
491.941 
Repl sprd: 
Sprd DV01: 
Days: 
IR DV01: 
205 
-4,576.8268824283 
23 
4292125752157 
Frequency: 
Day count 
A/360 
Recovery rate: 
0.4 culator 
on date: 
1
ettled on: 
16
95
pal: 
49
ed: 
-6
Val: 
4 2015 
-2015 
70000 
0.00 
00 
 
R
S
D
IR prd: 
DV01: 
1: 
205 
-4,576.8268824283 
23 
4292125752157 Frequen
Day cou
Recovery
d
i
i f
i
```

---

### OTHER (39 pages)

#### [162] [EFTA01461028](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01461028.pdf) -- Page 0

- **Interest Score:** 127.0
- **Fragments:** 6
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
SPY US 03/20/15 P186 
$ T7.17 +.54 
,I At 10:25 
Oplrit 7,411 
Vol 86 
SPY US E Li
07.16 /7.25 
535 x243 
0 6.67A H 7.171, 1. 6.67A Prey 6.63 
97) E
i
O
i
M
i
O
i
M
i
TF 
1191 40 
-1
lti 
ll Option
to 191.39
tioneyrie Monitor: Option Monitor 
9 
Volm 56156770 
HV 13.43 
f. 
P t
.31) SP'i 3/20/15 C1SO 
15.9':5.8 19 5".- .73 
440 
180.00 136) SPY 3/20/15 P180 
5.40 5.45 5.11 19.30 -.32 
518 286
32) SPY 3/20/15 C181 
14.9 15.2:19.4:19.26 .69 
313 
181.00 107) SPY 3/20/15 P181 
5.66 5.72 5.32 19.06 -.33 
32 23 
33) SPY 3/20/15 0182 
14.2 14.4414.4 19 02 .68 
10 1299 
182.00 108) SPY 3/20/15 P182 
5.936.00 5.38!1.8.81 -.35 
39 
34) SPY 3/20/15 C183 
13.5 13.7414.5=18.73.66 
850 
183.00 109) SPY 3/20/15 P183 
6.226.32 6.21 18.56 -.36 
127 
35) SPY 3/2.0/15 C184 
12.8 13.0;12.948.53 .64 
10 1278 
184.00 110) SPY 3/20/15 P184 
6.52 6.59 6.12 18.34 -.38 
252 4 
36) SPY 3/20/15 C185 
12.0 12.3:12.5118.20.63 
94 3317 
185.00 111) SPY 3/20/15 P185 
6.83 6.91 6.64 18.07 -.39 
731 
37) SPY 3/20/15 C186 
11.3 11.6:11..9(18.08.61 
30 1380 
186.00 112) SPY 3/20/15 P186 
7.16 7.25 7.17 17.84 -.41 
86 74 
38) SPY 3/20/15 0187 
10.7 10.8110.8:17.74'.59 
10 2905 
187.00 113) SPY 3/20/15 P187 
7.50 7.59 7.30 17.60 -.43 
29 12 
39) SPY 3/20/15 C188 
10.0 10.1'10.7117.42 .58 
1 1964 
188.00 114) SPY 3/20/15 P188 
7.86 7.99 7.90 17.36 -.44 
195 49 
40) SPY 3/20/15 C189 
9.44 9.53 10.2=17.17.56 
1343 
189.00 115) SPY 3/20/15 P189 
8.23 8.32 7.70 17.11 -.46 
143 1 
41) SPY 3/20/15 C190 
8.78 8.92 8.89 16.97 .54 
58 5658 
190.00 116) SPY 3/20/15 P190 
8.63 8.74 8.61 16.88 -.48 
256 13 
42) SPY 3/20/15 C191 
8.22 8.31 9.10 16.74 .52 
59 2120 
191.00 117) SPY 3/20/15 P191 
9.04 9.14 8.47 16.63 -. 50 
62 16 
43) SPY 3/20/15 0192 
7.61 7.72 8.44 16.46'.50 
21 5681 
192.00 118) SPY 3/20/15 P192 
9.479.58 9.33 16.37 -. 52 
300 82 
44) SPY 3/20/15 C193 
45) SPY 3/20/15 C194 
7.03 
6.48 
7.14 7.76 16.21 .48
6
6.60 .53 15.96 .46 
12 
87 
2643 
1446 
193.00 
194.00 
119) SPY 3/20/15 
120) SPY 3/20/15 
P193 
P194 
9.92 10.0:9.87 16.11 
10.3'10.4'9.65 15.83 
-. 54 
-.56 
27 31 
52 
46) SPY 3/20/15 0195 
5.95 6.08 6.00 15.72 .44 
6 6988 
195.00 121) SPY 3/20/15 P195 
io.8:10.9.10.8(15.67 -.58 
144 25 
47) SPY 3/20/15 C196 
5.45 5.57 5.81 15.50 .41 
33 4486 
196.00 122) SPY 3/20/15 P196 
11.3'11.4411.0'15.39 -.60 
208 22 
48) SPY 3/20/15 C197 
4.97 5.08 5.00 15.27 .39 
29 4604 
197.00 123) SPY 3/20/15 P197 
11.8:12.0'10.4415.10 -.63 
37 
49) SPY 3/20/15 C198 
4.51 4.63 4.77 15.02 .37 
28 10162 
198.00 " 
93) 0,7,' 
Color Legend 
Zoom 
004,
```

#### [163] [EFTA01462260](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01462260.pdf) -- Page 0

- **Interest Score:** 127.0
- **Fragments:** 6
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
SPY US 03/20/15 P186 
$ T7.17 +.54 
,I At 10:25 
Oplrit 7,411 
Vol 86 
SPY US E Li
07.16 /7.25 
535 x243 
0 6.67A H 7.171, 1. 6.67A Prey 6.63 
97) E
i
O
i
M
i
O
i
M
i
TF 
1191 40 
-1
lti 
ll Option
to 191.39
tioneyrie Monitor: Option Monitor 
9 
Volm 56156770 
HV 13.43 
f. 
P t
.31) SP'i 3/20/15 C1SO 
15.9':5.8 19 5".- .73 
440 
180.00 136) SPY 3/20/15 P180 
5.40 5.45 5.11 19.30 -.32 
518 286
32) SPY 3/20/15 C181 
14.9 15.2:19.4:19.26 .69 
313 
181.00 107) SPY 3/20/15 P181 
5.66 5.72 5.32 19.06 -.33 
32 23 
33) SPY 3/20/15 0182 
14.2 14.4414.4 19 02 .68 
10 1299 
182.00 108) SPY 3/20/15 P182 
5.936.00 5.38!1.8.81 -.35 
39 
34) SPY 3/20/15 C183 
13.5 13.7414.5=18.73.66 
850 
183.00 109) SPY 3/20/15 P183 
6.226.32 6.21 18.56 -.36 
127 
35) SPY 3/2.0/15 C184 
12.8 13.0;12.948.53 .64 
10 1278 
184.00 110) SPY 3/20/15 P184 
6.52 6.59 6.12 18.34 -.38 
252 4 
36) SPY 3/20/15 C185 
12.0 12.3:12.5118.20.63 
94 3317 
185.00 111) SPY 3/20/15 P185 
6.83 6.91 6.64 18.07 -.39 
731 
37) SPY 3/20/15 C186 
11.3 11.6:11..9(18.08.61 
30 1380 
186.00 112) SPY 3/20/15 P186 
7.16 7.25 7.17 17.84 -.41 
86 74 
38) SPY 3/20/15 0187 
10.7 10.8110.8:17.74'.59 
10 2905 
187.00 113) SPY 3/20/15 P187 
7.50 7.59 7.30 17.60 -.43 
29 12 
39) SPY 3/20/15 C188 
10.0 10.1'10.7117.42 .58 
1 1964 
188.00 114) SPY 3/20/15 P188 
7.86 7.99 7.90 17.36 -.44 
195 49 
40) SPY 3/20/15 C189 
9.44 9.53 10.2=17.17.56 
1343 
189.00 115) SPY 3/20/15 P189 
8.23 8.32 7.70 17.11 -.46 
143 1 
41) SPY 3/20/15 C190 
8.78 8.92 8.89 16.97 .54 
58 5658 
190.00 116) SPY 3/20/15 P190 
8.63 8.74 8.61 16.88 -.48 
256 13 
42) SPY 3/20/15 C191 
8.22 8.31 9.10 16.74 .52 
59 2120 
191.00 117) SPY 3/20/15 P191 
9.04 9.14 8.47 16.63 -. 50 
62 16 
43) SPY 3/20/15 0192 
7.61 7.72 8.44 16.46'.50 
21 5681 
192.00 118) SPY 3/20/15 P192 
9.479.58 9.33 16.37 -. 52 
300 82 
44) SPY 3/20/15 C193 
45) SPY 3/20/15 C194 
7.03 
6.48 
7.14 7.76 16.21 .48
6
6.60 .53 15.96 .46 
12 
87 
2643 
1446 
193.00 
194.00 
119) SPY 3/20/15 
120) SPY 3/20/15 
P193 
P194 
9.92 10.0:9.87 16.11 
10.3'10.4'9.65 15.83 
-. 54 
-.56 
27 31 
52 
46) SPY 3/20/15 0195 
5.95 6.08 6.00 15.72 .44 
6 6988 
195.00 121) SPY 3/20/15 P195 
io.8:10.9.10.8(15.67 -.58 
144 25 
47) SPY 3/20/15 C196 
5.45 5.57 5.81 15.50 .41 
33 4486 
196.00 122) SPY 3/20/15 P196 
11.3'11.4411.0'15.39 -.60 
208 22 
48) SPY 3/20/15 C197 
4.97 5.08 5.00 15.27 .39 
29 4604 
197.00 123) SPY 3/20/15 P197 
11.8:12.0'10.4415.10 -.63 
37 
49) SPY 3/20/15 C198 
4.51 4.63 4.77 15.02 .37 
28 10162 
198.00 " 
93) 0,7,' 
Color Legend 
Zoom 
004,
```

#### [164] [EFTA01462255](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01462255.pdf) -- Page 0

- **Interest Score:** 125.0
- **Fragments:** 6
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
SPY US 03/20/15 P186 
.:; ' /. 1/ 
- . 'A 
7.16 7.25 
535 243 
..d A: 10:25 
CriIiit 7,411 
VC. I 86 
1 6.67•` II 7.17: i 6.67; Hi i v 6.63 
p
9g Tem
U91.40 
1
 
t6 taus/Puts ns  
191.41 
 1` r.'h 
31 Term Option Monitor: Option t4onitor 
to 191.39 
Vein-. 56156770 
UV 13.43 
 
R1 Earnings Calendar (ACC,9) 
Mt-Attynotte '
32) SPY 3/20/15 C181 
33) SPY 3/20/15 C182 
34) SPY 3/20/15 C183 
35) SPY 3/20/15 C184 
36) SPY 3/20/15 C185 
37) SPY 3/20/15 0186 
3S) SPY 3/20/15 0187 
39) SPY 3/20/15 0188 
40) SPY 3/20/15 0189 
411 SPY 3/20/15 C190 
42) SPY 3/20/15 C191 
43) SPY 3/21)/1S C192 
44) SPY 3/20/15 C193 
45) SPY 3/20/15 C194 
46) SPY 3/20/15 C195 
47) SPY 3/20/15 0196 
4) SPY 3/20/15 C197 
49) SPY 3/20/15 0198 
'E) Default Color regent 
3:1 SPY 3,'23/15 CISO 
15.7-15..9'15.8. 19.53 .70 
n 
.44', 
180.00 
3/20/15 P1
14.9;15.2:19.41.9.26 69 
313 
3/20/15 P1
a 
10 
3/20/15 P1
66 
3/20/15 P1
64 
10 
3/20/15 P1
63 
94 
61 
30 
10 
1 
1278 
14.2414.4/14.449.02 
1299 
13.5 -3.744.5418.73 
850 
12.8 3.0:12. 18.53 
42.0 2.31123 18.20 
3317 
11.3 :1.&11. 18.06 
13801 
10.7 0.8°10.8 17.74.59 
2905i 
10.0(10.1S10.7 17.421.58 
3964I 
)9.44 9.53 10.2 17.17156 
1343 
8.78 8.92 8.89 16.97154 
58 5658 
8.22 .31 9.10145.74152 
59 2120 
7.51 7.72 8.44 16.461.50 
21 5681 
7.03 i..14 7.76 16.2108 
12 2643 
6.48:6.60 6.53 15.96l46 
87 1446 
15.95 6.08 6.00 15.72 A4 
6 6988 
S.45!5.57 5.81 15.50.41 
33 4486
4.97 5.C8 5.00 15.27.39 
29 4604 
4.514.63 4.77 15.02.37 
28 10I62 
1.81.00 
182.00 
183.00 
184.00 
185.00 
186.00 
187.00 
188.00 
189.00 
190.00 
191.00 
192.00 
193.00 
194.00 
195.00 
196.00 
197.00 
198.00 
sir; SPY 
1,21 SPY 
hi) SPY 
ES)
IN) SPY 
111) SPY 
112) SPY 
113) SPY 
1M) SPY 
115) SPY 
1151 SPY 
U7) SPY 
US) SPY 
119) SPY 
121) SPY 
121) SPY 
I22) SPY 
123) SPY 
3/20/15 P1
3/20/15 P1
3/20/15 P1
3/20/15 P1
3/20/15 P1
3/20/15 P1
3/20/15 P1
3/20/15 P1
3/20/15 P1
3/20/15 P1
3/20/15 P1
3/20/15 P1
3/20/15 P1
Z 0 
5.40 5.45 S. 
19 30 -.32 
518 2 
81 
5.66 5.72 5.32 19.061-.33 
3223•
2 
5.936.005.38/18.81€-.35 
3' 
3 
6.226.32 6.21 18.561-.361 
127 
4 
6.526.59 6.12 18.34 -.38 
2524 
73 
8674 
29'.12 
1954• 
5 
6 
7 
8 
9 
0 
91 
2 
3 
4 
5 
6 
7 
6.836.91 6.64 18.071-.39 
7.16 7.25 7.1717.841...41 
7.50 7.59 7.30 17.60 -.43 
7.86 7.99 7.9017.36-.44 
8.238.32 7.7017.11,1-.46 
8.638.748.61 16.88)-.48 
9.049.148.47 16.631-.50 
9.479.58 9.33 16.37 -.52 
9.92 10.0:9.8716.111-. 54 
10.3'10.4'9.65 15.83 -.56 
10.8110.910.8(15.67k 58 
11.3111.4411.0115.39 .60 
11.8:12.0'10.4415.10 .63 
1431•
256 13 
62 16 
30082 
27 31 
52 
144 
20822 
37
OOM -
```

#### [165] [EFTA01366082](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01366082.pdf) -- Page 0

- **Interest Score:** 123.5
- **Fragments:** 19
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
TWTR
A US 5 
1' 37.03 
.62 
,_.,— 
N37.02 /37.03K 
16
At 14:59 
Vol 13 867 990 0 36.49T 
H 37.330 
L 36.370 
Va 2.48M 
T bl "`
Twitter Inc
01,104 ri 
l
■
y 
T-er 
( to rent. y V 
et;4; 
55
Low 
31
Average 
43
Net 
3 0;1 
10/0
 
on 
06/0
98 
24,423
 
9
' ' 'Pg. is
1h 05/2 e.r 05/08/15 
37.59 
1
37 00
13 834 808 111 05/07/ 15
37 71
2 2 F; 04/17/15 
50.6
4 Th 04/16/15
52 03
05127/15 
36.41 
1
It
05/26/15
36 51
1 wo 05/06/15 
37.26 
29
to 05/05/15
37 42
22 Sw. 04;15/15 
51.30 
13,192
7u 04/14/15
5120
12 231
,
,
,
,
,
,
e I 
oF,/75/1F; 
OSTifil 5 
36.60 
°to 
9.861,815 'r 
05/04/15 
O5/01/1`. 
37.88 
3/.84 
24624537 ti., 
37,/85,543 t: 
04/13/15 
01/10/15 
51.62 
51.94 
14306,515 
13,2/1.155 
Th 05/21/15 
36.68 
17.447,682 lh 04/30/15 
38.96 
46,651,477 11, 04/09/15 
52.17 
17,877.667 
4i.• 05/70/15 
36.78 
23,404,469 WI' 04/X0/1', 
3849 
120,488557 t'sti 04/08/15 
5230 
22,368,972 
In 05/19/15 
37.50 
26,941,996 to 04/28/1,5 
42.77 
77,336412 Tu 04/97/15 
52.87 
37,080,755 
;L. 05/18/15 
37.28 
11.237,346 7V, 04/77/1'. 
51756 
23,991,902 T10 04/06/15 
50.84 
14,539480 
I i 05/15/15 
37.10 
16,799,060 I' f 
04/74/15 
50.87 
14,896,860 Fr 04/03/15 
III 05/14/15 
37.33 
14259407 Th 04/7.3/15 
5141 
11,490,400 lb 04/02/15 
50,42 
13,423,909 
.../.. 05/B/15 
37.72 
14,075331 .:” 04/22/15 
51.73 
11,4/9.493 140 04/01/15 
50.47 
24,299.197 
Tit 05/12/15 
37.48 
11,792,938 to 04/21/15 
51.32 
8,461283 1u 03/31/15 
50.08 
23,898,381 
7!n 05/11/15 
3731 
12379,491 Ho 04/20/15 
51.40 
11,004,476 1'10 03/30/15 
49.89 
20,365;393 ; 
5 
3
5 
3
5 
3
5 
3
 
3
 
3
5 
3
 
3
5 
3
 
3 9
8 
1
23
0 
26
 
1
 
1
3 
1
 
1
8 
1
 
1 °to 
'r 
05
O5
lh 04
WI' 04
 to 04
7V, 04
 I' f 
04
Th 04
 .:” 04
 to 04
 Ho 04 5 
3
5 
5 
4
'. 
5 
5 
5
5 
5 
5
5 2
3
6 
4
 
12
7
2
1
 
1
 
1
 
 
1
```

#### [166] [EFTA01447271](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01447271.pdf) -- Page 0

- **Interest Score:** 119.0
- **Fragments:** 10
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
SUNE US.. 
1 - 
At 15.42 Vol 9,595,276 
17.47 17.48 
39 ,10 
( i 17.90 
17.90 
16.91 
V- _ 165.68M 
97)
ON INC 
117.48 
Center N
k 
C l' 17.4
Tri. Ter
S ik LO 16.91 
Volm 9595276 
HV 71.81 
9(2) Next Earnings(EM) 08/07/14 E 
cre:..ness 
P
å) SUNE 6/21/14 C15 2.81 3.00 2.56 65.24.80 
15,00 
i) SUNE 6/21/14 C16 2.132.34 2.02 65.99 .70 129. 261 
16.00 
8) SUNE 6/21/14 C17 1.60 2.69 1.3864.96;..59 10101232 
17.00 
9) SUNE 6/21/14 C18 1.17 1.21 1.1765.011.48 1191 329 
18.00 
1 1,
' 
• 
-‘9 
7358 
19.00 
19 Jul 14 (65d); CS1ze 100; IDiv 50; R 20; IFwd 17 41111En
40) SUN
41) SUN
42) SUN
43) SUN
44) SUN
19 J E 6/21/14 
E 6/21/14 
E 6/21/14 
E 6/21/14 
E 6/21/14 P19 2.33 2.39 2.33 64.57 -.62 115 1 
ul 14 (65d); CSize 100; IDiv 50; R 20; IFwd 17
P15 
.44 .49 
.50 67.02 -.20 105 1 
P16 
.74 
P17 1.16 
P18 1.69 
.80 
1.21 
1.73 
.93 66.30 -.30 
1.22 65.35 -.41 
1.68 64.51 -.52 
150 1 
902 
23 2
8_ 7 
13.00 
70.57 .31 
7997 
71.36 .74 
5 2643 
66.60 .67 
121 
67.37 .59 
513 
67.15 .51 2281022 
66.78.43 261 102 
67.29.36 
419042 
12) SUNE 7/19/14 C14 3.8514.20 4.85y 
14.00 
13) SUNE 7/19/14 C15 
3.2013.501 3.25 
15.00 
14) SUNE 7/19/14 C16 ''2.592.753.50y 
16.00 
IS) SUNE 7/19/14 C17 202.2112.68y 
17.00 
14) SUNE 7/19/14 C18 
1.6911.751 1.74 
18,00 
17) SUNE 7/19/14 C19 1.3011.38 1.30 
19.00 
18) SUNE 7/19/14 C20 
1.0311.08. 
.88 
20.00 
In 
'F -- ' . C, . . -= C.' 1 
c :-) 
7.  '''' 
- -.' -.' 
7.7 - - 7 7, 
21.00 
18 Oct 14 (156d); CSize 100; IDiv .29; R .30; IFwd 17: ®®
45) SUN
46) SUN
49) SUN
48) SUN
49) SUN
Se SUN
Si) SUN
52) SUN
53) SUN
118 O E 7/19/14 P13 
.34 .41 
.39 70.86 -.13 
32 
E 7/19/14 P14 
.54 .61 .43y1 68.40 -.18 
4 
E 7/19/14 P15 
.84 .87 
.85 67.59 -.25 
315 
E 7/19/14 P16 1.201.28 1.24 67.71 -.33 334 6 
E 7/19/14 P17 1.661.73 1.87 66.82 -.41 
202 
E 7/19/14 P18 :2.202.26 2.27 65.51 -.49 
352 
E 7/19/14 P19 2.82 2.90 3.05 66.03 -.57 
153.
E 7/19/14 P20 3.50 3.70 3.55 66.90 -.63 
243 
E 7/19/14 P21 4.25 4.45 2.75y 64.75 -.71 
1 
Oct 14 (156d); CSize 100; IDiv .29; R .30; IFwd 17
28) SUNE 10/18/14 C15 I3.8.. 
15.00 
21) SUNE 10/18/14 C16'3.5013.85 3.80y 67.06 .60 
169 
16.00 
22) SUNE 10/18/14 C17 3.10'3.30' 3.30 66.39'.61 
1 468 
17.00 
54) SUN
SS) SUN
S6) SUN E 10/18/14 P15 1.69 1.79,1.60y 66.57 .29 
1 
E 10/18/14 P16 2.15 2.26 2.03y 66.20 -.34 
3 
E 10/18/14 P17 2.68 2.79 2.87 66.67 -.39 
105
```

#### [167] [EFTA01461651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01461651.pdf) -- Page 0

- **Interest Score:** 119.0
- **Fragments:** 10
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
SUNE US.. 
1 - 
At 15.42 Vol 9,595,276 
17.47 17.48 
39 ,10 
( i 17.90 
17.90 
16.91 
V- _ 165.68M 
97)
ON INC 
117.48 
Center N
k 
C l' 17.4
Tri. Ter
S ik LO 16.91 
Volm 9595276 
HV 71.81 
9(2) Next Earnings(EM) 08/07/14 E 
cre:..ness 
P
å) SUNE 6/21/14 C15 2.81 3.00 2.56 65.24.80 
15,00 
i) SUNE 6/21/14 C16 2.132.34 2.02 65.99 .70 129. 261 
16.00 
8) SUNE 6/21/14 C17 1.60 2.69 1.3864.96;..59 10101232 
17.00 
9) SUNE 6/21/14 C18 1.17 1.21 1.1765.011.48 1191 329 
18.00 
1 1,
' 
• 
-‘9 
7358 
19.00 
19 Jul 14 (65d); CS1ze 100; IDiv 50; R 20; IFwd 17 41111En
40) SUN
41) SUN
42) SUN
43) SUN
44) SUN
19 J E 6/21/14 
E 6/21/14 
E 6/21/14 
E 6/21/14 
E 6/21/14 P19 2.33 2.39 2.33 64.57 -.62 115 1 
ul 14 (65d); CSize 100; IDiv 50; R 20; IFwd 17
P15 
.44 .49 
.50 67.02 -.20 105 1 
P16 
.74 
P17 1.16 
P18 1.69 
.80 
1.21 
1.73 
.93 66.30 -.30 
1.22 65.35 -.41 
1.68 64.51 -.52 
150 1 
902 
23 2
8_ 7 
13.00 
70.57 .31 
7997 
71.36 .74 
5 2643 
66.60 .67 
121 
67.37 .59 
513 
67.15 .51 2281022 
66.78.43 261 102 
67.29.36 
419042 
12) SUNE 7/19/14 C14 3.8514.20 4.85y 
14.00 
13) SUNE 7/19/14 C15 
3.2013.501 3.25 
15.00 
14) SUNE 7/19/14 C16 ''2.592.753.50y 
16.00 
IS) SUNE 7/19/14 C17 202.2112.68y 
17.00 
14) SUNE 7/19/14 C18 
1.6911.751 1.74 
18,00 
17) SUNE 7/19/14 C19 1.3011.38 1.30 
19.00 
18) SUNE 7/19/14 C20 
1.0311.08. 
.88 
20.00 
In 
'F -- ' . C, . . -= C.' 1 
c :-) 
7.  '''' 
- -.' -.' 
7.7 - - 7 7, 
21.00 
18 Oct 14 (156d); CSize 100; IDiv .29; R .30; IFwd 17: ®®
45) SUN
46) SUN
49) SUN
48) SUN
49) SUN
Se SUN
Si) SUN
52) SUN
53) SUN
118 O E 7/19/14 P13 
.34 .41 
.39 70.86 -.13 
32 
E 7/19/14 P14 
.54 .61 .43y1 68.40 -.18 
4 
E 7/19/14 P15 
.84 .87 
.85 67.59 -.25 
315 
E 7/19/14 P16 1.201.28 1.24 67.71 -.33 334 6 
E 7/19/14 P17 1.661.73 1.87 66.82 -.41 
202 
E 7/19/14 P18 :2.202.26 2.27 65.51 -.49 
352 
E 7/19/14 P19 2.82 2.90 3.05 66.03 -.57 
153.
E 7/19/14 P20 3.50 3.70 3.55 66.90 -.63 
243 
E 7/19/14 P21 4.25 4.45 2.75y 64.75 -.71 
1 
Oct 14 (156d); CSize 100; IDiv .29; R .30; IFwd 17
28) SUNE 10/18/14 C15 I3.8.. 
15.00 
21) SUNE 10/18/14 C16'3.5013.85 3.80y 67.06 .60 
169 
16.00 
22) SUNE 10/18/14 C17 3.10'3.30' 3.30 66.39'.61 
1 468 
17.00 
54) SUN
SS) SUN
S6) SUN E 10/18/14 P15 1.69 1.79,1.60y 66.57 .29 
1 
E 10/18/14 P16 2.15 2.26 2.03y 66.20 -.34 
3 
E 10/18/14 P17 2.68 2.79 2.87 66.67 -.39 
105
```

#### [168] [EFTA01447608](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01447608.pdf) -- Page 0

- **Interest Score:** 115.0
- **Fragments:** 30
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
:1P1,1 US Eq
3PMorgan Cha
RaTge 
"arket rt to Excel 
Period 
Currency 
Da
IJS High 
Low 
Avg 
Net C 
Historical Price 
61.07 
03/24/14 
50.32 
09/24/13 
55.691 
17,850,442 
fig 
3.95 
7.18% 
P
votume
F 07
is 07
4 07
T 07
M 07 14 
14 
F 0
Ti06
14 
58.96 
10,865,787141 0
14 
58.27 
36,219,126 TI 0
14 
56.29 
14,011,991 MI 0 6/27/14 
/26/14 
6/25/14 
6/24/14 
6/23/14 
5
5
5
5
5 F 
 T 
41 
 T 
 H 
0
0
0
0
0 14 
14 
14 
14 
14 97 
15,
63 
16,
68 
9,
60 
9,
35 
9,
F 07/1
T 07/1 1/14 
5
0/14
5 5.80 
10,
5.56
12, 236,860 F 06/20/14 
436,589 T 06/19/14
57.55 
17,
57,30
11,6 25 F 
3 T
0
0 14 
5
14
5 57 
11,991,3
72
11,741,7
4 
5
4 
5 /14 
/14 
5
5 8 
1
2 
1 14 
14 5 
11
4 
14
I 07/0
F' 07/0
T 07/0
W 07/0
T 07/0 I 07/07/14 
56.67 
13,918,7431'9' 06/16/14 
F' 07/04/14 
F 06/13/14 
T 07/03/14 
57.05 
12,599,842 T' 06/12/14 
W 07/02/14 
56.97 
19,199,260W 06/11/14 
T 07/01/14 
57.57 
14,472,160 T 06/10/14 
M 06/30/14 
57.62 
11,549,859.M1 06/09/1•) 
Australia 
Japan 
Brazil 
Singapore 
56.87 
11,199,075 M 
57.04 
12,044,435 F 
57.04 
11,677,911 
57.27 
14,232,171 h,1 
57.90 
11,609,169 T 
57,42 
12,000,038 r•1 
Europe 
U.S. 1 
SN 
05/26/14 
05/23/14 
54.53 
10,878,697 
05/22/14 
54,55 
11,801,568 
05/21/14 
54.12 
13,210,922 
05/20/14 
53.72 
16,888,227 
05/19/14 
53.83 
12,068,854 
Germany 
Hong Kong 
Copyright 2014 Bloomberg Finance L.P. 
• EDT GMT-4:00 H653-5263-2 16-Jul-2014 13:14:47 4 
56.67 
13,9
4 
4 
57.05 
12,
4 
56.97 
19,
4 
57.57 
14,4 18,7431'9' 0
F 0
599,842 T' 0
99,260W 0
472,160 T 0 /14 
/14 
/14 
/14 
/14 
5
5
5
5 7 
1
4 
1
4 
1
7 
1
0 
1 5 M 
5 F 
1 
1 h,1 
9 T 
0
0
0
0
0 14 
14 
5
14 
5
14 
5
14 
5 4.53 
10,87
4,55 
11,80
4.12 
13,21
3.72 
16,88
```

#### [169] [EFTA01461889](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01461889.pdf) -- Page 0

- **Interest Score:** 112.5
- **Fragments:** 29
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
:1Phl US Eq
3PMorgan Cha
RaTge 
"a rket rt to Excel 
Period 
Currency 
Da
IJS VA  
a 
Historical Price 
High 
61.07 
03/24/14 
Low 
50.32 
09/24/13 
Avg 
55.691 
17,850,442 
Net Ctig 
3.95 
7.18% 
Vol me
DateP
ol me !
F 07
T 07
4 07
T 07
M 07 4 
F 0
4 
Ti06
14 
58.96 
10,865,787141 0
14 
58.27 
36,219,126 TI 0
14 
56.29 
14,011,991 MI 0 6/27/14 
/26/14 
6/25/14 
6/24/14 
6/23/14 
5
5
5
5 F 0
 T 0
11 0
T 0
H 0 4 
4 
4 
4 
4 7 
3 
8 
0 
5 
15,
16,8
9,7
9,1
9,4
F 07/1
T 07/1 1/14 
5
0/14
5 5.80 
10,
5.56
12, 236,860 F 06/20/14 
436,589 T 06/19/14
57.55 
17,1
57,30
11,6 5 F 0
3 T 0 4 
5
4
5 7 
2
11,991,3
11,741,7
4 
5
4 
5 8/14 
7/14 8 
1
2 
1 5 
4 
11
14
I 07/0
F 07/04
T 07/0
W 07/0
T 07/0 I 07/07/14 
56.67 
13,918,7431'9' 06/16/14 
F 07/04!14 
F 06/13/14 
T 07/03/14 
57.05 
12,599,842 Ti 06/12/14 
W 07/02/14 
56.97 
19,199,260W 06/11/14 
T 07/01/14 
57.57 
14,472,160 T 06/10/14 
M 06/30/14 
57.62 
11,549,859.M1 06/09/1•) 
56.87 
11,199,075 H 05/26/14 
57.04 
12,044,435 F 05/23/14 
54.53 
57.04 
11,677,911 1- 05/22/14 
54,55 
57.27 
14,232,171 
05/21/14 
54.12 
57.90 
11,609,169 T 05/20/14 
53.72 
57,42 
12,000,038 H 05/19/14 
53.83 
Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 
Japan 81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 
SN 
10,878,697 
11,801,568 
13,210,922 
16,888,227 
12,068,854 
7500 Germany 49 69 9204 1210 Hong Kong 852 2977 6000 
318 2000 
Copyright 2014 Bloomberg Finance L.P. 
264224 EDT GMT-4:00 H653-5263-2 16-Jul-2014 13:14:47 4 
56.67 
13,9
4 
4 
57.05 
12,
4 
56.97 
19,
4 
57.57 
14,4 18,7431'9' 0
F 0
599,842 Ti 0
99,260W 0
472,160 T 0 6/14 
/14 
/14 
/14 
0/14 
5
5 7 
1
4 
1
4 
1
7 
1
0 
1 5 H 0
5 F 0
1 1- 0
1 
0
9 T 0 4 
4 
5
4 
5
4 
5
4 
5 54.53 
54,55 
54.12 
53.72 
10,87
11,80
13,21
16,88
```

#### [170] [EFTA01461910](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01461910.pdf) -- Page 0

- **Interest Score:** 112.5
- **Fragments:** 29
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
:1Phl US Eq
3PMorgan Cha
RaTge 
"a rket rt to Excel 
Period 
Currency 
Da
IJS VA  
a 
Historical Price 
High 
61.07 
03/24/14 
Low 
50.32 
09/24/13 
Avg 
55.691 
17,850,442 
Net Ctig 
3.95 
7.18% 
Vol me
DateP
ol me !
F 07
T 07
4 07
T 07
M 07 4 
F 0
4 
Ti06
14 
58.96 
10,865,787141 0
14 
58.27 
36,219,126 TI 0
14 
56.29 
14,011,991 MI 0 6/27/14 
/26/14 
6/25/14 
6/24/14 
6/23/14 
5
5
5
5 F 0
 T 0
11 0
T 0
H 0 4 
4 
4 
4 
4 7 
3 
8 
0 
5 
15,
16,8
9,7
9,1
9,4
F 07/1
T 07/1 1/14 
5
0/14
5 5.80 
10,
5.56
12, 236,860 F 06/20/14 
436,589 T 06/19/14
57.55 
17,1
57,30
11,6 5 F 0
3 T 0 4 
5
4
5 7 
2
11,991,3
11,741,7
4 
5
4 
5 8/14 
7/14 8 
1
2 
1 5 
4 
11
14
I 07/0
F 07/04
T 07/0
W 07/0
T 07/0 I 07/07/14 
56.67 
13,918,7431'9' 06/16/14 
F 07/04!14 
F 06/13/14 
T 07/03/14 
57.05 
12,599,842 Ti 06/12/14 
W 07/02/14 
56.97 
19,199,260W 06/11/14 
T 07/01/14 
57.57 
14,472,160 T 06/10/14 
M 06/30/14 
57.62 
11,549,859.M1 06/09/1•) 
56.87 
11,199,075 H 05/26/14 
57.04 
12,044,435 F 05/23/14 
54.53 
57.04 
11,677,911 1- 05/22/14 
54,55 
57.27 
14,232,171 
05/21/14 
54.12 
57.90 
11,609,169 T 05/20/14 
53.72 
57,42 
12,000,038 H 05/19/14 
53.83 
Australia 61 2 9777 8600 Brazil 5511 3048 4500 Europe 44 20 7330 
Japan 81 3 3201 8900 
Singapore 65 6212 1000 
U.S. 1 212 
SN 
10,878,697 
11,801,568 
13,210,922 
16,888,227 
12,068,854 
7500 Germany 49 69 9204 1210 Hong Kong 852 2977 6000 
318 2000 
Copyright 2014 Bloomberg Finance L.P. 
264224 EDT GMT-4:00 H653-5263-2 16-Jul-2014 13:14:47 4 
56.67 
13,9
4 
4 
57.05 
12,
4 
56.97 
19,
4 
57.57 
14,4 18,7431'9' 0
F 0
599,842 Ti 0
99,260W 0
472,160 T 0 6/14 
/14 
/14 
/14 
0/14 
5
5 7 
1
4 
1
4 
1
7 
1
0 
1 5 H 0
5 F 0
1 1- 0
1 
0
9 T 0 4 
4 
5
4 
5
4 
5
4 
5 54.53 
54,55 
54.12 
53.72 
10,87
11,80
13,21
16,88
```

#### [171] [EFTA01652995](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652995.pdf) -- Page 13

- **Interest Score:** 104.1
- **Fragments:** 4
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Maxwell, Dershowitz, Alan, Trump, Donald, Andrew, Prince, Wexner, Les, Dubin, Glenn

**Reconstructed Text:**

```
TV&Sh
bi
nce of Fake Pm...
George B... 
BREAKING: 
Donald J. Trump. Prince Andrew. 
Alan Dershowitz. 
Lady Victoria Hervey, 
Leslie & Abigail Wexner, 
_______George B. Tot. 
Eileen Guggenheim, 
Glenn & Eva Dubin, 
Richard Branson. the Maxwell's. 
FBI, MI6, CIA or es
t 
sda 
DID NOT KILL 
Sent from my 'Phone 
killed 
KILLED
E9XK5SH Lnl?si sbjOobIWTRarkI xD
```

#### [172] [EFTA01302111](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01302111.pdf) -- Page 0

- **Interest Score:** 102.0
- **Fragments:** 4
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Epstein, Les, Palm Beach, New York

**Reconstructed Text:**

```
ation. ( if he talks about appeal., waivers, 1 think that is a non. 
oposed set of facts, to which we would have to stipulate. I.1
both of our sides. But if You take a step back, which I again 
e that our current proposal , while not what we, would 
e preferred- is currently the best overall solution, for both of 
think about it, and I suggest we postpone setting up any firm 
ave had ample time to review the current situation and 
bility of getting this complex matter firmly and totally. behind conversation re yesterdays call. I wanted to give you time to 
presented regarding the New York Times. . I'm sure you now realize 
 of David weinstein's actions as merely third party hearsay, I 
roof positive of what transpired. Proof positive of a breach of the 
e of a breach of the local rules of conduct„ I can't represent to you 
 doubt of a 6 e violation, but clearly enough facts that would 
ssed details of our plea negotiations, ( personal security and house 
e offices concern with the Palm beach post editorial. He discussed 
bout the multiple charging statues, even including the 1591 
patently unfair to Mr. Epstein. . Frankly, as you heard yesterday, Ken 
a man of great faith- both in his religion and his unwavering belief 
bibles, the king james version and the us attorneys manual. He 
ase he believes it has failed ,miserably. His fear is that the Bob 
to be a rubber stamp for the office. Regarding our proposal, I 
cipled position. Yesterday, I appreciated you telling me of ,as you 
d
id
h t
ould we get if we achieved a
opir) ,
lke
hat 
He
s tw
th
gn
y p
e ,
cki
tra
ce.
m, 
ere
en
```

#### [173] [EFTA01447495](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01447495.pdf) -- Page 0

- **Interest Score:** 88.2
- **Fragments:** 4
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Maria, Jay

**Reconstructed Text:**

```
Alpha Bank AE 
ronsensus 
crrtrEat 
Consensus Rating 
3.95 
10o -o 
Buys 
59.1% 
13 
Holds 
273% 
6 
S0: 
Sells 
13,68 
3 
12M Tgt Px 
17/23 
0.84 
0 
Last Price 
0.69 
0.00 
Return Potential 
21.7% 
- 0. 50 
LTM Return 
80.2% 
Show In-House Data 
J
Analyst 26/14 
r O.8O 
P. O,6O 
O,4O 
O,2O 
•
 
l<
I) 
2) 
:3) 
4) 
5) 
6;1 
1) 
8) 
9)
10) 
11) 
12) 
Au
Jap Wood & Company 
Alexandros Bouloug 
buy.
O6/2O/14 
Euroxx Securities 
Maria Kanellopoulo 
overweight 
0.90 06/19/14 15.00% 
1st IC 
Alpha Finance 
Nikolaos Lianeris 
restricted 
06/17/14 
le 
Natixis 
Alex Koagne 
40 
0,75 O6/16/14 
Pantel.akis Securities 
Paris Mantzavras 
overweight 
O.9O O6/13/14 
It: 
Nomura 
Daragh Quinn 
buy 
0.75 06/12/14 
0.20% 
Credit Suisse 
Hugo Swann 
• neutral 
0.80i 06/11/14 
Barclays 
Kiri Vijayarajah 
• 
overweight 
0.92 06/10/14 
 Goldman Sachs 
Pawel Dziedzic 
Buy/Neutral. 
0.801 06/06/14 
le 
HSBC 
Tamer Sengun 
overweight 
0.871 06/06/14 
IBG Research (ESN) 
Konstantinos Manol 
buy 
1.10 06/06/14 
Deutsche Bank 
Rahul Shah 
Alt buy 
0.90 06/04/14 
ralia 
Brazil 
Europe 
Germany 
Hong Kong 
n 
Singapore 
U.S. 
Copyright 2014 Bloomberg Finance L.P. 
SN 622439 H622-433-3 26-Jun-14 14:11:47 BST 
GMT+1:00
```

#### [174] [EFTA01461016](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01461016.pdf) -- Page 0

- **Interest Score:** 77.5
- **Fragments:** 52
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Les, Maria, Chris, Paul, Jay

**Reconstructed Text:**

```
Tangney 
; Mi
A
IJIJIJ
l;
D
l
R b
t
Foster J McCoy nice M Smith al; 
Leanna Rivera
Leo Bresnahan ); Mary C Keavene
Michael Mullin [ Paul Bartilucci yllis M Fineman
Paul Bartilucci 
Guest 
Tracey T Whitehead 
; 
Anh H Parisi
ana Bea
;
ut [
I=I
i1; n-Services Germany
; Shahin Ahdieh
); Malcolm ]; Vincent
; John ; Timo e [ 
; Aaron Price 
M Quattrocchi
1; Cheryl Palle Anna-Sofiya
Lupolover ; PWMLatA
; Maria Tellez Proko
1; Cynthia
Quattrocchi 
ij; Vrablic [ 
I; Lis
1; Carolin Botzenhard Ehrenberg
); Dahlia Uchihara Ahdieh
Javarone Brenda Guerrier Josie Alonso
]; Cynthia Rodrigue ; Anna-Sofrya Lu
; Jay Ha Brigid Ehren
Elizabeth Payne Sylvia Junghardt Theresa Romano
; Valerie Christ ; Josie Alonso
I; Gil Friede ; Michele-M
ala 
; Gina 
J Rebecca V
; Michael S Jac
a Ouyang 
MOPS REPORTING 
a ersight Control 
]; Lillian T
Debra Jasper al;
; Sheryl Davis ; Janet Morales al
```

#### [175] [EFTA01377514](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01377514.pdf) -- Page 0

- **Interest Score:** 75.9
- **Fragments:** 29
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Paul

**Reconstructed Text:**

```
Paul Morr
I US 
l At 14:13 
1 1 175(088 
24.00 
90 Export to Excel
K2
24.8 2.10 /22.11P 
88 
21.85 
Page 116
1 x3 
26.81M 
Historical PriceTable
oundation
1 Period 
i urren 
Dbte rice
volume
Date
50
18
33
-1 3 
• 
C4/0
7 
10/0
3701 
31
0 
-
st Price
Vo
Th 07/3 • 
G
5 
22.14 
1,175,088 Th 0 S 
3
5 
3 .17 
3
.35 
9 S 
5 
3
5 
2
5 
3
5 
3
5 
3
5 
3 30 
2
02 
2
47 
2
68 
1
78 
1 32
 
34
 
33
 
32 .44 
148
413 
153
.10 
136
.88 
98 5 
5 
5 
5 
5 
3
3
3
3 8 
1
7 
2
0 
4
0 
4
5 
2
5 
3
5 
3
5 
3
5 
3
5 
3
5
3 8 
1
1 
1
1 
2
8 
1
2 
1
4 3
3
 
3
3
3
3 1
 
5
 
4
1 5 
5 
5 
5 
5 
5
3
3
3
3
3 9 
65 
1
8 
1
1 
1
1 
1
8
1
lila 07/15/15 
32.74 
80,202 WA 06/24/15 
32.82 
191,273 ...c. 06/03/15 
Tu 07/14/15 
33.37 
147,943 Tu 06/23/15 
33.40 
202,011 Tu 06/02/15 
Mo 07/13/15 
33.45 
93,268 Mc 06/22/15 
33.59 
231,350 MD 06/01/15 
35.78 
197,389 
35.46 
228,099 
35.00 
205,576 5 
3
5 
3
5 
3 1
 
2
2 5 
5 
5 
3
3
3
P
Sh Wid
Th
```

#### [176] [EFTA01447928](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01447928.pdf) -- Page 0

- **Interest Score:** 74.3
- **Fragments:** 9
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Darren

**Reconstructed Text:**

```
IBESPL 7 pa 11/28/23 
At 10:24 
t 
194.882 
n 94.092 
F.l: 94.882 
• . 185 
94.266/95.497 
lc 87.156 
Prev 94.697 
BGN 
 
Li
Ch iR"'
PI
A
A
i
•
FA Fd
i lli
ca^ss'e
110 000
108.000
106 000
104.000
102.000
100.000 
Last Price 
94.882 
98.000 
T High on 06/09/14 111.227 
Average 
105.406 
1 Low on 06/30/14 
94.697 
)an 
Feb 
Mar 
2014 
Apr 
May 
Jun 
ES 
NCO ESPIRITO 
E:: 7 'is
:crp
BE SPL 
Var 11/23 
94.2460/95.4850 (8.735/8.374) 6GW 
@10:22 
ewe Ira
Derription Bond
a
e
CO
S
O
Indust, 
Baskin•
PTBEQ3040012 
s 
Mkt Is' 
Coro MTN 
ESS:T 
BEIGOOSMOK 032 
!Bond gaiings 
country 
PT 
Darrenzy 
EUR 
y 
B2 
•-
Rank 
 
Suborcfinated 
Series 
SEP 
8 
Coupon 
7.125 
VP. 
Variable 
Dar( 
BEN 
& 
Cpn Freq Annual 
Day Ent 
ACT/ACT 
:SS Price 
100.00000 
Ccr,cs • 
Matunty 11/28/2023 
Reoffer 
100 
Amt Issued/Outstandirg 
CALL 11/28/189100.00 
BJR 
750,000.00 CM) / 
Recite 
Iss Son:I 
 645.40bp vs OBL 1 10/12/18 
FOR 
750,000.W (PO 
?Oft 
elien 
Calc Type 
(1469) FJX-TO-VARIABLE BO 
n Piece/Increment 
etc, 
Announosmert Date 
11/21/2013 
100,000.00 / 100,000.60 
e, s 
Interest Acauai Date 
11/28/2013 
Par Amount 
1.00,000.00 
n 
1st Settle Date 
11/28/2013 
Book Romer 
BEST,BAML,C MS 
1-`.• 
-st Coupon Dare 
11/28/2014 
E:change 
MLI [Tic.
```

#### [177] [EFTA01660663](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01660663.pdf) -- Page 2

- **Interest Score:** 73.1
- **Fragments:** 3
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** New York

**Reconstructed Text:**

```
Fort Worth, Texas 76137 
part of the At 
family 
AtNight Media ('Relocating to Texas and Pennsylvania) 
85th Floor • 1 World Trade Center • New York. NY 10007
• atnightpictures.com 
• atnightmedia.com 
• worldnexus.co
Confidentiality Notice: This email is intended only for the named recipients) and may contain confidential information. If you are not an intended 
recipient. please delete this email and notify the sender immediately. 
Privacy Notice: Governed by Swiss data protection laws (Federal Act on Data Protection. FADP). For details. see 
. Swiss laws 
provide robust privacy protections. 
Legal Jurisdiction: This email and its data are subject to Swiss law. U.S. authorities do not have jurisdiction. 
Note: One World Media Corp. the parent company of Might Media utilizes Proton Technologies based in Switzerland.
```

#### [178] [EFTA01385873](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01385873.pdf) -- Page 0

- **Interest Score:** 72.9
- **Fragments:** 37
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
TtrrTR
A US $ 
t 3
At 14:59 
V 3 
• -62 
N37.02 /37.03K 
16
3 867 990 0 36.49" 
37.33D 
L 36.37D 
Va 9 
2.481-1
0 /08/1 a 
ov„,
31
43
3 98 
 
on 
06/0
24,423
9
5 
 
5 
5 
37.
36.
36 13
 
14
 
13 Th 05
.:tt 0
Ito 0
t to 0 2
2
 
2
2 5 
5
5 
5
15 
36.60 
9,861,815 I i 
0 01/15 
3
Th 0
:to. 0 21/15 
20/15
36
36 68 
1
78
23 lb 0
itritt 0 0/15 
3
9/15
3 96 
4
49
12 7 th 04/09/15 
52.
7 crit• 04/02/15
52.
it; 05/19/15 
ii ) 05/16/15
37
37 .50 
26,941,996 1u 04/28/15 
42.27
28
11 237 346 Ftc 04/27/1h
51 6 77,33
23 99 6,612 9u 04/07/15 
52.87 
902 T10 04/06/15
¶30 81
37.080,
14 539
r-/
05 /15
37 1 799 060 =
04/74/15 0 r-
04/03/15
/15 
/15
3733 
14
37 72
14 Th 04
We 04 15 
5
15
5 0 lb 04/02/15 
50.42 
3 we 04/01/15
50 47
13,423,909 
24 299 197
5 
37.4
37. to 04
 Nu 04 15 
5
15 31/15 
30/15 
4
```

#### [179] [EFTA01358175](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01358175.pdf) -- Page 0

- **Interest Score:** 69.4
- **Fragments:** 26
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
Arian
eld
TWTR US 
At 14:59 
S 
37 
Vol 
. 03 
13 L867 990 1 36.49 
to t 
37. 02 37.03 
1
• 37.33 
36.37 
Par 
1/6 
R US Equity
ficport 9 
2.4SM 
0.01 Price I Sr
. 
Inc 
— 
ta Per k.“I 
Citron .• 55
tow 
31
Avor st00 
43
Net Slxs 
3 19/0
 
on 
06/0
48 
24,423
 
9
S 
37
 
36
5 
36
 
 
36
5 
36
 
36
5 
37
 
37 00 
13
41 
14
51 
13
60 
9
68 
1
78 
23
30 
26
28 
1 0
III 05
We 0
 tu 05
rh,
, i 
0
0
En 0
ell' 0
 19 0
EL, 04 , 
 
 
 
3
 
4 1
1 
2
7
 
2
2
3
6 
4
 
17
7
 
2 5 
5 
5 
5 
5 
% 
5 
5
3 
S 
5
. 
5
5/15/15 
37.10 
1 ,799,060 >r 04/24/15 
502 ,896,86 0 r! 04/03/15
Th 05/14/15 
37.33 
14
140 05/13/15
37.72
14 Th 04/23/15 
5
We 04/22/15
5 00 lb 04/02/15 
50.42 
13,423,909 
93 s'ir• 04/01/15
50.47
24,299,197
Its 05/12/1
, . 0!,,, t,/u 5 
3
3 8 19 0
S-1O 0 /15 
5
0/15 3 ru 03/31/15 
6 Ms 03730/15
4 .08 
2
89
2
```

#### [180] [EFTA01358373](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01358373.pdf) -- Page 0

- **Interest Score:** 68.8
- **Fragments:** 35
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
rwri
A US $ 
t 3
At 14:59 
V 3 
+.62 
N37,02 /37.03K 
16
3 867 990 0 36.49' 
37.330 
L 36.37D 
Va 9 
2.48M
Range 
arkm 
vies 
I Per
CWrency 
( ” b 4 3) a 
Low 
f. 
31
43
3 898 
24,423
 
X9.569 
on 
06/0
5 
37.
 
36.
5 
36.
5 0 
13
1 
14
1 
13 (
 Th 0
 -5, 0
 ru 05
t to 0 5 
3
5 
5 
3
5 2
 
2
2
2 5 
s 
5 
5
05 
36.60 
9,861,815 'v 0 701/ 1T. 
3
th 0
Me 0 /15 
36
0/15
36 8 
17
23 Th 0
We 0 0/15 
3
9/15
3 6 
4
12 7 th 04/09/15 
52.
5/ MY 04/08/15
52.
In 05/19/15 
37
It) OS/ 18/15
37 .50 
26,941,996 1u 04/28/15 
42.27 
77
28
11 237 146 14n 04/77/15
51 66
23 6,612 1u 04/07/15 
52337 
37,080,
902 Mt) 04706/15
5084
14 539/
/25
37 1 0 !E
01/24/15 0 r
04
/25 
3733 
14
/15
37 72
14 Th 04
We 04 15 
5
15
5 lb 04/02/15 
50.42 
13.423,909 
WV 04/01/15
50 47
24 299 197
5 
37
5 
37 8 iu 04
I In 04
```

#### [181] [EFTA01652467](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652467.pdf) -- Page 0

- **Interest Score:** 66.8
- **Fragments:** 3
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Les, Ross, Paul

**Reconstructed Text:**

```
row 
orresblanco 
ate" 
,'CUR, Judith" 
Kathy Lombard 
. Melissa Lerner 
, Jennifer Plotkin 
"Petralia. Whim 
,'Lockwood, Beatrix" 
. Steve Ross 
, Robert Car uilo 
• -Balderama. Jen" 
a 
. Assistant to Frida Torresblanco 
, Sigrid M 
. dawn schneidcr 
. "Ka Ian. Karrah" 
,'De enbrock. Julie" 
, "Ma , Ethan" 
aY 
a 
Amy Smoker 
, Ton Diver 
• 'Olsewski. Paul" 
Frida Torresblanco 
a 
Ki 
, Helen Liles 
LaMarca. Michael' 
"Larabee. Michael" 
EXTERNALEMAIL) Sh
i R d t
Vi
&
Ki
ked you still hav yourjob at the FBI
```

#### [182] [EFTA01457604](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01457604.pdf) -- Page 0

- **Interest Score:** 62.0
- **Fragments:** 24
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
TWTR US
At 14: 59 
 :37.0:3 
Vol 13 ,867, 990 0 36 . 49 
aport 
tx0,1 
R US Equity
u
• • 37.33 
.37.02 37.03 
1
36.37 
V
Parr 1/6 9 
2.48M 
érillittr"
? 
• e +' -j 
tterewy 
"""""."17rniiin 55
LAM 
31
Aver nor,
Net Ch0 
43
3
W
.
T on 
10/0
 
un 
06/0
s9s 
24,423
 
9
Ptitir"7""9511
5 
37
 
36
5 
36
 
 
36
5 
36
 
36
5 
37
5 
3/ 00 
13
41 
14
51 
13
60 
9
48 
1
78 
23
50 
26
78 
1 r 0.
Th 05
We 0
 to 05
• i 
05
0
Th 0
egie 04
 /0 0
0 1
 
2
2
 
2
 
7
3
6 
4
 
12
7
 
7 5 
5 
5 
5 
5 
5 
5 
5
5 
5 
5
5
/15 
3/.1 ,799,060 á, 01174/15 
50.8 ,896,86 0 r 
04/o3/15
Th 0
0 5/14/15 
3733 
1
5/13/15
37.72 Th 04/23/15 
5
Wo 04/72/15
5 00 rh 04/02/15 
50.42 
13,423,909 
93 w.• <14/01715
50.47
24,299,19/
ln 
05/12/1
05/11)1 5 
3
5
3 8 to 04/2
Pl
{At /15 
/ IS 3 
03/31/15 
6 Pio 03/30/15 
4 0.08 
2
9.89
2
```

#### [183] [EFTA01626170](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01626170.pdf) -- Page 12

- **Interest Score:** 61.0
- **Fragments:** 59
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
I
I 
II
I
' 
1 
I 
I 
I 
1
1 IMIIII
I
I
I 
Il 
1 
1 
1 
I 
I 
I 
I
1
1 
1
I
I 
11 1 
1 
I 
I
I
I 
II
I
1
M
I
MI
Im II IMI
I MI I IN
-
 I 'I 
I
I 
11 1 
1 
I 
I 
I 
II 
III 
1 
II
I
1
M
M
1 MI
MI
MI IMI
M
• 
I
I 
11 1 
1 
I 
I
I
I 
II
IM
I
M
M
I MI
MI
1MI
1IMI
1MI
I I
I
I 
Il 
1 
1 
1 
I
I
I 
1 
1 
1 
1 
II
M
IM
I
M
M
I MI
MI
MI IMI
MI I
I
I 
11 1 
1 
I 
I
I
I 
II
I
1
M
M
'1I
MI
Im II IMI
I MI I IN
I
1
M
M
'1I
MI
Im II IMI
I MI I IN
I 
1 
1 
1 
1 
1
I MI
I 
I IM
M
M
1 1
MI
1MI
1IMI
M
1 
1 
1 
1 
1 
I 
I
M
M
I MI
MI
M1 1•1 mi i•
I 
I
I
I 
I 
I 
I 
I
In 
i im M 
M 
I MI 
MI
I M111 1 Imi1i  
ow 
I 
I
I
I 
im
•
•
imi
mi
'
11 1'
11
I I
I- I I I 
I 
I I 
I 
I-
1
M
MI
MI
MI
I MI I IMIM
M
I  -
1
1
1
M1
 
1
1 
-
1 MI
MI
Im II IMI
I MI I IN
1M
I 
I MI
1M1
1 
1
1 
M
I MI
1
' 11 1
' 11 M
1
' 11 1
' 11 •
1
1 
1 
I 
I
I
I 
I 
I 
I 
I 
IM
M
M
I MI
MI
1
IM1
M
•
I-I 
I I-
-
MIMI
MI
I MI I IMI
Im I I IN
1 
1 
1 
1 
1 
I
I MI I IMI
Im I I IN
1 
1 
1 
1 
1 
1
M
I 
I
I IM
M
M
I MI
Mi
1
M
1MI
M
•
1 
1 
1 
1 
1 
1 
I 
I
IM
M
M
I MI
Mi
MI MI
MI I•
1• II•
II
M
M
M
I MI
Mi
MI IM
I
MI I•
I 
I 
III 
III 
I 
I
I
I 
1
I
I II
I
II - 
I= 
M 
MI 
MI 
MI 
MIIMI 
M 
M
I
I  M 
IM 
M 
M 
I I MI 
Mi
MI MI
MI I•
1
1
III
III
1
I
I
I
lin 
M 
MIMI 
MI
?
I I IIMIIII MI I I•
•
•
II M 
IM 
M 
M 
I MI 
MI 
MI IMI 
M 
•
I
I  - 
I
= 1 M 
- 
1 I  MI 
MI
1= 111=1
I MI I IN 
I
I
I
I
I
I
I
I
I  = 
I
- 
1 M 
- 
1 I  MI 
MI
I MI I IMI
I MI I IN 
III
I
I
I
I
I
I
I
II
III
1
'II •
1
1
1
1
I
I
I
M 
IM I 
M 
M 
I MI 
MI
1MI 11_1 
M 
• 
1
1
1• III•
1
1
1
1
I
I
I
II M 
IM I 
M 
M 
I MI 
MI
1MI 1MI
I MI I I•
1• III•
II M 
IM I 
M 
M 
I MI 
MI 
MI IMI 
M 
• 
III
I
I
I
I
I
I
I
II
III
1
II M 
I- 
1 M 
MIMI 
MI 
MI IMO 
M 
M
II
I
I
I
I
I
I
I
I11IM 
M  
M  
MI I  MI
1.1
11_1 
M
IIM I 
 
• 
1
1
1
1
I
I
I
1
1
1
1
1• III•
1
1
1
1
I
I
I
II M 
IM I 
M 
M 
I MI 
MI
1MI 11_1 
M 
• 
1
1
1• III•
II M 
IM I 
M 
M 
I MI 
MI 
MI IMI 
M 
• 
I
I
I II
I
I
I
I
I
II M 
- 
1 M 
- 
1 I  MI 
MIIMIIIMIM
 
M
I
I
I II
I
I
I
I
I
II M 
- 
1 M 
- 
1 I  MI 
MIIMIIIMIM
 
M
I
I
I
1 1
1
III•
I
I M 
I M I
I  M
I  M 
I.1
MI
1_1I 
M
I
 
• 
1
1
II
•MI
1
1
1
I
1
1
1
II M
I 
I 
MM 
I MI I  MI 
MI 1 IMI 
M
 
I
I
I II
I
I
I
I
I
II M 
 
1 M 
 
1 I  MI 
MIIMIIIMIM
 
M
LI
 
in
 
I I I
 
I  M I  II  
II  M 1 I M II I  
1 I M 
I  Mt
I 
I 
I 
I 
M
I  • 
I.1 
MI
1MI 1MII 
M
I
 
• 
'I 
1 
M 
•I 
1 
 
 MI 
1 MI11MI
 
1 MI1OM
 
1 
1 
1 
1 
1 
1 
1
1 
 1 
I
M 
M 
I MI 
MI 
MI
I
M1 
M 
I
I
I
I
I
I
I
I• •
I 
I 
I 
I 
I 
I 
I 
II 
III 
1 
I 
- 
- 
1-I 
-I 
-I 
IMI 
- 
E
I 
I 
I 
I 
I 
I 
M
I 
M 
M 
I MI 
MI
1MI
1IM1I 
M
I
 
••
'I 
1 
M 
•I 
1 
M  
1 1.I
 
1 MI  
1 MI  
1 IM1  
1 
M
1 ••I
I I I = 
I M I II -I
I MI 1= 1111- 1111M 
I 
I 
I 
I 
I 
I 
M 
- 
1 I  MI 
MI
Im II IMI
I = 
1 
I 
I 
I 
I 
I 
I
M
M
I MI
MI
1MI
1IM1
1
M
1
1 
1 
1
1 
1 
1 
11 111
1 
I
M
I MI
MI
MI IM1
M
1 
1 
1
1 
1 
1
1
O
1 
I
M
I MI
MI
MI IM1
M
I 
I 
I 
I 
I 
M 
- 
1 I  MI 
MI
Im II IMI
I = 
1 
I 
I 
I 
I 
I 
I 
M 
M 
I  MI 
MI
1MI
1IM1
1
M 
1 
1 
1 
1•
1 
1 
1 
1 
1 
1 
1 
1 
1•
1 
1 
1 
I 
M 
 
I MI 
MI
1MI 1IM1
OM
I 
I 
I
 
I 
I 
I 
M 
Mini
1MI
I
I
I
M 1
111
M
1 
II 
I 
M 
- 
1 MI 
MI 
MI IMI 
M 
fl
I 
I 
I 
I 
I 
II 
I 
M 
- 
1 MI 
MIImIIIMIM
 
MI 
WI 
m
I 
I 
I 
I 
I 
I 
I 
I 
11 l• 
I • 
M 
I MI 
MI
1M 
I 
I 
• 
IMI 
MI
I 
1 
1 
1 
1 
1 
1 
1 
I 
I
 . 
M 
1 •1 
1 
1 
I 
 
M 
I MI S 
MI
1MI 1IM1 
• 
MI I I•M 
i 
I 
I 
M 
M 
I MI 
MI 
MI IM1 
M 
 
M 
• 
I 
I 
I 
I 
I 
I 
I
I 
' II
I 
I 
M 
M 
'II 
MI
Im II IMIM 
-OM 
M
I 
I 
I 
I 
I 
I
I 
II
I 
I • 
M 
I MI 
MI
1MI
1IMIM 
MI 
. 
• 
1 
1 
1 
1 
1 
1 
1 
I
I 
I
I 
1 •1 
1 
1 
M 
I MI S 
MI
1MI 1IM1 
• 
MII I  M 
• 
I 
M 
M 
I MI 
MI 
MI IM1 
M 
 
M 
• 
I 
I 
I 
I 
I 
I 
I
I 
' II
I 
M 
M 
'II 
MI
Im II IMIM 
-OM 
M
I 
I 
I 
I 
I 
I
I 
II
I 
M 
M 
'II 
MI
Im II IMIM 
-OM 
M
I 
I 
I 
I 
I 
I
I 
II
I 
M 
I MI 
MI
1MI
1IM1 
• 
MI 
M 
• 
1
1
1
1
1
1
1
I
II
I
M 
M 
I MI 
MI 
MI IM1 
M 
 
M 
• 
I 
I 
I 
I 
I 
I 
I
I 
' II
I 
M 
M 
I 
MI
Im II IMIM 
-OM
M 
MI 
MI 
MI 
MII-I 
M 
-OM 
M
I
I
I
I
I
I
I
I
II
I
1
1
M 
I MI 
MI
MI IM1 
• 
MI 
. 
• 
1
1
1
1
1
1
1
I
I
I
M 
I MI 
MI 
MI IM1 
M 
MI 
M 
• 
II
1
I
I
I
1
11 111
1
II
I
M 
M 
I MI 
MI 
MI IM1 
M 
 
M 
• 
I
I
I
I
I
I
I
I
' II
I
I
I
M 
M 
II 
MI
I IMIM 
-OM 
M
I
I
I
I
I
I
I
II
I
1
1
•
1
I MI 
MI
MI IM1 
M 
MI 
M 
• 
II
1
I
1
11 111
1
II
I
1
•1
1
1
M 
I MI S 
MI
1MI 1IM1 
• 
MII I M 
• 
I
M 
M 
I MI 
MI 
MI IM1 
M 
 
M 
• 
I
I
I
I
I
I
I
I
' II
I
Im
I
M 
M 
I III 
MI
I IM
 
-OM 
M
III
I
II
I
II
III
I
nil
```

#### [184] [EFTA01652971](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01652971.pdf) -- Page 22

- **Interest Score:** 60.1
- **Fragments:** 4
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Donald, Andrew, Les, Virginia, Giuffre

**Reconstructed Text:**

```
George 
BREAKIN
Virginia G
THE
EXPER I @Georg .. 
• 1h • • • 
rginia Giuffre killed 
e! 
TS WHO ARE NOW 
NVIRGINIA GIUFFRE
Donald J
La
Les
__
E
G
Richard
FB
DID NOT
VIRGINI
VIRG Andrew. 
z. 
ey, 
rner. 
. 
m, 
n. 
axwell's, 
ssad 
GIUFFRE. 
E KILLED 
FFRE
```

#### [185] [EFTA01731021](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01731021.pdf) -- Page 126

- **Interest Score:** 59.8
- **Fragments:** 23
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Epstein, Black

**Reconstructed Text:**

```
31 2021
(
31 21162820
)I t
i
61717 pd es 
: 30
.30.211
)I t
i
2 21165111 pdf Miotes 9 2 21165111 pdf
Blackbook pdf
(U) Epstein Blackbook pdf
)Interview o roffer 5.14.21.pdf 
(U 
 roffer 5.14.21.pdf 
549 pdf
(U)Jmage 161549 pdf
2 21204232 pdf
(UMotes8 12 21204232 pdf
238.pdf
(U•otes084238.pdf
view notes10330 nterview notes103309.pdf
) Interview o
erview notes 6.2.2116 nterview no
) INT 00000 ) INT 00000
ew_notes_9.1.21.pdf (U 
interview notes 9.1.21.pdf
(U) Service of subpoena. 
(U) On Tuesday, September 21, 2021
```

#### [186] [EFTA01387651](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01387651.pdf) -- Page 0

- **Interest Score:** 59.6
- **Fragments:** 3
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Les, Sarah

**Reconstructed Text:**

```
The hunt 
for security 
zlcti 
c.igi)inst 
cybercrime and geopolitical risk 
Thursday, October 26, 2017 
:2 00prn. 21/j err. 
Ti's Colt 99 East 54'd Strait hie* Yon( 
4..T9 
ffN N 
rl(A l
Patrick Campion. Head of Deutsche dank Weal*, Management 
Amerces b pitsnsed to lave::: you lo 3 pity-ate discussion on repent.
deweimaments in the cyber security seyffor 
The conversation will include fascinating insights Into cyber-attacks 
and how to counter them—as well as informed ideasonhow to
roach investingin the cybei security
Sort Spea<eiS 
N 
Chef Information Security Officer, 
CantralIntaliiroce Agency 
Cy-ui 
tasy 
Global Chief Inuestinent Cancer. 
Deutsche Bat* Wealth Management 
RSVP to Sarah Rafferty al larin.citsutigsly o'er 
hen. hat' TottraMesataw 
pe..^InIMIrreenlaL rainety 
Mil.VerMrdirlesrairsaed*Cktp 
tete, teettIo•JR•AVO "Wide* tocri Thaw Gaorp.ow. 
na•ten nit afar.. Palace, are Coat...
```

#### [187] [EFTA01376953](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01376953.pdf) -- Page 0

- **Interest Score:** 59.2
- **Fragments:** 21
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
TWTR
A
usam US $ 
i 37.03 
37.02 37.0
At 14:59 
Vol 13 867 990 036.49T 
37.33 
3
matam
egiowmar 3 
6.37 
Par 1/6
1 9 
2.48M 
oe's/ ri
"fable
tter Inc g
Period 
(ncrenne 
ffifwatiart Nn 
Hite/. 
:Ivor 
Net e 
Tr"--
Varn -
55
3
43
1 on 
10/0
 
898 
 
on 
06/0
74,423
9
37.00 
13,834,808 
US/08/1S 
37.5
05/07/1S' 
37.7 2 t  
4 Ile 
(A/1/715 
04/16/15 
50
52 6 
3 
16
14
05/21/15 
36.41 
t te 95/26/15 
36.51 
14,463
13,068 rio 
Su 
OS/06/75 
37.26 
05/05/15 
37.42 
2
2 We 
Ile 
04/15/15 
04/14/15 
5130 
5120
13,192
12,231
5 
, 
36.
5 
36.
 
36.
5 
315
 
37.
 
37.
5 
373
 
37.7
5 
37.
373 8 
 
0 
8 
 
3 
8 
 
9
17
23
26
1
16
14
14
1
12 to 05
I 05
Th 04
We 04
 fu 04
k, 04
5e 04
 th 04
*el. 04
8 rrr, 04
`4 5 
3
5 
S 
 ti
5 
S
`. 
S 
5 
5 
5
3
4 8 
6 
 
 
 
 
 
 
2
3
4
12
7
.
1
1
1
1 5 
3 
5 
5 
5 
5 
h 
5 
5 
5 
5 
5
All
d
i
i f
i
```

#### [188] [EFTA01370410](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01370410.pdf) -- Page 0

- **Interest Score:** 58.5
- **Fragments:** 3
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Les, Barak, Paul

**Reconstructed Text:**

```
Scott Prokop 
;
• B
PWMLatAm_NY-Miami SVC 
Matthew Pontoriero 
Moore 
Natalie 
Hilde 
Barak 
rde Berrios 
Maur
; Anu 
; Ma 
The
; Eliz
B
; Pa
PWMLatAm_NY-Miami SVC 
Eduardo Pieta 
Andrea Nicoletti 
Mary C 
• 
Keaveney 
uana Beale 
Lantz 
Rachel
aglicic 
Mark RWesthoff 
Wolkenb 
l
rod 
Michae S Jacob 
Brown 
M 
W 
Cataudella 
Westhoff 
Keavene 
Lantz 
Germany 
Edward Golden 
Timothy MacGuire 
Carmen A Ayala 
; B
; Salva
; H
; Timoth
B
• Michae
Brian 
; Fo
; 
; Cath
; Ove e-NI Quattrocchi 
rios 
Beat
; E
; Carol Meister I 
Romano 
Prokop 
a 
Brandi Goldenber 
ge 
n 
; Michael Mullin 
yer 
chel Plut 
on-Services German 
ee Flutter 
 Ed Lok 
ean Jules 
; Joanne Jensen 
; Vincent Commisso 
• Ca
Gavin Kim 
• Stew
Josie Alo
; 
R
Mauricio Pretelt 
Edward G
; B
• M
h 
resnahan' 
Betts 
A McGrath 
uattrocchi 
ichel Plut 
or 
T
; Ste
; 
; 
T
J
; Kimbe
; Heath
; Rachel Maglicic
• Br
; Mal
• Deirdre J
;Catherine M ()Connor 
Michael S Jacoby ; C
elanis 
I; Lesle
hrab 
Josie Alo
riguez 
occhi 
olover 
• Sha
I; Bria
nnor 
on 
Paul E Be
mble 
a 
ernadette
on 
e 
hen-M Jo
acob 
Team-E
rts 
Chip Pa
TING
```

#### [189] [EFTA01377958](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01377958.pdf) -- Page 0

- **Interest Score:** 56.1
- **Fragments:** 12
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Les, Roberts, Bradley

**Reconstructed Text:**

```
okop 
Romano 
; Gavin 
Carlos -M Quattrocc
Bradley Gillin
id M
i
Josie Alonso 
Hilde arde Berrios 
Mayra Fonseca 
Lesley
; Michel
; Edward Go
; Beatriz Die ;'Matthew
uricio Pretelt 
elanis 
; 'PWM
;
Les
Ju
hardt rie Hansen Cosby
ardt 
I; Liz
Essenbreis 
e 
on 
ove 
a Wilbur' 
breis 
el Lantz 
es germany 
nberg 
• Seq
; Mic
Sean 
; M
;'Jo
Br Hansen Cosby
I; Gavin K
ouglas Robertson 
Tangney 
y MacGuire 
rath 
; 
• Mic
; team-
; Leann
; 
J McCoy 
nberg 
; Michael 5Jaco
Robertson 
y 
; Kimb
]
-M Quattrocchi 
Sohrab 
; Tim
n.' Stanfield 
• And
Teresa Metallo 
; Talith
• utstan ng 
icia 
ecks R
Official Outstanding Check Re ra Jasper 
18 
2018 zip
; O
```

#### [190] [EFTA01453345](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01453345.pdf) -- Page 0

- **Interest Score:** 55.5
- **Fragments:** 10
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Epstein, Jeffrey

**Reconstructed Text:**

```
uptalIMIS
"'lir - 
197.28 /97.29 _ 
1 2 
., 96.95 
8.119 
Op 96.80 
Hi 97.31 
06.6S 
0penInt200854 
119-9we Ns
vs Actions
-
97) 551ff •
9
Teele
'.' ca-eve 
*2 N
C
103.00 
102.00
1 
1 
1 
I 
I 
l 
f 
101.00 
 
100.00 
 
I 
1 
99.00
iiii  Last Pr
T High on 
F 4- Average
[ .1 Low on 
• Prey Clo
19 20 21 
Used with perm e 
9
3/03 10:30 10
9
3/17 13:00 
9
e  
 
10
24 25 26 
2
eb 2014 
ission of Bloo 98.00 
28 03 04 05 06 07 10 11 12 13 14 17 18 
Mar 2014 
rg Finance LP
"jeffrey epstein" <OevacatioNgpr
Trade Report 3/13/14 w
```

#### [191] [EFTA01385894](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01385894.pdf) -- Page 0

- **Interest Score:** 54.9
- **Fragments:** 23
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
TWTR US $ 
1 37.03 
• .62 
r'
-- 
N37.O2 /37.O
a... At 14:59 
Vol 13 867 990 0 36.49T 
H 37.33D 
1 3
mm 3K 
1
.37D 
V 9 
2.48M
11SMIIIU
Twine, Inc
Ra rap. 
rlarkrl
iq WY6wi llittir
rerk
,  
t 'Hew./ 
D T""nn "M"""Mr"""""154nrinalrflarPnarnbre""
Iti9h 
55
el 
I .OW 
31
Ave r a4ct 
41
Itt r hei 
3
"i
i 2 
on 
10/0
5 
on 
06/0
98 
24,423
3 
9
fi lE
B
5 
 
3
. 
3
5 
3
 
5 
3
5 
3
 
3
5 
3
 
3
S 
3
5 
3 00 
13
41 
1
51 
13
60 
9
68 
1
78 
73
50 
26
78 
1
0 
1
33 
14 ; r 05
Th 05
w' 05
To 05
OS
• t 
0
Th 04
W" 0
10 04
0
1. 0
It, 0 g
5 
S, 
S 
3
5, 
S 
. 
: 
5 
5 
4
5 
5 
5 1
 
2
 
2
 
2
2
3
6 
4
 
17
 
7
 
7
 
1
 
1 5 
5 
. 
5 
5 
5 
5 
5
5 
S 
5
S 
5
3
S 
3 W. 04/72/IS 
5
8 Tti 04/21/15 I h. 04
In 03 5 
5
5 
5 7 
8 
2
o•,7t1/1!. 
3/11 
1 o•,7t1/1!. 
3/11 
17,379,401 
04/10/ kc 
51.40 
11,004,476 
03/30/15 
49.89 
70,365.393 01 
04/10/ kc 1.40 
1 4,476 
03/30/15 
4
```

#### [192] [EFTA00014026](https://www.justice.gov/epstein/files/DataSet%208/EFTA00014026.pdf) -- Page 0

- **Interest Score:** 54.5
- **Fragments:** 4
- **Document Type:** OTHER
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Jeffrey, Edwards, Palm Beach

**Reconstructed Text:**

```
' 
(USAFLS)" <I 
"ROBERT C. JOSEFSBERG" 
EZELL" 
' 
[=. 
(USAFLS)" 
 
(USAFLS)" <I
West Palm Beach, FL 33401
ROBERT C. JOSEFSBER
(USAFLS
t: Mon Dec 29 17:16:03 20
bject: Jeffrey Epstein ; KATHERINE W. EZELL; Brad Edwards 
8
```

#### [193] [EFTA01748145](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01748145.pdf) -- Page 0

- **Interest Score:** 53.4
- **Fragments:** 15
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Stephen, Paul, Jay

**Reconstructed Text:**

```
IMINSII~I>
<a, 
T
wski, Te 
reth Riley" , N
olly"
D vari' ^c^-4 cA" "Flint Alexis"
A
as t~~.....e "Spire, Jean
terbi
aiff~saiiHorowitt
Gre " Ro er Guillemin
Mille 
Hovanissian e, ndy Pelletier apu
Michael McCullou h 
, Sam Horowitz 
, Ju y W fie < 
Paul Kreutz 
ggaspen Ilia 
Stephen Wolfram 
Michael Farrell  
-1 
Jay 
nz cr Cullou h
1.0.1~11,
```

#### [194] [EFTA01461027](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01461027.pdf) -- Page 0

- **Interest Score:** 53.0
- **Fragments:** 6
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
SPX 
T 391/.01 
1916.53 / 1917.66 
At 10:28 
0 1925.63 H 1936.98 L 1915.30 Prey 1928.21 
SPX I d
6) A ti
97) E
i
O
i
M
i
O
i
M
i
500 IN DEX 
Ce .2c) 
Strik p
p
936.98 
Lo 1915.30 
Volm 
HV 13.51 
52) Earnings Catendar(ACDR)
11) :-,r'„ __ ,__ , 
J6 -,,y 
lii.04 
. .:),, 
1875 
12) SPX 11/22/ 
64.40 68.30 72.20y 18.66 .62 
11 
1880 
13) SPX 11/22/ 
60.90 64.50 130.6 
0.,,l 
18.38 .61 
2 
1885 
14) SPX 11/22/ 
57.50 61.10 65.00y 18.17 .59 
23 
1890 
15) SPX 11/22/ 
54.20 57.90 66.10 17.96 .57 
1 
13 
1895 
16) SPX 11/22/ 
50.90 54.30 55.35 17.70 .56 
1 3406 
1900 
17) SPX 11/22/ 
47.70 51.10 57.99y 17.46 .54 
9 
1905 
1.3) SPX 11/22/ 
44.50 47.90 51.80 17.19 .52 
3 
220 
1910 
19) SPX 11/22/ 
42.20 45.00 69.20y 17.16 .50 
7 
1915 
20) SPX 11/22/ 
38.60 41.90 41.00 16.77 .49• 
16 
234 
1920 
21) SPX 11/22/ 
35.70 38.70 39.40 16.49 .47 
13 11107 
1925 
22) SPX 11/22/ 
33.00 35.90 35.00 16.24 .45 
6 2121 
1930 
73) SPX 11/22/ 
30.30 33.10 36.50 15.98 .43 
9 1045 
1935 
24) SPX 11/22/ 
27.70' 30.40 28.90 15.74 .41 
55 3672 
1940 
25) SPX 11/22/ 
25.80 27.80 30.00 15.58 .39 
1 1282 
1945 
26) SPX 11/22/ 
22.90 25.40 24.20 15.22 .37 2547 17069 
1950 
27) SPX 11/22/ 
20.70 23.10 27.40 14.99 .34 
17 
525 
1955 
28) SPX 11/22/ 
18.601 20.90 21.00,14.77 .32 
25 1446 
1960 
_9) SPX 11/22/ 16.701 18.90 17.90114.531.301
65 5022 
1965 
61 SPX 11/2: 29.90 
32.40 31.00 18.69 -.36 
55 28333
62) SPX 11/2% 31.60 
33.70 24.97 18.51 -.38 
11 1735 
63) SPX 11/2: 32.80 
36.20 32.50 18.42 -.39 
23 1860 
64) SPX 11/2: 34.30 
37.80 35.20 18.21 -.41 
31 9295 
65) SPX 11/2: 35.70 
38.50 34.05 17.74 -.42 
2 404 
66) SPX 11/2: 37.60 
39.80 39.06 17.48 -.44 29640 4295.,
67) SPX 11/2: 39.30 
42.20 40.25 17.35 -.46 
25 1187 
68) SPX 11/2: 41.10 
44.80 43.90'17.24 -.48 
58 5781 
69) SPX 11/2 
43.10 
46.70 45.10 17.02 -.49 
27 
112 
70) SPX 11/2: 45.00 
48.80 46.20 16.80 -.51 
146 7353 
71) SPX 11/2: 47.10 
50.60 46.80 16.47 -.53 23200 4076,-
72) SPX 11/2: 49.20 
53.10 51.00 16.27 -.55 
51 1095•
73) SPX 11/2: 51.50 
55.40 45.50 16.03 -.57 
63 1067
74) SPX 11/2: 53.90 
57.90 54.90 15.81 -.59 
95 6573 
75) SPX 11/2: 56.30 
60.40 56.50 15.54 -.61 
20 
728 
76) SPX 11/2: 58.90 
63.00 60.85'15.30 -.63 
185 3748 
77) SPX 11/2: 61.30 
65.80 53.90 15.00 -.65 
1 1131
78) SPX 11/2; 64.00 
68.80 64.90j14.82 -.67 
38 6453 
Zoom
```

#### [195] [EFTA01462259](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01462259.pdf) -- Page 0

- **Interest Score:** 53.0
- **Fragments:** 6
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
SPX 
T 391/.01 
1916.53 / 1917.66 
At 10:28 
0 1925.63 H 1936.98 L 1915.30 Prey 1928.21 
SPX I d
6) A ti
97) E
i
O
i
M
i
O
i
M
i
500 IN DEX 
Ce .2c) 
Strik p
p
936.98 
Lo 1915.30 
Volm 
HV 13.51 
52) Earnings Catendar(ACDR)
11) :-,r'„ __ ,__ , 
J6 -,,y 
lii.04 
. .:),, 
1875 
12) SPX 11/22/ 
64.40 68.30 72.20y 18.66 .62 
11 
1880 
13) SPX 11/22/ 
60.90 64.50 130.6 
0.,,l 
18.38 .61 
2 
1885 
14) SPX 11/22/ 
57.50 61.10 65.00y 18.17 .59 
23 
1890 
15) SPX 11/22/ 
54.20 57.90 66.10 17.96 .57 
1 
13 
1895 
16) SPX 11/22/ 
50.90 54.30 55.35 17.70 .56 
1 3406 
1900 
17) SPX 11/22/ 
47.70 51.10 57.99y 17.46 .54 
9 
1905 
1.3) SPX 11/22/ 
44.50 47.90 51.80 17.19 .52 
3 
220 
1910 
19) SPX 11/22/ 
42.20 45.00 69.20y 17.16 .50 
7 
1915 
20) SPX 11/22/ 
38.60 41.90 41.00 16.77 .49• 
16 
234 
1920 
21) SPX 11/22/ 
35.70 38.70 39.40 16.49 .47 
13 11107 
1925 
22) SPX 11/22/ 
33.00 35.90 35.00 16.24 .45 
6 2121 
1930 
73) SPX 11/22/ 
30.30 33.10 36.50 15.98 .43 
9 1045 
1935 
24) SPX 11/22/ 
27.70' 30.40 28.90 15.74 .41 
55 3672 
1940 
25) SPX 11/22/ 
25.80 27.80 30.00 15.58 .39 
1 1282 
1945 
26) SPX 11/22/ 
22.90 25.40 24.20 15.22 .37 2547 17069 
1950 
27) SPX 11/22/ 
20.70 23.10 27.40 14.99 .34 
17 
525 
1955 
28) SPX 11/22/ 
18.601 20.90 21.00,14.77 .32 
25 1446 
1960 
_9) SPX 11/22/ 16.701 18.90 17.90114.531.301
65 5022 
1965 
61 SPX 11/2: 29.90 
32.40 31.00 18.69 -.36 
55 28333
62) SPX 11/2% 31.60 
33.70 24.97 18.51 -.38 
11 1735 
63) SPX 11/2: 32.80 
36.20 32.50 18.42 -.39 
23 1860 
64) SPX 11/2: 34.30 
37.80 35.20 18.21 -.41 
31 9295 
65) SPX 11/2: 35.70 
38.50 34.05 17.74 -.42 
2 404 
66) SPX 11/2: 37.60 
39.80 39.06 17.48 -.44 29640 4295.,
67) SPX 11/2: 39.30 
42.20 40.25 17.35 -.46 
25 1187 
68) SPX 11/2: 41.10 
44.80 43.90'17.24 -.48 
58 5781 
69) SPX 11/2 
43.10 
46.70 45.10 17.02 -.49 
27 
112 
70) SPX 11/2: 45.00 
48.80 46.20 16.80 -.51 
146 7353 
71) SPX 11/2: 47.10 
50.60 46.80 16.47 -.53 23200 4076,-
72) SPX 11/2: 49.20 
53.10 51.00 16.27 -.55 
51 1095•
73) SPX 11/2: 51.50 
55.40 45.50 16.03 -.57 
63 1067
74) SPX 11/2: 53.90 
57.90 54.90 15.81 -.59 
95 6573 
75) SPX 11/2: 56.30 
60.40 56.50 15.54 -.61 
20 
728 
76) SPX 11/2: 58.90 
63.00 60.85'15.30 -.63 
185 3748 
77) SPX 11/2: 61.30 
65.80 53.90 15.00 -.65 
1 1131
78) SPX 11/2; 64.00 
68.80 64.90j14.82 -.67 
38 6453 
Zoom
```

#### [196] [EFTA01422362](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01422362.pdf) -- Page 3

- **Interest Score:** 52.8
- **Fragments:** 9
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Les, Mitchell, Paul

**Reconstructed Text:**

```
Richard Leeds 
Matthew Kadar 
Third Lake Cap
Kiser 
Kim 
Kim, Steven 
Kirwood 
Kokas 
Collis
Ch
l
Philppe
an 
Lawrence 
Lawrence --
Stew 
Paul
N
el -- 
Yorkt
Jonathan 
Liggett 
nathan Liggett -- 
Neal 
Milch 
Paul 
David 
Mitchell 
vid Mitchell --
Scott 
Lindell 
Stew 
Adam 
Lindemann 
am Lindemann -- 
Erik 
Moody 
Paul 
N 
II
- 
Linde
 
Paul 
General Atlantic Fami
Paul 
N 
A1486
Dhruv Maniktala -- 
Markus 
Paul 
Y 
Blue Mountain 
Martin 
Stew 
Y 
A
Shamrock 
Masuda 
Stew 
Y 
Caruso, Richard 
Meister 
Paul 
Y 
A
Meister, Todd 
Meiste 
Paul 
Y 
A
Meister
Todd
Bluestem
Bonnie Mitra 
Orix 
Sandy 
Pensler 
ler --
Joe 
Monaco 
Collis, Charles 
Katherine 
Montrone
```

#### [197] [EFTA01422362](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01422362.pdf) -- Page 5

- **Interest Score:** 52.6
- **Fragments:** 5
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Bill, Les, Chris, Paul

**Reconstructed Text:**

```
tiles 
tiritz 
Dorrance
Kristin Eby 
y --
John 
Straus 
Michael Tabacinic 
chael Tabacinic -- 
Drew 
Tarlow 
Luke 
Thomas 
Rahul 
Vaid 
Stew 
Parami Capital Managem
Stew 
Stew 
Fallin
Third Lake Ca
Stew 
Stew 
- 
 
Collis, Charles 
Cox, Berry
66" 
"fiC216=Christoper Zafiriou 
Gosha 
Zandt 
Richard Zipkis 
chard Zipkis --
Alex 
Zubillaga 
ex Zubillaga --
Richard Kahn 
■ 
Warner Steve 
Mike 
McVean 
n --
Guy 
Stew 
Y 
A
Stew 
Stew 
Stew 
Stew 
Stew 
Granite G
Paul 
A220&" "6B
A221O "6
• 
A
A223&" "6B
```

#### [198] [EFTA00015963](https://www.justice.gov/epstein/files/DataSet%208/EFTA00015963.pdf) -- Page 0

- **Interest Score:** 52.5
- **Fragments:** 19
- **Document Type:** OTHER
- **Dataset:** ds1-9_11-12
- **Names Found:** Epstein, Ghislaine, Scarola

**Reconstructed Text:**

```
ack Scarola 
Weeets 
Ma M
(FBI)"
16 2020 10 37
Wetjets<a
M ry McCann <
ubject: Re:
in a c alk in ad
will probably ass
Epstein Palm Be
dealings with of 
und him a 
coopera
ex boy
Ghislaine Max
ook he outsid
went w o Epstein
arran ements. Acted like secretary
Some older man came
may h
- saw him at hous
```

#### [199] [EFTA01449275](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01449275.pdf) -- Page 0

- **Interest Score:** 52.5
- **Fragments:** 6
- **Document Type:** OTHER
- **Dataset:** ds10
- **Names Found:** Alan, Bill, Les

**Reconstructed Text:**

```
Figure 1: The basic balance remains positive... Figure 2: 
as net FDI inflows continue to climb
Figure 3: Net Portfolio flows have been falling since 
2010 
200
200 Figure 4: Foreign investors have favored Australian 
debt (negative IIP a liability for AU)... 
Wt (baby liP
Figure 5: 
and to a lesser extent equities... 
450
Not Equly Ltabilliss for AU 
450 g
y
p
y
Australians of foreign debt 
700 
—lint Debt Labiate; lot AU
```

#### [200] [EFTA01365171](https://www.justice.gov/epstein/files/DataSet%2010/EFTA01365171.pdf) -- Page 0

- **Interest Score:** 52.5
- **Fragments:** 5
- **Document Type:** OTHER
- **Dataset:** ds10

**Reconstructed Text:**

```
SPX 
T 1911.O1 
11. 
1916.53 /1917.66 
At 10:28 
0 1925.63 H 1936.98 L 1915.30 Prey 1928.21 
6) A ti
97)
500 IN DEX 
Ce p
p
936.98 
Lo 1915.30 
Volm 
HV 13.51 
92) Earnings Calendar (ACOR
II) L-A',., __ ,_ , 
:46._,,y iL•,..3.4 .3,, 
1875 
12) SPX 11/22/ 
64.40 68.30 72.20y 18.66 .62 
11 
1880 
13) SPX 11/22/ 
60.90 64.50130.6 
0.,,l 
18.38 .61 
2 
1885 
14) SPX 11/22/ 
57.50 61.10 65.00y 18.17 .59 
23 
1890 
15) SPX 11/22/ 
54.20 57.90 66.10 17.96 .57 
1 
13 
1895 
16) SPX 11/22/ 
50.90 54.30 55.35 17.70 .56 
1 3406 
1900 
17) SPX 11/22/ 
47.70 51.10 57.99y 17.46 .54 
9 
1905 
18) SPX 11/22/ 
44.50 47.90 51.80 17.19'.52 
3 
220 
1910 
19) SPX 11/22/ 
42.20 45.00 69.20y 17.16 .50 
7 
1915 
20) SPX 11/22/ 
38.60 41.90 41.00 16.77 .49• 
16 
234 
1920 
21) SPX 11/22/ 
35.70 38.70 39.40 16.49 .47 
13 11107 
1925 
22) SPX 11/22/ 
33.00 35.90 35.00 16.24'.45' 
6 2121 
1930 
23) SPX 11/22/ 
30.30 33.10 36.50 15.98 .43 
9 1045 
1935 
24) SPX 11/22/ 
27.70 30.40 28.90 15.74 .41 
55 3672 
1940 
25) SPX 11/22/ 
25.80 27.80 30.00 15.58 .39 
1 1282 
1945 
26) SPX 11/22/ 
22.90 25.40 24.20 15.22 .37 2547 17069 
1950 
27) SPX 11/22/ 
20.70 23.10 27.40 14.99 .34 
17 
525 
1955 
28) SPX 11/22/ 
18.601 20.90 21.0014.77 .32 
25 1446 
1960 
:9) SPX 11/22/ 
_6.701 18.90 17.90114.531.30'
65 5022 
1965 
6:1 SPX 11/2: 29.90 
32.40 31.00 18.69 -.36 
55 28333
62) SPX 11/2: 31.60 
33.70 24.97 18.51 -.38 
11 1735 
63) SPX 11/21 32.80 
36.20 32.50 18.42 -.39 
23 1860 
64) SPX 11/21 34.30 
37.80 35.20 18.21 -.41 
31 9295 
65) SPX 11/2: 35.70 
38.50 34.05 17.74 -.42 
2 404 
66) SPX 11/2: 37.60 
39.80 39.06 17.48 -.44 29640 4295_
67) SPX 11/2: 39.30 
42.20 40.25 17.35 -.46 
25 1187 
68) SPX 11/2; 41.10 
44.80 43.90 17.24 -.48 
58 5781
69) SPX 11/2: 43.10 
46.70 45.10 17.02 -.49 
27 112 
70) SPX 11/21 45.00 
48.80 46.20 16.80 -.51 146 7353 
71) SPX 11/2: 47.10 
50.60 46.80 16.47 -.53 23200 4076-
72) SPX 11/2: 49.20 
53.10 51.00 16.27 -.55 
51 1095.
73) SPX 11/2: 51.50 
55.40 45.50 16.03 -.57 
63 1067
74) SPX 11/2: 53.90 
57.90 54.90 15.81 -.59 
95 6573 
75) SPX 11/2: 56.30 
60.40 56.50 15.54 -.61 
20 728 
76) SPX 11/2: 58.90 
63.00 60.85 15.30 -.63 
185 3748 
77) SPX 11/2: 61.30 
65.80 53.9015.00 -.65 
1 1131
78) SPX 11/2: 64.00 
68.80 64.9014.82 -.67 
38 6453 
Zoom
```

