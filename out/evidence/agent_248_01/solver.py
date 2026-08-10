#!/usr/bin/env python3
"""Blind solver for item agent_248#01 - Silverbrook Medical Devices Inc. ESPP (LO 20-3).

WHAT THIS SOLVES
----------------
Two employee stock purchase plans, $2 par common stock.

  Plan N - noncompensatory design.  Purchase price 95% of market on the purchase
           date (5% discount, within the ASC 718-50-25-1 safe harbor), open to
           substantially all eligible employees on an equitable basis, refunds of
           withholdings on cancellation before purchase, enrollment window after
           the price is fixed <= 31 days.  All three noncompensatory criteria are
           met, so NO compensation cost is recognized.

  Plan C - compensatory design.  Only designated high performers may participate
           (fails the "substantially all employees" criterion) AND the discount is
           10% (exceeds the 5% safe harbor).  Compensation expense equals the
           employee discount on the shares purchased.

ROUNDING CONVENTION
-------------------
* All money is decimal.Decimal.  No binary floats are used anywhere.
* ROUND_HALF_UP, applied per period / per computed line (not deferred to the end).
  Every amount in this fact pattern is exact to the cent before rounding
  (prices are $48.00, $40.00; percentages 95% and 90% land on whole cents), so
  the quantizer is a guard rail rather than a source of difference.
* Money is quantized to 2 decimal places ($0.01) at the point each amount is
  computed; the JSON emitter drops a trailing ".00" so whole-dollar amounts print
  as plain integers.
* Share counts: whole shares only.  Shares = accumulated withholdings // price
  per share, using integer floor division on the Decimal quotient.  The stem
  states "whole shares only; exact fit", and the derivation below confirms the
  division is exact (no residual liability balance carries forward).
* Paid-in Capital in Excess of Par is the balancing credit in every issuance
  entry, consistent with the course text's ESPP illustrations.

DERIVATION (all figures below are computed, none are hard-coded)
---------------------------------------------------------------
Cash purchases on September 30, Year 1, market price $48:
  Plan N: 3,000 sh x $48 x 95% = cash;  par credit 3,000 x $2;  APIC = balance.
          Noncompensatory -> no compensation expense.
  Plan C: 2,000 sh x $48 x 90% = cash;  compensation expense = 2,000 x $48 x 10%;
          par credit 2,000 x $2;  APIC = balance.

Payroll-funded Plan N cohort (Jan 1 - Jun 30 offering):
  $11,400 withheld each month for 6 months, credited to Liability-ESPP.
  Accumulated liability at June 30 = 6 x $11,400.
  June 30 purchase price = 95% x $40 market.
  Shares issued = accumulated liability / purchase price (whole shares).
  Settlement clears the liability: par credit = shares x $2, APIC = balance.
  Plan N is noncompensatory -> no compensation expense on this cohort either.

Total Year 1 compensation expense from these ESPP transactions is therefore the
Plan C discount only.

Run:  python3 solver.py   ->  prints one JSON object on stdout.
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 40

CENT = Decimal("0.01")


def money(x: Decimal) -> Decimal:
    """Quantize to cents using the course convention, ROUND_HALF_UP."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly number: int when the amount is whole dollars, else float-free str->float."""
    q = money(x)
    if q == q.to_integral_value():
        return int(q)
    # keep exact cents without ever constructing a binary float from arithmetic
    return float(str(q))


# ---------------------------------------------------------------------------
# Given fact pattern (transcribed from the stem only)
# ---------------------------------------------------------------------------
PAR = Decimal("2")                       # $2 par common stock

PLAN_N_PCT = Decimal("0.95")             # purchase price = 95% of market
PLAN_C_PCT = Decimal("0.90")             # purchase price = 90% of market

SEP30_MARKET = Decimal("48")             # market price on September 30, Year 1
PLAN_N_SHARES_SEP30 = 3000
PLAN_C_SHARES_SEP30 = 2000

MONTHLY_WITHHOLDING = Decimal("11400")   # per month, six months
MONTHS = 6
MONTH_LABELS = ["January 31", "February 28", "March 31",
                "April 30", "May 31", "June 30"]
JUN30_MARKET = Decimal("40")             # market price on June 30, Year 1


# ---------------------------------------------------------------------------
# a. Classification
# ---------------------------------------------------------------------------
# Plan N: discount = 1 - 95% = 5% (<= 5% safe harbor), substantially all employees
#         on an equitable basis, refundable withholdings, <= 31-day enrollment
#         window -> noncompensatory.
plan_n_discount_pct = (Decimal("1") - PLAN_N_PCT) * Decimal("100")
# Plan C: participation limited to designated high performers (fails the
#         "substantially all employees" criterion) and discount = 10% > 5%.
plan_c_discount_pct = (Decimal("1") - PLAN_C_PCT) * Decimal("100")

plan_n_class = "Noncompensatory"
plan_c_class = "Compensatory"


# ---------------------------------------------------------------------------
# b. September 30 - Plan N initial recognition (noncompensatory)
# ---------------------------------------------------------------------------
n_price = money(SEP30_MARKET * PLAN_N_PCT)                 # $ per share paid
n_cash = money(Decimal(PLAN_N_SHARES_SEP30) * n_price)
n_par = money(Decimal(PLAN_N_SHARES_SEP30) * PAR)
n_apic = money(n_cash - n_par)                             # balancing credit

je_b = {
    "part": "b",
    "description": "September 30, Year 1 - issuance of 3,000 shares under Plan N "
                   "(noncompensatory employee stock purchase plan)",
    "lines": [
        {"account": "Cash", "debit": num(n_cash), "credit": 0},
        {"account": "Common Stock", "debit": 0, "credit": num(n_par)},
        {"account": "Paid-in Capital in Excess of Par-Common Stock",
         "debit": 0, "credit": num(n_apic)},
    ],
}


# ---------------------------------------------------------------------------
# c. September 30 - Plan C initial recognition (compensatory)
# ---------------------------------------------------------------------------
c_price = money(SEP30_MARKET * PLAN_C_PCT)
c_cash = money(Decimal(PLAN_C_SHARES_SEP30) * c_price)
c_comp_exp = money(Decimal(PLAN_C_SHARES_SEP30) * SEP30_MARKET *
                   (Decimal("1") - PLAN_C_PCT))            # employee discount
c_par = money(Decimal(PLAN_C_SHARES_SEP30) * PAR)
c_apic = money(c_cash + c_comp_exp - c_par)                # balancing credit

je_c = {
    "part": "c",
    "description": "September 30, Year 1 - issuance of 2,000 shares under Plan C "
                   "(compensatory employee stock purchase plan)",
    "lines": [
        {"account": "Cash", "debit": num(c_cash), "credit": 0},
        {"account": "Compensation Expense", "debit": num(c_comp_exp), "credit": 0},
        {"account": "Common Stock", "debit": 0, "credit": num(c_par)},
        {"account": "Paid-in Capital in Excess of Par-Common Stock",
         "debit": 0, "credit": num(c_apic)},
    ],
}


# ---------------------------------------------------------------------------
# d. Six-month Liability-ESPP accumulation schedule and shares issued
# ---------------------------------------------------------------------------
schedule = []
running = Decimal("0")
for i in range(MONTHS):
    beginning = money(running)
    withheld = money(MONTHLY_WITHHOLDING)
    running = money(beginning + withheld)          # round per period
    schedule.append({
        "date": MONTH_LABELS[i] + ", Year 1",
        "beginning_balance": num(beginning),
        "withholding": num(withheld),
        "ending_balance": num(running),
    })

accumulated = running                              # Liability-ESPP at June 30
jun30_price = money(JUN30_MARKET * PLAN_N_PCT)     # 95% of $40 market

shares_issued = int((accumulated / jun30_price).to_integral_value(rounding="ROUND_FLOOR"))
residual = money(accumulated - Decimal(shares_issued) * jun30_price)
exact_fit = residual == Decimal("0")


# ---------------------------------------------------------------------------
# e. Representative January 31 withholding JE and June 30 settlement JE
# ---------------------------------------------------------------------------
je_e1 = {
    "part": "e",
    "description": "January 31, Year 1 - representative period-end payroll "
                   "withholding for the Plan N cohort (one of six identical "
                   "monthly entries)",
    "lines": [
        {"account": "Cash", "debit": num(MONTHLY_WITHHOLDING), "credit": 0},
        {"account": "Liability-Employee Stock Purchase Plan",
         "debit": 0, "credit": num(MONTHLY_WITHHOLDING)},
    ],
}

settle_par = money(Decimal(shares_issued) * PAR)
settle_apic = money(accumulated - settle_par)      # balancing credit

je_e2 = {
    "part": "e",
    "description": "June 30, Year 1 - settlement: issuance of shares to the "
                   "payroll-funded Plan N cohort at 95% of the $40 market price",
    "lines": [
        {"account": "Liability-Employee Stock Purchase Plan",
         "debit": num(accumulated), "credit": 0},
        {"account": "Common Stock", "debit": 0, "credit": num(settle_par)},
        {"account": "Paid-in Capital in Excess of Par-Common Stock",
         "debit": 0, "credit": num(settle_apic)},
    ],
}


# ---------------------------------------------------------------------------
# f. Total Year 1 compensation expense from these ESPP transactions
# ---------------------------------------------------------------------------
comp_plan_n_cash = Decimal("0")      # noncompensatory
comp_plan_c_cash = c_comp_exp        # compensatory discount
comp_payroll_cohort = Decimal("0")   # Plan N cohort, noncompensatory
total_comp_expense = money(comp_plan_n_cash + comp_plan_c_cash + comp_payroll_cohort)


# ---------------------------------------------------------------------------
# Integrity checks - debits must equal credits in every entry
# ---------------------------------------------------------------------------
def check_balanced(entry):
    d = sum(Decimal(str(l["debit"])) for l in entry["lines"])
    c = sum(Decimal(str(l["credit"])) for l in entry["lines"])
    assert d == c, f"unbalanced entry {entry['description']!r}: {d} != {c}"


journal_entries = [je_b, je_c, je_e1, je_e2]
for e in journal_entries:
    check_balanced(e)

assert exact_fit, f"withholdings do not buy a whole number of shares; residual {residual}"
assert plan_n_discount_pct == Decimal("5")
assert plan_c_discount_pct == Decimal("10")


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
answers = [
    {"label": "a: Plan N classification", "value": plan_n_class},
    {"label": "a: Plan C classification", "value": plan_c_class},
    {"label": "d: Liability-ESPP balance after January withholding", "value": num(Decimal(schedule[0]["ending_balance"]))},
    {"label": "d: Liability-ESPP balance after February withholding", "value": num(Decimal(schedule[1]["ending_balance"]))},
    {"label": "d: Liability-ESPP balance after March withholding", "value": num(Decimal(schedule[2]["ending_balance"]))},
    {"label": "d: Liability-ESPP balance after April withholding", "value": num(Decimal(schedule[3]["ending_balance"]))},
    {"label": "d: Liability-ESPP balance after May withholding", "value": num(Decimal(schedule[4]["ending_balance"]))},
    {"label": "d: Liability-ESPP balance at June 30 (total accumulated)", "value": num(accumulated)},
    {"label": "d: shares issued June 30 to the payroll-funded Plan N cohort", "value": shares_issued},
    {"label": "f: total Year 1 compensation expense from these ESPP transactions", "value": num(total_comp_expense)},
]

notes = (
    "a. Plan N is noncompensatory: the 5% discount is within the ASC 718-50-25-1 "
    "safe harbor, substantially all eligible employees may participate equitably, "
    "withholdings are refundable on cancellation before the purchase date, and the "
    "post-price enrollment window does not exceed 31 days - so no compensation cost "
    "is recognized. Plan C is compensatory: participation is limited to designated "
    "high performers (failing the substantially-all-employees criterion) and the 10% "
    "discount exceeds the 5% safe harbor, so the employee discount is compensation "
    "expense. "
    "d. Withholdings accumulate $11,400 per month to $68,400 at June 30; the Plan N "
    "price is 95% x $40 = $38, giving 68,400 / 38 = 1,800 whole shares with no "
    "residual liability (exact fit, as stated). "
    "e. The January 31 entry is one of six identical monthly entries; the debit is "
    "shown as Cash for the funds withheld from employee pay and held by the company "
    "(an equivalent presentation debits Salaries and Wages Payable for the withheld "
    "portion of that payroll). "
    "f. Only Plan C generates compensation expense (2,000 x $48 x 10% = $9,600); the "
    "Plan N cash purchase and the Plan N payroll cohort generate none."
)

out = {
    "id": "agent_248#01",
    "rounding_convention": (
        "decimal.Decimal only, never floats; ROUND_HALF_UP quantized to $0.01 "
        "per period / per computed line (round-per-period, not round-at-end); "
        "whole shares only via floor division of accumulated withholdings by the "
        "purchase price; Paid-in Capital in Excess of Par is the balancing credit"
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(out, indent=2))
