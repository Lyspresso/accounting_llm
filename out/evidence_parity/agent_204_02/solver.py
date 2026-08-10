"""Solver for agent_204#02 — donated equipment, partial-year SL depreciation, scrap disposal.

Rounding convention: all money is decimal.Decimal; every periodic amount is rounded
to the cent with ROUND_HALF_UP independently per period (per-period rounding, not
cumulative), and accumulated depreciation / NBV are built by summing the already
rounded per-period amounts so the schedule always ties.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def r(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def n(x):
    x = r(x)
    return int(x) if x == x.to_integral_value() else float(x)

# ---- inputs (from the scenario text) ----
fair_value      = Decimal("180000")
title_cost      = Decimal("3000")     # legal title transfer: directly attributable -> capitalized
life_years      = Decimal("6")
residual        = Decimal("12000")
scrap_proceeds  = Decimal("9500")
acq_month       = 4                   # April 1, Year 1
months_in_year  = Decimal("12")

# ---- a. contribution ----
cost = r(fair_value + title_cost)                       # capitalized carrying amount
contribution_revenue = r(fair_value)
cash_paid = r(title_cost)

# ---- b. schedule ----
depreciable_base = r(cost - residual)
annual_dep = r(depreciable_base / life_years)
months_y1 = Decimal(12 - (acq_month - 1))               # Apr 1 -> Dec 31 = 9 months
dep = {
    1: r(annual_dep * months_y1 / months_in_year),
    2: annual_dep,
    3: annual_dep,
}
accum, nbv, schedule = Decimal("0"), None, []
for y in (1, 2, 3):
    accum = r(accum + dep[y])
    nbv = r(cost - accum)
    schedule.append((y, dep[y], accum, nbv))

# ---- d. scrap disposal ----
nbv_at_disposal = r(cost - accum)
loss_on_disposal = r(nbv_at_disposal - scrap_proceeds)

answers = [
    {"label": "a: Equipment capitalized (Dr) = $180,000 FV + $3,000 title cost", "value": n(cost)},
    {"label": "a: Contribution revenue (Cr)", "value": n(contribution_revenue)},
    {"label": "a: Cash paid (Cr)", "value": n(cash_paid)},
    {"label": "b: Depreciable base (cost - residual)", "value": n(depreciable_base)},
    {"label": "b: Full-year straight-line depreciation", "value": n(annual_dep)},
    {"label": "b: Months held in Year 1 (Apr 1 - Dec 31)", "value": int(months_y1)},
]
for y, d, a, v in schedule:
    answers += [
        {"label": f"b: Year {y} depreciation expense", "value": n(d)},
        {"label": f"b: Year {y} year-end accumulated depreciation", "value": n(a)},
        {"label": f"b: Year {y} year-end net book value", "value": n(v)},
    ]
answers += [
    {"label": "c: Dec 31, Year 1 depreciation adjusting entry amount", "value": n(dep[1])},
    {"label": "c: Dec 31, Year 2 depreciation adjusting entry amount", "value": n(dep[2])},
    {"label": "d: Dec 31, Year 3 depreciation adjusting entry amount", "value": n(dep[3])},
    {"label": "d: NBV immediately before scrapping", "value": n(nbv_at_disposal)},
    {"label": "d: Cash received from salvage dealer", "value": n(scrap_proceeds)},
    {"label": "d: Loss on disposal (scrapping)", "value": n(loss_on_disposal)},
]

def je(part, lines):
    dr = sum(Decimal(str(l[1])) for l in lines)
    cr = sum(Decimal(str(l[2])) for l in lines)
    assert r(dr) == r(cr), (part, dr, cr)
    return {"part": part,
            "lines": [{"account": a, "debit": n(d), "credit": n(c)} for a, d, c in lines]}

journal_entries = [
    je("a", [("Equipment", cost, 0),
             ("Cash", 0, cash_paid),
             ("Contribution Revenue (Revenue from contribution received)", 0, contribution_revenue)]),
    je("c", [("Depreciation Expense - Equipment (Dec 31, Year 1)", dep[1], 0),
             ("Accumulated Depreciation - Equipment", 0, dep[1])]),
    je("c", [("Depreciation Expense - Equipment (Dec 31, Year 2)", dep[2], 0),
             ("Accumulated Depreciation - Equipment", 0, dep[2])]),
    je("d", [("Depreciation Expense - Equipment (Dec 31, Year 3)", dep[3], 0),
             ("Accumulated Depreciation - Equipment", 0, dep[3])]),
    je("d", [("Cash", scrap_proceeds, 0),
             ("Accumulated Depreciation - Equipment", accum, 0),
             ("Loss on Disposal of Equipment", loss_on_disposal, 0),
             ("Equipment", 0, cost)]),
]

print(json.dumps({
    "id": "agent_204#02",
    "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP to the cent applied per period (each year's depreciation rounded independently), accumulated depreciation and NBV built from the rounded per-period amounts; Dr = Cr enforced on every entry.",
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": "Nonreciprocal transfer: equipment recognized at $180,000 fair value with the $3,000 legal title-transfer cost capitalized as a directly attributable cost of readying the asset, giving a $183,000 capitalized cost and $180,000 contribution revenue. Straight-line: ($183,000 - $12,000)/6 = $28,500 per full year; Year 1 held 9 months (Apr 1 - Dec 31) = $21,375. Accumulated depreciation at Dec 31, Year 3 = $78,375, NBV $104,625; scrapping for $9,500 cash yields a $95,125 loss on disposal."
}, indent=1))
