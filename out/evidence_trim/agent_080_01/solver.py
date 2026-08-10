"""Coastal Glassworks Inc. tempering furnace: SL depreciation, prospective
change in estimate (life + residual) at 1/1/Yr5, disposal 12/31/Yr6 with loss.

Rounding convention: all money handled with decimal.Decimal; each period's
depreciation is computed independently and rounded to the cent using
ROUND_HALF_UP (no float arithmetic anywhere). Every figure is derived from the
stated facts; nothing is hard-coded.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def r(x):  # ROUND_HALF_UP to cents, per period
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def n(x):  # JSON-friendly number
    x = r(x)
    return int(x) if x == x.to_integral_value() else float(x)

# ---- Facts ----
cost              = Decimal("240000")
resid_orig        = Decimal("24000")
life_orig         = Decimal("8")
change_year       = 4          # years already elapsed at 1/1/Year 5
life_total_new    = Decimal("12")
resid_new         = Decimal("12000")
proceeds          = Decimal("95000")
disposal_year     = 6

# ---- b. Original annual depreciation & Years 1-4 schedule ----
dep_orig = r((cost - resid_orig) / life_orig)
sched_1_4, accum, ca = [], Decimal("0"), cost
for y in range(1, change_year + 1):
    accum += dep_orig
    ca = cost - accum
    sched_1_4.append({"year": y, "depreciation": n(dep_orig),
                      "accum_dep_end": n(accum), "carrying_amount_end": n(ca)})

accum_at_change = accum
ca_at_change    = cost - accum_at_change

# ---- c. Revised (prospective) annual depreciation ----
remaining_life = life_total_new - Decimal(change_year)
dep_new = r((ca_at_change - resid_new) / remaining_life)

# ---- d. Years 5-12 schedule ----
sched_5_12 = []
accum_d, ca_d = accum_at_change, ca_at_change
last_year = int(life_total_new)
for y in range(change_year + 1, last_year + 1):
    d = dep_new
    if y == last_year:  # force exact residual in final year (rounding plug)
        d = r(ca_d - resid_new)
    accum_d += d
    ca_d = cost - accum_d
    sched_5_12.append({"year": y, "depreciation": n(d),
                       "accum_dep_end": n(accum_d), "carrying_amount_end": n(ca_d)})
ca_end_life = cost - accum_d

# ---- e. Disposal 12/31/Year 6 ----
accum_at_disposal = accum_at_change + dep_new * Decimal(disposal_year - change_year)
ca_at_disposal    = cost - accum_at_disposal
gain_loss         = proceeds - ca_at_disposal      # negative => loss
loss              = -gain_loss

answers = [
 {"label": "a: Debit Equipment (tempering furnace) on 1/1/Yr1", "value": n(cost)},
 {"label": "a: Credit Cash on 1/1/Yr1", "value": n(cost)},
 {"label": "b: Original annual straight-line depreciation (Years 1-4)", "value": n(dep_orig)},
 {"label": "b: Depreciation schedule Years 1-4 (dep / accum / carrying amount)", "value": sched_1_4},
 {"label": "b: Accumulated depreciation at 12/31/Yr4", "value": n(accum_at_change)},
 {"label": "c: Carrying amount at 1/1/Yr5", "value": n(ca_at_change)},
 {"label": "c: Remaining useful life at 1/1/Yr5 (years)", "value": n(remaining_life)},
 {"label": "c: Revised annual depreciation, Years 5-12", "value": n(dep_new)},
 {"label": "c: Year 5 depreciation expense (period-end JE amount)", "value": n(dep_new)},
 {"label": "d: Depreciation schedule Years 5-12 (dep / accum / carrying amount)", "value": sched_5_12},
 {"label": "d: Carrying amount at end of Year 12 (equals revised residual)", "value": n(ca_end_life)},
 {"label": "e: Accumulated depreciation at 12/31/Yr6 (date of sale)", "value": n(accum_at_disposal)},
 {"label": "e: Carrying amount at 12/31/Yr6 before sale", "value": n(ca_at_disposal)},
 {"label": "e: Loss on disposal", "value": n(loss)},
 {"label": "f: Classification", "value": "Change in accounting estimate - accounted for prospectively over the remaining useful life; it is not a change in principle and not an error correction."},
]

jes = [
 {"part": "a", "lines": [
   {"account": "Equipment - Tempering Furnace", "debit": n(cost), "credit": 0},
   {"account": "Cash", "debit": 0, "credit": n(cost)}]},
 {"part": "c", "lines": [
   {"account": "Depreciation Expense", "debit": n(dep_new), "credit": 0},
   {"account": "Accumulated Depreciation - Equipment", "debit": 0, "credit": n(dep_new)}]},
 {"part": "e", "lines": [
   {"account": "Cash", "debit": n(proceeds), "credit": 0},
   {"account": "Accumulated Depreciation - Equipment", "debit": n(accum_at_disposal), "credit": 0},
   {"account": "Loss on Disposal of Equipment", "debit": n(loss), "credit": 0},
   {"account": "Equipment - Tempering Furnace", "debit": 0, "credit": n(cost)}]},
]
for je in jes:
    assert r(sum(Decimal(str(l["debit"])) for l in je["lines"])) == \
           r(sum(Decimal(str(l["credit"])) for l in je["lines"])), je["part"]
assert ca_end_life == resid_new

print(json.dumps({
 "id": "agent_080#01",
 "rounding_convention": "decimal.Decimal throughout (no floats); each period's depreciation rounded to the cent with ROUND_HALF_UP; final-year depreciation trued up so the carrying amount lands exactly on the revised residual.",
 "answers": answers,
 "journal_entries": jes,
 "insufficient_info": False,
 "notes": "Original SL dep = (240,000 - 24,000)/8 = 27,000/yr; 4 years accumulate 108,000, leaving a 1/1/Yr5 carrying amount of 132,000. The 1/1/Yr5 revision (total life 12 years => 8 remaining; residual 12,000) is applied prospectively: (132,000 - 12,000)/8 = 15,000/yr for Years 5-12, which reaches the 12,000 residual exactly at 12/31/Yr12. At 12/31/Yr6 accumulated depreciation is 108,000 + 2(15,000) = 138,000 and carrying amount is 102,000; proceeds of 95,000 give a 7,000 loss."
}, indent=1))
