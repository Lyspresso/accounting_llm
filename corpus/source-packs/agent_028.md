# Agent 28 — CORE DEMO — LO 18-3

**Chapter:** 18  
**LO title:** Recognize deferred tax assets attributable to deductible temporary differences  
**Critical gap LO:** yes

## Concept list for this pack
- Deductible temporary difference: future deductible amounts (GAAP asset < tax asset, or GAAP liability > tax liability)
- Deferred tax asset = cumulative deductible temporary difference × enacted tax rate
- Initial recognition JE: Dr Deferred Tax Asset, Cr reduces Income Tax Expense (with current tax payable)
- Subsequent measurement schedule of cumulative temporary difference and DTA balance by year
- Period-end adjusting tax JE when the DTA balance changes (originates or reverses)
- Full reversal / “settlement” of DTA when the temporary difference is fully eliminated
- Balance-sheet classification: deferred tax assets reported as **noncurrent**; note disclosure of current vs deferred tax expense
- Common sources of DTA: warranties, deferred revenue (taxed up front), allowance for doubtful accounts
- Number-variant twin with all amounts recomputed

---

### Q1 — CORE — Warranty deductible temporary difference: initial DTA recognition, multi-year schedule, full reversal
**LO:** LO 18-3  
**Concept:** Initial recognition of deferred tax asset from warranty accrual; subsequent DTA schedule; period-end tax JEs; settlement when liability is paid  
**Scenario:** **Forge & Field Tools Inc.** sells equipment with a multi-year warranty. There are **zero** beginning balances in deferred tax accounts on January 1 of Year 1. The enacted tax rate is **25%** for all years. Accounting and tax years both end December 31. No permanent differences and no other temporary differences.

In **Year 1**, Forge & Field accrues warranty expense of **$60,000** for financial reporting (GAAP warranty liability ending balance **$60,000**; tax basis of the liability **$0**). Warranty costs are deductible for tax **only when paid**. Cash payments that settle the warranty liability occur as follows:

| Year paid | Amount settled |
|---|---:|
| Year 2 | $20,000 |
| Year 3 | $25,000 |
| Year 4 | $15,000 |

Taxable income (from the tax return) is:

| Year | Taxable income |
|---|---:|
| Year 1 | $400,000 |
| Year 2 | $360,000 |
| Year 3 | $350,000 |
| Year 4 | $370,000 |

**Required:**  
(a) Identify why the warranty creates a **deductible** temporary difference and compute the cumulative deductible temporary difference and required **Deferred Tax Asset** balance at each December 31 (Years 1–4). Prepare a roll-forward **schedule**.  
(b) Record the **December 31, Year 1** income tax journal entry (emphasize initial recognition of the DTA).  
(c) Record the **December 31, Year 2** and **December 31, Year 3** period-end tax adjusting entries.  
(d) Record the **December 31, Year 4** entry that fully eliminates the DTA (settlement / maturity of the temporary difference).  
(e) Show Year 1 **balance sheet** classification of the deferred tax asset and Income Tax Payable, and the Year 1 **note disclosure** of current and deferred tax expense.  
(f) Briefly reconcile pretax GAAP income to total income tax expense for Year 1 (show that total tax expense = pretax GAAP income × 25%).

**Answer key:**

**(a) Why deductible; DTA schedule**

Warranty expense is recognized for **GAAP when sales occur**, but is deductible for **tax only when paid**. At year-end, **GAAP liability basis ($60,000 initially) > tax liability basis ($0)** → future deductible amounts when the liability is settled → **deductible temporary difference** → **deferred tax asset**.

Cumulative deductible temporary difference = ending GAAP warranty liability (tax basis always $0 here).

| Dec. 31 | Ending warranty liability (cumulative deductible TD) | Tax rate | Required DTA balance | Change in DTA |
|---|---:|---:|---:|---:|
| Year 1 | $60,000 | 25% | **$15,000** | +$15,000 (originate) |
| Year 2 | $40,000 | 25% | **$10,000** | −$5,000 |
| Year 3 | $15,000 | 25% | **$3,750** | −$6,250 |
| Year 4 | $0 | 25% | **$0** | −$3,750 (full reverse) |

Formula: \(\text{Deferred tax asset} = \text{Cumulative deductible temporary difference} \times \text{enacted tax rate}\).

**(b) December 31, Year 1 — initial recognition (emphasis)**

Current tax on tax return: \(400{,}000 \times 0.25 = \mathbf{\$100{,}000}\).  
Increase DTA to required $15,000 (from $0).

```
Dr Income Tax Expense .............................. 85,000
Dr Deferred Tax Asset .............................. 15,000
   Cr Income Tax Payable ...................................... 100,000
```
(Dr = Cr = $100,000)

Check: Total income tax expense $85,000 = current $100,000 − deferred benefit $15,000.

**(c) Period-end adjusting entries — Years 2 and 3**

**December 31, Year 2**  
Income Tax Payable: \(360{,}000 \times 0.25 = \$90{,}000\).  
DTA required $10,000 vs beginning $15,000 → decrease DTA $5,000 (increases deferred tax expense).

```
Dr Income Tax Expense .............................. 95,000
   Cr Deferred Tax Asset ........................................ 5,000
   Cr Income Tax Payable ....................................... 90,000
```
(Dr = Cr = $95,000)

**December 31, Year 3**  
Income Tax Payable: \(350{,}000 \times 0.25 = \$87{,}500\).  
DTA required $3,750 vs beginning $10,000 → decrease DTA $6,250.

```
Dr Income Tax Expense .............................. 93,750
   Cr Deferred Tax Asset ........................................ 6,250
   Cr Income Tax Payable ....................................... 87,500
```
(Dr = Cr = $93,750)

**(d) December 31, Year 4 — full settlement of temporary difference**

Warranty liability and cumulative deductible TD = $0 → required DTA = $0.  
Income Tax Payable: \(370{,}000 \times 0.25 = \$92{,}500\).  
Clear remaining DTA of $3,750.

```
Dr Income Tax Expense .............................. 96,250
   Cr Deferred Tax Asset ........................................ 3,750
   Cr Income Tax Payable ....................................... 92,500
```
(Dr = Cr = $96,250)

**(e) Year 1 financial statement presentation**

**Balance sheet (Dec. 31, Year 1 excerpt):**  
- **Noncurrent assets** — Deferred tax asset: **$15,000** (DTAs are classified noncurrent under current GAAP)  
- **Current liabilities** — Income tax payable: **$100,000**

**Income statement (Year 1):** Income tax expense **$85,000**

**Notes — components of income tax expense (Year 1):**

| Component | Amount |
|---|---:|
| Current | $100,000 |
| Deferred | (15,000) |
| **Total income tax expense** | **$85,000** |

**(f) Pretax GAAP ↔ tax expense check (Year 1)**  
Only temporary difference: warranty accrual $60,000 (GAAP expense not yet tax-deductible) →  
Taxable income $400,000 = pretax GAAP income + $60,000 → pretax GAAP income = **$340,000**.  
\(340{,}000 \times 25\% = \mathbf{\$85{,}000}\) = total income tax expense. ✓

**Key insight:** A deductible temporary difference creates a **future tax benefit** measured as cumulative deductible TD × enacted rate. An **increase** in the DTA reduces total income tax expense; as the difference **reverses** (warranty paid), the DTA is reduced and deferred tax expense increases. When the cumulative difference reaches zero, the DTA is fully eliminated.

---

### Q2 — CORE number variant — Deferred subscription revenue DTA (all numbers changed)
**LO:** LO 18-3  
**Concept:** Deductible temporary difference from revenue taxed before GAAP recognition; multi-year DTA schedule and JEs (number-variant twin)  
**Scenario:** On **January 1 of Year 1**, **Cedarline Media Inc.** collects **$240,000** cash from customers for multi-year subscriptions and records **deferred revenue** for GAAP. For **tax** purposes, the entire **$240,000** is included in taxable income in Year 1 (taxed on cash receipt). Cedarline recognizes the $240,000 as **GAAP revenue evenly** over Year 1 through Year 4 (**$60,000** per year). Enacted tax rate is **30%** each year. Deferred tax account balances are zero at the beginning of Year 1. No other temporary or permanent differences.

Pretax **GAAP** income (already includes the $60,000 subscription revenue recognized each year):

| Year | Pretax GAAP income |
|---|---:|
| Year 1 | $180,000 |
| Year 2 | $200,000 |
| Year 3 | $195,000 |
| Year 4 | $190,000 |

**Required:**  
(a) For each year-end Years 1–4, compute: ending deferred revenue (cumulative deductible TD), required DTA, taxable income, current tax payable, change in DTA, and total income tax expense. Present as a **schedule**.  
(b) Record the income tax journal entry for **Year 1** (initial DTA recognition) and **Year 2** (subsequent decrease).  
(c) Record the **Year 4** entry that settles the DTA to zero.  
(d) State how the DTA is classified on the balance sheet at December 31 of Year 1.

**Answer key:**

**(a) Multi-year schedule**

Ending deferred revenue (GAAP liability basis; tax basis $0) = cumulative deductible temporary difference.

| Year | Ending deferred revenue (cum. deductible TD) | Required DTA (×30%) | Pretax GAAP | Taxable income | Income tax payable (×30%) | Δ DTA | Total tax expense |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | $180,000 | $54,000 | $180,000 | $360,000 | $108,000 | +$54,000 | $54,000 |
| 2 | $120,000 | $36,000 | $200,000 | $140,000 | $42,000 | −$18,000 | $60,000 |
| 3 | $60,000 | $18,000 | $195,000 | $135,000 | $40,500 | −$18,000 | $58,500 |
| 4 | $0 | $0 | $190,000 | $130,000 | $39,000 | −$18,000 | $57,000 |

Taxable income checks:  
- Y1: pretax GAAP $180,000 + unearned portion taxed up front $180,000 = **$360,000**  
- Y2–Y4: pretax GAAP − $60,000 GAAP revenue already taxed in Year 1 = **$140,000 / $135,000 / $130,000**

Total tax expense each year equals pretax GAAP × 30% (only temporary differences).

**(b) Journal entries — Years 1 and 2**

**December 31, Year 1 — initial recognition**
```
Dr Income Tax Expense .............................. 54,000
Dr Deferred Tax Asset .............................. 54,000
   Cr Income Tax Payable ...................................... 108,000
```
(Dr = Cr = $108,000)

**December 31, Year 2 — subsequent measurement**
```
Dr Income Tax Expense .............................. 60,000
   Cr Deferred Tax Asset ....................................... 18,000
   Cr Income Tax Payable ....................................... 42,000
```
(Dr = Cr = $60,000)

**(c) December 31, Year 4 — full reversal / settlement**
```
Dr Income Tax Expense .............................. 57,000
   Cr Deferred Tax Asset ....................................... 18,000
   Cr Income Tax Payable ....................................... 39,000
```
(Dr = Cr = $57,000)

**(d) Classification**  
Deferred tax asset of **$54,000** is reported as a **noncurrent** asset on the December 31, Year 1 balance sheet.

**Key insight:** When cash advances are **taxable before** they are recognized as GAAP revenue, the remaining deferred revenue is a **deductible temporary difference** (GAAP liability > tax basis). The DTA equals that remaining balance × the enacted rate and declines as performance obligations are satisfied for GAAP.

---

### Q3 — CORE alternate angle — Allowance for doubtful accounts: period-end DTA adjustment and full write-off settlement; presentation
**LO:** LO 18-3  
**Concept:** DTA from allowance for doubtful accounts (GAAP asset basis < tax basis); period-end adjusting tax JEs; settlement when receivables are written off; classification/disclosure  
**Scenario:** **Summit Ridge Outdoor Co.** estimates uncollectible accounts for GAAP using an allowance method. For **tax**, bad debts are deductible **only when specific accounts are written off** (direct write-off). Enacted tax rate is **21%** for all years. Beginning deferred tax balances on January 1 of Year 1 are zero. No other temporary or permanent differences.

| Year | Pretax GAAP income | Bad debt expense (GAAP) | Write-offs (tax deductible) | Ending allowance for doubtful accounts |
|---|---:|---:|---:|---:|
| Year 1 | $500,000 | $25,000 | $0 | $25,000 |
| Year 2 | $480,000 | $8,000 | $10,000 | $23,000 |
| Year 3 | $450,000 | $5,000 | $28,000 | $0 |

(The Year 3 write-offs clear the remaining allowance; ending net AR for tax and GAAP no longer differ due to this item.)

**Required:**  
(a) Explain why the allowance creates a deductible temporary difference (basis comparison).  
(b) For each year, compute taxable income, required DTA, and record the **December 31 income tax journal entry**.  
(c) On the December 31, Year 2 balance sheet, classify the DTA and state the amount.  
(d) Prepare the Year 2 note disclosure of current vs deferred tax expense.

**Answer key:**

**(a) Basis analysis**  
GAAP carrying amount of AR **net of allowance** is **less than** tax basis of AR (tax has no allowance). GAAP asset basis < tax asset basis → future deductible amounts when write-offs occur for tax → **deductible temporary difference** equal to the **allowance balance** → **deferred tax asset**.

**(b) Computations and journal entries**

Taxable income = pretax GAAP income + bad debt expense − write-offs  
DTA = ending allowance × 21%

| Year | Taxable income | ITP (×21%) | Ending allowance | Required DTA | Δ DTA | Total ITE |
|---|---:|---:|---:|---:|---:|---:|
| 1 | $525,000 | $110,250 | $25,000 | $5,250 | +$5,250 | $105,000 |
| 2 | $478,000 | $100,380 | $23,000 | $4,830 | −$420 | $100,800 |
| 3 | $427,000 | $89,670 | $0 | $0 | −$4,830 | $94,500 |

Checks: total ITE = pretax GAAP × 21% each year ($105,000; $100,800; $94,500).

**December 31, Year 1 — initial recognition**
```
Dr Income Tax Expense ............................. 105,000
Dr Deferred Tax Asset ............................... 5,250
   Cr Income Tax Payable ...................................... 110,250
```
(Dr = Cr = $110,250)

**December 31, Year 2 — period-end adjusting**
```
Dr Income Tax Expense ............................. 100,800
   Cr Deferred Tax Asset .......................................... 420
   Cr Income Tax Payable ...................................... 100,380
```
(Dr = Cr = $100,800)

**December 31, Year 3 — settlement (temporary difference fully reversed)**
```
Dr Income Tax Expense .............................. 94,500
   Cr Deferred Tax Asset ........................................ 4,830
   Cr Income Tax Payable ....................................... 89,670
```
(Dr = Cr = $94,500)

**(c) Classification at Dec. 31, Year 2**  
Deferred tax asset **$4,830** — reported as **noncurrent** asset.

**(d) Year 2 tax expense disclosure**

| Component | Amount |
|---|---:|
| Current tax expense | $100,380 |
| Deferred tax expense | 420 |
| **Total income tax expense** | **$100,800** |

**Key insight:** The DTA tracks the **remaining** deductible temporary difference (here, the allowance). Write-offs reverse the difference for tax; the period-end tax entry always sets the DTA to (ending cumulative deductible TD × enacted rate), not to the year’s write-offs alone.

---

### Q4 — MC — Balance-sheet classification of deferred tax assets
**LO:** LO 18-3  
**Concept:** Classification / presentation of deferred tax assets  
**Question:** Under current U.S. GAAP (ASC 740), how should a deferred tax asset arising solely from a deductible temporary difference (e.g., warranty liability) be classified on the classified balance sheet?

- A) Always current, because income taxes are settled annually  
- B) Always noncurrent  
- C) Split current/noncurrent based on when the temporary difference is expected to reverse  
- D) Net only against income tax payable; never shown as an asset  

**Answer:** **B.** Current GAAP requires deferred tax assets and deferred tax liabilities to be classified as **noncurrent**. (Older rules that split based on reversal timing no longer apply.)

---

### Q5 — MC — Which item creates a deferred tax asset?
**LO:** LO 18-3  
**Concept:** Identifying deductible temporary differences that create DTAs  
**Question:** Which of the following items, existing at year-end, creates a **deferred tax asset** (assuming a positive enacted tax rate and no valuation allowance issues)?

- A) Tax depreciation in excess of GAAP depreciation to date (tax basis of PPE lower than GAAP basis)  
- B) Prepaid rent deducted for tax when paid, still prepaid for GAAP  
- C) Product warranty liability recognized for GAAP; not yet deductible for tax  
- D) Municipal bond interest recognized in pretax GAAP income  

**Answer:** **C.** A warranty liability has GAAP basis > tax basis (tax basis typically $0 until paid) → future deductible amounts → DTA.  
A creates a **taxable** temporary difference (DTL). B also tends to create a taxable temporary difference (asset GAAP basis > tax basis). D is a **permanent** difference (never creates DTA/DTL).

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (DTA = cum. deductible TD × rate; ITE ties to pretax GAAP × rate)
- [x] Core demo path (Demo 18-3 style: deductible TD → DTA; not valuation-allowance sidebar / not LO 18-7 carryforwards)
- [x] LO + Concept on every item
- [x] MC ≤ 2
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE (full reverse), classification_presentation_or_disclosure, number_variant_twin
