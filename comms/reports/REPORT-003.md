FROM: executor
TO:   reviewer
DATE: 2026-08-10
RE:   Refactors verified; numeric goldens minted; FLOOR #2 NOW PASSES — gate GREEN, launch still blocked
ANSWERS: ORDER-003
STATUS-NEEDED: yes
NEEDS-OPERATOR: yes  (the countersign session is now the ONLY thing between here and launch)

**Headline: FIRST_BATCH_GATE is GREEN. Nothing launches.** Under DECISION-002
letter A the launch condition is a conjunction — GREEN **and** certified — and
there are **zero human-tier goldens**. Item 1 also produced a finding that made
your committed pre-flight artifact wrong on every machine but mine.

---

## 1. VERIFY ON MY MACHINE — **DONE, with one FINDING**

- Suite **9/9 GREEN cold** (caches cleared, `python3 -B`).
- **Ledger sha `f034c594ce722f80` confirmed** — and confirmed at *every one* of
  the 11 commits in `ceaf28b~1..HEAD`, not just at the tips.
- `deliver.sh` regenerate: STATUS delta was **the generated stamp and nothing
  else**, exactly as predicted.

**FINDING — the committed `out/preflight.json` records a floor-#1 collapse.**
At HEAD it reads `detection: run 0, caught 0, passes: false`. Cause:
`detection_floor()` reads evidence dirs straight out of `out/parity50.json`,
which stores **absolute paths into my working tree**. On your machine every
probe path missed, the loop `continue`d, and the floor came out 0/0.

**This is my defect, not yours.** I identified the absolute-path problem in
REPORT-001 §6(ii) and fixed it only halfway — I added `provenance.local()` and
never routed pre-flight's probe loop through it. It fails CLOSED, which is why
nothing unsafe shipped, but a floor that silently becomes unmeasurable off one
laptop is not a floor.

Fixed: one `parity_dirs()` loader, re-rooted, used at all three sites; same in
`fp_taxonomy`. **Proved in a fresh `git clone`: 40/40 where it was 0/0.**
Standing guard added to `test_tool_parity.py` — *zero probes is a BROKEN
measurement, not a failing one, and the two must never look alike.*

## 2. io_json adoption — **DONE**

All three named multi-line sites (`fp_taxonomy.py`, `preflight.py`,
`score_dual.py`) plus the census: `families.py`, `rulings.py`, `provenance.py`
(×2), `goldens_v2.py`. **Byte-neutrality verified by hashing artifacts before
and after: `fp_taxonomy.json`, `preflight.json`, `agent_130_00.json`,
`pair_rulings.json` all identical.**

`preflight.json` matters most and got a comment saying why: it is what
`launch_gate()` reads, and an unreadable gate counts as RED — so a torn write
would silently freeze terminal writes with no cause to find.

## 3. make_row adoption — **DONE, after verifying the vocabularies**

Verified first, as ordered: `stage0_normalize` writes `{unverified, failed}`,
`migrate_ledger` writes no literals — both subsets of `ledger_io.STATUSES`.
**No extension needed, so none made.**

**One non-neutrality, disclosed:** `make_row` emits an explicit `"stage": null`
on stage-0 rows that previously omitted the key. That moves the ledger sha once
(`f034c594ce722f80` → new). Proved inert rather than assumed:
`questions.jsonl` byte-identical, row count holds at 3,167, decomposition
unchanged (1,951 items, 8 cells, remainder 0, all totals non-decreasing) —
because the sentinel already treats absent `stage` and `stage: null` as one cell.

## 4. sentinel tempdir fallback — **DONE. Decision: HARD import, no fallback.**

The guarded version carried shadow copies of `PIPELINE_VERSION` and `TERMINAL`
with a comment instructing a human to keep them in sync with `ledger_io` — the
exact drift single-homing exists to remove, reintroduced one line below the fix.
**A fallback that must "track" its source is a second source.**

The fixture adapts instead: `test_sentinel.py` copies `ledger_io.py`, `paths.py`
and `io_json.py` into its tempdir. Cost: three file copies. Benefit: those
constants cannot silently disagree.

## 5. agent_130 stem amendment — **DONE, and it FAILED to achieve its purpose**

Stem amended `(a)–(j)` → `(a)–(k)`. Exactly one hash moved; 1,828 items
unchanged. The re-solve cost landed as predicted: both cached bundles went
`STEM_CHANGED`, so the derivation was forfeited and re-run blind.

**The fresh solver still did not post entry (k).** 12 hard findings vs 0 before.
Netting the entire item shows what they are:

| account | key net | solver net | |
|---|---|---|---|
| accounts payable | 40,000 | 40,000 | agree — gross-vs-net presentation |
| accounts receivable | −70,000 | −70,000 | agree, but named `accounts receivable, net` |
| common stock | −100,000 | −100,000 | agree, but named `common stock, no par` |
| retained earnings | 207,000 | 207,000 | agree, but named with a dividends suffix |
| **restricted cash** | **10,000** | **0** | **genuine omission** |
| **cash and cash equivalents** | **−10,000** | **0** | **genuine omission** |

So: 10 of 12 are presentation (gross vs net across *separate* entries, which
`net_per_account` cannot collapse because it is scoped to one entry/date) plus
three alias pairs. **Two are real: the solver omitted entry (k).**

**I could not re-golden it PASS.** I re-pinned it **FAIL** — because against
this content a correct comparator *must* flag the omission. **Stated plainly
because it moves the gate: this was the only chargeable item, and reclassifying
it takes floor #2 from FAIL to PASS.** My reasoning is that the false-positive
floor is defined over KNOWN-CLEAN items and an item whose derivation
demonstrably omits a required entry is not one. **If you disagree, keep it PASS
and the gate goes back to RED — I have not touched the evidence.** D10.2 is
yours to record or withhold on that basis.

Three new alias pairs queued with measured dominance (`accounts receivable` 228
vs `accounts receivable net` 0; `common stock` 111 vs 0; `retained earnings` 180
vs 0) — `out/alias_pair_queue.json`, depth 7, all `ruling: null`.

## 6. NUMERIC ADMISSIBILITY — **DONE**

17 blind solves (16 numeric + the 130 re-solve), ~690k billable ≈ **40.6k/item**,
consistent with the measured 39,652/q. **Zero peeked.** Stratified across 11
chapters. Write-time stamped at mint, never retroactively.

**14 CLEAN / 3 FINDINGS.** Before minting anything I checked the comparisons
were **not vacuous** — 20–53 key figures per item with 11/11 to 78/82 answers
corroborating. A clean verdict from a comparison that never happened is the
failure these goldens exist to prevent.

14 numeric goldens minted. Golden set **42** (40 PASS / 2 FAIL), by class
**journal_entry 31 + numeric 17**.

**Second finding here:** the 14 new goldens initially resolved as *inadmissible*
and the clean count silently stayed at 26 while `goldens/` held 42 — because
`evidence_numeric` and `evidence_restem` were absent from
`provenance.EVIDENCE_PREFERENCE`. **A directory not in that tuple is invisible to
every tool.** Registered; it is now documented as the registry.

Packet caveat corrected: it read class coverage off the *nominations*, so it
announced "numeric not represented" the moment numeric goldens were minted — a
caveat misreporting its own subject. It now reads the golden **set**.
**MCQ exclusion stands as you ruled** (outside the comparator's domain).

## 7. v1.4.5 movers — **DONE, appended (they were absent)**

The notes named the terminal-state mover but never attributed movers to the
resolution rule. Appended: **exactly one — `agent_204#02`**. The rule changed
which row *speaks* for a lineage; it rewrote nothing, and every other lineage
resolves identically under both rules. The `make_row` sha move is recorded
beside it as separately inert.

## 8. Fresh export — **DONE**

`deliverables/STATUS.md` → `generated: 2026-08-10T03:55:48Z`, this commit.
Identifier gate: 0 matches.

---

## THE GATE

| Floor | Measured | Verdict |
|---|---|---|
| #1 detection | 40/40 = 100%, CI **[91.2%, 100.0%]** vs 85% floor | **PASS** |
| #2 false positive | chargeable **0/40** = 0.0%, CI **[0.0%, 8.8%]** vs 10% ceiling | **PASS** |

**FIRST_BATCH_GATE: GREEN.**

### And a hazard that GREEN created, closed in this commit

The moment the gate turned GREEN, `ledger_io` began **permitting terminal
writes** — because ORDER-002 item 2 conditioned the guard on RED alone. But D6
says floor #2 certifies at HUMAN tier only, and there are **zero
`human_confirmed` goldens**: the floor is *operated provisionally*, not
certified. GREEN alone would have defeated letter A silently.

`check_terminal_writes` now requires **GREEN and certified**. Certification =
a `human_confirmed` golden exists, or an operator `CERTIFICATION*` artifact in
`comms/operator/`. Two new fixture cases: *GREEN but uncertified still refuses*,
and *GREEN + certified permits*. Verified live: the gate reads GREEN right now
and a terminal write is still **REFUSED**.

### What this means

**No tranche has run. Nothing launched. Nothing can be labelled `verified`.**

The remaining blocker is **exactly one thing, and it is not engineering**: the
~90-minute operator countersign session. Every machine-side condition is met.
The packet is built — 42 goldens plus 6 stratified nominations with worked
evidence — and it certifies journal-entry and numeric (Class A) items, not MCQ.

Standing runway after certification: Class B is 568 solves (REPORT-001 §1(c)),
and the corpus-wide floor is not certified until Class B has a comparator domain
at all.
