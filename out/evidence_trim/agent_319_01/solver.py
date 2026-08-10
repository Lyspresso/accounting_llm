"""LCNRV schedule + period-end allowance JE (Lakeshore Pet Supply LLC).

Rounding convention: all money handled with decimal.Decimal, quantized to
0.01 using ROUND_HALF_UP once per period (period-end, Dec 31). No floats.
Every figure is derived from the input table; nothing is hard-coded.
"""
import json
from decimal import Decimal, ROUND_HALF_UP
from collections import OrderedDict

CENT = Decimal("0.01")
def q(x): return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)
def n(d):
    d = q(d)
    return int(d) if d == d.to_integral_value() else float(d)

# ---- inputs (from the scenario table) ----
ITEMS = [
    # (item, category, cost, NRV)
    ("Grain Blend",  "Dry Food",    Decimal("36000"), Decimal("32500")),
    ("Senior Blend", "Dry Food",    Decimal("21000"), Decimal("23000")),
    ("Chew Rope",    "Accessories", Decimal("14500"), Decimal("15800")),
    ("Puzzle Toy",   "Accessories", Decimal("29000"), Decimal("26500")),
]
COGS_BEFORE = Decimal("255000")

# ---- (a) item approach ----
item_lcnrv = OrderedDict((name, min(cost, nrv)) for name, cat, cost, nrv in ITEMS)
total_cost = sum((c for _, _, c, _ in ITEMS), Decimal("0"))
total_nrv  = sum((v for _, _, _, v in ITEMS), Decimal("0"))
total_item_lcnrv = sum(item_lcnrv.values(), Decimal("0"))
writedown_item = total_cost - total_item_lcnrv

# ---- (a) category approach ----
cats = OrderedDict()
for name, cat, cost, nrv in ITEMS:
    c, v = cats.get(cat, (Decimal("0"), Decimal("0")))
    cats[cat] = (c + cost, v + nrv)
cat_lcnrv = OrderedDict((cat, min(c, v)) for cat, (c, v) in cats.items())
total_cat_lcnrv = sum(cat_lcnrv.values(), Decimal("0"))
writedown_cat = total_cost - total_cat_lcnrv

# ---- (a) total approach ----
total_total_lcnrv = min(total_cost, total_nrv)
writedown_total = total_cost - total_total_lcnrv

# ---- (b) JE under the stated policy: individual-item, allowance, charge COGS ----
je_amt = writedown_item
lines = [
    {"account": "Cost of Goods Sold", "debit": n(je_amt), "credit": 0},
    {"account": "Allowance to Reduce Inventory to NRV", "debit": 0, "credit": n(je_amt)},
]
assert sum(Decimal(str(l["debit"])) for l in lines) == sum(Decimal(str(l["credit"])) for l in lines)

# ---- (c) presentation ----
inventory_net = total_cost - je_amt
cogs_after = COGS_BEFORE + je_amt

answers = []
for name in item_lcnrv:
    answers.append({"label": "a: LCNRV by item — %s" % name, "value": n(item_lcnrv[name])})
answers.append({"label": "a: Total inventory at LCNRV — individual-item approach",
                "value": n(total_item_lcnrv)})
for cat in cat_lcnrv:
    answers.append({"label": "a: LCNRV by category — %s" % cat, "value": n(cat_lcnrv[cat])})
answers.append({"label": "a: Total inventory at LCNRV — category approach",
                "value": n(total_cat_lcnrv)})
answers.append({"label": "a: Total inventory at LCNRV — total (whole-inventory) approach",
                "value": n(total_total_lcnrv)})
answers.append({"label": "a: Write-down required — individual-item approach",
                "value": n(writedown_item)})
answers.append({"label": "b: Dr Cost of Goods Sold", "value": n(je_amt)})
answers.append({"label": "b: Cr Allowance to Reduce Inventory to NRV", "value": n(je_amt)})
answers.append({"label": "c: Inventory, net on the balance sheet (cost %s less allowance %s)"
                % (n(total_cost), n(je_amt)), "value": n(inventory_net)})
answers.append({"label": "c: Cost of Goods Sold after adjustment", "value": n(cogs_after)})

notes = (
    "Item approach writes each item down to the lower of its own cost or NRV: "
    "Grain Blend and Puzzle Toy are impaired (3,500 + 2,500 = %s); the gains on "
    "Senior Blend and Chew Rope are ignored. Category approach nets within a "
    "category (Dry Food NRV %s < cost %s; Accessories NRV %s < cost %s) giving a "
    "%s write-down, and the total approach also gives %s — both smaller than the "
    "item approach because gains offset losses. Company policy is the item "
    "approach, so the recorded write-down is %s. Allowance method keeps Inventory "
    "at cost %s and reports it net of the allowance; the charge goes to COGS, so "
    "COGS rises from %s to %s. Average cost is used, so LCNRV (not LCM with a "
    "ceiling/floor) applies."
) % (n(writedown_item), n(cats['Dry Food'][1]), n(cats['Dry Food'][0]),
     n(cats['Accessories'][1]), n(cats['Accessories'][0]), n(writedown_cat),
     n(writedown_total), n(writedown_item), n(total_cost), n(COGS_BEFORE), n(cogs_after))

print(json.dumps({
    "id": "agent_319#01",
    "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP to the cent, applied once per period (Dec 31 period-end); no floating-point arithmetic",
    "answers": answers,
    "journal_entries": [{"part": "b", "lines": lines}],
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
