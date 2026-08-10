"""Redcedar Freight Systems Inc. -- contingently issuable shares EPS (LO 20-8).

Rounding convention: all money/EPS arithmetic uses decimal.Decimal (never float).
EPS figures are rounded to the cent with ROUND_HALF_UP, applied once per period
(per-period rounding; no chained rounding of intermediate share counts).
Share counts are exact integers. Every figure is derived from the fact table
below -- nothing is hard-coded as an output.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
def eps(num: Decimal, den: int) -> Decimal:
    return (num / Decimal(den)).quantize(CENT, rounding=ROUND_HALF_UP)

# ---- given facts -----------------------------------------------------------
ni1        = Decimal("510000")   # Year 1 net income
waso1      = 85000               # common shares outstanding all of Year 1
contingent = 7000                # shares grantable to CEO
target     = Decimal("480000")   # Year 2 NI target
ni2        = Decimal("445000")   # Year 2 net income (actual)
waso2      = 85000               # Year 2 shares outstanding (none issued)

# ---- Year 1 ----------------------------------------------------------------
# ASC 260 contingently issuable shares: test the condition as if the end of the
# reporting period were the end of the contingency period. The condition is an
# earnings level, so CURRENT-year earnings are the proxy for the Year 2 target.
y1_condition_met = ni1 >= target                       # 510,000 >= 480,000 -> True
y1_cont_in_dil   = contingent if y1_condition_met else 0
b1  = eps(ni1, waso1)
d1_num = ni1                                           # no numerator adjustment
d1_den = waso1 + y1_cont_in_dil
d1  = eps(d1_num, d1_den)

# ---- Year 2 ----------------------------------------------------------------
y2_condition_met = ni2 >= target                       # 445,000 >= 480,000 -> False
y2_cont_in_dil   = contingent if y2_condition_met else 0
b2  = eps(ni2, waso2)
d2_num = ni2
d2_den = waso2 + y2_cont_in_dil
d2  = eps(d2_num, d2_den)

f = lambda d: float(d)
answers = [
 {"label":"a: Year 1 basic EPS ($510,000 / 85,000 shares)","value":f(b1)},
 {"label":"a: Year 1 diluted EPS ($510,000 / 92,000 shares)","value":f(d1)},
 {"label":"a: Contingent shares included in Year 1 diluted EPS","value":y1_cont_in_dil},

 {"label":"b: Year 1 schedule - basic row numerator (net income)","value":f(ni1)},
 {"label":"b: Year 1 schedule - basic row denominator (weighted-average shares)","value":waso1},
 {"label":"b: Year 1 schedule - basic EPS","value":f(b1)},
 {"label":"b: Year 1 schedule - contingent-share row numerator effect","value":f(Decimal("0"))},
 {"label":"b: Year 1 schedule - contingent-share row denominator effect (shares added)","value":y1_cont_in_dil},
 {"label":"b: Year 1 schedule - diluted row numerator","value":f(d1_num)},
 {"label":"b: Year 1 schedule - diluted row denominator","value":d1_den},
 {"label":"b: Year 1 schedule - diluted EPS","value":f(d1)},

 {"label":"c: Year 2 basic EPS ($445,000 / 85,000 shares)","value":f(b2)},
 {"label":"c: Year 2 diluted EPS ($445,000 / 85,000 shares)","value":f(d2)},
 {"label":"c: Contingent shares entering Year 2 diluted EPS","value":y2_cont_in_dil},

 {"label":"d: Two-year schedule - Year 1 net income","value":f(ni1)},
 {"label":"d: Two-year schedule - Year 1 basic WASO","value":waso1},
 {"label":"d: Two-year schedule - Year 1 contingent shares in diluted","value":y1_cont_in_dil},
 {"label":"d: Two-year schedule - Year 1 basic EPS","value":f(b1)},
 {"label":"d: Two-year schedule - Year 1 diluted EPS","value":f(d1)},
 {"label":"d: Two-year schedule - Year 2 net income","value":f(ni2)},
 {"label":"d: Two-year schedule - Year 2 basic WASO","value":waso2},
 {"label":"d: Two-year schedule - Year 2 contingent shares in diluted","value":y2_cont_in_dil},
 {"label":"d: Two-year schedule - Year 2 basic EPS","value":f(b2)},
 {"label":"d: Two-year schedule - Year 2 diluted EPS","value":f(d2)},

 {"label":"e: Number of settlement/issuance journal entries in Year 2 or Year 3","value":0},
 {"label":"e: Shares actually issued to the CEO","value":0},

 {"label":"f: Year 1 income statement presentation - Earnings per share, basic","value":f(b1)},
 {"label":"f: Year 1 income statement presentation - Earnings per share, diluted","value":f(d1)},
]

notes = (
 "a. Basic EPS = $510,000 / 85,000 = $6.00. Contingently issuable shares are included in "
 "DILUTED EPS when the contingency condition would be satisfied assuming the end of the "
 "reporting period were the end of the contingency period. The condition here is an earnings "
 "level, so Year 1 earnings are the proxy for the Year 2 target: $510,000 >= $480,000, so the "
 "target is currently met and all 7,000 contingent shares are added to the denominator with no "
 "numerator adjustment (no cash is received and no income effect). Diluted EPS = $510,000 / "
 "(85,000 + 7,000 = 92,000) = $5.5435 -> $5.54. The shares are dilutive ($5.54 < $6.00), so they "
 "are included; they are NOT treated as outstanding for basic EPS because they have not been "
 "issued and issuance is not yet assured beyond the passage of time. "
 "b. Year 1 period-end diluted schedule: Basic  $510,000 / 85,000 = $6.00; Contingent CEO shares "
 "  $0 / +7,000; Diluted  $510,000 / 92,000 = $5.54. "
 "c. Year 2: basic EPS = $445,000 / 85,000 = $5.2353 -> $5.24. At the Year 2 period end the "
 "contingency period has ended and the target failed ($445,000 < $480,000), so 0 contingent "
 "shares enter diluted EPS; diluted EPS = basic EPS = $5.24 (no dilutive securities remain). "
 "d. Two-year subsequent measurement schedule: "
 "Year 1 - NI $510,000; basic WASO 85,000; contingent shares in diluted 7,000; basic $6.00; diluted $5.54. "
 "Year 2 - NI $445,000; basic WASO 85,000; contingent shares in diluted 0; basic $5.24; diluted $5.24. "
 "Year 1 diluted EPS as originally reported is NOT restated when the contingency later fails; the "
 "change is reflected prospectively in the Year 2 computation. "
 "e. No settlement or issuance journal entry in Year 2 or Year 3. The Year 2 target was missed, so "
 "the CEO earns no shares and none are issued -- there is no transaction to record. Even in the "
 "year the shares were counted (Year 1), the contingent-share agreement produced no journal entry: "
 "including them in diluted EPS is purely a disclosure/computational assumption, not an accounting "
 "event. A JE (Dr Compensation-related account / Cr Common Stock and APIC) would arise only if the "
 "shares were actually earned and issued, which never happens here. "
 "f. Year 1 income statement presentation (bottom of the statement, after net income): "
 "Earnings per share - Basic  $6.00; Earnings per share - Diluted  $5.54. Both figures are shown "
 "on the face of the income statement for each period presented; with no discontinued operations "
 "only the single basic and diluted amounts are required."
)

out = {
 "id":"agent_253#01",
 "rounding_convention":("decimal.Decimal throughout; EPS rounded to the nearest cent using "
   "ROUND_HALF_UP once per period (per-period rounding, no chained rounding). Share counts are "
   "exact integers; net income is exact. No amortization/PV schedule is involved, so no "
   "close-to-face adjustment is needed. No journal entries arise, so Dr = Cr is trivially satisfied."),
 "answers":answers,
 "journal_entries":[],
 "insufficient_info":False,
 "notes":notes,
}
print(json.dumps(out))
