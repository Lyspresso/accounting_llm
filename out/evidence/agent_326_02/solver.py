#!/usr/bin/env python3
"""Blind solver — Summit Peak Retail Group, conventional retail method (LO 10-8).

Item id: agent_326#02

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; no binary floats are used anywhere in the
derivation. Money is quantized to whole cents ("0.01") with ROUND_HALF_UP,
applied per computed figure (round-at-each-reported-figure, not round-at-end),
which is this course's convention.

Cost ratios are carried as EXACT Decimal quotients (Decimal division at 28
significant digits) when applied to convert retail amounts to cost; the ratio is
rounded only for *reporting*. Reported ratios are expressed as percentages
rounded to 2 decimal places with ROUND_HALF_UP (e.g. 53.49 means 53.49%).
Here the conventional ratio is exactly 0.50, so no rounding difference can arise
on the cost conversions; the average-cost comparison ratio in part (b) is
reporting-only and is never applied to an amount.

METHOD (per Kieso/Wahlen "Complicating Factors for Retail Inventory Methods",
Demo 10-8C, conventional retail = LCM approximation):

  Cost column   : BI + purchases + freight-in - purchase returns
                  - abnormal casualty cost
  Retail column : BI + purchases - purchase returns + net markups
                  - abnormal casualty retail
  Cost ratio    = cost GAS / retail GAS  (net markups IN, net markdowns OUT)

  Deducted BELOW the cost ratio, retail column only:
      net sales (gross sales - sales returns restored to inventory),
      employee discounts, normal spoilage, net markdowns.

Periodic system, so the period-end entry establishes ending inventory, removes
beginning inventory, and closes the purchase-side accounts into COGS.

Run: python3 solver.py   -> prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Quantize to whole cents, ROUND_HALF_UP."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def pct(x: Decimal) -> Decimal:
    """Express a ratio as a percentage rounded to 2 dp, ROUND_HALF_UP."""
    return (Decimal(x) * Decimal(100)).quantize(CENT, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------------------
# Given fact pattern (stem only)
# ---------------------------------------------------------------------------
BI_COST = Decimal("50000")
BI_RETAIL = Decimal("100000")

PURCHASES_COST = Decimal("200000")
PURCHASES_RETAIL = Decimal("400000")

FREIGHT_IN = Decimal("10000")

PURCH_RET_COST = Decimal("10000")
PURCH_RET_RETAIL = Decimal("20000")

NET_MARKUPS = Decimal("20000")

CASUALTY_COST = Decimal("20000")
CASUALTY_RETAIL = Decimal("40000")

SALES_GROSS = Decimal("360000")
SALES_RETURNS = Decimal("20000")      # goods restored to inventory
EMPLOYEE_DISCOUNTS = Decimal("5000")
NORMAL_SPOILAGE = Decimal("5000")
NET_MARKDOWNS = Decimal("30000")

PHYSICAL_COUNT_RETAIL = Decimal("74000")

# ---------------------------------------------------------------------------
# (a) Conventional retail schedule
# ---------------------------------------------------------------------------
# Cost column: freight-in ADDS to cost only; purchase returns reduce both;
# abnormal casualty removed from BOTH columns BEFORE the ratio.
gas_cost = money(
    BI_COST + PURCHASES_COST + FREIGHT_IN - PURCH_RET_COST - CASUALTY_COST
)

# Retail column for the RATIO denominator: net markups included,
# net markdowns EXCLUDED (that is what makes it "conventional"/LCM).
gas_retail_conventional = money(
    BI_RETAIL
    + PURCHASES_RETAIL
    - PURCH_RET_RETAIL
    + NET_MARKUPS
    - CASUALTY_RETAIL
)

cost_ratio = gas_cost / gas_retail_conventional          # exact Decimal quotient

# Deductions below the ratio, retail column only.
net_sales = money(SALES_GROSS - SALES_RETURNS)
ei_retail_est = money(
    gas_retail_conventional
    - net_sales
    - EMPLOYEE_DISCOUNTS
    - NORMAL_SPOILAGE
    - NET_MARKDOWNS
)

ei_cost_est = money(ei_retail_est * cost_ratio)

# ---------------------------------------------------------------------------
# (b) What the AVERAGE COST retail ratio would have been
#     (same pre-ratio cost and retail; markdowns subtracted from the retail base)
# ---------------------------------------------------------------------------
gas_retail_average = money(gas_retail_conventional - NET_MARKDOWNS)
avg_cost_ratio = gas_cost / gas_retail_average

# ---------------------------------------------------------------------------
# (c) Journal entries
# ---------------------------------------------------------------------------
# (c1) Abnormal casualty removal; cost is removed out of Purchases.
je_c1 = [
    {"account": "Loss from Abnormal Casualty (Theft)", "debit": money(CASUALTY_COST), "credit": money(Decimal(0))},
    {"account": "Purchases", "debit": money(Decimal(0)), "credit": money(CASUALTY_COST)},
]

# (c2) Period-end adjusting/closing entry, periodic system.
# Purchases account balance after the casualty credit in (c1):
purchases_after_casualty = money(PURCHASES_COST - CASUALTY_COST)
cogs_before_shrinkage = money(gas_cost - ei_cost_est)

je_c2 = [
    {"account": "Inventory (ending, 12/31/Yr 1 — estimated)", "debit": ei_cost_est, "credit": money(Decimal(0))},
    {"account": "Cost of Goods Sold", "debit": cogs_before_shrinkage, "credit": money(Decimal(0))},
    {"account": "Purchase Returns", "debit": money(PURCH_RET_COST), "credit": money(Decimal(0))},
    {"account": "Inventory (beginning, 1/1/Yr 1)", "debit": money(Decimal(0)), "credit": money(BI_COST)},
    {"account": "Purchases", "debit": money(Decimal(0)), "credit": purchases_after_casualty},
    {"account": "Freight-In", "debit": money(Decimal(0)), "credit": money(FREIGHT_IN)},
]

# ---------------------------------------------------------------------------
# (d) Shrinkage and settlement to the physical count
# ---------------------------------------------------------------------------
shrinkage_retail = money(ei_retail_est - PHYSICAL_COUNT_RETAIL)
shrinkage_cost = money(shrinkage_retail * cost_ratio)

je_d = [
    {"account": "Cost of Goods Sold (inventory shrinkage)", "debit": shrinkage_cost, "credit": money(Decimal(0))},
    {"account": "Inventory", "debit": money(Decimal(0)), "credit": shrinkage_cost},
]

# ---------------------------------------------------------------------------
# (e) Balance sheet ending inventory after settlement
# ---------------------------------------------------------------------------
ei_cost_final = money(ei_cost_est - shrinkage_cost)
# Independent cross-check: physical count at retail x cost ratio.
assert ei_cost_final == money(PHYSICAL_COUNT_RETAIL * cost_ratio)

# ---------------------------------------------------------------------------
# Integrity checks
# ---------------------------------------------------------------------------
for entry in (je_c1, je_c2, je_d):
    debits = sum((ln["debit"] for ln in entry), Decimal("0"))
    credits = sum((ln["credit"] for ln in entry), Decimal("0"))
    assert debits == credits, (debits, credits)


# ---------------------------------------------------------------------------
# Serialization: Decimal -> int/float only at the JSON boundary
# ---------------------------------------------------------------------------
def jnum(d: Decimal):
    d = Decimal(d)
    return int(d) if d == d.to_integral_value() else float(d)


def convert(obj):
    if isinstance(obj, Decimal):
        return jnum(obj)
    if isinstance(obj, dict):
        return {k: convert(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [convert(v) for v in obj]
    return obj


result = {
    "id": "agent_326#02",
    "rounding_convention": (
        "Decimal only, no floats. Money quantized to cents with ROUND_HALF_UP at each "
        "reported figure. Cost ratio carried as an exact Decimal quotient when converting "
        "retail to cost; ratios reported as percentages rounded to 2 dp ROUND_HALF_UP. "
        "Conventional ratio = markups in / markdowns out; markdowns deducted below the ratio."
    ),
    "answers": [
        {"label": "a: cost ratio, conventional retail (percent)", "value": pct(cost_ratio)},
        {"label": "a: estimated ending inventory at retail (before physical count)", "value": ei_retail_est},
        {"label": "a: estimated ending inventory at cost (before physical count)", "value": ei_cost_est},
        {"label": "b: average cost retail cost ratio if net markdowns included in denominator (percent)", "value": pct(avg_cost_ratio)},
        {"label": "d: shrinkage at retail", "value": shrinkage_retail},
        {"label": "d: shrinkage at cost", "value": shrinkage_cost},
        {"label": "e: ending inventory reported on the balance sheet after settlement", "value": ei_cost_final},
    ],
    "journal_entries": [
        {"part": "c1", "lines": je_c1},
        {"part": "c2", "lines": je_c2},
        {"part": "d", "lines": je_d},
    ],
    "insufficient_info": False,
    "notes": (
        "Conventional retail per Demo 10-8C: freight-in added to cost only; purchase returns "
        "deducted from both columns; abnormal casualty removed from both columns before the ratio; "
        "sales returns (goods restored) netted against gross sales; employee discounts, normal "
        "spoilage and net markdowns deducted in the retail column below the ratio. Part (c2) closes "
        "the Purchases balance net of the casualty credit from (c1)."
    ),
}

print(json.dumps(convert(result), indent=2))
