#!/usr/bin/env python3
"""Solver for item agent_007#02 — AFS debt investment, intent-to-sell impairment,
subsequent-period disposal (LO 14-6).

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; no binary floats are used anywhere.
Rounding is ROUND_HALF_UP to the cent, applied per period / per computed line
item (never a single round at the end).  Every input in this fact pattern is a
whole-dollar amount and every derived figure is a difference of whole-dollar
amounts, so the ROUND_HALF_UP quantization is exact here and changes nothing;
it is applied anyway so the script's discipline matches the course convention.
No present-value discounting is performed: the stem supplies the present value
of expected cash flows ($91,000) directly, so no PV table factor or exact
annuity formula is needed.

FACT PATTERN (from the stem, nothing else)
------------------------------------------
  Jan 1, Yr 1  Summit Ridge buys $100,000 face of Oakmont Energy 4% bonds at
               par; classified available-for-sale (AFS).  Interest paid
               annually each Dec 31.  Amortized cost stays $100,000 through
               Year 1 (bought at par, no amortization).
  Dec 31, Yr 1 Fair value = $88,000.
               Summit Ridge HAS DECIDED TO SELL in early Year 2.
               PV of cash flows expected to be collected = $91,000.
               The FV-OCI fair-value adjustment is recorded FIRST, then the
               impairment analysis.
  Feb 10, Yr 2 Entire position sold for cash proceeds of $89,500.  Immediately
               before sale: Investment in AFS $88,000 (new cost basis after the
               Year 1 write-down), no Allowance, no remaining FVA.

AUTHORITY / METHOD (ASC 326-30; course text ch. 14, LO 14-6)
------------------------------------------------------------
a)  AFS securities are carried at fair value with the change routed through
    OCI using the Fair Value Adjustment (FVA) account, not the investment
    account.  FV ($88,000) < amortized cost ($100,000), so an unrealized
    holding LOSS of $12,000 is debited to Unrealized Gain or Loss—OCI and
    credited to Fair Value Adjustment—AFS.

b)  ASC 326-30-35-10: if the entity INTENDS TO SELL (or more likely than not
    will be required to sell before recovery), any allowance for credit losses
    is written off and the amortized cost basis is written down to fair value,
    with the whole incremental impairment reported in EARNINGS.  So the NI hit
    is the FULL amortized-cost-to-fair-value gap, $100,000 - $88,000 = $12,000,
    NOT the $9,000 credit-loss measure.  Per the text's table, the credit side
    of the write-down goes to the INVESTMENT account (fair value becomes the
    new cost basis), and the OCI loss booked in (a) is eliminated by debiting
    Fair Value Adjustment—AFS and crediting Unrealized Gain or Loss—OCI.

c)  Contrast — no intent to sell and not more likely than not required to sell:
    only the CREDIT portion hits net income, measured as amortized cost less
    the PV of cash flows expected to be collected ($100,000 - $91,000 =
    $9,000), capped at the amount by which fair value is below amortized cost
    ($12,000).  $9,000 < $12,000, so the cap does not bite: $9,000 to NI via
    an Allowance for Credit Losses; the $3,000 noncredit remainder stays in
    OCI.

d)  Feb 10, Yr 2 sale: after the write-down the investment's cost basis is
    $88,000 and there is no FVA or allowance left to reverse, so the realized
    result is simply proceeds less that new basis: $89,500 - $88,000 = $1,500
    realized GAIN.  (The stem gives proceeds and the pre-sale carrying amounts
    and says nothing about accrued interest between the Dec 31 coupon date and
    Feb 10, so no accrued-interest split is made — see notes.)

e)  Qualitative; no figure.  Handled in `notes`.

Run:  python3 solver.py   -> prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def money(x) -> Decimal:
    """Quantize to cents with the course convention, ROUND_HALF_UP."""
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly plain number: int when whole, else float-free string-safe."""
    d = money(d)
    if d == d.to_integral_value():
        return int(d)
    return float(d)  # only reached for sub-dollar residue; none arises here


# ---------------------------------------------------------------------------
# Given facts (stem only)
# ---------------------------------------------------------------------------
FACE = money("100000")            # $100,000 face, purchased at par
COUPON_RATE = Decimal("0.04")     # 4%, paid annually each Dec 31
AMORTIZED_COST_Y1 = money("100000")   # par purchase, no amortization in Yr 1
FAIR_VALUE_Y1 = money("88000")        # FV at Dec 31, Year 1
PV_EXPECTED_CF = money("91000")       # PV of cash flows expected to be collected
PROCEEDS = money("89500")             # cash proceeds, Feb 10, Year 2
INTENDS_TO_SELL = True                # "has decided to sell" in early Year 2

# Sanity tie-out of the par purchase (not reported):
assert money(FACE) == AMORTIZED_COST_Y1
_annual_coupon = money(FACE * COUPON_RATE)   # $4,000, collected Dec 31 Yr 1

# ---------------------------------------------------------------------------
# (a) Dec 31, Year 1 FV-OCI adjustment, recorded BEFORE the impairment analysis
# ---------------------------------------------------------------------------
fva_change = money(FAIR_VALUE_Y1 - AMORTIZED_COST_Y1)     # -12,000
unrealized_holding_loss_oci = money(-fva_change)          # 12,000 debit to OCI

entry_a = {
    "part": "a",
    "description": "Dec 31, Year 1 - record AFS fair value adjustment through OCI "
                   "(before impairment analysis)",
    "lines": [
        {"account": "Unrealized Gain or Loss-OCI",
         "debit": num(unrealized_holding_loss_oci), "credit": 0},
        {"account": "Fair Value Adjustment-AFS",
         "debit": 0, "credit": num(unrealized_holding_loss_oci)},
    ],
}

# ---------------------------------------------------------------------------
# (b) Impairment under the INTENT-TO-SELL path: full write-down to fair value,
#     entire gap to net income (ASC 326-30-35-10)
# ---------------------------------------------------------------------------
gap_to_fair_value = money(AMORTIZED_COST_Y1 - FAIR_VALUE_Y1)   # 12,000

if INTENDS_TO_SELL:
    impairment_loss_ni = gap_to_fair_value                     # 12,000
else:                                                          # not this stem
    impairment_loss_ni = min(money(AMORTIZED_COST_Y1 - PV_EXPECTED_CF),
                             gap_to_fair_value)

new_cost_basis = money(AMORTIZED_COST_Y1 - impairment_loss_ni)  # 88,000 = FV
assert new_cost_basis == FAIR_VALUE_Y1, "write-down must land on fair value"

entry_b = {
    "part": "b",
    "description": "Dec 31, Year 1 - record impairment loss (intent to sell): write "
                   "amortized cost down to fair value with the full gap in net "
                   "income; fair value becomes the new cost basis, and the OCI "
                   "loss from (a) is eliminated",
    "lines": [
        {"account": "Loss on Impairment",
         "debit": num(impairment_loss_ni), "credit": 0},
        {"account": "Fair Value Adjustment-AFS",
         "debit": num(impairment_loss_ni), "credit": 0},
        {"account": "Investment in AFS-Oakmont Energy Bonds",
         "debit": 0, "credit": num(impairment_loss_ni)},
        {"account": "Unrealized Gain or Loss-OCI",
         "debit": 0, "credit": num(impairment_loss_ni)},
    ],
}

# ---------------------------------------------------------------------------
# (c) Contrast: NI impairment if there were NO intent to sell
#     credit loss = amortized cost - PV of expected cash flows, capped at the
#     amount fair value is below amortized cost
# ---------------------------------------------------------------------------
credit_loss_raw = money(AMORTIZED_COST_Y1 - PV_EXPECTED_CF)        # 9,000
impairment_loss_ni_no_intent = min(credit_loss_raw, gap_to_fair_value)   # 9,000
noncredit_left_in_oci = money(gap_to_fair_value - impairment_loss_ni_no_intent)  # 3,000

# ---------------------------------------------------------------------------
# (d) Feb 10, Year 2 sale of the entire position
# ---------------------------------------------------------------------------
carrying_amount_at_sale = new_cost_basis                    # 88,000, no FVA/allowance
realized_result = money(PROCEEDS - carrying_amount_at_sale)  # +1,500 = gain
realized_gain = realized_result if realized_result > 0 else money(0)
realized_loss = money(-realized_result) if realized_result < 0 else money(0)

sale_lines = [
    {"account": "Cash", "debit": num(PROCEEDS), "credit": 0},
    {"account": "Investment in AFS-Oakmont Energy Bonds",
     "debit": 0, "credit": num(carrying_amount_at_sale)},
]
if realized_result > 0:
    sale_lines.append({"account": "Gain on Sale of Investment",
                       "debit": 0, "credit": num(realized_gain)})
elif realized_result < 0:
    sale_lines.insert(1, {"account": "Loss on Sale of Investment",
                          "debit": num(realized_loss), "credit": 0})

entry_d = {
    "part": "d",
    "description": "Feb 10, Year 2 - sell the entire Oakmont position for cash; "
                   "gain/loss measured against the post-impairment cost basis",
    "lines": sale_lines,
}

# ---------------------------------------------------------------------------
# Balance check every entry (debits must equal credits)
# ---------------------------------------------------------------------------
journal_entries = [entry_a, entry_b, entry_d]
for je in journal_entries:
    dr = sum(Decimal(str(ln["debit"])) for ln in je["lines"])
    cr = sum(Decimal(str(ln["credit"])) for ln in je["lines"])
    assert money(dr) == money(cr), f"part {je['part']} out of balance: {dr} vs {cr}"

# ---------------------------------------------------------------------------
# Output — only the figures the Required parts ask for
# ---------------------------------------------------------------------------
answers = [
    {"label": "b: impairment loss recognized in net income (intent-to-sell path)",
     "value": num(impairment_loss_ni)},
    {"label": "c: impairment loss in net income if no intent to sell (credit loss only)",
     "value": num(impairment_loss_ni_no_intent)},
    {"label": "d: realized gain on the February 10, Year 2 sale",
     "value": num(realized_gain)},
]

notes = (
    "a: FV-OCI adjustment is the $12,000 excess of amortized cost ($100,000) over "
    "fair value ($88,000), booked to the Fair Value Adjustment-AFS account rather "
    "than the investment account. "
    "b: with intent to sell, ASC 326-30-35-10 requires writing the amortized cost "
    "basis all the way down to fair value with the entire $12,000 in earnings; the "
    "$9,000 credit-loss measure is not used, and no allowance is set up because "
    "fair value becomes the new cost basis. "
    "c: without intent to sell (and not more likely than not required to sell), only "
    "the credit portion hits net income: $100,000 amortized cost less the $91,000 PV "
    "of expected cash flows = $9,000, which is below the $12,000 fair-value cap, so "
    "$9,000 goes to net income through Allowance for Credit Losses and the remaining "
    "$3,000 noncredit decline stays in OCI - $3,000 less net income impact than the "
    "intent-to-sell path. "
    "d: gain = $89,500 proceeds - $88,000 post-impairment cost basis = $1,500. The "
    "stem gives proceeds and the pre-sale carrying amounts and is silent on interest "
    "accrued between the Dec 31 coupon date and Feb 10, so no accrued-interest "
    "element is split out of the proceeds. "
    "e: the Year 1 impairment loss is reported in NET INCOME (it is not left in OCI) "
    "on the income statement in the other income and expense / other gains and losses "
    "(nonoperating) section, below income from operations; the write-down also reduces "
    "the AFS investment's carrying amount on the balance sheet to its new $88,000 cost "
    "basis. Required AFS credit-loss disclosure under the allowance model (no-intent "
    "path): a rollforward of the allowance for credit losses on available-for-sale debt "
    "securities - beginning balance, current-period provision, write-offs/recoveries and "
    "ending balance - by major security type."
)

result = {
    "id": "agent_007#02",
    "rounding_convention": (
        "decimal.Decimal only, never floats; ROUND_HALF_UP to the cent applied per "
        "period / per computed line item, not once at the end. No PV table factors or "
        "discounting used - the stem supplies the $91,000 present value of expected "
        "cash flows directly. All inputs and derived figures are whole dollars."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(result, indent=2))
