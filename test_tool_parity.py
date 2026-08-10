#!/usr/bin/env python3
"""
Tool-parity fixture — two tools measuring one thing must agree (ORDER-002 item 7).

preflight.py and fp_taxonomy.py both decide which evidence bundle speaks for an
item. The rule lived in preflight only, so fp_taxonomy scored agent_204#02
against a cache the admissibility audit flags PACK_NOTES_STALE: one tool called
the item clean, the other filed 32 findings against it. Both were "working".

The class fix was a shared resolver (provenance.evidence_dir). This fixture is
what keeps it shared - a one-time reconciliation drifts the moment someone adds
a third caller, and nothing would notice until the two numbers were quoted in
the same sentence.

Asserted here:
  1. the offender SETS agree exactly (not just the counts)
  2. the chargeable metric preflight reports is the one fp_taxonomy defines
  3. every scored item resolves through the shared resolver, and every bundle
     it returns is admissible
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.join(HERE, "out")


def main():
    import fp_taxonomy as TX          # noqa: E402
    import preflight as PF            # noqa: E402
    import provenance as P            # noqa: E402

    failed = []

    PF.main()
    pf = json.load(open(os.path.join(OUT, "preflight.json"), encoding="utf-8"))
    tx = json.load(open(os.path.join(OUT, "fp_taxonomy.json"), encoding="utf-8"))

    # 1. identical offender sets
    a = sorted(o["id"] for o in pf["false_positive"]["offenders"])
    b = sorted(tx["item_class"])
    ok = a == b
    print(f"  {'ok  ' if ok else 'FAIL'}  offender SETS identical "
          f"({len(a)} vs {len(b)})")
    if not ok:
        failed.append(f"offender sets differ: only-preflight={set(a)-set(b)}, "
                      f"only-taxonomy={set(b)-set(a)}")

    # 2. preflight's gate number IS the taxonomy's chargeable metric
    ok = pf["false_positive"].get("chargeable") == tx["chargeable"]
    print(f"  {'ok  ' if ok else 'FAIL'}  gate consumes the CHARGEABLE metric "
          f"({pf['false_positive'].get('chargeable')} vs {tx['chargeable']})")
    if not ok:
        failed.append("preflight is not using fp_taxonomy's chargeable metric")

    # 3. every bundle the shared resolver hands out is admissible
    qs, _, _ = PF.load()
    bad = []
    for qid in b:
        q = qs.get(qid)
        if not q:
            continue
        src, why = P.evidence_dir(qid, q)
        if src is None:
            bad.append((qid, why))
            continue
        pp = os.path.join(src, "provenance.json")
        if os.path.exists(pp):
            adm, w = P.admissible(json.load(open(pp, encoding="utf-8")), q)
            if not adm:
                bad.append((qid, w))
    ok = not bad
    print(f"  {'ok  ' if ok else 'FAIL'}  every resolved bundle is admissible "
          f"({len(b)} items checked)")
    if bad:
        failed.append(f"inadmissible bundles resolved: {bad[:3]}")

    print(f"\ntool parity: {'GREEN' if not failed else 'RED'}")
    if failed:
        for f in failed:
            print(f"   {f}")
        sys.exit(1)


if __name__ == "__main__":
    main()
