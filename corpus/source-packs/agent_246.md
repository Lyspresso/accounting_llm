# Agent 246 — CORE DEMO — LO 20-10

**Chapter:** 20  
**LO title:** Describe accounting for stock appreciation rights  
**Critical gap LO:** no  
**Emphasis angle:** subsequent_measurement_schedule

## Concept list for this pack
- **Stock appreciation rights (SARs):** employee right to compensation equal to the **appreciation** in market price above a **predetermined (base/grant) price**
- **Classification:** **equity** when the **employer** may settle in stock (transfer of assets not required); **liability** when the **employee** can require **cash** (or chooses cash/stock)
- **Equity SARs:** estimate **grant-date fair value**; recognize compensation **straight-line** over the **requisite service period**; credit **Paid-in Capital—SARs**; **no** remeasurement for later stock-price changes
- **Liability SARs:** **remeasure** each period-end; **Total SARs liability** = (year-end FV per unit × # SARs) × **% of service period accrued**; annual expense = **change in liability** (can be **negative**)
- **Subsequent measurement schedule (emphasis):** year-end FV → aggregate compensation → % accrued → cumulative liability → current-period expense
- **Period-end adjusting JE:** Dr Compensation Expense / Cr SARs Liability (or reverse)
- **Settlement / exercise JE:** clear **SARs Liability** or **PIC—SARs** and record **Cash** and/or **Common Stock** (and APIC); cash settlement of equity-classified awards can require additional compensation

---

### Q1 — CORE — Northpeak Dynamics: liability SARs multipath (schedule emphasis, period-end JEs, cash settlement)
**LO:** LO 20-10  
**Concept:** Liability-classified SARs: subsequent measurement schedule (year-end FV × units × % service); period-end adjusting JEs including a reverse year; cash settlement at exercise  
**Scenario:**  
On **January 1, Year 1**, **Northpeak Dynamics** grants **10,000** stock appreciation rights to key executives under a cash-settled plan. For each SAR, the executive receives **cash** equal to the excess of the market price of Northpeak common stock on the exercise date over a **predetermined price of $12**. The **employee** has the right to require cash settlement, so the awards are **liability-classified**.

The rights require continuing employment and may first be exercised on **December 31, Year 4** (four years after grant). The **requisite service period is four years**. Fair values of the SARs **per unit** (and the market price of common stock at exercise) are:

| Date | Fair value per SAR | Notes |
|---|---:|---|
| Dec. 31, Year 1 | $1.20 | |
| Dec. 31, Year 2 | $4.00 | |
| Dec. 31, Year 3 | $2.50 | FV declined |
| Dec. 31, Year 4 | $5.00 | Exercise date |
| Dec. 31, Year 4 market price of stock | $17 | Predetermined base = $12 |

Executives exercise all 10,000 SARs for cash on **December 31, Year 4**. Cash paid = \((\$17 - \$12) \times 10{,}000 = \$50{,}000\).

**Required:**  
(a) Prepare the **subsequent measurement schedule** for Years 1–4: year-end fair value, aggregate compensation, % of service accrued, cumulative SARs liability, and **annual compensation expense**. (**Emphasis.**)  
(b) Record the **December 31 period-end adjusting journal entry** for compensation in each of Years 1–4.  
(c) Record the **settlement journal entry** on December 31, Year 4 when cash is paid.  
(d) Prove that the **liability is zero** after settlement and that cumulative net compensation expense equals cash paid.

**Answer key:**

**(a) Subsequent measurement schedule (liability SARs)**

| Date | Year-end FV per unit (A) | Aggregate compensation (A × 10,000) (B) | % of service accrued (C) | Total SARs liability (B × C) (D) | Annual expense (D − prior D) |
|---|---:|---:|---:|---:|---:|
| Dec. 31, Year 1 | $1.20 | $12,000 | 25% | $3,000 | $3,000 |
| Dec. 31, Year 2 | 4.00 | 40,000 | 50% | 20,000 | 17,000 |
| Dec. 31, Year 3 | 2.50 | 25,000 | 75% | 18,750 | **(1,250)** |
| Dec. 31, Year 4 | 5.00 | 50,000 | 100% | 50,000 | 31,250 |
| **Totals** | | | | | **$50,000** |

**Checks:**  
- Year 1: \(12{,}000 \times 0.25 = 3{,}000\).  
- Year 2: \(40{,}000 \times 0.50 = 20{,}000\); expense \(20{,}000 - 3{,}000 = 17{,}000\).  
- Year 3: \(25{,}000 \times 0.75 = 18{,}750\); expense \(18{,}750 - 20{,}000 = (1{,}250)\).  
- Year 4: \(50{,}000 \times 1.00 = 50{,}000\); expense \(50{,}000 - 18{,}750 = 31{,}250\).  
- Sum of annual expense: \(3{,}000 + 17{,}000 - 1{,}250 + 31{,}250 = \mathbf{\$50{,}000}\).

**(b) Period-end adjusting journal entries**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Dec. 31, Year 1 | Compensation Expense | 3,000 | |
| | SARs Liability | | 3,000 |
| | *Accrue 25% of aggregate FV* | | |
| Dec. 31, Year 2 | Compensation Expense | 17,000 | |
| | SARs Liability | | 17,000 |
| | *Increase liability to $20,000* | | |
| Dec. 31, Year 3 | SARs Liability | 1,250 | |
| | Compensation Expense | | 1,250 |
| | *Reduce liability to $18,750 (FV decline)* | | |
| Dec. 31, Year 4 | Compensation Expense | 31,250 | |
| | SARs Liability | | 31,250 |
| | *Increase liability to $50,000 at full vesting* | | |

Each entry balances (Dr = Cr).

**(c) Settlement JE — December 31, Year 4**

| Account | Debit | Credit |
|---|---:|---:|
| SARs Liability | 50,000 | |
| Cash | | 50,000 |
| *Cash settlement: ($17 − $12) × 10,000* | | |

**Check:** Dr 50,000 = Cr 50,000. **Balanced.**

**(d) Proof**

| Item | Amount |
|---|---:|
| Cumulative liability immediately before settlement | $50,000 |
| Cash paid | 50,000 |
| Liability after settlement | $0 |
| Cumulative net compensation expense (Y1–Y4) | $50,000 |

**Key insight:** For **cash-settled (liability) SARs**, compensation is **remeasured every period**. The schedule multiplies **current aggregate fair value** by the **cumulative service percentage**; the **change** in that liability is the period’s expense (or expense reduction). At exercise, the liability equals the cash settlement and is cleared against Cash.

---

### Q2 — CORE number variant — Cascade River Foods: liability SARs (3-year schedule + settlement)
**LO:** LO 20-10  
**Concept:** Number-variant twin: liability SARs subsequent measurement schedule; period-end adjusting JEs; cash settlement at exercise  
**Scenario:**  
On **January 1, Year 1**, **Cascade River Foods Inc.** grants **4,000** SARs to its COO. The employee may redeem each SAR for **cash** equal to the excess of the market price of Cascade common over a **predetermined price of $25**. Because the **employee** can require cash, the SARs are **liability-classified**.

The SARs vest and may first be exercised on **December 31, Year 3**. The **requisite service period is three years**. Year-end fair values per SAR and the exercise-date market price:

| Date | Fair value per SAR |
|---|---:|
| Dec. 31, Year 1 | $3.00 |
| Dec. 31, Year 2 | $7.50 |
| Dec. 31, Year 3 | $6.00 |
| Dec. 31, Year 3 market price of stock | $31 |

On December 31, Year 3, the COO exercises all SARs for cash: \((\$31 - \$25) \times 4{,}000 = \$24{,}000\).

**Required:**  
(a) Prepare the **subsequent measurement schedule** for Years 1–3 (aggregate compensation, % accrued, cumulative liability, annual expense).  
(b) Record **period-end adjusting journal entries** for Years 1–3.  
(c) Record the **cash settlement** entry on December 31, Year 3.  
(d) State the **ending SARs Liability** after settlement.

**Answer key:**

**(a) Subsequent measurement schedule**

| Date | Year-end FV per unit | Aggregate (× 4,000) | % service accrued | Cumulative liability | Annual expense |
|---|---:|---:|---:|---:|---:|
| Dec. 31, Year 1 | $3.00 | $12,000 | 33⅓% (1/3) | $4,000 | $4,000 |
| Dec. 31, Year 2 | 7.50 | 30,000 | 66⅔% (2/3) | 20,000 | 16,000 |
| Dec. 31, Year 3 | 6.00 | 24,000 | 100% | 24,000 | 4,000 |
| **Totals** | | | | | **$24,000** |

**Checks:**  
- Y1: \(12{,}000 \times 1/3 = 4{,}000\).  
- Y2: \(30{,}000 \times 2/3 = 20{,}000\); expense \(20{,}000 - 4{,}000 = 16{,}000\).  
- Y3: \(24{,}000 \times 1 = 24{,}000\); expense \(24{,}000 - 20{,}000 = 4{,}000\).  
- \(4{,}000 + 16{,}000 + 4{,}000 = 24{,}000\) = cash paid.

**(b) Period-end adjusting JEs**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Dec. 31, Year 1 | Compensation Expense | 4,000 | |
| | SARs Liability | | 4,000 |
| Dec. 31, Year 2 | Compensation Expense | 16,000 | |
| | SARs Liability | | 16,000 |
| Dec. 31, Year 3 | Compensation Expense | 4,000 | |
| | SARs Liability | | 4,000 |

Each entry balances.

**(c) Settlement — December 31, Year 3**

| Account | Debit | Credit |
|---|---:|---:|
| SARs Liability | 24,000 | |
| Cash | | 24,000 |
| *Cash settlement: ($31 − $25) × 4,000* | | |

**Check:** Dr 24,000 = Cr 24,000. **Balanced.**

**(d)** Ending SARs Liability after settlement = **$0**.

**Key insight:** Same liability model as Q1 with different units, prices, and a three-year service period. The **schedule** drives every adjusting entry; settlement simply extinguishes the fully accrued liability for cash equal to intrinsic appreciation.

---

### Q3 — CORE alternate angle — Meridian Apex: equity SARs (grant-date FV, no remeasurement) + stock settlement; contrast cash settlement of equity-classified award
**LO:** LO 20-10  
**Concept:** Equity-classified SARs (employer may settle in stock): grant-date FV straight-line over service period; no FV remeasurement; settlement reclass to common stock/APIC; contrast if employer pays cash instead  
**Scenario:**  
On **January 1, Year 1**, **Meridian Apex Group** grants **5,000** SARs to its CFO. The **employer** (not the employee) has the right to settle the SARs in **common stock**, so the awards are **equity-classified**. Grant-date fair value of the SARs is estimated at **$8 per unit**, or **$40,000** total. The requisite service period is **four years** (straight-line recognition). The predetermined base price is **$18** per share; Meridian common has **$1 par**.

Assume the CFO remains employed through vesting. On **December 31, Year 4**, market price is **$30**. Appreciation per SAR = \(\$30 - \$18 = \$12\); total intrinsic value = \(12 \times 5{,}000 = \$60{,}000\).

**Part A — Equity settlement (core path):** Meridian settles by issuing common stock with a fair value equal to the intrinsic appreciation (i.e., issues \(\$60{,}000 / \$30 = 2{,}000\) shares).

**Part B — Alternate cash settlement by employer:** Instead of stock, Meridian elects to pay **$60,000 cash** on December 31, Year 4 (same facts otherwise).

**Required:**  
(a) Compute **annual compensation expense** for Years 1–4 under equity classification.  
(b) Record the **period-end adjusting JE** for Year 1 (Years 2–4 identical in amount).  
(c) **Part A:** Record the **December 31, Year 4 stock settlement** entry.  
(d) **Part B:** Record the **December 31, Year 4 cash settlement** entry (employer pays cash on an equity-classified SAR).  
(e) Briefly explain why Years 2–4 **do not** adjust the equity credit for changes in the stock’s fair value.

**Answer key:**

**(a) Annual compensation (grant-date FV, straight-line)**

Total grant-date compensation = \(5{,}000 \times \$8 = \mathbf{\$40{,}000}\).  
Annual expense = \(40{,}000 / 4 = \mathbf{\$10{,}000}\) per year for Years 1–4.  
Cumulative PIC—SARs at end of Year 4 (before settlement) = **$40,000**.

**(b) Period-end adjusting JE (each of Years 1–4)**

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 10,000 | |
| Paid-in Capital—SARs Plan | | 10,000 |
| *Straight-line accrual of grant-date FV* | | |

**Check:** Dr 10,000 = Cr 10,000. **Balanced.** (Same entry Years 2, 3, and 4.)

**(c) Part A — Stock settlement, December 31, Year 4**

Shares issued = \(60{,}000 / 30 = 2{,}000\) shares at $1 par.

| Account | Debit | Credit |
|---|---:|---:|
| Paid-in Capital—SARs Plan | 40,000 | |
| Common Stock (2,000 × $1) | | 2,000 |
| Paid-in Capital in Excess of Par | | 38,000 |
| *Reclassify equity SARs into common equity on stock settlement* | | |

**Check:** Dr 40,000 = Cr \(2{,}000 + 38{,}000\). **Balanced.**  
(Note: Equity settlement reclassifies the **carrying amount** of PIC—SARs; no additional compensation is recognized for the higher intrinsic value when the award remains equity-settled in shares.)

**(d) Part B — Cash settlement by employer, December 31, Year 4**

| Account | Debit | Credit |
|---|---:|---:|
| Paid-in Capital—SARs Plan | 40,000 | |
| Compensation Expense | 20,000 | |
| Cash | | 60,000 |
| *Clear PIC—SARs; additional compensation for cash paid above grant-date FV* | | |

**Check:** Dr \(40{,}000 + 20{,}000 = 60{,}000\); Cr 60,000. **Balanced.**  
Additional compensation = cash paid − cumulative PIC = \(60{,}000 - 40{,}000 = 20{,}000\).

**(e)** Under **equity classification**, measurement is fixed at **grant-date fair value**. Because a transfer of assets is **not required** when the employer settles in stock, **no liability** is recorded and **no remeasurement** is made for subsequent changes in the stock’s fair value over the service period (unlike liability SARs).

**Key insight:** **Who controls settlement form** drives classification. **Employer stock settlement → equity** (fixed grant-date FV, credit PIC). **Employee cash right → liability** (remeasure schedule). If an equity-classified SAR is later settled in **cash**, clear PIC and charge any excess cash to **compensation expense**.

---

### Q4 — MC — Liability vs equity classification of SARs
**LO:** LO 20-10  
**Concept:** Classification of SARs as liability vs equity based on cash-settlement feature  
**Question:**  
Which of the following stock appreciation rights arrangements is **correctly classified as a liability** under U.S. GAAP (ASC 718)?

- A) Employer may settle SARs only by issuing its own common shares; employee has no cash election.  
- B) SARs are settled exclusively in the employer’s equity shares at the employer’s option; grant-date FV is fixed.  
- C) Employee has the right to require settlement of the SARs in **cash** equal to stock-price appreciation.  
- D) Employer settles SARs in shares and never remeasures after the grant date.

**Answer:** **C.**  
When the **entity can be required** to settle the SAR (or similar instrument) by transferring **cash or other assets**, the award is classified as a **liability** and is **remeasured** each period to the expected cash payment. Options A, B, and D describe **equity** classification (employer stock settlement; no liability; no post-grant FV remeasurement of the equity credit).

---

### Q4b — MC — Measurement basis after grant
**LO:** LO 20-10  
**Concept:** Subsequent measurement of liability SARs vs equity SARs  
**Question:**  
At December 31 of Year 2 of a three-year requisite service period, a company holds outstanding SARs. Which statement is **true**?

- A) Equity-classified SARs: remeasure the PIC credit each year-end to current fair value × cumulative service %.  
- B) Liability-classified SARs: year-end liability = (current FV per unit × number of SARs) × cumulative % of service period accrued; expense equals the change in that liability.  
- C) Both equity and liability SARs ignore service-period percentage until final vesting.  
- D) Liability SARs lock in grant-date FV and never reverse prior expense if FV declines.

**Answer:** **B.**  
Liability SARs use the **subsequent measurement schedule**: aggregate current FV × % service accrued = cumulative liability; the **period expense is the change** (which can reverse if FV falls). Equity SARs use **grant-date** FV only and do **not** remeasure PIC for later FV changes (A is false). Service % is applied each period for liabilities (C false). Liability expense **can reverse** when FV declines (D false).

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on all entries)
- [x] Math recomputed (schedules roll: Q1 expense sum $50,000 = cash; Q2 sum $24,000 = cash; Q3 annual $10,000 × 4 = $40,000 PIC)
- [x] Core demo not sidebar-only (Demo 20-10 equity + liability SARs; not Expanding Your Knowledge RSUs/sell-back)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4 and Q4b classification/measurement only)
- [x] Angles covered: initial_recognition_JE (period-end accruals as recognition), subsequent_measurement_schedule (emphasis), period_end_adjusting_JE, disposal_maturity_or_settlement_JE
