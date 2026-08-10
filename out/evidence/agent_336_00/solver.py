#!/usr/bin/env python3
"""
Solver for item agent_336#00 — Meridian Fabrication Co.

Full lifecycle for a nonmonetary exchange WITH commercial substance (LO 11-9):
initial recognition, residual-aware straight-line depreciation schedule,
pre-exchange depreciation update through the exchange date, the exchange JE
(loss + cash paid), subsequent depreciation on the acquired asset, and the
later disposal.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; no binary floats anywhere in this module.
Rounding is ROUND_HALF_UP to the cent (2 decimal places), applied PER PERIOD:
each period's depreciation charge is computed and rounded on its own, then
accumulated, rather than rounding only a cumulative total at the end. This
matches the course convention (ROUND_HALF_UP per period).

Depreciation is straight-line on a residual-aware base, recorded "to the
nearest month" as the stem directs, so a partial period is
    monthly_rate = (cost - residual) / (useful_life_years * 12)
and a partial period charge = monthly_rate * months_in_service, each rounded
per period. In this fact pattern every figure lands exactly on a whole dollar,
so the rounding rule is never actually load-bearing — but it is applied
deliberately rather than assumed away.

VALUATION CONVENTION FOR THE EXCHANGE (ASC 845 / textbook LO 11-9)
-----------------------------------------------------------------
The exchange has commercial substance, so any gain OR loss is fully
recognized. The fair value of the asset received (the mill) is NOT more
clearly determinable than the fair value of the asset surrendered (the
press), so the acquired asset is recorded at:
    fair value of asset given up + cash paid
A loss is recognized in full in any case (commercial substance or not),
because capitalizing above fair value is not permitted.

Run:  python3 solver.py   -> prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x) -> Decimal:
    """Round a Decimal to the cent using ROUND_HALF_UP (per-period rounding)."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly number: int when the cents are zero, else float-free string->float."""
    d = money(d)
    if d == d.to_integral_value():
        return int(d)
    return float(d)  # only for display; all arithmetic above stayed Decimal


# ---------------------------------------------------------------------------
# Given facts (transcribed from the stem — nothing here is a derived answer)
# ---------------------------------------------------------------------------

# Hydraulic press
PRESS_COST = Decimal("90000")
PRESS_RESIDUAL = Decimal("9000")
PRESS_LIFE_YEARS = 6
# Acquired 20X1-01-01; exchanged 20X4-09-30.

# Exchange on 20X4-09-30
PRESS_FAIR_VALUE = Decimal("38000")
CASH_PAID = Decimal("25000")

# CNC mill, placed in service 20X4-10-01
MILL_RESIDUAL = Decimal("3000")
MILL_LIFE_YEARS = 5

# Disposal 20X7-06-30
MILL_SALE_PROCEEDS = Decimal("28000")


# ---------------------------------------------------------------------------
# Straight-line, residual-aware, nearest-month machinery
# ---------------------------------------------------------------------------

def sl_monthly_rate(cost: Decimal, residual: Decimal, life_years: int) -> Decimal:
    """Unrounded monthly SL rate; rounding happens per recorded period."""
    return (cost - residual) / Decimal(life_years * 12)


def sl_period(monthly_rate: Decimal, months: int) -> Decimal:
    """One period's depreciation charge, rounded ROUND_HALF_UP per period."""
    return money(monthly_rate * Decimal(months))


# ---------------------------------------------------------------------------
# (b) Press depreciation schedule: 20X1-01-01 through 20X4-09-30
# ---------------------------------------------------------------------------

press_monthly = sl_monthly_rate(PRESS_COST, PRESS_RESIDUAL, PRESS_LIFE_YEARS)

# Months of service in each reporting period up to the exchange date.
press_periods = [
    ("20X1 (full year)", 12),
    ("20X2 (full year)", 12),
    ("20X3 (full year)", 12),
    ("20X4 Jan 1 - Sep 30 (9 months, partial)", 9),
]

press_schedule = []
press_accum = Decimal("0")
for label, months in press_periods:
    charge = sl_period(press_monthly, months)
    press_accum = money(press_accum + charge)   # accumulate rounded charges
    press_schedule.append(
        {
            "period": label,
            "months": months,
            "depreciation_expense": num(charge),
            "accumulated_depreciation_end": num(press_accum),
            "book_value_end": num(money(PRESS_COST - press_accum)),
        }
    )

press_ad_at_exchange = press_accum                       # 20X4-09-30 AD
press_dep_20x4_partial = sl_period(press_monthly, 9)     # the (c) adjusting amount
press_bv_at_exchange = money(PRESS_COST - press_ad_at_exchange)

# ---------------------------------------------------------------------------
# (d) Exchange with commercial substance: loss + cash paid
# ---------------------------------------------------------------------------

# Gain/(loss) = fair value of asset given up - its book value.
exchange_gain_loss = money(PRESS_FAIR_VALUE - press_bv_at_exchange)  # negative => loss

# Acquired asset is recorded at FV of asset given up + cash paid, because the
# mill's fair value is not more clearly determinable.
MILL_COST = money(PRESS_FAIR_VALUE + CASH_PAID)

# ---------------------------------------------------------------------------
# (e) Mill depreciation schedule: 20X4-10-01 through 20X7-06-30
# ---------------------------------------------------------------------------

mill_monthly = sl_monthly_rate(MILL_COST, MILL_RESIDUAL, MILL_LIFE_YEARS)

mill_periods = [
    ("20X4 Oct 1 - Dec 31 (3 months, partial)", 3),
    ("20X5 (full year)", 12),
    ("20X6 (full year)", 12),
    ("20X7 Jan 1 - Jun 30 (6 months, partial)", 6),
]

mill_schedule = []
mill_accum = Decimal("0")
mill_charge_by_label = {}
for label, months in mill_periods:
    charge = sl_period(mill_monthly, months)
    mill_accum = money(mill_accum + charge)
    mill_charge_by_label[label] = charge
    mill_schedule.append(
        {
            "period": label,
            "months": months,
            "depreciation_expense": num(charge),
            "accumulated_depreciation_end": num(mill_accum),
            "book_value_end": num(money(MILL_COST - mill_accum)),
        }
    )

mill_dep_20x4 = mill_charge_by_label["20X4 Oct 1 - Dec 31 (3 months, partial)"]
mill_dep_20x7 = mill_charge_by_label["20X7 Jan 1 - Jun 30 (6 months, partial)"]
mill_ad_at_disposal = mill_accum
mill_bv_at_disposal = money(MILL_COST - mill_ad_at_disposal)

# ---------------------------------------------------------------------------
# (f) Disposal on 20X7-06-30
# ---------------------------------------------------------------------------

disposal_gain_loss = money(MILL_SALE_PROCEEDS - mill_bv_at_disposal)  # negative => loss


# ---------------------------------------------------------------------------
# Journal entries
# ---------------------------------------------------------------------------

def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


entries = []

# (a) Initial recognition of the press, 20X1-01-01
entries.append(
    {
        "part": "a",
        "description": "January 1, 20X1 - initial recognition of hydraulic press (cash purchase)",
        "lines": [
            line("Equipment - Hydraulic Press", debit=PRESS_COST),
            line("Cash", credit=PRESS_COST),
        ],
    }
)

# (c) Pre-exchange depreciation update on the press, 20X4-09-30
entries.append(
    {
        "part": "c",
        "description": (
            "September 30, 20X4 - adjusting entry updating depreciation on the press "
            "through the exchange date (9 months of 20X4)"
        ),
        "lines": [
            line("Depreciation Expense", debit=press_dep_20x4_partial),
            line("Accumulated Depreciation - Hydraulic Press", credit=press_dep_20x4_partial),
        ],
    }
)

# (d) The exchange itself, 20X4-09-30
exchange_lines = [
    line("Equipment - CNC Mill", debit=MILL_COST),
    line("Accumulated Depreciation - Hydraulic Press", debit=press_ad_at_exchange),
]
if exchange_gain_loss < 0:
    exchange_lines.append(line("Loss on Exchange of Asset", debit=-exchange_gain_loss))
exchange_lines.append(line("Equipment - Hydraulic Press", credit=PRESS_COST))
exchange_lines.append(line("Cash", credit=CASH_PAID))
if exchange_gain_loss > 0:
    exchange_lines.insert(-2, line("Gain on Exchange of Asset", credit=exchange_gain_loss))

entries.append(
    {
        "part": "d",
        "description": (
            "September 30, 20X4 - exchange of press plus cash for CNC mill "
            "(commercial substance; loss fully recognized)"
        ),
        "lines": exchange_lines,
    }
)

# (e) Depreciation adjusting entries on the mill
entries.append(
    {
        "part": "e",
        "description": "December 31, 20X4 - depreciation on CNC mill (3 months, Oct 1 - Dec 31)",
        "lines": [
            line("Depreciation Expense", debit=mill_dep_20x4),
            line("Accumulated Depreciation - CNC Mill", credit=mill_dep_20x4),
        ],
    }
)
entries.append(
    {
        "part": "e",
        "description": "June 30, 20X7 - depreciation on CNC mill through disposal date (6 months)",
        "lines": [
            line("Depreciation Expense", debit=mill_dep_20x7),
            line("Accumulated Depreciation - CNC Mill", credit=mill_dep_20x7),
        ],
    }
)

# (f) Disposal of the mill, 20X7-06-30
disposal_lines = [
    line("Cash", debit=MILL_SALE_PROCEEDS),
    line("Accumulated Depreciation - CNC Mill", debit=mill_ad_at_disposal),
]
if disposal_gain_loss < 0:
    disposal_lines.append(line("Loss on Disposal of Asset", debit=-disposal_gain_loss))
disposal_lines.append(line("Equipment - CNC Mill", credit=MILL_COST))
if disposal_gain_loss > 0:
    disposal_lines.append(line("Gain on Disposal of Asset", credit=disposal_gain_loss))

entries.append(
    {
        "part": "f",
        "description": "June 30, 20X7 - sale of CNC mill for cash",
        "lines": disposal_lines,
    }
)

# Prove Dr = Cr on every entry (parts d and f explicitly demand the proof).
for e in entries:
    dr = sum(Decimal(str(l["debit"])) for l in e["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in e["lines"])
    assert money(dr) == money(cr), f"Entry {e['part']} out of balance: Dr {dr} vs Cr {cr}"


# ---------------------------------------------------------------------------
# Answers: only figures the Required parts ask for
# ---------------------------------------------------------------------------

answers = []

# (b) schedule for the press: annual and partial-year amounts + cumulative AD
for row in press_schedule:
    answers.append(
        {
            "label": f"b: press depreciation expense - {row['period']}",
            "value": row["depreciation_expense"],
        }
    )
    answers.append(
        {
            "label": f"b: press cumulative accumulated depreciation at end of {row['period']}",
            "value": row["accumulated_depreciation_end"],
        }
    )

# (d) book value, gain/loss on exchange, cost assigned to the mill
answers.append(
    {"label": "d: book value of press at September 30, 20X4", "value": num(press_bv_at_exchange)}
)
answers.append(
    {
        "label": "d: loss on exchange (negative = loss)",
        "value": num(exchange_gain_loss),
    }
)
answers.append({"label": "d: cost assigned to CNC mill", "value": num(MILL_COST)})

# (e) schedule for the mill
for row in mill_schedule:
    answers.append(
        {
            "label": f"e: CNC mill depreciation expense - {row['period']}",
            "value": row["depreciation_expense"],
        }
    )
    answers.append(
        {
            "label": f"e: CNC mill cumulative accumulated depreciation at end of {row['period']}",
            "value": row["accumulated_depreciation_end"],
        }
    )

# (f) gain or loss on disposal
answers.append(
    {
        "label": "f: loss on disposal of CNC mill, June 30, 20X7 (negative = loss)",
        "value": num(disposal_gain_loss),
    }
)

output = {
    "id": "agent_336#00",
    "rounding_convention": (
        "decimal.Decimal only, no floats. ROUND_HALF_UP to the cent applied PER PERIOD: "
        "each period's straight-line charge is rounded on its own and then accumulated "
        "(not rounded once at the end). Straight-line on a residual-aware base with "
        "depreciation recorded to the nearest month, so a partial period = "
        "(cost - residual) / (life in months) x months in service. Exchange with "
        "commercial substance: acquired asset = fair value of asset given up + cash paid "
        "(the mill's fair value is not more clearly determinable); loss recognized in full."
    ),
    "answers": answers,
    "journal_entries": entries,
    "insufficient_info": False,
    "notes": (
        "All figures land on whole dollars, so per-period rounding is not load-bearing here "
        "but is applied deliberately. Gains/losses are signed: negative = loss. Part (d) loss "
        "= fair value of press ($38,000) less its book value at 9/30/X4; part (f) loss = "
        "proceeds ($28,000) less the mill's book value at 6/30/X7. Dr = Cr asserted on all "
        "six journal entries."
    ),
}

print(json.dumps(output, indent=2))
