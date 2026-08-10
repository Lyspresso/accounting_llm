"""Solver for agent_204#02 — LO 11-8 donated equipment, partial-year schedule, scrap disposal.

Rounding convention: all money is decimal.Decimal; every amount is rounded to whole
dollars using ROUND_HALF_UP once per period (per-year depreciation is rounded as it is
computed, and the schedule is closed exactly by forcing the final year's charge to the
undepreciated remainder above residual). Journal entries are whole dollars; the
underlying rate math is carried at full Decimal precision.

Pack treatment (overrides default judgement): the donated asset is recorded at FULL fair
value; the incidental title-transfer cost paid in cash is credited to Cash and DEDUCTED
from Contribution Revenue (revenue = FV - costs paid). The incidental cost is NOT
capitalized, so it is not in the depreciable base.
"""
from decimal import Decimal, ROUND_HALF_UP
import json

C = Decimal("0.01")
D0 = Decimal("1")


def r(x):
    return Decimal(x).quantize(D0, rounding=ROUND_HALF_UP)


# ---- Facts (from the fact pattern only) ----
fair_value = Decimal("180000")
title_cost_cash = Decimal("3000")
life_years = Decimal("6")
residual = Decimal("12000")
months_held_y1 = Decimal("9")          # Apr 1 -> Dec 31 = 9 months
scrap_proceeds = Decimal("9500")

# ---- (a) contribution ----
equipment_cost = fair_value                      # full FV capitalized, costs expensed against revenue
contribution_revenue = fair_value - title_cost_cash

# ---- (b) schedule ----
depreciable_base = equipment_cost - residual
annual_full = depreciable_base / life_years
dep = {}
dep[1] = r(annual_full * (months_held_y1 / Decimal("12")))
dep[2] = r(annual_full)
dep[3] = r(annual_full)

# close the schedule exactly: cap cumulative depreciation at the depreciable base
accum = Decimal("0")
rows = []
for y in (1, 2, 3):
    charge = dep[y]
    if accum + charge > depreciable_base:
        charge = depreciable_base - accum
    accum += charge
    dep[y] = charge
    rows.append((y, charge, accum, equipment_cost - accum))

accum_y3 = rows[2][2]
nbv_y3 = rows[2][3]

# ---- (d) disposal ----
loss = nbv_y3 - scrap_proceeds

answers = [
    {"label": "a: Equipment (donated asset) debited at full fair value", "value": int(equipment_cost)},
    {"label": "a: Cash credited for legal title transfer cost paid", "value": int(title_cost_cash)},
    {"label": "a: Contribution Revenue credited (fair value net of costs paid)", "value": int(contribution_revenue)},
    {"label": "b: Year 1 depreciation expense (9 months held)", "value": int(rows[0][1])},
    {"label": "b: Year 1 year-end accumulated depreciation", "value": int(rows[0][2])},
    {"label": "b: Year 1 year-end net book value", "value": int(rows[0][3])},
    {"label": "b: Year 2 depreciation expense", "value": int(rows[1][1])},
    {"label": "b: Year 2 year-end accumulated depreciation", "value": int(rows[1][2])},
    {"label": "b: Year 2 year-end net book value", "value": int(rows[1][3])},
    {"label": "b: Year 3 depreciation expense", "value": int(rows[2][1])},
    {"label": "b: Year 3 year-end accumulated depreciation", "value": int(rows[2][2])},
    {"label": "b: Year 3 year-end net book value", "value": int(rows[2][3])},
    {"label": "c: Dec 31 Year 1 depreciation adjusting entry amount", "value": int(rows[0][1])},
    {"label": "c: Dec 31 Year 2 depreciation adjusting entry amount", "value": int(rows[1][1])},
    {"label": "d: Dec 31 Year 3 depreciation adjusting entry amount", "value": int(rows[2][1])},
    {"label": "d: Cash received on scrapping", "value": int(scrap_proceeds)},
    {"label": "d: Accumulated depreciation removed on disposal", "value": int(accum_y3)},
    {"label": "d: Loss on disposal of equipment", "value": int(loss)},
    {"label": "d: Equipment credited (removed at cost) on disposal", "value": int(equipment_cost)},
]


def L(acct, dr=0, cr=0):
    return {"account": acct, "debit": int(dr), "credit": int(cr)}


jes = [
    {"part": "a", "memo": "Apr 1, Yr 1 - donated equipment received at fair value; title-transfer cost paid in cash nets against contribution revenue",
     "lines": [L("Equipment", dr=equipment_cost),
               L("Cash", cr=title_cost_cash),
               L("Contribution Revenue", cr=contribution_revenue)]},
    {"part": "c", "memo": "Dec 31, Yr 1 - depreciation for 9 months held",
     "lines": [L("Depreciation Expense", dr=rows[0][1]),
               L("Accumulated Depreciation - Equipment", cr=rows[0][1])]},
    {"part": "c", "memo": "Dec 31, Yr 2 - full-year depreciation",
     "lines": [L("Depreciation Expense", dr=rows[1][1]),
               L("Accumulated Depreciation - Equipment", cr=rows[1][1])]},
    {"part": "d", "memo": "Dec 31, Yr 3 - full-year depreciation",
     "lines": [L("Depreciation Expense", dr=rows[2][1]),
               L("Accumulated Depreciation - Equipment", cr=rows[2][1])]},
    {"part": "d", "memo": "Dec 31, Yr 3 - equipment scrapped for salvage proceeds",
     "lines": [L("Cash", dr=scrap_proceeds),
               L("Accumulated Depreciation - Equipment", dr=accum_y3),
               L("Loss on Disposal of Equipment", dr=loss),
               L("Equipment", cr=equipment_cost)]},
]

for je in jes:
    assert sum(x["debit"] for x in je["lines"]) == sum(x["credit"] for x in je["lines"]), je["part"]

notes = (
    "Pack treatment applied: equipment recorded at full FV $180,000; the $3,000 title-transfer cost "
    "is credited to Cash and deducted from Contribution Revenue ($180,000 - $3,000 = $177,000), not "
    "capitalized. Depreciable base = $180,000 - $12,000 residual = $168,000; straight-line over 6 years "
    "= $28,000/full year. Year 1 held Apr 1 - Dec 31 = 9 months, so 9/12 x $28,000 = $21,000. "
    "Schedule closes exactly (cumulative depreciation capped at the depreciable base); no cap was needed "
    "through Year 3 since accumulated $77,000 < $168,000. Year 3 NBV $103,000 less $9,500 proceeds = "
    "$93,500 loss on scrapping. Dr = Cr verified on all five entries."
)

out = {
    "id": "agent_204#02",
    "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP to whole dollars once per period; schedule closed exactly to residual value",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": notes,
}
print(json.dumps(out, indent=1))
