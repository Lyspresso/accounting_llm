#!/usr/bin/env python3
"""Solver for item agent_280#00 -- Meridian Forge Inc. convertible bonds issued at a premium.

FACT PATTERN (from stem.md only)
--------------------------------
Jan 1, Year 1: issue $400,000 face, 6% coupon, 10-year convertible bonds for
$424,000 cash. Straight-debt treatment at issuance (U.S. GAAP: no separate
equity component for the conversion feature). Premium amortized STRAIGHT-LINE.
Cash interest paid annually each December 31.
Each $1,000 bond converts into 20 shares of $5 par common stock.
Dec 31, Year 3, AFTER the year-end interest/amortization entry, holders of 50%
of the bonds convert. Stock trades at $48 (explicitly a distractor).

METHOD
------
* Premium = 424,000 - 400,000 = 24,000; straight-line over 10 annual periods.
* Annual cash interest = face x stated rate (annual payment, so no x n/12).
* Annual interest expense = cash interest - premium amortization (premium
  amortization REDUCES expense).
* Conversion uses the BOOK VALUE METHOD: the carrying amount of the converted
  bonds (pro-rata face + pro-rata unamortized premium) is transferred to
  equity. Common Stock is credited at par; the plug goes to Paid-in Capital in
  Excess of Par. NO gain or loss is recognized and the $48 market price never
  enters the entry (that is the market value method, not U.S. GAAP here).

ROUNDING CONVENTION
-------------------
decimal.Decimal exclusively -- no floats anywhere.
ROUND_HALF_UP to the cent ($0.01) applied PER PERIOD (round-per-period, not
round-at-end): each year's amortization and interest amounts are rounded as
they are computed and the rounded figures roll forward into the next period's
beginning balance, so the schedule ties exactly. No present-value factors are
required for this item (the bond price is given), so no PV-table question
arises. Straight-line amortization of 24,000 over 10 periods is exact
(2,400.00 per period) and the 50% conversion split is exact, so no rounding
residual accumulates; the convention is nonetheless applied deliberately at
every step. Any final penny difference would be absorbed in the last period's
amortization, but none arises here.
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def money(x):
    """Round a Decimal to the cent using ROUND_HALF_UP (applied per period)."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d):
    """Emit a Decimal as a JSON-friendly number (int when whole, else float-free str->float)."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------- given facts
FACE = Decimal("400000")
PROCEEDS = Decimal("424000")
STATED_RATE = Decimal("0.06")
TERM_YEARS = 10
PAR_PER_SHARE = Decimal("5")
BOND_DENOM = Decimal("1000")
SHARES_PER_BOND = Decimal("20")
CONVERT_FRACTION = Decimal("0.50")
CONVERT_YEAR = 3
MARKET_PRICE = Decimal("48")  # distractor: never used in any entry

# ------------------------------------------------- issuance / premium set-up
premium_total = money(PROCEEDS - FACE)                       # 24,000.00
annual_amort = money(premium_total / Decimal(TERM_YEARS))    # 2,400.00
annual_cash_interest = money(FACE * STATED_RATE)             # 24,000.00
annual_interest_expense = money(annual_cash_interest - annual_amort)  # 21,600.00

# ------------------------------------------- part c: schedule, Years 1 -> 3
schedule = []
unamortized = premium_total
for year in range(1, CONVERT_YEAR + 1):
    beginning = unamortized
    # Last-period true-up guard (inert here, but keeps the schedule self-correcting).
    amort = annual_amort if year < TERM_YEARS else beginning
    if amort > beginning:
        amort = beginning
    ending = money(beginning - amort)
    carrying = money(FACE + ending)
    schedule.append(
        {
            "year": year,
            "beginning_unamortized_premium": beginning,
            "amortization": amort,
            "ending_unamortized_premium": ending,
            "carrying_amount_dec_31": carrying,
        }
    )
    unamortized = ending

premium_after_year3 = schedule[-1]["ending_unamortized_premium"]   # 16,800.00
carrying_after_year3 = schedule[-1]["carrying_amount_dec_31"]      # 416,800.00

# --------------------------------------------- part d: 50% conversion at BV
face_converted = money(FACE * CONVERT_FRACTION)
premium_converted = money(premium_after_year3 * CONVERT_FRACTION)
carrying_converted = money(face_converted + premium_converted)

bonds_converted_count = face_converted / BOND_DENOM
shares_issued = bonds_converted_count * SHARES_PER_BOND
common_stock_credit = money(shares_issued * PAR_PER_SHARE)
apic_credit = money(carrying_converted - common_stock_credit)

# --------------------------------- part e: remaining bonds after conversion
face_remaining = money(FACE - face_converted)
premium_remaining = money(premium_after_year3 - premium_converted)
carrying_remaining = money(face_remaining + premium_remaining)

# ------------------------------------------------------------ journal entries
def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


je_a = {
    "part": "a",
    "date": "January 1, Year 1",
    "description": "Issuance of convertible bonds at a premium (straight-debt treatment)",
    "lines": [
        line("Cash", debit=PROCEEDS),
        line("Bonds Payable", credit=FACE),
        line("Premium on Bonds Payable", credit=premium_total),
    ],
}

je_b = {
    "part": "b",
    "date": "December 31, Year 1",
    "description": "Period-end interest payment and straight-line premium amortization",
    "lines": [
        line("Interest Expense", debit=annual_interest_expense),
        line("Premium on Bonds Payable", debit=annual_amort),
        line("Cash", credit=annual_cash_interest),
    ],
}

je_d = {
    "part": "d",
    "date": "December 31, Year 3",
    "description": (
        "Conversion of 50% of the bonds into common stock at book value "
        "(after the Year 3 interest/amortization entry); no gain or loss"
    ),
    "lines": [
        line("Bonds Payable", debit=face_converted),
        line("Premium on Bonds Payable", debit=premium_converted),
        line("Common Stock", credit=common_stock_credit),
        line("Paid-in Capital in Excess of Par - Common Stock", credit=apic_credit),
    ],
}

journal_entries = [je_a, je_b, je_d]

# Debits must equal credits in every entry.
for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert money(dr) == money(cr), f"unbalanced entry in part {je['part']}: {dr} vs {cr}"

# Internal consistency of the schedule.
assert money(sum(r["amortization"] for r in schedule)) == money(annual_amort * CONVERT_YEAR)
assert carrying_after_year3 == money(FACE + premium_after_year3)
assert money(carrying_converted + carrying_remaining) == carrying_after_year3
assert MARKET_PRICE == Decimal("48")  # given, deliberately unused

# ------------------------------------------------------------------- answers
answers = []

# Part c -- the amortization schedule, Years 1-3.
for row in schedule:
    y = row["year"]
    answers.append({
        "label": f"c: Year {y} beginning unamortized premium",
        "value": num(row["beginning_unamortized_premium"]),
    })
    answers.append({
        "label": f"c: Year {y} premium amortization (straight-line)",
        "value": num(row["amortization"]),
    })
    answers.append({
        "label": f"c: Year {y} ending unamortized premium",
        "value": num(row["ending_unamortized_premium"]),
    })
    answers.append({
        "label": f"c: carrying amount at December 31, Year {y}",
        "value": num(row["carrying_amount_dec_31"]),
    })

# Part e -- Year 3 balance-sheet presentation and equity credited on conversion.
answers.append({
    "label": "e: face of convertible bonds remaining after the 50% conversion",
    "value": num(face_remaining),
})
answers.append({
    "label": "e: unamortized premium remaining on the unconverted bonds, December 31, Year 3",
    "value": num(premium_remaining),
})
answers.append({
    "label": "e: carrying amount of remaining convertible bonds presented as a long-term liability, December 31, Year 3",
    "value": num(carrying_remaining),
})
answers.append({
    "label": "e: Common Stock credited on conversion (par)",
    "value": num(common_stock_credit),
})
answers.append({
    "label": "e: Paid-in Capital in Excess of Par credited on conversion",
    "value": num(apic_credit),
})
answers.append({
    "label": "e: gain or loss recognized on conversion (book value method)",
    "value": 0,
})

notes = (
    "Straight-debt treatment: entire $424,000 to liability, no equity component at issuance. "
    "Premium $24,000 / 10 years = $2,400 straight-line per year; annual cash interest "
    "$400,000 x 6% = $24,000, so interest expense is $21,600 per year. "
    "Part e: the $200,000 face plus $8,400 unamortized premium remaining is reported as a "
    "single long-term liability line at its $208,400 carrying amount (premium shown as an "
    "addition to Bonds Payable); the bonds are not current because they do not mature until "
    "the end of Year 10. Equity accounts credited on conversion are Common Stock $20,000 "
    "(4,000 shares x $5 par) and Paid-in Capital in Excess of Par $188,400. Under the book "
    "value method required here, NO gain or loss is recognized -- the $208,400 carrying amount "
    "of the converted bonds is simply reclassified to equity. The $48 market price does NOT "
    "enter the conversion entry; it is a distractor (using it would be the market value method, "
    "which would force a loss and is not applied to conversions of the issuer's own convertible "
    "debt under U.S. GAAP)."
)

out = {
    "id": "agent_280#00",
    "rounding_convention": (
        "decimal.Decimal only, no floats; ROUND_HALF_UP to the cent applied per period "
        "(round-per-period, rounded balances roll forward). Straight-line premium "
        "amortization; no PV table factors needed since the issue price is given."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(out, indent=2))
