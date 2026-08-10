#!/usr/bin/env python3
"""Blind solver — agent_060#00: Meridian Hardware Co., fire loss (LO 10-4).

Fact pattern (periodic system, fire on September 14, Year 1):
    Inventory, September 1 .................. $540,000
    Net purchases, September 1-14 ............ 295,000
    Net sales, September 1-14 ................ 720,000
    Undamaged merchandise moved out, at cost .. 52,000
    Markup ................................... 25% of cost
    Insurance recovery recognized 9/14 (probable and
      reasonably estimable) and settled in cash 10/5 . 195,000

METHOD (textbook LO 10-4, gross profit method, two steps):
  Step 1 — convert markup on cost to gross profit as a percentage of sales:
      GP% of sales = GP% of cost / (1 + GP% of cost)
  Step 2 — estimate inventory at the fire date:
      Beginning inventory
    + Net purchases
    = Cost of goods available for sale
    - Estimated COGS  [ = Net sales x (1 - GP% of sales) ]
    = Estimated inventory on hand at the fire date (before salvage)
  Inventory loss = estimated inventory at fire date - salvageable inventory
                   carried out at cost.

ROUNDING CONVENTION
  All money is decimal.Decimal — never float. Every monetary result is
  quantized to cents (0.01) with ROUND_HALF_UP, applied per computed
  amount as it is produced (round-per-step, not round-only-at-the-end),
  which is this course's convention. The gross-profit rate is carried as
  an exact Decimal ratio (25/125 = 0.2 exactly) and is quantized to four
  decimal places with ROUND_HALF_UP only for reporting as a percentage;
  the unrounded ratio is what multiplies net sales, so no rate rounding
  error can propagate into cost of goods sold. On this fact pattern every
  amount lands on a whole dollar, so the rounding rule is not binding —
  it is stated and applied so the run is reproducible either way.

JOURNAL ENTRY CONVENTIONS
  (d) The salvaged goods are reclassified out of Inventory at their $52,000
      cost, the destroyed portion is written off, and the residual is the
      casualty loss — recorded gross, before any insurance.
  (e) Because recovery is probable and reasonably estimable, the expected
      recovery is set up as a receivable with a credit that reduces the
      casualty loss (a loss recovery is offset against the loss, not
      reported as revenue).
  (f) Cash settlement simply collects the receivable already recorded; no
      gain or loss remains because the settlement equals the receivable.

Run:  python3 solver.py   -> prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENTS = Decimal("0.01")
RATE_PLACES = Decimal("0.0001")


def money(x: Decimal) -> Decimal:
    """Quantize to cents, ROUND_HALF_UP (applied per computed amount)."""
    return Decimal(x).quantize(CENTS, rounding=ROUND_HALF_UP)


def rate(x: Decimal) -> Decimal:
    """Quantize a ratio to 4 dp, ROUND_HALF_UP (reporting only)."""
    return Decimal(x).quantize(RATE_PLACES, rounding=ROUND_HALF_UP)


def out(x: Decimal):
    """Emit a Decimal as int when whole, else as float-free string-safe number."""
    x = money(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------- given facts
BEGINNING_INVENTORY = Decimal("540000")      # Inventory, September 1
NET_PURCHASES = Decimal("295000")            # September 1-14
NET_SALES = Decimal("720000")                # September 1-14
SALVAGE_AT_COST = Decimal("52000")           # undamaged goods, counted at cost
MARKUP_ON_COST = Decimal("25") / Decimal("100")   # 25% of cost
INSURANCE_RECOVERY = Decimal("195000")       # expected 9/14, paid in cash 10/5

# ------------------------------------------- (a) markup on cost -> GP% of sales
# GP% of sales = GP% of cost / (1 + GP% of cost) = 0.25 / 1.25
gp_pct_of_sales = MARKUP_ON_COST / (Decimal("1") + MARKUP_ON_COST)
gp_pct_of_sales_reported = rate(gp_pct_of_sales) * Decimal("100")   # in percent

# ------------------------------------------------- (b) gross profit schedule
cost_of_goods_available = money(BEGINNING_INVENTORY + NET_PURCHASES)
estimated_cogs = money(NET_SALES * (Decimal("1") - gp_pct_of_sales))
estimated_inventory_at_fire = money(cost_of_goods_available - estimated_cogs)

# ------------------------------------------------------------ (c) fire loss
inventory_loss = money(estimated_inventory_at_fire - SALVAGE_AT_COST)

# ------------------------------- (d)-(f) journal entries; (g) presentation
# (d) 9/14 gross casualty entry, before insurance
je_d = {
    "part": "d",
    "date": "September 14, Year 1",
    "description": ("Reclassify salvaged inventory at cost, write off inventory "
                    "destroyed by fire, and recognize the casualty loss before "
                    "insurance recovery."),
    "lines": [
        {"account": "Inventory - Salvaged Merchandise",
         "debit": out(SALVAGE_AT_COST), "credit": 0},
        {"account": "Loss from Fire (Casualty Loss)",
         "debit": out(inventory_loss), "credit": 0},
        {"account": "Inventory",
         "debit": 0, "credit": out(estimated_inventory_at_fire)},
    ],
}

# (e) 9/14 recognition of the probable, estimable insurance recovery
je_e = {
    "part": "e",
    "date": "September 14, Year 1",
    "description": ("Recognize insurance receivable for the expected recovery; "
                    "the recovery reduces the casualty loss."),
    "lines": [
        {"account": "Insurance Claim Receivable",
         "debit": out(INSURANCE_RECOVERY), "credit": 0},
        {"account": "Loss from Fire (Casualty Loss)",
         "debit": 0, "credit": out(INSURANCE_RECOVERY)},
    ],
}

# (f) 10/5 cash settlement of the claim already receivable
je_f = {
    "part": "f",
    "date": "October 5, Year 1",
    "description": "Collect final cash settlement of the insurance claim.",
    "lines": [
        {"account": "Cash", "debit": out(INSURANCE_RECOVERY), "credit": 0},
        {"account": "Insurance Claim Receivable",
         "debit": 0, "credit": out(INSURANCE_RECOVERY)},
    ],
}

journal_entries = [je_d, je_e, je_f]

# Internal integrity check: debits must equal credits in every entry.
for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert money(dr) == money(cr), f"entry {je['part']} does not balance"

# (g) Inventory carried on the balance sheet right after the 9/14 entries is
#     only the salvaged goods, at cost. The $195,000 insurance claim is a
#     receivable, presented separately from inventory.
inventory_on_balance_sheet = money(SALVAGE_AT_COST)

# --------------------------------------------------------------- (h) narrative
use_note = ("Use: the gross profit method estimates the cost of inventory "
            "destroyed by a casualty such as a fire, which is needed both for "
            "the accounting records and as the basis for the insurance claim "
            "(it also tests the reasonableness of a physical count and supports "
            "interim reporting when no perpetual records exist).")
limitation_note = ("Limitation: it relies on a past gross profit rate that may "
                   "not hold in the current period, and markup rates differ "
                   "across inventory lines, so a change in rate or in sales mix "
                   "makes the estimate unreliable.")

result = {
    "id": "agent_060#00",
    "rounding_convention": ("decimal.Decimal only; monetary amounts quantized to "
                           "cents with ROUND_HALF_UP applied per computed amount "
                           "(round-per-step); gross profit rate held exact "
                           "(25/125) and rounded HALF_UP to 4 dp for reporting "
                           "only. All amounts here are whole dollars."),
    "answers": [
        {"label": "a: gross profit as a percentage of sales (percent)",
         "value": out(gp_pct_of_sales_reported)},
        {"label": "b: cost of goods available for sale (Sept 1-14)",
         "value": out(cost_of_goods_available)},
        {"label": "b: estimated cost of goods sold (Sept 1-14)",
         "value": out(estimated_cogs)},
        {"label": "b: estimated inventory on hand at fire date, before salvage",
         "value": out(estimated_inventory_at_fire)},
        {"label": "c: inventory loss from the fire",
         "value": out(inventory_loss)},
        {"label": "g: inventory reported on the balance sheet immediately after "
                  "the September 14 entries (salvaged merchandise at cost)",
         "value": out(inventory_on_balance_sheet)},
    ],
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "(b) Schedule: Beginning inventory $540,000 + net purchases $295,000 = "
        "cost of goods available for sale $835,000; less estimated cost of goods "
        "sold $720,000 x (1 - 0.20) = $576,000; estimated inventory at the fire "
        "date $259,000. (c) $259,000 - $52,000 salvaged = $207,000 loss. "
        "(g) Inventory on the balance sheet is only the $52,000 of salvaged "
        "merchandise, at cost; the $195,000 insurance claim is presented "
        "separately as a current receivable, not as inventory, and the net "
        "casualty loss carried to the income statement is $12,000. " +
        use_note + " " + limitation_note
    ),
}

print(json.dumps(result, indent=2))
