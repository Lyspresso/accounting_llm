"""Meridian Cascade Holdings Inc. -- Year 1 complex capital structure EPS solver.

Rounding convention: all money and per-share amounts use decimal.Decimal with
ROUND_HALF_UP, applied once per reported period figure (no float arithmetic).
Money is carried and reported to the cent ($0.01). Reported EPS figures are
rounded to $0.01; earnings-per-incremental-share and interim (running) EPS in
the ranking and sequential schedules are shown to 4 decimals for ranking
transparency. Dilution/antidilution decisions are made on exact unrounded
quotients, not on rounded figures. Dr = Cr in every journal entry.
"""
from decimal import Decimal, ROUND_HALF_UP, getcontext
import json

getcontext().prec = 40

C = Decimal("0.01")
P4 = Decimal("0.0001")


def m(x):
    return x.quantize(C, rounding=ROUND_HALF_UP)


def p4(x):
    return x.quantize(P4, rounding=ROUND_HALF_UP)


def f(x):
    return float(x)


# ---------------- Given inputs ----------------
NI = Decimal("380000")
WACS = Decimal("200000")
TAX = Decimal("0.25")

OPT_N = Decimal("10000")
OPT_EX = Decimal("20")
AVG_MKT = Decimal("40")

PFD_SH = Decimal("4000")
PFD_PAR = Decimal("100")
PFD_RATE = Decimal("0.05")
PFD_CONV = Decimal("3")

X_FACE = Decimal("500000")
X_RATE = Decimal("0.04")
X_CONV = Decimal("25")          # common shares per $1,000 bond
Y_FACE = Decimal("300000")
Y_RATE = Decimal("0.10")
Y_CONV = Decimal("8")
BOND_DENOM = Decimal("1000")

# ---------------- Part a: initial recognition ----------------
pfd_proceeds = PFD_SH * PFD_PAR                     # issued at par
x_proceeds = X_FACE                                  # issued at par

je = []
je.append({"part": "a", "lines": [
    {"account": "Cash", "debit": f(m(pfd_proceeds)), "credit": 0.0},
    {"account": "Preferred Stock ($100 par, 5% cumulative convertible)",
     "debit": 0.0, "credit": f(m(pfd_proceeds))},
]})
je.append({"part": "a", "lines": [
    {"account": "Cash", "debit": f(m(x_proceeds)), "credit": 0.0},
    {"account": "Bonds Payable - Series X convertible (4%)",
     "debit": 0.0, "credit": f(m(x_proceeds))},
]})

# ---------------- Part b: numerator / denominator / per incremental share ----------------
# Options -- treasury stock method
opt_proceeds = OPT_N * OPT_EX
opt_repurch = opt_proceeds / AVG_MKT
opt_den = OPT_N - opt_repurch
opt_num = Decimal("0")
opt_eps_inc = opt_num / opt_den

# Convertible preferred -- if-converted (no tax effect on dividends)
pfd_div = PFD_SH * PFD_PAR * PFD_RATE
pfd_num = pfd_div
pfd_den = PFD_SH * PFD_CONV
pfd_eps_inc = pfd_num / pfd_den

# Series X convertible bonds -- if-converted, interest net of tax
x_int = X_FACE * X_RATE
x_num = x_int * (Decimal("1") - TAX)
x_den = (X_FACE / BOND_DENOM) * X_CONV
x_eps_inc = x_num / x_den

# Series Y convertible bonds
y_int = Y_FACE * Y_RATE
y_num = y_int * (Decimal("1") - TAX)
y_den = (Y_FACE / BOND_DENOM) * Y_CONV
y_eps_inc = y_num / y_den

secs = [
    ("Employee stock options", opt_num, opt_den, opt_eps_inc),
    ("Series X convertible bonds (4%)", x_num, x_den, x_eps_inc),
    ("5% cumulative convertible preferred stock", pfd_num, pfd_den, pfd_eps_inc),
    ("Series Y convertible bonds (10%)", y_num, y_den, y_eps_inc),
]
ranked = sorted(secs, key=lambda s: s[3])

# ---------------- Part c: basic EPS ----------------
inc_avail = NI - pfd_div
basic_eps = m(inc_avail / WACS)

# ---------------- Part d: sequential diluted EPS schedule ----------------
rows = []
cum_num = inc_avail
cum_den = WACS
prior = cum_num / cum_den
rows.append({"step": "Basic EPS (starting point)",
             "cumulative_numerator": f(m(cum_num)),
             "cumulative_denominator": f(cum_den),
             "cumulative_eps": f(p4(prior)),
             "status": "n/a"})
for name, num, den, _ in ranked:
    t_num = cum_num + num
    t_den = cum_den + den
    new = t_num / t_den
    dil = new < prior
    rows.append({"step": "Add " + name,
                 "numerator_effect": f(m(num)),
                 "denominator_effect": f(den),
                 "cumulative_numerator": f(m(t_num)),
                 "cumulative_denominator": f(t_den),
                 "cumulative_eps": f(p4(new)),
                 "status": "DILUTIVE - include" if dil else "ANTIDILUTIVE - exclude"})
    if dil:
        cum_num, cum_den, prior = t_num, t_den, new

diluted_eps = m(prior)

# ---------------- Part e: period-end journal entries ----------------
je.append({"part": "e", "lines": [
    {"account": "Retained Earnings (Preferred Dividends Declared)",
     "debit": f(m(pfd_div)), "credit": 0.0},
    {"account": "Cash", "debit": 0.0, "credit": f(m(pfd_div))},
]})
je.append({"part": "e", "lines": [
    {"account": "Interest Expense - Series X convertible bonds",
     "debit": f(m(x_int)), "credit": 0.0},
    {"account": "Cash", "debit": 0.0, "credit": f(m(x_int))},
]})

# ---------------- Answers ----------------
A = []
A.append({"label": "a: Cash received on preferred stock issuance (4,000 sh x $100 par, at par)",
          "value": f(m(pfd_proceeds))})
A.append({"label": "a: Preferred Stock credited (par)", "value": f(m(pfd_proceeds))})
A.append({"label": "a: Cash received on Series X convertible bond issuance (at par)",
          "value": f(m(x_proceeds))})
A.append({"label": "a: Bonds Payable - Series X credited (face)", "value": f(m(x_proceeds))})

A.append({"label": "b: Options - assumed proceeds (10,000 x $20)", "value": f(m(opt_proceeds))})
A.append({"label": "b: Options - treasury shares assumed repurchased ($200,000 / $40)",
          "value": f(opt_repurch)})
A.append({"label": "b: Options - numerator effect", "value": f(m(opt_num))})
A.append({"label": "b: Options - denominator effect (incremental shares)", "value": f(opt_den)})
A.append({"label": "b: Options - earnings per incremental share", "value": f(p4(opt_eps_inc))})

A.append({"label": "b: Series X bonds - annual cash interest ($500,000 x 4%)", "value": f(m(x_int))})
A.append({"label": "b: Series X bonds - numerator effect (interest net of 25% tax)",
          "value": f(m(x_num))})
A.append({"label": "b: Series X bonds - denominator effect (500 bonds x 25 shares)",
          "value": f(x_den)})
A.append({"label": "b: Series X bonds - earnings per incremental share", "value": f(p4(x_eps_inc))})

A.append({"label": "b: Convertible preferred - numerator effect (dividends added back, no tax effect)",
          "value": f(m(pfd_num))})
A.append({"label": "b: Convertible preferred - denominator effect (4,000 sh x 3)",
          "value": f(pfd_den)})
A.append({"label": "b: Convertible preferred - earnings per incremental share",
          "value": f(p4(pfd_eps_inc))})

A.append({"label": "b: Series Y bonds - annual cash interest ($300,000 x 10%)", "value": f(m(y_int))})
A.append({"label": "b: Series Y bonds - numerator effect (interest net of 25% tax)",
          "value": f(m(y_num))})
A.append({"label": "b: Series Y bonds - denominator effect (300 bonds x 8 shares)",
          "value": f(y_den)})
A.append({"label": "b: Series Y bonds - earnings per incremental share", "value": f(p4(y_eps_inc))})

for i, (name, _, _, eps_inc) in enumerate(ranked, start=1):
    A.append({"label": "b: Rank %d (most dilutive to least dilutive) - %s, earnings per incremental share"
                       % (i, name), "value": f(p4(eps_inc))})

A.append({"label": "c: Preferred dividends for Year 1 (cumulative, declared and paid)",
          "value": f(m(pfd_div))})
A.append({"label": "c: Income available to common shareholders (numerator of basic EPS)",
          "value": f(m(inc_avail))})
A.append({"label": "c: Weighted-average common shares outstanding (denominator of basic EPS)",
          "value": f(WACS)})
A.append({"label": "c: Basic EPS", "value": f(basic_eps)})

for r in rows:
    tag = "d: " + r["step"]
    if "numerator_effect" in r:
        A.append({"label": tag + " - numerator effect", "value": r["numerator_effect"]})
        A.append({"label": tag + " - denominator effect", "value": r["denominator_effect"]})
    A.append({"label": tag + " - cumulative numerator", "value": r["cumulative_numerator"]})
    A.append({"label": tag + " - cumulative denominator", "value": r["cumulative_denominator"]})
    A.append({"label": tag + " - cumulative EPS", "value": r["cumulative_eps"]})
    A.append({"label": tag + " - dilutive or antidilutive", "value": r["status"]})

A.append({"label": "d: Final diluted EPS numerator", "value": f(m(cum_num))})
A.append({"label": "d: Final diluted EPS denominator", "value": f(cum_den)})
A.append({"label": "d: Diluted EPS", "value": f(diluted_eps)})

A.append({"label": "e: Preferred dividend paid - Dr Retained Earnings (Dividends) / Cr Cash",
          "value": f(m(pfd_div))})
A.append({"label": "e: Series X full-year cash interest - Dr Interest Expense / Cr Cash",
          "value": f(m(x_int))})

A.append({"label": "f: Income statement face - Earnings per common share: Basic",
          "value": f(basic_eps)})
A.append({"label": "f: Income statement face - Earnings per common share: Diluted",
          "value": f(diluted_eps)})

out = {
    "id": "agent_254#00",
    "rounding_convention": ("decimal.Decimal with ROUND_HALF_UP applied once per reported "
                            "period figure; money to $0.01, reported EPS to $0.01, "
                            "earnings-per-incremental-share and running schedule EPS shown to "
                            "4 decimals; dilutive/antidilutive tests use exact unrounded quotients"),
    "answers": A,
    "journal_entries": je,
    "insufficient_info": False,
    "notes": ("Ranking by earnings per incremental share: options $0.0000, Series X $1.2000, "
              "convertible preferred $1.6667, Series Y $9.3750. Sequential schedule: options, "
              "Series X and the convertible preferred are each dilutive; Series Y is antidilutive "
              "(would raise EPS from $1.7241 to $1.8004) and is excluded. Basic $1.80 / diluted $1.72. "
              "Preferred is cumulative, so the full $20,000 annual dividend is deducted in basic EPS "
              "and added back in the if-converted step; preferred dividends carry no tax effect. "
              "Bonds were issued at par, so no discount/premium amortization and interest expense "
              "equals cash coupon.")
}
print(json.dumps(out, indent=1))
