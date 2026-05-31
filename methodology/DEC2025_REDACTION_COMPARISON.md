# December 19, 2025 Epstein Files Redaction Comparison Report

## Executive Summary

On December 19, 2025, the U.S. Department of Justice released DataSets 1 and 2 of the
Jeffrey Epstein Task Force Act (EFTA) documents. The redactions in these documents were
improperly applied: black rectangles were drawn over sensitive text in Adobe, but the
underlying text remained selectable and copyable in the PDF. The DOJ subsequently
re-released these datasets with proper redactions (text actually removed from the PDF
content stream).

This report compares the original poorly-redacted December 19, 2025 release to the
corrected re-release to identify exactly which documents were affected and what text
was exposed.

### Key Findings

- **Total documents with different file hashes between releases: 59**
  - DataSet 1: 58 documents (out of 3,158)
  - DataSet 2: 1 documents (out of 574)
- **2 documents removed entirely** from DataSet 1 ([EFTA00000467](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000467.pdf), [EFTA00000468](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000468.pdf))
- Breakdown by category:
  - Documents with meaningful text exposed: 8
  - Documents with OCR artifact differences only: 18
  - Documents with PDF structure changes only (no text diff): 26
  - Documents with current-only text changes: 7
- DataSets 3-8 were **NOT affected** by this issue (released later, after Dec 19)

## 1. ZIP File Comparison

| Dataset | Original ZIP Hash | Current ZIP Hash | Orig Size | Curr Size | Differ? |
|---------|------------------|-----------------|-----------|-----------|--------|
| DataSet 1 | `c54a12403fbb352113aa544934b5d156` | `b77a0ae7d07f94929883b4415cc62173` | 1,322,628,898 | 1,321,480,300 | YES |
| DataSet 2 | `3d23e215c75cc35ac2944c86ebb15f4d` | `0c043b6362e493e9134159bb2699e943` | 661,420,596 | 661,431,549 | YES |

Both DataSet 1 and DataSet 2 ZIP files differ between the original Dec 19 release and
the corrected re-release, confirming the DOJ replaced these files.

## 2. Documents Removed in Re-Release

Two documents present in the original DataSet 1 release were completely removed in the re-release:

| Document | Content |
|----------|--------|
| `EFTA00000467.pdf` | `‘4. 
it
-n•Alte
r:12
 ":41.
% 
C.! 
tZ 
[EFTA00000467](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000467.pdf)` |
| `EFTA00000468.pdf` | `EFTA00000468` |

## 3. Documents with Meaningful Text Exposed by Poor Redaction

These documents contain readable text in the original that was removed in the re-release.
This text was hidden behind visual black rectangles but remained in the PDF data.

### [EFTA00000470](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000470.pdf).pdf (DataSet1)

- Original size: 433,324 bytes | Current size: 429,003 bytes
- Original text: 77 chars | Current text: 22 chars
- Text delta: +55 chars

**Text EXPOSED in original (behind poor redaction):**

```
<
Nit
.t:C I
.4 1.0
8
.......
I II
_ i
s
Casper
z
C
<
```

**Text in current re-redacted version (replacement):**

```
MAIL
I
```

---

### [EFTA00000476](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000476.pdf).pdf (DataSet1)

- Original size: 365,781 bytes | Current size: 362,263 bytes
- Original text: 2,853 chars | Current text: 2,392 chars
- Text delta: +461 chars

**Text EXPOSED in original (behind poor redaction):**

```
)1
4
04044 so 4,10y• yentaYI ory a
4
Afaoutt •••W a Paso pew teoi 016.4
L290
/39 51 • 92100'0I
ono wna••5'N faclad) • 905060 it
affas
fkOff SO C
WO,
8402 IOp
4 €
61 Qua
e
al e rt
and 80 AUs 1 a .6vAIS
IL°
I forittafld uo %WI* tied Padua
r 5  as
fi t
r"W AT59i
a
cs
ai nca
fraws ▪
ff A Para a
au
ta
°4
7 ""
fence
Th
at
se"..;:s
t„
▪ :
°° 1,28os
°linos . 7.•
*Mtn.
no
088,52080 0747
Oa Iota oaf
C•o347004 Woe
arf.00ce
Olfor3fal vfor
02re rata ar
03.26/2cot Yofe
Coat ra
woe
09.070X9
1110
ta nsy
'1"888ant
fa Ware Da
ma Was Car r
JOON. conerin
florae rasa
Thr..4 hOrdin. DOS
lbnFri New 005
tans x lee..
fota 8-oroof K rota & Sr.,.-p, P A
Oral
teapot PC
lerytingAn0 MANKRawc•I ryyp
Van 'Sera iaea of ~a
FM.nu.
nn'.''
FOR T.
CAN., epoSSOI:Mtn.
" PE XX, SEP
4Th
?ST.
tat • 10 DODS
fftrao
a Onnana
sy Ft..
ei,rts
"a.
M. Jo; flurAn, OA" To,o,..
001 • Rd* Ono.*
0.8
Cle•
0.4
MI.35.041 rwo
Well. Owls l MS OR
OW la Ow 075 WO
RANO Oa 100000 Pr, ne
Oysta (manatee to...
toe w•
ol
Vn 00
„
,0001
150%
oat*
r 0100
2% COO 00
PA CA
4.821.111
•••••••••
floaliraus
aloft
4080000
4131.30.01
8501:84,:,
13251360 16%82 Maw Ag
<0400006 Vans
Scent Vinon a T m0010
caw. 8. Ca 78884
4201824
88n9 us8288480880,7887.1..
O2301000 VAR,"
CoMfatt AzflopOA FtP
Elan& War. Car TV
424524
i
&Kir
05,302006 vanan Vonsto Sawa, froffekap. MCI
Tesonon• • tone 888m.
1 20 00
(882.0'+48 2778.4.78 J781 8.003
a
I
II
4
Atil Da &null
a
09f302006 Was
FeWid (WON
*vow, 0.8.ecy
2 724 20
96 PSIS
l'itetta0 0 (V Put
il
l
i
0581342008 8701
Iniarfor Office a Cann, Owe
00%0, sitatie Aral
-1)37)00
7.0116tC1
(OX
(DO rat
)
DOW T8 Any ma notword
'
5 2
,
I
;
v.
sans
Aim ntrci Jo) 0,4
1
0571372009 8703
08713Th:06 8702
090320% 8704
04,13'1006 8705
Insurattas 0444 d Cantial Olve
Parma* Gila a Central ONO
Inatome* Offte of Gast Ora
tr4L45,44 Office m Cram One
50% Off ea Were/prom
50%fol Par.
SO% of Zeno PAOITROlars
50% of 2440 4444r440*.
7660200
SO 70
42100
•2402 CO
'agate)
Sig 1/0 Y, 0441 /0804008305)
!
000 /52006 8'47
841 3DC*5
8707
Invtince Ca:A of Cer!nil Ooo
auffro. 081ce of central Oror
5014 of Osifn 0*500 toroasoirof
50% of Porto's% Umtata Paco
II 212 00
31=92
tient
awe WOWS° awn - out
.7o 4785 70
Seas
.ape—
Neelpeyite(Al WI MI)
02112006 8700
09/18,2005 8724
Armencim Express 3718-65847245009
Ammon E/381411 372740633241005
bourne 3113 8564723609
Acoouni • 3727 M638241005
'5721000
.149.474 14
SSW
900nliPatai a
08,13/2006 8720
American Expos* 3715669401-4 7008
Aa0of. 371545940447009
-241142
09,247/800 8751
Colonial Bet 4470 1153 4000 5213
888444r8 • 4701153 4000 5215
-37.10502
Nati
000812006 6754
Colonial Bonk 44t0 1153 4008485
ACCOUM • 4470 1153 40,20 08411
4.41L82
itaaliaa
```

**Text in current re-redacted version (replacement):**

```
PNWPG0  410 gnog. ~us
a ai d ai
~aka
, aall
Pace a. av Pal
•
1,2
"9 -lart
...soW
ao &Jaa -,010~1,
OC•91 -tø JO
o0 tad
J 90
eas
4. pa Kl 01~
SIV
04d a AOF
PO *SKYS Ul SLOM
g 00
9,
Q
z
00 te9 Sr • 47 100'01
sa
a...ar..
n-0
I
q
Ilt ri t
r6 tete)
alfa -SPØ
ISO ria)
P•dun
• ~
pale no %Ot"
§
=II
1
50-51.950 la -13 bad Ag
log eig 4.~
11
!Sagmo ida
j ny JI.ItC0 tadd  -a
gi
risswPo rs7 Pov AN Pv soll
I
i ;
900e .ce ard mo umwhici
1
3, g 1
8~048
~
101 al .4
»- g a
~ mo. owd A5 • 00,141
a me ~89
48456n • 6of
/88.4 666
sped
401Pd 4SL net 1
6
BOW Ti ~ri
1
00. b2000
09,2~
Va.
CSOG~
VW*
ro
N A P.a..o, re
~Ny
p
&Na Iowa
tw was.
lam Won., Ca.
Jaa Tateno el a
NMIr
oy
Tatenea
bt
J~P"
asteta.
"..."'ø
N:"
'lasken...Ni Ra
nffNf
fe I a-. Is
INWPNION Atl N:.
NPf4100 Of P f ≥0Ort
f"
2TNI
noti. ivHlrf Notatn Shrot ta
OwWP ~on
P C
MIN•NeeNNI ONN*
r
y
_
041
Gek
Ga
Nano,
an. »a ~4
.9.4 ta_
W
It 00p.at
ita a tole i. "it CCO
Na, o pye 17, g00
bla
OP• %OG C.X> ~n a
fill•baa
'flOSto
453000,
0007~
112$
'Ar Sitat battrl a iletarea Ara
Gotter EINTYPS tan
-150 voo
oriDr-l000
yallot
<moar. Sofa. ~tat
4 i ~nø
Gata 5 Cio Dei^
attSbli
0. -3O-2004 yap,.
CONNINN A43~41, IFLP
ENN:b".. V.~.. CP** TV
33t> f4
Oht,O2C05 Vasut ~co Bent." tocoemos.
lapna• • kro ta«
.%tft
09,83,038 Vanta
Fakta ~en
PON•00 pa.," a fl or«.
-7 124 ,,
0803,2000 5701
Intartile ClOka 01Cantitl Osa
50% OI V.>..pMArtdM
.13,37303
45020008 8703
Iroultnos CoOt Of CANON Obo
fl ax* Offic•
50% Ot EI BeNt NONOONettele
tital
ta.
0103/20:4 8702
00%0' Pv., Oom.g.n.,,
.17,6y70
of Conina
09113~ 8704
1~000 018•4 of ~I
Oroo
o• ?co. As
ro no
~00
OW43.20o8 4703
~nye
0~
of ~Ml
On»
5014 or 'GIN
N1.1MINCNIrs.
-1/03203
04,13/2008 8108
~na
0111c• olOosi 080
5014 oil Pawn OMN" ANCYMOONN,
-112å300
001372008 8707
0404
Centra100.4
50% d Peatta ~telne Odal(
95c,•80
le4~4
ot
0011311006 071:0
/ven» Exit.« 3713-858•72.38009
Accooni • 3713~72-38009
-5721800
09,102036 4724
~OM banes« 3727~332-8~
Accowq 8 372744633241035
'49}7414
011,13,2005 5720
~am
4.00884 3710659401-47039
Account • 371540tOta7002
4,61162
oGrarto00 4763
CØ
~4
4470 1153 •OCO 5213
*taum • 4170 11534000 5213
41.10542
cenemooe 8754
Co.omel Bank 4470 1153 4030 8414
AccOufit 04870 11534030 5458
```

---

### [EFTA00001218](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001218.pdf).pdf (DataSet1)

- Original size: 374,978 bytes | Current size: 370,713 bytes
- Original text: 48 chars | Current text: 41 chars
- Text delta: +7 chars

**Text EXPOSED in original (behind poor redaction):**

```
1011111IIIIIII
v\IIIIiiiiiiiiiii
```

**Text in current re-redacted version (replacement):**

```
V11IIIIIIIIIIIIII
miniii,
```

---

### [EFTA00001402](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001402.pdf).pdf (DataSet1)

- Original size: 425,787 bytes | Current size: 402,737 bytes
- Original text: 97 chars | Current text: 13 chars
- Text delta: +84 chars

**Text EXPOSED in original (behind poor redaction):**

```
\•'?‘:
-)1\ ,
-r-crittfit,k1.
r- -
p,',. • i"
4/%1 • \
1
zio
0 tS
-
Trtto
```

---

### [EFTA00001523](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001523.pdf).pdf (DataSet1)

- Original size: 372,561 bytes | Current size: 368,229 bytes
- Original text: 42 chars | Current text: 13 chars
- Text delta: +29 chars

**Text EXPOSED in original (behind poor redaction):**

```
r fl
Ent
rmwel
41011L-alf
```

---

### [EFTA00001931](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001931.pdf).pdf (DataSet1)

- Original size: 589,734 bytes | Current size: 585,628 bytes
- Original text: 133 chars | Current text: 160 chars
- Text delta: -27 chars

**Text EXPOSED in original (behind poor redaction):**

```
7iFfreli erslein
4-57 Illadooit ave IR
flew JorK, new yore
1002Z
ir)022.+684a
.....
zin ia nu,
tti3
"
1410
,
z
```

**Text in current re-redacted version (replacement):**

```
II' 1"1"11 TI"Il "1"1"1"1"111111"I 'I
ImIll1"1
'ZI,199+Z.Z.00
r77001
ittoh tun
4 ktion (tun
/14 24V u°51?
Zc 47
upisa3 OWE
≤900b va fit
```

---

### [EFTA00001932](https://www.justice.gov/epstein/files/DataSet%201/EFTA00001932.pdf).pdf (DataSet1)

- Original size: 573,379 bytes | Current size: 572,881 bytes
- Original text: 1,409 chars | Current text: 1,240 chars
- Text delta: +169 chars

**Text EXPOSED in original (behind poor redaction):**

```
ear e.i-freA;
1- i.O,,-_)c ot( hac.i. a wonderi-iti 110ii-
dali SeaSO11.
rec"'"L ille IL'*Illac
i
eild"- seal in . Zi was healthful, }}tarok.
iinsienreawnictueatrs v..,t11._ il,, , I, Jim. tii,er
ih, _ raw 4,
,,,,zrz.for gout help. Ok: adve;qures ic Me Vi,
i
,zen, vi
well atci I rcalitc a d  ikever!i 7 UZI
11A5 . 7 )
ISICMC15,
es Paint
cash, as Vegas, and ilewrI/Lxi co
ou verb
Cttristrrias • wet-dwell wait mil family. nl
..:. t haye ken as qtral as ii was for meralisli eitrgoiula
have all made This a tie-ar to renternber. 1T l sister hac
a wonclerFu.1 iime on, rite le.)  Vela and flew Mexico
trip, and also whcailatt flew }ter out to ilev.2 ,401-11 to
visa me far Me weettend. allowigq in-e lo 5rar  1) in
liour aparimeni ill, Illanitallan mad, nt14 lite so
5Pail it in, ari O1/aaviii,
daN 7-
r
1 fauch easier and le,s stressful. rt was 1,eru nice
1-0 }tavernI own, space where t coul,4 he v iet and
draw withicati ialkini io an/one //or worrlirts abc.1
inirOitij on farni 4 or Ater Friends. Z1 wa5 a15.
very hind. of low io help mil friend aielbancita,
Seem v9 morher in ,W,
help
wonderful, 2- have nol
iotien lo spend a. considerable amount or time
with. her 5e/lee z moved out ittztvover;
h me 1O bc
Ike 171O51
I wonderful llanq you havc done /5 pus
Oliank
4.,
b
llil rhilik. about mj lik
esi and rea
1
for ever Vaal low have don, vor me.
```

**Text in current re-redacted version (replacement):**

```
ear c.ff-reA;
l lel
I. hope
had a 1VO111/4:',.L i 1 ..Lt r1.01/-
dail season.
seni Me Zi was beauliful 111(:
-
you vent rtuca. Christmas wen{ 'well will'
&Mil 711
zi, Arizona will' our da,N.
pertor7.:
RS-kr and
5pera
•,, a •
on
wars will lite circus in- ta. evertiiitinq 'has
bee&
well anal.
reali !-.. 11241 the va4,_
woui
toi have icon as qmai as
was co me' 1:15cLor ett
been. for your heii.
acive.-ziurcsr
It°
r5lands, Ve51. Palnz
each, izts Vci as, and. new.
,
hove all made.
a car to rentember. 1111 5i stet had
a wonderful
ore rhe ,k15 Vela and flew nicxic,'
14 on flew her 0111-
trip. and also when
vt;il me for the week-encl. allowinqine 10 ay
our
d
aparime
Nankoilan mod,: my life so
much ebtsicr and leas Simssful 11 was -Very nice
lo have m 0107L space tritcpc Z could
$uiet and
draw wilt la lalking to anlone nor wortiyirq a boui
jar dingy on Farah' or oilier friends.
vet hind of you to' help my friend
ve nal
Seeing
'was' wonderful,
jo 5 n
considerable amount or tem,-
with lter 5L CC r 711C".'ed ouL RiZt1VVCI; l[iC MC51'
wonderful flanq you. have
i flush
jo be  az
besi and reallv lhink abo I rt3
for ever lhi al you_ /taw cionAn tar Me.
...••
•••••/.1.
■
```

---

### [EFTA00003632](https://www.justice.gov/epstein/files/DataSet%202/EFTA00003632.pdf).pdf (DataSet2)

- Original size: 1,265,728 bytes | Current size: 1,276,766 bytes
- Original text: 110 chars | Current text: 179 chars
- Text delta: -69 chars

**Text EXPOSED in original (behind poor redaction):**

```
;
ye gm; as .
j foam
?Mons N
VitID Main,
4 400
S I N
Va
tZ9
M 3 SI
.1 V I S (7. 1
```

**Text in current re-redacted version (replacement):**

```
0 ,
1.4i.)STATF
INHEWb .44)
lot
NE
1.14 wai NES
1
1% luanthemol tursuisiga FIR AM,:
elSTATTONERV
• a
*
Si
•
Jr
•
,4
,
• . •
1 144%,.:
•
•
*
$
```

---

## 4. Documents with OCR Artifact Differences Only

These documents changed between versions, but the differences appear to be OCR noise
rather than meaningful redacted text. The redaction rectangles covered areas where
OCR produced garbled characters.

| Document | Dataset | Orig Size | Curr Size | Exposed Lines | Sample |
|----------|---------|-----------|-----------|---------------|--------|
| `EFTA00000160.pdf` | DataSet1 | 397,947 | 388,924 | 1 | `S1` |
| `EFTA00000167.pdf` | DataSet1 | 448,075 | 425,303 | 1 | `.4` |
| `EFTA00000177.pdf` | DataSet1 | 467,347 | 463,753 | 1 | `i!` |
| `EFTA00000229.pdf` | DataSet1 | 386,042 | 366,410 | 1 | `I` |
| `EFTA00000503.pdf` | DataSet1 | 324,162 | 322,628 | 1 | `_LISM[WIN-` |
| `EFTA00000531.pdf` | DataSet1 | 601,106 | 607,050 | 11 | `fib` |
| `EFTA00000746.pdf` | DataSet1 | 430,354 | 356,430 | 1 | `I` |
| `EFTA00001069.pdf` | DataSet1 | 381,556 | 369,339 | 1 | `i` |
| `EFTA00001124.pdf` | DataSet1 | 448,710 | 434,515 | 8 | `.` |
| `EFTA00001225.pdf` | DataSet1 | 379,180 | 370,641 | 5 | `ft` |
| `EFTA00001353.pdf` | DataSet1 | 424,286 | 425,409 | 1 | `kit` |
| `EFTA00001424.pdf` | DataSet1 | 539,183 | 529,085 | 1 | `.` |
| `EFTA00001524.pdf` | DataSet1 | 352,864 | 347,397 | 5 | `Pr .` |
| `EFTA00001528.pdf` | DataSet1 | 417,589 | 413,708 | 2 | `OP` |
| `EFTA00001590.pdf` | DataSet1 | 315,144 | 298,538 | 1 | `kil` |
| `EFTA00001596.pdf` | DataSet1 | 285,383 | 278,554 | 2 | `I` |
| `EFTA00002063.pdf` | DataSet1 | 411,834 | 409,018 | 2 | `t` |
| `EFTA00002064.pdf` | DataSet1 | 416,865 | 416,759 | 1 | `/` |

## 5. Documents with PDF Structure Changes Only

These documents have different file hashes but identical extracted text. The changes
are at the PDF binary level -- the redaction method was changed from overlay rectangles
to actual content removal, and/or the PDF was re-generated with updated timestamps.

| Document | Dataset | Orig Size | Curr Size | Size Delta |
|----------|---------|-----------|-----------|------------|
| `EFTA00000164.pdf` | DataSet1 | 456,164 | 447,851 | -8,313 |
| `EFTA00000165.pdf` | DataSet1 | 477,022 | 465,817 | -11,205 |
| `EFTA00000214.pdf` | DataSet1 | 480,678 | 473,823 | -6,855 |
| `EFTA00000216.pdf` | DataSet1 | 430,564 | 421,038 | -9,526 |
| `EFTA00000384.pdf` | DataSet1 | 330,754 | 330,754 | +0 |
| `EFTA00000657.pdf` | DataSet1 | 494,909 | 473,055 | -21,854 |
| `EFTA00000822.pdf` | DataSet1 | 412,589 | 410,375 | -2,214 |
| `EFTA00000824.pdf` | DataSet1 | 467,294 | 464,209 | -3,085 |
| `EFTA00000827.pdf` | DataSet1 | 469,223 | 445,636 | -23,587 |
| `EFTA00001046.pdf` | DataSet1 | 399,347 | 399,854 | +507 |
| `EFTA00001051.pdf` | DataSet1 | 496,412 | 486,046 | -10,366 |
| `EFTA00001052.pdf` | DataSet1 | 471,645 | 467,194 | -4,451 |
| `EFTA00001053.pdf` | DataSet1 | 490,646 | 469,570 | -21,076 |
| `EFTA00001055.pdf` | DataSet1 | 503,998 | 500,469 | -3,529 |
| `EFTA00001056.pdf` | DataSet1 | 509,007 | 472,829 | -36,178 |
| `EFTA00001103.pdf` | DataSet1 | 394,070 | 375,087 | -18,983 |
| `EFTA00001107.pdf` | DataSet1 | 414,121 | 387,549 | -26,572 |
| `EFTA00001110.pdf` | DataSet1 | 395,165 | 369,740 | -25,425 |
| `EFTA00001213.pdf` | DataSet1 | 367,389 | 359,774 | -7,615 |
| `EFTA00001217.pdf` | DataSet1 | 382,292 | 378,384 | -3,908 |
| `EFTA00001244.pdf` | DataSet1 | 402,880 | 397,247 | -5,633 |
| `EFTA00001375.pdf` | DataSet1 | 414,763 | 405,082 | -9,681 |
| `EFTA00001417.pdf` | DataSet1 | 406,233 | 399,361 | -6,872 |
| `EFTA00001421.pdf` | DataSet1 | 442,249 | 447,701 | +5,452 |
| `EFTA00001423.pdf` | DataSet1 | 489,677 | 475,306 | -14,371 |
| `EFTA00001533.pdf` | DataSet1 | 286,787 | 254,491 | -32,296 |

Note: [EFTA00000384](https://www.justice.gov/epstein/files/DataSet%201/EFTA00000384.pdf) has identical file sizes but differs only in creation/modification
date metadata (original: 2025-12-18, current: 2026-01-06), confirming the re-processing date.

## 6. Documents with Current-Only Text Changes

These documents have text present in the current version that is not in the original.
This typically indicates the re-processing added metadata or adjusted rendering.

| Document | Dataset | Orig Size | Curr Size | Lines Added |
|----------|---------|-----------|-----------|-------------|
| `EFTA00000172.pdf` | DataSet1 | 597,542 | 596,697 | 1 |
| `EFTA00000215.pdf` | DataSet1 | 423,098 | 418,296 | 5 |
| `EFTA00000656.pdf` | DataSet1 | 555,270 | 546,552 | 1 |
| `EFTA00000888.pdf` | DataSet1 | 453,159 | 448,821 | 1 |
| `EFTA00001532.pdf` | DataSet1 | 298,566 | 292,104 | 1 |
| `EFTA00001589.pdf` | DataSet1 | 192,243 | 182,610 | 1 |
| `EFTA00001591.pdf` | DataSet1 | 284,258 | 271,356 | 1 |

## 7. DataSets 3-8: Were They Affected?

DataSets 3 through 8 were released after December 19, 2025, and were NOT part of
the initial flawed release. We verified this by comparing archive.org captures
(dated December 22-24, 2025) of complete-PDF compilations to the current individual PDFs.

| Dataset | Archive.org Pages | Current PDFs | Archive Text | Current Text | Diff | Status |
|---------|-------------------|-------------|-------------|-------------|------|--------|
| DS3 | 1,847 | 67 | 275,994 | 275,943 | +51 | No issue |
| DS4 | 2,704 | 152 | 3,365,605 | 3,364,909 | +696 | No issue |
| DS5 | 120 | 120 | 45,480 | 46,862 | -1,382 | No issue |
| DS6 | 487 | 13 | 491,386 | 491,355 | +31 | No issue |
| DS7 | 660 | 17 | 720,756 | 720,756 | +0 | No issue |
| DS8 | 29,349 | 10,594 | N/A* | N/A* | N/A | No issue |

*DS8 text comparison skipped due to extremely large size (1.9GB PDF / 4.2GB ZIP).
The near-zero text differences in DS3-7 confirm these datasets were not affected by
the redaction failure. The minor character-level differences are attributable to PDF
rendering differences between the single-file compilation and individual PDFs.

## 8. Archive.org Verification

The archive.org COMPLETE PDF files (captured December 22, 2025) match the original
poorly-redacted versions. This confirms they were captured before the DOJ re-released
the corrected versions.

- **DataSet 1 COMPLETE.pdf**: 1,324,476,439 bytes, 3158 pages, MD5: `ecfa5fa09c0a6e9fe69e8700c334f165`
- **DataSet 2 COMPLETE.pdf**: 660,081,849 bytes, 699 pages, MD5: `1d48359faa7ae58c530b6e15df3451d6`

The archive.org DS1 COMPLETE PDF contains identical text to the original extracted
individual PDFs (verified by comparing text from changed documents - 100% match).

## 9. Complete List of All Affected Documents

| # | Dataset | Filename | Category | Orig Size | Curr Size | Size Delta | Text Exposed |
|---|---------|----------|----------|-----------|-----------|------------|-------------|
| 1 | DataSet1 | `EFTA00000160.pdf` | OCR artifacts | 397,947 | 388,924 | +9,023 | 1 lines |
| 2 | DataSet1 | `EFTA00000164.pdf` | Structure only | 456,164 | 447,851 | +8,313 | 0 lines |
| 3 | DataSet1 | `EFTA00000165.pdf` | Structure only | 477,022 | 465,817 | +11,205 | 0 lines |
| 4 | DataSet1 | `EFTA00000167.pdf` | OCR artifacts | 448,075 | 425,303 | +22,772 | 1 lines |
| 5 | DataSet1 | `EFTA00000172.pdf` | Current-only | 597,542 | 596,697 | +845 | 0 lines |
| 6 | DataSet1 | `EFTA00000177.pdf` | OCR artifacts | 467,347 | 463,753 | +3,594 | 1 lines |
| 7 | DataSet1 | `EFTA00000214.pdf` | Structure only | 480,678 | 473,823 | +6,855 | 0 lines |
| 8 | DataSet1 | `EFTA00000215.pdf` | Current-only | 423,098 | 418,296 | +4,802 | 0 lines |
| 9 | DataSet1 | `EFTA00000216.pdf` | Structure only | 430,564 | 421,038 | +9,526 | 0 lines |
| 10 | DataSet1 | `EFTA00000229.pdf` | OCR artifacts | 386,042 | 366,410 | +19,632 | 1 lines |
| 11 | DataSet1 | `EFTA00000384.pdf` | Structure only | 330,754 | 330,754 | +0 | 0 lines |
| 12 | DataSet1 | `EFTA00000470.pdf` | Text exposed | 433,324 | 429,003 | +4,321 | 13 lines |
| 13 | DataSet1 | `EFTA00000476.pdf` | Text exposed | 365,781 | 362,263 | +3,518 | 213 lines |
| 14 | DataSet1 | `EFTA00000503.pdf` | OCR artifacts | 324,162 | 322,628 | +1,534 | 1 lines |
| 15 | DataSet1 | `EFTA00000531.pdf` | OCR artifacts | 601,106 | 607,050 | -5,944 | 11 lines |
| 16 | DataSet1 | `EFTA00000656.pdf` | Current-only | 555,270 | 546,552 | +8,718 | 0 lines |
| 17 | DataSet1 | `EFTA00000657.pdf` | Structure only | 494,909 | 473,055 | +21,854 | 0 lines |
| 18 | DataSet1 | `EFTA00000746.pdf` | OCR artifacts | 430,354 | 356,430 | +73,924 | 1 lines |
| 19 | DataSet1 | `EFTA00000822.pdf` | Structure only | 412,589 | 410,375 | +2,214 | 0 lines |
| 20 | DataSet1 | `EFTA00000824.pdf` | Structure only | 467,294 | 464,209 | +3,085 | 0 lines |
| 21 | DataSet1 | `EFTA00000827.pdf` | Structure only | 469,223 | 445,636 | +23,587 | 0 lines |
| 22 | DataSet1 | `EFTA00000888.pdf` | Current-only | 453,159 | 448,821 | +4,338 | 0 lines |
| 23 | DataSet1 | `EFTA00001046.pdf` | Structure only | 399,347 | 399,854 | -507 | 0 lines |
| 24 | DataSet1 | `EFTA00001051.pdf` | Structure only | 496,412 | 486,046 | +10,366 | 0 lines |
| 25 | DataSet1 | `EFTA00001052.pdf` | Structure only | 471,645 | 467,194 | +4,451 | 0 lines |
| 26 | DataSet1 | `EFTA00001053.pdf` | Structure only | 490,646 | 469,570 | +21,076 | 0 lines |
| 27 | DataSet1 | `EFTA00001055.pdf` | Structure only | 503,998 | 500,469 | +3,529 | 0 lines |
| 28 | DataSet1 | `EFTA00001056.pdf` | Structure only | 509,007 | 472,829 | +36,178 | 0 lines |
| 29 | DataSet1 | `EFTA00001069.pdf` | OCR artifacts | 381,556 | 369,339 | +12,217 | 1 lines |
| 30 | DataSet1 | `EFTA00001103.pdf` | Structure only | 394,070 | 375,087 | +18,983 | 0 lines |
| 31 | DataSet1 | `EFTA00001107.pdf` | Structure only | 414,121 | 387,549 | +26,572 | 0 lines |
| 32 | DataSet1 | `EFTA00001110.pdf` | Structure only | 395,165 | 369,740 | +25,425 | 0 lines |
| 33 | DataSet1 | `EFTA00001124.pdf` | OCR artifacts | 448,710 | 434,515 | +14,195 | 8 lines |
| 34 | DataSet1 | `EFTA00001213.pdf` | Structure only | 367,389 | 359,774 | +7,615 | 0 lines |
| 35 | DataSet1 | `EFTA00001217.pdf` | Structure only | 382,292 | 378,384 | +3,908 | 0 lines |
| 36 | DataSet1 | `EFTA00001218.pdf` | Text exposed | 374,978 | 370,713 | +4,265 | 2 lines |
| 37 | DataSet1 | `EFTA00001225.pdf` | OCR artifacts | 379,180 | 370,641 | +8,539 | 5 lines |
| 38 | DataSet1 | `EFTA00001244.pdf` | Structure only | 402,880 | 397,247 | +5,633 | 0 lines |
| 39 | DataSet1 | `EFTA00001353.pdf` | OCR artifacts | 424,286 | 425,409 | -1,123 | 1 lines |
| 40 | DataSet1 | `EFTA00001375.pdf` | Structure only | 414,763 | 405,082 | +9,681 | 0 lines |
| 41 | DataSet1 | `EFTA00001402.pdf` | Text exposed | 425,787 | 402,737 | +23,050 | 11 lines |
| 42 | DataSet1 | `EFTA00001417.pdf` | Structure only | 406,233 | 399,361 | +6,872 | 0 lines |
| 43 | DataSet1 | `EFTA00001421.pdf` | Structure only | 442,249 | 447,701 | -5,452 | 0 lines |
| 44 | DataSet1 | `EFTA00001423.pdf` | Structure only | 489,677 | 475,306 | +14,371 | 0 lines |
| 45 | DataSet1 | `EFTA00001424.pdf` | OCR artifacts | 539,183 | 529,085 | +10,098 | 1 lines |
| 46 | DataSet1 | `EFTA00001523.pdf` | Text exposed | 372,561 | 368,229 | +4,332 | 4 lines |
| 47 | DataSet1 | `EFTA00001524.pdf` | OCR artifacts | 352,864 | 347,397 | +5,467 | 5 lines |
| 48 | DataSet1 | `EFTA00001528.pdf` | OCR artifacts | 417,589 | 413,708 | +3,881 | 2 lines |
| 49 | DataSet1 | `EFTA00001532.pdf` | Current-only | 298,566 | 292,104 | +6,462 | 0 lines |
| 50 | DataSet1 | `EFTA00001533.pdf` | Structure only | 286,787 | 254,491 | +32,296 | 0 lines |
| 51 | DataSet1 | `EFTA00001589.pdf` | Current-only | 192,243 | 182,610 | +9,633 | 0 lines |
| 52 | DataSet1 | `EFTA00001590.pdf` | OCR artifacts | 315,144 | 298,538 | +16,606 | 1 lines |
| 53 | DataSet1 | `EFTA00001591.pdf` | Current-only | 284,258 | 271,356 | +12,902 | 0 lines |
| 54 | DataSet1 | `EFTA00001596.pdf` | OCR artifacts | 285,383 | 278,554 | +6,829 | 2 lines |
| 55 | DataSet1 | `EFTA00001931.pdf` | Text exposed | 589,734 | 585,628 | +4,106 | 12 lines |
| 56 | DataSet1 | `EFTA00001932.pdf` | Text exposed | 573,379 | 572,881 | +498 | 47 lines |
| 57 | DataSet1 | `EFTA00002063.pdf` | OCR artifacts | 411,834 | 409,018 | +2,816 | 2 lines |
| 58 | DataSet1 | `EFTA00002064.pdf` | OCR artifacts | 416,865 | 416,759 | +106 | 1 lines |
| 59 | DataSet2 | `EFTA00003632.pdf` | Text exposed | 1,265,728 | 1,276,766 | -11,038 | 11 lines |

**Additionally removed (not in above table):**
- `EFTA00000467.pdf` - Present in original DataSet 1, absent in re-release
- `EFTA00000468.pdf` - Present in original DataSet 1, absent in re-release

## 10. Methodology

1. Extracted the original Dec 19, 2025 ZIP files for DataSets 1 and 2
2. Compared each PDF by MD5 hash to identify changed files
3. For changed PDFs, extracted text using PDF analysis tools from both versions
4. Generated unified diffs to identify text present in originals but absent in re-release
5. Categorized differences as meaningful text, OCR artifacts, or structure-only changes
6. For DS3-8, compared archive.org Dec 22-24 captures to current versions by total text length
7. Verified archive.org DS1 COMPLETE.pdf matches original extracted PDFs

### Sources

- **Original Dec 19 release**: `DataSet1_ORIGINAL_Dec19_2025.zip` (1,322,628,898 bytes)
  and `DataSet2_ORIGINAL_Dec19_2025.zip` (661,420,596 bytes)
- **Current re-release**: `DataSet1.zip` (1,321,480,300 bytes)
  and `DataSet2.zip` (661,431,549 bytes)
- **Archive.org captures**: `DataSet_{1-8}_COMPLETE.pdf` (Dec 22-24, 2025)

### Tools

- PDF analysis tools v1.24.14 for PDF text extraction
- MD5 hashing for file comparison
- Python difflib for text differencing

---

*Report generated: 2026-02-05*
*Structured data: `dec2025_redaction_diffs.jsonl` (59 records)*
