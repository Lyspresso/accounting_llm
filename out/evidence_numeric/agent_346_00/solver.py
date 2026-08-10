"""Q1 agent_346#00 -- Held-for-sale (ASC 360-10) life cycle solver.

Rounding convention: all amounts are exact whole dollars in the source data;
every computation uses decimal.Decimal with ROUND_HALF_UP quantized to the
cent (0.01) and presented in whole dollars.  No present values are involved,
so no schedule-closing plug is needed; the subsequent-measurement schedule
closes exactly (cumulative HFS impairment removed on disposal equals the
valuation-allowance balance carried at the disposal date).  Nothing is
hard-coded: every figure is derived from the scenario inputs below.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def n(x):  # JSON-friendly number (whole dollars when exact)
    x = q(x)
    return int(x) if x == x.to_integral_value() else float(x)

# ---------------- inputs ----------------
cost            = q("90000")
accum_dep_y1    = q("35000")
fv_y1           = q("48000")
cts_y1          = q("3000")
fv_y2           = q("52000")
cts_y2          = q("3000")
proceeds_y3     = q("51000")
selling_cost_y3 = q("2500")

ZERO = q("0")

# ---------------- (a) classification date, Dec 31 Year 1 ----------------
ca_before_y1 = q(cost - accum_dep_y1)          # carrying amount before HFS adj
nrv_y1       = q(fv_y1 - cts_y1)               # FV - costs to sell
ceiling      = ca_before_y1                    # CA at classification (no dep. after HFS)
meas_y1      = min(ca_before_y1, nrv_y1)       # lower of CA and FV - CTS
impair_y1    = q(ca_before_y1 - meas_y1)       # initial write-down (loss if > 0)
ca_after_y1  = meas_y1
cum_after_y1 = impair_y1

# ---------------- (c) Dec 31 Year 2 remeasurement ----------------
ca_before_y2 = ca_after_y1
nrv_y2       = q(fv_y2 - cts_y2)
# gain (recovery) limited to cumulative HFS impairment previously recognized;
# further loss unlimited.  Measurement also capped by the ceiling.
target_y2    = min(nrv_y2, ceiling, q(ca_before_y2 + cum_after_y1))
adj_y2       = q(target_y2 - ca_before_y2)     # + = recovery gain, - = further loss
ca_after_y2  = q(ca_before_y2 + adj_y2)
cum_after_y2 = q(cum_after_y1 - adj_y2)

# ---------------- (d) disposal, March 15 Year 3 ----------------
ca_at_sale   = ca_after_y2
net_cash     = q(proceeds_y3 - selling_cost_y3)
gain_on_sale = q(net_cash - ca_at_sale)        # negative => loss
loss_on_sale = q(-gain_on_sale) if gain_on_sale < 0 else ZERO
allowance_at_sale = cum_after_y2               # valuation allowance balance removed

# ---------------- journal entries ----------------
jes = []
if impair_y1 > 0:
    jes.append({"part": "a", "date": "Dec 31, Year 1",
                "description": "Initial HFS write-down to fair value less costs to sell",
                "lines": [
        {"account": "Loss on impairment - asset held for sale", "debit": n(impair_y1), "credit": 0},
        {"account": "Allowance to reduce held-for-sale asset to fair value less cost to sell",
         "debit": 0, "credit": n(impair_y1)}]})

if adj_y2 > 0:
    jes.append({"part": "c", "date": "Dec 31, Year 2",
                "description": "Period-end recovery of previously recognized HFS impairment (limited to cumulative loss)",
                "lines": [
        {"account": "Allowance to reduce held-for-sale asset to fair value less cost to sell",
         "debit": n(adj_y2), "credit": 0},
        {"account": "Recovery of impairment loss - asset held for sale", "debit": 0, "credit": n(adj_y2)}]})
elif adj_y2 < 0:
    jes.append({"part": "c", "date": "Dec 31, Year 2",
                "description": "Period-end additional HFS write-down",
                "lines": [
        {"account": "Loss on impairment - asset held for sale", "debit": n(-adj_y2), "credit": 0},
        {"account": "Allowance to reduce held-for-sale asset to fair value less cost to sell",
         "debit": 0, "credit": n(-adj_y2)}]})

d_lines = [
    {"account": "Cash (proceeds $%s less selling costs paid $%s)" % (n(proceeds_y3), n(selling_cost_y3)),
     "debit": n(net_cash), "credit": 0},
    {"account": "Accumulated depreciation - milling machine", "debit": n(accum_dep_y1), "credit": 0},
    {"account": "Allowance to reduce held-for-sale asset to fair value less cost to sell",
     "debit": n(allowance_at_sale), "credit": 0},
]
if gain_on_sale < 0:
    d_lines.append({"account": "Loss on sale of asset held for sale", "debit": n(-gain_on_sale), "credit": 0})
d_lines.append({"account": "Milling machine (equipment)", "debit": 0, "credit": n(cost)})
if gain_on_sale > 0:
    d_lines.append({"account": "Gain on sale of asset held for sale", "debit": 0, "credit": n(gain_on_sale)})
jes.append({"part": "d", "date": "March 15, Year 3", "description": "Disposal of held-for-sale milling machine",
            "lines": d_lines})

for je in jes:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, (je, dr, cr)

# schedule closes exactly: allowance removed == cumulative impairment balance
assert q(cum_after_y1 - adj_y2) == allowance_at_sale
assert q(cost - accum_dep_y1 - allowance_at_sale) == ca_at_sale

ans = [
 {"label": "a: Carrying amount before HFS adjustment, Dec 31 Year 1 (cost $90,000 - accum. dep. $35,000)", "value": n(ca_before_y1)},
 {"label": "a: Fair value less costs to sell, Dec 31 Year 1 ($48,000 - $3,000)", "value": n(nrv_y1)},
 {"label": "a: Initial HFS impairment loss recognized Dec 31 Year 1", "value": n(impair_y1)},
 {"label": "a: Adjusted carrying amount of HFS asset, Dec 31 Year 1", "value": n(ca_after_y1)},
 {"label": "a: Balance-sheet classification", "value": "Current asset - reported separately as 'Milling machine held for sale, net' at $%s (cost $%s less accumulated depreciation $%s less valuation allowance $%s); depreciation ceases at classification" % (n(ca_after_y1), n(cost), n(accum_dep_y1), n(impair_y1))},

 {"label": "b: Row 1 (Dec 31, Year 1 - classification) carrying amount before adjustment", "value": n(ca_before_y1)},
 {"label": "b: Row 1 (Dec 31, Year 1) FV - CTS", "value": n(nrv_y1)},
 {"label": "b: Row 1 (Dec 31, Year 1) ceiling (carrying amount at classification date)", "value": n(ceiling)},
 {"label": "b: Row 1 (Dec 31, Year 1) adjustment - impairment loss (decrease)", "value": n(-impair_y1)},
 {"label": "b: Row 1 (Dec 31, Year 1) carrying amount after adjustment", "value": n(ca_after_y1)},
 {"label": "b: Row 1 (Dec 31, Year 1) cumulative HFS impairment", "value": n(cum_after_y1)},

 {"label": "b: Row 2 (Dec 31, Year 2) carrying amount before adjustment", "value": n(ca_before_y2)},
 {"label": "b: Row 2 (Dec 31, Year 2) FV - CTS ($52,000 - $3,000)", "value": n(nrv_y2)},
 {"label": "b: Row 2 (Dec 31, Year 2) ceiling (carrying amount at classification date)", "value": n(ceiling)},
 {"label": "b: Row 2 (Dec 31, Year 2) adjustment - recovery gain (increase, capped at cumulative impairment)", "value": n(adj_y2)},
 {"label": "b: Row 2 (Dec 31, Year 2) carrying amount after adjustment", "value": n(ca_after_y2)},
 {"label": "b: Row 2 (Dec 31, Year 2) cumulative HFS impairment", "value": n(cum_after_y2)},

 {"label": "b: Row 3 (Mar 15, Year 3 - disposal) carrying amount at disposal", "value": n(ca_at_sale)},
 {"label": "b: Row 3 (Mar 15, Year 3) net proceeds (FV realized less costs to sell)", "value": n(net_cash)},
 {"label": "b: Row 3 (Mar 15, Year 3) ceiling (carrying amount at classification date)", "value": n(ceiling)},
 {"label": "b: Row 3 (Mar 15, Year 3) adjustment - loss on sale", "value": n(gain_on_sale)},
 {"label": "b: Row 3 (Mar 15, Year 3) carrying amount after disposal", "value": n(ZERO)},
 {"label": "b: Row 3 (Mar 15, Year 3) cumulative HFS impairment removed on disposal", "value": n(allowance_at_sale)},

 {"label": "c: Dec 31 Year 2 recovery of impairment recognized (gain)", "value": n(adj_y2)},
 {"label": "c: Adjusted carrying amount after Dec 31 Year 2 entry", "value": n(ca_after_y2)},

 {"label": "d: Cash proceeds received Mar 15 Year 3", "value": n(proceeds_y3)},
 {"label": "d: Selling costs paid in cash Mar 15 Year 3", "value": n(selling_cost_y3)},
 {"label": "d: Net cash inflow at closing", "value": n(net_cash)},
 {"label": "d: Loss on sale of held-for-sale asset", "value": n(loss_on_sale)},
]

out = {
 "id": "agent_346#00",
 "rounding_convention": "decimal.Decimal throughout, ROUND_HALF_UP quantized to the cent each period and presented in whole dollars; all inputs are exact whole dollars so no rounding differences arise and no plug is used. The subsequent-measurement schedule closes exactly to zero carrying amount on disposal, with the valuation allowance removed equal to the cumulative HFS impairment balance ($%s).",
 "answers": ans,
 "journal_entries": jes,
 "insufficient_info": False,
 "notes": ("ASC 360-10-35-43/45: on classification the asset is measured at the lower of carrying amount ($%s) "
           "and fair value less cost to sell ($%s), and depreciation ceases. Subsequent gains are recognized only "
           "to the extent of cumulative losses previously recognized under the HFS model, so the Dec 31 Year 2 "
           "increase in FV-CTS from $%s to $%s ($%s) is fully recognized because cumulative impairment was $%s; "
           "carrying amount is capped by the $%s ceiling (carrying amount at classification, unadjusted since no "
           "depreciation would have been taken). Write-downs are carried in a valuation allowance rather than "
           "credited directly to the asset, so cost and accumulated depreciation are both removed at disposal. "
           "Disposal: net cash $%s vs. carrying amount $%s gives a $%s loss on sale.")
          % (n(ca_before_y1), n(nrv_y1), n(nrv_y1), n(nrv_y2), n(adj_y2), n(cum_after_y1), n(ceiling),
             n(net_cash), n(ca_at_sale), n(loss_on_sale)),
}
out["rounding_convention"] = out["rounding_convention"] % (n(allowance_at_sale),)
print(json.dumps(out, indent=1))
