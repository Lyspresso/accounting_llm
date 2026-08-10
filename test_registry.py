#!/usr/bin/env python3
"""
Evidence-registry completeness probe (ORDER-004 item 4).

Law: **a directory not in provenance.EVIDENCE_PREFERENCE is invisible to every
tool.** It was learned the expensive way — 14 numeric goldens were minted into
`out/evidence_numeric/`, a directory listed nowhere, and every one of them
resolved "no admissible evidence". `goldens/` held 42 while the floor scored 26,
and the discrepancy was silent: no error, no warning, just a smaller number that
looked plausible.

So every `out/evidence_*` directory must be either REGISTERED in the preference
tuple or EXPLICITLY excluded here, with a reason. Silence is not a third option.
An unregistered directory means solver work that was paid for and cannot be seen.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import provenance as P     # noqa: E402

# Directories deliberately NOT resolvable, each with the reason it is excluded.
# An entry here is a decision; an omission is a bug.
EXCLUDED = {
    # (none today - every evidence dir on disk is registered)
}


def main():
    out = P.OUT
    on_disk = sorted(d for d in os.listdir(out)
                     if d.startswith("evidence") and os.path.isdir(os.path.join(out, d)))
    registered = set(P.EVIDENCE_PREFERENCE)
    failed = []

    print(f"  evidence dirs on disk : {len(on_disk)}")
    print(f"  registered in tuple   : {len(registered)}")

    for d in on_disk:
        n = len([x for x in os.listdir(os.path.join(out, d))
                 if os.path.isdir(os.path.join(out, d, x))])
        if d in registered:
            print(f"  ok    {d:22s} REGISTERED   ({n} bundles)")
        elif d in EXCLUDED:
            print(f"  ok    {d:22s} EXCLUDED     ({EXCLUDED[d]})")
        else:
            print(f"  FAIL  {d:22s} UNREGISTERED ({n} bundles are INVISIBLE)")
            failed.append(d)

    # the reverse direction: a registered dir that does not exist is dead weight,
    # and worse, it silently shifts resolution order for everything after it
    ghosts = [d for d in registered if not os.path.isdir(os.path.join(out, d))]
    for d in ghosts:
        print(f"  note  {d:22s} registered but absent on disk (harmless, but stale)")

    print(f"\nregistry completeness: {'GREEN' if not failed else 'RED'}")
    if failed:
        print("   unregistered evidence directories hold solver work that no tool")
        print("   can resolve. Add them to provenance.EVIDENCE_PREFERENCE (in")
        print("   newest-first order) or to EXCLUDED here with a reason.")
        sys.exit(1)


if __name__ == "__main__":
    main()
