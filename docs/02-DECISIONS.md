# 02-DECISIONS.md — settled rulings ledger
Every entry is STANDING law unless a later entry supersedes it by citing
it. Reopening any ruling requires citing its ID and presenting NEW
evidence. Evidence details: deliverables/, reviewer/, docs/04-04-items-casebook.md.

- **D1 Authority**: `textbook_then_gaap`. The edition (Hanlon 4e) governs;
  current GAAP fills silence; divergences flag `conflict`, never fail.
- **D2 Two terminal states only**: `verified` | `needs_human`;
  `machine_passed` is progress, not completion. **D2.1 (ORDER-002):**
  terminal transitions are GATE-CHECKED IN THE WRITE PATH — ledger_io
  refuses them while the launch gate is RED absent an explicit operator
  override file; enforcement-probed. The one pre-ruling terminal
  (agent_204#02) was reverted with evidence retained. Investigation
  closure ("close the item") = machine_passed + casebook CLOSED, never
  a terminal label.
- **D3 Corroboration rate RETIRED as a quality signal**. Detection =
  coverage × adjudication; report (coverage, candidates, adjudicated-
  findings) triples. Baseline's higher corroboration was under-reporting.
- **D4 Trim-1 adopted** as production harness (parity passed: zero
  unadjudicated flips, canaries clean, coverage ≥ incumbent). Measured
  cost 39,652 billable/q — CHEAPER than baseline (50,091).
- **D5 Dual independent derivation is the standard** for key-silent
  required figures; runs BY DEFAULT; no-counterpart figures stay
  unverified, never default-pass.
- **D6 Floor #2 certifies at HUMAN tier only**; ai_cross_checked goldens
  operate it provisionally. The 26.9% reading is STALE (see RETIRED).
- **D7 ch17 vintage**: pure ASC 842. Round-then-carry vs carry-then-plug
  inside schedules are BOTH blessed conventions, not errors. A ch17 stem
  lacking a stated rounding convention is a QUESTION defect (stem
  clarification, zero budget). Accrued finance interest credits Lease
  Liability; amortization credits ROU directly. Lessor LOs + LO 17-11
  out of course scope.
- **D8 ch17 amendment (GOLDEN_WRONG class born)**: agent_283's key had a
  REAL $1 defect ($279,286 vs correctly-rounded $279,287) — repaired at
  source. A floor-#2 "failure" can be the comparator being right.
- **D9 LO 11-8 donated assets**: the edition NETS incidental costs
  (Demo 11-8: 495,000). Capitalizing is the known wrong path. Trim's
  divergence was a CONTEXT DEFICIT (it was never given the note), not
  evidence trim reasons worse — the original "solver-quality finding"
  attribution is formally RETRACTED (see D19).
- **D10 agent_130**: KEY_REPAIR (T-account credit total 2,835,000;
  misplaced balancing line) — repaired at source; two independent
  checkers converged on the same figure. Its two 10,000.0 trim lines =
  KEY_SILENT (restricted-cash transfer the key mentions in prose but
  never journalizes). Not solver error. **D10.1 (REPORT-001):** upgraded —
  the key is INCOMPLETE against its own Required (b) (restricted-cash
  balance rises; no key line posts Restricted Cash); KEY_REPAIR approved
  per-item in ORDER-002 item 3.
- **D11 agent_303**: STEM_AMBIGUOUS (refund-liability identity supports
  ≥3 readings). Fix class: stem clarification.
- **D12 agent_283 "total lease expense"**: CONSTRUAL — 360,000 (total
  payments) is correct by the convergence identity (full-term operating
  expense ≡ total payments); 80,713 is the interest sub-component,
  model-mismatched (operating leases have no separate interest expense
  line). Stem stands.
- **D13 FORMAT_DRIFT**: all 7 paused packs CLEARED (benign low overlap;
  parse 1.00). Drift tests one-sided with absolute bands where only one
  direction means anything. Every gate carries an enforcement probe —
  the original pause never actually gated.
- **D14 Duplicates**: 8 byte-identical groups → 8 canonical + 9 retired
  DUPLICATE_OF (lineages preserved); coverage counts groups once.
- **D15 Alias/pair rulings (seed yields to measured dominance)**:
  Note Payable over Notes Payable (612:82 textbook, 173-corpus);
  Building over Buildings (corpus plural count: ZERO); Income Tax
  Payable over the seed's Income Taxes Payable. Unrealized G/L:
  family-level 'Holding' equivalence WITHIN a destination; —Income vs
  —OCI are merge barriers, never conflated. R&D = "Research and
  Development Expense" (the shorthand never existed in the corpus).
  APIC security-unqualified forms (bare, Additional PIC, Share Premium)
  fold to —Common Stock ONLY context-conditionally (preferred context
  suspends and flags); measured exposure today: zero.
- **D16 Notations** ("X (or Y)") are NOT accounts: NOTATION class,
  routed to acceptable-form handling, never alias canonicals.
- **D17 Unit ladder**: rows (forensics) < content hashes (versions) <
  LINEAGES (reporting unit; 1,828 = 1,819 active + 9 retired). Bytes-
  unchanged re-keys carry ALL states forward.
- **D18 Provenance**: captured at write time, immutable; retroactive
  stamping is banned (it launders staleness); history re-stamps only by
  labeled reconstruction. Key-only repair ⇒ free re-compare; stem or
  pack-notes change ⇒ re-solve. Comparison symmetry: staleness
  evaluates EVERY input before scoring.
- **D19 Re-attribution discipline**: when a comparison is found
  contaminated, its author proactively re-attributes every conclusion
  that leaned on it. Executed once (agent_204, self-retracted).
- **D20 Budget**: Option B recorded — tranche 1 = 10,000,000 billable
  hard cap (harness meter authoritative), ≈182 questions; launch fires
  AUTOMATICALLY on pre-flight GREEN; FIRST_BATCH_GATE report-and-
  continue; human decisions at tranche boundaries only.
- **D20.1 (operator letter A, comms/operator/DECISION-002-certify-first.md):**
  the launch trigger is now a CONJUNCTION — pre-flight GREEN **and**
  countersign session complete. An agent seeing GREEN alone does not
  launch. D20's budget terms stand unchanged. The executor's rewrite of
  the auto-fire text inside the decision file (so stale readers cannot
  misfire) is the correct pattern for amended triggers.
- **D22 State resolution rule (REPORT-002, shipped as v1.4.5):** in the
  append-only ledger, an item's current state = the row at the HIGHEST
  stage, latest-wins within that stage. Replaces two failed rules
  (latest-row-wins hid verdicts behind stage-0 rows; terminal-outranks
  made reverts impossible). Movers audited: the ORDER-002 204 revert.
- **D10.2 (ORDER-004):** 130's key repair DONE; stem amended (a)-(k); the
  fresh blind solver STILL omitted entry (k), so the golden is re-pinned
  **expects-FAIL** — correct, because the comparator must flag a real
  omission. Production remedy = a treatment note (zero-net intra-pool
  transfers ARE journalized when a required part demands entries for all
  BS changes), queued for tranche-1 prep.
- **D23 Floor-over-known-clean (ORDER-004):** the false-positive floor is
  defined over KNOWN-CLEAN items only. An item whose derivation
  demonstrably omits required content exits the clean set; charging the
  comparator for flagging it would punish correctness. Ratified with
  independent verification: omission arithmetic re-derived and both
  floors re-measured on the reviewer's machine (40/40; 0 chargeable,
  CI [0, 8.8%]) — the GREEN stands on merits, not convenience.
- **D15.1 (ORDER-004):** three pairs approved under dominance (base 228/
  111/180 vs suffixed 0): `accounts receivable`, `common stock`,
  `retained earnings` canonical; the suffixed forms alias in.
- **D21 Continuous release** (operator's order, 2026-08-10): every spec
  change publishes immediately as the next patch version; releases are
  append-only under skill/releases/; see docs/08-08-RELEASING.md.
