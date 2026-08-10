"""Solver for agent_381#02 — Lakeshore Fiber Optics Ltd., Year 1.

Rounding convention: all money computed with decimal.Decimal (never floats),
quantized to 2 decimal places using ROUND_HALF_UP; per-share amounts (EPS) also
ROUND_HALF_UP to 2 decimals (cents). Weighted-average share layers are carried
at full Decimal precision and quantized to whole shares with ROUND_HALF_UP.
Every figure is derived from the stated facts; nothing is hard-coded.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
S = Decimal("1")

def m(x):
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)

def sh(x):
    return Decimal(x).quantize(S, rounding=ROUND_HALF_UP)

def f(x):
    return float(x)

# ---------------- given facts ----------------
beg_common = Decimal("50000")
par_common = Decimal("1")
pfd_shares = Decimal("5000")
pfd_par = Decimal("100")
pfd_rate = Decimal("0.06")

apr_shares = Decimal("10000")
apr_price = Decimal("20")

jul_shares = Decimal("5000")
jul_cost = Decimal("22")

months_year = Decimal("12")
net_income = m("360000")

# ---------------- a. April 1 issuance ----------------
a_cash = m(apr_shares * apr_price)
a_cs = m(apr_shares * par_common)
a_apic = m(a_cash - a_cs)

# ---------------- b. July 1 treasury purchase ----------------
b_cost = m(jul_shares * jul_cost)

# ---------------- c. October 1 large stock dividend ----------------
out_before_div = beg_common + apr_shares - jul_shares          # 55,000
div_shares = out_before_div * Decimal("1.00")                  # 100% -> 1 new per share outstanding
c_capitalize = m(div_shares * par_common)
out_after_div = out_before_div + div_shares                    # 110,000

# ---------------- d. December 10 preferred dividend ----------------
d_pfd_div = m(pfd_shares * pfd_par * pfd_rate)                 # 30,000 (stated annual amount)

# ---------------- e. weighted-average shares (retroactive restatement) ----------------
restate = (out_before_div + div_shares) / out_before_div       # 2.0 factor for the 100% stock dividend
layers = [
    ("Jan 1 - Mar 31 (3 months)", beg_common, restate, Decimal("3")),
    ("Apr 1 - Jun 30 (3 months)", beg_common + apr_shares, restate, Decimal("3")),
    ("Jul 1 - Sep 30 (3 months)", out_before_div, restate, Decimal("3")),
    ("Oct 1 - Dec 31 (3 months)", out_after_div, Decimal("1"), Decimal("3")),
]
rows = []
wavg = Decimal("0")
for name, actual, fac, mo in layers:
    restated = actual * fac
    weighted = restated * mo / months_year
    wavg += weighted
    rows.append((name, actual, fac, restated, mo, weighted))
wavg = sh(wavg)

# ---------------- f. basic EPS ----------------
inc_to_common = m(net_income - d_pfd_div)
eps = (inc_to_common / wavg).quantize(C, rounding=ROUND_HALF_UP)

answers = [
    {"label": "a: April 1 issuance - Cash debit", "value": f(a_cash)},
    {"label": "a: April 1 issuance - Common Stock credit (par)", "value": f(a_cs)},
    {"label": "a: April 1 issuance - Paid-in Capital in Excess of Par credit", "value": f(a_apic)},
    {"label": "b: July 1 treasury stock cost (5,000 x $22)", "value": f(b_cost)},
    {"label": "c: Common shares outstanding immediately BEFORE the stock dividend", "value": f(out_before_div)},
    {"label": "c: Shares issued in the 100% stock dividend", "value": f(div_shares)},
    {"label": "c: Amount capitalized (par of shares issued)", "value": f(c_capitalize)},
    {"label": "c: Common shares outstanding immediately AFTER the stock dividend", "value": f(out_after_div)},
    {"label": "d: Preferred cash dividend declared and paid (5,000 x $100 x 6%)", "value": f(d_pfd_div)},
    {"label": "e: Retroactive restatement factor for periods before Oct 1", "value": f(restate)},
]
for name, actual, fac, restated, mo, weighted in rows:
    answers.append({"label": "e: " + name + " - actual shares outstanding", "value": f(actual)})
    answers.append({"label": "e: " + name + " - restatement factor", "value": f(fac)})
    answers.append({"label": "e: " + name + " - restated shares", "value": f(restated)})
    answers.append({"label": "e: " + name + " - weighted portion (x " + str(int(mo)) + "/12)", "value": f(weighted)})
answers += [
    {"label": "e: Weighted-average common shares outstanding for Year 1", "value": f(wavg)},
    {"label": "f: Net income", "value": f(net_income)},
    {"label": "f: Less preferred dividends declared (noncumulative)", "value": f(d_pfd_div)},
    {"label": "f: Income available to common shareholders", "value": f(inc_to_common)},
    {"label": "f: Weighted-average common shares", "value": f(wavg)},
    {"label": "f: Basic EPS", "value": f(eps)},
]

journal_entries = [
    {"part": "a", "lines": [
        {"account": "Cash", "debit": f(a_cash), "credit": 0},
        {"account": "Common Stock ($1 par)", "debit": 0, "credit": f(a_cs)},
        {"account": "Paid-in Capital in Excess of Par - Common", "debit": 0, "credit": f(a_apic)},
    ]},
    {"part": "b", "lines": [
        {"account": "Treasury Stock (cost method)", "debit": f(b_cost), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": f(b_cost)},
    ]},
    {"part": "c", "lines": [
        {"account": "Stock Dividends (Retained Earnings)", "debit": f(c_capitalize), "credit": 0},
        {"account": "Common Stock ($1 par)", "debit": 0, "credit": f(c_capitalize)},
    ]},
    {"part": "d", "lines": [
        {"account": "Cash Dividends - Preferred (Retained Earnings)", "debit": f(d_pfd_div), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": f(d_pfd_div)},
    ]},
]

for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, (je["part"], dr, cr)

notes = ("f explanation: The noncumulative preferred dividend is subtracted because it was "
         "DECLARED in Year 1, so that $30,000 of net income belongs to preferred holders and is "
         "not available to common (for a noncumulative issue, undeclared dividends would not be "
         "subtracted). The 100% stock dividend brings in no new resources and merely subdivides "
         "the existing ownership, so it is applied retroactively (x2) to all pre-October periods, "
         "whereas the April 1 cash issuance brought in $200,000 of new capital and is therefore "
         "weighted only from April 1 forward (9/12). Treasury shares are excluded from shares "
         "outstanding from July 1 on, and the stock dividend was distributed only on the 55,000 "
         "shares outstanding on October 1.")

print(json.dumps({
    "id": "agent_381#02",
    "rounding_convention": "decimal.Decimal throughout; money and per-share (EPS) amounts quantized to 2 decimals with ROUND_HALF_UP; share counts to whole shares with ROUND_HALF_UP",
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
