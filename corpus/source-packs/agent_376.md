# Agent 376 — CORE DEMO — LO 20-1

**Chapter:** 20  
**LO title:** Accounting for Restricted Stock Plans  
**Critical gap LO:** no  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **Restricted stock awards (RSA):** shares issued at **grant date** but held restricted; measure total compensation at **grant-date fair value**; debit **Unearned Compensation—Equity** (contra-equity)
- **Restricted stock units (RSU):** right to receive shares after vesting; **no grant-date JE**; credit **Paid-in Capital—Restricted Stock** as expense is recognized
- **Initial recognition JE:** RSA grant-date equity issuance at FV; RSU measurement only (memo total cost)
- **Subsequent measurement schedule:** straight-line amortization of grant-date FV over the **requisite service period** (typically the vesting period); post-grant price changes **ignored**
- **Period-end adjusting JE (emphasis):** year-end Dr **Compensation Expense**, Cr **Unearned Compensation—Equity** (RSA) or Cr **Paid-in Capital—Restricted Stock** (RSU); revise cumulative expense for forfeiture estimate changes
- **Disposal / maturity / settlement JE:** (1) RSA **forfeiture** — reverse CS, PIC, remaining unearned, and prior compensation expense; (2) RSU **vesting/issuance** — reclassify PIC—Restricted Stock into Common Stock and PIC—Common Stock
- **Forfeiture policies:** estimate forfeitures (reduce expected awards) **or** record forfeitures as incurred (practical expedient); change in estimate is **cumulative catch-up** in the current period

---

### Q1 — CORE — RSA full cycle: grant, amortization schedule, YE adjusting, forfeiture settlement
**LO:** LO 20-1  
**Concept:** Restricted stock awards — initial recognition JE; subsequent amortization schedule; period-end adjusting JE; forfeiture (settlement) JE when employee leaves  
**Scenario:**  
**Helix Forge Inc.** (calendar year-end) grants restricted stock to one senior operations officer.

| Fact | Amount / term |
|---|---|
| **January 1, Year 1** — grant | **2,400** shares of **$1** par common stock |
| Grant-date fair value | **$28** per share |
| Vesting / requisite service period | **3 years** cliff (must remain employed through Dec 31, Year 3) |
| Forfeiture policy | Recognize forfeitures **as incurred** |
| **January 1, Year 2** | Officer resigns; all restricted shares are forfeited |
| Market price Dec 31, Year 1 / Jan 1, Year 2 | **$31** / **$29** (not used for measurement) |

**Required:**  
a. Compute total compensation cost at the grant date. Prepare the **January 1, Year 1 initial recognition JE**.  
b. Prepare a **3-year subsequent measurement (amortization) schedule** assuming the officer completes service (for planning). State annual compensation expense under the original plan.  
c. Prepare the **December 31, Year 1 period-end adjusting JE** and show the **stockholders’ equity presentation** for this award at Dec 31, Year 1.  
d. Prepare the **January 1, Year 2 forfeiture (settlement) JE**. Explain why the Dec 31 / Jan 1 market prices do not change the amounts.

**Answer key:**  

**a. Total compensation and grant-date JE**

\[
\text{Total compensation} = 2{,}400 \times \$28 = \mathbf{\$67{,}200}
\]

*January 1, Year 1 — To record issuance of restricted stock (initial recognition)*

| Account | Debit | Credit |
|---|---:|---:|
| Unearned Compensation—Equity | 67,200 | |
| Common Stock (2,400 × $1) | | 2,400 |
| Paid-in Capital in Excess of Par—Common Stock | | 64,800 |
| *Issue restricted shares at grant-date FV; unearned contra-equity* | | |

**Check:** Dr 67,200 = Cr 67,200 (2,400 + 64,800). **Balanced.**

**b. Subsequent measurement schedule (planned full service)**

Straight-line over 3-year requisite service period:

\[
\text{Annual compensation expense} = \$67{,}200 / 3 = \mathbf{\$22{,}400}
\]

| Year | Beg. Unearned Comp. | Amortization (Comp. Exp.) | End. Unearned Comp. | Cumulative Comp. Exp. |
|---:|---:|---:|---:|---:|
| 1 | 67,200 | 22,400 | 44,800 | 22,400 |
| 2 | 44,800 | 22,400 | 22,400 | 44,800 |
| 3 | 22,400 | 22,400 | 0 | 67,200 |

**Schedule roll-forward:** \(22{,}400 \times 3 = 67{,}200\); ending unearned after Year 3 = **$0**.

**c. Period-end adjusting JE and equity presentation (emphasis)**

*December 31, Year 1 — To record compensation expense (period-end adjusting)*

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 22,400 | |
| Unearned Compensation—Equity | | 22,400 |
| *Amortize 1/3 of grant-date FV over requisite service period* | | |

**Check:** Dr 22,400 = Cr 22,400. **Balanced.**

**Stockholders’ equity presentation — Dec 31, Year 1 (related accounts)**

| Account | Amount |
|---|---:|
| Common stock | $2,400 |
| Paid-in capital in excess of par—common stock | 64,800 |
| Unearned compensation—equity \((\$67{,}200 - \$22{,}400)\) | **(44,800)** |
| **Net equity effect of award** | **22,400** |

Income statement Year 1: Compensation expense **$22,400**.

**d. Forfeiture / settlement JE — January 1, Year 2**

Related equity accounts are derecognized; previously recognized compensation expense is reversed (forfeitures as incurred).

*January 1, Year 2 — To record restricted stock forfeiture*

| Account | Debit | Credit |
|---|---:|---:|
| Common Stock | 2,400 | |
| Paid-in Capital in Excess of Par—Common Stock | 64,800 | |
| Unearned Compensation—Equity | | 44,800 |
| Compensation Expense | | 22,400 |
| *Derecognize award; reverse prior-year expense and remaining unearned* | | |

**Check:** Dr 67,200 = Cr 67,200 (44,800 + 22,400). **Balanced.**

**Key insight:** Grant-date **fair value** locks total compensation; later market prices are **irrelevant**. RSA issues stock immediately (with unearned contra-equity). Forfeiture as incurred reverses both the capital stock accounts and cumulative expense already recognized.

---

### Q2 — CORE number variant — RSA grant through full vesting (no forfeiture)
**LO:** LO 20-1  
**Concept:** Restricted stock awards — number-variant twin: initial recognition, multi-year amortization schedule, successive period-end adjusting JEs, equity after full vesting  
**Scenario:**  
**Meridian Optics Corp.** (calendar year-end) grants restricted stock to its CFO.

| Fact | Amount / term |
|---|---|
| **January 1, Year 1** — grant | **1,500** shares of **$2** par common stock |
| Grant-date fair value | **$48** per share |
| Vesting / requisite service period | **3 years** cliff |
| Forfeitures | **None** anticipated or incurred |
| Average market prices Years 1–3 | $45, $52, $55 (irrelevant for measurement) |
| CFO remains employed through Dec 31, Year 3 | Shares become unrestricted |

**Required:**  
a. Compute total compensation and prepare the **January 1, Year 1 grant JE**.  
b. Prepare the **amortization schedule** for Years 1–3.  
c. Prepare the **December 31, Year 1, Year 2, and Year 3 period-end adjusting JEs**.  
d. State the balances in Common Stock, PIC—Common Stock, and Unearned Compensation—Equity immediately **after** the Year 3 adjusting entry. Is a separate “issuance” entry required at vesting for an RSA?

**Answer key:**  

**a. Total compensation and grant JE**

\[
\text{Total compensation} = 1{,}500 \times \$48 = \mathbf{\$72{,}000}
\]

*January 1, Year 1 — To record issuance of restricted stock*

| Account | Debit | Credit |
|---|---:|---:|
| Unearned Compensation—Equity | 72,000 | |
| Common Stock (1,500 × $2) | | 3,000 |
| Paid-in Capital in Excess of Par—Common Stock | | 69,000 |
| *RSA at grant-date FV* | | |

**Check:** Dr 72,000 = Cr 72,000 (3,000 + 69,000). **Balanced.**

**b. Amortization schedule**

\[
\text{Annual expense} = \$72{,}000 / 3 = \mathbf{\$24{,}000}
\]

| Year | Beg. Unearned | Comp. Expense | End. Unearned | Cum. Expense |
|---:|---:|---:|---:|---:|
| 1 | 72,000 | 24,000 | 48,000 | 24,000 |
| 2 | 48,000 | 24,000 | 24,000 | 48,000 |
| 3 | 24,000 | 24,000 | 0 | 72,000 |

**Roll-forward check:** \(24{,}000 \times 3 = 72{,}000\); ending unearned = **$0**.

**c. Period-end adjusting JEs**

*December 31, Year 1 — Compensation expense*

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 24,000 | |
| Unearned Compensation—Equity | | 24,000 |

**Check:** Dr 24,000 = Cr 24,000. **Balanced.**

*December 31, Year 2 — Compensation expense*

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 24,000 | |
| Unearned Compensation—Equity | | 24,000 |

**Check:** Dr 24,000 = Cr 24,000. **Balanced.**

*December 31, Year 3 — Compensation expense (final amortization; full vesting)*

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 24,000 | |
| Unearned Compensation—Equity | | 24,000 |

**Check:** Dr 24,000 = Cr 24,000. **Balanced.**

**d. Equity balances after Year 3 adjusting entry**

| Account | Balance |
|---|---:|
| Common Stock | $3,000 |
| Paid-in Capital in Excess of Par—Common Stock | 69,000 |
| Unearned Compensation—Equity | **$0** |

**No separate issuance JE at vesting** for a restricted **stock award**: shares were already issued at the grant date. Vesting removes the restriction; the final amortization zeroes the unearned contra-equity. (Contrast with RSUs, which issue shares only upon settlement.)

**Key insight:** RSA lifecycle is **issue at grant → amortize unearned → (optional) reverse on forfeiture**. Successful vesting is simply the last period-end amortization; capital stock accounts remain at grant-date amounts.

---

### Q3 — CORE alternate angle — RSU period-end adjusting, forfeiture estimate change, and settlement issuance
**LO:** LO 20-1  
**Concept:** Restricted stock units — no grant JE; period-end adjusting JEs with estimated forfeitures and cumulative catch-up; settlement JE when units vest and shares are issued  
**Scenario:**  
**Cascade BioLabs Inc.** (calendar year-end) grants **restricted stock units (RSUs)** to six managers.

| Fact | Amount / term |
|---|---|
| **January 1, Year 1** — grant | **6,000** RSUs (each unit = right to **1** share of **$1** par common) |
| Grant-date fair value | **$20** per unit |
| Requisite service period | **3 years** cliff |
| Forfeiture policy | **Estimate forfeitures** (entity-wide election) |
| Grant-date forfeiture estimate | **1,200** units (20%) will be forfeited |
| **December 31, Year 2** — revised estimate | Expected forfeitures increase to **2,400** units (40%); **no** units actually forfeited yet |
| **December 31, Year 3** | Estimate holds; **2,400** units forfeited by year-end; **3,600** units vest |
| **January 1, Year 4** | Company issues **3,600** common shares to settle vested RSUs |

**Required:**  
a. Compute total grant-date fair value of all units and **expected** compensation cost under the initial forfeiture estimate. Explain why there is **no January 1, Year 1 JE**.  
b. Prepare the **December 31, Year 1 period-end adjusting JE**.  
c. Prepare the **December 31, Year 2 period-end adjusting JE** reflecting the **change in forfeiture estimate** (cumulative catch-up). Show the measurement schedule of target cumulative PIC—Restricted Stock.  
d. Prepare the **December 31, Year 3 period-end adjusting JE**.  
e. Prepare the **January 1, Year 4 settlement (issuance) JE** for the vested units.  
f. Briefly state how Year 2 expense would differ if Cascade instead elected **forfeitures as incurred** and one manager (1,000 units) left on Dec 31, Year 2 with no other estimate changes (original scenario of 6,000 units, no initial estimate).

**Answer key:**  

**a. Measurement at grant; no grant-date JE**

\[
\text{Gross FV of all units} = 6{,}000 \times \$20 = \mathbf{\$120{,}000}
\]

\[
\text{Expected awards} = 6{,}000 - 1{,}200 = 4{,}800 \text{ units}
\]

\[
\text{Expected total compensation} = 4{,}800 \times \$20 = \mathbf{\$96{,}000}
\]

**No journal entry on January 1, Year 1:** RSUs convey a **right** to future shares; stock is not issued until vesting. Total cost is calculated for amortization planning only.

**b. Period-end adjusting JE — December 31, Year 1 (emphasis)**

\[
\text{Year 1 expense} = \$96{,}000 / 3 = \mathbf{\$32{,}000}
\]

*December 31, Year 1 — To record compensation expense*

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 32,000 | |
| Paid-in Capital—Restricted Stock | | 32,000 |
| *Recognize 1/3 of expected grant-date FV* | | |

**Check:** Dr 32,000 = Cr 32,000. **Balanced.**

**c. Change in estimate — December 31, Year 2 period-end adjusting JE**

Revised expected awards: \(6{,}000 - 2{,}400 = 3{,}600\) units.

\[
\text{Revised total compensation} = 3{,}600 \times \$20 = \mathbf{\$72{,}000}
\]

After **2 of 3** service years, cumulative PIC—Restricted Stock (and cumulative expense) should be:

\[
\$72{,}000 \times \frac{2}{3} = \mathbf{\$48{,}000}
\]

Amount already recognized in Year 1: **$32,000**.

\[
\text{Year 2 compensation expense} = \$48{,}000 - \$32{,}000 = \mathbf{\$16{,}000}
\]

**Cumulative catch-up schedule (target PIC—Restricted Stock)**

| Year-end | Expected total cost | Service fraction | Target cumulative PIC—RS | Beg. PIC—RS | Period expense | End. PIC—RS |
|---:|---:|---:|---:|---:|---:|---:|
| Y1 | 96,000 | 1/3 | 32,000 | 0 | 32,000 | 32,000 |
| Y2 | 72,000 (revised) | 2/3 | 48,000 | 32,000 | **16,000** | 48,000 |
| Y3 | 72,000 | 3/3 | 72,000 | 48,000 | 24,000 | 72,000 |

*December 31, Year 2 — To record compensation expense (includes cumulative effect of estimate change)*

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 16,000 | |
| Paid-in Capital—Restricted Stock | | 16,000 |
| *Bring cumulative cost to $48,000 under revised forfeiture estimate* | | |

**Check:** Dr 16,000 = Cr 16,000. **Balanced.**

**d. Period-end adjusting JE — December 31, Year 3**

Target cumulative PIC—RS = full revised cost **$72,000**.  
Prior cumulative = **$48,000**.

\[
\text{Year 3 expense} = \$72{,}000 - \$48{,}000 = \mathbf{\$24{,}000}
\]

*December 31, Year 3 — To record compensation expense*

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 24,000 | |
| Paid-in Capital—Restricted Stock | | 24,000 |

**Check:** Dr 24,000 = Cr 24,000. **Balanced.**

**Total expense over life:** \(32{,}000 + 16{,}000 + 24{,}000 = \mathbf{\$72{,}000}\) (= 3,600 × $20).

**e. Settlement / issuance JE — January 1, Year 4**

*January 1, Year 4 — To record issuance of common stock for vested RSUs*

| Account | Debit | Credit |
|---|---:|---:|
| Paid-in Capital—Restricted Stock | 72,000 | |
| Common Stock (3,600 × $1) | | 3,600 |
| Paid-in Capital in Excess of Par—Common Stock | | 68,400 |
| *Reclassify PIC—Restricted Stock into permanent capital stock accounts* | | |

**Check:** Dr 72,000 = Cr 72,000 (3,600 + 68,400). **Balanced.**

**f. Contrast — forfeitures as incurred (illustrative Year 2 only)**

If no estimate is used: Year 1 expense = \(6{,}000 \times \$20 / 3 = \mathbf{\$40{,}000}\).  
If 1,000 units forfeit on Dec 31, Year 2: revised total cost for remaining 5,000 units = \(5{,}000 \times \$20 = \$100{,}000\); after 2/3 service, target PIC—RS = \(100{,}000 \times 2/3 = \$66{,}667\) (or exact fraction \(100{,}000 \times 2/3\)).  
Year 2 expense = target − Year 1 recognized = \(66{,}667 - 40{,}000 = \mathbf{\$26{,}667}\) (rounded), **not** a simple 1/3 of original.  
*(If exact thirds preferred without rounding: target \(100{,}000 \times 2/3 = 200{,}000/3\); expense Year 2 = \(200{,}000/3 - 40{,}000 = 200{,}000/3 - 120{,}000/3 = 80{,}000/3 = \$26{,}666.67\).)*  
Policy difference changes **timing** of expense when forfeitures occur; lifetime expense still equals FV of awards that ultimately vest.

**Key insight (emphasis):** RSU **period-end adjusting** entries credit **PIC—Restricted Stock**, not unearned contra-equity. Estimated forfeitures reduce the base; a revised estimate triggers a **cumulative catch-up** so that cumulative expense equals (revised expected cost × service fraction completed). Settlement **issues stock** by debiting PIC—Restricted Stock.

---

### Q4 — MC — Grant-date accounting: RSA vs RSU
**LO:** LO 20-1  
**Concept:** Classification / method — distinguish restricted stock award vs restricted stock unit at the grant date  
**Question:**  
On the **grant date**, a company awards equity-classified restricted stock (not units) measured at grant-date fair value. Which journal entry (or treatment) is correct?

- A) No entry is recorded until the vesting date, when Common Stock is credited for fair value.  
- B) Debit Compensation Expense for the full grant-date fair value; credit Paid-in Capital—Restricted Stock.  
- C) Debit Unearned Compensation—Equity for grant-date fair value; credit Common Stock (par) and Paid-in Capital in Excess of Par for the remainder.  
- D) Debit Unearned Compensation—Equity each period for the **current** market price of the shares; credit Common Stock only at vesting.

**Answer:** **C.**  
Restricted **stock awards** issue shares at grant (often held in trust); total compensation is measured at **grant-date FV** and recorded as **Unearned Compensation—Equity** (contra-equity) against Common Stock and PIC. Compensation expense is recognized over the service period by amortizing unearned compensation—not by remeasuring to each period’s market price (A is RSU-like for timing of stock issuance; B is the RSU **period-end** pattern, not the RSA grant entry; D incorrectly uses subsequent market prices).

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (67,200/3; 72,000/3; 96,000→72,000 catch-up; settlement 3,600×$1 + PIC)
- [x] Core demo not sidebar-only (Demo 20-1A / 20-1B primary path: RSA, RSU, forfeitures, settlement)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (one MC on RSA vs RSU grant treatment)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE (emphasis), disposal_maturity_or_settlement_JE (forfeiture + RSU issuance)
