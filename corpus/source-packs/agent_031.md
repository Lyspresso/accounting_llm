# Agent 31 — CORE DEMO — LO 18-6

**Chapter:** 18  
**LO title:** Explain how a change in tax rates impacts deferred taxes  
**Critical gap LO:** yes

## Concept list for this pack
- Deferred tax assets/liabilities measured using **enacted** tax rates for the year(s) temporary differences reverse (not anticipated rates)
- Income-statement effect of a rate change recognized **in the period of enactment** (ASC 740)
- Multi-year phased-in rates matched to scheduled future taxable/deductible amounts
- **Initial recognition JE:** current tax (payable at current statutory rate) + deferred tax (at future enacted rates)
- Rate **decrease** reduces DTA → **increases** income tax expense; rate **decrease** reduces DTL → **decreases** income tax expense
- Subsequent remeasurement of existing DTA/DTL when a new rate is enacted; T-account rollforward
- Settlement/reversal of temporary differences in later years (use then-current rates for current tax; update remaining DTA/DTL)
- Classification/presentation: statutory-to-effective rate reconciliation including rate-change reconciling item

---

### Q1 — CORE — Multi-rate DTL initial recognition, Year-1 tax JE, subsequent reversal schedule, settlement
**LO:** LO 18-6  
**Concept:** Initial recognition of deferred tax liability using phased-in enacted rates matched to years of reversal; period-end tax JE; subsequent reversal and settlement of TTD  
**Scenario:**  
**Cedarcrest Manufacturing Co.** has one temporary difference at December 31, Year 1: the GAAP carrying amount of depreciable equipment exceeds the tax basis by a cumulative taxable temporary difference (TTD) of **$48,000**. The entire difference originated in Year 1. Beginning balances in all deferred tax accounts are **zero**. Accounting and tax years both end December 31.

Future taxable amounts from the TTD reverse as follows:

| Year of reversal | Future taxable amount |
|---:|---:|
| Year 2 | $18,000 |
| Year 3 | $18,000 |
| Year 4 | $12,000 |
| **Total** | **$48,000** |

**Enacted tax rates** (signed into law before December 31, Year 1):

| Period | Enacted rate |
|---|---:|
| Year 1 (current) | **30%** |
| Year 2 | **25%** |
| Year 3 | **25%** |
| Year 4 | **20%** |

Year 1 **taxable income** is **$200,000**. Pretax GAAP income equals taxable income plus the originating TTD (no permanent differences).

**Year 2 additional facts (settlement of first tranche):**  
- The **$18,000** Year 2 portion of the cumulative TTD **reverses** in Year 2; remaining cumulative TTD at Dec 31, Year 2 is **$30,000** ($18,000 Y3 + $12,000 Y4).  
- Year 2 **taxable income** is **$150,000**.  
- Pretax GAAP income Year 2 is **$132,000** (when a TTD reverses, taxable income exceeds pretax GAAP by the reversing amount: \(150{,}000 - 18{,}000 = 132{,}000\)).  
- Enacted rates for remaining years are **unchanged** (Y3 still 25%, Y4 still 20%). Year 2 statutory rate for current tax is **25%**.

**Required:**  
a. Prepare the **schedule to compute the deferred tax liability** balance at December 31, Year 1 (match each year’s future taxable amount to the enacted rate for that year).  
b. Compute Year 1 **income tax payable**, **deferred tax expense**, and **total income tax expense**. Prepare the **December 31, Year 1** income tax journal entry (**initial recognition** of the DTL).  
c. Prepare a **subsequent measurement schedule** showing DTL at Dec 31 Y1, the Year 2 reversal, and ending DTL at Dec 31 Y2.  
d. Prepare the **December 31, Year 2** income tax journal entry (current tax + adjustment of DTL for the reversed tranche).  
e. Briefly state balance-sheet classification of the remaining DTL components at Dec 31, Year 2 (current vs noncurrent is not required under ASC 740 noncurrent presentation, but identify which remaining years the liability relates to).

**Answer key:**  

**a. Schedule — Deferred Tax Liability at Dec 31, Year 1**

| Year of reversal | Future taxable amount | Enacted rate | Deferred tax liability |
|---:|---:|---:|---:|
| Year 2 | 18,000 | 25% | **4,500** |
| Year 3 | 18,000 | 25% | **4,500** |
| Year 4 | 12,000 | 20% | **2,400** |
| **Total** | **48,000** | | **$11,400** |

**Check:** \(18{,}000\times0.25 + 18{,}000\times0.25 + 12{,}000\times0.20 = 4{,}500 + 4{,}500 + 2{,}400 = 11{,}400\).

Do **not** measure the entire $48,000 at the Year 1 rate of 30% (\(48{,}000\times0.30 = 14{,}400\)) — multi-year **enacted** rates in the years of reversal control.

**b. Year 1 amounts and initial recognition JE**

- Income tax payable (current tax): \(200{,}000 \times 30\% = \mathbf{\$60{,}000}\)  
- Deferred tax expense (increase in DTL): \(\mathbf{\$11{,}400}\)  
- Total income tax expense: \(60{,}000 + 11{,}400 = \mathbf{\$71{,}400}\)  
- Pretax GAAP income check: \(200{,}000 + 48{,}000 = \mathbf{\$248{,}000}\)

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 71,400 | |
| Deferred Tax Liability | | 11,400 |
| Income Tax Payable | | 60,000 |
| *To record current tax at 30% and DTL at multi-year enacted rates for years of reversal* | | |

**Check:** Dr 71,400 = Cr 11,400 + 60,000. Balanced.

**c. Subsequent DTL measurement schedule**

| Date / event | Cumulative TTD | Computation of DTL | DTL balance |
|---|---:|---|---:|
| Dec 31, Y1 (after initial recognition) | 48,000 | 4,500 + 4,500 + 2,400 | **11,400** |
| Year 2: reverse Y2 tranche | (18,000) | Release Y2 layer: \(18{,}000 \times 25\% = 4{,}500\) | |
| Dec 31, Y2 (after reversal; rates unchanged) | 30,000 | \(18{,}000\times25\% + 12{,}000\times20\% = 4{,}500 + 2{,}400\) | **6,900** |

T-account:

| Deferred Tax Liability | | |
|---|---:|---:|
| | Beg. Y1 | 0 |
| | Y1 originating | 11,400 |
| Y2 reverse | 4,500 | |
| | End Y2 | **6,900** |

**d. December 31, Year 2 — period-end tax JE (settlement of reversed layer + current tax)**

- Income tax payable: \(150{,}000 \times 25\% = \mathbf{\$37{,}500}\)  
- Decrease in DTL (benefit): \(\mathbf{\$4{,}500}\)  
- Income tax expense: \(37{,}500 - 4{,}500 = \mathbf{\$33{,}000}\)  
- Cross-check vs pretax: pretax GAAP \(132{,}000 \times 25\% = 33{,}000\) (remaining layers still measured at their enacted rates; no new rate change in Y2).

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 33,000 | |
| Deferred Tax Liability | 4,500 | |
| Income Tax Payable | | 37,500 |
| *Current tax at Year 2 enacted 25%; settle/release DTL for reversed $18,000 × 25%* | | |

**Check:** Dr 33,000 + 4,500 = Cr 37,500. Balanced.

**e. Presentation / remaining layers**  
Remaining DTL of **$6,900** relates to future taxable amounts in Year 3 ($4,500) and Year 4 ($2,400). Under ASC 740, deferred tax liabilities are generally classified as **noncurrent**. Disclose the nature of the temporary difference (depreciable basis difference) and that measurement uses enacted rates in the years of expected reversal.

**Key insight:** Match **each year’s** future taxable amount to the **enacted rate for that year**. Rate changes (or multi-rate phase-ins) affect the DTL balance and flow through **income tax expense in the period rates are enacted / applied at measurement date**—not when management merely anticipates a future law change.

---

### Q2 — CORE number variant — Multi-rate DTL twin + rate-change remeasurement mid-life
**LO:** LO 18-6  
**Concept:** Number-variant twin — multi-rate DTL initial recognition; later enactment reduces rates and remeasures existing DTL  
**Scenario:**  
**Ironbridge Fabricators Inc.** originates a taxable temporary difference of **$90,000** in Year 1 solely from excess of GAAP carrying amount of plant assets over tax basis. Beginning deferred tax balances are zero. Year 1 taxable income is **$360,000**. No permanent differences.

Scheduled reversals and **rates enacted as of Dec 31, Year 1**:

| Year of reversal | Future taxable amount | Enacted rate (as of 12/31/Y1) |
|---:|---:|---:|
| Year 2 | $40,000 | **28%** |
| Year 3 | $30,000 | **28%** |
| Year 4 | $20,000 | **24%** |
| **Total** | **$90,000** | |

Year 1 current statutory rate for taxes payable: **28%**.

**During Year 2** (on **December 15, Year 2**, before year-end closing), a new tax law is **enacted** that sets:

| Period | Newly enacted rate |
|---|---:|
| Year 2 (current year for Y2 return) | remains **28%** (no change for Y2) |
| Year 3 and thereafter | **21%** (replaces prior 28% for Y3 and 24% for Y4) |

Year 2 facts:  
- The **$40,000** Year 2 tranche of the TTD **reverses** during Year 2.  
- Year 2 taxable income: **$275,000**.  
- Remaining cumulative TTD at Dec 31, Year 2 (after reversal): **$50,000** (all reverses equally: **$30,000** in Y3 and **$20,000** in Y4).  
- The rate change is recognized at **date of enactment** (measured at Dec 31, Year 2 year-end tax entry for this problem).

**Required:**  
a. Compute Dec 31, Year 1 DTL schedule and prepare the Year 1 income tax journal entry.  
b. Compute the DTL **immediately before** the Year 2 rate-change remeasurement (after reflecting the Y2 $40,000 reverse at the old rates for remaining years).  
c. Remeasure the remaining $50,000 TTD at the **new** enacted rates; compute the rate-change adjustment.  
d. Prepare the **combined** December 31, Year 2 income tax journal entry (current tax + reverse of settled layer + rate-change remeasurement). Show a T-account for Deferred Tax Liability for Years 1–2.

**Answer key:**  

**a. Year 1 — multi-rate DTL and initial JE**

| Year | Taxable amount | Rate | DTL |
|---:|---:|---:|---:|
| 2 | 40,000 | 28% | 11,200 |
| 3 | 30,000 | 28% | 8,400 |
| 4 | 20,000 | 24% | 4,800 |
| **Total** | **90,000** | | **$24,400** |

Current tax: \(360{,}000 \times 28\% = \mathbf{\$100{,}800}\)  
Tax expense: \(100{,}800 + 24{,}400 = \mathbf{\$125{,}200}\)

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 125,200 | |
| Deferred Tax Liability | | 24,400 |
| Income Tax Payable | | 100,800 |

**Check:** Dr 125,200 = Cr 24,400 + 100,800. Balanced.

**b. After Y2 reverse, before rate remeasurement**  
Release Y2 layer: \(40{,}000 \times 28\% = \mathbf{\$11{,}200}\)  
DTL before remeasurement: \(24{,}400 - 11{,}200 = \mathbf{\$13{,}200}\)  
(Components still on old rates: \(30{,}000\times28\% + 20{,}000\times24\% = 8{,}400 + 4{,}800 = 13{,}200\).)

**c. Remeasurement at newly enacted 21% for Y3 and Y4**  
Required ending DTL: \(50{,}000 \times 21\% = \mathbf{\$10{,}500}\)  
(Alternatively by year: \(30{,}000\times21\% + 20{,}000\times21\% = 6{,}300 + 4{,}200 = 10{,}500\).)  
Rate-change **decrease** in DTL: \(13{,}200 - 10{,}500 = \mathbf{\$2{,}700}\) (debit DTL, credit/reduce tax expense).

**d. Year 2 combined JE**

- Income tax payable: \(275{,}000 \times 28\% = \mathbf{\$77{,}000}\)  
- Total DTL reduction for the year: reverse layer \(11{,}200\) + rate change \(2{,}700\) = \(\mathbf{\$13{,}900}\)  
- Income tax expense: \(77{,}000 - 13{,}900 = \mathbf{\$63{,}100}\)

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 63,100 | |
| Deferred Tax Liability | 13,900 | |
| Income Tax Payable | | 77,000 |
| *Current tax 28%; settle Y2 layer $11,200; remeasure remaining DTL for rate cut to 21% ($2,700)* | | |

**Check:** Dr 63,100 + 13,900 = Cr 77,000. Balanced.

**Deferred Tax Liability T-account**

| | Debit | Credit |
|---|---:|---:|
| Beg. Y1 | | 0 |
| Y1 originating (multi-rate) | | 24,400 |
| Y2 reverse of $40,000 layer | 11,200 | |
| Y2 rate-change remeasurement | 2,700 | |
| **End Y2** | | **10,500** |

**Key insight:** When enacted rates fall, an existing **DTL is written down**, producing a **tax benefit** (lower tax expense) in the **enactment period**—even though cash taxes this year may be unchanged by the future-rate cut. Settlement of a reversing layer uses the rate that was embedded in that layer; remaining layers are remeasured when law changes.

---

### Q3 — CORE — Existing DTA rate decrease, adjusting JE, warranty settlement, rate reconciliation
**LO:** LO 18-6  
**Concept:** Rate-change impact on an existing deferred tax asset; period-end adjusting JE; settlement when deductible difference reverses; statutory-to-effective rate reconciliation  
**Scenario:**  
**Lakeshore Retail Group** accrues a litigation/warranty liability for GAAP purposes. At **December 31, Year 1**, before considering a year-end tax law change:

- Cumulative **deductible temporary difference (DTD):** **$80,000** (GAAP warranty liability $80,000; tax basis $0).  
- The entire DTD is expected to reverse in **Year 2** when claims are paid and become tax-deductible.  
- Deferred Tax Asset was recorded earlier in Year 1 at the then-expected rate of **40%**: balance **$32,000** (\(80{,}000 \times 40\%\)).  
- Year 1 taxable income: **$220,000**.  
- Year 1 pretax **GAAP** income: **$140,000** (taxable income $220,000 − originating DTD $80,000).  
- Year 1 current statutory rate used for taxes payable: **40%**.

On **December 31, Year 1**, a new tax rate of **25%** is **enacted**, effective for Year 2 and thereafter.

**Year 2 (settlement):**  
- Warranty claims of **$80,000** are paid in cash and are fully deductible on the Year 2 tax return (DTD fully reverses).  
- Year 2 taxable income: **$100,000**.  
- Year 2 pretax GAAP income: **$180,000** (taxable $100,000 + reversing DTD $80,000).  
- Statutory rate Year 2: **25%**. No other temporary or permanent differences. Beginning DTA after Year 1 closing equals the remeasured amount from Year 1.

**Required:**  
a. Prepare the schedule of the **remeasured** deferred tax asset at December 31, Year 1 after the enacted rate change.  
b. Prepare the **December 31, Year 1** income tax journal entry (current tax + adjustment of DTA for the rate decrease). Use a single combined entry. Also show the **DTA T-account** for Year 1.  
c. Prepare a **statutory-to-effective tax rate reconciliation** for Year 1 (dollars and percentages of pretax GAAP income).  
d. Prepare the **December 31, Year 2** income tax journal entry when the warranty DTD fully settles/reverses.  
e. Explain in one or two sentences the **income-statement presentation** effect of the Year 1 rate change (and contrast with what would have happened if Lakeshore had held a net DTL instead).

**Answer key:**  

**a. Remeasured DTA at Dec 31, Year 1**

| Item | Amount |
|---|---:|
| GAAP warranty liability | $80,000 |
| Tax basis | 0 |
| Deductible temporary difference | $80,000 |
| Enacted rate in year of reversal (Year 2) | × 25% |
| **Deferred tax asset, ending** | **$20,000** |

Required adjustment: existing DTA $32,000 − target $20,000 = **$12,000 credit** to DTA (write-down).

**b. December 31, Year 1 — period-end tax JEs**

- Income tax payable: \(220{,}000 \times 40\% = \mathbf{\$88{,}000}\)  
- Background (already on books before the law change): DTA **$32,000** at 40% with current tax recorded so YTD tax expense = \(88{,}000 - 32{,}000 = \mathbf{\$56{,}000}\).

**(1) Entry already on books (originating DTA at 40% + current tax)** — given as background:

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 56,000 | |
| Deferred Tax Asset | 32,000 | |
| Income Tax Payable | | 88,000 |

**Check:** 56,000 + 32,000 = 88,000.

**(2) Period-end adjusting JE for enacted rate change (required):**

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 12,000 | |
| Deferred Tax Asset | | 12,000 |
| *Remeasure DTA: $80,000 × (40% − 25%) = $12,000; rate cut reduces DTA and increases tax expense* | | |

**Check:** Dr = Cr = 12,000.  
**Ending DTA = $20,000.** **Total Year 1 tax expense = $68,000** (\(56{,}000 + 12{,}000\)).

**DTA T-account Year 1**

| | Debit | Credit |
|---|---:|---:|
| Originating at 40% | 32,000 | |
| Rate-change remeasurement | | 12,000 |
| **End Y1** | **20,000** | |

**c. Statutory-to-effective rate reconciliation — Year 1**

| | Dollars | Percent of pretax GAAP |
|---|---:|---:|
| Tax at statutory rate (\(140{,}000 \times 40\%\)) | 56,000 | 40.00% |
| Effect of deductible temporary difference reversing at lower enacted rate \(80{,}000 \times (40\% - 25\%)\) | 12,000 | 8.57% |
| **Income tax expense / effective rate** | **68,000** | **48.57%** |

**Check:** \(68{,}000 / 140{,}000 = 48.571\% \approx 48.57\%\).  
Effective rate **exceeds** statutory because the future deduction will save tax at only 25%, not 40%.

**d. Year 2 — settlement / full reverse of DTD**

When warranty is paid: tax deduction of $80,000 occurs; DTA is realized (no longer needed).

- Income tax payable: \(100{,}000 \times 25\% = \mathbf{\$25{,}000}\)  
- Reverse remaining DTA: \(\mathbf{\$20{,}000}\)  
- Income tax expense: \(25{,}000 + 20{,}000 = \mathbf{\$45{,}000}\)

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 45,000 | |
| Deferred Tax Asset | | 20,000 |
| Income Tax Payable | | 25,000 |
| *Current tax; reverse DTA as warranty DTD settles/reverses in full* | | |

**Check:** Dr 45,000 = Cr 20,000 + 25,000. Balanced.  
**Check pretax:** \(180{,}000 \times 25\% = 45{,}000\) effective tax expense — matches (no remaining rate mismatch).

**e. Presentation contrast**  
A rate **decrease** that revalues a **net DTA** **increases** income tax expense (asset devaluation), raising the effective tax rate—as in Year 1 for Lakeshore. The **same** rate decrease revaluing a **net DTL** **decreases** income tax expense (liability reduction), lowering the effective tax rate. Effects appear in **continuing operations** tax expense in the **enactment period**.

**Key insight:** Enacted-rate cuts hurt companies with large deferred tax **assets** and help companies with large deferred tax **liabilities**. Always remeasure at enactment date; never wait until the temporary difference reverses to recognize the rate effect.

---

### Q4 — MC — Classification of rate-change effects on deferred taxes
**LO:** LO 18-6  
**Concept:** Classification of income-statement effect when enacted rates change for DTA vs DTL  
**Question 1:**  
On December 31, Year 1, **Pinehurst Logistics** has a single deferred tax **asset** of $50,000 measured at 30%. On that date a new law is enacted reducing the rate to 21% for all future years (when the related deductible temporary difference will reverse). No valuation allowance is needed. The immediate effect of remeasurement is:

- A) Debit Deferred Tax Asset; credit Income Tax Expense  
- B) Credit Deferred Tax Asset; debit Income Tax Expense  
- C) Debit Deferred Tax Liability; credit Income Tax Expense  
- D) No entry until the temporary difference reverses  

**Answer:** **B.** A rate decrease reduces the DTA (\(50{,}000 \times (30\%-21\%)/30\%\) reduction in the account balance, or remeasure underlying DTD × new rate). Credit DTA and debit Income Tax Expense in the **period of enactment**. No entry is delayed until reversal (eliminates A, D). There is no DTL in this fact pattern (eliminates C).

**Question 2:**  
Same date, **Summit Ore Co.** has only a deferred tax **liability** measured at the old 30% rate; the enacted future rate falls to 21%. Remeasurement:

- A) Increases income tax expense and increases the effective tax rate  
- B) Decreases income tax expense and decreases the effective tax rate  
- C) Has no effect on income tax expense because rates apply only to current taxable income  
- D) Is recorded in OCI, not net income  

**Answer:** **B.** Writing down a DTL (debit DTL, credit/reduce tax expense) **decreases** tax expense and the effective tax rate in the enactment period. Rate-change effects on deferred taxes run through **net income** (continuing operations tax expense), not OCI, under the core ASC 740 model for ordinary temporary differences (eliminates D). Current taxable income is not the only driver of tax expense (eliminates C). The opposite of A.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (multi-rate schedules, rate-change deltas, rate reconciliations)
- [x] Core demo not sidebar-only (Demo 18-6 path: multi-rate DTL, DTA rate cut, DTL rate cut, rate reconciliation; sidebars on ratios excluded)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification MCs)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE (reversal/settlement of temp. differences), classification_presentation_or_disclosure, number_variant_twin
