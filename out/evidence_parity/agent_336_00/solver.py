"""Meridian Fabrication Co. -- LO 11-9 full lifecycle solver.

Rounding convention: all money is decimal.Decimal. Every period's
depreciation charge is computed independently and rounded to the nearest
cent using ROUND_HALF_UP at the end of each period (per-period rounding,
not cumulative-truncation). Partial years use nearest-month convention
(months in service / 12 of the annual straight-line charge).
Nothing is hard-coded; every figure is derived from the fact pattern.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

C = Decimal("0.01")
def r(x): return Decimal(x).quantize(C, rounding=ROUND_HALF_UP)
def f(x): return float(r(x))

# ---------- facts ----------
press_cost      = Decimal("90000")
press_residual  = Decimal("9000")
press_life      = Decimal("6")
press_fv        = Decimal("38000")
cash_paid       = Decimal("25000")
mill_residual   = Decimal("3000")
mill_life       = Decimal("5")
sale_price      = Decimal("28000")

# ---------- (b) press depreciation schedule ----------
press_base   = press_cost - press_residual
press_annual = press_base / press_life
press_month  = press_annual / Decimal("12")

def charge(months):
    return r(press_annual * Decimal(months) / Decimal("12"))

press_rows = [("20X1 (full year)", 12), ("20X2 (full year)", 12),
              ("20X3 (full year)", 12), ("20X4 Jan 1 - Sep 30 (9 months)", 9)]
press_sched, cum = [], Decimal("0")
for lbl, m in press_rows:
    amt = charge(m)
    cum += amt
    press_sched.append((lbl, amt, cum, press_cost - cum))

press_ad_at_exch = cum
press_dep_20X4   = press_sched[-1][1]
press_bv         = press_cost - press_ad_at_exch

# ---------- (d) exchange (commercial substance; FV of asset given up) ----------
gain_loss_exch = r(press_fv - press_bv)          # negative => loss
loss_exch      = -gain_loss_exch
mill_cost      = r(press_fv + cash_paid)

exch_dr = mill_cost + press_ad_at_exch + loss_exch
exch_cr = press_cost + cash_paid

# ---------- (e) mill depreciation schedule ----------
mill_base   = mill_cost - mill_residual
mill_annual = mill_base / mill_life

def mcharge(months):
    return r(mill_annual * Decimal(months) / Decimal("12"))

mill_rows = [("20X4 Oct 1 - Dec 31 (3 months)", 3), ("20X5 (full year)", 12),
             ("20X6 (full year)", 12), ("20X7 Jan 1 - Jun 30 (6 months)", 6)]
mill_sched, mcum = [], Decimal("0")
for lbl, m in mill_rows:
    amt = mcharge(m)
    mcum += amt
    mill_sched.append((lbl, amt, mcum, mill_cost - mcum))

mill_ad_total = mcum
mill_dep_X4   = mill_sched[0][1]
mill_dep_X7   = mill_sched[-1][1]
mill_bv_sale  = mill_cost - mill_ad_total

# ---------- (f) disposal ----------
gain_loss_disp = r(sale_price - mill_bv_sale)     # negative => loss
loss_disp      = -gain_loss_disp
disp_dr = sale_price + mill_ad_total + loss_disp
disp_cr = mill_cost

# ---------- output ----------
A = []
def add(lbl, val): A.append({"label": lbl, "value": f(val)})

add("a: Equipment - Hydraulic Press debited (cash cost) at 1/1/20X1", press_cost)
add("b: Press depreciable base (cost 90,000 - residual 9,000)", press_base)
add("b: Press annual straight-line depreciation", press_annual)
add("b: Press monthly straight-line depreciation", press_month)
for lbl, amt, ccum, cbv in press_sched:
    add(f"b: Press depreciation expense - {lbl}", amt)
    add(f"b: Press cumulative accumulated depreciation after {lbl}", ccum)
    add(f"b: Press carrying (book) value after {lbl}", cbv)
add("c: Depreciation expense recorded 1/1/20X4 - 9/30/20X4 (9 months) on press", press_dep_20X4)
add("c: Accumulated depreciation - press balance immediately after the 9/30/20X4 adjusting entry", press_ad_at_exch)
add("d: Book value of press at 9/30/20X4 (90,000 - 50,625)", press_bv)
add("d: Fair value of press given up", press_fv)
add("d: Loss on exchange (FV 38,000 - BV 39,375)", loss_exch)
add("d: Cost assigned to CNC mill (FV of press given up 38,000 + cash paid 25,000)", mill_cost)
add("d: Exchange JE total debits", exch_dr)
add("d: Exchange JE total credits", exch_cr)
add("e: Mill depreciable base (cost 63,000 - residual 3,000)", mill_base)
add("e: Mill annual straight-line depreciation", mill_annual)
for lbl, amt, ccum, cbv in mill_sched:
    add(f"e: Mill depreciation expense - {lbl}", amt)
    add(f"e: Mill cumulative accumulated depreciation after {lbl}", ccum)
    add(f"e: Mill carrying (book) value after {lbl}", cbv)
add("e: 12/31/20X4 depreciation adjusting entry amount (3 months)", mill_dep_X4)
add("e: 6/30/20X7 depreciation adjusting entry amount (6 months)", mill_dep_X7)
add("f: Book value of mill at 6/30/20X7 (63,000 - 33,000)", mill_bv_sale)
add("f: Loss on sale of mill (proceeds 28,000 - BV 30,000)", loss_disp)
add("f: Disposal JE total debits", disp_dr)
add("f: Disposal JE total credits", disp_cr)

def L(acct, dr=Decimal("0"), cr=Decimal("0")):
    return {"account": acct, "debit": f(dr), "credit": f(cr)}

JE = [
 {"part": "a", "lines": [
    L("Equipment - Hydraulic Press", dr=press_cost),
    L("Cash", cr=press_cost)]},
 {"part": "c", "lines": [
    L("Depreciation Expense - Hydraulic Press", dr=press_dep_20X4),
    L("Accumulated Depreciation - Hydraulic Press", cr=press_dep_20X4)]},
 {"part": "d", "lines": [
    L("Equipment - CNC Mill", dr=mill_cost),
    L("Accumulated Depreciation - Hydraulic Press", dr=press_ad_at_exch),
    L("Loss on Exchange of Equipment", dr=loss_exch),
    L("Equipment - Hydraulic Press", cr=press_cost),
    L("Cash", cr=cash_paid)]},
 {"part": "e", "lines": [
    L("Depreciation Expense - CNC Mill (12/31/20X4, 3 months)", dr=mill_dep_X4),
    L("Accumulated Depreciation - CNC Mill", cr=mill_dep_X4)]},
 {"part": "e", "lines": [
    L("Depreciation Expense - CNC Mill (6/30/20X7, 6 months)", dr=mill_dep_X7),
    L("Accumulated Depreciation - CNC Mill", cr=mill_dep_X7)]},
 {"part": "f", "lines": [
    L("Cash", dr=sale_price),
    L("Accumulated Depreciation - CNC Mill", dr=mill_ad_total),
    L("Loss on Sale of Equipment", dr=loss_disp),
    L("Equipment - CNC Mill", cr=mill_cost)]},
]
for e in JE:
    assert r(sum(Decimal(str(x["debit"])) for x in e["lines"])) == \
           r(sum(Decimal(str(x["credit"])) for x in e["lines"])), e["part"]

print(json.dumps({
 "id": "agent_336#00",
 "rounding_convention": "decimal.Decimal throughout; each period's depreciation rounded to the nearest cent with ROUND_HALF_UP at the end of that period (per-period rounding); partial years by nearest-month convention (months/12 of the annual straight-line charge).",
 "answers": A,
 "journal_entries": JE,
 "insufficient_info": False,
 "notes": "Exchange has commercial substance and the FV of the press given up is the more clearly determinable value, so the mill is recorded at FV of press given up + cash paid (38,000 + 25,000 = 63,000) and the full 1,375 loss is recognized immediately (losses are recognized in full regardless of commercial substance)."
}, indent=1))
