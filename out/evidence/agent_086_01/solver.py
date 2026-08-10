#!/usr/bin/env python3
"""Solver for item agent_086#01 -- Cedarline Robotics, Year 1 intangibles.

Topic: LO 13-1 / 13-2 (US GAAP, ASC 350 / ASC 805). Classification of intangible
items, initial recognition entries, Year-1 amortization schedule, the December 31
adjusting entry, and December 31 carrying amounts.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal. No floats anywhere.
Rounding is ROUND_HALF_UP to the cent (2 dp), applied *per period* -- each
period's amortization charge is computed from exact (unrounded) rates and then
rounded to cents before it is posted or accumulated. Carrying amounts are
derived from the rounded posted charges, never from an unrounded running total.
No present-value factors are involved in this item.

DERIVATION NOTES (why each number is what it is)
------------------------------------------------
* Straight-line amortization, zero residual, over the shorter of legal life and
  estimated useful life (ASC 350-30-35-6).
* Copyright (12-yr useful life, legal life longer) -> finite life, 72,000 / 12.
* Franchise renewable annually with renewals expected indefinitely and no
  foreseeable limit -> indefinite life, NOT amortized (ASC 350-30-35-4).
* Patent: legal life 14 yrs but useful life 7 yrs -> amortize over 7 (shorter).
* Item 4: outside-counsel fees to successfully register an internally developed
  trade name are capitalized (registration/legal costs are not R&D); the trade
  name is expected to be renewed indefinitely -> indefinite life, no
  amortization, so the April 1 date does not matter.
* Item 5: internal salaries and lab supplies to create an invention are R&D and
  are expensed as incurred (ASC 730-10-25-1) -- internally generated intangibles
  are not capitalized.
* Item 6: goodwill = consideration paid - FV of identifiable net assets.
* Item 7: costs of a SUCCESSFUL outside defense of a patent are added to the
  cost of the patent; the patent stays a finite-life intangible. Per the text's
  Demo 13-2 pattern, the added cost is amortized over the patent's REMAINING
  useful life from the date incurred: 7 - 0.5 = 6.5 years remaining at July 1,
  and only 6 of 12 months fall in Year 1, as the stem instructs
  ("prorate partial-year amortization for the patent defense costs").
  Equivalently (and the script checks this): carrying amount at July 1
  = 56,000 - 4,000 = 52,000, + 11,200 = 63,200, over 6.5 yrs for half a year
  = 4,861.54, plus the 4,000 already taken Jan-Jun = 8,861.54 for the year.
* Item 8: a two-year municipal license is a contractual right with a finite
  2-year life, acquired Jan 1 -> a full year of amortization in Year 1.
* Amortization is credited directly to the intangible asset accounts, which is
  the presentation used by the textbook (Demo 13-2); crediting an Accumulated
  Amortization contra account instead would give identical amounts.

Run:  python3 solver.py      -> prints one JSON object on stdout
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x):
    """Round to the cent, ROUND_HALF_UP -- applied once per posted amount."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d):
    """JSON-friendly number: int when whole, else float of the cent-rounded Decimal."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------- fact pattern
COPYRIGHT_COST = Decimal("72000")
COPYRIGHT_LIFE = Decimal("12")          # useful life < legal life

FRANCHISE_COST = Decimal("110000")      # indefinite life

PATENT_COST = Decimal("56000")
PATENT_USEFUL_LIFE = Decimal("7")       # shorter of 14 legal / 7 useful

TRADE_NAME_COST = Decimal("8400")       # registration legal fees, indefinite

RD_COST = Decimal("145000")             # internally generated -> expense

PURCHASE_PRICE = Decimal("1250000")
FV_IDENTIFIABLE_NET_ASSETS = Decimal("980000")

DEFENSE_COST = Decimal("11200")         # July 1, successful defense
DEFENSE_MONTHS_IN_YEAR1 = Decimal("6")

LICENSE_COST = Decimal("24000")
LICENSE_LIFE = Decimal("2")

MONTHS = Decimal("12")

# ------------------------------------------------------- a. classification
classification = {
    "1 Copyright $72,000": "Finite-life intangible asset (12-year useful life; "
                           "shorter than legal life)",
    "2 Franchise $110,000": "Indefinite-life intangible asset (not goodwill); "
                            "renewals expected indefinitely, no amortization",
    "3 Patent $56,000": "Finite-life intangible asset (7-year useful life, "
                        "shorter than the 14-year remaining legal life)",
    "4 Trade name registration fees $8,400": "Indefinite-life intangible asset "
                                             "(not goodwill); external legal/registration "
                                             "costs are capitalized, not amortized",
    "5 Internal engineer salaries and lab supplies $145,000": "Expense (research and "
                                                              "development expensed as incurred; "
                                                              "internally generated intangible)",
    "6 Acquisition of competitor": "Goodwill for the residual excess of price over the "
                                   "fair value of identifiable net assets",
    "7 Successful patent defense fees $11,200": "Capitalized as part of the cost of the "
                                                "patent (finite-life intangible asset)",
    "8 Two-year municipal license $24,000": "Finite-life intangible asset (2-year life)",
}

item7_effect = (
    "Item 7 does not change the patent's classification: it remains a finite-life "
    "intangible asset. The $11,200 successful-defense cost is added to the patent's "
    "carrying amount on July 1 and is amortized straight-line over the patent's "
    "remaining 6.5-year useful life, so only 6 months of that amortization falls in "
    "Year 1. (Had the defense failed, the fees would have been expensed and the "
    "patent tested for impairment.)"
)

# ------------------------------------------------------------------ b. goodwill
goodwill = money(PURCHASE_PRICE - FV_IDENTIFIABLE_NET_ASSETS)

# ------------------------------------------ c. Year-1 amortization schedule
# Copyright: acquired Jan 1 -> full year
copyright_amort = money(COPYRIGHT_COST / COPYRIGHT_LIFE)

# Patent, original cost: acquired Jan 1 -> full year
patent_base_amort = money(PATENT_COST / PATENT_USEFUL_LIFE)

# Patent defense costs: added July 1, remaining useful life 6.5 years, 6/12 in Year 1
# 7 years of useful life less the 0.5 year already elapsed (Jan 1 -> Jul 1)
remaining_life_at_defense = PATENT_USEFUL_LIFE - (DEFENSE_MONTHS_IN_YEAR1 / MONTHS)
defense_amort = money(
    DEFENSE_COST / remaining_life_at_defense * (DEFENSE_MONTHS_IN_YEAR1 / MONTHS)
)

patent_amort_total = money(patent_base_amort + defense_amort)

# Franchise, trade name, goodwill: indefinite life / goodwill -> no amortization
franchise_amort = money(0)
trade_name_amort = money(0)
goodwill_amort = money(0)

# License: acquired Jan 1, 2-year life -> full year
license_amort = money(LICENSE_COST / LICENSE_LIFE)

total_amort = money(
    copyright_amort + patent_amort_total + franchise_amort
    + trade_name_amort + license_amort + goodwill_amort
)

# ------------------------------------------- e. December 31 carrying amounts
patent_cv = money(PATENT_COST + DEFENSE_COST - patent_amort_total)
copyright_cv = money(COPYRIGHT_COST - copyright_amort)
franchise_cv = money(FRANCHISE_COST - franchise_amort)
trade_name_cv = money(TRADE_NAME_COST - trade_name_amort)
license_cv = money(LICENSE_COST - license_amort)
goodwill_cv = money(goodwill - goodwill_amort)

# ------------------------------------------------------- internal consistency
# Textbook (Demo 13-2) restatement of the patent: half a year on original cost,
# then the July 1 balance (including defense cost) over the remaining 6.5 years
# for the second half of the year. Must equal patent_amort_total.
_half_year_original = money(PATENT_COST / PATENT_USEFUL_LIFE * Decimal("0.5"))
_july1_balance = PATENT_COST - _half_year_original + DEFENSE_COST
_second_half = money(_july1_balance / remaining_life_at_defense * Decimal("0.5"))
assert money(_half_year_original + _second_half) == patent_amort_total, (
    _half_year_original, _second_half, patent_amort_total
)

# ------------------------------------------------------------ journal entries
def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": num(debit), "credit": num(credit)}


journal_entries = [
    {"part": "b", "date": "Year 1, January 1", "description": "Purchase copyright (item 1)",
     "lines": [line("Copyright", debit=COPYRIGHT_COST),
               line("Cash", credit=COPYRIGHT_COST)]},
    {"part": "b", "date": "Year 1, January 1", "description": "Purchase franchise (item 2)",
     "lines": [line("Franchise", debit=FRANCHISE_COST),
               line("Cash", credit=FRANCHISE_COST)]},
    {"part": "b", "date": "Year 1, January 1", "description": "Purchase patent (item 3)",
     "lines": [line("Patent", debit=PATENT_COST),
               line("Cash", credit=PATENT_COST)]},
    {"part": "b", "date": "Year 1, January 1",
     "description": "Purchase two-year municipal license (item 8)",
     "lines": [line("License", debit=LICENSE_COST),
               line("Cash", credit=LICENSE_COST)]},
    {"part": "b", "date": "Year 1",
     "description": "Internal salaries and lab supplies on internally developed invention "
                    "(item 5) -- expensed as incurred",
     "lines": [line("Research and Development Expense", debit=RD_COST),
               line("Cash", credit=RD_COST)]},
    {"part": "b", "date": "Year 1",
     "description": "Acquisition of competitor (item 6); residual to goodwill",
     "lines": [line("Identifiable Net Assets (at fair value)",
                    debit=FV_IDENTIFIABLE_NET_ASSETS),
               line("Goodwill", debit=goodwill),
               line("Cash", credit=PURCHASE_PRICE)]},
    {"part": "b", "date": "Year 1, April 1",
     "description": "External counsel fees to register internally developed trade name (item 4)",
     "lines": [line("Trade Name", debit=TRADE_NAME_COST),
               line("Cash", credit=TRADE_NAME_COST)]},
    {"part": "b", "date": "Year 1, July 1",
     "description": "External legal fees to successfully defend the purchased patent (item 7); "
                    "capitalized to the patent",
     "lines": [line("Patent", debit=DEFENSE_COST),
               line("Cash", credit=DEFENSE_COST)]},
    {"part": "d", "date": "Year 1, December 31",
     "description": "Year-1 amortization adjusting entry",
     "lines": [line("Amortization Expense", debit=total_amort),
               line("Patent", credit=patent_amort_total),
               line("Copyright", credit=copyright_amort),
               line("License", credit=license_amort)]},
]

for entry in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in entry["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in entry["lines"])
    assert money(dr) == money(cr), (entry["description"], dr, cr)

# -------------------------------------------------------------------- answers
answers = [
    # a. classification
    {"label": "a: item 1 copyright $72,000 - classification", "value": classification["1 Copyright $72,000"]},
    {"label": "a: item 2 franchise $110,000 - classification", "value": classification["2 Franchise $110,000"]},
    {"label": "a: item 3 patent $56,000 - classification", "value": classification["3 Patent $56,000"]},
    {"label": "a: item 4 trade name registration fees $8,400 - classification",
     "value": classification["4 Trade name registration fees $8,400"]},
    {"label": "a: item 5 internal engineer salaries and lab supplies $145,000 - classification",
     "value": classification["5 Internal engineer salaries and lab supplies $145,000"]},
    {"label": "a: item 6 acquisition of competitor - classification",
     "value": classification["6 Acquisition of competitor"]},
    {"label": "a: item 6 goodwill recognized", "value": num(goodwill)},
    {"label": "a: item 7 patent defense fees $11,200 - classification",
     "value": classification["7 Successful patent defense fees $11,200"]},
    {"label": "a: item 7 effect on the patent's classification and subsequent measurement",
     "value": item7_effect},
    {"label": "a: item 8 two-year municipal license $24,000 - classification",
     "value": classification["8 Two-year municipal license $24,000"]},

    # c. Year-1 amortization schedule
    {"label": "c: Year-1 amortization - patent, original cost (56,000 / 7, full year)",
     "value": num(patent_base_amort)},
    {"label": "c: Year-1 amortization - patent defense costs (11,200 / 6.5 x 6/12)",
     "value": num(defense_amort)},
    {"label": "c: Year-1 amortization - patent, total", "value": num(patent_amort_total)},
    {"label": "c: Year-1 amortization - copyright (72,000 / 12)", "value": num(copyright_amort)},
    {"label": "c: Year-1 amortization - franchise (indefinite life, none)",
     "value": num(franchise_amort)},
    {"label": "c: Year-1 amortization - trade name (indefinite life, none)",
     "value": num(trade_name_amort)},
    {"label": "c: Year-1 amortization - license (24,000 / 2)", "value": num(license_amort)},
    {"label": "c: Year-1 amortization - goodwill (not amortized)", "value": num(goodwill_amort)},
    {"label": "c: Year-1 amortization expense - total", "value": num(total_amort)},

    # e. December 31, Year 1 carrying amounts
    {"label": "e: Dec 31 Year 1 carrying amount - patent (incl. defense costs)",
     "value": num(patent_cv)},
    {"label": "e: Dec 31 Year 1 carrying amount - copyright", "value": num(copyright_cv)},
    {"label": "e: Dec 31 Year 1 carrying amount - franchise", "value": num(franchise_cv)},
    {"label": "e: Dec 31 Year 1 carrying amount - trade name", "value": num(trade_name_cv)},
    {"label": "e: Dec 31 Year 1 carrying amount - license", "value": num(license_cv)},
    {"label": "e: Dec 31 Year 1 carrying amount - goodwill", "value": num(goodwill_cv)},
]

output = {
    "id": "agent_086#01",
    "rounding_convention": (
        "decimal.Decimal throughout; ROUND_HALF_UP to the cent applied per period "
        "(each period's amortization charge is rounded before posting, carrying "
        "amounts derived from the rounded charges). Straight-line, zero residual; "
        "no present-value factors in this item."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "US GAAP (ASC 350 / ASC 730 / ASC 805) per the course text. Item 5 R&D is "
        "expensed as incurred; item 4 external registration fees on an indefinite-life "
        "trade name are capitalized and not amortized, so the April 1 date is "
        "irrelevant. Item 7 successful-defense fees are added to the patent and "
        "amortized over the 6.5-year remaining useful life from July 1, giving "
        "11,200 / 6.5 x 6/12 = 861.54 in Year 1 (equivalently, the textbook's "
        "restate-and-amortize approach: 4,000 for Jan-Jun plus 63,200 / 6.5 x 0.5 = "
        "4,861.54 for Jul-Dec = 8,861.54, the same total). Amortization is credited "
        "directly to the asset accounts as in the text's Demo 13-2; using Accumulated "
        "Amortization contra accounts would give identical amounts."
    ),
}

print(json.dumps(output, indent=2))
