# The release standard (adopted 2026-08-10, operator's order)

**No more freezing. Every spec change publishes immediately as a new
patch version. Old releases are never deleted or rewritten.**

- The next release is **v1.4.2**, then v1.4.3, and so on — one version
  per change-set, cut the moment the change lands, not batched.
- `skill/maxxer-mode-prompt.md` and `skill/budget-mode-prompt.md` are
  always the CURRENT release. Every published release is also preserved
  verbatim under `skill/releases/vX.Y.Z/`.
- Releases are append-only: never edit a published release directory,
  never force-push, never rewrite history. If a release was wrong, the
  fix is the next release.
- Every release declares its type in its header:
  **spec catch-up** (documents already-running behavior — does NOT
  invalidate verdicts, the ledger, or the sentinel baseline) or
  **behavior change** (invalidates per the provenance rules, with
  before/after capture and a mover audit).
- **Regression protocol**: suspect a regression → `diff -ru
  skill/releases/vA skill/releases/vB` (or `git diff tagA tagB`) to see
  exactly what changed between any two releases; the rulebook entry (docs/07-RULEBOOK.md)
  for each rule names the incident that motivated it.
- `docs/07-RULEBOOK.md` (the rulebook) is the incident-provenance ledger:
  under continuous release, every new rule lands in the queue AND the
  current prompts AND a fresh release directory in the same commit.

## The two versions (2.2)

- **Spec version** (`skill/` prompts, `pipeline_version` in config): bumps on
  every release, including non-invalidating catch-ups.
- **BEHAVIOR_VERSION** (`ledger_io.py`, stamped into ledger rows as
  `pipeline_version`): bumps ONLY when comparator/harness/state semantics
  change in a way the sentinel and caches must treat as a new regime.
  A behavior release declares in its notes whether BEHAVIOR_VERSION moved
  and why; a catch-up release never moves it.
