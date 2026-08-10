#!/usr/bin/env python3
"""Solver for agent_254#00 - Meridian Cascade Holdings Inc., complex capital
structure: initial recognition JEs, dilutive-security ranking, basic EPS,
sequential diluted EPS schedule, period-end JEs, and EPS face presentation.

ROUNDING CONVENTION
-------------------
ROUND_HALF_UP throughout; no binary floats anywhere (decimal.Decimal only).

  * Money (cash, par, dividends, interest, tax effects) is exact to the cent;
    every figure in this fact pattern happens to land on whole dollars.
  * Per-share amounts (basic EPS, each tentative diluted EPS, final diluted
    EPS) are rounded ROUND_HALF_UP to 2 decimal places for *reporting and
    presentation* only.
  * Earnings per incremental share (the ranking metric) is rounded
    ROUND_HALF_UP to 4 decimal places for reporting.
  * DILUTIVE / ANTIDILUTIVE decisions and the ranking order are made on the
    UNROUNDED exact Decimal quotients, never on the rounded display values.
    This matters here: the tentative EPS after the Series X bonds
    (375,000 / 217,500 = 1.724137...) and after the preferred stock
    (395,000 / 229,500 = 1.721132...) both display as $1.72, but the exact
    values show the preferred stock still reduces EPS, so it is dilutive.
    Final diluted EPS is $1.72 either way.

METHOD (ASC 260)
----------------
  * Basic EPS = (Net income - current-year preferred dividends) / WACSO.
    The preferred is cumulative, so its dividend is deducted whether declared
    or not; here it was declared and paid.
  * Options: treasury stock method. Proceeds = options x exercise price;
    assumed treasury shares = proceeds / average market price; incremental
    shares = options - treasury shares. No numerator effect.
  * Convertible preferred: numerator effect = add back the preferred dividend
    (no tax effect - dividends are not deductible); denominator effect =
    shares issuable on conversion.
  * Convertible bonds: numerator effect = interest expense net of tax
    (coupon x face x (1 - tax rate), since issued at par so coupon = expense);
    denominator effect = shares issuable on conversion.
  * Securities are ranked by earnings per incremental share, lowest first
    (most dilutive), and folded into the schedule in that sequence. The first
    security that raises the running EPS is antidilutive; it and everything
    ranked after it are excluded (ASC 260-10-45-18).

Run:  python3 solver.py   -> prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")
TEN_THOU = Decimal("0.0001")


def money(x: Decimal) -> Decimal:
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def per_share(x: Decimal) -> Decimal:
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def ratio4(x: Decimal) -> Decimal:
    return x.quantize(TEN_THOU, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly plain number (int when integral)."""
    d = d.normalize()
    if d == d.to_integral_value():
        return int(d)
    return float(d)  # display only; all arithmetic above is Decimal


# ---------------------------------------------------------------- given facts
NET_INCOME = Decimal("380000")
WACSO = Decimal("200000")
TAX_RATE = Decimal("0.25")

# 1. Employee stock options
OPT_COUNT = Decimal("10000")
OPT_EXERCISE = Decimal("20")
AVG_MKT = Decimal("40")

# 2. 5% cumulative convertible preferred
PFD_SHARES = Decimal("4000")
PFD_PAR = Decimal("100")
PFD_RATE = Decimal("0.05")
PFD_CONV_RATIO = Decimal("3")

# 3. Series X convertible bonds
X_FACE = Decimal("500000")
X_COUPON = Decimal("0.04")
X_SHARES_PER_1000 = Decimal("25")

# 4. Series Y convertible bonds
Y_FACE = Decimal("300000")
Y_COUPON = Decimal("0.10")
Y_SHARES_PER_1000 = Decimal("8")

BOND_DENOM = Decimal("1000")

# ------------------------------------------------- a. initial recognition JEs
pfd_proceeds = money(PFD_SHARES * PFD_PAR)          # issued at par -> no APIC
x_proceeds = money(X_FACE)                          # issued at par

je_a = [
    {
        "part": "a(1)",
        "date": "Year 1, January 1",
        "description": "Issuance of 4,000 shares of 5% cumulative convertible "
                       "preferred stock, $100 par, at par",
        "lines": [
            {"account": "Cash", "debit": num(pfd_proceeds), "credit": 0},
            {"account": "Preferred stock", "debit": 0, "credit": num(pfd_proceeds)},
        ],
    },
    {
        "part": "a(2)",
        "date": "Year 1, January 1",
        "description": "Issuance of $500,000 face, 4% Series X convertible "
                       "bonds at par",
        "lines": [
            {"account": "Cash", "debit": num(x_proceeds), "credit": 0},
            {"account": "Bonds payable", "debit": 0, "credit": num(x_proceeds)},
        ],
    },
]

# --------------------------------------------- b. numerator/denominator effects
# Options - treasury stock method, no numerator effect.
opt_proceeds = money(OPT_COUNT * OPT_EXERCISE)
opt_treasury_shares = opt_proceeds / AVG_MKT
opt_incremental = OPT_COUNT - opt_treasury_shares
opt_numerator = Decimal("0")

# Convertible preferred - add back the preferred dividend (not tax affected).
pfd_dividend = money(PFD_SHARES * PFD_PAR * PFD_RATE)
pfd_incremental = PFD_SHARES * PFD_CONV_RATIO
pfd_numerator = pfd_dividend

# Convertible bonds - add back after-tax interest.
x_interest = money(X_FACE * X_COUPON)
x_numerator = money(x_interest * (Decimal("1") - TAX_RATE))
x_incremental = (X_FACE / BOND_DENOM) * X_SHARES_PER_1000

y_interest = money(Y_FACE * Y_COUPON)
y_numerator = money(y_interest * (Decimal("1") - TAX_RATE))
y_incremental = (Y_FACE / BOND_DENOM) * Y_SHARES_PER_1000

securities = [
    {"key": "options", "name": "Employee stock options",
     "numerator": opt_numerator, "denominator": opt_incremental},
    {"key": "preferred", "name": "5% cumulative convertible preferred stock",
     "numerator": pfd_numerator, "denominator": pfd_incremental},
    {"key": "series_x", "name": "Series X convertible bonds (4%)",
     "numerator": x_numerator, "denominator": x_incremental},
    {"key": "series_y", "name": "Series Y convertible bonds (10%)",
     "numerator": y_numerator, "denominator": y_incremental},
]

for s in securities:
    s["eps_per_incremental_exact"] = s["numerator"] / s["denominator"]

# Rank on the exact (unrounded) ratio, lowest = most dilutive.
ranked = sorted(securities, key=lambda s: s["eps_per_incremental_exact"])
for i, s in enumerate(ranked, start=1):
    s["rank"] = i

# ------------------------------------------------------------- c. basic EPS
basic_numerator = money(NET_INCOME - pfd_dividend)
basic_eps_exact = basic_numerator / WACSO
basic_eps = per_share(basic_eps_exact)

# ------------------------------- d. sequential diluted EPS schedule (exact cmp)
schedule = []
run_num = basic_numerator
run_den = WACSO
run_eps_exact = basic_eps_exact
antidilutive_reached = False

schedule.append({
    "step": "Basic EPS",
    "numerator": num(run_num),
    "denominator": num(run_den),
    "eps": num(per_share(run_eps_exact)),
    "status": "basic",
})

for s in ranked:
    if antidilutive_reached:
        schedule.append({
            "step": f"Effect of {s['name']}",
            "numerator": None,
            "denominator": None,
            "eps": None,
            "status": "antidilutive (excluded - ranked after the first "
                      "antidilutive security)",
        })
        s["dilutive"] = False
        continue

    trial_num = money(run_num + s["numerator"])
    trial_den = run_den + s["denominator"]
    trial_eps_exact = trial_num / trial_den

    is_dilutive = trial_eps_exact < run_eps_exact  # exact comparison
    s["dilutive"] = is_dilutive

    schedule.append({
        "step": f"Effect of {s['name']}",
        "add_to_numerator": num(s["numerator"]),
        "add_to_denominator": num(s["denominator"]),
        "numerator": num(trial_num),
        "denominator": num(trial_den),
        "eps": num(per_share(trial_eps_exact)),
        "status": "dilutive" if is_dilutive else "antidilutive (excluded)",
    })

    if is_dilutive:
        run_num, run_den, run_eps_exact = trial_num, trial_den, trial_eps_exact
    else:
        antidilutive_reached = True

diluted_eps = per_share(run_eps_exact)

schedule.append({
    "step": "Diluted EPS",
    "numerator": num(run_num),
    "denominator": num(run_den),
    "eps": num(diluted_eps),
    "status": "final",
})

# --------------------------------------------------- e. period-end JEs (12/31)
je_e = [
    {
        "part": "e(1)",
        "date": "Year 1, December 31",
        "description": "Annual 5% preferred dividend declared and paid in cash "
                       "the same day (4,000 sh x $100 par x 5%)",
        "lines": [
            {"account": "Retained earnings", "debit": num(pfd_dividend), "credit": 0},
            {"account": "Cash", "debit": 0, "credit": num(pfd_dividend)},
        ],
    },
    {
        "part": "e(2)",
        "date": "Year 1, December 31",
        "description": "Full-year cash interest on Series X convertible bonds "
                       "($500,000 x 4%); bonds issued at par so no amortization",
        "lines": [
            {"account": "Interest expense", "debit": num(x_interest), "credit": 0},
            {"account": "Cash", "debit": 0, "credit": num(x_interest)},
        ],
    },
]

journal_entries = je_a + je_e

# Debits must equal credits in every entry.
for je in journal_entries:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert d == c, f"Entry {je['part']} out of balance: {d} vs {c}"

# ---------------------------------------------------------------- f. face
presentation = {
    "caption": "Income statement (face) - year ended December 31, Year 1",
    "lines": [
        {"line": "Earnings per share - basic", "amount": num(basic_eps)},
        {"line": "Earnings per share - diluted", "amount": num(diluted_eps)},
    ],
    "note": "No discontinued operations, so net income is the only line "
            "requiring EPS presentation; income from continuing operations "
            "equals net income.",
}

# ---------------------------------------------------------------- answers
answers = []

# b - per security: numerator effect, denominator effect, EPS per incremental
#     share, and rank (1 = most dilutive).
for s in ranked:
    answers.append({
        "label": f"b: {s['name']} - numerator effect",
        "value": num(s["numerator"]),
    })
    answers.append({
        "label": f"b: {s['name']} - denominator effect (incremental shares)",
        "value": num(s["denominator"]),
    })
    answers.append({
        "label": f"b: {s['name']} - earnings per incremental share",
        "value": num(ratio4(s["eps_per_incremental_exact"])),
    })
    answers.append({
        "label": f"b: {s['name']} - rank (1 = most dilutive)",
        "value": s["rank"],
    })

# c - basic EPS
answers.append({"label": "c: basic EPS", "value": num(basic_eps)})

# d - diluted EPS
answers.append({"label": "d: diluted EPS", "value": num(diluted_eps)})

# f - face presentation amounts
answers.append({"label": "f: face of income statement - basic EPS",
                "value": num(basic_eps)})
answers.append({"label": "f: face of income statement - diluted EPS",
                "value": num(diluted_eps)})

ranking_text = " < ".join(
    f"{s['name']} (${ratio4(s['eps_per_incremental_exact'])})" for s in ranked
)
status_text = "; ".join(
    f"{s['name']}: {'dilutive' if s['dilutive'] else 'antidilutive'}"
    for s in ranked
)

out = {
    "id": "agent_254#00",
    "rounding_convention": (
        "decimal.Decimal only, ROUND_HALF_UP. Money exact to the cent; "
        "EPS (basic, each tentative diluted, final diluted) rounded to 2 "
        "decimals for reporting; earnings per incremental share rounded to 4 "
        "decimals for reporting. Ranking and dilutive/antidilutive tests use "
        "the unrounded exact quotients, not the rounded display values."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": (
        "Ranking most dilutive to least dilutive (earnings per incremental "
        f"share): {ranking_text}. Sequential schedule results: {status_text}. "
        "Series Y is antidilutive because adding $22,500 after-tax interest "
        "for only 2,400 shares raises EPS above the running $1.72, so it is "
        "excluded. Options carry no numerator effect (treasury stock method: "
        "$200,000 proceeds buy 5,000 shares at the $40 average price, leaving "
        "5,000 incremental shares). The preferred dividend is added back "
        "without a tax effect; bond interest is added back net of the 25% "
        "tax. Note the near-tie in the schedule: tentative EPS after Series X "
        "is 1.724138 and after the preferred is 1.721133 - both display as "
        "$1.72, but the exact comparison makes the preferred dilutive; final "
        "diluted EPS is $1.72 under either treatment."
    ),
    "schedule": schedule,
    "presentation": presentation,
}

print(json.dumps(out, indent=2))
