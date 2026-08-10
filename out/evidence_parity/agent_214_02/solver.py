"""Solver for agent_214#02 - LO 12-7 multi-asset recoverability, impairment JE,
post-write-down subsequent measurement schedule.

Rounding convention: all money is decimal.Decimal, quantized to the cent with
ROUND_HALF_UP applied per period (each year's depreciation is rounded on its own,
not derived from a rounded cumulative figure). No floats anywhere. Every figure is
derived from the fact table below; nothing is hard-coded.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def n(x): return float(q(x))

# --- given facts -------------------------------------------------------------
assets = [
    {"tag": "A", "name": "Precision press",  "cost": Decimal("400000"), "accdep": Decimal("100000"),
     "undisc": Decimal("350000"), "fv": Decimal("280000")},
    {"tag": "B", "name": "Curing oven",      "cost": Decimal("700000"), "accdep": Decimal("200000"),
     "undisc": Decimal("420000"), "fv": Decimal("310000")},
    {"tag": "C", "name": "Assembly conveyor","cost": Decimal("900000"), "accdep": Decimal("150000"),
     "undisc": Decimal("750000"), "fv": Decimal("600000")},
]
B_LIFE = 5                      # more years for Asset B after write-down
B_RESIDUAL = Decimal("10000")   # revised residual on Asset B

answers = []
jes = []

# --- part a: carrying amount, recoverability test, impairment loss -----------
total_loss = Decimal("0")
impaired = []
for a in assets:
    ca = q(a["cost"] - a["accdep"])
    a["ca"] = ca
    # Recoverability test: impaired only if CA exceeds undiscounted future cash flows.
    fails = a["undisc"] < ca
    loss = q(ca - a["fv"]) if fails else Decimal("0.00")
    a["loss"] = loss
    total_loss += loss
    if fails:
        impaired.append(a)
    answers.append({"label": "a: Asset %s (%s) carrying amount at 12/31/Yr3" % (a["tag"], a["name"]), "value": n(ca)})
    answers.append({"label": "a: Asset %s recoverability test (undiscounted $%s vs carrying $%s)"
                    % (a["tag"], q(a["undisc"]), ca),
                    "value": "Fails recoverability test - impaired" if fails
                             else "Passes recoverability test - not impaired"})
    answers.append({"label": "a: Asset %s impairment loss" % a["tag"], "value": n(loss)})
answers.append({"label": "a: Total impairment loss recognized 12/31/Yr3", "value": n(total_loss)})

# --- part b: single combined journal entry ----------------------------------
lines = [{"account": "Loss on Impairment", "debit": n(total_loss), "credit": 0}]
for a in impaired:
    lines.append({"account": "Accumulated Depreciation - %s (Asset %s)" % (a["name"], a["tag"]),
                  "debit": 0, "credit": n(a["loss"])})
jes.append({"part": "b", "lines": lines})
answers.append({"label": "b: Dec 31, Year 3 entry - debit Loss on Impairment", "value": n(total_loss)})
answers.append({"label": "b: Dec 31, Year 3 entry - credit Accumulated Depreciation (Asset B, Curing oven)",
                "value": n(total_loss)})

# --- part c: Asset B subsequent measurement schedule ------------------------
B = [a for a in assets if a["tag"] == "B"][0]
new_basis = q(B["ca"] - B["loss"])          # = fair value at write-down
depreciable = q(new_basis - B_RESIDUAL)
annual = q(depreciable / Decimal(B_LIFE))   # ROUND_HALF_UP per period
answers.append({"label": "c: Asset B carrying amount after write-down (new depreciable base)", "value": n(new_basis)})
answers.append({"label": "c: Asset B depreciable cost (new basis less $%s residual)" % q(B_RESIDUAL),
                "value": n(depreciable)})
answers.append({"label": "c: Asset B annual straight-line depreciation, Years 4-8", "value": n(annual)})

accum = Decimal("0")
carry = new_basis
for i in range(B_LIFE):
    yr = 4 + i
    dep = annual
    if i == B_LIFE - 1:                      # true-up final period to residual
        dep = q(carry - B_RESIDUAL)
    accum = q(accum + dep)
    carry = q(carry - dep)
    answers.append({"label": "c: Year %d depreciation expense (Asset B)" % yr, "value": n(dep)})
    answers.append({"label": "c: Year %d accumulated depreciation since write-down (Asset B)" % yr, "value": n(accum)})
    answers.append({"label": "c: Year %d ending carrying amount (Asset B)" % yr, "value": n(carry)})
answers.append({"label": "c: Asset B carrying amount at end of Year 8 (equals residual)", "value": n(carry)})

jes.append({"part": "c", "lines": [
    {"account": "Depreciation Expense - Curing Oven (Asset B)", "debit": n(annual), "credit": 0},
    {"account": "Accumulated Depreciation - Curing Oven (Asset B)", "debit": 0, "credit": n(annual)},
]})

# --- part d ------------------------------------------------------------------
answers.append({"label": "d: Why fair value below carrying amount can still mean no impairment loss",
                "value": ("Impairment is a two-step test for assets held for use. Step 1 (recoverability) "
                          "compares the carrying amount with the TOTAL UNDISCOUNTED future cash flows expected "
                          "from use and disposal; a loss is recorded only if the carrying amount exceeds that "
                          "undiscounted amount. Only if step 1 fails is the loss measured in step 2 as carrying "
                          "amount less fair value. Fair value is a discounted, market-based exit price, so it is "
                          "normally lower than undiscounted cash flows. Assets A and C recover their carrying "
                          "amounts on an undiscounted basis ($350,000 > $300,000; $750,000 = $750,000), so they "
                          "pass step 1 and no loss is recognized even though each has a fair value below carrying "
                          "amount.")})

# --- proof: Dr = Cr on every entry ------------------------------------------
for je in jes:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert d == c, (je["part"], d, c)

print(json.dumps({
    "id": "agent_214#02",
    "rounding_convention": "decimal.Decimal throughout (no floats); ROUND_HALF_UP to the cent applied per period, with the final year of the Asset B schedule trued up so the ending carrying amount equals the $10,000 residual",
    "answers": answers,
    "journal_entries": jes,
    "insufficient_info": False,
    "notes": "Recoverability test fails only when carrying amount EXCEEDS undiscounted future cash flows. Asset A: $350,000 > $300,000 - passes. Asset C: $750,000 = $750,000 - equal, so it passes (no loss). Asset B: $420,000 < $500,000 - fails, loss = $500,000 - $310,000 fair value = $190,000. Part b is a single combined entry covering the only impaired asset (B); the credit is to Accumulated Depreciation, leaving the asset at historical cost with a new $310,000 book basis. Asset B then depreciates ($310,000 - $10,000) / 5 = $60,000 per year for Years 4-8, ending at the $10,000 residual. Assets A and C keep their pre-existing depreciation policies and are unaffected."
}, indent=1))
