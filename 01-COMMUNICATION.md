# 01-COMMUNICATION.md — how the agents and the operator talk
The repo is the record. Chat is only a doorbell ("pushed REPORT-003 —
pull"). If it matters and it is not a file in this repo, it did not
happen.

## The mailbox

| folder | direction | files |
|---|---|---|
| `comms/orders/` | REVIEWER → EXECUTOR | `ORDER-001.md`, `ORDER-002.md`, … |
| `comms/reports/` | EXECUTOR → REVIEWER | `REPORT-001.md`, `REPORT-002.md`, … |
| `comms/operator/` | LYDIA → everyone | `DECISION-001-….md`, notes, go/no-go calls |

Numbering is monotonic and never reused. Messages are **append-only**:
never edit a sent message — a correction is a NEW message that cites the
old one by name.

## Message format (copy this header exactly)

```
FROM: executor | reviewer | operator
TO:   executor | reviewer | operator
DATE: YYYY-MM-DD
RE:   one line
ANSWERS: ORDER-00N   (reports only — which order this answers)
STATUS-NEEDED: yes/no  (does the sender need a reply to proceed?)
```

## The turn rule (how to know what to do)

1. EXECUTOR: find the highest-numbered ORDER with no REPORT answering
   it. Answer it. Your REPORT addresses **every numbered item** in that
   order, each with one status: `DONE` / `BLOCKED` / `NOT-STARTED`,
   plus one line of evidence (a repo path) or one line of why.
2. REVIEWER: find the highest-numbered REPORT with no ORDER responding
   to it. Verify its arithmetic yourself. Respond with the next ORDER.
3. OPERATOR: you owe nothing on a schedule. When a message carries
   `NEEDS-OPERATOR: yes` in its header, your answer lands as a file in
   `comms/operator/`, however short. One line is a valid file.

## Hard communication rules

1. **Every claim points at a repo path.** "Fixtures green" is not a
   claim; "run_fixtures.sh output in REPORT-004 §2, reproduced from
   commit abc123" is.
2. **A REPORT ships in the same commit as its evidence** — including a
   fresh `deliver.sh` export (STATUS.md must carry a new `generated:`
   timestamp; a stale stamp means the export step was skipped).
3. **BLOCKED names the exact missing path.** The repo version of the
   operator's one-sentence rule: "BLOCKED — `out/evidence/agent_204/`
   does not exist" and nothing else. Never guess around a missing file.
4. **Messages are self-contained.** Never reference chat history, "as
   discussed," or anything outside the repo. Cite files and DECISIONS
   IDs. A reader with only this repo must understand every message.
5. **Numbers carry units and their unit-ladder rung** (rows / hashes /
   lineages), and any number that changed since the last message names
   its mover.
6. **Commit messages** start with the message name they carry:
   `REPORT-004: pre-flight results` / `ORDER-007: taxonomy corrections`.
7. Settled things stay settled: before proposing work, check
   `docs/02-DECISIONS.md` and `docs/03-RETIRED.md`; cite an ID if you
   are reopening one, with new evidence.

## Why this exists

Twelve document-transport failures in three days: empty attachments,
stale exports shipped four batches running, a budget decision that died
in transit as an unfilled template, and one six-hour stall on a report
that was never exported. Every one of those failure modes is impossible
under this protocol, because the message and its evidence travel as one
commit, and staleness is visible in a timestamp instead of arguable in
a chat window.
