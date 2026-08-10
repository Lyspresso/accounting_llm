"""Independent (second) cold derivation of agent_002#03.

Q4 CORE - LO 14-10: HTM -> AFS transfer at fair value through OCI (no NI effect),
then the subsequent AFS period-end fair-value adjusting entry.

Rounding convention: all money is decimal.Decimal, quantized to whole cents with
ROUND_HALF_UP once per period/computation step (no float arithmetic anywhere).
Every figure in the stem is an exact whole dollar, so no rounding is actually
triggered; the convention is stated and applied for discipline.

Reasoning, built bottom-up from the fact pattern:
  * All bonds were purchased at par, so amortized cost = par and there is no
    premium/discount amortization in Year 4. Amortized cost stays $150,000.
  * A transfer OUT of HTM into AFS is recorded by reclassifying the security at
    its carrying (amortized cost) amount and then establishing a Fair Value
    Adjustment for the transfer-date unrealized holding gain/loss, which goes to
    OCI, not net income. The amortized cost basis is retained as the reference
    point for measuring later unrealized gains/losses.
  * At 12/31/Y4 the Fair Value Adjustment account must be restated so that the
    reported carrying amount equals aggregate fair value; the change in that
    account for the period is the OCI entry.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def m(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d):
    d = m(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------- given facts
# (security, amortized cost, FV 12/31/Y3 = FV on 1/1/Y4 transfer date, FV 12/31/Y4)
DATA = [
    ("Quill Corp. bonds", "90000", "96300", "94000"),
    ("Dune Partners bonds", "60000", "55800", "57000"),
]

amort_cost = {n: m(a) for n, a, _, _ in DATA}
fv_transfer = {n: m(t) for n, _, t, _ in DATA}
fv_y4end = {n: m(e) for n, _, _, e in DATA}

tot_ac = m(sum(amort_cost.values()))
tot_fv_tr = m(sum(fv_transfer.values()))
tot_fv_y4 = m(sum(fv_y4end.values()))

# per-security transfer-date unrealized amounts (derived, not copied)
ur_tr = {n: m(fv_transfer[n] - amort_cost[n]) for n in amort_cost}
net_ur_tr = m(sum(ur_tr.values()))          # + = net unrealized gain

# ------------------------------------------------- part a: 1/1/Y4 transfer JEs
# Entry 1: reclassify at carrying (amortized cost) amount.
je_a1 = [
    {"account": "Debt Investments (available-for-sale), at amortized cost",
     "debit": num(tot_ac), "credit": 0},
    {"account": "Debt Investments (held-to-maturity)",
     "debit": 0, "credit": num(tot_ac)},
]
# Entry 2: recognize transfer-date fair value through OCI.
# net_ur_tr is a net gain -> debit Fair Value Adjustment, credit OCI.
if net_ur_tr >= 0:
    je_a2 = [
        {"account": "Fair Value Adjustment (available-for-sale)",
         "debit": num(net_ur_tr), "credit": 0},
        {"account": "Unrealized Holding Gain or Loss - Equity (OCI)",
         "debit": 0, "credit": num(net_ur_tr)},
    ]
else:
    je_a2 = [
        {"account": "Unrealized Holding Gain or Loss - Equity (OCI)",
         "debit": num(-net_ur_tr), "credit": 0},
        {"account": "Fair Value Adjustment (available-for-sale)",
         "debit": 0, "credit": num(-net_ur_tr)},
    ]

carry_after_transfer = m(tot_ac + net_ur_tr)   # = aggregate transfer-date FV

# ---------------------------------------------- part c: 12/31/Y4 AFS FVA entry
ur_y4 = {n: m(fv_y4end[n] - amort_cost[n]) for n in amort_cost}
net_ur_y4 = m(sum(ur_y4.values()))            # required ending FVA (debit if +)
fva_open = net_ur_tr                          # balance carried from the transfer
fva_change = m(net_ur_y4 - fva_open)          # - = credit FVA / debit OCI

if fva_change >= 0:
    je_c = [
        {"account": "Fair Value Adjustment (available-for-sale)",
         "debit": num(fva_change), "credit": 0},
        {"account": "Unrealized Holding Gain or Loss - Equity (OCI)",
         "debit": 0, "credit": num(fva_change)},
    ]
else:
    je_c = [
        {"account": "Unrealized Holding Gain or Loss - Equity (OCI)",
         "debit": num(-fva_change), "credit": 0},
        {"account": "Fair Value Adjustment (available-for-sale)",
         "debit": 0, "credit": num(-fva_change)},
    ]

# per-security change in unrealized position during Y4 (cross-check on net)
chg = {n: m(ur_y4[n] - ur_tr[n]) for n in amort_cost}
assert m(sum(chg.values())) == fva_change
assert m(tot_ac + net_ur_y4) == tot_fv_y4

# Dr = Cr check on every entry
for e in (je_a1, je_a2, je_c):
    assert m(sum(Decimal(str(l["debit"])) for l in e)) == \
           m(sum(Decimal(str(l["credit"])) for l in e))

Q, D = DATA[0][0], DATA[1][0]

answers = [
    {"label": "a: Total amortized cost reclassified HTM -> AFS on 1/1/Y4 (Dr AFS / Cr HTM)",
     "value": num(tot_ac)},
    {"label": "a: Aggregate fair value on transfer date 1/1/Y4",
     "value": num(tot_fv_tr)},
    {"label": f"a: {Q} transfer-date unrealized gain (96,300 - 90,000)",
     "value": num(ur_tr[Q])},
    {"label": f"a: {D} transfer-date unrealized loss (55,800 - 60,000)",
     "value": num(ur_tr[D])},
    {"label": "a: Net transfer-date unrealized gain debited to Fair Value Adjustment (AFS) and credited to OCI",
     "value": num(net_ur_tr)},
    {"label": "a: AFS carrying amount immediately after the 1/1/Y4 transfer (amortized cost 150,000 + FVA 2,100)",
     "value": num(carry_after_transfer)},
    {"label": "b: Effect of the transfer on Year 4 net income (none - HTM -> AFS unrealized amount bypasses NI)",
     "value": 0},
    {"label": "b: Effect of the transfer on Year 4 other comprehensive income (increase)",
     "value": num(net_ur_tr)},
    {"label": "b: AOCI (accumulated unrealized holding gain) balance immediately after the transfer",
     "value": num(net_ur_tr)},
    {"label": f"c: {Q} unrealized gain at 12/31/Y4 (94,000 - 90,000)",
     "value": num(ur_y4[Q])},
    {"label": f"c: {D} unrealized loss at 12/31/Y4 (57,000 - 60,000)",
     "value": num(ur_y4[D])},
    {"label": "c: Aggregate fair value of AFS portfolio at 12/31/Y4",
     "value": num(tot_fv_y4)},
    {"label": "c: Amortized cost of AFS portfolio at 12/31/Y4 (bonds bought at par; no amortization)",
     "value": num(tot_ac)},
    {"label": "c: Required Fair Value Adjustment (AFS) balance at 12/31/Y4 (debit)",
     "value": num(net_ur_y4)},
    {"label": "c: Fair Value Adjustment (AFS) balance before the 12/31/Y4 entry (debit, from transfer)",
     "value": num(fva_open)},
    {"label": "c: 12/31/Y4 adjustment - decrease in Fair Value Adjustment (Dr OCI / Cr FVA)",
     "value": num(-fva_change)},
    {"label": f"c: {Q} change in unrealized position during Y4 (4,000 - 6,300)",
     "value": num(chg[Q])},
    {"label": f"c: {D} change in unrealized position during Y4 (-3,000 - (-4,200))",
     "value": num(chg[D])},
    {"label": "c: AOCI (accumulated unrealized holding gain) balance at 12/31/Y4",
     "value": num(net_ur_y4)},
    {"label": "c: AFS carrying amount reported on the 12/31/Y4 balance sheet",
     "value": num(tot_fv_y4)},
    {"label": "c: Effect of the 12/31/Y4 adjusting entry on Year 4 net income (none)",
     "value": 0},
]

journal_entries = [
    {"part": "a", "date": "Jan. 1, Year 4",
     "description": "Reclassify both bonds out of HTM into AFS at carrying (amortized cost) amount",
     "lines": je_a1},
    {"part": "a", "date": "Jan. 1, Year 4",
     "description": "Record transfer-date fair value; net unrealized holding gain of $2,100 goes to OCI, not net income",
     "lines": je_a2},
    {"part": "c", "date": "Dec. 31, Year 4",
     "description": "Adjust AFS portfolio to aggregate fair value $151,000 vs. amortized cost $150,000; reduce Fair Value Adjustment from $2,100 to $1,000 through OCI",
     "lines": je_c},
]

notes = (
    "All bonds were purchased at par, so amortized cost equals par ($150,000) at every date "
    "and there is no premium/discount amortization in Year 4. "
    "Part a: the transfer out of HTM is recorded in two steps - reclassify the securities at their "
    "$150,000 amortized cost carrying amount, then set up a Fair Value Adjustment (AFS) of $2,100 "
    "(Quill +$6,300 gain net of Dune -$4,200 loss) with the offset in OCI, bringing the AFS carrying "
    "amount to the $152,100 transfer-date fair value. The amortized cost basis is retained as the "
    "reference for measuring later unrealized amounts. "
    "Part b: no effect on net income ($0); OCI increases $2,100, so AOCI holds a $2,100 net unrealized "
    "holding gain right after the transfer. (Under the older 'transfer at fair value' presentation the "
    "same $2,100 is debited to the investment account itself instead of a separate valuation account - "
    "either presentation produces the same $152,100 carrying amount, $0 NI and +$2,100 OCI.) "
    "Part c: at 12/31/Y4 fair value is $94,000 + $57,000 = $151,000 against $150,000 amortized cost, so "
    "the Fair Value Adjustment must be a $1,000 debit balance ($4,000 Quill gain less $3,000 Dune loss). "
    "It currently stands at $2,100 debit, so the entry credits Fair Value Adjustment $1,100 and debits "
    "Unrealized Holding Gain or Loss - Equity (OCI) $1,100 (Quill -$2,300 plus Dune +$1,200 = -$1,100). "
    "No net income effect; AOCI ends Year 4 at a $1,000 net unrealized gain and the AFS portfolio is "
    "reported at $151,000. "
    "Part d (disclosure, narrative): the footnote should disclose the transfer out of held-to-maturity - "
    "the reason for the change in intent (the significant deterioration in the issuers' credit standings, "
    "which is one of the limited circumstances that does not taint the remaining HTM classification), the "
    "amortized cost and fair value of the securities transferred ($150,000 and $152,100) and the transfer "
    "date, the net unrealized holding gain of $2,100 recognized in other comprehensive income on transfer "
    "(with no effect on net income), the circumstances/nature of the securities involved, and the fact that "
    "the securities are now carried at fair value with subsequent changes reported in OCI."
)

print(json.dumps({
    "id": "agent_002#03",
    "rounding_convention": "decimal.Decimal only (no floats); every money figure quantized to cents with ROUND_HALF_UP once per computation step. Stem amounts are exact whole dollars, so no rounding is triggered; journal entries are stated in whole dollars.",
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
