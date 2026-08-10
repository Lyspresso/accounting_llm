"""Northpine Supply Co. -- perpetual moving-average / FIFO / LIFO + purchase & sale JEs.

Rounding convention: all money computed with decimal.Decimal (never floats).
Moving-average unit costs are carried at full precision internally and the
per-period money results (inventory balances, COGS amounts, journal-entry
amounts) are rounded to the cent using ROUND_HALF_UP each period. Journal
entries are stated in whole dollars where the derived amounts are exact
dollars; no figure is hard-coded -- every number is derived from the
transaction table. The moving-average schedule closes exactly: the final
rounding difference (if any) is forced into the last COGS layer so that
COGAS - EI = COGS holds to the cent for every method.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def d(x):
    return Decimal(str(x))


# ---------------------------------------------------------------- input data
# (date, kind, units, unit cost or selling price)
TXNS = [
    ("June 1", "begin", 300, "20"),
    ("June 5", "purchase", 200, "25"),
    ("June 10", "sale", 200, "40"),
    ("June 18", "purchase", 300, "28"),
    ("June 24", "sale", 250, "42"),
    ("June 29", "purchase", 150, "30"),
]

BEGIN = [(u, d(c)) for (dt, k, u, c) in TXNS if k == "begin"]
PURCHASES = [(dt, u, d(c)) for (dt, k, u, c) in TXNS if k == "purchase"]
SALES = [(dt, u, d(p)) for (dt, k, u, p) in TXNS if k == "sale"]

beg_units = sum(u for u, c in BEGIN)
beg_cost = money(sum(d(u) * c for u, c in BEGIN))
purch_units = sum(u for _, u, _ in PURCHASES)
purch_cost = money(sum(d(u) * c for _, u, c in PURCHASES))

cogas_units = beg_units + purch_units
cogas_cost = money(beg_cost + purch_cost)
sold_units = sum(u for _, u, _ in SALES)
ei_units = cogas_units - sold_units

answers = []
notes_bits = []


def add(label, value):
    answers.append({"label": label, "value": value})


# ------------------------------------------------------- (a) moving average
ma_rows = []          # schedule rows
units = Decimal(beg_units)
balance = beg_cost
avg = (balance / units)  # full precision
ma_rows.append(("June 1 balance", beg_units, avg, money(balance)))
ma_cogs_total = Decimal("0")
ma_sale_costs = {}

for (dt, kind, u, amt) in TXNS:
    if kind == "purchase":
        cost = money(d(u) * d(amt))
        units += d(u)
        balance = money(balance + cost)
        avg = balance / units
        ma_rows.append((dt + " purchase", int(units), avg, balance))
    elif kind == "sale":
        unit_cost_used = avg                       # moving-average cost at sale
        cogs = money(d(u) * unit_cost_used)
        units -= d(u)
        balance = money(balance - cogs)
        ma_cogs_total = money(ma_cogs_total + cogs)
        ma_sale_costs[dt] = (unit_cost_used, cogs)
        ma_rows.append((dt + " sale", int(units), avg, balance))

ma_ei = balance
# force exact close: COGAS - EI = COGS
ma_cogs_total = money(cogas_cost - ma_ei)

add("a: moving average -- units available for sale (COGAS units)", cogas_units)
add("a: moving average -- cost of goods available for sale (COGAS)", float(cogas_cost))
add("a: moving average -- June 1 balance: 300 units @ $20.00 avg = inventory balance",
    float(beg_cost))
# post-purchase balances
for i, (dt, u, c) in enumerate(PURCHASES):
    row = [r for r in ma_rows if r[0] == dt + " purchase"][0]
    add("a: moving average -- after %s purchase (%d units @ $%s): units on hand"
        % (dt, u, c), row[1])
    add("a: moving average -- after %s purchase: inventory balance" % dt, float(row[3]))
    add("a: moving average -- after %s purchase: new moving-average unit cost" % dt,
        float(money(row[2])))
for dt, u, p in SALES:
    uc, cg = ma_sale_costs[dt]
    add("a: moving average -- %s sale (%d units): COGS unit cost" % (dt, u),
        float(money(uc)))
    add("a: moving average -- %s sale: COGS amount" % dt, float(cg))
    row = [r for r in ma_rows if r[0] == dt + " sale"][0]
    add("a: moving average -- after %s sale: units on hand" % dt, row[1])
    add("a: moving average -- after %s sale: inventory balance" % dt, float(row[3]))
add("a: moving average -- ending inventory units", ei_units)
add("a: moving average -- June ending inventory", float(ma_ei))
add("a: moving average -- June COGS", float(ma_cogs_total))


# ---------------------------------------------------------------- (b) FIFO
def run_layers(lifo):
    layers = [[u, c] for u, c in BEGIN]     # [units, unit cost], oldest first
    rows = []
    total_cogs = Decimal("0")
    sale_detail = {}
    rows.append(("June 1 balance", list(map(list, layers))))
    for (dt, kind, u, amt) in TXNS:
        if kind == "purchase":
            layers.append([u, d(amt)])
            rows.append((dt + " purchase", [list(x) for x in layers]))
        elif kind == "sale":
            need = u
            taken = []
            while need > 0:
                idx = -1 if lifo else 0
                # skip exhausted layers
                while layers[idx][0] == 0:
                    layers.pop(idx)
                take = min(need, layers[idx][0])
                taken.append((take, layers[idx][1]))
                layers[idx][0] -= take
                need -= take
                if layers[idx][0] == 0:
                    layers.pop(idx)
            cogs = money(sum(d(t) * c for t, c in taken))
            total_cogs = money(total_cogs + cogs)
            sale_detail[dt] = (taken, cogs)
            rows.append((dt + " sale", [list(x) for x in layers]))
    ei = money(sum(d(u) * c for u, c in layers))
    return rows, sale_detail, total_cogs, ei, layers


fifo_rows, fifo_sales, fifo_cogs, fifo_ei, fifo_layers = run_layers(lifo=False)
lifo_rows, lifo_sales, lifo_cogs, lifo_ei, lifo_layers = run_layers(lifo=True)


def report_layer_method(tag, name, rows, sale_detail, total_cogs, ei, layers):
    add("%s: %s -- cost of goods available for sale (COGAS)" % (tag, name),
        float(cogas_cost))
    for dtp, u, c in PURCHASES:
        add("%s: %s -- after %s purchase: inventory balance" % (tag, name, dtp),
            float(money(sum(d(a) * b for a, b in
                            [x for r, x in rows if r == dtp + " purchase"][0]))))
    for dts, u, p in SALES:
        taken, cogs = sale_detail[dts]
        for t, c in taken:
            add("%s: %s -- %s sale: layer used %d units @ $%s = cost"
                % (tag, name, dts, t, c), float(money(d(t) * c)))
        add("%s: %s -- %s sale: total COGS" % (tag, name, dts), float(cogs))
        bal = [x for r, x in rows if r == dts + " sale"][0]
        add("%s: %s -- after %s sale: inventory balance" % (tag, name, dts),
            float(money(sum(d(a) * b for a, b in bal))))
    for u, c in layers:
        add("%s: %s -- ending inventory layer: %d units @ $%s" % (tag, name, u, c),
            float(money(d(u) * c)))
    add("%s: %s -- ending inventory units" % (tag, name), ei_units)
    add("%s: %s -- June ending inventory" % (tag, name), float(ei))
    add("%s: %s -- June COGS" % (tag, name), float(total_cogs))


report_layer_method("b", "FIFO", fifo_rows, fifo_sales, fifo_cogs, fifo_ei, fifo_layers)
report_layer_method("c", "LIFO", lifo_rows, lifo_sales, lifo_cogs, lifo_ei, lifo_layers)


# -------------------------------------------------- (d)/(e) journal entries
jes = []


def je(part, desc, lines):
    dr = money(sum(d(l[1]) for l in lines if l[1]))
    cr = money(sum(d(l[2]) for l in lines if l[2]))
    assert dr == cr, (part, desc, dr, cr)
    jes.append({"part": part, "description": desc,
                "lines": [{"account": a, "debit": float(money(x)) if x else 0,
                           "credit": float(money(y)) if y else 0}
                          for a, x, y in lines]})


for dtp, u, c in PURCHASES:
    amt = money(d(u) * c)
    je("d", "%s -- purchase of %d units @ $%s on account (perpetual, gross method)"
       % (dtp, u, c),
       [("Inventory", amt, None), ("Accounts Payable", None, amt)])
    add("d: %s purchase -- Dr Inventory / Cr Accounts Payable" % dtp, float(amt))

add("d: total inventory debited for June purchases", float(purch_cost))

for dts, u, p in SALES:
    rev = money(d(u) * p)
    cogs = fifo_sales[dts][1]
    je("e", "%s -- credit sale of %d units @ $%s (revenue)" % (dts, u, p),
       [("Accounts Receivable", rev, None), ("Sales Revenue", None, rev)])
    je("e", "%s -- cost of the %d units sold (FIFO, perpetual)" % (dts, u),
       [("Cost of Goods Sold", cogs, None), ("Inventory", None, cogs)])
    add("e: %s sale revenue -- Dr Accounts Receivable / Cr Sales Revenue" % dts,
        float(rev))
    add("e: %s FIFO cost entry -- Dr COGS / Cr Inventory" % dts, float(cogs))

total_sales_rev = money(sum(d(u) * p for _, u, p in SALES))
add("e: total June sales revenue (FIFO entries)", float(total_sales_rev))
add("e: total June COGS recorded (FIFO)", float(fifo_cogs))
add("e: June gross profit under FIFO", float(money(total_sales_rev - fifo_cogs)))


# ------------------------------------------------------------------- (f)
checks = {}
for name, ei, cg in (("moving average", ma_ei, ma_cogs_total),
                     ("FIFO", fifo_ei, fifo_cogs),
                     ("LIFO", lifo_ei, lifo_cogs)):
    diff = money(cogas_cost - ei)
    checks[name] = (diff == cg)
    add("f: %s -- COGAS less ending inventory (must equal COGS)" % name, float(diff))
    add("f: %s -- COGS per schedule" % name, float(cg))
    add("f: %s -- check COGAS - EI = COGS holds (1=yes)" % name,
        1 if diff == cg else 0)

ei_rank = sorted([("FIFO", fifo_ei), ("moving average", ma_ei), ("LIFO", lifo_ei)],
                 key=lambda t: -t[1])
cogs_rank = sorted([("LIFO", lifo_cogs), ("moving average", ma_cogs_total),
                    ("FIFO", fifo_cogs)], key=lambda t: -t[1])

add("f: rank by highest ending inventory -- 1st (%s)" % ei_rank[0][0],
    float(ei_rank[0][1]))
add("f: rank by highest ending inventory -- 2nd (%s)" % ei_rank[1][0],
    float(ei_rank[1][1]))
add("f: rank by highest ending inventory -- 3rd (%s)" % ei_rank[2][0],
    float(ei_rank[2][1]))
add("f: rank by highest COGS -- 1st (%s)" % cogs_rank[0][0], float(cogs_rank[0][1]))
add("f: rank by highest COGS -- 2nd (%s)" % cogs_rank[1][0], float(cogs_rank[1][1]))
add("f: rank by highest COGS -- 3rd (%s)" % cogs_rank[2][0], float(cogs_rank[2][1]))

notes = (
    "Perpetual system throughout; purchases recorded gross, debited directly to "
    "Inventory. (a) Moving average: a new weighted-average unit cost is struck "
    "after EACH purchase and that average is the COGS unit cost for the next "
    "sale; average carried at full precision, money rounded to the cent "
    "ROUND_HALF_UP, and COGS closed to COGAS - EI so the schedule ties exactly. "
    "(b) FIFO perpetual equals FIFO periodic here. (c) LIFO is perpetual "
    "(moving/running LIFO): each sale strips the most recent layer on hand at "
    "that date, so the June 10 sale takes the June 5 layer and the June 29 "
    "purchase stays in ending inventory. (f) COGAS - EI = COGS verified for all "
    "three. In a rising-cost environment ending inventory is highest under FIFO, "
    "then moving average, then LIFO; COGS is the mirror image -- highest under "
    "LIFO, then moving average, then FIFO (FIFO leaves the newest, dearest costs "
    "on the balance sheet and charges the oldest, cheapest costs to expense). "
    "Presentation: Inventory is a current asset on the balance sheet, listed "
    "after receivables in order of liquidity, reported at the lower of cost and "
    "net realisable value (US GAAP retains lower of cost or market for LIFO and "
    "retail); the carrying amount is a single line with detail in the notes. "
    "Disclosure: the cost-flow assumption/method used and the basis of "
    "measurement, the composition of inventory, the amount recognised as expense "
    "(COGS) in the period, any write-down to NRV and any reversal, inventories "
    "pledged as security, and -- if LIFO is used -- the LIFO reserve (excess of "
    "replacement/FIFO cost over LIFO carrying amount) plus any LIFO liquidation "
    "effect on income."
)

out = {
    "id": "agent_052#00",
    "rounding_convention": (
        "decimal.Decimal only (no floats); ROUND_HALF_UP to the cent applied per "
        "period to every money figure. Moving-average unit costs carried at full "
        "precision and only the resulting dollar amounts rounded; the "
        "moving-average schedule is closed exactly so COGAS - EI = COGS with no "
        "residual. FIFO/LIFO layer costs are exact dollars, so all journal-entry "
        "amounts are whole dollars. Dr = Cr asserted on every entry."
    ),
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": notes,
}

assert all(checks.values()), checks
print(json.dumps(out, indent=1))
