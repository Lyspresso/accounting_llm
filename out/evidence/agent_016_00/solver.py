#!/usr/bin/env python3
"""
Solver for item agent_016#00 — ACCOUNT-343, LO 16-6.

FACT PATTERN (from stem.md)
--------------------------
Redwood Metalworks Inc. issues a 3-year, $80,000 note payable on Jan 1, Year 1.
Stated (cash) rate 5%, paid annually each December 31. Market (effective) rate 9%.
Fiscal year ends December 31. Effective interest method.

Required: (a) cash proceeds/issue price; (b) initial recognition JE;
(c) full effective-interest amortization schedule with a final-period plug;
(d) Dec 31 Year 1 interest JE; (e) Dec 31 Year 3 interest JE + maturity JE.

ROUNDING CONVENTION
-------------------
* All money is decimal.Decimal. No floats anywhere.
* Present value is computed from the EXACT discount formula, not 5-decimal
  printed table factors. Two reasons: (1) the stem explicitly instructs
  "Round the present value to the nearest cent", which only has meaning if the
  underlying PV carries more precision than a table factor gives, and (2) the
  CH 16 course handout works these with Excel's PV()/RATE() functions, which
  are exact-formula. Internal PV arithmetic runs at 50 significant digits and
  is rounded ONCE, at the end, to the cent with ROUND_HALF_UP.
      PV = 80,000 / 1.09^3  +  4,000 * (1 - 1.09^-3) / 0.09
* ROUND_HALF_UP per period thereafter: each year's interest expense is
  carrying_amount * 9% rounded to the cent BEFORE the discount amortization
  and the new carrying amount are derived from it. No carry of unrounded
  residue between periods.
* Final period is PLUGGED, per the Required (c) instruction: Year 3 discount
  amortization is forced to (face - beginning carrying amount) so the ending
  carrying amount equals $80,000.00 exactly, and Year 3 interest expense is
  restated as cash interest + that plugged amortization. This absorbs the
  accumulated per-period rounding drift.

Run:  python3 solver.py    ->  prints one JSON object on stdout.
"""

import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

# High precision for the PV computation; every *reported* figure is quantized
# to the cent explicitly below.
getcontext().prec = 50

CENT = Decimal("0.01")


def cents(x: Decimal) -> Decimal:
    """Round a Decimal to the nearest cent, ROUND_HALF_UP (course convention)."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def f(x: Decimal) -> float:
    """Emit a plain JSON number (no $ signs, no commas)."""
    return float(cents(x))


# ---------------------------------------------------------------------------
# Given facts
# ---------------------------------------------------------------------------
FACE = Decimal("80000")
STATED_RATE = Decimal("0.05")
MARKET_RATE = Decimal("0.09")
TERM = 3  # annual periods

CASH_INTEREST = cents(FACE * STATED_RATE)  # 80,000 * 5% = 4,000.00 per year

# ---------------------------------------------------------------------------
# (a) Issue price = PV of principal + PV of the ordinary annuity of interest
# ---------------------------------------------------------------------------
one_plus_i = Decimal(1) + MARKET_RATE
discount_factor = one_plus_i ** TERM               # 1.09^3
pv_single_factor = Decimal(1) / discount_factor    # exact PV of $1, 3 yrs, 9%
pv_annuity_factor = (Decimal(1) - pv_single_factor) / MARKET_RATE

pv_principal_exact = FACE * pv_single_factor
pv_interest_exact = CASH_INTEREST * pv_annuity_factor
issue_price = cents(pv_principal_exact + pv_interest_exact)

discount_on_note = cents(FACE - issue_price)

# ---------------------------------------------------------------------------
# (c) Effective-interest amortization schedule
# ---------------------------------------------------------------------------
schedule = []
carrying = issue_price

for year in range(1, TERM + 1):
    beginning = carrying
    if year < TERM:
        interest_expense = cents(beginning * MARKET_RATE)
        amortization = cents(interest_expense - CASH_INTEREST)
        ending = cents(beginning + amortization)
    else:
        # Final period: plug so ending carrying amount == face exactly.
        amortization = cents(FACE - beginning)
        interest_expense = cents(CASH_INTEREST + amortization)
        ending = FACE.quantize(CENT)

    schedule.append(
        {
            "year": year,
            "beginning_carrying_amount": beginning,
            "cash_interest": CASH_INTEREST,
            "interest_expense": interest_expense,
            "discount_amortization": amortization,
            "ending_carrying_amount": ending,
        }
    )
    carrying = ending

# Internal consistency guards (not reported figures).
assert schedule[-1]["ending_carrying_amount"] == FACE.quantize(CENT), "schedule must retire to face"
assert cents(sum(r["discount_amortization"] for r in schedule)) == discount_on_note, \
    "total amortization must equal the original discount"
for r in schedule:
    assert cents(r["beginning_carrying_amount"] + r["discount_amortization"]) == r["ending_carrying_amount"]
    assert cents(r["cash_interest"] + r["discount_amortization"]) == r["interest_expense"]

y1, y2, y3 = schedule

# ---------------------------------------------------------------------------
# Journal entries
# ---------------------------------------------------------------------------
ZERO = Decimal("0")


def line(account, debit=ZERO, credit=ZERO):
    return {"account": account, "debit": f(debit), "credit": f(credit)}


journal_entries = [
    {
        # (b) Initial recognition, January 1, Year 1
        "part": "b",
        "date": "Year 1 January 1",
        "description": "Issuance of 3-year, 5% note payable at a discount (9% market rate)",
        "lines": [
            line("Cash", debit=issue_price),
            line("Discount on Notes Payable", debit=discount_on_note),
            line("Notes Payable", credit=FACE),
        ],
    },
    {
        # (d) Period-end interest, December 31, Year 1
        "part": "d",
        "date": "Year 1 December 31",
        "description": "Annual interest payment and discount amortization (effective interest method)",
        "lines": [
            line("Interest Expense", debit=y1["interest_expense"]),
            line("Discount on Notes Payable", credit=y1["discount_amortization"]),
            line("Cash", credit=CASH_INTEREST),
        ],
    },
    {
        # (e) Final period-end interest, December 31, Year 3
        "part": "e",
        "date": "Year 3 December 31",
        "description": "Final annual interest payment and discount amortization (final-period plug)",
        "lines": [
            line("Interest Expense", debit=y3["interest_expense"]),
            line("Discount on Notes Payable", credit=y3["discount_amortization"]),
            line("Cash", credit=CASH_INTEREST),
        ],
    },
    {
        # (e) Maturity settlement of principal, December 31, Year 3
        "part": "e",
        "date": "Year 3 December 31",
        "description": "Maturity settlement of note principal",
        "lines": [
            line("Notes Payable", debit=FACE),
            line("Cash", credit=FACE),
        ],
    },
]

for je in journal_entries:
    td = sum(Decimal(str(l["debit"])) for l in je["lines"])
    tc = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert cents(td) == cents(tc), f"entry {je['part']} {je['description']} is out of balance"

# ---------------------------------------------------------------------------
# Reported answers — only figures the Required parts ask for.
#   (a) -> issue price
#   (c) -> the schedule's cash interest / interest expense / amortization /
#          carrying amount for each of the 3 years
# (b), (d), (e) are journal entries and live in journal_entries.
# ---------------------------------------------------------------------------
answers = [
    {"label": "a: cash proceeds (issue price) of the note on January 1, Year 1", "value": f(issue_price)},
]

for r in schedule:
    y = r["year"]
    answers.extend(
        [
            {"label": f"c: Year {y} carrying amount at beginning of year", "value": f(r["beginning_carrying_amount"])},
            {"label": f"c: Year {y} cash interest paid", "value": f(r["cash_interest"])},
            {"label": f"c: Year {y} interest expense", "value": f(r["interest_expense"])},
            {"label": f"c: Year {y} discount amortization", "value": f(r["discount_amortization"])},
            {"label": f"c: Year {y} carrying amount at end of year", "value": f(r["ending_carrying_amount"])},
        ]
    )

notes = (
    "PV computed from the exact formula (80,000/1.09^3 + 4,000*(1-1.09^-3)/0.09) at 50-digit "
    "precision, rounded once to the cent = 71,899.86; discount = 8,100.14. The stem's instruction "
    "to 'round the present value to the nearest cent' rules out 5-decimal printed table factors "
    "(those would give 71,899.56), and the CH 16 course handout works notes with Excel PV()/RATE(), "
    "which are exact-formula. Schedule rounds interest expense to the cent each period before "
    "deriving amortization and the new carrying amount. Per Required (c), Year 3 is plugged: "
    "amortization forced to 80,000.00 - 77,064.23 = 2,935.77 so carrying amount retires exactly to "
    "face, making Year 3 interest expense 6,935.77 rather than the unplugged 6,935.78. Part (e) is "
    "shown as two entries (final interest, then principal settlement), which the stem permits."
)

output = {
    "id": "agent_016#00",
    "rounding_convention": (
        "decimal.Decimal throughout, ROUND_HALF_UP. PV from the exact discount formula at 50-digit "
        "internal precision, rounded once to the nearest cent (NOT 5-decimal table factors). "
        "Effective-interest schedule: interest expense = carrying amount x 9% rounded to the cent "
        "per period, then amortization and new carrying amount derived from that rounded figure; "
        "final period plugged so ending carrying amount equals face."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(output, indent=2))
