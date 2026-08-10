"""Northvale Outfitters LLC - interim gross profit method, storm loss, insurance.

ROUNDING CONVENTION: all money uses decimal.Decimal, quantized to cents
(0.01) with ROUND_HALF_UP applied per period / per computed figure (never on
floats, never deferred to the end). Percentages are exact Decimal ratios
quantized to 0.01 percentage points with ROUND_HALF_UP.
Every figure is derived from the scenario inputs; nothing is hard-coded.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def m(x):
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def pct(x):
    return (Decimal(x) * 100).quantize(C, rounding=ROUND_HALF_UP)
def f(x):
    return float(x)

# ---- inputs ----
BI_JAN1 = m("360000")
MARKUP_ON_COST = Decimal("0.25")
Q1_PUR, Q1_SALES = m("420000"), m("500000")
Q2_PUR, Q2_SALES = m("390000"), m("480000")
JUL_PUR, JUL_SALES = m("48000"), m("90000")
SALVAGE = m("40000")
INS_RECOVERY = m("300000")

# ---- (a) markup on cost -> gross profit % of sales ----
gp_rate = MARKUP_ON_COST / (Decimal(1) + MARKUP_ON_COST)   # 0.25/1.25
cost_rate = Decimal(1) - gp_rate

def roll(bi, pur, sales):
    gas = m(bi + pur)
    cogs = m(sales * cost_rate)
    ei = m(gas - cogs)
    return gas, cogs, ei

# ---- (b) subsequent measurement schedule ----
q1_gas, q1_cogs, q1_ei = roll(BI_JAN1, Q1_PUR, Q1_SALES)
q2_gas, q2_cogs, q2_ei = roll(q1_ei, Q2_PUR, Q2_SALES)

# ---- (d) storm-date estimate ----
jul_gas, jul_cogs, jul_ei = roll(q2_ei, JUL_PUR, JUL_SALES)
loss = m(jul_ei - SALVAGE)

# ---- (f) net loss after expected recovery ----
net_loss = m(loss - INS_RECOVERY)

# ---- (h) balance sheet inventory after write-off ----
bs_inventory = SALVAGE

answers = [
 {"label": "a: Markup on cost", "value": f(pct(MARKUP_ON_COST))},
 {"label": "a: Gross profit as a percentage of sales (25%/125%)", "value": f(pct(gp_rate))},
 {"label": "a: Cost percentage of sales", "value": f(pct(cost_rate))},

 {"label": "b: Q1 beginning inventory, Jan 1 (physical count)", "value": f(BI_JAN1)},
 {"label": "b: Q1 net purchases", "value": f(Q1_PUR)},
 {"label": "b: Q1 goods available for sale (GAS)", "value": f(q1_gas)},
 {"label": "b: Q1 net sales", "value": f(Q1_SALES)},
 {"label": "b: Q1 estimated COGS (80% x net sales)", "value": f(q1_cogs)},
 {"label": "b: Estimated ending inventory, March 31", "value": f(q1_ei)},
 {"label": "b: Q2 beginning inventory (Mar 31 estimate)", "value": f(q1_ei)},
 {"label": "b: Q2 net purchases", "value": f(Q2_PUR)},
 {"label": "b: Q2 goods available for sale (GAS)", "value": f(q2_gas)},
 {"label": "b: Q2 net sales", "value": f(Q2_SALES)},
 {"label": "b: Q2 estimated COGS (80% x net sales)", "value": f(q2_cogs)},
 {"label": "b: Estimated ending inventory, June 30", "value": f(q2_ei)},

 {"label": "d: Beginning inventory, July 1 (Jun 30 estimate)", "value": f(q2_ei)},
 {"label": "d: Net purchases, July 1-12", "value": f(JUL_PUR)},
 {"label": "d: Goods available for sale to July 12", "value": f(jul_gas)},
 {"label": "d: Net sales, July 1-12", "value": f(JUL_SALES)},
 {"label": "d: Estimated COGS, July 1-12 (80% x net sales)", "value": f(jul_cogs)},
 {"label": "d: Estimated inventory on hand at July 12 storm date (before salvage)", "value": f(jul_ei)},
 {"label": "d: Less salvaged goods still salable, at cost", "value": f(SALVAGE)},
 {"label": "d: Estimated inventory loss from storm", "value": f(loss)},

 {"label": "f: Insurance receivable recognized (probable and estimable)", "value": f(INS_RECOVERY)},
 {"label": "f: Net casualty loss after expected recovery", "value": f(net_loss)},

 {"label": "g: Cash received August 5 in full settlement", "value": f(INS_RECOVERY)},

 {"label": "h: Inventory reported on the balance sheet immediately after the July 12 write-off (salvaged goods at cost)", "value": f(bs_inventory)},
 {"label": "h: Insurance receivable reported separately as a current receivable (not inventory)", "value": f(INS_RECOVERY)},
 {"label": "h: One USE of the gross profit method", "value": "It produces an inventory estimate without a physical count - used for interim (quarterly) reporting, to test the reasonableness of a count, and to measure inventory destroyed in a casualty such as this storm, where counting the goods is impossible."},
 {"label": "h: One LIMITATION of the gross profit method", "value": "It is only an estimate based on a past gross profit percentage; if the current markup, sales mix, theft or spoilage differ from history the estimate is wrong, so GAAP does not accept it as the sole basis for annual financial statements - a physical count is still required at December 31."},
]

def je(part, lines):
    d = sum(Decimal(str(l.get("debit", 0))) for l in lines)
    c = sum(Decimal(str(l.get("credit", 0))) for l in lines)
    assert d == c, (part, d, c)
    return {"part": part, "lines": lines}

def L(acct, dr=None, cr=None):
    return {"account": acct, "debit": f(dr) if dr is not None else 0,
            "credit": f(cr) if cr is not None else 0}

journal_entries = [
 # (c) March 31 period-end adjusting entry (periodic)
 je("c", [
    L("Inventory (March 31 estimated ending inventory)", dr=q1_ei),
    L("Cost of Goods Sold", dr=q1_cogs),
    L("Inventory (January 1 beginning balance removed)", cr=BI_JAN1),
    L("Purchases (Q1 net purchases closed)", cr=Q1_PUR),
 ]),
 # (c) June 30 period-end adjusting entry
 je("c", [
    L("Inventory (June 30 estimated ending inventory)", dr=q2_ei),
    L("Cost of Goods Sold", dr=q2_cogs),
    L("Inventory (March 31 beginning balance removed)", cr=q1_ei),
    L("Purchases (Q2 net purchases closed)", cr=Q2_PUR),
 ]),
 # (e) July 12 - step 1: bring inventory to the storm-date estimate
 je("e", [
    L("Inventory (July 12 estimated balance before storm)", dr=jul_ei),
    L("Cost of Goods Sold (July 1-12)", dr=jul_cogs),
    L("Inventory (June 30 balance removed)", cr=q2_ei),
    L("Purchases (July 1-12 net purchases closed)", cr=JUL_PUR),
 ]),
 # (e) July 12 - step 2: reclassify salvage, write off destroyed goods, record loss
 je("e", [
    L("Inventory - Salvaged Goods (salable, at cost)", dr=SALVAGE),
    L("Casualty Loss from Storm", dr=loss),
    L("Inventory (destroyed goods written off)", cr=jul_ei),
 ]),
 # (f) July 12 insurance receivable
 je("f", [
    L("Insurance Claim Receivable", dr=INS_RECOVERY),
    L("Recovery of Casualty Loss (loss reduction)", cr=INS_RECOVERY),
 ]),
 # (g) August 5 settlement
 je("g", [
    L("Cash", dr=INS_RECOVERY),
    L("Insurance Claim Receivable", cr=INS_RECOVERY),
 ]),
]

out = {
 "id": "agent_322#00",
 "rounding_convention": "decimal.Decimal throughout; every money figure quantized to cents (0.01) with ROUND_HALF_UP applied per period/per figure; percentages quantized to 0.01 percentage points with ROUND_HALF_UP. All amounts here are exact whole dollars. Debits equal credits in every entry (asserted).",
 "answers": answers,
 "journal_entries": journal_entries,
 "insufficient_info": False,
 "notes": "(a) 25% markup on cost = 25/125 = 20% gross profit on sales; cost ratio 80%. (b)-(c) Each quarter's estimated ending inventory is booked by a period-end adjusting entry and carried forward as the next period's beginning inventory. (e) Split into two entries: the first is the July 1-12 period-end adjusting entry that establishes the estimated storm-date inventory of 362,000 (removing the 386,000 June 30 balance and closing 48,000 of July purchases); the second reclassifies the 40,000 of salvaged goods and writes off the 322,000 destroyed. A single combined entry (Dr COGS 72,000, Dr Inventory-Salvaged 40,000, Dr Casualty Loss 322,000; Cr Inventory 386,000, Cr Purchases 48,000) is equivalent. (f) Because recovery is probable and reasonably estimable, the 300,000 receivable is recognized on July 12 as a reduction of the loss, leaving a net casualty loss of 22,000; no gain is recognized since the recovery does not exceed the loss. (h) Only the 40,000 of salvaged goods remains in Inventory; the 300,000 claim is a separate current receivable, not inventory."
}
print(json.dumps(out, indent=1))
