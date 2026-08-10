"""Lakebound Merchants Inc. - perpetual moving average, FIFO, LIFO (LO 9-5).

Rounding convention: all money is decimal.Decimal, quantized to 2 dp with
ROUND_HALF_UP per period (each unit-cost recomputation and each dollar amount
is rounded half-up to the cent as it is computed; no floats anywhere).
Every figure is derived from the transaction table below; nothing hard-coded.
"""
import json
from decimal import Decimal as D, ROUND_HALF_UP, getcontext

getcontext().prec = 28
C = D("0.01")


def q(x):
    return x.quantize(C, rounding=ROUND_HALF_UP)


def f(x):
    return float(q(x))


# ---- transaction table (the only inputs) ----
TXNS = [
    ("Oct 1", "BI", D(500), D("8")),
    ("Oct 6", "P", D(300), D("10")),
    ("Oct 12", "S", D(400), D("18")),
    ("Oct 18", "P", D(500), D("11")),
    ("Oct 25", "S", D(450), D("19")),
    ("Oct 30", "P", D(100), D("12")),
]

purchases = [t for t in TXNS if t[1] == "P"]
sales = [t for t in TXNS if t[1] == "S"]

cogas_cost = q(sum((u * c for _, k, u, c in TXNS if k in ("BI", "P")), D(0)))
cogas_units = sum((u for _, k, u, _ in TXNS if k in ("BI", "P")), D(0))

# ---------------- moving average ----------------
ma_sched, ma_cogs = [], D(0)
units = D(0)
bal = D(0)
avg = D(0)
for date, kind, u, c in TXNS:
    if kind in ("BI", "P"):
        units += u
        bal = q(bal + q(u * c))
        avg = q(bal / units)
        ma_sched.append((date, kind, units, avg, bal))
    else:
        cost = q(u * avg)
        ma_cogs = q(ma_cogs + cost)
        units -= u
        bal = q(bal - cost)
        avg = q(bal / units) if units else D(0)
        ma_sched.append((date, kind, units, avg, bal))
ma_ei = bal

# ---------------- layered engines (FIFO / LIFO) ----------------
def layered(method):
    layers, cogs, sched = [], D(0), []
    for date, kind, u, c in TXNS:
        if kind in ("BI", "P"):
            layers.append([u, c])
        else:
            need = u
            cost = D(0)
            while need > 0:
                i = 0 if method == "FIFO" else len(layers) - 1
                take = min(need, layers[i][0])
                cost = q(cost + q(take * layers[i][1]))
                layers[i][0] -= take
                need -= take
                if layers[i][0] == 0:
                    layers.pop(i)
            cogs = q(cogs + cost)
        bal = q(sum((q(l[0] * l[1]) for l in layers), D(0)))
        sched.append((date, kind, sum((l[0] for l in layers), D(0)),
                      [(int(l[0]), str(l[1])) for l in layers], bal))
    return cogs, bal, sched


fifo_cogs, fifo_ei, fifo_sched = layered("FIFO")
lifo_cogs, lifo_ei, lifo_sched = layered("LIFO")

# per-sale LIFO COGS (needed for part c)
def lifo_sale_costs():
    layers, out = [], []
    for date, kind, u, c in TXNS:
        if kind in ("BI", "P"):
            layers.append([u, c])
        else:
            need, cost = u, D(0)
            while need > 0:
                i = len(layers) - 1
                take = min(need, layers[i][0])
                cost = q(cost + q(take * layers[i][1]))
                layers[i][0] -= take
                need -= take
                if layers[i][0] == 0:
                    layers.pop(i)
            out.append((date, u, cost))
    return out


lifo_sales = lifo_sale_costs()

answers = []
# (a) schedules
for date, kind, un, avgc, bal in ma_sched:
    lbl = "purchase" if kind in ("BI", "P") else "sale"
    if kind == "BI":
        lbl = "beginning inventory"
    answers.append({"label": "a1 MA: %s after %s - units %d @ avg unit cost $%s; inventory balance"
                    % (date, lbl, int(un), q(avgc)), "value": f(bal)})
for name, sched in (("a2 FIFO", fifo_sched), ("a3 LIFO", lifo_sched)):
    for date, kind, un, lay, bal in sched:
        lbl = "beginning inventory" if kind == "BI" else ("purchase" if kind == "P" else "sale")
        ltxt = " + ".join("%d @ $%s" % (n, c) for n, c in lay)
        answers.append({"label": "%s: %s after %s - units %d, layers [%s]; inventory balance"
                        % (name, date, lbl, int(un), ltxt), "value": f(bal)})

answers += [
    {"label": "a1 Moving average: October ending inventory", "value": f(ma_ei)},
    {"label": "a1 Moving average: October COGS", "value": f(ma_cogs)},
    {"label": "a2 FIFO perpetual: October ending inventory", "value": f(fifo_ei)},
    {"label": "a2 FIFO perpetual: October COGS", "value": f(fifo_cogs)},
    {"label": "a3 LIFO perpetual: October ending inventory", "value": f(lifo_ei)},
    {"label": "a3 LIFO perpetual: October COGS", "value": f(lifo_cogs)},
    {"label": "d: Cost of goods available for sale (all methods; %d units)" % int(cogas_units),
     "value": f(cogas_cost)},
    {"label": "d: Moving average check COGAS - EI = COGS", "value": f(cogas_cost - ma_ei)},
    {"label": "d: FIFO check COGAS - EI = COGS", "value": f(cogas_cost - fifo_ei)},
    {"label": "d: LIFO check COGAS - EI = COGS", "value": f(cogas_cost - lifo_ei)},
]

jes = []
for date, _, u, c in purchases:
    amt = q(u * c)
    jes.append({"part": "b", "date": date, "memo": "Purchase on account, gross method: %d units @ $%s"
                % (int(u), c),
                "lines": [{"account": "Inventory", "debit": f(amt), "credit": 0.0},
                          {"account": "Accounts Payable", "debit": 0.0, "credit": f(amt)}]})

for (date, kind, u, sp), (sdate, su, scost) in zip(sales, [(d_, u_, c_) for d_, u_, c_ in lifo_sales]):
    rev = q(u * sp)
    jes.append({"part": "c", "date": date, "memo": "Credit sale %d units @ $%s (LIFO)" % (int(u), sp),
                "lines": [{"account": "Accounts Receivable", "debit": f(rev), "credit": 0.0},
                          {"account": "Sales Revenue", "debit": 0.0, "credit": f(rev)}]})
    jes.append({"part": "c", "date": date, "memo": "COGS on %s sale under LIFO perpetual" % date,
                "lines": [{"account": "Cost of Goods Sold", "debit": f(scost), "credit": 0.0},
                          {"account": "Inventory", "debit": 0.0, "credit": f(scost)}]})

for je in jes:
    assert q(sum(D(str(l["debit"])) for l in je["lines"])) == \
           q(sum(D(str(l["credit"])) for l in je["lines"])), je
assert cogas_cost - ma_ei == ma_cogs
assert cogas_cost - fifo_ei == fifo_cogs
assert cogas_cost - lifo_ei == lifo_cogs

notes = (
    "COGAS = 500@$8 + 300@$10 + 500@$11 + 100@$12 = $%s (1,400 units); 850 units sold, 550 on hand. "
    "MA: avg $8.75 after Oct 6 purchase, $10.00 after Oct 18 purchase. "
    "FIFO EI = 450@$11 + 100@$12. LIFO perpetual EI = 400@$8 + 50@$11 + 100@$12. "
    "Part (c) COGS entries use LIFO amounts: Oct 12 $%s (300@$10 + 100@$8), "
    "Oct 25 $%s (450@$11). Reciprocal test in (d) holds for all three methods."
    % (q(cogas_cost), q(lifo_sales[0][2]), q(lifo_sales[1][2]))
)

print(json.dumps({
    "id": "agent_052#01",
    "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP to 2 dp (cents) applied per period on every computed unit cost and dollar amount; no floating point",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
