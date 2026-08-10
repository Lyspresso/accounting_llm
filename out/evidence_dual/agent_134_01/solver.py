"""Independent cold derivation of agent_134#01 (LO 14-2, trading securities FV-NI).

Rounding convention: all monetary math uses decimal.Decimal; every per-period
amount (cash interest, required FVA balance, each period's FVA adjustment) is
rounded to whole dollars with ROUND_HALF_UP at the moment it is computed for
that period. Bonds were bought at par, so there is no premium/discount to
amortize and no present-value work is required; the FVA schedule closes exactly
(cumulative unrealized G/L ties to proceeds - cost with zero residual).

Model: cost-plus-Fair-Value-Adjustment (FVA) account. The investment account
stays at original cost ($ par ) and FVA--TS carries the cumulative difference
between fair value and cost. Positive FVA = debit balance, negative = credit.
"""
from decimal import Decimal, ROUND_HALF_UP
import json

C = Decimal("1")
def d(x):  # whole-dollar, ROUND_HALF_UP
    return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)

# ---------------- facts from the stem ----------------
par           = Decimal("40000")
stated_rate   = Decimal("0.06")
price_pct     = Decimal("1")          # "purchased for par"
fv_y1         = Decimal("38500")
fv_y2         = Decimal("41200")
proceeds_y3   = Decimal("41000")
periods_per_yr = 1                     # interest paid annually

cost = d(par * price_pct)

# ---------------- (b) cash interest ----------------
cash_interest = d(par * stated_rate / periods_per_yr)
# par purchase -> no amortization -> interest income == cash interest
interest_income_y1 = cash_interest

# ---------------- FVA engine ----------------
fva_bal = Decimal("0")                 # beginning FVA--TS is zero
def fva_step(fair_value, label):
    """Return (required_bal, prior_bal, adjustment) and roll the balance."""
    global fva_bal
    required = d(fair_value - cost)
    prior = fva_bal
    adj = d(required - prior)
    fva_bal = required
    return {"label": label, "cost": cost, "fair_value": fair_value,
            "required": required, "prior": prior, "adjustment": adj}

s1 = fva_step(fv_y1, "Dec 31 Year 1")
s2 = fva_step(fv_y2, "Dec 31 Year 2")
s3 = fva_step(proceeds_y3, "Jan 1 Year 3 (sale date FV = proceeds)")

carry_y1 = d(cost + s1["required"])
carry_y2 = d(cost + s2["required"])
carry_sale = d(cost + s3["required"])

# ---------------- (g) cumulative proof ----------------
cum = d(s1["adjustment"] + s2["adjustment"] + s3["adjustment"])
target = d(proceeds_y3 - cost)
residual = d(cum - target)
assert residual == 0, (cum, target)

# realized gain/loss at sale, after adjusting carrying amount to FV
realized = d(proceeds_y3 - carry_sale)
assert realized == 0

# NI effects
ni_y1 = d(interest_income_y1 + s1["adjustment"])

def sgn(x):  # helper for labels
    return "gain" if x > 0 else ("loss" if x < 0 else "none")

# ---------------- journal entries ----------------
def L(acct, dr=Decimal("0"), cr=Decimal("0")):
    return {"account": acct, "debit": int(d(dr)), "credit": int(d(cr))}

jes = []
jes.append({"part": "a", "lines": [
    L("Investment in Trading Securities (Redwood Corp. bonds), at cost", dr=cost),
    L("Cash", cr=cost)]})
jes.append({"part": "b", "lines": [
    L("Cash", dr=cash_interest),
    L("Interest Income (Interest Revenue)", cr=interest_income_y1)]})
# (c) Y1 FVA adjust: adjustment is negative -> credit FVA, debit unrealized loss
a1 = s1["adjustment"]
jes.append({"part": "c", "lines": (
    [L("Unrealized Loss on Trading Securities (NI)", dr=-a1),
     L("Fair Value Adjustment--Trading Securities", cr=-a1)] if a1 < 0 else
    [L("Fair Value Adjustment--Trading Securities", dr=a1),
     L("Unrealized Gain on Trading Securities (NI)", cr=a1)])})
a2 = s2["adjustment"]
jes.append({"part": "e", "lines": (
    [L("Fair Value Adjustment--Trading Securities", dr=a2),
     L("Unrealized Gain on Trading Securities (NI)", cr=a2)] if a2 > 0 else
    [L("Unrealized Loss on Trading Securities (NI)", dr=-a2),
     L("Fair Value Adjustment--Trading Securities", cr=-a2)])})
a3 = s3["adjustment"]
jes.append({"part": "f-i", "lines": (
    [L("Unrealized Loss on Trading Securities (NI)", dr=-a3),
     L("Fair Value Adjustment--Trading Securities", cr=-a3)] if a3 < 0 else
    [L("Fair Value Adjustment--Trading Securities", dr=a3),
     L("Unrealized Gain on Trading Securities (NI)", cr=a3)])})
sale_lines = [L("Cash", dr=proceeds_y3)]
fva_end = s3["required"]
if fva_end > 0:
    sale_lines.append(L("Fair Value Adjustment--Trading Securities", cr=fva_end))
elif fva_end < 0:
    sale_lines.insert(1, L("Fair Value Adjustment--Trading Securities", dr=-fva_end))
sale_lines.append(L("Investment in Trading Securities (at cost)", cr=cost))
if realized > 0:
    sale_lines.append(L("Realized Gain on Sale of Trading Securities", cr=realized))
elif realized < 0:
    sale_lines.insert(1, L("Realized Loss on Sale of Trading Securities", dr=-realized))
jes.append({"part": "f-ii", "lines": sale_lines})

for je in jes:
    assert sum(l["debit"] for l in je["lines"]) == sum(l["credit"] for l in je["lines"]), je

# ---------------- answers ----------------
A = []
def add(label, value):
    A.append({"label": label, "value": int(value) if isinstance(value, Decimal) else value})

add("a: purchase price paid = par x 100% (Dr Investment in TS)", cost)
add("a: Cash credited", cost)
add("b: annual cash interest = $40,000 x 6% x 1 yr", cash_interest)
add("b: interest income Year 1 (par purchase, no amortization)", interest_income_y1)
add("c: FVA schedule Y1 -- cost (carrying at amortized/original cost)", cost)
add("c: FVA schedule Y1 -- fair value Dec 31 Y1", fv_y1)
add("c: FVA schedule Y1 -- required FVA balance (FV - cost), negative = credit", s1["required"])
add("c: FVA schedule Y1 -- FVA balance before adjustment (beginning)", s1["prior"])
add("c: FVA schedule Y1 -- adjustment needed (negative = credit FVA)", s1["adjustment"])
add("c: Year 1 unrealized loss recognized in NI", -s1["adjustment"])
add("c: FVA--TS ending balance Dec 31 Y1 (credit)", s1["required"])
add("d: BS Dec 31 Y1 -- Trading securities at fair value (current asset)", carry_y1)
add("d: BS Dec 31 Y1 -- investment at cost", cost)
add("d: BS Dec 31 Y1 -- less Fair Value Adjustment--TS (credit)", -s1["required"])
add("d: IS Year 1 -- Interest income", interest_income_y1)
add("d: IS Year 1 -- Unrealized loss on trading securities (in NI, other income/expense)", -s1["adjustment"])
add("d: IS Year 1 -- net pretax effect on Year 1 net income", ni_y1)
add("e: rollforward Y2 -- cost", cost)
add("e: rollforward Y2 -- fair value Dec 31 Y2", fv_y2)
add("e: rollforward Y2 -- required FVA balance (FV - cost), positive = debit", s2["required"])
add("e: rollforward Y2 -- FVA balance before adjustment (from Y1, credit 1,500)", s2["prior"])
add("e: rollforward Y2 -- adjustment needed (positive = debit FVA)", s2["adjustment"])
add("e: Year 2 unrealized gain recognized in NI", s2["adjustment"])
add("e: FVA--TS ending balance Dec 31 Y2 (debit)", s2["required"])
add("e: carrying amount = fair value Dec 31 Y2", carry_y2)
add("f-i: sale-date fair value (= proceeds) Jan 1 Y3", proceeds_y3)
add("f-i: required FVA balance at sale date (FV - cost)", s3["required"])
add("f-i: FVA balance before sale-date adjustment", s3["prior"])
add("f-i: sale-date FV-NI adjustment (negative = credit FVA)", s3["adjustment"])
add("f-i: unrealized loss recognized at sale date (Year 3 NI)", -s3["adjustment"])
add("f-ii: Cash received on sale", proceeds_y3)
add("f-ii: FVA--TS eliminated (credited, debit balance removed)", s3["required"])
add("f-ii: Investment in TS removed at cost (credit)", cost)
add("f-ii: realized gain/loss on sale after FV adjustment", realized)
add("g: holding-period unrealized G/L -- Year 1", s1["adjustment"])
add("g: holding-period unrealized G/L -- Year 2", s2["adjustment"])
add("g: holding-period unrealized G/L -- Year 3 (sale date)", s3["adjustment"])
add("g: cumulative unrealized G/L recognized in NI over holding period", cum)
add("g: proceeds - cost", target)
add("g: residual (schedule closes exactly)", residual)
add("g: total NI effect including interest, Years 1-3 (interest 2,400 x 2 yrs + 1,000)",
    d(cash_interest * 2 + cum))

out = {
 "id": "agent_134#01",
 "rounding_convention": ("decimal.Decimal throughout, ROUND_HALF_UP to whole dollars "
   "applied per period as each figure is computed; bonds bought at par so no "
   "premium/discount amortization and no PV rounding -- FVA schedule closes exactly "
   "to zero residual (cumulative unrealized G/L = proceeds - cost)."),
 "answers": A,
 "journal_entries": jes,
 "insufficient_info": False,
 "notes": ("Cost-plus-FVA (valuation allowance) presentation: Investment in TS stays at "
   "$40,000 cost; FVA--TS carries cumulative FV-cost. Par purchase => interest income "
   "= cash interest $2,400/yr, no discount/premium. FVA rollforward: 0 -> (1,500) cr at "
   "12/31/Y1 -> 1,200 dr at 12/31/Y2 (2,700 dr swing) -> 1,000 dr at 1/1/Y3 sale date "
   "(200 cr adjust); eliminating entry leaves zero realized gain because carrying amount "
   "was first marked to the $41,000 sale price. Cumulative unrealized: (1,500) + 2,700 + "
   "(200) = 1,000 = 41,000 proceeds - 40,000 cost. Direct-write-down (no FVA account) "
   "would give identical NI amounts. Year 2 cash interest of $2,400 (Dr Cash / Cr Interest "
   "income) is implied by the fact pattern but not requested as a separate part; no "
   "interest accrues for the Jan 1 Year 3 sale date since the 12/31/Y2 coupon was just paid.")
}
print(json.dumps(out, indent=1))
