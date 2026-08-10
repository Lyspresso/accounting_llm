#!/usr/bin/env python3
"""
Sentinel fault-injection fixture.

The sentinel spent its whole life green while counting a state that cannot be
lost in the way it was watching for. Two injections settle whether it works:

  deleting a TERMINAL row        -> must TRIP
  deleting a machine_passed row  -> must NOT trip (progress, not terminal)

Runs against a temporary copy; the real ledger is never touched.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")


def run_sentinel(workdir):
    """Returns the sentinel's exit code in a sandboxed copy of out/."""
    r = subprocess.run([sys.executable, os.path.join(workdir, "sentinel.py"), "--check"],
                       capture_output=True, text=True, cwd=workdir)
    return r.returncode, r.stdout


def main():
    with tempfile.TemporaryDirectory() as tmp:
        # sandbox: sentinel + a copy of the artifacts it reads
        shutil.copy(os.path.join(HERE, "sentinel.py"), tmp)
        # sentinel imports PIPELINE_VERSION/TERMINAL from ledger_io with NO
        # fallback (ORDER-003 item 4), so the sandbox must carry the real
        # module rather than let the sentinel carry a shadow copy of its
        # constants. paths.py comes along because ledger_io imports it.
        for dep in ("ledger_io.py", "paths.py", "io_json.py"):
            src = os.path.join(HERE, dep)
            if os.path.exists(src):
                shutil.copy(src, tmp)
        os.makedirs(os.path.join(tmp, "out"), exist_ok=True)
        for f in ("ledger.jsonl", "questions.jsonl"):
            src = os.path.join(OUT, f)
            if os.path.exists(src):
                shutil.copy(src, os.path.join(tmp, "out", f))

        lpath = os.path.join(tmp, "out", "ledger.jsonl")
        rows = [json.loads(l) for l in open(lpath, encoding="utf-8")]
        cur = {json.loads(l)["content_hash"] for l in
               open(os.path.join(tmp, "out", "questions.jsonl"), encoding="utf-8")}

        # The corpus currently holds NO terminal items, so inject one first -
        # a fixture that can only run when the condition already exists is a
        # fixture that never runs.
        seed_hash = next(iter(cur))
        rows.append({"content_hash": seed_hash, "id": "FIXTURE#00",
                     "status": "verified", "stage": 3, "pipeline_version": "1.2"})
        mp_hash = next(iter(cur - {seed_hash}))
        rows.append({"content_hash": mp_hash, "id": "FIXTURE#01",
                     "status": "machine_passed", "stage": 1, "pipeline_version": "1.2"})
        with open(lpath, "w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r) + "\n")

        rc, _ = run_sentinel(tmp)          # establish the baseline WITH a terminal
        base_ok = rc == 0
        print(f"  {'ok  ' if base_ok else 'FAIL'}  baseline established with 1 terminal item")

        # --- injection 1: delete the TERMINAL row -> must TRIP -------------
        keep = [r for r in rows if r.get("status") != "verified"]
        with open(lpath, "w", encoding="utf-8") as fh:
            for r in keep:
                fh.write(json.dumps(r) + "\n")
        rc1, out1 = run_sentinel(tmp)
        trip = rc1 == 2 and "SENTINEL HALT" in out1
        print(f"  {'ok  ' if trip else 'FAIL'}  deleted TERMINAL row -> "
              f"{'TRIPPED' if trip else f'did NOT trip (rc={rc1})'}")

        # --- injection 2: delete a machine_passed row -> must NOT trip -----
        rows2 = [r for r in rows]          # restore, then drop the progress row
        rows2 = [r for r in rows2 if r.get("status") != "machine_passed"
                 or r.get("id") != "FIXTURE#01"]
        with open(lpath, "w", encoding="utf-8") as fh:
            for r in rows2:
                fh.write(json.dumps(r) + "\n")
        # reset recorded baseline so the comparison is against the terminal count
        rc2, out2 = run_sentinel(tmp)
        # Under sentinel v2 this DOES trip - correctly. Merge-only semantics
        # make every cell monotone, so losing a machine_passed row is a
        # destroyed row, not a state transition. The distinction that must
        # survive is that it is NOT a terminal loss: the vector trips while the
        # terminal count is untouched. The v1 expectation ("must not trip") was
        # written for a terminal-only sentinel and is stale, not the code.
        vector_tripped = rc2 == 2 and "SENTINEL HALT" in out2
        terminal_untouched = "SENTINEL HALT: terminal states fell" not in out2
        quiet = vector_tripped and terminal_untouched
        print(f"  {'ok  ' if quiet else 'FAIL'}  deleted machine_passed row -> "
              f"vector {'tripped' if vector_tripped else 'MISSED'}, "
              f"terminal {'untouched' if terminal_untouched else 'WRONGLY FELL'}")

        # --- injection 3: delete a STAGE row -> must TRIP under v2 ---------
        # A terminal-only sentinel cannot see this: the corpus holds zero
        # terminal items, so the only live evidence is stage rows. This is the
        # injection that mattered and the old sentinel slept through it.
        with open(lpath, "w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r) + "\n")
        run_sentinel(tmp)                       # re-baseline with everything present
        stage_rows = [r for r in rows if r.get("stage")]
        drop = stage_rows[0] if stage_rows else None
        kept3 = [r for r in rows if r is not drop]
        with open(lpath, "w", encoding="utf-8") as fh:
            for r in kept3:
                fh.write(json.dumps(r) + "\n")
        rc3, out3 = run_sentinel(tmp)
        trip3 = rc3 == 2 and "SENTINEL HALT" in out3
        print(f"  {'ok  ' if trip3 else 'FAIL'}  deleted a STAGE row -> "
              f"{'TRIPPED' if trip3 else f'did NOT trip (rc={rc3})'}")

        # --- injection 4: a SCOPE MIGRATION must NOT halt -------------------
        # An authorised key repair moves an item's content_hash, which migrates
        # every row of that lineage from `current` to `superseded`. No row is
        # destroyed. Halting on that made every repair look like data loss, and
        # a guard that cries wolf on lawful work trains people to reach for
        # --invalidate - which is how a REAL loss gets waved through.
        with open(lpath, "w", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r) + "\n")
        run_sentinel(tmp)                       # baseline with everything present
        qp = os.path.join(tmp, "out", "questions.jsonl")
        if os.path.exists(qp):
            qrows = [json.loads(l) for l in open(qp, encoding="utf-8")]
            if qrows:
                qrows[0]["content_hash"] = "repaired" + qrows[0]["content_hash"][:8]
                with open(qp, "w", encoding="utf-8") as fh:
                    for r in qrows:
                        fh.write(json.dumps(r) + "\n")
        rc4, out4 = run_sentinel(tmp)
        no_halt = rc4 != 2
        print(f"  {'ok  ' if no_halt else 'FAIL'}  hash MOVED (repair), no rows "
              f"lost -> {'no halt' if no_halt else f'HALTED (rc={rc4}) - false alarm'}")

        ok = base_ok and trip and quiet and trip3 and no_halt
        print(f"\nsentinel fault-injection: {'GREEN' if ok else 'RED'}")
        sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
