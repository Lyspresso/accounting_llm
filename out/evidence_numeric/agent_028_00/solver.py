"""Solver for agent_028#00 — Warranty deductible temporary difference (DTA lifecycle).

Rounding convention: all money is decimal.Decimal; every computed figure is
quantized to whole dollars (0.01 exactness is trivially preserved here) using
ROUND_HALF_UP, applied per period (each December 31) rather than cumulatively.
No present values are involved. The DTA roll-forward closes exactly to zero at
December 31, Year 4 because the schedule's ending balance is computed from the
remaining warranty liability, which is driven to zero by the payment schedule.
Nothing is hard-coded: every balance, change, tax payable, expense and pretax
income figure is derived from the given inputs.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x):
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)

def num(d):
    d = q(d)
    return int(d) if d == d.to_integral_value() else float(d)

# ---- Inputs ----------------------------------------------------------------
RATE = Decimal("0.25")
WARRANTY_ACCRUAL_Y1 = Decimal("60000")
PAYMENTS = {1: Decimal("0"), 2: Decimal("20000"), 3: Decimal("25000"), 4: Decimal("15000")}
ACCRUALS = {1: WARRANTY_ACCRUAL_Y1, 2: Decimal("0"), 3: Decimal("0"), 4: Decimal("0")}
TAXABLE_INCOME = {1: Decimal("400000"), 2: Decimal("360000"),
                  3: Decimal("350000"), 4: Decimal("370000")}
YEARS = [1, 2, 3, 4]

# ---- (a) Roll-forward schedule --------------------------------------------
sched = []
liab = Decimal("0")          # GAAP warranty liability (tax basis is always 0)
dta_prior = Decimal("0")
for y in YEARS:
    beg_liab = liab
    beg_dta = dta_prior
    liab = beg_liab + ACCRUALS[y] - PAYMENTS[y]
    # cumulative deductible temporary difference = book basis - tax basis of liability
    cum_td = liab - Decimal("0")
    end_dta = q(cum_td * RATE)
    change = q(end_dta - beg_dta)
    sched.append({"year": y, "beg_liab": q(beg_liab), "accrual": q(ACCRUALS[y]),
                  "paid": q(PAYMENTS[y]), "end_liab": q(liab),
                  "cum_td": q(cum_td), "beg_dta": q(beg_dta),
                  "change": change, "end_dta": end_dta})
    dta_prior = end_dta
assert dta_prior == Decimal("0.00"), "DTA must close to zero at end of Year 4"
assert q(liab) == Decimal("0.00"), "warranty liability must close to zero"

# ---- Tax computations per year --------------------------------------------
tax = {}
for row in sched:
    y = row["year"]
    payable = q(TAXABLE_INCOME[y] * RATE)          # current tax expense
    deferred = q(-row["change"])                   # + = deferred expense, - = benefit
    total_exp = q(payable + deferred)
    # taxable income = pretax GAAP + nondeductible accrual - warranty paid
    # => pretax GAAP = taxable income - accrual + paid
    pretax = q(TAXABLE_INCOME[y] - ACCRUALS[y] + PAYMENTS[y])
    assert q(pretax * RATE) == total_exp, f"Y{y} reconciliation failed"
    tax[y] = {"payable": payable, "current": payable, "deferred": deferred,
              "total": total_exp, "pretax": pretax}

# ---- Answers ---------------------------------------------------------------
A = []
def add(label, value):
    A.append({"label": label, "value": num(value)})

for row in sched:
    y = row["year"]
    add(f"a: Year {y} warranty liability (book basis), beginning balance", row["beg_liab"])
    add(f"a: Year {y} warranty accrued (book expense, not yet deductible)", row["accrual"])
    add(f"a: Year {y} warranty paid (tax deduction taken)", row["paid"])
    add(f"a: Dec 31 Year {y} warranty liability book basis (tax basis $0)", row["end_liab"])
    add(f"a: Dec 31 Year {y} cumulative deductible temporary difference", row["cum_td"])
    add(f"a: Year {y} DTA beginning balance", row["beg_dta"])
    add(f"a: Year {y} DTA change (debit + / credit -) to reach required balance", row["change"])
    add(f"a: Dec 31 Year {y} required Deferred Tax Asset balance (25%)", row["end_dta"])

add("b: Dec 31 Year 1 income tax expense (total)", tax[1]["total"])
add("b: Dec 31 Year 1 Deferred Tax Asset recognized (debit)", sched[0]["change"])
add("b: Dec 31 Year 1 income tax payable (credit)", tax[1]["payable"])

for y in (2, 3):
    add(f"c: Dec 31 Year {y} income tax expense (total)", tax[y]["total"])
    add(f"c: Dec 31 Year {y} Deferred Tax Asset reversal (credit)", -sched[y - 1]["change"])
    add(f"c: Dec 31 Year {y} income tax payable (credit)", tax[y]["payable"])

add("d: Dec 31 Year 4 income tax expense (total)", tax[4]["total"])
add("d: Dec 31 Year 4 Deferred Tax Asset eliminated (credit)", -sched[3]["change"])
add("d: Dec 31 Year 4 income tax payable (credit)", tax[4]["payable"])
add("d: Dec 31 Year 4 ending Deferred Tax Asset balance", sched[3]["end_dta"])

add("e: Dec 31 Year 1 Deferred Tax Asset — noncurrent asset", sched[0]["end_dta"])
add("e: Dec 31 Year 1 Income Tax Payable — current liability", tax[1]["payable"])
add("e: Year 1 note — current income tax expense", tax[1]["current"])
add("e: Year 1 note — deferred income tax benefit (reduces expense)", -tax[1]["deferred"])
add("e: Year 1 note — total income tax expense", tax[1]["total"])

add("f: Year 1 pretax GAAP income (taxable income $400,000 less $60,000 warranty accrual)", tax[1]["pretax"])
add("f: Year 1 pretax GAAP income x 25%", q(tax[1]["pretax"] * RATE))
add("f: Year 1 total income tax expense per entry (b)", tax[1]["total"])

# ---- Journal entries -------------------------------------------------------
def ln(acct, dr=Decimal("0"), cr=Decimal("0")):
    return {"account": acct, "debit": num(dr), "credit": num(cr)}

JE = []
JE.append({"part": "b", "lines": [
    ln("Income Tax Expense", dr=tax[1]["total"]),
    ln("Deferred Tax Asset", dr=sched[0]["change"]),
    ln("Income Tax Payable", cr=tax[1]["payable"]),
]})
for y in (2, 3):
    JE.append({"part": "c", "lines": [
        ln("Income Tax Expense", dr=tax[y]["total"]),
        ln("Deferred Tax Asset", cr=-sched[y - 1]["change"]),
        ln("Income Tax Payable", cr=tax[y]["payable"]),
    ]})
JE.append({"part": "d", "lines": [
    ln("Income Tax Expense", dr=tax[4]["total"]),
    ln("Deferred Tax Asset", cr=-sched[3]["change"]),
    ln("Income Tax Payable", cr=tax[4]["payable"]),
]})
for e in JE:
    assert q(sum(Decimal(str(l["debit"])) for l in e["lines"])) == \
           q(sum(Decimal(str(l["credit"])) for l in e["lines"])), "Dr must equal Cr"

notes = (
    "(a) Why deductible: the warranty is expensed for GAAP when accrued but deducted for tax only when paid, "
    "so the liability's book basis ($60,000 at 12/31/Y1) exceeds its tax basis ($0). The future settlement of that "
    "liability produces future tax deductions, i.e. future taxable amounts are reduced -> a DEDUCTIBLE temporary "
    "difference, recognized as a deferred tax asset at the enacted 25% rate. Taxable income exceeds pretax GAAP income "
    "in Year 1 and is below it in Years 2-4 as the difference reverses with each cash payment. "
    "Roll-forward (liability = cumulative temporary difference; DTA = 25% of it): "
    "Y1 0 + 60,000 accrued - 0 paid = 60,000 -> DTA 15,000 (originate, Dr 15,000); "
    "Y2 60,000 - 20,000 = 40,000 -> DTA 10,000 (reverse, Cr 5,000); "
    "Y3 40,000 - 25,000 = 15,000 -> DTA 3,750 (reverse, Cr 6,250); "
    "Y4 15,000 - 15,000 = 0 -> DTA 0 (reverse, Cr 3,750). A full valuation allowance is not needed: taxable income of "
    "$360,000-$370,000 in the reversal years is ample evidence the deductions will be realized. "
    "(e) Under ASC 740-10-45-4 all deferred tax assets/liabilities are classified NONCURRENT, so the $15,000 DTA is a "
    "noncurrent asset on the Dec 31, Year 1 balance sheet; Income Tax Payable of $100,000 is a current liability. "
    "Year 1 note: current tax expense $100,000, deferred tax benefit $(15,000), total income tax expense $85,000. "
    "(f) Pretax GAAP income $340,000 = taxable income $400,000 - $60,000 warranty accrual; $340,000 x 25% = $85,000 = "
    "total income tax expense ($100,000 current - $15,000 deferred), so the effective rate equals the 25% statutory rate "
    "(no permanent differences). Assumption: the warranty accrual is the only book-tax difference, so pretax GAAP income "
    "is derived from taxable income; the same reconciliation holds in Years 2-4 (Y2 $380,000 x 25% = $95,000; "
    "Y3 $375,000 x 25% = $93,750; Y4 $385,000 x 25% = $96,250). "
    "Convention: whole-dollar amounts throughout, ROUND_HALF_UP; the schedule closes exactly to zero at 12/31/Y4."
)

print(json.dumps({
    "id": "agent_028#00",
    "rounding_convention": "decimal.Decimal throughout; each period's figures quantized to the cent with ROUND_HALF_UP (all amounts fall on whole dollars); journal entries stated in whole dollars; DTA roll-forward closes exactly to zero at Dec 31, Year 4",
    "answers": A,
    "journal_entries": JE,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
