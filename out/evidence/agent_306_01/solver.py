#!/usr/bin/env python3
"""
Blind solver for item agent_306#01 - Cedarpoint Metals Corp. secured borrowing
(accounts receivable assigned as collateral), LO 8-6.

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP to the nearest whole dollar, applied PER PERIOD (each month's
interest accrual is rounded to whole dollars as it is computed, and the rounded
figure is what is recorded and what carries into the schedule/journal entries).
No present-value factors are involved in this item, so no PV-table question
arises. All money is decimal.Decimal; no floats are used in any computation.
Monthly interest = outstanding principal x annual rate x 1/12.

MODEL (from the fact pattern; matches the textbook's LO 8-6 secured-borrowing
pattern - Demo 8-6A "Using Receivables as Collateral for Borrowing"):

* Secured borrowing, NOT a sale: the receivables stay on Cedarpoint's books and
  a note payable is recorded for the advance.
* The flat finance fee is deducted from the loan proceeds at inception and is
  expensed immediately (Finance Expense).
* Interest is charged monthly on the unpaid loan balance and is paid at each
  period end. Cash remitted to the finance company is applied FIRST to that
  month's interest, with the remainder reducing principal (i.e. the remittance
  is the total cash outflow to the lender, not principal-only).
* Write-offs of assigned accounts and further collections do not by themselves
  change the loan balance; the loan is settled by the final payoff.
* Total financing cost = flat finance fee + all interest expense.

NOTE ON AN INTERNAL INCONSISTENCY IN THE STEM: the fee is given as a flat
"$2,250" but glossed "(1.5% of face AR)". 1.5% x $200,000 face = $3,000;
$2,250 is 1.5% of the $150,000 advance. The explicitly stated flat dollar
amount ($2,250) governs and is what this solver uses; the alternative reading
is quantified in "notes" so the discrepancy is visible rather than hidden.

Run: python3 solver.py   ->  prints one JSON object on stdout.
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
DOLLAR = Decimal("1")


def d(x):
    return Decimal(str(x))


def money(x):
    """Round to the nearest whole dollar, ROUND_HALF_UP (per-period rounding)."""
    return x.quantize(DOLLAR, rounding=ROUND_HALF_UP)


# ---------------------------------------------------------------------------
# Facts from the stem
# ---------------------------------------------------------------------------
FACE_AR_ASSIGNED = d("200000")      # AR assigned as collateral, Mar 1 Year 1
ADVANCE_RATE = d("0.75")            # advance = 75% of assigned AR
FLAT_FINANCE_FEE = d("2250")        # flat fee, deducted at inception
ANNUAL_RATE = d("0.12")             # 12% per year on the unpaid loan balance
MONTHS_PER_YEAR = d("12")

# March 31, Year 1 collection event
MAR_AR_SETTLED = d("82000")         # assigned AR cleared
MAR_RETURNS = d("5000")             # sales returns -> Refund Liability
MAR_DISCOUNTS = d("3000")           # sales discounts
MAR_CASH_COLLECTED = d("74000")     # cash collected
MAR_REMITTANCE = d("74000")         # cash remitted to the finance company

# April events
APR_WRITEOFF = d("2500")            # assigned AR written off against AFDA
APR_CASH_COLLECTED = d("50000")     # further collections on assigned accounts


# ---------------------------------------------------------------------------
# Derivations
# ---------------------------------------------------------------------------
def monthly_interest(balance):
    return money(balance * ANNUAL_RATE / MONTHS_PER_YEAR)


# --- (a) March 1 initial recognition -------------------------------------
loan_principal = money(FACE_AR_ASSIGNED * ADVANCE_RATE)          # 150,000
cash_at_inception = money(loan_principal - FLAT_FINANCE_FEE)     # 147,750

# --- internal consistency of the March collection ------------------------
mar_cash_check = money(MAR_AR_SETTLED - MAR_RETURNS - MAR_DISCOUNTS)
assert mar_cash_check == MAR_CASH_COLLECTED, (
    "March cash collected does not reconcile to AR less returns and discounts"
)

# --- (b) loan amortization schedule --------------------------------------
schedule = []

bal = loan_principal
schedule.append({
    "date": "Mar 1, Year 1",
    "event": "Loan issued (advance 75% of $200,000 assigned AR)",
    "beginning_balance": None,
    "interest_expense": None,
    "cash_paid": None,
    "principal_reduction": None,
    "ending_balance": bal,
})

# March 31: interest on the balance outstanding during March, remit collections
mar_interest = monthly_interest(bal)                              # 1,500
mar_principal_reduction = money(MAR_REMITTANCE - mar_interest)    # 72,500
mar_begin = bal
bal = money(bal - mar_principal_reduction)                        # 77,500
schedule.append({
    "date": "Mar 31, Year 1",
    "event": "Remit March collections (interest first, remainder to principal)",
    "beginning_balance": mar_begin,
    "interest_expense": mar_interest,
    "cash_paid": MAR_REMITTANCE,
    "principal_reduction": mar_principal_reduction,
    "ending_balance": bal,
})

# April 30: pay remaining loan in full including April interest
apr_begin = bal
apr_interest = monthly_interest(apr_begin)                        # 775
apr_principal_reduction = apr_begin
apr_cash_paid = money(apr_principal_reduction + apr_interest)     # 78,275
bal = money(apr_begin - apr_principal_reduction)                  # 0
schedule.append({
    "date": "Apr 30, Year 1",
    "event": "Pay remaining loan in full plus April interest",
    "beginning_balance": apr_begin,
    "interest_expense": apr_interest,
    "cash_paid": apr_cash_paid,
    "principal_reduction": apr_principal_reduction,
    "ending_balance": bal,
})

assert bal == Decimal("0"), "loan does not amortize to zero"

total_interest = money(mar_interest + apr_interest)               # 2,275
total_cash_to_lender = money(MAR_REMITTANCE + apr_cash_paid)      # 152,275
assert money(total_cash_to_lender - total_interest) == loan_principal, (
    "cash paid to lender does not equal principal plus interest"
)

# --- (f) total financing cost --------------------------------------------
total_financing_cost = money(FLAT_FINANCE_FEE + total_interest)   # 4,525

# --- (d) April write-off / collection amounts ----------------------------
apr_ar_credit = money(APR_CASH_COLLECTED + APR_WRITEOFF)          # 52,500


# ---------------------------------------------------------------------------
# Journal entries
# ---------------------------------------------------------------------------
def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": money(d(debit)), "credit": money(d(credit))}


journal_entries = [
    {
        "part": "a",
        "date": "Mar 1, Year 1",
        "description": "Record receipt of loan proceeds; $200,000 of AR assigned as "
                       "collateral (secured borrowing - receivables stay on the books)",
        "lines": [
            line("Cash", debit=cash_at_inception),
            line("Finance Expense", debit=FLAT_FINANCE_FEE),
            line("Note Payable", credit=loan_principal),
        ],
    },
    {
        "part": "c",
        "date": "Mar 31, Year 1",
        "description": "Record collection on assigned accounts",
        "lines": [
            line("Cash", debit=MAR_CASH_COLLECTED),
            line("Sales Discount", debit=MAR_DISCOUNTS),
            line("Refund Liability", debit=MAR_RETURNS),
            line("Accounts Receivable", credit=MAR_AR_SETTLED),
        ],
    },
    {
        "part": "c",
        "date": "Mar 31, Year 1",
        "description": "Record remittance to the finance company (March interest plus "
                       "principal reduction)",
        "lines": [
            line("Note Payable", debit=mar_principal_reduction),
            line("Interest Expense", debit=mar_interest),
            line("Cash", credit=MAR_REMITTANCE),
        ],
    },
    {
        "part": "d",
        "date": "April, Year 1",
        "description": "Record April collection on assigned accounts and write-off of "
                       "uncollectible assigned accounts",
        "lines": [
            line("Cash", debit=APR_CASH_COLLECTED),
            line("Allowance for Doubtful Accounts", debit=APR_WRITEOFF),
            line("Accounts Receivable", credit=apr_ar_credit),
        ],
    },
    {
        "part": "e",
        "date": "Apr 30, Year 1",
        "description": "Record payment of the remaining loan balance plus April interest",
        "lines": [
            line("Note Payable", debit=apr_principal_reduction),
            line("Interest Expense", debit=apr_interest),
            line("Cash", credit=apr_cash_paid),
        ],
    },
]

for je in journal_entries:
    dr = sum((l["debit"] for l in je["lines"]), Decimal("0"))
    cr = sum((l["credit"] for l in je["lines"]), Decimal("0"))
    assert dr == cr, "entry does not balance: %s %s (Dr %s / Cr %s)" % (
        je["part"], je["date"], dr, cr)


# ---------------------------------------------------------------------------
# Answers (only figures the Required parts ask for)
# ---------------------------------------------------------------------------
answers = []

# b - loan amortization schedule, Mar 1 -> final payoff
answers.append({"label": "b: Mar 1, Year 1 loan balance after issuance",
                "value": schedule[0]["ending_balance"]})
answers.append({"label": "b: Mar 31, Year 1 beginning loan balance",
                "value": schedule[1]["beginning_balance"]})
answers.append({"label": "b: Mar 31, Year 1 interest expense",
                "value": schedule[1]["interest_expense"]})
answers.append({"label": "b: Mar 31, Year 1 cash paid to finance company",
                "value": schedule[1]["cash_paid"]})
answers.append({"label": "b: Mar 31, Year 1 principal reduction",
                "value": schedule[1]["principal_reduction"]})
answers.append({"label": "b: Mar 31, Year 1 ending loan balance",
                "value": schedule[1]["ending_balance"]})
answers.append({"label": "b: Apr 30, Year 1 beginning loan balance",
                "value": schedule[2]["beginning_balance"]})
answers.append({"label": "b: Apr 30, Year 1 interest expense",
                "value": schedule[2]["interest_expense"]})
answers.append({"label": "b: Apr 30, Year 1 cash paid to finance company",
                "value": schedule[2]["cash_paid"]})
answers.append({"label": "b: Apr 30, Year 1 principal reduction",
                "value": schedule[2]["principal_reduction"]})
answers.append({"label": "b: Apr 30, Year 1 ending loan balance",
                "value": schedule[2]["ending_balance"]})

# f - total financing cost
answers.append({"label": "f: total financing cost (finance fee $2,250 + interest $2,275)",
                "value": total_financing_cost})


# ---------------------------------------------------------------------------
# Emit
# ---------------------------------------------------------------------------
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            q = o.quantize(CENT, rounding=ROUND_HALF_UP)
            return int(q) if q == q.to_integral_value() else float(str(q))
        return super().default(o)


out = {
    "id": "agent_306#01",
    "rounding_convention": (
        "decimal.Decimal throughout; ROUND_HALF_UP to the nearest whole dollar "
        "applied per period (each month's interest rounded as accrued and carried "
        "forward at that rounded amount). No PV factors are used in this item."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Secured borrowing (LO 8-6): the assigned receivables remain on Cedarpoint's "
        "books; a note payable is recorded for the 75% advance ($150,000) and the flat "
        "finance fee is netted out of the proceeds and expensed at inception. Monthly "
        "cash remitted to the finance company is applied first to that month's interest "
        "on the unpaid balance, with the remainder reducing principal: the $74,000 "
        "March 31 remittance covers $1,500 of interest (150,000 x 12% x 1/12) and "
        "$72,500 of principal, leaving $77,500, which is retired April 30 with $775 of "
        "April interest for $78,275 of cash. The April write-off and the additional "
        "$50,000 April collection do not change the loan balance. "
        "STEM INCONSISTENCY: the fee is stated as a flat $2,250 but glossed '1.5% of "
        "face AR'; 1.5% x $200,000 = $3,000, whereas $2,250 = 1.5% of the $150,000 "
        "advance. The explicit flat dollar amount ($2,250) is used. Had $3,000 been "
        "intended, part (a) cash would be $147,000 and part (f) total financing cost "
        "$5,275; nothing else in the schedule or entries would change."
    ),
}

print(json.dumps(out, indent=2, cls=DecimalEncoder))
