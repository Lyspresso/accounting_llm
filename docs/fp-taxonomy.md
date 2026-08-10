# False-Positive Floor — Five-Way Taxonomy
Every finding that kept floor #2 red, classified by MECHANISM. Only `TRUE_FP` and
`PENDING` count against the 10% ceiling.

**Dollar figures are redacted** (`<figure>`): the amounts are answer-key content and
this repository is public. The mechanism is the part that matters here.

## Result

- clean goldens scored: **26**
- `TRUE_FP`: **0**
- `GOLDEN_WRONG`: **0**
- `MATCHER_ARTIFACT`: **11**
- `HASH_MIXING`: **32**
- `PENDING`: **0**

Chargeable items: **0/26** — 95% CI [0.0%, 12.9%], ceiling 10%.

> At 26 goldens a flawless run still bounds at 12.9%. The floor is unreachable at
> this sample size regardless of comparator quality; it needs **≥35 clean goldens**.

## The four open comparator gaps

Each is a *loosening*. Floor #1 (detection) must be **re-measured after each one** — a
comparator that accepts more also detects less.

1. **Prose-null wording.** A key answering "none" is not recognised as agreeing with a
   solver reporting 0, unless the wording matches a fixed phrase.
2. **Aggregation across an unruled alias.** A solver pooling two lines into one is
   equivalent when sides and totals agree, but the account names must be alias-linked
   first or equal money would certify unequal accounting.
3. **Ratio-derivable figures.** `derivable_from_key` does subset-sums only, so a
   percentage the key states *both inputs* of is charged as a mismatch.
4. **Compounded-rounding tolerance.** Independently-rounded components accumulate past
   a sub-dollar tolerance.

## Findings

| item | class | kind | mechanism |
|---|---|---|---|
| `agent_002#03` | MATCHER_ARTIFACT | SOLVER_MISMATCH | key answers 'none'; prose-null not recognised for this wording |
| `agent_002#03` | MATCHER_ARTIFACT | JE_LINE_NOT_IN_KEY | aggregation-equivalent: same sides, same totals, token-linked (needs an alias ruling to clear) |
| `agent_002#03` | MATCHER_ARTIFACT | JE_LINE_NOT_IN_KEY | aggregation-equivalent: same sides, same totals, token-linked (needs an alias ruling to clear) |
| `agent_002#03` | MATCHER_ARTIFACT | KEY_LINE_NOT_IN_SOLVER | aggregation-equivalent: same sides, same totals, token-linked (needs an alias ruling to clear) |
| `agent_002#03` | MATCHER_ARTIFACT | KEY_LINE_NOT_IN_SOLVER | aggregation-equivalent: same sides, same totals, token-linked (needs an alias ruling to clear) |
| `agent_002#03` | MATCHER_ARTIFACT | KEY_LINE_NOT_IN_SOLVER | aggregation-equivalent: same sides, same totals, token-linked (needs an alias ruling to clear) |
| `agent_002#03` | MATCHER_ARTIFACT | KEY_LINE_NOT_IN_SOLVER | aggregation-equivalent: same sides, same totals, token-linked (needs an alias ruling to clear) |
| `agent_151#01` | MATCHER_ARTIFACT | SOLVER_MISMATCH | rounding: key <figure> vs solver <figure> (delta 1.35) inside compounded-rounding range |
| `agent_151#01` | MATCHER_ARTIFACT | SOLVER_MISMATCH | KEY_SILENT hard-failed - key never mentions ['option', 'paying', 'purchase'] |
| `agent_204#02` | HASH_MIXING | SOLVER_MISMATCH | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | SOLVER_MISMATCH | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | SOLVER_MISMATCH | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | SOLVER_MISMATCH | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | SOLVER_MISMATCH | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | SOLVER_MISMATCH | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | SOLVER_MISMATCH | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | SOLVER_MISMATCH | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | SOLVER_MISMATCH | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | SOLVER_MISMATCH | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | SOLVER_MISMATCH | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | SOLVER_MISMATCH | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | SOLVER_MISMATCH | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | SOLVER_MISMATCH | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | SOLVER_MISMATCH | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | JE_LINE_NOT_IN_KEY | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | JE_LINE_NOT_IN_KEY | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | JE_LINE_NOT_IN_KEY | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | JE_LINE_NOT_IN_KEY | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | JE_LINE_NOT_IN_KEY | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | JE_LINE_NOT_IN_KEY | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | JE_LINE_NOT_IN_KEY | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | JE_LINE_NOT_IN_KEY | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | JE_LINE_NOT_IN_KEY | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | KEY_LINE_NOT_IN_SOLVER | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | KEY_LINE_NOT_IN_SOLVER | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | KEY_LINE_NOT_IN_SOLVER | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | KEY_LINE_NOT_IN_SOLVER | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | KEY_LINE_NOT_IN_SOLVER | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | KEY_LINE_NOT_IN_SOLVER | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | KEY_LINE_NOT_IN_SOLVER | solver output inadmissible (provenance) |
| `agent_204#02` | HASH_MIXING | KEY_LINE_NOT_IN_SOLVER | solver output inadmissible (provenance) |
| `agent_283#02` | MATCHER_ARTIFACT | SOLVER_MISMATCH | ratio-derivable from key figures: <figure> / 3.00 = <figure> (pct); derivable_from_key is sum-only |
| `agent_285#00` | MATCHER_ARTIFACT | SOLVER_MISMATCH | ratio-derivable from key figures: <figure> / <figure> = 58.<figure> (pct); derivable_from_key is sum-only |

## Per-item

- `agent_002#03` → **MATCHER_ARTIFACT**
- `agent_151#01` → **MATCHER_ARTIFACT**
- `agent_204#02` → **HASH_MIXING**
- `agent_283#02` → **MATCHER_ARTIFACT**
- `agent_285#00` → **MATCHER_ARTIFACT**
