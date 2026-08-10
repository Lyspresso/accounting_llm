# Startup Checklist (Budget mode first)

1. **The 4000 questions in one place** — a single folder or file, any format;
   Stage 0 normalizes. If they're scattered across exports, consolidate first.
   Keep pack/batch boundaries visible (folder or filename per pack) — the
   pipeline uses pack identity for format profiling and cohort escalation.
   This becomes QUESTIONS_PATH.
2. **Machine-readable textbook per class** — PDF with a text layer or extracted
   text (TEXTBOOK_PATH). Scanned pages need OCR first. Canonical authority, so
   quality here matters most.
3. **Syllabus per class** (SYLLABUS_PATH) — defines coverage scope.
4. **Notes and slides** (NOTES_PATH) — secondary source; fine to add later.
5. **Edition note** — one paragraph per textbook: edition, copyright year,
   which standards treatments it uses (ASC 606/842/740 vintage). Seeds the
   standards-vintage notes and the GAAP-divergence `conflict` flags.
6. **Pack seeds** — provided in `pack/`: chart of accounts, alias table, entry
   templates. Extend the chart from your book's own chapter examples; the
   templates and aliases grow themselves from escalations and flags.
7. **Model choices** — one frontier model (Opus-class) runs everything in
   both modes; optionally name a second frontier model as the decorrelated
   auditor. Budget mode saves on run size, never on model tier.
8. **A hard spend cap for the run** — Budget mode checkpoints every 50 and
   stops cleanly at the cap. Pick the number before you start.
9. **Runner environment** — Claude Code or any agent with Python 3 and file
   access; create OUTPUT_DIR; keep `tests/` in the repo (the prompts require
   both sims to keep passing).
10. **Config** — fill paths in `config.template.yaml`, save as `config.yaml`,
    keep defaults to start. Create an empty `goldens/` folder (GOLDENS_PATH).
11. **Pilot batch** — ~100 questions end-to-end before the full 4000. Shakes
    out parsing, alias gaps, and template misses while mistakes cost pennies,
    and gives you a real cost-per-question number to check your cap against.
12. **Your 50-question hand check** — random sample, alongside the pilot.
    Measures the true base error rate AND seeds `goldens/` for the probe
    stream. Every needs_human item you later fix also becomes a golden.
13. **One taxonomy eyeball** — when `taxonomy.json` lands, spend twenty minutes
    checking it against the syllabus and table of contents. Every coverage
    claim inherits from that one small file.

With 1–10 done, paste budget-mode-prompt.md into the runner and go; 11–13 are
the only human-minutes week one requires.
