"""Cedarline Outdoor Gear - assurance-type warranty (LO 15-5).

Rounding convention: all money handled with decimal.Decimal (never float);
each period's computed amount is quantized to the cent using
ROUND_HALF_UP at the moment it is computed (per-period rounding), and
rounded per-period amounts roll forward into the liability schedule.
Every figure is derived from the scenario inputs; nothing is hard-coded.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def q(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


def num(d):
    d = q(d)
    return int(d) if d == d.to_integral_value() else float(d)


# ---- inputs (from the scenario) ----
RATE = Decimal("0.015")
sales = {1: Decimal("2400000"), 2: Decimal("2800000"), 3: Decimal("3000000")}
claims = {1: Decimal("12000"), 2: Decimal("48000"), 3: Decimal("55000")}
years = [1, 2, 3]

# ---- derived: accruals and liability rollforward ----
accrual = {y: q(sales[y] * RATE) for y in years}
begin, end = {}, {}
bal = q(Decimal("0"))
for y in years:
    begin[y] = bal
    bal = q(begin[y] + accrual[y] - claims[y])
    end[y] = bal

answers = []
a = answers.append

a({"label": "a: Year 1 product sales - Cash debited (= Sales revenue credited)",
   "value": num(sales[1])})
a({"label": "b: Dec 31, Year 1 adjusting accrual - Warranty expense (1.5% x Year 1 sales)",
   "value": num(accrual[1])})
a({"label": "c: Year 1 warranty claims paid - Warranty liability debited / Cash credited",
   "value": num(claims[1])})

for y in years:
    a({"label": f"d: Year {y} warranty liability - beginning balance", "value": num(begin[y])})
    a({"label": f"d: Year {y} warranty liability - add accrual (1.5% of sales)", "value": num(accrual[y])})
    a({"label": f"d: Year {y} warranty liability - less actual claims paid", "value": num(claims[y])})
    a({"label": f"d: Year {y} warranty liability - ending balance", "value": num(end[y])})

a({"label": "e: Dec 31, Year 2 adjusting accrual - Warranty expense (1.5% x Year 2 sales)",
   "value": num(accrual[2])})
a({"label": "f: Year 3 warranty claims paid - Warranty liability debited / Cash credited",
   "value": num(claims[3])})
a({"label": "g: Assurance-type warranty is a loss contingency, not deferred revenue",
   "value": ("It is not a separate performance obligation - it is not sold separately and "
             "simply guarantees the product already delivered meets agreed specifications, "
             "so no transaction price is allocated to it and no revenue is deferred. Instead "
             "it is a probable, reasonably estimable future sacrifice arising from the past "
             "sale, so the full estimated cost is expensed and accrued as a liability in the "
             "year of sale (matching), and later claims are charged against that liability.")})

je = [
    {"part": "a", "lines": [
        {"account": "Cash", "debit": num(sales[1]), "credit": 0},
        {"account": "Sales Revenue", "debit": 0, "credit": num(sales[1])}]},
    {"part": "b", "lines": [
        {"account": "Warranty Expense", "debit": num(accrual[1]), "credit": 0},
        {"account": "Estimated Warranty Liability", "debit": 0, "credit": num(accrual[1])}]},
    {"part": "c", "lines": [
        {"account": "Estimated Warranty Liability", "debit": num(claims[1]), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": num(claims[1])}]},
    {"part": "e", "lines": [
        {"account": "Warranty Expense", "debit": num(accrual[2]), "credit": 0},
        {"account": "Estimated Warranty Liability", "debit": 0, "credit": num(accrual[2])}]},
    {"part": "f", "lines": [
        {"account": "Estimated Warranty Liability", "debit": num(claims[3]), "credit": 0},
        {"account": "Cash", "debit": 0, "credit": num(claims[3])}]},
]

for e in je:
    dr = sum(Decimal(str(l["debit"])) for l in e["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in e["lines"])
    assert dr == cr, e["part"]

notes = ("Warranty accrual each year = 1.5% x that year's sales: Yr1 36,000; Yr2 42,000; Yr3 45,000. "
         "Liability rollforward: 0 + 36,000 - 12,000 = 24,000 (end Yr1); "
         "24,000 + 42,000 - 48,000 = 18,000 (end Yr2); 18,000 + 45,000 - 55,000 = 8,000 (end Yr3). "
         "Claims are charged to the liability (not to expense) because the cost was already accrued; "
         "the two-year coverage is why Year 1 claims are small relative to the accrual and later "
         "years' claims exceed that year's accrual. Cost of goods sold ignored per instructions; "
         "the liability stays positive throughout, so no expense catch-up is required.")

print(json.dumps({
    "id": "agent_229#00",
    "rounding_convention": ("decimal.Decimal throughout; amounts quantized to the cent with "
                            "ROUND_HALF_UP per period (each year's accrual rounded when computed, "
                            "then rolled forward); all amounts here are exact whole dollars"),
    "answers": answers,
    "journal_entries": je,
    "insufficient_info": False,
    "notes": notes,
}, indent=1))
