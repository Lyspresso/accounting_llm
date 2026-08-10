#!/usr/bin/env python3
"""
Solver for item agent_145#02 -- Cascade Brewing Co., straight-line discount
amortization on a 3-year, $100,000 face, 8% annual-coupon bond issued 1/1/Yr1
for $95,026 (market yield 10%), interest paid each 12/31, maturing 12/31/Yr3.

ROUNDING CONVENTION
-------------------
- All money is decimal.Decimal. No floats appear anywhere in this module.
- Money is carried and reported to whole dollars, quantized with
  ROUND_HALF_UP, applied PER PERIOD (not once at the end). This matches the
  course's straight-line schedules (Demo 16-4B), which round each period's
  amortization and then let the final period absorb the residual.
- Straight-line amortization per period = total discount / number of periods,
  rounded HALF_UP per period. The FINAL period is a plug equal to the
  remaining unamortized discount so that (a) the discount is exactly fully
  amortized, (b) ending carrying amount is exactly face value, and (c) the
  sum of the periodic amortizations equals the initial discount. Here
  $4,974 / 3 = $1,658 divides evenly, so the plug equals the regular amount
  and no rounding residual arises; the logic is implemented generally anyway.
- No present-value work is required: the issue price is given in the stem, so
  no PV table factor vs. exact-formula choice arises. The 10% market yield is
  contextual only -- under the straight-line interest method it does not enter
  any computed figure.
- Interest expense per period = cash interest + discount amortized for that
  period (textbook straight-line relation: A + C).

Every reported figure is derived from the stem's raw facts (face, stated rate,
proceeds, term, payment frequency). Nothing is hard-coded from the stem's
bullet list of pre-computed hints.

Run: python3 solver.py    ->    one JSON object on stdout
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("1")  # whole dollars; this problem's amounts are whole dollars


def money(x: Decimal) -> Decimal:
    """Quantize to whole dollars using ROUND_HALF_UP (applied per period)."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly number: int when integral, else float-free string-safe."""
    if x == x.to_integral_value():
        return int(x)
    return float(x)  # not reached for this item; money stays whole-dollar


# ---------------------------------------------------------------------------
# Raw facts from the stem (nothing else is assumed)
# ---------------------------------------------------------------------------
FACE = Decimal("100000")
STATED_RATE = Decimal("8") / Decimal("100")      # 8% annual
PROCEEDS = Decimal("95026")                      # issue price 1/1/Year 1
PAYMENTS_PER_YEAR = 1                            # interest paid annually 12/31
TERM_YEARS = 3                                   # 1/1/Yr1 -> 12/31/Yr3
N_PERIODS = TERM_YEARS * PAYMENTS_PER_YEAR

# ---------------------------------------------------------------------------
# Derived core quantities
# ---------------------------------------------------------------------------
initial_discount = money(FACE - PROCEEDS)                       # 4,974
cash_interest = money(FACE * STATED_RATE / Decimal(PAYMENTS_PER_YEAR))  # 8,000
regular_amort = money(initial_discount / Decimal(N_PERIODS))    # 1,658

# ---------------------------------------------------------------------------
# Part b -- straight-line amortization schedule, Years 1-3
# Columns mirror the course schedule: Cash (stated interest), Interest Expense,
# Discount Amortization, Unamortized Discount (end), Carrying Amount (end).
# ---------------------------------------------------------------------------
schedule = []
unamortized = initial_discount
carrying = money(FACE - unamortized)

# opening row (issuance date)
schedule.append({
    "period": "January 1, Year 1 (issuance)",
    "cash_interest": None,
    "interest_expense": None,
    "discount_amortization": None,
    "unamortized_discount_end": num(unamortized),
    "carrying_amount_end": num(carrying),
})

for period in range(1, N_PERIODS + 1):
    if period == N_PERIODS:
        amort = unamortized          # final period plugs the residual
    else:
        amort = regular_amort
    expense = money(cash_interest + amort)
    unamortized = money(unamortized - amort)
    carrying = money(FACE - unamortized)
    schedule.append({
        "period": f"December 31, Year {period}",
        "cash_interest": num(cash_interest),
        "interest_expense": num(expense),
        "discount_amortization": num(amort),
        "unamortized_discount_end": num(unamortized),
        "carrying_amount_end": num(carrying),
    })

# integrity checks on the derivation (not reported as answers)
assert unamortized == Decimal("0"), "discount must be fully amortized at maturity"
assert carrying == FACE, "carrying amount must equal face at maturity"
paid_rows = [r for r in schedule if r["discount_amortization"] is not None]
assert sum(Decimal(str(r["discount_amortization"])) for r in paid_rows) == initial_discount

# ---------------------------------------------------------------------------
# Answers -- exactly what the Required parts ask for
# ---------------------------------------------------------------------------
answers = []
for row in schedule:
    if row["cash_interest"] is None:
        answers.append({
            "label": "b: carrying amount at issuance (Jan 1, Year 1)",
            "value": row["carrying_amount_end"],
        })
        answers.append({
            "label": "b: unamortized discount at issuance (Jan 1, Year 1)",
            "value": row["unamortized_discount_end"],
        })
        continue
    yr = row["period"]
    answers.append({"label": f"b: {yr} - cash interest paid",
                    "value": row["cash_interest"]})
    answers.append({"label": f"b: {yr} - discount amortization",
                    "value": row["discount_amortization"]})
    answers.append({"label": f"b: {yr} - interest expense",
                    "value": row["interest_expense"]})
    answers.append({"label": f"b: {yr} - unamortized discount, end of year",
                    "value": row["unamortized_discount_end"]})
    answers.append({"label": f"b: {yr} - carrying amount, end of year",
                    "value": row["carrying_amount_end"]})

answers.append({
    "label": ("e: Under ASC 835-30, when is straight-line acceptable and where "
              "is unamortized discount reported?"),
    "value": (
        "GAAP requires the effective interest ('interest') method; ASC 835-30-55-2 "
        "permits an alternative such as the straight-line interest method only when "
        "its results are not materially different from the effective interest method "
        "(as assumed here). Straight-line may not be used if the results differ "
        "materially. The unamortized Discount on Bonds Payable is a contra-liability, "
        "not an asset: it is reported on the balance sheet as a direct deduction from "
        "the $100,000 face amount of Bonds Payable, so only the net carrying amount "
        "($96,684 at end of Year 1 and $98,342 at end of Year 2; $0 discount remains "
        "at maturity) appears as the long-term liability. Amortization of the discount "
        "is reported as interest expense (ASC 835-30-45-3)."
    ),
})

# ---------------------------------------------------------------------------
# Journal entries -- parts a, c, d
# ---------------------------------------------------------------------------
y1 = schedule[1]
y2 = schedule[2]
y3 = schedule[3]

journal_entries = [
    {
        "part": "a",
        "date": "January 1, Year 1",
        "description": "Issuance of bonds at a discount",
        "lines": [
            {"account": "Cash", "debit": num(PROCEEDS), "credit": 0},
            {"account": "Discount on Bonds Payable",
             "debit": num(initial_discount), "credit": 0},
            {"account": "Bonds Payable", "debit": 0, "credit": num(FACE)},
        ],
    },
    {
        "part": "c",
        "date": "December 31, Year 1",
        "description": "Annual interest payment and straight-line discount amortization",
        "lines": [
            {"account": "Interest Expense",
             "debit": y1["interest_expense"], "credit": 0},
            {"account": "Discount on Bonds Payable",
             "debit": 0, "credit": y1["discount_amortization"]},
            {"account": "Cash", "debit": 0, "credit": y1["cash_interest"]},
        ],
    },
    {
        "part": "c",
        "date": "December 31, Year 2",
        "description": "Annual interest payment and straight-line discount amortization",
        "lines": [
            {"account": "Interest Expense",
             "debit": y2["interest_expense"], "credit": 0},
            {"account": "Discount on Bonds Payable",
             "debit": 0, "credit": y2["discount_amortization"]},
            {"account": "Cash", "debit": 0, "credit": y2["cash_interest"]},
        ],
    },
    {
        "part": "d",
        "date": "December 31, Year 3",
        "description": ("Final annual interest payment and final straight-line "
                        "discount amortization (discount now fully amortized)"),
        "lines": [
            {"account": "Interest Expense",
             "debit": y3["interest_expense"], "credit": 0},
            {"account": "Discount on Bonds Payable",
             "debit": 0, "credit": y3["discount_amortization"]},
            {"account": "Cash", "debit": 0, "credit": y3["cash_interest"]},
        ],
    },
    {
        "part": "d",
        "date": "December 31, Year 3",
        "description": "Derecognition of bonds payable at maturity (repayment of face)",
        "lines": [
            {"account": "Bonds Payable", "debit": num(FACE), "credit": 0},
            {"account": "Cash", "debit": 0, "credit": num(FACE)},
        ],
    },
]

for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, f"unbalanced entry: part {je['part']} {je['date']}"

result = {
    "id": "agent_145#02",
    "rounding_convention": (
        "decimal.Decimal only, no floats; whole dollars, ROUND_HALF_UP applied per "
        "period; straight-line amortization = total discount / number of periods with "
        "the final period plugged to the remaining unamortized discount so the "
        "discount fully amortizes and carrying amount equals face at maturity "
        "($4,974 / 3 = $1,658 divides evenly, so no residual arises here). No PV "
        "factors needed -- the issue price is given."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Part b is the schedule itself, so all of its columns are reported as answers. "
        "Part e is qualitative and is reported as a text answer. The 10% market yield "
        "is contextual only: under the straight-line interest method it does not enter "
        "any computed amount. Interest expense is $9,658 in each of Years 1-3 and "
        "total interest expense over the term is $28,974 (= $24,000 cash + $4,974 "
        "discount)."
    ),
}

print(json.dumps(result, indent=2))
