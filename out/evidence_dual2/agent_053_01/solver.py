"""Northfork Merchandising LLC - LIFO reserve (allowance to reduce inventory to LIFO).

Rounding convention: all money is decimal.Decimal, quantized to whole dollars
(0.01 precision retained internally) using ROUND_HALF_UP per period. Every
figure is derived from the two inventory measurement columns; nothing hard-coded
except the given fact-pattern inputs.

Mechanics derived bottom-up:
  LIFO reserve (allowance balance) at each year-end
      = ending inventory at internal (average) cost - ending inventory at LIFO.
  The allowance is a contra-inventory account; its balance must equal the
  reserve at every balance-sheet date, so the entry each year plugs the change:
      delta = reserve(t) - reserve(t-1)      [reserve(0) = 0, Year 1 = first year]
      delta > 0 -> Dr Cost of Goods Sold, Cr Allowance
      delta < 0 -> Dr Allowance,          Cr Cost of Goods Sold
  Cumulative COGS effect over Years 1-3 = sum of deltas = ending reserve at
  Dec 31 Year 3 (net debit to COGS if positive).
"""
from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("1")


def d(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def money(x):
    q = d(x)
    return int(q)


# ---- given fact pattern ----------------------------------------------------
years = [1, 2, 3]
avg_cost = {1: Decimal("90000"), 2: Decimal("105000"), 3: Decimal("98000")}
lifo = {1: Decimal("55000"), 2: Decimal("62000"), 3: Decimal("70000")}

# ---- (a) reserve and delta schedule ---------------------------------------
reserve = {}
delta = {}
prior = {}
prev = Decimal("0")  # Year 1 is first year of operations -> no opening allowance
for y in years:
    r = d(avg_cost[y] - lifo[y])
    reserve[y] = r
    prior[y] = prev
    delta[y] = d(r - prev)
    prev = r

# ---- (e) cumulative COGS effect -------------------------------------------
cumulative = d(sum(delta[y] for y in years))

answers = []
for y in years:
    answers.append({"label": "a: Dec 31, Year %d - ending inventory at average cost" % y,
                    "value": money(avg_cost[y])})
    answers.append({"label": "a: Dec 31, Year %d - ending inventory at LIFO" % y,
                    "value": money(lifo[y])})
    answers.append({"label": "a: Dec 31, Year %d - LIFO reserve (required allowance balance)" % y,
                    "value": money(reserve[y])})
    answers.append({"label": "a: Dec 31, Year %d - prior-year allowance balance" % y,
                    "value": money(prior[y])})
    answers.append({"label": "a: Year %d - change in LIFO reserve (increase/(decrease))" % y,
                    "value": money(delta[y])})

answers.append({"label": "d: Dec 31, Year 3 balance sheet - Inventory at average cost (gross, internal method)",
                "value": money(avg_cost[3])})
answers.append({"label": "d: Dec 31, Year 3 balance sheet - Less: Allowance to reduce inventory to LIFO",
                "value": money(reserve[3])})
answers.append({"label": "d: Dec 31, Year 3 balance sheet - Inventory at LIFO (net)",
                "value": money(d(avg_cost[3] - reserve[3]))})

answers.append({"label": "e: Cumulative effect on COGS, Years 1-3 (net debit = increase in COGS)",
                "value": money(cumulative)})

# ---- (b)/(c) journal entries ----------------------------------------------
part_for = {1: "b", 2: "c", 3: "c"}
jes = []
for y in years:
    dl = delta[y]
    if dl >= 0:
        lines = [
            {"account": "Cost of Goods Sold", "debit": money(dl), "credit": 0},
            {"account": "Allowance to Reduce Inventory to LIFO", "debit": 0, "credit": money(dl)},
        ]
    else:
        amt = -dl
        lines = [
            {"account": "Allowance to Reduce Inventory to LIFO", "debit": money(amt), "credit": 0},
            {"account": "Cost of Goods Sold", "debit": 0, "credit": money(amt)},
        ]
    assert sum(l["debit"] for l in lines) == sum(l["credit"] for l in lines)
    jes.append({"part": part_for[y], "date": "Dec 31, Year %d" % y, "lines": lines})

# allowance rolls forward exactly to the Year 3 reserve
roll = Decimal("0")
for y in years:
    roll = d(roll + delta[y])
assert roll == reserve[3]

out = {
    "id": "agent_053#01",
    "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP applied per period, amounts stated in whole dollars (all given data are exact whole dollars, so no rounding difference arises). Allowance rolls forward from zero and closes exactly to the Dec 31, Year 3 reserve of $28,000.",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": "Year 1 is the first year of operations, so the opening allowance is $0 and the Year 1 entry creates the full $35,000 allowance. The allowance is a contra-inventory (valuation) account; each year-end entry is the plug that brings its balance to the current LIFO reserve. Year 3's reserve declines ($43,000 -> $28,000), so that entry is a $15,000 debit to the allowance and a credit that reduces COGS. Cumulative net debit to COGS over the three years ($35,000 + $8,000 - $15,000 = $28,000) equals the ending allowance balance.",
}
print(json.dumps(out, indent=2))
