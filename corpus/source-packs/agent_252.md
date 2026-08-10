# Agent 252 — CORE DEMO — LO 20-7

**Chapter:** 20  
**LO title:** Compute EPS using treasury stock method for options, warrants, and restricted stock  
**Critical gap LO:** no  
**Emphasis angle:** subsequent_measurement_schedule

## Concept list for this pack
- **Treasury stock method (TSM):** assume exercise/issuance of options, warrants, or unvested restricted stock; assume proceeds repurchase treasury shares at the **average market price** for the period; add only **incremental shares** to the diluted EPS denominator
- **Incremental shares:** shares assumed issued − shares assumed repurchased for the treasury
- **Numerator:** generally **no effect** for options, warrants, and unvested restricted stock under the TSM
- **Dilutive vs antidilutive:** if average market price **≤** exercise (strike) price, options/warrants are **antidilutive** (no diluted EPS effect; calculations unnecessary)
- **Unvested restricted stock / RSUs:** assumed proceeds = **remaining unearned compensation** (compensation not yet recognized); only **unvested** awards enter diluted EPS (vested restricted shares are already in basic EPS)
- **Initial recognition JE:** grant-date equity credit for share-based awards (compensation → Paid-in Capital—Stock Options / PIC—Restricted Stock; RSA may debit Unearned Compensation)
- **Subsequent measurement schedule (emphasis):** multi-line TSM incremental-shares schedule and basic → diluted EPS computation schedule
- **Period-end adjusting JE:** recognize share-based compensation for the period; close net income (EPS itself is presentation-only)
- **Settlement / exercise JE:** cash exercise of options/warrants; issuance of shares on RSU vesting

---

### Q1 — CORE — Diluted EPS with stock options (TSM incremental-shares schedule emphasis)
**LO:** LO 20-7  
**Concept:** Treasury stock method incremental-shares schedule for fully vested options; basic and diluted EPS computation schedules; prior grant equity recognition; period-end close; option exercise settlement JE; antidilutive when market < strike  
**Scenario:**  
**Copperfield Logistics Inc.** is a calendar-year public company. For **Year 1**:

| Item | Amount |
|---|---:|
| Net income | $840,000 |
| Common shares outstanding the **entire year** ($1 par) | 280,000 |
| Fully vested employee stock options outstanding **all year** | 50,000 options |
| Exercise (strike) price per option | $18 |
| Average market price of common stock for Year 1 | $30 |
| Balance in Paid-in Capital—Stock Options at Jan 1, Year 1 (related to these options) | $150,000 |

Compensation cost for the 50,000 options was fully recognized in **prior years** (grant-date fair value totaled $150,000). There is no preferred stock and no other potentially dilutive securities. No noncontrolling interest.

On **January 5, Year 2**, employees exercise **all** 50,000 options for cash at the contractual exercise price (settlement of the options after the Year 1 reporting period).

**Required:**  
a. Reconstruct the **prior-period compensation recognition** journal entry that built the $150,000 Paid-in Capital—Stock Options balance (treat as a single cumulative entry for the total grant-date fair value).  
b. Prepare the **treasury stock method incremental shares schedule** for Year 1 (**subsequent measurement schedule — emphasis**).  
c. Prepare a **basic EPS computation schedule** and a **diluted EPS computation schedule** for Year 1. State the EPS amount(s) Copperfield reports on the face of its Year 1 income statement.  
d. Prepare the **December 31, Year 1 period-end closing entry** that transfers net income to retained earnings (use Income Summary).  
e. **Antidilutive alternate:** Recompute using the TSM if the average market price for Year 1 had been **$12** instead of $30. What EPS amount(s) would Copperfield report?  
f. Prepare the **January 5, Year 2 settlement journal entry** when employees exercise all 50,000 options.

**Answer key:**  

**a. Prior-period initial recognition of option equity (cumulative)**

Total grant-date fair value = **$150,000** (given; already fully recognized before Year 1).

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 150,000 | |
| Paid-in Capital—Stock Options | | 150,000 |
| *Recognize total grant-date FV of equity-classified options over the requisite service period (shown cumulatively)* | | |

**Check:** Dr = Cr = **150,000**. **Balanced.**

*Note:* In Year 1 there is **no further** compensation entry for these fully vested options. The equity credit remains in PIC—Stock Options until exercise or expiration.

**b. Treasury stock method — incremental shares schedule (emphasis)**

Assumed proceeds from exercise = 50,000 × $18 = **$900,000**  
Treasury shares assumed repurchased = $900,000 ÷ $30 = **30,000** shares  

| Component | Shares |
|---|---:|
| New shares assumed issued upon exercise of options | 50,000 |
| Less: treasury shares assumed purchased ($900,000 / $30) | (30,000) |
| **Incremental common shares (dilutive)** | **20,000** |

*Check:* 50,000 − 30,000 = 20,000.

Because average market price ($30) **>** exercise price ($18), the options are **in-the-money** and the TSM produces a **positive** incremental share count (dilutive potential).

**c. Basic and diluted EPS computation schedules**

**Basic EPS**

| Component | Amount |
|---|---:|
| Net income available to common stockholders (numerator) | $840,000 |
| Weighted-average common shares outstanding (denominator) | 280,000 |
| **Basic EPS** | **$3.00** |

\[
\text{Basic EPS} = \frac{\$840{,}000}{280{,}000} = \mathbf{\$3.00}
\]

**Diluted EPS (treasury stock method)**

| Component | Amount |
|---|---:|
| Net income available to common (numerator — **no TSM adjustment**) | $840,000 |
| Weighted-average common shares (basic) | 280,000 |
| Add: incremental shares from options (TSM) | 20,000 |
| Diluted weighted-average shares | 300,000 |
| **Diluted EPS** | **$2.80** |

\[
\text{Diluted EPS} = \frac{\$840{,}000}{300{,}000} = \mathbf{\$2.80}
\]

*Check:* \(300{,}000 \times \$2.80 = \$840{,}000\).

**Effects summary**

| | Numerator | Denominator |
|---|---|---|
| Stock options under TSM | No effect | +20,000 incremental shares |

The options are **dilutive** because EPS falls from **$3.00** (basic) to **$2.80** (diluted). Copperfield reports **both** basic EPS of **$3.00** and diluted EPS of **$2.80** on the face of the Year 1 income statement.

**Income statement presentation (partial) — Year 1**

| | |
|---|---:|
| Net income | $840,000 |
| Basic earnings per share | **$3.00** |
| Diluted earnings per share | **$2.80** |

**d. December 31, Year 1 — period-end closing of net income**

| Account | Debit | Credit |
|---|---:|---:|
| Income Summary | 840,000 | |
| Retained Earnings | | 840,000 |
| *Close Year 1 net income to retained earnings* | | |

**Check:** Dr = Cr = **840,000**. **Balanced.**

*Note:* EPS is a **presentation** measure computed from net income and share counts; there is no ledger account that “books” EPS.

**e. Antidilutive alternate — average market price $12**

Assumed proceeds still = 50,000 × $18 = **$900,000**  
Treasury shares at $12 = $900,000 ÷ $12 = **75,000**  
Implied incremental shares = 50,000 − 75,000 = **(25,000)** (negative)

A negative incremental share count would **increase** EPS and is therefore **antidilutive**. When the average market price is **below** the exercise price, the assumed exercise is always antidilutive; the TSM calculation is unnecessary for inclusion.

| | Amount |
|---|---:|
| Basic EPS (reported) | **$3.00** |
| Diluted EPS from options | **Not reported** (options antidilutive) |

Copperfield would report **only basic EPS of $3.00** (and would not reduce EPS for these options). In practice, when all potential common shares are antidilutive, diluted EPS equals basic EPS; the company does not present a lower diluted figure from out-of-the-money options.

**f. January 5, Year 2 — settlement (exercise of all options)**

Cash received = 50,000 × $18 = **$900,000**  
Common stock at par = 50,000 × $1 = **$50,000**  
APIC—Common = ($900,000 + $150,000) − $50,000 = **$1,000,000**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 900,000 | |
| Paid-in Capital—Stock Options | 150,000 | |
| Common Stock ($1 par) | | 50,000 |
| Additional Paid-in Capital—Common | | 1,000,000 |
| *Employees exercise 50,000 options at $18; reclassify PIC—Stock Options* | | |

**Check:** Dr = 900,000 + 150,000 = **1,050,000**; Cr = 50,000 + 1,000,000 = **1,050,000**. **Balanced.**

**Key insight:** Under LO 20-7, options enter **diluted** EPS only through the **treasury stock method**: assume exercise, use cash proceeds to buy treasury shares at the **average market price**, and add only the **incremental** shares to the denominator. The numerator is unchanged. Higher average market prices reduce treasury shares repurchased and **increase** dilution. Out-of-the-money options (market < strike) are **antidilutive**.

---

### Q2 — CORE number variant — Options / warrants TSM twin
**LO:** LO 20-7  
**Concept:** Number-variant twin: TSM incremental-shares schedule for stock purchase warrants; basic and diluted EPS schedules; warrant issuance (initial recognition); period-end close; cash exercise settlement  
**Scenario:**  
**Baycrest Instruments Corp.** is a calendar-year public company. For **Year 1**:

| Item | Amount |
|---|---:|
| Net income | $1,080,000 |
| Common shares outstanding the **entire year** ($2 par) | 360,000 |
| Stock purchase **warrants** outstanding **all year** (issued to investors) | 80,000 warrants |
| Exercise price per warrant | $20 |
| Average market price of common stock for Year 1 | $40 |
| Cash received when warrants were originally issued (prior year) | $200,000 total |

Each warrant is exercisable for **one** share of common stock. Warrants are equity-classified. No employee options, no preferred stock, and no other potentially dilutive securities. No noncontrolling interest.

On **February 1, Year 2**, warrant holders exercise **all** 80,000 warrants for cash at $20 per share.

**Required:**  
a. Prepare the **prior-year initial recognition journal entry** when Baycrest issued the 80,000 warrants for **$200,000** cash (credit Paid-in Capital—Stock Warrants).  
b. Prepare the **treasury stock method incremental shares schedule** for Year 1.  
c. Prepare **basic** and **diluted EPS computation schedules** for Year 1 and state the amounts reported on the income statement.  
d. Prepare the **December 31, Year 1** closing entry for net income.  
e. Prepare the **February 1, Year 2 settlement journal entry** on full exercise of the warrants.

**Answer key:**  

**a. Prior-year initial recognition — issuance of warrants for cash**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 200,000 | |
| Paid-in Capital—Stock Warrants | | 200,000 |
| *Issue 80,000 equity-classified stock purchase warrants for cash* | | |

**Check:** Dr = Cr = **200,000**. **Balanced.**

**b. Treasury stock method — incremental shares schedule**

Assumed proceeds from exercise = 80,000 × $20 = **$1,600,000**  
Treasury shares assumed repurchased = $1,600,000 ÷ $40 = **40,000** shares  

| Component | Shares |
|---|---:|
| New shares assumed issued upon exercise of warrants | 80,000 |
| Less: treasury shares assumed purchased ($1,600,000 / $40) | (40,000) |
| **Incremental common shares** | **40,000** |

*Check:* 80,000 − 40,000 = 40,000. Market ($40) > exercise ($20) → dilutive.

**c. Basic and diluted EPS schedules**

**Basic EPS**

| Component | Amount |
|---|---:|
| Net income available to common stockholders | $1,080,000 |
| Weighted-average common shares outstanding | 360,000 |
| **Basic EPS** | **$3.00** |

\[
\text{Basic EPS} = \frac{\$1{,}080{,}000}{360{,}000} = \mathbf{\$3.00}
\]

**Diluted EPS**

| Component | Amount |
|---|---:|
| Net income available to common (numerator unchanged) | $1,080,000 |
| Basic weighted-average shares | 360,000 |
| Add: incremental shares from warrants (TSM) | 40,000 |
| Diluted weighted-average shares | 400,000 |
| **Diluted EPS** | **$2.70** |

\[
\text{Diluted EPS} = \frac{\$1{,}080{,}000}{400{,}000} = \mathbf{\$2.70}
\]

*Check:* \(400{,}000 \times \$2.70 = \$1{,}080{,}000\).

Warrants are **dilutive** ($3.00 → $2.70). Baycrest reports **basic EPS $3.00** and **diluted EPS $2.70**.

**d. December 31, Year 1 — close net income**

| Account | Debit | Credit |
|---|---:|---:|
| Income Summary | 1,080,000 | |
| Retained Earnings | | 1,080,000 |

**Check:** Dr = Cr = **1,080,000**. **Balanced.**

**e. February 1, Year 2 — settlement (exercise of all warrants)**

Cash = 80,000 × $20 = **$1,600,000**  
Common stock (par) = 80,000 × $2 = **$160,000**  
APIC—Common = ($1,600,000 + $200,000) − $160,000 = **$1,640,000**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 1,600,000 | |
| Paid-in Capital—Stock Warrants | 200,000 | |
| Common Stock ($2 par) | | 160,000 |
| Additional Paid-in Capital—Common | | 1,640,000 |
| *Warrant holders exercise 80,000 warrants at $20* | | |

**Check:** Dr = 1,600,000 + 200,000 = **1,800,000**; Cr = 160,000 + 1,640,000 = **1,800,000**. **Balanced.**

**Key insight:** Warrants use the **same treasury stock method** as options for diluted EPS: assumed exercise proceeds repurchase shares at the average market price; only incremental shares dilute the denominator. Cash originally received for the warrants sits in PIC—Warrants and is reclassified to common equity on exercise—but that cash is **not** part of the TSM proceeds (TSM uses the **exercise price** cash, not the original warrant premium).

---

### Q3 — CORE alternate angle — Unvested restricted stock / RSUs under the TSM
**LO:** LO 20-7  
**Concept:** Unvested RSUs: grant-date measurement and period-end compensation JE; unearned compensation as TSM assumed proceeds; incremental shares schedule; basic vs diluted EPS; share issuance on vesting (settlement)  
**Scenario:**  
**Evergreen Path Pharma Inc.** is a calendar-year public company. On **January 1, Year 1**, Evergreen grants **8,000 restricted stock units (RSUs)** to senior executives. Each RSU entitles the holder to one share of **$1 par** common stock after a **four-year** service vesting period. Grant-date fair value is **$25 per RSU**. Shares are **not** issued until vesting.

Additional Year 1 facts:

| Item | Amount |
|---|---:|
| Net income | $400,000 |
| Common shares outstanding the **entire year** (excludes unvested RSUs) | 200,000 |
| Average market price of common stock for Year 1 | $25 |
| Expected forfeitures | None (ignore forfeitures) |

No preferred stock and no other potentially dilutive securities. No noncontrolling interest. The RSUs are equity-classified time-based awards (not performance-contingent).

**Required:**  
a. Prepare the **January 1, Year 1 memorandum / measurement note** and explain why there is typically **no** journal entry solely for “granting” equity-classified RSUs at grant date. State total compensation cost to be recognized.  
b. Prepare the **December 31, Year 1 period-end adjusting journal entry** to recognize Year 1 compensation cost.  
c. Prepare an **unearned compensation rollforward schedule** for Year 1 (subsequent measurement).  
d. Prepare the **treasury stock method incremental shares schedule** for the unvested RSUs for Year 1.  
e. Prepare **basic** and **diluted EPS computation schedules** for Year 1 and state the amounts reported.  
f. Prepare the **January 1, Year 5 settlement journal entry** when the RSUs fully vest and Evergreen issues 8,000 shares (assume all service conditions were met; cumulative PIC—Restricted Stock equals total grant-date FV).

**Answer key:**  

**a. Grant-date measurement (initial recognition of the award’s cost)**

Total compensation cost = 8,000 × $25 = **$200,000**, measured at **grant date** and recognized over the **4-year** requisite service period.

Equity-classified RSUs generally produce **no balance-sheet journal entry on the grant date itself**; the award is measured at grant-date fair value, and compensation cost is recognized with a credit to equity (Paid-in Capital—Restricted Stock) **as service is rendered**. (Contrast: restricted **stock awards** that issue shares at grant often debit Unearned Compensation / credit Common Stock and APIC at grant.)

**b. December 31, Year 1 — period-end compensation adjusting JE**

Year 1 compensation expense = $200,000 ÷ 4 years = **$50,000**

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense | 50,000 | |
| Paid-in Capital—Restricted Stock | | 50,000 |
| *Recognize Year 1 RSU compensation cost (1/4 of grant-date FV)* | | |

**Check:** Dr = Cr = **50,000**. **Balanced.**

**c. Unearned compensation rollforward schedule (Year 1)**

| Description | Amount |
|---|---:|
| Total grant-date compensation (Jan 1, Year 1) | $200,000 |
| Less: compensation recognized in Year 1 | (50,000) |
| **Remaining unearned compensation (Dec 31, Year 1)** | **$150,000** |

This **$150,000** remaining unearned compensation is the assumed “proceeds” used under the treasury stock method for unvested restricted stock/RSUs (Demo 20-7B approach).

**d. Treasury stock method — incremental shares schedule (unvested RSUs)**

Assumed proceeds = remaining unearned compensation = **$150,000**  
Treasury shares assumed purchased = $150,000 ÷ $25 average market price = **6,000** shares  

| Component | Shares |
|---|---:|
| New shares assumed issued (unvested RSUs) | 8,000 |
| Less: treasury shares assumed purchased ($150,000 / $25) | (6,000) |
| **Incremental common shares** | **2,000** |

*Check:* 8,000 − 6,000 = 2,000.

**Numerator effect:** none. **Denominator effect:** +2,000 incremental shares.

*Note:* Unvested RSUs are **excluded from basic EPS** (shares not yet outstanding). Only the TSM incremental shares enter **diluted** EPS.

**e. Basic and diluted EPS schedules**

**Basic EPS**

| Component | Amount |
|---|---:|
| Net income available to common stockholders | $400,000 |
| Weighted-average common shares outstanding | 200,000 |
| **Basic EPS** | **$2.00** |

\[
\text{Basic EPS} = \frac{\$400{,}000}{200{,}000} = \mathbf{\$2.00}
\]

**Diluted EPS**

| Component | Amount |
|---|---:|
| Net income available to common (no numerator adjustment) | $400,000 |
| Basic weighted-average shares | 200,000 |
| Add: incremental shares from unvested RSUs (TSM) | 2,000 |
| Diluted weighted-average shares | 202,000 |
| **Diluted EPS** | **$1.98** |

\[
\text{Diluted EPS} = \frac{\$400{,}000}{202{,}000} = \mathbf{\$1.9802\ldots \approx \$1.98}
\]

(Rounded to two decimal places, consistent with Demo 20-7B style.)

The RSUs are **dilutive** ($2.00 → $1.98). Evergreen reports **basic EPS $2.00** and **diluted EPS $1.98**.

**f. January 1, Year 5 — settlement (issuance of shares on full vesting)**

After four years, cumulative compensation recognized = $200,000, so PIC—Restricted Stock = **$200,000**. On vesting, Evergreen issues 8,000 shares of $1 par common:

| Account | Debit | Credit |
|---|---:|---:|
| Paid-in Capital—Restricted Stock | 200,000 | |
| Common Stock ($1 par) | | 8,000 |
| Additional Paid-in Capital—Common | | 192,000 |
| *Issue 8,000 shares upon vesting of RSUs* | | |

**Check:** Dr = **200,000**; Cr = 8,000 + 192,000 = **200,000**. **Balanced.**

After vesting, the shares are **outstanding** and enter **basic** EPS for subsequent periods; they are no longer a TSM “potential” share item for diluted-only treatment.

**Key insight:** For **unvested** restricted stock/RSUs, the treasury stock method treats **remaining unearned compensation** as the assumed repurchase proceeds (not an employee cash exercise price). Incremental shares = awards outstanding − (unearned compensation ÷ average market price). Vested restricted shares are already in the basic denominator; unvested awards affect **diluted** EPS only.

---

### Q4 — MC — Dilutive vs antidilutive under the treasury stock method
**LO:** LO 20-7  
**Concept:** Classification of when options enter diluted EPS under the treasury stock method  
**Question:**  
Lakeview Components Co. has fully vested employee stock options outstanding all year. The exercise price is **$28** per share. Which statement correctly describes the effect on **diluted EPS** under the treasury stock method?

- A) If the average market price for the year is **$22**, the options are dilutive and incremental shares equal options outstanding × ($28 − $22)/$22.  
- B) If the average market price for the year is **$35**, assumed proceeds equal options × $28, treasury shares equal those proceeds ÷ $35, and only the **incremental** shares (options − treasury shares) are added to the diluted denominator; the numerator is generally unchanged.  
- C) Options always increase the diluted EPS **numerator** by the after-tax interest savings imputed on assumed proceeds.  
- D) If the average market price equals the exercise price, diluted EPS is always lower than basic EPS by the full option share count.

**Answer:** **B.**  
Under ASC 260 / LO 20-7, the treasury stock method assumes exercise at the beginning of the period (or issuance date), uses cash proceeds at the **strike** to repurchase shares at the **average market price**, and adds only **incremental** shares to the denominator. The numerator is generally **unaffected** for options and warrants.  
- A is wrong: when market ($22) < strike ($28), options are **antidilutive** (not dilutive).  
- C confuses options with the **if-converted** method for convertible debt.  
- D is wrong: if market = strike, treasury shares equal options issued, incremental shares = **0**, so diluted EPS equals basic EPS (no dilution from those options).

---

### Q5 — MC — Assumed proceeds for unvested restricted stock
**LO:** LO 20-7  
**Concept:** Classification of the amount used as treasury-stock-method proceeds for unvested restricted stock  
**Question:**  
In computing diluted EPS for **unvested time-based restricted stock** under the treasury stock method, the assumed proceeds used to repurchase treasury shares at the average market price equal:

- A) The cash exercise price the employee will pay at vesting (always equal to par value).  
- B) The **remaining unearned (unrecognized) compensation cost** on the unvested award at the reporting date (after recognizing current-period compensation).  
- C) The grant-date fair value of the award **without** reducing for compensation already recognized.  
- D) Zero, because restricted stock never affects diluted EPS—only basic EPS.

**Answer:** **B.**  
Per LO 20-7 / Demo 20-7B, assumed proceeds for unvested restricted stock equal **compensation not yet expensed** (remaining unearned compensation). That amount ÷ average market price = treasury shares assumed purchased; incremental shares = restricted shares − treasury shares.  
- A is wrong for typical restricted stock (no cash exercise price like options).  
- C overstates proceeds (and understates incremental shares) by ignoring compensation already recognized.  
- D is wrong: unvested awards affect **diluted** EPS; vested restricted shares are in **basic** EPS.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (incremental shares, basic/diluted EPS, settlement amounts)
- [x] Core demo not sidebar-only (Demo 20-7A options/warrants TSM; Demo 20-7B unvested restricted stock TSM — not Expanding Your Knowledge partial-year exercise sidebars)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5 only)
- [x] Emphasis on subsequent_measurement_schedule (TSM incremental-shares + EPS schedules in Q1–Q3)
- [x] Angles covered: initial_recognition_JE (option compensation / warrant cash issue / RSU measurement), subsequent_measurement_schedule, period_end_adjusting_JE (close NI; RSU compensation), disposal_maturity_or_settlement_JE (option/warrant exercise; RSU share issuance)
