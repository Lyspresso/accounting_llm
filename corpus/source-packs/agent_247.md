# Agent 247 — CORE DEMO — LO 20-2

**Chapter:** 20  
**LO title:** Account for stock options  
**Critical gap LO:** no  
**Emphasis angle:** subsequent_measurement_schedule

## Concept list for this pack
- **Initial recognition / measurement:** measure total compensation cost at the **grant date** using an option-pricing model (e.g., Black-Scholes); **no journal entry** at grant for equity-classified options
- **Subsequent measurement schedule (emphasis):** allocate grant-date fair value **straight-line** over the **requisite service period**; track cumulative expense and PIC—Stock Options rollforward each year
- **Period-end adjusting JE:** Dr Compensation Expense / Cr Paid-in Capital—Stock Options each reporting period
- **Exercise (settlement) JE:** Dr Cash (strike × shares) + Dr PIC—Stock Options (pro rata grant-date cost) / Cr Common Stock + Cr PIC in Excess of Par
- **Expiration (maturity) JE:** reclassify remaining PIC—Stock Options → PIC—Expired Stock Options (within equity; no P&L impact)
- **Forfeitures:** as-incurred (revise cumulative expense in period of forfeiture) or estimate at grant
- **Performance conditions:** accrue only when achievement is **probable**; cumulative catch-up when probability flips
- **Classification:** equity-classified awards credit **equity** (PIC—Stock Options), not a liability

---

### Q1 — CORE — Full option life cycle with multi-year recognition schedule (emphasis)
**LO:** LO 20-2  
**Concept:** Grant-date fair-value measurement (no grant JE); multi-year subsequent measurement schedule with cumulative PIC—Stock Options rollforward; period-end adjusting JE; exercise and expiration settlement JEs  
**Scenario:**  
**Meridian Circuit Works Inc.** (calendar year-end) grants **75,000** employee stock options on **January 1, Year 1**. Each option entitles the holder to purchase one share of Meridian’s **$1 par** common stock at an exercise price of **$18**. The market price of Meridian common on the grant date is also **$18** (intrinsic value = $0). Options cliff-vest after a **four-year** requisite service period (first exercisable **January 1, Year 5**) and expire on **December 31, Year 11** (or earlier if employment ends before vesting). Using a Black-Scholes option-pricing model, management estimates the **fair value of each option at $8.00**, so total grant-date compensation cost is **$600,000**. Meridian’s policy is to recognize forfeitures **as incurred**. Assume all grantees remain employed through the service period unless a later part states otherwise.

On **January 1, Year 5**, employees exercise **56,250** options (75% of the award) when the market price is **$27** per share. The remaining **18,750** options (25%) are never exercised and expire on **December 31, Year 11**.

**Required:**  
a. Compute total compensation cost at the grant date. Record any journal entry on **January 1, Year 1** (grant date).  
b. Prepare the **four-year subsequent measurement (compensation recognition) schedule** showing annual expense and **cumulative** Paid-in Capital—Stock Options. Record the **December 31, Year 1** period-end adjusting entry.  
c. Record the **January 1, Year 5** journal entry for exercise of 56,250 options.  
d. Record the **December 31, Year 11** journal entry for expiration of the remaining 18,750 options.  
e. **Classification:** How is the credit balance in PIC—Stock Options reported during Years 1–4? Does the grant create a liability?

**Answer key:**

**a. Grant-date measurement and initial recognition JE**

Total compensation cost (grant-date fair value)  
= 75,000 options × $8.00 = **$600,000**

*January 1, Year 1 — Grant date*  
**No journal entry.** Equity-classified option cost is measured at grant date but recognized as expense over the requisite service period.

**Check:** No Dr/Cr. **N/A balanced.**

**b. Subsequent measurement schedule (emphasis) and Year 1 period-end JE**

Straight-line annual compensation = $600,000 ÷ 4 years = **$150,000** per year.

| Year | Compensation expense | Cumulative expense | Ending PIC—Stock Options |
|---:|---:|---:|---:|
| Year 1 | $150,000 | $150,000 | $150,000 |
| Year 2 | 150,000 | 300,000 | 300,000 |
| Year 3 | 150,000 | 450,000 | 450,000 |
| Year 4 | 150,000 | 600,000 | 600,000 |
| **Total** | **$600,000** | | **$600,000** |

**PIC—Stock Options rollforward (Years 1–4):**

| | Amount |
|---|---:|
| Beginning balance, Jan 1, Year 1 | $0 |
| + Year 1 recognition | 150,000 |
| Ending, Dec 31, Year 1 | 150,000 |
| + Year 2 recognition | 150,000 |
| Ending, Dec 31, Year 2 | 300,000 |
| + Year 3 recognition | 150,000 |
| Ending, Dec 31, Year 3 | 450,000 |
| + Year 4 recognition | 150,000 |
| Ending, Dec 31, Year 4 (fully vested) | **$600,000** |

*December 31, Year 1 — To record compensation expense*  

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 150,000 | |
| Paid-in Capital—Stock Options | | 150,000 |
| *Grant-date FV $600,000 / 4-year requisite service period* | | |

**Check:** Dr 150,000 = Cr 150,000. **Balanced.**  
(Identical $150,000 entries at Dec 31 of Years 2, 3, and 4.)

**c. Exercise (settlement) JE — January 1, Year 5**

Cash collected = 56,250 × $18 = **$1,012,500**  
PIC—Stock Options released = $600,000 × 75% = **$450,000**  
Common Stock = 56,250 × $1 = **$56,250**  
PIC in Excess of Par (plug) = $1,012,500 + $450,000 − $56,250 = **$1,406,250**

*January 1, Year 5 — To record exercise of stock options*  

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 1,012,500 | |
| Paid-in Capital—Stock Options | 450,000 | |
| Common Stock | | 56,250 |
| Paid-in Capital in Excess of Par—Common Stock | | 1,406,250 |
| *Exercise 56,250 options @ $18; release 75% of PIC—SO* | | |

**Check:** Dr \(1{,}012{,}500 + 450{,}000 = 1{,}462{,}500\); Cr \(56{,}250 + 1{,}406{,}250 = 1{,}462{,}500\). **Balanced.**  
(Market price of $27 is **not** used in the equity issuance entry; grant-date FV already drove compensation expense.)

**d. Expiration (maturity) JE — December 31, Year 11**

Remaining PIC—Stock Options = $600,000 × 25% = **$150,000**

*December 31, Year 11 — To record expiration of unexercised stock options*  

| Account | Debit | Credit |
|---|---:|---:|
| Paid-in Capital—Stock Options | 150,000 | |
| Paid-in Capital—Expired Stock Options | | 150,000 |
| *Reclassify equity within equity; no income statement effect* | | |

**Check:** Dr 150,000 = Cr 150,000. **Balanced.**

**e. Classification / presentation**

- **Paid-in Capital—Stock Options** is reported in **stockholders’ equity** (APIC), not as a liability.  
- **Compensation Expense** is recognized in **net income** over the requisite service period.  
- The grant does **not** create a liability for equity-classified employee stock options under ASC 718; the credit is to equity as services are rendered.

**Key insight:** Measure at grant-date fair value (option-pricing model), book **nothing** at grant, then allocate cost on a **straight-line subsequent measurement schedule** (Dr Comp Exp / Cr PIC—SO each period). Exercise combines cash at the strike with a pro-rata release of PIC—SO into permanent capital; unexercised options reclassify PIC—SO to PIC—Expired (still equity).

---

### Q2 — CORE number variant — Full option life cycle (all numbers changed)
**LO:** LO 20-2  
**Concept:** Number-variant twin: grant-date FV measurement (no grant JE); three-year subsequent measurement schedule; exercise and expiration JEs  
**Scenario:**  
**Redwood Transit Systems Corp.** grants **90,000** stock options on **January 1, Year 1**. Each option allows purchase of one share of **$2 par** common stock at an exercise price of **$25**. Market price on the grant date is **$25**. Options cliff-vest after a **three-year** requisite service period (exercisable beginning January 1, Year 4) and expire December 31, Year 10. An option-pricing model values each option at **$7.50** (total compensation cost **$675,000**). Redwood recognizes forfeitures as incurred; assume no forfeitures through vesting. On **January 1, Year 4**, employees exercise **72,000** options (80%) when the market price is **$36**. The remaining **18,000** options (20%) expire unexercised on **December 31, Year 10**.

**Required:**  
a. Compute total compensation cost and record any **January 1, Year 1** grant-date entry.  
b. Prepare the **three-year subsequent measurement schedule** (annual and cumulative) and the **December 31, Year 1** adjusting JE.  
c. Record the **January 1, Year 4** exercise entry for 72,000 options.  
d. Record the **December 31, Year 10** expiration entry for 18,000 options.  
e. State the PIC—Stock Options balance at December 31, Year 2 and its balance-sheet classification.

**Answer key:**

**a. Grant-date measurement**

Total compensation = 90,000 × $7.50 = **$675,000**  
*January 1, Year 1:* **No journal entry.**

**b. Subsequent measurement schedule and Year 1 adjusting JE**

Annual expense = $675,000 ÷ 3 = **$225,000**

| Year | Compensation expense | Cumulative PIC—Stock Options |
|---:|---:|---:|
| Year 1 | $225,000 | $225,000 |
| Year 2 | 225,000 | 450,000 |
| Year 3 | 225,000 | 675,000 |
| **Total** | **$675,000** | **$675,000** |

*December 31, Year 1 — To record compensation expense*  

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 225,000 | |
| Paid-in Capital—Stock Options | | 225,000 |

**Check:** Dr 225,000 = Cr 225,000. **Balanced.**

**c. Exercise JE — January 1, Year 4**

Cash = 72,000 × $25 = **$1,800,000**  
PIC—Stock Options = $675,000 × 80% = **$540,000**  
Common Stock = 72,000 × $2 = **$144,000**  
PIC in Excess of Par = $1,800,000 + $540,000 − $144,000 = **$2,196,000**

*January 1, Year 4 — To record exercise of stock options*  

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 1,800,000 | |
| Paid-in Capital—Stock Options | 540,000 | |
| Common Stock | | 144,000 |
| Paid-in Capital in Excess of Par—Common Stock | | 2,196,000 |

**Check:** Dr \(1{,}800{,}000 + 540{,}000 = 2{,}340{,}000\); Cr \(144{,}000 + 2{,}196{,}000 = 2{,}340{,}000\). **Balanced.**

**d. Expiration JE — December 31, Year 10**

PIC—Stock Options remaining = $675,000 × 20% = **$135,000**

*December 31, Year 10 — To record expiration of stock options*  

| Account | Debit | Credit |
|---|---:|---:|
| Paid-in Capital—Stock Options | 135,000 | |
| Paid-in Capital—Expired Stock Options | | 135,000 |

**Check:** Dr 135,000 = Cr 135,000. **Balanced.**

**e. Classification at December 31, Year 2**

PIC—Stock Options balance = **$450,000** (after two years of recognition). Reported in **stockholders’ equity** (APIC), not as a liability or asset.

**Key insight:** Same accounting skeleton as Q1 with new counts, par, strike, FV, and service years — always measure at grant FV, expense on the **subsequent measurement schedule**, then settle via exercise or reclassify on expiration.

---

### Q3 — CORE alternate angle — Forfeiture catch-up schedules and performance-condition gates
**LO:** LO 20-2  
**Concept:** Subsequent measurement schedules under as-incurred vs estimated forfeitures (cumulative catch-up); period-end adjusting JEs; performance-condition probability gate with multi-year catch-up  
**Scenario:**  
**Atlas Polymer Packaging Inc.** grants **100,000** stock options on **January 1, Year 1**. Grant-date fair value (option-pricing model) totals **$480,000**. Requisite service period is **three years** (cliff vesting on January 1, Year 4). Common stock is **$1 par**; exercise price is **$16**. Atlas’s default policy is to recognize forfeitures **as incurred**.

**Part A — Forfeitures as incurred (with full recognition schedule)**  
Year 1: no forfeitures.  
During Year 2, employees holding **25,000** options (25% of the award) leave; those options are forfeited. No further forfeitures in Year 3.

**Part B — Estimated forfeitures (alternate policy)**  
Ignore Part A. Instead, at grant Atlas estimates **10%** forfeitures and expenses based on expected awards that will vest. No actual forfeitures occur in Year 1.

**Part C — Performance condition**  
Ignore Parts A–B. Same $480,000 grant-date fair value and three-year service period, but options vest only if Atlas’s annual revenue grows by at least **6%** in each of Years 1–3.  
(i) At December 31, Year 1, management concludes achievement is **not probable**.  
(ii) At December 31, Year 2, management concludes achievement **is probable** (and remains probable through Year 3).

**Required:**  
a. Under Part A, prepare the **three-year subsequent measurement schedule** reflecting the Year 2 forfeiture (revised total cost, annual expense, cumulative expense). Record the **December 31, Year 1** and **December 31, Year 2** adjusting JEs.  
b. Record compensation expense at **December 31, Year 1** under the estimated-forfeiture policy in Part B.  
c. For Part C: state (and record, if any) Year 1 and Year 2 compensation expense under the performance condition.  
d. After full vesting and full expense recognition, if remaining options **expire unexercised**, does expiration reverse previously recognized compensation expense? Explain.

**Answer key:**

**a. Forfeitures as incurred — subsequent measurement schedule and JEs (Part A)**

*Year 1 (no forfeitures):*  
Annual amount = $480,000 ÷ 3 = **$160,000**

*December 31, Year 1 — To record compensation expense*  

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 160,000 | |
| Paid-in Capital—Stock Options | | 160,000 |

**Check:** Dr 160,000 = Cr 160,000. **Balanced.**

Year 2 forfeiture: 25% of options → revised total compensation cost  
= $480,000 × 75% = **$360,000**

**Revised three-year subsequent measurement schedule:**

| Year | Logic | Compensation expense | Cumulative expense / PIC—SO |
|---:|---|---:|---:|
| Year 1 | Original $480,000 × 1/3 | $160,000 | $160,000 |
| Year 2 | Cumulative to $360,000 × 2/3 = $240,000; catch-up from $160,000 | **80,000** | **240,000** |
| Year 3 | Remainder $360,000 − $240,000 | **120,000** | **360,000** |
| **Total** | | **$360,000** | **$360,000** |

Verification: After two years of service, cumulative should be \(360{,}000 \times 2/3 = 240{,}000\); Year 2 expense = \(240{,}000 - 160{,}000 = 80{,}000\).

*December 31, Year 2 — To record compensation expense adjusted for forfeitures*  

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 80,000 | |
| Paid-in Capital—Stock Options | | 80,000 |
| *Cumulative to $240,000 after 25% forfeiture; catch-up from $160,000* | | |

**Check:** Dr 80,000 = Cr 80,000. **Balanced.**  
(Year 3 entry would be Dr Comp Exp 120,000 / Cr PIC—SO 120,000.)

**b. Estimated forfeitures at grant (Part B)**

Expected cost = $480,000 × 90% = **$432,000**  
Year 1 expense = $432,000 ÷ 3 = **$144,000**

*December 31, Year 1 — To record compensation expense (estimated forfeitures)*  

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 144,000 | |
| Paid-in Capital—Stock Options | | 144,000 |

**Check:** Dr 144,000 = Cr 144,000. **Balanced.**

**c. Performance condition (Part C)**

(i) *December 31, Year 1* — Achievement **not probable** → **no compensation expense** recorded (no JE).

(ii) *December 31, Year 2* — Achievement becomes **probable**. Cumulative expense should equal two years of service on full grant-date cost:  
$480,000 × 2/3 = **$320,000**  
(Recognize the full catch-up in Year 2 because probability flipped.)

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 320,000 | |
| Paid-in Capital—Stock Options | | 320,000 |
| *Probable performance condition; cumulative 2/3 of $480,000* | | |

**Check:** Dr 320,000 = Cr 320,000. **Balanced.**  
(Year 3 would recognize the remaining $160,000 if still probable.)

**d. Expiration after full vesting — income-statement effect**

**No.** Expiration after full vesting and full expense recognition does **not** reverse compensation expense. The company reclassifies PIC—Stock Options to PIC—Expired Stock Options **within equity**. Net income is unaffected by the reclassification.

**Key insight:** The **subsequent measurement schedule** is revised with cumulative catch-up when forfeitures are incurred or when a performance condition becomes probable. Expiration never “undoes” expense already earned under the service condition.

---

### Q4 — MC — Measurement and recognition timing at grant date
**LO:** LO 20-2  
**Concept:** Classification of the accounting event at the grant date for equity-classified employee stock options  
**Question:**  
On the **grant date** of an equity-classified employee stock option award measured using an option-pricing model, which statement is correct?

- A) Debit Compensation Expense and credit a liability for the full grant-date fair value.  
- B) Debit Unearned Compensation (contra-equity) and credit Common Stock for the grant-date fair value.  
- C) Measure total compensation cost at grant-date fair value, but record **no** journal entry until expense is recognized over the requisite service period (typically via period-end adjusting entries).  
- D) Measure compensation cost at intrinsic value only; if strike equals market, total cost is zero and remains zero even if an option-pricing model yields a positive fair value.

**Answer:** **C.** Under ASC 718 / core Demo 20-2 treatment, total compensation is measured at grant-date fair value from an option-pricing model, but the journal entry recognizing expense and PIC—Stock Options is made over the **requisite service period**—not at grant. A is wrong (equity-classified awards are not recorded as liabilities). B confuses restricted stock award mechanics with options. D is the outdated intrinsic-value approach; options can have positive fair value even when intrinsic value is zero.

---

### Q5 — MC — Settlement outcomes after full vesting
**LO:** LO 20-2  
**Concept:** Classification of settlement outcomes for vested stock options (exercise vs time-lapse expiration)  
**Question:**  
After a stock option award has fully vested and all related compensation cost has been recognized in PIC—Stock Options, what is the correct accounting when some options **expire unexercised** at the contractual expiration date?

- A) Debit Compensation Expense and credit PIC—Stock Options to reverse the original expense.  
- B) Debit PIC—Stock Options and credit PIC—Expired Stock Options (equity reclassification; no income effect).  
- C) Debit PIC—Stock Options and credit Gain on Expiration of Options.  
- D) Debit Retained Earnings and credit Common Stock for the grant-date fair value of the expired options.

**Answer:** **B.** Expiration is a **within-equity** reclassification from PIC—Stock Options to PIC—Expired Stock Options. Compensation expense is not reversed, and no gain is recognized.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on all entries)
- [x] Math recomputed (600k/4; 75%/25% splits; 675k/3; 80%/20%; 480k×75% catch-up schedule; performance 2/3 catch-up; estimated 10% forfeitures)
- [x] Core demo path (Demo 20-2 stock options), not Expanding Your Knowledge graded-vesting sidebar
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5 classification only)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (emphasis), period_end_adjusting_JE, disposal_maturity_or_settlement_JE (exercise + expiration)
- [x] Original company names and numbers (not textbook Ram Co. / $540,000 demo)
