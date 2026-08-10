"""Northlake Precision Inc. 2025 -- issuance, treasury buyback, preferred dividend,
large (20%) stock dividend, weighted-average shares, basic EPS.

Rounding convention: all money computed with decimal.Decimal (never floats);
monetary amounts quantized to $0.01 and EPS quantized to $0.01 using
ROUND_HALF_UP, applied per period / per computed figure (no chained rounding).
Share counts are whole shares (ROUND_HALF_UP to 1 share). Every figure derived
from the scenario inputs below; nothing hard-coded.
"""
from decimal import Decimal as D, ROUND_HALF_UP
import json

CENT = D("0.01")
def m(x):  return (x).quantize(CENT, rounding=ROUND_HALF_UP)
def sh(x): return (x).quantize(D("1"), rounding=ROUND_HALF_UP)
def num(x):
    x = D(x)
    return int(x) if x == x.to_integral_value() else float(x)

# ---------------- inputs ----------------
common_begin      = D("120000")
common_par        = D("2")
pfd_shares        = D("8000")
pfd_rate          = D("0.06")
pfd_par           = D("25")
net_income        = D("378000")

apr_shares, apr_price = D("30000"), D("14")
jul_shares, jul_price = D("6000"),  D("16")
sd_pct                = D("0.20")          # Nov 1, large stock dividend at par
months_in_year        = D("12")

# ---------------- (a) initial recognition JEs ----------------
apr_cash = m(apr_shares * apr_price)
apr_par  = m(apr_shares * common_par)
apr_apic = m(apr_cash - apr_par)

jul_cost = m(jul_shares * jul_price)

pfd_div  = m(pfd_shares * pfd_par * pfd_rate)

sh_before_sd = common_begin + apr_shares - jul_shares   # outstanding for EPS on Nov 1
sd_shares    = sh(sh_before_sd * sd_pct)
sd_amount    = m(sd_shares * common_par)                # large dividend -> par

jes = [
 {"part":"a","date":"2025-04-01","description":"Issued 30,000 common shares for cash at $14",
  "lines":[{"account":"Cash","debit":num(apr_cash),"credit":0},
           {"account":"Common Stock ($2 par)","debit":0,"credit":num(apr_par)},
           {"account":"Paid-in Capital in Excess of Par - Common","debit":0,"credit":num(apr_apic)}]},
 {"part":"a","date":"2025-07-01","description":"Purchased 6,000 treasury shares at $16 (cost method)",
  "lines":[{"account":"Treasury Stock","debit":num(jul_cost),"credit":0},
           {"account":"Cash","debit":0,"credit":num(jul_cost)}]},
 {"part":"a","date":"2025-09-30","description":"Declared and paid full annual preferred dividend (8,000 x $25 x 6%)",
  "lines":[{"account":"Retained Earnings (Cash Dividends - Preferred)","debit":num(pfd_div),"credit":0},
           {"account":"Cash","debit":0,"credit":num(pfd_div)}]},
 {"part":"a","date":"2025-11-01","description":"Declared and distributed 20% large stock dividend (28,800 shares) recorded at $2 par",
  "lines":[{"account":"Retained Earnings (Stock Dividend Distributed)","debit":num(sd_amount),"credit":0},
           {"account":"Common Stock ($2 par)","debit":0,"credit":num(sd_amount)}]},
]
for je in jes:
    assert sum(D(str(l["debit"])) for l in je["lines"]) == sum(D(str(l["credit"])) for l in je["lines"])

# ---------------- (b) weighted-average share schedule ----------------
factor = D("1") + sd_pct                    # retroactive restatement factor
periods = [
 ("Jan 1 - Mar 31", common_begin,                       D("3"), factor),
 ("Apr 1 - Jun 30", common_begin + apr_shares,          D("3"), factor),
 ("Jul 1 - Oct 31", sh_before_sd,                       D("4"), factor),
 ("Nov 1 - Dec 31", sh_before_sd + sd_shares,           D("2"), D("1")),
]
rows, was = [], D("0")
for name, outst, mo, f in periods:
    w = sh(outst * f * mo / months_in_year)
    was += w
    rows.append((name, outst, f, mo, w))

# ---------------- (c) income available to common and basic EPS ----------------
inc_avail = m(net_income - pfd_div)
eps = (inc_avail / was).quantize(CENT, rounding=ROUND_HALF_UP)

answers = [
 {"label":"a: Apr 1 - cash received on common issuance","value":num(apr_cash)},
 {"label":"a: Apr 1 - credit to Common Stock at $2 par","value":num(apr_par)},
 {"label":"a: Apr 1 - credit to Paid-in Capital in Excess of Par","value":num(apr_apic)},
 {"label":"a: Jul 1 - Treasury Stock debit at cost","value":num(jul_cost)},
 {"label":"a: Sep 30 - preferred cash dividend paid","value":num(pfd_div)},
 {"label":"a: Nov 1 - stock dividend shares distributed","value":num(sd_shares)},
 {"label":"a: Nov 1 - stock dividend recorded at par","value":num(sd_amount)},
 {"label":"b: retroactive stock-dividend restatement factor","value":num(factor)},
]
for name, outst, f, mo, w in rows:
    answers.append({"label":f"b: {name} - actual shares outstanding","value":num(outst)})
    answers.append({"label":f"b: {name} - restatement factor","value":num(f)})
    answers.append({"label":f"b: {name} - fraction of year (months/12)","value":f"{int(mo)}/12"})
    answers.append({"label":f"b: {name} - weighted restated shares","value":num(w)})
answers += [
 {"label":"b: weighted-average common shares outstanding, 2025","value":num(was)},
 {"label":"c: net income","value":num(net_income)},
 {"label":"c: less preferred dividend claim (cumulative, 1 year)","value":num(pfd_div)},
 {"label":"c: income available to common stockholders","value":num(inc_avail)},
 {"label":"c: basic EPS (income avail. to common / weighted-avg shares)","value":num(eps)},
 {"label":"d: income-statement presentation (simple capital structure)",
  "value":f"Net income $ {net_income:,.2f}; presented on the face of the 2025 income statement immediately below net income: "
          f"\"Earnings per common share - basic .... $ {eps}\" (single EPS figure only; no diluted EPS is required for a simple "
          f"capital structure). A note discloses that income available to common of $ {inc_avail:,.2f} is net income less the "
          f"$ {pfd_div:,.2f} cumulative preferred claim, over {int(was):,} weighted-average shares restated for the 20% stock dividend."},
 {"label":"e: why the stock dividend is treated differently from the April 1 cash issuance in the denominator",
  "value":"The April 1 issuance brought new cash into the company, so the extra 30,000 shares had earning assets behind them only "
          "from April 1 forward - they are weighted for the 9/12 of the year they were outstanding. The 20% stock dividend brought "
          "in no resources; it only slices the same equity into more certificates, so every shareholder's proportionate interest is "
          "unchanged. To keep EPS comparable across the whole period (and prior periods presented), the new shares are applied "
          "retroactively: all pre-November share counts are multiplied by 1.20 rather than weighted from November 1."},
]

print(json.dumps({
 "id":"agent_119#00",
 "rounding_convention":"decimal.Decimal throughout (no floats); money quantized to $0.01 and EPS to $0.01 with ROUND_HALF_UP, applied per period/per figure; share counts to whole shares (ROUND_HALF_UP).",
 "answers":answers,
 "journal_entries":jes,
 "insufficient_info":False,
 "notes":"Preferred dividend = 8,000 x $25 x 6% = $12,000 (cumulative, outstanding all year, one full year deducted). "
         "Treasury shares are carried at cost and, per the scenario, excluded from EPS-outstanding shares, so the 20% stock "
         "dividend is computed on the 144,000 shares outstanding for EPS on Nov 1 (120,000 + 30,000 - 6,000) = 28,800 new shares "
         "at $2 par = $57,600 charged to Retained Earnings (large stock dividend recorded at par, per instruction). Because the "
         "Nov 1 dividend was declared and distributed the same day, the Common Stock Dividend Distributable step is collapsed into "
         "one entry. Retroactive factor 1.20 applied to all periods before Nov 1; Nov-Dec shares (172,800) already include the "
         "dividend shares. Basic EPS = $366,000 / 167,400 = $2.1864 -> $2.19."
}, indent=1))
