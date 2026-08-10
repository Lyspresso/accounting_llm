# Ledger row matrix

generated: 2026-08-09T05:03:54Z

Unit ladder: **rows** (this file, forensics) → distinct content hashes → **lineages** (the reporting unit).

| status | scope | causing event | rows |
|---|---|---|---:|
| `unverified` | current | migrated | 1728 |
| `machine_passed` | current | stage0 | 513 |
| `unverified` | superseded | stage0 | 129 |
| `failed` | current | stage0 | 93 |
| `machine_passed` | current | mechanical re-key, bytes unchanged | 83 |
| `machine_passed` | superseded | stage0 | 75 |
| `machine_passed` | current | evidence/comparison.json | 73 |
| `failed` | superseded | stage0 | 19 |
| `failed` | current | mechanical re-key, bytes unchanged | 15 |
| `failed` | current | evidence/comparison.json | 13 |
| `machine_passed` | superseded | evidence/comparison.json | 11 |
| `DUPLICATE_OF` | superseded | stage0 | 9 |
| `failed` | superseded | evidence/comparison.json | 3 |
| `unverified` | current | bytes changed by key repair - must re-verify | 1 |
| **SUM** | | | **2765** |

Total rows in ledger: **2765** — remainder **0**.

## Reading the cells

- `mechanical re-key, bytes unchanged` — a hash change that left the content a student reads untouched, so state carried forward in full.
- `evidence/comparison.json` — verdicts reconstructed from evidence bundles after a truncating write destroyed the ledger rows. The bundles are the real record; the ledger is a derived index.
- `bytes changed by key repair` — the single row that correctly forfeited state (`agent_130#00`), later re-minted by free re-comparison at comparator v3.8.
- `superseded` — rows at content hashes no longer current. Retained deliberately: lineages end, they never disappear.

