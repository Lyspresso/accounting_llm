"""QuarryBend Foods Co. — Q3 CORE alternate angle (agent_367#02).

Discontinued-component disposal JE, intraperiod tax allocation with a
permanent difference (nondeductible fines) and an originating taxable
temporary difference, period-end tax adjusting JE, and income statement.

Rounding convention: all money is decimal.Decimal; every tax computation is
rounded once, at the period level, to the cent using ROUND_HALF_UP.
Nothing is hard-coded: all figures derive from the scenario inputs below.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def r(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def n(x):
    x = r(x)
    return int(x) if x == x.to_integral_value() else float(x)

# ---- scenario inputs ----
revenues          = Decimal("900000")
cogs              = Decimal("400000")
operating_exp     = Decimal("150000")   # includes nondeductible fines
fines_permanent   = Decimal("3000")     # never deductible
future_taxable    = Decimal("36000")    # originating taxable temporary difference
proceeds          = Decimal("156000")
net_assets        = Decimal("180000")
rate              = Decimal("0.25")

# ---- (a) disposal journal entry, Oct 1 Year 3 ----
disposal_gain_loss = proceeds - net_assets          # negative = loss
disposal_loss      = -disposal_gain_loss            # 24,000 pretax loss

# ---- (b) pretax income from continuing operations ----
pretax_cont = revenues - cogs - operating_exp

# ---- (c) taxable income and taxes payable ----
total_pretax_book = pretax_cont - disposal_loss
taxable_income    = total_pretax_book + fines_permanent - future_taxable
taxes_payable     = r(taxable_income * rate)

# ---- (d) deferred tax liability + intraperiod split ----
dtl = r(future_taxable * rate)
tax_expense_cont      = r((pretax_cont + fines_permanent) * rate)
tax_benefit_disc      = r(disposal_loss * rate)
total_tax_expense_net = tax_expense_cont - tax_benefit_disc
# current-tax cross-check of the split
current_tax_cont = r((pretax_cont + fines_permanent - future_taxable) * rate)
split_ties = (current_tax_cont - tax_benefit_disc == taxes_payable) and \
             (total_tax_expense_net == taxes_payable + dtl)

# ---- (e) period-end adjusting JE ----
je_e = [
    {"account": "Income Tax Expense — Continuing Operations", "debit": n(tax_expense_cont), "credit": 0},
    {"account": "Income Tax Benefit — Discontinued Operations", "debit": 0, "credit": n(tax_benefit_disc)},
    {"account": "Income Taxes Payable", "debit": 0, "credit": n(taxes_payable)},
    {"account": "Deferred Tax Liability", "debit": 0, "credit": n(dtl)},
]
total_dr = tax_expense_cont
total_cr = tax_benefit_disc + taxes_payable + dtl

# ---- (f) income statement ----
gross_profit      = revenues - cogs
income_from_cont  = pretax_cont - tax_expense_cont
disc_net_of_tax   = -(disposal_loss - tax_benefit_disc)   # negative = net loss
net_income        = income_from_cont + disc_net_of_tax

answers = [
    {"label": "a: Cash debited on disposal (Oct 1, Yr 3)", "value": n(proceeds)},
    {"label": "a: Loss on disposal of discontinued component debited (pretax)", "value": n(disposal_loss)},
    {"label": "a: Net assets of discontinued component credited (carrying amount removed)", "value": n(net_assets)},

    {"label": "b: Pretax income from continuing operations", "value": n(pretax_cont)},

    {"label": "c: Total pretax book income (continuing + discontinued)", "value": n(total_pretax_book)},
    {"label": "c: Add permanent difference — nondeductible fines", "value": n(fines_permanent)},
    {"label": "c: Deduct originating future taxable amount (temporary difference)", "value": n(future_taxable)},
    {"label": "c: Taxable income, Year 3", "value": n(taxable_income)},
    {"label": "c: Income taxes payable (25% of taxable income)", "value": n(taxes_payable)},

    {"label": "d: Deferred tax liability originating in Year 3 (36,000 x 25%)", "value": n(dtl)},
    {"label": "d: Intraperiod allocation — income tax expense, continuing operations", "value": n(tax_expense_cont)},
    {"label": "d: Intraperiod allocation — income tax benefit, discontinued operations", "value": n(tax_benefit_disc)},
    {"label": "d: Total income tax expense, net (continuing less discontinued benefit)", "value": n(total_tax_expense_net)},

    {"label": "e: Total debits in period-end tax entry", "value": n(total_dr)},
    {"label": "e: Total credits in period-end tax entry", "value": n(total_cr)},

    {"label": "f: Revenues", "value": n(revenues)},
    {"label": "f: Cost of goods sold", "value": n(cogs)},
    {"label": "f: Gross profit", "value": n(gross_profit)},
    {"label": "f: Operating expenses", "value": n(operating_exp)},
    {"label": "f: Income from continuing operations before income taxes", "value": n(pretax_cont)},
    {"label": "f: Income tax expense (continuing operations)", "value": n(tax_expense_cont)},
    {"label": "f: Income from continuing operations", "value": n(income_from_cont)},
    {"label": "f: Discontinued operations — loss on disposal, pretax", "value": n(-disposal_loss)},
    {"label": "f: Discontinued operations — income tax benefit", "value": n(tax_benefit_disc)},
    {"label": "f: Loss from discontinued operations, net of tax", "value": n(disc_net_of_tax)},
    {"label": "f: Net income", "value": n(net_income)},
]

out = {
    "id": "agent_367#02",
    "rounding_convention": "decimal.Decimal throughout; tax amounts rounded once per period to the cent using ROUND_HALF_UP; all figures whole dollars here",
    "answers": answers,
    "journal_entries": [
        {"part": "a", "lines": [
            {"account": "Cash", "debit": n(proceeds), "credit": 0},
            {"account": "Loss on Disposal of Discontinued Component", "debit": n(disposal_loss), "credit": 0},
            {"account": "Net Assets of Discontinued Component", "debit": 0, "credit": n(net_assets)},
        ]},
        {"part": "e", "lines": je_e},
    ],
    "insufficient_info": False,
    "notes": (
        "Dr=Cr proof (a): 156,000 + 24,000 = 180,000. "
        "Dr=Cr proof (e): debits " + str(n(total_dr)) + " = credits " + str(n(total_cr)) + ". "
        "Split cross-check ties to payable + DTL: " + str(split_ties) + " "
        "(continuing current tax " + str(n(current_tax_cont)) + " less disc. ops current benefit "
        + str(n(tax_benefit_disc)) + " = taxes payable " + str(n(taxes_payable)) + "). "
        "g: Tax on the disposal loss is NOT shown with continuing-operations tax expense. Under intraperiod "
        "allocation the 24,000 pretax disposal loss carries its own 6,000 tax benefit (24,000 x 25%), reported "
        "inside the discontinued operations section so that section is presented net of tax at an 18,000 loss; "
        "continuing operations is charged the full 88,250 computed as if it were the only item, which includes "
        "the 750 rate effect of the 3,000 nondeductible fines (a permanent difference that raises the effective "
        "rate and never creates a deferred tax). The 36,000 originating taxable temporary difference does not "
        "change tax expense, only its split: it defers 9,000 of the continuing-operations charge into a deferred "
        "tax liability rather than taxes payable."
    ),
}
print(json.dumps(out, indent=1))
