#!/usr/bin/env python3
"""Solver for item agent_136#01 -- Equity securities measured at FV-NI
(unrealized loss in Year 1, partial recovery at sale in Year 2).

FACT PATTERN (from stem.md)
--------------------------
Copperline Holdings Corp. (calendar year end) buys, on March 1 Year 1, 6,000 of
Brookfield Media Co.'s 80,000 outstanding common shares at $15.50/share and pays
$1,200 of commissions.  Ownership = 7.5%, insignificant influence, fair value
readily determinable  =>  measure at FV-NI.  Beginning FVA balance = 0.
  1. Jun 30 Yr 1 - Brookfield declares and pays $48,000 total cash dividends.
  2. Dec 31 Yr 1 - fair value $14.00/share.
  3. Feb  8 Yr 2 - Copperline sells the entire holding for $86,400 cash.

METHOD (ACCOUNT-343 / Cambridge INT 4e, Chapter 14, LO 14-4, DEMO 14-4)
-----------------------------------------------------------------------
* Initial recognition: an FV-NI equity investment is recorded at purchase price
  PLUS incidental acquisition costs (brokerage/commissions, excise taxes,
  transfer costs).  Commissions are CAPITALIZED, not expensed.  The Investment
  account is then frozen at that original cost for the life of the holding.
* Dividends: with insignificant influence the investor cannot direct investee
  earnings, so revenue is recognized only on declaration -- the investor's
  ownership share of the declared dividend is Dividend Revenue.
* Subsequent measurement: carrying amount is marked to fair value through a
  separate Fair Value Adjustment (FVA) account, never the Investment account.
  The REQUIRED FVA balance is always measured against ORIGINAL COST:
        required FVA = fair value - original cost
  (positive => debit/adjunct balance; negative => credit/contra balance).
  The entry booked each period is the CHANGE needed:
        adjustment = required FVA - existing FVA balance
  with the offsetting side going to Unrealized Gain or Loss - Income.
* Sale: first adjust the investment to fair value at the SALE DATE using the
  same FVA mechanic (so the change in fair value from the last reporting date
  to the sale date hits Year 2 net income).  Then record the sale, removing the
  Investment at original cost and eliminating the FVA balance.  Because the
  fair value change was already recognized, NO separate gain/loss on sale is
  recorded -- proceeds equal the marked carrying amount by construction.
* Holding-period reconciliation: the sum of the unrealized amounts recognized
  across all periods equals total proceeds less original cost.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal, quantized to the cent ("0.01") with
decimal.ROUND_HALF_UP, applied PER PERIOD / PER COMPUTED AMOUNT (the course
convention) rather than only at the end.  No present-value factors are involved
in this item, so no PV table-factor vs exact-formula question arises.  Every
figure here happens to be exact to the cent, so the rounding rule is applied but
never actually breaks a tie; results are emitted as integers when the cents are
zero.  Floats are never used for money.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x):
    """Quantize to the cent, ROUND_HALF_UP. Applied per computed amount."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def out(d):
    """Emit a Decimal as int when whole, else as a 2dp float-free number."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------- given facts
SHARES_BOUGHT = Decimal("6000")
SHARES_OUTSTANDING = Decimal("80000")
PRICE_PER_SHARE = Decimal("15.50")
COMMISSIONS = Decimal("1200")
TOTAL_DIVIDENDS_DECLARED = Decimal("48000")
FV_PER_SHARE_DEC31_Y1 = Decimal("14")
SALE_PROCEEDS = Decimal("86400")
BEGINNING_FVA = Decimal("0")          # stem: "Beginning FVA = 0"

INVESTMENT_ACCT = "Investment in Brookfield Media Co. Common Stock"
FVA_ACCT = "Fair Value Adjustment-Equity Securities"
UGL_ACCT = "Unrealized Gain or Loss-Income"

# --------------------------------------------------- (a) March 1, Year 1 cost
purchase_price = money(SHARES_BOUGHT * PRICE_PER_SHARE)      # 6,000 x 15.50
original_cost = money(purchase_price + COMMISSIONS)          # commissions capitalized

# ownership percentage, derived (not assumed from the stem's "7.5%")
ownership_pct = SHARES_BOUGHT / SHARES_OUTSTANDING           # exact ratio, unrounded

# ------------------------------------------------ (b) June 30, Year 1 dividend
dividend_revenue = money(TOTAL_DIVIDENDS_DECLARED * ownership_pct)

# ------------------------------- (c) FVA schedule: Dec 31 Yr 1 and sale date
fv_dec31_y1 = money(SHARES_BOUGHT * FV_PER_SHARE_DEC31_Y1)   # 6,000 x 14

# Required FVA balance is always measured against ORIGINAL COST.
required_fva_dec31_y1 = money(fv_dec31_y1 - original_cost)   # negative => credit
fva_adjustment_dec31_y1 = money(required_fva_dec31_y1 - BEGINNING_FVA)

# Fair value at the sale date is evidenced by the arm's-length sale proceeds.
fv_sale_date = money(SALE_PROCEEDS)
required_fva_sale_date = money(fv_sale_date - original_cost)
fva_adjustment_sale_date = money(required_fva_sale_date - required_fva_dec31_y1)

# ------------------------------------- (d) Year 1 balance sheet / income stmt
bs_carrying_amount_dec31_y1 = money(original_cost + required_fva_dec31_y1)
y1_unrealized_gain_loss = fva_adjustment_dec31_y1            # negative => loss

# ------------------------------------------------- (e) Year 2 sale and recon
y2_unrealized_gain_loss = fva_adjustment_sale_date            # positive => gain
holding_period_total = money(SALE_PROCEEDS - original_cost)   # negative => net loss

# ------------------------------------------------------------- sanity checks
assert bs_carrying_amount_dec31_y1 == fv_dec31_y1, "Dec 31 carrying amount must equal fair value"
assert money(y1_unrealized_gain_loss + y2_unrealized_gain_loss) == holding_period_total, \
    "Period unrealized amounts must reconcile to total proceeds less cost"


def entry(part, description, lines):
    """Build a journal entry and prove debits == credits before emitting it."""
    dr = sum((money(l[1]) for l in lines), Decimal("0"))
    cr = sum((money(l[2]) for l in lines), Decimal("0"))
    assert money(dr) == money(cr), f"part {part}: debits {dr} != credits {cr}"
    return {
        "part": part,
        "description": description,
        "lines": [
            {"account": a, "debit": out(d), "credit": out(c)} for a, d, c in lines
        ],
    }


Z = Decimal("0")

journal_entries = [
    entry("a", "March 1, Year 1 - purchase of equity investment (commissions capitalized)", [
        (INVESTMENT_ACCT, original_cost, Z),
        ("Cash", Z, original_cost),
    ]),
    entry("b", "June 30, Year 1 - dividend revenue (Copperline's 7.5% share)", [
        ("Cash", dividend_revenue, Z),
        ("Dividend Revenue", Z, dividend_revenue),
    ]),
    entry("c", "December 31, Year 1 - adjust investment to fair value (FV-NI)", [
        (UGL_ACCT, -fva_adjustment_dec31_y1, Z),      # adjustment is negative -> debit the loss
        (FVA_ACCT, Z, -fva_adjustment_dec31_y1),
    ]),
    entry("e", "February 8, Year 2 - sale-date adjustment of investment to fair value (FV-NI)", [
        (FVA_ACCT, fva_adjustment_sale_date, Z),      # adjustment is positive -> debit FVA
        (UGL_ACCT, Z, fva_adjustment_sale_date),
    ]),
    entry("e", "February 8, Year 2 - record sale, eliminating the FVA balance (no separate gain/loss)", [
        ("Cash", SALE_PROCEEDS, Z),
        (FVA_ACCT, -required_fva_sale_date, Z),       # credit balance -> debited to eliminate
        (INVESTMENT_ACCT, Z, original_cost),
    ]),
]

answers = [
    {"label": "c: required Fair Value Adjustment balance at Dec 31, Year 1 (credit/contra balance)",
     "value": out(-required_fva_dec31_y1)},
    {"label": "c: required Fair Value Adjustment balance at Feb 8, Year 2 sale date (credit/contra balance)",
     "value": out(-required_fva_sale_date)},
    {"label": "d: Dec 31, Year 1 balance sheet carrying amount of the equity investment",
     "value": out(bs_carrying_amount_dec31_y1)},
    {"label": "d: Year 1 income statement - dividend revenue",
     "value": out(dividend_revenue)},
    {"label": "d: Year 1 income statement - unrealized holding LOSS on equity securities",
     "value": out(-y1_unrealized_gain_loss)},
    {"label": "e: Year 2 income statement - unrealized holding GAIN recognized at the sale date",
     "value": out(y2_unrealized_gain_loss)},
    {"label": "e: holding-period reconciliation - total net LOSS recognized over the ownership period",
     "value": out(-holding_period_total)},
]

result = {
    "id": "agent_136#01",
    "rounding_convention": (
        "decimal.Decimal throughout; ROUND_HALF_UP to the cent applied per period / "
        "per computed amount (no floats). No PV factors in this item. Required FVA "
        "balance is measured against ORIGINAL COST (purchase price + capitalized "
        "commissions) at each measurement date; only the change is journalized."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Cambridge INT 4e Ch.14 LO 14-4 (DEMO 14-4) method. Commissions of $1,200 are "
        "capitalized into cost, so original cost = 6,000 x $15.50 + $1,200 = $94,200. "
        "Loss/gain answers are reported as positive magnitudes and named LOSS or GAIN in "
        "the label: Year 1 unrealized loss $10,200, Year 2 unrealized gain $2,400, net "
        "holding-period loss $7,800 = $86,400 proceeds - $94,200 cost. At sale the FVA has "
        "a $7,800 CREDIT balance, so it is DEBITED to eliminate it, and no separate gain or "
        "loss on sale is recorded because the fair value change was already recognized."
    ),
}

print(json.dumps(result, indent=2))
