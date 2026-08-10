"""Solver for agent_002#03 — HTM to AFS transfer (LO 14-10).

Rounding convention: all monetary amounts use decimal.Decimal with
ROUND_HALF_UP applied once per period at the cent level (2 dp). No floats.
Every figure below is derived from the given per-security amortized costs and
fair values; nothing is hard-coded beyond the problem's stated inputs.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
def r(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)
def n(x):
    x = r(x)
    return int(x) if x == x.to_integral_value() else float(x)

# --- Given inputs ---------------------------------------------------------
# security: (amortized cost, FV at 12/31/Y3 = transfer-date FV, FV at 12/31/Y4)
port = {
    "Quill Corp. bonds":     (Decimal("90000"), Decimal("96300"), Decimal("94000")),
    "Dune Partners bonds":   (Decimal("60000"), Decimal("55800"), Decimal("57000")),
}

# --- Derived totals -------------------------------------------------------
cost_total = r(sum(v[0] for v in port.values()))
fv_transfer = r(sum(v[1] for v in port.values()))
fv_y4       = r(sum(v[2] for v in port.values()))

# Transfer date (1/1/Y4): net unrealized holding gain(loss) -> OCI
unreal_transfer = r(fv_transfer - cost_total)          # +2,100 net gain

# 12/31/Y4: required Fair Value Adjustment balance vs. existing balance
fva_required_y4 = r(fv_y4 - cost_total)                # +1,000 debit balance
fva_existing    = unreal_transfer                       # carried from transfer
fva_change      = r(fva_required_y4 - fva_existing)     # -1,100 => credit FVA
adj_amount      = abs(fva_change)
adj_is_credit_to_fva = fva_change < 0

# --- Journal entries ------------------------------------------------------
def line(acct, dr=Decimal("0"), cr=Decimal("0")):
    return {"account": acct, "debit": n(dr), "credit": n(cr)}

jes = [
    {"part": "a", "lines": [
        line("Debt Investments — Available-for-Sale (Quill + Dune)", dr=cost_total),
        line("Debt Investments — Held-to-Maturity (Quill + Dune)", cr=cost_total),
    ]},
    {"part": "a", "lines": [
        line("Fair Value Adjustment (Available-for-Sale)", dr=unreal_transfer),
        line("Unrealized Holding Gain or Loss — Equity (OCI)", cr=unreal_transfer),
    ]},
    {"part": "c", "lines": (
        [line("Unrealized Holding Gain or Loss — Equity (OCI)", dr=adj_amount),
         line("Fair Value Adjustment (Available-for-Sale)", cr=adj_amount)]
        if adj_is_credit_to_fva else
        [line("Fair Value Adjustment (Available-for-Sale)", dr=adj_amount),
         line("Unrealized Holding Gain or Loss — Equity (OCI)", cr=adj_amount)]
    )},
]
for je in jes:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert r(d) == r(c), (je["part"], d, c)

disclosure = ("Disclose in the notes the reason for the transfer (change in intent caused by "
              "significant deterioration in the issuers' credit standing), the securities moved out "
              "of held-to-maturity, their amortized cost and fair value at the transfer date, and the "
              "net unrealized holding gain of $2,100 recognized in other comprehensive income (accumulated "
              "OCI) on transfer with no effect on net income. Because transfers out of HTM are permitted only "
              "in rare circumstances, the note should explain the circumstances and their effect on the "
              "remaining HTM classification.")

out = {
    "id": "agent_002#03",
    "rounding_convention": "decimal.Decimal throughout; ROUND_HALF_UP to the cent, applied once per period (all amounts resolve to whole dollars)",
    "answers": [
        {"label": "a: Carrying (amortized cost) amount reclassified from HTM to AFS on 1/1/Y4", "value": n(cost_total)},
        {"label": "a: Transfer-date total fair value of the two securities (1/1/Y4)", "value": n(fv_transfer)},
        {"label": "a: Net unrealized holding gain recognized in OCI on transfer (Dr Fair Value Adjustment)", "value": n(unreal_transfer)},
        {"label": "b: Effect of the transfer on net income", "value": 0},
        {"label": "b: Effect of the transfer on OCI (increase, net unrealized holding gain)", "value": n(unreal_transfer)},
        {"label": "c: Total amortized cost of the AFS portfolio at 12/31/Y4", "value": n(cost_total)},
        {"label": "c: Total fair value of the AFS portfolio at 12/31/Y4 (94,000 + 57,000)", "value": n(fv_y4)},
        {"label": "c: Required Fair Value Adjustment (AFS) debit balance at 12/31/Y4", "value": n(fva_required_y4)},
        {"label": "c: Existing Fair Value Adjustment (AFS) debit balance carried from the transfer", "value": n(fva_existing)},
        {"label": "c: Year-end adjustment — credit to Fair Value Adjustment / debit to Unrealized Holding Gain or Loss — Equity (OCI)", "value": n(adj_amount)},
        {"label": "d: Required footnote disclosure", "value": disclosure},
    ],
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": ("Transfer out of HTM is recorded at fair value on the transfer date; the entire unrealized "
              "holding gain/loss existing at that date goes to OCI (equity), never to net income, so NI effect "
              "is $0 and OCI increases $2,100. At 12/31/Y4 the AFS portfolio is remeasured to fair value of "
              "$151,000 against amortized cost of $150,000, so the Fair Value Adjustment account must be reduced "
              "from a $2,100 debit to a $1,000 debit — a $1,100 credit, with the offsetting $1,100 debit to OCI. "
              "Individual securities are pooled in one portfolio adjustment; no reclassification out of AOCI to NI occurs.")
}
print(json.dumps(out, indent=1))
