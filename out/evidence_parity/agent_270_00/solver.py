"""Solver for agent_270#00 — Larkspur Trading Partners, trading debt securities (FV-NI), LO 14-7.

Rounding convention: all money is decimal.Decimal, quantized to $0.01 using
ROUND_HALF_UP, applied once per computed period amount (per-period rounding,
not cumulative-then-round). No floats are used in any computation.

Every figure is derived from the stated facts; nothing is hard-coded except the
given facts themselves (face, rate, dates, fair value, sale proceeds).
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
def q(x): return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)

# ---------------- Given facts ----------------
FACE          = Decimal("60000")
COUPON_RATE   = Decimal("0.09")
PURCH_PRICE_PCT_OF_PAR = Decimal("1")          # "at par"
MONTHS_PER_COUPON      = Decimal("6")          # Jun 30 / Dec 31
MONTHS_DATED_TO_PURCH  = Decimal("4")          # Jul 1 Y1 -> Nov 1 Y1
MONTHS_PURCH_TO_YE1    = Decimal("2")          # Nov 1 Y1 -> Dec 31 Y1
FV_1231_Y1    = Decimal("57000")
SALE_PROCEEDS = Decimal("57600")               # Mar 15 Y2, clean price

# ---------------- (a) Nov 1, Year 1 initial recognition ----------------
cost = q(FACE * PURCH_PRICE_PCT_OF_PAR)                                   # 60,000.00
semi_coupon = q(FACE * COUPON_RATE * (MONTHS_PER_COUPON / Decimal("12"))) # 2,700.00
accrued_to_seller = q(FACE * COUPON_RATE * (MONTHS_DATED_TO_PURCH / Decimal("12")))  # 1,800.00
cash_paid_a = q(cost + accrued_to_seller)                                 # 61,800.00

# ---------------- (b) Dec 31, Year 1 cash interest receipt ----------------
cash_interest_received = semi_coupon                                      # 2,700.00
interest_revenue_y1 = q(FACE * COUPON_RATE * (MONTHS_PURCH_TO_YE1 / Decimal("12")))  # 900.00
receivable_cleared = accrued_to_seller                                    # 1,800.00
assert q(interest_revenue_y1 + receivable_cleared) == cash_interest_received

# ---------------- (c) Period-end FVA worksheet, Dec 31 Year 1 ----------------
# Trading debt bought at par with no discount/premium => amortized cost == cost.
amortized_cost_1231_y1 = cost
fva_required_y1 = q(FV_1231_Y1 - amortized_cost_1231_y1)   # -3,000.00 (credit balance)
fva_existing_before_y1 = Decimal("0.00")
fva_adjustment_y1 = q(fva_required_y1 - fva_existing_before_y1)           # -3,000.00
unrealized_loss_y1 = -fva_adjustment_y1                                   # 3,000.00 loss

# ---------------- (d) Year 1 statement effects ----------------
carrying_amount_1231_y1 = q(amortized_cost_1231_y1 + fva_required_y1)     # 57,000.00
net_income_effect_y1 = q(interest_revenue_y1 + fva_adjustment_y1)         # -2,100.00

# ---------------- (e) Mar 15, Year 2 disposal (no FVA touched) ----------------
amortized_cost_at_sale = cost                                             # 60,000.00
realized_gl = q(SALE_PROCEEDS - amortized_cost_at_sale)                   # -2,400.00
fva_balance_after_sale = fva_required_y1                                  # -3,000.00 still on books

# ---------------- (f) Dec 31, Year 2 FVA cleanup + reconciliation ----------------
amortized_cost_1231_y2 = Decimal("0.00")   # no TS held
fv_1231_y2 = Decimal("0.00")
fva_required_y2 = q(fv_1231_y2 - amortized_cost_1231_y2)                  # 0.00
fva_adjustment_y2 = q(fva_required_y2 - fva_balance_after_sale)           # +3,000.00 debit to FVA
unrealized_gain_y2 = fva_adjustment_y2                                    # 3,000.00 gain

net_y2_gl = q(realized_gl + unrealized_gain_y2)                           # +600.00
cumulative_gl = q(unrealized_loss_y1 * Decimal("-1") + net_y2_gl)         # -2,400.00
economic_gl = q(SALE_PROCEEDS - cost)                                     # -2,400.00
assert cumulative_gl == economic_gl

def s(d): return str(q(d))
def f(d): return float(q(d))

answers = [
 {"label":"a: Debt Investments (Trading) recorded at cost/par, Nov 1 Yr 1","value":f(cost)},
 {"label":"a: Accrued interest paid to seller (Jul 1 - Nov 1, 4 months)","value":f(accrued_to_seller)},
 {"label":"a: Total cash paid Nov 1, Year 1","value":f(cash_paid_a)},
 {"label":"b: Cash interest received Dec 31, Year 1 (semiannual coupon)","value":f(cash_interest_received)},
 {"label":"b: Interest Receivable cleared (accrued purchased)","value":f(receivable_cleared)},
 {"label":"b: Interest Revenue earned Nov 1 - Dec 31, Year 1 (2 months)","value":f(interest_revenue_y1)},
 {"label":"c: FVA worksheet - amortized cost (cost) at 12/31/Yr1","value":f(amortized_cost_1231_y1)},
 {"label":"c: FVA worksheet - fair value at 12/31/Yr1","value":f(FV_1231_Y1)},
 {"label":"c: FVA worksheet - required FVA balance at 12/31/Yr1 (negative = credit)","value":f(fva_required_y1)},
 {"label":"c: FVA worksheet - existing FVA balance before adjustment","value":f(fva_existing_before_y1)},
 {"label":"c: FVA worksheet - required adjustment at 12/31/Yr1 (negative = credit FVA)","value":f(fva_adjustment_y1)},
 {"label":"c: Unrealized Holding Loss - Income recognized 12/31/Yr1","value":f(unrealized_loss_y1)},
 {"label":"d: Year 1 balance-sheet carrying amount of trading securities (= fair value)","value":f(carrying_amount_1231_y1)},
 {"label":"d: Year 1 income statement - Interest Revenue","value":f(interest_revenue_y1)},
 {"label":"d: Year 1 income statement - Unrealized Holding Gain/(Loss) - Income","value":f(fva_adjustment_y1)},
 {"label":"d: Year 1 total pre-tax income effect","value":f(net_income_effect_y1)},
 {"label":"e: Sale proceeds Mar 15, Year 2","value":f(SALE_PROCEEDS)},
 {"label":"e: Amortized cost of investment removed at sale","value":f(amortized_cost_at_sale)},
 {"label":"e: Realized gain/(loss) on sale vs amortized cost","value":f(realized_gl)},
 {"label":"e: FVA balance immediately after sale (untouched, credit)","value":f(fva_balance_after_sale)},
 {"label":"f: FVA required balance at 12/31/Yr2 (no TS held)","value":f(fva_required_y2)},
 {"label":"f: FVA balance before 12/31/Yr2 adjustment (credit)","value":f(fva_balance_after_sale)},
 {"label":"f: 12/31/Yr2 adjustment to eliminate FVA (positive = debit FVA)","value":f(fva_adjustment_y2)},
 {"label":"f: Unrealized Holding Gain - Income recognized 12/31/Yr2","value":f(unrealized_gain_y2)},
 {"label":"f: Reconciliation - Year 1 unrealized holding gain/(loss)","value":f(fva_adjustment_y1)},
 {"label":"f: Reconciliation - Year 2 realized gain/(loss) on sale","value":f(realized_gl)},
 {"label":"f: Reconciliation - Year 2 unrealized holding gain/(loss) (FVA reversal)","value":f(unrealized_gain_y2)},
 {"label":"f: Reconciliation - Year 2 net gain/(loss) recognized","value":f(net_y2_gl)},
 {"label":"f: Reconciliation - cumulative holding-period gain/(loss) Yr1 + Yr2","value":f(cumulative_gl)},
 {"label":"f: Reconciliation - proof: proceeds less original cost","value":f(economic_gl)},
]

jes = [
 {"part":"a","lines":[
   {"account":"Debt Investments - Trading (Cascade Biologics 9% bonds)","debit":f(cost),"credit":0},
   {"account":"Interest Receivable","debit":f(accrued_to_seller),"credit":0},
   {"account":"Cash","debit":0,"credit":f(cash_paid_a)}]},
 {"part":"b","lines":[
   {"account":"Cash","debit":f(cash_interest_received),"credit":0},
   {"account":"Interest Receivable","debit":0,"credit":f(receivable_cleared)},
   {"account":"Interest Revenue","debit":0,"credit":f(interest_revenue_y1)}]},
 {"part":"c","lines":[
   {"account":"Unrealized Holding Gain or Loss - Income","debit":f(unrealized_loss_y1),"credit":0},
   {"account":"Fair Value Adjustment - Trading","debit":0,"credit":f(unrealized_loss_y1)}]},
 {"part":"e","lines":[
   {"account":"Cash","debit":f(SALE_PROCEEDS),"credit":0},
   {"account":"Loss on Sale of Investments","debit":f(-realized_gl),"credit":0},
   {"account":"Debt Investments - Trading (Cascade Biologics 9% bonds)","debit":0,"credit":f(amortized_cost_at_sale)}]},
 {"part":"f","lines":[
   {"account":"Fair Value Adjustment - Trading","debit":f(fva_adjustment_y2),"credit":0},
   {"account":"Unrealized Holding Gain or Loss - Income","debit":0,"credit":f(unrealized_gain_y2)}]},
]

for je in jes:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert q(dr) == q(cr), je["part"]

out = {
 "id":"agent_270#00",
 "rounding_convention":"decimal.Decimal throughout; quantize to $0.01 with ROUND_HALF_UP, applied once per period amount (per-period rounding, no float arithmetic). All figures here are exact to the cent.",
 "answers":answers,
 "journal_entries":jes,
 "insufficient_info":False,
 "notes":("Bonds bought at par with no fees, so cost = amortized cost = $60,000 throughout (no premium/discount amortization). "
          "Accrued interest bought Jul 1-Nov 1 (4 mo) = $1,800 is debited to Interest Receivable, not to the investment. "
          "Per LO 14-7 policy, FVA is adjusted only at each Dec 31: no FVA entry on the Mar 15 Yr 2 sale date, so the realized "
          "loss is measured against amortized cost ($57,600 - $60,000 = $2,400 loss) and the $3,000 credit FVA remains on the "
          "books until it is eliminated at 12/31/Yr2 as a $3,000 unrealized holding gain. Net Yr 2 effect = $600 gain; cumulative "
          "Yr1+Yr2 = $2,400 loss = proceeds less original cost. Per instruction, no Jan 1-Mar 15 Yr 2 accrued interest is recorded.")
}
print(json.dumps(out, indent=1))
