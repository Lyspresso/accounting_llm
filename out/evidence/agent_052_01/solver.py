#!/usr/bin/env python3
"""
Solver for agent_052#01 -- Lakebound Merchants Inc., LO 9-5.
Perpetual inventory: moving average, FIFO, and LIFO cost flow.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; no floats appear anywhere in this module.

* Rounding mode: ROUND_HALF_UP, applied PER TRANSACTION (per period), never
  deferred to the end.
* Moving-average unit cost is recomputed after every purchase (a "moving"
  average under the perpetual system) and is carried at 4 decimal places,
  quantized ROUND_HALF_UP.  The cost of each sale is (units sold x that
  4-decimal unit cost), then quantized to cents ROUND_HALF_UP at the moment of
  the sale.  The remaining inventory carrying amount is taken as
  (balance before sale - cost of that sale) so that the running ledger stays
  internally consistent to the cent and no rounding residue accumulates in a
  fictitious extra layer.
* FIFO and LIFO consume whole unit-cost layers, so every figure is exact at the
  cent and rounding is never actually invoked; the quantization is still applied
  so the code is convention-correct if the inputs changed.
* Final presentation: every reported amount quantized to cents (2 dp),
  ROUND_HALF_UP.

No PV/discounting is involved in this item, so no PV table-factor convention
applies.

Everything below is derived from the stem's transaction table.  The only
hard-coded values are the fact pattern itself (dates, units, unit costs,
selling prices).

Run:  python3 solver.py      -> prints one JSON object on stdout
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
UNIT_COST_Q = Decimal("0.0001")  # moving-average unit cost carried to 4 dp


def money(x: Decimal) -> Decimal:
    """Quantize to cents, ROUND_HALF_UP."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def unit_cost(x: Decimal) -> Decimal:
    """Quantize a moving-average unit cost to 4 dp, ROUND_HALF_UP."""
    return x.quantize(UNIT_COST_Q, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly number: int when whole, else float of the cent-exact value."""
    x = money(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------------------
# Fact pattern straight from the stem
# ---------------------------------------------------------------------------
# (date, kind, units, unit cost OR selling price)
BEGINNING = ("Oct 1", 500, Decimal("8"))

ACTIVITY = [
    ("Oct 6", "purchase", 300, Decimal("10")),
    ("Oct 12", "sale", 400, Decimal("18")),
    ("Oct 18", "purchase", 500, Decimal("11")),
    ("Oct 25", "sale", 450, Decimal("19")),
    ("Oct 30", "purchase", 100, Decimal("12")),
]


# ---------------------------------------------------------------------------
# (a)(1) Moving average, perpetual
# ---------------------------------------------------------------------------
def moving_average():
    units = BEGINNING[1]
    balance = money(Decimal(units) * BEGINNING[2])
    avg = unit_cost(balance / Decimal(units))
    cogs = Decimal("0.00")
    trail = [{"date": BEGINNING[0], "event": "beginning inventory",
              "units": units, "unit_cost": float(avg), "balance": num(balance)}]

    for date, kind, qty, price in ACTIVITY:
        if kind == "purchase":
            balance = money(balance + money(Decimal(qty) * price))
            units += qty
            avg = unit_cost(balance / Decimal(units))
            trail.append({"date": date, "event": "purchase",
                          "units": units, "unit_cost": float(avg),
                          "balance": num(balance)})
        else:
            cost_of_sale = money(Decimal(qty) * avg)
            cogs += cost_of_sale
            balance = money(balance - cost_of_sale)
            units -= qty
            # unit cost is unchanged by a sale under moving average
            trail.append({"date": date, "event": "sale",
                          "units": units, "unit_cost": float(avg),
                          "balance": num(balance),
                          "cost_of_sale": num(cost_of_sale)})

    return money(balance), money(cogs), units, trail


# ---------------------------------------------------------------------------
# (a)(2)/(3) Layered cost flows, perpetual
# ---------------------------------------------------------------------------
def layered(method: str):
    """method: 'FIFO' consumes the oldest layer first, 'LIFO' the newest."""
    layers = [[BEGINNING[1], BEGINNING[2]]]  # [units, unit cost]
    cogs = Decimal("0.00")
    sale_costs = {}
    trail = [{"date": BEGINNING[0], "event": "beginning inventory",
              "layers": [[BEGINNING[1], float(BEGINNING[2])]],
              "balance": num(Decimal(BEGINNING[1]) * BEGINNING[2])}]

    def balance_of(ls):
        return money(sum((Decimal(u) * c for u, c in ls), Decimal("0")))

    for date, kind, qty, price in ACTIVITY:
        if kind == "purchase":
            layers.append([qty, price])
            trail.append({"date": date, "event": "purchase",
                          "layers": [[u, float(c)] for u, c in layers],
                          "balance": num(balance_of(layers))})
        else:
            remaining = qty
            cost_of_sale = Decimal("0")
            while remaining > 0:
                idx = 0 if method == "FIFO" else len(layers) - 1
                take = min(remaining, layers[idx][0])
                cost_of_sale += Decimal(take) * layers[idx][1]
                layers[idx][0] -= take
                remaining -= take
                if layers[idx][0] == 0:
                    layers.pop(idx)
            cost_of_sale = money(cost_of_sale)
            sale_costs[date] = cost_of_sale
            cogs += cost_of_sale
            trail.append({"date": date, "event": "sale",
                          "layers": [[u, float(c)] for u, c in layers],
                          "balance": num(balance_of(layers)),
                          "cost_of_sale": num(cost_of_sale)})

    ei = balance_of(layers)
    ei_units = sum(u for u, _ in layers)
    return ei, money(cogs), ei_units, trail, sale_costs


def main():
    # Goods available for sale -- used only for the part (d) confirmation.
    cogas = money(Decimal(BEGINNING[1]) * BEGINNING[2] +
                  sum((Decimal(q) * p for _, k, q, p in ACTIVITY
                       if k == "purchase"), Decimal("0")))

    ma_ei, ma_cogs, ma_units, ma_trail = moving_average()
    fifo_ei, fifo_cogs, fifo_units, fifo_trail, _ = layered("FIFO")
    lifo_ei, lifo_cogs, lifo_units, lifo_trail, lifo_sale_costs = layered("LIFO")

    # The running schedules part (a) asks to "show" are intermediates, so they
    # are not reported; they are used here as internal cross-checks that the
    # ledger rolled forward to the same ending balance the totals claim.
    for trail, ei in ((ma_trail, ma_ei), (fifo_trail, fifo_ei), (lifo_trail, lifo_ei)):
        assert Decimal(str(trail[-1]["balance"])) == ei, trail[-1]

    # ---- (d) confirmation: COGAS - EI == COGS for each method -------------
    confirmations = {
        "moving_average": cogas - ma_ei == ma_cogs,
        "fifo": cogas - fifo_ei == fifo_cogs,
        "lifo": cogas - lifo_ei == lifo_cogs,
    }
    assert all(confirmations.values()), confirmations
    assert ma_units == fifo_units == lifo_units

    # ---- (b) purchase journal entries -------------------------------------
    journal = []
    for date, kind, qty, cost in ACTIVITY:
        if kind != "purchase":
            continue
        amt = money(Decimal(qty) * cost)
        journal.append({
            "part": "b",
            "date": date,
            "lines": [
                {"account": "Inventory", "debit": num(amt), "credit": 0},
                {"account": "Accounts Payable", "debit": 0, "credit": num(amt)},
            ],
        })

    # ---- (c) sales + COGS journal entries under LIFO -----------------------
    for date, kind, qty, sp in ACTIVITY:
        if kind != "sale":
            continue
        revenue = money(Decimal(qty) * sp)
        cost = lifo_sale_costs[date]
        journal.append({
            "part": "c",
            "date": date,
            "lines": [
                {"account": "Accounts Receivable", "debit": num(revenue), "credit": 0},
                {"account": "Sales Revenue", "debit": 0, "credit": num(revenue)},
            ],
        })
        journal.append({
            "part": "c",
            "date": date,
            "lines": [
                {"account": "Cost of Goods Sold", "debit": num(cost), "credit": 0},
                {"account": "Inventory", "debit": 0, "credit": num(cost)},
            ],
        })

    for je in journal:
        d = sum(Decimal(str(l["debit"])) for l in je["lines"])
        c = sum(Decimal(str(l["credit"])) for l in je["lines"])
        assert d == c, je

    answers = [
        {"label": "a1: moving average - ending inventory", "value": num(ma_ei)},
        {"label": "a1: moving average - COGS", "value": num(ma_cogs)},
        {"label": "a2: FIFO - ending inventory", "value": num(fifo_ei)},
        {"label": "a2: FIFO - COGS", "value": num(fifo_cogs)},
        {"label": "a3: LIFO - ending inventory", "value": num(lifo_ei)},
        {"label": "a3: LIFO - COGS", "value": num(lifo_cogs)},
    ]

    notes = (
        "1,400 units available, 850 sold, 550 units in ending inventory under all "
        "three methods. Moving-average unit cost after each purchase: $8.75 (Oct 6), "
        "$10.00 (Oct 18), $10.3636 (Oct 30); a sale does not change the average. "
        "FIFO layers at Oct 31: 450 @ $11 + 100 @ $12. LIFO layers at Oct 31: "
        "400 @ $8 + 50 @ $11 + 100 @ $12. Part (d) verified in code: "
        "goods available for sale less ending inventory equals COGS for moving "
        "average, FIFO and LIFO alike (assertion passes). Part (a)'s running "
        "balances/layers and part (d)'s check total are omitted from `answers` "
        "because they are schedule detail and a check figure, not reported amounts."
    )

    out = {
        "id": "agent_052#01",
        "rounding_convention": (
            "decimal.Decimal only, no floats. ROUND_HALF_UP applied per "
            "transaction (per period), not deferred to the end. Moving-average "
            "unit cost recomputed after each purchase and carried at 4 decimals "
            "(ROUND_HALF_UP); each sale's cost = units x that unit cost, "
            "quantized to cents at the sale date, with the inventory balance "
            "rolled forward as prior balance minus that cost so no rounding "
            "residue accumulates. FIFO/LIFO consume whole layers, so all amounts "
            "are cent-exact. All reported figures quantized to cents "
            "ROUND_HALF_UP. No PV factors involved in this item."
        ),
        "answers": answers,
        "journal_entries": journal,
        "insufficient_info": False,
        "notes": notes,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
