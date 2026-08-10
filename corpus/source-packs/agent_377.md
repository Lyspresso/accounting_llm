# Agent 377 — CORE DEMO — LO 20-10

**Chapter:** 20  
**LO title:** Describe accounting for stock appreciation rights  
**Critical gap LO:** no  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **Stock appreciation rights (SARs):** right to compensation equal to **appreciation** in market price above a **predetermined (base/grant) price**
- **Classification:** **equity** when the **employer** may settle in stock; **liability** when the **employee** can require **cash** (ASC 718-10-25-11)
- **Equity SARs:** grant-date fair value fixed; straight-line Compensation Expense → **Paid-in Capital—SARs**; **no** remeasurement for later stock-price changes
- **Liability SARs:** remeasure each period-end; cumulative liability = (year-end FV per unit × # SARs) × **% of service period accrued**; expense = **change** in liability (may reverse)
- **Period-end adjusting JE (emphasis):** true-up SARs Liability (or reverse) / or accrue PIC—SARs so the balance matches the schedule
- **Initial recognition JE:** first period-end accrual starts the liability (or equity) credit; typically **no** grant-date entry if measurement begins at year-end
- **Settlement / exercise JE:** clear SARs Liability or PIC—SARs against **Cash** and/or **Common Stock**/APIC

---

### Q1 — CORE — Cedarwright Medical: liability SARs multipath (period-end adjusting JEs emphasis)
**LO:** LO 20-10  
**Concept:** Liability-classified SARs: period-end adjusting JEs each year (including reverse entry when FV declines); subsequent measurement schedule; cash settlement  
**Scenario:**  
On **January 1, Year 1**, **Cedarwright Medical Devices** grants **8,000** stock appreciation rights to key executives. For each SAR, the executive receives **cash** equal to the excess of the market price of Cedarwright common stock on the exercise date over a **predetermined price of $22**. The **employee** has the right to require cash settlement, so the awards are **liability-classified**.

The rights require continuing employment and may first be exercised on **December 31, Year 4**. The **requisite service period is four years**. Year-end fair values of the SARs **per unit** and the exercise-date market price:

| Date | Fair value per SAR | Notes |
|---|---:|---|
| Dec. 31, Year 1 | $1.50 | |
| Dec. 31, Year 2 | $4.00 | |
| Dec. 31, Year 3 | $2.50 | FV declined → reverse adjusting JE |
| Dec. 31, Year 4 | $6.00 | Exercise date |
| Dec. 31, Year 4 market price of stock | $28 | Predetermined base = $22 |

Executives exercise all 8,000 SARs for cash on **December 31, Year 4**. Cash paid = \((\$28 - \$22) \times 8{,}000 = \$48{,}000\).

No journal entry is recorded on the **grant date** (January 1, Year 1). All recognition occurs through **period-end adjusting entries**.

**Required:**  
(a) Prepare the **subsequent measurement schedule** for Years 1–4: year-end fair value, aggregate compensation, % of service accrued, cumulative SARs liability, and **annual compensation expense**.  
(b) **(Emphasis.)** Record the **December 31 period-end adjusting journal entry** for compensation in **each** of Years 1–4. Label Year 1 as **initial recognition**. Show the **reverse** entry when expense is negative.  
(c) Record the **settlement journal entry** on December 31, Year 4 when cash is paid.  
(d) Prove that cumulative net compensation expense equals cash paid and that the liability is zero after settlement.

**Answer key:**

**(a) Subsequent measurement schedule (liability SARs)**

| Date | Year-end FV per unit (A) | Aggregate compensation (A × 8,000) (B) | % of service accrued (C) | Total SARs liability (B × C) (D) | Annual expense (D − prior D) |
|---|---:|---:|---:|---:|---:|
| Dec. 31, Year 1 | $1.50 | $12,000 | 25% | $3,000 | $3,000 |
| Dec. 31, Year 2 | 4.00 | 32,000 | 50% | 16,000 | 13,000 |
| Dec. 31, Year 3 | 2.50 | 20,000 | 75% | 15,000 | **(1,000)** |
| Dec. 31, Year 4 | 6.00 | 48,000 | 100% | 48,000 | 33,000 |
| **Totals** | | | | | **$48,000** |

**Checks:**  
- Year 1: \(12{,}000 \times 0.25 = 3{,}000\).  
- Year 2: \(32{,}000 \times 0.50 = 16{,}000\); expense \(16{,}000 - 3{,}000 = 13{,}000\).  
- Year 3: \(20{,}000 \times 0.75 = 15{,}000\); expense \(15{,}000 - 16{,}000 = (1{,}000)\).  
- Year 4: \(48{,}000 \times 1.00 = 48{,}000\); expense \(48{,}000 - 15{,}000 = 33{,}000\).  
- Sum: \(3{,}000 + 13{,}000 - 1{,}000 + 33{,}000 = \mathbf{\$48{,}000}\).

**(b) Period-end adjusting journal entries (emphasis)**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Dec. 31, Year 1 | Compensation Expense | 3,000 | |
| | SARs Liability | | 3,000 |
| | *Initial recognition: accrue 25% of aggregate year-end FV* | | |
| Dec. 31, Year 2 | Compensation Expense | 13,000 | |
| | SARs Liability | | 13,000 |
| | *Increase liability from $3,000 to $16,000* | | |
| Dec. 31, Year 3 | SARs Liability | 1,000 | |
| | Compensation Expense | | 1,000 |
| | *Reverse/reduce liability from $16,000 to $15,000 (FV decline)* | | |
| Dec. 31, Year 4 | Compensation Expense | 33,000 | |
| | SARs Liability | | 33,000 |
| | *Increase liability to $48,000 at full vesting* | | |

Each entry balances (Dr = Cr).  
**Liability roll-forward:** \(0 + 3{,}000 + 13{,}000 - 1{,}000 + 33{,}000 = \$48{,}000\) before settlement.

**(c) Settlement JE — December 31, Year 4**

| Account | Debit | Credit |
|---|---:|---:|
| SARs Liability | 48,000 | |
| Cash | | 48,000 |
| *Cash settlement: ($28 − $22) × 8,000* | | |

**Check:** Dr 48,000 = Cr 48,000. **Balanced.**

**(d) Proof**

| Item | Amount |
|---|---:|
| Cumulative net compensation expense (Y1–Y4) | $48,000 |
| Cash paid at exercise | 48,000 |
| Liability immediately before settlement | 48,000 |
| Liability after settlement | **$0** |

**Key insight:** For **cash-settled (liability) SARs**, every **period-end adjusting JE** resets the liability to (current aggregate FV × cumulative service %). When fair value **falls**, the adjusting entry **debits SARs Liability and credits Compensation Expense** (expense reduction). At exercise, the fully remeasured liability equals cash paid and is cleared.

---

### Q2 — CORE number variant — Bluehaven Retail: liability SARs (3-year schedule + period-end JEs + settlement)
**LO:** LO 20-10  
**Concept:** Number-variant twin: liability SARs subsequent measurement schedule; period-end adjusting JEs; cash settlement at exercise  
**Scenario:**  
On **January 1, Year 1**, **Bluehaven Retail Group** grants **12,000** SARs to its COO. The employee may redeem each SAR for **cash** equal to the excess of the market price of Bluehaven common over a **predetermined price of $10**. Because the **employee** can require cash, the SARs are **liability-classified**.

The SARs vest and may first be exercised on **December 31, Year 3**. The **requisite service period is three years**. Year-end fair values per SAR and the exercise-date market price:

| Date | Fair value per SAR |
|---|---:|
| Dec. 31, Year 1 | $2.00 |
| Dec. 31, Year 2 | $5.50 |
| Dec. 31, Year 3 | $4.00 |
| Dec. 31, Year 3 market price of stock | $14 |

On December 31, Year 3, the COO exercises all SARs for cash: \((\$14 - \$10) \times 12{,}000 = \$48{,}000\).

**Required:**  
(a) Prepare the **subsequent measurement schedule** for Years 1–3 (aggregate compensation, % accrued, cumulative liability, annual expense).  
(b) Record **period-end adjusting journal entries** for Years 1–3 (initial recognition in Year 1).  
(c) Record the **cash settlement** entry on December 31, Year 3.  
(d) State the **ending SARs Liability** after settlement and prove expense sum equals cash.

**Answer key:**

**(a) Subsequent measurement schedule**

| Date | Year-end FV per unit | Aggregate (× 12,000) | % service accrued | Cumulative liability | Annual expense |
|---|---:|---:|---:|---:|---:|
| Dec. 31, Year 1 | $2.00 | $24,000 | 33⅓% (1/3) | $8,000 | $8,000 |
| Dec. 31, Year 2 | 5.50 | 66,000 | 66⅔% (2/3) | 44,000 | 36,000 |
| Dec. 31, Year 3 | 4.00 | 48,000 | 100% | 48,000 | 4,000 |
| **Totals** | | | | | **$48,000** |

**Checks:**  
- Y1: \(24{,}000 \times 1/3 = 8{,}000\).  
- Y2: \(66{,}000 \times 2/3 = 44{,}000\); expense \(44{,}000 - 8{,}000 = 36{,}000\).  
- Y3: \(48{,}000 \times 1 = 48{,}000\); expense \(48{,}000 - 44{,}000 = 4{,}000\).  
- \(8{,}000 + 36{,}000 + 4{,}000 = 48{,}000\) = cash paid.

**(b) Period-end adjusting JEs**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Dec. 31, Year 1 | Compensation Expense | 8,000 | |
| | SARs Liability | | 8,000 |
| | *Initial recognition: $24,000 × 1/3* | | |
| Dec. 31, Year 2 | Compensation Expense | 36,000 | |
| | SARs Liability | | 36,000 |
| | *True-up liability to $44,000* | | |
| Dec. 31, Year 3 | Compensation Expense | 4,000 | |
| | SARs Liability | | 4,000 |
| | *True-up liability to $48,000 at full vesting* | | |

Each entry balances.

**(c) Settlement — December 31, Year 3**

| Account | Debit | Credit |
|---|---:|---:|
| SARs Liability | 48,000 | |
| Cash | | 48,000 |
| *Cash settlement: ($14 − $10) × 12,000* | | |

**Check:** Dr 48,000 = Cr 48,000. **Balanced.**

**(d)** Ending SARs Liability after settlement = **$0**. Cumulative expense **$48,000** = cash paid **$48,000**.

**Key insight:** Same liability model as Q1 with different units, prices, and a three-year service period. **Period-end adjusting entries** are driven entirely by the schedule; settlement extinguishes the fully accrued liability for cash equal to intrinsic appreciation.

---

### Q3 — CORE alternate angle — Quarry Ridge: equity SARs (grant-date FV, period-end accruals) + stock vs cash settlement
**LO:** LO 20-10  
**Concept:** Equity-classified SARs (employer may settle in stock): grant-date FV straight-line period-end adjusting JEs; no FV remeasurement; stock settlement reclass; contrast cash settlement of equity-classified award  
**Scenario:**  
On **January 1, Year 1**, **Quarry Ridge Holdings** grants **8,000** SARs to its CFO. The **employer** (not the employee) has the right to settle the SARs in **common stock**, so the awards are **equity-classified**. Grant-date fair value of the SARs is estimated at **$5 per unit**, or **$40,000** total. The requisite service period is **four years** (straight-line recognition). The predetermined base price is **$15** per share; Quarry Ridge common has **$1 par**.

Assume the CFO remains employed through vesting. On **December 31, Year 4**, market price is **$25**. Appreciation per SAR = \(\$25 - \$15 = \$10\); total intrinsic value = \(10 \times 8{,}000 = \$80{,}000\).

**Part A — Equity settlement (core path):** Quarry Ridge settles by issuing common stock with a fair value equal to the intrinsic appreciation (issues \(\$80{,}000 / \$25 = 3{,}200\) shares).

**Part B — Alternate cash settlement by employer:** Instead of stock, Quarry Ridge elects to pay **$80,000 cash** on December 31, Year 4 (same facts otherwise).

**Required:**  
(a) Compute **annual compensation expense** for Years 1–4 under equity classification.  
(b) **(Emphasis.)** Record the **period-end adjusting JE** for Year 1 (Years 2–4 identical in amount). State why Years 2–4 do **not** change the credit amount for stock-price movements.  
(c) **Part A:** Record the **December 31, Year 4 stock settlement** entry.  
(d) **Part B:** Record the **December 31, Year 4 cash settlement** entry (employer pays cash on an equity-classified SAR).  
(e) Contrast the **period-end adjusting JE accounts** for equity SARs vs liability SARs.

**Answer key:**

**(a) Annual compensation (grant-date FV, straight-line)**

Total grant-date compensation = \(8{,}000 \times \$5 = \mathbf{\$40{,}000}\).  
Annual expense = \(40{,}000 / 4 = \mathbf{\$10{,}000}\) per year for Years 1–4.  
Cumulative PIC—SARs at end of Year 4 (before settlement) = **$40,000**.

**(b) Period-end adjusting JE (each of Years 1–4)**

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 10,000 | |
| Paid-in Capital—SARs Plan | | 10,000 |
| *Straight-line accrual of grant-date FV; no remeasurement* | | |

**Check:** Dr 10,000 = Cr 10,000. **Balanced.** (Same entry Years 2, 3, and 4.)

Under **equity classification**, measurement is locked at **grant-date fair value**. Because a transfer of assets is **not required** when the employer settles in stock, **no liability** is recorded and **no remeasurement** is made for subsequent changes in the stock’s fair value over the service period. Period-end adjusting entries stay at **$10,000** every year regardless of year-end stock price.

**(c) Part A — Stock settlement, December 31, Year 4**

Shares issued = \(80{,}000 / 25 = 3{,}200\) shares at $1 par.

| Account | Debit | Credit |
|---|---:|---:|
| Paid-in Capital—SARs Plan | 40,000 | |
| Common Stock (3,200 × $1) | | 3,200 |
| Paid-in Capital in Excess of Par | | 36,800 |
| *Reclassify equity SARs into common equity on stock settlement* | | |

**Check:** Dr 40,000 = Cr \(3{,}200 + 36{,}800\). **Balanced.**  
Equity settlement reclassifies the **carrying amount** of PIC—SARs; no additional compensation is recognized for the higher intrinsic value when the award remains equity-settled in shares.

**(d) Part B — Cash settlement by employer, December 31, Year 4**

| Account | Debit | Credit |
|---|---:|---:|
| Paid-in Capital—SARs Plan | 40,000 | |
| Compensation Expense | 40,000 | |
| Cash | | 80,000 |
| *Clear PIC—SARs; additional compensation for cash paid above grant-date FV* | | |

**Check:** Dr \(40{,}000 + 40{,}000 = 80{,}000\); Cr 80,000. **Balanced.**  
Additional compensation = cash paid − cumulative PIC = \(80{,}000 - 40{,}000 = 40{,}000\).

**(e) Period-end credit account contrast**

| Classification | Period-end Dr | Period-end Cr | Remeasure? |
|---|---|---|---|
| **Liability SARs** (employee cash right) | Compensation Expense (or reverse) | **SARs Liability** | **Yes** — each year-end to current FV × % service |
| **Equity SARs** (employer may settle in stock) | Compensation Expense | **Paid-in Capital—SARs** | **No** — fixed grant-date FV only |

**Key insight:** **Who controls settlement form** drives classification and the **period-end adjusting credit**. Employer stock settlement → fixed PIC accrual. Employee cash right → remeasured liability. If an equity-classified SAR is later settled in **cash**, clear PIC and charge any excess cash to **compensation expense**.

---

### Q4 — MC — Period-end adjusting JE when liability SARs fair value declines
**LO:** LO 20-10  
**Concept:** Period-end adjusting journal entry for liability SARs when year-end FV decline reduces cumulative liability  
**Question:**  
A company accounts for cash-settled SARs as liabilities. At the end of Year 2, the cumulative SARs liability from the measurement schedule is **$20,000**. At the end of Year 3, after applying the updated year-end fair value and the higher cumulative service percentage, the schedule shows a cumulative SARs liability of **$18,500**. What is the **correct period-end adjusting journal entry** at December 31, Year 3?

- A) Dr Compensation Expense 18,500; Cr SARs Liability 18,500  
- B) Dr Compensation Expense 1,500; Cr SARs Liability 1,500  
- C) Dr SARs Liability 1,500; Cr Compensation Expense 1,500  
- D) Dr Paid-in Capital—SARs 1,500; Cr Compensation Expense 1,500  

**Answer:** **C.**  
Annual expense (or expense reduction) equals the **change** in the cumulative SARs liability: \(18{,}500 - 20{,}000 = (1{,}500)\). When the liability **decreases**, the period-end adjusting entry **debits SARs Liability and credits Compensation Expense**. Option A records the cumulative balance as if it were the period entry. Option B increases the liability when it should decrease. Option D uses an **equity** credit account, which is incorrect for liability-classified SARs.

---

### Q4b — MC — Equity vs liability: which credit in the period-end adjusting JE?
**LO:** LO 20-10  
**Concept:** Correct credit account in period-end adjusting JE for equity-classified vs liability-classified SARs  
**Question:**  
Which statement correctly describes the **period-end adjusting journal entry** to recognize compensation for stock appreciation rights?

- A) Equity-classified SARs: Dr Compensation Expense; Cr SARs Liability (remeasured each year).  
- B) Liability-classified SARs: Dr Compensation Expense; Cr Paid-in Capital—SARs Plan (fixed grant-date FV).  
- C) Equity-classified SARs (employer may settle in stock): Dr Compensation Expense; Cr Paid-in Capital—SARs Plan, using grant-date fair value amortized over the requisite service period with **no** subsequent FV remeasurement.  
- D) Both equity and liability SARs always credit Cash at each period-end until exercise.

**Answer:** **C.**  
When the **employer** may settle SARs in stock, the award is **equity-classified**: period-end adjusting entries debit Compensation Expense and credit **PIC—SARs** for the straight-line portion of **grant-date** fair value, without remeasurement. Liability SARs (employee cash right) credit **SARs Liability** and **do** remeasure (A and B reverse the accounts). Cash is recorded only at **settlement**, not at each period-end accrual (D false).

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on all entries)
- [x] Math recomputed (Q1 expense sum $48,000 = cash; Q2 sum $48,000 = cash; Q3 annual $10,000 × 4 = $40,000 PIC; stock settlement 3,200 + 36,800 = 40,000; cash settlement 40,000 + 40,000 = 80,000)
- [x] Core demo not sidebar-only (Demo 20-10 equity + liability SARs; not Expanding Your Knowledge RSUs/sell-back)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4 and Q4b classification / period-end JE only)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE (emphasis), disposal_maturity_or_settlement_JE
- [x] Original company names/numbers (Cedarwright, Bluehaven, Quarry Ridge — not textbook Serenity/Brum)
