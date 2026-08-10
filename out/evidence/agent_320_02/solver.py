#!/usr/bin/env python3
"""Solver for item agent_320#02 - Aspen Forge Tools Inc., LCM by individual item.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal, never float. Every figure in this fact pattern is
given in whole dollars and every operation is addition/subtraction/min/max, so
no rounding is mathematically required. The convention is nevertheless applied
deliberately and uniformly: each reported amount is quantized to cents with
ROUND_HALF_UP at the point it is reported (round-at-report, not round-at-end of
a chain of averages), matching this course's ROUND_HALF_UP-per-period rule.
No present-value factors are involved in this item.

METHOD (ASC 330 / Kieso LCM, used because the company is on LIFO)
-----------------------------------------------------------------
Per item i:
    ceiling (NRV)          = estimated selling price - cost to complete & sell
    floor (NRV - profit)   = ceiling - normal profit margin
    designated market      = median(replacement cost, ceiling, floor)
                             i.e. RC bounded above by ceiling, below by floor
    LCM carrying amount    = min(LIFO cost, designated market)
    write-down             = LIFO cost - LCM carrying amount   (never negative)

Required allowance at a balance sheet date = sum of the item write-downs
(item-by-item application, so item gains never offset item losses).

Allowance method, adjusted only at December 31:
    period-end adjustment = required ending allowance - unadjusted allowance
    positive -> credit the allowance (debit COGS or Holding Loss)
    negative -> debit the allowance (credit COGS), i.e. a partial recovery

Year 2: all Year 1 ending inventory was sold during Year 2, so the entire Year 1
allowance relates to goods no longer on hand; the December 31, Year 2 entry
trues the allowance up to the Year 2 required balance in one step.

Run:  python3 solver.py    -> prints one JSON object on stdout
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def D(x: str) -> Decimal:
    return Decimal(x)


def money(x: Decimal) -> Decimal:
    """Report-time quantization: 2dp, ROUND_HALF_UP."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly plain number: int when whole, else float-free string-parsed Decimal->float."""
    q = money(x)
    return int(q) if q == q.to_integral_value() else float(q)


# ---------------------------------------------------------------------------
# Facts from the stem (December 31, Year 1 ending inventory, by item line)
# ---------------------------------------------------------------------------
ITEMS = [
    # name,           LIFO cost,  selling price, cost to complete & sell, normal profit, replacement cost
    ("Edger line", D("26000"), D("30000"), D("3000"), D("3000"), D("16000")),
    ("Clipper line", D("50000"), D("90000"), D("28000"), D("18000"), D("36000")),
    ("Blade Set line", D("15500"), D("18000"), D("1000"), D("2000"), D("14200")),
]

PREADJ_COGS_Y1 = D("210000")          # Year 1 COGS before the LCM adjustment
ALLOWANCE_BEFORE_Y1 = D("0")          # allowance credit balance before Year 1 entry

Y2_COST = D("70000")                  # Year 2 ending inventory at LIFO cost
Y2_DESIGNATED_MARKET = D("66000")     # already constrained by ceiling/floor


# ---------------------------------------------------------------------------
# (a) Per-item ceiling / floor / designated market / LCM / write-down
# ---------------------------------------------------------------------------
def lcm_item(cost, sp, cts, npm, rc):
    ceiling = sp - cts
    floor = ceiling - npm
    designated = min(max(rc, floor), ceiling)   # median of rc, ceiling, floor
    lcm = min(cost, designated)
    writedown = cost - lcm
    if writedown < 0:
        writedown = D("0")
    return ceiling, floor, designated, lcm, writedown


rows = []
total_cost = D("0")
total_lcm = D("0")
total_writedown = D("0")
for name, cost, sp, cts, npm, rc in ITEMS:
    ceiling, floor, designated, lcm, wd = lcm_item(cost, sp, cts, npm, rc)
    rows.append((name, cost, ceiling, floor, designated, lcm, wd))
    total_cost += cost
    total_lcm += lcm
    total_writedown += wd

required_allowance_y1 = total_writedown

# sanity: totals must tie
assert total_cost - total_lcm == total_writedown, "item totals do not tie"

# ---------------------------------------------------------------------------
# (b)/(c) December 31, Year 1 period-end adjusting entry
# ---------------------------------------------------------------------------
y1_adjustment = required_allowance_y1 - ALLOWANCE_BEFORE_Y1   # credit to allowance

# ---------------------------------------------------------------------------
# (d) Year 1 presentation
# ---------------------------------------------------------------------------
bs_inventory_at_cost = total_cost
bs_allowance = required_allowance_y1
bs_net_inventory = bs_inventory_at_cost - bs_allowance

is_cogs_under_b = PREADJ_COGS_Y1 + y1_adjustment      # write-down buried in COGS
is_cogs_under_c = PREADJ_COGS_Y1                      # COGS untouched
is_holding_loss_under_c = y1_adjustment               # separate loss line
pretax_income_effect = -y1_adjustment                 # identical under (b) and (c)

# ---------------------------------------------------------------------------
# (e) December 31, Year 2
# ---------------------------------------------------------------------------
required_allowance_y2 = Y2_COST - Y2_DESIGNATED_MARKET
if required_allowance_y2 < 0:
    required_allowance_y2 = D("0")

allowance_before_y2_entry = required_allowance_y1     # Year 1 credit balance carries
y2_adjustment = required_allowance_y2 - allowance_before_y2_entry   # negative => debit allowance
y2_allowance_debit = -y2_adjustment                   # amount debited to the allowance

# ---------------------------------------------------------------------------
# Assemble output
# ---------------------------------------------------------------------------
answers = []
for name, cost, ceiling, floor, designated, lcm, wd in rows:
    answers.append({"label": f"a: {name} - ceiling (NRV)", "value": num(ceiling)})
    answers.append({"label": f"a: {name} - floor (NRV less normal profit)", "value": num(floor)})
    answers.append({"label": f"a: {name} - designated market", "value": num(designated)})
    answers.append({"label": f"a: {name} - LCM carrying amount", "value": num(lcm)})
    answers.append({"label": f"a: {name} - write-down", "value": num(wd)})

answers.append({"label": "a: total LCM carrying amount (all items)", "value": num(total_lcm)})
answers.append({"label": "a: required allowance at 12/31 Year 1 (total write-down)",
                "value": num(required_allowance_y1)})

answers.append({"label": "d: balance sheet - inventory at LIFO cost, 12/31 Year 1",
                "value": num(bs_inventory_at_cost)})
answers.append({"label": "d: balance sheet - less allowance to reduce inventory to market",
                "value": num(bs_allowance)})
answers.append({"label": "d: balance sheet - inventory, net (at LCM), 12/31 Year 1",
                "value": num(bs_net_inventory)})
answers.append({"label": "d: income statement under (b) - Year 1 COGS after adjustment",
                "value": num(is_cogs_under_b)})
answers.append({"label": "d: income statement under (c) - Year 1 COGS after adjustment",
                "value": num(is_cogs_under_c)})
answers.append({"label": "d: income statement under (c) - holding loss on inventory",
                "value": num(is_holding_loss_under_c)})
answers.append({"label": "d: pretax income effect Year 1 (same under (b) and (c))",
                "value": num(pretax_income_effect)})

answers.append({"label": "e: required allowance at 12/31 Year 2",
                "value": num(required_allowance_y2)})
answers.append({"label": "e: Year 2 period-end adjustment (debit to allowance, reduction)",
                "value": num(y2_allowance_debit)})

journal_entries = [
    {
        "part": "b",
        "lines": [
            {"account": "Cost of Goods Sold", "debit": num(y1_adjustment), "credit": 0},
            {"account": "Allowance to Reduce Inventory to Market",
             "debit": 0, "credit": num(y1_adjustment)},
        ],
    },
    {
        "part": "c",
        "lines": [
            {"account": "Holding Loss on Inventory", "debit": num(y1_adjustment), "credit": 0},
            {"account": "Allowance to Reduce Inventory to Market",
             "debit": 0, "credit": num(y1_adjustment)},
        ],
    },
    {
        "part": "e",
        "lines": [
            {"account": "Allowance to Reduce Inventory to Market",
             "debit": num(y2_allowance_debit), "credit": 0},
            {"account": "Cost of Goods Sold", "debit": 0, "credit": num(y2_allowance_debit)},
        ],
    },
]

# debits must equal credits in every entry
for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, f"entry {je['part']} does not balance: {dr} vs {cr}"

notes = (
    "(a) Designated market = median(replacement cost, ceiling, floor). Replacement cost falls "
    "below the floor on all three lines, so the floor is the designated market for each: "
    "Edger 24,000 (RC 16,000 < floor), Clipper 44,000 (RC 36,000 < floor), Blade Set 15,000 "
    "(RC 14,200 < floor). LCM is applied item by item, so no item's unrealized gain offsets "
    "another item's write-down. "
    "(f) LCM (ceiling/floor/replacement-cost model) rather than LCNRV applies because Aspen "
    "Forge measures inventory using LIFO. Under ASC 330 as amended by ASU 2015-11, the simpler "
    "lower-of-cost-and-net-realizable-value rule is available only to inventories measured by "
    "FIFO or average cost; LIFO and retail-inventory-method companies remain on the traditional "
    "lower-of-cost-or-market model with the NRV ceiling and NRV-less-normal-profit floor. "
    "(e) Because all Year 1 ending inventory was sold during Year 2, the entire 8,500 Year 1 "
    "allowance relates to goods no longer on hand; the 12/31 Year 2 true-up reduces the "
    "allowance from 8,500 to the 4,000 required (70,000 cost less 66,000 designated market), "
    "a 4,500 debit to the allowance and credit to COGS (a recovery, limited to amounts "
    "previously written down)."
)

out = {
    "id": "agent_320#02",
    "rounding_convention": (
        "decimal.Decimal only, no floats; amounts quantized to 2 decimal places with "
        "ROUND_HALF_UP at the point of reporting (all inputs are whole dollars, so no "
        "rounding differences arise); no PV factors involved"
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(out, indent=2))
