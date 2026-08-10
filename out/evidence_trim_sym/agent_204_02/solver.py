"""Solver for agent_204#02 - LO 11-8 donated equipment, partial-year SL schedule, scrap disposal.

Rounding convention: decimal.Decimal throughout (no floats). Every period's
depreciation is rounded independently to whole dollars using ROUND_HALF_UP;
accumulated depreciation and NBV are the running sums of those rounded period
amounts, so the schedule closes exactly to the residual/carrying value.

Pack treatment (overrides default judgement): donated asset recorded at FULL
fair value; incidental title/legal cost credited to Cash; Contribution Revenue
credited NET (fair value MINUS costs paid); incidental costs are NOT
capitalized and therefore are NOT in the depreciable base.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("1")


def r(x):
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def money(x):
    return int(r(x))


# ---- given -------------------------------------------------------------
fair_value = Decimal("180000")
title_cost_paid = Decimal("3000")
life_years = Decimal("6")
residual = Decimal("12000")
months_year1 = Decimal("9")          # April 1 -> December 31
scrap_proceeds = Decimal("9500")

# ---- part a: contribution JE ------------------------------------------
equipment_cost = fair_value                       # full FV, costs not capitalized
contribution_revenue = fair_value - title_cost_paid

je_a = {"part": "a", "lines": [
    {"account": "Equipment", "debit": money(equipment_cost), "credit": 0},
    {"account": "Cash", "debit": 0, "credit": money(title_cost_paid)},
    {"account": "Contribution Revenue", "debit": 0,
     "credit": money(contribution_revenue)},
]}

# ---- part b: subsequent measurement schedule --------------------------
depreciable_base = equipment_cost - residual
annual_full = depreciable_base / life_years

rows = []
accum = Decimal("0")
for year in (1, 2, 3):
    frac = months_year1 / Decimal("12") if year == 1 else Decimal("1")
    dep = r(annual_full * frac)
    accum += dep
    nbv = equipment_cost - accum
    rows.append({"year": year, "dep": dep, "accum": accum, "nbv": nbv})

# ---- parts c & d: adjusting entries -----------------------------------
def dep_je(part, dep):
    return {"part": part, "lines": [
        {"account": "Depreciation Expense", "debit": money(dep), "credit": 0},
        {"account": "Accumulated Depreciation - Equipment", "debit": 0,
         "credit": money(dep)},
    ]}


je_c1 = dep_je("c", rows[0]["dep"])
je_c2 = dep_je("c", rows[1]["dep"])
je_d1 = dep_je("d", rows[2]["dep"])

accum_at_disposal = rows[2]["accum"]
nbv_at_disposal = equipment_cost - accum_at_disposal
loss = nbv_at_disposal - scrap_proceeds          # positive => loss

disposal_lines = [
    {"account": "Cash", "debit": money(scrap_proceeds), "credit": 0},
    {"account": "Accumulated Depreciation - Equipment",
     "debit": money(accum_at_disposal), "credit": 0},
]
if loss > 0:
    disposal_lines.append({"account": "Loss on Disposal of Equipment",
                           "debit": money(loss), "credit": 0})
disposal_lines.append({"account": "Equipment", "debit": 0,
                       "credit": money(equipment_cost)})
if loss < 0:
    disposal_lines.append({"account": "Gain on Disposal of Equipment",
                           "debit": 0, "credit": money(-loss)})
je_d2 = {"part": "d", "lines": disposal_lines}

journal_entries = [je_a, je_c1, je_c2, je_d1, je_d2]

# ---- Dr = Cr proof -----------------------------------------------------
for je in journal_entries:
    d = sum(l["debit"] for l in je["lines"])
    c = sum(l["credit"] for l in je["lines"])
    assert d == c, (je, d, c)

# schedule must close to residual-independent carrying value math
assert rows[2]["accum"] == sum(x["dep"] for x in rows)
assert nbv_at_disposal == equipment_cost - accum_at_disposal

answers = [
    {"label": "a: Equipment debited (full fair value)", "value": money(equipment_cost)},
    {"label": "a: Cash credited (legal title transfer paid)", "value": money(title_cost_paid)},
    {"label": "a: Contribution Revenue credited (FV net of costs paid)", "value": money(contribution_revenue)},
    {"label": "b: Depreciable base (cost - residual)", "value": money(depreciable_base)},
    {"label": "b: Full-year straight-line depreciation", "value": money(annual_full)},
    {"label": "b: Year 1 depreciation expense (9 months held)", "value": money(rows[0]["dep"])},
    {"label": "b: Year 1 year-end accumulated depreciation", "value": money(rows[0]["accum"])},
    {"label": "b: Year 1 year-end NBV", "value": money(rows[0]["nbv"])},
    {"label": "b: Year 2 depreciation expense", "value": money(rows[1]["dep"])},
    {"label": "b: Year 2 year-end accumulated depreciation", "value": money(rows[1]["accum"])},
    {"label": "b: Year 2 year-end NBV", "value": money(rows[1]["nbv"])},
    {"label": "b: Year 3 depreciation expense", "value": money(rows[2]["dep"])},
    {"label": "b: Year 3 year-end accumulated depreciation", "value": money(rows[2]["accum"])},
    {"label": "b: Year 3 year-end NBV", "value": money(rows[2]["nbv"])},
    {"label": "c: Dec 31 Year 1 depreciation adjusting entry amount", "value": money(rows[0]["dep"])},
    {"label": "c: Dec 31 Year 2 depreciation adjusting entry amount", "value": money(rows[1]["dep"])},
    {"label": "d: Dec 31 Year 3 depreciation adjusting entry amount", "value": money(rows[2]["dep"])},
    {"label": "d: Cash received on scrapping", "value": money(scrap_proceeds)},
    {"label": "d: Accumulated depreciation removed at disposal", "value": money(accum_at_disposal)},
    {"label": "d: Equipment cost removed at disposal", "value": money(equipment_cost)},
    {"label": "d: Loss on disposal", "value": money(loss)},
]

out = {
    "id": "agent_204#02",
    "rounding_convention": ("decimal.Decimal only; each period's depreciation rounded "
                            "independently to whole dollars with ROUND_HALF_UP; accumulated "
                            "depreciation and NBV are running sums of the rounded period "
                            "amounts, so the schedule closes exactly to carrying value. "
                            "Incidental $3,000 title cost expensed against Contribution "
                            "Revenue (net), not capitalized, so it is outside the "
                            "depreciable base."),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": ("Asset recorded at full FV $180,000; Contribution Revenue = $180,000 - $3,000 "
              "= $177,000; Cash credited $3,000. Depreciable base = $180,000 - $12,000 = "
              "$168,000 over 6 years = $28,000/yr; Year 1 = 9/12 x $28,000 = $21,000. "
              "Disposal on 12/31/Yr3 after Year 3 depreciation: NBV $103,000 vs $9,500 "
              "proceeds gives a $93,500 loss. Part c is two separate entries (Yr1, Yr2); "
              "part d is two entries (Yr3 depreciation, then scrap disposal)."),
}
print(json.dumps(out, indent=1))
