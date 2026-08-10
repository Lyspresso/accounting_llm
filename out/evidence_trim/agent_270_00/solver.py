"""Solver for agent_270#00 -- Larkspur Trading Partners, trading debt securities (LO 14-7).

ROUNDING CONVENTION: all monetary amounts use decimal.Decimal exclusively (never floats),
quantized to cents (0.01) with ROUND_HALF_UP applied independently in each period
(i.e., each period's interest / fair-value figure is rounded on its own, no carry-forward
of unrounded residuals). Interest is computed on a 12-month (months/12) basis.

Everything is derived from the fact pattern constants; no answer figure is hard-coded.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x):
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)

def f(x):  # JSON-friendly number
    x = q(x)
    return int(x) if x == x.to_integral_value() else float(x)

# ---------------- Fact-pattern inputs ----------------
FACE          = Decimal("60000")
COUPON_RATE   = Decimal("0.09")
# bonds dated July 1 Y1; interest paid semiannually June 30 / Dec 31
DATED_MONTH   = 7          # July (Year 1)
PURCH_MONTH   = 11         # November 1, Year 1
PAY_MONTH     = 12         # December 31, Year 1 coupon date
PERIODS_PER_YR = Decimal("2")
PURCHASE_PRICE_PCT = Decimal("1.00")   # "at par"
FV_DEC31_Y1   = Decimal("57000")
SALE_PROCEEDS = Decimal("57600")
BROKERAGE     = Decimal("0")
FVA_OPENING   = Decimal("0")           # first year holding TS
TS_HELD_AT_DEC31_Y2 = False            # holds no other TS after the sale

def interest(months):
    return q(FACE * COUPON_RATE * Decimal(months) / Decimal(12))

# ---------------- (a) November 1, Year 1 initial recognition ----------------
cost = q(FACE * PURCHASE_PRICE_PCT) + q(BROKERAGE)          # at par, no fees
months_accrued_to_seller = PURCH_MONTH - DATED_MONTH        # Jul 1 -> Nov 1 = 4 months
accrued_int_paid = interest(months_accrued_to_seller)       # 60,000 x 9% x 4/12
cash_paid_a = q(cost + accrued_int_paid)

je_a = [
    {"account": "Debt Investments (Trading) - Cascade Biologics 9% bonds",
     "debit": f(cost), "credit": 0},
    {"account": "Interest Receivable (accrued interest purchased)",
     "debit": f(accrued_int_paid), "credit": 0},
    {"account": "Cash", "debit": 0, "credit": f(cash_paid_a)},
]

# ---------------- (b) December 31, Year 1 cash interest receipt ----------------
semiannual_coupon = q(FACE * COUPON_RATE / PERIODS_PER_YR)  # 6 months of interest
months_per_period = int(Decimal(12) / PERIODS_PER_YR)       # 6-month coupon period Jul 1 -> Dec 31
months_earned = months_per_period - months_accrued_to_seller  # Nov 1 -> Dec 31 = 2 months
interest_revenue_y1 = interest(months_earned)
receivable_cleared = q(semiannual_coupon - interest_revenue_y1)  # = accrued purchased

je_b = [
    {"account": "Cash", "debit": f(semiannual_coupon), "credit": 0},
    {"account": "Interest Receivable", "debit": 0, "credit": f(receivable_cleared)},
    {"account": "Interest Revenue", "debit": 0, "credit": f(interest_revenue_y1)},
]

# ---------------- (c) Period-end FVA worksheet + Dec 31 Y1 adjusting JE ----------------
# Trading debt bought at par & maturing later: no discount/premium, so amortized cost = cost.
amortized_cost_y1 = cost
fva_required_y1 = q(FV_DEC31_Y1 - amortized_cost_y1)        # negative => credit balance needed
fva_adjustment_y1 = q(fva_required_y1 - FVA_OPENING)
unrealized_loss_y1 = q(-fva_adjustment_y1)                  # positive number = loss

je_c = [
    {"account": "Unrealized Holding Gain or Loss - Income",
     "debit": f(unrealized_loss_y1), "credit": 0},
    {"account": "Fair Value Adjustment (Trading)",
     "debit": 0, "credit": f(unrealized_loss_y1)},
]

# ---------------- (d) Year 1 balance sheet / income statement effects ----------------
carrying_amount_y1 = q(amortized_cost_y1 + fva_required_y1)   # = fair value 57,000
net_income_effect_y1 = q(interest_revenue_y1 - unrealized_loss_y1)

# ---------------- (e) March 15, Year 2 disposal (no FVA touched at sale) ----------------
realized_gl = q(SALE_PROCEEDS - amortized_cost_y1)            # vs amortized cost per LO 14-7
realized_loss = q(-realized_gl) if realized_gl < 0 else Decimal("0")
realized_gain = realized_gl if realized_gl > 0 else Decimal("0")

je_e = [{"account": "Cash", "debit": f(SALE_PROCEEDS), "credit": 0}]
if realized_loss > 0:
    je_e.append({"account": "Loss on Sale of Investments (realized)",
                 "debit": f(realized_loss), "credit": 0})
je_e.append({"account": "Debt Investments (Trading) - Cascade Biologics 9% bonds",
             "debit": 0, "credit": f(amortized_cost_y1)})
if realized_gain > 0:
    je_e.append({"account": "Gain on Sale of Investments (realized)",
                 "debit": 0, "credit": f(realized_gain)})

# ---------------- (f) Dec 31, Year 2 FVA cleanup + holding-period reconciliation ----------
fva_balance_before_y2 = fva_required_y1                        # untouched at sale: (3,000) Cr
fva_required_y2 = Decimal("0") if not TS_HELD_AT_DEC31_Y2 else None
fva_adjustment_y2 = q(fva_required_y2 - fva_balance_before_y2) # positive => debit FVA
unrealized_gain_y2 = fva_adjustment_y2

je_f = [
    {"account": "Fair Value Adjustment (Trading)",
     "debit": f(unrealized_gain_y2), "credit": 0},
    {"account": "Unrealized Holding Gain or Loss - Income",
     "debit": 0, "credit": f(unrealized_gain_y2)},
]

net_income_effect_y2_invest = q(unrealized_gain_y2 - realized_loss + realized_gain)
total_holding_gl = q(SALE_PROCEEDS - amortized_cost_y1)
check_total = q(-unrealized_loss_y1 + realized_gl + unrealized_gain_y2)
assert check_total == total_holding_gl

# balance check on every entry
for name, je in (("a", je_a), ("b", je_b), ("c", je_c), ("e", je_e), ("f", je_f)):
    d = sum(Decimal(str(l["debit"])) for l in je)
    c = sum(Decimal(str(l["credit"])) for l in je)
    assert q(d) == q(c), (name, d, c)

answers = [
 {"label": "a: Debt Investments (Trading) debited (purchase at par, no fees)", "value": f(cost)},
 {"label": "a: Interest Receivable debited - accrued interest paid to seller (Jul 1-Nov 1, %d mo)" % months_accrued_to_seller, "value": f(accrued_int_paid)},
 {"label": "a: Cash credited (total paid Nov 1, Year 1)", "value": f(cash_paid_a)},
 {"label": "b: Cash received Dec 31, Year 1 (semiannual coupon)", "value": f(semiannual_coupon)},
 {"label": "b: Interest Receivable credited (accrued purchased, cleared)", "value": f(receivable_cleared)},
 {"label": "b: Interest Revenue credited (Nov 1-Dec 31, %d mo earned)" % months_earned, "value": f(interest_revenue_y1)},
 {"label": "c: FVA worksheet - amortized cost of TS portfolio at 12/31/Y1", "value": f(amortized_cost_y1)},
 {"label": "c: FVA worksheet - fair value at 12/31/Y1", "value": f(FV_DEC31_Y1)},
 {"label": "c: FVA worksheet - required FVA balance at 12/31/Y1 (credit)", "value": f(fva_required_y1)},
 {"label": "c: FVA worksheet - existing FVA balance before adjustment", "value": f(FVA_OPENING)},
 {"label": "c: FVA worksheet - adjustment needed at 12/31/Y1 (credit FVA)", "value": f(unrealized_loss_y1)},
 {"label": "c: 12/31/Y1 adjusting JE - Unrealized Holding Gain or Loss-Income debited", "value": f(unrealized_loss_y1)},
 {"label": "d: Year 1 balance-sheet carrying amount of TS (current asset, at fair value)", "value": f(carrying_amount_y1)},
 {"label": "d: Year 1 income statement - Interest Revenue", "value": f(interest_revenue_y1)},
 {"label": "d: Year 1 income statement - Unrealized Holding Loss (FV-NI)", "value": f(unrealized_loss_y1)},
 {"label": "d: Year 1 net effect on income (interest less unrealized loss)", "value": f(net_income_effect_y1)},
 {"label": "e: 3/15/Y2 Cash received on sale", "value": f(SALE_PROCEEDS)},
 {"label": "e: 3/15/Y2 Debt Investments (Trading) credited at amortized cost", "value": f(amortized_cost_y1)},
 {"label": "e: 3/15/Y2 Realized loss on sale (proceeds less amortized cost; FVA untouched)", "value": f(realized_loss)},
 {"label": "f: FVA balance carried into 12/31/Y2 before cleanup (credit)", "value": f(fva_balance_before_y2)},
 {"label": "f: Required FVA balance at 12/31/Y2 (no TS held)", "value": f(fva_required_y2)},
 {"label": "f: 12/31/Y2 adjusting JE - debit FVA / credit Unrealized Holding Gain-Income", "value": f(unrealized_gain_y2)},
 {"label": "f: Reconciliation - Year 1 unrealized holding loss recognized", "value": f(q(-unrealized_loss_y1))},
 {"label": "f: Reconciliation - Year 2 realized loss on sale", "value": f(realized_gl)},
 {"label": "f: Reconciliation - Year 2 unrealized holding gain (FVA reversal)", "value": f(unrealized_gain_y2)},
 {"label": "f: Reconciliation - Year 2 net investment gain/(loss) in income", "value": f(net_income_effect_y2_invest)},
 {"label": "f: Reconciliation - cumulative holding-period gain/(loss) (proceeds less original cost)", "value": f(total_holding_gl)},
]

out = {
 "id": "agent_270#00",
 "rounding_convention": "decimal.Decimal only (no floats); amounts quantized to cents with ROUND_HALF_UP applied independently per period; interest accrued on a months/12 basis",
 "answers": answers,
 "journal_entries": [
   {"part": "a", "lines": je_a},
   {"part": "b", "lines": je_b},
   {"part": "c", "lines": je_c},
   {"part": "e", "lines": je_e},
   {"part": "f", "lines": je_f},
 ],
 "insufficient_info": False,
 "notes": ("Bonds bought at par between interest dates: 4 months (Jul 1-Nov 1) accrued interest of "
           "$1,800 is paid to the seller and debited to Interest Receivable, not to the investment. "
           "Bought at par with no fees, so amortized cost stays $60,000 (nothing to amortize). "
           "Dec 31 Y1 coupon $2,700 clears the $1,800 receivable and yields $900 of interest revenue "
           "(2 months held). Per LO 14-7 policy FVA is adjusted ONLY at Dec 31: at 12/31/Y1 FVA needs a "
           "$3,000 credit (FV 57,000 vs cost 60,000), giving a 57,000 carrying amount. The 3/15/Y2 sale "
           "is measured against AMORTIZED COST 60,000 (not the 57,000 carrying amount), producing a "
           "$2,400 realized loss, and FVA is deliberately left alone. At 12/31/Y2 no TS are held, so the "
           "stranded $3,000 credit FVA is removed with a debit to FVA and a $3,000 credit to Unrealized "
           "Holding Gain or Loss-Income. Reconciliation: (3,000) Y1 unrealized + (2,400) Y2 realized + "
           "3,000 Y2 unrealized reversal = (2,400) total, equal to 57,600 proceeds less 60,000 cost. "
           "Sale price is a clean price, so no interest accrual is recorded on 3/15/Y2 per the facts.")
}
print(json.dumps(out, indent=1))
