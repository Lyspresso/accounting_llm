"""Aspen Forge Tools Inc. -- LIFO / LCM by individual item, allowance method.

Rounding convention: all money is decimal.Decimal quantized to whole cents
(0.01) using ROUND_HALF_UP, applied per period (each period's computations are
rounded independently before being carried forward). No fractional cents arise
in this problem. Every figure is derived; nothing is hard-coded except the
facts given in the question.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def n(x):
    x = q(x)
    return int(x) if x == x.to_integral_value() else float(x)

# ---- Given facts (Year 1 ending inventory, by item line) -------------------
items = [
    # name, LIFO cost, selling price, cost to complete & sell, normal profit, replacement cost
    ("Edger line",     "26000", "30000",  "3000",  "3000", "16000"),
    ("Clipper line",   "50000", "90000", "28000", "18000", "36000"),
    ("Blade Set line", "15500", "18000",  "1000",  "2000", "14200"),
]
cogs_pre_y1 = q("210000")
allow_before_y1 = q("0")
y2_cost = q("70000")
y2_market = q("66000")

answers = []
def A(label, value): answers.append({"label": label, "value": value})

tot_cost = q(0); tot_lcm = q(0); tot_wd = q(0)
for name, cost, sp, cts, npm, rc in items:
    cost, sp, cts, npm, rc = q(cost), q(sp), q(cts), q(npm), q(rc)
    ceiling = q(sp - cts)                 # NRV
    floor = q(ceiling - npm)              # NRV less normal profit margin
    market = min(max(rc, floor), ceiling) # designated market = RC bounded by floor/ceiling
    lcm = min(cost, market)
    wd = q(cost - lcm)
    A(f"a: {name} -- ceiling (NRV)", n(ceiling))
    A(f"a: {name} -- floor (NRV less normal profit)", n(floor))
    A(f"a: {name} -- designated market", n(market))
    A(f"a: {name} -- LCM carrying amount", n(lcm))
    A(f"a: {name} -- write-down", n(wd))
    tot_cost = q(tot_cost + cost); tot_lcm = q(tot_lcm + lcm); tot_wd = q(tot_wd + wd)

A("a: Total LIFO cost, Dec 31 Year 1", n(tot_cost))
A("a: Total LCM (item-by-item), Dec 31 Year 1", n(tot_lcm))
A("a: Total write-down = required allowance balance, Dec 31 Year 1", n(tot_wd))

req_allow_y1 = tot_wd
adj_y1 = q(req_allow_y1 - allow_before_y1)
A("b: Year 1 period-end adjustment to the allowance (credit increase)", n(adj_y1))

jes = []
jes.append({"part": "b", "lines": [
    {"account": "Cost of Goods Sold", "debit": n(adj_y1), "credit": 0},
    {"account": "Allowance to Reduce Inventory to Market", "debit": 0, "credit": n(adj_y1)},
]})
jes.append({"part": "c", "lines": [
    {"account": "Holding Loss on Inventory", "debit": n(adj_y1), "credit": 0},
    {"account": "Allowance to Reduce Inventory to Market", "debit": 0, "credit": n(adj_y1)},
]})

# ---- (d) presentation -----------------------------------------------------
A("d: Balance sheet (both (b) and (c)) -- Inventory at LIFO cost", n(tot_cost))
A("d: Balance sheet (both (b) and (c)) -- Less: Allowance to Reduce Inventory to Market", n(req_allow_y1))
A("d: Balance sheet (both (b) and (c)) -- Inventory at LCM (net)", n(tot_lcm))
cogs_b = q(cogs_pre_y1 + adj_y1)
A("d: Income statement under (b) -- Cost of Goods Sold", n(cogs_b))
A("d: Income statement under (b) -- separate holding loss reported", n(q(0)))
A("d: Income statement under (c) -- Cost of Goods Sold", n(cogs_pre_y1))
A("d: Income statement under (c) -- Holding Loss on Inventory (separate line, other expenses/losses)", n(adj_y1))
A("d: Pre-tax income effect of the write-down under (b)", n(q(-adj_y1)))
A("d: Pre-tax income effect of the write-down under (c)", n(q(-adj_y1)))

# ---- (e) Year 2 true-up ---------------------------------------------------
req_allow_y2 = q(y2_cost - y2_market)
allow_before_y2 = req_allow_y1  # prior credit balance carries until year-end true-up
adj_y2 = q(req_allow_y2 - allow_before_y2)   # negative => debit the allowance
A("e: Year 2 required allowance, Dec 31 Year 2", n(req_allow_y2))
A("e: Allowance balance before the Year 2 adjustment (Year 1 credit balance)", n(allow_before_y2))
A("e: Year 2 period-end adjustment (debit to allowance / reduction)", n(abs(adj_y2)))
A("e: Year 2 balance sheet -- Inventory at LIFO cost", n(y2_cost))
A("e: Year 2 balance sheet -- Inventory at LCM (net)", n(y2_market))
jes.append({"part": "e", "lines": [
    {"account": "Allowance to Reduce Inventory to Market", "debit": n(abs(adj_y2)), "credit": 0},
    {"account": "Cost of Goods Sold", "debit": 0, "credit": n(abs(adj_y2))},
]})

A("f: Why LCM rather than LCNRV",
  "Aspen Forge measures inventory using LIFO. Under ASC 330-10-35, the LCNRV "
  "rule applies only to inventory measured by FIFO or average cost; inventory "
  "measured by LIFO (or the retail inventory method) remains subject to the "
  "traditional lower-of-cost-or-market rule, where market is replacement cost "
  "bounded by a ceiling (NRV) and a floor (NRV less a normal profit margin).")

for je in jes:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert q(d) == q(c), je

print(json.dumps({
    "id": "agent_320#02",
    "rounding_convention": "decimal.Decimal, quantized to cents (0.01) with ROUND_HALF_UP, applied per period; all amounts here are whole dollars",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": "Designated market = replacement cost bounded by ceiling (NRV = selling price less cost to complete & sell) and floor (NRV less normal profit margin); RC fell below the floor on all three Year 1 item lines, so the floor is designated market for each. LCM applied item by item, so no offsetting of the Clipper line's cost/market cushion. Year 1 allowance required 8,500 credit; the Year 1 layer was fully sold in Year 2, so the Year 2 entry is a true-up of the existing credit balance to the newly required 4,000, i.e. a 4,500 debit to the allowance with a credit to COGS (not a separate reversal-plus-new-write-down)."
}, indent=1))
