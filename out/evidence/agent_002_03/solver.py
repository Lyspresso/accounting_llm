#!/usr/bin/env python3
"""Solver for item agent_002#03 - Lakeshore Mutual Fund, HTM -> AFS transfer (LO 14-10).

WHAT THIS SOLVES
----------------
Lakeshore holds two par-purchased bond investments classified HTM at 12/31/Y3.
On 1/1/Y4 a significant deterioration in the issuers' credit standings causes a
change in intent, and both securities are transferred HTM -> AFS. At 12/31/Y4
the AFS portfolio is remeasured to fair value through OCI.

AUTHORITY / MODEL APPLIED
-------------------------
ASC 320-10-35-10(c) (per the course text, Ch. 14, LO 14-10 summary table):
  "Debt Transfer from HTM to AFS ... No effect on NI. Carrying value is adjusted
   to fair value as of the date of transfer through OCI."
So the whole transfer-date unrealized amount lands in OCI and none of it in NI.

Also ASC 320-10-25-6(a): "Evidence of a significant deterioration in the issuer's
creditworthiness" is an allowed change in circumstances, so the transfer does not
taint the remaining HTM portfolio.

ACCOUNT-TITLE CONVENTION follows the course text (Ch. 14 demos):
  Investment in HTM-<issuer> Bonds / Investment in AFS-<issuer> Bonds
  Fair Value Adjustment-AFS   (a valuation account carried alongside amortized cost)
  Unrealized Gain or Loss-OCI (equity / other comprehensive income)
Because HTM securities are carried at amortized cost with NO fair value
adjustment account, there is no pre-existing FVA balance to derecognize on the
transfer date; the required FVA balance is established from zero.

MECHANICS
---------
Both bonds were purchased AT PAR, so there is no premium/discount and amortized
cost is constant at face for every date in the problem. No interest amortization
schedule is needed and none is computed.

  FVA balance required on any date = (portfolio fair value) - (portfolio amortized cost)
  Entry to FVA on that date        = required balance - existing balance
  The offsetting side of every such entry is Unrealized Gain or Loss-OCI.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; floats are never used for any monetary value.
Every monetary result is quantized to cents ($0.01) with ROUND_HALF_UP, applied
per computed amount (i.e., round-per-period / round-at-each-entry, the course
convention), not deferred to the end. This problem's fact pattern contains only
whole-dollar amounts and involves no present-value factors, no interest
amortization, and no allocation, so no rounding difference actually arises -
the convention is applied and asserted anyway so the result is reproducible.

USAGE
-----
    python3 solver.py          # prints one JSON object to stdout
"""

import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def money(x) -> Decimal:
    """Quantize to cents using the stated ROUND_HALF_UP convention."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly number: int when the cent-quantized value is whole."""
    d = money(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------------------
# Fact pattern, taken from the stem. Nothing below is a hard-coded answer.
# ---------------------------------------------------------------------------
SECURITIES = ["Quill Corp.", "Dune Partners"]

# All bonds purchased at par -> amortized cost is face and never changes here.
AMORTIZED_COST = {
    "Quill Corp.": money("90000"),
    "Dune Partners": money("60000"),
}

FV_TRANSFER_DATE = {          # 12/31/Y3 fair values = 1/1/Y4 transfer-date FVs
    "Quill Corp.": money("96300"),
    "Dune Partners": money("55800"),
}

FV_DEC31_Y4 = {
    "Quill Corp.": money("94000"),
    "Dune Partners": money("57000"),
}


def total(mapping) -> Decimal:
    return money(sum(mapping.values(), Decimal("0")))


# ---------------------------------------------------------------------------
# Part a / b - January 1, Year 4 transfer
# ---------------------------------------------------------------------------
cost_total = total(AMORTIZED_COST)                  # 150,000
fv_transfer_total = total(FV_TRANSFER_DATE)         # 152,100

# HTM carries no fair value adjustment account, so the opening FVA balance is 0.
fva_balance_before_transfer = money("0")
fva_required_at_transfer = money(fv_transfer_total - cost_total)
fva_entry_at_transfer = money(fva_required_at_transfer - fva_balance_before_transfer)

# ASC 320-10-35-10(c): the entire transfer-date unrealized amount goes to OCI,
# nothing to net income.
effect_on_ni_at_transfer = money("0")
effect_on_oci_at_transfer = fva_entry_at_transfer

# Entry a-1: move the carrying (amortized cost) amounts out of HTM into AFS.
a1_lines = []
for s in SECURITIES:
    a1_lines.append({
        "account": f"Investment in AFS-{s} Bonds",
        "debit": num(AMORTIZED_COST[s]),
        "credit": 0,
    })
for s in SECURITIES:
    a1_lines.append({
        "account": f"Investment in HTM-{s} Bonds",
        "debit": 0,
        "credit": num(AMORTIZED_COST[s]),
    })

# Entry a-2: establish the AFS fair value adjustment at the transfer date, OCI side.
if fva_entry_at_transfer >= 0:
    a2_lines = [
        {"account": "Fair Value Adjustment-AFS",
         "debit": num(abs(fva_entry_at_transfer)), "credit": 0},
        {"account": "Unrealized Gain or Loss-OCI",
         "debit": 0, "credit": num(abs(fva_entry_at_transfer))},
    ]
else:
    a2_lines = [
        {"account": "Unrealized Gain or Loss-OCI",
         "debit": num(abs(fva_entry_at_transfer)), "credit": 0},
        {"account": "Fair Value Adjustment-AFS",
         "debit": 0, "credit": num(abs(fva_entry_at_transfer))},
    ]

# ---------------------------------------------------------------------------
# Part c - December 31, Year 4 AFS fair value adjustment
# ---------------------------------------------------------------------------
fv_y4_total = total(FV_DEC31_Y4)                    # 151,000
fva_required_y4_end = money(fv_y4_total - cost_total)
fva_entry_y4_end = money(fva_required_y4_end - fva_required_at_transfer)

if fva_entry_y4_end >= 0:
    c_lines = [
        {"account": "Fair Value Adjustment-AFS",
         "debit": num(abs(fva_entry_y4_end)), "credit": 0},
        {"account": "Unrealized Gain or Loss-OCI",
         "debit": 0, "credit": num(abs(fva_entry_y4_end))},
    ]
else:
    c_lines = [
        {"account": "Unrealized Gain or Loss-OCI",
         "debit": num(abs(fva_entry_y4_end)), "credit": 0},
        {"account": "Fair Value Adjustment-AFS",
         "debit": 0, "credit": num(abs(fva_entry_y4_end))},
    ]

journal_entries = [
    {"part": "a", "lines": a1_lines},
    {"part": "a", "lines": a2_lines},
    {"part": "c", "lines": c_lines},
]

# Debits must equal credits in every entry.
for je in journal_entries:
    dr = money(sum((Decimal(str(l["debit"])) for l in je["lines"]), Decimal("0")))
    cr = money(sum((Decimal(str(l["credit"])) for l in je["lines"]), Decimal("0")))
    assert dr == cr, f"unbalanced entry for part {je['part']}: {dr} vs {cr}"
    assert dr > 0, f"empty entry for part {je['part']}"

DISCLOSURE = (
    "The notes must describe the circumstances that led to the reclassification - "
    "the significant deterioration in the two issuers' creditworthiness (an ASC "
    "320-10-25-6(a) change in circumstances, so the transfer does not taint the "
    "remaining held-to-maturity portfolio) - together with the net carrying "
    "(amortized cost) amount of the securities transferred out of held-to-maturity "
    "and the net unrealized holding gain or loss on the transfer date that was "
    "recognized in other comprehensive income."
)

NOTES = (
    "Part b: no effect on net income; other comprehensive income increases by the "
    "transfer-date net unrealized holding gain. Part d is qualitative, so it is "
    "reported here rather than in 'answers': " + DISCLOSURE + " "
    "Both bonds were purchased at par, so amortized cost equals face on every date "
    "and no premium/discount amortization enters the computation."
)

result = {
    "id": "agent_002#03",
    "rounding_convention": (
        "decimal.Decimal only, never float; ROUND_HALF_UP quantized to cents "
        "applied per computed amount (round-at-each-entry, not deferred). No PV "
        "factors, interest amortization, or allocations arise in this item, so no "
        "rounding difference is created."
    ),
    "answers": [
        {"label": "b: effect on net income on the January 1, Year 4 transfer date",
         "value": num(effect_on_ni_at_transfer)},
        {"label": "b: effect on OCI on the January 1, Year 4 transfer date (increase)",
         "value": num(effect_on_oci_at_transfer)},
    ],
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": NOTES,
}

print(json.dumps(result, indent=2))
