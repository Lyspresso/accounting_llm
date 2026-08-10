#!/usr/bin/env python3
"""Blind solver -- agent_183#01.

Harborline Tools Corp.: perpetual inventory subsequent measurement for one SKU
under (1) moving average, (2) FIFO, (3) LIFO, plus purchase journal entries and
LIFO sale/COGS journal entries.

FACT PATTERN (from stem.md only)
--------------------------------
Perpetual records, purchases on account, gross method. November activity:
    Nov  1  Beginning inventory   800 units @ $6 cost
    Nov  4  Purchase on account   400 units @ $9 cost
    Nov 10  Credit sale           600 units @ $15 selling price
    Nov 15  Purchase on account   600 units @ $11 cost
    Nov 22  Credit sale           450 units @ $16 selling price
    Nov 28  Purchase on account   250 units @ $15 cost

METHOD
------
Every transaction is replayed in date order against a live inventory record, one
record per method, exactly as a perpetual system would post it:

  * Moving average -- the unit cost is recomputed immediately after each
    PURCHASE (total cost / total units) and that standing average is the cost
    relieved by the NEXT sale. Sales do not change the average.
  * FIFO perpetual -- layers held in purchase order; a sale consumes the oldest
    layers first.
  * LIFO perpetual -- layers held in purchase order; a sale consumes the newest
    layers on hand AT THE MOMENT OF SALE (this is the perpetual, not periodic,
    LIFO answer -- a later purchase cannot be pulled back into an earlier sale).

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP, applied per period (i.e. at each transaction), to the cent.
The moving-average unit cost is quantized to the cent with ROUND_HALF_UP
immediately after each purchase, and that rounded per-unit cost is what the next
sale relieves -- round-per-period, not round-at-end. Extended amounts are then
quantized to the cent with ROUND_HALF_UP as well. In this fact pattern every
average happens to land exactly on a whole cent ($7.00, $9.00, $10.50), so the
convention does not bite here, but it is applied deliberately rather than
assumed away. All money is decimal.Decimal; no floats are used anywhere.

No PV/discounting is involved in this item, so no table-factor convention applies.

Ending inventory under moving average is carried as the residual cost pool
(total cost less cost relieved) so the record stays internally consistent with
the per-period rounding above.

Output: one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Quantize to the cent using ROUND_HALF_UP (the course convention)."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly number: int when the cents are zero, else float of the
    already-rounded Decimal (no float arithmetic is ever performed)."""
    x = money(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------------------
# Fact pattern transcribed from the stem
# ---------------------------------------------------------------------------
BEGINNING = {"date": "Nov 1", "units": 800, "unit_cost": Decimal("6")}

EVENTS = [
    {"date": "Nov 4",  "kind": "purchase", "units": 400, "unit_cost": Decimal("9")},
    {"date": "Nov 10", "kind": "sale",     "units": 600, "unit_price": Decimal("15")},
    {"date": "Nov 15", "kind": "purchase", "units": 600, "unit_cost": Decimal("11")},
    {"date": "Nov 22", "kind": "sale",     "units": 450, "unit_price": Decimal("16")},
    {"date": "Nov 28", "kind": "purchase", "units": 250, "unit_cost": Decimal("15")},
]


# ---------------------------------------------------------------------------
# (1) Moving average perpetual
# ---------------------------------------------------------------------------
def moving_average():
    units = BEGINNING["units"]
    cost = money(Decimal(units) * BEGINNING["unit_cost"])
    avg = money(cost / Decimal(units))
    cogs = Decimal("0")
    trail = [{"after": BEGINNING["date"] + " beginning inventory",
              "units": units, "unit_cost": num(avg), "balance": num(cost)}]

    for e in EVENTS:
        if e["kind"] == "purchase":
            add = money(Decimal(e["units"]) * e["unit_cost"])
            units += e["units"]
            cost = money(cost + add)
            avg = money(cost / Decimal(units))          # re-average at purchase
            trail.append({"after": e["date"] + " purchase", "units": units,
                          "unit_cost": num(avg), "balance": num(cost)})
        else:
            relieved = money(Decimal(e["units"]) * avg)  # standing average
            units -= e["units"]
            cost = money(cost - relieved)
            cogs = money(cogs + relieved)
            trail.append({"after": e["date"] + " sale", "units": units,
                          "unit_cost": num(avg), "balance": num(cost),
                          "cogs_this_sale": num(relieved)})

    return {"ending_inventory": money(cost), "cogs": money(cogs),
            "ending_units": units, "trail": trail}


# ---------------------------------------------------------------------------
# (2)/(3) Layered perpetual: FIFO consumes oldest first, LIFO newest first
# ---------------------------------------------------------------------------
def layered(newest_first: bool):
    layers = [[BEGINNING["units"], BEGINNING["unit_cost"]]]
    cogs = Decimal("0")

    def snapshot():
        return [{"units": u, "unit_cost": num(c), "extended": num(Decimal(u) * c)}
                for u, c in layers if u > 0]

    trail = [{"after": BEGINNING["date"] + " beginning inventory",
              "layers": snapshot()}]

    for e in EVENTS:
        if e["kind"] == "purchase":
            layers.append([e["units"], e["unit_cost"]])
            trail.append({"after": e["date"] + " purchase", "layers": snapshot()})
        else:
            need = e["units"]
            relieved = Decimal("0")
            order = range(len(layers) - 1, -1, -1) if newest_first else range(len(layers))
            for i in order:
                if need == 0:
                    break
                take = min(need, layers[i][0])
                if take == 0:
                    continue
                relieved = money(relieved + money(Decimal(take) * layers[i][1]))
                layers[i][0] -= take
                need -= take
            if need != 0:
                raise ValueError("sale exceeds units on hand -- fact pattern error")
            layers[:] = [l for l in layers if l[0] > 0]
            cogs = money(cogs + relieved)
            trail.append({"after": e["date"] + " sale", "layers": snapshot(),
                          "cogs_this_sale": num(relieved)})

    ei = money(sum((Decimal(u) * c for u, c in layers), Decimal("0")))
    return {"ending_inventory": ei, "cogs": money(cogs),
            "ending_units": sum(u for u, _ in layers), "trail": trail,
            "per_sale_cogs": [t["cogs_this_sale"] for t in trail
                              if "cogs_this_sale" in t]}


def main():
    ma = moving_average()
    fifo = layered(newest_first=False)
    lifo = layered(newest_first=True)

    # (d) COGAS - EI = COGS identity, computed independently of the schedules.
    cogas = money(Decimal(BEGINNING["units"]) * BEGINNING["unit_cost"] +
                  sum((Decimal(e["units"]) * e["unit_cost"]
                       for e in EVENTS if e["kind"] == "purchase"), Decimal("0")))
    identity = {}
    for name, r in (("moving_average", ma), ("fifo", fifo), ("lifo", lifo)):
        identity[name] = bool(money(cogas - r["ending_inventory"]) == r["cogs"])
    if not all(identity.values()):
        raise AssertionError("COGAS - EI = COGS failed: %r" % identity)

    # ---------------- (b) purchase journal entries (gross method, on account)
    journal = []
    for e in EVENTS:
        if e["kind"] != "purchase":
            continue
        amt = money(Decimal(e["units"]) * e["unit_cost"])
        journal.append({
            "part": "b",
            "date": e["date"],
            "description": "Purchase of %d units @ $%s on account (gross method)"
                           % (e["units"], e["unit_cost"]),
            "lines": [
                {"account": "Inventory", "debit": num(amt), "credit": 0},
                {"account": "Accounts Payable", "debit": 0, "credit": num(amt)},
            ],
        })

    # ---------------- (c) LIFO sale + COGS entries for Nov 10 and Nov 22
    lifo_sale_cogs = list(lifo["per_sale_cogs"])
    sales = [e for e in EVENTS if e["kind"] == "sale"]
    for e, cogs_amt in zip(sales, lifo_sale_cogs):
        rev = money(Decimal(e["units"]) * e["unit_price"])
        journal.append({
            "part": "c",
            "date": e["date"],
            "description": "Credit sale of %d units @ $%s (revenue)"
                           % (e["units"], e["unit_price"]),
            "lines": [
                {"account": "Accounts Receivable", "debit": num(rev), "credit": 0},
                {"account": "Sales Revenue", "debit": 0, "credit": num(rev)},
            ],
        })
        journal.append({
            "part": "c",
            "date": e["date"],
            "description": "Cost of goods sold on the %s sale under perpetual LIFO"
                           % e["date"],
            "lines": [
                {"account": "Cost of Goods Sold", "debit": cogs_amt, "credit": 0},
                {"account": "Inventory", "debit": 0, "credit": cogs_amt},
            ],
        })

    for je in journal:
        d = sum(Decimal(str(l["debit"])) for l in je["lines"])
        c = sum(Decimal(str(l["credit"])) for l in je["lines"])
        if money(d) != money(c):
            raise AssertionError("unbalanced entry: %r" % je)

    answers = [
        {"label": "a1: ending inventory - moving average perpetual",
         "value": num(ma["ending_inventory"])},
        {"label": "a1: COGS - moving average perpetual",
         "value": num(ma["cogs"])},
        {"label": "a2: ending inventory - FIFO perpetual",
         "value": num(fifo["ending_inventory"])},
        {"label": "a2: COGS - FIFO perpetual",
         "value": num(fifo["cogs"])},
        {"label": "a3: ending inventory - LIFO perpetual",
         "value": num(lifo["ending_inventory"])},
        {"label": "a3: COGS - LIFO perpetual",
         "value": num(lifo["cogs"])},
    ]

    notes = (
        "Perpetual throughout. Moving average re-averages after each purchase only "
        "($7.00 after Nov 4, $9.00 after Nov 15, $10.50 after Nov 28); the Nov 10 "
        "sale relieves $7.00/unit and the Nov 22 sale $9.00/unit. FIFO layers after "
        "Nov 28: 150 @ $9, 600 @ $11, 250 @ $15. LIFO layers after Nov 28: 600 @ $6, "
        "150 @ $11, 250 @ $15 -- perpetual LIFO, so the Nov 22 sale draws on the "
        "Nov 15 $11 layer and the Nov 28 purchase is untouched by either sale. "
        "1,000 units on hand at Nov 30 under all three methods. Part (d) verified in "
        "code: COGAS - EI = COGS holds for moving average, FIFO and LIFO "
        "(the script raises if it does not). Part (a)'s running balances/layers are "
        "in the 'schedules' block, not in 'answers'."
    )

    out = {
        "id": "agent_183#01",
        "rounding_convention": (
            "ROUND_HALF_UP to the cent, applied per period (per transaction): the "
            "moving-average unit cost is rounded at each purchase and that rounded "
            "cost is what the next sale relieves; extended amounts rounded per "
            "transaction. decimal.Decimal only, no floats. No PV factors involved."
        ),
        "answers": answers,
        "journal_entries": journal,
        "insufficient_info": False,
        "notes": notes,
        "schedules": {
            "moving_average": ma["trail"],
            "fifo": fifo["trail"],
            "lifo": lifo["trail"],
        },
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
