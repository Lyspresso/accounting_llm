#!/usr/bin/env python3
"""
Solver for item agent_230#00 — Silverpine Fitness Equipment Co.
ACCOUNT-343 / Chapter 15 (LO 15-6): multi-year warranty liability subsequent
measurement, litigation contingency initial recognition and settlement,
commitment/contingency disclosure classification, and liquidity ratios.

ROUNDING CONVENTION
-------------------
- All monetary amounts use decimal.Decimal exclusively. No floats anywhere in
  the money path.
- Money is rounded to the cent with ROUND_HALF_UP, applied per period (each
  year's provision is computed and rounded on its own before it enters the
  rollforward; balances are never re-rounded from an unrounded running total).
  In this fact pattern every provision (sales x rate) lands exactly on a whole
  dollar, so the rounding step is a no-op guard rather than a live adjustment.
- Liquidity ratios are pure ratios, not money. They are computed from exact
  Decimal numerator/denominator and then quantized to 2 decimal places with
  ROUND_HALF_UP, matching the textbook's Demo 15-6 presentation
  (e.g. 11,990 / 12,708 = 0.94).
- No present-value factors are involved in this item.

DERIVATION NOTES
----------------
Warranty (company policy, stated in the stem): cash claims are debited to
Warranty Expense as incurred during the year; at year-end an adjusting entry
brings the liability to
    ending = beginning + estimated cost of that year's sales - claims paid.
Total warranty expense for a year equals the estimated cost for that year's
sales, so the year-end true-up amount is (provision - claims paid), which is
also exactly the change in the liability balance. The true-up therefore debits
Warranty Expense and credits Warranty Liability when the provision exceeds
claims paid (and reverses direction if claims exceed the provision).

Litigation: loss is probable and the best estimate within the range is
$160,000, so ASC 450-20 requires accrual of the best estimate (not the low end
of the range, because a best estimate exists).

Ratios: current ratio = current assets / current liabilities. Quick ratio =
(cash + short-term marketable securities + receivables) / current liabilities,
per the textbook definition -- inventory and prepaid expenses are excluded.
The Year-2 adjustments touch only the denominator: the warranty true-up and
the litigation accrual both raise current liabilities; no current asset moves.

Run: python3 solver.py   (prints one JSON object to stdout)
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
TWO_DP = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Round a monetary amount to the cent, ROUND_HALF_UP, per period."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def ratio(numerator: Decimal, denominator: Decimal) -> Decimal:
    """Ratio to 2 decimal places, ROUND_HALF_UP (textbook Demo 15-6 style)."""
    return (Decimal(numerator) / Decimal(denominator)).quantize(
        TWO_DP, rounding=ROUND_HALF_UP
    )


def num(x: Decimal):
    """JSON-friendly number: int when the value is whole, else float-free str->float."""
    x = Decimal(x)
    if x == x.to_integral_value():
        return int(x)
    return float(x)


# ---------------------------------------------------------------------------
# Given facts (transcribed from the stem)
# ---------------------------------------------------------------------------

WARRANTY_BEGIN_Y1 = Decimal("52000")

WARRANTY_FACTS = [
    # (year, product sales, estimated warranty cost rate, claims paid in cash)
    (1, Decimal("4800000"), Decimal("0.025"), Decimal("105000")),
    (2, Decimal("5400000"), Decimal("0.025"), Decimal("118000")),
    (3, Decimal("5700000"), Decimal("0.020"), Decimal("122000")),
]

# Litigation
LITIGATION_RANGE_LOW = Decimal("120000")
LITIGATION_RANGE_HIGH = Decimal("250000")
LITIGATION_BEST_ESTIMATE = Decimal("160000")
SETTLEMENT_CASH = Decimal("175000")

# Unadjusted December 31, Year 2 balances
CASH = Decimal("380000")
MARKETABLE_SECURITIES = Decimal("140000")
ACCOUNTS_RECEIVABLE = Decimal("920000")
INVENTORY = Decimal("1650000")
PREPAID = Decimal("110000")

ACCOUNTS_PAYABLE = Decimal("710000")
ACCRUED_EXPENSES = Decimal("390000")
SHORT_TERM_NOTES = Decimal("450000")
UNEARNED_REVENUE = Decimal("180000")
WARRANTY_LIAB_ON_BOOKS = Decimal("67000")  # Jan 1, Year 2 balance still on books


# ---------------------------------------------------------------------------
# (a) Three-year warranty liability subsequent-measurement schedule
# ---------------------------------------------------------------------------

warranty_schedule = []
beginning = WARRANTY_BEGIN_Y1
for year, sales, rate, claims in WARRANTY_FACTS:
    provision = money(sales * rate)          # rounded per period
    claims_paid = money(claims)
    ending = money(beginning + provision - claims_paid)
    warranty_schedule.append(
        {
            "year": year,
            "beginning": beginning,
            "provision": provision,
            "claims_paid": claims_paid,
            "ending": ending,
        }
    )
    beginning = ending

y1 = warranty_schedule[0]
y2 = warranty_schedule[1]
y3 = warranty_schedule[2]

# Internal consistency check: the Year-1 ending balance must equal the
# Jan 1, Year 2 warranty liability sitting on the unadjusted books ($67,000).
assert y1["ending"] == WARRANTY_LIAB_ON_BOOKS, (
    f"Year-1 ending warranty liability {y1['ending']} does not tie to the "
    f"Jan 1, Year 2 book balance {WARRANTY_LIAB_ON_BOOKS}"
)
assert y2["beginning"] == WARRANTY_LIAB_ON_BOOKS

# ---------------------------------------------------------------------------
# (b) Dec 31, Year 2 warranty true-up adjusting entry
# ---------------------------------------------------------------------------
# Claims of $118,000 already sit in Warranty Expense. Total Year-2 warranty
# expense must equal the Year-2 provision of $135,000, so the true-up is the
# difference, which is also the change in the liability balance.

warranty_trueup = money(y2["provision"] - y2["claims_paid"])
assert warranty_trueup == money(y2["ending"] - y2["beginning"])

if warranty_trueup >= 0:
    je_b = {
        "part": "b",
        "description": "Dec 31, Year 2 — warranty true-up adjusting entry",
        "lines": [
            {"account": "Warranty Expense", "debit": num(warranty_trueup), "credit": 0},
            {"account": "Warranty Liability", "debit": 0, "credit": num(warranty_trueup)},
        ],
    }
else:
    amt = -warranty_trueup
    je_b = {
        "part": "b",
        "description": "Dec 31, Year 2 — warranty true-up adjusting entry",
        "lines": [
            {"account": "Warranty Liability", "debit": num(amt), "credit": 0},
            {"account": "Warranty Expense", "debit": 0, "credit": num(amt)},
        ],
    }

# ---------------------------------------------------------------------------
# (c) Dec 31, Year 2 litigation loss contingency initial recognition
# ---------------------------------------------------------------------------
# Probable + reasonably estimable with a best estimate inside the range =>
# accrue the best estimate of $160,000 (ASC 450-20-30-1).

assert LITIGATION_RANGE_LOW <= LITIGATION_BEST_ESTIMATE <= LITIGATION_RANGE_HIGH
litigation_accrual = money(LITIGATION_BEST_ESTIMATE)

je_c = {
    "part": "c",
    "description": "Dec 31, Year 2 — initial recognition of litigation loss contingency",
    "lines": [
        {"account": "Loss from Litigation", "debit": num(litigation_accrual), "credit": 0},
        {"account": "Litigation Liability", "debit": 0, "credit": num(litigation_accrual)},
    ],
}

# ---------------------------------------------------------------------------
# (d) Contingency liability rollforward Year 2 -> settlement in Year 3,
#     plus the March 5, Year 3 settlement JE
# ---------------------------------------------------------------------------

cont_begin_y2 = Decimal("0")
cont_prov_y2 = litigation_accrual
cont_pay_y2 = Decimal("0")
cont_end_y2 = money(cont_begin_y2 + cont_prov_y2 - cont_pay_y2)

cont_begin_y3 = cont_end_y2
# Remeasurement in Year 3: the cash settlement exceeds the carrying accrual.
cont_remeasure_y3 = money(SETTLEMENT_CASH - cont_begin_y3)
cont_pay_y3 = money(SETTLEMENT_CASH)
cont_end_y3 = money(cont_begin_y3 + cont_remeasure_y3 - cont_pay_y3)

contingency_schedule = [
    {
        "year": 2,
        "beginning": cont_begin_y2,
        "provision": cont_prov_y2,
        "payments": cont_pay_y2,
        "ending": cont_end_y2,
    },
    {
        "year": 3,
        "beginning": cont_begin_y3,
        "provision": cont_remeasure_y3,
        "payments": cont_pay_y3,
        "ending": cont_end_y3,
    },
]

assert cont_end_y3 == Decimal("0.00")

je_d = {
    "part": "d",
    "description": "Mar 5, Year 3 — settlement of the lawsuit for cash",
    "lines": [
        {"account": "Litigation Liability", "debit": num(cont_begin_y3), "credit": 0},
        {"account": "Loss from Litigation", "debit": num(cont_remeasure_y3), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": num(cont_pay_y3)},
    ],
}

# ---------------------------------------------------------------------------
# (f) Liquidity ratios, unadjusted and adjusted
# ---------------------------------------------------------------------------

current_assets = money(
    CASH + MARKETABLE_SECURITIES + ACCOUNTS_RECEIVABLE + INVENTORY + PREPAID
)
quick_assets = money(CASH + MARKETABLE_SECURITIES + ACCOUNTS_RECEIVABLE)
current_liabilities_unadj = money(
    ACCOUNTS_PAYABLE
    + ACCRUED_EXPENSES
    + SHORT_TERM_NOTES
    + UNEARNED_REVENUE
    + WARRANTY_LIAB_ON_BOOKS
)

assert current_assets == Decimal("3200000.00")
assert current_liabilities_unadj == Decimal("1797000.00")

# The (b) and (c) entries add to current liabilities only; no current asset moves.
current_liabilities_adj = money(
    current_liabilities_unadj + warranty_trueup + litigation_accrual
)

current_ratio_unadj = ratio(current_assets, current_liabilities_unadj)
quick_ratio_unadj = ratio(quick_assets, current_liabilities_unadj)
current_ratio_adj = ratio(current_assets, current_liabilities_adj)
quick_ratio_adj = ratio(quick_assets, current_liabilities_adj)


# ---------------------------------------------------------------------------
# Assemble output
# ---------------------------------------------------------------------------

answers = []

# (a) three-year warranty liability schedule
for row in warranty_schedule:
    y = row["year"]
    answers.append(
        {"label": f"a: Year {y} warranty liability beginning balance",
         "value": num(row["beginning"])}
    )
    answers.append(
        {"label": f"a: Year {y} warranty provision (estimated cost of that year's sales)",
         "value": num(row["provision"])}
    )
    answers.append(
        {"label": f"a: Year {y} warranty claims paid", "value": num(row["claims_paid"])}
    )
    answers.append(
        {"label": f"a: Year {y} warranty liability ending balance",
         "value": num(row["ending"])}
    )

# (d) contingency liability schedule
for row in contingency_schedule:
    y = row["year"]
    answers.append(
        {"label": f"d: Year {y} contingency liability beginning balance",
         "value": num(row["beginning"])}
    )
    answers.append(
        {"label": f"d: Year {y} contingency provision / remeasurement",
         "value": num(row["provision"])}
    )
    answers.append(
        {"label": f"d: Year {y} contingency payments", "value": num(row["payments"])}
    )
    answers.append(
        {"label": f"d: Year {y} contingency liability ending balance",
         "value": num(row["ending"])}
    )

# (f) ratios
answers.append({"label": "f: current ratio — unadjusted Dec 31, Year 2",
                "value": float(current_ratio_unadj)})
answers.append({"label": "f: quick ratio — unadjusted Dec 31, Year 2",
                "value": float(quick_ratio_unadj)})
answers.append({"label": "f: current ratio — after warranty true-up and litigation accrual",
                "value": float(current_ratio_adj)})
answers.append({"label": "f: quick ratio — after warranty true-up and litigation accrual",
                "value": float(quick_ratio_adj)})

journal_entries = [je_b, je_c, je_d]

# Debits must equal credits in every entry.
for je in journal_entries:
    dr = sum(Decimal(str(ln["debit"])) for ln in je["lines"])
    cr = sum(Decimal(str(ln["credit"])) for ln in je["lines"])
    assert dr == cr, f"Entry {je['part']} out of balance: debits {dr} vs credits {cr}"

notes = (
    "Part a verification: Year-1 ending warranty liability of 67,000 (52,000 + 120,000 "
    "- 105,000) ties to the Jan 1, Year 2 balance still on the unadjusted books; Year-2 "
    "ending is 84,000 (67,000 + 135,000 - 118,000). Part b: claims of 118,000 were "
    "already expensed during Year 2, so the true-up is 135,000 - 118,000 = 17,000, which "
    "equals the change in the liability. Part c: probable with a best estimate inside the "
    "range, so the best estimate of 160,000 is accrued rather than the 120,000 low end. "
    "Part d narrative: the March 5, Year 3 settlement is a RECOGNIZED (Type 1) subsequent "
    "event because it confirms a condition existing at December 31, Year 2 and occurs "
    "before the March 12, Year 3 issuance date; the Year-2 statements would therefore be "
    "adjusted to accrue the full 175,000 (an extra 15,000 of Year-2 loss), leaving no "
    "Year-3 remeasurement. Part e classification: (i) litigation accrual — ACCRUED and "
    "DISCLOSED (probable and estimable; disclose nature of the suit, the 120,000-250,000 "
    "range, and the amount accrued); (ii) warranty liability — ACCRUED and DISCLOSED "
    "(ASC 460-10-50-8 requires the accounting policy/methodology plus a tabular "
    "reconciliation of the warranty liability rollforward); (iii) plant expansion "
    "commitment of 1,500,000 — DISCLOSED ONLY, not accrued (ASC 440-10-50-1(f)(1): a "
    "commitment for plant acquisition is not a present obligation; disclose the amount, "
    "the noncancelable terms, and the expected May Year 3 closing); (iv) unused letter of "
    "credit of 600,000 — DISCLOSED ONLY (ASC 440-10-50-1(a): disclose the existence and "
    "unused amount of the facility). Part f analysis: both entries hit only the "
    "denominator, raising current liabilities by 177,000 from 1,797,000 to 1,974,000 "
    "while current assets stay at 3,200,000, so the current ratio falls from 1.78 to 1.62 "
    "and the quick ratio falls from 0.80 to 0.73 — apparent short-term liquidity "
    "deteriorates even though no cash has yet left the company, and the quick ratio "
    "staying below 1.0 shows the most liquid assets alone do not cover current "
    "obligations."
)

output = {
    "id": "agent_230#00",
    "rounding_convention": (
        "decimal.Decimal only, no floats; money quantized to the cent with ROUND_HALF_UP "
        "applied per period (each year's provision rounded before entering the "
        "rollforward); liquidity ratios computed from exact Decimal amounts and quantized "
        "to 2 decimal places with ROUND_HALF_UP per the textbook Demo 15-6 presentation; "
        "no present-value factors apply to this item."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(output, indent=2))
