"""Solver for agent_135#01 — AFS (FV-OCI) bond investment, LO 14-3.

Rounding convention: all money handled with decimal.Decimal (never floats);
every computed amount is quantized to 0.01 using ROUND_HALF_UP at each period
(per-period rounding, no carry of unrounded residue). Bonds are bought AT PAR,
so amortized cost is constant and no discount/premium amortization arises;
all figures below are derived from the stated par, rate, fair values and
proceeds — nothing is hard-coded.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x):  # per-period ROUND_HALF_UP
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def n(x):  # JSON number
    return float(q(x))

# ---- Given inputs -----------------------------------------------------------
par        = Decimal("55000")
coupon_rt  = Decimal("0.09")
purch_cost = par                      # "purchased for par"
fv_y1      = Decimal("52250")         # Dec 31 Y1
fv_y2      = Decimal("57200")         # Dec 31 Y2
proceeds   = Decimal("57750")         # Jan 1 Y3 sale (= FV at sale date)

# ---- (a) purchase -----------------------------------------------------------
a_debit = q(purch_cost)

# ---- (b) annual cash interest ----------------------------------------------
cash_int = q(par * coupon_rt)

# ---- (c) FVA schedule -------------------------------------------------------
# Bought at par -> amortized cost stays at par at every measurement date.
amort_cost = q(par)
rows, prior = [], Decimal("0")
for date, fv in (("Dec 31, Year 1", fv_y1),
                 ("Dec 31, Year 2", fv_y2),
                 ("Jan 1, Year 3 (sale date)", proceeds)):
    req = q(fv - amort_cost)          # +ve = debit FVA, -ve = credit FVA
    adj = q(req - prior)
    rows.append({
        "date": date,
        "amortized_cost": n(amort_cost),
        "fair_value": n(fv),
        "required_FVA_balance": n(req),
        "prior_FVA_balance": n(prior),
        "FVA_adjustment": n(adj),
        "adjustment_direction": "debit FVA (unrealized gain OCI)" if adj > 0
                                else ("credit FVA (unrealized loss OCI)" if adj < 0 else "none"),
        "carrying_amount_after": n(amort_cost + req),
    })
    prior = req
fva_y1, adj_y1 = q(fv_y1 - amort_cost), q(fv_y1 - amort_cost)
fva_y2 = q(fv_y2 - amort_cost); adj_y2 = q(fva_y2 - fva_y1)
fva_s  = q(proceeds - amort_cost); adj_s = q(fva_s - fva_y2)

# ---- AOCI roll-forward ------------------------------------------------------
aoci_y1 = q(Decimal("0") + adj_y1)          # OCI equals the FVA adjustment
aoci_y2 = q(aoci_y1 + adj_y2)
aoci_pre_sale = q(aoci_y2 + adj_s)
reclass = q(aoci_pre_sale)                  # recycled to net income on sale
aoci_end_y3 = q(aoci_pre_sale - reclass)
gain_on_sale = q(proceeds - amort_cost)     # realized gain reported in NI

answers = [
 {"label": "a: Debit — Investment in Oakmont bonds (AFS/FV-OCI), Jan 1 Y1", "value": n(a_debit)},
 {"label": "a: Credit — Cash paid on purchase, Jan 1 Y1", "value": n(a_debit)},
 {"label": "b: Cash interest received Dec 31 Y1 (= $55,000 x 9%)", "value": n(cash_int)},
 {"label": "b: Interest income recognized Dec 31 Y1", "value": n(cash_int)},

 {"label": "c: Dec 31 Y1 — amortized cost", "value": n(amort_cost)},
 {"label": "c: Dec 31 Y1 — fair value", "value": n(fv_y1)},
 {"label": "c: Dec 31 Y1 — required FVA balance (credit)", "value": n(fva_y1)},
 {"label": "c: Dec 31 Y1 — prior FVA balance", "value": 0.0},
 {"label": "c: Dec 31 Y1 — FVA adjustment required (credit FVA / OCI loss)", "value": n(adj_y1)},
 {"label": "c: Dec 31 Y1 — carrying amount after adjustment", "value": n(fv_y1)},
 {"label": "c: Dec 31 Y2 — amortized cost", "value": n(amort_cost)},
 {"label": "c: Dec 31 Y2 — fair value", "value": n(fv_y2)},
 {"label": "c: Dec 31 Y2 — required FVA balance (debit)", "value": n(fva_y2)},
 {"label": "c: Dec 31 Y2 — prior FVA balance (credit)", "value": n(fva_y1)},
 {"label": "c: Dec 31 Y2 — FVA adjustment required (debit FVA / OCI gain)", "value": n(adj_y2)},
 {"label": "c: Dec 31 Y2 — carrying amount after adjustment", "value": n(fv_y2)},
 {"label": "c: Jan 1 Y3 sale date — amortized cost", "value": n(amort_cost)},
 {"label": "c: Jan 1 Y3 sale date — fair value (= proceeds)", "value": n(proceeds)},
 {"label": "c: Jan 1 Y3 sale date — required FVA balance (debit)", "value": n(fva_s)},
 {"label": "c: Jan 1 Y3 sale date — prior FVA balance (debit)", "value": n(fva_y2)},
 {"label": "c: Jan 1 Y3 sale date — FVA adjustment required (debit FVA / OCI gain)", "value": n(adj_s)},
 {"label": "c: Jan 1 Y3 sale date — carrying amount after adjustment", "value": n(proceeds)},

 {"label": "d: Year 1 unrealized holding loss recognized in OCI (Dr)", "value": n(-adj_y1)},
 {"label": "d: Year 1 credit to Fair value adjustment (AFS)", "value": n(-adj_y1)},

 {"label": "e: Year 1 income statement — interest income", "value": n(cash_int)},
 {"label": "e: Year 1 income statement — effect on net income", "value": n(cash_int)},
 {"label": "e: Year 1 SCI — other comprehensive loss, unrealized holding loss on FV-OCI investment", "value": n(adj_y1)},
 {"label": "e: Year 1 SCI — comprehensive income effect of this investment", "value": n(cash_int + adj_y1)},
 {"label": "e: Year 1 balance sheet — investment in bonds at fair value", "value": n(fv_y1)},
 {"label": "e: Year 1 balance sheet — amortized cost of investment", "value": n(amort_cost)},
 {"label": "e: Year 1 balance sheet — fair value adjustment (credit) offsetting the investment", "value": n(fva_y1)},
 {"label": "e: Year 1 balance sheet — AOCI balance in equity (debit/negative)", "value": n(aoci_y1)},

 {"label": "f: Year 2 debit to Fair value adjustment (AFS)", "value": n(adj_y2)},
 {"label": "f: Year 2 unrealized holding gain recognized in OCI", "value": n(adj_y2)},
 {"label": "f: Fair value adjustment balance Dec 31 Y2 (debit)", "value": n(fva_y2)},
 {"label": "f: AOCI balance Dec 31 Y2 (credit)", "value": n(aoci_y2)},

 {"label": "g(i): Jan 1 Y3 debit to Fair value adjustment (to bring to sale-date FV)", "value": n(adj_s)},
 {"label": "g(i): Jan 1 Y3 unrealized holding gain recognized in OCI", "value": n(adj_s)},
 {"label": "g(i): Fair value adjustment balance immediately before sale (debit)", "value": n(fva_s)},
 {"label": "g(ii): Cash received on sale", "value": n(proceeds)},
 {"label": "g(ii): Investment in bonds removed (at amortized cost)", "value": n(amort_cost)},
 {"label": "g(ii): Fair value adjustment eliminated (credit)", "value": n(fva_s)},
 {"label": "g(ii): Reclassification adjustment out of AOCI (debit OCI)", "value": n(reclass)},
 {"label": "g(ii): Realized gain on sale reported in net income", "value": n(gain_on_sale)},

 {"label": "h: AOCI balance brought forward Jan 1 Year 3 (credit)", "value": n(aoci_y2)},
 {"label": "h: Add sale-date unrealized holding gain in OCI", "value": n(adj_s)},
 {"label": "h: AOCI immediately before reclassification (credit)", "value": n(aoci_pre_sale)},
 {"label": "h: Less reclassification adjustment to net income", "value": n(-reclass)},
 {"label": "h: AOCI balance after the sale (Year 3)", "value": n(aoci_end_y3)},
]

def L(acct, dr=None, cr=None):
    return {"account": acct, "debit": n(dr) if dr is not None else 0,
            "credit": n(cr) if cr is not None else 0}

jes = [
 {"part": "a", "lines": [L("Investment in Oakmont Industries bonds (AFS / FV-OCI)", dr=purch_cost),
                          L("Cash", cr=purch_cost)]},
 {"part": "b", "lines": [L("Cash", dr=cash_int), L("Interest income", cr=cash_int)]},
 {"part": "d", "lines": [L("Unrealized holding loss — OCI", dr=-adj_y1),
                          L("Fair value adjustment (AFS / FV-OCI investment)", cr=-adj_y1)]},
 {"part": "f", "lines": [L("Fair value adjustment (AFS / FV-OCI investment)", dr=adj_y2),
                          L("Unrealized holding gain — OCI", cr=adj_y2)]},
 {"part": "g(i)", "lines": [L("Fair value adjustment (AFS / FV-OCI investment)", dr=adj_s),
                             L("Unrealized holding gain — OCI", cr=adj_s)]},
 {"part": "g(ii) sale / eliminate FVA", "lines": [
     L("Cash", dr=proceeds),
     L("Investment in Oakmont Industries bonds (AFS / FV-OCI)", cr=amort_cost),
     L("Fair value adjustment (AFS / FV-OCI investment)", cr=fva_s)]},
 {"part": "g(ii) reclassification from AOCI to net income", "lines": [
     L("Unrealized holding gain — OCI (reclassification adjustment)", dr=reclass),
     L("Gain on sale of investments (net income)", cr=gain_on_sale)]},
]

for je in jes:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert d == c, (je["part"], d, c)

print(json.dumps({
 "id": "agent_135#01",
 "rounding_convention": "decimal.Decimal throughout; every amount quantized to 0.01 with ROUND_HALF_UP at each period (per-period rounding). Bonds purchased at par, so amortized cost = $55,000 at all dates and no premium/discount amortization occurs.",
 "answers": answers,
 "journal_entries": jes,
 "fva_schedule": rows,
 "insufficient_info": False,
 "notes": "Purchase at par means the FV-OCI (AFS) fair value adjustment account is measured against a constant $55,000 amortized cost. Cumulative AOCI: (2,750) at Dec 31 Y1, 2,200 at Dec 31 Y2, 2,750 just before sale; the full 2,750 is recycled to net income as the realized gain on sale (proceeds 57,750 less amortized cost 55,000), leaving AOCI nil. Sale-date entries are shown as two entries (sale-date FV-OCI adjust and reclass are separable); combining them yields the same net effect. The FVA elimination credit of 2,750 plus the 55,000 investment credit exactly offsets the 57,750 cash debit, so no gain arises in the disposal entry itself — the gain comes from the reclassification entry."
}, indent=1))
