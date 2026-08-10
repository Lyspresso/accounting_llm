"""Solver for agent_240#00 — ASC 480 mandatorily redeemable preferred stock.

Rounding convention: all money is decimal.Decimal, quantized to the cent
using ROUND_HALF_UP each period (interest accretion is computed and rounded
per period, then rolled forward into the next period's beginning balance).
Nothing is hard-coded: proceeds, redemption amount, rate, and term drive
every figure; the schedule is derived by effective-interest accretion and
the final period's ending balance is proved against the stated redemption.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)

# ---- inputs from the scenario ----
proceeds    = Decimal("150000")
redemption  = Decimal("199650")
rate        = Decimal("0.10")
years       = [1, 2, 3]
par_total   = Decimal("3000") * Decimal("40")   # form only; not used to measure

# ---- (b) accretion schedule ----
rows = []
bal = q(proceeds)
for yr in years:
    beg = bal
    interest = q(beg * rate)
    end = q(beg + interest)
    rows.append({"year": yr, "beg": beg, "interest": interest, "end": end})
    bal = end

total_interest = q(sum((r["interest"] for r in rows), Decimal("0")))
final_end = rows[-1]["end"]
diff = q(redemption - proceeds)
ties = (final_end == redemption) and (total_interest == diff)

f = lambda d: float(d)

answers = [
    {"label": "a: Initial liability recognized at Jan 1, Year 1 (cash proceeds = fair value)", "value": f(q(proceeds))},
    {"label": "a: Cash debited at issuance", "value": f(q(proceeds))},
    {"label": "a: Amount reported in stockholders' equity immediately after issuance", "value": 0.0},
    {"label": "a: Classification immediately after issuance — noncurrent LIABILITY (mandatorily redeemable preferred, fixed amount $199,650 on a fixed date 12/31/Yr3, ASC 480-10-25-4); not equity, not mezzanine; the $120,000 total par is form only", "value": f(q(proceeds))},
    {"label": "b: Year 1 beginning carrying amount", "value": f(rows[0]["beg"])},
    {"label": "b: Year 1 interest expense (10% x beginning)", "value": f(rows[0]["interest"])},
    {"label": "b: Year 1 ending carrying amount", "value": f(rows[0]["end"])},
    {"label": "b: Year 2 beginning carrying amount", "value": f(rows[1]["beg"])},
    {"label": "b: Year 2 interest expense (10% x beginning)", "value": f(rows[1]["interest"])},
    {"label": "b: Year 2 ending carrying amount", "value": f(rows[1]["end"])},
    {"label": "b: Year 3 beginning carrying amount", "value": f(rows[2]["beg"])},
    {"label": "b: Year 3 interest expense (10% x beginning)", "value": f(rows[2]["interest"])},
    {"label": "b: Year 3 ending carrying amount (= mandatory redemption amount)", "value": f(rows[2]["end"])},
    {"label": "b: Total interest expense, Years 1-3", "value": f(total_interest)},
    {"label": "c: Dec 31, Year 1 interest expense accretion", "value": f(rows[0]["interest"])},
    {"label": "c: Liability carrying amount after the Dec 31, Year 1 entry", "value": f(rows[0]["end"])},
    {"label": "c: Dec 31, Year 2 interest expense accretion", "value": f(rows[1]["interest"])},
    {"label": "c: Liability carrying amount after the Dec 31, Year 2 entry", "value": f(rows[1]["end"])},
    {"label": "d: Dec 31, Year 3 interest expense accretion", "value": f(rows[2]["interest"])},
    {"label": "d: Liability carrying amount immediately before settlement", "value": f(rows[2]["end"])},
    {"label": "d: Cash paid at maturity settlement, Dec 31, Year 3", "value": f(q(redemption))},
    {"label": "d: Gain or loss on settlement (carrying amount equals redemption price)", "value": 0.0},
    {"label": "e: Total interest expense recognized over the three-year life", "value": f(total_interest)},
    {"label": "e: Redemption amount", "value": f(q(redemption))},
    {"label": "e: Issue proceeds", "value": f(q(proceeds))},
    {"label": "e: Redemption amount minus issue proceeds", "value": f(diff)},
    {"label": "e: Reconciling difference (total interest expense - (redemption - proceeds)); zero proves the schedule ties", "value": f(q(total_interest - diff))},
]

def L(acct, dr=None, cr=None):
    return {"account": acct, "debit": f(q(dr)) if dr is not None else 0.0,
            "credit": f(q(cr)) if cr is not None else 0.0}

jes = [
    {"part": "a", "lines": [
        L("Cash", dr=proceeds),
        L("Mandatorily redeemable preferred stock liability (Jan 1, Year 1)", cr=proceeds),
    ]},
    {"part": "c", "lines": [
        L("Interest expense (Dec 31, Year 1)", dr=rows[0]["interest"]),
        L("Mandatorily redeemable preferred stock liability", cr=rows[0]["interest"]),
    ]},
    {"part": "c", "lines": [
        L("Interest expense (Dec 31, Year 2)", dr=rows[1]["interest"]),
        L("Mandatorily redeemable preferred stock liability", cr=rows[1]["interest"]),
    ]},
    {"part": "d", "lines": [
        L("Interest expense (Dec 31, Year 3)", dr=rows[2]["interest"]),
        L("Mandatorily redeemable preferred stock liability", cr=rows[2]["interest"]),
    ]},
    {"part": "d", "lines": [
        L("Mandatorily redeemable preferred stock liability (settlement Dec 31, Year 3)", dr=redemption),
        L("Cash", cr=redemption),
    ]},
]

for je in jes:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert d == c, (je, d, c)
assert ties

notes = ("ASC 480-10-25-4: preferred stock with a mandatory cash redemption of a fixed "
         "$199,650 on the fixed date 12/31/Year 3 (not solely upon liquidation) is a "
         "liability, not equity or mezzanine, so nothing hits stockholders' equity. "
         "Initial measurement = $150,000 cash proceeds (fair value); the $120,000 aggregate "
         "par (3,000 x $40) is descriptive form only. Subsequent measurement uses the "
         "effective-interest method at the 10% implicit rate, with accretion charged to "
         "interest expense (not to retained earnings, since the instrument is a liability). "
         "The accretion is exact: 150,000 x 1.10^3 = 199,650, so Year 3's ending carrying "
         "amount equals the redemption price and settlement produces no gain or loss. "
         "Preferred dividends are ignored per the problem. All amounts rounded to the cent "
         "with ROUND_HALF_UP each period; no rounding differences arose.")

print(json.dumps({
    "id": "agent_240#00",
    "rounding_convention": ("decimal.Decimal throughout; interest accreted at 10% of the "
                            "beginning carrying amount and quantized to the cent with "
                            "ROUND_HALF_UP each period, then rolled forward"),
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
