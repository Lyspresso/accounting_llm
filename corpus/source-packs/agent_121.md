# Agent 121 — CORE DEMO — LO 20-7

**Chapter:** 20  
**LO title:** Compute EPS using treasury stock method for options, warrants, and restricted stock  
**Critical gap LO:** no

## Concept list for this pack
- **Treasury stock method (options & warrants):** assume exercise at beginning of period (or issuance if later); use exercise proceeds to repurchase common at **average market price**; add only **incremental** shares to diluted denominator
- **Numerator:** generally **no effect** on diluted EPS for options, warrants, or unvested restricted stock (time-based)
- **Dilutive vs antidilutive:** if average market price ≤ exercise (strike) price, options/warrants are **antidilutive** — exclude from diluted EPS; report basic only when all PCS are antidilutive
- **Unvested restricted stock (TSM):** treat as potential shares; assumed “proceeds” = **unearned compensation remaining** (total grant-date fair value − compensation already recognized); repurchase at average market price; add incremental shares
- **Initial recognition JE (restricted stock awards):** at grant, record common stock/APIC and **Unearned Compensation** (equity contra) for total grant-date FV
- **Period-end adjusting JE:** recognize compensation expense over the requisite service period; reduces unearned compensation and thus increases TSM incremental shares in later years
- **Subsequent measurement schedule:** multi-year roll-forward of unearned compensation and year-by-year TSM incremental shares
- **Settlement / exercise JE:** actual exercise of options or warrants — cash in, issue common stock; exercised shares enter basic WA from exercise date forward (diluted still reflects potential while outstanding)
- **Classification / presentation:** report **basic and diluted EPS** with equal prominence when dilutive PCS exist; disclose reconciliation of shares; exclude antidilutive securities from diluted

---

### Q1 — CORE — Options + unvested restricted stock: grant JE, TSM schedules, basic & diluted EPS
**LO:** LO 20-7  
**Concept:** Initial recognition JE for restricted stock award; period-end compensation JE; treasury stock method schedules for fully vested options and unvested RS; basic and diluted EPS presentation  
**Scenario:**  
**Cedarline Analytics Corp.** (calendar-year public company) has a complex capital structure for Year 1.

| Fact | Amount / term |
|---|---|
| Net income (Year 1) | **$720,000** |
| Preferred dividends | **$0** |
| Weighted-average **common** shares for basic EPS (entire year) | **240,000** |
| Fully vested employee stock options outstanding all year | **30,000** options |
| Option exercise (strike) price | **$16** per share |
| Average market price of common (Year 1) | **$40** per share |
| Restricted stock awards granted | **January 1, Year 1** |
| Restricted shares granted (unvested; **excluded** from basic WA) | **8,000** shares, **$1** par |
| Grant-date fair value per restricted share | **$25** |
| Requisite service (cliff vest) | **4 years** |
| Common stock legal form of RS award | Shares issued at grant but restricted until vest |

Assume options were granted and fully vested in a prior year (no current option compensation expense). No other potential common shares. Average market price for TSM on both options and restricted stock is **$40**.

**Required:**  
a. Prepare the **January 1, Year 1 initial recognition journal entry** for the restricted stock award (total compensation at grant-date fair value).  
b. Prepare the **December 31, Year 1 period-end adjusting journal entry** for restricted-stock compensation expense.  
c. Compute **basic EPS** for Year 1.  
d. Prepare the **treasury stock method schedule** for the stock options and compute incremental shares.  
e. Prepare the **treasury stock method schedule** for the unvested restricted stock and compute incremental shares.  
f. Compute **diluted EPS** for Year 1. State what EPS amount(s) Cedarline reports on the face of the income statement and whether the options/RS are dilutive.

**Answer key:**  

**a. January 1, Year 1 — initial recognition of restricted stock award**

Total compensation cost = 8,000 × $25 = **$200,000**

| Account | Debit | Credit |
|---|---:|---:|
| Unearned Compensation—Equity (contra equity) | 200,000 | |
| Common Stock ($1 par × 8,000) | | 8,000 |
| Paid-in Capital in Excess of Par—Common | | 192,000 |
| *Record restricted stock award at grant-date fair value* | | |

**Check:** Dr = Cr = 200,000. **Balanced.**

**b. December 31, Year 1 — period-end compensation adjusting JE**

Annual compensation expense = $200,000 / 4 years = **$50,000**

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense—Restricted Stock | 50,000 | |
| Unearned Compensation—Equity | | 50,000 |
| *Recognize Year 1 service-period compensation cost* | | |

**Check:** Dr = Cr = 50,000. **Balanced.**  
Unearned compensation remaining (for TSM) = $200,000 − $50,000 = **$150,000**.

**c. Basic EPS**

\[
\text{Basic EPS} = \frac{\$720{,}000}{240{,}000} = \mathbf{\$3.00}
\]

(Unvested restricted shares are **not** in the basic denominator.)

**d. Treasury stock method — stock options**

| Step | Amount |
|---|---:|
| Shares assumed issued on exercise | 30,000 |
| Assumed proceeds (30,000 × $16) | $480,000 |
| Shares assumed repurchased at avg market ($480,000 ÷ $40) | 12,000 |
| **Incremental shares** (30,000 − 12,000) | **18,000** |

- Numerator effect: **none**  
- Denominator effect: **+18,000** incremental common shares  

**e. Treasury stock method — unvested restricted stock**

| Step | Amount |
|---|---:|
| Shares assumed issued on vesting | 8,000 |
| Unearned compensation remaining ($200,000 − $50,000) | $150,000 |
| Shares assumed repurchased at avg market ($150,000 ÷ $40) | 3,750 |
| **Incremental shares** (8,000 − 3,750) | **4,250** |

- Numerator effect: **none**  
- Denominator effect: **+4,250** incremental common shares  

**f. Diluted EPS and presentation**

Diluted weighted-average shares = 240,000 + 18,000 + 4,250 = **262,250**

\[
\text{Diluted EPS} = \frac{\$720{,}000}{262{,}250} = \mathbf{\$2.75}
\]

(Exact: $720,000 ÷ 262,250 = $2.7455… → **$2.75** rounded to nearest cent.)

Both options and restricted stock are **dilutive** because diluted EPS ($2.75) < basic EPS ($3.00).  
Cedarline reports **both basic EPS $3.00 and diluted EPS $2.75** on the face of the income statement with equal prominence.

**Key insight:** Under the treasury stock method, diluted EPS never adds the full option or unvested RS share count—only the **incremental** shares after assumed repurchase at average market price. For unvested restricted stock, “proceeds” equal **remaining unearned compensation**, which declines as period-end compensation expense is recognized.

---

### Q2 — CORE number variant — Options, warrants, and restricted stock TSM twin
**LO:** LO 20-7  
**Concept:** Number-variant twin: initial RS grant JE; year-end compensation JE; TSM for options, warrants, and unvested RS; basic vs diluted EPS  
**Scenario:**  
**Pinnacle Wireworks Inc.** reports the following for Year 1:

| Fact | Amount / term |
|---|---|
| Net income | **$945,000** |
| Preferred dividends | **$0** |
| Weighted-average common shares (basic) | **315,000** |
| Fully vested options outstanding all year | **35,000** options |
| Option exercise price | **$20** |
| Warrants outstanding all year | **9,000** warrants |
| Warrant exercise price | **$28** |
| Average market price of common | **$35** |
| Restricted stock granted Jan 1, Year 1 | **12,000** shares, **$1** par |
| Grant-date FV per RS share | **$21** |
| Vesting (service) | **3 years** cliff |
| Unvested RS in basic WA? | **No** |

Options and warrants fully vested from prior periods (no current option/warrant compensation cost).

**Required:**  
a. Prepare the **January 1, Year 1 initial recognition JE** for the restricted stock award.  
b. Prepare the **December 31, Year 1 compensation adjusting JE**.  
c. Compute **basic EPS**.  
d. Complete TSM schedules for (1) options, (2) warrants, and (3) unvested restricted stock; state incremental shares for each.  
e. Compute **diluted EPS** and state presentation.  
f. Briefly explain why warrants use the **same** treasury stock method mechanics as options.

**Answer key:**  

**a. January 1, Year 1 — initial recognition**

Total compensation = 12,000 × $21 = **$252,000**

| Account | Debit | Credit |
|---|---:|---:|
| Unearned Compensation—Equity | 252,000 | |
| Common Stock ($1 × 12,000) | | 12,000 |
| Paid-in Capital in Excess of Par—Common | | 240,000 |
| *Restricted stock at grant-date fair value* | | |

**Check:** Dr = Cr = 252,000. **Balanced.**

**b. December 31, Year 1 — period-end adjusting JE**

Expense = $252,000 / 3 = **$84,000**

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense—Restricted Stock | 84,000 | |
| Unearned Compensation—Equity | | 84,000 |

**Check:** Dr = Cr = 84,000. **Balanced.**  
Unearned remaining = $252,000 − $84,000 = **$168,000**.

**c. Basic EPS**

\[
\text{Basic EPS} = \frac{\$945{,}000}{315{,}000} = \mathbf{\$3.00}
\]

**d. Treasury stock method schedules**

**(1) Options**

| Step | Amount |
|---|---:|
| Shares assumed issued | 35,000 |
| Proceeds (35,000 × $20) | $700,000 |
| Treasury shares ($700,000 ÷ $35) | **20,000** |
| Incremental shares | 35,000 − 20,000 = **15,000** |

**(2) Warrants**

| Step | Amount |
|---|---:|
| Shares assumed issued | 9,000 |
| Proceeds (9,000 × $28) | $252,000 |
| Treasury shares ($252,000 ÷ $35) | **7,200** |
| Incremental shares | 9,000 − 7,200 = **1,800** |

**(3) Unvested restricted stock**

| Step | Amount |
|---|---:|
| Shares assumed issued | 12,000 |
| Unearned remaining | $168,000 |
| Treasury shares ($168,000 ÷ $35) | **4,800** |
| Incremental shares | 12,000 − 4,800 = **7,200** |

Numerator effect for all three: **$0**.

**e. Diluted EPS**

Diluted WA shares = 315,000 + 15,000 + 1,800 + 7,200 = **339,000**

\[
\text{Diluted EPS} = \frac{\$945{,}000}{339{,}000} = \mathbf{\$2.79}
\]

($945,000 ÷ 339,000 = $2.7876… → **$2.79** rounded to nearest cent.)

All three instruments are dilutive (diluted < basic). Pinnacle reports **basic EPS $3.00** and **diluted EPS $2.79**.

**f. Warrants vs options**  
Warrants are treated like options under ASC 260: assume exercise, apply proceeds to repurchase at average market price, and include only **incremental** shares. Neither adjusts the diluted EPS **numerator**.

**Key insight:** Changing every input (NI, WA shares, strikes, market price, RS count and vesting years) still applies the same TSM engine: issued − (proceeds or unearned ÷ average market price).

---

### Q3 — CORE alternate angle — Multi-year RS TSM schedule; antidilutive options; warrant settlement JE
**LO:** LO 20-7  
**Concept:** Subsequent measurement schedule of unearned compensation and year-by-year TSM incremental shares; antidilutive options excluded; warrant exercise (settlement) journal entry; classification/presentation when some PCS are antidilutive  
**Scenario:**  
**Summit Harbor Brands Co.** has the following share-based and EPS facts.

**Restricted stock (ongoing):**  
On **January 1, Year 1**, Summit granted **6,000** restricted common shares ($1 par) to executives when the grant-date fair value was **$30** per share. The awards cliff-vest after **3 years** of service. Summit recognizes compensation cost straight-line. For Years 1–3, the **average market price** of common stock is:

| Year | Average market price |
|---:|---:|
| 1 | $30 |
| 2 | $40 |
| 3 | $45 |

**Year 3 EPS package (in addition to the RS above):**  
| Fact | Amount |
|---|---|
| Net income Year 3 | **$560,000** |
| Preferred dividends | **$0** |
| Basic weighted-average common shares Year 3 | **200,000** (excludes still-unvested RS until vest date) |
| Fully vested options outstanding all of Year 3 | **10,000** options @ **$50** exercise price |
| Average market price Year 3 (for options) | **$45** (same as table) |
| Warrants outstanding Jan 1–June 30, Year 3 | **4,000** warrants @ **$25** exercise |
| Warrants **exercised** | **July 1, Year 3** for cash at the $25 strike |
| Average market price Jan 1–June 30 (for pre-exercise TSM on warrants) | **$40** |
| Shares issued on warrant exercise included in basic WA | From July 1: 4,000 × 6/12 = **2,000** already **included** in the 200,000 basic WA figure above |

**Required:**  
a. Prepare the **January 1, Year 1 initial recognition JE** for the restricted stock grant.  
b. Prepare a **subsequent measurement schedule** for Years 1–3 showing: annual compensation expense, ending unearned compensation, TSM treasury shares, and **incremental shares** for diluted EPS each year (using that year’s average market price). Also show each year’s period-end compensation **adjusting JE** amounts (Dr/Cr).  
c. For **Year 3 only**, apply the treasury stock method to the **options**. Are they dilutive or antidilutive?  
d. For **Year 3**, compute the diluted-EPS **denominator adjustment** for warrants for the **pre-exercise** period (treasury stock method, time-weighted), given exercise on July 1.  
e. Prepare the **July 1, Year 3 settlement (exercise) journal entry** for the warrants (common $1 par).  
f. Compute **Year 3 basic EPS** and **Year 3 diluted EPS** (include dilutive RS incremental shares from the Year-3 row of your schedule; include warrant pre-exercise incremental shares if dilutive; exclude antidilutive options). State presentation/disclosure for antidilutive options.

**Answer key:**  

**a. January 1, Year 1 — initial recognition**

Total compensation = 6,000 × $30 = **$180,000**

| Account | Debit | Credit |
|---|---:|---:|
| Unearned Compensation—Equity | 180,000 | |
| Common Stock | | 6,000 |
| Paid-in Capital in Excess of Par—Common | | 174,000 |

**Check:** Dr = Cr = 180,000. **Balanced.**

**b. Subsequent measurement schedule — compensation and TSM (restricted stock)**

Annual expense each year = $180,000 / 3 = **$60,000**

Each year-end adjusting JE (Years 1, 2, and 3):

| Account | Debit | Credit |
|---|---:|---:|
| Compensation Expense—Restricted Stock | 60,000 | |
| Unearned Compensation—Equity | | 60,000 |

**Check:** Dr = Cr = 60,000 each year. **Balanced.**

| Year | Beg. unearned | Comp. expense | End. unearned | Avg mkt | Treasury shares (unearned ÷ mkt) | Incremental shares (6,000 − tre) |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | $180,000 | $60,000 | $120,000 | $30 | 4,000 | **2,000** |
| 2 | 120,000 | 60,000 | 60,000 | 40 | 1,500 | **4,500** |
| 3 | 60,000 | 60,000 | **0** | 45 | 0 | **6,000** |

Year 2: $60,000 ÷ $40 = **1,500** treasury; incremental = 6,000 − 1,500 = **4,500**.  
Year 3: after full expense, unearned = $0 → treasury shares = 0 → full **6,000** incremental (still unvested until Dec 31 cliff; if vesting occurs Dec 31 Year 3 after year-end, diluted includes 6,000; once vested and unrestricted, shares move into basic going forward).

**Roll-forward check:** $180,000 − 3 × $60,000 = **$0** ending unearned after Year 3.

**c. Year 3 options — antidilutive test**

Average market **$45** < exercise **$50** → assumed exercise would **increase** EPS (negative incremental shares).  
Options are **antidilutive**. **Exclude** from diluted EPS; no TSM calculation required for inclusion.

**d. Year 3 warrants — pre-exercise TSM (½ year)**

For Jan 1–June 30 (options still outstanding potential):

| Step | Amount |
|---|---:|
| Shares assumed issued | 4,000 |
| Proceeds (4,000 × $25) | $100,000 |
| Treasury shares ($100,000 ÷ $40) | 2,500 |
| Net incremental (full-year equivalent if outstanding all year) | 1,500 |
| **Time-weighted for 6/12** | 1,500 × 6/12 = **750** |

Denominator add for diluted EPS: **+750** shares.  
(Actual shares issued July 1 are already reflected in basic WA for the post-exercise half-year.)

**e. July 1, Year 3 — warrant exercise (settlement) JE**

Cash received = 4,000 × $25 = **$100,000**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 100,000 | |
| Common Stock ($1 × 4,000) | | 4,000 |
| Paid-in Capital in Excess of Par—Common | | 96,000 |
| *Record cash exercise of warrants* | | |

**Check:** Dr = Cr = 100,000. **Balanced.**

**f. Year 3 basic and diluted EPS**

Basic EPS:

\[
\text{Basic EPS} = \frac{\$560{,}000}{200{,}000} = \mathbf{\$2.80}
\]

Diluted denominator adjustments (Year 3):  
- Restricted stock incremental (from schedule): **+6,000**  
- Warrants pre-exercise TSM: **+750**  
- Options: **0** (antidilutive)

Diluted WA shares = 200,000 + 6,000 + 750 = **206,750**

\[
\text{Diluted EPS} = \frac{\$560{,}000}{206{,}750} \approx \mathbf{\$2.71}
\]

($560,000 ÷ 206,750 ≈ $2.7086 → **$2.71**.)

**Presentation / disclosure:**  
Report **basic EPS $2.80** and **diluted EPS $2.71**. The **10,000 out-of-the-money options** are **excluded** from diluted weighted-average shares and typically disclosed as antidilutive securities excluded from the diluted EPS computation.

**Key insight:** As unearned compensation declines over the vesting period, TSM **incremental shares for restricted stock rise** toward the full award. Out-of-the-money options never enter diluted EPS. Actual warrant exercise is a cash-and-equity settlement JE; diluted EPS still picks up **pre-exercise** incremental shares for the period the warrants were outstanding.

---

### Q4 — MC — Dilutive vs antidilutive under the treasury stock method
**LO:** LO 20-7  
**Concept:** Classification — when options/warrants are included in diluted EPS under the treasury stock method  
**Question:**  
Under the treasury stock method, which statement correctly describes when outstanding employee stock options are included in **diluted** EPS?

- A) Always include all option shares in the diluted denominator, regardless of market price.  
- B) Include options only when the average market price **exceeds** the exercise price (in-the-money), using incremental shares after assumed repurchase.  
- C) Include options only when the exercise price exceeds the average market price, and add the full option share count.  
- D) Include options in diluted EPS by adding cash exercise proceeds to the **numerator** and all option shares to the denominator.

**Answer:** **B.**  
If average market price > exercise price, assumed proceeds repurchase fewer shares than issued → positive incremental shares that dilute EPS. If market ≤ exercise, options are antidilutive and are excluded. The numerator is generally **not** adjusted for options; only the denominator is adjusted for incremental shares.

---

### Q5 — MC — Restricted stock “proceeds” in the treasury stock method
**LO:** LO 20-7  
**Concept:** Classification of assumed proceeds for unvested restricted stock in diluted EPS  
**Question:**  
In applying the treasury stock method to **unvested** time-based restricted stock for diluted EPS, the amount treated as assumed proceeds used to repurchase treasury shares is:

- A) The cash employees will pay at vesting (always zero for pure RS awards), so incremental shares always equal the full restricted share count.  
- B) The **grant-date total compensation cost still unearned** (not yet recognized as expense) at the reporting date.  
- C) The current stock price times restricted shares, with no reduction for unearned compensation.  
- D) Only the compensation expense recognized in the **current** period (not the remaining unearned balance).

**Answer:** **B.**  
ASC 260 / LO 20-7: unearned (remaining) compensation is the assumed “proceeds” for the TSM repurchase; incremental shares = restricted shares − (unearned compensation ÷ average market price).

---

### Self-check
- [x] Every JE balances (RS grant, period-end compensation, warrant exercise)
- [x] Math recomputed (TSM schedules, basic/diluted EPS, multi-year unearned roll-forward)
- [x] Core demo not sidebar-only (Demo 20-7A options path; Demo 20-7B restricted stock path; antidilutive exclusion; presentation)
- [x] LO + Concept on every item
- [x] MC ≤ 2
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE (warrant exercise), classification_presentation_or_disclosure, number_variant_twin
