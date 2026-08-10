# Agent 128 — CORE DEMO — LO 21-5

**Chapter:** 21  
**LO title:** Apply tax effects to changes in accounting principle and error corrections  
**Critical gap LO:** no

## Concept list for this pack
- **Initial recognition JE (change in principle, books ≠ tax):** retrospective cumulative effect **net of tax** to Retained Earnings; record **Deferred Tax Asset** when book inventory (or other base) falls below tax base, or **Deferred Tax Liability** when book base rises above tax base
- **Initial recognition JE (LIFO change, book = tax):** LIFO conformity forces tax method change; tax effect is **Income Tax Payable** (repay prior LIFO tax savings), not a deferred tax balance
- **Error correction JE (error on tax return, book = tax):** **Prior period adjustment** net of tax; tax effect is **Income Tax Receivable** (or Payable) because cash taxes were wrong—**no new temporary difference**
- **Error correction JE (books wrong, tax correct):** remove the **deferred tax** that arose from the temporary difference; PPA is pretax correction net of reversing the DTA/DTL
- **Subsequent measurement schedule:** temporary-difference / deferred-tax rollforward after a principle change; retained-earnings rollforward (beginning RE → cumulative effect or PPA net of tax → adjusted beginning RE)
- **Period-end adjusting / correcting JE:** record PPA and related tax when error is discovered after prior statements issued
- **Classification / presentation / disclosure:** change-in-principle cumulative effect and error PPAs appear **net of tax** in the statement of retained earnings / equity; disclose nature of change or error and tax effects **gross and net** (ASC 250)
- **Number-variant twin:** same structures, all amounts changed

---

### Q1 — CORE — Tax effects: FIFO→average-cost change and capitalized-repair error
**LO:** LO 21-5  
**Concept:** Initial recognition JE for change in accounting principle with DTA (books ≠ tax); temporary-difference schedule and RE rollforward; error-correction PPA with income tax receivable (error on tax return); opposite principle change creating DTL; presentation/disclosure  
**Scenario:**  
**Cedarline Retail Group** is a calendar-year company. Enacted tax rate is **25%** for all years.

**Change in accounting principle (Parts a–c, e):**  
On **January 1, Year 5**, Cedarline voluntarily changes its inventory costing method from **FIFO to weighted-average** for **financial reporting only**. It continues to use **FIFO for tax purposes**. Management determines that if weighted-average had been applied in all prior periods, the **December 31, Year 4 inventory** balance would have been **$80,000 lower** than the FIFO balance currently on the books.

Comparative equity will report two years. **Beginning retained earnings, January 1, Year 5, as previously reported** (before the principle change): **$450,000**. Year 5 net income under the new method will be recorded separately during Year 5 (not needed for the Jan 1 entry).

**Error correction (Part d):**  
On **January 1, Year 1**, Cedarline paid **$24,000** cash for ordinary repairs and **erroneously debited Equipment**. Straight-line depreciation is **10% per year** with no residual value. The **same depreciation rate is used for tax**, and the **error carried over to the tax return**. Cedarline discovers the error on **January 1, Year 2** (after Year 1 statements were issued).

**Required:**  
a. Prepare the **January 1, Year 5 initial recognition JE** to record the cumulative effect of the change from FIFO to weighted-average, including tax effects.  
b. Prepare a **temporary-difference / deferred-tax schedule** immediately after the Jan 1, Year 5 entry (inventory book vs tax carrying amount, temporary difference type, deferred tax balance).  
c. Prepare the **retained earnings rollforward** for the beginning of Year 5 showing the retrospective effect of the principle change (as previously reported → cumulative effect net of tax → adjusted beginning RE).  
d. Prepare the **January 1, Year 2 correcting JE** for the capitalized repairs, including tax effects. Show the pretax income effect calculation.  
e. **Alternate principle change (same inventory gap, opposite direction):** Suppose instead Cedarline changed from **weighted-average to FIFO** for financial reporting only (still average-cost for tax), so inventory would be **$80,000 higher** under FIFO. Prepare the Jan 1 JE including tax effects.  
f. **Classification / presentation / disclosure:** For the FIFO→average change and the repair error, state (1) where the net-of-tax amounts appear, (2) whether deferred tax or current tax receivable/payable is used and why, and (3) key ASC 250 disclosure elements.

**Answer key:**  

**a. Initial recognition — change FIFO → weighted-average (January 1, Year 5)**

Pretax cumulative effect (inventory ↓ / cumulative COGS ↑) = **$80,000**  
Deferred tax asset = \( \$80{,}000 \times 25\% = \mathbf{\$20{,}000} \)  
Net of tax debit to retained earnings = \( \$80{,}000 - \$20{,}000 = \mathbf{\$60{,}000} \)

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings | 60,000 | |
| Deferred Tax Asset | 20,000 | |
| Inventory | | 80,000 |
| *Retrospective change FIFO → weighted-average; books only; tax still FIFO* | | |

**Check:** Dr 60,000 + 20,000 = 80,000 = Cr 80,000. **Balanced.**

**b. Subsequent measurement — temporary difference schedule (Jan 1, Year 5 after entry)**

| Item | Book carrying amount | Tax carrying amount | Temporary difference | Deferred tax (25%) |
|---|---:|---:|---:|---:|
| Inventory | Tax basis − $80,000 | Tax basis (FIFO) | Deductible $80,000 | **DTA $20,000** |

Reason: Book inventory is lower than tax inventory → future taxable income will be lower when the difference reverses (higher book COGS relative to tax as layers turn) → **deductible temporary difference** → **deferred tax asset**.

**c. Retained earnings rollforward (beginning Year 5)**

| | Amount |
|---|---:|
| Retained earnings, Jan 1, Year 5, as previously reported | $450,000 |
| Cumulative effect of change in accounting principle (net of $20,000 tax benefit) | (60,000) |
| **Retained earnings, Jan 1, Year 5, as adjusted** | **$390,000** |

**d. Error correction — repairs capitalized (January 1, Year 2)**

| Component | Amount |
|---|---:|
| Correct repair expense for Year 1 | $24,000 |
| Depreciation incorrectly recorded in Year 1 ($24,000 × 10%) | (2,400) |
| **Net understatement of Year 1 pretax expense (overstatement of pretax income)** | **$21,600** |
| Income tax receivable ($21,600 × 25%) | $5,400 |
| **Prior period adjustment, net of tax ($21,600 × 75%)** | **$16,200** |

Because the error also appeared on the tax return and book = tax methods, cash taxes were overpaid → **Income Tax Receivable**, **not** a deferred tax balance. No DTL/DTA to reverse (book and tax depreciation were identical under the error).

| Account | Debit | Credit |
|---|---:|---:|
| Accumulated Depreciation—Equipment | 2,400 | |
| Retained Earnings—Prior Period Adjustment | 16,200 | |
| Income Tax Receivable | 5,400 | |
| Equipment | | 24,000 |
| *Correct Year 1 capitalization of ordinary repairs; error on books and tax return* | | |

**Check:** Dr 2,400 + 16,200 + 5,400 = 24,000 = Cr 24,000. **Balanced.**

**e. Alternate — weighted-average → FIFO (books only; tax still average-cost)**

Pretax inventory increase = $80,000  
DTL = \( 80{,}000 \times 25\% = \$20{,}000 \)  
Net credit to RE = \( 80{,}000 - 20{,}000 = \$60{,}000 \)

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 80,000 | |
| Deferred Tax Liability | | 20,000 |
| Retained Earnings | | 60,000 |
| *Retrospective change average-cost → FIFO; books only* | | |

**Check:** Dr 80,000 = Cr 20,000 + 60,000. **Balanced.**

Book inventory higher than tax inventory → **taxable temporary difference** → **DTL**.

**f. Classification / presentation / disclosure**

1. **Where amounts appear:** Both the cumulative effect of the principle change and the error’s prior period adjustment are reported **net of tax** as adjustments to **beginning retained earnings** (statement of retained earnings / stockholders’ equity)—**not** as current-period income statement gains/losses.  
2. **Deferred vs current tax:**  
   - Principle change with **book method ≠ tax method** → **DTA or DTL** (temporary difference remains until inventory turns).  
   - Error that **carried to the tax return** with same measurement for book and tax → **Income Tax Receivable or Payable** (corrects cash taxes; no temporary difference).  
3. **Disclosures (ASC 250):** Nature of the principle change or error; effect on each FS line item and per-share amounts for periods presented (as applicable); cumulative effect on beginning RE of earliest period presented; for PPAs, effects **both gross and net of applicable income tax**.

**Key insight:** Retrospective principle changes and error PPAs are always **net of tax** to equity. The tax **account** depends on whether book and tax bases still differ (deferred tax) or whether cash taxes were simply wrong (receivable/payable).

---

### Q2 — CORE number variant
**LO:** LO 21-5  
**Concept:** Number-variant twin — FIFO→average with DTA at a different rate; multi-year depreciation error with tax receivable; RE schedule  
**Scenario:**  
**Harborline Distributors Inc.** (calendar year-end). Enacted tax rate is **30%**.

**Principle change:** On **January 1, Year 6**, Harborline changes from **FIFO to weighted-average** for financial reporting only; continues **FIFO for tax**. If weighted-average had always been used, Dec 31, Year 5 inventory would be **$120,000 lower**. Beginning RE as previously reported on Jan 1, Year 6: **$680,000**.

**Error:** On Jan 1, Year 1, Harborline paid **$40,000** for ordinary repairs and capitalized them to Equipment. SL depreciation **10%** per year, no residual; same for tax; error on tax return. Error discovered **January 1, Year 2**.

**Required:**  
a. January 1, Year 6 JE for the inventory principle change (with tax).  
b. Temporary-difference schedule after the entry.  
c. Beginning RE rollforward for Year 6.  
d. January 1, Year 2 correcting JE for the repair error (with tax), including pretax computation.  
e. Briefly state how Year 2 comparative statements treat the Year 1 error.

**Answer key:**  

**a. Change FIFO → weighted-average (January 1, Year 6)**

DTA = \( \$120{,}000 \times 30\% = \mathbf{\$36{,}000} \)  
RE debit = \( \$120{,}000 - \$36{,}000 = \mathbf{\$84{,}000} \)

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings | 84,000 | |
| Deferred Tax Asset | 36,000 | |
| Inventory | | 120,000 |

**Check:** Dr 84,000 + 36,000 = 120,000 = Cr 120,000. **Balanced.**

**b. Temporary-difference schedule**

| Item | Book vs tax | Temporary difference | Deferred tax (30%) |
|---|---|---:|---:|
| Inventory | Book = Tax − $120,000 | Deductible $120,000 | **DTA $36,000** |

**c. RE rollforward**

| | Amount |
|---|---:|
| RE, Jan 1, Year 6, as previously reported | $680,000 |
| Cumulative effect of principle change (net of $36,000 tax) | (84,000) |
| **RE, Jan 1, Year 6, as adjusted** | **$596,000** |

**d. Repair error correction (January 1, Year 2)**

| Component | Amount |
|---|---:|
| Correct repair expense Year 1 | $40,000 |
| Depreciation recorded Year 1 ($40,000 × 10%) | (4,000) |
| **Net pretax income overstatement Year 1** | **$36,000** |
| Income tax receivable ($36,000 × 30%) | $10,800 |
| **PPA net of tax ($36,000 × 70%)** | **$25,200** |

| Account | Debit | Credit |
|---|---:|---:|
| Accumulated Depreciation—Equipment | 4,000 | |
| Retained Earnings—Prior Period Adjustment | 25,200 | |
| Income Tax Receivable | 10,800 | |
| Equipment | | 40,000 |

**Check:** Dr 4,000 + 25,200 + 10,800 = 40,000 = Cr 40,000. **Balanced.**

**e. Comparative presentation**  
Restate Year 1 comparative amounts (remove equipment/AD effects; correct expenses and tax expense/net income). Cumulative income effect for periods not presented adjusts beginning RE of the earliest year presented, **net of tax**. Disclose nature of error and effects gross and net of tax.

**Key insight:** Changing the tax rate and inventory gap scales DTA and net RE proportionally; the **structure** of the entry (Dr RE + Dr DTA / Cr Inventory) is unchanged when books fall below tax.

---

### Q3 — CORE alternate angle — LIFO tax payable; multi-year error; books≠tax DTL
**LO:** LO 21-5  
**Concept:** LIFO→average change with Income Tax Payable (book = tax); multi-year depreciation understatement PPA with tax receivable; error only on books removing DTL; equity presentation schedule  
**Scenario:**  
**Northridge Products Co.** (calendar year-end). Tax rate **25%** unless noted.

**Part A — LIFO change (conformity):**  
On **January 1, Year 4**, Northridge changes from **LIFO to weighted-average** for **both financial reporting and tax** (LIFO conformity). If weighted-average had been used in all prior periods, inventory at Dec 31, Year 3 would be **$200,000 higher**. Taxes previously saved under LIFO must be repaid (treat the tax effect as currently payable for this problem).

**Part B — Multi-year depreciation error (book = tax):**  
In **Year 3**, Northridge discovers that depreciation expense was **understated by $8,000 in Year 1 and $8,000 in Year 2** (total pretax **$16,000**) for **both accounting and income tax purposes**. Record the entry on **January 1, Year 3**.

**Part C — Books wrong, tax correct (DTL reverse):**  
Also in Year 3, Northridge discovers that **$48,000** of operating costs paid in prior years were incorrectly left in **Prepaid Expense** on the books (never expensed). For **tax**, the costs were **correctly deducted when paid**. A deferred tax liability of \( \$48{,}000 \times 25\% = \$12{,}000 \) is on the books for this temporary difference. Prepare the correcting entry on January 1, Year 3.

**Part D — Equity presentation (Part A only):**  
Beginning RE as reported Jan 1, Year 4 before the LIFO change: **$525,000**. Show the RE rollforward for the cumulative effect of the LIFO change.

**Part E — Settlement of tax payable:**  
On **March 15, Year 4**, Northridge remits the full **$50,000** Income Tax Payable arising from the LIFO change (treat as a single settlement payment for this problem; ignore IRS installment timing details).

**Required:**  
a. JE for LIFO → weighted-average including tax (Part A).  
b. JE for multi-year depreciation error including tax (Part B).  
c. JE for prepaid/expense error removing DTL (Part C).  
d. RE rollforward for Part A.  
e. **Settlement JE** for payment of the LIFO-related Income Tax Payable (Part E).  
f. **Classification:** For each of (a)–(c), identify the tax balance sheet account used and one-sentence rationale.

**Answer key:**  

**a. LIFO → weighted-average, book and tax (January 1, Year 4)**

Pretax inventory increase = $200,000  
Income tax payable = \( \$200{,}000 \times 25\% = \mathbf{\$50{,}000} \)  
Net credit to RE = \( \$200{,}000 - \$50{,}000 = \mathbf{\$150{,}000} \)

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 200,000 | |
| Income Tax Payable | | 50,000 |
| Retained Earnings | | 150,000 |
| *Leave LIFO; increase inventory to average-cost; repay prior LIFO tax savings* | | |

**Check:** Dr 200,000 = Cr 50,000 + 150,000. **Balanced.**

(Not DTL: tax method changes with books under LIFO conformity, so the tax is a **current** obligation to repay prior savings, not a temporary difference that will reverse under different future tax treatment of the same base.)

**b. Multi-year depreciation understatement (January 1, Year 3)**

Pretax income overstatement total = \( \$8{,}000 + \$8{,}000 = \$16{,}000 \)  
Income tax receivable = \( \$16{,}000 \times 25\% = \mathbf{\$4{,}000} \)  
PPA net of tax = \( \$16{,}000 \times 75\% = \mathbf{\$12{,}000} \)

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings—Prior Period Adjustment | 12,000 | |
| Income Tax Receivable | 4,000 | |
| Accumulated Depreciation | | 16,000 |
| *Correct understated depreciation Years 1–2; error on books and tax* | | |

**Check:** Dr 12,000 + 4,000 = 16,000 = Cr 16,000. **Balanced.**

**c. Prepaid left on books; tax already deducted (January 1, Year 3)**

Remove overstated asset $48,000 and reverse related DTL $12,000; net hit to RE = $36,000.

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings—Prior Period Adjustment | 36,000 | |
| Deferred Tax Liability | 12,000 | |
| Prepaid Expense | | 48,000 |
| *Expense costs previously left in prepaid; tax already correct — reverse DTL* | | |

**Check:** Dr 36,000 + 12,000 = 48,000 = Cr 48,000. **Balanced.**

**d. RE rollforward — LIFO change only**

| | Amount |
|---|---:|
| RE, Jan 1, Year 4, as previously reported | $525,000 |
| Cumulative effect of change LIFO → average-cost (net of $50,000 tax) | 150,000 |
| **RE, Jan 1, Year 4, as adjusted** | **$675,000** |

**e. Settlement of LIFO-related Income Tax Payable (March 15, Year 4)**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Payable | 50,000 | |
| Cash | | 50,000 |
| *Settle tax obligation arising from change from LIFO* | | |

**Check:** Dr 50,000 = Cr 50,000. **Balanced.**

**f. Tax account classification**

| Scenario | Tax account | Why |
|---|---|---|
| (a) Leave LIFO (book = tax after change) | **Income Tax Payable** | Prior LIFO tax savings repaid; no ongoing book/tax inventory base difference from the method split |
| (b) Dep error on tax return | **Income Tax Receivable** | Taxable income was overstated; claim refund; book = tax so no temporary difference |
| (c) Books only error; tax correct | **Deferred Tax Liability** (removed) | Temporary difference is eliminated when the book asset is corrected |

**Key insight:** Same “net of tax to RE” pattern appears in three different tax accounts—**Payable** (LIFO repay), **Receivable** (tax return error), **DTA/DTL** (book ≠ tax temporary difference). Choosing the wrong tax account is a common exam trap. Settlement of the payable is a pure balance-sheet cash outflow (no additional RE hit).

---

### Q4 — MC (classification of tax effects)
**LO:** LO 21-5  
**Concept:** Classify tax balance-sheet account for principle changes and error corrections  

**Question 1:**  
On January 1, Year 3, a company changes from FIFO to weighted-average for **financial reporting only** and continues FIFO for **tax**. Inventory would have been **$60,000 lower** under weighted-average. Tax rate 25%. The tax effect of the retrospective entry is recorded as:

- A) Debit Income Tax Payable $15,000  
- B) Debit Deferred Tax Asset $15,000  
- C) Credit Deferred Tax Liability $15,000  
- D) Debit Income Tax Receivable $15,000  

**Answer:** **B.** Book inventory falls $60,000 below tax inventory → deductible temporary difference \( 60{,}000 \times 25\% = \$15{,}000 \) → **Deferred Tax Asset**. Not payable/receivable (tax method unchanged). Not DTL (book base is lower, not higher).

**Question 2:**  
An error **overstated expenses** in a prior period by the **same amount for financial reporting and tax**. When the error is corrected in a subsequent period, the tax effect is recorded as:

- A) Deferred Tax Liability  
- B) Deferred Tax Asset  
- C) Income Tax Payable  
- D) Valuation allowance on a deferred tax asset  

**Answer:** **C.** Because book and tax treatments were the same, there is **no temporary difference**. Understated taxable income meant **too little tax was paid** → correcting the error increases tax owed → **Income Tax Payable** (not deferred tax).

---

### Self-check
- [x] Every JE balances
- [x] Math recomputed (80k/25%, 120k/30%, 200k/25%, repair nets 21,600/36,000, multi-year 16,000, prepaid 48,000)
- [x] Core demo not sidebar-only (Demo 21-5A / 21-5B path; LIFO payable is textbook LO 21-5 related core treatment)
- [x] LO + Concept on every item
- [x] MC ≤ 2
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE (tax payable settlement obligation / reversal of DTL as “settlement” of temporary difference), classification_presentation_or_disclosure, number_variant_twin
