#!/usr/bin/env python3
"""Solver for agent_279#01 -- Copper Ridge Utilities bonds (LO 16-7).

FACT PATTERN (from stem.md, nothing else)
-----------------------------------------
Jan 1 Year 1: issued $400,000 face, 4-year, 6% bonds; cash interest paid
annually each Dec 31; priced to yield 8%; sold for $373,503 (discount $26,497).
Effective-interest method; Dec 31 year-end.

Dec 31 Year 2: AFTER the period-end interest entry and the cash interest
payment, 50% of the bonds are retired in the open market at 103. The remaining
50% is held to maturity (Dec 31 Year 4).

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP to the nearest whole dollar, applied PER PERIOD (round-per-period,
not round-at-end). Interest expense for each period is computed as
    beginning carrying value x 8% effective rate
and rounded to whole dollars at that moment; the discount amortization for the
period is then the PLUG (rounded interest expense - cash interest), exactly as
the course handout prescribes for the effective-interest method. Each period's
rounded carrying value carries forward as the next period's base. Cash interest
is exact (400,000 x 6% = 24,000), so no rounding is needed there.

No PV table factors are used: the issue price ($373,503) is GIVEN in the stem,
so the schedule is built forward from that given figure. Nothing is hard-coded
that the script does not itself derive from the fact-pattern inputs below.

The retired half is carried forward on its own half-sized schedule after the
Dec 31 Year 2 retirement: the remaining 50% has a beginning carrying value equal
to 50% of the Dec 31 Year 2 carrying value, and its Year 3 / Year 4 interest
expense is that half-carrying-value x 8%, rounded per period the same way.

Run: python3 solver.py    (prints one JSON object on stdout)
"""

import json
from decimal import Decimal, ROUND_HALF_UP

# ---------------------------------------------------------------- inputs ----
FACE = Decimal("400000")
STATED_RATE = Decimal("0.06")
EFFECTIVE_RATE = Decimal("0.08")
TERM_YEARS = 4
ISSUE_PRICE = Decimal("373503")
DISCOUNT_AT_ISSUE = Decimal("26497")
RETIRE_FRACTION = Decimal("0.50")
CALL_PRICE_PCT = Decimal("103") / Decimal("100")  # "at 103" = 103% of face
RETIREMENT_AFTER_PERIOD = 2  # Dec 31, Year 2, after that period's interest

CENT = Decimal("1")  # whole dollars


def r(x):
    """ROUND_HALF_UP to the nearest whole dollar."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def money(x):
    """JSON-safe plain number (whole dollars)."""
    return int(x)


# --------------------------------------------------- internal consistency ---
assert FACE - ISSUE_PRICE == DISCOUNT_AT_ISSUE, "stem discount does not tie"

CASH_INTEREST = r(FACE * STATED_RATE)  # 24,000 each Dec 31


# ------------------------------------------- (b) amortization schedule ------
def build_schedule(begin_cv, face, stated_rate, eff_rate, periods):
    """Effective-interest schedule, round-per-period, amortization as plug."""
    rows = []
    cv = begin_cv
    cash = r(face * stated_rate)
    for period in range(1, periods + 1):
        exp = r(cv * eff_rate)
        amort = exp - cash
        end_cv = cv + amort
        rows.append(
            {
                "period": period,
                "beginning_carrying_value": cv,
                "cash_interest": cash,
                "interest_expense": exp,
                "discount_amortized": amort,
                "ending_carrying_value": end_cv,
            }
        )
        cv = end_cv
    return rows


schedule = build_schedule(
    ISSUE_PRICE, FACE, STATED_RATE, EFFECTIVE_RATE, TERM_YEARS
)

# The schedule must self-close: total amortization = discount, CV -> face.
total_amort = sum((row["discount_amortized"] for row in schedule), Decimal("0"))
assert total_amort == DISCOUNT_AT_ISSUE, f"amortization {total_amort} != discount"
assert schedule[-1]["ending_carrying_value"] == FACE, "CV does not reach face"


# ------------------------------------------------- (c) 50% extinguishment ---
cv_at_retirement = schedule[RETIREMENT_AFTER_PERIOD - 1]["ending_carrying_value"]
unamortized_discount = FACE - cv_at_retirement

face_retired = r(FACE * RETIRE_FRACTION)
cv_retired = r(cv_at_retirement * RETIRE_FRACTION)
discount_retired = face_retired - cv_retired  # removed contra-account share
cash_paid = r(face_retired * CALL_PRICE_PCT)

# Reacquisition price > carrying value => LOSS (handout LO16-7 step 3).
gain_loss = cv_retired - cash_paid  # negative = loss
loss_on_retirement = -gain_loss

assert discount_retired == r(unamortized_discount * RETIRE_FRACTION)


# ----------------------- (d) remaining half: Year 3, Year 4, and maturity ---
face_remaining = FACE - face_retired
cv_remaining_start = cv_at_retirement - cv_retired
cash_interest_half = r(face_remaining * STATED_RATE)

half_rows = []
cv = cv_remaining_start
for period in range(RETIREMENT_AFTER_PERIOD + 1, TERM_YEARS + 1):
    exp = r(cv * EFFECTIVE_RATE)
    amort = exp - cash_interest_half
    cv = cv + amort
    half_rows.append(
        {
            "period": period,
            "cash_interest": cash_interest_half,
            "interest_expense": exp,
            "discount_amortized": amort,
            "ending_carrying_value": cv,
        }
    )

assert half_rows[-1]["ending_carrying_value"] == face_remaining, (
    "remaining half CV does not reach its face"
)


# --------------------------------------------------------- journal entries --
def entry(part, date, lines):
    dr = sum((ln["debit"] for ln in lines), Decimal("0"))
    cr = sum((ln["credit"] for ln in lines), Decimal("0"))
    assert dr == cr, f"{part} {date}: debits {dr} != credits {cr}"
    return {
        "part": part,
        "date": date,
        "lines": [
            {
                "account": ln["account"],
                "debit": money(ln["debit"]),
                "credit": money(ln["credit"]),
            }
            for ln in lines
        ],
    }


def dr(account, amount):
    return {"account": account, "debit": amount, "credit": Decimal("0")}


def cr(account, amount):
    return {"account": account, "debit": Decimal("0"), "credit": amount}


journal_entries = []

# (a) Issuance, January 1, Year 1
journal_entries.append(
    entry(
        "a",
        "January 1, Year 1",
        [
            dr("Cash", ISSUE_PRICE),
            dr("Discount on Bonds Payable", DISCOUNT_AT_ISSUE),
            cr("Bonds Payable", FACE),
        ],
    )
)

# (c) December 31, Year 2 -- period-end interest on the full $400,000
y2 = schedule[RETIREMENT_AFTER_PERIOD - 1]
journal_entries.append(
    entry(
        "c",
        "December 31, Year 2 - interest",
        [
            dr("Interest Expense", y2["interest_expense"]),
            cr("Discount on Bonds Payable", y2["discount_amortized"]),
            cr("Cash", y2["cash_interest"]),
        ],
    )
)

# (c) December 31, Year 2 -- retirement of 50% at 103
journal_entries.append(
    entry(
        "c",
        "December 31, Year 2 - retire 50% at 103",
        [
            dr("Bonds Payable", face_retired),
            dr("Loss on Redemption of Bonds", loss_on_retirement),
            cr("Discount on Bonds Payable", discount_retired),
            cr("Cash", cash_paid),
        ],
    )
)

# (d) Year 3 and Year 4 interest on the remaining half
for row in half_rows:
    journal_entries.append(
        entry(
            "d",
            f"December 31, Year {row['period']} - interest (remaining 50%)",
            [
                dr("Interest Expense", row["interest_expense"]),
                cr("Discount on Bonds Payable", row["discount_amortized"]),
                cr("Cash", row["cash_interest"]),
            ],
        )
    )

# (d) Maturity of the remaining half, December 31, Year 4
journal_entries.append(
    entry(
        "d",
        "December 31, Year 4 - maturity (remaining 50%)",
        [
            dr("Bonds Payable", face_remaining),
            cr("Cash", face_remaining),
        ],
    )
)


# ---------------------------------------------------------------- answers ---
answers = []

# (b) full effective-interest amortization schedule, Years 1-4
for row in schedule:
    y = row["period"]
    answers.append(
        {
            "label": f"b: Year {y} cash interest",
            "value": money(row["cash_interest"]),
        }
    )
    answers.append(
        {
            "label": f"b: Year {y} interest expense",
            "value": money(row["interest_expense"]),
        }
    )
    answers.append(
        {
            "label": f"b: Year {y} discount amortized",
            "value": money(row["discount_amortized"]),
        }
    )
    answers.append(
        {
            "label": f"b: Year {y} ending carrying value",
            "value": money(row["ending_carrying_value"]),
        }
    )

# (c) gain/loss computation on the 50% extinguishment
answers.append(
    {
        "label": "c: carrying value of the 50% retired (Dec 31, Year 2)",
        "value": money(cv_retired),
    }
)
answers.append(
    {"label": "c: reacquisition price paid (50% at 103)", "value": money(cash_paid)}
)
answers.append(
    {
        "label": "c: loss on extinguishment of 50% of the bonds",
        "value": money(loss_on_retirement),
    }
)

# (d) remaining-half interest amounts, Years 3 and 4
for row in half_rows:
    y = row["period"]
    answers.append(
        {
            "label": f"d: Year {y} interest expense (remaining 50%)",
            "value": money(row["interest_expense"]),
        }
    )
    answers.append(
        {
            "label": f"d: Year {y} discount amortized (remaining 50%)",
            "value": money(row["discount_amortized"]),
        }
    )
    answers.append(
        {
            "label": f"d: Year {y} cash interest (remaining 50%)",
            "value": money(row["cash_interest"]),
        }
    )
answers.append(
    {
        "label": "d: cash paid at maturity, December 31, Year 4 (remaining 50%)",
        "value": money(face_remaining),
    }
)


output = {
    "id": "agent_279#01",
    "rounding_convention": (
        "ROUND_HALF_UP to whole dollars, applied per period (round-per-period). "
        "Interest expense = beginning carrying value x 8% effective rate, rounded "
        "each period; discount amortization is the plug (expense - cash interest); "
        "each rounded carrying value carries forward. Issue price is given in the "
        "stem, so no PV table factors are used."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Schedule self-closes: the four periods' amortization sums to the given "
        "$26,497 discount and carrying value reaches $400,000 at Dec 31 Year 4 with "
        "no plug. Retirement is recorded after the Dec 31 Year 2 interest entry, so "
        "carrying value is 385,734; half of that (192,867) versus 206,000 paid gives "
        "a loss. The remaining 50% is amortized on its own half-sized schedule "
        "(192,867 x 8% in Year 3), which closes exactly to 200,000 at maturity."
    ),
}

print(json.dumps(output, indent=2))
