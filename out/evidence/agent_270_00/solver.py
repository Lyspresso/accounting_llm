#!/usr/bin/env python3
"""Blind solver for item agent_270#00.

Q1 -- Larkspur Trading Partners: trading debt securities (TS) measured at FV-NI
with Fair Value Adjustment (FVA) entries recorded ONLY at each December 31
period-end (Appendix 14A / LO 14-7).

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; no binary floats appear anywhere in this module.
Every monetary result is quantized to whole cents ("0.01") using ROUND_HALF_UP,
applied per period / per computed amount rather than once at the end.  Interest
accruals are computed on the 30/360-style "months elapsed / 12" basis the course
uses for bond coupons (face x stated rate x months/12), each accrual rounded on
the date it is recorded.  No present-value work is required here: the bonds are
purchased AT PAR, so amortized cost equals face for the whole holding period and
there is no discount/premium amortization and no PV table factor involved.

METHOD (LO 14-7, the period-end-only variant)
---------------------------------------------
1. Purchase between interest dates -> buyer reimburses the seller for interest
   accrued from the last coupon date (bonds dated July 1) to the purchase date
   (Nov 1) = 4 months.  That reimbursement is debited to Interest Receivable,
   NOT to the investment account, so amortized cost stays at par.
2. The Dec 31 coupon pays a full 6 months of cash; it derecognizes the 4 months
   of Interest Receivable and records only the 2 months actually earned
   (Nov 1 -> Dec 31) as Interest Revenue.
3. FVA is a valuation account.  Required FVA balance = fair value of TS held
   MINUS amortized cost of TS held.  The period-end entry books the CHANGE
   (required balance - existing balance) against Unrealized Gain or Loss--Income.
4. Under LO 14-7 the investment is NOT written to fair value at the sale date.
   Gain/loss on sale = cash proceeds - AMORTIZED COST, and the stale FVA balance
   is left on the books until the next December 31, where it is swept out
   (required balance is zero because no TS remain).
5. Holding-period reconciliation: Year 1 unrealized + Year 2 (realized +
   unrealized) must equal total proceeds - total cost.

Run:  python3 solver.py     -> prints one JSON object on stdout.
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def money(x):
    """Quantize to whole cents with ROUND_HALF_UP (applied per amount/period)."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d):
    """Render a Decimal for JSON: int when it is a whole dollar amount."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------------------
# Fact pattern (transcribed from the stem; nothing below is a hard-coded answer)
# ---------------------------------------------------------------------------
FACE = Decimal("60000")            # face amount of Cascade Biologics bonds
STATED_RATE = Decimal("0.09")      # 9% stated/coupon rate
PURCHASE_PRICE = FACE              # "purchases at par", no brokerage fees
MONTHS_PER_COUPON = Decimal("6")   # semiannual: June 30 and December 31
# Bonds dated July 1, Year 1; purchased November 1, Year 1.
MONTHS_DATED_TO_PURCHASE = Decimal("4")     # Jul 1 -> Nov 1
MONTHS_PURCHASE_TO_YEAREND = Decimal("2")   # Nov 1 -> Dec 31
FV_DEC31_Y1 = Decimal("57000")     # fair value at 12/31/Y1
SALE_PROCEEDS = Decimal("57600")   # March 15, Year 2, clean price
# After the sale Larkspur holds no other TS.
FV_TS_HELD_DEC31_Y2 = Decimal("0")
AMORTIZED_COST_TS_HELD_DEC31_Y2 = Decimal("0")


def accrue(months):
    """Coupon interest for `months` months on the face at the stated rate."""
    return money(FACE * STATED_RATE * (Decimal(months) / Decimal("12")))


# ---------------------------------------------------------------------------
# (a) November 1, Year 1 -- initial recognition
# ---------------------------------------------------------------------------
# Purchased at par, so amortized cost = par.  Interest accrued from the bond
# date (Jul 1) to the purchase date (Nov 1) is paid to the seller and parked in
# Interest Receivable; it is recovered in the full Dec 31 coupon.
investment_cost = money(PURCHASE_PRICE)
accrued_interest_paid = accrue(MONTHS_DATED_TO_PURCHASE)          # 4 months
cash_paid_at_purchase = money(investment_cost + accrued_interest_paid)

je_a = {
    "part": "a",
    "date": "November 1, Year 1",
    "description": "To record purchase of trading securities between interest dates",
    "lines": [
        {"account": "Investment in Trading Securities--Cascade Bonds",
         "debit": num(investment_cost), "credit": 0},
        {"account": "Interest Receivable",
         "debit": num(accrued_interest_paid), "credit": 0},
        {"account": "Cash",
         "debit": 0, "credit": num(cash_paid_at_purchase)},
    ],
}

# ---------------------------------------------------------------------------
# (b) December 31, Year 1 -- receipt of semiannual cash interest
# ---------------------------------------------------------------------------
cash_coupon_dec31_y1 = accrue(MONTHS_PER_COUPON)                  # 6 months
interest_revenue_y1 = accrue(MONTHS_PURCHASE_TO_YEAREND)          # 2 months earned
# Cross-check identity of the entry: coupon = receivable released + revenue.
assert cash_coupon_dec31_y1 == money(accrued_interest_paid + interest_revenue_y1)

je_b = {
    "part": "b",
    "date": "December 31, Year 1",
    "description": "To record receipt of semiannual cash interest",
    "lines": [
        {"account": "Cash", "debit": num(cash_coupon_dec31_y1), "credit": 0},
        {"account": "Interest Receivable",
         "debit": 0, "credit": num(accrued_interest_paid)},
        {"account": "Interest Revenue",
         "debit": 0, "credit": num(interest_revenue_y1)},
    ],
}

# ---------------------------------------------------------------------------
# (c) December 31, Year 1 -- period-end FVA worksheet and adjusting entry
# ---------------------------------------------------------------------------
amortized_cost_dec31_y1 = money(investment_cost)   # at par: no amortization
unrealized_gl_y1 = money(FV_DEC31_Y1 - amortized_cost_dec31_y1)   # (3,000)
fva_balance_before_y1 = Decimal("0.00")            # first year of ownership
required_fva_dec31_y1 = unrealized_gl_y1           # FV - amortized cost of TS held
fva_change_y1 = money(required_fva_dec31_y1 - fva_balance_before_y1)

if fva_change_y1 < 0:
    je_c_lines = [
        {"account": "Unrealized Gain or Loss--Income",
         "debit": num(-fva_change_y1), "credit": 0},
        {"account": "Fair Value Adjustment--Trading Securities",
         "debit": 0, "credit": num(-fva_change_y1)},
    ]
else:
    je_c_lines = [
        {"account": "Fair Value Adjustment--Trading Securities",
         "debit": num(fva_change_y1), "credit": 0},
        {"account": "Unrealized Gain or Loss--Income",
         "debit": 0, "credit": num(fva_change_y1)},
    ]

je_c = {
    "part": "c",
    "date": "December 31, Year 1",
    "description": "Period-end adjustment of trading securities to fair value (FV-NI)",
    "lines": je_c_lines,
}

fva_balance_after_y1 = money(fva_balance_before_y1 + fva_change_y1)   # (3,000) credit

# ---------------------------------------------------------------------------
# (d) Year 1 balance sheet carrying amount and income statement effects
# ---------------------------------------------------------------------------
carrying_amount_dec31_y1 = money(amortized_cost_dec31_y1 + fva_balance_after_y1)
assert carrying_amount_dec31_y1 == money(FV_DEC31_Y1)   # carrying amount = FV
y1_income_effect = money(interest_revenue_y1 + unrealized_gl_y1)

# ---------------------------------------------------------------------------
# (e) March 15, Year 2 -- disposal (no FVA adjustment at sale under LO 14-7)
# ---------------------------------------------------------------------------
amortized_cost_at_sale = money(investment_cost)     # still par; FVA untouched
realized_gl_on_sale = money(SALE_PROCEEDS - amortized_cost_at_sale)   # (2,400)

je_e_lines = [{"account": "Cash", "debit": num(SALE_PROCEEDS), "credit": 0}]
if realized_gl_on_sale < 0:
    je_e_lines.append({"account": "Loss on Sale of Investment",
                       "debit": num(-realized_gl_on_sale), "credit": 0})
    je_e_lines.append({"account": "Investment in Trading Securities--Cascade Bonds",
                       "debit": 0, "credit": num(amortized_cost_at_sale)})
else:
    je_e_lines.append({"account": "Investment in Trading Securities--Cascade Bonds",
                       "debit": 0, "credit": num(amortized_cost_at_sale)})
    je_e_lines.append({"account": "Gain on Sale of Investment",
                       "debit": 0, "credit": num(realized_gl_on_sale)})

je_e = {
    "part": "e",
    "date": "March 15, Year 2",
    "description": ("To record sale of trading securities; gain/loss = cash received "
                    "less amortized cost (Fair Value Adjustment not adjusted at sale)"),
    "lines": je_e_lines,
}

# ---------------------------------------------------------------------------
# (f) December 31, Year 2 -- sweep out the leftover FVA balance
# ---------------------------------------------------------------------------
required_fva_dec31_y2 = money(FV_TS_HELD_DEC31_Y2 - AMORTIZED_COST_TS_HELD_DEC31_Y2)
fva_balance_before_y2 = fva_balance_after_y1
fva_change_y2 = money(required_fva_dec31_y2 - fva_balance_before_y2)   # +3,000

if fva_change_y2 > 0:
    je_f_lines = [
        {"account": "Fair Value Adjustment--Trading Securities",
         "debit": num(fva_change_y2), "credit": 0},
        {"account": "Unrealized Gain or Loss--Income",
         "debit": 0, "credit": num(fva_change_y2)},
    ]
else:
    je_f_lines = [
        {"account": "Unrealized Gain or Loss--Income",
         "debit": num(-fva_change_y2), "credit": 0},
        {"account": "Fair Value Adjustment--Trading Securities",
         "debit": 0, "credit": num(-fva_change_y2)},
    ]

je_f = {
    "part": "f",
    "date": "December 31, Year 2",
    "description": "To eliminate the Fair Value Adjustment balance (no trading securities held)",
    "lines": je_f_lines,
}

# Holding-period gain/loss reconciliation
y1_holding_gl = unrealized_gl_y1                                   # (3,000)
y2_unrealized_gl = fva_change_y2                                   #  3,000
y2_holding_gl = money(realized_gl_on_sale + y2_unrealized_gl)      #    600
total_holding_gl = money(y1_holding_gl + y2_holding_gl)            # (2,400)
# Economic proof: total recognized gain/loss = proceeds - original cost.
assert total_holding_gl == money(SALE_PROCEEDS - investment_cost)

# ---------------------------------------------------------------------------
# Assemble output
# ---------------------------------------------------------------------------
journal_entries = [je_a, je_b, je_c, je_e, je_f]
for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert money(dr) == money(cr), "unbalanced entry in part %s" % je["part"]

answers = [
    # c -- period-end FVA worksheet, December 31, Year 1
    {"label": "c: TS amortized cost, December 31 Year 1",
     "value": num(amortized_cost_dec31_y1)},
    {"label": "c: TS fair value, December 31 Year 1",
     "value": num(FV_DEC31_Y1)},
    {"label": "c: unrealized holding gain (loss), Year 1",
     "value": num(unrealized_gl_y1)},
    {"label": "c: existing FVA account balance before adjustment",
     "value": num(fva_balance_before_y1)},
    {"label": "c: increase (decrease) to FVA account needed, December 31 Year 1",
     "value": num(fva_change_y1)},
    # d -- Year 1 financial statement effects
    {"label": "d: Year 1 balance-sheet carrying amount of trading securities",
     "value": num(carrying_amount_dec31_y1)},
    {"label": "d: Year 1 interest revenue",
     "value": num(interest_revenue_y1)},
    {"label": "d: Year 1 unrealized holding gain (loss) on trading securities",
     "value": num(unrealized_gl_y1)},
    {"label": "d: Year 1 net pretax income effect of the investment",
     "value": num(y1_income_effect)},
    # f -- December 31, Year 2 worksheet and holding-period reconciliation
    {"label": "f: required FVA ending balance, December 31 Year 2",
     "value": num(required_fva_dec31_y2)},
    {"label": "f: existing FVA account balance, December 31 Year 2",
     "value": num(fva_balance_before_y2)},
    {"label": "f: increase (decrease) to FVA account needed, December 31 Year 2",
     "value": num(fva_change_y2)},
    {"label": "f: reconciliation - Year 1 income statement gain (loss)",
     "value": num(y1_holding_gl)},
    {"label": "f: reconciliation - Year 2 realized gain (loss) on sale",
     "value": num(realized_gl_on_sale)},
    {"label": "f: reconciliation - Year 2 unrealized gain (loss)",
     "value": num(y2_unrealized_gl)},
    {"label": "f: reconciliation - Year 2 income statement gain (loss)",
     "value": num(y2_holding_gl)},
    {"label": "f: reconciliation - total gain (loss) recognized over holding period",
     "value": num(total_holding_gl)},
]

result = {
    "id": "agent_270#00",
    "rounding_convention": (
        "decimal.Decimal only, no floats; ROUND_HALF_UP to whole cents applied per "
        "period/per computed amount. Interest accrued on a months/12 basis "
        "(face x 9% x months/12). Bonds bought at par, so amortized cost = face "
        "throughout; no discount/premium amortization and no PV table factors needed."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "LO 14-7 (Appendix 14A) period-end-only variant. Accrued interest paid to the "
        "seller on 11/1/Y1 (4 months, Jul 1 bond date to Nov 1) is debited to Interest "
        "Receivable, not to the investment, so amortized cost stays at par $60,000. The "
        "12/31/Y1 coupon of $2,700 (6 months) clears that $1,800 receivable and records "
        "only the $900 earned (2 months). No FVA entry is made on the 3/15/Y2 sale date: "
        "the loss is proceeds $57,600 less amortized cost $60,000. The stale $3,000 credit "
        "FVA balance is swept out on 12/31/Y2 because no TS remain. Year 2 has no interest "
        "revenue (next coupon was 6/30/Y2 and the stem directs that March accrued interest "
        "be ignored)."
    ),
}

print(json.dumps(result, indent=2))
