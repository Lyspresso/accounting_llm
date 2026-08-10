#!/usr/bin/env python3
"""Blind solver for item agent_189#00 — CedarPeak Outdoor Gear LLC.

Topic: LIFO / lower-of-cost-or-market (LCM) applied to each individual item,
Allowance to Reduce Inventory to Market maintained under the year-end
true-up method, multi-year allowance rollforward, period-end adjusting
entries, and a disposal/settlement alternative that closes the allowance
into Cost of Goods Sold.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal, never float.  Every monetary figure is
quantized to two decimal places (cents) with ROUND_HALF_UP, applied
per period / per line item as it is computed (round-per-period, not
round-at-end).  Per-unit LCM amounts are rounded to cents first, then
multiplied by whole-unit quantities, which is how an item-by-item LCM
schedule is prepared.  No present-value factors are involved in this
item.  Every input in the fact pattern is a whole dollar amount, so the
rounding rule never actually bites here — it is stated and applied so the
script is reproducible under the course convention.

MEASUREMENT RULES APPLIED (traditional LCM, required because cost flow is LIFO)
------------------------------------------------------------------------------
  ceiling (NRV)            = estimated selling price - estimated cost to
                             complete and sell
  floor (NRV less normal   = ceiling - normal profit margin
        profit)
  designated market        = middle value of (replacement cost, ceiling, floor)
                             i.e. RC bounded above by the ceiling and below by
                             the floor
  LCM per unit             = lower of original cost and designated market
  write-down per unit      = cost - LCM (never negative; no write-ups above cost)

Allowance method, year-end true-up: the required allowance at each
year-end is (inventory at cost - designated market of that inventory) but
never below zero.  The adjusting entry moves the unadjusted (carry-over)
allowance to the required balance, debiting or crediting COGS for the
difference.  The allowance is NOT closed when inventory turns; it is
closed only on the specified sale-settlement date in part (f).

Run:  python3 solver.py     -> prints one JSON object on stdout
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENTS = Decimal("0.01")


def m(x) -> Decimal:
    """Money constructor + rounding convention (ROUND_HALF_UP to cents)."""
    return Decimal(str(x)).quantize(CENTS, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly plain number: int when whole, else float-free string->float."""
    d = d.quantize(CENTS, rounding=ROUND_HALF_UP)
    if d == d.to_integral_value():
        return int(d)
    # Keep exactness by emitting the decimal literal through json as a number
    return float(d)


# ---------------------------------------------------------------------------
# Fact pattern — Year 1 ending inventory, per-unit data at December 31, Year 1
# ---------------------------------------------------------------------------
# (item, qty, selling price, cost to complete & sell, normal profit margin,
#  original cost (LIFO), replacement cost)
ITEMS = [
    ("AlpineShell", 120, "95", "15", "12", "78", "70"),
    ("BaseLayer", 200, "42", "6", "7", "32", "38"),
    ("TrailBoot", 90, "130", "22", "18", "105", "88"),
    ("SummitPoles", 150, "55", "8", "6", "48", "40"),
    ("DayPack", 75, "110", "18", "14", "72", "95"),
]

UNADJUSTED_ALLOWANCE_Y1 = m("0")
COGS_Y1_BEFORE_LCM = m("412000")

# Aggregate LIFO cost and designated market for subsequent years
SUBSEQUENT = [
    ("Year 2", m("44200"), m("39850")),
    ("Year 3", m("41000"), m("41800")),
]

# Part (f) disposal / settlement alternative
SALE_CASH = m("42500")
SALE_INVENTORY_COST = m("44200")  # Year 2 ending inventory cost still on books


# ---------------------------------------------------------------------------
# (a) + (b)  Item-by-item ceiling / floor / market / LCM, and the schedule
# ---------------------------------------------------------------------------
schedule = []
total_cost = m("0")
total_lcm = m("0")
total_writedown = m("0")

for name, qty, sp, ctcs, npm, cost, rc in ITEMS:
    sp, ctcs, npm, cost, rc = m(sp), m(ctcs), m(npm), m(cost), m(rc)

    ceiling = m(sp - ctcs)                       # net realizable value
    floor = m(ceiling - npm)                     # NRV less normal profit margin

    # designated market = middle of (RC, ceiling, floor)
    if rc > ceiling:
        market, constraint = ceiling, "ceiling"
    elif rc < floor:
        market, constraint = floor, "floor"
    else:
        market, constraint = rc, "RC"

    lcm_unit = min(cost, market)
    wd_unit = m(cost - lcm_unit)
    if wd_unit < 0:
        wd_unit = m("0")

    ext_cost = m(cost * qty)
    ext_lcm = m(lcm_unit * qty)
    ext_wd = m(ext_cost - ext_lcm)

    total_cost += ext_cost
    total_lcm += ext_lcm
    total_writedown += ext_wd

    schedule.append(
        dict(item=name, qty=qty, ceiling=ceiling, floor=floor, market=market,
             constraint=constraint, lcm_unit=lcm_unit, wd_unit=wd_unit,
             ext_cost=ext_cost, ext_lcm=ext_lcm, ext_wd=ext_wd)
    )

total_cost, total_lcm, total_writedown = m(total_cost), m(total_lcm), m(total_writedown)

# Internal consistency: sum of item write-downs must equal cost - LCM totals
assert total_writedown == m(total_cost - total_lcm)

# ---------------------------------------------------------------------------
# (c) Initial recognition at December 31, Year 1
# ---------------------------------------------------------------------------
required_allow_y1 = total_writedown            # cost - designated market, item approach
adjustment_y1 = m(required_allow_y1 - UNADJUSTED_ALLOWANCE_Y1)   # credit to allowance
inventory_net_y1 = m(total_cost - required_allow_y1)
cogs_y1_after_lcm = m(COGS_Y1_BEFORE_LCM + adjustment_y1)

# ---------------------------------------------------------------------------
# (d) Multi-year subsequent measurement / allowance rollforward, Years 1-3
#     Year-end true-up method: allowance is not closed when inventory turns.
# ---------------------------------------------------------------------------
rollforward = []
unadjusted = UNADJUSTED_ALLOWANCE_Y1
periods = [("Year 1", total_cost, total_lcm)] + SUBSEQUENT

for label, cost_amt, market_amt in periods:
    required = m(cost_amt - market_amt)
    if required < 0:
        required = m("0")                       # market above cost -> no allowance
    # Positive adjustment = credit to the allowance (increase, Dr COGS);
    # negative adjustment = debit to the allowance (decrease, Cr COGS).
    delta = m(required - unadjusted)
    ending = required
    net = m(cost_amt - ending)
    rollforward.append(
        dict(period=label, cost=cost_amt, market=market_amt, required=required,
             unadjusted=unadjusted, delta=delta, ending=ending, net=net)
    )
    unadjusted = ending

allow_end_y2 = rollforward[1]["ending"]

# ---------------------------------------------------------------------------
# (f) March 15, Year 3 sale of all Year 2 inventory + closing the allowance
# ---------------------------------------------------------------------------
gross_cogs_on_sale = SALE_INVENTORY_COST
allowance_closed = allow_end_y2
net_cogs_layer = m(gross_cogs_on_sale - allowance_closed)


# ---------------------------------------------------------------------------
# Answers — only figures the Required parts ask for
# ---------------------------------------------------------------------------
answers = []

# (a) per item: ceiling, floor, designated market, LCM per unit, constraint
for r in schedule:
    answers.append({"label": f"a: {r['item']} — ceiling (NRV) per unit",
                    "value": num(r["ceiling"])})
    answers.append({"label": f"a: {r['item']} — floor (NRV less normal profit) per unit",
                    "value": num(r["floor"])})
    answers.append({"label": f"a: {r['item']} — designated market per unit",
                    "value": num(r["market"])})
    answers.append({"label": f"a: {r['item']} — LCM per unit",
                    "value": num(r["lcm_unit"])})
    answers.append({"label": f"a: {r['item']} — constraint setting market",
                    "value": r["constraint"]})

# (b) schedule totals by item + total required write-down
for r in schedule:
    answers.append({"label": f"b: {r['item']} — total cost", "value": num(r["ext_cost"])})
    answers.append({"label": f"b: {r['item']} — total LCM", "value": num(r["ext_lcm"])})
    answers.append({"label": f"b: {r['item']} — write-down", "value": num(r["ext_wd"])})
answers.append({"label": "b: total inventory at cost", "value": num(total_cost)})
answers.append({"label": "b: total inventory at LCM (item approach)", "value": num(total_lcm)})
answers.append({"label": "b: total required write-down, Year 1", "value": num(total_writedown)})

# (c) balance-sheet presentation + income-statement effect
answers.append({"label": "c: balance sheet — inventory at LIFO cost, Dec 31 Year 1",
                "value": num(total_cost)})
answers.append({"label": "c: balance sheet — less allowance to reduce inventory to market",
                "value": num(required_allow_y1)})
answers.append({"label": "c: balance sheet — inventory, net (Dec 31 Year 1)",
                "value": num(inventory_net_y1)})
answers.append({"label": "c: income statement — COGS after LCM adjustment, Year 1",
                "value": num(cogs_y1_after_lcm)})

# (d) rollforward columns, Years 1-3
for r in rollforward:
    p = r["period"]
    answers.append({"label": f"d: {p} — inventory cost", "value": num(r["cost"])})
    answers.append({"label": f"d: {p} — designated market", "value": num(r["market"])})
    answers.append({"label": f"d: {p} — required allowance", "value": num(r["required"])})
    answers.append({"label": f"d: {p} — unadjusted allowance", "value": num(r["unadjusted"])})
    answers.append({
        "label": f"d: {p} — adjustment to allowance Dr/(Cr)",
        "value": num(m(-r["delta"])),  # credit shown as negative, debit as positive
    })
    answers.append({"label": f"d: {p} — ending allowance", "value": num(r["ending"])})
    answers.append({"label": f"d: {p} — inventory, net", "value": num(r["net"])})

# (f) net COGS on the settled layer
answers.append({"label": "f: net COGS related to the Year 2 inventory layer",
                "value": num(net_cogs_layer)})


# ---------------------------------------------------------------------------
# Journal entries
# ---------------------------------------------------------------------------
Z = 0


def line(acct, dr=None, cr=None):
    return {"account": acct,
            "debit": num(dr) if dr is not None else Z,
            "credit": num(cr) if cr is not None else Z}


journal_entries = []

# (c) December 31, Year 1 initial recognition
journal_entries.append({
    "part": "c",
    "date": "December 31, Year 1",
    "lines": [
        line("Cost of Goods Sold", dr=adjustment_y1),
        line("Allowance to Reduce Inventory to Market", cr=adjustment_y1),
    ],
})

# (e) period-end adjusting entries, Years 1-3
for r in rollforward:
    yr = r["period"]
    d = r["delta"]
    if d > 0:      # increase the allowance
        lines = [line("Cost of Goods Sold", dr=d),
                 line("Allowance to Reduce Inventory to Market", cr=d)]
    elif d < 0:    # decrease/reverse the allowance
        amt = m(-d)
        lines = [line("Allowance to Reduce Inventory to Market", dr=amt),
                 line("Cost of Goods Sold", cr=amt)]
    else:
        lines = []
    journal_entries.append({"part": "e", "date": f"December 31, {yr}", "lines": lines})

# (f) March 15, Year 3 — sale of all Year 2 inventory, then close the allowance
journal_entries.append({
    "part": "f",
    "date": "March 15, Year 3 — sale of inventory for cash",
    "lines": [
        line("Cash", dr=SALE_CASH),
        line("Sales Revenue", cr=SALE_CASH),
    ],
})
journal_entries.append({
    "part": "f",
    "date": "March 15, Year 3 — cost of the inventory sold",
    "lines": [
        line("Cost of Goods Sold", dr=gross_cogs_on_sale),
        line("Inventory", cr=gross_cogs_on_sale),
    ],
})
journal_entries.append({
    "part": "f",
    "date": "March 15, Year 3 — close the December 31, Year 2 allowance",
    "lines": [
        line("Allowance to Reduce Inventory to Market", dr=allowance_closed),
        line("Cost of Goods Sold", cr=allowance_closed),
    ],
})

# Debits must equal credits in every entry
for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, f"unbalanced entry: {je}"

out = {
    "id": "agent_189#00",
    "rounding_convention": (
        "decimal.Decimal only; ROUND_HALF_UP to cents applied per period / per "
        "line item (round-per-period, not round-at-end). Per-unit LCM rounded "
        "first, then extended by whole-unit quantities. No PV factors apply."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Traditional LCM (LIFO cost flow): designated market = replacement cost "
        "bounded by ceiling (NRV) above and floor (NRV less normal profit) below; "
        "LCM = lower of cost and designated market, applied item by item. "
        "Year-end true-up allowance method: at Dec 31 Year 3 designated market "
        "(41,800) exceeds cost (41,000), so the required allowance is zero and the "
        "entire prior balance is reversed to COGS (recovery limited to amounts "
        "previously written down). In part (d) the adjustment column is signed "
        "Dr/(Cr): negative = credit to the allowance, positive = debit."
    ),
}

print(json.dumps(out, indent=2))
