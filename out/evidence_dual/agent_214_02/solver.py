"""Solver for agent_214#02 — Redwood Circuits LLC, Dec 31 Year 3 multi-asset impairment.

Rounding convention: all money is decimal.Decimal; every computed amount is
quantized to whole dollars with ROUND_HALF_UP per period (each period's
depreciation is rounded independently, not derived from a rounded cumulative).
The Asset B schedule closes exactly to the revised residual value of $10,000
(no plug was needed: the depreciable base divides evenly).

Model (held-and-used long-lived assets, two-step test):
  Step 1 recoverability: impaired only if SUM of expected UNDISCOUNTED future
  cash flows ("recoverable cost") is LESS THAN carrying amount. Equality passes.
  Step 2 measurement: loss = carrying amount - fair value, for failing assets only.
Everything below is derived from the stem's table; no figure is hard-coded.
"""
from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("1")


def d(x):
    return Decimal(x)


def money(x):
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def num(x):
    return int(x) if x == x.to_integral_value() else float(x)


# ---- stem facts -------------------------------------------------------------
assets = [
    {"key": "A", "name": "Precision press", "cost": d("400000"),
     "accum_dep": d("100000"), "recoverable": d("350000"), "fair_value": d("280000")},
    {"key": "B", "name": "Curing oven", "cost": d("700000"),
     "accum_dep": d("200000"), "recoverable": d("420000"), "fair_value": d("310000")},
    {"key": "C", "name": "Assembly conveyor", "cost": d("900000"),
     "accum_dep": d("150000"), "recoverable": d("750000"), "fair_value": d("600000")},
]
B_LIFE_YEARS = 5
B_RESIDUAL = d("10000")
B_FIRST_YEAR = 4

answers = []
journal_entries = []

# ---- part a: carrying amount, recoverability test, impairment loss ----------
total_loss = d("0")
for a in assets:
    ca = money(a["cost"] - a["accum_dep"])
    a["carrying"] = ca
    fails = a["recoverable"] < ca          # strict: equality passes
    a["fails"] = fails
    loss = money(ca - a["fair_value"]) if fails else d("0")
    a["loss"] = loss
    total_loss += loss
    shortfall = money(ca - a["recoverable"])
    label = f"Asset {a['key']} — {a['name']}"
    answers.append({"label": f"a: {label} — carrying amount at 12/31/Yr3 (cost - accumulated depreciation)",
                    "value": num(ca)})
    answers.append({"label": f"a: {label} — step 1 recoverability: undiscounted recoverable cost vs carrying amount",
                    "value": (f"${num(a['recoverable']):,} recoverable vs ${num(ca):,} carrying — "
                              + (f"recoverable is LESS by ${num(shortfall):,} -> test FAILS, asset is impaired"
                                 if fails else
                                 ("recoverable EQUALS carrying amount -> test PASSES, not impaired"
                                  if a["recoverable"] == ca else
                                  f"recoverable EXCEEDS carrying by ${num(-shortfall):,} -> test PASSES, not impaired")))})
    answers.append({"label": f"a: {label} — impairment loss recognized (carrying - fair value, only if step 1 fails)",
                    "value": num(loss)})

answers.append({"label": "a: total impairment loss recognized at 12/31/Year 3 (all three assets)",
                "value": num(money(total_loss))})
answers.append({"label": "a: assets impaired / not impaired",
                "value": ("impaired: " + ", ".join(x["key"] for x in assets if x["fails"]) +
                          "; not impaired: " + ", ".join(x["key"] for x in assets if not x["fails"]))})

# ---- part b: single combined impairment journal entry -----------------------
lines = [{"account": "Loss on Impairment", "debit": num(money(total_loss)), "credit": 0}]
for a in assets:
    if a["fails"]:
        lines.append({"account": f"Accumulated Depreciation—{a['name']} (Asset {a['key']})",
                      "debit": 0, "credit": num(a["loss"])})
journal_entries.append({"part": "b", "date": "December 31, Year 3", "lines": lines})
answers.append({"label": "b: single 12/31/Year 3 entry — total debit to Loss on Impairment",
                "value": num(money(total_loss))})
answers.append({"label": "b: single 12/31/Year 3 entry — credit to Accumulated Depreciation—Curing Oven (Asset B)",
                "value": num(next(x["loss"] for x in assets if x["key"] == "B"))})
answers.append({"label": "b: entries for Assets A and C",
                "value": "none — both passed the undiscounted recoverability test, so no loss is recorded for them"})

# ---- part c: Asset B subsequent measurement schedule ------------------------
B = next(x for x in assets if x["key"] == "B")
b_new_basis = money(B["carrying"] - B["loss"])            # = fair value after write-down
b_dep_base = money(b_new_basis - B_RESIDUAL)
b_gross_accum_after = money(B["accum_dep"] + B["loss"])   # ties to cost - new basis

answers.append({"label": "c: Asset B new carrying amount immediately after the write-down (new depreciable basis)",
                "value": num(b_new_basis)})
answers.append({"label": "c: Asset B accumulated depreciation balance immediately after the write-down (old $ + impairment credit)",
                "value": num(b_gross_accum_after)})
answers.append({"label": "c: Asset B revised depreciable base (new carrying amount - revised residual $10,000)",
                "value": num(b_dep_base)})

annual = money(b_dep_base / Decimal(B_LIFE_YEARS))
schedule = []
accum = d("0")
carrying = b_new_basis
for i in range(B_LIFE_YEARS):
    yr = B_FIRST_YEAR + i
    if i == B_LIFE_YEARS - 1:
        expense = money(b_dep_base - accum)   # close exactly to residual
    else:
        expense = annual
    accum = money(accum + expense)
    carrying = money(b_new_basis - accum)
    schedule.append({"year": yr, "expense": expense, "accum": accum, "carrying": carrying})

answers.append({"label": "c: Asset B annual straight-line depreciation, Years 4-8 ($300,000 base / 5 years)",
                "value": num(annual)})
for row in schedule:
    answers.append({"label": f"c: Asset B schedule Year {row['year']} — depreciation expense",
                    "value": num(row["expense"])})
    answers.append({"label": f"c: Asset B schedule Year {row['year']} — accumulated depreciation since write-down",
                    "value": num(row["accum"])})
    answers.append({"label": f"c: Asset B schedule Year {row['year']} — carrying amount, end of year",
                    "value": num(row["carrying"])})
answers.append({"label": "c: Asset B carrying amount at end of Year 8 equals revised residual value",
                "value": num(schedule[-1]["carrying"])})
answers.append({"label": "c: Asset B total depreciation recorded over Years 4-8",
                "value": num(money(sum((r["expense"] for r in schedule), d("0"))))})

journal_entries.append({"part": "c", "date": "December 31, Year 4", "lines": [
    {"account": "Depreciation Expense", "debit": num(schedule[0]["expense"]), "credit": 0},
    {"account": f"Accumulated Depreciation—{B['name']} (Asset B)", "debit": 0,
     "credit": num(schedule[0]["expense"])},
]})

# ---- part d ----------------------------------------------------------------
answers.append({"label": "d: why fair value below carrying amount can still mean no impairment loss",
                "value": ("The screen is a two-step test. Step 1 compares carrying amount to the SUM of "
                          "expected future cash flows on an UNDISCOUNTED basis; a loss is recognized only if "
                          "those undiscounted flows are less than carrying amount. Fair value (a discounted / "
                          "market exit price) is only the step-2 measurement input, so it is never compared to "
                          "carrying amount unless step 1 already failed. Because undiscounted flows ignore the "
                          "time value of money and any resale discount, they can recover the carrying amount "
                          "even when fair value does not — Assets A ($350,000 vs $300,000) and C ($750,000 vs "
                          "$750,000, equal so it passes) are exactly that case, and no loss is booked despite "
                          "fair values of $280,000 and $600,000. Holding and using the asset, not selling it, "
                          "is what recovers the cost.")})

# ---- internal proofs -------------------------------------------------------
for je in journal_entries:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, (je["part"], dr, cr)
assert b_new_basis == B["fair_value"]
assert money(B["cost"] - b_gross_accum_after) == b_new_basis
assert schedule[-1]["carrying"] == B_RESIDUAL
assert money(sum((r["expense"] for r in schedule), d("0"))) == b_dep_base

out = {
    "id": "agent_214#02",
    "rounding_convention": ("decimal.Decimal throughout; ROUND_HALF_UP to whole dollars per period; "
                            "final schedule year plugged to close Asset B exactly to its $10,000 revised "
                            "residual (no plug was required — $300,000 / 5 = $60,000 exactly)"),
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": ("Held-and-used two-step test: step 1 compares carrying amount with UNDISCOUNTED expected cash "
              "flows ('recoverable cost'); step 2 measures loss as carrying amount less fair value. "
              "A — CA $300,000 vs $350,000 undiscounted: passes, no loss (fair value $280,000 is irrelevant). "
              "B — CA $500,000 vs $420,000: fails; loss $500,000 - $310,000 = $190,000. "
              "C — CA $750,000 vs $750,000 undiscounted: recoverable cost is NOT less than carrying amount, "
              "so the test passes and no loss is recognized (fair value $600,000 is irrelevant); this "
              "tie-goes-to-no-impairment point is the trap in the item. Part b is therefore a single entry of "
              "$190,000 for Asset B only. The impairment credit is shown in Accumulated Depreciation, which "
              "keeps Cost $700,000 / Accum. dep. $390,000 / carrying $310,000; crediting the asset account "
              "directly for $190,000 (cost $510,000, accum. dep. $200,000) is an accepted alternative and "
              "changes no amount. Written-down basis $310,000 becomes the new depreciable basis; less the "
              "revised $10,000 residual gives a $300,000 base over 5 years = $60,000 per year for Years 4-8, "
              "ending at exactly $10,000. Impairment losses on held-and-used assets are not reversed if value "
              "later recovers.")
}
print(json.dumps(out, indent=2))
