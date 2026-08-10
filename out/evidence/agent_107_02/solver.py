#!/usr/bin/env python3
"""Blind solver for item agent_107#02 -- Bayline Packaging Co. lump-sum (combined)
stock issuance: proportional method (Case A) vs incremental method (Case B),
plus paid-in-capital presentation (part c) and the stock-issue-cost concept (part d).

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; no floats anywhere.

* Money is carried and reported at the cent (2 decimal places) using
  ROUND_HALF_UP, applied once per allocated amount at the moment that amount
  is determined (round-per-period / round-per-allocation, NOT round-at-end).
* Allocation percentages are computed as exact Decimal ratios and are reported
  rounded to 4 decimal places (e.g. 0.7200 = 72.00%) with ROUND_HALF_UP, but the
  UNROUNDED exact ratio is what multiplies the lump sum, so no percentage
  rounding error leaks into the dollar allocation.
* Under the proportional method the LAST class allocated is taken as the
  plug (lump sum less the amounts already allocated) so that the allocated
  proceeds foot exactly to the cash received and the journal entry balances to
  the penny. With this fact pattern the plug equals the directly-rounded figure
  anyway (72% / 28% of $95,000 are both exact cents), so the safeguard never
  actually bends a number here.
* No present-value factors are involved in this item, so no PV table-factor vs
  exact-formula choice arises.

METHOD (derived from the stem, nothing hard-coded but the given facts)
----------------------------------------------------------------------
Case A -- both fair values known => PROPORTIONAL method. Compute each class's
total fair value (shares x per-share FV), sum to get total relative fair value,
divide each class's FV by that total to get its allocation percentage, and apply
those percentages to the lump-sum cash received. Split each class's allocated
proceeds into par (shares x par) and paid-in capital in excess of par (remainder).

Case B -- only the common fair value is reliable => INCREMENTAL method. Assign
the known class its full fair value (2,000 x $38) and treat the remainder of the
lump sum as the amount attributable to the class with no reliable market value
(preferred). Split each class into par and PIC in excess of par as above.

Part c -- present the Case A results as the paid-in capital section: par lines
for each class plus the excess-of-par lines, totalling to the cash received.

Part d -- conceptual (no figure): stock issue costs are a cost of raising
capital, so they are debited against the proceeds (a reduction of paid-in
capital in excess of par), never expensed.

Run: python3 solver.py   -> prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENTS = Decimal("0.01")
PCT = Decimal("0.0001")


def money(x: Decimal) -> Decimal:
    """Round a Decimal to cents, ROUND_HALF_UP."""
    return x.quantize(CENTS, rounding=ROUND_HALF_UP)


def pct(x: Decimal) -> Decimal:
    """Round an allocation ratio to 4 dp, ROUND_HALF_UP (reporting only)."""
    return x.quantize(PCT, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly number: int when the cents are zero, else float of the
    already-rounded 2dp Decimal (value is exact at 2dp, so no float drift)."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------------------
# Facts from the stem
# ---------------------------------------------------------------------------
COMMON_SHARES = Decimal("2000")
COMMON_PAR = Decimal("5")
PREFERRED_SHARES = Decimal("1000")
PREFERRED_PAR = Decimal("10")

# Case A
A_LUMP_SUM = Decimal("95000")
A_COMMON_FV_PER_SHARE = Decimal("36")
A_PREFERRED_FV_PER_SHARE = Decimal("28")

# Case B
B_LUMP_SUM = Decimal("100000")
B_COMMON_FV_PER_SHARE = Decimal("38")
# preferred has NO reliable market price -> incremental method

# Par credits are the same in both cases (same share counts / par values)
COMMON_PAR_TOTAL = money(COMMON_SHARES * COMMON_PAR)          # 2,000 x $5
PREFERRED_PAR_TOTAL = money(PREFERRED_SHARES * PREFERRED_PAR)  # 1,000 x $10

# ---------------------------------------------------------------------------
# Case A -- PROPORTIONAL (relative fair value) allocation
# ---------------------------------------------------------------------------
a_common_fv = money(COMMON_SHARES * A_COMMON_FV_PER_SHARE)        # 72,000
a_preferred_fv = money(PREFERRED_SHARES * A_PREFERRED_FV_PER_SHARE)  # 28,000
a_total_fv = money(a_common_fv + a_preferred_fv)                  # 100,000

# Exact (unrounded) ratios drive the dollars; rounded copies are for reporting.
a_common_ratio_exact = a_common_fv / a_total_fv
a_preferred_ratio_exact = a_preferred_fv / a_total_fv
a_common_pct = pct(a_common_ratio_exact)
a_preferred_pct = pct(a_preferred_ratio_exact)

a_common_alloc = money(A_LUMP_SUM * a_common_ratio_exact)
# Last class allocated is the plug so the allocation foots to cash exactly.
a_preferred_alloc = money(A_LUMP_SUM - a_common_alloc)

a_common_apic = money(a_common_alloc - COMMON_PAR_TOTAL)
a_preferred_apic = money(a_preferred_alloc - PREFERRED_PAR_TOTAL)

# ---------------------------------------------------------------------------
# Case B -- INCREMENTAL allocation (known FV first, remainder to the other class)
# ---------------------------------------------------------------------------
b_common_alloc = money(COMMON_SHARES * B_COMMON_FV_PER_SHARE)   # known FV: 76,000
b_preferred_alloc = money(B_LUMP_SUM - b_common_alloc)          # remainder: 24,000

b_common_apic = money(b_common_alloc - COMMON_PAR_TOTAL)
b_preferred_apic = money(b_preferred_alloc - PREFERRED_PAR_TOTAL)

# ---------------------------------------------------------------------------
# Part c -- paid-in capital presentation immediately after the Case A issuance
# ---------------------------------------------------------------------------
c_total_paid_in_capital = money(
    PREFERRED_PAR_TOTAL + COMMON_PAR_TOTAL + a_preferred_apic + a_common_apic
)

# ---------------------------------------------------------------------------
# Journal entries
# ---------------------------------------------------------------------------
Z = Decimal("0")


def line(account, debit=Z, credit=Z):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


entry_a = {
    "part": "a",
    "date": "March 1, Year 1",
    "description": "Case A -- lump-sum issuance allocated by the proportional "
                   "(relative fair value) method",
    "lines": [
        line("Cash", debit=A_LUMP_SUM),
        line("Preferred Stock", credit=PREFERRED_PAR_TOTAL),
        line("Paid-in Capital in Excess of Par - Preferred Stock",
             credit=a_preferred_apic),
        line("Common Stock", credit=COMMON_PAR_TOTAL),
        line("Paid-in Capital in Excess of Par - Common Stock",
             credit=a_common_apic),
    ],
}

entry_b = {
    "part": "b",
    "date": "March 1, Year 1",
    "description": "Case B -- lump-sum issuance allocated by the incremental "
                   "method (common at its known fair value, remainder to preferred)",
    "lines": [
        line("Cash", debit=B_LUMP_SUM),
        line("Preferred Stock", credit=PREFERRED_PAR_TOTAL),
        line("Paid-in Capital in Excess of Par - Preferred Stock",
             credit=b_preferred_apic),
        line("Common Stock", credit=COMMON_PAR_TOTAL),
        line("Paid-in Capital in Excess of Par - Common Stock",
             credit=b_common_apic),
    ],
}

# Debits must equal credits -- fail loudly rather than publish an unbalanced entry.
for e in (entry_a, entry_b):
    dr = sum(Decimal(str(ln["debit"])) for ln in e["lines"])
    cr = sum(Decimal(str(ln["credit"])) for ln in e["lines"])
    assert dr == cr, f"entry {e['part']} does not balance: {dr} vs {cr}"

# Allocations must foot to the cash received.
assert a_common_alloc + a_preferred_alloc == A_LUMP_SUM
assert b_common_alloc + b_preferred_alloc == B_LUMP_SUM
assert c_total_paid_in_capital == A_LUMP_SUM

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
answers = [
    # a -- relative fair values, percentages, allocated proceeds (all explicitly required)
    {"label": "a: Case A relative fair value of common (2,000 x $36)",
     "value": num(a_common_fv)},
    {"label": "a: Case A relative fair value of preferred (1,000 x $28)",
     "value": num(a_preferred_fv)},
    {"label": "a: Case A total relative fair value",
     "value": num(a_total_fv)},
    {"label": "a: Case A allocation percentage to common (0.72 = 72%)",
     "value": float(a_common_pct)},
    {"label": "a: Case A allocation percentage to preferred (0.28 = 28%)",
     "value": float(a_preferred_pct)},
    {"label": "a: Case A proceeds allocated to common stock",
     "value": num(a_common_alloc)},
    {"label": "a: Case A proceeds allocated to preferred stock",
     "value": num(a_preferred_alloc)},

    # b -- incremental allocation
    {"label": "b: Case B proceeds allocated to common stock (2,000 x $38 known FV)",
     "value": num(b_common_alloc)},
    {"label": "b: Case B proceeds allocated to preferred stock (remainder)",
     "value": num(b_preferred_alloc)},

    # c -- paid-in capital lines immediately after the Case A issuance
    {"label": "c: Preferred Stock, $10 par, 1,000 shares issued and outstanding",
     "value": num(PREFERRED_PAR_TOTAL)},
    {"label": "c: Common Stock, $5 par, 2,000 shares issued and outstanding",
     "value": num(COMMON_PAR_TOTAL)},
    {"label": "c: Paid-in Capital in Excess of Par - Preferred Stock",
     "value": num(a_preferred_apic)},
    {"label": "c: Paid-in Capital in Excess of Par - Common Stock",
     "value": num(a_common_apic)},
    {"label": "c: Total paid-in capital",
     "value": num(c_total_paid_in_capital)},
]

notes = (
    "Case A uses the proportional method because both fair values are known: "
    "common FV $72,000 and preferred FV $28,000 give a total relative fair value "
    "of $100,000, so 72% / 28% of the $95,000 lump sum is allocated to common / "
    "preferred. Case B uses the incremental method because preferred has no "
    "reliable market price: common takes its known fair value of $76,000 and the "
    "$24,000 remainder of the $100,000 lump sum is assigned to preferred. "
    "Part c presentation (Case A, paid-in capital section, immediately after "
    "issuance): Preferred Stock $10,000; Common Stock $10,000; Paid-in Capital in "
    "Excess of Par - Preferred $16,600; Paid-in Capital in Excess of Par - Common "
    "$58,400; total paid-in capital $95,000 (equal to the cash received, since no "
    "issue costs were incurred and no earnings exist yet). "
    "Part d (no figure required): stock issue costs are a cost of raising capital "
    "rather than a cost of operating, so they are netted against the issuance "
    "proceeds -- debited to Paid-in Capital in Excess of Par, reducing the amount "
    "credited to equity -- instead of being reported as an expense on the income "
    "statement."
)

result = {
    "id": "agent_107#02",
    "rounding_convention": (
        "decimal.Decimal only, no floats; money quantized to cents with "
        "ROUND_HALF_UP at each allocation (round-per-allocation, not round-at-end); "
        "allocation percentages computed as exact ratios and reported at 4 dp "
        "ROUND_HALF_UP, with the exact unrounded ratio used for the dollar "
        "allocation; final class allocated as the plug so allocated proceeds foot "
        "exactly to cash and debits equal credits; no PV factors involved"
    ),
    "answers": answers,
    "journal_entries": [entry_a, entry_b],
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(result, indent=2))
