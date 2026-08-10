#!/usr/bin/env python3
"""Blind solver -- item agent_352#01.

Northvale Retail Corp. (calendar year-end): indefinite-life trademark purchase,
business combination / goodwill residual, crypto asset at fair value, an
intangibles carrying-value schedule for 20X1-20X2, and the 20X2 trademark
disposal.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal; no binary floats anywhere.  Every amount is
carried and reported at the cent (quantized to 0.01) using ROUND_HALF_UP,
applied per period / per computed amount rather than only at the end.  The
fact pattern supplies whole-dollar figures and every derived amount here is a
plain sum or difference of them, so no rounding is actually triggered -- the
convention is stated and enforced so the result is reproducible.  No present
value work is required by this fact pattern, so no PV table factors are used.

ACCOUNTING BASIS (ASC 350 / ASC 805, per ACCOUNT-343 Ch. 13)
------------------------------------------------------------
* An externally purchased indefinite-life trademark is capitalized at purchase
  price plus directly attributable external registration/legal fees.
* Indefinite-life intangibles (purchased trademark, acquired brand) and
  acquired in-process research and development (ASC 805; IPR&D acquired in a
  business combination is capitalized at fair value as an INDEFINITE-life
  intangible until the project is completed or abandoned) are NOT amortized.
  Goodwill is NOT amortized (ASC 350-20-35-1).  All are impairment-tested only,
  and the stem states there is no impairment.
* Goodwill = consideration transferred - fair value of identifiable net assets
  acquired (identifiable assets, including identifiable intangibles, less
  liabilities assumed).
* A qualifying crypto asset (ASC 350-60) is measured at FAIR VALUE at each
  reporting date, with remeasurement gains and losses in NET INCOME.  Crypto is
  therefore remeasured -- not amortized and not impairment-model-tested.
* Disposal of an indefinite-life intangible: gain/loss = proceeds - carrying
  amount, with no amortization catch-up because none was ever recorded.

Run:  python3 solver.py   -> prints one JSON object on stdout.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("0.01")


def m(x) -> Decimal:
    """Money constructor: exact Decimal, quantized to the cent, ROUND_HALF_UP."""
    return Decimal(str(x)).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d: Decimal):
    """JSON-friendly number: int when the cents are zero, else float-free str->float.

    Amounts are whole dollars in this fact pattern; emit ints so the value is
    a plain number with no formatting noise.
    """
    d = d.quantize(CENT, rounding=ROUND_HALF_UP)
    return int(d) if d == d.to_integral_value() else float(d)


# ---------------------------------------------------------------------------
# Fact pattern (transcribed from the stem -- nothing else is hard-coded)
# ---------------------------------------------------------------------------

# 1. Feb 1, 20X1 -- purchased indefinite-life trademark
TM_PURCHASE_PRICE = m(120_000)
TM_REGISTRATION_FEES = m(8_000)

# 2. June 30, 20X1 -- 100% acquisition of Oakridge Brands LLC
CONSIDERATION = m(780_000)

ACQUIRED_ASSETS_FV = [
    ("Cash", m(40_000)),
    ("Accounts Receivable", m(70_000)),
    ("Inventory", m(125_000)),
    ("Property, Plant, and Equipment", m(410_000)),
    ("Customer Relationships", m(45_000)),          # finite-life identifiable
    ("Trademark--Brand", m(80_000)),                # indefinite-life
    ("Acquired In-Process Research and Development", m(50_000)),
]
ASSUMED_LIABILITIES_FV = [
    ("Accounts Payable", m(55_000)),
    ("Long-Term Debt", m(195_000)),
]

# 3. Sept 1, 20X1 -- three units of a qualifying crypto asset
CRYPTO_COST = m(75_000)
CRYPTO_UNITS = 3

# 4. Dec 31, 20X1 -- crypto fair value; no impairment of indefinite intangibles
CRYPTO_FV_X1 = m(80_000)

# 5. April 1, 20X2 -- sells the Feb 1, 20X1 purchased trademark
TM_SALE_PROCEEDS = m(110_000)

# 6. Dec 31, 20X2 -- crypto still held
CRYPTO_FV_X2 = m(68_000)


# ---------------------------------------------------------------------------
# (a) Trademark cost and goodwill
# ---------------------------------------------------------------------------

# Purchase price + external registration/legal fees are both directly
# attributable costs of acquiring the trademark -> capitalize.
trademark_cost = m(TM_PURCHASE_PRICE + TM_REGISTRATION_FEES)

identifiable_assets_fv = m(sum((fv for _, fv in ACQUIRED_ASSETS_FV), Decimal("0")))
liabilities_assumed_fv = m(sum((fv for _, fv in ASSUMED_LIABILITIES_FV), Decimal("0")))
net_identifiable_assets = m(identifiable_assets_fv - liabilities_assumed_fv)
goodwill = m(CONSIDERATION - net_identifiable_assets)


# ---------------------------------------------------------------------------
# (b) Dec 31, 20X1 crypto AJ; amortization AJs required
# ---------------------------------------------------------------------------

crypto_adj_x1 = m(CRYPTO_FV_X1 - CRYPTO_COST)   # positive => unrealized gain

# No amortization for any of: purchased trademark (indefinite), acquired brand
# (indefinite), acquired IPR&D (indefinite until completed/abandoned), goodwill.
AMORT_X1 = {
    "purchased trademark": m(0),
    "acquired brand": m(0),
    "acquired IPR&D": m(0),
    "goodwill": m(0),
}


# ---------------------------------------------------------------------------
# (c) 20X1-20X2 carrying-value schedule
# ---------------------------------------------------------------------------

acq_fv = dict(ACQUIRED_ASSETS_FV)

# Purchased trademark: cost, no amortization, no impairment; sold 4/1/X2.
tm_cv_x1 = trademark_cost
tm_cv_x2 = m(0)

# Acquired brand: indefinite, no amortization, no impairment.
brand_cv_x1 = acq_fv["Trademark--Brand"]
brand_cv_x2 = brand_cv_x1

# Acquired IPR&D: indefinite until completed/abandoned, no amortization.
iprd_cv_x1 = acq_fv["Acquired In-Process Research and Development"]
iprd_cv_x2 = iprd_cv_x1

# Goodwill: never amortized, no impairment.
gw_cv_x1 = goodwill
gw_cv_x2 = gw_cv_x1

# Crypto: remeasured to fair value at each reporting date.
crypto_cv_x1 = m(CRYPTO_COST + crypto_adj_x1)   # == CRYPTO_FV_X1
crypto_adj_x2 = m(CRYPTO_FV_X2 - crypto_cv_x1)  # negative => unrealized loss
crypto_cv_x2 = m(crypto_cv_x1 + crypto_adj_x2)  # == CRYPTO_FV_X2


# ---------------------------------------------------------------------------
# (d) April 1, 20X2 disposal; Dec 31, 20X2 crypto AJ
# ---------------------------------------------------------------------------

disposal_gain = m(TM_SALE_PROCEEDS - tm_cv_x1)  # negative => loss


# ---------------------------------------------------------------------------
# Journal entries
# ---------------------------------------------------------------------------

def line(account, debit=Decimal("0"), credit=Decimal("0")):
    return {"account": account, "debit": num(m(debit)), "credit": num(m(credit))}


journal_entries = []

# (a) Feb 1, 20X1 -- purchased trademark at cost
journal_entries.append({
    "part": "a",
    "date": "20X1-02-01",
    "description": "Purchase of indefinite-life trademark (price plus external registration/legal fees)",
    "lines": [
        line("Trademark", debit=trademark_cost),
        line("Cash", credit=trademark_cost),
    ],
})

# (a) June 30, 20X1 -- acquisition of Oakridge Brands LLC
acq_lines = [line(name, debit=fv) for name, fv in ACQUIRED_ASSETS_FV]
acq_lines.append(line("Goodwill", debit=goodwill))
acq_lines += [line(name, credit=fv) for name, fv in ASSUMED_LIABILITIES_FV]
acq_lines.append(line("Cash", credit=CONSIDERATION))
journal_entries.append({
    "part": "a",
    "date": "20X1-06-30",
    "description": "Acquisition of 100% of Oakridge Brands LLC; goodwill is the residual",
    "lines": acq_lines,
})

# (a) Sept 1, 20X1 -- crypto purchase at cost
journal_entries.append({
    "part": "a",
    "date": "20X1-09-01",
    "description": f"Purchase of {CRYPTO_UNITS} units of a qualifying crypto asset",
    "lines": [
        line("Crypto Assets", debit=CRYPTO_COST),
        line("Cash", credit=CRYPTO_COST),
    ],
})

# (b) Dec 31, 20X1 -- crypto fair value AJ
journal_entries.append({
    "part": "b",
    "date": "20X1-12-31",
    "description": "Remeasure crypto assets to fair value; change to net income (ASC 350-60)",
    "lines": (
        [line("Crypto Assets", debit=crypto_adj_x1),
         line("Unrealized Gain--Crypto Assets (Income)", credit=crypto_adj_x1)]
        if crypto_adj_x1 > 0 else
        [line("Unrealized Loss--Crypto Assets (Income)", debit=-crypto_adj_x1),
         line("Crypto Assets", credit=-crypto_adj_x1)]
    ),
})

# (d) April 1, 20X2 -- sale of the purchased trademark
disposal_lines = [line("Cash", debit=TM_SALE_PROCEEDS)]
if disposal_gain < 0:
    disposal_lines.append(line("Loss on Disposal of Trademark", debit=-disposal_gain))
disposal_lines.append(line("Trademark", credit=tm_cv_x1))
if disposal_gain > 0:
    disposal_lines.append(line("Gain on Disposal of Trademark", credit=disposal_gain))
journal_entries.append({
    "part": "d",
    "date": "20X2-04-01",
    "description": "Sale of the February 1, 20X1 purchased trademark (no amortization was ever recorded)",
    "lines": disposal_lines,
})

# (d) Dec 31, 20X2 -- crypto fair value AJ
journal_entries.append({
    "part": "d",
    "date": "20X2-12-31",
    "description": "Remeasure crypto assets to fair value; change to net income (ASC 350-60)",
    "lines": (
        [line("Crypto Assets", debit=crypto_adj_x2),
         line("Unrealized Gain--Crypto Assets (Income)", credit=crypto_adj_x2)]
        if crypto_adj_x2 > 0 else
        [line("Unrealized Loss--Crypto Assets (Income)", debit=-crypto_adj_x2),
         line("Crypto Assets", credit=-crypto_adj_x2)]
    ),
})

# Balance proof -- debits must equal credits in every entry.
for je in journal_entries:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert d == c, f"unbalanced entry {je['part']} {je['date']}: {d} vs {c}"


# ---------------------------------------------------------------------------
# Answers -- only figures the Required parts ask for
# ---------------------------------------------------------------------------

answers = [
    # (a)
    {"label": "a: trademark cost (Feb 1, 20X1 purchased trademark)", "value": num(trademark_cost)},
    {"label": "a: goodwill from the Oakridge Brands acquisition", "value": num(goodwill)},
    # (b)
    {"label": "b: Dec 31, 20X1 crypto fair value adjustment (unrealized gain to income)",
     "value": num(crypto_adj_x1)},
    {"label": "b: 20X1 amortization on purchased trademark (indefinite life - none)",
     "value": num(AMORT_X1["purchased trademark"])},
    {"label": "b: 20X1 amortization on acquired brand (indefinite life - none)",
     "value": num(AMORT_X1["acquired brand"])},
    {"label": "b: 20X1 amortization on acquired IPR&D (indefinite until completed/abandoned - none)",
     "value": num(AMORT_X1["acquired IPR&D"])},
    {"label": "b: 20X1 amortization on goodwill (not amortized - none)",
     "value": num(AMORT_X1["goodwill"])},
    # (c) carrying-value schedule
    {"label": "c: purchased Trademark carrying value 12/31/20X1", "value": num(tm_cv_x1)},
    {"label": "c: purchased Trademark carrying value 12/31/20X2 (sold 4/1/20X2)", "value": num(tm_cv_x2)},
    {"label": "c: Acquired Brand carrying value 12/31/20X1", "value": num(brand_cv_x1)},
    {"label": "c: Acquired Brand carrying value 12/31/20X2", "value": num(brand_cv_x2)},
    {"label": "c: IPR&D carrying value 12/31/20X1", "value": num(iprd_cv_x1)},
    {"label": "c: IPR&D carrying value 12/31/20X2", "value": num(iprd_cv_x2)},
    {"label": "c: Goodwill carrying value 12/31/20X1", "value": num(gw_cv_x1)},
    {"label": "c: Goodwill carrying value 12/31/20X2", "value": num(gw_cv_x2)},
    {"label": "c: Crypto carrying value 12/31/20X1", "value": num(crypto_cv_x1)},
    {"label": "c: Crypto carrying value 12/31/20X2", "value": num(crypto_cv_x2)},
    # (d)
    {"label": "d: loss on disposal of the purchased trademark (April 1, 20X2)",
     "value": num(-disposal_gain if disposal_gain < 0 else disposal_gain)},
    {"label": "d: gain/loss on disposal, signed (negative = loss)", "value": num(disposal_gain)},
    {"label": "d: Dec 31, 20X2 crypto fair value adjustment (unrealized loss to income)",
     "value": num(-crypto_adj_x2 if crypto_adj_x2 < 0 else crypto_adj_x2)},
]

notes = (
    "Trademark cost = $120,000 purchase price + $8,000 external registration/legal fees = $128,000. "
    "Goodwill = $780,000 consideration - ($820,000 identifiable assets at FV - $250,000 liabilities "
    "assumed) = $210,000. No amortization is recorded on the purchased trademark, the acquired brand, "
    "acquired IPR&D (indefinite-lived until the project is completed or abandoned), or goodwill; they are "
    "impairment-tested only and the stem states there is no impairment. Acquired customer relationships "
    "($45,000) are finite-lived and would be amortized, but part (b) does not ask about them. Crypto is "
    "carried at fair value each reporting date with remeasurement in net income (ASC 350-60): +$5,000 in "
    "20X1 ($75,000 -> $80,000) and -$12,000 in 20X2 ($80,000 -> $68,000). The April 1, 20X2 sale yields a "
    "$18,000 loss ($110,000 proceeds - $128,000 carrying amount); no amortization catch-up applies. "
    "All journal entries balance."
)

output = {
    "id": "agent_352#01",
    "rounding_convention": (
        "decimal.Decimal throughout, no floats; every amount quantized to the cent with "
        "ROUND_HALF_UP applied per computed amount/period (not only at the end). No present "
        "value work is required by this fact pattern, so no PV table factors are used."
    ),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": notes,
}

print(json.dumps(output, indent=2))
