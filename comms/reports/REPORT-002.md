FROM: executor
TO:   reviewer
DATE: 2026-08-10
RE:   ORDER-002 executed; four loosenings serialized; countersign packet built
ANSWERS: ORDER-002
STATUS-NEEDED: yes
NEEDS-OPERATOR: no  (DECISION-002 answered — see item 10)

All ten items below. Ships with a fresh `deliver.sh` export and v1.4.5.

---

## 1. RULING — revert the terminal — **DONE**

`agent_204#02` moved `verified` → `machine_passed`, stage 1, evidence retained
(`out/evidence_trim_sym/agent_204_02`, `out/evidence_dual2/agent_204_02`), row
carries `reverted_from: verified`, `authority: ORDER-002 item 1`, and
`casebook: CLOSED (scored, returned to machine_passed)`. Ledger 3,165 → 3,167
rows — nothing deleted. Terminal count now **0**.

**The revert exposed a defect in the sentinel, which is the more useful finding.**
The revert did not register: `terminal_count` counted *any row ever terminal*,
and `decompose` ranked terminal above staged. Under merge-only history that made
a terminal state **unrevertable** — a reviewer ruling could not physically land.
Both now use one resolver, `resolve_current()`: highest STAGE wins (stage-0
re-normalisation never overrides a verdict), and among rows at that stage the
LAST wins (so a verdict can be revised, visibly). The sentinel then correctly
halted on the fall, and I cleared it with `--invalidate` rather than silently —
authority recorded in the row.

## 2. STRUCTURAL — terminal write gate — **DONE**, shipped as v1.4.5

`ledger_io.append_rows` refuses `verified`/`needs_human` while the gate is RED,
unless `comms/operator/OVERRIDE-terminal*.md` exists. **An unreadable or missing
gate file counts as RED** — a gate that cannot be read is not a green light.
The override is a *file*, so an exception is an artifact with an author and a
diff, never a flag someone passed once.

Enforcement probe standing in `test_writepath.py`, 5 cases: refused under RED;
`machine_passed` still accepted under RED; missing gate defaults to RED;
override file permits; GREEN permits. **Expected movers: ZERO, confirmed** — the
guard restricts future writes only and rewrote nothing.

Type declared **behavior change**; before/after capture in
`skill/PACKAGE-CHANGELOG.md` under v1.4.5.

## 3. APPROVED — agent_130#00 KEY_REPAIR — **DONE**

Entry `(k)` added to `corpus/source-packs/agent_130.md`: Dr Restricted Cash
10,000 / Cr Cash and Cash Equivalents 10,000, with the check line showing it
nets to zero inside the combined cash pool so part (d)'s T-account proof is
unchanged. Re-normalised: **exactly one hash moved**, item count 1,828 → 1,828.
Golden re-pinned post-repair to PASS.

**The free-re-compare property held exactly as predicted**: stem unchanged ⇒
cached solver output still admissible ⇒ re-compared at zero solve cost ⇒
**0 hard findings**. Key repair, not stem repair; no re-solve owed.

**ONE THING THE ORDER COULD NOT HAVE KNOWN — flagging, not acting.** The stem's
Required (b) says *"labeled a–j"*, and the key already used exactly (a)–(j). The
repair is (k). So the key is now complete against "explain all balance sheet
account changes" while its own label range reads stale. Options: amend the stem
to a–k (a STEM repair ⇒ forfeits the cached derivation ⇒ one re-solve for this
item), or rule that the label range is illustrative. **I did not touch the
stem** — that is a different repair class with a different cost, and it was not
what was approved.

## 4. LAWFUL NUMBER — **DONE**

`preflight.py` now consumes `fp_taxonomy.chargeable_items()`. Both numbers are
printed, the lawful one marked:

```
finding-bearing: 1  raw rate 3.7% CI [0.7%, 18.3%]  (NOT the gate's number)
CHARGEABLE     : 0  rate 0.0%   <- the gate's number (TRUE_FP | PENDING)
  class split  : {'TRUE_FP': 0, 'GOLDEN_WRONG': 0, 'MATCHER_ARTIFACT': 6,
                  'HASH_MIXING': 0, 'PENDING': 0}
95% CI         : [0.0%, 12.5%]   ceiling 10%   -> FAIL on the upper bound
```

As you predicted, no verdict changed. The displayed number is now the one the
law defines.

## 5. THE FOUR LOOSENINGS — **DONE, serialized, floor #1 re-measured after each**

| # | loosening | floor #1 after | finding-bearing items |
|---|---|---|---|
| baseline | — | 40/40, CI [91.2%, 100%] | 4 |
| 1 | prose-null wording variant | **40/40, CI [91.2%, 100%]** | 4 |
| 2 | compounded rounding (D7 scope) | **40/40, CI [91.2%, 100%]** | 4 |
| 3 | key-silent routing to Stage 2 | **40/40, CI [91.2%, 100%]** | 3 |
| 4 | ratio-derivable quotients | **40/40, CI [91.2%, 100%]** | **1** |

**Detection did not move once.** Each loosening is bounded rather than broad:

- **(1) prose-null** requires the null word to be bound to a MEASURE
  (`NI: none`, `no gain or loss`, `effect … $0`). A bare "none" does not match —
  otherwise any zero passes anywhere. Verified against `none of the above`.
- **(2) compounded rounding** applies **only inside a schedule context** and the
  bound is *derived*: `0.5 × ROUND_CHAIN_MAX`, 0.5 per rounding point, depth 3
  measured from the corpus. Outside a schedule, nothing changed (0.5 as before).
  Probed: accepts the $1.35 convention pair, still rejects a $2 error and a $10
  error.
- **(3) key-silent routing** emits `KEY_SILENT_UNADDRESSED` (SOFT) and routes to
  Stage 2. **It is not a pass** — per D5 a no-counterpart figure stays
  UNVERIFIED and never default-passes; the label just moves to the stage that
  can settle it.
- **(4) ratio-derivable** is guarded exactly like the subset-sum: divisors within
  0.01 of 1 rejected (a key routinely contains a 1, and an unguarded quotient
  scan certifies everything and stops testing), and a "ratio" equal to one of its
  own inputs rejected as degenerate.

**agent_002 alias pair: routed to the PAIR QUEUE, not special-cased.**
`out/alias_pair_queue.json`, entry 4, `ruling: null`, with measured corpus
dominance attached (`investment in htm securities <name> bonds` is the dominant
key form; the solver's pooled `debt investments—available for sale` form does
not occur in any key). Awaiting your ruling under the dominance rule. Its 6
findings are the only ones left.

**Two regressions the fixtures caught during this work, both mine:**
- Moving the key-silence test into `canon` carried the taxonomy's *narrower*
  `PROSE_NULL` with it, which silently overwrote the loosening-1 pattern. The
  canon fixture went RED within the minute. One definition now, at the top.
- The ratio branch was initially placed after a candidate filter that keeps only
  pool values ≤ v — right for sums, exactly wrong for ratios, whose inputs are
  larger than the quotient. It was unreachable for every case it was written for.

## 6. DELIVERABLES PURITY — **DONE**

`ch17_standards_vintage.md` moved to `pack/` (`git mv`, history preserved) — it
is a pack asset with no generator. `deliverables/` now holds only what
`deliver.sh` regenerates. Hand-edit ratification noted, thank you.

Identifier gate added to `deliver.sh`: **count must be 0 or the export aborts**.
Patterns live in `.identifier_scan_local`, gitignored, per your constraint that
the guard must never publish what it guards. **Negative-tested**: planted an
identifier, export aborted with exit 1; removed it, gate returns 0 matches. A
guard that has never failed is not known to work.

## 7. FIXTURES — **DONE, both standing**

- `test_tool_parity.py` (new, 8th suite): asserts the offender **SETS** are
  identical (not just counts), that preflight's gate number **is** the
  taxonomy's chargeable metric, and that every bundle the shared resolver hands
  out is admissible.
- Cold cache is now enforced **inside** `run_fixtures.sh` — it clears
  `__pycache__` and runs every suite with `python3 -B`. This is not decoration:
  a suite reported 8/8 GREEN in this project while a module held a
  `SyntaxError`, because Python served stale bytecode.

Suite is now **9/9 GREEN**. New sentinel case added: *a hash move (repair) must
NOT halt* — see item 1.

## 8. COUNTERSIGN PACKET — **DONE**, and it carries a limit you should see first

`countersign_packet.py` → `out/countersign_packet.json`. 13 nominations
(7 needed to reach n≥35, +6 margin for cross-check attrition), each with worked
evidence: harness, evidence path, key_lines, answer count, admissibility.
Stratified one per chapter across **13 chapters** (ch8–ch22).

**CLASS COVERAGE WARNING — the packet is 13/13 journal_entry.**

| class | corpus | in packet |
|---|---|---|
| journal_entry | 1,128 | 13 |
| **mcq** | **596** | **0** |
| **numeric** | **104** | **0** |

Not a selection choice — **no mcq or numeric item has an admissible derivation
to nominate**, because Stage 1 has never run on them. So certifying floor #2 on
this packet certifies it **for journal-entry items and for those only**. It is
not a corpus-wide certification and must not be quoted as one. The warning is
printed by the tool and stored in the JSON so it cannot travel separately from
the number.

That interacts with your sequence-to-GREEN: n≥35 is reachable now, but a
corpus-wide floor #2 requires Stage 1 coverage of Class B first — which is the
568 solves from REPORT-001 §1(c).

## 9. RECORDED — **DONE**, no action

Class B negative result, blast-radius closure, and the per-item staleness
scoping correction are accepted into the books.

## 10. OPERATOR — DECISION-002 — **ANSWERED: A, CERTIFY FIRST**

`comms/operator/DECISION-002-certify-first.md`. Nothing launches until the
countersign session is done.

**Launch semantics amended, explicitly**: DECISION-001's budget stands
unchanged, but its trigger is now a conjunction —

    tranche 1 fires when   pre-flight GREEN
                     AND   the operator session has certified floor #2 at human tier

An executor seeing GREEN with no completed session **does not launch**, and says
so. The write-path gate from item 2 is still built; under A it is defence in
depth rather than the thing that makes launching safe.

---

## State at this commit

| | |
|---|---|
| floor #1 detection | 40/40 = 100%, CI [91.2%, 100.0%] — **PASS** |
| floor #2 chargeable | 0/27 = 0.0%, CI [0.0%, **12.5%**] vs 10% ceiling — **FAIL** |
| finding-bearing items | 1 (agent_002#03, awaiting the pair-queue ruling) |
| terminal states | 0 |
| ledger | 3,167 rows, 1,828 lineages |
| fixtures | 9/9 GREEN, cold cache |
| gate | **RED**. No tranche has run. |

Floor #2 now fails on **one** blocker, not three: sample size. The point
estimate is 0 and detection never moved; n=27 → need 35. The nominations exist
and are attached.
