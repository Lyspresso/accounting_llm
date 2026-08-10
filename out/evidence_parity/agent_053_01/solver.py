"""Solver for agent_053#01 — Northfork Merchandising LIFO reserve twin (LO 9-6).

Rounding convention: all money handled with decimal.Decimal, quantized to the
cent using ROUND_HALF_UP at the end of each period's computation (no rounding
inside a period beyond that). Inputs are whole dollars, so no fractional cents
arise, but the convention is applied uniformly. Dr = Cr enforced on every entry.

Derivations (nothing hard-coded beyond the given inventory data):
  LIFO reserve (allowance to reduce inventory to LIFO) = avg-cost EI - LIFO EI
  Delta reserve_t = reserve_t - reserve_{t-1}   (reserve_0 = 0, Yr1 = first year)
  Delta > 0  -> Dr COGS / Cr Allowance      (LIFO effect increases COGS)
  Delta < 0  -> Dr Allowance / Cr COGS      (reserve drawdown reduces COGS)
  BS net = avg-cost EI - allowance balance  = LIFO EI
  Cumulative COGS effect = sum of deltas = ending reserve balance (net Dr)
"""
from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def q(x: Decimal) -> Decimal:
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    x = q(x)
    return int(x) if x == x.to_integral_value() else float(x)


# --- given data -------------------------------------------------------------
DATA = [
    ("Year 1", Decimal("90000"), Decimal("55000")),
    ("Year 2", Decimal("105000"), Decimal("62000")),
    ("Year 3", Decimal("98000"), Decimal("70000")),
]

ALLOW = "Allowance to Reduce Inventory to LIFO (LIFO reserve)"
COGS = "Cost of Goods Sold"

answers = []
jes = []

prior = Decimal("0")
rows = []
for yr, avg, lifo in DATA:
    reserve = q(avg - lifo)
    delta = q(reserve - prior)
    rows.append((yr, avg, lifo, reserve, delta, prior))
    prior = reserve

# --- a. measurement schedule ------------------------------------------------
for yr, avg, lifo, reserve, delta, beg in rows:
    answers.append({"label": f"a: {yr} — ending inventory at average cost", "value": num(avg)})
    answers.append({"label": f"a: {yr} — ending inventory at LIFO", "value": num(lifo)})
    answers.append({"label": f"a: {yr} — LIFO reserve (allowance) required ending balance", "value": num(reserve)})
    answers.append({"label": f"a: {yr} — allowance beginning balance", "value": num(beg)})
    answers.append({"label": f"a: {yr} — change in LIFO reserve (Delta reserve; + = increase)", "value": num(delta)})

# --- b / c. journal entries -------------------------------------------------
part_map = {"Year 1": "b", "Year 2": "c", "Year 3": "c"}
for yr, avg, lifo, reserve, delta, beg in rows:
    part = part_map[yr]
    if delta > 0:
        lines = [
            {"account": COGS, "debit": num(delta), "credit": 0},
            {"account": ALLOW, "debit": 0, "credit": num(delta)},
        ]
        desc = f"Dr COGS / Cr Allowance {num(delta)}"
    else:
        amt = -delta
        lines = [
            {"account": ALLOW, "debit": num(amt), "credit": 0},
            {"account": COGS, "debit": 0, "credit": num(amt)},
        ]
        desc = f"Dr Allowance / Cr COGS {num(amt)}"
    assert sum(Decimal(str(l["debit"])) for l in lines) == sum(Decimal(str(l["credit"])) for l in lines)
    jes.append({"part": part, "lines": lines})
    answers.append({"label": f"{part}: Dec 31, {yr} entry amount ({desc})", "value": num(abs(delta))})

# --- d. balance sheet presentation, Dec 31 Year 3 ---------------------------
_, avg3, lifo3, res3, d3, _ = rows[2]
answers.append({"label": "d: BS Dec 31, Year 3 — Inventory at average cost (gross, internal method)", "value": num(avg3)})
answers.append({"label": "d: BS Dec 31, Year 3 — Less: Allowance to reduce inventory to LIFO", "value": num(res3)})
answers.append({"label": "d: BS Dec 31, Year 3 — Inventory, net (at LIFO)", "value": num(lifo3)})

# --- e. cumulative effect on COGS ------------------------------------------
cum = q(sum((r[4] for r in rows), Decimal("0")))
answers.append({"label": "e: Cumulative net effect on COGS, Years 1-3 (net DEBIT = increase in COGS)", "value": num(cum)})

out = {
    "id": "agent_053#01",
    "rounding_convention": "decimal.Decimal throughout; quantized to cents with ROUND_HALF_UP once per period; debits equal credits on every entry",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": "LIFO reserve = average-cost ending inventory less LIFO ending inventory: Yr1 35,000; Yr2 43,000; Yr3 28,000. Deltas: Yr1 +35,000 (create allowance, Dr COGS), Yr2 +8,000 (Dr COGS), Yr3 -15,000 (reserve declines, Dr Allowance / Cr COGS). Net cumulative debit to COGS 28,000 equals the ending allowance balance, so net inventory on the Dec 31 Year 3 balance sheet is 98,000 - 28,000 = 70,000, the LIFO amount.",
}
print(json.dumps(out, indent=1))
