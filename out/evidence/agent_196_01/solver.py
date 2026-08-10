#!/usr/bin/env python3
"""Solver for item agent_196#01 - LIFO retail single-year schedule and period-end JE.

Fact pattern (Redwood Trail Mercantile Co., adopts LIFO retail on Jan 1 of the
current year; prices stable within the year; periodic system; Dec 31 year-end):

                          At cost     At retail
    Beginning inventory   $ 50,000    $100,000
    Net purchases          240,000     400,000
    Net markups                  -      20,000
    Net markdowns                -      20,000
    Net sales                    -     350,000

METHOD (Textbook LO 10-9, Demo 10-9A "LIFO Retail Method"; periodic close entry
per Demo 9-2A):

  Step 1 - Ending inventory at retail, using the AVERAGE COST retail method
           (LIFO retail applies the average cost retail method, NOT the
           conventional method): both net markups AND net markdowns are
           included in the retail column.
             EI@retail = BI@retail + NP@retail + markups - markdowns - sales

  Step 2 - Two cost ratios:
             Base-year (prior-year) ratio = BI@cost / BI@retail
             Current-year ratio = (purchases@cost)
                                  / (purchases@retail + markups - markdowns)
           i.e. the "subtotal excluding beginning inventory" columns. Markups
           and markdowns are assumed to relate entirely to purchases.

  Step 3 - Layer schedule. Because prices are stable within the year, the whole
           change in retail inventory is a quantity change (no price-index
           deflation - that is dollar-value LIFO retail, not plain LIFO retail).
             Base layer      = min(EI@retail, BI@retail)  x base ratio
             Current layer   = EI@retail - BI@retail (if positive) x current ratio
           EI@LIFO cost = sum of layers.

  Step 4 - COGS = (BI@cost + NP@cost) - EI@LIFO cost   [periodic residual]

  Step 5 - Period-end periodic close JE: debit Inventory, Ending and Cost of
           Goods Sold; credit Purchases and Inventory, Beginning.

  Step 6 - Purchases on account during the year (periodic system => "Purchases"
           temporary account, not Inventory): debit Purchases, credit A/P.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal - never float. Cost ratios are carried as exact
Decimal quotients (here they terminate exactly: 0.50 and 0.60) and are NOT
pre-rounded before being applied to a layer; each layer's extended cost is then
rounded to the cent with ROUND_HALF_UP, per period / per layer (round-per-layer,
not round-at-end). Ending inventory at cost is the sum of the already-rounded
layer costs, and COGS is derived as the residual from that rounded total so the
period-end journal entry balances to the cent by construction. Ratios are
reported rounded to 4 decimal places (ROUND_HALF_UP) for display only.

Run: python3 solver.py    -> prints one JSON object to stdout.
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
RATIO_DP = Decimal("0.0001")


def money(x: Decimal) -> Decimal:
    """Round a Decimal to the cent, ROUND_HALF_UP."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def ratio(x: Decimal) -> Decimal:
    """Round a cost ratio to 4 dp, ROUND_HALF_UP (display only)."""
    return x.quantize(RATIO_DP, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly number: int when integral, else float of the exact 2dp string."""
    x = money(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------- given facts
BI_COST = Decimal("50000")
BI_RETAIL = Decimal("100000")
NP_COST = Decimal("240000")
NP_RETAIL = Decimal("400000")
MARKUPS = Decimal("20000")
MARKDOWNS = Decimal("20000")
NET_SALES = Decimal("350000")

# ------------------------------------- Step 1: ending inventory at retail (avg cost retail)
subtotal_excl_bi_cost = NP_COST
subtotal_excl_bi_retail = NP_RETAIL + MARKUPS - MARKDOWNS

gafs_cost = BI_COST + subtotal_excl_bi_cost
gafs_retail = BI_RETAIL + subtotal_excl_bi_retail

ei_retail = gafs_retail - NET_SALES

# ------------------------------------------------------ Step 2: the two cost ratios
base_ratio_exact = BI_COST / BI_RETAIL
current_ratio_exact = subtotal_excl_bi_cost / subtotal_excl_bi_retail

# ---------------------------------------------------- Step 3: LIFO layer schedule
# Prices stable within the year => no index deflation; retail change is quantity.
if ei_retail >= BI_RETAIL:
    base_layer_retail = BI_RETAIL
    current_layer_retail = ei_retail - BI_RETAIL
else:
    # Liquidation case: base layer is eroded, no current-year layer.
    base_layer_retail = ei_retail
    current_layer_retail = Decimal("0")

base_layer_cost = money(base_layer_retail * base_ratio_exact)
current_layer_cost = money(current_layer_retail * current_ratio_exact)
ei_lifo_cost = base_layer_cost + current_layer_cost

# ------------------------------------------------------------- Step 4: COGS (residual)
cogs = money(gafs_cost - ei_lifo_cost)

# -------------------------------------------------------------- Steps 5 & 6: JEs
je_d = [
    {"account": "Inventory, Ending (LIFO retail)", "debit": num(ei_lifo_cost), "credit": 0},
    {"account": "Cost of Goods Sold", "debit": num(cogs), "credit": 0},
    {"account": "Purchases", "debit": 0, "credit": num(NP_COST)},
    {"account": "Inventory, Beginning", "debit": 0, "credit": num(BI_COST)},
]

je_e = [
    {"account": "Purchases", "debit": num(NP_COST), "credit": 0},
    {"account": "Accounts Payable", "debit": 0, "credit": num(NP_COST)},
]

journal_entries = [
    {"part": "d", "lines": je_d},
    {"part": "e", "lines": je_e},
]

# Balance check: debits must equal credits in every entry.
for entry in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in entry["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in entry["lines"])
    assert dr == cr, f"Entry {entry['part']} does not balance: {dr} vs {cr}"

# -------------------------------------------------------------------- output
answers = [
    {"label": "a: ending inventory at retail", "value": num(ei_retail)},
    {"label": "a: base-year cost ratio", "value": float(ratio(base_ratio_exact))},
    {"label": "a: current-year cost ratio", "value": float(ratio(current_ratio_exact))},
    {"label": "b: base layer at retail", "value": num(base_layer_retail)},
    {"label": "b: base layer at LIFO cost", "value": num(base_layer_cost)},
    {"label": "b: current-year layer at retail", "value": num(current_layer_retail)},
    {"label": "b: current-year layer at LIFO cost", "value": num(current_layer_cost)},
    {"label": "b: ending inventory at LIFO cost", "value": num(ei_lifo_cost)},
    {"label": "c: cost of goods sold", "value": num(cogs)},
]

out = {
    "id": "agent_196#01",
    "rounding_convention": (
        "decimal.Decimal only, no floats. Cost ratios carried as exact Decimal "
        "quotients (not pre-rounded) and applied per layer; each layer's cost "
        "rounded to the cent ROUND_HALF_UP per layer/period, not at the end. "
        "Ending inventory at cost = sum of rounded layer costs; COGS derived as "
        "the periodic residual from that total so the close entry balances. "
        "Ratios shown rounded to 4 dp ROUND_HALF_UP for display only."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "LIFO retail applies the AVERAGE COST retail method, so both net markups "
        "and net markdowns are included in the current-year cost ratio "
        "denominator (240,000 / 400,000). Prices are stated as stable within the "
        "year, so no price index is applied (that would be dollar-value LIFO "
        "retail). Periodic system, so purchases are recorded in the temporary "
        "Purchases account and COGS is a period-end residual."
    ),
}

print(json.dumps(out, indent=2))
