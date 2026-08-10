# Agent 378 — CORE DEMO — LO 20-2

**Chapter:** 20  
**LO title:** Account for stock options  
**Critical gap LO:** no  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **Grant-date measurement:** total compensation = grant-date **fair value** of options from an option-pricing model (e.g., Black-Scholes); **no JE** at grant (service not yet rendered)
- **Requisite service period:** recognize compensation cost **straight-line** (cliff vest) over the period employees must serve to earn the award
- **Period-end adjusting JE (emphasis):** each reporting date, **Dr Compensation Expense / Cr Paid-in Capital—Stock Options** for the portion of grant-date FV earned that period
- **Subsequent measurement schedule:** cumulative PIC—Stock Options rolls forward; annual expense = total (adjusted) compensation ÷ service years (or catch-up under as-incurred forfeitures)
- **Exercise (settlement):** **Dr Cash** (exercise price × options exercised) + **Dr PIC—Stock Options** (allocated FV of options exercised) / **Cr Common Stock** (par) + **Cr PIC in Excess of Par** (plug)
- **Expiration (maturity / time lapse):** reclassify remaining **PIC—Stock Options** to **PIC—Expired Stock Options** (no P&L)
- **Forfeitures as incurred:** reduce remaining total compensation when employees leave; period expense = target cumulative − already recognized
- **Estimated forfeitures:** reduce total compensation at outset; expense reduced total ÷ service years (policy choice)
- **Performance conditions:** accrue only if achievement is **probable**; reverse/stop if not probable (full catch-up in year of estimate change)
- **Market conditions:** already in grant-date FV; do **not** stop expense if market target is missed

---

### Q1 — CORE — Full stock-option cycle with period-end adjusting JEs
**LO:** LO 20-2  
**Concept:** Grant-date FV measurement (no JE); period-end compensation adjusting JEs; multi-year expense schedule; exercise settlement JE; expiration reclassification JE  
**Scenario:**  
**Northwind Analytics Inc.** (calendar year-end) grants equity-classified employee stock options.

| Fact | Amount / term |
|---|---|
| **January 1, Year 1** — options granted | **80,000** options (one share each) |
| Common stock par | **$1** per share |
| Exercise (strike) price | **$12** per share |
| Market price on grant date | **$12** per share |
| Grant-date fair value (Black-Scholes), **total** | **$360,000** |
| Vesting | **Cliff** — exercisable after **January 1, Year 4** |
| Requisite service period | **3 years** (Years 1–3) |
| Expiration | **December 31, Year 9**, or when employee leaves, whichever is first |
| Forfeiture policy | Ignore forfeitures for parts (a)–(e) (none occur) |

Additional events:
- **January 1, Year 4:** employees exercise **70,000** options when the market price is **$18** per share. Cash collected = exercise price × options exercised.
- **December 31, Year 9:** the remaining **10,000** vested options expire unexercised.

**Required:**  
a. State total compensation cost and record any **grant-date (January 1, Year 1)** journal entry.  
b. Prepare the **December 31, Year 1 period-end adjusting JE** for compensation expense (emphasis).  
c. Prepare a **subsequent measurement (compensation) schedule** for Years 1–3 showing annual expense, cumulative expense, and ending balance in PIC—Stock Options. Record the Year 2 and Year 3 period-end adjusting JEs.  
d. Prepare the **January 1, Year 4 exercise (settlement) JE**. Show allocation of PIC—Stock Options and the PIC in excess of par plug.  
e. Prepare the **December 31, Year 9 expiration JE** for the unexercised options.  
f. Briefly explain why market price at exercise (**$18**) does **not** change the compensation cost or the amount reclassified from PIC—Stock Options.

**Answer key:**  

**a. Grant date — measurement only; no JE**

Total compensation cost (grant-date FV): **$360,000**  
Intrinsic value on grant date: \((\$12 - \$12) \times 80{,}000 = \$0\), but option-pricing FV is still **$360,000** (time value / volatility).

*January 1, Year 1 — Grant of stock options*

**No journal entry.** Compensation is measured at grant date but recognized over the requisite service period.

**b. December 31, Year 1 — Period-end adjusting JE (emphasis)**

Annual compensation (straight-line cliff):  
\[
\frac{\$360{,}000}{3} = \$120{,}000
\]

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 120,000 | |
| Paid-in Capital—Stock Options | | 120,000 |
| *Year 1 share-based compensation (options)* | | |

**Check:** Dr 120,000 = Cr 120,000. **Balanced.**

**c. Subsequent measurement schedule and Years 2–3 adjusting JEs**

| Year | Compensation expense | Cumulative expense | PIC—Stock Options (EOY) |
|---:|---:|---:|---:|
| 1 | 120,000 | 120,000 | 120,000 |
| 2 | 120,000 | 240,000 | 240,000 |
| 3 | 120,000 | 360,000 | 360,000 |
| **Total** | **360,000** | | |

*December 31, Year 2 — Period-end adjusting JE*

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 120,000 | |
| Paid-in Capital—Stock Options | | 120,000 |

**Check:** Dr 120,000 = Cr 120,000. **Balanced.**

*December 31, Year 3 — Period-end adjusting JE*

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 120,000 | |
| Paid-in Capital—Stock Options | | 120,000 |

**Check:** Dr 120,000 = Cr 120,000. **Balanced.**  
After Year 3: PIC—Stock Options balance = **$360,000** (fully vested).

**d. January 1, Year 4 — Exercise of 70,000 options**

Cash received: \(70{,}000 \times \$12 = \mathbf{\$840{,}000}\)  
PIC—Stock Options reclassified (portion of grant-date FV):  
\[
\$360{,}000 \times \frac{70{,}000}{80{,}000} = \$360{,}000 \times 0.875 = \mathbf{\$315{,}000}
\]  
Common stock at par: \(70{,}000 \times \$1 = \mathbf{\$70{,}000}\)  
PIC in excess of par (to balance):  
\[
\$840{,}000 + \$315{,}000 - \$70{,}000 = \mathbf{\$1{,}085{,}000}
\]

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 840,000 | |
| Paid-in Capital—Stock Options | 315,000 | |
| Common Stock | | 70,000 |
| Paid-in Capital in Excess of Par—Common Stock | | 1,085,000 |
| *Exercise of 70,000 employee stock options* | | |

**Check:** Dr \(840{,}000 + 315{,}000 = 1{,}155{,}000\) = Cr \(70{,}000 + 1{,}085{,}000 = 1{,}155{,}000\). **Balanced.**  
PIC—Stock Options remaining: \(360{,}000 - 315{,}000 = \mathbf{\$45{,}000}\) (for the 10,000 unexercised options).

**e. December 31, Year 9 — Expiration of remaining 10,000 options**

Allocated FV of expired options:  
\[
\$360{,}000 \times \frac{10{,}000}{80{,}000} = \mathbf{\$45{,}000}
\]

| Account | Debit | Credit |
|---|---:|---:|
| Paid-in Capital—Stock Options | 45,000 | |
| Paid-in Capital—Expired Stock Options | | 45,000 |
| *Reclassify PIC for options expired unexercised* | | |

**Check:** Dr 45,000 = Cr 45,000. **Balanced.**  
No P&L impact; equity reclassification only. PIC—Stock Options ends at **$0**.

**f. Market price at exercise**

Compensation cost is locked at **grant-date fair value**. The **$18** market price at exercise affects the employee’s economic gain but does **not** change the employer’s compensation expense already recognized or the **$315,000** of PIC—Stock Options reclassified on exercise.

**Key insight:** Measure options at grant-date FV, expense over the service period with **period-end adjusting JEs** to PIC—Stock Options, then settle via cash + PIC—SO into common equity accounts (or reclassify to expired PIC if never exercised).

---

### Q2 — CORE number variant — Full cycle twin
**LO:** LO 20-2  
**Concept:** Grant measurement; period-end compensation adjusting JEs; four-year expense schedule; full exercise settlement  
**Scenario:**  
**Lakeshore Robotics Corp.** (calendar year-end) grants equity-classified stock options to key engineers.

| Fact | Amount / term |
|---|---|
| **January 1, Year 1** — options granted | **50,000** options |
| Common stock par | **$2** per share |
| Exercise price | **$20** per share |
| Market price on grant date | **$20** per share |
| Grant-date fair value (option-pricing model), **total** | **$480,000** |
| Vesting | **Cliff** — exercisable after **January 1, Year 5** |
| Requisite service period | **4 years** (Years 1–4) |
| Expiration | **December 31, Year 12** |
| Forfeitures | None |

**March 15, Year 5:** employees exercise **all 50,000** options when the market price is **$32** per share.

**Required:**  
a. Total compensation and grant-date entry (if any).  
b. **December 31, Year 1** period-end compensation adjusting JE.  
c. Compensation **schedule** for Years 1–4 (expense and PIC—SO roll-forward).  
d. **March 15, Year 5** exercise JE (all options).  
e. What would the Year 1 adjusting entry have been if the company had **estimated 10% forfeitures** at grant (policy: estimate forfeitures)?

**Answer key:**  

**a. Grant**

Total compensation: **$480,000**.  
*January 1, Year 1:* **No journal entry.**

**b. December 31, Year 1 — Period-end adjusting JE**

Annual expense: \(\$480{,}000 / 4 = \mathbf{\$120{,}000}\)

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 120,000 | |
| Paid-in Capital—Stock Options | | 120,000 |
| *Year 1 option compensation* | | |

**Check:** Dr 120,000 = Cr 120,000. **Balanced.**

**c. Subsequent measurement schedule**

| Year | Expense | Cumulative expense | PIC—Stock Options (EOY) |
|---:|---:|---:|---:|
| 1 | 120,000 | 120,000 | 120,000 |
| 2 | 120,000 | 240,000 | 240,000 |
| 3 | 120,000 | 360,000 | 360,000 |
| 4 | 120,000 | 480,000 | 480,000 |
| **Total** | **480,000** | | |

Years 2–4 each use the same period-end adjusting JE as Year 1 (Dr Comp Exp 120,000 / Cr PIC—SO 120,000). All balance.

**d. March 15, Year 5 — Full exercise**

Cash: \(50{,}000 \times \$20 = \mathbf{\$1{,}000{,}000}\)  
PIC—Stock Options (100%): **$480,000**  
Common stock: \(50{,}000 \times \$2 = \mathbf{\$100{,}000}\)  
PIC in excess of par: \(1{,}000{,}000 + 480{,}000 - 100{,}000 = \mathbf{\$1{,}380{,}000}\)

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 1,000,000 | |
| Paid-in Capital—Stock Options | 480,000 | |
| Common Stock | | 100,000 |
| Paid-in Capital in Excess of Par—Common Stock | | 1,380,000 |
| *Exercise of 50,000 stock options* | | |

**Check:** Dr \(1{,}000{,}000 + 480{,}000 = 1{,}480{,}000\) = Cr \(100{,}000 + 1{,}380{,}000 = 1{,}480{,}000\). **Balanced.**  
PIC—Stock Options after exercise: **$0**. Market price **$32** does not enter the JE.

**e. Estimated 10% forfeitures — Year 1 adjusting JE only**

Expected total compensation: \(\$480{,}000 \times 90\% = \mathbf{\$432{,}000}\)  
Annual expense: \(\$432{,}000 / 4 = \mathbf{\$108{,}000}\)

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 108,000 | |
| Paid-in Capital—Stock Options | | 108,000 |

**Check:** Dr 108,000 = Cr 108,000. **Balanced.**

**Key insight:** Changing only the service-period length, option count, par, and total FV still yields the same structure: no grant JE → equal period-end accruals → exercise reclassifies the full PIC—SO into permanent equity with cash.

---

### Q3 — CORE alternate angle — Period-end catch-up with forfeitures as incurred (and performance condition)
**LO:** LO 20-2  
**Concept:** Period-end adjusting JE when forfeitures are recognized **as incurred**; multi-year schedule with catch-up; performance-condition probability and period-end accrual  
**Scenario:**  
**Cedarline Foods Co.** (calendar year-end) awards options under a service-based plan. Policy: **recognize forfeitures as incurred** (not estimated up front).

| Fact | Amount / term |
|---|---|
| **January 1, Year 1** grant | **40,000** options |
| Common stock par | **$1** |
| Exercise price | **$8** per share |
| Grant-date total fair value | **$240,000** |
| Requisite service period | **3 years** (cliff vest Jan 1, Year 4) |
| Forfeitures | **None in Year 1**; in **Year 2**, employees holding **6,000** options leave (forfeit) |

**Required:**  
a. **December 31, Year 1** period-end compensation adjusting JE.  
b. Compute revised total compensation after the Year 2 forfeitures. Compute the **target** cumulative PIC—Stock Options at Dec 31, Year 2 and the **Year 2 period-end adjusting JE** (catch-up).  
c. Complete the **Years 1–3 compensation schedule** after forfeitures; record the **Year 3** period-end adjusting JE.  
d. **Alternate performance overlay (same original $240,000, 3-year service, ignore forfeitures):** options vest only if sales grow ≥ 5% each year for three years.  
   - (i) Management assesses at Dec 31, Year 1 that achievement is **probable** — Year 1 adjusting JE?  
   - (ii) At Dec 31, Year 2 management concludes achievement is **not probable** — Year 2 adjusting JE (including catch-up of Year 1)?  
e. If instead the award had a **market condition** (e.g., stock price must hit $15) already reflected in the $240,000 grant-date FV, would Year 1 expense still be recognized if the market condition later appears unlikely? (One sentence.)

**Answer key:**  

**a. December 31, Year 1 — Period-end adjusting JE**

\[
\frac{\$240{,}000}{3} = \$80{,}000
\]

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 80,000 | |
| Paid-in Capital—Stock Options | | 80,000 |
| *Year 1 option compensation (no forfeitures yet)* | | |

**Check:** Dr 80,000 = Cr 80,000. **Balanced.**

**b. Year 2 forfeitures as incurred — catch-up period-end JE**

Options remaining: \(40{,}000 - 6{,}000 = 34{,}000\) (85% of grant)  
Revised total compensation: \(\$240{,}000 \times 85\% = \mathbf{\$204{,}000}\)  
After 2 of 3 service years, cumulative PIC—SO **should be**:  
\[
\$204{,}000 \times \frac{2}{3} = \mathbf{\$136{,}000}
\]  
Already recognized in Year 1: **$80,000**  
Year 2 compensation expense: \(136{,}000 - 80{,}000 = \mathbf{\$56{,}000}\)

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 56,000 | |
| Paid-in Capital—Stock Options | | 56,000 |
| *Year 2 compensation adjusted for as-incurred forfeitures* | | |

**Check:** Dr 56,000 = Cr 56,000. **Balanced.**  
EOY Year 2 PIC—Stock Options: \(80{,}000 + 56{,}000 = \mathbf{\$136{,}000}\).

**c. Years 1–3 schedule and Year 3 adjusting JE**

Remaining total to recognize after Year 2: \(204{,}000 - 136{,}000 = \mathbf{\$68{,}000}\) (also \(204{,}000 / 3 = 68{,}000\) for the final third).

| Year | Event | Expense | Cumulative expense | PIC—SO (EOY) |
|---:|---|---:|---:|---:|
| 1 | Full plan | 80,000 | 80,000 | 80,000 |
| 2 | Forfeit 6,000; catch-up | 56,000 | 136,000 | 136,000 |
| 3 | Remainder of revised total | 68,000 | 204,000 | 204,000 |
| **Total** | | **204,000** | | |

*December 31, Year 3 — Period-end adjusting JE*

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 68,000 | |
| Paid-in Capital—Stock Options | | 68,000 |

**Check:** Dr 68,000 = Cr 68,000. **Balanced.**  
Sum of expenses: \(80{,}000 + 56{,}000 + 68{,}000 = 204{,}000\) ✓

**d. Performance condition**

**(i) Probable at Dec 31, Year 1** — accrue as if the service award will vest:

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 80,000 | |
| Paid-in Capital—Stock Options | | 80,000 |

**Check:** Dr 80,000 = Cr 80,000. **Balanced.**

**(ii) Not probable at Dec 31, Year 2** — reverse cumulative accruals (full catch-up in year of estimate change):

| Account | Debit | Credit |
|---|---:|---:|
| Paid-in Capital—Stock Options | 80,000 | |
| Compensation Expense | | 80,000 |
| *Reverse prior accrual; performance not probable* | | |

**Check:** Dr 80,000 = Cr 80,000. **Balanced.**  
(Equivalent presentation: credit Compensation Expense, reducing current-period expense / increasing income.) After this entry, cumulative compensation for the award is **$0**.

**e. Market condition**

Yes — market conditions are embedded in grant-date FV; the company continues to recognize compensation over the service period even if the market target later appears unlikely (unless the award is forfeited for a **service** failure).

**Key insight:** As-incurred forfeitures and performance-probability changes both force a **period-end catch-up** so that cumulative PIC—Stock Options equals (revised total compensation × portion of service elapsed), not merely “last year’s amount again.”

---

### Q4 — MC — Method / classification choices for stock options
**LO:** LO 20-2  
**Concept:** Grant-date measurement; equity-classified option expense vs exercise accounting; performance vs market conditions  

**Question 1:** On the **grant date** of equity-classified employee stock options measured under ASC 718, which statement is correct?  
- A) Debit Compensation Expense for the full grant-date fair value and credit PIC—Stock Options.  
- B) Debit Compensation Expense for intrinsic value only if the options are in the money.  
- C) **No journal entry is recorded; total compensation is measured at grant-date fair value and recognized over the requisite service period.**  
- D) Credit Common Stock for the exercise price times options granted.

**Answer:** **C.** Grant-date FV is measured (e.g., Black-Scholes) but expense is recognized as employees render service via period-end adjusting entries; common stock is recorded only on exercise.  
**LO:** LO 20-2  
**Concept:** Initial recognition (measurement without JE) for stock options  

**Question 2:** Employees exercise fully vested equity-classified options. The employer should:  
- A) Recognize additional compensation expense equal to market price minus exercise price on the exercise date.  
- B) Debit Cash for proceeds, debit PIC—Stock Options for the related grant-date FV allocated to options exercised, and credit Common Stock (par) and PIC in excess of par.  
- C) Debit PIC—Expired Stock Options and credit Cash.  
- D) Reverse all previously recognized compensation expense.

**Answer:** **B.** Exercise is a capital transaction: cash + reclassification of PIC—Stock Options into permanent equity; no additional compensation for the “spread” at exercise under the fair-value method for equity-classified awards.  
**LO:** LO 20-2  
**Concept:** Disposal / settlement JE on option exercise  

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (schedules roll forward; exercise plugs check; forfeiture catch-up 80+56+68=204)
- [x] Core demo path (Demo 20-2 style: grant → expense over service → exercise / expire / forfeitures / performance) — not graded-vesting sidebar-only
- [x] LO + Concept on every item
- [x] MC ≤ 2
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE (emphasis), disposal_maturity_or_settlement_JE
- [x] Original company names and numbers (not textbook Ram Co. demo figures)
