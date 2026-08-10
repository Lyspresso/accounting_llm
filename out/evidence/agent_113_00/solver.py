#!/usr/bin/env python3
"""Solver for item agent_113#00 — Lakeshore Dynamics Inc. (LO 19-8).

Appropriation-of-retained-earnings journal entry plus a two-year equity-ratio
schedule (book value per common share, payout ratio, return on equity,
price-to-earnings ratio).

ROUNDING CONVENTION
-------------------
* All money and all ratio arithmetic uses ``decimal.Decimal``. No floats
  anywhere. The working precision is 28 significant digits (Decimal default).
* Rounding is ``ROUND_HALF_UP``, applied ONCE per reported figure at the end of
  that figure's derivation. Intermediates (common stockholders' equity, net
  income available to common, average common equity) are carried at full
  precision and are NOT pre-rounded — this is the "round-at-report" reading of
  the course's ROUND_HALF_UP-per-period rule, since this item has no periodic
  schedule (no amortization/PV work) in which a per-period rounding could
  compound.
* Per-share dollar figures (book value per common share, price-to-earnings) are
  rounded to 2 decimal places, matching the textbook's Demo 19-8 presentation
  ($28.83, $20.78).
* Payout ratio and return on equity are REPORTED AS PERCENTAGES rounded to 2
  decimal places (e.g. 20.80 means 20.80%). The textbook demo shows these two
  ratios as 2-decimal decimals (0.31, 0.33); at 2 decimals both of Lakeshore's
  payout figures collapse to 0.21, which would destroy the two-year comparison
  part (f) explicitly asks for, so percent is used. The unrounded decimal
  equivalents are restated in "notes" so either convention can be checked.
* Journal-entry amounts are exact whole dollars; debits are proved equal to
  credits before output.

SOURCES FOR THE FORMULAS (course textbook, chapter 19, LO 19-8):
  book value per share = common stock equity / common shares outstanding,
      where common stock equity = total stockholders' equity less preferred
      stockholder claims (liquidation value + any dividends in arrears)
  payout ratio        = cash common dividends / net income available to common
  return on equity    = net income available to common / average common
      stockholders' equity (simple average of beginning and ending)
  price-to-earnings   = market price per share / earnings per share

Run:  python3 solver.py      -> prints one JSON object on stdout
"""

from __future__ import annotations

import json
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28

D = Decimal
CENT = D("0.01")


def r2(x: Decimal) -> Decimal:
    """Round to 2 decimal places, ROUND_HALF_UP."""
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def num(x: Decimal):
    """JSON-friendly: int when integral, else float of the *already rounded*
    Decimal (str->float is exact enough for 2dp transport)."""
    if x == x.to_integral_value():
        return int(x)
    return float(x)


# ---------------------------------------------------------------------------
# 1. Fact pattern, transcribed from the stem (nothing here is an answer)
# ---------------------------------------------------------------------------

# Stockholders' equity components by year-end.
EQUITY = {
    "Y3": {
        "preferred_stock_par": D("400000"),
        "apic_preferred": D("40000"),
        "common_stock_par": D("120000"),
        "apic_common": D("2480000"),
        "retained_earnings": D("1860000"),
        "aoci": D("-80000"),
        "treasury_stock": D("-150000"),
        "total_reported": D("4670000"),
    },
    "Y2": {
        "preferred_stock_par": D("400000"),
        "apic_preferred": D("40000"),
        "common_stock_par": D("120000"),
        "apic_common": D("2480000"),
        "retained_earnings": D("1420000"),
        "aoci": D("-50000"),
        "treasury_stock": D("-150000"),
        "total_reported": D("4260000"),
    },
    "Y1": {
        "preferred_stock_par": D("400000"),
        "apic_preferred": D("40000"),
        "common_stock_par": D("100000"),
        "apic_common": D("1900000"),
        "retained_earnings": D("1150000"),
        "aoci": D("-40000"),
        "treasury_stock": D("0"),
        "total_reported": D("3550000"),
    },
}

PREFERRED_SHARES = D("8000")
PREFERRED_PAR_PER_SHARE = D("50")
PREFERRED_DIV_RATE = D("0.05")
PREFERRED_LIQUIDATION_PER_SHARE = D("55")
PREFERRED_ARREARS = D("0")  # stem: no dividends in arrears at any year-end

COMMON_SHARES_OUT = {"Y3": D("115000"), "Y2": D("115000"), "Y1": D("100000")}
NET_INCOME = {"Y3": D("520000"), "Y2": D("380000")}
COMMON_DIVIDENDS = {"Y3": D("104000"), "Y2": D("76000")}
MARKET_PRICE = {"Y3": D("48.00"), "Y2": D("36.00")}
BASIC_EPS = {"Y3": D("4.35"), "Y2": D("3.13")}

APPROPRIATION = D("250000")  # Dec. 31, Year 3 plant-expansion reserve

YEARS = ("Y3", "Y2", "Y1")
LABEL = {"Y3": "Year 3", "Y2": "Year 2", "Y1": "Year 1"}


# ---------------------------------------------------------------------------
# 2. Internal-consistency checks (not reported; they only guard the inputs)
# ---------------------------------------------------------------------------

for y in YEARS:
    e = EQUITY[y]
    footed = (
        e["preferred_stock_par"]
        + e["apic_preferred"]
        + e["common_stock_par"]
        + e["apic_common"]
        + e["retained_earnings"]
        + e["aoci"]
        + e["treasury_stock"]
    )
    assert footed == e["total_reported"], (y, footed, e["total_reported"])

assert PREFERRED_SHARES * PREFERRED_PAR_PER_SHARE == EQUITY["Y3"]["preferred_stock_par"]

# Preferred dividend requirement, derived (stem states $20,000).
preferred_dividend = PREFERRED_DIV_RATE * EQUITY["Y3"]["preferred_stock_par"]
assert preferred_dividend == D("20000"), preferred_dividend

# Preferred claim deducted from total equity to reach common equity:
# liquidation preference plus arrears (arrears = 0 here).
preferred_claim = PREFERRED_SHARES * PREFERRED_LIQUIDATION_PER_SHARE + PREFERRED_ARREARS
assert preferred_claim == D("440000"), preferred_claim


# ---------------------------------------------------------------------------
# 3. Derivations
# ---------------------------------------------------------------------------

# (a) Appropriation journal entry, December 31, Year 3.
je_a_lines = [
    {
        "account": "Retained Earnings (Unappropriated)",
        "debit": num(APPROPRIATION),
        "credit": 0,
    },
    {
        "account": "Retained Earnings Appropriated for Plant Expansion",
        "debit": 0,
        "credit": num(APPROPRIATION),
    },
]
assert sum(D(str(l["debit"])) for l in je_a_lines) == sum(
    D(str(l["credit"])) for l in je_a_lines
)

# Common stockholders' equity by year = total SE - preferred claim.
common_equity = {
    y: EQUITY[y]["total_reported"] - preferred_claim for y in YEARS
}

# (b) Book value per common share.
bvps = {
    y: r2(common_equity[y] / COMMON_SHARES_OUT[y]) for y in ("Y3", "Y2")
}

# Net income available to common stockholders (preferred is cumulative, so the
# current-year requirement is deducted whether or not declared; it is paid here).
ni_available = {y: NET_INCOME[y] - preferred_dividend for y in ("Y3", "Y2")}

# (c) Payout ratio = cash common dividends / net income available to common.
payout_dec = {y: COMMON_DIVIDENDS[y] / ni_available[y] for y in ("Y3", "Y2")}
payout_pct = {y: r2(payout_dec[y] * D("100")) for y in ("Y3", "Y2")}

# (d) Return on equity = NI available to common / average common equity.
avg_common_equity = {
    "Y3": (common_equity["Y3"] + common_equity["Y2"]) / D("2"),
    "Y2": (common_equity["Y2"] + common_equity["Y1"]) / D("2"),
}
roe_dec = {y: ni_available[y] / avg_common_equity[y] for y in ("Y3", "Y2")}
roe_pct = {y: r2(roe_dec[y] * D("100")) for y in ("Y3", "Y2")}

# (e) Price-to-earnings = market price per share / basic EPS.
pe = {y: r2(MARKET_PRICE[y] / BASIC_EPS[y]) for y in ("Y3", "Y2")}


# ---------------------------------------------------------------------------
# 4. Output
# ---------------------------------------------------------------------------

answers = []
for y in ("Y3", "Y2"):
    answers.append(
        {"label": f"b: book value per common share — {LABEL[y]} ($)", "value": num(bvps[y])}
    )
for y in ("Y3", "Y2"):
    answers.append(
        {"label": f"c: payout ratio — {LABEL[y]} (%)", "value": num(payout_pct[y])}
    )
for y in ("Y3", "Y2"):
    answers.append(
        {"label": f"d: return on equity — {LABEL[y]} (%)", "value": num(roe_pct[y])}
    )
for y in ("Y3", "Y2"):
    answers.append(
        {"label": f"e: price-to-earnings ratio — {LABEL[y]} (times)", "value": num(pe[y])}
    )
# (f) is the two-year schedule assembling (b)-(e); same eight figures, no new
# numbers, so it adds no separate answer values.

notes = (
    "Formulas per course textbook ch.19 LO 19-8 / Demo 19-8. Common stockholders' "
    "equity = total stockholders' equity less the preferred claim of $440,000 "
    "(8,000 sh x $55 liquidation preference; no arrears): Year 3 $4,230,000, "
    "Year 2 $3,820,000, Year 1 $3,110,000. Net income available to common = net "
    "income less the $20,000 cumulative preferred requirement: Year 3 $500,000, "
    "Year 2 $360,000. "
    "(c)/(d) are reported as percentages; unrounded decimal equivalents are "
    "payout 0.2080 (Yr 3) and 0.2111 (Yr 2); ROE 0.1242 (Yr 3) and 0.1039 (Yr 2) "
    "— at the textbook's 2-decimal decimal convention payout is 0.21 in both "
    "years and ROE is 0.12 / 0.10. "
    "(f) Two-year ratio schedule (Year 3 | Year 2): book value per common share "
    "$36.78 | $33.22; payout ratio 20.80% | 21.11%; return on equity 12.42% | "
    "10.39%; price-to-earnings 11.03 | 11.50. "
    "(g) ASC 505 equity disclosures relevant here: (1) number of shares "
    "authorized, issued and outstanding for each class and their par value; "
    "(2) rights and privileges of each class outstanding — the 5% cumulative "
    "preferred's dividend rate, its cumulative feature and its $55 per share "
    "liquidation preference; (3) the liquidation preference in the aggregate "
    "($440,000) disclosed in the equity section, together with the excess of "
    "that preference over par ($40,000); (4) the nature and amount of the "
    "retained earnings restriction/appropriation — $250,000 appropriated for "
    "plant expansion under the bank loan covenant, with retained earnings shown "
    "in appropriated and unappropriated components; (5) changes in each class of "
    "equity for each period presented (a statement of stockholders' equity), "
    "including treasury share activity; (6) treasury stock — shares held and "
    "the cost basis shown as a deduction from equity; (7) any dividends in "
    "arrears on cumulative preferred (none here, which is itself the "
    "disclosure); (8) accumulated other comprehensive loss by component. "
    "(h) No to both. The appropriation is a reclassification within retained "
    "earnings — it debits unappropriated retained earnings and credits "
    "appropriated retained earnings, both equity accounts — so total "
    "stockholders' equity stays $4,670,000, no cash moves, no asset or "
    "liability changes, and Year 3 book value per common share stays $36.78. "
    "It only signals that $250,000 of retained earnings is unavailable for "
    "dividends under the loan covenant."
)

result = {
    "id": "agent_113#00",
    "rounding_convention": (
        "decimal.Decimal throughout, no floats; ROUND_HALF_UP applied once per "
        "reported figure at the end of its derivation (intermediates carried at "
        "full precision). Per-share dollars and the P/E multiple to 2 decimals; "
        "payout ratio and ROE reported as percentages to 2 decimals (decimal "
        "equivalents given in notes). Journal entry in exact whole dollars, "
        "debits proved equal to credits."
    ),
    "answers": answers,
    "journal_entries": [{"part": "a", "lines": je_a_lines}],
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(result, indent=2))
