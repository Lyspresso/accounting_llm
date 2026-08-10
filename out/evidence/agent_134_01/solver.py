#!/usr/bin/env python3
"""
Solver for item agent_134#01 — ACCOUNT-343 Ch.14 LO 14-2.

FACT PATTERN (from stem.md, nothing hard-coded beyond these givens)
-------------------------------------------------------------------
Jan 1, Year 1: Harborpeak Capital LLC buys, AT PAR, $40,000 of Redwood Corp. 6%
bonds maturing Dec 31 of Year 8. Cash interest paid ANNUALLY each Dec 31.
Classified as trading securities (TS), measured FV-NI. Year-end Dec 31.
Beginning Fair Value Adjustment—TS (FVA) balance is zero. No other TS activity.

  Dec 31, Year 1  fair value  $38,500
  Dec 31, Year 2  fair value  $41,200  (still held)
  Jan  1, Year 3  sold entire holding for $41,000

METHOD
------
Purchased AT PAR => stated rate == market rate => there is NO discount or
premium, so amortized cost stays at par ($40,000) for every measurement date
and no effective-interest amortization table is required. Cash interest each
Dec 31 is par x stated rate x 12/12 and is entirely Interest Revenue (the
Jan 1 purchase date coincides with the start of an interest period, so no
accrued interest is purchased and no year-end accrual is needed).

Under FV-NI the investment account is never touched for fair value changes.
The Fair Value Adjustment—TS valuation account carries the difference:

    required FVA balance (at any date) = fair value - amortized cost
    adjustment recorded  = required FVA balance - existing FVA balance

A debit (positive) FVA balance is ADDED to the investment; a credit (negative)
FVA balance is SUBTRACTED. The offsetting side of every adjustment goes to
Unrealized Gain or Loss—Income (net income), per the textbook's TS demo.

Sale of TS is a two-step per the Required wording: (i) first adjust to the
sale-date fair value through FV-NI — sale-date fair value IS the proceeds,
$41,000 — then (ii) record the sale, eliminating the remaining FVA balance.
Because step (i) already trues the carrying amount up to the proceeds, step
(ii) recognizes NO separate realized gain or loss.

Sign convention used in this script: positive = debit-balance / gain,
negative = credit-balance / loss. Journal-entry output converts to explicit
debit/credit columns so every entry can be checked for Dr = Cr.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal — never float. Every monetary figure is
quantized to cents (0.01) using ROUND_HALF_UP, applied per period / per
computed line as it is produced (round-per-period, not round-at-end), which
is this course's convention. Interest is computed as
par x stated rate x (months/12) and rounded to cents at each interest date.
With the given facts every amount lands on an exact whole dollar, so the
rounding rule never actually has to break a tie here; it is applied anyway so
the derivation is reproducible under different inputs.
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENTS = Decimal("0.01")


def money(x) -> Decimal:
    """Quantize to cents with ROUND_HALF_UP (applied per period / per line)."""
    return Decimal(x).quantize(CENTS, rounding=ROUND_HALF_UP)


def out(d: Decimal):
    """Render a Decimal for JSON: int when whole, else float-free string->number."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------- givens ----
PAR = money("40000")            # face amount purchased, bought AT PAR
STATED_RATE = Decimal("0.06")   # 6% coupon
MONTHS_PER_COUPON = 12          # "Cash interest is paid annually each December 31"

FV_Y1 = money("38500")          # Dec 31, Year 1 fair value
FV_Y2 = money("41200")          # Dec 31, Year 2 fair value
PROCEEDS_Y3 = money("41000")    # Jan 1, Year 3 sale price = sale-date fair value

FVA_OPENING = money("0")        # "Beginning FVA-TS is zero"

INVESTMENT_ACCT = "Investment in TS-Redwood Bonds"
FVA_ACCT = "Fair Value Adjustment-TS"
UGL_ACCT = "Unrealized Gain or Loss-Income"


# ------------------------------------------------------- amortized cost ----
# Purchased at par => no discount/premium => amortized cost == par throughout.
AMORTIZED_COST = PAR


def cash_interest(par: Decimal, rate: Decimal, months: int) -> Decimal:
    return money(par * rate * Decimal(months) / Decimal(12))


# ------------------------------------------------------------- part (a) ----
# Jan 1, Year 1 purchase. Bought on an interest-period start date at par, so
# no accrued interest is purchased.
purchase_cost = AMORTIZED_COST
je_a = {
    "part": "a",
    "date": "January 1, Year 1",
    "description": "To record investment purchase (trading securities, at par)",
    "lines": [
        {"account": INVESTMENT_ACCT, "debit": out(purchase_cost), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": out(purchase_cost)},
    ],
}

# ------------------------------------------------------------- part (b) ----
# Dec 31, Year 1 annual cash interest; full 12 months held, all revenue.
interest_y1 = cash_interest(PAR, STATED_RATE, MONTHS_PER_COUPON)
je_b = {
    "part": "b",
    "date": "December 31, Year 1",
    "description": "To record receipt of annual cash interest",
    "lines": [
        {"account": "Cash", "debit": out(interest_y1), "credit": 0},
        {"account": "Interest Revenue", "debit": 0, "credit": out(interest_y1)},
    ],
}

# ------------------------------------------------------------- part (c) ----
# Dec 31, Year 1 FVA schedule and adjusting entry.
required_fva_y1 = money(FV_Y1 - AMORTIZED_COST)          # -1,500 (credit balance)
existing_fva_y1 = FVA_OPENING                            # 0
adjust_y1 = money(required_fva_y1 - existing_fva_y1)     # -1,500
unrealized_y1 = adjust_y1                                # amount hitting NI in Y1

je_c = {
    "part": "c",
    "date": "December 31, Year 1",
    "description": "To adjust trading securities to fair value (FV-NI)",
    "lines": (
        [
            {"account": UGL_ACCT, "debit": out(-adjust_y1), "credit": 0},
            {"account": FVA_ACCT, "debit": 0, "credit": out(-adjust_y1)},
        ]
        if adjust_y1 < 0
        else [
            {"account": FVA_ACCT, "debit": out(adjust_y1), "credit": 0},
            {"account": UGL_ACCT, "debit": 0, "credit": out(adjust_y1)},
        ]
    ),
}

# ------------------------------------------------------------- part (d) ----
# Year 1 balance sheet / income statement presentation.
bs_carrying_y1 = money(AMORTIZED_COST + required_fva_y1)   # = FV_Y1 = 38,500
is_interest_y1 = interest_y1
is_unrealized_y1 = unrealized_y1                           # (1,500) loss
net_income_effect_y1 = money(is_interest_y1 + is_unrealized_y1)

# ------------------------------------------------------------- part (e) ----
# Dec 31, Year 2 FVA rollforward and adjusting entry.
required_fva_y2 = money(FV_Y2 - AMORTIZED_COST)            # +1,200 (debit balance)
existing_fva_y2 = required_fva_y1                          # -1,500 carried forward
adjust_y2 = money(required_fva_y2 - existing_fva_y2)       # +2,700
unrealized_y2 = adjust_y2

je_e = {
    "part": "e",
    "date": "December 31, Year 2",
    "description": "To adjust trading securities to fair value (FV-NI)",
    "lines": (
        [
            {"account": FVA_ACCT, "debit": out(adjust_y2), "credit": 0},
            {"account": UGL_ACCT, "debit": 0, "credit": out(adjust_y2)},
        ]
        if adjust_y2 > 0
        else [
            {"account": UGL_ACCT, "debit": out(-adjust_y2), "credit": 0},
            {"account": FVA_ACCT, "debit": 0, "credit": out(-adjust_y2)},
        ]
    ),
}

# ---------------------------------------------------------- part (f)(i) ----
# Jan 1, Year 3 sale-date FV-NI adjustment. Sale-date fair value = proceeds.
fv_at_sale = PROCEEDS_Y3
required_fva_sale = money(fv_at_sale - AMORTIZED_COST)     # +1,000
existing_fva_sale = required_fva_y2                        # +1,200
adjust_sale = money(required_fva_sale - existing_fva_sale)  # -200
unrealized_y3 = adjust_sale

je_f1 = {
    "part": "f(i)",
    "date": "January 1, Year 3",
    "description": "To adjust investment to fair value at date of sale (FV-NI)",
    "lines": (
        [
            {"account": UGL_ACCT, "debit": out(-adjust_sale), "credit": 0},
            {"account": FVA_ACCT, "debit": 0, "credit": out(-adjust_sale)},
        ]
        if adjust_sale < 0
        else [
            {"account": FVA_ACCT, "debit": out(adjust_sale), "credit": 0},
            {"account": UGL_ACCT, "debit": 0, "credit": out(adjust_sale)},
        ]
    ),
}

# --------------------------------------------------------- part (f)(ii) ----
# Record the sale, eliminating the remaining FVA balance (+1,000 debit balance
# => credit it away). Carrying amount now equals proceeds, so no gain/loss.
sale_lines = [{"account": "Cash", "debit": out(PROCEEDS_Y3), "credit": 0}]
if required_fva_sale > 0:
    sale_lines.append({"account": FVA_ACCT, "debit": 0, "credit": out(required_fva_sale)})
elif required_fva_sale < 0:
    sale_lines.append({"account": FVA_ACCT, "debit": out(-required_fva_sale), "credit": 0})
sale_lines.append({"account": INVESTMENT_ACCT, "debit": 0, "credit": out(AMORTIZED_COST)})

realized_gain_loss_on_sale = money(
    PROCEEDS_Y3 - (AMORTIZED_COST + required_fva_sale)
)  # zero by construction

je_f2 = {
    "part": "f(ii)",
    "date": "January 1, Year 3",
    "description": "To record sale of trading securities, eliminating the FVA balance",
    "lines": sale_lines,
}

# ------------------------------------------------------------- part (g) ----
# Holding-period unrealized G/L schedule: cumulative NI from fair value
# changes must equal proceeds - original cost.
cumulative_unrealized = money(unrealized_y1 + unrealized_y2 + unrealized_y3)
proceeds_less_cost = money(PROCEEDS_Y3 - purchase_cost)

# ------------------------------------------------------------ self-check ---
journal_entries = [je_a, je_b, je_c, je_e, je_f1, je_f2]
for je in journal_entries:
    dr = sum(Decimal(str(ln["debit"])) for ln in je["lines"])
    cr = sum(Decimal(str(ln["credit"])) for ln in je["lines"])
    assert money(dr) == money(cr), f"Entry {je['part']} out of balance: {dr} vs {cr}"

assert cumulative_unrealized == proceeds_less_cost, "Part (g) proof failed"
assert realized_gain_loss_on_sale == money("0"), "Sale should produce no separate G/L"
assert bs_carrying_y1 == FV_Y1

# ---------------------------------------------------------------- answers --
answers = [
    # (c) FVA schedule, Dec 31 Year 1
    {"label": "c: Year 1 unrealized holding gain (loss) = fair value - amortized cost",
     "value": out(unrealized_y1)},
    {"label": "c: required Fair Value Adjustment-TS balance at Dec 31, Year 1 (credit)",
     "value": out(required_fva_y1)},
    {"label": "c: existing FVA balance before the Dec 31, Year 1 adjustment",
     "value": out(existing_fva_y1)},
    {"label": "c: increase (decrease) to FVA account needed at Dec 31, Year 1",
     "value": out(adjust_y1)},

    # (d) Year 1 presentation
    {"label": "d: balance sheet - Investment in trading securities (current asset), Dec 31 Year 1",
     "value": out(bs_carrying_y1)},
    {"label": "d: income statement - Interest revenue, Year 1",
     "value": out(is_interest_y1)},
    {"label": "d: income statement - Unrealized holding gain (loss) on trading securities, Year 1",
     "value": out(is_unrealized_y1)},
    {"label": "d: net effect on Year 1 net income from this investment",
     "value": out(net_income_effect_y1)},

    # (e) Dec 31 Year 2 rollforward
    {"label": "e: required Fair Value Adjustment-TS balance at Dec 31, Year 2 (debit)",
     "value": out(required_fva_y2)},
    {"label": "e: existing FVA balance before the Dec 31, Year 2 adjustment (credit)",
     "value": out(existing_fva_y2)},
    {"label": "e: increase (decrease) to FVA account needed at Dec 31, Year 2",
     "value": out(adjust_y2)},
    {"label": "e: Year 2 unrealized holding gain (loss) recognized in net income",
     "value": out(unrealized_y2)},

    # (f) sale
    {"label": "f(i): required FVA balance at date of sale, Jan 1 Year 3 (debit)",
     "value": out(required_fva_sale)},
    {"label": "f(i): increase (decrease) to FVA account needed at date of sale",
     "value": out(adjust_sale)},
    {"label": "f(ii): gain (loss) recognized on the sale itself",
     "value": out(realized_gain_loss_on_sale)},

    # (g) holding-period proof
    {"label": "g: Year 1 unrealized holding gain (loss)", "value": out(unrealized_y1)},
    {"label": "g: Year 2 unrealized holding gain (loss)", "value": out(unrealized_y2)},
    {"label": "g: Year 3 (sale-date) unrealized holding gain (loss)", "value": out(unrealized_y3)},
    {"label": "g: cumulative gain (loss) recognized over holding period",
     "value": out(cumulative_unrealized)},
    {"label": "g: proceeds minus original cost (proof figure)",
     "value": out(proceeds_less_cost)},
]

result = {
    "id": "agent_134#01",
    "rounding_convention": (
        "decimal.Decimal only, never float; every money figure quantized to cents "
        "with ROUND_HALF_UP applied per period/per line as produced (round-per-period, "
        "not round-at-end). Bonds bought at par, so amortized cost = par $40,000 at "
        "every date and no effective-interest amortization or PV table factor is "
        "needed; annual cash interest = par x 6% x 12/12 rounded to cents."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Bought AT PAR on an interest-payment-period start date, so there is no "
        "discount/premium to amortize and no accrued interest purchased; amortized "
        "cost stays $40,000 throughout. FVA rolls -1,500 (Y1) -> +1,200 (Y2) -> "
        "+1,000 (sale date), giving NI effects of (1,500), 2,700 and (200). Sale-date "
        "fair value is taken as the $41,000 proceeds, so the sale entry itself "
        "records no separate realized gain or loss. Cumulative fair-value effect on "
        "NI = 1,000 = $41,000 proceeds - $40,000 cost, which is the part (g) proof. "
        "Year 2 cash interest of $2,400 was received Dec 31 Year 2 but part (e) asks "
        "only for the FVA rollforward and adjusting entry, so it is not reported."
    ),
}

print(json.dumps(result, indent=2))
