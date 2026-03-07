# How We Built epstein-data.com: A Methodology for AI-Assisted Public Records Analysis

*Rye Howard-Stone, February 2026*

---

## Abstract

In November 2025, the DOJ released 1.38 million documents (2.77 million pages) under the Epstein Files Transparency Act. The documents were published as individual PDFs on justice.gov with no search functionality. Within two weeks, one person using AI-assisted development built a full-text search engine, entity extraction pipeline, seven analytical databases, an AI research assistant, and a public website serving 3,000-5,000 daily active users. This document describes exactly how — every architectural decision, tool, and tradeoff — so that others can replicate the approach for any document corpus.

---

## Table of Contents

1. [The Problem](#the-problem)
2. [Architecture Overview](#architecture-overview)
3. [Phase 1: Text Extraction](#phase-1-text-extraction)
4. [Phase 2: The Database Schema That Makes It Work](#phase-2-the-database-schema)
5. [Phase 3: Entity Extraction and Knowledge Graph](#phase-3-entity-extraction)
6. [Phase 4: The Web Interface](#phase-4-the-web-interface)
7. [Phase 5: The AI Research Assistant (RAG)](#phase-5-ai-research-assistant)
8. [Phase 6: PII Redaction](#phase-6-pii-redaction)
9. [Phase 7: Forensic Auditing at Scale](#phase-7-forensic-auditing)
10. [Phase 8: Investigation Reports](#phase-8-investigation-reports)
11. [Phase 9: Deployment and Production](#phase-9-deployment)
12. [What AI Did vs. What Required Human Judgment](#what-ai-did)
13. [Replication Guide: The Minimum Viable Document Database](#replication-guide)
14. [Cost Breakdown](#cost-breakdown)
15. [Limitations and Lessons Learned](#limitations)

---

## The Problem

Government transparency laws are only as effective as the public's ability to access and analyze the released records. The Epstein Files Transparency Act was a bipartisan law requiring full document release. The DOJ complied — technically. They published 2.77 million pages as individual PDFs across 12 datasets, accessible only by EFTA number (a sequential Bates stamp like `EFTA00074206`). There was no search functionality, no index, no way to find all documents mentioning a specific person, entity, or financial transaction without manually opening PDFs one at a time.

This is a pattern. FOIA productions, congressional investigations, court document dumps — they all arrive as folders of PDFs. The producing agency has search tools; the public does not. The asymmetry is the problem.

This methodology describes how to eliminate that asymmetry for any document corpus.

---

## Architecture Overview

The complete system has nine layers. Not all are required — a useful searchable database can be built with just the first four. The layers are:

```
Layer 1: Text Extraction      PDF → per-page plain text
Layer 2: Database Schema       documents + pages + FTS5 full-text index
Layer 3: Entity Extraction     Named entities (people, orgs, dates, money)
Layer 4: Web Interface         Datasette + custom templates
Layer 5: AI Research Assistant  RAG system over FTS5 (natural language → citations)
Layer 6: PII Redaction         Victim privacy protection (3-tier pipeline)
Layer 7: Forensic Auditing     Automated verification of source availability
Layer 8: Investigation Reports  Markdown → HTML with auto-linkification
Layer 9: Production Deployment  nginx, Cloudflare, rate limiting, bot blocking
```

**Tech stack**: Python 3.10+, SQLite with FTS5, Datasette, PyMuPDF/Docling (OCR), spaCy (NER), Playwright (browser automation), OpenRouter (LLM API). Total infrastructure cost: $17.99/month.

**Source code**: All code is open source.
- Extraction pipeline: [github.com/rhowardstone/Epstein-Pipeline](https://github.com/rhowardstone/Epstein-Pipeline)
- Website and services: [github.com/rhowardstone/epstein-datasette](https://github.com/rhowardstone/epstein-datasette)
- Structured data: [github.com/rhowardstone/Epstein-research-data](https://github.com/rhowardstone/Epstein-research-data)

---

## Phase 1: Text Extraction

### The challenge

Government PDFs come in three flavors:
1. **Native digital** — text is selectable, extraction is trivial
2. **Scanned with OCR layer** — an invisible text layer sits behind the scanned image (rendering mode Tr=3 in PDF spec). The text is there but not visible.
3. **Scanned without OCR** — just images. Requires optical character recognition.

The EFTA production was primarily types 1 and 2, with some type 3 documents. The extraction pipeline needed to handle all three.

### Two-backend approach

We used two OCR/extraction backends and took the better result:

**PyMuPDF (fitz)** — A Python binding for MuPDF. Excellent at extracting invisible OCR text layers (type 2 documents). Fast, lightweight, handles most government PDFs well.

**Docling (IBM)** — A layout-aware document understanding model. Better at table extraction, multi-column layouts, and documents where PyMuPDF produces garbled output. Slower but more accurate for complex layouts.

The pipeline runs PyMuPDF first. If the extracted text is empty or below a character-count threshold, it falls back to Docling. This "both" mode catches documents that either backend alone would miss.

### Per-page extraction: the critical design decision

Most document processing tools extract text per-document — one blob of text per PDF. **We extract per-page.** This is the single most important architectural decision in the entire system.

Why it matters:
- A journalist searching for "Leon Black" needs to know it appears on **page 47** of a 200-page document, not just "somewhere in EFTA00193199"
- Citations become precise: "EFTA00074206, page 3" is verifiable; "EFTA00074206" is not
- The AI research assistant can cite specific pages
- Search results show the actual page text, not a document summary

The extraction pipeline produces one JSON record per document containing an array of page objects:

```json
{
  "id": "EFTA00074206",
  "title": "Southern Trust Company Bank Statements",
  "pages": [
    {"page_number": 1, "text": "SOUTHERN TRUST COMPANY...", "char_count": 2847},
    {"page_number": 2, "text": "Account Number: ****4291...", "char_count": 3102}
  ]
}
```

### Resumable processing

Processing 1.38 million PDFs takes days. The pipeline is fully resumable: each document is hashed (SHA-256 of the PDF content), and the processing state is tracked in a SQLite database (`.cache/pipeline_state.db`). If the pipeline crashes at document 500,000, it picks up at 500,001. This is implemented via a simple check: `state.is_processed(file_hash, "ocr")` before processing each file.

### Parallel execution

OCR is CPU-bound. The pipeline uses `ProcessPoolExecutor` with configurable workers (default 4, we ran 8-16 depending on the machine). Each worker processes one PDF independently. A Rich progress bar shows real-time throughput and ETA.

### OCR noise cleaning

Government PDFs produce noisy OCR output. The pipeline cleans:
- Control characters (`\x00-\x1f`)
- Repeated characters (10+ of the same char collapsed to 3)
- Decorative lines (`___`, `===`)
- Excessive whitespace (5+ spaces → 2, 3+ newlines → 2)

This cleaning happens before storage, not at query time, so search results are clean by default.

---

## Phase 2: The Database Schema

### The two-table core

The entire system is built on two tables in SQLite:

```sql
CREATE TABLE documents (
    id INTEGER PRIMARY KEY,
    efta_number TEXT UNIQUE,    -- Bates stamp (e.g., 'EFTA00074206')
    dataset TEXT,               -- Which production set (1-12)
    file_path TEXT,             -- Original filename
    total_pages INTEGER,
    char_count INTEGER          -- Total characters across all pages
);

CREATE TABLE pages (
    id INTEGER PRIMARY KEY,
    efta_number TEXT,           -- Foreign key to documents
    page_number INTEGER,
    text_content TEXT,          -- The actual page text
    char_count INTEGER
);
```

This is deliberately simple. The `documents` table holds metadata; the `pages` table holds text. They join on `efta_number`.

### FTS5: the search engine

SQLite's FTS5 extension turns the `pages` table into a full-text search engine:

```sql
CREATE VIRTUAL TABLE pages_fts USING fts5(
    text_content,
    content='pages',
    content_rowid='id'
);
```

FTS5 supports phrase queries (`"Leon Black"`), boolean operators (`black AND NOT leon`), prefix matching (`bank*`), and column filtering. It's fast — sub-second queries across 2.77 million pages.

The FTS5 index is kept in sync with the `pages` table via triggers:

```sql
CREATE TRIGGER pages_ai AFTER INSERT ON pages BEGIN
    INSERT INTO pages_fts(rowid, text_content) VALUES (new.id, new.text_content);
END;
```

### A typical search query

```sql
SELECT d.efta_number, d.dataset, p.page_number,
       substr(p.text_content, 1, 500) AS snippet
FROM pages_fts fts
JOIN pages p ON p.rowid = fts.rowid
JOIN documents d ON d.efta_number = p.efta_number
WHERE pages_fts MATCH '"Deutsche Bank" AND wire'
ORDER BY rank
LIMIT 50;
```

This returns the 50 most relevant pages mentioning "Deutsche Bank" and "wire" together, with the document's Bates stamp, dataset number, and page number. A journalist can then construct the DOJ source URL: `https://www.justice.gov/epstein/files/DataSet%20{N}/EFTA{NUMBER}.pdf`.

### Multiple analytical databases

The full-text corpus is the primary database, but we built six additional databases for specialized analysis:

| Database | Size | Purpose |
|----------|------|---------|
| `full_text_corpus.db` | 6.3 GB | Master text: 1.38M docs, 2.77M pages, FTS5 |
| `redaction_analysis_v2.db` | 1.0 GB | 2.6M redaction regions detected in PDFs |
| `image_analysis.db` | 407 MB | 21,859 extracted images with AI descriptions |
| `knowledge_graph.db` | 782 KB | 524 entities, 2,096 relationships |
| `transcripts.db` | 5 MB | 375 audio files transcribed (92K words) |
| `ocr_database.db` | 71 MB | Tesseract OCR results (alternative to PyMuPDF) |
| `spreadsheet_corpus.db` | 4 MB | Native spreadsheet data (Excel/CSV files) |

Each database is served independently by Datasette, giving users seven different analytical lenses into the same corpus. A journalist researching visual evidence searches `image_analysis`; someone interested in redaction patterns searches `redaction_analysis_v2`.

### Why SQLite, not Postgres/Elasticsearch

SQLite is:
- **Zero-configuration**: No server process, no connection strings, no authentication
- **Portable**: The entire 6.3 GB database is a single file you can `scp` to any server
- **FTS5-native**: Full-text search is built in, not an add-on
- **Datasette-compatible**: Datasette turns any SQLite database into a web API with zero code

For a single-server deployment serving thousands of daily users, SQLite with WAL mode handles the read load easily. Write contention isn't an issue because the database is effectively read-only after ingestion.

---

## Phase 3: Entity Extraction

### Two-pass NER

Named entity recognition extracts people, organizations, locations, dates, and monetary amounts from document text. We use a two-pass approach:

**Pass 1: spaCy NER** — The `en_core_web_sm` model processes each page's text and extracts PERSON entities. Each extracted name is matched against a person registry (1,538 known persons with aliases) using:
1. Exact match (O(1) dictionary lookup after lowercasing)
2. Fuzzy match (rapidfuzz `token_sort_ratio`, threshold 85) for OCR-mangled names

**Pass 2: Direct scan** — Iterate the entire registry and check if each name (plus aliases) appears verbatim in the text. This catches names that spaCy misses — common in legal documents where names appear in unusual formatting (ALL CAPS, comma-separated lists, table cells).

The two-pass approach compensates for spaCy's limitations on government documents. Legal text has formatting patterns (Bates stamps, case numbers, form fields) that confuse NER models trained on news text.

### Person registry

The registry was built by merging three sources:
1. **Epstein-Pipeline** extraction (1,404 persons with categories and aliases)
2. **La Rana Chicana** dataset (241 names with descriptions and involvement)
3. **Knowledge graph** entities (489 persons with types: perpetrator, enabler, victim, associate)

Deduplication uses normalized name keys. Category priority: knowledge graph type > pipeline category > inferred from description. The final registry has 1,538 unique persons with aliases, categories, and search terms.

### Knowledge graph

For each document containing multiple identified persons, we create co-occurrence edges between all pairs. Edge weights accumulate: if Person A and Person B appear together in 50 documents, their edge weight is 50. Higher-weight signals (co-passengers on flights, email correspondents) get multiplied weights.

The resulting graph enables network analysis: betweenness centrality identifies gatekeepers, community detection finds clusters, and shortest-path queries reveal indirect connections.

Export formats: JSON (D3.js-compatible for visualization) and GEXF (Gephi for analysis).

---

## Phase 4: The Web Interface

### Datasette as foundation

[Datasette](https://datasette.io/) is an open-source tool for exploring and publishing SQLite databases. It provides:
- A web UI for browsing tables and running SQL queries
- A JSON API for every table and query
- FTS5 search integration
- Faceted browsing
- CSV/JSON export

We run Datasette with seven immutable databases and custom templates that replace the default UI with a purpose-built research interface.

### Custom templates

Datasette supports Jinja2 template overrides. We replaced three templates:

**`index.html` (1,447 lines)** — The homepage. Includes:
- Age verification gate (localStorage-based)
- Full-text search box that queries all seven databases in parallel (client-side JavaScript)
- EFTA number detection (regex `^\d{5,8}$`) for direct document lookup
- Featured investigation reports (weighted random sampling from 400+ reports)
- Trending search terms (from hit-counter analytics)
- Database statistics (document counts, page counts)

**`table.html` (335 lines)** — The table browser. Includes:
- Inline FTS5 search with result counts
- Column filtering (equals, contains, starts with, greater than, less than, is null)
- Document reader mode: for documents ≤50 pages, fetches all pages and renders inline with search term highlighting
- Source URL badges that link EFTA numbers to justice.gov PDFs and HOUSE_OVERSIGHT numbers to archive.org images

**`row.html`** — The record detail view. Shows all fields for a single document/page with PDF download links and related records.

### Client-side search orchestration

The homepage search doesn't hit a single backend endpoint. Instead, JavaScript fires parallel fetch requests to six database tables simultaneously:

```javascript
// Pseudocode for the search flow
async function search(query) {
    const results = await Promise.allSettled([
        fetch(`/full_text_corpus/pages_fts.json?_search=${query}`),
        fetch(`/image_analysis/images_fts.json?_search=${query}`),
        fetch(`/transcripts/transcripts_fts.json?_search=${query}`),
        fetch(`/redaction_analysis_v2/documents.json?text__contains=${query}`),
        fetch(`/knowledge_graph/entities.json?name__contains=${query}`),
        fetch(`/spreadsheet_corpus/sheets.json?content__contains=${query}`),
    ]);
    // Merge, deduplicate, render
}
```

This gives sub-second search across all seven databases with no backend coordination. Datasette's JSON API handles the actual query execution.

---

## Phase 5: The AI Research Assistant (RAG)

### What it does

Users type natural language questions — "What financial connections did Epstein have to Deutsche Bank?" — and get answers grounded in specific, cited documents. Every claim links to a verifiable source page.

### Architecture: Retrieval-Augmented Generation

The AI assistant is a custom RAG (Retrieval-Augmented Generation) system with three stages:

**Stage 1: Query planning** — An LLM reads the user's question and generates Datasette API URLs to search relevant tables. The system prompt teaches the model FTS5 syntax (OR, quoted phrases, prefix matching) and the available database endpoints.

```
User: "Deutsche Bank compliance failures"
LLM generates: [
    "/full_text_corpus/pages_fts.json?_search=Deutsche+Bank+compliance",
    "/full_text_corpus/pages_fts.json?_search=Deutsche+Bank+KYC",
    "/full_text_corpus/pages_fts.json?_search=%22know+your+customer%22+Deutsche"
]
```

**Stage 2: Parallel search** — The generated URLs are fetched in parallel (ThreadPoolExecutor, 20 workers). Results are deduplicated by (EFTA number, page number) tuple and capped at 4 pages per document to prevent a single mega-document from dominating context.

**Stage 3: Answer synthesis** — The search results are injected into a second LLM prompt along with the user's question. The model generates a streaming response via Server-Sent Events (SSE), citing specific EFTA numbers and page numbers. The system prompt instructs: "Only answer using evidence from the search results. Cite document identifiers for every factual claim."

### Free model fallback chain

The assistant runs on free-tier models via [OpenRouter](https://openrouter.ai/), costing $0/month. Eight models are configured in a fallback chain:

1. Trinity Large Preview (131K context, 13B active MoE) — primary
2. StepFun 3.5 — fallback
3. Nemotron — fallback
4. Solar — fallback
5. Mistral — fallback
6. Trinity Mini — fallback
7. GPT-OSS-120B — fallback
8. Hermes-405B — fallback

Each provider has independent rate limits. When a model returns 429 (rate limited), it enters a 60-second cooldown and the next model takes over. This circuit-breaker pattern provides resilience: the system has never been fully down during peak traffic.

### Response caching and repetition detection

Responses are cached in memory (LRU, 500 entries, 15-minute TTL) keyed by normalized question text. Cache hit rates exceed 80% because many users search for the same names.

A repetition detector scans the last 400 characters of output for repeated patterns (20-120 characters). If a pattern repeats 4+ times — a common failure mode for LLMs reconstructing tables — output is terminated and the next model in the fallback chain is tried.

### Conversation sharing

Users can share AI research sessions via URL. The `/api/share` endpoint stores conversation threads (up to 50 messages) in a SQLite database with a cryptographic token (`secrets.token_urlsafe(8)`). Shared conversations are retrievable at `/ask?s={token}`.

---

## Phase 6: PII Redaction

### The problem

Government document releases sometimes contain victim-identifying information — names, phone numbers, Social Security numbers, dates of birth, home addresses. The EFTA production was no exception. We discovered victim PII across approximately 400 documents.

### Ethical framework

Our principle: **transparency and privacy can coexist.** We do not remove documents from public access. We redact the specific PII strings within the text, replacing them with empty strings. The document remains searchable and readable; only the identifying information is removed.

We use empty-string replacement rather than labeled tags (like `[REDACTED-NAME]`) to prevent reverse-searchability. A tag like `[REDACTED-NAME]` narrows the search space for re-identification; an empty string does not.

### Three-tier pipeline

The PII redaction tool (`pii_redactor.py`, 972 lines) operates in three tiers:

**Tier 1: High-confidence patterns** — Full names (first + last), phone numbers, email addresses, Social Security numbers. These are auto-confirmed with minimal false positives. Regex patterns with word-boundary matching.

**Tier 2: Context-dependent patterns** — Dates of birth, street addresses. These require surrounding-text analysis to distinguish victim DOBs from financial filing dates, and victim addresses from law office addresses. Context keywords ("victim," "age," "born") trigger classification.

**Tier 3: Surname-only patterns** — Some victims' surnames appear without first names. These have high false positive rates (common surnames appear in non-victim contexts). We use a dual-mode system:
- **Blacklist mode** for rare surnames (SCHWEGEL, DICENSO, PENTEK): redact everywhere except specified skip-EFTAs
- **Whitelist mode** for common surnames (VELASCO, CARTWRIGHT, LANGLEY): redact only in specified victim-context EFTAs

### False positive management

Phone number patterns collide with EFTA numbers (both are 8-10 digit sequences), base64-encoded data, hex strings, and URLs. The pipeline filters these with format-specific checks.

DOB patterns collide with financial filing dates, court dates, and document timestamps. Context-keyword analysis distinguishes these.

All false positives are tracked in `.pii_false_positives.json` and excluded from future scans.

### Audit trail

Every redaction is logged: EFTA number, page number, original text, replacement, tier, timestamp. The pre-redaction text is backed up in a `pages_pii_backup` table in the local database (never deployed to the server). This allows reverification and rollback.

### Results

- 2,099 victim PII instances redacted across approximately 1,400 pages in approximately 400 documents
- Three rounds of scanning: Tier 1, Tier 2, then targeted surname+phone cleanup
- A private watchlist (`.victim_pii_watchlist.json`, 173 entries, 35 victims) tracks all known victim identifiers for ongoing monitoring

---

## Phase 7: Forensic Auditing at Scale

### The discovery

While building the search engine, we noticed that some EFTA URLs on justice.gov were returning HTTP 404. A systematic scan revealed that approximately 64,000 documents had been silently removed from the DOJ website after initial publication — with no Federal Register notices filed as required by law.

### The methodology challenge

The DOJ's website has an age-verification system that confounds automated scanning. Unauthenticated HTTP requests to EFTA PDFs receive a 404 response — not because the document is missing, but because the age gate intercepts the request. This means a naive scan (HEAD request, check status code) produces massive false positives.

### Three-stage audit

**Stage 1: Initial scan** — Automated HEAD requests to all 1.38 million EFTA URLs. This ran across multiple VPS instances over 48 hours. Result: 78,234 HTTP 404 responses.

**Stage 2: Authenticated rescan** — For each of the 78,234 flagged URLs, we used Playwright (Firefox, not Chromium — headless Chromium can't render the age gate's JavaScript button) to:
1. Navigate to the DOJ age-verification page
2. Click the "I am 18" button
3. Obtain session cookies (`justiceGovAgeVerified` + Akamai `ak_bmsc`)
4. Make authenticated HEAD requests using the browser's cookie jar

Result: 67,784 confirmed 404s (10,450 were age-gate false positives).

**Stage 3: Statistical sampling** — From the 67,784 confirmed 404s, we drew a random sample (n=500, seed=42) and verified each with Playwright in a fresh authenticated session. Every 50 requests, canary checks verified the session was still valid (known-good EFTA → should return 200; known-bad EFTA → should return 404).

Result: 474 confirmed removed, 26 still live (5.2% false positive rate). Best estimate: ~64,259 genuinely removed (95% CI: 62,940-65,578).

### Key technical insights

- **Akamai rate limit**: 3,000 requests per IP address, hard limit. Exceeding it returns 401. We spaced requests at 0.3-second intervals.
- **Last-Modified header**: Genuine removal 404s have `Last-Modified: Tue, 02 Sep 2025` (predating the EFTA production). 404s with this header are 100% genuine removals. 404s without it have an 18.8% false positive rate.
- **Session expiry**: Akamai sessions expire. Canary checks every 50 requests detect expiry and trigger re-authentication.
- **Playwright Firefox vs. Chromium**: Chromium's headless shell cannot render the age gate's `#age-button-yes` button. Firefox headless works.

### Impact

This finding was cited by NPR and aligns with noncompliance arguments in the Democracy Defenders Fund's ongoing FOIA litigation. The corrected methodology — accounting for the age gate's false-positive mechanism — became a finding in itself about how government web architecture can create false compliance signals.

---

## Phase 8: Investigation Reports

### The pipeline

Investigation reports are written in Markdown and converted to styled HTML for publication. The conversion pipeline (`build-reports.py`, 1,044 lines) handles:

**EFTA auto-linkification** — Every `EFTA########` pattern in the text is automatically converted to a clickable link pointing to the search engine (`/?q=EFTA12345678`). The regex uses word boundaries and skips patterns already inside `<a>` tags. This means authors write plain EFTA numbers and readers get clickable citations.

**Git-aware dating** — Each report's publication date is extracted from the first Git commit that added the file. Reports pushed in the initial bulk deployment (February 18, 2026) show "February 2026"; individually published reports show the exact date.

**Description extraction** — For index pages and social sharing, the pipeline extracts a description by looking for an "Executive Summary" section first, then falling back to the first meaningful paragraph. Markdown formatting is stripped before truncation.

**Featured reports** — A curated dictionary of 200+ hand-written one-line descriptions controls how reports appear on the homepage. The homepage randomly samples 3-4 featured reports per page load, weighted by view count (from the hit-counter service), so popular reports surface more often.

### Publication flow

1. Write report in Markdown with EFTA citations
2. Commit to `epstein-research` GitHub repository
3. Run `build-reports.py` on the server
4. Script converts all Markdown files to HTML with site styling
5. HTML is served as static files via nginx (Cloudflare-cached for 1 hour)

The entire reports index (400+ reports across 15+ categories) is generated from the directory structure of the Git repository. No CMS, no database, no admin panel.

---

## Phase 9: Deployment and Production

### The server

One Hetzner CPX31 VPS: 4 vCPUs, 8 GB RAM, 160 GB disk. Ashburn, Virginia (near DOJ servers for low-latency source verification). Cost: $17.99/month.

### Three services

| Service | Port | Purpose | Technology |
|---------|------|---------|------------|
| Datasette | 8001 | Database UI + API | Python, SQLite |
| ask-proxy | 8002 | AI research assistant | Python, OpenRouter |
| hit-counter | 8003 | Analytics + comments | Python, SQLite |

All three run as systemd services with automatic restart on failure. Datasette runs as an unprivileged `datasette` user with filesystem restrictions (ProtectSystem=strict, ProtectHome=true, NoNewPrivileges=true).

### nginx reverse proxy

nginx handles TLS termination, routing, rate limiting, and caching:

**Rate limiting zones:**
- General pages: 30 requests/second (handles normal browsing)
- JSON/CSV API: 2 requests/second with burst 5 (prevents bulk scraping)
- AI assistant: 10 requests/minute with burst 3 (protects OpenRouter quota)
- Conversation sharing: 10 requests/minute with burst 3

**Bot blocking:** A `map` directive in the nginx HTTP block matches 20+ AI crawler user-agent patterns (GPTBot, ClaudeBot, Anthropic-ai, etc.) and returns 403 inside each location block. This prevents AI companies from ingesting the corpus via their crawlers.

**Security headers:** X-Frame-Options (SAMEORIGIN), X-Content-Type-Options (nosniff), X-Robots-Tag (noai, noimageai).

### Cloudflare edge caching

Cloudflare sits in front of nginx and caches at the edge:
- HTML pages: 1 hour (`s-maxage=3600`)
- Static assets (CSS/JS/images): 7 days (immutable)
- Featured reports metadata: 5 minutes
- API responses: no caching (`no-store`)

This means the $17.99 server handles 3,000-5,000 daily active users without strain. Cloudflare absorbs the bandwidth and most repeat requests.

### Cloudflare mutual TLS

The server only accepts connections from Cloudflare. A Cloudflare Origin CA certificate handles server-to-Cloudflare encryption, and Cloudflare's Authenticated Origin Pull certificate validates that incoming connections are genuinely from Cloudflare. Direct access to the server IP returns a TLS error.

---

## What AI Did vs. What Required Human Judgment

This project was built with Claude Code (Anthropic's AI coding assistant). Being transparent about what AI did and didn't do matters for credibility and replicability.

### What AI did well

- **Boilerplate code**: CLI scaffolding, Pydantic models, SQLite schema creation, systemd service files, nginx configuration. AI generated correct, working code on the first attempt for most infrastructure tasks.
- **Data pipeline orchestration**: The PDF → text → SQLite → FTS5 pipeline was designed and implemented through AI-assisted development. The parallel processing, resumable state tracking, and error handling were all AI-generated.
- **Template development**: The Datasette HTML templates (1,400+ lines of HTML/CSS/JavaScript) were built iteratively with AI. The client-side search orchestration, age gate, and responsive design were AI-generated.
- **PII pattern matching**: The regex patterns for phone numbers, SSNs, email addresses, and date-of-birth formats were AI-generated. The false-positive filters (EFTA number collision detection, context-keyword analysis) were designed collaboratively.
- **Investigation research**: AI processed thousands of pages of corpus text, identified patterns, cross-referenced entities, and drafted investigation reports. The analytical throughput — reading and synthesizing hundreds of documents per investigation — would be impossible for one person without AI.

### What required human judgment

- **Ethical decisions**: Which information to redact, how to handle victim privacy, whether to publish specific findings. AI flagged PII; humans decided the redaction policy and reviewed edge cases.
- **Editorial standards**: Every investigation report was fact-checked against source documents. AI drafts frequently contained errors from context compression (summarized memories losing precision on dates, dollar amounts, and entity names). The rule "never write from compaction memory — always re-read source documents" was learned through painful experience.
- **Publication decisions**: What to publish, what to hold, what to share with journalists first. The editorial principle — focus on unreported architecture and systems, not celebrity name-drops — is a human judgment call.
- **Forensic audit methodology**: The three-stage audit design (initial scan → authenticated rescan → statistical sampling) was a human methodological decision. AI implemented it, but the insight that the age gate was causing false positives came from manual investigation.
- **Deployment security**: Rate limiting thresholds, bot blocking patterns, Cloudflare configuration, PII redaction verification. AI wrote the configs; humans verified they were secure.

### The error pattern

The most dangerous AI failure mode is **compaction drift**: when conversation context gets long, AI assistants compress earlier messages into summaries. These summaries lose precision. A dollar amount becomes approximate. A date shifts. An entity name gets confused with a similar name. If you write from these compressed memories without re-reading the source, you publish errors.

Our mitigation: scratchpad files that preserve critical facts before context gets long, mandatory re-reading of source documents after any context compression, and a citation audit that verifies every EFTA reference actually contains the claimed content.

---

## Replication Guide: The Minimum Viable Document Database

You don't need all nine layers. Here's the minimum to turn a folder of PDFs into a searchable database:

### Step 1: Extract text (30 minutes of setup, hours/days of processing)

```bash
pip install pymupdf
```

```python
import fitz  # PyMuPDF
import sqlite3
import os

def extract_pdf(pdf_path):
    """Extract per-page text from a PDF."""
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text()
        if text.strip():
            pages.append((i + 1, text, len(text)))
    doc.close()
    return pages

def build_database(pdf_dir, db_path):
    """Build a searchable SQLite database from a directory of PDFs."""
    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT UNIQUE,
            total_pages INTEGER,
            total_chars INTEGER
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS pages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER REFERENCES documents(id),
            filename TEXT,
            page_number INTEGER,
            text_content TEXT,
            char_count INTEGER
        )
    """)
    conn.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS pages_fts USING fts5(
            text_content,
            content='pages',
            content_rowid='id'
        )
    """)
    # FTS5 sync triggers
    conn.execute("""
        CREATE TRIGGER IF NOT EXISTS pages_ai AFTER INSERT ON pages BEGIN
            INSERT INTO pages_fts(rowid, text_content)
            VALUES (new.id, new.text_content);
        END
    """)

    for filename in sorted(os.listdir(pdf_dir)):
        if not filename.lower().endswith('.pdf'):
            continue
        filepath = os.path.join(pdf_dir, filename)
        pages = extract_pdf(filepath)
        if not pages:
            continue

        total_chars = sum(c for _, _, c in pages)
        conn.execute(
            "INSERT OR IGNORE INTO documents (filename, total_pages, total_chars) VALUES (?, ?, ?)",
            (filename, len(pages), total_chars)
        )
        doc_id = conn.execute(
            "SELECT id FROM documents WHERE filename = ?", (filename,)
        ).fetchone()[0]

        for page_num, text, char_count in pages:
            conn.execute(
                "INSERT INTO pages (document_id, filename, page_number, text_content, char_count) VALUES (?, ?, ?, ?, ?)",
                (doc_id, filename, page_num, text, char_count)
            )

    conn.execute("INSERT INTO pages_fts(pages_fts) VALUES('optimize')")
    conn.commit()
    conn.close()
    print(f"Done. Database: {db_path}")

# Usage:
build_database("/path/to/your/pdfs", "corpus.db")
```

### Step 2: Serve with Datasette (5 minutes)

```bash
pip install datasette
datasette serve corpus.db --setting sql_time_limit_ms 15000
```

Open `http://localhost:8001`. You now have a searchable database with a web UI, JSON API, and full-text search. For any document corpus. In under an hour of setup time.

### Step 3: Add an AI assistant (optional, 2-4 hours)

The ask-proxy pattern:
1. User asks a natural language question
2. An LLM generates FTS5 search queries from the question
3. Execute the queries against your database
4. Inject the search results into a second LLM prompt
5. Stream the answer with citations

The key insight: the LLM doesn't need to "know" your documents. It just needs to read search results and cite them. This is why free-tier models work — the task is synthesis and citation, not knowledge retrieval.

### Step 4: Deploy (1-2 hours)

```bash
# On a $5-20/month VPS:
apt install nginx
pip install datasette
datasette serve corpus.db --host 0.0.0.0 --port 8001 &

# nginx reverse proxy (minimal):
# server { listen 80; location / { proxy_pass http://127.0.0.1:8001; } }
```

Add Cloudflare (free plan) for TLS, CDN caching, and DDoS protection. Total cost: $5-20/month for the VPS.

---

## Cost Breakdown

### One-time costs

| Item | Cost | Notes |
|------|------|-------|
| Claude Code (development) | ~$200 | API usage during 2-week build |
| VPS for DOJ scanning | ~$50 | Temporary servers, deleted after audit |
| Domain registration | $10/year | epstein-data.com |

### Ongoing monthly costs

| Item | Cost | Notes |
|------|------|-------|
| Hetzner CPX31 VPS | $17.99/month | 4 vCPU, 8 GB RAM, 160 GB disk |
| Cloudflare | $0/month | Free plan (CDN, TLS, DDoS protection) |
| OpenRouter (AI models) | $0/month | Free-tier models only |
| **Total** | **$17.99/month** | |

The AI research assistant costs $0 because it uses free-tier models via OpenRouter. The quality is lower than paid models, but it's sufficient for document search and citation — the task is retrieval and synthesis, not creative writing.

### What $50,000 would fund

The infrastructure costs are negligible. The expensive resource is human time: reading documents, fact-checking AI output, making editorial decisions, redacting PII, writing investigation reports, responding to journalist requests, and maintaining the platform. Grant funding goes to researcher salary, not technology.

---

## Limitations and Lessons Learned

### OCR quality varies

Government PDFs range from clean digital documents to poorly scanned faxes from the 1990s. OCR output is noisy. Some documents have character-level errors that defeat exact-match search. FTS5 helps (it's tolerant of minor variations), but important documents should be manually verified.

### FTS5 is not semantic search

FTS5 matches words, not meanings. A search for "money laundering" won't find documents that describe the same activity using different words. Vector embeddings and semantic search would help, but add complexity and cost. For government documents — which tend to use precise legal and financial terminology — keyword search works better than you'd expect.

### AI assistants hallucinate

The free-tier models used for the research assistant occasionally generate plausible-sounding claims not supported by the search results. The citation requirement mitigates this (users can verify each claim), but it doesn't eliminate it. Every report published on the site includes the footer: "This analysis relies on Claude Code running Opus 4.6, which can make mistakes."

### Context compression loses precision

The most insidious error source is AI context compression. During long research sessions, earlier context gets summarized, and summaries lose precision on numbers, dates, and names. The mitigation — scratchpad files, mandatory re-reading, citation audits — works but requires discipline.

### One person is a single point of failure

The entire system is maintained by one person. If the maintainer stops, the site stops. Documentation (including this document) is part of the mitigation. The code is open source. But sustainability requires either institutional backing or a community of contributors.

### Privacy is harder than transparency

Identifying and redacting victim PII is more labor-intensive than building the search engine. The three-tier pipeline handles most cases, but edge cases (partial names, indirect identifiers, context-dependent sensitivity) require human review. Any document corpus tool needs PII scanning as a first-class feature, not an afterthought.

---

## Conclusion

The core insight is simple: **SQLite + FTS5 + Datasette + per-page text storage** turns any pile of PDFs into a searchable research tool. Everything else — entity extraction, AI assistants, knowledge graphs, fancy templates — is valuable but optional. The minimum viable version is 50 lines of Python and one `pip install`.

The hard parts aren't technical. They're ethical (PII redaction), methodological (verifying AI output against source documents), and editorial (deciding what to publish and how to frame it). AI dramatically accelerates the technical work but doesn't replace the judgment calls.

If you're a journalist, lawyer, or researcher sitting on a document dump — whether it's a FOIA production, court records, congressional investigation, or corporate disclosure — the barrier to making it searchable is now one afternoon of work and $18/month. The tools are free. The code is open source. The methodology is documented here.

Build the search engine. Let the public find what matters.

---

*This document is part of the epstein-data.com project. The full source code, databases, and investigation reports are available at [epstein-data.com](https://epstein-data.com) and on [GitHub](https://github.com/rhowardstone).*

*This methodology document was written with Claude Code (Opus 4.6), which can make mistakes. All technical claims have been verified against the actual codebase and deployment.*
