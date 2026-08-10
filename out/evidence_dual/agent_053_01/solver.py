"""
Northfork Merchandising LLC -- LIFO reserve (allowance to reduce inventory to LIFO).

Rounding convention: decimal.Decimal throughout, ROUND_HALF_UP applied per period
(each year's reserve and delta-reserve computed and rounded to whole dollars
independently, no cumulative-precision carryforward). All inputs are whole dollars
so no rounding actually bites; the quantizer is applied anyway for discipline.

Derivation logic (bottom-up from the fact pattern):
  * Internal records are kept at AVERAGE COST. External reporting is LIFO.
  * LIFO reserve (a.k.a. "Allowance to Reduce Inventory to LIFO") =
        internal-basis (average cost) ending inventory - LIFO ending inventory.
    It is a credit-balance contra-asset carried at the cumulative amount.
  * Delta reserve for a year = reserve at end of year - reserve at end of prior year
    (prior reserve = 0 before Year 1, since Year 1 is the first year of operations).
  * A period-end adjusting entry moves the allowance to its required balance:
        increase in reserve  -> Dr COGS, Cr Allowance to Reduce Inventory to LIFO
        decrease in reserve  -> Dr Allowance to Reduce Inventory to LIFO, Cr COGS
    ("Adjustments are recognized in the accounts", so real JEs are made, and the
     effect runs through Cost of Goods Sold -- often titled "Cost of Goods Sold"
     or "LIFO Effect"/"Effect of change to LIFO" -- here COGS.)
  * Balance sheet: Inventory at average cost (gross, internal method), less the
    allowance, equals inventory at LIFO (net) -- which must tie to the given LIFO
    ending inventory figure.
  * Cumulative effect on COGS over Years 1-3 = sum of the yearly COGS debits/credits,
    which telescopes to the Year 3 ending reserve (= net debit to COGS, i.e., COGS
    higher cumulatively / income lower).
"""
from decimal import Decimal, ROUND_HALF_UP
import json

TWO = Decimal("1")  # whole dollars
def q(x: Decimal) -> Decimal:
    return Decimal(x).quantize(TWO, rounding=ROUND_HALF_UP)

def n(d: Decimal):
    d = q(d)
    return int(d) if d == d.to_integral_value() else float(d)

# ---- given facts (stem) ----
avg = {1: Decimal("90000"), 2: Decimal("105000"), 3: Decimal("98000")}
lifo = {1: Decimal("55000"), 2: Decimal("62000"), 3: Decimal("70000")}
years = [1, 2, 3]

# ---- (a) reserve + delta schedule ----
reserve = {}
delta = {}
prior = Decimal("0")  # Year 1 is first year of operations -> no opening reserve
for y in years:
    reserve[y] = q(avg[y] - lifo[y])
    delta[y] = q(reserve[y] - prior)
    prior = reserve[y]

# internal check: gross - allowance == LIFO for every year
for y in years:
    assert q(avg[y] - reserve[y]) == q(lifo[y]), y

answers = []
schedule_rows = []
for y in years:
    opening = Decimal("0") if y == 1 else reserve[y - 1]
    schedule_rows.append({
        "year": y,
        "ending_inventory_average_cost": n(avg[y]),
        "ending_inventory_lifo": n(lifo[y]),
        "required_ending_lifo_reserve": n(reserve[y]),
        "opening_lifo_reserve": n(opening),
        "change_in_reserve": n(delta[y]),
        "direction": "increase" if delta[y] > 0 else ("decrease" if delta[y] < 0 else "no change"),
        "cogs_effect": ("Dr COGS " if delta[y] > 0 else "Cr COGS ") + str(abs(n(delta[y]))) if delta[y] != 0 else "none",
    })
    answers.append({"label": f"a: Year {y} — ending inventory at average cost (internal, gross)", "value": n(avg[y])})
    answers.append({"label": f"a: Year {y} — ending inventory at LIFO (external, net)", "value": n(lifo[y])})
    answers.append({"label": f"a: Year {y} — opening LIFO reserve (allowance) balance", "value": n(opening)})
    answers.append({"label": f"a: Year {y} — required ending LIFO reserve (average cost − LIFO)", "value": n(reserve[y])})
    answers.append({"label": f"a: Year {y} — Δ reserve (change to record; positive = increase)", "value": n(delta[y])})

# ---- (b)/(c) journal entries ----
jes = []
def build_je(part, y):
    d = delta[y]
    lines = []
    if d > 0:
        lines.append({"account": "Cost of Goods Sold", "debit": n(d), "credit": 0})
        lines.append({"account": "Allowance to Reduce Inventory to LIFO (LIFO reserve)", "debit": 0, "credit": n(d)})
    elif d < 0:
        lines.append({"account": "Allowance to Reduce Inventory to LIFO (LIFO reserve)", "debit": n(-d), "credit": 0})
        lines.append({"account": "Cost of Goods Sold", "debit": 0, "credit": n(-d)})
    tot_d = sum(Decimal(str(l["debit"])) for l in lines)
    tot_c = sum(Decimal(str(l["credit"])) for l in lines)
    assert tot_d == tot_c, (part, tot_d, tot_c)
    return {"part": part, "date": f"December 31, Year {y}",
            "memo": ("Create allowance to reduce inventory to LIFO" if y == 1
                     else f"Adjust LIFO reserve from {n(reserve[y-1])} to {n(reserve[y])}"),
            "lines": lines}

jes.append(build_je("b", 1))
jes.append(build_je("c", 2))
jes.append(build_je("c", 3))

answers.append({"label": "b: Dec 31 Year 1 — Dr Cost of Goods Sold", "value": n(delta[1])})
answers.append({"label": "b: Dec 31 Year 1 — Cr Allowance to Reduce Inventory to LIFO", "value": n(delta[1])})
answers.append({"label": "c: Dec 31 Year 2 — Dr Cost of Goods Sold", "value": n(delta[2])})
answers.append({"label": "c: Dec 31 Year 2 — Cr Allowance to Reduce Inventory to LIFO", "value": n(delta[2])})
answers.append({"label": "c: Dec 31 Year 3 — Dr Allowance to Reduce Inventory to LIFO (reserve declined)", "value": n(-delta[3])})
answers.append({"label": "c: Dec 31 Year 3 — Cr Cost of Goods Sold", "value": n(-delta[3])})
answers.append({"label": "c: Allowance balance after Dec 31 Year 2 entry", "value": n(reserve[2])})
answers.append({"label": "c: Allowance balance after Dec 31 Year 3 entry", "value": n(reserve[3])})

# ---- (d) balance sheet presentation, Dec 31 Year 3 ----
gross3 = avg[3]
allow3 = reserve[3]
net3 = q(gross3 - allow3)
assert net3 == q(lifo[3])
answers.append({"label": "d: BS Dec 31 Yr 3 — Inventory at average cost (gross, internal method)", "value": n(gross3)})
answers.append({"label": "d: BS Dec 31 Yr 3 — Less: Allowance to reduce inventory to LIFO", "value": n(allow3)})
answers.append({"label": "d: BS Dec 31 Yr 3 — Inventory at LIFO (net carrying amount)", "value": n(net3)})

# ---- (e) cumulative effect on COGS, Years 1-3 ----
cum = q(sum(delta[y] for y in years))
assert cum == reserve[3]  # telescoping check
answers.append({"label": "e: Cumulative net effect on COGS, Years 1–3 (net DEBIT to COGS; = ending reserve)", "value": n(cum)})
answers.append({"label": "e: Cumulative effect on pretax income, Years 1–3 (decrease)", "value": n(cum)})

out = {
    "id": "agent_053#01",
    "rounding_convention": "decimal.Decimal money; ROUND_HALF_UP quantized to whole dollars per period (each year's reserve and Δ reserve rounded independently). Inputs are whole dollars, so no rounding difference arises; schedule closes exactly (gross − allowance = LIFO each year, and Σ Δ reserve = Year 3 ending reserve).",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": ("LIFO reserve = internal average-cost inventory − LIFO inventory: Yr1 90,000−55,000=35,000; "
              "Yr2 105,000−62,000=43,000; Yr3 98,000−70,000=28,000. Δ reserve: Yr1 +35,000 (from zero, first year "
              "of operations); Yr2 +8,000; Yr3 −15,000. Because adjustments are recognized in the accounts, each "
              "year-end entry adjusts the contra-asset 'Allowance to Reduce Inventory to LIFO' to its required "
              "balance with the offset to Cost of Goods Sold: Yr1 Dr COGS 35,000 / Cr Allowance 35,000; "
              "Yr2 Dr COGS 8,000 / Cr Allowance 8,000; Yr3 Dr Allowance 15,000 / Cr COGS 15,000 (reserve declined, "
              "so the entry reverses part of the allowance and credits COGS). Dec 31 Yr 3 balance sheet: inventory "
              "at average cost 98,000 less allowance 28,000 = 70,000 net LIFO, which ties to the given LIFO figure. "
              "Cumulative COGS effect Yr1–Yr3 = 35,000 + 8,000 − 15,000 = 28,000 net DEBIT to COGS (equals the "
              "ending reserve, since the reserve began at zero), i.e., cumulative pretax income is 28,000 lower "
              "under LIFO than under average cost. Schedule rows in extra_schedule.")
}
out["extra_schedule"] = schedule_rows
print(json.dumps(out, indent=2))
