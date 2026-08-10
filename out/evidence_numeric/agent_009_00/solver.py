"""Cascade Peaks AFS full life cycle (Appendix 14B / LO 14-8 period-end-only FV method).

ROUNDING CONVENTION: all money is decimal.Decimal (never float); every computed
amount is quantized to the cent with ROUND_HALF_UP once per period/entry.
The bonds are bought at par, so amortized cost stays at face and no
discount/premium schedule exists; every figure resolves to an exact whole
dollar. The Fair Value Adjustment account is closed exactly to the required
$0 balance at Dec 31, Year 3 (schedule closes to zero, not plugged).
Every figure is derived from the fact pattern below; nothing is hard-coded.
Dr = Cr is asserted on every entry.
"""
import json
from decimal import Decimal as D, ROUND_HALF_UP

CENT = D("0.01")
def q(x):  # one ROUND_HALF_UP per computed amount
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)
def n(x):
    v = q(x)
    return int(v) if v == v.to_integral_value() else float(v)

# ---- given facts (inputs only) -------------------------------------------
face        = D("40000")
price       = face                 # "purchased for par"
coupon      = D("0.07")            # annual stated rate
per_year    = D("2")               # semiannual coupons (Jun 30 / Dec 31)
fv_y1       = D("37600")
fv_y2       = D("41200")
proceeds    = D("42000")           # Jan 1, Yr 3 sale, no accrued interest
fva_begin   = D("0")
aoci_begin  = D("0")
fva_req_y3  = D("0")               # no AFS remains at Dec 31, Yr 3

# ---- derived -------------------------------------------------------------
semi_int    = q(face * coupon / per_year)              # 1,400 per coupon date
amort_cost  = q(price)                                 # par purchase -> no amortization

# (c) Dec 31 Yr 1
fva_req_y1  = q(fv_y1 - amort_cost)                    # -2,400 (credit)
fva_adj_y1  = q(fva_req_y1 - fva_begin)                # -2,400 OCI loss
carry_y1    = q(amort_cost + fva_req_y1)               # 37,600
aoci_y1     = q(aoci_begin + fva_adj_y1)               # -2,400
int_rev_y1  = semi_int                                 # one coupon period (Jul 1 - Dec 31)

# (e) Dec 31 Yr 2 bridge
fva_exist_y2 = fva_req_y1
fva_req_y2   = q(fv_y2 - amort_cost)                   # +1,200 (debit)
fva_adj_y2   = q(fva_req_y2 - fva_exist_y2)            # +3,600 OCI gain
aoci_y2      = q(aoci_y1 + fva_adj_y2)                 # +1,200

# (f) Jan 1 Yr 3 sale - period-end-only: FVA untouched at sale date
gain_sale    = q(proceeds - amort_cost)                # realized vs amortized cost

# (g) Dec 31 Yr 3 elimination of FVA
fva_exist_y3 = fva_req_y2
fva_adj_y3   = q(fva_req_y3 - fva_exist_y3)            # -1,200 (closes FVA to exactly 0)
assert q(fva_exist_y3 + fva_adj_y3) == fva_req_y3 == D("0")

# (h) Year 3 AOCI reconciliation
aoci_y3_beg  = aoci_y2
reclass_y3   = q(-aoci_y3_beg)                         # entire prior AOCI realized on sale
unreal_y3    = q(fva_adj_y3 - reclass_y3)              # residual current-period unrealized
aoci_y3_end  = q(aoci_y3_beg + unreal_y3 + reclass_y3)
assert aoci_y3_end == D("0")

INV  = "Debt Investments-Available-for-Sale (Meridian 7% bonds)"
FVA  = "Fair Value Adjustment-Available-for-Sale"
UHGL = "Unrealized Holding Gain or Loss-OCI"

def je(part, lines):
    dr = sum((D(str(l["debit"])) for l in lines), D("0"))
    cr = sum((D(str(l["credit"])) for l in lines), D("0"))
    assert dr == cr, (part, dr, cr)
    return {"part": part, "lines": lines}

def L(acct, dr=D("0"), cr=D("0")):
    return {"account": acct, "debit": n(dr), "credit": n(cr)}

jes = [
    je("a", [L(INV, dr=price), L("Cash", cr=price)]),
    je("b", [L("Cash", dr=semi_int), L("Interest Revenue", cr=semi_int)]),
    je("c", [L(UHGL, dr=-fva_adj_y1), L(FVA, cr=-fva_adj_y1)]),
    je("e", [L(FVA, dr=fva_adj_y2), L(UHGL, cr=fva_adj_y2)]),
    je("f", [L("Cash", dr=proceeds), L(INV, cr=amort_cost),
             L("Gain on Sale of Investments", cr=gain_sale)]),
    je("g", [L(UHGL, dr=-fva_adj_y3), L(FVA, cr=-fva_adj_y3)]),
]

answers = [
    {"label": "d: Dec 31, Year 1 balance sheet carrying amount of AFS investment (amortized cost 40,000 + FVA -2,400 = fair value)", "value": n(carry_y1)},
    {"label": "d: Dec 31, Year 1 Accumulated OCI related to these bonds (negative = debit balance / net unrealized loss)", "value": n(aoci_y1)},
    {"label": "d: Year 1 interest revenue (one semiannual coupon, Jul 1-Dec 31)", "value": n(int_rev_y1)},
    {"label": "d: Year 1 OCI unrealized holding gain (loss) (negative = loss)", "value": n(fva_adj_y1)},
    {"label": "e: FVA bridge - required FVA balance at Dec 31, Year 2 (positive = debit)", "value": n(fva_req_y2)},
    {"label": "e: FVA bridge - existing FVA balance before adjustment (negative = credit)", "value": n(fva_exist_y2)},
    {"label": "e: FVA bridge - Dec 31, Year 2 adjustment needed (positive = debit FVA, credit OCI)", "value": n(fva_adj_y2)},
    {"label": "h: Year 3 AOCI reconciliation - beginning AOCI, Jan 1, Year 3 (positive = credit / net unrealized gain)", "value": n(aoci_y3_beg)},
    {"label": "h: Year 3 AOCI reconciliation - current-period unrealized holding gain (loss) in OCI", "value": n(unreal_y3)},
    {"label": "h: Year 3 AOCI reconciliation - reclassification adjustment to net income (negative = removed from AOCI)", "value": n(reclass_y3)},
    {"label": "h: Year 3 AOCI reconciliation - ending AOCI, Dec 31, Year 3", "value": n(aoci_y3_end)},
]

notes = (
    "Bonds bought at par, so amortized cost = $40,000 throughout and interest revenue = cash interest "
    "($40,000 x 7% x 6/12 = $1,400 per coupon date). (c) FVA required -2,400 vs 0 existing -> credit FVA 2,400. "
    "(e) required +1,200 vs existing -2,400 -> debit FVA 3,600. (f) Period-end-only method: FVA and OCI are NOT "
    "touched at the Jan 1, Year 3 sale date; the realized gain is proceeds 42,000 - amortized cost 40,000 = 2,000 "
    "to net income. (g) At Dec 31, Year 3 the remaining 1,200 debit FVA is eliminated (debit OCI 1,200), closing "
    "the account exactly to the required $0. (h) That 1,200 OCI debit is entirely the reclassification adjustment "
    "for the previously recognized unrealized gain now realized in net income; no current-period unrealized amount "
    "arises because nothing was held at any period end during Year 3, so ending AOCI = 0."
)

print(json.dumps({
    "id": "agent_009#00",
    "rounding_convention": ("decimal.Decimal only (no floats); every amount quantized to the cent with "
                            "ROUND_HALF_UP once per period/entry; par purchase means no discount/premium "
                            "amortization, so all figures are exact whole dollars; the Fair Value Adjustment "
                            "schedule is closed exactly to the required $0 balance at Dec 31, Year 3 (no plug)"),
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
