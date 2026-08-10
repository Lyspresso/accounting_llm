#!/usr/bin/env python3
"""Blind solver — Lakeshore Goods LLC, multi-year LIFO retail (item agent_327#00).

WHAT THIS SOLVES
----------------
Three consecutive years of the LIFO retail method (textbook LO 10-9,
Demo 10-9A), plus the periodic-system journal entries the Required parts ask
for (initial purchase recognition, sales, and the December 31 period-end
adjusting entry each year).

METHOD (derived from the fact pattern in stem.md, nothing hard-coded)
---------------------------------------------------------------------
Step 1 — Ending inventory at retail, AVERAGE COST retail approach.
    Both net markups AND net markdowns are treated as relating to purchases
    and are included in the goods-available-at-retail column:
        EI_retail = (BI_retail + net_purchases_retail + markups - markdowns)
                    - net_sales
    (Conventional retail, which excludes markdowns from the ratio denominator
    to approximate LCM, is deliberately NOT used here — see part (f).)

Step 2 — Cost ratios.
    Base (prior-year) ratio  = BI_cost / BI_retail
    Current-year ratio       = purchases_cost
                               / (purchases_retail + markups - markdowns)
    Each year gets its own current-year ratio; a layer keeps forever the ratio
    of the year that created it.

Step 3 — LIFO layer schedule.
    If EI_retail > BI_retail, the excess is a NEW layer costed at this year's
    ratio. If EI_retail < BI_retail, layers are LIQUIDATED newest-first (LIFO)
    until the remaining layers sum to EI_retail; no new layer is created.
    EI_cost = sum over surviving layers of (layer_retail * layer_ratio).

Step 4 — COGS (periodic, residual):
    COGS = BI_cost + net_purchases_cost - EI_cost

Each year's closing EI (cost and retail) and the surviving layer stack roll
forward to become the next year's beginning inventory.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal — never float.
- Cost ratios are computed exactly and then quantized to 4 decimal places
  using ROUND_HALF_UP (the textbook states ratios such as 0.58 / 0.60).
- Each layer's cost is computed as layer_retail * quantized_ratio and then
  quantized to the cent using ROUND_HALF_UP -- i.e. ROUND_HALF_UP PER LAYER
  PER PERIOD, not once at the end. Ending inventory at cost is the sum of the
  already-rounded layer costs.
- COGS is a residual (BI_cost + purchases_cost - EI_cost) and so absorbs any
  rounding difference, which keeps the period-end journal entry in balance by
  construction.
- Money is reported to the cent; values that are whole dollars print as
  integers in the JSON.
No PV/annuity factors are involved in this item.

USAGE
-----
    python3 solver.py            # prints one JSON object on stdout
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP, getcontext
from typing import List

getcontext().prec = 40

CENT = Decimal("0.01")
RATIO_Q = Decimal("0.0001")

ITEM_ID = "agent_327#00"


def money(x: Decimal) -> Decimal:
    """Quantize to the cent, ROUND_HALF_UP (applied per layer, per period)."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def ratio(numer: Decimal, denom: Decimal) -> Decimal:
    """Cost ratio to 4 dp, ROUND_HALF_UP."""
    return (numer / denom).quantize(RATIO_Q, rounding=ROUND_HALF_UP)


def jnum(x: Decimal):
    """Render a Decimal for JSON: int when whole, else float-free string->float."""
    x = money(x)
    if x == x.to_integral_value():
        return int(x)
    return float(x)


# ----------------------------------------------------------------------------
# Fact pattern, transcribed from stem.md
# ----------------------------------------------------------------------------

BI_COST_Y1 = Decimal("58000")
BI_RETAIL_Y1 = Decimal("100000")


@dataclass
class YearFacts:
    name: str
    purch_cost: Decimal
    purch_retail: Decimal
    markups: Decimal
    markdowns: Decimal
    sales: Decimal


YEARS = [
    YearFacts("Year 1", Decimal("372000"), Decimal("600000"),
              Decimal("40000"), Decimal("20000"), Decimal("560000")),
    YearFacts("Year 2", Decimal("420000"), Decimal("700000"),
              Decimal("35000"), Decimal("35000"), Decimal("640000")),
    YearFacts("Year 3", Decimal("300000"), Decimal("500000"),
              Decimal("20000"), Decimal("20000"), Decimal("620000")),
]


@dataclass
class Layer:
    """One LIFO layer: retail dollars carried at the ratio of its origin year."""
    origin: str
    retail: Decimal
    cost_ratio: Decimal

    @property
    def cost(self) -> Decimal:
        return money(self.retail * self.cost_ratio)


@dataclass
class YearResult:
    name: str
    ei_retail: Decimal
    current_ratio: Decimal
    layers: List[Layer]
    ei_cost: Decimal
    cogs: Decimal
    bi_cost: Decimal
    bi_retail: Decimal
    liquidations: List[dict] = field(default_factory=list)
    new_layer_retail: Decimal = Decimal("0")


def run() -> List[YearResult]:
    # Base layer, established on adoption 1/1/Year 1.
    base_ratio = ratio(BI_COST_Y1, BI_RETAIL_Y1)
    layers: List[Layer] = [Layer("Base (1/1/Year 1)", BI_RETAIL_Y1, base_ratio)]

    bi_cost = BI_COST_Y1
    bi_retail = BI_RETAIL_Y1

    results: List[YearResult] = []

    for yf in YEARS:
        # --- Step 1: EI at retail, average cost retail approach ------------
        current_retail = yf.purch_retail + yf.markups - yf.markdowns
        goods_avail_retail = bi_retail + current_retail
        ei_retail = goods_avail_retail - yf.sales

        # --- Step 2: current-year cost ratio -------------------------------
        current_ratio = ratio(yf.purch_cost, current_retail)

        # --- Step 3: layer schedule ---------------------------------------
        new_layers = [Layer(l.origin, l.retail, l.cost_ratio) for l in layers]
        liquidations: List[dict] = []
        new_layer_retail = Decimal("0")

        if ei_retail > bi_retail:
            new_layer_retail = ei_retail - bi_retail
            new_layers.append(Layer(yf.name, new_layer_retail, current_ratio))
        elif ei_retail < bi_retail:
            # Liquidate newest layers first until the stack equals EI at retail.
            shortfall = bi_retail - ei_retail
            while shortfall > 0 and new_layers:
                top = new_layers[-1]
                if top.retail <= shortfall:
                    liquidations.append({
                        "layer": top.origin,
                        "retail_liquidated": top.retail,
                        "cost_ratio": top.cost_ratio,
                        "cost_removed": top.cost,
                        "fully_liquidated": True,
                    })
                    shortfall -= top.retail
                    new_layers.pop()
                else:
                    liquidations.append({
                        "layer": top.origin,
                        "retail_liquidated": shortfall,
                        "cost_ratio": top.cost_ratio,
                        "cost_removed": money(shortfall * top.cost_ratio),
                        "fully_liquidated": False,
                    })
                    top.retail -= shortfall
                    shortfall = Decimal("0")

        # sanity: layers must reconcile to EI at retail
        assert sum((l.retail for l in new_layers), Decimal("0")) == ei_retail, (
            f"{yf.name}: layer retail does not tie to EI at retail")

        ei_cost = sum((l.cost for l in new_layers), Decimal("0"))

        # --- Step 4: COGS as periodic residual ------------------------------
        cogs = bi_cost + yf.purch_cost - ei_cost

        results.append(YearResult(
            name=yf.name,
            ei_retail=ei_retail,
            current_ratio=current_ratio,
            layers=new_layers,
            ei_cost=ei_cost,
            cogs=cogs,
            bi_cost=bi_cost,
            bi_retail=bi_retail,
            liquidations=liquidations,
            new_layer_retail=new_layer_retail,
        ))

        # roll forward
        layers = new_layers
        bi_cost = ei_cost
        bi_retail = ei_retail

    return results


def line(account: str, debit: Decimal = Decimal("0"),
         credit: Decimal = Decimal("0")) -> dict:
    return {"account": account, "debit": jnum(debit), "credit": jnum(credit)}


def period_end_entry(part: str, r: YearResult, purch_cost: Decimal) -> dict:
    """Periodic close (textbook Demo 9-2A form): establish EI, close BI and
    Purchases, record COGS as the balancing residual."""
    lines = [
        line("Inventory, Ending (December 31, %s — at LIFO retail cost)" % r.name,
             debit=r.ei_cost),
        line("Cost of Goods Sold", debit=r.cogs),
        line("Inventory, Beginning (January 1, %s)" % r.name, credit=r.bi_cost),
        line("Purchases", credit=purch_cost),
    ]
    return {"part": part,
            "description": "December 31, %s period-end adjusting entry "
                           "(periodic close)" % r.name,
            "lines": lines}


def main() -> None:
    y1, y2, y3 = run()
    base_ratio = ratio(BI_COST_Y1, BI_RETAIL_Y1)

    answers = []

    # ---- (a) Year 1 -------------------------------------------------------
    answers += [
        {"label": "a: Year 1 ending inventory at retail (average cost retail approach)",
         "value": jnum(y1.ei_retail)},
        {"label": "a: base (prior-year) cost ratio",
         "value": float(base_ratio)},
        {"label": "a: Year 1 current-year cost ratio",
         "value": float(y1.current_ratio)},
        {"label": "a: Year 1 layer schedule — base layer at retail",
         "value": jnum(y1.layers[0].retail)},
        {"label": "a: Year 1 layer schedule — base layer at cost",
         "value": jnum(y1.layers[0].cost)},
        {"label": "a: Year 1 layer schedule — Year 1 layer at retail",
         "value": jnum(y1.layers[1].retail)},
        {"label": "a: Year 1 layer schedule — Year 1 layer at cost",
         "value": jnum(y1.layers[1].cost)},
        {"label": "a: Year 1 ending inventory at LIFO retail cost",
         "value": jnum(y1.ei_cost)},
        {"label": "a: Year 1 cost of goods sold", "value": jnum(y1.cogs)},
    ]

    # ---- (d) Year 2 -------------------------------------------------------
    answers += [
        {"label": "d: Year 2 ending inventory at retail",
         "value": jnum(y2.ei_retail)},
        {"label": "d: Year 2 cost ratio", "value": float(y2.current_ratio)},
        {"label": "d: Year 2 layer schedule — base layer at cost",
         "value": jnum(y2.layers[0].cost)},
        {"label": "d: Year 2 layer schedule — Year 1 layer at cost",
         "value": jnum(y2.layers[1].cost)},
        {"label": "d: Year 2 layer schedule — Year 2 layer at retail",
         "value": jnum(y2.layers[2].retail)},
        {"label": "d: Year 2 layer schedule — Year 2 layer at cost",
         "value": jnum(y2.layers[2].cost)},
        {"label": "d: Year 2 ending inventory at LIFO retail cost",
         "value": jnum(y2.ei_cost)},
        {"label": "d: Year 2 cost of goods sold", "value": jnum(y2.cogs)},
    ]

    # ---- (e) Year 3 -------------------------------------------------------
    answers += [
        {"label": "e: Year 3 ending inventory at retail",
         "value": jnum(y3.ei_retail)},
        {"label": "e: Year 3 cost ratio", "value": float(y3.current_ratio)},
    ]
    for liq in y3.liquidations:
        answers.append({
            "label": "e: layer liquidated — %s layer, retail liquidated"
                     % liq["layer"],
            "value": jnum(liq["retail_liquidated"]),
        })
        answers.append({
            "label": "e: layer liquidated — %s layer, LIFO cost removed"
                     % liq["layer"],
            "value": jnum(liq["cost_removed"]),
        })
    answers += [
        {"label": "e: Year 3 ending inventory at LIFO retail cost (base layer only)",
         "value": jnum(y3.ei_cost)},
        {"label": "e: Year 3 cost of goods sold", "value": jnum(y3.cogs)},
    ]

    # ---- journal entries --------------------------------------------------
    y1f, y2f, y3f = YEARS

    entries = [
        {"part": "b",
         "description": "Year 1 — initial recognition of net purchases on account "
                        "(periodic system)",
         "lines": [line("Purchases", debit=y1f.purch_cost),
                   line("Accounts Payable", credit=y1f.purch_cost)]},
        {"part": "b",
         "description": "Year 1 — net sales (cash and on account). Under a periodic "
                        "system only revenue is recorded at the date of sale; the "
                        "retail pool is relieved at period end in part (c).",
         "lines": [line("Cash and Accounts Receivable", debit=y1f.sales),
                   line("Sales Revenue", credit=y1f.sales)]},
        period_end_entry("c", y1, y1f.purch_cost),
        period_end_entry("d", y2, y2f.purch_cost),
        period_end_entry("e", y3, y3f.purch_cost),
    ]

    for e in entries:
        d = sum(Decimal(str(l["debit"])) for l in e["lines"])
        c = sum(Decimal(str(l["credit"])) for l in e["lines"])
        assert d == c, "unbalanced entry in part %s: %s vs %s" % (e["part"], d, c)

    notes = (
        "(f) LIFO retail uses the average cost retail cost-ratio approach — "
        "including BOTH net markups and net markdowns in the ratio — because the "
        "goal is to approximate actual LIFO cost of each layer, whereas the "
        "conventional retail approach deliberately omits net markdowns from the "
        "denominator to build in a lower-of-cost-or-market write-down, which would "
        "distort the cost of the LIFO layers. "
        "Year 3 is a liquidation year: ending inventory at retail of 100,000 is "
        "below beginning inventory at retail of 220,000, so the Year 2 layer "
        "(60,000 retail at 0.60) and the Year 1 layer (60,000 retail at 0.60) are "
        "both fully liquidated and no Year 3 layer is created; only the 100,000 "
        "base layer at 0.580 survives. "
        "The sales entry in part (b) combines cash and on-account sales on one "
        "debit line because the stem does not split the 560,000 between them."
    )

    out = {
        "id": ITEM_ID,
        "rounding_convention": (
            "decimal.Decimal throughout, never float. Cost ratios quantized to "
            "4 dp ROUND_HALF_UP; each LIFO layer's cost quantized to the cent "
            "ROUND_HALF_UP per layer per period (round-per-period, not "
            "round-at-end); ending inventory at cost is the sum of the rounded "
            "layer costs; COGS taken as the periodic residual "
            "(BI cost + net purchases at cost - EI cost). No PV factors apply."
        ),
        "answers": answers,
        "journal_entries": entries,
        "insufficient_info": False,
        "notes": notes,
    }

    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
