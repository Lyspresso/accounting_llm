"""Cascade Outfitters -- 0% stated / 10% market 3-year note receivable.

Rounding convention: all money is decimal.Decimal, quantized to cents with
ROUND_HALF_UP at each period (each interest-revenue / discount-amortization
figure is rounded when computed, and the rounded figure rolls into the next
period's carrying amount). The FINAL full-term period is a PLUG so that the
carrying amount closes exactly to face ($15,000) and total interest revenue
equals the initial discount exactly. Interim (Dec-31) allocations split each
12-month amortization period 6/12 with ROUND_HALF_UP; the second half of each
period is the plug (period amount less the first half) so the halves sum
exactly to the period total. Dr = Cr on every entry.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def q(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def f(x): return float(q(x))

# ---- Inputs given in the scenario ------------------------------------------
FACE = Decimal("15000")            # face / maturity value, due Jun 30 Yr 4
FV   = Decimal("11269")            # fair value of inventory = PV of the note
i    = Decimal("0.10")             # market (effective) rate
n    = 3                           # annual periods
STATED = Decimal("0")              # 0% stated rate -> no cash interest

pv_math = FACE / ((Decimal(1) + i) ** n)          # 11,269.7221 (unrounded)
discount0 = FACE - FV                              # initial discount

# ---- (b) effective-interest amortization schedule --------------------------
rows = []
ca = FV
for k in range(1, n + 1):
    cash = q(FACE * STATED)
    if k < n:
        interest = q(ca * i)
    else:
        interest = FACE - ca                       # plug: closes to face
    amort = interest - cash
    ca = ca + amort
    rows.append({"period": k, "cash": cash, "interest": interest,
                 "amort": amort, "ca_end": ca})
tot_cash = sum(r["cash"] for r in rows)
tot_int  = sum(r["interest"] for r in rows)
tot_amort = sum(r["amort"] for r in rows)

# ---- (d) allocate each 12-month period 6/12 into Dec-31 reporting periods ---
halves = []
for r in rows:
    h1 = q(r["interest"] / 2)
    h2 = r["interest"] - h1                        # plug half
    halves.append((h1, h2))

# Dec 31 Yr1 = 2nd half of calendar Yr1 = first half of period 1
d1 = halves[0][0]
# Dec 31 Yr2 = 2nd half of period 1 + 1st half of period 2
d2 = halves[0][1] + halves[1][0]
# Dec 31 Yr3 = 2nd half of period 2 + 1st half of period 3
d3 = halves[1][1] + halves[2][0]
# Jun 30 Yr4 = 2nd half of period 3
d4 = halves[2][1]
cal_total = d1 + d2 + d3 + d4

ca_d1 = FV + d1
ca_d2 = ca_d1 + d2
ca_d3 = ca_d2 + d3
ca_d4 = ca_d3 + d4
unamort_d1 = FACE - ca_d1

answers = [
 {"label": "a: PV of note / fair value of inventory recorded (sales revenue), Jun 30 Yr 1", "value": f(FV)},
 {"label": "a: Face (maturity) value of note receivable", "value": f(FACE)},
 {"label": "a: Initial Discount on Note Receivable (face less PV)", "value": f(discount0)},
 {"label": "a: Cash interest received each period (0% stated rate)", "value": f(Decimal(0))},

 {"label": "b: Period 1 (Jun 30 Yr1-Jun 30 Yr2) carrying amount, beginning", "value": f(FV)},
 {"label": "b: Period 1 cash interest", "value": f(rows[0]["cash"])},
 {"label": "b: Period 1 interest revenue (10% x carrying amount)", "value": f(rows[0]["interest"])},
 {"label": "b: Period 1 discount amortization", "value": f(rows[0]["amort"])},
 {"label": "b: Period 1 carrying amount, ending (Jun 30 Yr2)", "value": f(rows[0]["ca_end"])},
 {"label": "b: Period 2 cash interest", "value": f(rows[1]["cash"])},
 {"label": "b: Period 2 interest revenue", "value": f(rows[1]["interest"])},
 {"label": "b: Period 2 discount amortization", "value": f(rows[1]["amort"])},
 {"label": "b: Period 2 carrying amount, ending (Jun 30 Yr3)", "value": f(rows[1]["ca_end"])},
 {"label": "b: Period 3 cash interest", "value": f(rows[2]["cash"])},
 {"label": "b: Period 3 interest revenue (plug to close to face)", "value": f(rows[2]["interest"])},
 {"label": "b: Period 3 discount amortization", "value": f(rows[2]["amort"])},
 {"label": "b: Period 3 carrying amount, ending (Jun 30 Yr4) = face", "value": f(rows[2]["ca_end"])},
 {"label": "b: Total cash interest over term", "value": f(tot_cash)},
 {"label": "b: Total interest revenue over term", "value": f(tot_int)},
 {"label": "b: Total discount amortized over term (= initial discount)", "value": f(tot_amort)},

 {"label": "c: Interest revenue accrued Jun 30 Yr2", "value": f(rows[0]["interest"])},
 {"label": "c: Interest revenue accrued Jun 30 Yr3", "value": f(rows[1]["interest"])},
 {"label": "c: Interest revenue accrued Jun 30 Yr4", "value": f(rows[2]["interest"])},
 {"label": "c: Cash collected at maturity Jun 30 Yr4", "value": f(FACE)},

 {"label": "d: Interest revenue accrued Dec 31 Yr1 (6 months of period 1)", "value": f(d1)},
 {"label": "d: Carrying amount Dec 31 Yr1", "value": f(ca_d1)},
 {"label": "d: Interest revenue accrued Dec 31 Yr2 (2nd half period 1 + 1st half period 2)", "value": f(d2)},
 {"label": "d: Carrying amount Dec 31 Yr2", "value": f(ca_d2)},
 {"label": "d: Interest revenue accrued Dec 31 Yr3 (2nd half period 2 + 1st half period 3)", "value": f(d3)},
 {"label": "d: Carrying amount Dec 31 Yr3", "value": f(ca_d3)},
 {"label": "d: Interest revenue accrued Jun 30 Yr4 (2nd half period 3)", "value": f(d4)},
 {"label": "d: Carrying amount Jun 30 Yr4 before collection = face", "value": f(ca_d4)},
 {"label": "d: Total interest revenue across reporting periods", "value": f(cal_total)},
 {"label": "d: Verification - total interest revenue equals original discount", "value": bool(cal_total == discount0)},

 {"label": "e: Note Receivable (face) presented at Dec 31 Yr1", "value": f(FACE)},
 {"label": "e: Less unamortized Discount on Note Receivable at Dec 31 Yr1", "value": f(unamort_d1)},
 {"label": "e: Net carrying amount presented at Dec 31 Yr1 (noncurrent asset)", "value": f(ca_d1)},
 {"label": "e: Amount classified as current asset at Dec 31 Yr1", "value": 0.0},
]

def je(part, desc, lines):
    d = sum(Decimal(str(l[1])) for l in lines)
    c = sum(Decimal(str(l[2])) for l in lines)
    assert q(d) == q(c), (part, desc, d, c)
    return {"part": part, "description": desc,
            "lines": [{"account": a, "debit": f(dr), "credit": f(cr)} for a, dr, cr in lines]}

jes = [
 je("a", "Jun 30 Yr1 - receipt of noninterest-bearing note for inventory", [
    ("Note Receivable", FACE, 0), ("Discount on Note Receivable", 0, discount0),
    ("Sales Revenue", 0, FV)]),
 je("c", "Jun 30 Yr2 - interest accrual (June 30 fiscal year-end)", [
    ("Discount on Note Receivable", rows[0]["interest"], 0),
    ("Interest Revenue", 0, rows[0]["interest"])]),
 je("c", "Jun 30 Yr3 - interest accrual (June 30 fiscal year-end)", [
    ("Discount on Note Receivable", rows[1]["interest"], 0),
    ("Interest Revenue", 0, rows[1]["interest"])]),
 je("c", "Jun 30 Yr4 - interest accrual (June 30 fiscal year-end)", [
    ("Discount on Note Receivable", rows[2]["interest"], 0),
    ("Interest Revenue", 0, rows[2]["interest"])]),
 je("c", "Jun 30 Yr4 - collection of face at maturity", [
    ("Cash", FACE, 0), ("Note Receivable", 0, FACE)]),
 je("d", "Dec 31 Yr1 - interest accrual (December 31 year-end)", [
    ("Discount on Note Receivable", d1, 0), ("Interest Revenue", 0, d1)]),
 je("d", "Dec 31 Yr2 - interest accrual", [
    ("Discount on Note Receivable", d2, 0), ("Interest Revenue", 0, d2)]),
 je("d", "Dec 31 Yr3 - interest accrual", [
    ("Discount on Note Receivable", d3, 0), ("Interest Revenue", 0, d3)]),
 je("d", "Jun 30 Yr4 - final interest accrual (Jan 1 - Jun 30 Yr4)", [
    ("Discount on Note Receivable", d4, 0), ("Interest Revenue", 0, d4)]),
 je("d", "Jun 30 Yr4 - collection of face at maturity", [
    ("Cash", FACE, 0), ("Note Receivable", 0, FACE)]),
]

notes = ("Exact math PV(10%,3,0,15000) = {} ; the scenario states the inventory fair value / "
         "note PV as $11,269, so 11,269 is used as the initial carrying amount and the initial "
         "discount is 15,000 - 11,269 = 3,731. Period 3 interest revenue is the plug "
         "(15,000 - 13,635.49) so the schedule closes exactly to face. No cash interest is ever "
         "received (0% stated rate), so all interest revenue is discount amortization. "
         "(e) At Dec 31 Yr1 the note matures Jun 30 Yr4, more than one year (and beyond one "
         "operating cycle) after the balance sheet date, so it is reported as a NONCURRENT asset: "
         "Note receivable $15,000.00 less unamortized discount $3,167.55 = $11,832.45 net; the "
         "discount is a contra-asset shown as a direct deduction, never as a liability, and no "
         "portion is current."
        ).format(pv_math.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))

print(json.dumps({
  "id": "agent_043#00",
  "rounding_convention": ("decimal.Decimal throughout; ROUND_HALF_UP to the cent each period; "
                         "rounded period figures roll forward into the next carrying amount; "
                         "final period interest is a plug so carrying amount closes to face and "
                         "total interest revenue equals the initial discount exactly; interim "
                         "6/12 half-period splits use ROUND_HALF_UP with the second half plugged"),
  "answers": answers,
  "journal_entries": jes,
  "insufficient_info": False,
  "notes": notes}, indent=1))
