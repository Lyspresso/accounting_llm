"""Solver for agent_254#00 -- Meridian Cascade Holdings Inc., complex capital structure EPS.

ROUNDING CONVENTION: all money and per-share amounts use decimal.Decimal exclusively
(never floats). Dollar amounts are exact to the cent, quantized with ROUND_HALF_UP to
0.01. Per-share EPS figures reported on the face of the income statement and in the
sequential schedule are quantized with ROUND_HALF_UP to 0.01; "earnings per incremental
share" ranking metrics are quantized with ROUND_HALF_UP to 0.0001 for display only.
All dilution ordering / dilutive-vs-antidilutive comparisons are made on UNROUNDED
Decimal quotients so rounding never changes the sequencing decision. Rounding is applied
once per period (year ended December 31, Year 1), at presentation, not mid-computation.
Every figure is derived from the fact pattern; nothing is hard-coded.
"""
from decimal import Decimal as D, ROUND_HALF_UP, getcontext
import json

getcontext().prec = 40
C = D("0.01")
F = D("0.0001")
def c(x): return x.quantize(C, rounding=ROUND_HALF_UP)
def f4(x): return x.quantize(F, rounding=ROUND_HALF_UP)
def m(x): return float(c(x))

# ---------------- Given facts ----------------
NI          = D("380000")
WACSO       = D("200000")
TAX         = D("0.25")
PAR_COMMON  = D("1")

OPT_N       = D("10000")
OPT_EX      = D("20")
AVG_MKT     = D("40")

PS_SHARES   = D("4000")
PS_PAR      = D("100")
PS_RATE     = D("0.05")
PS_CONV     = D("3")

X_FACE      = D("500000")
X_RATE      = D("0.04")
X_CONV_PER_1000 = D("25")

Y_FACE      = D("300000")
Y_RATE      = D("0.10")
Y_CONV_PER_1000 = D("8")

BOND_UNIT   = D("1000")

# ---------------- (a) Initial recognition, Jan 1 Year 1 ----------------
ps_proceeds = PS_SHARES * PS_PAR              # issued at par -> no APIC
x_proceeds  = X_FACE                          # issued at par -> no premium/discount

# ---------------- (b) Numerator / denominator / per-incremental-share ----------------
# Options: treasury stock method; no numerator effect.
opt_proceeds   = OPT_N * OPT_EX
opt_reacquired = opt_proceeds / AVG_MKT
opt_den        = OPT_N - opt_reacquired
opt_num        = D("0")
opt_per        = opt_num / opt_den

# Cumulative convertible preferred: add back the dividend (no tax effect), add conv shares.
ps_div  = PS_SHARES * PS_PAR * PS_RATE
ps_num  = ps_div
ps_den  = PS_SHARES * PS_CONV
ps_per  = ps_num / ps_den

# Convertible bonds: add back after-tax interest, add conversion shares (if-converted).
x_int   = X_FACE * X_RATE
x_num   = x_int * (D("1") - TAX)
x_den   = (X_FACE / BOND_UNIT) * X_CONV_PER_1000
x_per   = x_num / x_den

y_int   = Y_FACE * Y_RATE
y_num   = y_int * (D("1") - TAX)
y_den   = (Y_FACE / BOND_UNIT) * Y_CONV_PER_1000
y_per   = y_num / y_den

secs = [
    ("Employee stock options (treasury stock method)", opt_num, opt_den, opt_per),
    ("5% cumulative convertible preferred stock",      ps_num,  ps_den,  ps_per),
    ("Series X convertible bonds (4%)",                x_num,   x_den,   x_per),
    ("Series Y convertible bonds (10%)",               y_num,   y_den,   y_per),
]
ranked = sorted(secs, key=lambda s: s[3])   # most dilutive = lowest earnings per incremental share

# ---------------- (c) Basic EPS ----------------
inc_avail = NI - ps_div
basic_eps = inc_avail / WACSO

# ---------------- (d) Sequential diluted EPS schedule ----------------
run_num, run_den = inc_avail, WACSO
prior = basic_eps
schedule = []
for name, n, d_, per in ranked:
    t_num, t_den = run_num + n, run_den + d_
    tent = t_num / t_den
    dil = tent < prior
    schedule.append({
        "security": name,
        "numerator_effect": m(n),
        "denominator_effect": float(d_),
        "cumulative_numerator": m(t_num),
        "cumulative_denominator": float(t_den),
        "tentative_eps": float(c(tent)),
        "status": "DILUTIVE -- include" if dil else "ANTIDILUTIVE -- exclude (stop)",
    })
    if dil:
        run_num, run_den, prior = t_num, t_den, tent
    else:
        break
diluted_eps = run_num / run_den

# ---------------- (e) Period-end JEs, Dec 31 Year 1 ----------------
# ps_div (declared + paid same day); x_int cash interest.

answers = [
 {"label":"a(1): Jan 1 -- Cash debited on convertible preferred stock issuance", "value": m(ps_proceeds)},
 {"label":"a(1): Jan 1 -- Preferred Stock ($100 par) credited (issued at par, no APIC)", "value": m(ps_proceeds)},
 {"label":"a(2): Jan 1 -- Cash debited on Series X convertible bond issuance", "value": m(x_proceeds)},
 {"label":"a(2): Jan 1 -- Bonds Payable, Series X credited (issued at par, no premium/discount)", "value": m(x_proceeds)},

 {"label":"b: Options -- numerator effect (no earnings adjustment)", "value": m(opt_num)},
 {"label":"b: Options -- denominator effect (incremental shares, treasury stock method)", "value": float(opt_den)},
 {"label":"b: Options -- earnings per incremental share", "value": float(f4(opt_per))},
 {"label":"b: Convertible preferred -- numerator effect (dividend add-back, no tax effect)", "value": m(ps_num)},
 {"label":"b: Convertible preferred -- denominator effect (4,000 x 3)", "value": float(ps_den)},
 {"label":"b: Convertible preferred -- earnings per incremental share", "value": float(f4(ps_per))},
 {"label":"b: Series X bonds -- numerator effect (after-tax interest add-back)", "value": m(x_num)},
 {"label":"b: Series X bonds -- denominator effect (500 bonds x 25)", "value": float(x_den)},
 {"label":"b: Series X bonds -- earnings per incremental share", "value": float(f4(x_per))},
 {"label":"b: Series Y bonds -- numerator effect (after-tax interest add-back)", "value": m(y_num)},
 {"label":"b: Series Y bonds -- denominator effect (300 bonds x 8)", "value": float(y_den)},
 {"label":"b: Series Y bonds -- earnings per incremental share", "value": float(f4(y_per))},
 {"label":"b: Ranking most dilutive -> least dilutive",
  "value": " > ".join("%d. %s ($%s/share)" % (i+1, s[0], f4(s[3])) for i, s in enumerate(ranked))},

 {"label":"c: Income available to common shareholders (numerator of basic EPS)", "value": m(inc_avail)},
 {"label":"c: Weighted-average common shares outstanding (denominator of basic EPS)", "value": float(WACSO)},
 {"label":"c: Basic EPS", "value": float(c(basic_eps))},
]
for i, st in enumerate(schedule, start=1):
    answers.append({"label":"d: Step %d -- add %s -- cumulative numerator" % (i, st["security"]),
                    "value": st["cumulative_numerator"]})
    answers.append({"label":"d: Step %d -- add %s -- cumulative denominator" % (i, st["security"]),
                    "value": st["cumulative_denominator"]})
    answers.append({"label":"d: Step %d -- add %s -- tentative EPS" % (i, st["security"]),
                    "value": st["tentative_eps"]})
    answers.append({"label":"d: Step %d -- %s -- classification" % (i, st["security"]),
                    "value": st["status"]})
answers += [
 {"label":"d: Diluted EPS numerator (final)", "value": m(run_num)},
 {"label":"d: Diluted EPS denominator (final)", "value": float(run_den)},
 {"label":"d: Diluted EPS", "value": float(c(diluted_eps))},

 {"label":"e(1): Dec 31 -- Retained Earnings (Preferred Dividends) debited", "value": m(ps_div)},
 {"label":"e(1): Dec 31 -- Cash credited for preferred dividend", "value": m(ps_div)},
 {"label":"e(2): Dec 31 -- Interest Expense debited, Series X full-year coupon", "value": m(x_int)},
 {"label":"e(2): Dec 31 -- Cash credited, Series X full-year coupon", "value": m(x_int)},

 {"label":"f: Face of income statement -- Earnings per common share -- Basic", "value": float(c(basic_eps))},
 {"label":"f: Face of income statement -- Earnings per common share -- Diluted", "value": float(c(diluted_eps))},
]

def je(part, lines):
    tot_d = sum(D(str(l[1])) for l in lines)
    tot_c = sum(D(str(l[2])) for l in lines)
    assert tot_d == tot_c, (part, tot_d, tot_c)
    return {"part": part, "lines": [{"account": a, "debit": float(dr), "credit": float(cr)} for a, dr, cr in lines]}

jes = [
 je("a(1) Jan 1, Year 1 -- issuance of 4,000 shares of 5% cumulative convertible preferred, $100 par, at par", [
    ("Cash", m(ps_proceeds), 0.0),
    ("Preferred Stock ($100 par, 5% cumulative convertible)", 0.0, m(ps_proceeds)),
 ]),
 je("a(2) Jan 1, Year 1 -- issuance of $500,000 face Series X 4% convertible bonds at par", [
    ("Cash", m(x_proceeds), 0.0),
    ("Bonds Payable -- Series X convertible", 0.0, m(x_proceeds)),
 ]),
 je("e(1) Dec 31, Year 1 -- annual preferred dividend declared and paid in cash", [
    ("Retained Earnings (Preferred Dividends)", m(ps_div), 0.0),
    ("Cash", 0.0, m(ps_div)),
 ]),
 je("e(2) Dec 31, Year 1 -- full-year cash interest on Series X bonds", [
    ("Interest Expense", m(x_int), 0.0),
    ("Cash", 0.0, m(x_int)),
 ]),
]

notes = (
 "US GAAP, complex capital structure (ASC 260). (a) Both securities were issued at par on 1/1/Yr1, so "
 "no APIC, premium, or discount arises; under US GAAP a conventional convertible bond is NOT bifurcated, "
 "so the full $%s is credited to Bonds Payable. (b) Options use the treasury stock method: proceeds "
 "$%s / $%s average market price = %s shares reacquired, leaving %s incremental shares with a $0 numerator "
 "effect, so options are always the most dilutive (earnings per incremental share = $0). The preferred is "
 "CUMULATIVE, so its $%s dividend is deducted in basic EPS whether or not declared (here it was declared and "
 "paid) and is added back on an if-converted basis with NO tax effect (dividends are not deductible). Bond "
 "interest is added back NET of the %s%% tax rate. (c) Basic EPS = ($%s - $%s) / %s = $%s. (d) Sequential "
 "if-converted schedule in rank order: options ($0.0000), Series X ($%s), preferred ($%s) are each dilutive; "
 "Series Y at $%s per incremental share raises tentative EPS above the running subtotal, so Series Y is "
 "ANTIDILUTIVE and is excluded -- and once one security is antidilutive in a properly ranked schedule, all "
 "remaining (less dilutive) securities are too. Diluted EPS = $%s / %s = $%s. (e) Because the dividend was "
 "declared and paid the same day, the declaration and payment are recorded in one entry (no Dividends Payable "
 "left outstanding); bonds issued at par carry no amortization, so cash interest equals interest expense. "
 "(f) ASC 260 requires dual presentation of basic and diluted EPS with equal prominence on the face of the "
 "income statement; there are no discontinued operations, so only income-from-continuing-operations/net-income "
 "EPS lines are presented."
) % (c(x_proceeds), c(opt_proceeds), c(AVG_MKT), opt_reacquired, opt_den, c(ps_div), (TAX*100).quantize(D("1")),
     c(NI), c(ps_div), WACSO, c(basic_eps), f4(x_per), f4(ps_per), f4(y_per), c(run_num), run_den, c(diluted_eps))

print(json.dumps({
  "id": "agent_254#00",
  "rounding_convention": ("decimal.Decimal only (no floats); ROUND_HALF_UP applied once per period at "
                          "presentation -- dollars to $0.01, EPS to $0.01, earnings-per-incremental-share to "
                          "$0.0001; all dilution ranking and dilutive/antidilutive tests performed on unrounded "
                          "Decimal quotients"),
  "answers": answers,
  "journal_entries": jes,
  "insufficient_info": False,
  "notes": notes,
}, indent=1))
