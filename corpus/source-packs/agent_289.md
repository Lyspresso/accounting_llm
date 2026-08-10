# Agent 289 — CORE DEMO — LO 18-2

**Chapter:** 18  
**LO title:** Recognize deferred tax liabilities attributable to taxable temporary differences  
**Critical gap LO:** yes  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **Taxable temporary difference:** future taxable amounts when revenues are taxable after pretax GAAP income, or expenses are deductible for tax before pretax GAAP income
- **Balance-sheet signal:** **asset GAAP basis > asset tax basis** (common) → deferred tax liability (DTL)
- **Measurement:** **DTL = cumulative taxable temporary difference × enacted tax rate** (rate expected when the difference reverses)
- **Initial recognition JE:** Dr Income Tax Expense; Cr Deferred Tax Liability (originating); Cr Income Tax Payable
- **Current vs deferred tax expense:** current = taxable income × rate; deferred tax expense (benefit) = increase (decrease) in DTL
- **Subsequent measurement schedule:** multi-year rollforward of GAAP NBV, tax NBV, cumulative TTD, ending DTL, and Δ DTL each year
- **Period-end adjusting JE (emphasis):** set DTL to **desired ending balance** (ending − beginning = deferred tax expense or benefit); combine with current tax payable in one year-end income tax entry
- **Settlement / reverse:** when cumulative TTD returns to zero (full depreciation life, prepaid expires, or disposal of the related asset), reverse remaining DTL
- **Classification / presentation / disclosure:** DTL reported as **noncurrent**; note disclosure of current and deferred components of income tax expense
- **Number-variant twin:** same LO 18-2 path with all amounts changed

---

### Q1 — CORE — Multi-year accelerated tax depreciation: period-end DTL adjusting JEs (emphasis)

**LO:** LO 18-2  
**Concept:** Initial recognition of DTL from taxable temporary difference; subsequent measurement schedule; multi-year period-end tax adjusting JEs (emphasis); full reverse/settlement of DTL; noncurrent presentation and current vs deferred disclosure  
**Scenario:**  
On **January 1, Year 1**, **Harborline Plastics LLC** (calendar year) places specialized molding equipment in service:

| Item | Detail |
|------|--------|
| Cost | **$96,000** (zero residual for both GAAP and tax) |
| GAAP depreciation | Straight-line over **4 years** → **$24,000** per year |
| Tax depreciation | Y1 **$40,000**; Y2 **$28,000**; Y3 **$18,000**; Y4 **$10,000** |
| Enacted tax rate (all years) | **25%** (flat; no rate change expected) |
| Beginning deferred tax balances | **$0** |
| Only temporary difference | Depreciable equipment book–tax basis difference |
| Accounting and tax year-ends | December 31 |

Pretax **GAAP** income (after GAAP depreciation; no permanent differences):

| Year | Pretax GAAP income |
|------|-------------------:|
| 1 | $240,000 |
| 2 | $255,000 |
| 3 | $250,000 |
| 4 | $245,000 |

**Required:**  
(a) Explain why the depreciation difference is a **taxable** temporary difference. Compute **Year 1** taxable income and income tax payable.  
(b) Compute the **Year 1 ending DTL** and record the **December 31, Year 1 period-end adjusting JE** that **initially recognizes** the DTL and current tax.  
(c) Prepare a **subsequent measurement schedule** for December 31 of Years 1–4 showing: GAAP NBV, tax NBV, cumulative taxable temporary difference, ending DTL, and deferred tax expense/(benefit) for the year.  
(d) Record the **period-end tax adjusting JEs** for Years 2–4. Show that every JE balances and that Year 4 **settles** the DTL to zero.  
(e) For Year 1 only, show **balance-sheet** classification of Income Tax Payable and Deferred Tax Liability, and the **note** split of current vs deferred tax expense.  
(f) Briefly state what “settlement” of the DTL means when the temporary difference fully reverses by end of Year 4.

**Answer key:**

**(a) Why taxable temporary difference; Year 1 taxable income and payable**

Tax depreciation exceeds GAAP depreciation in early years → tax basis of the asset falls faster than GAAP basis → **asset GAAP basis > asset tax basis**. Future recovery of the higher GAAP carrying amount (with little or no remaining tax basis) will produce **future taxable amounts** relative to pretax GAAP income. That is a **taxable temporary difference** → **deferred tax liability**.

| | Amount |
|---|---:|
| Pretax GAAP income, Year 1 | $240,000 |
| Less: excess of tax dep over GAAP dep ($40,000 − $24,000) | (16,000) |
| **Taxable income, Year 1** | **$224,000** |
| × 25% | |
| **Income tax payable (current tax), Year 1** | **$56,000** |

**(b) Year 1 ending DTL and period-end initial recognition JE (emphasis)**

| | Amount |
|---|---:|
| GAAP NBV Dec 31 Y1 ($96,000 − $24,000) | $72,000 |
| Tax NBV Dec 31 Y1 ($96,000 − $40,000) | 56,000 |
| **Cumulative taxable temporary difference** | **$16,000** |
| × 25% | |
| **Deferred tax liability, Dec 31 Y1** | **$4,000** |

Deferred tax expense (increase in DTL) = $4,000 − $0 = **$4,000**.  
Total income tax expense = current $56,000 + deferred $4,000 = **$60,000**  
(check: pretax GAAP × 25% = $240,000 × 25% = $60,000).

**December 31, Year 1 — period-end adjusting JE (initial recognition of DTL):**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 60,000 | |
| Deferred Tax Liability | | 4,000 |
| Income Tax Payable | | 56,000 |
| *Record current tax and establish DTL for taxable temporary difference* | | |

**Check:** Dr 60,000 = Cr 4,000 + 56,000. **Balanced.**

**(c) Subsequent measurement schedule — Years 1–4**

| Dec 31 | GAAP NBV | Tax NBV | Cum. taxable temp. diff. | Rate | **DTL balance** | Δ DTL = deferred tax exp/(ben) |
|--------:|---------:|--------:|-------------------------:|-----:|---------------:|-------------------------------:|
| Y1 | 72,000 | 56,000 | 16,000 | 25% | **4,000** | 4,000 |
| Y2 | 48,000 | 28,000 | 20,000 | 25% | **5,000** | 1,000 |
| Y3 | 24,000 | 10,000 | 14,000 | 25% | **3,500** | (1,500) |
| Y4 | 0 | 0 | 0 | 25% | **0** | (3,500) |

Supporting depreciation each year:

| Year | GAAP dep | Tax dep | Originating/(reversing) TTD |
|-----:|---------:|--------:|----------------------------:|
| 1 | 24,000 | 40,000 | +16,000 |
| 2 | 24,000 | 28,000 | +4,000 |
| 3 | 24,000 | 18,000 | (6,000) |
| 4 | 24,000 | 10,000 | (14,000) |
| **Total** | **96,000** | **96,000** | **0** |

**Schedule checks:** total tax and GAAP depreciation both equal cost $96,000; cumulative TTD and DTL return to **zero** at end of Year 4; sum of Δ DTL = 4,000 + 1,000 − 1,500 − 3,500 = **0**. Originating years: Y1–Y2. Reversing years: Y3–Y4.

**(d) Period-end tax adjusting JEs — Years 2–4 (emphasis)**

**Year 2**  
TI = $255,000 − $4,000 = **$251,000**; payable = $251,000 × 25% = **$62,750**  
Desired ending DTL = $5,000; beginning DTL = $4,000; deferred tax expense = **$1,000**  
Total tax expense = $62,750 + $1,000 = **$63,750** (= $255,000 × 25%).

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 63,750 | |
| Deferred Tax Liability | | 1,000 |
| Income Tax Payable | | 62,750 |
| *Period-end: true-up DTL to ending balance; record current tax* | | |

**Check:** Dr 63,750 = Cr 1,000 + 62,750. **Balanced.**

**Year 3**  
TI = $250,000 + $6,000 = **$256,000**; payable = $256,000 × 25% = **$64,000**  
Desired ending DTL = $3,500; beginning DTL = $5,000; deferred tax **benefit** = **$1,500**  
Total tax expense = $64,000 − $1,500 = **$62,500** (= $250,000 × 25%).

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 62,500 | |
| Deferred Tax Liability | 1,500 | |
| Income Tax Payable | | 64,000 |
| *Period-end: reverse portion of DTL as TTD begins to reverse* | | |

**Check:** Dr 62,500 + 1,500 = 64,000 = Cr 64,000. **Balanced.**

**Year 4 (full settlement of DTL)**  
TI = $245,000 + $14,000 = **$259,000**; payable = $259,000 × 25% = **$64,750**  
Desired ending DTL = $0; beginning DTL = $3,500; deferred tax **benefit** = **$3,500**  
Total tax expense = $64,750 − $3,500 = **$61,250** (= $245,000 × 25%).

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 61,250 | |
| Deferred Tax Liability | 3,500 | |
| Income Tax Payable | | 64,750 |
| *Period-end: settle remaining DTL as cumulative TTD returns to zero* | | |

**Check:** Dr 61,250 + 3,500 = 64,750 = Cr 64,750. **Balanced.**  
DTL balance after Year 4 entry = **$0**.

**(e) Year 1 financial statement presentation**

**Balance Sheet (excerpt) — Dec 31, Year 1**

| Liabilities | Amount |
|---|---:|
| **Current liabilities** | |
| Income tax payable | $56,000 |
| **Noncurrent liabilities** | |
| Deferred tax liability | $4,000 |

**Income Statement (excerpt) — Year 1**  
Income tax expense …………………… **$60,000**

**Financial statement notes — Income tax expense**

| Component | Amount |
|---|---:|
| Current | $56,000 |
| Deferred | 4,000 |
| **Total** | **$60,000** |

**(f) Settlement meaning**  
“Settlement” of the DTL means the cumulative taxable temporary difference has fully reversed (GAAP and tax bases both zero; all excess early tax depreciation has been “caught up” by higher later taxable income). The period-end adjusting JE **debits Deferred Tax Liability** down to a **zero ending balance**; the related future tax obligation has been realized through higher current taxes in reversing years.

**Key insight:** At each **period-end**, measure **desired ending DTL** = cumulative TTD × enacted rate, then record the **adjusting JE** for (ending − beginning). Originating years **credit** DTL (deferred tax expense); reversing years **debit** DTL (deferred tax benefit). Total income tax expense still equals pretax GAAP × rate when the only difference is temporary.

---

### Q2 — CORE number variant — 100% bonus depreciation → multi-year DTL lifecycle

**LO:** LO 18-2  
**Concept:** Number-variant twin—DTL from taxable temporary difference under 100% tax expensing; subsequent measurement schedule; period-end adjusting JEs; full reverse settlement; noncurrent presentation  
**Scenario:**  
On **January 1, Year 1**, **Summit Ridge Logistics Inc.** (calendar year) places delivery-fleet equipment in service:

| Item | Detail |
|------|--------|
| Cost | **$48,000** (zero residual for both GAAP and tax) |
| GAAP depreciation | Straight-line over **3 years** → **$16,000** per year |
| Tax depreciation | **100% immediate expensing** in Year 1 ($48,000); $0 in Years 2–3 |
| Enacted tax rate (all years) | **25%** |
| Beginning deferred tax balances | **$0** |
| Only temporary difference | Depreciable equipment book–tax basis difference |

Pretax **GAAP** income (after GAAP depreciation; no permanent differences):

| Year | Pretax GAAP income |
|------|-------------------:|
| 1 | $160,000 |
| 2 | $170,000 |
| 3 | $165,000 |

**Required:**  
(a) Compute Year 1 taxable income, income tax payable, ending DTL, and the **December 31, Year 1 period-end tax JE**.  
(b) Prepare a **DTL measurement schedule** for December 31 of Years 1–3.  
(c) Record the **period-end tax adjusting JEs** for Years 2 and 3 (show full settlement in Year 3).  
(d) Show Year 1 balance-sheet classification and note disclosure of current vs deferred tax expense.

**Answer key:**

**(a) Year 1 computations and period-end JE**

| | Amount |
|---|---:|
| Pretax GAAP income | $160,000 |
| Less: excess of tax dep over GAAP dep ($48,000 − $16,000) | (32,000) |
| **Taxable income** | **$128,000** |
| **Income tax payable** ($128,000 × 25%) | **$32,000** |
| GAAP NBV Dec 31 Y1 ($48,000 − $16,000) | $32,000 |
| Tax NBV Dec 31 Y1 ($48,000 − $48,000) | 0 |
| **Cumulative TTD** | **$32,000** |
| **DTL** ($32,000 × 25%) | **$8,000** |
| Total income tax expense ($32,000 + $8,000) | **$40,000** |
| Check: $160,000 × 25% | $40,000 |

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 40,000 | |
| Deferred Tax Liability | | 8,000 |
| Income Tax Payable | | 32,000 |
| *Period-end: initial recognition of DTL under 100% tax expensing* | | |

**Check:** Dr 40,000 = Cr 8,000 + 32,000. **Balanced.**

**(b) Subsequent measurement schedule — Years 1–3**

| Dec 31 | GAAP NBV | Tax NBV | Cum. TTD | Rate | **DTL** | Δ DTL exp/(ben) |
|--------:|---------:|--------:|---------:|-----:|--------:|----------------:|
| Y1 | 32,000 | 0 | 32,000 | 25% | **8,000** | 8,000 |
| Y2 | 16,000 | 0 | 16,000 | 25% | **4,000** | (4,000) |
| Y3 | 0 | 0 | 0 | 25% | **0** | (4,000) |

| Year | GAAP dep | Tax dep | Originating/(reversing) TTD |
|-----:|---------:|--------:|----------------------------:|
| 1 | 16,000 | 48,000 | +32,000 |
| 2 | 16,000 | 0 | (16,000) |
| 3 | 16,000 | 0 | (16,000) |
| **Total** | **48,000** | **48,000** | **0** |

Originating: Year 1 only. Reversing: Years 2–3 (GAAP depreciation continues with zero remaining tax basis). Sum of Δ DTL = 8,000 − 4,000 − 4,000 = **0**.

**(c) Period-end JEs — Years 2 and 3**

**Year 2**  
TI = $170,000 + $16,000 = **$186,000**; payable = **$46,500**  
Ending DTL = $4,000; beginning $8,000; deferred tax benefit = **$4,000**  
Tax expense = $46,500 − $4,000 = **$42,500** (= $170,000 × 25%).

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 42,500 | |
| Deferred Tax Liability | 4,000 | |
| Income Tax Payable | | 46,500 |

**Check:** Dr 42,500 + 4,000 = 46,500. **Balanced.**

**Year 3 (full settlement)**  
TI = $165,000 + $16,000 = **$181,000**; payable = **$45,250**  
Ending DTL = $0; beginning $4,000; deferred tax benefit = **$4,000**  
Tax expense = $45,250 − $4,000 = **$41,250** (= $165,000 × 25%).

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 41,250 | |
| Deferred Tax Liability | 4,000 | |
| Income Tax Payable | | 45,250 |

**Check:** Dr 41,250 + 4,000 = 45,250. **Balanced.** DTL = **$0**.

**(d) Year 1 presentation**

**Balance sheet — Dec 31, Year 1**  
Current liabilities: Income tax payable ………… **$32,000**  
Noncurrent liabilities: Deferred tax liability … **$8,000**

**Note — Income tax expense, Year 1**  
Current $32,000 + Deferred $8,000 = **$40,000**

**Key insight:** 100% bonus depreciation creates a large **originating** taxable temporary difference in Year 1 (asset GAAP basis ≫ tax basis of zero). Subsequent years reverse the DTL through **period-end adjusting JEs** as GAAP depreciation continues with no tax basis left.

---

### Q3 — CORE alternate angle — Prepaid origin/reverse (period-end emphasis), PPE disposal settlement, classification

**LO:** LO 18-2  
**Concept:** Period-end adjusting JE for prepaid-expense taxable temporary difference and full reverse; multi-year equipment DTL with mid-life disposal settlement; noncurrent classification and current/deferred disclosure  
**Scenario:**  
**Pinecrest Outdoor Gear Inc.** (calendar year; enacted tax rate **25%** for all years; no permanent differences) has the following independent situations related to **taxable temporary differences** and **deferred tax liabilities**.

---

**Situation A — Prepaid insurance: period-end origin then reverse**  
At **December 31, Year 1**, Prepaid Insurance has a **GAAP basis of $20,000** and a **tax basis of $0** (premium paid and fully deducted for tax in Year 1; amortized for GAAP in Year 2). Taxable income for Year 1 is **$220,000**. Beginning deferred tax balances are **$0**.  
In **Year 2**, the prepaid fully amortizes for GAAP (and remains $0 for tax). Taxable income for Year 2 is **$240,000**. No other temporary differences exist in Years 1–2.

**Situation B — Equipment DTL then disposal settlement**  
On **January 1, Year 1**, Pinecrest places equipment costing **$40,000** in service (zero residual). GAAP: straight-line over **4 years** (**$10,000**/year). Tax: **100% expensed in Year 1**. Pretax GAAP income (after GAAP depreciation): Year 1 **$200,000**; Year 2 **$210,000**. No other temporary differences.  
On **January 1, Year 3**, Pinecrest **sells** the equipment for **$20,000** cash (equal to Year-2 ending GAAP NBV; **zero book gain/loss**). Tax basis at sale is **$0**. Pretax GAAP income for Year 3 (excluding any sale effects already reflected) is **$100,000**. No other temporary differences remain after the sale.

**Required:**  
(a) **Situation A, Year 1:** Compute ending DTL and record the **period-end income tax JE**. Show BS classification and note split of tax expense.  
(b) **Situation A, Year 2:** Record the **period-end JE** that **settles** the prepaid-related DTL.  
(c) **Situation B:** Prepare a schedule of cumulative TTD and DTL at Dec 31 Year 1 and Year 2; record both years’ **period-end tax JEs**.  
(d) **Situation B, Year 3 disposal:** Compute taxable income, explain settlement of the remaining DTL, and record the **period-end tax JE** for Year 3.  
(e) In one sentence, state the **balance-sheet classification** rule for deferred tax liabilities under current GAAP (ASC 740).

**Answer key:**

**(a) Situation A — Year 1 period-end origin (emphasis)**

Cumulative taxable temporary difference = GAAP prepaid − tax basis = $20,000 − $0 = **$20,000**  
DTL = $20,000 × 25% = **$5,000**  
Current tax = $220,000 × 25% = **$55,000**  
Total tax expense = $55,000 + $5,000 = **$60,000**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 60,000 | |
| Deferred Tax Liability | | 5,000 |
| Income Tax Payable | | 55,000 |
| *Period-end: DTL for prepaid (GAAP asset > tax basis)* | | |

**Check:** Dr 60,000 = Cr 5,000 + 55,000. **Balanced.**

**Balance sheet Dec 31, Year 1:** Income tax payable **current** $55,000; Deferred tax liability **noncurrent** $5,000.  
**Note:** Current tax expense $55,000; deferred tax expense $5,000; total $60,000.

**(b) Situation A — Year 2 period-end reverse/settlement**

Ending cumulative TTD = $0 (prepaid fully amortized for GAAP).  
Desired ending DTL = $0; beginning DTL = $5,000; deferred tax **benefit** = **$5,000**.  
Current tax = $240,000 × 25% = **$60,000**.  
Total tax expense = $60,000 − $5,000 = **$55,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 55,000 | |
| Deferred Tax Liability | 5,000 | |
| Income Tax Payable | | 60,000 |
| *Period-end: reverse DTL as prepaid temporary difference fully reverses* | | |

**Check:** Dr 55,000 + 5,000 = 60,000. **Balanced.**

**(c) Situation B — Years 1–2 schedule and period-end JEs**

| Dec 31 | GAAP NBV | Tax NBV | Cum. TTD | **DTL** | Δ DTL |
|--------:|---------:|--------:|---------:|--------:|------:|
| Y1 | 30,000 | 0 | 30,000 | **7,500** | 7,500 |
| Y2 | 20,000 | 0 | 20,000 | **5,000** | (2,500) |

**Year 1**  
TI = $200,000 − ($40,000 − $10,000) = $200,000 − $30,000 = **$170,000**  
Payable = $170,000 × 25% = **$42,500**  
Tax expense = $42,500 + $7,500 = **$50,000** (= $200,000 × 25%).

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 50,000 | |
| Deferred Tax Liability | | 7,500 |
| Income Tax Payable | | 42,500 |

**Check:** Dr 50,000 = Cr 7,500 + 42,500. **Balanced.**

**Year 2**  
TI = $210,000 + $10,000 = **$220,000** (GAAP dep continues; tax dep already zero)  
Payable = $220,000 × 25% = **$55,000**  
Deferred tax benefit = $7,500 − $5,000 = **$2,500**  
Tax expense = $55,000 − $2,500 = **$52,500** (= $210,000 × 25%).

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 52,500 | |
| Deferred Tax Liability | 2,500 | |
| Income Tax Payable | | 55,000 |

**Check:** Dr 52,500 + 2,500 = 55,000. **Balanced.**

**(d) Situation B — Year 3 disposal settles remaining DTL**

Sale proceeds $20,000; GAAP NBV $20,000 → **book gain $0**.  
Tax basis $0 → **taxable gain $20,000**.  
Taxable income = pretax GAAP $100,000 + tax-only gain $20,000 = **$120,000**.  
Payable = $120,000 × 25% = **$30,000**.  
Remaining cum. TTD at sale = GAAP NBV − tax NBV = $20,000 − $0 = $20,000; after sale both bases are gone → ending TTD **$0**, ending DTL **$0**.  
Beginning DTL $5,000; deferred tax **benefit** $5,000.  
Tax expense = $30,000 − $5,000 = **$25,000** (= $100,000 × 25%).

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 25,000 | |
| Deferred Tax Liability | 5,000 | |
| Income Tax Payable | | 30,000 |
| *Period-end: settle remaining DTL when asset disposal eliminates taxable temporary difference* | | |

**Check:** Dr 25,000 + 5,000 = 30,000. **Balanced.**  
(Optional sale JE for completeness—not a tax entry: Dr Cash 20,000; Cr Equipment (net) 20,000.)

**(e) Classification rule**  
Under ASC 740, deferred tax liabilities (and assets) are classified as **noncurrent** on the balance sheet (offset within the same tax-paying component and jurisdiction).

**Key insight:** Whether the TTD comes from **prepaid expenses**, **accelerated tax depreciation**, or is **cleared by disposal**, the **period-end adjusting JE** always targets the **desired ending DTL** (cum. TTD × enacted rate). Settlement is simply driving ending DTL to zero when the temporary difference disappears.

---

### Q4 — MC — Balance-sheet classification and composition of tax expense

**LO:** LO 18-2  
**Concept:** Balance-sheet classification of DTL (noncurrent) and composition of total income tax expense (current + deferred)  
**Question:**  
At December 31, Year 1, **Lakewood Ceramics Co.** has Income Tax Payable of $48,000 and a Deferred Tax Liability of $6,000 arising solely from a taxable temporary difference (asset GAAP basis > tax basis). The enacted rate is 25%. How should Lakewood report these amounts, and what is the correct description of total income tax expense for Year 1 if deferred tax expense equals the increase in the DTL?

- A) Report both Income Tax Payable and Deferred Tax Liability as current liabilities; total income tax expense equals only current tax of $48,000.  
- B) Report Income Tax Payable as a current liability and Deferred Tax Liability as a **noncurrent** liability; total income tax expense equals current tax $48,000 **plus** deferred tax expense $6,000 = **$54,000**.  
- C) Report Deferred Tax Liability as a contra-equity account; total income tax expense equals only deferred tax of $6,000.  
- D) Net Income Tax Payable against Deferred Tax Liability and report a single current liability of $42,000; total expense is $42,000.

**Answer:** **B.**  
Under ASC 740, DTLs are presented as **noncurrent**. Income tax payable is a **current** liability. Total income tax expense = **current tax expense** (taxable income × rate, which equals the payable when no payments on account are considered) **+ deferred tax expense** (increase in DTL). Current and deferred components are disclosed in the notes.

---

### Q5 — MC — Identify taxable temporary difference creating a DTL

**LO:** LO 18-2  
**Concept:** Identify which situation creates a taxable temporary difference and therefore a deferred tax liability  
**Question:**  
Which of the following creates a **taxable temporary difference** that is recognized as a **deferred tax liability**?

- A) Warranty expense accrued for GAAP; deductible for tax only when claims are paid.  
- B) Municipal bond interest included in pretax GAAP income but never taxable.  
- C) Machinery with **GAAP carrying amount $45,000** and **tax basis $28,000** after Year 1 accelerated tax depreciation.  
- D) Customer advances deferred for GAAP but already included in taxable income when cash was collected.

**Answer:** **C.**  
Asset **GAAP basis > tax basis** means future recovery of the book carrying amount will produce **future taxable amounts** → **taxable temporary difference** → **DTL**.  
A and D create **deductible** temporary differences (DTAs). B is a **permanent** difference (no deferred tax).

---

### Self-check
- [x] Every JE balances (Dr = Cr verified for all tax entries)
- [x] Math recomputed (TI, payable, cum TTD, DTL, Δ DTL; pretax × rate = total tax expense when only temporary differences)
- [x] Core demo not sidebar-only (Demo 18-2 / Review 18-2 path: prepaid and depreciable asset taxable temporary differences → DTL)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE (emphasis), disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
