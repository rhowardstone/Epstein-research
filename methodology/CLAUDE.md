# Epstein Files — Investigation Reports

## What This Is

165+ forensic analysis reports examining the DOJ's 2.91 million page Epstein case file release (January 30, 2026). Every claim in these reports cites specific EFTA document numbers that can be verified against the original PDFs on justice.gov.

These reports are the analysis layer. The underlying data — searchable databases of all 2.91 million pages — lives in the companion repo: [rhowardstone/Epstein-research-data](https://github.com/rhowardstone/Epstein-research-data).

---

## First Session Bootstrap

If this is your first time working with these files:

1. **Read [METHODOLOGY.md](METHODOLOGY.md) and [WRITING_GUIDE.md](WRITING_GUIDE.md).** These contain the investigation pipeline, fact-checking rules, and writing standards. Memorize the key points.
2. **Note the absolute paths** to both this repo and the companion data repo in your memories.
3. **Verify database setup** by running the verification query in the data repo's CLAUDE.md.
4. **Store a directory structure index** in your memories so you can navigate reports without re-scanning.

These auxiliary files are kept separate from CLAUDE.md to save context window tokens. Read them once, internalize the rules, and refer back when needed.

---

## Directory Map

### `overview/` — Start here (10 reports)
Executive summaries and master findings.
- **`FINAL_INVESTIGATION_REPORT.md`** — Comprehensive findings across all investigation lines
- **`PHASE4_BRIEFING_KIT.md`** — Condensed briefing with key evidence chains
- **`SESSION9_MASTER_FINDINGS.md`** — Latest session consolidated findings

### `congressional/` — Congressional briefings (8 reports)
Materials prepared for congressional oversight.
- **`CONGRESSIONAL_SUBPOENA_GUIDE.md`** — 64 witnesses, 490 verified EFTA URLs, recommended subpoena targets
- **`WITNESS_BRIEF_INDYKE.md`** / **`WITNESS_BRIEF_KAHN.md`** — Deep-dive witness preparation briefs

### `financial/` — Follow the money (20 reports)
Shell entities, wire transfers, Deutsche Bank compliance failures, art market laundering.
- **`SHELL_ENTITY_MAP.md`** — Complete map of Epstein's corporate structure
- **`FORENSIC_ACCT_*.md`** (6 parts) — Forensic accounting series: trust drawdowns, money sources, inter-entity flows
- **`CRYPTO_NETWORK_INVESTIGATION.md`** — Cryptocurrency and financial network analysis

### `individuals/` — Named person investigations (28 reports)
Deep dives on specific people appearing in the files.
- **`BILL_CLINTON_INVESTIGATION.md`** / **`DONALD_TRUMP_INVESTIGATION.md`** — Political figures
- **`INVESTIGATION_6_LEON_BLACK.md`** / **`LEON_BLACK_PROSECUTION_FAILURE.md`** — Apollo Global
- **`WILLIAM_BARR_INVESTIGATION.md`** — AG recusal and NTOC tip handling
- **`PSEUDONYM_CODENAME_REGISTRY.md`** — 273 pseudonyms/codenames found in the corpus

### `institutional/` — System failures (19 reports)
How institutions enabled or failed to stop the operation.
- **`DOJ_DOCUMENT_ALTERATION_FORENSICS.md`** — 212,730 changes detected between original and current DOJ-hosted documents
- **`DOJ_DOCUMENT_REMOVAL_AUDIT.md`** — ~64,259 documents removed from justice.gov after initial release
- **`FBI_302_MISSING_SERIALS_DOSSIER.md`** — FBI interview records that should exist but are missing from production
- **`SECONDARY_BATES_STAMP_ANALYSIS.md`** — Hidden numbering systems revealing production manipulation
- **`DS12_EXPANSION_ANALYSIS.md`** — 23 new documents quietly added March 2026

### `evidence/` — Device and physical forensics (13 reports)
Computer forensics, phone records, PLIST analysis, blackout periods.
- **`DEVICE_FORENSICS_COMPLETE.md`** — All seized electronic devices
- **`PHONE_RECORDS_INVESTIGATION.md`** — Call records analysis
- **`BLACKOUT_PERIOD_INVESTIGATION.md`** — Gaps in the evidentiary timeline

### `pqg_lines_of_investigation/` — Prosecutorial gaps (11 reports)
What the grand jury subpoenas demanded vs. what was actually produced.
- **`00_INDEX.md`** — Start here: overview of all 10 investigation lines
- Topics: temporal blackouts, redacted targets, tech company gaps, travel records, Deutsche Bank, financial no-returns, crypto dead ends, MCC death investigation

### `intelligence/` — Intelligence connections (4 reports)
- **`FBI_INTELLIGENCE_INVESTIGATIONS.md`** — FBI's intelligence-side investigations
- **`ISRAEL_DEEP_DIVE_V2.md`** — Israeli intelligence connections

### `government-officials/` — Branch-by-branch analysis (7 reports)
Organized by party and branch: executive, judicial, legislative (Democrat/Republican/Independent).

### `victims/` — Victim analysis (4 reports)
Trafficking routes, victim census, interview analysis. **All victim-identifying information is redacted.**

### `methodology/` — Data quality and methods (12 reports)
Redaction analysis, data quality audits, evidence reliability assessments, corpus inventory.

### Other directories
| Directory | Reports | Focus |
|-----------|---------|-------|
| `art/` | 4 | Art market investigation |
| `scientists/` | 3 | Science network, David Shaw, biotech connections |
| `social-networks/` | 6 | Geffen, Kotick, Peggy Siegal, Reuben Brothers |
| `raw-dataset-analysis/` | 11 | Per-dataset deep dives (DS8, DS10) |
| `internet-theories/` | 3 | Corpus searches testing internet claims (pizzagate, occult, misc) |
| `recovered_corrupted_pdfs/` | 1 | Recovered data from corrupted PDFs in the DOJ release |

---

## How to Search

### Find reports mentioning a person or topic

```bash
grep -rl "Leon Black" --include="*.md" .
```

### Search with context

```bash
grep -rn "EFTA00074206" --include="*.md" -C 2 .
```

### Find reports about a specific EFTA document

```bash
grep -rl "EFTA01688067" --include="*.md" .
```

---

## Accessing Original PDFs

Every EFTA number cited in these reports can be opened as a PDF. The DOJ is the canonical source (requires age gate); two independent mirrors serve byte-identical raw PDFs with no gate.

| Source | URL Template | Notes |
|--------|-------------|-------|
| **DOJ** | `justice.gov/epstein/files/DataSet%20{N}/EFTA{NUMBER}.pdf` | Canonical. Requires dataset number + age gate. |
| **RollCall** | `media-cdn.rollcall.com/epstein-files/EFTA{NUMBER}.pdf` | Raw PDF, no gate, no dataset needed. Full coverage. |
| **Kino/JDrive** | `assets.getkino.com/documents/EFTA{NUMBER}.pdf` | Raw PDF, no gate. DS1-7 + DS9-11. Missing DS12. |
| **Kino/JDrive (DS8)** | `assets.getkino.com/documents/vol00008-official-doj-latest-efta{number}.pdf` | DS8 uses different naming. Note **lowercase** `efta`. |
| **JMail Viewer** | `jmail.world/drive/EFTA{NUMBER}.pdf` (or `vol00008-...` for DS8) | Formatted viewer. Uses Kino CDN. |

To find the correct dataset number for DOJ URLs, use the companion data repo's database:

```sql
sqlite3 full_text_corpus.db "SELECT dataset FROM documents WHERE efta_number = 'EFTA00074206';"
```

Or use this boundary table:

| Dataset | EFTA Range |
|---------|-----------|
| 1 | 00000001 – 00003158 |
| 2 | 00003159 – 00003857 |
| 3 | 00003858 – 00005586 |
| 4 | 00005705 – 00008320 |
| 5 | 00008409 – 00008528 |
| 6 | 00008529 – 00008998 |
| 7 | 00009016 – 00009664 |
| 8 | 00009676 – 00039023 |
| 9 | 00039025 – 01262781 |
| 10 | 01262782 – 02205654 |
| 11 | 02205655 – 02730264 |
| 12 | 02730265 – 02858497 |

**Note:** Dataset boundaries have gaps — always verify via the database when possible.

---

## Critical Rules

1. **Never include real victim names or identifying details.** Use pseudonyms (Jane Doe, JD#1) or EFTA references only. The goal is exposing the system and the perpetrators, never retraumatizing or identifying victims.

2. **Corpus absence ≠ non-existence.** A document not appearing in the EFTA production may be under seal, filed in a different case, or outside the scope of the DOJ release. Do not assume non-compliance from a gap.

3. **Present data, not conclusions.** These reports document what the files contain. Readers draw their own inferences.

4. **Verify before citing.** Cross-check EFTA numbers against the actual documents before repeating claims.

---

## Companion Repository

The searchable databases behind these reports: [rhowardstone/Epstein-research-data](https://github.com/rhowardstone/Epstein-research-data) — 6.3 GB full-text corpus with FTS5 search, concordance metadata, redaction analysis, image descriptions, audio transcripts, and more. See that repo's CLAUDE.md for setup instructions and a SQL query cookbook.

---

## Updating

```bash
# Pull new reports and data files
git pull origin main
```

To check what's new on the remote **before** pulling:

```bash
git fetch origin main
git log HEAD..origin/main --oneline
```

Always fetch from the remote before reporting what's changed — your local checkout may be behind.

---

## Read-Only Distribution

These repositories are distributed read-only. If you cloned them to investigate locally:

- **Do not push, create branches, or submit pull requests.** Your copy is for local research only.
- **Pull updates** with `git pull origin main` to get new reports.
- **All your work stays local.** Write findings to your own files outside the repo, or in a gitignored directory.
