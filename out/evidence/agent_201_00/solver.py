#!/usr/bin/env python3
"""Blind solver for item agent_201#00 -- Cedar Ridge Landfill LLC asset
retirement obligation (ARO): initial recognition, accretion schedule,
period-end adjusting entries, and settlement.

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP to the cent, applied *per period*, never at the end only.

  * Present value of the ARO is computed with the exact discount formula
    PV = FV / (1 + i)**n using decimal.Decimal arithmetic (no floats
    anywhere), then rounded ROUND_HALF_UP to the cent. Using the exact
    formula rather than a 5-place PV table factor matters here: the fact
    pattern was built so the PV is an exact figure, and a truncated table
    factor (0.62092) would introduce a spurious few-dollar error that would
    then propagate through five years of accretion.
  * Accretion expense for each year = (rounded beginning ARO balance) x 10%,
    itself rounded ROUND_HALF_UP to the cent before being added to the
    beginning balance. Each year's ending balance is therefore a rounded
    figure that becomes the next year's beginning balance (round-per-period,
    not round-at-end). This is what forces the schedule to close exactly on
    the undiscounted retirement cost.
  * Straight-line depreciation is computed per year as
    (depreciable base) / (useful life), rounded ROUND_HALF_UP to the cent.

All money is decimal.Decimal. Floats are never used for any monetary value.

FACT PATTERN (from the stem)
----------------------------
  Construction cost of the cell, already recorded ....... $8,500,000
  Undiscounted cost to dismantle and reclaim ............   $483,153
  Cash outflow date for the reclamation ................. Dec 31, Year 6
  ARO recognition date .................................. Dec 31, Year 1
  Credit-adjusted risk-free rate ........................         10%
  Cell placed in service ................................ Jan 1, Year 2
  Useful life / residual value .......................... 4 years / zero
  Cash actually paid to settle on Dec 31, Year 6 ........   $500,000

DERIVATION NOTES
----------------
  * Discount period is Dec 31 Year 1 -> Dec 31 Year 6 = 5 years, NOT the
    4-year useful life. The stem is explicit that the cash outflow occurs
    one year after the end of the cell's useful life, so the ARO keeps
    accreting for a sixth year (Year 6) after the asset is fully
    depreciated at the end of Year 5.
  * The ARO's present value is capitalized into the carrying amount of the
    landfill cell, so the depreciable base is 8,500,000 + PV, depreciated
    over the 4-year useful life (Years 2-5) -- NOT over the 5-year discount
    period. Depreciation and accretion run on different clocks by design.
  * Settlement loss = cash paid - ARO carrying amount at settlement, which
    by construction equals the undiscounted estimate once Year 6 accretion
    has been recorded.

Run:  python3 solver.py      (prints one JSON object to stdout)
"""

from decimal import Decimal, ROUND_HALF_UP
import json
import re

CENT = Decimal("0.01")


def money(value):
    """Round a Decimal to the cent using ROUND_HALF_UP."""
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------------------
# Given facts
# ---------------------------------------------------------------------------
CONSTRUCTION_COST = Decimal("8500000")   # already recorded, excludes the ARO
RETIREMENT_COST = Decimal("483153")      # undiscounted, due Dec 31 Year 6
RATE = Decimal("0.10")                   # credit-adjusted risk-free rate
YEARS_TO_SETTLEMENT = 5                  # Dec 31 Y1 -> Dec 31 Y6
USEFUL_LIFE = 4                          # years, Jan 1 Y2 -> Dec 31 Y5
RESIDUAL = Decimal("0")
CASH_PAID_AT_SETTLEMENT = Decimal("500000")

# ---------------------------------------------------------------------------
# (a) Present value of the ARO at December 31, Year 1
# ---------------------------------------------------------------------------
discount_divisor = (Decimal("1") + RATE) ** YEARS_TO_SETTLEMENT
aro_pv = money(RETIREMENT_COST / discount_divisor)

# ---------------------------------------------------------------------------
# (b) Full accretion schedule, Dec 31 Year 1 through Dec 31 Year 6
#     Round-per-period: each year's accretion is rounded before it rolls
#     into the next year's beginning balance.
# ---------------------------------------------------------------------------
schedule = []
balance = aro_pv
for offset in range(YEARS_TO_SETTLEMENT):
    year = 2 + offset                       # Year 2 through Year 6
    beginning = balance
    accretion = money(beginning * RATE)
    ending = money(beginning + accretion)
    schedule.append(
        {
            "date": "December 31, Year %d" % year,
            "year": year,
            "beginning_aro": beginning,
            "accretion_expense": accretion,
            "ending_aro": ending,
        }
    )
    balance = ending

aro_at_settlement = balance
total_accretion = money(sum((row["accretion_expense"] for row in schedule), Decimal("0")))

# ---------------------------------------------------------------------------
# Depreciation of the cell (Years 2-5); the capitalized ARO is part of cost
# ---------------------------------------------------------------------------
capitalized_cost = money(CONSTRUCTION_COST + aro_pv)
depreciable_base = money(capitalized_cost - RESIDUAL)
annual_depreciation = money(depreciable_base / Decimal(USEFUL_LIFE))
total_depreciation = money(annual_depreciation * Decimal(USEFUL_LIFE))

# ---------------------------------------------------------------------------
# (d) Settlement on December 31, Year 6 (Year 6 accretion already recorded)
# ---------------------------------------------------------------------------
settlement_loss = money(CASH_PAID_AT_SETTLEMENT - aro_at_settlement)

# ---------------------------------------------------------------------------
# Journal entries
# ---------------------------------------------------------------------------
ZERO = Decimal("0")


def line(account, debit=ZERO, credit=ZERO):
    return {"account": account, "debit": money(debit), "credit": money(credit)}


journal_entries = [
    {
        # (a) initial recognition of the ARO; construction cost already booked
        "part": "a",
        "date": "December 31, Year 1",
        "description": "Initial recognition of the ARO at present value, "
                       "capitalized into the cost of the landfill cell",
        "lines": [
            line("Landfill Cell (Asset Retirement Cost)", debit=aro_pv),
            line("Asset Retirement Obligation", credit=aro_pv),
        ],
    },
    {
        # (c)(1) depreciation for Year 2
        "part": "c1",
        "date": "December 31, Year 2",
        "description": "Straight-line depreciation of the landfill cell "
                       "(includes the capitalized asset retirement cost)",
        "lines": [
            line("Depreciation Expense", debit=annual_depreciation),
            line("Accumulated Depreciation - Landfill Cell",
                 credit=annual_depreciation),
        ],
    },
    {
        # (c)(2) accretion for Year 2
        "part": "c2",
        "date": "December 31, Year 2",
        "description": "Accretion of the ARO at 10% of the beginning balance",
        "lines": [
            line("Accretion Expense", debit=schedule[0]["accretion_expense"]),
            line("Asset Retirement Obligation",
                 credit=schedule[0]["accretion_expense"]),
        ],
    },
    {
        # (d) settlement
        "part": "d",
        "date": "December 31, Year 6",
        "description": "Settlement of the ARO with a third-party reclamation "
                       "firm; Year 6 accretion already recorded",
        "lines": [
            line("Asset Retirement Obligation", debit=aro_at_settlement),
            line("Loss on Settlement of Asset Retirement Obligation",
                 debit=settlement_loss),
            line("Cash", credit=CASH_PAID_AT_SETTLEMENT),
        ],
    },
]

# Debits must equal credits in every entry.
for entry in journal_entries:
    debits = sum((ln["debit"] for ln in entry["lines"]), Decimal("0"))
    credits = sum((ln["credit"] for ln in entry["lines"]), Decimal("0"))
    assert debits == credits, "Entry %s is out of balance: %s vs %s" % (
        entry["part"], debits, credits)

# The schedule must close exactly on the undiscounted retirement cost.
assert aro_at_settlement == RETIREMENT_COST, (
    "Accretion schedule failed to close on the undiscounted estimate: %s"
    % aro_at_settlement)
assert money(aro_pv + total_accretion) == RETIREMENT_COST

# ---------------------------------------------------------------------------
# Answers -- only the figures the Required parts ask for
# ---------------------------------------------------------------------------
answers = [
    {"label": "a: present value of the ARO at December 31, Year 1",
     "value": aro_pv},
]

for row in schedule:
    answers.append({
        "label": "b: %s - beginning ARO" % row["date"],
        "value": row["beginning_aro"],
    })
    answers.append({
        "label": "b: %s - accretion expense at 10%%" % row["date"],
        "value": row["accretion_expense"],
    })
    answers.append({
        "label": "b: %s - ending ARO" % row["date"],
        "value": row["ending_aro"],
    })

answers.append({
    "label": "e: total accretion expense over the life of the ARO",
    "value": total_accretion,
})
answers.append({
    "label": "e: total depreciation of the landfill cell",
    "value": total_depreciation,
})

notes = (
    "Discount period is 5 years (Dec 31 Year 1 to the Dec 31 Year 6 cash "
    "outflow), not the 4-year useful life, so the ARO accretes through a "
    "sixth year after the cell is fully depreciated at the end of Year 5. "
    "The schedule's beginning balance at December 31, Year 1 is the "
    "recognition-date PV; the first accretion charge falls in Year 2. "
    "Depreciation runs Years 2-5 on a base of construction cost plus the "
    "capitalized asset retirement cost. "
    "e (explanation): the ARO's present value is capitalized rather than "
    "expensed immediately because the legal obligation to dismantle and "
    "reclaim is an unavoidable cost of getting the cell into service - it is "
    "part of the total cost of using the asset, and it produces future "
    "economic benefit over the cell's operating life. Capitalizing it and "
    "depreciating it over the 4-year life matches that retirement cost "
    "against the revenue the cell generates, instead of dumping the whole "
    "amount into the period of construction when no benefit has yet been "
    "consumed. The liability is recorded at present value because settlement "
    "is five years away; the discount unwinds as accretion expense, which is "
    "an operating expense (not interest expense) under the effective-interest "
    "approach."
)

result = {
    "id": "agent_201#00",
    "rounding_convention": (
        "ROUND_HALF_UP to the cent, applied per period. PV via the exact "
        "formula FV/(1+i)^n in Decimal (not a truncated table factor); each "
        "year's accretion is rounded before rolling into the next year's "
        "beginning balance."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}


class DecimalAwareEncoder(json.JSONEncoder):
    """Emit Decimal values as bare JSON numbers without going through float."""

    # Must be printable ASCII: json.dumps would escape a control character
    # (e.g. \x00 -> ) and the strip-the-quotes regex below would miss it.
    SENTINEL = "@@DEC@@"

    def default(self, obj):
        if isinstance(obj, Decimal):
            return self.SENTINEL + format_number(obj) + self.SENTINEL
        return super().default(obj)


def format_number(value):
    """Render a Decimal as a plain JSON number: no $, no commas, no
    exponent, and no trailing '.00' on whole amounts."""
    text = format(value.quantize(CENT, rounding=ROUND_HALF_UP), "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def dump(payload):
    raw = json.dumps(payload, cls=DecimalAwareEncoder, indent=2)
    # Strip the quotes the encoder had to put around the sentinel strings so
    # the Decimals land in the output as real JSON numbers.
    sentinel = re.escape(DecimalAwareEncoder.SENTINEL)
    pattern = r'"%s(-?[0-9.]+)%s"' % (sentinel, sentinel)
    out, count = re.subn(pattern, r"\1", raw)
    assert DecimalAwareEncoder.SENTINEL not in out, (
        "A Decimal survived as a quoted string; the sentinel was escaped.")
    assert count > 0, "No Decimal values were emitted."
    return out


if __name__ == "__main__":
    print(dump(result))
