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
  exactly what changed between any two releases; the fold-queue entry
  for each rule names the incident that motivated it.
- `docs/v1.4-fold-queue.md` continues as the incident-provenance ledger:
  under continuous release, every new rule lands in the queue AND the
  current prompts AND a fresh release directory in the same commit.
