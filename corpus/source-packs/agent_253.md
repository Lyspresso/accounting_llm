# Agent 253 — CORE DEMO — LO 20-8

**Chapter:** 20  
**LO title:** Compute EPS Given Contingently Issuable Shares  
**Critical gap LO:** no  
**Emphasis angle:** subsequent_measurement_schedule

## Concept list for this pack
- **Contingently issuable shares (ASC 260-10-45-48 / Demo 20-8):** shares issuable only if specified conditions are met (target earnings, market price, other events)
- **Diluted EPS — conditions satisfied by period end:** include contingent shares from the **beginning of the period** in which conditions were satisfied (or agreement date, if later); **numerator unchanged**
- **Diluted EPS — conditions not yet legally satisfied:** include the number of shares that **would be issuable if the reporting period-end were the end of the contingency period** (current earnings / period-end price proxy), **if dilutive**, from beginning of period (or agreement date if later)
- **Basic EPS:** exclude contingent shares until all necessary conditions are satisfied **and** shares are outstanding (Demo 20-8 core path keeps them out of basic until issued)
- **Numerator:** pure common contingently issuable shares have **no numerator effect** (no interest or preferred dividend add-back)
- **Subsequent measurement schedule (emphasis):** multi-year roll-forward of basic WASO, contingent shares in the diluted denominator, basic EPS, diluted EPS, and dual presentation flag
- **Initial recognition JE:** cash issuance of outstanding common that establishes the EPS base denominator
- **Period-end adjusting / closing JE:** close net income to retained earnings; **no** “EPS” ledger account; contingent arrangement alone does not force a period-end equity adjusting entry
- **Disposal / settlement JE:** when contingency is resolved and shares are issued (stock dividend / fixed-share issuance), record a **balanced** equity entry
- **Classification / presentation:** complex structure when dilutive contingent shares exist → report basic **and** diluted with equal prominence; if as-if test fails and no other dilutives, basic = diluted

---

### Q1 — CORE — Multi-year contingency: subsequent measurement schedule (emphasis)
**LO:** LO 20-8  
**Concept:** Initial recognition JE for common stock; period-end as-if diluted test; multi-year subsequent measurement schedule of basic/diluted EPS with contingent shares; period-end closing JE; settlement issuance JE when conditions are met  
**Scenario:**  
**Harborwick Instruments Corp.** is a calendar-year public company. On **January 1, Year 1**, Harborwick issues **150,000 shares** of **$1 par** common stock for **$16** cash per share. Those shares remain outstanding until any contingent issuance occurs. No preferred stock and no other potentially dilutive securities exist.

On **January 1, Year 1**, Harborwick enters a contingent stock agreement with the former owners of an acquired product line:

| Term | Detail |
|---|---|
| Condition | If **Year 2** net income **exceeds $900,000**, Harborwick will issue **24,000** additional common shares |
| Issuance date if met | **January 2, Year 3** as a **stock dividend** |
| Accounting policy | Small stock dividends recorded at **fair value** (market price × shares issued) |
| Market price on January 2, Year 3 | **$22** per share |

Reported net income:

| Year | Net income |
|---:|---:|
| Year 1 | **$820,000** |
| Year 2 | **$960,000** |
| Year 3 | **$1,050,000** |

**Required:**  
a. Prepare the **January 1, Year 1 initial recognition journal entry** for the common stock issuance. Show Dr = Cr.  
b. **Year 1 — period-end diluted test:** How many contingently issuable shares enter **diluted** EPS? Compute **basic** and **diluted** EPS. Present a short EPS schedule.  
c. **Year 2 — conditions satisfied:** Compute basic and diluted EPS. Present the diluted EPS schedule (basic row + contingent effect).  
d. Prepare the **December 31, Year 2 period-end closing entry** transferring net income to retained earnings (use Income Summary).  
e. Prepare the **January 2, Year 3 settlement / issuance journal entry** when the 24,000 shares are issued. Confirm Dr = Cr.  
f. Build a **subsequent measurement / multi-year schedule** (emphasis) for Years 1–3: net income, basic WASO, contingent shares in diluted denominator, diluted WASO, basic EPS, diluted EPS, and whether dual EPS presentation is required.

**Answer key:**  

**a. January 1, Year 1 — initial recognition of common stock issuance**

Cash proceeds = 150,000 × $16 = **$2,400,000**  
Common stock (par) = 150,000 × $1 = **$150,000**  
APIC—Common = $2,400,000 − $150,000 = **$2,250,000**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 2,400,000 | |
| Common Stock ($1 par) | | 150,000 |
| Additional Paid-in Capital—Common | | 2,250,000 |
| *Issue 150,000 shares of $1 par common at $16* | | |

**Check:** Dr = **2,400,000**; Cr = 150,000 + 2,250,000 = **2,400,000**. **Balanced.**

**b. Year 1 — period-end “as if contingency ended now” test**

Agreement requires **Year 2** NI > $900,000. Under ASC 260-10-45-48 / Demo 20-8, treat **December 31, Year 1** as if it were the end of the contingency period and use **Year 1 current earnings** as the proxy:  
Year 1 NI **$820,000** ≯ $900,000 → **condition not met** under the as-if rule.

Contingent shares in **diluted** EPS Year 1 = **0**  
Contingent shares in **basic** EPS Year 1 = **0** (not outstanding; conditions not satisfied)

| | Net income available to common | Weighted-average common shares | Per share |
|---|---:|---:|---:|
| **Basic EPS** | $820,000 | 150,000 | **$5.47** |
| Effect of contingently issuable shares | — | 0 | |
| **Diluted EPS** | $820,000 | 150,000 | **$5.47** |

$820,000 ÷ 150,000 = **$5.4666… → $5.47** (nearest cent).

**Report:** Basic = diluted = **$5.47**. Contingent arrangement is disclosed; no dilutive share add-on.

**c. Year 2 — conditions satisfied by period end**

Year 2 NI **$960,000** > $900,000 → **all necessary conditions satisfied** by December 31, Year 2.  
For **diluted** EPS: include **24,000** contingent shares **as of the beginning of Year 2** (period in which conditions were satisfied).  
Numerator: **no adjustment**.  
For **basic** EPS Year 2: shares not yet issued → basic WASO remains **150,000**.

| | Net income available to common | Weighted-average common shares | Per share |
|---|---:|---:|---:|
| **Basic EPS** | $960,000 | 150,000 | **$6.40** |
| Effect of contingently issuable stock: add shares | — | 24,000 | |
| **Diluted EPS** | $960,000 | 174,000 | **$5.52** |

Checks:  
Basic: $960,000 ÷ 150,000 = **$6.40**  
Diluted: $960,000 ÷ 174,000 = **$5.51724… → $5.52**  
Diluted < basic → **dilutive**; report both.

**d. December 31, Year 2 — period-end closing of net income**

| Account | Debit | Credit |
|---|---:|---:|
| Income Summary | 960,000 | |
| Retained Earnings | | 960,000 |
| *Close Year 2 net income to retained earnings* | | |

**Check:** Dr = Cr = **960,000**. **Balanced.**

*Note:* Meeting the contingency for **diluted EPS presentation** does **not** by itself create a December 31, Year 2 adjusting entry to Common Stock. The equity issuance is recorded when shares are actually issued (part e). EPS is a presentation measure—there is no “EPS expense” account.

**e. January 2, Year 3 — settlement / issuance JE**

Fair value of stock dividend = 24,000 × $22 = **$528,000**  
Par portion = 24,000 × $1 = **$24,000**  
APIC = $528,000 − $24,000 = **$504,000**

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings | 528,000 | |
| Common Stock ($1 par) | | 24,000 |
| Additional Paid-in Capital—Common | | 504,000 |
| *Issue 24,000 contingent shares as stock dividend when conditions met* | | |

**Check:** Dr = **528,000**; Cr = 24,000 + 504,000 = **528,000**. **Balanced.**

After issuance, outstanding common shares = 150,000 + 24,000 = **174,000**. Because issuance is on **January 2**, treat the new shares as outstanding for essentially the **entire** Year 3 for weighted-average purposes (or weight 364/365 ≈ full year). Use **174,000** WASO for Year 3.

**f. Subsequent measurement schedule — Years 1–3 (emphasis)**

| Year | NI | Basic WASO | Contingent shares in diluted | Diluted WASO | Basic EPS | Diluted EPS | Dual EPS? |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 820,000 | 150,000 | 0 | 150,000 | $5.47 | $5.47 | Same (one line OK) |
| 2 | 960,000 | 150,000 | 24,000 | 174,000 | $6.40 | $5.52 | **Yes** |
| 3 | 1,050,000 | 174,000 | 0 (now outstanding) | 174,000 | $6.03 | $6.03 | Same |

Year 3 EPS: $1,050,000 ÷ 174,000 = **$6.03448… → $6.03**.

**Roll-forward insight:** Contingent shares move from **excluded (Y1 as-if fail)** → **diluted-only denominator (Y2 conditions met)** → **issued equity + basic outstanding (Y3)**. The multi-year schedule is the LO 20-8 subsequent measurement tool.

**Key insight:** For diluted EPS, assume the **reporting date is the contingency deadline** and count shares that would be issuable **if** that test is passed—and only if dilutive. Basic ignores those shares until they are outstanding. Issuance is a pure equity entry that **must balance**. The **subsequent measurement schedule** tracks the path from disclosure-only to diluted-only to outstanding.

---

### Q2 — CORE number variant — CEO income target; Year 1 dilutive; Year 2 miss
**LO:** LO 20-8  
**Concept:** Number-variant twin of Demo 20-8 path: current-year earnings used as proxy for next-year NI target; subsequent measurement schedule when target later fails; no settlement issuance JE  
**Scenario:**  
**Redcedar Freight Systems Inc.** reports the following.

| Fact | Amount / term |
|---|---|
| Year 1 net income | **$510,000** |
| Common shares outstanding entire Year 1 | **85,000** |
| Contingent agreement (entered beginning of Year 1) | Grant **7,000** common shares to the CEO if **Year 2** net income **reaches $480,000** |
| Year 2 net income (actual) | **$445,000** |
| Common shares outstanding entire Year 2 | **85,000** (no shares issued) |
| Other dilutive securities / preferred | **None** |

**Required:**  
a. Compute **basic** and **diluted** EPS for **Year 1** (Demo 20-8 style). Explain why contingent shares are (or are not) included in diluted.  
b. Prepare a **period-end diluted EPS schedule** for Year 1 (basic row + contingent effect).  
c. Compute basic and diluted EPS for **Year 2**. How many contingent shares enter diluted EPS?  
d. Prepare a **two-year subsequent measurement schedule** (NI, basic WASO, contingent shares in diluted, basic EPS, diluted EPS).  
e. Is there a **settlement / issuance JE** in Year 2 or Year 3? Why or why not?  
f. State Year 1 **income statement presentation** of EPS.

**Answer key:**  

**a. Year 1 basic and diluted EPS**

As-if test at end of Year 1: Year 1 NI **$510,000** ≥ $480,000 target → presume condition would be met if contingency period ended now → add **7,000** shares to diluted denominator.  
Numerator unchanged.

Basic EPS = $510,000 ÷ 85,000 = **$6.00**  
Diluted EPS = $510,000 ÷ (85,000 + 7,000) = $510,000 ÷ 92,000 = **$5.54**

**b. Year 1 period-end schedule**

| | Net income available to common | Weighted-average common shares | Per share |
|---|---:|---:|---:|
| **Basic EPS** | $510,000 | 85,000 | **$6.00** |
| Effect of contingently issuable stock: add shares | — | 7,000 | |
| **Diluted EPS** | $510,000 | 92,000 | **$5.54** |

$510,000 ÷ 92,000 = 5.543478… → **$5.54**. Dilutive.

**c. Year 2**

Actual Year 2 NI **$445,000** < $480,000 → conditions **not** satisfied.  
Contingent shares in diluted EPS Year 2 = **0**.  
Shares never issued → basic WASO still **85,000**.

Basic EPS = Diluted EPS = $445,000 ÷ 85,000 = **$5.24**  
($445,000 ÷ 85,000 = 5.23529… → **$5.24**)

**d. Subsequent measurement schedule (Years 1–2)**

| Year | NI | Basic WASO | Contingent in diluted | Diluted WASO | Basic EPS | Diluted EPS | Dual? |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 510,000 | 85,000 | 7,000 | 92,000 | $6.00 | $5.54 | **Yes** |
| 2 | 445,000 | 85,000 | 0 | 85,000 | $5.24 | $5.24 | Same |

**Roll-forward:** Year 1 as-if success pulls shares into diluted only; Year 2 actual miss removes them from diluted and leaves basic WASO unchanged—no equity issuance.

**e. Settlement JE**  
**No journal entry.** The performance condition failed; no shares are issued. There is nothing to debit or credit for share issuance. (ASC 718 compensation accounting for a share-based award, if applicable, is a different LO; under the pure LO 20-8 contingent-EPS path, failure = zero shares and no equity issuance entry.)

**f. Presentation Year 1**  
Report **basic EPS $6.00** and **diluted EPS $5.54** with equal prominence on the face of the income statement. Disclose the contingent arrangement (terms, threshold, shares potentially issuable).

**Key insight:** Surpassing the dollar target in the **current** year pulls contingent shares into **diluted** EPS under the as-if rule—even though the legal contingency still points at **next** year’s income. If next year misses, the subsequent measurement schedule drops the shares from diluted and **no issuance JE** is recorded.

---

### Q3 — CORE alternate angle — Earnings-formula contingency; period-end share count schedule; dual presentation
**LO:** LO 20-8  
**Concept:** Period-end determination of contingently issuable shares under an earnings formula; subsequent measurement of basic vs diluted share counts; income-statement presentation; memo that no period-end equity adjusting JE is required until issuance  
**Scenario:**  
**Solstice Packaging Group** has **200,000** common shares outstanding for the **entire** current year. No preferred stock and no other potentially dilutive securities. Net income for the year is **$700,000**.

Contingent stock agreement (in effect all year; shares issuable in the **following** year if conditions are met):

> Issue **1,200** common shares for **each $50,000** of net income in excess of **$400,000**. Only whole $50,000 increments count (no partial increments).

Solstice will issue any earned contingent shares on **January 5 of the next year** as a stock dividend. Common stock is **$2 par**. Year-end market price (used only if/when issued next year) is **$15**.

**Required:**  
a. Compute contingent shares under the diluted **period-end = contingency-end** rule. Show the formula schedule.  
b. How many contingent shares enter **basic** EPS for the current year?  
c. Prepare a full **basic and diluted EPS computation schedule**.  
d. Show the **income statement presentation** of EPS for the current year.  
e. Prepare the **period-end closing entry** for net income (Income Summary → Retained Earnings). State whether any **additional period-end adjusting JE** is required for the contingent shares themselves.  
f. Assume next year the board issues the earned shares on January 5 at the prior year-end market price of $15 (small stock dividend at FV). Prepare the **settlement issuance JE** and confirm Dr = Cr.

**Answer key:**  

**a. Contingent shares — diluted as-if formula schedule**

| Step | Computation | Result |
|---|---|---:|
| Net income | Given | $700,000 |
| Threshold | Given | $400,000 |
| Excess income | $700,000 − $400,000 | **$300,000** |
| Whole $50,000 increments | $300,000 ÷ $50,000 | **6** |
| Shares per increment | 1,200 | |
| **Contingent shares for diluted EPS** | 6 × 1,200 | **7,200** |

(If NI had been $749,999, still only 6 increments—partial increments do not count.)

**b. Basic EPS contingent shares**  
**0** — shares are not outstanding in the current year (issuable next year). Demo 20-8 / core path keeps them out of basic until issued.

**c. EPS computation schedule**

| | Numerator | Denominator | Per share |
|---|---:|---:|---:|
| **Basic EPS** | $700,000 | 200,000 | **$3.50** |
| Effect of contingently issuable stock: add shares | — | 7,200 | |
| **Diluted EPS** | $700,000 | 207,200 | **$3.38** |

Diluted: $700,000 ÷ 207,200 = 3.378378… → **$3.38**. Dilutive (numerator unchanged).

**d. Financial statement presentation**

Solstice has a **complex capital structure** for EPS purposes because of dilutive contingently issuable shares.

**Income Statement (partial) — current year**

| | |
|---|---:|
| Net income | $700,000 |
| Basic earnings per share | **$3.50** |
| Diluted earnings per share | **$3.38** |

Disclose the contingent formula, the **7,200** shares included in diluted EPS, and a reconciliation of the basic-to-diluted denominator.

**e. Period-end closing JE; no contingent equity adjusting JE**

| Account | Debit | Credit |
|---|---:|---:|
| Income Summary | 700,000 | |
| Retained Earnings | | 700,000 |
| *Close current-year net income* | | |

**Check:** Dr = Cr = **700,000**. **Balanced.**

**No additional period-end adjusting JE** is recorded for the contingent shares themselves under the LO 20-8 EPS path. The arrangement affects the **diluted EPS denominator and disclosure** in the current year; equity accounts change when shares are **issued** (part f).

**f. Next-year settlement issuance JE (January 5)**

Fair value = 7,200 × $15 = **$108,000**  
Par = 7,200 × $2 = **$14,400**  
APIC = $108,000 − $14,400 = **$93,600**

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings | 108,000 | |
| Common Stock ($2 par) | | 14,400 |
| Additional Paid-in Capital—Common | | 93,600 |
| *Issue 7,200 contingent formula shares as stock dividend* | | |

**Check:** Dr = **108,000**; Cr = 14,400 + 93,600 = **108,000**. **Balanced.**

**Key insight:** Earnings-formula contingencies are measured **at period end** for diluted EPS using whole contractual increments. The subsequent measurement of the share count (formula schedule → diluted denominator → later basic WASO after issuance) is the core LO 20-8 skill. Basic stays clean until shares are outstanding; settlement is a balanced equity entry.

---

### Q4 — MC (classification / method) — When contingent shares enter diluted EPS
**LO:** LO 20-8  
**Concept:** Classification of when contingently issuable shares are included in diluted EPS under the as-if period-end rule  
**Question:**  
**Mossbrook Media Ltd.** has **50,000** common shares outstanding all year and net income of **$200,000**. In Year 1 it agreed that if Year 2 net income exceeds **$180,000**, it will issue **5,000** shares in Year 3. Year 1 net income is **$200,000**. No other potential common shares exist. Which statement is **correct** for Year 1?

- A) Include 5,000 shares in **basic** EPS only; diluted EPS is not reported.  
- B) Include 5,000 shares in **diluted** EPS (as-if contingency period ended at Year 1 year-end) because Year 1 NI exceeds $180,000; basic EPS uses 50,000 shares.  
- C) Include 5,000 shares in both basic and diluted EPS for the full year.  
- D) Exclude the 5,000 shares from both basic and diluted EPS because the legal condition refers to Year 2, not Year 1.

**Answer:** **B.**  
Under ASC 260 / Demo 20-8, if conditions have not yet been legally satisfied, diluted EPS still includes shares that would be issuable **if the end of the reporting period were the end of the contingency period**. Year 1 NI $200,000 > $180,000 → include 5,000 in diluted. Basic uses only outstanding shares (50,000). A reverses the treatment. C incorrectly puts shares in basic before issuance. D ignores the as-if diluted rule.

---

### Q5 — MC (presentation) — Conditions not met under as-if test
**LO:** LO 20-8  
**Concept:** EPS presentation when contingently issuable shares fail the period-end as-if test  
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
- [x] Every JE balances (Q1 issuance $2,400,000; Q1 close $960,000; Q1 settlement $528,000; Q3 close $700,000; Q3 settlement $108,000)
- [x] Math recomputed (all EPS, share counts, FV/par/APIC splits double-checked)
- [x] Core demo path (Demo 20-8 / Review 20-8 / ASC 260-10-45-48)—not Expanding Your Knowledge sidebar
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5 classification/presentation only)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (emphasis), period_end_adjusting_JE (closing), disposal_maturity_or_settlement_JE (issuance)
- [x] Original companies/numbers (not textbook Gridley/Case demos)
