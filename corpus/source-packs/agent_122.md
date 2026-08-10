# Agent 122 — CORE DEMO — LO 20-8

**Chapter:** 20  
**LO title:** Compute EPS Given Contingently Issuable Shares  
**Critical gap LO:** no

## Concept list for this pack
- **Contingently issuable shares (ASC 260):** shares issuable only if specified conditions are met (target earnings, market price, patents/other events)
- **Diluted EPS — conditions met by period end:** include contingent shares from the **beginning of the period** in which conditions were satisfied (or agreement date, if later); numerator unchanged
- **Diluted EPS — conditions not yet met:** include the number of shares that **would be issuable if the reporting period-end were the end of the contingency period** (e.g., based on current earnings or period-end market price), **if dilutive**, from beginning of period (or agreement date if later)
- **Basic EPS:** do **not** include contingent shares until all necessary conditions are satisfied and shares are outstanding (or treated as outstanding under ASC 260); Demo 20-8 path keeps them out of basic until issued
- **Numerator:** contingently issuable common shares have **no numerator effect** (no interest add-back, no preferred dividend add-back)
- **Initial recognition / settlement JE:** when contingency is resolved and shares are issued (stock dividend or fixed-share issuance), record balanced equity entry (RE or other equity offset → Common Stock / APIC)
- **Subsequent measurement schedule:** multi-year tracking of basic WASO, contingent shares in diluted, and when shares enter outstanding for basic
- **Period-end determination:** year-end “as if contingency period ended now” test for diluted; dual vs single-line EPS presentation
- **Classification / presentation / disclosure:** report basic and diluted with equal prominence when complex; if contingency not met and no other dilutives, diluted may equal basic or only basic is presented; disclose antidilutive or unused contingent arrangements

---

### Q1 — CORE — Multi-year contingency: diluted test, schedule, issuance JE (emphasis: initial recognition / settlement JE)
**LO:** LO 20-8  
**Concept:** Contingently issuable shares in diluted EPS when period-end is treated as contingency-period end; multi-year EPS schedule; balanced JE when shares are issued after conditions are met  
**Scenario:**  
**Cedarline Analytics Inc.** (calendar year) has a simple capital structure except for one contingent stock agreement with former owners of an acquired division.

| Fact | Amount / term |
|---|---|
| Common shares outstanding all Year 1 and Year 2 (before any contingent issue) | **280,000** |
| Contingent agreement (entered **January 1, Year 1**) | If **Year 2** net income **exceeds $750,000**, Cedarline will issue **35,000** additional common shares to the former owners on **January 15, Year 3** as a **stock dividend** |
| Common stock par value | **$2** per share |
| Market price of common stock on January 15, Year 3 | **$18** per share |
| Year 1 net income | **$680,000** |
| Year 2 net income | **$810,000** |
| Year 3 net income | **$900,000** |
| Other potentially dilutive securities | **None** |
| Preferred stock | **None** |

Cedarline records small stock dividends at **fair value** (market price × shares).

**Required:**  
a. **Year 1 — period-end diluted test:** How many contingently issuable shares enter **diluted** EPS? Compute **basic** and **diluted** EPS for Year 1. What EPS amount(s) does Cedarline report?  
b. **Year 2 — conditions satisfied:** How many contingent shares enter diluted EPS? Compute basic and diluted EPS for Year 2. Show the diluted EPS schedule (basic row + contingent effect).  
c. Prepare the **January 15, Year 3 settlement / issuance journal entry** when the 35,000 shares are issued (initial recognition of the issued shares on the books). Confirm Dr = Cr.  
d. Build a **subsequent measurement / multi-year schedule** for Years 1–3: net income, basic WASO, contingent shares in diluted denominator, basic EPS, diluted EPS, and whether dual presentation is required.  
e. **Presentation / disclosure:** In one or two sentences, state how Cedarline presents Year 1 vs Year 2 EPS on the face of the income statement and what note disclosure is appropriate for the contingent agreement.

**Answer key:**  

**a. Year 1 — period-end “as if contingency ended now” test**

Contingency test for diluted EPS (ASC 260-10-45-48 / Demo 20-8 logic): treat **December 31, Year 1** as if it were the end of the contingency period. The agreement requires **Year 2** NI > $750,000. Using Year 1 NI as the proxy for “current period earnings” under the as-if rule:  
Year 1 NI **$680,000** ≯ $750,000 → **condition not met**.

Contingent shares in **diluted** EPS Year 1 = **0**  
Contingent shares in **basic** EPS Year 1 = **0** (shares not outstanding; conditions not satisfied)

| | Net income available to common | Weighted-average common shares | Per share |
|---|---:|---:|---:|
| **Basic EPS** | $680,000 | 280,000 | **$2.43** |
| Effect of contingently issuable shares | — | 0 | |
| **Diluted EPS** | $680,000 | 280,000 | **$2.43** |

$680,000 ÷ 280,000 = **$2.42857… → $2.43** (rounded to nearest cent).

**Report:** Only **basic EPS of $2.43** is needed for presentation when basic and diluted are the same (dual presentation can be one line, or only basic is emphasized). No dilutive contingent shares.

**b. Year 2 — conditions satisfied by period end**

Year 2 NI **$810,000** > $750,000 → **all necessary conditions satisfied** by December 31, Year 2.  
For **diluted** EPS: include **35,000** contingent shares **as of the beginning of Year 2** (period in which conditions were satisfied).  
Numerator: **no adjustment** (common shares only; no interest or preferred add-back).  
For **basic** EPS Year 2: shares not yet issued → basic WASO remains **280,000**.

| | Net income available to common | Weighted-average common shares | Per share |
|---|---:|---:|---:|
| **Basic EPS** | $810,000 | 280,000 | **$2.89** |
| Effect of contingently issuable stock: add shares | — | 35,000 | |
| **Diluted EPS** | $810,000 | 315,000 | **$2.57** |

Checks:  
Basic: $810,000 ÷ 280,000 = **$2.89286… → $2.89**  
Diluted: $810,000 ÷ 315,000 = **$2.57143… → $2.57**  
Diluted < basic → **dilutive**; report both.

**c. January 15, Year 3 — settlement / issuance JE (emphasis: initial recognition of issued shares)**

Fair value of stock dividend = 35,000 × $18 = **$630,000**  
Par portion = 35,000 × $2 = **$70,000**  
APIC = $630,000 − $70,000 = **$560,000**

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings | 630,000 | |
| Common Stock ($2 par) | | 70,000 |
| Paid-in Capital in Excess of Par—Common | | 560,000 |
| *Issue 35,000 contingent shares as stock dividend when conditions met* | | |

**Check:** Dr = **630,000**; Cr = 70,000 + 560,000 = **630,000**. **Balanced.**

(No cash changes hands. Before issuance, the contingent arrangement itself did not require a period-end adjusting JE to retained earnings—only disclosure and the diluted EPS denominator effect in Year 2.)

**d. Subsequent measurement schedule — Years 1–3**

After January 15, Year 3 issuance, outstanding common shares = 280,000 + 35,000 = **315,000** for the rest of Year 3.  
Year 3 weighted-average basic shares (issued Jan 15):  
= 280,000 × (14/365) + 315,000 × (351/365)  
≈ 280,000 × 0.038356 + 315,000 × 0.961644  
≈ 10,740 + 302,918 = **313,658** (approx.)

For exam-style clarity, if the course weights full months: issued mid-January ≈ **11.5/12** of year outstanding for new shares:  
WASO ≈ 280,000 + 35,000 × (11.5/12) = 280,000 + 33,542 = **313,542**  

Using **exact day-count** 313,658 below; either is acceptable if method is stated. Diluted Year 3 has no remaining contingency → diluted WASO = basic WASO.

| Year | NI | Basic WASO | Contingent shares in diluted | Diluted WASO | Basic EPS | Diluted EPS | Dual EPS? |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 680,000 | 280,000 | 0 | 280,000 | $2.43 | $2.43 | Same (one line OK) |
| 2 | 810,000 | 280,000 | 35,000 | 315,000 | $2.89 | $2.57 | **Yes** |
| 3 | 900,000 | 313,658 | 0 (now outstanding) | 313,658 | $2.87 | $2.87 | Same |

Year 3 basic EPS: $900,000 ÷ 313,658 ≈ **$2.87**.

**Roll-forward:** Contingent shares move from **diluted-only (Y2)** → **issued equity + basic outstanding (Y3)**.

**e. Presentation / disclosure**  
Year 1: report basic EPS **$2.43** (diluted equals basic). Year 2: present **basic $2.89** and **diluted $2.57** with equal prominence. Disclose the contingent stock agreement (terms, shares issuable, conditions) in the EPS notes even in years when shares are not included in diluted EPS.

**Key insight:** For diluted EPS, assume the **reporting date is the contingency deadline** and count shares that would be issuable **if** that test is passed—and only if the result is dilutive. Basic ignores those shares until they are outstanding. Issuance is a pure equity reclassification/dividend entry that **must balance**.

---

### Q2 — CORE number variant — CEO income target; Year 1 dilutive; Year 2 miss
**LO:** LO 20-8  
**Concept:** Number-variant twin of Demo 20-8 path: current-year earnings used as proxy for next-year NI target; diluted denominator add-on; schedule when target later fails; no issuance JE  
**Scenario:**  
**Northspire Devices Corp.** reports the following for the current year (Year 1) and the following year (Year 2).

| Fact | Amount / term |
|---|---|
| Year 1 net income | **$420,000** |
| Common shares outstanding entire Year 1 | **60,000** |
| Contingent agreement | Grant **4,500** common shares to the CEO if **Year 2** net income reaches **$400,000** |
| Year 2 net income (actual) | **$375,000** |
| Common shares outstanding entire Year 2 | **60,000** (no shares issued) |
| Other dilutive securities / preferred | **None** |

**Required:**  
a. Compute **basic** and **diluted** EPS for **Year 1** (Demo 20-8 style). Explain why contingent shares are (or are not) included in diluted.  
b. Prepare a **period-end diluted EPS schedule** for Year 1 (basic row + contingent effect).  
c. Compute basic and diluted EPS for **Year 2**. How many contingent shares enter diluted EPS?  
d. Is there a **settlement / issuance JE** in Year 2 or Year 3? Why or why not?  
e. State Year 1 **income statement presentation** of EPS.

**Answer key:**  

**a. Year 1 basic and diluted EPS**

As-if test at end of Year 1: Year 1 NI **$420,000** ≥ $400,000 target → presume condition would be met if contingency period ended now → add **4,500** shares to diluted denominator.  
Numerator unchanged.

Basic EPS = $420,000 ÷ 60,000 = **$7.00**  
Diluted EPS = $420,000 ÷ (60,000 + 4,500) = $420,000 ÷ 64,500 = **$6.51**

**b. Year 1 period-end schedule**

| | Net income available to common | Weighted-average common shares | Per share |
|---|---:|---:|---:|
| **Basic EPS** | $420,000 | 60,000 | **$7.00** |
| Effect of contingently issuable stock: add shares | — | 4,500 | |
| **Diluted EPS** | $420,000 | 64,500 | **$6.51** |

$420,000 ÷ 64,500 = 6.5116… → **$6.51**. Dilutive.

**c. Year 2**

Actual Year 2 NI **$375,000** < $400,000 → conditions **not** satisfied.  
Contingent shares in diluted EPS Year 2 = **0**.  
Shares never issued → basic WASO still **60,000**.

Basic EPS = Diluted EPS = $375,000 ÷ 60,000 = **$6.25**

**d. Settlement JE**  
**No journal entry.** The performance condition failed; no shares are issued. There is nothing to debit or credit for share issuance. (Compensation accounting for a share-based award, if applicable under ASC 718, is a different LO; under pure LO 20-8 contingent-EPS path, failure = zero shares and no equity issuance entry.)

**e. Presentation Year 1**  
Report **basic EPS $7.00** and **diluted EPS $6.51** with equal prominence on the face of the income statement.

**Key insight:** Surpassing the dollar target in the **current** year pulls contingent shares into **diluted** EPS under the as-if rule—even though the legal contingency still points at **next** year’s income. If next year misses, diluted no longer includes the shares and **no issuance JE** is recorded.

---

### Q3 — CORE alternate angle — Multi-condition contingency (earnings formula, events, market price); basic vs diluted share count; presentation
**LO:** LO 20-8  
**Concept:** Period-end determination of contingently issuable shares under multiple conditions; basic vs diluted share counts; classification of dual EPS presentation  
**Scenario:**  
**Pinnacle BioLabs Inc.** must issue shares to the former shareholders of an acquired lab if conditions are met. Shares are issuable in the **year after** conditions are met. Agreement terms:

1. **Earnings:** issue **25** shares for each **$1,000** of combined net income in excess of **$200,000**.  
2. **Patents:** issue **800** shares for each new patent awarded to the acquired lab during the year.  
3. **Market price:** issue **40** shares for each **$4** increase in Pinnacle’s stock price above the beginning-of-year price.

Data for the current year:

| Item | Amount |
|---|---|
| Net income (earnings for contingency) | **$320,000** |
| New patents awarded | **4** |
| Beginning stock price | **$28** |
| Ending stock price | **$40** |
| Common shares outstanding entire year | **100,000** |
| Preferred stock / other dilutives | **None** |

**Required:**  
a. Compute contingent shares from **each** condition under the diluted “period-end = contingency-end” rule.  
b. Total contingent shares for **diluted** EPS.  
c. Contingent shares for **basic** EPS for the current year (shares not yet issued; conditions measured at year-end but issuance is next year—follow Demo 20-8: exclude from basic until outstanding).  
d. Compute **basic** and **diluted** EPS.  
e. Prepare a brief **classification / presentation** note: what appears on the face of the income statement?

**Answer key:**  

**a. Contingent shares by condition (diluted as-if test)**

**(1) Earnings**  
Excess NI = $320,000 − $200,000 = **$120,000**  
Units of $1,000 = $120,000 ÷ $1,000 = **120**  
Shares = 120 × 25 = **3,000**

**(2) Patents**  
Shares = 4 × 800 = **3,200**

**(3) Market price**  
Price increase = $40 − $28 = **$12**  
Increments of $4 = $12 ÷ $4 = **3**  
Shares = 3 × 40 = **120**

**b. Total for diluted EPS**  
3,000 + 3,200 + 120 = **6,320** contingent shares (all dilutive as a package with no numerator effect).

**c. Basic EPS contingent shares**  
**0** — shares are not outstanding in the current year (issuable next year); Demo 20-8 / core path keeps them out of basic until issued.

**d. EPS**

| | Numerator | Denominator | Per share |
|---|---:|---:|---:|
| Basic EPS | $320,000 | 100,000 | **$3.20** |
| Diluted EPS | $320,000 | 100,000 + 6,320 = **106,320** | **$3.01** |

Diluted: $320,000 ÷ 106,320 = 3.00978… → **$3.01**. Dilutive.

**e. Presentation**  
Pinnacle has a **complex capital structure** for EPS purposes because of contingently issuable shares. Report on the face of the income statement:

- Basic earnings per share — **$3.20**  
- Diluted earnings per share — **$3.01**  

Disclose the contingent stock agreement terms and the **6,320** shares included in diluted EPS (reconciliation of denominators).

**Key insight:** Each contingency type is measured **as of period end** for diluted EPS. Market-price and earnings formulas can produce fractional “steps,” but only whole increments earned under the contract count. Basic stays clean until shares are outstanding.

---

### Q4 — MC (classification / method) — When contingent shares enter diluted EPS
**LO:** LO 20-8  
**Concept:** Classification of when contingently issuable shares are included in diluted EPS  
**Question:**  
Lakehurst Media has 50,000 common shares outstanding all year and net income of $200,000. In Year 1 it agreed that if Year 2 net income exceeds $180,000, it will issue 5,000 shares in Year 3. Year 1 net income is $200,000. No other potential common shares exist. Which statement is **correct** for Year 1?

- A) Include 5,000 shares in **basic** EPS only; diluted EPS is not reported.  
- B) Include 5,000 shares in **diluted** EPS (as-if contingency period ended at Year 1 year-end) because Year 1 NI exceeds $180,000; basic EPS uses 50,000 shares.  
- C) Include 5,000 shares in both basic and diluted EPS for the full year.  
- D) Exclude the 5,000 shares from both basic and diluted EPS because the legal condition refers to Year 2, not Year 1.

**Answer:** **B.**  
Under ASC 260 / Demo 20-8, if conditions have not yet been legally satisfied, diluted EPS still includes shares that would be issuable **if the end of the reporting period were the end of the contingency period**. Year 1 NI $200,000 > $180,000 → include 5,000 in diluted. Basic uses only outstanding shares (50,000). A is wrong (direction reversed). C is wrong (not in basic yet). D is wrong (ignores the as-if diluted rule).

---

### Q5 — MC (presentation) — Conditions not met
**LO:** LO 20-8  
**Concept:** EPS presentation when contingently issuable shares fail the period-end test  
**Question:**  
Same facts as Q4, except Year 1 net income is **$150,000** (below the $180,000 threshold). What is the correct Year 1 EPS reporting?

- A) Basic EPS $3.00; diluted EPS $2.73 (include 5,000 shares).  
- B) Basic EPS $4.00; diluted EPS $3.00.  
- C) Basic EPS = diluted EPS = $150,000 ÷ 50,000 = **$3.00**; contingent shares excluded from diluted because the as-if test fails.  
- D) No EPS is reported until Year 2 when the contingency is resolved.

**Answer:** **C.**  
$150,000 ≯ $180,000 → zero contingent shares in diluted. Basic = diluted = **$3.00**. A incorrectly includes shares. B uses wrong NI. D is false—EPS is reported every period.

---

### Self-check
- [x] Every JE balances (Q1 issuance: Dr 630,000 = Cr 630,000)
- [x] Math recomputed (all EPS and share counts double-checked)
- [x] Core demo path (Demo 20-8 / Review 20-8 / Problem 20-10 style)—not Expanding Your Knowledge sidebar
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5 classification/presentation only)
- [x] Angles covered: initial_recognition_JE (issuance), subsequent_measurement_schedule, period_end test, settlement JE, classification/presentation, number_variant_twin
