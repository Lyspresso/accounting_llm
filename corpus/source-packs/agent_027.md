# Agent 27 — CORE DEMO — LO 18-2

**Chapter:** 18  
**LO title:** Recognize deferred tax liabilities attributable to taxable temporary differences  
**Critical gap LO:** yes

## Concept list for this pack
- Taxable temporary difference: future taxable amounts (revenues taxable after GAAP, or expenses deductible before GAAP)
- Balance-sheet signal: **asset GAAP basis > asset tax basis** → deferred tax liability (DTL)
- Measurement: **DTL = cumulative taxable temporary difference × enacted tax rate** (rate in effect when difference reverses)
- Initial recognition JE: Dr Income Tax Expense; Cr Deferred Tax Liability; Cr Income Tax Payable
- Current tax expense = taxable income × enacted rate; deferred tax expense (benefit) = increase (decrease) in DTL
- Multi-year **originating then reversing** temporary differences (accelerated tax depreciation vs GAAP SL)
- Period-end adjusting tax JE each year using **desired ending DTL** minus beginning DTL
- Settlement/elimination of DTL when cumulative temporary difference returns to zero (full reverse or asset disposal)
- Presentation: DTL reported as **noncurrent**; note disclosure of current vs deferred tax expense

---

### Q1 — CORE — Cedar Peak Fabricators: accelerated tax depreciation → DTL lifecycle (initial recognition emphasis)
**LO:** LO 18-2  
**Concept:** Initial recognition and multi-year measurement of DTL from taxable temporary difference (tax dep > GAAP dep); period-end tax JEs; full reversal settlement; noncurrent presentation  
**Scenario:**  
On **January 1, Year 1**, **Cedar Peak Fabricators Inc.** places specialized production equipment in service:

| Item | Detail |
|------|--------|
| Cost | **$80,000** (zero residual for both GAAP and tax) |
| GAAP depreciation | Straight-line over **4 years** → **$20,000** per year |
| Tax depreciation | Y1 **$32,000**; Y2 **$24,000**; Y3 **$16,000**; Y4 **$8,000** |
| Enacted tax rate (all years) | **25%** (flat; no rate change expected) |
| Beginning deferred tax balances | **$0** |
| Only temporary difference | Depreciable equipment book–tax basis difference |
| Year-end | December 31 |

Pretax **GAAP** income (after GAAP depreciation; no permanent differences):

| Year | Pretax GAAP income |
|------|-------------------:|
| 1 | $180,000 |
| 2 | $200,000 |
| 3 | $195,000 |
| 4 | $190,000 |

**Required:**  
(a) Explain why the depreciation difference is a **taxable** temporary difference and compute the **Year 1** taxable income and income tax payable.  
(b) Compute the **Year 1 ending DTL** and record the **December 31, Year 1** income tax expense journal entry (**initial recognition** of the DTL).  
(c) Prepare a **schedule** of cumulative taxable temporary difference and DTL balance at December 31 of Years 1–4 (show GAAP NBV, tax NBV, cum TTD, DTL).  
(d) Record the **period-end tax adjusting JEs** for Years 2, 3, and 4. Show that every JE balances and that Year 4 **settles** the DTL to zero.  
(e) For Year 1 only, show **balance-sheet** classification of Income Tax Payable and Deferred Tax Liability, and the **income-statement / note** split of current vs deferred tax expense.  
(f) Briefly state what “settlement” of the DTL means when the temporary difference fully reverses by end of Year 4.

**Answer key:**

**(a) Why taxable temporary difference; Year 1 taxable income and payable**

Tax depreciation exceeds GAAP depreciation in early years → tax basis of the asset falls faster than GAAP basis → **asset GAAP basis > asset tax basis**. Future recovery of the higher GAAP carrying amount (with little or no remaining tax basis) will produce **future taxable amounts** relative to pretax GAAP income. That is a **taxable temporary difference** → **deferred tax liability**.

| | Amount |
|---|---:|
| Pretax GAAP income, Year 1 | $180,000 |
| Less: excess of tax dep over GAAP dep ($32,000 − $20,000) | (12,000) |
| **Taxable income, Year 1** | **$168,000** |
| × 25% | |
| **Income tax payable (current tax), Year 1** | **$42,000** |

**(b) Year 1 ending DTL and initial recognition JE**

| | Amount |
|---|---:|
| GAAP NBV Dec 31 Y1 ($80,000 − $20,000) | $60,000 |
| Tax NBV Dec 31 Y1 ($80,000 − $32,000) | 48,000 |
| **Cumulative taxable temporary difference** | **$12,000** |
| × 25% | |
| **Deferred tax liability, Dec 31 Y1** | **$3,000** |

Deferred tax expense (increase in DTL) = $3,000 − $0 = **$3,000**.  
Total income tax expense = current $42,000 + deferred $3,000 = **$45,000**  
(check: pretax GAAP × 25% = $180,000 × 25% = $45,000).

**December 31, Year 1 — initial recognition of DTL (period-end tax adjusting JE):**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 45,000 | |
| Deferred Tax Liability | | 3,000 |
| Income Tax Payable | | 42,000 |

(Dr = Cr = **$45,000**)

**(c) Subsequent measurement schedule — Years 1–4**

| Dec 31 | GAAP NBV | Tax NBV | Cum. taxable temp. diff. | Enacted rate | **DTL balance** | Δ DTL (deferred tax exp/(ben)) |
|--------:|---------:|--------:|-------------------------:|-------------:|---------------:|-------------------------------:|
| Y1 | 60,000 | 48,000 | 12,000 | 25% | **3,000** | 3,000 |
| Y2 | 40,000 | 24,000 | 16,000 | 25% | **4,000** | 1,000 |
| Y3 | 20,000 | 8,000 | 12,000 | 25% | **3,000** | (1,000) |
| Y4 | 0 | 0 | 0 | 25% | **0** | (3,000) |

Originating years: Y1–Y2 (tax dep > GAAP dep). Reversing years: Y3–Y4 (tax dep < GAAP dep). Cum. TTD and DTL return to **zero** at end of Year 4.

Supporting taxable income / payable by year:

| Year | Pretax GAAP | Excess tax dep (rev.) | Taxable income | Tax payable @ 25% | Deferred tax exp/(ben) | Total tax expense |
|-----:|------------:|----------------------:|---------------:|------------------:|-----------------------:|------------------:|
| 1 | 180,000 | 12,000 | 168,000 | 42,000 | 3,000 | 45,000 |
| 2 | 200,000 | 4,000 | 196,000 | 49,000 | 1,000 | 50,000 |
| 3 | 195,000 | (4,000) | 199,000 | 49,750 | (1,000) | 48,750 |
| 4 | 190,000 | (12,000) | 202,000 | 50,500 | (3,000) | 47,500 |

Checks: each total tax expense = pretax GAAP × 25%.

**(d) Period-end adjusting JEs — Years 2–4 (settlement in Year 4)**

**December 31, Year 2** (DTL to $4,000; increase $1,000):

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 50,000 | |
| Deferred Tax Liability | | 1,000 |
| Income Tax Payable | | 49,000 |

(Dr = Cr = **$50,000**)

**December 31, Year 3** (DTL to $3,000; decrease $1,000 → debit DTL):

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 48,750 | |
| Deferred Tax Liability | 1,000 | |
| Income Tax Payable | | 49,750 |

(Dr = Cr = **$49,750**)

**December 31, Year 4** (DTL to $0; decrease $3,000 — **full settlement/elimination** of DTL):

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 47,500 | |
| Deferred Tax Liability | 3,000 | |
| Income Tax Payable | | 50,500 |

(Dr = Cr = **$50,500**)

After this entry, Deferred Tax Liability balance = **$0** (temporary difference fully reversed).

**(e) Year 1 presentation and disclosure**

**Balance sheet (excerpt) — December 31, Year 1**

| Classification | Account | Amount |
|---|---|---:|
| Current liabilities | Income Tax Payable | $42,000 |
| **Noncurrent** liabilities | **Deferred Tax Liability** | **$3,000** |

(Under ASC 740, deferred tax liabilities are presented as **noncurrent**.)

**Income statement / notes — Year 1**

| | Amount |
|---|---:|
| Income tax expense (total) | $45,000 |
| — Current | $42,000 |
| — Deferred | $3,000 |

**(f) Settlement meaning**  
“Settlement” of a DTL is not a separate cash payment of the liability. As the taxable temporary difference **reverses**, future taxable income is higher relative to pretax GAAP income; the company pays **higher current tax** in those years and **debits Deferred Tax Liability**, reducing (and ultimately eliminating) the balance. By end of Year 4, DTL is fully settled to zero.

**Key insight:** A DTL is recognized when a taxable temporary difference exists (here, accelerated tax depreciation). Measure the **cumulative** book–tax basis difference × **enacted** rate for the **desired ending DTL**, then adjust the DTL account so the tax JE’s deferred component equals the change in that balance. Current tax always tracks the tax return; deferred tax tracks the future taxable consequence.

---

### Q2 — CORE number variant — Meridian Alloy Works: accelerated tax dep DTL twin
**LO:** LO 18-2  
**Concept:** DTL from taxable temporary difference (number-variant twin of Q1) — initial recognition, multi-year schedule, period-end JEs, full reverse  
**Scenario:**  
On **January 1, Year 1**, **Meridian Alloy Works LLC** acquires a finishing line:

| Item | Detail |
|------|--------|
| Cost | **$120,000** (zero residual GAAP and tax) |
| GAAP depreciation | SL over **4 years** → **$30,000**/year |
| Tax depreciation | Y1 **$48,000**; Y2 **$36,000**; Y3 **$24,000**; Y4 **$12,000** |
| Enacted tax rate (all years) | **30%** |
| Beginning deferred taxes | **$0** |
| Only temporary difference | Equipment book–tax basis |

Pretax GAAP income:

| Year | Pretax GAAP income |
|------|-------------------:|
| 1 | $250,000 |
| 2 | $280,000 |
| 3 | $270,000 |
| 4 | $260,000 |

**Required:**  
(a) Year 1 taxable income, tax payable, ending DTL, and **initial recognition** tax JE.  
(b) Full **DTL measurement schedule** Years 1–4.  
(c) Period-end tax JEs for Years 2–4 (show Year 4 settles DTL to zero).  
(d) State the Year 2 balance-sheet amount and classification of the DTL.

**Answer key:**

**(a) Year 1**

| | Amount |
|---|---:|
| Pretax GAAP | $250,000 |
| Excess tax dep ($48,000 − $30,000) | (18,000) |
| **Taxable income** | **$232,000** |
| Tax payable @ 30% | **$69,600** |
| Cum. TTD (GAAP NBV $90,000 − tax NBV $72,000) | **$18,000** |
| **DTL ending** ($18,000 × 30%) | **$5,400** |
| Total tax expense ($69,600 + $5,400) | **$75,000** (= $250,000 × 30%) |

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 75,000 | |
| Deferred Tax Liability | | 5,400 |
| Income Tax Payable | | 69,600 |

(Dr = Cr = **$75,000**)

**(b) Schedule**

| Dec 31 | GAAP NBV | Tax NBV | Cum. TTD | Rate | **DTL** | Δ DTL |
|--------:|---------:|--------:|---------:|-----:|--------:|------:|
| Y1 | 90,000 | 72,000 | 18,000 | 30% | **5,400** | 5,400 |
| Y2 | 60,000 | 36,000 | 24,000 | 30% | **7,200** | 1,800 |
| Y3 | 30,000 | 12,000 | 18,000 | 30% | **5,400** | (1,800) |
| Y4 | 0 | 0 | 0 | 30% | **0** | (5,400) |

Supporting payable / expense:

| Year | TI | Payable | Deferred exp/(ben) | Total tax exp |
|-----:|---:|--------:|-------------------:|--------------:|
| 1 | 232,000 | 69,600 | 5,400 | 75,000 |
| 2 | 274,000 | 82,200 | 1,800 | 84,000 |
| 3 | 276,000 | 82,800 | (1,800) | 81,000 |
| 4 | 278,000 | 83,400 | (5,400) | 78,000 |

**(c) Period-end JEs Years 2–4**

**Year 2:**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 84,000 | |
| Deferred Tax Liability | | 1,800 |
| Income Tax Payable | | 82,200 |

(Dr = Cr = **$84,000**)

**Year 3:**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 81,000 | |
| Deferred Tax Liability | 1,800 | |
| Income Tax Payable | | 82,800 |

(Dr = Cr = **$82,800**)

**Year 4 (settlement to zero):**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 78,000 | |
| Deferred Tax Liability | 5,400 | |
| Income Tax Payable | | 83,400 |

(Dr = Cr = **$83,400**; DTL ending balance **$0**)

**(d) Presentation Year 2**  
Deferred Tax Liability **$7,200**, reported as a **noncurrent** liability (not netted with Income Tax Payable).

**Key insight:** Changing cost, rate, and pretax income does not change the model: **cum. TTD × enacted rate = DTL**; the tax JE plugs current payable from the return and deferred from the change in DTL.

---

### Q3 — CORE alternate angles — prepaid origin/reverse + installment sale + disposal settlement
**LO:** LO 18-2  
**Concept:** (1) Prepaid expense taxable temp. difference — initial DTL and full reverse next year; (2) installment receivable DTL; (3) disposal of depreciable asset settles remaining DTL  
**Scenario:**  
Three independent situations for companies with a **25%** enacted tax rate and **zero** beginning deferred tax balances unless stated. Accounting and tax years end December 31.

**Situation A — Harbor Ridge Outfitters (prepaid insurance; Demo 18-2 style)**  
Year 1 taxable income is **$300,000**. Sole temporary difference: Prepaid Insurance has a **GAAP basis of $16,000** and a **tax basis of $0** at December 31, Year 1 (fully deductible for tax when paid in Year 1; expensed for GAAP in Year 2). In Year 2 the prepaid is fully expensed for GAAP; taxable income is **$320,000**; cumulative temporary difference is zero at year-end.

**Situation B — Lakeshore Machine Co. (installment sale receivable)**  
In Year 1 Lakeshore sells equipment on the installment basis. Pretax GAAP income of **$150,000** includes the **full $24,000** gross profit. For tax, only the portion of gross profit on cash collections is taxable. Cash collections in Year 1 recognize **$7,200** of the gross profit for tax; the remaining **$16,800** of uncollected gross profit is a taxable temporary difference (installment receivable GAAP basis exceeds tax basis). Year 2 collects the rest; pretax GAAP income is **$140,000** (no additional installment gross profit); taxable income includes the remaining **$16,800** of gross profit on collection.

**Situation C — Summit Castings Inc. (bonus depreciation + disposal settles DTL)**  
January 1, Year 1: machine cost **$48,000**, residual zero.  
- GAAP: SL over **3 years** → **$16,000**/year.  
- Tax: **100%** bonus depreciation in Year 1 ($48,000).  
- Pretax GAAP income Year 1: **$100,000**.  
- Pretax GAAP income Year 2 **before** any sale: **$110,000** (includes Year 2 GAAP depreciation of $16,000).  
- On **December 31, Year 2**, immediately after recording Year 2 depreciation, Summit **sells** the machine for **$18,000** cash. Book NBV at sale = $16,000 → book gain **$2,000**. Tax basis at sale = **$0** → tax gain **$18,000**. Pretax GAAP income Year 2 **including** the $2,000 book gain is therefore **$112,000**. No other temporary differences.

**Required:**  
(a) **Situation A:** Compute Year 1 DTL and record Year 1 and Year 2 tax JEs.  
(b) **Situation B:** Compute Year 1 DTL; record Year 1 and Year 2 tax JEs (settlement of installment DTL on collection).  
(c) **Situation C:** Compute Year 1 DTL and Year 1 tax JE. Compute Year 2 taxable income (include tax gain on sale), ending DTL, and Year 2 tax JE. Explain how **disposal** settles the remaining DTL.  
(d) For Situations A–C, state balance-sheet **classification** of any ending DTL at December 31, Year 1.

**Answer key:**

**(a) Situation A — prepaid insurance**

Year 1: Cum. TTD = $16,000 − $0 = **$16,000**; DTL = $16,000 × 25% = **$4,000**.  
Current tax = $300,000 × 25% = **$75,000**.  
Total tax expense = $75,000 + $4,000 = **$79,000**.

**Dec 31, Year 1:**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 79,000 | |
| Deferred Tax Liability | | 4,000 |
| Income Tax Payable | | 75,000 |

(Dr = Cr = **$79,000**)

Year 2: Cum. TTD = **$0** → desired DTL = **$0**; decrease DTL = **$4,000**.  
Current tax = $320,000 × 25% = **$80,000**.  
Total tax expense = $80,000 − $4,000 = **$76,000**.

**Dec 31, Year 2 (full reverse / settle DTL):**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 76,000 | |
| Deferred Tax Liability | 4,000 | |
| Income Tax Payable | | 80,000 |

(Dr = Cr = **$80,000**)

**(b) Situation B — installment sale**

Year 1: Uncollected gross profit (taxable temporary difference) = **$16,800**.  
DTL = $16,800 × 25% = **$4,200**.  
Taxable income = $150,000 − $16,800 = **$133,200**  
(or $150,000 − $24,000 full GP + $7,200 taxable GP).  
Tax payable = $133,200 × 25% = **$33,300**.  
Total tax expense = $33,300 + $4,200 = **$37,500** (= $150,000 × 25%).

**Dec 31, Year 1:**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 37,500 | |
| Deferred Tax Liability | | 4,200 |
| Income Tax Payable | | 33,300 |

(Dr = Cr = **$37,500**)

Year 2: Remaining GP collected → cum. TTD = **$0**; reverse DTL **$4,200**.  
Taxable income = $140,000 + $16,800 = **$156,800**.  
Tax payable = $156,800 × 25% = **$39,200**.  
Total tax expense = $39,200 − $4,200 = **$35,000** (= $140,000 × 25%).

**Dec 31, Year 2 (settlement of installment DTL):**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 35,000 | |
| Deferred Tax Liability | 4,200 | |
| Income Tax Payable | | 39,200 |

(Dr = Cr = **$39,200**)

**(c) Situation C — bonus depreciation + disposal**

**Year 1:** Excess tax dep = $48,000 − $16,000 = **$32,000**.  
TI = $100,000 − $32,000 = **$68,000**; payable = **$17,000**.  
GAAP NBV $32,000 − tax NBV $0 = cum. TTD **$32,000**; DTL = **$8,000**.  
Tax expense = $17,000 + $8,000 = **$25,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 25,000 | |
| Deferred Tax Liability | | 8,000 |
| Income Tax Payable | | 17,000 |

(Dr = Cr = **$25,000**)

**Year 2 (including sale):**  
- Ops pretax before sale $110,000 already includes GAAP dep $16,000 (tax dep $0) → $16,000 of the original $32,000 TTD would reverse through use.  
- Sale: book gain $2,000 included in pretax $112,000; tax gain $18,000. Remaining basis difference $16,000 becomes taxable on sale.  
- End of Year 2: asset gone; cum. TTD = **$0**; desired DTL = **$0**; Δ DTL from beginning $8,000 = **($8,000)**.

Taxable income Year 2:  
\[
TI = 112{,}000 + 16{,}000\ (\text{book dep with zero tax dep}) - 2{,}000\ (\text{remove book gain}) + 18{,}000\ (\text{tax gain}) = \mathbf{\$144{,}000}
\]  
(Equivalently: ops TI $110,000 + $16,000 + tax gain on sale $18,000 = $144,000.)

Tax payable = $144,000 × 25% = **$36,000**.  
Total tax expense = $36,000 − $8,000 = **$28,000** (= $112,000 × 25%).

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 28,000 | |
| Deferred Tax Liability | 8,000 | |
| Income Tax Payable | | 36,000 |

(Dr = Cr = **$36,000**; DTL settled to **$0**)

**Disposal settlement:** Selling the asset recovers the remaining GAAP carrying amount while tax basis is already zero, generating **extra taxable gain** equal to the remaining taxable temporary difference. That reverse eliminates the DTL in the same period as the sale (debit DTL; higher current tax on the tax return).

**(d) Classification at Dec 31, Year 1**  
All DTLs (A $4,000; B $4,200; C $8,000) are reported as **noncurrent liabilities**. Income Tax Payable is **current**.

**Key insight:** Any taxable temporary difference — prepaid expense, installment receivable, or depreciable asset — measures the same way: **cum. future taxable amount × enacted rate = DTL**. The DTL is eliminated when the difference reverses through use, collection, or **disposal**.

---

### Q4 — MC — Classification / presentation of deferred tax liability
**LO:** LO 18-2  
**Concept:** Balance-sheet classification of DTL and composition of income tax expense  
**Question:**  
At December 31, Year 1, Pine Valley Distributors has Income Tax Payable of $90,000 and a Deferred Tax Liability of $12,000 arising solely from a taxable temporary difference that will reverse evenly over the next three years. Under U.S. GAAP (ASC 740), how should these amounts be presented, and how is the $12,000 related to Year 1 income tax expense?

- A) Show $90,000 current and $12,000 noncurrent liabilities; the $12,000 is **deferred** tax expense (part of total income tax expense).  
- B) Show $94,000 current and $8,000 noncurrent liabilities by classifying one year of the DTL as current; the $12,000 reduces current tax expense.  
- C) Net the amounts and show a single current liability of $78,000; the $12,000 is a permanent difference.  
- D) Show both the $90,000 and the $12,000 as current liabilities because the temporary difference begins reversing next year.

**Answer:** **A.**  
ASC 740 requires deferred tax liabilities (and assets) to be classified as **noncurrent**. Income Tax Payable is current. An **increase** in DTL increases **deferred** income tax expense; companies still disclose current vs deferred components of total income tax expense. There is no current/noncurrent split of the DTL based on reversal timing under current GAAP.

---

### Q5 — MC — Identifying a taxable temporary difference that creates a DTL
**LO:** LO 18-2  
**Concept:** Which fact pattern creates a deferred tax liability (taxable temporary difference)  
**Question:**  
Which of the following situations creates a **deferred tax liability** at year-end?

- A) Warranty expense accrued for GAAP; costs are deductible for tax only when paid.  
- B) Rent received in advance: taxable when cash is collected; deferred as unearned revenue for GAAP.  
- C) Equipment cost fully expensed (bonus depreciation) for tax in Year 1; depreciated straight-line for GAAP over five years.  
- D) Municipal bond interest recognized in pretax GAAP income; permanently tax-exempt.

**Answer:** **C.**  
Bonus/accelerated tax depreciation reduces tax basis below GAAP basis (**asset GAAP > asset tax**) → future taxable amounts → **taxable temporary difference** → **DTL**.  
A and B create **deductible** temporary differences (DTAs). D is a **permanent** difference (no deferred tax).

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on all entries)
- [x] Math recomputed (pretax × rate = total tax expense checks; schedules roll to zero)
- [x] Core demo not sidebar-only (Demo 18-2 / Review 18-2 path: prepaid, accelerated dep, installment, presentation)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5 only)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
