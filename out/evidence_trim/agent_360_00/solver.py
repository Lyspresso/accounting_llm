"""Solver for agent_360#00 (Ironwood Consumer Products).

ROUNDING CONVENTION: all money uses decimal.Decimal (never float) and is
quantized to the cent (0.01) with ROUND_HALF_UP, applied per period /
per computed line item (each year's warranty accrual is rounded on its own
before it enters the liability roll-forward). Every figure is derived from
the scenario inputs below; nothing is hard-coded.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
def q(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)

def num(d):
    d = q(d)
    return int(d) if d == d.to_integral_value() else float(d)

# ---------------- inputs (from scenario) ----------------
SUIT_SOUGHT      = Decimal("350000")
RANGE_LOW        = Decimal("90000")
RANGE_HIGH       = Decimal("280000")
BETTER_ESTIMATE  = Decimal("120000")
SETTLEMENT       = Decimal("145000")

WARRANTY_RATE    = Decimal("0.020")          # 2.0% of that year's product sales
SALES  = {1: Decimal("3200000"), 2: Decimal("3600000"), 3: Decimal("4000000")}
CLAIMS = {1: Decimal("18000"),   2: Decimal("52000"),   3: Decimal("61000")}

# ---------------- litigation ----------------
# (a) probable + reasonably estimable -> accrue counsel's better estimate
accrual_a = q(BETTER_ESTIMATE)
assert RANGE_LOW <= accrual_a <= RANGE_HIGH

# (b) recognized (Type 1) subsequent event: condition existed at 12/31/Y1, so the
#     12/31/Y1 liability is remeasured to the settlement amount.
remeasured_liab = q(SETTLEMENT)
incremental_loss = q(remeasured_liab - accrual_a)

# (c) settlement payment 5/1/Y2 extinguishes the recorded liability
cash_paid = q(remeasured_liab)

# ---------------- warranty ----------------
accrual = {y: q(SALES[y] * WARRANTY_RATE) for y in SALES}
sched, beg = {}, Decimal("0.00")   # first year of the program -> beginning bal 0
for y in sorted(SALES):
    end = q(beg + accrual[y] - CLAIMS[y])
    sched[y] = {"beginning": q(beg), "accrual": accrual[y],
                "claims": q(CLAIMS[y]), "ending": end}
    beg = end

# ---------------- journal entries ----------------
def je(part, desc, lines):
    d = sum(q(l[1]) for l in lines)
    c = sum(q(l[2]) for l in lines)
    assert d == c, (part, d, c)
    return {"part": part, "description": desc,
            "lines": [{"account": a, "debit": num(dr), "credit": num(cr)}
                      for a, dr, cr in lines]}

Z = Decimal("0")
jes = [
    je("a", "12/31/Y1 period-end AJE - accrue probable & estimable litigation loss at counsel's better estimate",
       [("Loss from Litigation (Litigation Expense)", accrual_a, Z),
        ("Estimated Litigation Liability", Z, accrual_a)]),
    je("b", "12/31/Y1 period-end AJE - recognized subsequent event: remeasure litigation liability to the 2/18/Y2 settlement amount",
       [("Loss from Litigation (Litigation Expense)", incremental_loss, Z),
        ("Estimated Litigation Liability", Z, incremental_loss)]),
    je("c", "5/1/Y2 - pay litigation settlement",
       [("Estimated Litigation Liability", cash_paid, Z),
        ("Cash", Z, cash_paid)]),
    je("d", "Year 1 - record cash product sales",
       [("Cash", SALES[1], Z), ("Sales Revenue", Z, SALES[1])]),
    je("d", "12/31/Y1 period-end AJE - accrue assurance-type warranty at 2.0% of Year 1 sales",
       [("Warranty Expense", accrual[1], Z),
        ("Estimated Warranty Liability", Z, accrual[1])]),
    je("d", "Year 1 - actual warranty claims paid in cash",
       [("Estimated Warranty Liability", CLAIMS[1], Z), ("Cash", Z, CLAIMS[1])]),
    je("f", "12/31/Y2 period-end AJE - accrue assurance-type warranty at 2.0% of Year 2 sales",
       [("Warranty Expense", accrual[2], Z),
        ("Estimated Warranty Liability", Z, accrual[2])]),
]

# ---------------- answers ----------------
answers = [
 {"label": "a: 12/31/Y1 AJE - Dr Loss from Litigation / Cr Estimated Litigation Liability (better estimate within the probable, estimable range)", "value": num(accrual_a)},
 {"label": "b: 12/31/Y1 recognized-subsequent-event AJE - additional Dr Loss from Litigation / Cr Estimated Litigation Liability", "value": num(incremental_loss)},
 {"label": "b: remeasured 12/31/Y1 Estimated Litigation Liability balance after the 2/18/Y2 settlement agreement", "value": num(remeasured_liab)},
 {"label": "c: 5/1/Y2 - Dr Estimated Litigation Liability / Cr Cash", "value": num(cash_paid)},
 {"label": "d: Year 1 product sales - Dr Cash / Cr Sales Revenue", "value": num(SALES[1])},
 {"label": "d: 12/31/Y1 warranty AJE - Dr Warranty Expense / Cr Estimated Warranty Liability", "value": num(accrual[1])},
 {"label": "d: Year 1 claims settled - Dr Estimated Warranty Liability / Cr Cash", "value": num(CLAIMS[1])},
]
for y in sorted(sched):
    for k in ("beginning", "accrual", "claims", "ending"):
        lbl = {"beginning": "beginning warranty liability",
               "accrual": "warranty accrual (2.0% of sales)",
               "claims": "actual claims paid",
               "ending": "ending warranty liability"}[k]
        answers.append({"label": "e: Year %d %s" % (y, lbl), "value": num(sched[y][k])})
answers.append({"label": "f: 12/31/Y2 warranty AJE - Dr Warranty Expense / Cr Estimated Warranty Liability", "value": num(accrual[2])})
answers.append({"label": "g: if the litigation loss were only reasonably possible at 12/31/Y1, what period-end reporting applies?",
                "value": "No period-end adjusting entry and no accrued liability - the $120,000 is not recorded; Ironwood instead discloses the loss contingency in the Year 1 notes, describing the nature of the lawsuit and the estimated loss (or range of $90,000-$280,000)."})

notes = ("Litigation: loss is probable and reasonably estimable, so ASC 450-20 requires accrual at 12/31/Y1; "
         "when a point estimate within the range is the better estimate it is accrued (%s), not the range minimum (%s). "
         "The 2/18/Y2 settlement is a RECOGNIZED (Type 1) subsequent event because the underlying condition (the Oct Y1 accident) "
         "existed at the balance-sheet date and the agreement occurred before the 3/10/Y2 issuance date, so the 12/31/Y1 liability is "
         "adjusted up by %s to the %s settlement amount; the $350,000 amount sought is not the measurement basis. "
         "Warranty: an assurance-type (two-year) warranty is not a separate performance obligation, so no revenue is deferred - "
         "expense is accrued at 2.0%% of each year's sales in the period-end AJE and actual cash claims reduce the liability, "
         "regardless of which year's sales the claims relate to. Year 1 begins with a zero warranty liability. "
         "All entries balance (Dr = Cr)." % (BETTER_ESTIMATE, RANGE_LOW, incremental_loss, remeasured_liab))

print(json.dumps({
  "id": "agent_360#00",
  "rounding_convention": "decimal.Decimal only (no floats); quantized to $0.01 with ROUND_HALF_UP, applied per period/line item (each year's 2.0% warranty accrual rounded before entering the roll-forward). Amounts here are exact whole dollars.",
  "answers": answers,
  "journal_entries": jes,
  "insufficient_info": False,
  "notes": notes,
}, indent=1))
