FROM: operator
TO:   reviewer, executor
DATE: 2026-08-10
RE:   Countersign sequencing — answer to DECISION-002-REQUEST
ANSWERS: comms/operator/DECISION-002-REQUEST.md
STATUS-NEEDED: no

# A — CERTIFY FIRST.

Nothing launches until the countersign session is done.

The reviewer recommended B (parallel). The operator chose **A**. That choice is
recorded as made, not as debated.

## What this changes

DECISION-001 stands on budget and remains in force: tranche 1 = 10,000,000
billable tokens, harness meter authoritative, FIRST_BATCH_GATE inside the
tranche is report-and-continue, human decisions at tranche boundaries only.

DECISION-001's **launch trigger is amended**. It read: launch fires
automatically on pre-flight GREEN, no further authorization. Under A the trigger
is a conjunction:

    tranche 1 fires when   pre-flight GREEN
                     AND   the operator countersign session has certified
                           floor #2 at human tier

Not one or the other, and not GREEN alone. An executor that sees GREEN and no
completed countersign session **does not launch**, and says so.

## Consequences, stated plainly so nobody is surprised later

1. **The operator's calendar is now on the critical path.** Every other blocker
   can clear and the project still waits. That is the accepted cost of A.
2. The write-path terminal gate ordered in ORDER-002 item 2 is still built and
   still required. Under A it is not the thing that makes launching safe — it is
   defence in depth. Belt and braces both stay.
3. The sequence to launch is unchanged in content, only in strictness:
   loosenings with floor-#1 re-measured after each → n ≥ 35 clean goldens →
   pre-flight re-run → **operator session certifies** → launch.

## Why A is coherent

Under B, a tranche would collect evidence against floors that no human had yet
certified, with terminal labels withheld mechanically. That is defensible. A
declines the extra moving part: no evidence is produced under an uncertified
floor at all, so there is no population of results whose standing depends on a
later signature. It costs calendar time and buys the absence of a category of
question — "what do we do with the tranche if certification fails?" — which
under A cannot arise.
