# Comparison-site audit — enumerated

Every code path in the stack that compares two numeric values. "Unified" is an
enumerated fact here, not a claim.

## The partition — exact and disjoint

**43 = 35 non-value + 5 routed + 2 justified-inside + 1 retired.**

| class | n | in the accounting-value count? |
|---|---:|---|
| non-value (string/status equality) | 35 | **no** — not comparisons of amounts |
| routed through canon | 5 | **yes** |
| justified, INSIDE the count | 2 | **yes** — balance invariant, aggregation |
| retired (superseded module) | 1 | **yes**, historically |
| **TOTAL** | **43** | accounting-value sites = **8** |

Two sites are classified explicitly because they sit on the boundary:

- **Balance invariant** (`abs(dr - cr) > 0.01`) — **INSIDE** the accounting-value
  count. It compares two amounts. It is justified rather than routed because it
  is intra-source: each source's entry must balance in its OWN arithmetic,
  exactly. Routing it through a cross-source tolerance would let an unbalanced
  entry pass because the other source happened to balance.
- **Canary** (`abs(x - planted) <= 0.01`) — **OUTSIDE** the accounting-value
  count. The planted value is off-manifold by construction; the question is "did
  a blind solver reproduce a number no correct derivation yields". It is a
  blindness test, not a correctness test, and loosening it would weaken the
  wrong property. Counted in the 35.

The two tie-detectors (`labelgrammar:112`, `score_dual:72`) are **OUTSIDE**: they
compare match *scores*, not amounts. Also counted in the 35.

## Routed through canon — canon is authoritative

| site | function | rule |
|---|---|---|
| `canon.py:166` | `corroborates` | scalar path, precision inheritance |
| `canon.py:173` | `corroborates` | percent ↔ fraction |
| `canon.py:111` | `precision_tol` | magnitude-scaled tolerance |
| `canon.py:145` | `period_factor_pair` | period/unit equivalence, granularity-guarded |
| `compare_stage1_v3.py:149` | `agg_matches` | → `precision_tol` |
| `compare_stage1_v3.py:233` | `aggregates_to` | → `precision_tol` |
| `compare_stage1_v3.py` JE gate | two-pass exact-then-tolerance | → `precision_tol` |

## Justified, not routed — written justification required

| site | comparison | justification |
|---|---|---|
| `compare_stage1_v3.py:181` | `abs(dr - cr) > 0.01` | **Balance invariant, intra-source only.** Each source's entry must balance in its OWN arithmetic, exactly. Routing this through a cross-source tolerance would let an unbalanced entry pass because the *other* source happened to balance. Never compares across sources. |
| `compare_parity.py:128` | `abs(x - planted) <= 0.01` | **Canary.** The planted value is off-manifold by construction; the check is "did a blind solver reproduce a number no correct derivation yields". A tolerance here would weaken a blindness test, not a correctness test. |
| `labelgrammar.py:112` | tie detection `< 1e-9` | Compares **match scores**, not amounts. Detects ambiguity between two candidate pairings. |
| `score_dual.py:72` | tie detection `< 1e-9` | Same: match scores. |

## Retired

| site | status |
|---|---|
| `compare_stage1.py` (comparator v2) | **Superseded.** Carries its own private `tol()`. Retained only as history; must not be imported. Live drift risk if anything ever calls it. |

## The site the grep could not see

`ms()` compares journal lines by **`Counter` equality on `(account, side, round(amount,2))`**. That is a numeric comparison with an implicit exact-equality rule, and it appears in **no** grep for `==`, `abs(`, or `round(...) ==` because the comparison happens inside dict equality.

It was the single unrouted accounting comparison in the stack, and it disagreed
with the scalar path: `corroborates()` called `279,286.65` and `279,287`
equivalent while `ms()` called them different — same figure, same item, two
verdicts. Now routed through canon via two-pass matching (exact first, tolerance
second) with `(account, side)` retained as a hard structural gate.

**Lint implication:** a pattern-based comparison-site lint would have missed
this. New comparison sites must be declared, not detected — the enumeration is
maintained by hand and this file is the record.
