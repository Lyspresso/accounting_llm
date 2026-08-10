"""Solver for agent_268#00 — equity method with basis difference (LO 14-5).

Rounding convention: all money is decimal.Decimal. Every computed amount is
quantized to cents (0.01) using ROUND_HALF_UP, applied once per period /
per line item (no float arithmetic anywhere). Debits must equal credits.
Nothing is hard-coded except the scenario facts given in the question.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x):
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)

def f(d):
    return float(d)

# ---- Given facts ----
COST            = Decimal("240000")
PCT             = Decimal("30") / Decimal("100")
BV_NET_ASSETS   = Decimal("700000")
EQUIP_UNDERVAL  = Decimal("40000")     # 100% basis, on investee books
LIFE_YEARS      = Decimal("8")
INVESTEE_NI     = Decimal("80000")
INVESTEE_DIV    = Decimal("20000")
FV_INTEREST_1231= Decimal("255000")

# ---- b. Cost allocation ----
share_bv      = q(BV_NET_ASSETS * PCT)                 # share of book value
basis_equip   = q(EQUIP_UNDERVAL * PCT)                # investor share of undervalued equipment
goodwill      = q(COST - share_bv - basis_equip)       # residual, not amortized
fv_net_assets_share = q(share_bv + basis_equip)        # share of FV of net assets

# ---- c/e. Year 1 equity-method amounts ----
share_ni      = q(INVESTEE_NI * PCT)
excess_dep    = q(basis_equip / LIFE_YEARS)            # straight-line, no residual
div_received  = q(INVESTEE_DIV * PCT)
net_eq_income = q(share_ni - excess_dep)
fv_adjustment = q(Decimal("0"))                        # none under equity method

# ---- d. Investment rollforward ----
beg           = q(COST)
after_ni      = q(beg + share_ni)
after_dep     = q(after_ni - excess_dep)
ending        = q(after_dep - div_received)
unrecorded_fv_diff = q(FV_INTEREST_1231 - ending)      # disclosed only, not booked

# ---- Journal entries ----
jes = [
    {"part": "a", "lines": [
        {"account": "Investment in Meridian Forge Co.", "debit": f(COST), "credit": 0.0},
        {"account": "Cash", "debit": 0.0, "credit": f(COST)},
    ]},
    {"part": "c", "lines": [
        {"account": "Investment in Meridian Forge Co.", "debit": f(share_ni), "credit": 0.0},
        {"account": "Equity in Investee Income (Investment Income)", "debit": 0.0, "credit": f(share_ni)},
    ]},
    {"part": "c", "lines": [
        {"account": "Equity in Investee Income (Investment Income)", "debit": f(excess_dep), "credit": 0.0},
        {"account": "Investment in Meridian Forge Co.", "debit": 0.0, "credit": f(excess_dep)},
    ]},
    {"part": "c", "lines": [
        {"account": "Cash", "debit": f(div_received), "credit": 0.0},
        {"account": "Investment in Meridian Forge Co.", "debit": 0.0, "credit": f(div_received)},
    ]},
]
for je in jes:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert d == c, (je, d, c)

answers = [
    {"label": "a: Initial recognition — Dr Investment in Meridian Forge Co. (cash cost, Jan 1 Year 1)", "value": f(COST)},
    {"label": "a: Initial recognition — Cr Cash", "value": f(COST)},
    {"label": "b: Share of book value of net assets acquired (30% x $700,000)", "value": f(share_bv)},
    {"label": "b: Basis difference allocated to undervalued equipment (30% x $40,000)", "value": f(basis_equip)},
    {"label": "b: Goodwill (residual, not amortized)", "value": f(goodwill)},
    {"label": "b: Total cost allocated (share of FV of net assets $222,000 + goodwill)", "value": f(COST)},
    {"label": "c: Share of investee net income recognized (30% x $80,000)", "value": f(share_ni)},
    {"label": "c: Excess depreciation on equipment basis difference ($12,000 / 8 yrs)", "value": f(excess_dep)},
    {"label": "c: Dividends received — return of investment (30% x $20,000)", "value": f(div_received)},
    {"label": "c: Fair-value adjustment recorded at Dec 31 (none under the equity method)", "value": f(fv_adjustment)},
    {"label": "d: Investment schedule — beginning balance / cost, Jan 1 Year 1", "value": f(beg)},
    {"label": "d: Investment schedule — add share of net income", "value": f(share_ni)},
    {"label": "d: Investment schedule — running balance after share of net income", "value": f(after_ni)},
    {"label": "d: Investment schedule — less excess depreciation", "value": f(excess_dep)},
    {"label": "d: Investment schedule — running balance after excess depreciation", "value": f(after_dep)},
    {"label": "d: Investment schedule — less dividends received", "value": f(div_received)},
    {"label": "d: Investment carrying amount, Dec 31 Year 1", "value": f(ending)},
    {"label": "e: Net equity-method income recognized in Year 1 ($24,000 - $1,500)", "value": f(net_eq_income)},
]

notes = (
    "a. Equity method applies because Cascade holds 30% of the voting common stock "
    "(20%-50% range) and can exercise significant influence over Meridian; the investment "
    "is recorded initially at the $240,000 cash cost. "
    "b. Cost $240,000 - share of book value $210,000 = $30,000 basis difference, of which "
    "$12,000 is the investor's share of the undervalued equipment and $18,000 is goodwill "
    "(share of FV of net assets = $222,000). "
    "c. Three Dec 31 adjusting entries: share of net income, amortization of the equipment "
    "basis difference (excess depreciation reduces both investment income and the investment "
    "account), and dividends treated as a return of investment (credit Investment, not revenue). "
    "No fair-value adjustment is recorded — the $255,000 fair value of the 30% interest is not "
    "recognized under the equity method; the carrying amount stays at $256,500 (a $"
    + str(abs(unrecorded_fv_diff)) + " unrecorded difference), subject only to impairment testing. "
    "e. Net equity-method income = $24,000 share of NI - $1,500 excess depreciation = $22,500."
)

print(json.dumps({
    "id": "agent_268#00",
    "rounding_convention": "decimal.Decimal throughout; amounts quantized to cents (0.01) with ROUND_HALF_UP once per period/line item; no floats used in computation",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
