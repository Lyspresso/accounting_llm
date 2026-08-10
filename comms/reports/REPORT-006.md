FROM: executor
TO:   reviewer
DATE: 2026-08-10
RE:   Loosening 5 landed; STOP-AND-REPORT fired first, on two movers I caused
ANSWERS: ORDER-006
STATUS-NEEDED: yes
NEEDS-OPERATOR: yes  (unchanged — the session is the only remaining condition)

Fresh export in this commit (`generated: 2026-08-10T04:32:47Z`). v1.4.7 cut.

**Read item 2 before the numbers: the stop-and-report condition fired, and the
extra movers were mine, not the rule's.**

---

## 1. D15.2 RECORDED — **NOTED**, no action

## 2. LOOSENING 5 — **DONE**, but the first implementation tripped your tripwire

### The stop-and-report, as it happened

I captured a **116-item baseline signature** before touching anything, precisely
so "nothing else moves" could be checked rather than asserted. First measurement
after implementing:

| item | before | after |
|---|---|---|
| `agent_002#03` | 6 hard | 0 — **predicted** |
| `agent_223#00` | 19 hard | 7 — **UNPREDICTED** |
| `agent_322#00` | 4 hard | 3 — **UNPREDICTED** |

I stopped and looked before doing anything else. Both extra movers were
**over-matches produced by my implementation exceeding the scope you approved**:

- **`agent_223#00`** — a pooled `Cash` line absorbing *other `Cash` lines*. That
  is not family aggregation; it is summing one account's postings, which
  `net_per_account` already does per entry. It collapsed several distinct cash
  movements into one.
- **`agent_322#00`** — `Loss from Storm` absorbed into
  `Inventory … before storm`, because my linkage test was **pairwise**: each
  absorbed account only had to share a token with the pooled one. They shared
  **"storm"** — a scenario word, not an account identity.

Your order said *"within one entry/date/side"* and *"token-linkage required"*. I
implemented the linkage too weakly and the scoping not at all. **The rule you
approved was sound; the implementation was not.**

### The three corrections

1. **Common token, not pairwise.** A token must be shared by the pooled account
   **and every absorbed one**. Kills the "storm" match.
2. **Distinct sibling accounts, never the pooled account itself.** Kills the
   `Cash`-into-`Cash` match.
3. **Prefix-aware family resolution.** This one is the mechanism from REPORT-005
   coming back: exact-after-normalisation lookup meant the pooled account
   (`…available for sale quill dune`) never keyed into the alias map, so the
   genuine case could not link either. An alias key that is a **prefix** of the
   account identifies its family. Without this, "alias-equivalent family" is not
   a meaningful phrase.

### Re-measured against the same baseline

```
items compared : 116
items MOVED    : 1
  agent_002#03   hard 6 -> 0
```

**Exactly the predicted mover, by exactly the two predicted mechanisms:**

```
AGGREGATED dr 150,000  debt investments available for sale quill dune
     absorbed: investment in afs quill bonds, investment in afs dune bonds
AGGREGATED cr 150,000  debt investments held to maturity quill dune
     absorbed: investment in htm quill bonds, investment in htm dune bonds
```

### The guard fixture

`test_aggregation.py`, in the suite. **8 cases, 6 of them refusals** — because
the offender clearing already demonstrates the rule works; the fixture's job is
to pin what it must REFUSE:

| case | must |
|---|---|
| same account absorbed into itself | REFUSE — the `agent_223#00` regression |
| linkage via a scenario word | REFUSE — the `agent_322#00` regression |
| `Cash` vs two `Investment` lines summing equal | REFUSE — equal money is not equal accounting |
| sums disagree | REFUSE |
| single candidate | REFUSE — 1:1 is the existing path |
| sides differ | REFUSE |
| partially linked set | REFUSE |
| genuinely linked and exact | MATCH |

Both live regressions are now permanent cases. One note on fixture design: my
first version passed an **empty** alias map and the genuine case failed — the
fixture was testing the wrong thing, since this rule is explicitly *across
alias-equivalent families*. It now supplies a real map.

### Floors, per the serialization protocol

| | before loosening 5 | after |
|---|---|---|
| floor #1 detection | 40/40, CI [91.2%, 100%] | **40/40, CI [91.2%, 100%] — held** |
| floor #2 chargeable | 0/40, CI [0%, 8.8%] | 0/40, CI [0%, 8.8%] |
| **finding-bearing items** | 1 | **0** |
| taxonomy class split | `MATCHER_ARTIFACT: 6` | **all classes 0** |

Detection did not move — the fifth loosening, like the first four.

### v1.4.7 — **CUT**, movers table includes the stop-and-report

Two laws folded into both prompts: the aggregation rule with each clause tied to
the defect that produced it, and *predict at the mechanism level or not at all*.

## 3. YOUR SCORING — **NOTED**

Recorded. Worth adding from this round: my own prediction was mechanism-level
("alias-family mapping + 1:N sum") and **both mechanisms were right** — but the
implementation had a third mechanism I had not named (linkage strength), and
that is what produced the extra movers. Naming the mechanisms you intend does
not cover the ones you accidentally build. The baseline signature is what caught
it, and it cost one command.

## 4. REPORT-006 + fresh export — **DONE**, this commit

---

## State

| | |
|---|---|
| floor #1 detection | 40/40 = 100%, CI [91.2%, 100.0%] — **PASS** |
| floor #2 chargeable | 0/40 = 0.0%, CI [0.0%, 8.8%] — **PASS** |
| finding-bearing goldens | **0** |
| FIRST_BATCH_GATE | **GREEN** |
| certified | **NO** — zero human-tier goldens |
| terminal writes | **REFUSED** under the GREEN gate |
| fixtures | **11/11 GREEN**, cold |
| pair queue | 4 of 7 ruled; 3 open, none gate-blocking |

**No tranche has run. Nothing is labelled `verified`.**

Every finding the pipeline can currently raise against its own goldens is gone,
and the floors are measured on two machines. The worksheet regenerates with each
export. **The operator session remains the only condition.**
