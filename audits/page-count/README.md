# Page-count audit — machine-readable receipts

Supporting data for the forensic page-count audit ("Where Are the 3.5 Million Epstein Pages?").
Every file here is deterministic and reproducible from public DOJ material.

| File | What it is | Rows |
|---|---|---|
| `DS9_BLANK_SLOTS.csv` | The 23 Data Set 9 Bates numbers the DOJ manifest lists but serves as blank/non-substantive files, with the exact byte size justice.gov returns for each (through the age gate, 2026-07-31): 20 empty (0 bytes), 1 broken stub (45 bytes), 2 "No Images Produced" placeholder pages (2,433 bytes). | 23 |
| `HOC_UNPOSTED_009974-010476.csv` | The 503 House Oversight Committee pages (HOUSE_OVERSIGHT_009974–010476) produced to Congress but never posted publicly. | 503 |

Related receipts elsewhere in this repo:
- `../../NATIVE_FILES_CATALOG.csv` — complete native-file inventory (source of the 547-page reconciliation).
- `../../methodology/MISSING_EFTA_ANALYSIS.md` — the page-based EFTA gap-detection method behind the 187-stamp accounting.
