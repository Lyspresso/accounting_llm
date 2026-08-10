#!/usr/bin/env python3
"""Blind solver — Meridian Kitchenware Inc., multi-period LCNRV allowance (LO 10-1).

ROUNDING CONVENTION
-------------------
All money is carried as ``decimal.Decimal`` (never float). Every amount in this
fact pattern is a whole-dollar figure and every derived amount is a sum or
difference of whole-dollar figures, so no rounding is mathematically required.
The convention is nevertheless applied deliberately and uniformly: each reported
money figure is quantized to the cent with ``ROUND_HALF_UP`` at the point it is
reported (round-at-report, i.e. no intermediate re-rounding, because no
intermediate here is inexact). There are no present-value factors, interest
accruals, or per-period allocations in this item, so the "ROUND_HALF_UP per
period / PV via table factors" course convention has no additional bite.

DERIVATION NOTES
----------------
* LCNRV = min(cost, NRV) applied at the stated level of aggregation.
* Allowance method: Inventory stays on the books at FIFO cost; the contra
  account "Allowance to Reduce Inventory to Net Realizable Value" carries the
  cumulative write-down. The *required* allowance at a year-end equals
  cost - LCNRV at that date; the year-end adjusting entry is the change from
  the unadjusted (prior-year) allowance balance.
* Write-downs and recoveries both run through Cost of Goods Sold (per stem).
  Part (c) also shows the alternative "Holding Loss on Inventory" presentation.
* Year 1 uses the item approach (Meridian's stated policy). Years 2-3 use total
  cost vs total NRV, as the stem gives only totals for those dates.
* At the Apr 12, Year 4 sale the inventory leaves at full cost and the remaining
  allowance is closed to COGS, so net COGS on the layer = cost - allowance.

Run: python3 solver.py   -> prints one JSON object on stdout.
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Apply the stated rounding convention to a reported figure."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def out(x: Decimal):
    """JSON-friendly plain number (int when the cents are zero)."""
    q = money(x)
    return int(q) if q == q.to_integral_value() else float(q)


def lcnrv(cost: Decimal, nrv: Decimal) -> Decimal:
    return cost if cost < nrv else nrv


# ---------------------------------------------------------------- fact pattern
# Dec 31, Year 1 ending inventory detail: (item, category, cost, NRV)
Y1_ITEMS = [
    ("Cast Skillet", "Cookware", Decimal("28000"), Decimal("25500")),
    ("Sauce Pan Set", "Cookware", Decimal("15000"), Decimal("16200")),
    ("Chef Knife", "Cutlery", Decimal("42000"), Decimal("44000")),
    ("Bread Knife", "Cutlery", Decimal("19500"), Decimal("17000")),
]

Y2_COST, Y2_NRV = Decimal("118000"), Decimal("109200")
Y3_COST, Y3_NRV = Decimal("76000"), Decimal("72400")
Y4_SALE_CASH = Decimal("74000")

# ------------------------------------------------------- (a) Jan 5, Y1 purchase
purchase_cost = sum((c for _, _, c, _ in Y1_ITEMS), Decimal("0"))  # 104,500 derived

# ------------------------------------- (b) LCNRV schedule at Dec 31, Year 1
y1_total_cost = purchase_cost
y1_total_nrv = sum((n for _, _, _, n in Y1_ITEMS), Decimal("0"))

# (1) individual items
lcnrv_item = sum((lcnrv(c, n) for _, _, c, n in Y1_ITEMS), Decimal("0"))
writedown_item = y1_total_cost - lcnrv_item

# (2) each category
categories = []
for cat in sorted({cat for _, cat, _, _ in Y1_ITEMS}, key=lambda k: [c for _, c, _, _ in Y1_ITEMS].index(k)):
    c_cost = sum((c for _, k, c, _ in Y1_ITEMS if k == cat), Decimal("0"))
    c_nrv = sum((n for _, k, _, n in Y1_ITEMS if k == cat), Decimal("0"))
    categories.append((cat, c_cost, c_nrv, lcnrv(c_cost, c_nrv)))
lcnrv_category = sum((row[3] for row in categories), Decimal("0"))
writedown_category = y1_total_cost - lcnrv_category

# (3) inventory in total
lcnrv_total = lcnrv(y1_total_cost, y1_total_nrv)
writedown_total = y1_total_cost - lcnrv_total

# ------------------- (d) multi-year subsequent measurement schedule of allowance
schedule = []
unadjusted = Decimal("0")  # no allowance existed before Dec 31, Year 1

for year, cost, nrv, required_lcnrv in (
    ("Year 1", y1_total_cost, y1_total_nrv, lcnrv_item),          # item approach
    ("Year 2", Y2_COST, Y2_NRV, lcnrv(Y2_COST, Y2_NRV)),          # total approach
    ("Year 3", Y3_COST, Y3_NRV, lcnrv(Y3_COST, Y3_NRV)),          # total approach
):
    required_allowance = cost - required_lcnrv
    adjustment = required_allowance - unadjusted   # + => credit allowance / debit COGS
    schedule.append(
        {
            "year_end": year,
            "cost": cost,
            "nrv": nrv,
            "required_lcnrv": required_lcnrv,
            "required_allowance": required_allowance,
            "unadjusted_allowance": unadjusted,
            "adjustment": adjustment,
            "adjustment_direction": "credit allowance (debit COGS)"
            if adjustment > 0
            else ("debit allowance (credit COGS)" if adjustment < 0 else "none"),
        }
    )
    unadjusted = required_allowance

y1_adj = schedule[0]["adjustment"]          # 5,000 increase
y2_adj = schedule[1]["adjustment"]          # 3,800 increase
y3_adj = schedule[2]["adjustment"]          # 5,200 decrease (recovery)
allowance_after_y3 = schedule[2]["required_allowance"]

# --------------------------------------------- (f) Apr 12, Year 4 sale + closeout
inventory_cost_at_sale = Y3_COST
cogs_gross = inventory_cost_at_sale
allowance_closed = allowance_after_y3
net_cogs = cogs_gross - allowance_closed
gross_profit = Y4_SALE_CASH - net_cogs

# ------------------------------------------------------------- journal entries
def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": out(debit), "credit": out(credit)}


journal_entries = [
    {
        "part": "a",
        "date": "January 5, Year 1",
        "description": "Purchase on account of inventory remaining at year-end",
        "lines": [
            line("Inventory", debit=purchase_cost),
            line("Accounts Payable", credit=purchase_cost),
        ],
    },
    {
        "part": "c",
        "date": "December 31, Year 1",
        "description": "Year-end LCNRV adjustment, item approach (COGS method)",
        "lines": [
            line("Cost of Goods Sold", debit=y1_adj),
            line("Allowance to Reduce Inventory to Net Realizable Value", credit=y1_adj),
        ],
    },
    {
        "part": "c-alternative",
        "date": "December 31, Year 1",
        "description": "Same write-down presented as a separate holding loss (loss method)",
        "lines": [
            line("Holding Loss on Inventory", debit=y1_adj),
            line("Allowance to Reduce Inventory to Net Realizable Value", credit=y1_adj),
        ],
    },
    {
        "part": "e",
        "date": "December 31, Year 2",
        "description": "Increase allowance to required balance",
        "lines": [
            line("Cost of Goods Sold", debit=y2_adj),
            line("Allowance to Reduce Inventory to Net Realizable Value", credit=y2_adj),
        ],
    },
    {
        "part": "e",
        "date": "December 31, Year 3",
        "description": "Reduce allowance to required balance (recovery through COGS)",
        "lines": [
            line("Allowance to Reduce Inventory to Net Realizable Value", debit=-y3_adj),
            line("Cost of Goods Sold", credit=-y3_adj),
        ],
    },
    {
        "part": "f",
        "date": "April 12, Year 4",
        "description": "Cash sale of all remaining Year 3 ending inventory",
        "lines": [
            line("Cash", debit=Y4_SALE_CASH),
            line("Sales Revenue", credit=Y4_SALE_CASH),
        ],
    },
    {
        "part": "f",
        "date": "April 12, Year 4",
        "description": "Relieve inventory at cost",
        "lines": [
            line("Cost of Goods Sold", debit=cogs_gross),
            line("Inventory", credit=cogs_gross),
        ],
    },
    {
        "part": "f",
        "date": "April 12, Year 4",
        "description": "Close the allowance into Cost of Goods Sold",
        "lines": [
            line("Allowance to Reduce Inventory to Net Realizable Value", debit=allowance_closed),
            line("Cost of Goods Sold", credit=allowance_closed),
        ],
    },
]

# balance check — debits must equal credits in every entry
for je in journal_entries:
    d = sum((Decimal(str(l["debit"])) for l in je["lines"]), Decimal("0"))
    c = sum((Decimal(str(l["credit"])) for l in je["lines"]), Decimal("0"))
    assert d == c, f"unbalanced entry: {je['part']} {je['date']} {d} != {c}"

# ------------------------------------------------------------- required answers
answers = [
    # (b) LCNRV schedule at Dec 31, Year 1 under the three applications
    {"label": "b(1): LCNRV inventory valuation — individual-item approach", "value": out(lcnrv_item)},
    {"label": "b(1): write-down under individual-item approach (Meridian's policy)", "value": out(writedown_item)},
    {"label": "b(2): LCNRV inventory valuation — category approach", "value": out(lcnrv_category)},
    {"label": "b(2): write-down under category approach", "value": out(writedown_category)},
    {"label": "b(3): LCNRV inventory valuation — total inventory approach", "value": out(lcnrv_total)},
    {"label": "b(3): write-down under total inventory approach", "value": out(writedown_total)},
    # (d) subsequent measurement schedule of the allowance
    {"label": "d: required allowance balance at December 31, Year 1", "value": out(schedule[0]["required_allowance"])},
    {"label": "d: December 31, Year 1 adjustment (credit to allowance / debit COGS)", "value": out(y1_adj)},
    {"label": "d: required allowance balance at December 31, Year 2", "value": out(schedule[1]["required_allowance"])},
    {"label": "d: December 31, Year 2 adjustment (credit to allowance / debit COGS)", "value": out(y2_adj)},
    {"label": "d: required allowance balance at December 31, Year 3", "value": out(schedule[2]["required_allowance"])},
    {"label": "d: December 31, Year 3 adjustment (debit to allowance / credit COGS)", "value": out(-y3_adj)},
    # (f) close-out results
    {"label": "f: net cost of goods sold on this inventory layer", "value": out(net_cogs)},
    {"label": "f: gross profit on the April 12, Year 4 sale", "value": out(gross_profit)},
]

result = {
    "id": "agent_188#00",
    "rounding_convention": (
        "decimal.Decimal throughout, never float; ROUND_HALF_UP to the cent applied at "
        "the point each figure is reported (no intermediate re-rounding). All inputs and "
        "derived amounts are whole dollars, so no rounding actually bites; no PV factors "
        "or per-period allocations are involved in this item."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "LCNRV applied at the individual-item level for Year 1 per Meridian's stated policy "
        "(write-down 5,000); the category and total applications are shown only because part (b) "
        "requires the comparative schedule. Years 2-3 use total cost vs total NRV as the stem "
        "provides only totals. The Year 3 adjustment is a recovery (debit allowance, credit COGS) "
        "limited to the previously recognized write-down, so the allowance never goes below zero."
    ),
}

print(json.dumps(result, indent=2))
