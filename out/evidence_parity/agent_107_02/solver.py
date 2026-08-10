"""Solver for agent_107#02 - Bayline Packaging Co. lump-sum stock issuance.

Rounding convention: all monetary amounts computed with decimal.Decimal and
rounded HALF_UP to the cent ($0.01) at each reported figure; allocation
percentages rounded HALF_UP to 4 decimal places for display only (allocations
are computed from unrounded ratios). No floats are used anywhere.
"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
PCT = Decimal("0.0001")

def m(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)

def p(x):
    return Decimal(x).quantize(PCT, rounding=ROUND_HALF_UP)

def f(d):
    return float(d)

# ---- Given inputs (from the question text only) ----
cs_shares = Decimal("2000")
cs_par = Decimal("5")
ps_shares = Decimal("1000")
ps_par = Decimal("10")

# Case A
a_lump = Decimal("95000")
a_cs_fv_per = Decimal("36")
a_ps_fv_per = Decimal("28")

# Case B
b_lump = Decimal("100000")
b_cs_fv_per = Decimal("38")

# ---- Case A: proportional (relative fair value) allocation ----
a_cs_fv = cs_shares * a_cs_fv_per
a_ps_fv = ps_shares * a_ps_fv_per
a_total_fv = a_cs_fv + a_ps_fv
a_cs_pct = a_cs_fv / a_total_fv
a_ps_pct = a_ps_fv / a_total_fv
a_cs_alloc = m(a_lump * a_cs_pct)
a_ps_alloc = m(a_lump - (a_lump * a_cs_pct))  # remainder keeps Dr = Cr

a_cs_par_total = m(cs_shares * cs_par)
a_ps_par_total = m(ps_shares * ps_par)
a_cs_apic = m(a_cs_alloc - a_cs_par_total)
a_ps_apic = m(a_ps_alloc - a_ps_par_total)

# ---- Part c: paid-in capital presentation, Case A ----
c_total_pic = m(a_ps_par_total + a_cs_par_total + a_ps_apic + a_cs_apic)

# ---- Case B: incremental allocation ----
b_cs_alloc = m(cs_shares * b_cs_fv_per)
b_ps_alloc = m(b_lump - b_cs_alloc)
b_cs_par_total = m(cs_shares * cs_par)
b_ps_par_total = m(ps_shares * ps_par)
b_cs_apic = m(b_cs_alloc - b_cs_par_total)
b_ps_apic = m(b_ps_alloc - b_ps_par_total)

answers = [
    # a - Case A
    {"label": "a: Case A - fair value of common issued (2,000 sh x $36)", "value": f(m(a_cs_fv))},
    {"label": "a: Case A - fair value of preferred issued (1,000 sh x $28)", "value": f(m(a_ps_fv))},
    {"label": "a: Case A - total relative fair value", "value": f(m(a_total_fv))},
    {"label": "a: Case A - allocation percentage to common (%)", "value": f(p(a_cs_pct * 100))},
    {"label": "a: Case A - allocation percentage to preferred (%)", "value": f(p(a_ps_pct * 100))},
    {"label": "a: Case A - proceeds allocated to common stock", "value": f(a_cs_alloc)},
    {"label": "a: Case A - proceeds allocated to preferred stock", "value": f(a_ps_alloc)},
    {"label": "a: Case A - Common Stock at par (2,000 sh x $5)", "value": f(a_cs_par_total)},
    {"label": "a: Case A - Paid-in Capital in Excess of Par - Common", "value": f(a_cs_apic)},
    {"label": "a: Case A - Preferred Stock at par (1,000 sh x $10)", "value": f(a_ps_par_total)},
    {"label": "a: Case A - Paid-in Capital in Excess of Par - Preferred", "value": f(a_ps_apic)},
    {"label": "a: Case A - cash debited March 1", "value": f(m(a_lump))},
    # b - Case B
    {"label": "b: Case B - proceeds allocated to common stock (2,000 sh x $38, incremental)", "value": f(b_cs_alloc)},
    {"label": "b: Case B - residual proceeds allocated to preferred stock ($100,000 - $76,000)", "value": f(b_ps_alloc)},
    {"label": "b: Case B - Common Stock at par (2,000 sh x $5)", "value": f(b_cs_par_total)},
    {"label": "b: Case B - Paid-in Capital in Excess of Par - Common", "value": f(b_cs_apic)},
    {"label": "b: Case B - Preferred Stock at par (1,000 sh x $10)", "value": f(b_ps_par_total)},
    {"label": "b: Case B - Paid-in Capital in Excess of Par - Preferred", "value": f(b_ps_apic)},
    {"label": "b: Case B - cash debited March 1", "value": f(m(b_lump))},
    # c - Case A presentation
    {"label": "c: Case A presentation - Preferred stock, $10 par, 1,000 shares issued and outstanding", "value": f(a_ps_par_total)},
    {"label": "c: Case A presentation - Common stock, $5 par, 2,000 shares issued and outstanding", "value": f(a_cs_par_total)},
    {"label": "c: Case A presentation - Paid-in capital in excess of par - preferred", "value": f(a_ps_apic)},
    {"label": "c: Case A presentation - Paid-in capital in excess of par - common", "value": f(a_cs_apic)},
    {"label": "c: Case A presentation - Total paid-in capital", "value": f(c_total_pic)},
    # d
    {"label": "d: Treatment of stock issue costs (not an expense)",
     "value": "Direct costs of issuing stock are a cost of obtaining capital, not of operations, so they are netted against the issuance proceeds - debited to Paid-in Capital in Excess of Par (reducing recorded paid-in capital) rather than reported as an expense on the income statement."},
]

journal_entries = [
    {"part": "a", "lines": [
        {"account": "Cash (March 1, Year 1 - Case A lump-sum issuance)", "debit": f(m(a_lump)), "credit": 0},
        {"account": "Preferred Stock ($10 par, 1,000 shares)", "debit": 0, "credit": f(a_ps_par_total)},
        {"account": "Paid-in Capital in Excess of Par - Preferred", "debit": 0, "credit": f(a_ps_apic)},
        {"account": "Common Stock ($5 par, 2,000 shares)", "debit": 0, "credit": f(a_cs_par_total)},
        {"account": "Paid-in Capital in Excess of Par - Common", "debit": 0, "credit": f(a_cs_apic)},
    ]},
    {"part": "b", "lines": [
        {"account": "Cash (March 1, Year 1 - Case B lump-sum issuance)", "debit": f(m(b_lump)), "credit": 0},
        {"account": "Preferred Stock ($10 par, 1,000 shares)", "debit": 0, "credit": f(b_ps_par_total)},
        {"account": "Paid-in Capital in Excess of Par - Preferred", "debit": 0, "credit": f(b_ps_apic)},
        {"account": "Common Stock ($5 par, 2,000 shares)", "debit": 0, "credit": f(b_cs_par_total)},
        {"account": "Paid-in Capital in Excess of Par - Common", "debit": 0, "credit": f(b_cs_apic)},
    ]},
]

for je in journal_entries:
    d = sum(Decimal(str(l["debit"])) for l in je["lines"])
    c = sum(Decimal(str(l["credit"])) for l in je["lines"])
    assert d == c, (je["part"], d, c)

assert a_cs_alloc + a_ps_alloc == m(a_lump)
assert b_cs_alloc + b_ps_alloc == m(b_lump)
assert c_total_pic == m(a_lump)

out = {
    "id": "agent_107#02",
    "rounding_convention": "decimal.Decimal throughout; monetary amounts rounded HALF_UP to the cent; allocation percentages rounded HALF_UP to 4 decimals for display only, with allocations computed from unrounded ratios and the residual class taking the balancing amount so Dr = Cr.",
    "answers": answers,
    "journal_entries": journal_entries,
    "insufficient_info": False,
    "notes": "Case A uses the proportional (relative fair value) method because both fair values are known: common $72,000 / $100,000 = 72%, preferred $28,000 / $100,000 = 28% of the $95,000 lump sum. Case B uses the incremental method because only the common fair value is reliable: common takes its $76,000 fair value and preferred takes the $24,000 residual. Part c total paid-in capital of $95,000 equals the Case A cash proceeds, since no issue costs were incurred.",
}
print(json.dumps(out, indent=2))
