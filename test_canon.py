#!/usr/bin/env python3
"""
canon rule fixtures — every one-off verification that mattered, made permanent.

A verification run once in a shell evaporates on the next edit. Each case here
was a real ruling; the fixture is what keeps the ruling true.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canon  # noqa: E402

CASES = []


def case(name, fn, expect):
    CASES.append((name, fn, expect))


# --- APIC context-conditional resolution (both suspend paths) --------------
APIC = "Paid-in Capital in Excess of Par—Common Stock"
case("apic bare, no context -> fold",
     lambda: canon.resolve_contextual("Paid-in Capital in Excess of Par", [], "")[0], APIC)
case("apic additional, common context -> fold",
     lambda: canon.resolve_contextual("Additional Paid-in Capital",
                                      ["Cash", "Common Stock"], "common issuance")[0], APIC)
case("apic share premium, PREFERRED account in entry -> SUSPEND",
     lambda: canon.resolve_contextual("Share Premium",
                                      ["Preferred Stock", "Cash"], "issued shares")[1], True)
case("apic bare, PREFERRED in part text -> SUSPEND",
     lambda: canon.resolve_contextual("Paid-in Capital in Excess of Par", [],
                                      "the preferred shares were issued")[1], True)
case("apic already qualified -> untouched even in preferred context",
     lambda: canon.resolve_contextual(APIC, ["Preferred Stock"], "preferred")[0], APIC)

# --- corroboration rules ---------------------------------------------------
case("latex money is readable",
     lambda: 18000.0 in canon.nums(r"Net DTA reported = \mathbf{\$18{,}000}"), True)
case("no cross-magnitude corroboration (900 vs 0.9)",
     lambda: canon.corroborates(900, {0.9}, key_text="0.9"), False)
case("prose null corroborates a reported zero",
     lambda: canon.corroborates(0, {5000.0}, key_text="No journal entry is required."), True)
case("percent <-> fraction",
     lambda: canon.corroborates(0.72, {72.0}, key_text="allocation 72%",
                                label="allocation percentage"), True)
case("whole-dollar key tolerates a cents solver",
     lambda: canon.corroborates(279286.65, {279287.0}, key_text="$279,287",
                                schedule=True), True)
case("period factor needs a granularity difference",
     lambda: canon.period_factor_pair(60000, 180000,
                                      "Year 3 accumulated depreciation",
                                      "Year 3 accumulated depreciation"), False)
case("period factor fires on a real unit difference",
     lambda: canon.period_factor_pair(1125, 13500,
                                      "monthly depreciation",
                                      "annual depreciation"), True)


# --- operating-lease regression golden: the two acceptable presentation forms --
_COMPOUND = [{"account": "Lease Expense", "side": "dr", "amount": 34972, "date": "Dec 31"},
             {"account": "Lease Liability", "side": "cr", "amount": 3251, "date": "Dec 31"},
             {"account": "Right-of-Use Asset", "side": "cr", "amount": 31721, "date": "Dec 31"}]
_TWOPART = [{"account": "Right-of-Use Asset", "side": "dr", "amount": 3251, "date": "Dec 31"},
            {"account": "Lease Liability", "side": "cr", "amount": 3251, "date": "Dec 31"},
            {"account": "Lease Expense", "side": "dr", "amount": 34972, "date": "Dec 31"},
            {"account": "Right-of-Use Asset", "side": "cr", "amount": 34972, "date": "Dec 31"}]


def _key(lines):
    return sorted((canon.norm_acct(l["account"]), l["side"], round(abs(l["amount"]), 2))
                  for l in canon.net_per_account(lines))


case("operating lease: compound == two-part after net-per-account",
     lambda: _key(_COMPOUND) == _key(_TWOPART), True)
case("net-per-account is SCOPED to one entry/date",
     lambda: len(canon.net_per_account(
         [{"account": "Cash", "side": "dr", "amount": 100, "date": "A"},
          {"account": "Cash", "side": "cr", "amount": 100, "date": "B"}])) == 2, True)
case("fully offsetting legs within one date produce no net line",
     lambda: len(canon.net_per_account(
         [{"account": "Cash", "side": "dr", "amount": 100, "date": "A"},
          {"account": "Cash", "side": "cr", "amount": 100, "date": "A"}])) == 0, True)


def main():
    failed = []
    for name, fn, expect in CASES:
        try:
            got = fn()
        except Exception as e:                         # noqa: BLE001
            got = f"ERROR {e}"
        ok = got == expect
        if not ok:
            failed.append((name, expect, got))
        print(f"  {'ok  ' if ok else 'FAIL'}  {name}")
    print(f"\ncanon fixtures: {len(CASES) - len(failed)}/{len(CASES)} passing")
    if failed:
        for n, e, g in failed:
            print(f"   {n}: expected {e!r}, got {g!r}")
        sys.exit(1)
    print("CANON FIXTURES GREEN")


if __name__ == "__main__":
    main()
