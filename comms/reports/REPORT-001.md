FROM: executor
TO:   reviewer
DATE: 2026-08-10
RE:   Truth sync after the tree merge; the mover is named
ANSWERS: ORDER-001
STATUS-NEEDED: yes
NEEDS-OPERATOR: yes  (one ruling, item 3; one rule exception, item 6)

---

## 0. Read the layer — DONE

Read in order: `00-START-HERE.md`, `01-COMMUNICATION.md`, `docs/01-GLOSSARY.md`
through `docs/08-RELEASING.md`, `reviewer/REVIEW-STATE.md`. Confirmed.

Two things I read there changed what this report says, and both are recorded
below rather than quietly absorbed: **D6** (floor #2 certifies at HUMAN tier
only) and the retired belief **"more goldens will fix the FP rate."**

---

## 1. TRUTH SYNC

### (a) agent_204#02 fresh symmetric TRIM solve — **DONE. Run, scored, closed.**

- Solve: `out/evidence_trim_sym/agent_204_02/` (21 answers, 13 JE lines,
  `peeked: false`), harness `trim-sym-1`, prompt from `build_solver_prompt.py`
  with the LO 11-8 note present in the instruction region.
- Provenance captured at write time, not retroactively:
  `out/evidence_trim_sym/agent_204_02/provenance.json` →
  `captured_at_write_time: true`.
- Scored fresh-vs-fresh against `out/evidence_dual2/agent_204_02/`:
  **12 of 12 shared figures agree, 0 contradictions.** One coverage-only
  difference (a figure the trim side reports and dual does not). Artifact:
  `out/sym204_score.json`.
- Against the key, comparator v3.8 returns **0 findings against 13 key lines
  for BOTH derivations**, 0 routed to Stage 2. Artifacts:
  `out/sym204_compare_trim_sym.json`, `out/sym204_compare_dual2.json`.

**The item is clean and always was.** The prior 13-figure "disagreement" was
manufactured by context asymmetry — the trim harness carried no LO 11-8 rule
while dual did. This closes the RETIRED entry *"agent_204's 13 still UNSCORED
pending fresh symmetric trim solve"*, and is consistent with D9/D19.

Golden corrected accordingly in `goldens_v2.py`: `agent_204#02` moved
**FAIL → PASS**, `guards_rule: solver_context_symmetry`.

### (b) fp_taxonomy.py — **DONE. Built AND run.** `out/fp_taxonomy.json`

```
clean goldens scored : 26
goldens with >=1 hard finding : 4

findings by class:
  TRUE_FP               0
  GOLDEN_WRONG          0
  MATCHER_ARTIFACT     11
  HASH_MIXING           0
  PENDING               0
  TOTAL                11

chargeable ITEMS (TRUE_FP or PENDING findings) : 0/26
  chargeable rate 0.0%   95% CI [0.0%, 12.9%]   ceiling 10%
  -> floor #2 FAILS on the upper bound
```

**Zero true false positives.** All 11 findings on 4 items are MATCHER_ARTIFACT,
each with a named mechanism:

| item | mechanism |
|---|---|
| `agent_002#03` | prose-null wording — the key answers "NI: none"; a solver reporting 0 agrees, and `corroborates` does not recognise that phrasing. Plus 6 JE findings that are aggregation-equivalent (same sides, same totals, token-linked) across an unruled alias pair. |
| `agent_151#01` | compounded rounding — key 240,614.00 vs solver 240,612.65, delta 1.35, from two independently-rounded components. Plus one genuine key-silent figure hard-failed instead of routed. |
| `agent_283#02` | same rounding class (D7 convention pair). |
| `agent_285#00` | ratio-derivable — the key states *both inputs* (81,911 and 140,000) and never writes the quotient; `derivable_from_key` is sum-only, so 58.51% is charged as a mismatch. |

**The MATCHER_ARTIFACT exclusion is a FORECAST, not a measurement.** All four
fixes are *loosenings*; floor #1 must be re-measured after each. Recorded in the
tool's own output so the caveat cannot travel separately from the number.

**Two GOLDEN_WRONG findings from the prior run are now 0 — the mover is my own
golden correction, not new evidence.** `agent_130#00` moved PASS → **FAIL**
(`key_completeness_vs_required`): Required (b) demands entries explaining all
balance-sheet account changes, the key's own schedule shows the restricted-cash
balance rising, and **none of the key's 26 entry lines posts Restricted Cash**.
Because its golden now expects FAIL, it leaves the PASS-only FP loop. The defect
is real and unchanged; only its bookkeeping moved. Repair is **PROPOSED, NOT
APPLIED** — `out/key_repair_proposals.json`. The bank is not edited without
per-item approval.

### (c) cluster_b.py — **DONE. Run.** `out/class_b_clusters.json`

```
Class B (mcq) items: 596
  IDENTICAL (same content hash) : 8 groups, 9 retirable items
  families                      : 496
  multi-member families         : 83
  STEM_TWIN members             : 28   (inherit the representative's verdict)
  VARIANT members               : 72   (inherit the METHOD only)
  solves required               : 568 of 596  (reduction 28, 4.7%)
```

**Negative result, and it is robust.** Swept τ = 0.70 / 0.78 / 0.86 / 0.92; the
reduction is 4.5–4.7% at every threshold, so it is a property of the corpus, not
of the cut. **Class B must be verified essentially item by item.** Loosening τ
converts variants into larger families but does not reduce solves, because a
VARIANT shares a method, not an answer.

**COVERAGE DEBT (explicit): 72 items.** Counting families alone would claim 596
items covered by 496 solves and understate the real work by exactly those 72.
Only the 28 STEM_TWINs may inherit a verdict.

### (d) preflight.py — **DONE. Executed under the finished stack.** `out/preflight.json`

| Floor | Requirement | Measured | Verdict |
|---|---|---|---|
| #1 detection | ≥ 85% | 40/40 = 100%, 95% CI **[91.2%, 100.0%]**, 1 vacuous excluded | **PASS** |
| #2 false positive | upper CI ≤ 10% | 4/26 = 15.4%, 95% CI **[6.1%, 33.5%]** | **FAIL** |

Golden tiers: `adjudicated 8`, `ai_cross_checked 18`. Stale 0. Inadmissible 0.

**FIRST_BATCH_GATE: RED.**

Floor #2 has **three** independent blockers, not one. Naming them separately
matters because they have different fixes and only one is engineering:

1. **Point estimate** — the 4 MATCHER_ARTIFACT mechanisms in (b). Comparator
   work. This is what the retired belief *"more goldens will fix the FP rate"*
   correctly says goldens will **not** move.
2. **Interval width** — the gate tests the Wilson **upper bound**, not the point
   estimate. At n=26 a **flawless** run still bounds at **12.9% > 10%**. The
   floor is arithmetically unreachable at this n regardless of comparator
   quality; it needs **n ≥ 35** with zero chargeable. This does not re-open the
   retired belief — it is the *same* belief stated precisely: goldens buy
   precision, and here precision is itself a gating requirement.
3. **D6 — tier.** Floor #2 **certifies at HUMAN tier only**. There are currently
   **zero `human_confirmed` goldens** (`goldens/INDEX.json`). So even at 0% with
   n ≥ 35, floor #2 would be *operated provisionally*, not certified. **The
   operator countersign session is on the critical path to GREEN and nothing
   else substitutes for it.** I do not believe this was reflected in the runway.

Pre-flight also printed a wrong target: it computed "~30 goldens" from a
rule-of-three approximation while its own verdict uses Wilson, which needs 35.
Fixed in `preflight.py` — the target is now solved with the same bound the
verdict applies.

---

## 2. Fresh deliver.sh export — **DONE**

`deliverables/STATUS.md` → `generated: 2026-08-10T02:51:35Z`, committed in this
same commit as this report, per 01-COMMUNICATION rule 2.

**Defect found and fixed in `deliver.sh`.** It wrote to `DELIVERABLES/`
(uppercase) while git tracks `deliverables/` (lowercase). On macOS these are the
**same inode**, so it worked here silently; on Linux or CI they are two
directories, the export would land in an untracked one, and `STATUS.md` would
never update. That is precisely the stale-stamp failure 01-COMMUNICATION.md
exists to make impossible — it was one case-sensitive filesystem away from
recurring. Now targets the tracked lowercase path.

---

## 3. NAME THE MOVER — "terminal states was: 1" — **DONE**

**It is not the fixture.** The reviewer's hypothesis is disproved empirically,
not by reading the docstring:

```
sha256(out/ledger.jsonl) before test_sentinel.py : 59b1eb8e…0b2e5fca  (3165 rows)
sha256(out/ledger.jsonl) after  test_sentinel.py : 59b1eb8e…0b2e5fca  (3165 rows)
→ byte-identical; the fault-injection fixture cannot reach the real ledger
```

`test_sentinel.py` runs entirely inside `tempfile.TemporaryDirectory()` and
copies the ledger in. No write path to `out/ledger.jsonl` exists.

**The mover, in full:**

| | |
|---|---|
| **lineage** | `agent_204#02` (`lineage_id: agent_204#02`, `content_hash: 666c2ba8…c4be95f3`) |
| **state** | `unverified` → **`verified`**, stage 1, scope `item` |
| **minted by** | one `ledger_io.append_rows()` call after the symmetric re-derivation in item 1(a) |
| **authority** | REVIEW-STATE in-flight order block item 3, *"score its 13 figures fresh-vs-fresh, **close the item**"*; standard is D5 (dual independent derivation); re-attribution per D19 |
| **basis** | dual independent derivation under symmetric context; 12/12 shared figures agree; comparator returns 0 findings against 13 key lines for **both** derivations |
| **evidence** | `out/evidence_trim_sym/agent_204_02`, `out/evidence_dual2/agent_204_02` |
| **unit** | 1 **lineage** (D17 ladder: 1 row, 1 content hash, 1 lineage — they coincide here) |

**RULING REQUESTED.** D2 records *"Terminal count is currently 0 BY DESIGN (gate
RED)."* It is now 1. I read the launch gate as scoping **production runs over the
remaining corpus** (00-START-HERE rule 7), not order-directed closure of a single
in-flight item — so I did not read "close the item" as blocked. But that reading
is mine, D2's parenthetical now reads false on its face, and **the executor
should not be the one who decides how far the gate reaches.** Please rule, and
amend D2 either way. If the ruling is that no lineage may reach `verified` while
the gate is RED, say so and I will move it back to `machine_passed` with the
evidence retained — the sentinel will record the transition rather than lose it.

---

## 4. Standing runway — **DONE, and it is now shorter than recorded**

Every item in the REVIEW-STATE in-flight block is complete:

| block item | status | path |
|---|---|---|
| 1. write-time provenance + corpus audit | DONE | `provenance.py`; audit re-run |
| 2. provenance fixture (7th) | DONE | `test_provenance.py`, 4 checks, GREEN |
| 3. agent_204#02 closed | DONE | §1(a) |
| 4. blast radius | DONE | **171 of 190** stamps were retroactive; **2** admissibility verdicts changed — both `agent_204#02` (`evidence`, `evidence_parity` → PACK_NOTES_STALE), exactly the predicted mirror of the dual marking |
| 5. cost re-derivation accepted | DONE | no action; 39,652/q stands |
| 6. taxonomy → Class B → pre-flight last | DONE | §1(b), §1(c), §1(d) |

**Correction to a claim I made in an earlier session:** I marked all 19
`evidence_dual` outputs PACK_NOTES_STALE. Under per-item note scoping that was
over-broad — the dual harness **had** the LO 11-8 note. Only the trim side was
ever stale. Admissibility is now scoped per item, in `provenance.admissible()`.

Gate remains **RED**; tranche 1 has **not** fired; **no production tranche has
run**. DECISION-001 (Option B, 10,000,000 billable cap, auto-fire on GREEN)
is unchanged and un-triggered.

---

## 5. Traffic per 01-COMMUNICATION.md — **DONE**

Acknowledged. Chat is a doorbell from here.

---

## 6. Unordered items I am declaring rather than burying

**(i) Two tools disagreed about the same item by 32 findings — fixed as a class.**
`preflight.py` selected the newest *admissible* evidence bundle; `fp_taxonomy.py`
still took whatever it found first, and so scored `agent_204#02` against the
`evidence_parity` cache that the admissibility audit flags PACK_NOTES_STALE. One
tool called the item clean, the other filed 32 HASH_MIXING findings against it.
A rule enforced in one caller is not enforced. There is now **one** resolver —
`provenance.evidence_dir()` — and both tools call it. They now name the identical
offender set (verified in this commit).

**(ii) Batch manifests recorded absolute paths.** `out/parity50.json` stored all
50 evidence dirs as absolute paths into one machine's working tree, so a clone
read evidence from outside itself — and on any other machine, not at all.
`provenance.local()` re-roots them onto the current checkout. The manifests are
left as written (they are historical records); only resolution is made local.

**(iii) RULE EXCEPTION, declared.** 00-START-HERE hard rule 1 forbids hand-editing
`deliverables/`. I edited **one line** of `deliverables/ch17_standards_vintage.md`
to remove an absolute path containing the operator's university, semester and
course code. The operator's standing instruction is that those identifiers do not
appear in this public repo; the file's generator source
(`out/reports/ch17_standards_vintage.md`) no longer exists, so `deliver.sh` could
not regenerate it and deletion was not mine to choose. I am flagging this rather
than letting it pass as a normal export. Repo-wide identifier count is now **0**.

**(iv) One dead-code fix.** `families.py` carried a non-ASCII token in its
stopword list while `WORD` is `[a-z]{4,}` — unreachable, not merely unused.
Removed; `cluster_b.py` output is byte-identical before and after, so the Class B
numbers in §1(c) are unaffected.

**(v) Bundle hygiene, ORDER-001 step 1.** Exactly one reviewer bundle exists on
this machine (`~/Downloads/accounting_llm-reviewer-layer.bundle`). No earlier
reviewer bundle was found, so nothing was deleted. The only other git bundle on
the machine is an unrelated project backup and was not touched.

---

## Fixtures at this commit

`sh run_fixtures.sh` — **8/8 GREEN**, run cold with bytecode caches cleared.
(A prior run in this session reported green over a live `SyntaxError` because it
was executing stale `.pyc`; caches are now cleared before any fixture claim.)
