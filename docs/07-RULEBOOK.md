# RULEBOOK (formerly v1.4-fold-queue.md) — every rule + the incident that taught it

# v1.4 Fold-Queue — every spec delta since v1.3, prompt-ready

RELEASE TYPE: **spec catch-up**. Everything below is ALREADY RUNNING in the
production stack (comparator v3.6, goldens v2, meter fixture, dual-derivation
standard). v1.4 documents practice; it does not change behavior — therefore
the v1.4 version bump MUST NOT invalidate verdicts or the ledger. Reserve
invalidation for behavior-change releases.

Each entry: the rule as it should read in the prompts, then [origin].

## Correctness & verification standards

- **Dual-independent-derivation standard.** A figure the key does not state
  and that does not derive from the key's stated components (same
  method/date context only) is verified by a SECOND blind solver agreeing —
  state `verified_by_derivation`. Solver-vs-key applies only where the key
  speaks. A key-silent figure with no second-derivation counterpart stays
  unverified — never default-pass. [26-point coverage-vs-corroboration
  spread; 63-vs-7 key-silent figure split]
- **Detection = coverage × adjudication.** Coverage generates candidates;
  adjudication converts candidates into findings; under-reporting generates
  silence. Corroboration rate is RETIRED as a quality signal; report
  (coverage, candidates, adjudicated-findings) triples. No single pass-rate
  headline until the instrument stack is frozen. [baseline 40/50 "winning"
  for six hours while surfacing 0 of 3 genuine findings]
- **Authority rulings produce three zero-budget fix classes**: KEY_REPAIR
  (fix the key at the SOURCE PACK so it survives re-normalization),
  stem clarification (STEM_AMBIGUOUS), and pack treatment note. Repair-not-
  remake extends to KEYS: never regenerate a sound question to fix key
  formatting. [agent_130 T-account; agent_303 refund identity; agent_204
  netting]
- **Pack treatment notes reach SOLVER context, patch-before-run**: a ruling
  that changes treatment gates the affected family until the note (with
  authority citation and a worked wrong-path example) is live in the harness
  that will run them. [LO 11-8: 12 of 13 items gated; dual solver carrying
  the note independently contradicted the erring solver]

## Comparator specification (v3.4 → v3.6 accumulated)

- Number extraction must read LaTeX money (\mathbf{\$18{,}000}) and any
  notation the keys use — probe with notation goldens. [60.6% of keys
  invisible]
- **Precision-inherited tolerance**: corroborate each figure at the key's
  displayed precision (whole-dollar key ⇒ half-dollar equivalence; cents ⇒
  cents); per-share/per-unit figures exact to their instructed rounding.
  No blanket money tolerance in either direction. [hidden ±$1 blanket;
  33 surfaced cent-level mismatches, 16 dissolved by inheritance]
- **Rounding-convention equivalence scopes by CONTEXT** (any carrying-amount
  rollforward / effective-interest schedule), never by chapter. [SCHEDULE_CTX
  regex missed the two items the ruling came from]
- **Aggregation equivalence** (JE_AGGREGATED): pooled entry vs per-item
  split of the same ledger matches. [Investments–AFS 150,000 vs 90,000+60,000]
- **Prose-null ↔ 0**: "no entry / none / not required" corroborates 0 for
  count- and amount-labeled parts. [items 17/18; 8.4% of corpus]
- **Percent ↔ fraction normalization** before diffing. [0.72 vs 72%]
- **KEY_SILENT_SUSPECTED is deterministic** (subset-sum over the key's own
  stated figures) — never order- or reporting-volume-dependent. [downgrade
  rule that manufactured flips]
- Verdicts score on the PRODUCTION OUTCOME ("would this have blocked
  machine_passed / reached adjudication"), never on internal signal counts.
  [side-flip probes scored on the wrong layer]
- **One canonicalization library**, imported by comparator, dual scorer, and
  probe generator. No scorer reimplements comparison. [three scorers
  rediscovering the same equivalence classes]
- comparator_version AND harness_version stamped in every evidence bundle;
  no pooling across harness versions without a passed parity test on record.

## Harness-change (parity) protocol

- Any harness change requires an n≥50, chapter-stratified parity test scored
  under the CURRENT comparator. Anchor = the stem's Required parts
  (required-figure coverage), never "match the incumbent" — incumbent
  behavior was never validated either. Every verdict flip is adjudicated to
  whichever side was right. Criteria in rank order: zero unadjudicated
  flips; canary-clean; coverage ≥ incumbent. Cost ratio is informational,
  never a criterion. [trim flip agent_052: the "extra" figures were required;
  baseline was the under-reporter]

## Calibration layer v2

- **Probes are symmetric and end-to-end**: inject at RAW key text, traverse
  Stage 0 → extraction → comparison. Two populations — mutants must FAIL,
  goldens must PASS. Two floors, both with 95% bounds: detection ≥
  PROBE_DET_FLOOR and false-positive ≤ PROBE_FP_CEILING. Floors clear
  statistically only (rule of three; ≥ PROBE_MIN_FALSIFIABLE falsifiable
  probes) and RE-CLEAR under the exact production stack after any
  comparator/harness change. [probes read 40/40 straight through three
  comparator defects — they never saw extraction, and had no false-positive
  side at all]
- **Golden provenance tiers**: human_confirmed > ai_cross_checked >
  adjudicated. Floor #2 may be MEASURED provisionally at ai tier; it is
  CERTIFIED only at human tier — another AI checker is a member of the class
  whose reliability is the open question. [the agent's own block, concurred]
- **Goldens are truth-versioned**: truth_as_of_hash + truth_as_of_bytes; a
  golden whose content moved downgrades to STALE, never reports a phantom
  defect. [agent_130 scored post-repair against pre-repair truth]
- **Regression-golden rule**: the motivating items of every ruling become
  permanent probe goldens for the rule that encodes it. [the rounding rule
  missing agent_283/151 — its own motivating items]
- Wrong-key canaries re-run after ANY prompt/harness restructuring —
  surgery is when blindness breaks. [standing; re-verified at trim adoption]

## Meters

- Meters get probes like checkers: a known-usage calibration fixture runs
  through every counting path each session; fixture-scope disagreement
  beyond tolerance halts COST REPORTING (production meter-vs-meter gaps are
  logged and bounded, never halted on). Authority rule: harness figure
  authoritative for cost; transcript parser for structure. Dedupe usage
  records by message id — final record per call only. **Physics bound**:
  billable output tokens per elapsed second must sit inside model throughput
  at the run's concurrency, or the meter halts. [three parser artifacts;
  the 2.4× phantom correction; 18.8-calls figure failing wall-clock physics]

## Ledger & state integrity

- Stage 0 MERGES the ledger; it never truncates. ("w"-mode is forbidden.)
  [three silent zeroings in one night]
- **Ledger sentinel**: terminal-state count is monotonically non-decreasing
  at fixed PIPELINE_VERSION absent explicit invalidation; any decrease halts
  and alerts, checked at every session start.
- **Evidence bundles are the source of truth; the ledger is an index.**
  Every verdict must be reconstructable from bundles alone. [99% recovery
  after the zeroing — the property that saved the night]
- Content hash covers the WHOLE key (any change ⇒ new hash), plus a
  bytes_hash for mechanical change detection. Hash-FUNCTION changes require
  an old→new migration carrying terminal states where bytes are unchanged.
  [key repair invisible to a JE-lines-only hash; 99% cache survival via
  migration]

## Adjudication protocol

- **Cohorts before individuals**: chapter/standard cohorts get one
  investigation with artifacts (vintage note, templates, patch-or-ruling);
  numeric mismatches get a delta histogram (unit-scale, rounding, precision
  classes) before any item-level work; failures adjudicate GROUPED BY
  full-corpus family with 2–3 sibling solves before any is treated as a
  one-off. [ch17 six-for-one; 25-"families" sampling artifact]
- Nearest-neighbor / heuristic matches are proxies — validate against
  measured data before use, and count ambiguous cases AGAINST the flattering
  reading. [92,930.84→930.84; the discarded 2.0% key-silent heuristic]
- Two-pass disagreements (item ruling vs synthesis override) are recorded
  as dissent in the bundle; overrides earn permanence only as SCOPED rules.
  [ch17 rounding override]

## Reporting & process

- **Pre-registration rule**: a prediction registers with its metric AND
  threshold, or it is not registered. [the invented ≤12 "PREDICTION FAILS"
  line]
- Significance-test the metric that MOVED, not just the headline
  (composition shifts, failure-mix chi-square); batch comparisons state the
  sampling design (cluster vs stratified) before any pooling. [p=0.29
  pass-rate vs p≈3e-6 composition; one-per-pack cluster sampling]
- "Nothing changed" claims are verified mechanically (config/prompt/model
  hashes), never asserted. [the schema field that did change]
- Duplicate policy: byte-identical groups keep one canonical, rest retire
  DUPLICATE_OF (lineages preserved); coverage counts groups once;
  near-duplicate scan runs via family similarity on top. [8 groups /
  17 items]
- Sampling: chapter-stratified, unsampled chapters first, deliberate
  within-pack replication where cohort analysis needs it.

## New states, classes, params since v1.3

- States: verified_by_derivation; golden STALE.
- Classes: KEY_REPAIR, STEM_AMBIGUOUS, DUPLICATE_OF, JE_AGGREGATED,
  KEY_SILENT_SUSPECTED (deterministic), SIDE_MISMATCH.
- Params: PROBE_FP_CEILING now floor-#2-bearing with tiered certification;
  golden tier field; bytes_hash.

## Added after canon.py unification

- **Refactor-neutrality rule**: capture current outputs BEFORE any change
  labeled a refactor; the change must reproduce verdicts exactly, and any
  movement is a bug until root-caused. [canon unification moved 84/16 →
  87/13 via a carried-over rescale block — a wrong→verified loosening that
  only the neutrality check could see]
- **Declared scale only**: magnitude rescaling (thousands/millions)
  corroborates only when the key DECLARES a unit header ("$ in thousands");
  inferred-scale matching is banned. [solver 900 corroborated against key
  0.9 — three orders of magnitude apart]
- **Pairing guards**: the figure matcher never pairs a nonzero figure
  against a zero counterpart in either direction; unpairable figures route
  to unverified, never into the findings count and never default-passed.
  [agent_283's two phantom disagreements]
- **Order blocks are self-contained**: any instruction relayed between
  operators must carry everything it references — no pointers to prose
  outside the block. [the ~65M budget figure that never reached the agent]

## Added after the label grammar and key repairs

- **Provenance-scoped artifact caching**: solver outputs are functions of
  the STEM (solvers never see keys) — they cache against stem_hash +
  harness_version + pack_notes_version and are NEVER invalidated by
  key-only repairs. Verdicts bind to the whole-content hash + canon/
  comparator versions. Key repair ⇒ free re-comparison from cached
  outputs; stem repair ⇒ re-solve. [HASH_MIXING going live on
  agent_130/283 after their key repairs]
- **Semantic gates, positional penalties**: in label matching, dimensions
  of the quantity itself (period, date, cumulative-vs-periodic)
  DISQUALIFY on mismatch; positional context (part letter) only
  penalizes — adjudication established the same quantity can appear
  under two parts. [the NBV case re-broken by an over-strict part gate]
- **Fixture-first for matchers**: matcher changes prove out against the
  pairing fixture (which encodes adjudicated pairings) before deployment,
  so over-corrections fail on first run instead of in production.

## Added after the 0-of-2 prediction failure

- **Completeness claims are enumerations**: "X is unified / complete" ships
  with the enumerated list of sites it covers, verified mechanically — a
  comparison-site audit plus a lint/fixture assertion so new comparison
  sites fail loudly. An asserted "one shared library" missed the JE
  structural path entirely. [279,286.65 corroborating as a scalar and
  failing as a journal line, same item]
- **One arithmetic-equivalence authority**: every numeric comparison in
  the stack routes through canon. Structural pairing (date, account,
  dr/cr side) stays a hard gate; AMOUNT equivalence is canon's alone,
  with precision inheritance and schedule-context conventions. Balance
  invariants are checked INTRA-source, exact in each source's own
  arithmetic — never across sources, which is what made "tolerance breaks
  balancing" a false objection.
- **Precondition checks before invoking a policy**: verify the premise the
  policy depends on before applying it. [stems checked for repaired
  tokens before trusting key-repair ⇒ free-re-compare]
- **Failed predictions are yield, not embarrassment**: a pre-registered
  0-of-2 surfaced the incomplete unification faster than any audit would
  have. A prediction ledger where everything passes is itself a red flag.

## Added after the wiring dump and FORMAT_DRIFT audit

- **Wire generators, not emissions**: any per-run generated script inherits
  only what its builder emits — patches to emitted files evaporate on the
  next generation. Pack context (treatment notes, conventions) lands in
  the BUILDER/template. [LO 11-8 note absent from trim-1 while "confirmed
  on the wire"; the two grep hits were the stem, not the rule]
- **Wiring probes**: every gated treatment note gets a fixture asserting
  its rule string appears in a FRESHLY GENERATED solver context for the
  affected family, anchored to the instructions region (never satisfied
  by question text). Runs each session.
- **Enforcement probes**: any pause/gate mechanism gets a fixture proving
  it actually blocks — a deliberately gated item must be REFUSED by the
  scheduler. A pause that doesn't pause is worse than no pause, because
  it manufactures false confidence. [FORMAT_DRIFT pause never consulted
  by the dispatcher; two paused-pack items ran anyway]
- **One-sided drift metrics**: deviation tests use one-sided bands where
  only one direction is meaningful (low stem↔solution overlap is fine;
  only high overlap means leakage) and absolute bands for bounded
  signals. [all 7 pack pauses fired on benign low overlap]
- **Net-per-account scoping**: within one entry/date, when the SAME
  account appears on both dr and cr, collapse to the net line before
  diffing (the textbook's own two-part operating form demands it);
  entries without a same-account pair keep SIDE_MISMATCH as a hard gate,
  so netting can never launder a genuine side error. [Demo 17-3 probe
  failing: dr 3,251 + cr 34,972 vs net cr 31,721]
- **Order text uses exact artifact strings**: reviewer orders quote
  account names, labels, and figures verbatim from the artifacts —
  shorthand creates phantom rulings. ["R&D Expense" never existed in the
  corpus; the harvest row was "Research and Development Expense"]

## Added after the alias closure

- **Semantically load-bearing suffixes are merge barriers**: account
  suffixes that carry accounting meaning (—Income vs —OCI destinations,
  par denominations) can never merge across values; equivalence rulings
  apply only WITHIN an identical suffix. [27 Unrealized-G/L spellings:
  'Holding' equivalent within a destination, destinations never conflate
  — a naive merge would have folded income-statement and OCI accounts]
- **Dominance rule for both-forms usage**: when the textbook uses two
  forms of one account, balanced usage ⇒ equivalence pair; dominant
  usage (≳3:1, measured, both overall and in journal-entry position) ⇒
  the dominant form is canonical and the other aliases to it. [Note
  Payable 612:82 over Notes Payable]
- **Notations never enter the account alias table**: acceptable-alternate
  hedges ("Retained Earnings (or Dividends)") are notations, not
  accounts; their case-normalization lives in the acceptable-form
  handler, and the tokenizer classifies them NOTATION so they pollute
  neither the chart nor the UNKNOWN_ACCOUNT count. [notation rows
  applied as alias canonicals in the same record that disclaimed them]

## Added after the alias corrections round

- **Exports regenerate and timestamp at send**: every generated state file
  (STATUS, stage0) carries a `generated:` UTC timestamp and is re-emitted
  at export time. [STATUS.md byte-identical stale across two batches while
  stage0.md moved in the same export — an artifact claiming "generated
  from live artifacts" while lagging them, with no way to see it]
- **Units on adjacent metrics**: when two metrics with different units sit
  side by side, the units are stated. [129 NOTATION *lines* against a −13
  *items* drop in UNKNOWN_ACCOUNT reads as a contradiction until the
  item-vs-line distinction is made explicit]
- **Unqualified forms resolve context-conditionally, never by
  unconditional fold**: an account form omitting a semantically
  load-bearing qualifier (security class, destination) is resolved per
  entry context — default to the dominant qualified form, suspend and
  flag when context signals the other class. Extends the suffix-barrier
  rule to the ABSENCE of the suffix. [Additional Paid-in Capital and
  Share Premium folded unconditionally to —Common Stock in the same
  document that ruled the bare excess-of-par form context-dependent]

## Added after the APIC guard and STATUS regeneration

- **Regeneration tests assert a content canary, not just a hash change**:
  two exports hashing differently proves re-emission (the timestamp
  moved), not that content tracks the artifacts. The proof is a known
  previously-stale fact flipping — the LO 11-8 line reading LIFTED did
  what the hash test could not.
- **One-off verifications graduate to fixtures**: any behavior verified
  "across N cases" folds those cases into the standing fixture suite as
  regression goldens (the five APIC guard cases, both suspend paths
  included), or the verification evaporates on the next edit.
- **Flag-level metrics disclose their line-level scale**: an item-counted
  flag reads as small when the line-level reality is large —
  UNKNOWN_ACCOUNT 925 items is 5,036 lines. Both numbers, both units,
  every report.

## Added after the fixture consolidation

- **Comparison sites are declared, not detected**: value comparisons can
  hide inside structures no pattern-lint can see (Counter equality held
  the ms() comparison). New comparison sites register at creation;
  comparison_sites.md is the register; CI asserts every value-comparing
  module either imports canon or appears in the register with written
  justification. The lint catches patterns; the register catches
  architecture.
- **Sentinel deltas carry attribution in both directions**: monotonicity
  guards the floor, not the ceiling. Any large terminal-count change —
  including increases — decomposes by state and causing event.
  "Non-decreasing" is necessary, never sufficient. [338 → 671 under a
  RED gate, presented as a pass without explanation]
- **Register arithmetic ties**: an enumeration artifact's headline counts
  partition exactly (N = routed + justified + retired, disjoint) or the
  register fails its own purpose. [8 sites vs 7 + 4]

## Added after the sentinel decomposition

- **Watchdogs are tested against the loss they exist to catch**: sentinels
  get fault-injection fixtures — a synthetically deleted terminal row must
  TRIP the sentinel, and a deleted progress-state row must NOT (the
  definition test). A watchdog blind to its own purpose is worse than
  none: this one would have sat green through the cache-zeroing it was
  built for, because progress rows masked the loss.
- **Progress and completion are separate ledgers**: STATUS carries a
  pipeline funnel (distinct items × stage-state × scope) so real progress
  is visible without corrupting the terminal metric. Zero terminal and
  513 rows of Stage 1 progress are both true; conflating them was the
  defect.
- **Decompositions partition exactly or carry an explicit remainder line**
  — including the decomposition that corrects a partition failure.
  [2,710 table vs 2,765 headline, inside the sentinel correction itself]
- **Corrected instruments derive their old readings**: a fixed meter or
  sentinel reproduces its prior wrong values from the same data under
  the broken formula, or a further defect is still hiding. [338 and 671
  not yet derived from the row table]
- **Seeds yield to measured dominance**: seed chart entries are
  hypotheses, not law — when corpus usage dominates a seed variant
  (Building vs Buildings, Income Tax vs Taxes Payable), the pair ruling
  can update the SEED, with the losing form aliasing in.

## Added after the fourth defect

- **Twice is a class**: the second occurrence of a defect pattern converts
  the fix from instance to architecture. State stores get ONE write API
  (merge-only); direct file opens on the store are banned by lint AND
  asserted absent by fixture — the write-path equivalent of canon being
  the one comparison authority. [the "w"-mode truncation fixed in
  stage0_normalize.py, then found alive in migrate_ledger.py, having
  destroyed 171 rows]
- **Fixtures synthesize their preconditions**: a fault-injection test
  gated on naturally occurring state never runs when it matters most —
  inject the terminal row, then delete it. [the sentinel's delete-test
  could never have run against a zero-terminal corpus, which is exactly
  how it stayed green for its entire life]
- **The unit ladder — rows < hashes < lineages**: every metric declares
  its rung. Rows are forensic history; hashes are content versions;
  LINEAGES are the questions. Funnels and progress reports speak
  lineages (state at current hash), and mechanical re-keys with bytes
  unchanged carry ALL states forward, not just terminals — otherwise
  real progress reads as zero, the mirror image of the original
  inflation. [1,950 "distinct items" = distinct hashes; the corpus has
  1,828 lineages, and the pilot's Stage 1 progress vanished from the
  item view]

## Added at the close of the sentinel saga

- **Stage rows are evidence that work happened — no writer may discard
  them**: the ledger write API's core invariant, stated as law. Losing a
  stage row is the failure the module exists to prevent, regardless of
  which script is writing.
- **Single-writer guarantees are fixture-asserted, not lint-asserted
  alone**: lint catches the pattern (open on a literal path); the fixture
  catches evasion (variable paths, new scripts) — an attempted direct
  write in a test copy must be refused or detected.
- **One-unit deltas between adjacent tables carry their labels**: four
  defects this session hid inside small unexplained increments (the +11,
  the +35, the −171, the 84→85). A number that moves by one between two
  reports names its mover.

## Added after the write-path fixture

- **Guard the invariant, not the instance**: under merge-only semantics
  every status count is monotone non-decreasing at fixed version — so
  the sentinel watches the FULL status-count vector, not just the
  terminal cell. A terminal-only sentinel over a zero-terminal corpus
  guards nothing live; the full-vector version would have caught both
  truncations the night they happened.
- **Detectable beats pretend-preventable**: guarantees against writes
  arriving from outside the process (shell redirects, new scripts) are
  framed as detection commitments — evidence-loss trips an alarm —
  never as prevention claims the architecture cannot make.

## Added after sentinel v2

- **Fixtures age with semantics**: when an instrument's semantics change,
  every fixture assertion that encoded the old behavior is re-audited —
  a stale expectation is a wrong answer wearing a green checkmark.
  Assertions test the current invariant (trips the vector, terminal
  untouched), never the implementation era they were written in. [the
  v1 "must not trip" assertion failing correctly against v2]

## Added after JE unification

- **Stacked defects mask each other — "fixed" claims are per-defect,
  never per-item**: an item that stays red after a fix gets
  re-diagnosed fresh, because the original diagnosis may not exhaust
  its defects. [agent_285: the extraction bug and the unnetted ROU leg
  each hid behind the other; the item passed only when BOTH were fixed]
- **Behavior changes score their mover prediction**: capture
  before/after, and the prediction names both the CLASS and the
  expected shape of movement; held here at exactly one mover, in-class,
  probes unmoved at 40/40.

## Added after the propagation check

- **Rulings emit banned-form patterns; the chart carries standing
  invariants**: a pair ruling's losing form becomes a machine-readable
  pattern (base AND compounds), and a chart-invariants fixture asserts
  every run that (a) no two canonical rows collide under the string
  normalizer, (b) no chart row matches any banned pattern, (c) every
  alias targets an existing canonical. Propagation-in-the-apply-step is
  the procedure; the fixture is what makes forgetting it impossible.
  [standalone Buildings + the compound plural surviving the ruling;
  two dash-variant Equipment canonicals coexisting undetected]

## Added after the fixture's first catch

- **Apply steps sweep the full store, never the rows in view**: three
  orphans from one class proved the pattern — each ruling was applied to
  the proposal rows on screen while the chart's own matching entries sat
  untouched. Any ruling's application enumerates and sweeps the ENTIRE
  store it governs (chart, templates, treatment notes alike); the
  invariants fixture is the backstop, not the mechanism.

## Added after the fourth orphan

- **Rule application is generated, never hand-applied per instance**: the
  fourth orphan existed because pattern coverage varied BY RULING —
  Building's ruling got compound patterns, Note Payable's got an exact
  anchor, purely by authorship. One banned_patterns(ruling) generator
  produces the full pattern class (exact, compound, prefix-compound) for
  EVERY ruling, and the fixture carries a meta-invariant asserting
  generator uniformity across pair_rulings.json. Per-instance hand-
  widening recreates the propagation gap one level up; this is the
  one-authority pattern's third application (canon for comparisons,
  ledger_io for writes, one generator for ruling patterns).

## Added at the generator's landing

- **Store facts, derive artifacts**: a stored derived list is exactly
  where drift hides — Building's patterns and Note Payable's diverged
  because both were stored artifacts authored at different moments.
  Registries hold declared facts (winning form, losing form); every
  derived form (patterns, aliases, probes) is generated at read time by
  the one authority, with an internal completeness assert so a declared-
  but-unimplemented class fails loudly instead of silently narrowing.

## Added after the residual rulings

- **Solver-context parity across harnesses**: every solver path —
  primary, dual, remake — is built by the same builder or provably
  carries the same pack notes, and wiring probes cover every path.
  Context asymmetry between solvers manufactures construal splits that
  masquerade as disagreements. [the dual solver decomposing an operating
  lease finance-style while trim carried the vintage's single-line
  convention]
- **Construal splits sub-classify**: a defensible alternative reading of
  an ambiguous stem routes to stem clarification; a reading that is
  simply wrong under the governing model (operating leases recognize no
  separate interest expense line) is a solver treatment datum — the stem
  stands, and the fix is context, not wording.

## Added after the context-parity finding

- **Findings inherit the validity of their comparisons**: when a context
  or instrument asymmetry is discovered, every conclusion that leaned on
  the contaminated comparison is re-attributed proactively — by the one
  who reported it, without being asked. Item-level verdicts may stand
  (trim's netting answer was still wrong for the course) while the
  INFERENCE drawn from them (solver quality) retracts. [agent_204
  reclassified from "solver-quality finding" to context deficit; the
  dual's "independent corroboration" of the key retracted as garnish —
  the ruling stands on textbook citations alone]
- **Context divides into treatment-defining and knowledge-carrying**:
  harness-defining instructions (required-figure coverage) legitimately
  vary by design and ARE the treatment under test; pack knowledge
  (treatment notes, vintage conventions) must be uniform across every
  solver path. The builder's role parameter varies exactly one framing
  line; the rule set is invariant by construction, asserted by the
  parity fixture.

## Added after the trace confirmation

- **Informational numbers rot into load-bearing ones**: any figure that
  survives into a projection gets re-derived from decision-grade
  evidence first; contaminated color is DISCARDED, never refreshed —
  re-running a broken A/B to update a number no decision needs spends
  tokens on nostalgia. [the 0.799 cost ratio quietly feeding tranche
  projections; the +44% observation discarded]
- **Exclusion via provenance beats special-case re-derivation**: marking
  stale outputs (PACK_NOTES_STALE) lets the STANDARD path re-derive
  them as ordinary uncorroborated figures — same fresh work, no bespoke
  pre-pass, evidence retained as records of the harness that produced
  it. The marking is free; the re-derivation spend was already in the
  run's scope, and paying it is the price of symmetry.

## Added after the provenance finding

- **Provenance is captured at write time, never backfilled with current
  values**: a stamp applied retroactively with today's versions records
  what is true NOW, not what was true at generation — it launders
  staleness instead of catching it. Bundles stamp pack_notes_version,
  harness_version, and comparator_version at the moment of generation,
  immutably. Historical outputs may be re-stamped only by RECONSTRUCTION
  from independent evidence (run logs, script history), labeled as
  reconstructed. [stamp() marking the note-less parity50 trim cache as
  current, hiding the swapped asymmetry in agent_204's comparison]
- **Symmetry is a property of the comparison, not of one side**: marking
  one input stale while comparing against another input stale for the
  identical reason swaps the asymmetry rather than removing it.
  Staleness rules evaluate EVERY input of a comparison before its output
  is scored.

---
*Continuous-release standard adopted 2026-08-10 (see docs/08-08-RELEASING.md): rules now land in the prompts immediately as patch releases; this file continues as the incident-provenance ledger.*

## Added at the case-history consolidation (v1.4.2)

- **The case history is part of the system**: settled rulings
  (DECISIONS), retired numbers/approaches/beliefs (RETIRED), and the
  items casebook travel with the repo and bind every agent. Reopening a
  settled question requires citing its ID with new evidence; quoting a
  retired number as current is an error. Anti-loop by construction.


## Added at REPORT-001 review

- **A rule enforced in one caller is not enforced**: shared law lives in
  one authority function every consumer calls (provenance.evidence_dir()
  — preflight and fp_taxonomy disagreed by 32 findings on one item until
  both called it). Fifth application of one-authority.
- **Terminal transitions are gate-checked in the write path**: the state
  store itself refuses `verified`/`needs_human` while the launch gate is
  RED absent an explicit operator override — D2 became an enforced
  invariant instead of a description. [one order-directed closure minted
  a terminal under RED]
- **Caveats travel inside the artifact that carries the number**: the
  MATCHER_ARTIFACT exclusion is a FORECAST until floor #1 re-measures,
  and the tool's own output says so — a caveat that can travel
  separately from its number will.
- **Fixture claims run cold**: bytecode caches cleared before any
  fixture verdict — a stale .pyc reported green over a live SyntaxError.
- **Paths route through one constant; case-sensitivity is a portability
  bug class**: DELIVERABLES/ vs deliverables/ was one Linux checkout
  away from freezing the STATUS stamp forever.
- **deliverables/ holds only what its generator can regenerate**;
  generatorless files promote to pack/ or docs/. Privacy guards keep
  their literal strings in LOCAL gitignored files — a guard must never
  publish what it guards.
- **Manifests may record foreign absolute paths as history; RESOLUTION
  is always re-rooted onto the current checkout** (provenance.local()).


## Added during the reviewer-executed refactor (Tier 1)

- **Append-only stores need an explicit READ-path resolution rule** —
  reversibility is a requirement on resolution, not on history. "Latest
  wins" hid verdicts; "terminal outranks" made a reviewer ruling
  physically unlandable. Highest stage, then latest, is right in both
  directions. [the 204 revert that could not land]
- **When an operator decision amends a trigger, edit the OLD rule's text
  everywhere stale readers will look** — the executor's conjunction
  rewrite inside DECISION-001's language is the pattern.
- **Gates assert; they never echo.** A neutrality gate that prints the
  fixture count and commits anyway is the gate-that-doesn't-gate class,
  reviewer edition. [two commits landed at 8/9 before the gate aborted]
- **Read immediately before editing** — an edit written against a
  remembered read is written against a file that may no longer exist.
  [ledger_io had grown a write-gate between my read and my edit]
- **A commit message is a claim and the diff is its evidence** — verify
  the diff proves the message BEFORE committing. [three overclaims in
  one session: 'sentinel imports TERMINAL' before it did; 'adopted at
  the matching sites' with zero matches]


## Added at gate GREEN

- **A broken measurement must never look like a failing one**: zero
  probes reaching the floor is BROKEN, not 0/0-failing — and the guard
  asserting the difference is now standing. [floor #1 silently
  unmeasurable off one laptop via absolute manifest paths]
- **A fallback that must "track" its source is a second source** — the
  executor's phrase, now law. Fixtures copy the real dependency instead
  of carrying shadow constants.
- **Registry tuples are visibility law**: a directory not in
  EVIDENCE_PREFERENCE is invisible to every tool — so the registry gets
  a completeness probe (every evidence dir is listed or explicitly
  excluded). [14 fresh goldens silently inadmissible]
- **A caveat reads its SUBJECT, not its inputs**: the packet's scope
  warning reported the nominations while describing the golden set — a
  caveat misreporting its own subject is worse than none.
