#!/usr/bin/env python3
"""Blind solver — Fox Valley Outfitters LLC (ACCOUNT-343, LO 15-1).

Fact pattern: perpetual inventory + gross method for purchases; company policy is
NOT to record sales taxes payable at the point of sale (the full tax-inclusive
amount is credited to Sales, and a month-end adjusting entry reclassifies the tax
out of Sales into Sales Taxes Payable).

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; no floats appear anywhere in this module.
Every monetary figure is quantized to cents (0.01) using ROUND_HALF_UP, applied
per computation (round-per-step, not round-at-end), which is this course's
convention.

Two rounding decisions are made deliberately:

1. Sales-tax extraction. For a tax-inclusive total T and rate r, pre-tax sales
   revenue is computed first as S = ROUND_HALF_UP(T / (1 + r), cents), and the
   sales tax is then taken as the residual, TAX = T - S. Deriving tax as the
   residual (rather than independently rounding S * r) guarantees the entry
   articulates exactly: the amount removed from Sales equals the amount credited
   to Sales Taxes Payable, and S + TAX == T to the cent with no plug.
   Both March totals here divide exactly (19,080/1.06 = 18,000.00 and
   12,720/1.06 = 12,000.00), so no rounding difference actually arises, but the
   rule is applied unconditionally.

2. Purchase discount. Under the gross method the 2% discount is computed on the
   INVOICE PRICE ONLY, not on freight-in: freight was paid in cash on the
   purchase date and never entered Accounts Payable, so it is not discountable.
   DISCOUNT = ROUND_HALF_UP(invoice * 0.02, cents); cash paid is the residual
   AP - DISCOUNT, again so the entry balances without a plug.

Freight-in is capitalized into Inventory (FOB shipping point; control passes at
shipment). Under a perpetual system the purchase discount taken is credited to
Inventory, not to a separate Purchase Discounts account (textbook Demo 15-1A).

No PV/annuity factors are involved in this item.

Run: python3 solver.py   -> prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENTS = Decimal("0.01")


def money(x) -> Decimal:
    """Quantize to cents using the course convention, ROUND_HALF_UP."""
    return Decimal(x).quantize(CENTS, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """Render a Decimal as a plain JSON number (int when it is a whole amount)."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------------------
# Given facts (transcribed from the stem only)
# ---------------------------------------------------------------------------
AP_BEGIN = Decimal("11600")          # Mar 1 Accounts Payable (February purchase, n/30)
STP_BEGIN = Decimal("0")             # Mar 1 Sales Taxes Payable

MAR2_INVOICE = Decimal("32000")      # merchandise on account, terms 2/10, n/30
MAR2_FREIGHT = Decimal("480")        # freight-in paid cash, FOB shipping point
DISCOUNT_RATE = Decimal("0.02")

MAR5_TOTAL_COLLECTED = Decimal("19080")   # tax-inclusive cash sales
MAR5_COGS = Decimal("10500")

MAR14_FEB_AP_PAYMENT = Decimal("11600")

MAR19_TOTAL_BILLED = Decimal("12720")     # tax-inclusive credit sales
MAR19_COGS = Decimal("7200")

TAX_RATE = Decimal("0.06")


# ---------------------------------------------------------------------------
# Derivations
# ---------------------------------------------------------------------------
def split_tax_inclusive(total: Decimal, rate: Decimal):
    """Return (pre-tax sales revenue, sales tax) from a tax-inclusive total."""
    sales = money(total / (Decimal(1) + rate))
    tax = money(total - sales)
    assert sales + tax == money(total), "tax split must reconstitute the total"
    return sales, tax


# (e) computational schedule: total / 1.06 for each sale date
mar5_sales, mar5_tax = split_tax_inclusive(MAR5_TOTAL_COLLECTED, TAX_RATE)
mar19_sales, mar19_tax = split_tax_inclusive(MAR19_TOTAL_BILLED, TAX_RATE)
march_tax_total = money(mar5_tax + mar19_tax)

# (a) Mar 2 purchase: inventory capitalizes invoice price; freight capitalized separately
mar2_inventory_from_invoice = money(MAR2_INVOICE)
mar2_inventory_from_freight = money(MAR2_FREIGHT)

# (c) Mar 11 settlement within the discount window, gross method
mar11_discount = money(MAR2_INVOICE * DISCOUNT_RATE)   # discount on invoice price only
mar11_ap_relieved = money(MAR2_INVOICE)                # freight never sat in AP
mar11_cash_paid = money(mar11_ap_relieved - mar11_discount)

# (g) Accounts Payable rollforward, Mar 1 - Mar 31
ap_additions = money(MAR2_INVOICE)
ap_reductions = money(mar11_ap_relieved + MAR14_FEB_AP_PAYMENT)
ap_end_mar31 = money(AP_BEGIN + ap_additions - ap_reductions)

# (g) Sales Taxes Payable rollforward, Mar 1 - Apr 22
stp_end_mar31 = money(STP_BEGIN + march_tax_total)     # nothing remitted during March
apr22_remittance = money(stp_end_mar31)                # March taxes remitted in full
stp_end_apr22 = money(stp_end_mar31 - apr22_remittance)


# ---------------------------------------------------------------------------
# Journal entries
# ---------------------------------------------------------------------------
def line(account: str, debit=Decimal(0), credit=Decimal(0)):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


def entry(part: str, date: str, memo: str, lines):
    total_dr = sum((money(l["debit"]) for l in lines), Decimal(0))
    total_cr = sum((money(l["credit"]) for l in lines), Decimal(0))
    assert total_dr == total_cr, f"{part} {date}: debits {total_dr} != credits {total_cr}"
    return {"part": part, "date": date, "memo": memo, "lines": lines}


journal_entries = [
    entry("a", "Mar 2", "Purchase of merchandise for resale on account (gross method)", [
        line("Inventory", debit=mar2_inventory_from_invoice),
        line("Accounts Payable", credit=mar2_inventory_from_invoice),
    ]),
    entry("a", "Mar 2", "Freight-in paid in cash, FOB shipping point (capitalized to Inventory)", [
        line("Inventory", debit=mar2_inventory_from_freight),
        line("Cash", credit=mar2_inventory_from_freight),
    ]),
    entry("b", "Mar 5", "Cash sales recorded under company policy (tax not broken out)", [
        line("Cash", debit=MAR5_TOTAL_COLLECTED),
        line("Sales", credit=MAR5_TOTAL_COLLECTED),
    ]),
    entry("b", "Mar 5", "Cost of goods sold on the March 5 cash sales (perpetual)", [
        line("Cost of Goods Sold", debit=MAR5_COGS),
        line("Inventory", credit=MAR5_COGS),
    ]),
    entry("c", "Mar 11", "Payment of Mar 2 invoice within the 2/10 discount period (gross method)", [
        line("Accounts Payable", debit=mar11_ap_relieved),
        line("Inventory", credit=mar11_discount),
        line("Cash", credit=mar11_cash_paid),
    ]),
    entry("d", "Mar 14", "Payment of February accounts payable, n/30, no discount available", [
        line("Accounts Payable", debit=MAR14_FEB_AP_PAYMENT),
        line("Cash", credit=MAR14_FEB_AP_PAYMENT),
    ]),
    entry("d", "Mar 19", "Credit sales recorded under company policy (tax not broken out)", [
        line("Accounts Receivable", debit=MAR19_TOTAL_BILLED),
        line("Sales", credit=MAR19_TOTAL_BILLED),
    ]),
    entry("d", "Mar 19", "Cost of goods sold on the March 19 credit sales (perpetual)", [
        line("Cost of Goods Sold", debit=MAR19_COGS),
        line("Inventory", credit=MAR19_COGS),
    ]),
    entry("e", "Mar 31", "Month-end adjusting entry reclassifying embedded sales taxes out of Sales", [
        line("Sales", debit=march_tax_total),
        line("Sales Taxes Payable", credit=march_tax_total),
    ]),
    entry("f", "Apr 22", "Remittance of March sales taxes to the state taxing authority", [
        line("Sales Taxes Payable", debit=apr22_remittance),
        line("Cash", credit=apr22_remittance),
    ]),
    entry("i", "Mar 5", "ALTERNATIVE policy: tax recorded at the point of sale (cash sales)", [
        line("Cash", debit=MAR5_TOTAL_COLLECTED),
        line("Sales", credit=mar5_sales),
        line("Sales Taxes Payable", credit=mar5_tax),
    ]),
    entry("i", "Mar 19", "ALTERNATIVE policy: tax recorded at the point of sale (credit sales)", [
        line("Accounts Receivable", debit=MAR19_TOTAL_BILLED),
        line("Sales", credit=mar19_sales),
        line("Sales Taxes Payable", credit=mar19_tax),
    ]),
    entry("i", "Mar 31", "ALTERNATIVE policy: no month-end adjusting entry required "
                         "(tax already isolated at each sale date; COGS entries are unchanged)", []),
]


# ---------------------------------------------------------------------------
# Reported answers - only figures the Required parts ask for
#   (e) the computational schedule; (g) the proven ending balances
# ---------------------------------------------------------------------------
answers = [
    {"label": "e: Mar 5 sales revenue ($19,080 / 1.06)", "value": num(mar5_sales)},
    {"label": "e: Mar 5 sales taxes payable ($19,080 - $18,000)", "value": num(mar5_tax)},
    {"label": "e: Mar 19 sales revenue ($12,720 / 1.06)", "value": num(mar19_sales)},
    {"label": "e: Mar 19 sales taxes payable ($12,720 - $12,000)", "value": num(mar19_tax)},
    {"label": "e: total March sales taxes reclassified (Mar 31 adjusting entry)",
     "value": num(march_tax_total)},
    {"label": "g: Accounts Payable ending balance, Mar 31, 2026", "value": num(ap_end_mar31)},
    {"label": "g: Sales Taxes Payable balance, Mar 31, 2026", "value": num(stp_end_mar31)},
    {"label": "g: Sales Taxes Payable ending balance after Apr 22, 2026 remittance",
     "value": num(stp_end_apr22)},
]

notes = (
    "h (classification, narrative): At Mar 31, 2026 Sales Taxes Payable of $1,800 is a CURRENT "
    "LIABILITY - the amount is collected from customers as agent for the state, is definite in "
    "amount, and is settled Apr 22, well within one year and within the operating cycle; it is not "
    "revenue and never reaches the income statement. Accounts Payable rolls to $0 at Mar 31 (both "
    "the February balance and the March 2 invoice were settled in March), so no AP is presented; "
    "any AP that had remained would likewise be current, being trade obligations due on n/30 terms "
    "arising from the normal operating cycle. After the Apr 22 remittance, Sales Taxes Payable is "
    "$0. | i: under point-of-sale recognition the Mar 31 adjusting entry is NOT required (shown as "
    "an entry with no lines), because the tax is already isolated at each sale date; total Sales "
    "($30,000), total Sales Taxes Payable ($1,800), and the COGS entries are identical under both "
    "policies - only the timing of the split differs. | Purchase discount is computed on the "
    "$32,000 invoice price only; the $480 cash freight-in never entered Accounts Payable and is "
    "not discountable."
)

output = {
    "id": "agent_356#00",
    "rounding_convention": (
        "decimal.Decimal throughout, no floats; ROUND_HALF_UP quantized to cents per computation. "
        "Sales tax extracted from tax-inclusive totals as S = ROUND_HALF_UP(total / 1.06) with tax "
        "taken as the residual total - S, so the reclassification entry articulates exactly. "
        "Purchase discount = ROUND_HALF_UP(invoice x 0.02) on the invoice price only (freight "
        "excluded), with cash paid as the residual. No PV factors involved."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

if __name__ == "__main__":
    # Proof checks - these must hold or the derivation, not the numbers, gets fixed.
    assert mar5_sales + mar5_tax == MAR5_TOTAL_COLLECTED
    assert mar19_sales + mar19_tax == MAR19_TOTAL_BILLED
    assert mar11_discount + mar11_cash_paid == mar11_ap_relieved
    assert ap_end_mar31 == money(AP_BEGIN + ap_additions - ap_reductions)
    assert stp_end_apr22 == Decimal("0.00")
    print(json.dumps(output, indent=2))
