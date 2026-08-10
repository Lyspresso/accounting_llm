# Agent 123 — CORE DEMO — LO 20-9

**Chapter:** 20  
**LO title:** Compute EPS given multiple securities and describe EPS financial statement presentation  
**Critical gap LO:** no

## Concept list for this pack
- **Ranking (most dilutive first):** Compute **earnings per incremental share** (numerator effect ÷ denominator effect) for each potentially dilutive security; include in diluted EPS from **lowest** ratio to **highest**
- **Options/warrants first:** Treasury-stock-method securities usually rank first because the numerator effect is **$0**
- **Sequential dilution schedule:** After ranking, add one security at a time; keep a security only if tentative diluted EPS **declines** (dilutive); stop when EPS **increases** (antidilutive)
- **If-converted numerator effects:** Add back convertible preferred dividends; add back convertible bond interest **net of tax**
- **Treasury stock method denominator:** Incremental shares = options assumed exercised − shares repurchasable with proceeds at **average** market price
- **Period-end preferred dividend JE:** Declared preferred dividends reduce income available to common for **basic** EPS (and are added back if the preferred is convertible and dilutive)
- **Antidilutive exclusion:** Securities that raise tentative EPS are **excluded** from diluted EPS but still disclosed as potentially dilutive
- **Financial statement presentation:** Complex capital structure → **basic and diluted** EPS with equal prominence for income from continuing operations and net income; discontinued operations EPS on face or in notes; control number for dilutiveness is **income from continuing operations**
- **Number-variant twin:** Same multi-security ranking and sequential schedule with fully changed amounts

---

### Q1 — CORE — Multi-security diluted EPS: ranking, sequential schedule, period-end preferred JE, presentation
**LO:** LO 20-9  
**Concept:** Initial ranking of potentially dilutive securities by earnings per incremental share; sequential dilution schedule; period-end preferred dividend JE; face presentation of basic and diluted EPS  
**Scenario:**  
**Northvale Industrial Corp.** has a **complex capital structure**. For the year ended December 31, Year 1:

| Item | Amount |
|---|---:|
| Net income | $420,000 |
| Weighted-average common shares outstanding (entire year) | 250,000 |
| Income tax rate | 25% |

There are **no** discontinued operations. All of the following securities were outstanding the **entire year**; none were exercised or converted:

1. **Employee stock options:** 8,000 options to purchase one common share each at an exercise price of **$15**. Average market price of common stock during Year 1: **$25**.
2. **6% cumulative convertible preferred stock:** 5,000 shares, **$100 par**. Each preferred share is convertible into **4** common shares. Preferred dividends were declared and paid for the full year.
3. **Series B convertible bonds:** **$600,000** face, **4%** coupon, issued at par. Each **$1,000** bond is convertible into **30** common shares. Interest was paid for the full year.
4. **Series A convertible bonds:** **$400,000** face, **8%** coupon, issued at par. Each **$1,000** bond is convertible into **12** common shares. Interest was paid for the full year.

**Required:**  
a. Prepare the **December 31, Year 1 period-end journal entry** to record the annual preferred dividend (cash paid the same day). Show that Dr = Cr.  
b. Compute the **numerator effect**, **denominator effect**, and **earnings per incremental share** for each potentially dilutive security. **Rank** the securities from most dilutive to least dilutive.  
c. Compute **basic EPS** for Year 1.  
d. Prepare a **sequential diluted EPS schedule** (most dilutive → least dilutive). Identify which securities are dilutive vs antidilutive and state **diluted EPS**.  
e. Show the **financial statement presentation** of EPS on the face of the income statement.

**Answer key:**  

**a. December 31, Year 1 — period-end preferred dividend JE**

Annual preferred dividends = 5,000 × $100 × 6% = **$30,000**

| Account | Debit | Credit |
|---|---:|---:|
| Preferred Dividends (or Retained Earnings) | 30,000 | |
| Cash | | 30,000 |
| *Declare and pay annual 6% cumulative convertible preferred dividend* | | |

**Check:** Dr = Cr = **30,000**. Balanced.

**b. Incremental effects and ranking (initial setup of diluted EPS inputs)**

**Stock options (treasury stock method)**  
Proceeds if exercised = 8,000 × $15 = **$120,000**  
Shares assumed repurchased = $120,000 ÷ $25 = **4,800**  
Incremental shares = 8,000 − 4,800 = **3,200**  
Numerator effect = **$0**  
Earnings per incremental share = $0 ÷ 3,200 = **$0.00**

**Series B convertible bonds (if-converted)**  
Pretax interest = $600,000 × 4% = **$24,000**  
After-tax interest add-back = $24,000 × (1 − 0.25) = **$18,000**  
Conversion shares = 600 bonds × 30 = **18,000**  
Earnings per incremental share = $18,000 ÷ 18,000 = **$1.00**

**Convertible preferred (if-converted)**  
Preferred dividends add-back = **$30,000**  
Conversion shares = 5,000 × 4 = **20,000**  
Earnings per incremental share = $30,000 ÷ 20,000 = **$1.50**

**Series A convertible bonds (if-converted)**  
Pretax interest = $400,000 × 8% = **$32,000**  
After-tax interest add-back = $32,000 × 0.75 = **$24,000**  
Conversion shares = 400 bonds × 12 = **4,800**  
Earnings per incremental share = $24,000 ÷ 4,800 = **$5.00**

**Ranking (most dilutive → least dilutive)**

| Rank | Security | Δ Income | Δ Shares | Earnings per incremental share |
|---:|---|---:|---:|---:|
| 1 | Stock options | $0 | 3,200 | **$0.00** |
| 2 | Series B convertible bonds | 18,000 | 18,000 | **1.00** |
| 3 | Convertible preferred stock | 30,000 | 20,000 | **1.50** |
| 4 | Series A convertible bonds | 24,000 | 4,800 | **5.00** |

**c. Basic EPS**

Income available to common = $420,000 − $30,000 = **$390,000**

\[
\text{Basic EPS} = \frac{\$390{,}000}{250{,}000} = \mathbf{\$1.56}
\]

**d. Sequential diluted EPS schedule**

| Step | Net income available to common | Weighted-average shares | Per share | Assessment |
|---|---:|---:|---:|---|
| Basic EPS | $390,000 | 250,000 | **$1.56** | — |
| + Stock options | 390,000 | 253,200 | **1.54** | Dilutive (1.54 < 1.56) |
| + Series B bonds | 408,000 | 271,200 | **1.50** | Dilutive (1.50 < 1.54) |
| + Convertible preferred | 438,000 | 291,200 | **1.50** | Dilutive (1.5041 < 1.5044) |
| + Series A bonds | 462,000 | 296,000 | **1.56** | **Antidilutive** (1.56 > 1.50) |

Detail:
- Options: $390,000 / 253,200 = **$1.5403** → dilutive  
- Series B: ($390,000 + $18,000) / (253,200 + 18,000) = $408,000 / 271,200 = **$1.5044** → dilutive  
- Preferred: ($408,000 + $30,000) / (271,200 + 20,000) = $438,000 / 291,200 = **$1.5041** → dilutive  
- Series A: ($438,000 + $24,000) / (291,200 + 4,800) = $462,000 / 296,000 = **$1.5608** → **antidilutive** (exclude)

**Diluted EPS** uses income **$438,000** and shares **291,200**:

\[
\text{Diluted EPS} = \frac{\$438{,}000}{291{,}200} = \mathbf{\$1.50}
\]

Series A is **excluded** from diluted EPS (still disclosed as potentially dilutive / antidilutive).

**e. Income statement presentation (face)**

| | |
|---|---:|
| Basic earnings per share | **$1.56** |
| Diluted earnings per share | **1.50** |

(Complex capital structure → dual presentation with equal prominence.)

**Key insight:** Maximum dilution requires ranking by **lowest earnings per incremental share** first, then adding securities **only while** tentative EPS continues to fall. A security that is dilutive in isolation (or lower-ranked) can become **antidilutive** after more dilutive securities are already included—Series A is excluded for that reason.

---

### Q2 — CORE number variant — Multi-security ranking and sequential diluted EPS twin
**LO:** LO 20-9  
**Concept:** Number-variant twin: recompute incremental effects, rank most-to-least dilutive, sequential schedule, and dual EPS presentation with all new amounts  
**Scenario:**  
**SummitForge Technologies Inc.** (complex capital structure) reports for Year 1:

| Item | Amount |
|---|---:|
| Net income | $615,000 |
| Weighted-average common shares outstanding (entire year) | 300,000 |
| Income tax rate | 25% |

No discontinued operations. Securities outstanding all year (none exercised/converted):

1. **Stock options:** 12,000 options to buy one share each at **$18**; average market price **$30**.
2. **6% cumulative convertible preferred:** 8,000 shares, **$100 par**; each convertible into **5** common shares. Full-year dividends declared and paid.
3. **Series C convertible bonds:** **$800,000** face, **5%** coupon, issued at par; each **$1,000** bond converts into **40** common shares.
4. **Series D convertible bonds:** **$500,000** face, **9%** coupon, issued at par; each **$1,000** bond converts into **15** common shares.

**Required:**  
a. Prepare the **period-end JE** for the annual preferred dividend (cash paid same day).  
b. Rank all potentially dilutive securities (show Δ income, Δ shares, incremental EPS).  
c. Compute basic EPS.  
d. Complete the sequential diluted EPS schedule; state diluted EPS and which security is antidilutive.  
e. Present basic and diluted EPS as they would appear on the income statement.

**Answer key:**  

**a. Preferred dividend JE**

Preferred dividends = 8,000 × $100 × 6% = **$48,000**

| Account | Debit | Credit |
|---|---:|---:|
| Preferred Dividends (or Retained Earnings) | 48,000 | |
| Cash | | 48,000 |
| *Annual 6% cumulative convertible preferred dividend* | | |

**Check:** Dr = Cr = **48,000**. Balanced.

**b. Ranking**

| Rank | Security | Δ Income | Δ Shares | Incremental EPS |
|---:|---|---:|---:|---:|
| 1 | Stock options | $0 | 4,800 | **$0.00** |
| 2 | Series C bonds | 30,000 | 32,000 | **0.9375** |
| 3 | Convertible preferred | 48,000 | 40,000 | **1.20** |
| 4 | Series D bonds | 33,750 | 7,500 | **4.50** |

Supporting computations:
- Options: proceeds $216,000; repurchase $216,000 ÷ $30 = 7,200; incremental = 12,000 − 7,200 = **4,800**
- Series C: after-tax interest = $800,000 × 5% × 0.75 = **$30,000**; shares = 800 × 40 = **32,000**
- Preferred: add-back **$48,000**; shares = 8,000 × 5 = **40,000**
- Series D: after-tax interest = $500,000 × 9% × 0.75 = **$33,750**; shares = 500 × 15 = **7,500**

**c. Basic EPS**

Income available to common = $615,000 − $48,000 = **$567,000**

\[
\text{Basic EPS} = \frac{\$567{,}000}{300{,}000} = \mathbf{\$1.89}
\]

**d. Sequential schedule**

| Step | Income | Shares | EPS | Result |
|---|---:|---:|---:|---|
| Basic | $567,000 | 300,000 | **$1.89** | — |
| + Options | 567,000 | 304,800 | **1.86** | Dilutive |
| + Series C | 597,000 | 336,800 | **1.77** | Dilutive |
| + Preferred | 645,000 | 376,800 | **1.71** | Dilutive |
| + Series D | 678,750 | 384,300 | **1.77** | **Antidilutive** |

Detail:
- Options: $567,000 / 304,800 = **$1.8602**  
- Series C: ($567,000 + $30,000) / (304,800 + 32,000) = $597,000 / 336,800 = **$1.7726**  
- Preferred: ($597,000 + $48,000) / (336,800 + 40,000) = $645,000 / 376,800 = **$1.7118**  
- Series D: ($645,000 + $33,750) / (376,800 + 7,500) = $678,750 / 384,300 = **$1.7662** → **antidilutive**

**Diluted EPS** = $645,000 / 376,800 = **$1.71**  
**Series D excluded** as antidilutive.

**e. Presentation**

| | |
|---|---:|
| Basic earnings per share | **$1.89** |
| Diluted earnings per share | **1.71** |

**Key insight:** Changing every input (NI, shares, coupons, conversion ratios, option terms) still follows the **same** LO 20-9 algorithm: rank → sequential include while EPS falls → dual presentation.

---

### Q3 — CORE alternate angle — Discontinued operations, control number, multi-security diluted EPS presentation
**LO:** LO 20-9  
**Concept:** Classification/presentation of basic and diluted EPS for continuing operations, discontinued operations, and net income when multiple dilutive securities exist; control number is income from continuing operations  
**Scenario:**  
**Harborline Systems Inc.** reports the following for Year 1 (complex capital structure; tax rate **25%**):

| Item | Amount |
|---|---:|
| Income from continuing operations | $180,000 |
| Gain from discontinued operations, net of tax | 30,000 |
| Net income | $210,000 |
| Weighted-average common shares outstanding | 50,000 |

Potentially dilutive securities outstanding all year:

1. **Options:** 4,000 options to buy one share at **$10**; average market price **$16**.
2. **8% cumulative convertible preferred:** 1,000 shares, **$100 par**; each converts into **5** common shares. Full-year preferred dividends declared and paid (**$8,000**).
3. **6% convertible bonds:** **$200,000** face at par; each **$1,000** bond converts into **15** common shares.

**Required:**  
a. Prepare the **period-end JE** for the $8,000 preferred dividend (assume paid in cash).  
b. Rank the three potentially dilutive securities by earnings per incremental share.  
c. Using **income from continuing operations available to common** as the control number, compute sequential diluted EPS and the final diluted share count.  
d. Prepare the **full EPS presentation** (basic and diluted) for continuing operations, discontinued operations, and net income—as required on the face of the income statement for a complex capital structure.  
e. Briefly state what would change if Harborline had a **loss from continuing operations** but overall net income.

**Answer key:**  

**a. Preferred dividend JE**

| Account | Debit | Credit |
|---|---:|---:|
| Preferred Dividends (or Retained Earnings) | 8,000 | |
| Cash | | 8,000 |
| *Annual 8% cumulative convertible preferred dividend* | | |

**Check:** Dr = Cr = **8,000**. Balanced.

**b. Ranking**

| Rank | Security | Δ Income | Δ Shares | Incremental EPS |
|---:|---|---:|---:|---:|
| 1 | Options | $0 | 1,500 | **$0.00** |
| 2 | Convertible preferred | 8,000 | 5,000 | **1.60** |
| 3 | Convertible bonds | 9,000 | 3,000 | **3.00** |

Supporting:
- Options: proceeds $40,000; repurchase $40,000 ÷ $16 = 2,500; incremental = 4,000 − 2,500 = **1,500**
- Preferred: add-back **$8,000**; shares = 1,000 × 5 = **5,000**
- Bonds: after-tax interest = $200,000 × 6% × 0.75 = **$9,000**; shares = 200 × 15 = **3,000**

**c. Sequential dilution using continuing operations as control number**

Income from continuing operations available to common (basic) = $180,000 − $8,000 = **$172,000**

| Step | Cont. ops. available | Shares | Cont. ops. EPS | Result |
|---|---:|---:|---:|---|
| Basic | $172,000 | 50,000 | **$3.44** | — |
| + Options | 172,000 | 51,500 | **3.34** | Dilutive |
| + Preferred | 180,000 | 56,500 | **3.19** | Dilutive |
| + Bonds | 189,000 | 59,500 | **3.18** | Dilutive |

All three securities are dilutive.  
**Diluted weighted-average shares** = **59,500**  
**Diluted EPS — continuing operations** = $189,000 / 59,500 = **$3.18**

**d. Full face presentation of EPS**

Basic numerators:  
- Continuing ops available = **$172,000**  
- Discontinued ops = **$30,000** (no preferred allocation)  
- Net income available = $210,000 − $8,000 = **$202,000**

Diluted numerators (same dilutive share count **59,500**):  
- Continuing ops = **$189,000** (after preferred add-back + after-tax interest)  
- Discontinued ops = **$30,000**  
- Net income = $210,000 + $9,000 = **$219,000** (pref cancels with add-back; interest added)

| | Basic | Diluted |
|---|---:|---:|
| Earnings per share — continuing operations | **$3.44** | **$3.18** |
| Earnings per share — discontinued operations | **0.60** | **0.50** |
| Earnings per share — net income | **$4.04** | **$3.68** |

Checks:  
Basic: $3.44 + $0.60 = $4.04  
Diluted: $3.18 + $0.50 = $3.68  
$30,000 / 50,000 = $0.60; $30,000 / 59,500 ≈ $0.50  
$219,000 / 59,500 = $3.68

**e. Loss from continuing operations**  
If continuing operations available to common were a **loss**, potential common shares would be **antidilutive** for the control number. Diluted EPS for continuing operations (and typically all EPS lines using that diluted share set) would equal **basic** EPS even if net income is positive after a discontinued gain. Antidilutive securities would still be **disclosed**.

**Key insight:** Dilutiveness is tested against **income from continuing operations**, not net income. Once the diluted share count is set, apply it (with appropriate numerator adjustments) to discontinued operations and net income for dual presentation with equal prominence.

---

### Q4 — MC — Ranking and antidilutive cutoff with multiple securities
**LO:** LO 20-9  
**Concept:** Classification of which securities enter diluted EPS after ranking by earnings per incremental share  
**Question:**  
**Perryline Media Co.** had **175,000** weighted-average common shares and net income available to common of **$276,500** for the year (no preferred outstanding for basic). Two potentially dilutive securities, already ranked most dilutive → least dilutive:

| Rank | Security | Increase in income | Increase in shares |
|---:|---|---:|---:|
| 1 | Security A | $5,000 | 15,000 |
| 2 | Security B | $22,000 | 18,000 |

What **diluted EPS** should Perryline report?

- A) $1.58  
- B) $1.46  
- C) $1.44  
- D) $1.43  

**Answer:** **B. $1.46**  

**Explanation:**  
Basic EPS = $276,500 / 175,000 = **$1.58**  

+ Security A: ($276,500 + $5,000) / (175,000 + 15,000) = $281,500 / 190,000 = **$1.4816** (dilutive vs $1.58)  

+ Security B: ($281,500 + $22,000) / (190,000 + 18,000) = $303,500 / 208,000 = **$1.4591** ≈ **$1.46** (dilutive vs $1.48)  

Both securities are included.  
Trap A is basic EPS only.  
Trap C/D would understate if incorrect share or numerator combinations were used without sequential testing.

---

### Q5 — MC — EPS presentation / complex capital structure disclosure
**LO:** LO 20-9  
**Concept:** Classification of required EPS presentation on the face of the income statement for complex vs simple capital structures  
**Question:**  
Which statement about **EPS financial statement presentation** is correct under ASC 260 for an entity with **convertible bonds and stock options** outstanding (complex capital structure)?

- A) Only diluted EPS is presented; basic EPS is disclosed only in the notes.  
- B) Basic and diluted EPS for income from continuing operations and for net income are presented on the face of the income statement with **equal prominence**.  
- C) Diluted EPS is presented only when it equals basic EPS.  
- D) Discontinued operations EPS, if any, must always be omitted from both the face and the notes.

**Answer:** **B.**  

**Explanation:** Entities with complex capital structures present **basic and diluted** per-share amounts for continuing operations and net income on the face of the income statement with equal prominence. Discontinued operations EPS is required on the face **or** in the notes. Diluted EPS is the amount after including **dilutive** potential common shares (not only when it equals basic). Simple capital structures present basic EPS only.

---

### Self-check
- [x] Every JE balances (preferred dividend entries in Q1–Q3)
- [x] Math recomputed (ranking ratios, sequential EPS, presentation cross-foots)
- [x] Core demo not sidebar-only (Demo 20-9 path: rank → sequential dilution → presentation)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5)
- [x] Angles covered: initial ranking/setup, sequential schedule, period-end preferred JE, antidilutive exclusion (settlement-of-inclusion decision), classification/presentation, number-variant twin
