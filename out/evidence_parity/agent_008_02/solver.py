"""Solver for agent_008#02 - Multi-security FVA schedule after mid-year disposal.

Rounding convention: all money handled with decimal.Decimal quantized to
$0.01 using ROUND_HALF_UP, applied once per period (per computed figure at
the end of each computation); no floats are used anywhere in the math.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
def q(x): return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)

# ---- Given data -------------------------------------------------------
# FVA-TS opening balance: credit 3,200 -> signed (debit-positive) = -3,200
fva_open_credit = q("3200")
fva_open_signed = -fva_open_credit

crest_cost = q("35000")
crest_proceeds = q("33800")

held = [("Dune 5% bonds", q("25000"), q("24100")),
        ("Pier 4% bonds", q("60000"), q("61500"))]

# ---- a. June 12 sale (period-end-only method: no FVA touched on sale) --
gain_loss_sale = q(crest_proceeds - crest_cost)          # negative = loss
loss_sale = q(-gain_loss_sale)

# ---- b. Year-end schedule --------------------------------------------
rows = []
tot_cost = Decimal("0")
tot_fv = Decimal("0")
for name, cost, fv in held:
    diff = q(fv - cost)
    rows.append((name, cost, fv, diff))
    tot_cost = q(tot_cost + cost)
    tot_fv = q(tot_fv + fv)
tot_diff = q(tot_fv - tot_cost)          # required FVA balance, debit-positive
required_fva_signed = tot_diff
adjustment_signed = q(required_fva_signed - fva_open_signed)   # + = debit FVA

# ---- c/e. Adjusting entry and income effects --------------------------
unrealized_gain = adjustment_signed        # positive => gain
net_income_effect = q(gain_loss_sale + unrealized_gain)

# ---- d. Balance sheet presentation ------------------------------------
bs_cost = tot_cost
bs_fva = required_fva_signed
bs_carrying = q(bs_cost + bs_fva)

def num(d):
    d = q(d)
    return int(d) if d == d.to_integral_value() else float(d)

answers = [
    {"label": "a: Loss on sale of trading securities (Crest), June 12", "value": num(loss_sale)},
    {"label": "a: Cash received on Crest sale", "value": num(crest_proceeds)},
    {"label": "a: Investment in TS (Crest) removed at amortized cost", "value": num(crest_cost)},
    {"label": "b: Dune 5% bonds - amortized cost", "value": num(rows[0][1])},
    {"label": "b: Dune 5% bonds - fair value 12/31/Y2", "value": num(rows[0][2])},
    {"label": "b: Dune 5% bonds - unrealized (FV - cost)", "value": num(rows[0][3])},
    {"label": "b: Pier 4% bonds - amortized cost", "value": num(rows[1][1])},
    {"label": "b: Pier 4% bonds - fair value 12/31/Y2", "value": num(rows[1][2])},
    {"label": "b: Pier 4% bonds - unrealized (FV - cost)", "value": num(rows[1][3])},
    {"label": "b: Total remaining portfolio - amortized cost", "value": num(tot_cost)},
    {"label": "b: Total remaining portfolio - fair value", "value": num(tot_fv)},
    {"label": "b: Required Fair Value Adjustment-TS ending balance (debit)", "value": num(required_fva_signed)},
    {"label": "b: Existing Fair Value Adjustment-TS balance 1/1/Y2 (credit)", "value": num(fva_open_credit)},
    {"label": "b: Required change in Fair Value Adjustment-TS (debit)", "value": num(adjustment_signed)},
    {"label": "c: Debit Fair Value Adjustment-TS", "value": num(adjustment_signed)},
    {"label": "c: Credit Unrealized Holding Gain or Loss-Income", "value": num(unrealized_gain)},
    {"label": "d: Investment in trading securities, at amortized cost (current asset)", "value": num(bs_cost)},
    {"label": "d: Add: Fair Value Adjustment-TS (debit balance)", "value": num(bs_fva)},
    {"label": "d: Investment in trading securities, at fair value", "value": num(bs_carrying)},
    {"label": "e(i): Income statement effect of Crest sale (realized loss)", "value": num(gain_loss_sale)},
    {"label": "e(ii): Income statement effect of 12/31 FVA adjustment (unrealized gain)", "value": num(unrealized_gain)},
    {"label": "e: Net Year 2 income statement effect", "value": num(net_income_effect)},
]

jes = [
    {"part": "a", "lines": [
        {"account": "Cash", "debit": num(crest_proceeds), "credit": 0},
        {"account": "Loss on Sale of Trading Securities", "debit": num(loss_sale), "credit": 0},
        {"account": "Investment in Trading Securities (Crest 4.5% bonds)", "debit": 0, "credit": num(crest_cost)},
    ]},
    {"part": "c", "lines": [
        {"account": "Fair Value Adjustment-Trading Securities", "debit": num(adjustment_signed), "credit": 0},
        {"account": "Unrealized Holding Gain or Loss-Income", "debit": 0, "credit": num(unrealized_gain)},
    ]},
]

for je in jes:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert q(d) == q(c), (je["part"], d, c)

out = {
    "id": "agent_008#02",
    "rounding_convention": "decimal.Decimal, ROUND_HALF_UP to $0.01, applied once per period/computed figure; no floats in the math",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": ("Period-end-only method: the June 12 sale is recorded against amortized cost with no "
              "entry to Fair Value Adjustment-TS, so the realized loss is 33,800 - 35,000 = (1,200). "
              "At 12/31/Y2 the remaining portfolio needs a debit FVA balance of 600 (85,600 - 85,000); "
              "the account starts with a 3,200 credit, so a 3,800 debit adjustment is required, "
              "recognizing a 3,800 unrealized holding gain in income. Net Year 2 effect = 3,800 - 1,200 = 2,600 increase.")
}
print(json.dumps(out, indent=1))
