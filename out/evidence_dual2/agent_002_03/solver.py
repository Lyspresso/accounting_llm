"""Solver for agent_002#03 — HTM -> AFS transfer (Jan 1 Y4) and Dec 31 Y4 AFS FV adjustment.

Rounding convention: all money is decimal.Decimal; every computed amount is quantized to
whole dollars using ROUND_HALF_UP once per period (no float arithmetic anywhere).
Bonds were bought at par, so amortized cost is constant at par -- no discount/premium
schedule exists; nothing to close to face beyond par itself.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("1")
def r(x): return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)

# ---- given fact pattern (inputs only) ----
port = {
    "Quill Corp. bonds":    {"amort_cost": Decimal("90000"), "fv_y3": Decimal("96300"), "fv_y4": Decimal("94000")},
    "Dune Partners bonds":  {"amort_cost": Decimal("60000"), "fv_y3": Decimal("55800"), "fv_y4": Decimal("57000")},
}

# ---- derived totals ----
tot_cost   = r(sum(s["amort_cost"] for s in port.values()))          # carrying amount of HTM at transfer
tot_fv_x   = r(sum(s["fv_y3"]      for s in port.values()))          # fair value at transfer date 1/1/Y4
tot_fv_y4  = r(sum(s["fv_y4"]      for s in port.values()))          # fair value at 12/31/Y4

xfer_ugl   = r(tot_fv_x - tot_cost)                                   # net unrealized gain at transfer -> OCI
assert xfer_ugl == r(sum(r(s["fv_y3"] - s["amort_cost"]) for s in port.values()))

# Transfer HTM->AFS is at fair value; the unrealized holding gain/loss at the transfer
# date is recognized in OCI (equity), never in net income.
ni_effect_transfer  = r(Decimal("0"))
oci_effect_transfer = xfer_ugl

# ---- 12/31/Y4 AFS valuation ----
# Bonds at par => amortized cost unchanged at 150,000 (no amortization, no interest accrual asked).
required_fva = r(tot_fv_y4 - tot_cost)        # required debit balance in Fair Value Adjustment (AFS)
existing_fva = xfer_ugl                       # debit balance carried over from the transfer entry
fva_change   = r(required_fva - existing_fva) # negative => credit FVA / debit OCI

adj_amt   = r(abs(fva_change))
adj_is_cr = fva_change < 0

def je(part, lines):
    d = r(sum(l["debit"] for l in lines)); c = r(sum(l["credit"] for l in lines))
    assert d == c, (part, d, c)
    return {"part": part, "lines": [{"account": l["account"], "debit": str(r(l["debit"])), "credit": str(r(l["credit"]))} for l in lines]}

Z = Decimal("0")
jes = [
    je("a", [  # (1) reclassify the portfolio out of HTM at its carrying (amortized-cost) amount
        {"account": "Debt Investments - Available-for-Sale (AFS)", "debit": tot_cost, "credit": Z},
        {"account": "Debt Investments - Held-to-Maturity (HTM)",   "debit": Z,        "credit": tot_cost},
    ]),
    je("a", [  # (2) bring the AFS portfolio to transfer-date fair value, gain/loss to OCI (not NI)
        {"account": "Fair Value Adjustment (AFS)", "debit": xfer_ugl, "credit": Z},
        {"account": "Unrealized Holding Gain or Loss - Equity (OCI)", "debit": Z, "credit": xfer_ugl},
    ]),
    je("c", [  # 12/31/Y4: move Fair Value Adjustment from 2,100 Dr to required 1,000 Dr
        {"account": "Unrealized Holding Gain or Loss - Equity (OCI)", "debit": adj_amt if adj_is_cr else Z,
         "credit": Z if adj_is_cr else adj_amt},
        {"account": "Fair Value Adjustment (AFS)", "debit": Z if adj_is_cr else adj_amt,
         "credit": adj_amt if adj_is_cr else Z},
    ]),
]

answers = [
    {"label": "a: AFS debt investments recorded at transfer-date fair value (1/1/Y4 total)", "value": str(tot_fv_x)},
    {"label": "a: HTM carrying (amortized cost) amount removed on transfer", "value": str(tot_cost)},
    {"label": "a: net unrealized holding gain at transfer date credited to OCI", "value": str(xfer_ugl)},
    {"label": "b: effect of the transfer on net income", "value": str(ni_effect_transfer)},
    {"label": "b: effect of the transfer on OCI (increase)", "value": str(oci_effect_transfer)},
    {"label": "c: 12/31/Y4 adjustment to Fair Value Adjustment (AFS) - credit / OCI debit", "value": str(adj_amt)},
]

notes = (
    "Transfer HTM->AFS is recorded at fair value on the transfer date; the entire transfer-date "
    "unrealized holding gain/loss goes to OCI and none to net income. Net transfer-date gain = "
    f"{tot_fv_x} FV - {tot_cost} amortized cost = {xfer_ugl} (Quill +6,300; Dune -4,200). "
    "b: NI effect $0; OCI increases $2,100 (AOCI credit 2,100). "
    f"c: bonds were bought at par so amortized cost stays {tot_cost}; 12/31/Y4 total FV = {tot_fv_y4} "
    f"(Quill 94,000 + Dune 57,000), so the Fair Value Adjustment account must show a {required_fva} debit "
    f"balance; it already carries {existing_fva} debit from the transfer, so it is credited {adj_amt} with a "
    f"{adj_amt} debit to Unrealized Holding Gain or Loss - Equity. AOCI ends Year 4 at {required_fva} credit "
    "(net unrealized gain). Whole-dollar ROUND_HALF_UP; all amounts are exact dollars, nothing to force-close. "
    "d: Footnote should disclose (i) the reason for the change in intent - significant deterioration in the "
    "issuers' creditworthiness, which is one of the limited ASC 320 conditions that does not taint the "
    "remaining HTM portfolio; (ii) the amortized cost and fair value of the securities transferred and the "
    "date/circumstances of the transfer; (iii) the net unrealized holding gain of $2,100 recognized in OCI "
    "(accumulated OCI) at the transfer date, with no effect on net income; and (iv) the fact that the "
    "securities are now carried at fair value with subsequent changes reported in OCI."
)

print(json.dumps({
    "id": "agent_002#03",
    "rounding_convention": "decimal.Decimal, ROUND_HALF_UP to whole dollars once per period; bonds at par so amortized cost is constant (no amortization schedule to close)",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
