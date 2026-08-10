"""Independent (second) cold derivation of agent_092#00 -- ASC 730 R&D cost cycle.

Money handling: decimal.Decimal exclusively; no floats anywhere.
Rounding convention: ROUND_HALF_UP to whole dollars per period (each period's
straight-line charge is rounded independently), with the final period forced so
the depreciation schedule closes EXACTLY to the $0 residual and the patent
amortization ties to the $12,000 capitalized cost. Here every quotient divides
evenly ($480,000/6 = $80,000; $12,000/10 = $1,200/yr, half-year $600), so no
rounding residue actually arises.

Derivation logic (bottom-up from the stem, nothing hard-coded):
  Each of the 10 facts is tagged with (a) whether ASC 730 treats it as R&D and
  (b) whether it is expensed immediately or capitalized. The tagging rules used:
    * Materials/equipment/facilities acquired for R&D with NO alternative
      future use -> expense in full when incurred (items 1, 3).
    * Assets with SIGNIFICANT alternative future use -> capitalize and
      depreciate; the depreciation is an R&D cost in periods of R&D use (item 2).
    * Personnel costs, contract research paid to others, reasonable indirect-
      cost allocations, and design/construction/testing of preproduction
      prototypes -> R&D expense (items 4, 5, 6, 9).
    * G&A not clearly related to R&D -> not R&D (item 7).
    * Routine troubleshooting / breakdown repair on an existing commercial
      production line -> not R&D (item 8).
    * Legal fees to register a patent on a successfully developed process ->
      capitalized intangible, amortized over the shorter of legal/useful life;
      neither the fee nor its amortization is R&D (item 10).
  Totals, the schedule, and the disposal gain are computed from those tags.
"""

from decimal import Decimal, ROUND_HALF_UP
import json

C = Decimal("0.01")
D = lambda s: Decimal(s)


def money(x):
    """Round to whole dollars, ROUND_HALF_UP."""
    return x.quantize(Decimal("1"), rounding=ROUND_HALF_UP)


def num(x):
    x = x.quantize(C)
    return int(x) if x == x.to_integral_value() else float(x)


# ---------------------------------------------------------------- fact pattern
# kind: 'rd_expense' | 'capitalize' | 'other_expense'
FACTS = [
    dict(n=1,  amt=D("240000"),  kind="rd_expense",
         desc="Materials consumed on current R&D, no alternative future use"),
    dict(n=2,  amt=D("480000"),  kind="capitalize", tag="equip",
         desc="Lab equipment, significant alternative future uses"),
    dict(n=3,  amt=D("96000"),   kind="rd_expense",
         desc="Specialized testing apparatus, single project, no alt. future use"),
    dict(n=4,  amt=D("1150000"), kind="rd_expense",
         desc="Salaries and wages of R&D scientists/technicians"),
    dict(n=5,  amt=D("85000"),   kind="rd_expense",
         desc="Contract research performed by outside university lab"),
    dict(n=6,  amt=D("72000"),   kind="rd_expense",
         desc="Reasonable allocation of indirect costs clearly related to R&D"),
    dict(n=7,  amt=D("310000"),  kind="other_expense", tag="ga",
         desc="Corporate HQ G&A not clearly related to R&D"),
    dict(n=8,  amt=D("41000"),   kind="other_expense", tag="repair",
         desc="Troubleshooting/repair of existing commercial production line"),
    dict(n=9,  amt=D("55000"),   kind="rd_expense",
         desc="Design and construction of preproduction prototypes"),
    dict(n=10, amt=D("12000"),   kind="capitalize", tag="patent",
         desc="Legal fees to register patent on successfully developed process"),
]

pick = lambda t: next(f for f in FACTS if f.get("tag") == t)

rd_cash_items = [f for f in FACTS if f["kind"] == "rd_expense"]
rd_cash_total = sum((f["amt"] for f in rd_cash_items), Decimal("0"))

equip = pick("equip")
patent = pick("patent")
ga = pick("ga")
repair = pick("repair")

# ------------------------------------------------- equipment depreciation (SL)
EQ_COST = equip["amt"]
EQ_RESID = D("0")
EQ_LIFE = 6                      # years, straight line, in service Jan 1 Yr 1
annual_dep_raw = (EQ_COST - EQ_RESID) / Decimal(EQ_LIFE)
schedule = []
bv = EQ_COST
accum = Decimal("0")
for yr in range(1, EQ_LIFE + 1):
    if yr < EQ_LIFE:
        dep = money(annual_dep_raw)
    else:                        # force exact close to residual
        dep = bv - EQ_RESID
    begin = bv
    bv = begin - dep
    accum += dep
    schedule.append(dict(year=yr, begin=begin, dep=dep, accum=accum, end=bv))
assert bv == EQ_RESID, "schedule must close to residual"
yr1_dep = schedule[0]["dep"]

# ------------------------------------------------------- patent amortization
PAT_COST = patent["amt"]
PAT_LEGAL_LIFE = 20
PAT_USEFUL_LIFE = 10             # amortize over shorter of legal/useful
PAT_AMORT_LIFE = min(PAT_LEGAL_LIFE, PAT_USEFUL_LIFE)
pat_annual = money(PAT_COST / Decimal(PAT_AMORT_LIFE))
MONTHS_IN_SERVICE_YR1 = 6        # July 1 -> Dec 31
pat_yr1 = money(PAT_COST / Decimal(PAT_AMORT_LIFE)
                * Decimal(MONTHS_IN_SERVICE_YR1) / Decimal(12))
pat_bv_end_yr1 = PAT_COST - pat_yr1

# ----------------------------------------------- part d: disclosed R&D total
rd_disclosed = rd_cash_total + yr1_dep
excluded = [
    ("Corporate HQ G&A not clearly related to R&D (item 7)", ga["amt"]),
    ("Routine troubleshooting/repair of existing production line (item 8)", repair["amt"]),
    ("Patent registration legal fees -- capitalized intangible (item 10)", PAT_COST),
    ("Year 1 patent amortization -- not an R&D cost", pat_yr1),
    ("Capitalized cost of multi-use lab equipment (only its depreciation is R&D)", EQ_COST),
]

# --------------------------------------------------- part e: Jan 1 Yr 4 sale
YEARS_HELD = 3
accum_at_sale = sum((r["dep"] for r in schedule[:YEARS_HELD]), Decimal("0"))
bv_at_sale = EQ_COST - accum_at_sale
PROCEEDS = D("250000")
gain = PROCEEDS - bv_at_sale     # positive => gain, negative => loss

# ------------------------------------------------------------- journal entries
def L(acct, dr=None, cr=None):
    return dict(account=acct,
                debit=num(dr) if dr is not None else 0,
                credit=num(cr) if cr is not None else 0)

jes = []
jes.append(dict(part="a", ref="a-1 (items 1, 3, 4, 5, 6, 9) -- expensed immediately as R&D",
    lines=[
        L("Research and Development Expense -- materials consumed (item 1)", dr=FACTS[0]["amt"]),
        L("Research and Development Expense -- special-purpose apparatus, no alt. use (item 3)", dr=FACTS[2]["amt"]),
        L("Research and Development Expense -- salaries and wages (item 4)", dr=FACTS[3]["amt"]),
        L("Research and Development Expense -- contract research, outside lab (item 5)", dr=FACTS[4]["amt"]),
        L("Research and Development Expense -- allocated indirect R&D costs (item 6)", dr=FACTS[5]["amt"]),
        L("Research and Development Expense -- preproduction prototypes (item 9)", dr=FACTS[8]["amt"]),
        L("Cash", cr=rd_cash_total),
    ]))
jes.append(dict(part="a", ref="a-2 (item 2) -- CAPITALIZED: significant alternative future use",
    lines=[L("Laboratory Equipment (multi-use)", dr=EQ_COST), L("Cash", cr=EQ_COST)]))
jes.append(dict(part="a", ref="a-3 (item 7) -- not R&D",
    lines=[L("General and Administrative Expense", dr=ga["amt"]), L("Cash", cr=ga["amt"])]))
jes.append(dict(part="a", ref="a-4 (item 8) -- not R&D (routine production troubleshooting)",
    lines=[L("Repairs and Maintenance Expense (manufacturing overhead)", dr=repair["amt"]),
           L("Cash", cr=repair["amt"])]))
jes.append(dict(part="a", ref="a-5 (item 10) -- CAPITALIZED intangible, not R&D",
    lines=[L("Patent", dr=PAT_COST), L("Cash", cr=PAT_COST)]))

jes.append(dict(part="b", ref="b-1 Dec 31 Yr 1 -- depreciation of multi-use lab equipment (an R&D cost)",
    lines=[L("Research and Development Expense (depreciation -- lab equipment)", dr=yr1_dep),
           L("Accumulated Depreciation -- Laboratory Equipment", cr=yr1_dep)]))
jes.append(dict(part="b", ref="b-2 Dec 31 Yr 1 -- patent amortization, 6 months (Jul 1 - Dec 31)",
    lines=[L("Amortization Expense -- Patent", dr=pat_yr1),
           L("Patent (or Accumulated Amortization -- Patent)", cr=pat_yr1)]))

disposal = [L("Cash", dr=PROCEEDS),
            L("Accumulated Depreciation -- Laboratory Equipment", dr=accum_at_sale),
            L("Laboratory Equipment (multi-use)", cr=EQ_COST)]
if gain > 0:
    disposal.append(L("Gain on Sale of Equipment", cr=gain))
elif gain < 0:
    disposal.insert(2, L("Loss on Sale of Equipment", dr=-gain))
jes.append(dict(part="e", ref="e Jan 1 Yr 4 -- sale of multi-use laboratory equipment", lines=disposal))

for je in jes:
    dr = sum(Decimal(str(l["debit"])) for l in je["lines"])
    cr = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert dr == cr, (je["ref"], dr, cr)

# -------------------------------------------------------------------- answers
A = []
add = lambda lbl, val: A.append(dict(label=lbl, value=num(val) if isinstance(val, Decimal) else val))

for f in FACTS:
    treat = {"rd_expense": "EXPENSE now as R&D",
             "capitalize": "CAPITALIZE",
             "other_expense": "EXPENSE, NOT R&D"}[f["kind"]]
    add(f"a: item {f['n']} ({f['desc']}) -- {treat}", f["amt"])
add("a: total charged to R&D Expense at initial recognition (items 1,3,4,5,6,9)", rd_cash_total)
add("a: total capitalized in Year 1 (item 2 equipment + item 10 patent)", EQ_COST + PAT_COST)
add("a: total cash paid, items 1-10", sum((f["amt"] for f in FACTS), Decimal("0")))
add("a: Year 1 non-R&D expense recognized (items 7 + 8)", ga["amt"] + repair["amt"])

add("b1: Dec 31 Yr 1 depreciation of multi-use lab equipment (debited to R&D Expense)", yr1_dep)
add("b2: patent amortization life used (shorter of 20-yr legal, 10-yr useful), years", PAT_AMORT_LIFE)
add("b2: patent full-year amortization", pat_annual)
add("b2: Dec 31 Yr 1 patent amortization (6 months)", pat_yr1)
add("b2: patent carrying amount Dec 31 Yr 1", pat_bv_end_yr1)

add("c: annual straight-line depreciation, lab equipment ($480,000 - $0) / 6", annual_dep_raw)
for r in schedule:
    add(f"c: Year {r['year']} beginning book value", r["begin"])
    add(f"c: Year {r['year']} depreciation expense (classified as R&D)", r["dep"])
    add(f"c: Year {r['year']} accumulated depreciation", r["accum"])
    add(f"c: Year {r['year']} ending book value", r["end"])
add("c: total depreciation Years 1-6 (ties to cost, closes to $0 residual)",
    sum((r["dep"] for r in schedule), Decimal("0")))

add("d: TOTAL Year 1 R&D expense disclosed", rd_disclosed)
add("d: ... of which cash R&D costs (items 1,3,4,5,6,9)", rd_cash_total)
add("d: ... of which depreciation on multi-use R&D equipment", yr1_dep)
for lbl, amt in excluded:
    add(f"d: EXCLUDED from R&D -- {lbl}", amt)

add("e: accumulated depreciation at Jan 1 Yr 4 (3 years x $80,000)", accum_at_sale)
add("e: book value at Jan 1 Yr 4", bv_at_sale)
add("e: cash proceeds", PROCEEDS)
add("e: gain on sale (proceeds - book value)", gain)

add("f: ASC 730 disclosure -- total R&D costs charged to expense in Year 1 must be "
    "disclosed on the face of the income statement or in the notes, for each period "
    "an income statement is presented (single aggregate figure)", rd_disclosed)

notes = (
    "Item 3 apparatus is expensed in full ($96,000) in Year 1 because it has no alternative "
    "future use -- no depreciation is taken on it, so the April 1 date is irrelevant. "
    "Item 2 equipment has significant alternative future uses, so it is capitalized and its "
    "annual depreciation ($80,000) is charged to R&D expense while used in R&D. "
    "Item 9 preproduction prototypes are R&D under ASC 730. Item 8 routine troubleshooting of "
    "an existing commercial production line and item 7 unrelated G&A are excluded from R&D. "
    "Item 10 patent registration legal fees are a capitalized intangible (not R&D, since the "
    "process was already successfully developed); amortized over the 10-year useful life "
    "(shorter than the 20-year remaining legal life) from July 1, giving $600 in Year 1. "
    "Disposal: 3 x $80,000 = $240,000 accumulated depreciation, book value $240,000, "
    "$250,000 proceeds => $10,000 gain. The Year 1-6 schedule closes exactly to $0."
)

print(json.dumps(dict(
    id="agent_092#00",
    rounding_convention=("decimal.Decimal throughout; ROUND_HALF_UP to whole dollars per "
                         "period, with the final schedule period forced so depreciation "
                         "closes exactly to the $0 residual (all quotients here divide evenly, "
                         "so no rounding residue arises)"),
    answers=A,
    journal_entries=jes,
    insufficient_info=False,
    notes=notes,
), indent=1))
