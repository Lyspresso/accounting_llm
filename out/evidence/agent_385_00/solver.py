#!/usr/bin/env python3
"""Blind solver for item agent_385#00 - Ironridge Analytics Corp. (LO 20-9).

Complex capital structure: initial recognition JEs, period-end adjusting JEs,
income finalization, ranking of dilutives by earnings per incremental share,
sequential diluted EPS with an antidilutive exclusion, closing entry, dual EPS
presentation, and post-period conversion settlement.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; no binary floats are used anywhere.

* Rounding mode is ROUND_HALF_UP, applied per period / per computed figure
  (this course's convention), never bankers' rounding.
* Dollar amounts in journal entries and schedules are exact to the cent here
  (every input is a whole-dollar face/par amount times a whole-percent rate),
  so they are quantized to 0.01 and carry no residual rounding error.
* Per-share figures (basic EPS, diluted EPS, and each security's earnings per
  incremental share) are quantized to the nearest cent, ROUND_HALF_UP, at the
  point of presentation.
* The dilutive/antidilutive sequencing test is performed on UNROUNDED
  (full-precision) EPS ratios and only then presented rounded, so a security is
  never misclassified by a presentation-level rounding tie. Both the rounded and
  unrounded comparisons agree for every step of this fact pattern.
* Interest is simple annual interest on bonds issued at par on Jan 1 and
  outstanding the entire year, so there is no amortization and no partial
  period; one full-year accrual per series.

Run:  python3 solver.py   -> prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")
ITEM_ID = "agent_385#00"


def money(x: Decimal) -> Decimal:
    """Quantize a dollar amount to the cent, ROUND_HALF_UP."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def per_share(x: Decimal) -> Decimal:
    """Quantize a per-share amount to the nearest cent, ROUND_HALF_UP."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly number: int when integral, else float of the exact Decimal."""
    x = Decimal(x)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------------------
# Given fact pattern (from the stem only)
# ---------------------------------------------------------------------------

# Common stock
COMMON_SHARES = Decimal("120000")
COMMON_PAR = Decimal("2")
COMMON_ISSUE_PRICE = Decimal("15")

# Convertible preferred: 6%, $100 par, cumulative; 3 common per preferred share
PFD_SHARES = Decimal("4000")
PFD_PAR = Decimal("100")
PFD_RATE = Decimal("0.06")
PFD_ISSUE_PRICE = Decimal("105")
PFD_CONV_RATIO = Decimal("3")

# Series B convertible bonds: $500,000 face, 5%, at par, 40 common per $1,000
SB_FACE = Decimal("500000")
SB_RATE = Decimal("0.05")
SB_SHARES_PER_1000 = Decimal("40")

# Series A convertible bonds: $300,000 face, 7%, at par, 20 common per $1,000
SA_FACE = Decimal("300000")
SA_RATE = Decimal("0.07")
SA_SHARES_PER_1000 = Decimal("20")

# Employee stock options
OPT_COUNT = Decimal("3000")
OPT_EXERCISE = Decimal("10")
OPT_AVG_MARKET = Decimal("15")

TAX_RATE = Decimal("0.20")
PRETAX_BEFORE_AJE = Decimal("480000")  # excludes bond interest and income tax

BOND_DENOM = Decimal("1000")


# ---------------------------------------------------------------------------
# (a) January 1, Year 1 initial recognition
# ---------------------------------------------------------------------------

common_cash = money(COMMON_SHARES * COMMON_ISSUE_PRICE)
common_par_total = money(COMMON_SHARES * COMMON_PAR)
common_apic = money(common_cash - common_par_total)

pfd_cash = money(PFD_SHARES * PFD_ISSUE_PRICE)
pfd_par_total = money(PFD_SHARES * PFD_PAR)
pfd_apic = money(pfd_cash - pfd_par_total)

sb_cash = money(SB_FACE)  # issued at par
sa_cash = money(SA_FACE)  # issued at par

entry_a1 = {
    "part": "a1",
    "description": "Jan 1, Year 1 - issue 120,000 shares of $2 par common at $15 cash",
    "lines": [
        {"account": "Cash", "debit": num(common_cash), "credit": 0},
        {"account": "Common Stock", "debit": 0, "credit": num(common_par_total)},
        {"account": "Paid-in Capital in Excess of Par - Common",
         "debit": 0, "credit": num(common_apic)},
    ],
}

entry_a2 = {
    "part": "a2",
    "description": ("Jan 1, Year 1 - issue 4,000 shares of 6%, $100 par cumulative "
                    "convertible preferred at $105 cash"),
    "lines": [
        {"account": "Cash", "debit": num(pfd_cash), "credit": 0},
        {"account": "Preferred Stock", "debit": 0, "credit": num(pfd_par_total)},
        {"account": "Paid-in Capital in Excess of Par - Preferred",
         "debit": 0, "credit": num(pfd_apic)},
    ],
}

entry_a3 = {
    "part": "a3",
    "description": "Jan 1, Year 1 - issue $500,000 face of 5% Series B convertible bonds at par",
    "lines": [
        {"account": "Cash", "debit": num(sb_cash), "credit": 0},
        {"account": "Bonds Payable - Series B", "debit": 0, "credit": num(sb_cash)},
    ],
}

entry_a4 = {
    "part": "a4",
    "description": "Jan 1, Year 1 - issue $300,000 face of 7% Series A convertible bonds at par",
    "lines": [
        {"account": "Cash", "debit": num(sa_cash), "credit": 0},
        {"account": "Bonds Payable - Series A", "debit": 0, "credit": num(sa_cash)},
    ],
}


# ---------------------------------------------------------------------------
# (b) December 31, Year 1 period-end adjusting entries  [EMPHASIS]
# ---------------------------------------------------------------------------

sb_interest = money(SB_FACE * SB_RATE)          # 500,000 x 5%
sa_interest = money(SA_FACE * SA_RATE)          # 300,000 x 7%
total_interest = money(sb_interest + sa_interest)

pretax_income = money(PRETAX_BEFORE_AJE - total_interest)
income_tax = money(pretax_income * TAX_RATE)
net_income = money(pretax_income - income_tax)

pfd_dividend = money(PFD_SHARES * PFD_PAR * PFD_RATE)   # full Year 1 cumulative claim
income_avail_common = money(net_income - pfd_dividend)

entry_b1 = {
    "part": "b1",
    "description": "Dec 31, Year 1 - accrue Year 1 interest on Series B bonds (500,000 x 5%)",
    "lines": [
        {"account": "Interest Expense", "debit": num(sb_interest), "credit": 0},
        {"account": "Interest Payable", "debit": 0, "credit": num(sb_interest)},
    ],
}

entry_b2 = {
    "part": "b2",
    "description": "Dec 31, Year 1 - accrue Year 1 interest on Series A bonds (300,000 x 7%)",
    "lines": [
        {"account": "Interest Expense", "debit": num(sa_interest), "credit": 0},
        {"account": "Interest Payable", "debit": 0, "credit": num(sa_interest)},
    ],
}

entry_b3 = {
    "part": "b3",
    "description": "Dec 31, Year 1 - record Year 1 income tax (434,000 x 20%)",
    "lines": [
        {"account": "Income Tax Expense", "debit": num(income_tax), "credit": 0},
        {"account": "Income Taxes Payable", "debit": 0, "credit": num(income_tax)},
    ],
}

entry_b4 = {
    "part": "b4",
    "description": ("Dec 31, Year 1 - declare full Year 1 cumulative preferred dividend "
                    "(4,000 x $100 x 6%)"),
    "lines": [
        {"account": "Retained Earnings", "debit": num(pfd_dividend), "credit": 0},
        {"account": "Dividends Payable - Preferred", "debit": 0, "credit": num(pfd_dividend)},
    ],
}


# ---------------------------------------------------------------------------
# (d) Ranking of potentially dilutive securities by earnings per incremental share
# ---------------------------------------------------------------------------

# Incremental shares
opt_proceeds = money(OPT_COUNT * OPT_EXERCISE)
opt_treasury_shares = opt_proceeds / OPT_AVG_MARKET               # 30,000 / 15 = 2,000
opt_incremental = OPT_COUNT - opt_treasury_shares                 # 3,000 - 2,000 = 1,000

sb_incremental = (SB_FACE / BOND_DENOM) * SB_SHARES_PER_1000      # 500 x 40 = 20,000
sa_incremental = (SA_FACE / BOND_DENOM) * SA_SHARES_PER_1000      # 300 x 20 = 6,000
pfd_incremental = PFD_SHARES * PFD_CONV_RATIO                     # 4,000 x 3 = 12,000

# Numerator effects
opt_numerator = Decimal("0")
sb_numerator = money(sb_interest * (Decimal("1") - TAX_RATE))     # after-tax interest saved
sa_numerator = money(sa_interest * (Decimal("1") - TAX_RATE))
pfd_numerator = pfd_dividend                                      # dividend no longer deducted

candidates = [
    {"security": "Employee stock options (treasury stock method)",
     "numerator_effect": opt_numerator, "incremental_shares": opt_incremental},
    {"security": "Series B convertible bonds (5%)",
     "numerator_effect": sb_numerator, "incremental_shares": sb_incremental},
    {"security": "Convertible preferred stock (6% cumulative)",
     "numerator_effect": pfd_numerator, "incremental_shares": pfd_incremental},
    {"security": "Series A convertible bonds (7%)",
     "numerator_effect": sa_numerator, "incremental_shares": sa_incremental},
]

for c in candidates:
    c["ratio_exact"] = c["numerator_effect"] / c["incremental_shares"]

# Most dilutive (lowest earnings per incremental share) first.
ranked = sorted(candidates, key=lambda c: c["ratio_exact"])


# ---------------------------------------------------------------------------
# (e) Sequential diluted EPS schedule
# ---------------------------------------------------------------------------

basic_eps_exact = income_avail_common / COMMON_SHARES
basic_eps = per_share(basic_eps_exact)

schedule = [{
    "step": "Basic EPS",
    "numerator": income_avail_common,
    "denominator": COMMON_SHARES,
    "eps_exact": basic_eps_exact,
    "eps": basic_eps,
    "status": "basic",
}]

running_num = income_avail_common
running_den = COMMON_SHARES
running_eps_exact = basic_eps_exact

for c in ranked:
    trial_num = money(running_num + c["numerator_effect"])
    trial_den = running_den + c["incremental_shares"]
    trial_eps_exact = trial_num / trial_den
    dilutive = trial_eps_exact < running_eps_exact
    schedule.append({
        "step": c["security"],
        "numerator": trial_num,
        "denominator": trial_den,
        "eps_exact": trial_eps_exact,
        "eps": per_share(trial_eps_exact),
        "status": "dilutive" if dilutive else "antidilutive - excluded",
    })
    if dilutive:
        running_num, running_den, running_eps_exact = trial_num, trial_den, trial_eps_exact

diluted_eps = per_share(running_eps_exact)
antidilutive = [row["step"] for row in schedule if row["status"].startswith("antidilutive")]


# ---------------------------------------------------------------------------
# (f) December 31, Year 1 closing entry
# ---------------------------------------------------------------------------

entry_f = {
    "part": "f",
    "description": "Dec 31, Year 1 - close net income to retained earnings",
    "lines": [
        {"account": "Income Summary", "debit": num(net_income), "credit": 0},
        {"account": "Retained Earnings", "debit": 0, "credit": num(net_income)},
    ],
}


# ---------------------------------------------------------------------------
# (h) January 8, Year 2 settlement (conversion) of Series B bonds - book value method
# ---------------------------------------------------------------------------

sb_conv_shares = sb_incremental                              # 20,000 common shares
sb_conv_par = money(sb_conv_shares * COMMON_PAR)             # 20,000 x $2 = 40,000
sb_carrying = money(SB_FACE)                                 # issued at par, no premium/discount
sb_conv_apic = money(sb_carrying - sb_conv_par)

entry_h = {
    "part": "h",
    "description": ("Jan 8, Year 2 - all Series B bondholders convert $500,000 of bonds into "
                    "20,000 common shares (book value method)"),
    "lines": [
        {"account": "Bonds Payable - Series B", "debit": num(sb_carrying), "credit": 0},
        {"account": "Common Stock", "debit": 0, "credit": num(sb_conv_par)},
        {"account": "Paid-in Capital in Excess of Par - Common",
         "debit": 0, "credit": num(sb_conv_apic)},
    ],
}


# ---------------------------------------------------------------------------
# Assemble output
# ---------------------------------------------------------------------------

journal_entries = [entry_a1, entry_a2, entry_a3, entry_a4,
                   entry_b1, entry_b2, entry_b3, entry_b4,
                   entry_f, entry_h]

# Self-check: every entry must balance.
for e in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in e["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in e["lines"])
    assert dr == cr, f"Entry {e['part']} does not balance: Dr {dr} vs Cr {cr}"

answers = [
    # (c) income-finalization schedule endpoints
    {"label": "c: Year 1 net income", "value": num(net_income)},
    {"label": "c: Year 1 income available to common stockholders",
     "value": num(income_avail_common)},
]

# (d) ranking schedule - numerator effect, incremental shares, ratio, in rank order
for i, c in enumerate(ranked, start=1):
    answers.append({
        "label": f"d: rank {i} - {c['security']} - numerator effect",
        "value": num(money(c["numerator_effect"])),
    })
    answers.append({
        "label": f"d: rank {i} - {c['security']} - incremental shares",
        "value": num(c["incremental_shares"]),
    })
    answers.append({
        "label": f"d: rank {i} - {c['security']} - earnings per incremental share",
        "value": num(per_share(c["ratio_exact"])),
    })

# (e) sequential diluted EPS schedule rows
for row in schedule:
    answers.append({
        "label": f"e: sequential schedule - {row['step']} - cumulative EPS ({row['status']})",
        "value": num(row["eps"]),
    })

answers.append({"label": "e/g: Year 1 basic EPS", "value": num(basic_eps)})
answers.append({"label": "e/g: Year 1 diluted EPS", "value": num(diluted_eps)})
answers.append({
    "label": "g: antidilutive security excluded from diluted EPS and disclosed",
    "value": "; ".join(antidilutive) if antidilutive else "none",
})

output = {
    "id": ITEM_ID,
    "rounding_convention": (
        "decimal.Decimal only, ROUND_HALF_UP per period/per figure. Dollar amounts "
        "quantized to $0.01 (all exact here); per-share amounts quantized to the "
        "nearest cent at presentation. Dilutive/antidilutive sequencing tested on "
        "unrounded EPS ratios. Bonds issued at par on Jan 1 and held all year, so "
        "simple full-year interest with no amortization."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Ranking by earnings per incremental share (most to least dilutive): options $0.00 "
        "(0 / 1,000 incremental shares under the treasury stock method: 3,000 options less "
        "3,000 x $10 / $15 = 2,000 treasury shares); Series B bonds $1.00 (20,000 after-tax "
        "interest / 20,000 shares); convertible preferred $2.00 (24,000 / 12,000 shares); "
        "Series A bonds $2.80 (16,800 after-tax interest / 6,000 shares). Adding Series A "
        "last raises EPS from 2.40 to 2.4151, so Series A convertible bonds are antidilutive, "
        "are excluded from diluted EPS, and are disclosed as such (part g). Part b4 debits "
        "Retained Earnings for the declared cumulative preferred dividend; a Dividends "
        "Declared account closed to Retained Earnings is equivalent. Part h uses the book "
        "value method, the course convention for convertible bond conversions."
    ),
}

print(json.dumps(output, indent=2))
