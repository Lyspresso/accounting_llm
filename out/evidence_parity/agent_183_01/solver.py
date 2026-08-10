"""Harborline Tools Corp. -- perpetual MA / FIFO / LIFO (LO 9-5).

Rounding convention: all money is decimal.Decimal (never float).
Every monetary amount (extensions, moving-average unit cost, COGS, running
inventory balances) is rounded HALF_UP (decimal.ROUND_HALF_UP) to the cent as
it is computed for the period; unit counts stay exact integers.
Every figure is derived from the transaction table below -- nothing hard-coded.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
def M(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)

def f(d):
    return float(M(d))

def money(d):
    return f"${M(d):,.2f}"

# ---- source data (Nov activity) -------------------------------------------
EVENTS = [
    ("Nov 1", "BI", 800, Decimal("6")),
    ("Nov 4", "P", 400, Decimal("9")),
    ("Nov 10", "S", 600, Decimal("15")),
    ("Nov 15", "P", 600, Decimal("11")),
    ("Nov 22", "S", 450, Decimal("16")),
    ("Nov 28", "P", 250, Decimal("15")),
]

purchases = [(d, u, c) for d, t, u, c in EVENTS if t == "P"]
sales = [(d, u, c) for d, t, u, c in EVENTS if t == "S"]
bi_units, bi_cost = [(u, c) for d, t, u, c in EVENTS if t == "BI"][0]

cogas = M(bi_units * bi_cost) + sum((M(u * c) for _, u, c in purchases), Decimal("0"))
units_available = bi_units + sum(u for _, u, _ in purchases)
units_sold = sum(u for _, u, _ in sales)
units_ending = units_available - units_sold

# ---- moving average --------------------------------------------------------
ma_rows = []
u_bal, d_bal = 0, Decimal("0")
for date, typ, units, cost in EVENTS:
    if typ in ("BI", "P"):
        u_bal += units
        d_bal = M(d_bal + M(units * cost))
        avg = M(d_bal / u_bal)
        ma_rows.append({"date": date, "typ": typ, "units": units, "cogs": None,
                        "u_bal": u_bal, "d_bal": d_bal, "avg": avg})
    else:
        avg = M(d_bal / u_bal)
        cogs = M(avg * units)
        u_bal -= units
        d_bal = M(d_bal - cogs)
        ma_rows.append({"date": date, "typ": typ, "units": units, "cogs": cogs,
                        "u_bal": u_bal, "d_bal": d_bal, "avg": avg})
ma_ei, ma_cogs = d_bal, sum((r["cogs"] for r in ma_rows if r["cogs"]), Decimal("0"))

# ---- layered methods (FIFO / LIFO perpetual) -------------------------------
def layer_str(layers):
    return " + ".join(f"{u:,} @ ${c}" for u, c in layers) if layers else "none"

def layer_total(layers):
    return sum((M(u * c) for u, c in layers), Decimal("0"))

def run_layered(method):
    layers, rows = [], []
    for date, typ, units, cost in EVENTS:
        if typ in ("BI", "P"):
            layers.append([units, cost])
            rows.append({"date": date, "typ": typ, "units": units, "cogs": None,
                         "layers": [(u, c) for u, c in layers]})
        else:
            need, cogs = units, Decimal("0")
            while need > 0:
                idx = 0 if method == "FIFO" else len(layers) - 1
                take = min(need, layers[idx][0])
                cogs = M(cogs + M(take * layers[idx][1]))
                layers[idx][0] -= take
                need -= take
                if layers[idx][0] == 0:
                    layers.pop(idx)
            rows.append({"date": date, "typ": typ, "units": units, "cogs": cogs,
                         "layers": [(u, c) for u, c in layers]})
    ei = layer_total([(u, c) for u, c in layers])
    total_cogs = sum((r["cogs"] for r in rows if r["cogs"]), Decimal("0"))
    return rows, [(u, c) for u, c in layers], ei, total_cogs

fifo_rows, fifo_layers, fifo_ei, fifo_cogs = run_layered("FIFO")
lifo_rows, lifo_layers, lifo_ei, lifo_cogs = run_layered("LIFO")

# ---- answers ---------------------------------------------------------------
answers = []
def A(label, value):
    answers.append({"label": label, "value": f(value)})

# (a)(1) moving average schedule
for r in ma_rows:
    tag = {"BI": "beginning inventory", "P": "purchase", "S": "sale"}[r["typ"]]
    if r["typ"] == "S":
        A(f"a1 moving average: COGS on {r['date']} sale ({r['units']:,} units @ {money(r['avg'])})", r["cogs"])
        A(f"a1 moving average: inventory balance after {r['date']} sale ({r['u_bal']:,} units @ {money(r['avg'])})", r["d_bal"])
    else:
        A(f"a1 moving average: inventory balance after {r['date']} {tag} ({r['u_bal']:,} units)", r["d_bal"])
        A(f"a1 moving average: moving-average unit cost after {r['date']} {tag}", r["avg"])
A(f"a1 moving average: November ending inventory ({units_ending:,} units)", ma_ei)
A("a1 moving average: November COGS", ma_cogs)

# (a)(2)/(a)(3) layered schedules
for name, rows, layers, ei, tcogs in (("a2 FIFO", fifo_rows, fifo_layers, fifo_ei, fifo_cogs),
                                      ("a3 LIFO", lifo_rows, lifo_layers, lifo_ei, lifo_cogs)):
    for r in rows:
        tag = {"BI": "beginning inventory", "P": "purchase", "S": "sale"}[r["typ"]]
        if r["typ"] == "S":
            A(f"{name} perpetual: COGS on {r['date']} sale ({r['units']:,} units)", r["cogs"])
            A(f"{name} perpetual: inventory balance after {r['date']} sale (layers {layer_str(r['layers'])})", layer_total(r["layers"]))
        else:
            A(f"{name} perpetual: inventory balance after {r['date']} {tag} (layers {layer_str(r['layers'])})", layer_total(r["layers"]))
    for u, c in layers:
        A(f"{name} perpetual: ending layer {u:,} units @ ${c}", M(u * c))
    A(f"{name} perpetual: November ending inventory ({units_ending:,} units)", ei)
    A(f"{name} perpetual: November COGS", tcogs)

# (d) COGAS - EI = COGS
A(f"d: cost of goods available for sale ({units_available:,} units)", cogas)
for name, ei, tcogs in (("moving average", ma_ei, ma_cogs), ("FIFO", fifo_ei, fifo_cogs), ("LIFO", lifo_ei, lifo_cogs)):
    A(f"d: COGAS − EI under {name} (equals COGS: {'confirmed' if M(cogas - ei) == M(tcogs) else 'MISMATCH'})", M(cogas - ei))

# ---- journal entries -------------------------------------------------------
def L(acct, dr=Decimal("0"), cr=Decimal("0")):
    return {"account": acct, "debit": f(dr), "credit": f(cr)}

jes = []
for date, units, cost in purchases:
    amt = M(units * cost)
    jes.append({"part": "b", "date": date,
                "description": f"Purchase on account, gross method ({units:,} units @ ${cost})",
                "lines": [L("Inventory", dr=amt), L("Accounts Payable", cr=amt)]})

lifo_sale_cogs = {r["date"]: r["cogs"] for r in lifo_rows if r["typ"] == "S"}
for date, units, sp in sales:
    rev = M(units * sp)
    cg = lifo_sale_cogs[date]
    jes.append({"part": "c", "date": date,
                "description": f"Credit sale ({units:,} units @ ${sp}) — LIFO",
                "lines": [L("Accounts Receivable", dr=rev), L("Sales Revenue", cr=rev)]})
    jes.append({"part": "c", "date": date,
                "description": f"Cost of goods sold on {date} sale — LIFO perpetual",
                "lines": [L("Cost of Goods Sold", dr=cg), L("Inventory", cr=cg)]})

assert all(abs(sum(l["debit"] for l in j["lines"]) - sum(l["credit"] for l in j["lines"])) < 1e-9 for j in jes)

out = {
    "id": "agent_183#01",
    "rounding_convention": "decimal.Decimal throughout (no floats); every monetary amount — cost extensions, moving-average unit cost, COGS, and running inventory balances — rounded HALF_UP (ROUND_HALF_UP) to the cent as computed for the period; unit quantities exact.",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": ("Perpetual records: COGS is settled at each sale date. Moving average recomputes the unit cost only after a purchase "
              "($7.00 after Nov 4, $9.00 after Nov 15, $10.50 after Nov 28). FIFO perpetual gives the same result as FIFO periodic. "
              "LIFO perpetual charges the most recent layers on hand at each sale (Nov 10: 400 @ $9 then 200 @ $6; Nov 22: 450 @ $11). "
              "COGAS $18,750.00 on 2,050 units; 1,050 units sold, 1,000 units on hand at Nov 30. COGAS − EI = COGS holds for all three methods. "
              "Purchases are recorded gross with no discount terms given, so no discount accrual is required.")
}
print(json.dumps(out, indent=1))
