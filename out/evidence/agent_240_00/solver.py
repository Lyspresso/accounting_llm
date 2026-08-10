#!/usr/bin/env python3
"""Blind solver — agent_240#00.

Rivertide Precision Tools: mandatorily redeemable preferred stock (ASC 480).
Fixed redemption amount ($199,650) on a fixed date (12/31/Year 3) and not solely
upon liquidation => the instrument is a LIABILITY at issuance, measured at the
$150,000 proceeds and accreted to the redemption amount using the effective
interest method at the 10% implicit rate.

Rounding convention
-------------------
decimal.Decimal throughout; no binary floats anywhere.
ROUND_HALF_UP to the cent, applied PER PERIOD (each year's interest expense is
rounded before it is added to the carrying amount, so the following year's
interest is computed on the rounded carrying amount). No PV table factors are
needed: the effective rate (10%) is given, so interest = beginning carrying
amount x 10% each year. The final period's interest is taken as the plug that
brings the carrying amount exactly to the contractual redemption amount, which
is standard effective-interest practice; here the plug and the rate-computed
figure agree to the cent (150,000 x 1.10^3 = 199,650 exactly), so no rounding
difference arises.

Run: python3 solver.py   -> prints one JSON object on stdout.
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def r(x: Decimal) -> Decimal:
    """ROUND_HALF_UP to the cent."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly: int when the value is a whole number of dollars."""
    x = r(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ----------------------------------------------------------------- fact pattern
PROCEEDS = Decimal("150000")        # cash received 1/1/Year 1
REDEMPTION = Decimal("199650")      # mandatory cash redemption 12/31/Year 3
RATE = Decimal("0.10")              # implicit effective interest rate
YEARS = 3

# -------------------------------------------- b. subsequent measurement schedule
schedule = []
carrying = PROCEEDS
for year in range(1, YEARS + 1):
    beginning = carrying
    if year < YEARS:
        interest = r(beginning * RATE)
        ending = r(beginning + interest)
    else:
        # final period: accrete exactly to the contractual redemption amount
        ending = REDEMPTION
        interest = r(ending - beginning)
    schedule.append(
        {
            "year": year,
            "beginning_carrying_amount": num(beginning),
            "interest_expense": num(interest),
            "ending_carrying_amount": num(ending),
        }
    )
    carrying = ending

# internal consistency: rate-computed final-year interest must match the plug
_rate_based_final = r(schedule[-1]["beginning_carrying_amount"] * RATE)
assert _rate_based_final == Decimal(str(schedule[-1]["interest_expense"])), (
    "final-year plug differs from rate-computed interest"
)
assert carrying == REDEMPTION, "schedule does not accrete to the redemption amount"

y1 = Decimal(str(schedule[0]["interest_expense"]))
y2 = Decimal(str(schedule[1]["interest_expense"]))
y3 = Decimal(str(schedule[2]["interest_expense"]))

# --------------------------------------------------------------- e. reconciliation
total_interest = r(y1 + y2 + y3)
discount_accreted = r(REDEMPTION - PROCEEDS)
assert total_interest == discount_accreted, "interest total != redemption - proceeds"

LIAB = "Mandatorily Redeemable Preferred Stock (liability)"


def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


journal_entries = [
    {
        "part": "a",
        "date": "January 1, Year 1",
        "description": "Initial recognition of mandatorily redeemable preferred "
                       "stock at proceeds received (ASC 480 liability)",
        "lines": [
            line("Cash", debit=PROCEEDS),
            line(LIAB, credit=PROCEEDS),
        ],
    },
    {
        "part": "c",
        "date": "December 31, Year 1",
        "description": "Interest accretion, Year 1 (10% x $150,000)",
        "lines": [
            line("Interest Expense", debit=y1),
            line(LIAB, credit=y1),
        ],
    },
    {
        "part": "c",
        "date": "December 31, Year 2",
        "description": "Interest accretion, Year 2 (10% x $165,000)",
        "lines": [
            line("Interest Expense", debit=y2),
            line(LIAB, credit=y2),
        ],
    },
    {
        "part": "d",
        "date": "December 31, Year 3",
        "description": "Interest accretion, Year 3 (10% x $181,500)",
        "lines": [
            line("Interest Expense", debit=y3),
            line(LIAB, credit=y3),
        ],
    },
    {
        "part": "d",
        "date": "December 31, Year 3",
        "description": "Mandatory redemption / settlement at maturity",
        "lines": [
            line(LIAB, debit=REDEMPTION),
            line("Cash", credit=REDEMPTION),
        ],
    },
]

for je in journal_entries:
    d = sum((Decimal(str(l["debit"])) for l in je["lines"]), Decimal("0"))
    c = sum((Decimal(str(l["credit"])) for l in je["lines"]), Decimal("0"))
    assert d == c, f"unbalanced entry: part {je['part']} {je['date']}"

classification = (
    "Liability, not equity. Because redemption is mandatory for a fixed amount "
    "on a fixed date (not solely upon liquidation), ASC 480 requires the "
    "instrument to be reported as a liability despite its legal form as "
    "preferred shares. Immediately after the January 1, Year 1 issuance it is a "
    "NONCURRENT liability of $150,000 (redemption is more than one year away); "
    "it becomes current during Year 3."
)

answers = [
    {"label": "a: liability recognized at issuance (Jan 1, Year 1)",
     "value": num(PROCEEDS)},
    {"label": "a: balance-sheet classification immediately after issuance",
     "value": classification},

    {"label": "b: Year 1 beginning carrying amount",
     "value": schedule[0]["beginning_carrying_amount"]},
    {"label": "b: Year 1 interest expense",
     "value": schedule[0]["interest_expense"]},
    {"label": "b: Year 1 ending carrying amount",
     "value": schedule[0]["ending_carrying_amount"]},

    {"label": "b: Year 2 beginning carrying amount",
     "value": schedule[1]["beginning_carrying_amount"]},
    {"label": "b: Year 2 interest expense",
     "value": schedule[1]["interest_expense"]},
    {"label": "b: Year 2 ending carrying amount",
     "value": schedule[1]["ending_carrying_amount"]},

    {"label": "b: Year 3 beginning carrying amount",
     "value": schedule[2]["beginning_carrying_amount"]},
    {"label": "b: Year 3 interest expense",
     "value": schedule[2]["interest_expense"]},
    {"label": "b: Year 3 ending carrying amount",
     "value": schedule[2]["ending_carrying_amount"]},

    {"label": "c: Dec 31, Year 1 interest accretion recorded",
     "value": num(y1)},
    {"label": "c: Dec 31, Year 2 interest accretion recorded",
     "value": num(y2)},

    {"label": "d: Dec 31, Year 3 interest accretion recorded",
     "value": num(y3)},
    {"label": "d: cash paid at maturity settlement",
     "value": num(REDEMPTION)},

    {"label": "e: total interest expense over the three-year life",
     "value": num(total_interest)},
    {"label": "e: redemption amount minus issue proceeds "
              "(199,650 - 150,000), equals total interest expense",
     "value": num(discount_accreted)},
]

out = {
    "id": "agent_240#00",
    "rounding_convention": (
        "decimal.Decimal only (no floats); ROUND_HALF_UP to the cent applied per "
        "period, so each year's rounded interest expense rolls into the next "
        "year's beginning carrying amount. Effective rate given (10%), so no PV "
        "table factors used; final year accreted to the contractual $199,650 "
        "(plug matches the 10% computation exactly, $0.00 rounding difference)."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "ASC 480: mandatorily redeemable preferred with a fixed amount and fixed "
        "date is a liability; periodic accretion is interest expense, not a "
        "dividend. Dividends ignored per the stem. 150,000 x 1.10^3 = 199,650, "
        "confirming the 10% implicit rate is internally consistent with the "
        "stated proceeds and redemption price."
    ),
}

print(json.dumps(out, indent=2))
