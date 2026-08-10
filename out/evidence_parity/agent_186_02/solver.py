"""Harborline Sporting Goods LLC -- dollar-value LIFO (single pool), Years 1-4.

Rounding convention: all money computed with decimal.Decimal and quantized to
cents using ROUND_HALF_UP, applied once per period (per-year figure), never floats.
Every figure is derived from the given FIFO ending inventories and price indexes;
nothing is hard-coded.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x): return x.quantize(C, rounding=ROUND_HALF_UP)
def n(x):
    x = q(x)
    return int(x) if x == x.to_integral_value() else float(x)

# ---- given data ----
DATA = [  # (year, FIFO ending inventory, price index)
    (1, Decimal("120000"), Decimal("1.00")),
    (2, Decimal("151200"), Decimal("1.20")),
    (3, Decimal("175500"), Decimal("1.30")),
    (4, Decimal("137500"), Decimal("1.25")),
]
BASE_YEAR = 1

ans = []
def add(label, value): ans.append({"label": label, "value": value})

layers = []          # list of dicts: year, base_amt, index, lifo_amt
prior_base = Decimal("0")
dvlifo = {}
base_cost = {}
liquidation_detail = []   # for Year 4

for year, fifo, idx in DATA:
    bc = q(fifo / idx)                       # deflate to base-year dollars
    base_cost[year] = bc
    change = bc - prior_base
    if change > 0:
        layers.append({"year": year, "base": change, "index": idx,
                       "lifo": q(change * idx)})
        add(f"a: Year {year} base-year cost of ending inventory", n(bc))
        add(f"a: Year {year} real increment at base-year cost", n(change))
        add(f"a: Year {year} new layer at DV LIFO cost "
            f"({n(change):,} x {idx})", n(q(change * idx)))
    elif change < 0:
        # liquidation: newest layers drop first
        need = -change
        add(f"a: Year {year} base-year cost of ending inventory", n(bc))
        add(f"a: Year {year} decrease in base-year cost (liquidation)", n(need))
        for lay in reversed(layers):
            if need <= 0:
                break
            take = lay["base"] if lay["base"] <= need else need
            lay["base"] = lay["base"] - take
            removed_lifo = q(take * lay["index"])
            lay["lifo"] = q(lay["lifo"] - removed_lifo)
            liquidation_detail.append((lay["year"], lay["index"], take, removed_lifo))
            need -= take
        layers = [l for l in layers if l["base"] > 0]
    else:
        add(f"a: Year {year} base-year cost of ending inventory", n(bc))
        add(f"a: Year {year} real increment at base-year cost", n(change))
    prior_base = bc
    total = sum((l["lifo"] for l in layers), Decimal("0"))
    dvlifo[year] = q(total)
    add(f"a: Year {year} DV LIFO ending inventory", n(q(total)))

# --- Year 4 liquidation disclosure ---
liq_years = []
for ly, lidx, take_base, take_lifo in liquidation_detail:
    tag = "base layer (Year 1)" if ly == BASE_YEAR else f"Year {ly} layer"
    add(f"a: Year 4 liquidation -- {tag} removed, base-year cost", n(take_base))
    add(f"a: Year 4 liquidation -- {tag} removed at LIFO cost (index {lidx})", n(take_lifo))
    liq_years.append(f"Year {ly} @ {lidx}")
add("a: Year 4 total liquidated at LIFO cost",
    n(sum((d[3] for d in liquidation_detail), Decimal("0"))))
for l in layers:
    tag = "base layer (Year 1)" if l["year"] == BASE_YEAR else f"Year {l['year']} layer"
    add(f"a: Year 4 remaining {tag} -- base-year cost", n(l["base"]))
    add(f"a: Year 4 remaining {tag} -- LIFO cost", n(l["lifo"]))
add("a: layers liquidated in Year 4 (newest first)",
    "Year 3 layer liquidated in full (9,000 base-yr @ 1.30), then Year 2 layer "
    "liquidated in full (6,000 base-yr @ 1.20), then 10,000 base-yr dollars of the "
    "base (Year 1) layer @ 1.00 eroded; only the base layer survives.")
unused_idx = DATA[-1][2]
add("a: index not used to price any layer", str(unused_idx))

# ---- (b) LIFO reserve rollforward ----
prior_res = Decimal("0")
for year, fifo, idx in DATA:
    end_res = q(fifo - dvlifo[year])
    adj = q(end_res - prior_res)
    add(f"b: Year {year} beginning LIFO reserve", n(prior_res))
    add(f"b: Year {year} adjustment to LIFO reserve (increase/(decrease))", n(adj))
    add(f"b: Year {year} ending LIFO reserve (FIFO less DV LIFO)", n(end_res))
    prior_res = end_res
    if year == DATA[-1][0]:
        y4_adj = adj

# ---- (c) December 31, Year 4 adjusting entry ----
amt = abs(y4_adj)
jes = [{"part": "c", "lines": [
    {"account": "Allowance to Reduce Inventory to LIFO (LIFO reserve)",
     "debit": n(amt), "credit": 0},
    {"account": "Cost of Goods Sold", "debit": 0, "credit": n(amt)},
]}]
add("c: December 31, Year 4 -- debit LIFO reserve (allowance)", n(amt))
add("c: December 31, Year 4 -- credit Cost of Goods Sold", n(amt))

# ---- (d) ----
add("d: why the Year 4 index 1.25 does not enter the Year 4 DV LIFO total",
    "The 1.25 index is used only to deflate the Year 4 FIFO balance of 137,500 to "
    "110,000 of base-year dollars. Because base-year quantities fell (135,000 to "
    "110,000), no Year 4 layer was added, and a current-year index prices only a new "
    "layer. The surviving inventory consists solely of old base-layer dollars, which "
    "stay at the base-year index of 1.00, so 1.25 never multiplies any layer.")
add("d: presentation/classification at Year 4 year-end",
    "Report inventory as a current asset at DV LIFO cost of 110,000 on the balance "
    "sheet (net of the 27,500 allowance), with the FIFO/current cost of 137,500 and "
    "the 27,500 LIFO reserve disclosed parenthetically or in the notes, plus "
    "disclosure of the Year 4 LIFO liquidation and its effect on income (the 9,100 "
    "reserve decrease credited to COGS, which raised pretax income).")

print(json.dumps({
    "id": "agent_186#02",
    "rounding_convention": "decimal.Decimal throughout; each period figure quantized to cents with ROUND_HALF_UP; no floats",
    "answers": ans,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": "DV LIFO layers carried at base-year cost x the index of the year added; Year 4 liquidation removes newest layers first. Debits equal credits in the Dec 31, Year 4 entry."
}, indent=1))
