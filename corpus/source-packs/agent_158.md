# Agent 158 — CORE DEMO — LO 18-2

**Chapter:** 18  
**LO title:** Recognize deferred tax liabilities attributable to taxable temporary differences  
**Critical gap LO:** yes

## Concept list for this pack
- **Taxable temporary difference:** future taxable amounts when revenues are taxable after pretax GAAP income, or expenses are deductible for tax before pretax GAAP income
- **Balance-sheet signal:** **asset GAAP basis > asset tax basis** (common) → deferred tax liability (DTL)
- **Measurement:** **DTL = cumulative taxable temporary difference × enacted tax rate** (rate expected when the difference reverses)
- **Initial recognition JE:** Dr Income Tax Expense; Cr Deferred Tax Liability (originating); Cr Income Tax Payable
- **Current vs deferred tax expense:** current = taxable income × rate; deferred tax expense (benefit) = increase (decrease) in DTL
- **Subsequent measurement schedule (emphasis):** multi-year rollforward of GAAP NBV, tax NBV, cumulative TTD, ending DTL, and Δ DTL each year
- **Period-end adjusting JE:** set DTL to **desired ending balance** (ending − beginning = deferred tax expense or benefit)
- **Settlement / reverse:** when cumulative TTD returns to zero (full depreciation life, prepaid expires, collections on installment, or disposal of the asset), reverse remaining DTL
- **Classification / presentation / disclosure:** DTL reported as **noncurrent**; note disclosure of current and deferred components of income tax expense
- **Number-variant twin:** same skills with all amounts changed

---

### Q1 — CORE — Multi-year accelerated tax depreciation: subsequent DTL measurement schedule (emphasis)
**LO:** LO 18-2  
**Concept:** Subsequent measurement schedule of cumulative taxable temporary difference and DTL; initial recognition JE; multi-year period-end tax adjusting JEs; full reverse/settlement of DTL; noncurrent presentation and current vs deferred disclosure  
**Scenario:**  
On **January 1, Year 1**, **Ironvale Manufacturing Corp.** (calendar year) places specialized production machinery in service:

| Item | Detail |
|------|--------|
| Cost | **$120,000** (zero residual for both GAAP and tax) |
| GAAP depreciation | Straight-line over **5 years** → **$24,000** per year |
| Tax depreciation | Y1 **$48,000**; Y2 **$36,000**; Y3 **$18,000**; Y4 **$12,000**; Y5 **$6,000** |
| Enacted tax rate (all years) | **25%** (flat; no rate change expected) |
| Beginning deferred tax balances | **$0** |
| Only temporary difference | Depreciable equipment book–tax basis difference |
| Accounting and tax year-ends | December 31 |

Pretax **GAAP** income (after GAAP depreciation; no permanent differences):

| Year | Pretax GAAP income |
|------|-------------------:|
| 1 | $300,000 |
| 2 | $320,000 |
| 3 | $310,000 |
| 4 | $305,000 |
| 5 | $295,000 |

**Required:**  
(a) Explain why the depreciation difference is a **taxable** temporary difference. Compute **Year 1** taxable income and income tax payable.  
(b) Compute the **Year 1 ending DTL** and record the **December 31, Year 1** income tax expense journal entry (**initial recognition** of the DTL).  
(c) Prepare a **subsequent measurement schedule** for December 31 of Years 1–5 showing: GAAP NBV, tax NBV, cumulative taxable temporary difference, ending DTL, and deferred tax expense/(benefit) for the year.  
(d) Record the **period-end tax adjusting JEs** for Years 2–5. Show that every JE balances and that Year 5 **settles** the DTL to zero.  
(e) For Year 1 only, show **balance-sheet** classification of Income Tax Payable and Deferred Tax Liability, and the **note** split of current vs deferred tax expense.  
(f) Briefly state what “settlement” of the DTL means when the temporary difference fully reverses by end of Year 5.

**Answer key:**

**(a) Why taxable temporary difference; Year 1 taxable income and payable**

Tax depreciation exceeds GAAP depreciation in early years → tax basis of the asset falls faster than GAAP basis → **asset GAAP basis > asset tax basis**. Future recovery of the higher GAAP carrying amount (with little or no remaining tax basis) will produce **future taxable amounts** relative to pretax GAAP income. That is a **taxable temporary difference** → **deferred tax liability**.

| | Amount |
|---|---:|
| Pretax GAAP income, Year 1 | $300,000 |
| Less: excess of tax dep over GAAP dep ($48,000 − $24,000) | (24,000) |
| **Taxable income, Year 1** | **$276,000** |
| × 25% | |
| **Income tax payable (current tax), Year 1** | **$69,000** |

**(b) Year 1 ending DTL and initial recognition JE**

| | Amount |
|---|---:|
| GAAP NBV Dec 31 Y1 ($120,000 − $24,000) | $96,000 |
| Tax NBV Dec 31 Y1 ($120,000 − $48,000) | 72,000 |
| **Cumulative taxable temporary difference** | **$24,000** |
| × 25% | |
| **Deferred tax liability, Dec 31 Y1** | **$6,000** |

Deferred tax expense (increase in DTL) = $6,000 − $0 = **$6,000**.  
Total income tax expense = current $69,000 + deferred $6,000 = **$75,000**  
(check: pretax GAAP × 25% = $300,000 × 25% = $75,000).

**December 31, Year 1 — initial recognition of DTL (period-end tax adjusting JE):**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 75,000 | |
| Deferred Tax Liability | | 6,000 |
| Income Tax Payable | | 69,000 |
| *Record current tax and establish DTL for taxable temporary difference* | | |

**Check:** Dr 75,000 = Cr 6,000 + 69,000. **Balanced.**

**(c) Subsequent measurement schedule — Years 1–5 (emphasis)**

| Dec 31 | GAAP NBV | Tax NBV | Cum. taxable temp. diff. | Rate | **DTL balance** | Δ DTL = deferred tax exp/(ben) |
|--------:|---------:|--------:|-------------------------:|-----:|---------------:|-------------------------------:|
| Y1 | 96,000 | 72,000 | 24,000 | 25% | **6,000** | 6,000 |
| Y2 | 72,000 | 36,000 | 36,000 | 25% | **9,000** | 3,000 |
| Y3 | 48,000 | 18,000 | 30,000 | 25% | **7,500** | (1,500) |
| Y4 | 24,000 | 6,000 | 18,000 | 25% | **4,500** | (3,000) |
| Y5 | 0 | 0 | 0 | 25% | **0** | (4,500) |

Supporting depreciation each year:

| Year | GAAP dep | Tax dep | Originating/(reversing) TTD |
|-----:|---------:|--------:|----------------------------:|
| 1 | 24,000 | 48,000 | +24,000 |
| 2 | 24,000 | 36,000 | +12,000 |
| 3 | 24,000 | 18,000 | (6,000) |
| 4 | 24,000 | 12,000 | (12,000) |
| 5 | 24,000 | 6,000 | (18,000) |
| **Total** | **120,000** | **120,000** | **0** |

**Schedule checks:** total tax and GAAP depreciation both equal cost $120,000; cumulative TTD and DTL return to **zero** at end of Year 5; sum of Δ DTL = 6,000 + 3,000 − 1,500 − 3,000 − 4,500 = **0**. Originating years: Y1–Y2. Reversing years: Y3–Y5.

**(d) Period-end tax adjusting JEs — Years 2–5**

**Year 2**  
TI = $320,000 − $12,000 = **$308,000**; payable = $308,000 × 25% = **$77,000**  
Deferred tax expense = $9,000 − $6,000 = **$3,000**  
Total tax expense = $77,000 + $3,000 = **$80,000** (= $320,000 × 25%)

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 80,000 | |
| Deferred Tax Liability | | 3,000 |
| Income Tax Payable | | 77,000 |

**Check:** Dr 80,000 = Cr 3,000 + 77,000. **Balanced.** Ending DTL = **$9,000**.

**Year 3**  
TI = $310,000 + $6,000 = **$316,000**; payable = $316,000 × 25% = **$79,000**  
Deferred tax **benefit** = $7,500 − $9,000 = **($1,500)**  
Total tax expense = $79,000 − $1,500 = **$77,500** (= $310,000 × 25%)

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 77,500 | |
| Deferred Tax Liability | 1,500 | |
| Income Tax Payable | | 79,000 |

**Check:** Dr 77,500 + 1,500 = Cr 79,000. **Balanced.** Ending DTL = **$7,500**.

**Year 4**  
TI = $305,000 + $12,000 = **$317,000**; payable = $317,000 × 25% = **$79,250**  
Deferred tax benefit = $4,500 − $7,500 = **($3,000)**  
Total tax expense = $79,250 − $3,000 = **$76,250** (= $305,000 × 25%)

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 76,250 | |
| Deferred Tax Liability | 3,000 | |
| Income Tax Payable | | 79,250 |

**Check:** Dr 76,250 + 3,000 = Cr 79,250. **Balanced.** Ending DTL = **$4,500**.

**Year 5 — settlement of DTL to zero**  
TI = $295,000 + $18,000 = **$313,000**; payable = $313,000 × 25% = **$78,250**  
Deferred tax benefit = $0 − $4,500 = **($4,500)**  
Total tax expense = $78,250 − $4,500 = **$73,750** (= $295,000 × 25%)

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 73,750 | |
| Deferred Tax Liability | 4,500 | |
| Income Tax Payable | | 78,250 |

**Check:** Dr 73,750 + 4,500 = Cr 78,250. **Balanced.** Ending DTL = **$0** (fully settled).

**(e) Year 1 presentation and disclosure**

**Balance sheet (excerpt) — Dec 31, Year 1**

| | Amount |
|---|---:|
| **Current liabilities** | |
| Income tax payable | $69,000 |
| **Noncurrent liabilities** | |
| Deferred tax liability | $6,000 |

**Income tax expense note — Year 1**

| | Amount |
|---|---:|
| Current | $69,000 |
| Deferred | 6,000 |
| **Total income tax expense** | **$75,000** |

**(f) Settlement meaning**

“Settlement” of the DTL means the **cumulative taxable temporary difference has reversed to zero** (GAAP and tax bases of the asset are both zero). The company no longer has an expected **future tax obligation** from that difference; the DTL balance is reduced to **zero** through deferred tax **benefit** as the difference reverses (higher taxable income relative to pretax GAAP in reversing years).

**Key insight:** Measure the DTL from the **balance-sheet cumulative temporary difference** each year (GAAP NBV − tax NBV) × enacted rate; the period JE simply moves the DTL account from its beginning balance to that desired ending balance. Originating years increase DTL (deferred tax expense); reversing years decrease DTL (deferred tax benefit) until settlement at zero.

---

### Q2 — CORE number variant — 100% tax expensing: full DTL lifecycle schedule
**LO:** LO 18-2  
**Concept:** Number-variant twin: DTL from taxable temporary difference under 100% bonus depreciation; subsequent measurement schedule; period-end JEs; full reverse settlement  
**Scenario:**  
On **January 1, Year 1**, **Silverpine Equipment Co.** acquires equipment:

| Item | Detail |
|------|--------|
| Cost | **$90,000** (zero residual for GAAP and tax) |
| GAAP depreciation | Straight-line over **3 years** → **$30,000** per year |
| Tax depreciation | **100% bonus expensing** in Year 1 ($90,000); $0 in Years 2–3 |
| Enacted tax rate | **25%** all years |
| Beginning deferred taxes | **$0** |
| Only temporary difference | Equipment book–tax basis |
| Year-end | December 31 |

Pretax GAAP income (after GAAP depreciation; no permanent differences):

| Year | Pretax GAAP income |
|------|-------------------:|
| 1 | $150,000 |
| 2 | $160,000 |
| 3 | $155,000 |

**Required:**  
(a) Compute Year 1 taxable income, income tax payable, ending DTL, and the **December 31, Year 1** tax JE.  
(b) Prepare the **3-year subsequent measurement schedule** (GAAP NBV, tax NBV, cum TTD, DTL, Δ DTL).  
(c) Record period-end tax JEs for Years 2 and 3 (Year 3 settles DTL to zero).  
(d) Verify that total income tax expense each year equals pretax GAAP income × 25%.

**Answer key:**

**(a) Year 1 — initial recognition**

| | Amount |
|---|---:|
| Pretax GAAP income | $150,000 |
| Less: excess tax dep ($90,000 − $30,000) | (60,000) |
| **Taxable income** | **$90,000** |
| Income tax payable ($90,000 × 25%) | **$22,500** |
| GAAP NBV Dec 31 Y1 | $60,000 |
| Tax NBV Dec 31 Y1 | 0 |
| Cum. taxable temporary difference | **$60,000** |
| **DTL ($60,000 × 25%)** | **$15,000** |
| Total income tax expense ($22,500 + $15,000) | **$37,500** |

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 37,500 | |
| Deferred Tax Liability | | 15,000 |
| Income Tax Payable | | 22,500 |
| *Establish DTL for 100% tax expensing taxable temporary difference* | | |

**Check:** Dr 37,500 = Cr 15,000 + 22,500. **Balanced.**  
Check: $150,000 × 25% = $37,500.

**(b) Subsequent measurement schedule**

| Dec 31 | GAAP NBV | Tax NBV | Cum. TTD | Rate | **DTL** | Δ DTL exp/(ben) |
|--------:|---------:|--------:|---------:|-----:|--------:|----------------:|
| Y1 | 60,000 | 0 | 60,000 | 25% | **15,000** | 15,000 |
| Y2 | 30,000 | 0 | 30,000 | 25% | **7,500** | (7,500) |
| Y3 | 0 | 0 | 0 | 25% | **0** | (7,500) |

Year 1 originates the entire $60,000 TTD (tax takes full cost immediately). Years 2–3 reverse $30,000 each year as GAAP continues to depreciate with zero tax basis remaining.

**(c) Years 2 and 3 period-end JEs**

**Year 2**  
TI = $160,000 + $30,000 = **$190,000**; payable = **$47,500**  
Deferred tax benefit = $7,500 − $15,000 = **($7,500)**  
Tax expense = $47,500 − $7,500 = **$40,000**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 40,000 | |
| Deferred Tax Liability | 7,500 | |
| Income Tax Payable | | 47,500 |

**Check:** Dr 40,000 + 7,500 = Cr 47,500. **Balanced.**

**Year 3 — settlement**  
TI = $155,000 + $30,000 = **$185,000**; payable = **$46,250**  
Deferred tax benefit = $0 − $7,500 = **($7,500)**  
Tax expense = $46,250 − $7,500 = **$38,750**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 38,750 | |
| Deferred Tax Liability | 7,500 | |
| Income Tax Payable | | 46,250 |

**Check:** Dr 38,750 + 7,500 = Cr 46,250. **Balanced.** Ending DTL = **$0**.

**(d) Pretax × rate checks**

| Year | Pretax × 25% | Tax expense from JE |
|-----:|-------------:|--------------------:|
| 1 | $37,500 | $37,500 |
| 2 | 40,000 | 40,000 |
| 3 | 38,750 | 38,750 |

**Key insight:** 100% tax expensing creates a **large originating** DTL in Year 1 that **reverses systematically** as book depreciation continues with tax basis already at zero. The schedule still drives the measurement: desired ending DTL each year equals remaining cum TTD × rate.

---

### Q3 — CORE alternate angles — Prepaid reverse, installment DTL, asset disposal settlement, presentation
**LO:** LO 18-2  
**Concept:** Period-end adjusting JE for prepaid-expense taxable temp. difference and full reverse; installment receivable DTL; disposal of depreciable asset settles remaining DTL; classification and disclosure  
**Scenario:**  
**Broadview Media Group** is a calendar-year corporation. Enacted tax rate is **25%** for all years unless noted. Treat each part as an independent fact pattern unless stated.

**Part A — Prepaid insurance (originate then reverse)**  
For the year ended **December 31, Year 1**, Broadview reports **taxable income of $240,000**. The only temporary difference is **Prepaid Insurance**: GAAP basis **$16,000**, tax basis **$0** (fully deducted for tax when paid). The prepaid will be expensed for GAAP entirely in Year 2. Beginning deferred tax balances = **$0**.  
In Year 2, taxable income is **$256,000**, and the prepaid has a zero balance for both GAAP and tax at December 31, Year 2.

**Part B — Installment sale receivable**  
On **December 31, Year 1**, Broadview has an installment receivable related to a sale recorded fully under GAAP. Remaining **gross profit embedded** in the installment receivable (taxable when cash is collected) is **$28,000**. Tax basis of the installment receivable’s unrecognized profit is **$0**. Beginning DTL related to this item = **$0**. Taxable income for Year 1 (after all current-year collections and other items) is **$200,000**. Assume this is the only temporary difference.

**Part C — Disposal of asset settles remaining DTL**  
**Canyonridge Industrial LLC** holds equipment with the following bases immediately **before sale** on **July 1, Year 3**:

| | Amount |
|---|---:|
| GAAP net book value | $45,000 |
| Tax basis | 15,000 |
| Cumulative taxable temporary difference | 30,000 |
| Existing Deferred Tax Liability balance ($30,000 × 25%) | **$7,500** |

Canyonridge sells the equipment for **$45,000 cash** (equal to GAAP NBV). Ignore any other temporary differences and ignore income from operations for this part—focus on tax consequences of the sale and the DTL settlement. Assume no other pretax items.

**Part D — Classification / presentation**  
Using Part A Year 1 amounts, state balance-sheet classification and income tax expense note presentation.

**Required:**  
(a) **Part A:** Compute Year 1 ending DTL and record the Year 1 and Year 2 period-end income tax JEs.  
(b) **Part B:** Compute Year 1 ending DTL and record the Year 1 income tax JE.  
(c) **Part C:** Compute the tax gain on sale, the current tax on that gain, and the JE that **settles** the remaining DTL in connection with the disposal (may combine current tax and DTL reverse). Explain why no residual DTL remains.  
(d) **Part D:** Balance-sheet classification and current/deferred note disclosure for Part A Year 1.  
(e) In one sentence each, name the **balance-sheet basis comparison** that creates a DTL for (1) prepaid insurance, (2) installment receivable, and (3) depreciable equipment before disposal.

**Answer key:**

**(a) Part A — prepaid insurance originate and reverse**

**Year 1**  
Cum. taxable temporary difference = $16,000 − $0 = **$16,000**  
DTL = $16,000 × 25% = **$4,000**  
Current tax payable = $240,000 × 25% = **$60,000**  
Deferred tax expense = **$4,000**  
Total income tax expense = $60,000 + $4,000 = **$64,000**  
(Implied pretax GAAP income = TI + originating TTD = $240,000 + $16,000 = $256,000; $256,000 × 25% = $64,000.)

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 64,000 | |
| Deferred Tax Liability | | 4,000 |
| Income Tax Payable | | 60,000 |
| *Year 1: current tax + DTL for prepaid insurance taxable temp. difference* | | |

**Check:** Dr 64,000 = Cr 4,000 + 60,000. **Balanced.**

**Year 2 — full reverse / settlement**  
Cum. TTD at Dec 31 Y2 = **$0** → desired DTL = **$0**  
Deferred tax benefit = $0 − $4,000 = **($4,000)**  
Current tax payable = $256,000 × 25% = **$64,000**  
Total income tax expense = $64,000 − $4,000 = **$60,000**  
(Implied pretax = TI − reversing TTD = $256,000 − $16,000 = $240,000; $240,000 × 25% = $60,000.)

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 60,000 | |
| Deferred Tax Liability | 4,000 | |
| Income Tax Payable | | 64,000 |
| *Year 2: reverse DTL as prepaid is expensed for GAAP; record current tax* | | |

**Check:** Dr 60,000 + 4,000 = Cr 64,000. **Balanced.** Ending DTL = **$0**.

**(b) Part B — installment receivable DTL**

Remaining embedded gross profit = cumulative taxable temporary difference = **$28,000**  
(asset GAAP basis of installment receivable includes profit already recognized for books; tax basis of that profit component is zero until collection).  
DTL = $28,000 × 25% = **$7,000**  
Current tax payable = $200,000 × 25% = **$50,000**  
Total tax expense = $50,000 + $7,000 = **$57,000**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 57,000 | |
| Deferred Tax Liability | | 7,000 |
| Income Tax Payable | | 50,000 |
| *DTL for installment sale gross profit taxable after GAAP recognition* | | |

**Check:** Dr 57,000 = Cr 7,000 + 50,000. **Balanced.**

**(c) Part C — disposal settles remaining DTL**

| | Amount |
|---|---:|
| Cash proceeds | $45,000 |
| GAAP NBV | 45,000 |
| **GAAP gain** | **$0** |
| Tax basis | 15,000 |
| **Taxable gain on sale** | **$30,000** |
| Current tax on taxable gain ($30,000 × 25%) | **$7,500** |
| Existing DTL related to the asset | **$7,500** |
| Desired DTL after disposal (asset gone; TTD = 0) | **$0** |

The $30,000 tax gain **is** the reversing cumulative taxable temporary difference. After disposal, future taxable amounts from this asset no longer exist, so the DTL is fully reversed.

Tax effects of the sale (standalone):
- Current tax on taxable gain: $30,000 × 25% = **$7,500** → increases Income Tax Payable  
- Reverse remaining DTL: **$7,500** → deferred tax **benefit**  
- Total income tax expense related to the sale = $7,500 current − $7,500 deferred benefit = **$0**, which matches pretax GAAP gain of $0 × 25%

**July 1, Year 3 — tax effects of disposal (settlement of DTL):**

| Account | Debit | Credit |
|---|---:|---:|
| Deferred Tax Liability | 7,500 | |
| Income Tax Payable | | 7,500 |
| *Reverse DTL on disposed asset; record current tax payable on $30,000 tax gain; net tax expense $0 given zero GAAP gain* | | |

**Check:** Dr 7,500 = Cr 7,500. **Balanced.** Ending DTL related to asset = **$0**.

**Why no residual DTL:** After sale, both GAAP and tax bases of the asset are gone; cumulative temporary difference is **zero**. The previously deferred tax has become **currently payable** via the taxable gain.

**(d) Part D — classification / presentation (Part A Year 1)**

**Balance sheet Dec 31, Year 1**

| | Amount |
|---|---:|
| Current liabilities — Income tax payable | $60,000 |
| Noncurrent liabilities — Deferred tax liability | $4,000 |

(DTLs are classified as **noncurrent** under current GAAP.)

**Income tax expense note — Year 1**

| | Amount |
|---|---:|
| Current | $60,000 |
| Deferred | 4,000 |
| **Total** | **$64,000** |

**(e) Balance-sheet signals**

1. **Prepaid insurance:** prepaid asset **GAAP basis > tax basis** (often tax basis = $0).  
2. **Installment receivable:** receivable **GAAP basis > tax basis** (profit recognized for books, deferred for tax).  
3. **Depreciable equipment:** net fixed asset **GAAP basis > tax basis** (accelerated or bonus tax depreciation).

**Key insight:** Every classic DTL story is the same measurement: identify the **cumulative taxable temporary difference** from basis differences, multiply by the **enacted rate**, and adjust the DTL account at each period end—or when the related asset is **disposed** and the difference settles into current taxable income.

---

### Q4 — MC — Classification of deferred tax liability and income tax expense components
**LO:** LO 18-2  
**Concept:** Balance-sheet classification of DTL (noncurrent) and composition of total income tax expense (current + deferred)  
**Question:**  
At December 31, Year 1, **Harborcrest Components Inc.** has a deferred tax liability of **$9,000** arising solely from accelerated tax depreciation on equipment that will reverse over the next several years, and income tax payable of **$52,000**. Total income tax expense for Year 1 is **$61,000**. Which presentation is correct under current U.S. GAAP (ASC 740)?

- A) Report Deferred Tax Liability **$9,000** as a **current** liability; disclose income tax expense only as a single line with no current/deferred split required in the notes.  
- B) Report Deferred Tax Liability **$9,000** as a **noncurrent** liability; Income Tax Payable **$52,000** as current; and disclose income tax expense as **current $52,000** and **deferred $9,000**.  
- C) Net Income Tax Payable and Deferred Tax Liability and report a single **current** liability of **$61,000**.  
- D) Report Deferred Tax Liability **$9,000** in **equity** because it relates to future taxes, not present legal obligations.

**Answer:** **B.**  
Under ASC 740, deferred tax liabilities (and assets) are classified as **noncurrent**. Income tax payable for taxes on the current return is a **current** liability. Companies disclose the **current** and **deferred** components of income tax expense (here $52,000 + $9,000 = $61,000). DTLs are not equity, and they are not netted with income tax payable into one current liability for presentation of the originating temporary difference.

---

### Q5 — MC — Which fact pattern creates a deferred tax liability
**LO:** LO 18-2  
**Concept:** Identify which situation creates a taxable temporary difference and therefore a deferred tax liability  
**Question:**  
Which of the following originating differences creates a **deferred tax liability**?

- A) Warranty expense accrued for GAAP; deductible for tax only when paid (tax basis of accrued warranty = $0; GAAP liability exists).  
- B) Revenue deferred for GAAP (performance obligation remaining); cash already included in taxable income when collected.  
- C) Equipment cost fully deducted for tax in Year 1 (bonus depreciation) but depreciated over five years for GAAP.  
- D) Municipal bond interest included in pretax GAAP income but permanently nontaxable.

**Answer:** **C.**  
Bonus tax depreciation reduces the **tax basis** of equipment below the **GAAP basis** → taxable temporary difference → **DTL**.  
A and B create **deductible** temporary differences (deferred tax **assets**). D is a **permanent** difference (no DTA/DTL).

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (cum TTD schedules roll to zero; pretax × rate = current + deferred)
- [x] Core demo path (taxable temp. differences → DTL), not Expanding Your Knowledge sidebars
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (emphasis), period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
- [x] Original companies/numbers (not textbook Roberts/Staples; not agent_027 Cedar Peak $80k pattern)
