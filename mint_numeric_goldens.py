#!/usr/bin/env python3
"""
Score the numeric Stage-1 batch and mint admissible numeric goldens
(ORDER-003 item 6), plus close the re-stemmed agent_130#00 (item 5).

Why numeric items specifically: the countersign packet was 13/13 journal_entry,
so certifying floor #2 on it would have certified journal-entry items and
nothing else. Numeric items are Class A — the comparator's own domain — so they
are the honest way to widen the packet. MCQ stays excluded on purpose: it is
outside the comparator's domain, not merely unrun.

Every bundle is stamped at WRITE time here, immediately after the solve, so no
output in this batch ever exists without provenance. A golden is minted only if
the comparator returns zero hard findings against an admissible bundle.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path.insert(0, HERE)

import compare_stage1_v3 as C     # noqa: E402
import io_json                    # noqa: E402
import ledger_io                  # noqa: E402
import preflight as PF            # noqa: E402
import provenance as P            # noqa: E402


def main():
    qs, known, amap = PF.load()
    rows, results = [], []

    targets = [("agent_130#00", "evidence_restem", "restem-1")]
    targets += [(s["id"], "evidence_numeric", "numeric-1")
                for s in json.load(open(os.path.join(OUT, "numeric_sample.json"),
                                        encoding="utf-8"))]

    for qid, sub, harness in targets:
        q = qs.get(qid)
        d = os.path.join(OUT, sub, qid.replace("#", "_"))
        sp = os.path.join(d, "solver_output.json")
        if not q or not os.path.exists(sp):
            results.append({"id": qid, "state": "NO_OUTPUT", "dir": sub})
            continue

        # WRITE-TIME stamp: immutable, captured now, never applied retroactively
        P.capture(d, qid, q["stem"], harness)
        adm, why = P.admissible(json.load(open(os.path.join(d, "provenance.json"),
                                              encoding="utf-8")), q)

        sol = json.load(open(sp, encoding="utf-8"))
        iss, meta = C.compare(sol, q, known, amap)
        hard = [i for i in iss if i["kind"] in C.HARD]
        peeked = bool(sol.get("peeked"))

        state = ("PEEKED" if peeked else
                 "INADMISSIBLE" if not adm else
                 "CLEAN" if not hard else "FINDINGS")
        results.append({
            "id": qid, "state": state, "harness": harness,
            "hard": len(hard), "key_lines": meta.get("key_lines", 0),
            "answers": len(sol.get("answers") or []),
            "routed_stage2": meta.get("routed_stage2", 0),
            "kinds": sorted({i["kind"] for i in hard}),
            "admissible": why, "evidence": os.path.relpath(d, HERE),
        })

        # ledger: progress only. `verified` is a PIPELINE terminal and the gate
        # is RED - ledger_io would refuse it, which is the point.
        rows.append(ledger_io.make_row(
            content_hash=q["content_hash"], id=qid,
            status="machine_passed" if state == "CLEAN" else "failed",
            stage=1, pack_id=q.get("pack_id"), lineage_id=q.get("lineage_id", qid),
            comparator_version=C.COMPARATOR_VERSION,
            harness=harness, evidence=os.path.relpath(d, HERE),
            pipeline_version=ledger_io.PIPELINE_VERSION))

    ledger_io.append_rows(rows)

    import collections
    tally = collections.Counter(r["state"] for r in results)
    print("=== NUMERIC STAGE-1 BATCH + RE-STEM ===\n")
    for r in results:
        print(f"  {r['id']:14s} {r['state']:13s} hard={r.get('hard', '-'):>2} "
              f"key_lines={r.get('key_lines', '-'):>3} "
              f"answers={r.get('answers', '-'):>3} {','.join(r.get('kinds', []))[:44]}")
    print(f"\n  {dict(tally)}")
    print(f"  ledger rows appended: {len(rows)} (all progress states; a terminal")
    print("  write would be REFUSED by the gate, which is the intended behaviour)")

    io_json.dump(os.path.join(OUT, "numeric_batch_results.json"),
                 {"results": results, "tally": dict(tally)})
    print(f"\nwrote {os.path.join(OUT, 'numeric_batch_results.json')}")


if __name__ == "__main__":
    main()
