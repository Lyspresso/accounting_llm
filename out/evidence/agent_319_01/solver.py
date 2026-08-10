#!/usr/bin/env python3
"""Blind solver — agent_319#01 (Lakeshore Pet Supply LLC, LCNRV, LO 10-1).

WHAT THIS SOLVES
----------------
Lakeshore Pet Supply LLC measures inventory using AVERAGE COST -- i.e. a method
other than LIFO and other than the retail inventory method -- so ASC 330-10-35-1B
requires the LOWER OF COST OR NET REALIZABLE VALUE (LCNRV) rule, not lower of
cost or market.  Three application levels are computed (individual item,
category, total), the stated policy is the INDIVIDUAL ITEM approach recorded
through an ALLOWANCE (contra-inventory) account with the charge to COST OF GOODS
SOLD, and the period-end presentation follows.

ROUNDING CONVENTION
-------------------
All money is ``decimal.Decimal``; floats are never used anywhere in this file.
The working context is set to ROUND_HALF_UP and every reported figure is
quantized to cents (``0.01``) at the point it is reported -- ROUND_HALF_UP per
period, i.e. each period-end comparison and its resulting write-down are rounded
once, at that period end, rather than accumulating unrounded residue.  No
present-value factors are involved in this item, so no table-factor-vs-exact-
formula choice arises.  Every input in the stem is a whole dollar amount and
LCNRV is a pure min/subtraction operation, so no rounding is actually triggered;
the convention is declared and applied so the script behaves correctly if the
same code is re-run against cent-level inputs.

METHOD
------
(a) Per item:      LCNRV(item)     = min(cost_i, nrv_i); item-approach inventory
                                     is the sum of those minima.
    Per category:  LCNRV(category) = min(sum cost in category, sum NRV in
                                     category); category-approach inventory is
                                     the sum of those minima.  Offsetting of a
                                     below-cost item against an above-cost item
                                     is permitted WITHIN a category only.
    In total:      LCNRV(total)    = min(total cost, total NRV).
    Write-down (item approach) = total cost - item-approach LCNRV.
    Per the textbook, the individual-item approach always yields the lowest
    carrying value because above-cost items may not offset below-cost items.

(b) Allowance method, charge to COGS (stated policy):
        Dr Cost of Goods Sold                                       write-down
            Cr Allowance to Reduce Inventory to Net Realizable Value write-down
    The allowance is a contra-inventory account, so Inventory stays on the books
    at original cost.  This is the FIRST period-end (no pre-existing allowance
    balance is given in the stem), so the entry equals the full required
    allowance balance rather than a top-up to it.

(c) Balance sheet:  Inventory (at cost) less the allowance = Inventory, net,
                    which equals the item-approach LCNRV.
    Income statement: COGS after adjustment = COGS before + write-down, because
                    the holding loss is charged to COGS rather than to a
                    separate holding-loss line.

Authority: ASC 330-10-35-1B, 330-10-35-8, 330-10-35-14; course text Chapter 10
LO 10-1 and DEMO 10-1 (same three-level schedule, allowance account, COGS
charge, and "COGS before adjustment + write-down" presentation).

Run:  python3 solver.py   ->  prints one JSON object on stdout.
"""

import json
from collections import OrderedDict
from decimal import Decimal, ROUND_HALF_UP, getcontext, localcontext

getcontext().rounding = ROUND_HALF_UP

CENTS = Decimal("0.01")


def money(text):
    """Parse a stem figure into Decimal. Strings only -- never float()."""
    return Decimal(text)


def q(amount):
    """Quantize to cents under ROUND_HALF_UP, then render as a plain number."""
    with localcontext() as ctx:
        ctx.rounding = ROUND_HALF_UP
        value = Decimal(amount).quantize(CENTS, rounding=ROUND_HALF_UP)
    # Emit ints as ints so the JSON reads like the schedule the question wants.
    if value == value.to_integral_value():
        return int(value)
    return float(str(value))  # display only; all arithmetic above is Decimal


# ---------------------------------------------------------------------------
# Fact pattern, transcribed verbatim from the stem.
# ---------------------------------------------------------------------------
INVENTORY = [
    # (item, category, cost, NRV)
    ("Grain Blend", "Dry Food", money("36000"), money("32500")),
    ("Senior Blend", "Dry Food", money("21000"), money("23000")),
    ("Chew Rope", "Accessories", money("14500"), money("15800")),
    ("Puzzle Toy", "Accessories", money("29000"), money("26500")),
]

COGS_BEFORE = money("255000")

# Stem's stated column totals, used only as an internal transcription check.
STATED_TOTAL_COST = money("100500")
STATED_TOTAL_NRV = money("97800")


def lower_of(a, b):
    return a if a <= b else b


def main():
    total_cost = sum((row[2] for row in INVENTORY), Decimal("0"))
    total_nrv = sum((row[3] for row in INVENTORY), Decimal("0"))

    # Transcription guard: the derived column sums must match the stem's totals.
    assert total_cost == STATED_TOTAL_COST, (total_cost, STATED_TOTAL_COST)
    assert total_nrv == STATED_TOTAL_NRV, (total_nrv, STATED_TOTAL_NRV)

    # --- (a) individual item -------------------------------------------------
    item_lcnrv = OrderedDict(
        (name, lower_of(cost, nrv)) for name, _cat, cost, nrv in INVENTORY
    )
    item_approach_total = sum(item_lcnrv.values(), Decimal("0"))

    # --- (a) by category -----------------------------------------------------
    cat_cost = OrderedDict()
    cat_nrv = OrderedDict()
    for _name, cat, cost, nrv in INVENTORY:
        cat_cost[cat] = cat_cost.get(cat, Decimal("0")) + cost
        cat_nrv[cat] = cat_nrv.get(cat, Decimal("0")) + nrv
    cat_lcnrv = OrderedDict(
        (cat, lower_of(cat_cost[cat], cat_nrv[cat])) for cat in cat_cost
    )
    category_approach_total = sum(cat_lcnrv.values(), Decimal("0"))

    # --- (a) in total --------------------------------------------------------
    total_approach = lower_of(total_cost, total_nrv)

    # --- (a) write-down under the stated (item) approach ---------------------
    write_down = total_cost - item_approach_total

    # --- (c) presentation ----------------------------------------------------
    inventory_net = total_cost - write_down          # = item_approach_total
    cogs_after = COGS_BEFORE + write_down
    assert inventory_net == item_approach_total

    answers = []
    for name in item_lcnrv:
        answers.append(
            {"label": "a: LCNRV by item - %s" % name, "value": q(item_lcnrv[name])}
        )
    answers.append(
        {
            "label": "a: LCNRV applied by individual item - total inventory",
            "value": q(item_approach_total),
        }
    )
    for cat in cat_lcnrv:
        answers.append(
            {"label": "a: LCNRV by category - %s" % cat, "value": q(cat_lcnrv[cat])}
        )
    answers.append(
        {
            "label": "a: LCNRV applied by category - total inventory",
            "value": q(category_approach_total),
        }
    )
    answers.append(
        {
            "label": "a: LCNRV applied to inventory in total",
            "value": q(total_approach),
        }
    )
    answers.append(
        {
            "label": "a: write-down under the individual item approach",
            "value": q(write_down),
        }
    )
    answers.append(
        {"label": "c: Inventory, net on the balance sheet", "value": q(inventory_net)}
    )
    answers.append(
        {"label": "c: Cost of goods sold after adjustment", "value": q(cogs_after)}
    )

    journal_entries = [
        {
            "part": "b",
            "date": "December 31",
            "description": "To reduce inventory to net realizable value "
            "(individual item approach; allowance account; charge to COGS)",
            "lines": [
                {
                    "account": "Cost of Goods Sold",
                    "debit": q(write_down),
                    "credit": 0,
                },
                {
                    "account": "Allowance to Reduce Inventory to "
                    "Net Realizable Value",
                    "debit": 0,
                    "credit": q(write_down),
                },
            ],
        }
    ]

    # Debits must equal credits in every entry.
    for entry in journal_entries:
        debits = sum(Decimal(str(l["debit"])) for l in entry["lines"])
        credits = sum(Decimal(str(l["credit"])) for l in entry["lines"])
        assert debits == credits, (entry["part"], debits, credits)

    out = {
        "id": "agent_319#01",
        "rounding_convention": (
            "decimal.Decimal throughout, no floats; ROUND_HALF_UP per period, "
            "quantized to cents at the period end; no PV factors involved "
            "(inputs are whole dollars, so no rounding is triggered)"
        ),
        "answers": answers,
        "journal_entries": journal_entries,
        "insufficient_info": False,
        "notes": (
            "Average cost is not LIFO/retail, so ASC 330-10-35-1B applies LCNRV "
            "(not lower of cost or market). Individual-item approach gives the "
            "lowest carrying value because above-cost items (Senior Blend, Chew "
            "Rope) cannot offset below-cost items. Category and total approaches "
            "coincide here at 97,800 because each category's NRV total happens to "
            "be below its cost total. Stem states no pre-existing allowance "
            "balance, so the Dec 31 entry is the full required allowance."
        ),
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
