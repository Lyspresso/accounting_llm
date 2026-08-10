"""Q1 agent_007#00 - AFS debt security impairment (CECL for AFS, LO 14-6).

Rounding convention: all money is decimal.Decimal, quantized to whole dollars
with ROUND_HALF_UP applied per period (per scenario / per measurement date).
No floats anywhere. Every figure is derived from the fact-pattern inputs.

Model applied (AFS debt security, no intent to sell and not more likely than
not required to sell before recovery):
  1. fair-value shortfall = amortized cost - fair value  (floored at zero)
  2. credit-loss estimate = amortized cost - PV of cash flows expected (given)
  3. allowance for credit losses recognized in NET INCOME
       = min(credit-loss estimate, fair-value shortfall)
     i.e. the credit loss is LIMITED to the amount by which fair value is
     below amortized cost. Any remaining decline (noncredit) stays in AOCI.
  4. paired reclassification: because the credit portion is now in net income
     via the allowance, the same amount of previously recorded FV-OCI loss is
     reclassified out of OCI (Dr Fair Value Adjustment-AFS, Cr Unrealized
     Gain or Loss-OCI), leaving only the noncredit decline in AOCI.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENTS = Decimal("1")
def r(x):  # per-period ROUND_HALF_UP to whole dollars
    return Decimal(x).quantize(CENTS, rounding=ROUND_HALF_UP)

def d(x):
    return float(x)  # JSON display only; all arithmetic done in Decimal

AC = r("80000")                      # amortized cost, Dec 31, all scenarios
CREDIT_EST = r("12000")              # expected loss due to credit factors
FV = {"A": r("85000"), "B": r("72000"), "C": r("65000")}

answers, jes = [], []
res = {}
for s in ("A", "B", "C"):
    fv = FV[s]
    decline = r(AC - fv)                             # + = FV below AC
    shortfall = decline if decline > 0 else r("0")   # FV shortfall (cap)
    credit = CREDIT_EST
    recognized = shortfall if shortfall < credit else credit   # min()
    noncredit = r(shortfall - recognized)
    res[s] = dict(fv=fv, shortfall=shortfall, credit=credit,
                  recognized=recognized, noncredit=noncredit)

    if s == "A":
        limit_note = ("cap = $0 (FV $%s exceeds amortized cost by $%s); "
                      "the FV-shortfall limit binds, no impairment") % (
                      fv, r(fv - AC))
    elif shortfall < credit:
        limit_note = "cap = FV shortfall $%s < credit estimate $%s; limit binds" % (shortfall, credit)
    else:
        limit_note = "cap = FV shortfall $%s > credit estimate $%s; credit estimate governs" % (shortfall, credit)

    answers.append({"label": "a: Scenario %s - fair-value shortfall (amortized cost - fair value, floor $0)" % s,
                    "value": d(shortfall)})
    answers.append({"label": "a: Scenario %s - credit-loss amount (expected loss due to credit factors)" % s,
                    "value": d(credit)})
    answers.append({"label": "a: Scenario %s - limit applied (max loss recognizable in net income = FV shortfall); %s" % (s, limit_note),
                    "value": d(shortfall)})
    answers.append({"label": "a: Scenario %s - impairment loss recognized in net income, Year 1" % s,
                    "value": d(recognized)})

    if recognized == 0:
        jes.append({"part": "b", "lines": [
            {"account": "Scenario A - no entry required (fair value $%s exceeds amortized cost $%s; no impairment)" % (FV["A"], AC),
             "debit": 0, "credit": 0}]})
    else:
        jes.append({"part": "b", "lines": [
            {"account": "Scenario %s - Credit Loss Expense (Impairment Loss on Investments) [net income]" % s,
             "debit": d(recognized), "credit": 0},
            {"account": "Scenario %s -   Allowance for Credit Losses - AFS Debt Investment" % s,
             "debit": 0, "credit": d(recognized)},
            {"account": "Scenario %s - Fair Value Adjustment - AFS (paired reclassification of credit portion out of OCI)" % s,
             "debit": d(recognized), "credit": 0},
            {"account": "Scenario %s -   Unrealized Gain or Loss - OCI" % s,
             "debit": 0, "credit": d(recognized)}]})

# ---- part c: Scenario C balance sheet after the impairment entry ----
c = res["C"]
pre_fva = r(-(AC - c["fv"]))                 # FVA balance before impairment entry (credit -15,000)
post_fva = r(pre_fva + c["recognized"])      # + Dr of reclassified credit portion
allowance = r(-c["recognized"])              # contra (credit balance)
net = r(AC + allowance + post_fva)
aoci_noncredit = c["noncredit"]

answers += [
 {"label": "c: Scenario C - amortized cost", "value": d(AC)},
 {"label": "c: Scenario C - less Allowance for Credit Losses", "value": d(allowance)},
 {"label": "c: Scenario C - Fair Value Adjustment - AFS balance after entry (credit)", "value": d(post_fva)},
 {"label": "c: Scenario C - net carrying amount of the investment on the balance sheet", "value": d(net)},
 {"label": "c: Scenario C - noncredit portion of the decline remaining in AOCI (unrealized loss)", "value": d(aoci_noncredit)},
]

# ---- internal checks ----
assert net == c["fv"], "Scenario C must carry at fair value 65,000"
assert r(c["recognized"] + aoci_noncredit) == c["shortfall"], "credit + noncredit must equal total decline"
for je in jes:
    assert r(sum(Decimal(str(l["debit"])) for l in je["lines"])) == \
           r(sum(Decimal(str(l["credit"])) for l in je["lines"])), "Dr must equal Cr"

notes = ("Scenario A: FV $85,000 exceeds amortized cost $80,000, so the FV shortfall is $0 and the "
         "$12,000 credit estimate is fully limited out - no impairment loss and no entry (the security "
         "stays at FV with a $5,000 unrealized gain in AOCI). "
         "Scenario B: shortfall $8,000 < credit estimate $12,000, so net income takes only $8,000 (the "
         "FV-shortfall limit binds); nothing remains in AOCI. "
         "Scenario C: shortfall $15,000 > credit estimate $12,000, so the $12,000 credit estimate governs "
         "and the $3,000 noncredit decline stays in AOCI. "
         "Entries assume Northridge does not intend to sell and is not more likely than not required to "
         "sell before recovery, so only the credit portion hits net income. The FV-OCI restatement to fair "
         "value (LO 14-3) was already recorded, so the second pair of lines only reclassifies the credit "
         "portion out of OCI. All amounts are whole dollars as given; ROUND_HALF_UP to whole dollars was "
         "applied per scenario and no rounding difference arose - each scenario closes exactly to fair value.")

print(json.dumps({"id": "agent_007#00",
                  "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP quantized to whole dollars per period (per scenario); journal entries in whole dollars; each scenario closes exactly to fair value",
                  "answers": answers,
                  "journal_entries": jes,
                  "insufficient_info": False,
                  "notes": notes}, indent=1))
