# Verification run — consolidated status

generated: 2026-08-10T04:32:47Z

## Corpus

| metric | value | unit |
|---|---:|---|
| Questions | 1828 | items |
| Class A (machine-verifiable) | 1232 | items |
| Class B (judgment) | 596 | items |
| Journal-entry lines parsed | 13972 | lines |

## Account resolution — units reconciled

| metric | value | unit |
|---|---:|---|
| `UNKNOWN_ACCOUNT` | 843 | **items** (one flag per item) |
| Unresolved account lines | 3690 | **lines** |
| `NOTATION` classified | 129 | **lines** |

Reconciliation: purging **129 notation LINES** removed **13 ITEMS** from the `UNKNOWN_ACCOUNT` flag (938 → 843). The two figures are in different units and do not subtract: an item is flagged once no matter how many of its lines are unresolved, so clearing lines only clears an item when it clears that item's LAST unresolved line.

## Pre-flight (last run)

| floor | result | verdict |
|---|---|---|
| detection | 40/40 = 100.0% | PASS |
| false positive | 0/40 = 0.0% | PASS |

**LAUNCH GATE: GREEN**

## Dual derivation — symmetric context

- verified by derivation: **18** (figures)
- genuine disagreement: **19** (figures)
- unverified / no counterpart: **9** (figures)
- items fully cleared: **4/11** (items)

## Goldens

- count: **42** (items)
- tiers: {'adjudicated': 8, 'ai_cross_checked': 34}
- rules guarded: **13**, none unguarded

## Duplicates

- byte-identical groups: **8**
- retired `DUPLICATE_OF`: **9** (items)

## APIC context guard

- security-unqualified APIC lines: **11** (lines)
- exposure (unqualified + preferred context): **0** (entries) — nothing currently mis-folded, guard installed prospectively

## Pipeline funnel — unit: LINEAGES

| state | lineages |
|---|---:|
| `unverified` | 1703 |
| `machine_passed` | 99 |
| `failed` | 17 |
| `DUPLICATE_OF` | 9 |
| **TOTAL** | **1828** |

Partition remainder: **0**.  Unit ladder: rows (3185, forensics) → distinct content hashes → **lineages (1828, the reporting unit)**.

## Cost — harness meter authoritative

| basis | value |
|---|---:|
| trim-1 cost per question (evidence_parity) | **39,652** billable |
| baseline-1 comparison | 50,091 billable |
| tranche-1 primary solves only, 10M cap | **252** questions |
| tranche-1 with dual-by-default @ 38% | **182** questions (16% of 1,132) |

Retired, discarded not refreshed: the 0.799 ratio and the +44% answer-count observation, both from `trim_ab.js`, which ran without the coverage instruction.

## Provenance

- 19 cached `evidence_dual` outputs marked **PACK_NOTES_STALE** (asymmetric context); retained as records, excluded from verdicts.
- OPEN: the trim side of the LO 11-8 comparison is stale for the same reason, and `stamp()` records the CURRENT pack-notes version rather than the one in force at generation. `agent_204#02` is therefore **unresolved**, not decided.

## Gates

| gate | state |
|---|---|
| LO 11-8 family | **LIFTED** — wiring probe green, 13/13 contexts |
| Launch | **RED** — floor #2 unmet |

