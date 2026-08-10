FROM: reviewer
TO:   operator
DATE: 2026-08-10
RE:   One letter — when must your countersign session happen?
NEEDS-OPERATOR: yes

The executor proved your ~90-minute countersign session is on the
critical path to a fully GREEN gate (floor #2 certifies at human tier
only, and zero human-tier goldens exist). Two ways to sequence it:

A — CERTIFY FIRST. Nothing launches until your session is done.
    Most conservative; your calendar gates the start of tranche 1.

B — PARALLEL (recommended). Tranche 1 launches when the MEASURED
    floors clear (n ≥ 35, zero chargeable, ai-tier); your session runs
    while it computes. Safe because terminal `verified` labels are now
    MECHANICALLY blocked in the ledger's write path until
    certification — the tranche collects evidence, nothing gets its
    final label until you sign.

Reply with one letter as a file here or one line in chat.
