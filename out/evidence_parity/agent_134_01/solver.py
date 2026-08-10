"""Solver for agent_134#01 — Trading securities (FV-NI), Harborpeak / Redwood 6% bonds.

Rounding convention: all money computed with decimal.Decimal and quantized to
cents using ROUND_HALF_UP, applied once per period/line (no float arithmetic).
Every figure is derived from the stated facts; nothing is hard-coded.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x):
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)

# ---- Given facts ----
par        = Decimal("40000")   # purchased AT PAR -> cost = par, no premium/discount
coupon     = Decimal("0.06")
fv_y1      = Decimal("38500")
fv_y2      = Decimal("41200")
proceeds   = Decimal("41000")   # Jan 1, Yr 3 sale price = sale-date fair value
fva_begin  = Decimal("0")

cost = q(par)
cash_int = q(par * coupon)                       # annual cash interest

# ---- FVA rollforward (TS carried at FV through NI; cost basis never adjusted) ----
req_y1  = q(fv_y1 - cost)                        # required FVA balance end of Yr 1
adj_y1  = q(req_y1 - fva_begin)
bal_y1  = q(fva_begin + adj_y1)

req_y2  = q(fv_y2 - cost)
adj_y2  = q(req_y2 - bal_y1)
bal_y2  = q(bal_y1 + adj_y2)

req_sale = q(proceeds - cost)                    # sale-date required FVA
adj_sale = q(req_sale - bal_y2)
bal_sale = q(bal_y2 + adj_sale)

carry_y1 = q(cost + bal_y1)
carry_y2 = q(cost + bal_y2)
carry_sale = q(cost + bal_sale)

ni_y1 = q(cash_int + adj_y1)                     # Yr 1 total effect on net income
cum_unreal = q(adj_y1 + adj_y2 + adj_sale)
proof = q(proceeds - cost)
gain_on_sale = q(proceeds - carry_sale)          # zero: carrying = FV at sale

answers = [
 {"label": "a: Debit Investment in Trading Securities (cost, at par), Jan 1 Yr 1", "value": cost},
 {"label": "a: Credit Cash, Jan 1 Yr 1", "value": cost},
 {"label": "b: Cash interest received Dec 31 Yr 1 ($40,000 x 6%)", "value": cash_int},
 {"label": "b: Interest income recognized Yr 1", "value": cash_int},
 {"label": "c: FVA schedule Yr 1 - cost basis of TS", "value": cost},
 {"label": "c: FVA schedule Yr 1 - fair value Dec 31 Yr 1", "value": q(fv_y1)},
 {"label": "c: FVA schedule Yr 1 - required FVA balance (credit/negative)", "value": req_y1},
 {"label": "c: FVA schedule Yr 1 - existing FVA balance before adjustment", "value": fva_begin},
 {"label": "c: FVA schedule Yr 1 - adjustment needed (credit FVA / unrealized loss)", "value": adj_y1},
 {"label": "c: FVA schedule Yr 1 - ending FVA balance", "value": bal_y1},
 {"label": "d: BS Yr 1 - Investment in trading securities at cost", "value": cost},
 {"label": "d: BS Yr 1 - Less Fair value adjustment-TS", "value": bal_y1},
 {"label": "d: BS Yr 1 - Trading securities at fair value (current asset)", "value": carry_y1},
 {"label": "d: IS Yr 1 - Interest income", "value": cash_int},
 {"label": "d: IS Yr 1 - Unrealized holding loss on TS (FV-NI)", "value": adj_y1},
 {"label": "d: IS Yr 1 - Net effect on income from this investment", "value": ni_y1},
 {"label": "e: FVA rollforward Yr 2 - beginning FVA balance (Jan 1 Yr 2)", "value": bal_y1},
 {"label": "e: FVA rollforward Yr 2 - fair value Dec 31 Yr 2", "value": q(fv_y2)},
 {"label": "e: FVA rollforward Yr 2 - required FVA balance (debit)", "value": req_y2},
 {"label": "e: FVA rollforward Yr 2 - adjustment (debit FVA / unrealized gain)", "value": adj_y2},
 {"label": "e: FVA rollforward Yr 2 - ending FVA balance Dec 31 Yr 2", "value": bal_y2},
 {"label": "e: BS Yr 2 - Trading securities at fair value (carrying amount)", "value": carry_y2},
 {"label": "f(i): sale-date required FVA balance (proceeds/FV 41,000 - cost)", "value": req_sale},
 {"label": "f(i): sale-date FV-NI adjustment (credit FVA / unrealized loss)", "value": adj_sale},
 {"label": "f(i): carrying amount of TS after sale-date adjustment", "value": carry_sale},
 {"label": "f(ii): Cash received on sale Jan 1 Yr 3", "value": q(proceeds)},
 {"label": "f(ii): FVA-TS eliminated on sale (debit balance removed)", "value": bal_sale},
 {"label": "f(ii): Investment in Trading Securities (cost) removed", "value": cost},
 {"label": "f(ii): Realized gain/loss on sale after sale-date adjustment", "value": gain_on_sale},
 {"label": "g: Yr 1 unrealized holding loss recognized in NI", "value": adj_y1},
 {"label": "g: Yr 2 unrealized holding gain recognized in NI", "value": adj_y2},
 {"label": "g: Yr 3 sale-date unrealized holding loss recognized in NI", "value": adj_sale},
 {"label": "g: Cumulative unrealized holding gain/loss in NI over holding period", "value": cum_unreal},
 {"label": "g: Proof - proceeds minus cost", "value": proof},
 {"label": "g: Proof difference (cumulative NI effect - (proceeds - cost))", "value": q(cum_unreal - proof)},
]

def dr(a, x): return {"account": a, "debit": q(x), "credit": Decimal("0.00")}
def cr(a, x): return {"account": a, "credit": q(x), "debit": Decimal("0.00")}

jes = [
 {"part": "a", "lines": [dr("Investment in Trading Securities (Redwood Corp. bonds)", cost),
                          cr("Cash", cost)]},
 {"part": "b", "lines": [dr("Cash", cash_int),
                          cr("Interest Income", cash_int)]},
 {"part": "c", "lines": [dr("Unrealized Holding Gain or Loss - Net Income", -adj_y1),
                          cr("Fair Value Adjustment - Trading Securities", -adj_y1)]},
 {"part": "e", "lines": [dr("Fair Value Adjustment - Trading Securities", adj_y2),
                          cr("Unrealized Holding Gain or Loss - Net Income", adj_y2)]},
 {"part": "f(i)", "lines": [dr("Unrealized Holding Gain or Loss - Net Income", -adj_sale),
                             cr("Fair Value Adjustment - Trading Securities", -adj_sale)]},
 {"part": "f(ii)", "lines": [dr("Cash", proceeds),
                              cr("Fair Value Adjustment - Trading Securities", bal_sale),
                              cr("Investment in Trading Securities (Redwood Corp. bonds)", cost)]},
]
for je in jes:
    d = sum(l["debit"] for l in je["lines"]); c = sum(l["credit"] for l in je["lines"])
    assert d == c, (je["part"], d, c)
assert cum_unreal == proof

out = {
 "id": "agent_134#01",
 "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP to the cent applied once per period/line; no floating point.",
 "answers": [{"label": a["label"], "value": a["value"]} for a in answers],
 "journal_entries": jes,
 "insufficient_info": False,
 "notes": ("Bonds bought at par, so cost basis = $40,000 and no premium/discount amortization; "
           "TS under FV-NI are reported at fair value via a Fair Value Adjustment (FVA) account, "
           "with all holding gains/losses in net income. Negative FVA values are credit balances "
           "(fair value below cost) and negative unrealized amounts are losses. Sale occurs Jan 1 "
           "of Year 3, one day after the Dec 31 Year 2 coupon, so no interest is accrued at sale; "
           "after the sale-date FV-NI adjustment the carrying amount equals the $41,000 proceeds, "
           "so no separate realized gain or loss is recorded on the sale entry."),
}
print(json.dumps(out, default=lambda o: float(o), indent=1))
