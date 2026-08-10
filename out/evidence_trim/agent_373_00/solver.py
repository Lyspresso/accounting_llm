"""SummitRidge Packaging Corp. -- stock dividends and stock split (LO 19-6).

Rounding convention: all money is decimal.Decimal, quantized to cents
(0.01) using ROUND_HALF_UP at each period/measurement point. Share counts
are exact integers (whole shares only; no fractional shares). No figure is
hard-coded except the stated facts of the problem; everything else derived.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def m(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def f(x):
    return float(m(x))


# ---------------- Given facts (Dec 15, Year 1) ----------------
par = m("3")
shares0 = 60000
cs0 = m(par * shares0)                 # 180,000
pic0 = m("540000")
re0 = m("750000")
tse0 = m(cs0 + pic0 + re0)             # 1,470,000 (ties to given total)
mkt = m("22")

# ---------------- Scenario A: 12% small stock dividend ----------------
rate_a = Decimal("0.12")
sh_a = int(Decimal(shares0) * rate_a)          # 7,200 whole shares
fv_a = m(Decimal(sh_a) * mkt)                  # measured at fair value
par_a = m(Decimal(sh_a) * par)                 # credited to CSDD
pic_a = m(fv_a - par_a)                        # excess to PIC

# (c) schedule
# (1) before declaration
s1 = dict(cs=cs0, csdd=m(0), pic=pic0, re=re0, tot=tse0, sh=shares0, par=par)
# (2) Dec 31 Y1: declared, not distributed
cs2, csdd2 = cs0, par_a
pic2 = m(pic0 + pic_a)
re2 = m(re0 - fv_a)
s2 = dict(cs=cs2, csdd=csdd2, pic=pic2, re=re2,
          tot=m(cs2 + csdd2 + pic2 + re2), sh=shares0, par=par)
# (3) after distribution Jan 12 Y2
cs3 = m(cs2 + csdd2)
s3 = dict(cs=cs3, csdd=m(0), pic=pic2, re=re2,
          tot=m(cs3 + pic2 + re2), sh=shares0 + sh_a, par=par)

# ---------------- Scenario B: 50% large stock dividend ----------------
rate_b = Decimal("0.50")
sh_b = int(Decimal(shares0) * rate_b)          # 30,000 shares
amt_b = m(Decimal(sh_b) * par)                 # measured at PAR, not market
cs_b_end = m(cs0 + amt_b)
pic_b_end = pic0                               # unchanged
re_b_end = m(re0 - amt_b)
sh_b_end = shares0 + sh_b
tot_b_end = m(cs_b_end + pic_b_end + re_b_end)

# ---------------- Scenario C: 2-for-1 true split ----------------
split = 2
sh_c = shares0 * split
par_c = (par / Decimal(split)).quantize(CENT, rounding=ROUND_HALF_UP)
cs_c = m(par_c * sh_c)                         # total CS unchanged

answers = [
    {"label": "a: Scenario A - shares in 12% small stock dividend", "value": sh_a},
    {"label": "a: Scenario A - Dr Retained Earnings (7,200 sh x $22 FV)", "value": f(fv_a)},
    {"label": "a: Scenario A - Cr Common Stock Dividends Distributable (at $3 par)", "value": f(par_a)},
    {"label": "a: Scenario A - Cr Paid-in Capital in Excess of Par-Common", "value": f(pic_a)},
    {"label": "b: Scenario A - Dec 31, Year 1 adjusting entry amount (none required)", "value": 0},
    {"label": "b: Scenario A - classification of Common Stock Dividends Distributable at 12/31/Y1",
     "value": "Stockholders' equity (paid-in capital section), reported just below/with Common Stock; NOT a liability"},
    {"label": "c(1): before declaration - Common stock", "value": f(s1["cs"])},
    {"label": "c(1): before declaration - Common stock dividends distributable", "value": f(s1["csdd"])},
    {"label": "c(1): before declaration - PIC in excess of par-common", "value": f(s1["pic"])},
    {"label": "c(1): before declaration - Retained earnings", "value": f(s1["re"])},
    {"label": "c(1): before declaration - Total stockholders' equity", "value": f(s1["tot"])},
    {"label": "c(1): before declaration - Shares outstanding", "value": s1["sh"]},
    {"label": "c(1): before declaration - Par per share", "value": f(s1["par"])},
    {"label": "c(2): Dec 31, Year 1 - Common stock", "value": f(s2["cs"])},
    {"label": "c(2): Dec 31, Year 1 - Common stock dividends distributable", "value": f(s2["csdd"])},
    {"label": "c(2): Dec 31, Year 1 - PIC in excess of par-common", "value": f(s2["pic"])},
    {"label": "c(2): Dec 31, Year 1 - Retained earnings", "value": f(s2["re"])},
    {"label": "c(2): Dec 31, Year 1 - Total stockholders' equity", "value": f(s2["tot"])},
    {"label": "c(2): Dec 31, Year 1 - Shares outstanding", "value": s2["sh"]},
    {"label": "c(2): Dec 31, Year 1 - Par per share", "value": f(s2["par"])},
    {"label": "c(3): after Jan 12, Year 2 distribution - Common stock", "value": f(s3["cs"])},
    {"label": "c(3): after Jan 12, Year 2 distribution - Common stock dividends distributable", "value": f(s3["csdd"])},
    {"label": "c(3): after Jan 12, Year 2 distribution - PIC in excess of par-common", "value": f(s3["pic"])},
    {"label": "c(3): after Jan 12, Year 2 distribution - Retained earnings", "value": f(s3["re"])},
    {"label": "c(3): after Jan 12, Year 2 distribution - Total stockholders' equity", "value": f(s3["tot"])},
    {"label": "c(3): after Jan 12, Year 2 distribution - Shares outstanding", "value": s3["sh"]},
    {"label": "c(3): after Jan 12, Year 2 distribution - Par per share", "value": f(s3["par"])},
    {"label": "d: Scenario A - Jan 12, Y2 Dr Common Stock Dividends Distributable", "value": f(par_a)},
    {"label": "d: Scenario A - Jan 12, Y2 Cr Common Stock", "value": f(par_a)},
    {"label": "e: Scenario B - shares in 50% large stock dividend", "value": sh_b},
    {"label": "e: Scenario B - Dec 15 Dr Retained Earnings (at par)", "value": f(amt_b)},
    {"label": "e: Scenario B - Dec 15 Cr Common Stock Dividends Distributable", "value": f(amt_b)},
    {"label": "e: Scenario B - Jan 12 Dr CSDD / Cr Common Stock", "value": f(amt_b)},
    {"label": "e: Scenario B - ending Common stock", "value": f(cs_b_end)},
    {"label": "e: Scenario B - ending PIC in excess of par-common", "value": f(pic_b_end)},
    {"label": "e: Scenario B - ending Retained earnings", "value": f(re_b_end)},
    {"label": "e: Scenario B - ending shares outstanding", "value": sh_b_end},
    {"label": "e: Scenario B - ending total stockholders' equity", "value": f(tot_b_end)},
    {"label": "f: Scenario C - journal entry required", "value": "None; memorandum entry only (no dollar amounts change)"},
    {"label": "f: Scenario C - shares outstanding after 2-for-1 split", "value": sh_c},
    {"label": "f: Scenario C - par per share after split", "value": f(par_c)},
    {"label": "f: Scenario C - total common stock dollar amount after split", "value": f(cs_c)},
]

jes = [
    {"part": "a", "lines": [
        {"account": "Dec 15, Y1 - Retained Earnings (Stock Dividends Declared)", "debit": f(fv_a), "credit": 0},
        {"account": "Common Stock Dividends Distributable ($3 par x 7,200 sh)", "debit": 0, "credit": f(par_a)},
        {"account": "Paid-in Capital in Excess of Par-Common Stock", "debit": 0, "credit": f(pic_a)},
    ]},
    {"part": "b", "lines": [
        {"account": "No adjusting entry required at Dec 31, Year 1 (declaration already recorded; distribution is an equity reclass in Year 2)", "debit": 0, "credit": 0},
    ]},
    {"part": "d", "lines": [
        {"account": "Jan 12, Y2 - Common Stock Dividends Distributable", "debit": f(par_a), "credit": 0},
        {"account": "Common Stock ($3 par, 7,200 shares issued)", "debit": 0, "credit": f(par_a)},
    ]},
    {"part": "e", "lines": [
        {"account": "Dec 15, Y1 - Retained Earnings (Stock Dividends Declared, at par)", "debit": f(amt_b), "credit": 0},
        {"account": "Common Stock Dividends Distributable ($3 par x 30,000 sh)", "debit": 0, "credit": f(amt_b)},
        {"account": "Jan 12, Y2 - Common Stock Dividends Distributable", "debit": f(amt_b), "credit": 0},
        {"account": "Common Stock ($3 par, 30,000 shares issued)", "debit": 0, "credit": f(amt_b)},
    ]},
    {"part": "f", "lines": [
        {"account": "No journal entry - memorandum entry only: 60,000 shares of $3 par replaced by 120,000 shares of $1.50 par", "debit": 0, "credit": 0},
    ]},
]

# Dr = Cr proof
for je in jes:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert d == c, (je["part"], d, c)
assert s1["tot"] == s2["tot"] == s3["tot"] == tse0
assert tot_b_end == tse0
assert cs_c == cs0

print(json.dumps({
    "id": "agent_373#00",
    "rounding_convention": "decimal.Decimal throughout; money quantized to cents (0.01) with ROUND_HALF_UP at each period/measurement point; shares are exact whole integers (no fractional shares).",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": "Scenario A (12% < 20-25%) = small stock dividend: measured at fair value $22/share, RE debited $158,400. No Dec 31 adjusting entry is needed - the declaration entry already captured the effect, and Common Stock Dividends Distributable is an EQUITY account (paid-in capital), presented in the stockholders' equity section immediately after/with Common Stock, never as a liability, because it will be settled in shares rather than assets. Total stockholders' equity is unchanged by every action here ($1,470,000 at all three dates in part c, and after Scenario B and Scenario C) - stock dividends and splits only reshuffle equity components. Scenario B (50% >= 20-25%) = large stock dividend / split effected as a dividend: measured at PAR ($90,000), market price ignored; PIC in excess of par is unaffected. Scenario C true split: no entry, par halves from $3.00 to $1.50, shares double to 120,000, and total common stock stays $180,000."
}, indent=1))
