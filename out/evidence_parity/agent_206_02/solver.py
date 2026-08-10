"""Solver for agent_206#02 -- Riverton Machine Co. LO 12-1.

Rounding convention: all money is decimal.Decimal, quantized to the cent with
ROUND_HALF_UP once per period (each year's depreciation is rounded as computed,
and the rounded amount drives the next period's carrying amount). No floats.
Every figure is derived from the scenario inputs; nothing is hard-coded.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x):
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def n(x):
    x = q(x)
    return int(x) if x == x.to_integral_value() else float(x)

cost = Decimal("50000")
residual = Decimal("5000")
life = 5
total_units = Decimal("10000")
units_y1 = Decimal("1800")
sale_price = Decimal("12000")
sale_year = 3

depreciable_base = cost - residual

# --- a. Year 1 under each method ---
sl_y1 = q(depreciable_base / life)

syd_sum = Decimal(sum(range(1, life + 1)))
syd_y1 = q(depreciable_base * Decimal(life) / syd_sum)

ddb_rate = Decimal(2) / Decimal(life)
ddb_y1 = q(cost * ddb_rate)

uop_rate = depreciable_base / total_units
uop_y1 = q(uop_rate * units_y1)

# --- b. DDB schedule with residual floor / final-year plug ---
schedule = []
book = cost
accum = Decimal("0")
for yr in range(1, life + 1):
    begin = book
    computed = q(begin * ddb_rate)
    floored = False
    if begin - computed < residual:
        expense = q(begin - residual)   # plug down to the residual floor
        floored = True
    else:
        expense = computed
    accum = accum + expense
    book = begin - expense
    schedule.append({
        "year": yr,
        "beginning_book_value": begin,
        "rate": ddb_rate,
        "computed_expense": computed,
        "depreciation_expense": expense,
        "accumulated_depreciation": accum,
        "ending_book_value": book,
        "floored": floored,
    })

# --- c. disposal after Year 3 DDB depreciation ---
row3 = schedule[sale_year - 1]
accum_at_sale = row3["accumulated_depreciation"]
bv_at_sale = row3["ending_book_value"]
gain = q(sale_price - bv_at_sale)

answers = [
    {"label": "a: Year 1 depreciation - straight-line", "value": n(sl_y1)},
    {"label": "a: Year 1 depreciation - sum-of-the-years'-digits (5/15 x $45,000)", "value": n(syd_y1)},
    {"label": "a: Year 1 depreciation - double-declining-balance (40% x $50,000)", "value": n(ddb_y1)},
    {"label": "a: Year 1 depreciation - units-of-production ($4.50/unit x 1,800 units)", "value": n(uop_y1)},
    {"label": "a: units-of-production rate per unit", "value": n(uop_rate)},
    {"label": "b: DDB rate applied to beginning book value (percent)", "value": n(ddb_rate * 100)},
]
for r in schedule:
    y = r["year"]
    answers.append({"label": f"b: Year {y} beginning book value", "value": n(r["beginning_book_value"])})
    answers.append({"label": f"b: Year {y} depreciation expense", "value": n(r["depreciation_expense"])})
    answers.append({"label": f"b: Year {y} accumulated depreciation (ending)", "value": n(r["accumulated_depreciation"])})
    answers.append({"label": f"b: Year {y} ending book value", "value": n(r["ending_book_value"])})
answers += [
    {"label": "b: Year 5 unadjusted 40% computation before residual floor", "value": n(schedule[4]["computed_expense"])},
    {"label": "b: Year 5 residual-floor plug (limited to beginning BV less residual)", "value": n(schedule[4]["depreciation_expense"])},
    {"label": "b: total depreciation Years 1-5 (equals cost less residual)", "value": n(sum(r["depreciation_expense"] for r in schedule))},
    {"label": "c: accumulated depreciation at Dec 31 Year 3 (after Year 3 dep)", "value": n(accum_at_sale)},
    {"label": "c: book value at Dec 31 Year 3 (after Year 3 dep)", "value": n(bv_at_sale)},
    {"label": "c: gain on disposal (proceeds $12,000 less book value $10,800)", "value": n(gain)},
]

jes = [
    {"part": "a", "lines": [
        {"account": "Depreciation Expense", "debit": n(ddb_y1), "credit": 0},
        {"account": "Accumulated Depreciation - Equipment", "debit": 0, "credit": n(ddb_y1)},
    ]},
    {"part": "c", "lines": [
        {"account": "Equipment", "debit": n(cost), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": n(cost)},
    ]},
    {"part": "c", "lines": [
        {"account": "Cash", "debit": n(sale_price), "credit": 0},
        {"account": "Accumulated Depreciation - Equipment", "debit": n(accum_at_sale), "credit": 0},
        {"account": "Equipment", "debit": 0, "credit": n(cost)},
        {"account": "Gain on Disposal of Equipment", "debit": 0, "credit": n(gain)},
    ]},
]
for je in jes:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert d == c, (je, d, c)

notes = ("d: DDB applies the 2x straight-line rate to the full declining book value "
         "(cost less accumulated depreciation), not to a depreciable base net of residual, "
         "because the declining-balance formula is a rate-on-carrying-amount mechanic; it still "
         "lands on residual because depreciation is stopped/plugged in the final year so book "
         "value is never driven below the $5,000 residual floor (Year 5 expense $1,480 instead "
         "of the formula's $2,592). Disposal result: gain of $1,200.")

print(json.dumps({
    "id": "agent_206#02",
    "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP to the cent once per period, with the rounded period figure carried into the next period's book value; DDB final year plugged so ending book value equals the $5,000 residual floor",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
