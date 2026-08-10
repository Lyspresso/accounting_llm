#!/usr/bin/env python3
"""Blind solver for item agent_366#02 - ASC 740-10 uncertain tax positions (LO 18-8).

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP, applied per computed amount, quantized to the cent ($0.01) at the
point each figure is produced (i.e., round-per-period / round-at-each-step, not
round-only-at-the-end). No present-value discounting appears anywhere in this
fact pattern, so no PV table factors or exact-formula choice is involved.
All money is decimal.Decimal; floats are never used for money.

DERIVATION NOTES (all figures computed below from the stem's fact pattern)
-------------------------------------------------------------------------
Two-step model (ASC 740-10-25-6, 740-10-30-7):
  Step one  - recognition: recognize a financial-statement benefit only if the
              position is more likely than not (>50%) to be sustained on its
              technical merits, assuming examination with full knowledge.
  Step two  - measurement: measure the benefit as the largest amount of benefit
              that is greater than 50% likely of being realized on settlement.
  Liability for Unrecognized Tax Benefits (UTB)
              = (deduction claimed on the return - deduction whose benefit is
                 recognized in the financial statements) x tax rate.

Part A (Northbridge Metals Co.) - period-end adjusting entries
  Year 1 position: $180,000 claimed. Opening UTB $15,000 implies an
  unrecognized base of $60,000 at 25% -> benefit of a $120,000 deduction had
  been recognized. Dec 31 Year 2 remeasurement: largest deduction with
  cumulative probability >50% is now $100,000, so the unrecognized base becomes
  $180,000 - $100,000 = $80,000 and required UTB = $80,000 x 25%. The change in
  the required balance is the adjusting entry (a change in estimate, recognized
  prospectively through income tax expense - textbook Demo 18-8 / Demo 18-5B
  balance-adjustment pattern).
  Interest and penalties: stated policy records them within income tax expense,
  credited to a separate accrued interest-and-penalties liability (they are not
  part of the UTB balance itself, per the Target disclosure excerpt).
  Position T (current year): $60,000 claimed, meets MLTN (step one passed), step
  two supports the benefit of a $36,000 deduction -> unrecognized base $24,000,
  UTB = $24,000 x 25%.
  Subsequent-measurement schedule rolls beginning -> prior-year remeasurement ->
  current-year addition -> ending (no settlements in Year 2; the stem says to
  ignore settlement of the Year 1 position).

Part B (Windmere Labs Inc.) - fails step one
  40% sustained probability is not >50%, so step one fails and step two is never
  reached: NO benefit is measured or recognized. Tax expense is computed as if
  the position will not be sustained, while income taxes payable follows the
  return as filed. Difference = UTB liability. (Demo 18-8 Example One pattern.)

Part C (Harborline Products LLC) - settlement outcomes
  Recorded UTB $11,250 = unrecognized base $45,000 x 25% on a $150,000 claimed
  deduction ($105,000 of benefit recognized). On resolution, the deduction
  actually disallowed drives the cash/payable obligation; the recorded UTB is
  derecognized and any difference goes to income tax expense (Demo 18-8
  Example Three a/b/c).
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(value) -> Decimal:
    """Quantize to the cent using ROUND_HALF_UP (applied per computed amount)."""
    return Decimal(value).quantize(CENT, rounding=ROUND_HALF_UP)


def num(value: Decimal):
    """JSON-friendly number: int when the amount is a whole dollar, else float."""
    value = money(value)
    return int(value) if value == value.to_integral_value() else float(value)


def entry(part: str, description: str, lines):
    """Build a journal entry dict and assert debits == credits."""
    out_lines = []
    total_dr = Decimal("0")
    total_cr = Decimal("0")
    for account, dr, cr in lines:
        dr = money(dr)
        cr = money(cr)
        total_dr += dr
        total_cr += cr
        out_lines.append({"account": account, "debit": num(dr), "credit": num(cr)})
    assert total_dr == total_cr, (
        f"{part} '{description}' out of balance: Dr {total_dr} vs Cr {total_cr}"
    )
    return {"part": part, "description": description, "lines": out_lines}


# ---------------------------------------------------------------------------
# Given facts (transcribed from the stem; nothing below is a hard-coded answer)
# ---------------------------------------------------------------------------
RATE = Decimal("0.25")

# Part A - Northbridge Metals Co.
A_OPENING_UTB = Decimal("15000")        # UTB liability at start of Year 2
A_PY_DEDUCTION_CLAIMED = Decimal("180000")   # Year 1 uncertain deduction claimed
A_PY_UNRECOGNIZED_BASE_OPENING = Decimal("60000")  # stated: $15,000 = $60,000 x 25%
A_PY_NEW_MEASURED_DEDUCTION = Decimal("100000")    # remeasured at Dec 31, Yr 2
A_INTEREST_PENALTIES = Decimal("2400")
A_T_DEDUCTION_CLAIMED = Decimal("60000")     # current-year Position T on return
A_T_MEASURED_DEDUCTION = Decimal("36000")    # step-two measured benefit
A_T_UNRECOGNIZED_BASE = Decimal("24000")     # stated unrecognized base

# Part B - Windmere Labs Inc.
B_DEDUCTION_CLAIMED = Decimal("75000")
B_SUSTAIN_PROBABILITY = Decimal("0.40")      # fails MLTN (not > 50%)
B_TAXABLE_INCOME_AFTER_DEDUCTION = Decimal("500000")

# Part C - Harborline Products LLC
C_RECORDED_UTB = Decimal("11250")
C_DEDUCTION_CLAIMED = Decimal("150000")
C_UNRECOGNIZED_BASE = Decimal("45000")       # stated: $11,250 = $45,000 x 25%
C_CASE3_ALLOWED = Decimal("105000")
C_CASE4_ALLOWED = Decimal("75000")

answers = []
journal_entries = []

# ---------------------------------------------------------------------------
# PART A
# ---------------------------------------------------------------------------
# Consistency check on the opening balance as described in the stem.
assert money(A_PY_UNRECOGNIZED_BASE_OPENING * RATE) == money(A_OPENING_UTB)

# (a-1) Required UTB for the Year 1 position after Year 2 remeasurement.
a_py_unrecognized_base_new = A_PY_DEDUCTION_CLAIMED - A_PY_NEW_MEASURED_DEDUCTION
a_py_required_utb = money(a_py_unrecognized_base_new * RATE)

# Adjusting amount = change in the required balance (change in estimate).
a_remeasurement_adjustment = money(a_py_required_utb - A_OPENING_UTB)

# (a-2) UTB for current-year Position T (step one met, step two measured).
assert A_T_UNRECOGNIZED_BASE == A_T_DEDUCTION_CLAIMED - A_T_MEASURED_DEDUCTION
a_position_t_utb = money(A_T_UNRECOGNIZED_BASE * RATE)

# (a-3) Year 2 subsequent measurement schedule.
a_schedule_beginning = money(A_OPENING_UTB)
a_schedule_prior_year_remeasurement = a_remeasurement_adjustment
a_schedule_current_year_addition = a_position_t_utb
a_schedule_ending = money(
    a_schedule_beginning
    + a_schedule_prior_year_remeasurement
    + a_schedule_current_year_addition
)

answers.append({
    "label": "a: Part A - Year 2 required UTB liability for the Year 1 position after remeasurement",
    "value": num(a_py_required_utb),
})
answers.append({
    "label": "a: Part A - UTB recorded for current-year Position T",
    "value": num(a_position_t_utb),
})
answers.append({
    "label": "a: Part A - Year 2 UTB schedule, beginning balance",
    "value": num(a_schedule_beginning),
})
answers.append({
    "label": "a: Part A - Year 2 UTB schedule, prior-year position remeasurement (increase)",
    "value": num(a_schedule_prior_year_remeasurement),
})
answers.append({
    "label": "a: Part A - Year 2 UTB schedule, current-year addition (Position T)",
    "value": num(a_schedule_current_year_addition),
})
answers.append({
    "label": "a: Part A - Year 2 UTB schedule, ending balance December 31, Year 2",
    "value": num(a_schedule_ending),
})

# Adjusting JE (i): remeasurement of the prior-year position.
if a_remeasurement_adjustment >= 0:
    journal_entries.append(entry(
        "a(i)",
        "December 31, Year 2 - adjust Liability for Unrecognized Tax Benefits "
        "for remeasurement of the Year 1 position "
        f"(required {a_py_required_utb} less recorded {A_OPENING_UTB})",
        [
            ("Income Tax Expense", a_remeasurement_adjustment, 0),
            ("Liability for Unrecognized Tax Benefits", 0, a_remeasurement_adjustment),
        ],
    ))
else:
    journal_entries.append(entry(
        "a(i)",
        "December 31, Year 2 - adjust Liability for Unrecognized Tax Benefits "
        "for remeasurement of the Year 1 position",
        [
            ("Liability for Unrecognized Tax Benefits", -a_remeasurement_adjustment, 0),
            ("Income Tax Expense", 0, -a_remeasurement_adjustment),
        ],
    ))

# Adjusting JE (ii): interest and penalties, recorded within income tax expense.
journal_entries.append(entry(
    "a(ii)",
    "December 31, Year 2 - accrue interest and penalties on the uncertain tax "
    "position (policy: recorded within income tax expense)",
    [
        ("Income Tax Expense", A_INTEREST_PENALTIES, 0),
        ("Accrued Interest and Penalties Payable", 0, A_INTEREST_PENALTIES),
    ],
))

# ---------------------------------------------------------------------------
# PART B
# ---------------------------------------------------------------------------
b_meets_mltn = B_SUSTAIN_PROBABILITY > Decimal("0.50")
assert not b_meets_mltn  # step one fails -> step two is never performed

b_taxes_payable = money(B_TAXABLE_INCOME_AFTER_DEDUCTION * RATE)
# Financial statements are prepared as if the position will not be sustained:
b_taxable_income_without_deduction = (
    B_TAXABLE_INCOME_AFTER_DEDUCTION + B_DEDUCTION_CLAIMED
)
b_income_tax_expense = money(b_taxable_income_without_deduction * RATE)
b_utb_liability = money(B_DEDUCTION_CLAIMED * RATE)
assert b_income_tax_expense == money(b_taxes_payable + b_utb_liability)

answers.append({
    "label": "b: Part B - Windmere income tax expense, December 31, Year 1",
    "value": num(b_income_tax_expense),
})
answers.append({
    "label": "b: Part B - Windmere income taxes payable, December 31, Year 1",
    "value": num(b_taxes_payable),
})
answers.append({
    "label": "b: Part B - Windmere Liability for Unrecognized Tax Benefits, December 31, Year 1",
    "value": num(b_utb_liability),
})

journal_entries.append(entry(
    "b",
    "December 31, Year 1 - record income tax expense with no benefit recognized "
    "for the position that fails the more-likely-than-not recognition threshold",
    [
        ("Income Tax Expense", b_income_tax_expense, 0),
        ("Income Taxes Payable", 0, b_taxes_payable),
        ("Liability for Unrecognized Tax Benefits", 0, b_utb_liability),
    ],
))

# ---------------------------------------------------------------------------
# PART C - settlement outcomes (each case considered separately)
# ---------------------------------------------------------------------------
assert money(C_UNRECOGNIZED_BASE * RATE) == money(C_RECORDED_UTB)


def settlement_entry(case_label: str, deduction_allowed: Decimal, description: str):
    """Derecognize the recorded UTB; the disallowed deduction drives the payable."""
    disallowed = C_DEDUCTION_CLAIMED - deduction_allowed
    tax_due = money(disallowed * RATE)
    difference = money(tax_due - C_RECORDED_UTB)  # +: extra expense, -: benefit

    lines = [("Liability for Unrecognized Tax Benefits", C_RECORDED_UTB, 0)]
    if difference > 0:
        lines.append(("Income Tax Expense", difference, 0))
    if tax_due > 0:
        lines.append(("Income Taxes Payable", 0, tax_due))
    if difference < 0:
        lines.append(("Income Tax Expense", 0, -difference))
    return entry(case_label, description, lines)


journal_entries.append(settlement_entry(
    "c-case1",
    Decimal("0"),
    "December of Year 2 - full tax benefit lost: none of the $150,000 deduction "
    "sustained; tax due on the entire deduction",
))
journal_entries.append(settlement_entry(
    "c-case2",
    C_DEDUCTION_CLAIMED,
    "December of Year 2 - full tax benefit realized: entire $150,000 deduction "
    "sustained; recorded UTB reversed to income tax expense",
))
journal_entries.append(settlement_entry(
    "c-case3",
    C_CASE3_ALLOWED,
    "December of Year 2 - $105,000 of the deduction allowed, exactly as "
    "previously measured; UTB reclassified to Income Taxes Payable",
))
journal_entries.append(settlement_entry(
    "c-case4",
    C_CASE4_ALLOWED,
    "December of Year 2 - only $75,000 of the deduction allowed; additional "
    "shortfall charged to income tax expense",
))

# Income-statement effects used only for the part d explanation (not reported
# as answers): case 1 = added expense, case 2 = benefit, case 3 = none,
# case 4 = added expense.
c_case1_effect = money((C_DEDUCTION_CLAIMED * RATE) - C_RECORDED_UTB)
c_case2_effect = money(-C_RECORDED_UTB)
c_case3_effect = money(((C_DEDUCTION_CLAIMED - C_CASE3_ALLOWED) * RATE) - C_RECORDED_UTB)
c_case4_effect = money(((C_DEDUCTION_CLAIMED - C_CASE4_ALLOWED) * RATE) - C_RECORDED_UTB)
assert c_case3_effect == Decimal("0.00")

# ---------------------------------------------------------------------------
# Narrative required parts (b explanation, d, e)
# ---------------------------------------------------------------------------
notes = (
    "b (why no benefit is measured under step two): recognition and measurement "
    "are sequential. Step one asks only whether the position is more likely than "
    "not (>50%) to be sustained on its technical merits, assuming the taxing "
    "authority examines it with full knowledge of all relevant information. "
    "Windmere's 40% assessment is not greater than 50%, so the position fails "
    "step one and the company is never permitted to reach step two; there is no "
    "recognized benefit to measure. The financial statements are therefore "
    "prepared as if the entire $75,000 deduction will be disallowed, even though "
    "the return as filed reduces taxes currently payable. "
    "d (case 3): allowing $105,000 is exactly the amount of benefit previously "
    "recognized, so the $11,250 already accrued equals the tax now owed on the "
    "$45,000 disallowed. The settlement entry simply reclassifies the Liability "
    "for Unrecognized Tax Benefits to Income Taxes Payable and has NO income "
    "statement effect - no additional expense and no benefit. By contrast, case 1 "
    "adds $26,250 of income tax expense (tax on the full $150,000 exceeds the "
    "accrual), case 4 adds $7,500 of income tax expense (tax on $75,000 "
    "disallowed exceeds the accrual), and case 2 reduces income tax expense by "
    "$11,250 as the no-longer-needed liability is reversed. Cases 1, 2 and 4 are "
    "changes in estimate accounted for prospectively in Year 2, not restatements "
    "of Year 1. "
    "e (classification and disclosure): a material UTB liability that is expected "
    "to be negotiated through examinations spanning more than one year - i.e., "
    "cash settlement is not expected within twelve months of the balance sheet "
    "date (or the operating cycle, if longer) - is reported as a NONCURRENT "
    "liability, presented separately from (and not netted against) current income "
    "taxes payable or deferred tax accounts. Typical roll-forward disclosure: a "
    "tabular reconciliation of the beginning and ending balances of total "
    "unrecognized tax benefits, showing gross additions for tax positions taken "
    "in the current year, gross additions and reductions for positions of prior "
    "years, reductions for settlements with taxing authorities, and reductions "
    "from lapses of the applicable statutes of limitations."
)

result = {
    "id": "agent_366#02",
    "rounding_convention": (
        "ROUND_HALF_UP applied per computed amount, quantized to the cent "
        "(round-at-each-step, not round-only-at-the-end); decimal.Decimal "
        "throughout, no floats. No present-value discounting in this item, so no "
        "PV table factor vs exact formula choice arises."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(result, indent=2))
