# Hidden Text in Court Documents: A Simple Guide

*How to recover redacted information from Jeffrey Epstein court filings*

**Updated:** April 23, 2026  
**For:** Journalists, researchers, and the general public

---

## What We Found

**Thousands of court documents in Epstein-related cases contain hidden text that anyone can recover with simple copy and paste.**

The U.S. Department of Justice published court filings online with faulty "redactions" — black bars that were supposed to hide sensitive information. **The text is still there underneath, and you can see it by copying the blacked-out sections and pasting them elsewhere.**

### Real Example

Here's what we recovered from a major lawsuit document that was supposed to be redacted:

> "signed Foundation account checks for over $400,000 made payable to young female models and actresses, including a former Russian model who received over $380,000 through monthly payments of $8,333"

That text was completely blacked out in the PDF viewer, but copying and pasting revealed the hidden details.

---

## How This Happened

### The Problem

When creating a PDF redaction, there are two ways to do it:

**❌ Wrong Way (What DOJ Did Initially):**
- Type the document normally
- Draw black rectangles on top of sensitive text
- **Result:** Text is hidden visually but still exists in the file

**✅ Right Way (What DOJ Does Now):**
- Print the document to an image (like taking a photo)
- Run text recognition software on the image
- **Result:** Hidden text is completely destroyed

### The Timeline

- **December 2025:** DOJ published thousands of court documents with faulty redactions
- **February 2026:** Someone (possibly journalists) discovered the problem  
- **February 25, 2026:** DOJ quietly replaced all files with properly redacted versions
- **Today:** Original files are only available through Internet Archive backups

---

## What Documents Are Affected

We've identified **over 12,000 court filing PDFs** with this problem across major Epstein cases:

| Court Case | # of Files | What It's About |
|------------|------------|-----------------|
| **Virginia Giuffre vs. Ghislaine Maxwell** | 2,978 | Settlement documents, depositions |
| **U.S. Virgin Islands vs. JPMorgan** | 1,840 | Bank's role in Epstein operations |
| **United States vs. Maxwell** | 1,318 | Criminal trial records |
| **Multiple Victim Lawsuits** | 6,000+ | Individual civil cases |

### Most Revealing Documents

Across our analyzed catalog of 7 cases (56 documents, 280 pages with redaction bars):

- **719 recoverable text fragments** confirmed after cross-validation
- **Content includes:** Financial transactions, entity names, operational details, payment amounts, privilege-log email addresses, deposition names

### How we checked our work

Every finding was cross-validated using two independent methods:

1. **Pixel-darkness detection** — our main tool, which renders each page as a high-resolution image and looks for words whose position is covered by a dark rectangle.
2. **PDF structural detection** — an independent open-source tool (Lee Drake's `unredact`) that inspects the raw PDF drawing commands to find filled black rectangles.

The two methods agree on the core findings but catch different failure modes: the pixel method catches redactions burned into scanned-document images (which the structural tool cannot see), and the structural tool catches narrow inline bars thinner than a whole word (which the pixel method occasionally misses). When the two disagreed, we visually inspected the pages — which caught one incorrect rejection (restored) and confirmed the 21 entries we dropped as non-evidentiary (PACER headers on fully-sealed pages, FOIA exemption labels, literal "xxxx" placeholders).

---

## How to Access These Documents

### Step 1: Find the Original Files

The current DOJ website has fixed versions. You need the **Internet Archive (Wayback Machine)** versions from before the fix:

**Go to:** `web.archive.org`

**Search for:** `justice.gov/multimedia/Court Records/[CASE NAME]/`

**Use dates:** December 2025 through February 2026

### Step 2: Download Specific Documents

**Example URL pattern:**
```
https://web.archive.org/web/20251228132625/https://www.justice.gov/multimedia/Court%20Records/Government%20of%20the%20United%20States%20Virgin%20Islands%20v.%20JPMorgan%20Chase%20Bank,%20N.A.,%20No.%20122-cv-10904%20(S.D.N.Y.%202022)/001-01.pdf
```

Replace the case name and document number with what you're looking for.

### Step 3: Test for Hidden Text

1. **Open the PDF** in any viewer
2. **Find sections with black bars** (redactions)
3. **Click and drag** to select the black area
4. **Copy** (Ctrl+C or Cmd+C)
5. **Paste** into a text editor (Ctrl+V or Cmd+V)

If you see text appear, the redaction was faulty!

---

## What Kind of Information is Hidden

### Financial Details
- Specific payment amounts to individuals
- Bank transfer details
- Entity ownership structures
- Loan arrangements

### Operational Information  
- Names of previously unknown entities
- Business relationships
- Property transactions
- Legal strategies

### Investigation Details
- Evidence handling procedures
- Witness information (redacted for privacy)
- Law enforcement communications

**Important:** We focus on systemic patterns and public interest information, not individual privacy details.

---

## Tools for Researchers

For those wanting to do systematic analysis:

### Simple Method (No Technical Skills)
1. **Manual copy/paste testing** on individual documents
2. **Search for key terms** like entity names, dollar amounts
3. **Document findings** in spreadsheets or notes

### Advanced Method (Some Technical Skills)
We've created tools that automatically:
- **Scan hundreds of PDFs** to identify which have faulty redactions
- **Extract all hidden text** from documents
- **Compare** original vs. fixed versions

**Tools available at:** Contact researchers or check public repositories

---

## Legal and Ethical Notes

### This is Legal Research
- These are **public court documents**
- The **vulnerability was created by the government agency**
- We're using **standard document analysis techniques**
- **Responsible disclosure** focuses on systematic transparency, not individual privacy

### Responsible Use
- **Protect victim privacy** — don't republish personal details
- **Focus on institutional accountability** — banks, law enforcement, estate management
- **Verify information** against other sources when possible
- **Consider public interest** vs. individual harm

---

## Why This Matters

### Government Transparency
This reveals significant problems with:
- **Document security practices** in federal agencies
- **Transparency vs. secrecy** in high-profile legal cases  
- **Technical competency** in handling sensitive information

### Historical Record
The hidden information provides unprecedented detail about:
- **Financial networks** supporting Epstein's operations
- **Institutional relationships** with banks and service providers
- **Investigation and prosecution strategies**

### Accountability
Recovered information may reveal:
- **Previously unknown entities** and relationships
- **Financial flows** that weren't disclosed in testimony
- **Coordination between defendants** and service providers

---

## Getting Started

### For Journalists
1. **Start with high-priority cases** (Giuffre v. Maxwell, USVI v. JPMorgan)
2. **Focus on financial documents** (highest recovery rates)
3. **Cross-reference** with existing reporting for context
4. **Verify findings** through multiple sources

### For Researchers  
1. **Download our case inventory** to prioritize targets
2. **Use systematic scanning** rather than random sampling
3. **Document methodology** for peer review
4. **Share findings** through established research channels

### For General Public
1. **Start with our verified examples** to understand the technique
2. **Pick specific topics** you're interested in (finances, real estate, etc.)
3. **Work in groups** to cover more documents efficiently  
4. **Report significant findings** to journalists or researchers

---

## Frequently Asked Questions

**Q: Is this hacking or illegal?**  
A: No. These are public court documents. We're using standard copy/paste functionality that works in any PDF viewer.

**Q: Why didn't DOJ fix this earlier?**  
A: PDF redaction is technically complex. Many organizations make this mistake. DOJ fixed it once discovered, but the originals are preserved by Internet Archive.

**Q: How much hidden text is there?**  
A: From our sample, about 50-60% of court filings have some recoverable text. Some documents have hundreds of hidden words.

**Q: How do you know the recoveries are real and not software bugs?**  
A: We verified every entry with two independent methods (pixel-darkness rendering and PDF-structure inspection using an open-source tool built by a separate researcher), and visually spot-checked pages where the two methods disagreed. The 21 entries our first pass flagged but couldn't substantiate were dropped from the published catalog.

**Q: Can I get in trouble for doing this?**  
A: These are public records with a technical flaw. Standard document research is protected activity. Use common sense about republishing sensitive personal information.

**Q: Are other cases affected?**  
A: We've focused on Epstein-related cases, but the same technical issue likely affected other DOJ multimedia archives during the same time period.

---

## Contact

For questions about methodology, tool access, or collaboration:
- **Technical questions:** See detailed technical report
- **Media inquiries:** Standard research disclosure practices
- **Academic collaboration:** Documented methodology available for peer review

---

*This guide demonstrates standard document analysis techniques for transparency research. All methods described use publicly available court records and standard software functionality.*