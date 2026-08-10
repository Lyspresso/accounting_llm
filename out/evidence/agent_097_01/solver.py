#!/usr/bin/env python3
"""
Blind solver for item agent_097#01.

QUESTION (paraphrased from stem.md, LO 15-4):
    Oakridge Supply Inc. borrows cash on August 1, Year 1 on a 10-month,
    interest-bearing note. Face / cash proceeds = $120,000. Stated annual rate
    = market = 8%. All cash interest is paid at maturity (May 31, Year 2) with
    principal. Fiscal year-end is December 31.

    Required:
      a. Record the August 1, Year 1 issuance.
      b. Interest schedule: Year 1 accrual months, Year 2 remaining months,
         total term interest.
      c. Record the December 31, Year 1 adjusting entry.
      d. Year 1 balance sheet amounts for Notes Payable and Interest Payable.
      e. Record the May 31, Year 2 settlement entry.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; no binary floats are used anywhere.

Interest is accrued on a MONTHS-OUT-OF-12 basis (the textbook convention for a
note stated in months rather than days):

        interest for a stretch = Face x Annual rate x (months / 12)

Each reporting stretch (Year 1 accrual period, Year 2 remaining period) is
computed and rounded INDEPENDENTLY at the moment it is recognized -- i.e.
ROUND_HALF_UP to the cent PER PERIOD, not rounded once at the end. Total term
interest is then the SUM of the already-rounded period amounts, so the
schedule foots exactly and the maturity cash payment equals principal plus the
sum of the amounts actually recorded. (Here every figure is exact to the cent
anyway -- $800.00 per month -- so the convention changes nothing numerically,
but it is applied deliberately rather than by accident.)

Because the note carries a stated rate equal to the market rate, it is recorded
at face; there is no discount or premium and no present-value factor is needed.

Balance-sheet classification: at December 31, Year 1 the note matures May 31,
Year 2, which is within twelve months of the balance sheet date, so both the
note and the accrued interest are CURRENT liabilities presented at face /
accrued amount (interest-bearing note -- no discount contra account).

Run:  python3 solver.py      (prints one JSON object to stdout)
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Round a Decimal to the cent, ROUND_HALF_UP. Applied per period."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def out(x: Decimal):
    """JSON-friendly number: int when the cents are zero, else float-free str."""
    x = money(x)
    return int(x) if x == x.to_integral_value() else float(x)


def months_between(y1: int, m1: int, y2: int, m2: int) -> int:
    """Whole months from the first day of (y1,m1) through the last day of (y2,m2)."""
    return (y2 - y1) * 12 + (m2 - m1) + 1


# ---------------------------------------------------------------------------
# Facts taken from the stem (nothing below is a hard-coded answer)
# ---------------------------------------------------------------------------
FACE = Decimal("120000")          # cash proceeds / face of note
ANNUAL_RATE = Decimal("8") / Decimal("100")   # 8% stated = market

# Issuance August 1, Year 1 (treat "Year 1" as relative year 1).
ISSUE_Y, ISSUE_M = 1, 8
# Maturity May 31, Year 2.
MATURITY_Y, MATURITY_M = 2, 5
# Fiscal year-end December 31.
FYE_M = 12

# ---------------------------------------------------------------------------
# Term decomposition
# ---------------------------------------------------------------------------
total_months = months_between(ISSUE_Y, ISSUE_M, MATURITY_Y, MATURITY_M)   # 10

# Year 1 accrual stretch: Aug 1, Year 1 -> Dec 31, Year 1
year1_months = months_between(ISSUE_Y, ISSUE_M, ISSUE_Y, FYE_M)           # 5
# Year 2 remaining stretch: Jan 1, Year 2 -> May 31, Year 2
year2_months = total_months - year1_months                               # 5

assert total_months == 10, "term should be the stated 10 months"
assert year1_months + year2_months == total_months

# ---------------------------------------------------------------------------
# Interest, rounded per period (ROUND_HALF_UP)
# ---------------------------------------------------------------------------
monthly_rate_fraction = Decimal(1) / Decimal(12)

year1_interest = money(FACE * ANNUAL_RATE * (Decimal(year1_months) * monthly_rate_fraction))
year2_interest = money(FACE * ANNUAL_RATE * (Decimal(year2_months) * monthly_rate_fraction))
total_interest = year1_interest + year2_interest      # sum of rounded periods

# ---------------------------------------------------------------------------
# Balances / cash flows
# ---------------------------------------------------------------------------
notes_payable_bs = FACE               # recorded at face; stated rate = market
interest_payable_bs = year1_interest  # accrued but unpaid at 12/31 Year 1
cash_at_maturity = FACE + total_interest

# ---------------------------------------------------------------------------
# Journal entries
# ---------------------------------------------------------------------------
def line(account, debit=Decimal(0), credit=Decimal(0)):
    return {"account": account, "debit": out(debit), "credit": out(credit)}


je_a = {
    "part": "a",
    "date": "August 1, Year 1",
    "lines": [
        line("Cash", debit=FACE),
        line("Notes Payable", credit=FACE),
    ],
}

je_c = {
    "part": "c",
    "date": "December 31, Year 1",
    "lines": [
        line("Interest Expense", debit=year1_interest),
        line("Interest Payable", credit=year1_interest),
    ],
}

je_e = {
    "part": "e",
    "date": "May 31, Year 2",
    "lines": [
        line("Notes Payable", debit=FACE),
        line("Interest Payable", debit=year1_interest),
        line("Interest Expense", debit=year2_interest),
        line("Cash", credit=cash_at_maturity),
    ],
}

journal_entries = [je_a, je_c, je_e]

for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, f"entry {je['part']} does not balance: {dr} vs {cr}"

# ---------------------------------------------------------------------------
# Answers -- only the figures the Required parts ask for (b and d)
# ---------------------------------------------------------------------------
answers = [
    {"label": "b: Year 1 interest (Aug 1 - Dec 31, Year 1)", "value": out(year1_interest)},
    {"label": "b: Year 2 interest (Jan 1 - May 31, Year 2)", "value": out(year2_interest)},
    {"label": "b: total interest over the 10-month term", "value": out(total_interest)},
    {"label": "d: Notes Payable on the December 31, Year 1 balance sheet (current liability)",
     "value": out(notes_payable_bs)},
    {"label": "d: Interest Payable on the December 31, Year 1 balance sheet (current liability)",
     "value": out(interest_payable_bs)},
]

result = {
    "id": "agent_097#01",
    "rounding_convention": (
        "decimal.Decimal throughout; ROUND_HALF_UP to the cent applied PER PERIOD "
        "(each reporting stretch rounded when recognized), total term interest = sum of "
        "the rounded period amounts; interest accrued months/12 (Face x rate x months/12); "
        "note recorded at face since stated rate = market, so no PV factor is used."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Term splits 5 months in Year 1 (Aug-Dec) and 5 months in Year 2 (Jan-May), "
        "10 months total, matching the stated 10-month term. Interest is cash-paid only "
        "at maturity, so Year 1 interest sits in Interest Payable at 12/31/Yr1 and is "
        "cleared in the May 31, Year 2 settlement. Both liabilities are current at "
        "12/31/Yr1 because maturity is within twelve months."
    ),
}

print(json.dumps(result, indent=2))
