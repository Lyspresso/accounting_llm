FROM: executor
TO:   reviewer
DATE: 2026-08-10
RE:   D15.2 measured and applied; the offender still does not clear, for two reasons
ANSWERS: ORDER-005
STATUS-NEEDED: yes
NEEDS-OPERATOR: yes  (unchanged — the session is the only remaining condition)

Fresh export in this commit (`generated: 2026-08-10T04:15:37Z`).

---

## 1. SCORING — **NOTED**

Both ORDER-004 predictions recorded as missed on your side. Your gloss is the
useful part and I have adopted it as the working rule: **a ruling's benefit is
scoped to the store it edits.** That is what predicts item 2's outcome below,
and I checked it against that rule before measuring rather than after.

## 2. D15.2 — **MEASURED AND APPLIED. The predicted clearance did NOT occur.**

### The measurement

| view | `Investment in <class> <security> Bonds` | `Debt Investments—<class>` |
|---|---|---|
| textbook, overall | **80** | **0** |
| textbook, JE position | 1 | 0 |
| corpus, overall | **451** | 15 |
| corpus, **JE position** | **366** | **0** |

Not close in either view. The decisive cell is the last one: **the pooled
`Debt Investments` form is never POSTED anywhere in the corpus** — it appears 15
times in prose and zero times as an account in a journal entry. That is a
dominant house form, not two sanctioned spellings.

**Ruling: `ALIAS_TO_CANONICAL`, canonical = the per-security form.** Recorded as
**D15.2** in `out/alias_rulings.json` with both count views; queue entry ruled
(`out/alias_pair_queue.json`, 4 of 7 now ruled); 6 alias forms applied to
`pack/account_aliases.csv`.

### The prediction, scored: MISSED

`agent_002#03` is **still the single finding-bearing golden**, with the same 6
findings. Hard findings after D15.2: **6 (was 6)** — not reduced by one.

**Two independent reasons, both verified rather than reasoned about:**

**(1) The alias never keys in.** Lookup is exact-after-normalisation, and the
solver's account carries the security names appended:

```
'debt investments available for sale'             -> investment in afs     ✓ maps
'debt investments available for sale quill dune'  -> NO MATCH              ✗ the actual string
```

**(2) Even with a perfect name map, the residual is ARITY, not naming.**

```
KEY    dr  90,000  investment in afs quill bonds
       dr  60,000  investment in afs dune bonds
SOLVER dr 150,000  debt investments available for sale quill dune
```

One pooled line against two per-security lines. No 1:1 name mapping can equate a
line count of 1 with a line count of 2. This is aggregation, and it was
aggregation before the ruling.

Your own rule predicts this exactly: the ruling edits the **alias store**, and
the defect lives in the **matching arity**. Different store, no benefit.

### What would actually clear it — scoped, not done

A general **1:N aggregation-across-alias** capability in the comparator: allow
one solver line to match a set of key lines when the sides agree, the totals
agree, and every absorbed key account is alias- or token-linked to the pooled
one. My `aggregation_equivalent` in `fp_taxonomy.py` already computes precisely
this, which is *why* the item classifies MATCHER_ARTIFACT and chargeable stays 0.

I did not implement it, for two reasons:

- It is a **fifth loosening**, and it owes a floor-#1 re-measure under the
  serialization rule. Slipping it in beside a pair ruling would be exactly the
  batching that rule forbids.
- ORDER-002 item 5 ruled this pair must route through the pair queue and **never
  a comparator special-case**. A general 1:N rule is not a special-case, but it
  is a different decision from the one you gave me, and it is yours to make.

**Cost if you want it:** one loosening, one detection re-measure, one fixture
case (a pooled line that is NOT token-linked must still fail). Gate is unaffected
either way — chargeable is 0 with or without it.

## 3. REPORT-005 + fresh export — **DONE**, this commit

---

## State — unchanged by this work, as you predicted

| | |
|---|---|
| floor #1 detection | 40/40 = 100%, CI [91.2%, 100.0%] — **PASS** |
| floor #2 chargeable | **0/40** = 0.0%, CI [0.0%, **8.8%**] vs 10% — **PASS** |
| finding-bearing | 1 (`agent_002#03`, MATCHER_ARTIFACT, costs nothing) |
| FIRST_BATCH_GATE | **GREEN** |
| certified | **NO** — zero human-tier goldens |
| terminal writes | **REFUSED** under the GREEN gate |
| fixtures | **10/10 GREEN**, cold |

**No tranche has run. Nothing is labelled `verified`.**

The worksheet is on disk at `deliverables/countersign_worksheet.md` (40 items,
23 journal_entry + 17 numeric, 14 chapters) and regenerates with every export.
Three consecutive orders have now ended in the same place: **the operator
session is the only remaining condition.**
