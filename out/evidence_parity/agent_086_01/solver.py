"""Solver for agent_086#01 -- Cedarline Robotics intangibles (LO 13-1).

Rounding convention: all money is decimal.Decimal; every amortization amount is
rounded to the cent with ROUND_HALF_UP once per period (per asset, per year),
never with floats. Carrying amounts are computed from rounded period amounts.
Every figure is derived from the scenario inputs; nothing is hard-coded.
"""
from decimal import Decimal, ROUND_HALF_UP
import json

C = Decimal("0.01")
def r(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def n(x):
    x = r(x)
    return int(x) if x == x.to_integral_value() else float(x)

# ---- scenario inputs -------------------------------------------------------
copyright_cost   = Decimal("72000");  copyright_life = Decimal("12")
franchise_cost   = Decimal("110000")
patent_cost      = Decimal("56000");  patent_life    = Decimal("7")
tradename_cost   = Decimal("8400")                      # April 1 registration fees
internal_dev     = Decimal("145000")                    # item 5
purchase_price   = Decimal("1250000"); fv_inas         = Decimal("980000")
defense_cost     = Decimal("11200")                     # July 1, added to patent
license_cost     = Decimal("24000");  license_life_yr = Decimal("2")
MONTHS = Decimal("12")

# ---- derived ---------------------------------------------------------------
goodwill = purchase_price - fv_inas

copyright_annual = r(copyright_cost / copyright_life)
patent_annual    = r(patent_cost / patent_life)
license_annual   = r(license_cost / license_life_yr)

# defense costs capitalized July 1 -> amortized over the patent's REMAINING
# useful life at that date (7 yrs - 6 months elapsed = 6.5 yrs), prorated 6/12.
defense_months_used   = Decimal("6")
patent_remaining_life = patent_life - defense_months_used / MONTHS      # 6.5 yrs
defense_annual = r(defense_cost / patent_remaining_life)
defense_yr1    = r(defense_cost / patent_remaining_life * (defense_months_used / MONTHS))

patent_total_yr1 = patent_annual + defense_yr1
total_amort = copyright_annual + patent_total_yr1 + license_annual

# ---- Dec 31 Yr 1 carrying amounts -----------------------------------------
cv_patent    = patent_cost + defense_cost - patent_total_yr1
cv_copyright = copyright_cost - copyright_annual
cv_franchise = franchise_cost                     # indefinite life: no amortization
cv_tradename = tradename_cost                     # indefinite life: no amortization
cv_license   = license_cost - license_annual
cv_goodwill  = goodwill                           # not amortized

answers = [
 {"label":"a: Item 1 copyright $72,000 - classification","value":"Finite-life intangible asset; amortize over the 12-year useful life (shorter than legal life)"},
 {"label":"a: Item 2 franchise $110,000 - classification","value":"Indefinite-life intangible asset (not goodwill); no amortization, test for impairment"},
 {"label":"a: Item 3 patent $56,000 - classification","value":"Finite-life intangible asset; amortize over the 7-year useful life (not the 14-year legal life)"},
 {"label":"a: Item 4 trade name registration legal fees $8,400 - classification","value":"Indefinite-life intangible asset; external registration costs are capitalized, no amortization"},
 {"label":"a: Item 5 internal engineer salaries and lab supplies $145,000 - classification","value":"Expense as incurred (internal research and development); not capitalized"},
 {"label":"a: Item 6 business combination - classification","value":"Goodwill (indefinite-life, not amortized); identifiable net assets recorded at fair value"},
 {"label":"a: Item 6 goodwill amount","value":n(goodwill)},
 {"label":"a: Item 7 successful defense costs $11,200 - classification and effect","value":"Capitalized to the patent (successful defense); the patent stays a FINITE-life intangible - classification unchanged. Subsequent measurement: the added cost is amortized over the patent's remaining useful life of 6.5 years from July 1, prorated 6/12 in Year 1"},
 {"label":"a: Item 8 two-year municipal license $24,000 - classification","value":"Finite-life intangible asset; amortize over the 2-year term"},

 {"label":"c: Copyright - cost","value":n(copyright_cost)},
 {"label":"c: Copyright - useful life (years)","value":12},
 {"label":"c: Copyright - Year 1 amortization (full year)","value":n(copyright_annual)},
 {"label":"c: Patent original cost - cost","value":n(patent_cost)},
 {"label":"c: Patent original cost - useful life (years)","value":7},
 {"label":"c: Patent original cost - Year 1 amortization (full year)","value":n(patent_annual)},
 {"label":"c: Patent defense costs (July 1) - cost","value":n(defense_cost)},
 {"label":"c: Patent defense costs - remaining useful life at July 1 (years)","value":float(patent_remaining_life)},
 {"label":"c: Patent defense costs - full-year amortization","value":n(defense_annual)},
 {"label":"c: Patent defense costs - months amortized in Year 1","value":int(defense_months_used)},
 {"label":"c: Patent defense costs - Year 1 amortization (6/12 prorated)","value":n(defense_yr1)},
 {"label":"c: Patent total Year 1 amortization","value":n(patent_total_yr1)},
 {"label":"c: License - cost","value":n(license_cost)},
 {"label":"c: License - useful life (years)","value":2},
 {"label":"c: License - Year 1 amortization (full year)","value":n(license_annual)},
 {"label":"c: Franchise - Year 1 amortization (indefinite life)","value":0},
 {"label":"c: Trade name - Year 1 amortization (indefinite life)","value":0},
 {"label":"c: Goodwill - Year 1 amortization (not amortized)","value":0},
 {"label":"c: Total Year 1 amortization expense","value":n(total_amort)},

 {"label":"e: Patent carrying amount 12/31 Yr 1 (incl. defense costs)","value":n(cv_patent)},
 {"label":"e: Copyright carrying amount 12/31 Yr 1","value":n(cv_copyright)},
 {"label":"e: Franchise carrying amount 12/31 Yr 1","value":n(cv_franchise)},
 {"label":"e: Trade name carrying amount 12/31 Yr 1","value":n(cv_tradename)},
 {"label":"e: License carrying amount 12/31 Yr 1","value":n(cv_license)},
 {"label":"e: Goodwill carrying amount 12/31 Yr 1","value":n(cv_goodwill)},
]

def je(part, lines):
    dr = sum(Decimal(str(l.get("debit",0))) for l in lines)
    cr = sum(Decimal(str(l.get("credit",0))) for l in lines)
    assert r(dr) == r(cr), (part, dr, cr)
    return {"part":part,"lines":lines}

def L(acct, dr=Decimal("0"), cr=Decimal("0")):
    return {"account":acct,"debit":n(dr),"credit":n(cr)}

jes = [
 je("b", [L("Copyright", dr=copyright_cost), L("Cash", cr=copyright_cost)]),
 je("b", [L("Franchise", dr=franchise_cost), L("Cash", cr=franchise_cost)]),
 je("b", [L("Patent", dr=patent_cost), L("Cash", cr=patent_cost)]),
 je("b", [L("Trade Name (Apr 1 registration legal fees)", dr=tradename_cost), L("Cash", cr=tradename_cost)]),
 je("b", [L("Research and Development Expense", dr=internal_dev), L("Cash / Salaries Payable / Supplies", cr=internal_dev)]),
 je("b", [L("Identifiable Net Assets Acquired (at fair value)", dr=fv_inas), L("Goodwill", dr=goodwill), L("Cash", cr=purchase_price)]),
 je("b", [L("Patent (July 1 successful defense costs)", dr=defense_cost), L("Cash", cr=defense_cost)]),
 je("b", [L("License", dr=license_cost), L("Cash", cr=license_cost)]),
 je("d", [L("Amortization Expense", dr=total_amort),
          L("Accumulated Amortization - Patent", cr=patent_total_yr1),
          L("Accumulated Amortization - Copyright", cr=copyright_annual),
          L("Accumulated Amortization - License", cr=license_annual)]),
]

out = {
 "id":"agent_086#01",
 "rounding_convention":"decimal.Decimal throughout; ROUND_HALF_UP to the nearest cent applied once per period per asset (annual/partial-year amortization), no floats",
 "answers":answers,
 "journal_entries":jes,
 "insufficient_info":False,
 "notes":"Item 7: successful-defense legal fees are capitalized to the patent, so the patent remains finite-life; the $11,200 is amortized over the patent's remaining useful life at July 1 (7.0 - 0.5 = 6.5 years) and prorated 6/12 in Year 1 = $861.54 (annual rate $1,723.08). Items 2, 4 and 6 (franchise, registered trade name, goodwill) are indefinite-life and are not amortized. Item 5 internal development costs of $145,000 are expensed. Total Year 1 amortization $26,861.54 = copyright $6,000 + patent $8,000 + defense $861.54 + license $12,000."
}
print(json.dumps(out, indent=1))
