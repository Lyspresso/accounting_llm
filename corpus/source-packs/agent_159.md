# Agent 159 — CORE DEMO — LO 18-3

**Chapter:** 18  
**LO title:** Recognize deferred tax assets attributable to deductible temporary differences  
**Critical gap LO:** yes  
**Emphasis:** subsequent_measurement_schedule

## Concept list for this pack
- Deductible temporary difference → future deductible amounts when the difference reverses
- Creation rule: GAAP asset basis < tax asset basis, **or** GAAP liability basis > tax liability basis
- Measurement: **Deferred tax asset = cumulative deductible temporary difference × enacted tax rate**
- Initial recognition JE: Dr Deferred Tax Asset (with Dr Income Tax Expense / Cr Income Tax Payable for current tax)
- **Subsequent measurement schedule:** roll-forward of cumulative deductible TD and required DTA each year-end
- Period-end adjusting tax JE sets the DTA to the **required ending balance** (originate or reverse)
- Settlement / full reversal JE when cumulative deductible TD returns to zero
- Presentation: DTA reported as **noncurrent**; note disclosure of current vs deferred tax expense
- Common DTA sources: deferred revenue taxed up front, warranties, allowance for doubtful accounts, inventory LCNRV, FV-NI unrealized losses
- Number-variant twin with fully recomputed amounts

---

### Q1 — CORE — Deferred service-contract revenue: multi-year DTA schedule (emphasis), initial JE, reverse to zero
**LO:** LO 18-3  
**Concept:** Subsequent measurement schedule of DTA from deferred revenue taxed before GAAP recognition; initial recognition, period-end adjusting, and full settlement JEs; noncurrent presentation  
**Scenario:** On **January 1 of Year 1**, **Redrock Trail Outfitters Corp.** collects **$200,000** cash for multi-year service contracts and records **deferred revenue** under GAAP. For **tax** purposes, the entire **$200,000** is included in taxable income in **Year 1** (taxed on cash receipt). Redrock recognizes the $200,000 as **GAAP revenue evenly** over Years 1–4 (**$50,000** per year). The enacted tax rate is **25%** each year. Deferred tax account balances are **zero** at the beginning of Year 1. Accounting and tax years both end December 31. No other temporary or permanent differences.

Pretax **GAAP** income already includes the $50,000 of contract revenue recognized each year:

| Year | Pretax GAAP income |
|---|---:|
| Year 1 | $220,000 |
| Year 2 | $240,000 |
| Year 3 | $230,000 |
| Year 4 | $235,000 |

**Required:**  
(a) Explain why the deferred revenue creates a **deductible** temporary difference (basis comparison).  
(b) Prepare a **subsequent measurement schedule** for Dec. 31 of Years 1–4 showing: ending deferred revenue (cumulative deductible TD), required DTA balance, taxable income, income tax payable, change in DTA, and total income tax expense.  
(c) Record the **December 31, Year 1** income tax journal entry (**initial recognition** of the DTA).  
(d) Record the **December 31, Year 2** and **December 31, Year 3** period-end tax adjusting entries.  
(e) Record the **December 31, Year 4** entry that fully eliminates the DTA (**settlement** of the temporary difference).  
(f) Show Year 1 balance-sheet **classification** of the DTA and Income Tax Payable, and the Year 1 **note disclosure** of current vs deferred tax expense.

**Answer key:**

**(a) Why deductible**  
Cash advances are **taxable when collected** but **deferred for GAAP** until performance. At each year-end while the liability remains, **GAAP liability basis > tax liability basis** (tax basis of deferred revenue is typically $0 because the amount was already taxed). Future periods recognize GAAP revenue without a corresponding taxable amount → **future deductible amounts** → **deductible temporary difference** → **deferred tax asset**.

**(b) Subsequent measurement schedule (emphasis)**

Ending deferred revenue = unearned remaining balance = cumulative deductible temporary difference (tax basis $0).

| Dec. 31 | Ending deferred revenue (cum. deductible TD) | Required DTA (×25%) | Pretax GAAP | Taxable income | Income tax payable (×25%) | Δ DTA | Total income tax expense |
|---|---:|---:|---:|---:|---:|---:|---:|
| Year 1 | $150,000 | **$37,500** | $220,000 | $370,000 | $92,500 | **+$37,500** | **$55,000** |
| Year 2 | $100,000 | **$25,000** | $240,000 | $190,000 | $47,500 | **−$12,500** | **$60,000** |
| Year 3 | $50,000 | **$12,500** | $230,000 | $180,000 | $45,000 | **−$12,500** | **$57,500** |
| Year 4 | $0 | **$0** | $235,000 | $185,000 | $46,250 | **−$12,500** | **$58,750** |

Taxable income checks:  
- Year 1: pretax GAAP $220,000 + amount taxed before GAAP recognition still unearned $150,000 = **$370,000** (equivalently: pretax + $200,000 cash taxed − $50,000 GAAP revenue recognized).  
- Years 2–4: pretax GAAP − $50,000 GAAP revenue already taxed in Year 1 = **$190,000 / $180,000 / $185,000**.  

Roll-forward checks:  
- Total pretax GAAP $220k + $240k + $230k + $235k = **$925,000** = total taxable income $370k + $190k + $180k + $185k.  
- Each year, total tax expense = pretax GAAP × 25% (only temporary differences).  
- Formula: \(\text{DTA} = \text{cumulative deductible temporary difference} \times \text{enacted rate}\).

**(c) December 31, Year 1 — initial recognition**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 55,000 | |
| Deferred Tax Asset | 37,500 | |
| Income Tax Payable | | 92,500 |
| **Totals** | **92,500** | **92,500** |

*Check:* Dr = Cr = $92,500. Total tax expense $55,000 = current $92,500 − deferred tax benefit $37,500.

**(d) Period-end adjusting entries — Years 2 and 3**

**December 31, Year 2** (required DTA $25,000 vs beginning $37,500 → decrease $12,500):

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 60,000 | |
| Deferred Tax Asset | | 12,500 |
| Income Tax Payable | | 47,500 |
| **Totals** | **60,000** | **60,000** |

**December 31, Year 3** (required DTA $12,500 vs beginning $25,000 → decrease $12,500):

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 57,500 | |
| Deferred Tax Asset | | 12,500 |
| Income Tax Payable | | 45,000 |
| **Totals** | **57,500** | **57,500** |

**(e) December 31, Year 4 — full settlement (temporary difference eliminated)**

Required DTA = $0; clear remaining DTA of $12,500.

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 58,750 | |
| Deferred Tax Asset | | 12,500 |
| Income Tax Payable | | 46,250 |
| **Totals** | **58,750** | **58,750** |

**(f) Year 1 presentation and disclosure**

**Balance sheet (Dec. 31, Year 1 excerpt):**  
- **Noncurrent assets** — Deferred tax asset: **$37,500** (ASC 740: deferred tax assets/liabilities classified **noncurrent**)  
- **Current liabilities** — Income tax payable: **$92,500**

**Income statement (Year 1):** Income tax expense **$55,000**

**Notes — components of income tax expense (Year 1):**

| Component | Amount |
|---|---:|
| Current | $92,500 |
| Deferred | (37,500) |
| **Total income tax expense** | **$55,000** |

**Key insight:** The **subsequent measurement schedule** is the control document: each year-end the DTA is remeasured to **ending cumulative deductible TD × enacted rate**. Originating differences increase the DTA (deferred tax benefit); reversals decrease the DTA (deferred tax expense). When the contract is fully performed for GAAP, the cumulative difference and the DTA both go to zero.

---

### Q2 — CORE number variant — Warranty liability DTA (all numbers and rate changed)
**LO:** LO 18-3  
**Concept:** Number-variant twin — warranty deductible temporary difference; multi-year DTA schedule and tax JEs under a different enacted rate  
**Scenario:** **Silverpine Kitchenware Co.** sells products with multi-year warranties. Warranty expense is recognized for **GAAP when sales occur**; warranty costs are deductible for **tax only when paid**. Enacted tax rate is **21%** for all years. Deferred tax balances are zero on January 1 of Year 1. No other temporary or permanent differences. Accounting and tax years end December 31.

In **Year 1**, Silverpine accrues warranty expense of **$48,000** (ending GAAP warranty liability **$48,000**; tax basis **$0**). No new warranty accruals occur in later years. Cash settlements of the liability:

| Year paid | Amount settled |
|---|---:|
| Year 2 | $18,000 |
| Year 3 | $16,000 |
| Year 4 | $14,000 |

Pretax **GAAP** income:

| Year | Pretax GAAP income |
|---|---:|
| Year 1 | $320,000 |
| Year 2 | $300,000 |
| Year 3 | $310,000 |
| Year 4 | $290,000 |

**Required:**  
(a) Prepare the **subsequent measurement schedule** of cumulative deductible TD, required DTA, taxable income, income tax payable, Δ DTA, and total tax expense for Years 1–4.  
(b) Record the **Year 1** initial recognition tax JE and the **Year 2** period-end adjusting tax JE.  
(c) Record the **Year 4** settlement entry that brings the DTA to zero.  
(d) State the Year 1 DTA balance-sheet classification and amount.

**Answer key:**

**(a) Subsequent measurement schedule**

Ending warranty liability = cumulative deductible temporary difference (tax basis of liability = $0).

| Dec. 31 | Ending warranty liability (cum. deductible TD) | Required DTA (×21%) | Pretax GAAP | Taxable income | Income tax payable (×21%) | Δ DTA | Total tax expense |
|---|---:|---:|---:|---:|---:|---:|---:|
| Year 1 | $48,000 | **$10,080** | $320,000 | $368,000 | $77,280 | **+$10,080** | **$67,200** |
| Year 2 | $30,000 | **$6,300** | $300,000 | $282,000 | $59,220 | **−$3,780** | **$63,000** |
| Year 3 | $14,000 | **$2,940** | $310,000 | $294,000 | $61,740 | **−$3,360** | **$65,100** |
| Year 4 | $0 | **$0** | $290,000 | $276,000 | $57,960 | **−$2,940** | **$60,900** |

Taxable income:  
- Year 1: pretax GAAP $320,000 + non-deductible (yet) warranty accrual $48,000 = **$368,000**.  
- Years 2–4: pretax GAAP − tax-deductible warranty payments = **$282,000 / $294,000 / $276,000**.  

Checks: total pretax $1,220,000 = total taxable income; each year’s total tax expense = pretax × 21%.

**(b) Journal entries — Years 1 and 2**

**December 31, Year 1 — initial recognition**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 67,200 | |
| Deferred Tax Asset | 10,080 | |
| Income Tax Payable | | 77,280 |
| **Totals** | **77,280** | **77,280** |

**December 31, Year 2 — subsequent decrease in DTA**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 63,000 | |
| Deferred Tax Asset | | 3,780 |
| Income Tax Payable | | 59,220 |
| **Totals** | **63,000** | **63,000** |

**(c) December 31, Year 4 — full reverse / settlement**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 60,900 | |
| Deferred Tax Asset | | 2,940 |
| Income Tax Payable | | 57,960 |
| **Totals** | **60,900** | **60,900** |

**(d) Classification**  
Deferred tax asset of **$10,080** is reported as a **noncurrent** asset on the December 31, Year 1 balance sheet.

**Key insight:** Same measurement engine as Q1 with different facts: warranty creates a deductible temporary difference because **GAAP liability > tax basis**. The schedule, not the annual payment alone, drives the DTA balance and the deferred portion of tax expense.

---

### Q3 — CORE alternate angle — FV-NI unrealized loss: period-end DTA adjustments, sale settlement, disclosure
**LO:** LO 18-3  
**Concept:** DTA from unrealized holding loss on equity securities (FV-NI); GAAP asset basis < tax basis; period-end adjusting JEs; settlement on sale; classification and current/deferred tax expense disclosure  
**Scenario:** **Pinnacle Harbor Marine Co.** holds equity securities classified as **fair value through net income (FV-NI)**. Unrealized holding losses are recognized for **GAAP** each period but are deductible for **tax only when realized on sale**. Enacted tax rate is **25%**. Beginning deferred tax balances on January 1 of Year 1 are zero. No other temporary or permanent differences.

| Year | Pretax GAAP income | Change in cumulative unrealized holding loss (deductible TD) | Ending cumulative unrealized loss (= cum. deductible TD) |
|---|---:|---:|---:|
| Year 1 | $250,000 | +$30,000 (originate) | $30,000 |
| Year 2 | $270,000 | +$10,000 (additional decline) | $40,000 |
| Year 3 | $300,000 | −$40,000 (sold; difference fully reverses) | $0 |

Pretax GAAP already reflects the unrealized losses (Years 1–2) and the Year 3 sale effects for financial reporting. For tax, the loss is recognized only in Year 3 when the investment is sold.

**Required:**  
(a) Explain the basis comparison that creates the deferred tax asset.  
(b) For each year, compute taxable income, required DTA, and record the **December 31 income tax journal entry**.  
(c) At December 31, Year 2, classify the DTA and prepare the Year 2 **note disclosure** of current vs deferred tax expense.  
(d) In one sentence, describe what the Year 3 entry accomplishes regarding settlement of the temporary difference.

**Answer key:**

**(a) Basis analysis**  
Unrealized holding losses reduce the **GAAP carrying amount** of the investment below its **tax basis** (tax still carries original cost until sale). **GAAP asset basis < tax asset basis** → future deductible amounts when the loss is realized for tax → **deductible temporary difference** equal to the **cumulative unrealized loss** → **deferred tax asset**.

**(b) Computations and journal entries**

Taxable income = pretax GAAP income + increase in cumulative unrealized loss − decrease (realization)  
DTA = ending cumulative unrealized loss × 25%

| Year | Taxable income | ITP (×25%) | Ending cum. deductible TD | Required DTA | Δ DTA | Total ITE |
|---|---:|---:|---:|---:|---:|---:|
| 1 | $280,000 | $70,000 | $30,000 | $7,500 | +$7,500 | $62,500 |
| 2 | $280,000 | $70,000 | $40,000 | $10,000 | +$2,500 | $67,500 |
| 3 | $260,000 | $65,000 | $0 | $0 | −$10,000 | $75,000 |

Checks: total pretax $820,000 = total taxable income $280k + $280k + $260k; each year’s ITE = pretax × 25%.

**December 31, Year 1 — initial recognition**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 62,500 | |
| Deferred Tax Asset | 7,500 | |
| Income Tax Payable | | 70,000 |
| **Totals** | **70,000** | **70,000** |

**December 31, Year 2 — period-end adjusting (DTA increases)**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 67,500 | |
| Deferred Tax Asset | 2,500 | |
| Income Tax Payable | | 70,000 |
| **Totals** | **70,000** | **70,000** |

**December 31, Year 3 — settlement on sale (full reverse of DTA)**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 75,000 | |
| Deferred Tax Asset | | 10,000 |
| Income Tax Payable | | 65,000 |
| **Totals** | **75,000** | **75,000** |

**(c) Classification and Year 2 disclosure**

**Balance sheet Dec. 31, Year 2:** Deferred tax asset **$10,000** — **noncurrent** asset.

**Notes — components of income tax expense (Year 2):**

| Component | Amount |
|---|---:|
| Current tax expense | $70,000 |
| Deferred tax benefit | (2,500) |
| **Total income tax expense** | **$67,500** |

**(d) Settlement description**  
Year 3 reduces the DTA to zero because sale realizes the previously recognized GAAP loss for tax, eliminating the cumulative deductible temporary difference.

**Key insight:** The DTA always tracks the **remaining** cumulative deductible temporary difference. Subsequent fair-value declines can **increase** the DTA mid-life; disposal/sale **settles** the difference and reverses the entire remaining DTA in the tax expense entry.

---

### Q4 — MC — Identifying a deductible temporary difference that creates a DTA
**LO:** LO 18-3  
**Concept:** Classification of book-tax differences — which item creates a deferred tax asset  
**Question:** Which of the following year-end situations creates a **deferred tax asset** (assume a positive enacted tax rate and that realization is not an issue)?

- A) Accumulated tax depreciation exceeds accumulated GAAP depreciation, so the tax basis of equipment is lower than the GAAP carrying amount  
- B) Prepaid insurance was deducted in full for tax when paid and remains an asset for GAAP  
- C) A product warranty liability is recognized for GAAP; the related costs have not yet been paid and are not yet deductible for tax  
- D) Interest on municipal bonds is included in pretax GAAP income  

**Answer:** **C.** Warranty liability: GAAP liability basis > tax basis → future deductible amounts when settled → **deductible temporary difference** → **deferred tax asset**.  
A creates a **taxable** temporary difference (deferred tax **liability**). B typically creates a taxable temporary difference (GAAP asset basis > tax basis). D is a **permanent** difference and never creates a DTA or DTL.

---

### Q5 — MC — Balance-sheet classification of deferred tax assets
**LO:** LO 18-3  
**Concept:** Classification / presentation of deferred tax assets under current GAAP  
**Question:** Under current U.S. GAAP (ASC 740), how should a deferred tax asset arising from a deductible temporary difference (for example, deferred revenue taxed up front) be presented on a classified balance sheet?

- A) Always current, because income taxes are settled each year  
- B) Always noncurrent  
- C) Split between current and noncurrent based on expected reversal timing of the temporary difference  
- D) Net only against Income Tax Payable; never shown separately as an asset  

**Answer:** **B.** Current GAAP requires deferred tax assets and deferred tax liabilities to be classified as **noncurrent**. (Former guidance that split current/noncurrent based on reversal timing no longer applies.)

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (DTA = cum. deductible TD × rate; ITE = pretax GAAP × rate when only temporary differences; schedules roll forward)
- [x] Core demo path (Demo 18-3 / Review 18-3 style deductible TD → DTA; not valuation-allowance LO 18-5; not NOL carryforward LO 18-7)
- [x] LO + Concept on every item
- [x] MC ≤ 2
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (emphasis), period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
- [x] Original company names and numbers (not textbook Demo 18-3 Flannery / Review Staples figures)
