#!/usr/bin/env python3
"""Blind solver -- item agent_322#00.

Northvale Outfitters LLC: interim inventory estimated by the GROSS PROFIT METHOD
under a PERIODIC system, plus a July 12 storm casualty and the related insurance
recovery.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal (never float). Every monetary figure is quantized to
two decimal places with ROUND_HALF_UP, applied *per period* (i.e. each quarter's
estimated COGS and estimated ending inventory are rounded before that figure is
carried forward as the next period's beginning inventory), never round-at-end.
Percentages are exact rationals here (25/125 = 20% exactly, cost ratio 80%
exactly), so no rounding is actually triggered by the fact pattern -- the
convention is nonetheless applied deliberately at every step so the derivation is
reproducible if the inputs change.

DERIVATION OUTLINE
------------------
(a) Markup is stated as 25% OF COST. Convert to a sales basis:
        gross profit % of sales = markup_on_cost / (1 + markup_on_cost)
                                = 0.25 / 1.25 = 20%
        cost % of sales         = 1 / (1 + markup_on_cost) = 80%
(b) Roll forward, per quarter:
        GAS  = beginning inventory + net purchases
        COGS = cost % of sales x net sales
        EI   = GAS - COGS         (becomes next period's beginning inventory)
(c) Periodic period-end adjusting entry, gross form: debit COGS and the ending
    Inventory, credit the beginning Inventory balance and close Purchases.
(d) Same roll-forward for July 1-12 using the Jun 30 estimate as beginning
    inventory; inventory loss = estimated inventory at storm date - salvage cost.
(e) July 12: bring the periodic accounts current, carve out salvage at cost, and
    expense the destroyed goods as a casualty loss (before any insurance).
(f) July 12: recognize the probable, estimable insurance recovery as a
    receivable, crediting it against the casualty loss recognized in (e).
(g) Aug 5: cash settlement of that receivable, dollar for dollar.
(h) Inventory carried on the balance sheet right after the write-off is the
    salvaged goods only; the insurance claim is a receivable, not inventory.

Run:  python3 solver.py    -> prints one JSON object to stdout.
"""

import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28
CENT = Decimal("0.01")


def m(x):
    """Quantize a monetary amount to cents, ROUND_HALF_UP (applied per period)."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d):
    """JSON-friendly plain number: int when the amount is whole dollars."""
    d = m(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------------------
# Facts taken from the stem (nothing else is assumed)
# ---------------------------------------------------------------------------
MARKUP_ON_COST = Decimal("0.25")          # "consistent markup of 25% of cost"

INV_JAN_1 = m("360000")                   # physical count

Q1_PURCH, Q1_SALES = m("420000"), m("500000")
Q2_PURCH, Q2_SALES = m("390000"), m("480000")

JUL_PURCH, JUL_SALES = m("48000"), m("90000")   # July 1-12
SALVAGE_AT_COST = m("40000")
INSURANCE_RECOVERY = m("300000")                # probable + estimable, paid Aug 5

# ---------------------------------------------------------------------------
# (a) Markup on cost -> gross profit % of sales, and cost % of sales
# ---------------------------------------------------------------------------
gp_rate_on_sales = (MARKUP_ON_COST / (Decimal("1") + MARKUP_ON_COST))
cost_rate_on_sales = (Decimal("1") / (Decimal("1") + MARKUP_ON_COST))

gp_pct_of_sales = (gp_rate_on_sales * Decimal("100")).quantize(
    CENT, rounding=ROUND_HALF_UP)
cost_pct_of_sales = (cost_rate_on_sales * Decimal("100")).quantize(
    CENT, rounding=ROUND_HALF_UP)

assert gp_rate_on_sales + cost_rate_on_sales == Decimal("1")


def gp_method_period(beginning_inv, net_purchases, net_sales):
    """One gross-profit-method roll-forward. Returns (GAS, est COGS, est EI)."""
    gas = m(beginning_inv + net_purchases)
    cogs = m(cost_rate_on_sales * net_sales)      # rounded per period
    ei = m(gas - cogs)                            # rounded per period
    return gas, cogs, ei


# ---------------------------------------------------------------------------
# (b) Subsequent measurement schedule -- Mar 31 and Jun 30
# ---------------------------------------------------------------------------
q1_gas, q1_cogs, q1_ei = gp_method_period(INV_JAN_1, Q1_PURCH, Q1_SALES)
q2_gas, q2_cogs, q2_ei = gp_method_period(q1_ei, Q2_PURCH, Q2_SALES)

# ---------------------------------------------------------------------------
# (d) July 1-12 roll-forward to the storm date, then the inventory loss
# ---------------------------------------------------------------------------
jul_gas, jul_cogs, jul_inv_at_storm = gp_method_period(
    q2_ei, JUL_PURCH, JUL_SALES)
inventory_loss = m(jul_inv_at_storm - SALVAGE_AT_COST)

# ---------------------------------------------------------------------------
# (h) Inventory on the balance sheet immediately after the July 12 write-off
# ---------------------------------------------------------------------------
inventory_after_writeoff = SALVAGE_AT_COST

# ---------------------------------------------------------------------------
# Journal entries
# ---------------------------------------------------------------------------
def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


def check_balanced(entry):
    d = sum(m(l["debit"]) for l in entry["lines"])
    c = sum(m(l["credit"]) for l in entry["lines"])
    if d != c:
        raise AssertionError(
            "Entry %s out of balance: debits %s vs credits %s"
            % (entry["part"], d, c))


# (c) Mar 31 period-end adjusting entry (periodic, gross form)
je_mar31 = {
    "part": "c",
    "date": "Year 1 March 31",
    "description": "Period-end adjusting entry: record estimated COGS for Q1, "
                   "close Purchases and beginning Inventory, establish "
                   "estimated ending Inventory (gross profit method).",
    "lines": [
        line("Cost of Goods Sold", debit=q1_cogs),
        line("Inventory (ending, Mar 31 - estimated)", debit=q1_ei),
        line("Purchases", credit=Q1_PURCH),
        line("Inventory (beginning, Jan 1)", credit=INV_JAN_1),
    ],
}

# (c) Jun 30 period-end adjusting entry
je_jun30 = {
    "part": "c",
    "date": "Year 1 June 30",
    "description": "Period-end adjusting entry: record estimated COGS for Q2, "
                   "close Purchases and the Mar 31 estimated Inventory, "
                   "establish estimated ending Inventory at Jun 30.",
    "lines": [
        line("Cost of Goods Sold", debit=q2_cogs),
        line("Inventory (ending, Jun 30 - estimated)", debit=q2_ei),
        line("Purchases", credit=Q2_PURCH),
        line("Inventory (beginning, Mar 31)", credit=q1_ei),
    ],
}

# (e) July 12 initial recognition: salvage reclass, write-off, casualty loss
je_storm = {
    "part": "e",
    "date": "Year 1 July 12",
    "description": "Storm loss (before insurance): record July 1-12 estimated "
                   "COGS, close July Purchases and the Jun 30 Inventory "
                   "balance, reclassify salvaged goods at cost, and write off "
                   "the destroyed inventory as a casualty loss.",
    "lines": [
        line("Cost of Goods Sold (July 1-12, estimated)", debit=jul_cogs),
        line("Inventory - Salvaged Goods", debit=SALVAGE_AT_COST),
        line("Loss from Storm (Casualty Loss)", debit=inventory_loss),
        line("Purchases", credit=JUL_PURCH),
        line("Inventory (beginning, Jun 30)", credit=q2_ei),
    ],
}

# (f) July 12 insurance receivable for the probable, estimable recovery
je_claim = {
    "part": "f",
    "date": "Year 1 July 12",
    "description": "Recognize the probable and reasonably estimable insurance "
                   "recovery, reducing the casualty loss recorded in (e).",
    "lines": [
        line("Insurance Claim Receivable", debit=INSURANCE_RECOVERY),
        line("Loss from Storm (Casualty Loss)", credit=INSURANCE_RECOVERY),
    ],
}

# (g) Aug 5 settlement in cash
je_settlement = {
    "part": "g",
    "date": "Year 1 August 5",
    "description": "Insurer pays the claim in full settlement; the receivable "
                   "is collected dollar for dollar, so no gain or loss.",
    "lines": [
        line("Cash", debit=INSURANCE_RECOVERY),
        line("Insurance Claim Receivable", credit=INSURANCE_RECOVERY),
    ],
}

journal_entries = [je_mar31, je_jun30, je_storm, je_claim, je_settlement]
for _e in journal_entries:
    check_balanced(_e)

# ---------------------------------------------------------------------------
# Reported answers -- only figures the Required parts ask for
# ---------------------------------------------------------------------------
answers = [
    {"label": "a: gross profit as a percentage of sales (%)",
     "value": num(gp_pct_of_sales)},
    {"label": "a: cost percentage of sales (%)",
     "value": num(cost_pct_of_sales)},

    {"label": "b: Q1 (Mar 31) goods available for sale",
     "value": num(q1_gas)},
    {"label": "b: Q1 (Mar 31) estimated cost of goods sold",
     "value": num(q1_cogs)},
    {"label": "b: estimated ending inventory, March 31",
     "value": num(q1_ei)},
    {"label": "b: Q2 (Jun 30) goods available for sale",
     "value": num(q2_gas)},
    {"label": "b: Q2 (Jun 30) estimated cost of goods sold",
     "value": num(q2_cogs)},
    {"label": "b: estimated ending inventory, June 30",
     "value": num(q2_ei)},

    {"label": "d: July 1-12 goods available for sale",
     "value": num(jul_gas)},
    {"label": "d: July 1-12 estimated cost of goods sold",
     "value": num(jul_cogs)},
    {"label": "d: estimated inventory on hand at July 12 storm date "
              "(before salvage)",
     "value": num(jul_inv_at_storm)},
    {"label": "d: inventory loss from the storm",
     "value": num(inventory_loss)},

    {"label": "h: inventory reported on the balance sheet immediately after "
              "the July 12 write-off",
     "value": num(inventory_after_writeoff)},
]

notes = (
    "(a) 25% markup on cost -> GP% of sales = 0.25/1.25 = 20%; cost ratio 80%. "
    "(c)/(e) shown in the gross periodic form (close beginning Inventory and "
    "Purchases, debit COGS and the new Inventory balance); the equivalent "
    "net form debits Inventory only for the change. "
    "(e) is stated before insurance, so the full $322,000 casualty loss is "
    "recognized there and (f) credits it back by the $300,000 probable "
    "recovery, leaving a $22,000 net loss; a presentation that credits an "
    "'Insurance Recovery' income account instead is equivalent in net income. "
    "(h) Inventory = $40,000 of salvaged goods at cost; the $300,000 claim is "
    "reported as a receivable, not inventory. USE of the gross profit method: "
    "it estimates inventory and COGS for interim statements without the cost "
    "of a physical count, and it estimates inventory destroyed by a casualty "
    "when records are lost. LIMITATION: it relies on a past gross profit rate "
    "that may not hold in the current period and on the mix of goods sold "
    "being unchanged, it yields only an estimate (GAAP does not accept it for "
    "the annual financial statements, which require a physical count), and it "
    "cannot detect shrinkage, theft, or spoilage because any such shortage is "
    "buried in the estimated ending inventory."
)

result = {
    "id": "agent_322#00",
    "rounding_convention": (
        "decimal.Decimal only; ROUND_HALF_UP to 2 dp applied per period "
        "(each quarter's estimated COGS and estimated ending inventory are "
        "rounded before being carried forward), not round-at-end. Gross profit "
        "rate derived exactly from the 25% markup on cost (0.25/1.25 = 20%); "
        "no PV factors involved."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(result, indent=2))
