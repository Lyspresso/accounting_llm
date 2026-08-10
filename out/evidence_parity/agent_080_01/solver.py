"""Solver for agent_080#01 — Coastal Glassworks Inc. tempering furnace.

Rounding convention: all money handled with decimal.Decimal (never float).
Each period's depreciation is computed independently and rounded to the cent
with ROUND_HALF_UP at the end of every period (no cumulative drift carried
forward as unrounded values). Every figure is derived from the fact table;
nothing is hard-coded.
"""
from decimal import Decimal, ROUND_HALF_UP
import json

C = Decimal("0.01")
def r(x):
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)

def num(d):
    d = r(d)
    return int(d) if d == d.to_integral_value() else float(d)

# --- Given facts -----------------------------------------------------------
cost            = Decimal("240000")
resid_orig      = Decimal("24000")
life_orig       = Decimal("8")
change_year     = 5                      # Jan 1, Year 5 revision
total_life_new  = Decimal("12")
resid_new       = Decimal("12000")
proceeds        = Decimal("95000")
disposal_year   = 6                      # Dec 31, Year 6, after Y6 depreciation

# --- b. original annual depreciation + schedule Years 1-4 ------------------
dep_orig = r((cost - resid_orig) / life_orig)
years_before = change_year - 1           # Years 1-4 under original estimate

sched_1_4 = []
accum = Decimal("0")
for y in range(1, years_before + 1):
    accum = r(accum + dep_orig)
    sched_1_4.append({"year": y, "dep": dep_orig, "accum": accum,
                      "cv": r(cost - accum)})

accum_at_change = accum
cv_at_change = r(cost - accum_at_change)

# --- c. revised depreciation ----------------------------------------------
remaining_life = total_life_new - Decimal(years_before)
dep_new = r((cv_at_change - resid_new) / remaining_life)

# --- d. schedule Years 5-12 ------------------------------------------------
sched_5_end = []
accum = accum_at_change
last_year = int(total_life_new)
for y in range(change_year, last_year + 1):
    accum = r(accum + dep_new)
    sched_5_end.append({"year": y, "dep": dep_new, "accum": accum,
                        "cv": r(cost - accum)})

cv_end_final = sched_5_end[-1]["cv"]
residual_check_ok = (cv_end_final == resid_new)

# --- e. disposal at Dec 31, Year 6 ----------------------------------------
row_disp = next(x for x in sched_5_end if x["year"] == disposal_year)
accum_at_disposal = row_disp["accum"]
cv_at_disposal = row_disp["cv"]
gain_loss = r(proceeds - cv_at_disposal)   # negative => loss
loss = -gain_loss

answers = [
    {"label": "a: Debit Equipment - Tempering Furnace (Jan 1, Year 1)", "value": num(cost)},
    {"label": "a: Credit Cash (Jan 1, Year 1)", "value": num(cost)},
    {"label": "b: Original annual straight-line depreciation = (240,000 - 24,000) / 8", "value": num(dep_orig)},
]
for row in sched_1_4:
    y = row["year"]
    answers += [
        {"label": f"b: Year {y} depreciation expense", "value": num(row["dep"])},
        {"label": f"b: Year {y} accumulated depreciation (end of year)", "value": num(row["accum"])},
        {"label": f"b: Year {y} carrying amount (end of year)", "value": num(row["cv"])},
    ]
answers += [
    {"label": "c: Carrying amount at January 1, Year 5 (240,000 - 108,000)", "value": num(cv_at_change)},
    {"label": "c: Remaining useful life at Jan 1, Year 5 (12 total - 4 elapsed), years", "value": num(remaining_life)},
    {"label": "c: Revised depreciable base (132,000 - 12,000 revised residual)", "value": num(cv_at_change - resid_new)},
    {"label": "c: Updated annual depreciation (Years 5-12)", "value": num(dep_new)},
    {"label": "c: Year 5 period-end depreciation expense (JE amount)", "value": num(dep_new)},
]
for row in sched_5_end:
    y = row["year"]
    answers += [
        {"label": f"d: Year {y} depreciation expense", "value": num(row["dep"])},
        {"label": f"d: Year {y} accumulated depreciation (end of year)", "value": num(row["accum"])},
        {"label": f"d: Year {y} carrying amount (end of year)", "value": num(row["cv"])},
    ]
answers += [
    {"label": "d: Spot-check - carrying amount at end of Year 12 equals revised residual 12,000", "value": num(cv_end_final)},
    {"label": "e: Accumulated depreciation at December 31, Year 6 (after Year 6 depreciation)", "value": num(accum_at_disposal)},
    {"label": "e: Carrying amount at December 31, Year 6", "value": num(cv_at_disposal)},
    {"label": "e: Cash proceeds", "value": num(proceeds)},
    {"label": "e: Loss on disposal (95,000 proceeds - 102,000 carrying amount)", "value": num(loss)},
]

journal_entries = [
    {"part": "a", "lines": [
        {"account": "Equipment - Tempering Furnace", "debit": num(cost), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": num(cost)},
    ]},
    {"part": "c", "lines": [
        {"account": "Depreciation Expense", "debit": num(dep_new), "credit": 0},
        {"account": "Accumulated Depreciation - Equipment", "debit": 0, "credit": num(dep_new)},
    ]},
    {"part": "e", "lines": [
        {"account": "Cash", "debit": num(proceeds), "credit": 0},
        {"account": "Accumulated Depreciation - Equipment", "debit": num(accum_at_disposal), "credit": 0},
        {"account": "Loss on Disposal of Equipment", "debit": num(loss), "credit": 0},
        {"account": "Equipment - Tempering Furnace", "debit": 0, "credit": num(cost)},
    ]},
]

# Dr = Cr check for every entry
for je in journal_entries:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert d == c, (je["part"], d, c)
assert residual_check_ok

notes = ("f: This is a change in accounting estimate (revised useful life and residual value), "
         "not a change in accounting principle or an error correction, so it is accounted for "
         "prospectively over the remaining 8 years with no restatement of Years 1-4. "
         "Original annual depreciation 27,000; carrying amount at 1/1/Y5 132,000; revised annual "
         "depreciation 15,000; Year 12 ending carrying amount equals the revised residual of 12,000; "
         "sale of the furnace for 95,000 against a 102,000 carrying amount yields a 7,000 loss.")

print(json.dumps({
    "id": "agent_080#01",
    "rounding_convention": "decimal.Decimal throughout (no floats); each period's amount quantized to the cent with ROUND_HALF_UP at period end; totals accumulated from rounded period amounts",
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
