"""
Cedarline Robotics — Year 1 intangibles (LO 13-1), independent derivation #2.

ROUNDING CONVENTION
-------------------
All money is decimal.Decimal. Rates/monthly amounts are carried at FULL
precision internally; every amount that lands in a journal entry or a
schedule row is rounded to whole dollars with ROUND_HALF_UP, applied once
PER PERIOD (per-period rounding, not cumulative re-derivation).
The patent-defense amortization schedule is closed to ZERO exactly by
forcing the final period to the remaining unamortized balance (plug in the
last row), so the schedule ties to zero rather than drifting by rounding.

DERIVATION LOGIC (nothing about the answers is hard-coded; only the stem's
raw facts are inputs)
  * Finite-life IA  -> capitalize, amortize straight line over USEFUL life
                       (useful life, not legal life, when useful < legal),
                       residual zero, monthly proration from in-service date.
  * Indefinite-life IA (not goodwill) -> capitalize, NO amortization.
  * Goodwill = consideration paid - FV of identifiable net assets.
  * Internally generated R&D creating an invention -> EXPENSE as incurred.
  * External legal fees to SUCCESSFULLY DEFEND a purchased patent ->
    capitalize into the patent (defense preserves the right). Classification
    is unchanged (still finite-life); the added cost is amortized
    PROSPECTIVELY over the patent's REMAINING useful life from the date it is
    added (78 months remain of the 84-month useful life at July 1).
  * External legal fees to successfully REGISTER an intangible -> capitalize
    (a direct cost of securing the right), life follows the right (indefinite
    here), so no amortization.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

CENT = Decimal("1")           # whole dollars
def r(x: Decimal) -> Decimal:
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)

def num(d: Decimal):
    d = Decimal(d)
    i = int(d)
    return i if Decimal(i) == d else float(d)

# ----------------------------------------------------------------- raw facts
YEAR_MONTHS = Decimal(12)

FACTS = {
    1: dict(name="Copyright (printing rights)", amount=Decimal("72000"),
            useful_life_years=Decimal("12"), legal_life="much longer",
            indefinite=False, in_service_month=1, kind="asset"),
    2: dict(name="Franchise", amount=Decimal("110000"),
            useful_life_years=None, indefinite=True,
            in_service_month=1, kind="asset"),
    3: dict(name="Patent", amount=Decimal("56000"),
            useful_life_years=Decimal("7"), legal_life_years=Decimal("14"),
            indefinite=False, in_service_month=1, kind="asset"),
    4: dict(name="Trade name (external registration counsel fees)",
            amount=Decimal("8400"), useful_life_years=None, indefinite=True,
            in_service_month=4, kind="asset"),
    5: dict(name="Internal engineer salaries + lab supplies (R&D)",
            amount=Decimal("145000"), kind="expense"),
    6: dict(name="Business combination", consideration=Decimal("1250000"),
            fv_identifiable_net_assets=Decimal("980000"), kind="combination"),
    7: dict(name="Successful defense of purchased patent",
            amount=Decimal("11200"), added_month=7, kind="add_to_patent",
            target=3),
    8: dict(name="Two-year municipal license", amount=Decimal("24000"),
            useful_life_years=Decimal("2"), indefinite=False,
            in_service_month=1, kind="asset"),
}

# ----------------------------------------------------------------- part a
classification = {}
for i, f in FACTS.items():
    if f["kind"] == "expense":
        classification[i] = "expense (R&D expensed as incurred)"
    elif f["kind"] == "combination":
        classification[i] = "goodwill (residual)"
    elif f["kind"] == "add_to_patent":
        classification[i] = "finite-life IA (capitalized into the patent)"
    elif f["indefinite"]:
        classification[i] = "indefinite-life IA (not goodwill)"
    else:
        classification[i] = "finite-life IA"

goodwill = FACTS[6]["consideration"] - FACTS[6]["fv_identifiable_net_assets"]

# ----------------------------------------------------------------- part c engine
def months_in_year1(in_service_month: int) -> Decimal:
    """Months of service in Year 1 for an item placed in service on the 1st
    of `in_service_month` of a calendar Year 1."""
    return Decimal(12 - in_service_month + 1)

schedule = []          # one row per intangible component
patent_life_months = FACTS[3]["useful_life_years"] * YEAR_MONTHS

# original finite/indefinite assets
for i in (1, 2, 3, 4, 8):
    f = FACTS[i]
    cost = f["amount"]
    if f["indefinite"]:
        row = dict(item=i, asset=f["name"], cost=cost,
                   basis="indefinite life - not amortized",
                   life_months=None, months_amortized=Decimal(0),
                   annual_amort=Decimal(0), year1_amort=Decimal(0))
    else:
        life_m = f["useful_life_years"] * YEAR_MONTHS
        monthly = cost / life_m                      # full precision
        m = months_in_year1(f["in_service_month"])
        row = dict(item=i, asset=f["name"], cost=cost,
                   basis="straight line over useful life, residual 0",
                   life_months=life_m, months_amortized=m,
                   annual_amort=r(cost / f["useful_life_years"]),
                   year1_amort=r(monthly * m))
    schedule.append(row)

# item 7: defense cost layered onto the patent, prospective over remaining life
f7 = FACTS[7]
elapsed_before_add = Decimal(f7["added_month"] - 1)          # Jan..Jun = 6
remaining_months = patent_life_months - elapsed_before_add   # 78
monthly7 = f7["amount"] / remaining_months
months7_y1 = months_in_year1(f7["added_month"])              # Jul..Dec = 6
schedule.append(dict(item=7, asset="Patent - capitalized defense costs",
                     cost=f7["amount"],
                     basis="straight line over patent's REMAINING useful life "
                           f"({remaining_months} months) from July 1",
                     life_months=remaining_months,
                     months_amortized=months7_y1,
                     annual_amort=r(monthly7 * YEAR_MONTHS),
                     year1_amort=r(monthly7 * months7_y1)))

# closure proof for the defense layer: run it out, plug the last period
def run_out(cost: Decimal, total_months: Decimal, first_chunk: Decimal):
    """Amortize `cost` over total_months; first period = first_chunk months,
    then full 12-month years; last period forced to residual so it closes
    to exactly zero."""
    rows, bal, mleft = [], cost, total_months
    chunk = first_chunk
    monthly = cost / total_months
    while mleft > 0:
        take = min(chunk, mleft)
        amt = r(monthly * take)
        if take == mleft:                 # final period -> plug
            amt = bal
        if amt > bal:
            amt = bal
        bal -= amt
        rows.append(dict(months=take, amort=amt, end_balance=bal))
        mleft -= take
        chunk = YEAR_MONTHS
    return rows

defense_runout = run_out(f7["amount"], remaining_months, months7_y1)
assert defense_runout[-1]["end_balance"] == 0
assert sum((x["amort"] for x in defense_runout), Decimal(0)) == f7["amount"]

# patent original layer + copyright + license also close exactly
for i in (1, 3, 8):
    f = FACTS[i]
    ro = run_out(f["amount"], f["useful_life_years"] * YEAR_MONTHS,
                 months_in_year1(f["in_service_month"]))
    assert ro[-1]["end_balance"] == 0

total_year1_amort = sum((row["year1_amort"] for row in schedule), Decimal(0))

# per-account Year-1 amortization (patent = original layer + defense layer)
amort_by_account = {}
for row in schedule:
    acct = {1: "Copyright", 2: "Franchise", 3: "Patent", 4: "Trade Name",
            7: "Patent", 8: "License"}[row["item"]]
    amort_by_account[acct] = amort_by_account.get(acct, Decimal(0)) + row["year1_amort"]

# ----------------------------------------------------------------- part e
gross = {"Patent": FACTS[3]["amount"] + FACTS[7]["amount"],
         "Copyright": FACTS[1]["amount"],
         "Franchise": FACTS[2]["amount"],
         "Trade Name": FACTS[4]["amount"],
         "License": FACTS[8]["amount"],
         "Goodwill": goodwill}
carrying = {k: v - amort_by_account.get(k, Decimal(0)) for k, v in gross.items()}

total_intangibles = sum(carrying.values(), Decimal(0))

# ----------------------------------------------------------------- part b/d JEs
def je(part, date, lines, memo):
    d = sum((Decimal(l[1]) for l in lines if l[1]), Decimal(0))
    c = sum((Decimal(l[2]) for l in lines if l[2]), Decimal(0))
    assert d == c, (memo, d, c)
    return dict(part=part, date=date, memo=memo,
                lines=[dict(account=a, debit=num(dr or 0), credit=num(cr or 0))
                       for a, dr, cr in lines])

Z = Decimal(0)
jes = [
 je("b", "Year 1, Jan 1",
    [("Copyright", FACTS[1]["amount"], Z), ("Cash", Z, FACTS[1]["amount"])],
    "Item 1 - purchase copyright, finite 12-yr useful life"),
 je("b", "Year 1, Jan 1",
    [("Franchise", FACTS[2]["amount"], Z), ("Cash", Z, FACTS[2]["amount"])],
    "Item 2 - purchase franchise, indefinite life (no amortization)"),
 je("b", "Year 1, Jan 1",
    [("Patent", FACTS[3]["amount"], Z), ("Cash", Z, FACTS[3]["amount"])],
    "Item 3 - purchase patent, 7-yr useful life (< 14-yr legal life)"),
 je("b", "Year 1, Apr 1",
    [("Trade Name", FACTS[4]["amount"], Z), ("Cash", Z, FACTS[4]["amount"])],
    "Item 4 - external counsel fees to register trade name, indefinite life"),
 je("b", "Year 1, during the year",
    [("Research and Development Expense", FACTS[5]["amount"], Z),
     ("Cash / Salaries Payable / Supplies", Z, FACTS[5]["amount"])],
    "Item 5 - internal development costs expensed as incurred (not capitalized)"),
 je("b", "Year 1, acquisition date",
    [("Identifiable Net Assets Acquired (at fair value)",
      FACTS[6]["fv_identifiable_net_assets"], Z),
     ("Goodwill", goodwill, Z),
     ("Cash", Z, FACTS[6]["consideration"])],
    "Item 6 - business combination; goodwill = 1,250,000 - 980,000 residual"),
 je("b", "Year 1, Jul 1",
    [("Patent", FACTS[7]["amount"], Z), ("Cash", Z, FACTS[7]["amount"])],
    "Item 7 - successful defense of purchased patent capitalized to Patent"),
 je("b", "Year 1, Jan 1",
    [("License", FACTS[8]["amount"], Z), ("Cash", Z, FACTS[8]["amount"])],
    "Item 8 - two-year municipal license, finite 2-yr life"),
]

adj_lines = [("Amortization Expense", total_year1_amort, Z)]
for acct in ("Patent", "Copyright", "License"):
    a = amort_by_account.get(acct, Decimal(0))
    if a > 0:
        adj_lines.append((f"Accumulated Amortization - {acct}", Z, a))
jes.append(je("d", "Year 1, Dec 31", adj_lines,
              "Year-1 amortization: finite-life intangibles only "
              "(franchise, trade name, goodwill not amortized)"))

# ----------------------------------------------------------------- answers
A = []
def add(label, value):
    A.append({"label": label, "value": value})

cls_text = {
 1: "finite-life intangible asset (copyright, 12-year useful life; amortize over useful life, not the longer legal life)",
 2: "indefinite-life intangible asset, not goodwill (franchise renewable indefinitely; no amortization, impairment-test only)",
 3: "finite-life intangible asset (patent; amortize over 7-year useful life, shorter than the 14-year remaining legal life)",
 4: "indefinite-life intangible asset, not goodwill (external registration costs of an internally developed trade name are capitalizable; indefinite renewal = no amortization)",
 5: "expense (internal R&D salaries and lab supplies expensed as incurred; not capitalized even though a patent later results)",
 6: "goodwill (residual: consideration paid less fair value of identifiable net assets; indefinite, not amortized)",
 7: "finite-life intangible asset - capitalized into the Patent account (successful defense)",
 8: "finite-life intangible asset (2-year municipal license; amortize over its 2-year term)",
}
for i in range(1, 9):
    add(f"a: item {i} classification - {FACTS[i]['name']}", cls_text[i])
add("a: item 7 effect on patent classification",
    "No change in classification - the patent remains a finite-life intangible. "
    "The $11,200 successful-defense cost is capitalized (added to the patent's cost, "
    "gross carrying amount becomes $67,200) because the defense preserved the right; "
    "it does NOT extend the useful life.")
add("a: item 7 effect on subsequent measurement",
    "Amortized prospectively over the patent's REMAINING useful life from July 1, Year 1 - "
    f"{int(remaining_months)} months (6.5 years) - i.e. ${num(r(monthly7*YEAR_MONTHS))} per full year "
    f"and ${num(r(monthly7*months7_y1))} for the 6 months of Year 1. The original $56,000 layer "
    "continues at its existing $8,000 per year.")
add("a: goodwill computed (item 6)", num(goodwill))
add("a: item 5 amount expensed as R&D", num(FACTS[5]["amount"]))

# part c schedule rows
for row in schedule:
    tag = f"c: schedule row item {row['item']} - {row['asset']}"
    add(tag + " | cost/gross carrying amount", num(row["cost"]))
    add(tag + " | amortization basis", row["basis"])
    add(tag + " | useful life (months)",
        None if row["life_months"] is None else num(row["life_months"]))
    add(tag + " | months amortized in Year 1", num(row["months_amortized"]))
    add(tag + " | full-year amortization", num(row["annual_amort"]))
    add(tag + " | Year-1 amortization expense", num(row["year1_amort"]))
    add(tag + " | Dec 31 Yr 1 accumulated amortization", num(row["year1_amort"]))
    add(tag + " | Dec 31 Yr 1 carrying amount (this layer)",
        num(row["cost"] - row["year1_amort"]))

add("c: patent total Year-1 amortization (original $56,000 layer + defense layer)",
    num(amort_by_account["Patent"]))
add("c: copyright Year-1 amortization", num(amort_by_account["Copyright"]))
add("c: license Year-1 amortization", num(amort_by_account["License"]))
add("c: franchise Year-1 amortization (indefinite life)", num(amort_by_account["Franchise"]))
add("c: trade name Year-1 amortization (indefinite life)", num(amort_by_account["Trade Name"]))
add("c: goodwill Year-1 amortization (never amortized)", 0)
add("c: TOTAL Year-1 amortization expense", num(total_year1_amort))
add("c: exact unrounded total Year-1 amortization (before whole-dollar rounding)",
    str((FACTS[1]['amount']/FACTS[1]['useful_life_years']
         + FACTS[3]['amount']/FACTS[3]['useful_life_years']
         + FACTS[8]['amount']/FACTS[8]['useful_life_years']
         + monthly7*months7_y1).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))

# defense-layer run-out (proof the schedule closes to zero)
lbl = "c: defense-cost layer run-out period {} ({} months) amortization / ending balance"
for n, x in enumerate(defense_runout, start=1):
    add(lbl.format(n, num(x["months"])),
        f'{num(x["amort"])} / {num(x["end_balance"])}')

# part d
add("d: Dec 31 Yr 1 debit to Amortization Expense", num(total_year1_amort))
add("d: Dec 31 Yr 1 credit Accumulated Amortization - Patent", num(amort_by_account["Patent"]))
add("d: Dec 31 Yr 1 credit Accumulated Amortization - Copyright", num(amort_by_account["Copyright"]))
add("d: Dec 31 Yr 1 credit Accumulated Amortization - License", num(amort_by_account["License"]))

# part e
add("e: Patent gross carrying amount incl. defense costs", num(gross["Patent"]))
add("e: Patent accumulated amortization Dec 31 Yr 1", num(amort_by_account["Patent"]))
add("e: Patent carrying amount Dec 31 Yr 1 (incl. defense costs)", num(carrying["Patent"]))
add("e: Copyright carrying amount Dec 31 Yr 1", num(carrying["Copyright"]))
add("e: Franchise carrying amount Dec 31 Yr 1", num(carrying["Franchise"]))
add("e: Trade name carrying amount Dec 31 Yr 1", num(carrying["Trade Name"]))
add("e: License carrying amount Dec 31 Yr 1", num(carrying["License"]))
add("e: Goodwill carrying amount Dec 31 Yr 1", num(carrying["Goodwill"]))
add("e: total intangible assets carrying amount Dec 31 Yr 1 (check total)",
    num(total_intangibles))

out = {
 "id": "agent_086#01",
 "rounding_convention": ("decimal.Decimal throughout; rates/monthly amounts at full "
   "precision, every JE and schedule amount rounded to whole dollars with ROUND_HALF_UP "
   "applied once per period. Schedules closed to EXACTLY zero by plugging the final "
   "period with the remaining unamortized balance (the $11,200 defense layer runs "
   "$862 + 6 x $1,723 + final plug $1,722 = $11,200)."),
 "answers": A,
 "journal_entries": jes,
 "insufficient_info": False,
 "notes": ("Classification: finite-life = copyright ($72,000/12yr), patent ($56,000/7yr "
   "useful < 14yr legal), capitalized patent-defense costs ($11,200), 2-year license "
   "($24,000/2yr); indefinite-life (not goodwill) = franchise $110,000 and registered "
   "trade name $8,400; goodwill = $1,250,000 - $980,000 = $270,000; expense = $145,000 "
   "internal R&D. Item 7: successful defense is capitalized to the patent, classification "
   "unchanged (still finite-life), amortized prospectively over the 78 months of useful "
   "life remaining at July 1 -> $11,200 x 6/78 = $861.54 -> $862 in Year 1. Year-1 "
   "amortization = 6,000 copyright + 8,000 patent + 862 defense + 12,000 license = "
   "$26,862; franchise, trade name and goodwill are not amortized (impairment tested). "
   "Dec 31 Yr 1 carrying amounts: patent $58,338 (67,200 - 8,862), copyright $66,000, "
   "franchise $110,000, trade name $8,400, license $12,000, goodwill $270,000; total "
   "$524,738. If an instructor instead amortizes the defense layer over a full 7 years "
   "(11,200/7 x 1/2 = $800) Year-1 amortization would be $26,800 and the patent $58,400 - "
   "that convention does not fully amortize the layer by the end of the patent's useful "
   "life, so the remaining-life (78-month) basis is used here.")
}
print(json.dumps(out, indent=1))
