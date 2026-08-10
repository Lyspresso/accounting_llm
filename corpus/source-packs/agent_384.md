# Agent 384 — CORE DEMO — LO 20-8

**Chapter:** 20  
**LO title:** Compute EPS Given Contingently Issuable Shares  
**Critical gap LO:** no  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **Contingently issuable shares (ASC 260-10-45-48 / Demo 20-8):** shares issuable only if specified conditions are met (target earnings, earnings formulas, market price, patents/other events)
- **Diluted EPS — conditions satisfied by period end:** include contingent shares **from the beginning of the period** in which conditions were satisfied (or agreement date, if later); **numerator unchanged**
- **Diluted EPS — conditions not yet legally satisfied:** include the number of shares that **would be issuable if the reporting period-end were the end of the contingency period** (current earnings / period-end price proxy), **if dilutive**, from beginning of period (or agreement date if later)
- **Basic EPS:** exclude contingent shares until shares are **outstanding** (Demo 20-8 core path keeps them out of basic until issued)
- **Numerator:** pure common contingently issuable shares have **no numerator effect** (no interest or preferred dividend add-back)
- **Initial recognition JE:** cash issuance of outstanding common that establishes the basic EPS denominator
- **Subsequent measurement schedule:** multi-year roll-forward of basic WASO, contingent shares in the diluted denominator, basic/diluted EPS, dual-presentation flag
- **Period-end adjusting / closing JE (emphasis):** year-end **as-if contingency-end** diluted share determination worksheet; close net income to retained earnings; **no** “EPS” ledger account and **no** equity adjusting entry merely because diluted EPS includes contingent shares
- **Disposal / settlement JE:** when the contingency is resolved and shares are issued (stock dividend / fixed-share issuance), record a **balanced** equity entry (RE → Common Stock / APIC at FV for small stock dividend)
- **Presentation:** complex structure when dilutive contingent shares exist → report basic **and** diluted with equal prominence; if as-if test fails and no other dilutives, basic = diluted

---

### Q1 — CORE — Multi-type contingencies; period-end diluted test (emphasis); multi-year schedule; settlement JEs
**LO:** LO 20-8  
**Concept:** Period-end as-if diluted share determination for four contingency types; initial common-stock recognition JE; period-end closing JEs (emphasis); multi-year subsequent measurement schedule; settlement issuance JEs when conditions are met  
**Scenario:**  
**Windmere Precision Ltd.** is a calendar-year public company. On **January 1, Year 1**, Windmere issues **90,000 shares** of **$1 par** common stock for **$12** cash per share. Those shares remain outstanding until any contingent issuances occur. No preferred stock and no other potentially dilutive securities exist.

Also on **January 1, Year 1**, Windmere acquires Bolt & Thread Co. The acquisition agreement includes the following **contingent stock** terms (shares, if earned, are issued as **small stock dividends** recorded at fair value):

| # | Contingency type | Terms |
|---|---|---|
| 1 | **Next-year NI target** (Demo 20-8 style) | Issue **6,000** common shares if **Year 2** net income **reaches or exceeds $420,000**. If met, issue on **January 10, Year 3**. |
| 2 | **Earnings formula (current year)** | Issue **25** common shares for each **$1,000** of Windmere consolidated NI **in excess of $300,000** for the year (whole $1,000 increments only). Issue earned shares on **January 10 of the following year**. |
| 3 | **Market-price contingency** | Issue **80** common shares for each **$4** increase in Windmere’s stock price from beginning-of-year price to year-end price (whole $4 increments only). Issue on **January 10 of the following year**. |
| 4 | **Patent awards** | Issue **1,500** common shares for each new patent awarded to Bolt during the year. Issue on **January 10 of the following year**. |

**Market prices and events**

| Item | Amount |
|---|---|
| Beginning Year 1 stock price | **$20** |
| Ending Year 1 stock price | **$36** |
| Patents awarded to Bolt in Year 1 | **2** |
| Fair value of Windmere stock on January 10, Year 2 | **$25** |
| Fair value of Windmere stock on January 10, Year 3 | **$28** |

**Reported net income**

| Year | Net income |
|---:|---:|
| Year 1 | **$480,000** |
| Year 2 | **$450,000** |
| Year 3 | **$500,000** |

Assume Year 2 has **no new** formula/market/patent contingencies beyond settling Year 1 earnouts and testing contingency #1. After January 10, Year 2, outstanding shares equal 90,000 plus Year 1 earnout shares issued. After January 10, Year 3, outstanding shares also include contingency #1 shares (if issued). Treat January 10 issuances as outstanding for essentially the **entire** remaining year for weighted-average purposes (use full-year WASO after issuance).

**Required:**  
a. Prepare the **January 1, Year 1 initial recognition journal entry** for the common stock issuance. Show Dr = Cr.  
b. **Period-end emphasis — Year 1 diluted share determination worksheet:** For each contingency (#1–#4), compute the number of contingently issuable shares that enter **diluted** EPS under the period-end = contingency-end rule. Total the diluted add-on. State how many enter **basic** EPS.  
c. Prepare the **Year 1 basic and diluted EPS computation schedule** (basic row + contingent effect). State the EPS amount(s) reported.  
d. Prepare the **December 31, Year 1 period-end closing entry** (Income Summary → Retained Earnings). State whether any additional period-end equity adjusting JE is required solely because diluted EPS includes contingent shares.  
e. Prepare the **January 10, Year 2 settlement / issuance JE** for all Year 1 formula, market, and patent shares earned. Confirm Dr = Cr.  
f. Compute **Year 2 basic and diluted EPS** (contingency #1 legal test uses actual Year 2 NI). Show the diluted schedule.  
g. Prepare the **December 31, Year 2 period-end closing entry**.  
h. Prepare the **January 10, Year 3 settlement JE** for contingency #1 (if earned).  
i. Build a **subsequent measurement / multi-year schedule** for Years 1–3: NI, basic WASO, contingent shares in diluted denominator, diluted WASO, basic EPS, diluted EPS, dual presentation?

**Answer key:**  

**a. January 1, Year 1 — initial recognition of common stock**

Cash proceeds = 90,000 × $12 = **$1,080,000**  
Common stock (par) = 90,000 × $1 = **$90,000**  
APIC—Common = $1,080,000 − $90,000 = **$990,000**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 1,080,000 | |
| Common Stock ($1 par) | | 90,000 |
| Additional Paid-in Capital—Common | | 990,000 |
| *Issue 90,000 shares of $1 par common at $12* | | |

**Check:** Dr = **1,080,000**; Cr = 90,000 + 990,000 = **1,080,000**. **Balanced.**

**b. Year 1 — period-end diluted share determination worksheet (emphasis)**

| # | Contingency | Period-end test | Contingent shares in **diluted** EPS |
|---|---|---|---:|
| 1 | Next-year NI ≥ $420,000 | As-if: use Year 1 NI **$480,000** as proxy → $480,000 ≥ $420,000 → **met** | **6,000** |
| 2 | Formula: 25 sh per $1,000 excess over $300,000 | Excess = $480,000 − $300,000 = **$180,000**; increments = 180,000 ÷ 1,000 = **180**; shares = 180 × 25 | **4,500** |
| 3 | Market: 80 sh per $4 rise over $20 | Rise = $36 − $20 = **$16**; increments = 16 ÷ 4 = **4**; shares = 4 × 80 | **320** |
| 4 | Patents: 1,500 × patents awarded | 2 patents awarded → conditions satisfied for those awards | **3,000** |
| | **Total contingent shares in diluted EPS** | | **13,820** |

**Basic EPS contingent shares Year 1 = 0** — none of these shares are outstanding in Year 1 (issuable next year / later). Demo 20-8 path keeps them out of basic until issued.

Numerator effect of all pure common contingencies: **none**.

**c. Year 1 EPS computation schedule**

| | Net income available to common | Weighted-average common shares | Per share |
|---|---:|---:|---:|
| **Basic EPS** | $480,000 | 90,000 | **$5.33** |
| Effect of contingently issuable stock: add shares | — | 13,820 | |
| **Diluted EPS** | $480,000 | 103,820 | **$4.62** |

Checks:  
Basic: $480,000 ÷ 90,000 = **$5.333… → $5.33**  
Diluted: $480,000 ÷ 103,820 = **$4.623… → $4.62**  
Diluted < basic → **dilutive**. Report both with equal prominence.

**d. December 31, Year 1 — period-end closing JE (emphasis)**

| Account | Debit | Credit |
|---|---:|---:|
| Income Summary | 480,000 | |
| Retained Earnings | | 480,000 |
| *Close Year 1 net income to retained earnings* | | |

**Check:** Dr = Cr = **480,000**. **Balanced.**

**No additional period-end equity adjusting JE** is recorded for the 13,820 contingent shares. Meeting the diluted as-if tests affects the **EPS denominator and disclosures only**. Common Stock / APIC change when shares are **actually issued** (part e / h). There is no “EPS expense” account.

**e. January 10, Year 2 — settlement JE (formula + market + patents)**

Shares issued = 4,500 + 320 + 3,000 = **7,820**  
Fair value = 7,820 × $25 = **$195,500**  
Par = 7,820 × $1 = **$7,820**  
APIC = $195,500 − $7,820 = **$187,680**

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings | 195,500 | |
| Common Stock ($1 par) | | 7,820 |
| Additional Paid-in Capital—Common | | 187,680 |
| *Issue 7,820 Year 1 earnout shares as stock dividend at FV $25* | | |

**Check:** Dr = **195,500**; Cr = 7,820 + 187,680 = **195,500**. **Balanced.**

Outstanding common after issuance = 90,000 + 7,820 = **97,820**.

**f. Year 2 basic and diluted EPS**

Actual Year 2 NI **$450,000** ≥ $420,000 → contingency #1 **conditions satisfied** by December 31, Year 2.  
For **diluted** EPS: include **6,000** shares from the **beginning of Year 2**.  
Basic WASO = **97,820** (shares already issued Jan 10; contingency #1 not yet issued).

| | Net income available to common | Weighted-average common shares | Per share |
|---|---:|---:|---:|
| **Basic EPS** | $450,000 | 97,820 | **$4.60** |
| Effect of contingently issuable stock: add shares | — | 6,000 | |
| **Diluted EPS** | $450,000 | 103,820 | **$4.33** |

Checks:  
Basic: $450,000 ÷ 97,820 = **$4.600… → $4.60**  
Diluted: $450,000 ÷ 103,820 = **$4.334… → $4.33**  
Dilutive; report both.

**g. December 31, Year 2 — period-end closing JE**

| Account | Debit | Credit |
|---|---:|---:|
| Income Summary | 450,000 | |
| Retained Earnings | | 450,000 |
| *Close Year 2 net income* | | |

**Check:** Dr = Cr = **450,000**. **Balanced.**

Again: **no** December 31 equity entry for the still-unissued 6,000 contingency #1 shares—only diluted EPS presentation and disclosure.

**h. January 10, Year 3 — settlement JE for contingency #1**

Fair value = 6,000 × $28 = **$168,000**  
Par = 6,000 × $1 = **$6,000**  
APIC = $168,000 − $6,000 = **$162,000**

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings | 168,000 | |
| Common Stock ($1 par) | | 6,000 |
| Additional Paid-in Capital—Common | | 162,000 |
| *Issue 6,000 contingency #1 shares as stock dividend at FV $28* | | |

**Check:** Dr = **168,000**; Cr = 6,000 + 162,000 = **168,000**. **Balanced.**

Outstanding / Year 3 WASO = 97,820 + 6,000 = **103,820**.

**i. Subsequent measurement schedule — Years 1–3**

| Year | NI | Basic WASO | Contingent in diluted | Diluted WASO | Basic EPS | Diluted EPS | Dual EPS? |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 480,000 | 90,000 | 13,820 | 103,820 | $5.33 | $4.62 | **Yes** |
| 2 | 450,000 | 97,820 | 6,000 | 103,820 | $4.60 | $4.33 | **Yes** |
| 3 | 500,000 | 103,820 | 0 (all issued) | 103,820 | $4.82 | $4.82 | Same |

Year 3 EPS: $500,000 ÷ 103,820 = **$4.816… → $4.82**.

**Roll-forward insight:** Contingent shares move from **period-end diluted-only add-ons (Y1 multi-type worksheet)** → **partly issued into basic WASO (Y2)** with remaining target still diluted-only → **fully outstanding (Y3)**. The **period-end determination worksheet + closing JE** is the emphasis path: EPS is presentation; books change on **issuance**.

**Key insight:** At each period-end, apply ASC 260-10-45-48: (a) if conditions are already satisfied, add shares from the start of that period for diluted; (b) if not legally satisfied, still add shares that would be issuable **if period-end were contingency-end**, when dilutive. Basic waits for actual outstanding shares. Period-end **closing** of NI always balances; contingent dilution alone does **not** create an equity adjusting JE.

---

### Q2 — CORE number variant — Next-year CEO target; Year 1 dilutive as-if; Year 2 miss; period-end schedules
**LO:** LO 20-8  
**Concept:** Number-variant twin of Demo 20-8 path: current-year earnings used as proxy for next-year NI target; period-end diluted EPS schedules; subsequent measurement when target later fails; no settlement JE  
**Scenario:**  
**Oakridge Analytics Inc.** reports the following.

| Fact | Amount / term |
|---|---|
| Year 1 net income | **$360,000** |
| Common shares outstanding entire Year 1 | **60,000** ($1 par) |
| Contingent agreement (entered beginning of Year 1) | Grant **5,000** common shares to the CEO if **Year 2** net income **reaches $340,000** |
| Year 2 net income (actual) | **$310,000** |
| Common shares outstanding entire Year 2 | **60,000** (no shares issued) |
| Other dilutive securities / preferred | **None** |

**Required:**  
a. **Period-end emphasis:** At December 31, Year 1, perform the as-if contingency-end test. How many contingent shares enter diluted EPS?  
b. Prepare the **Year 1 basic and diluted EPS computation schedule**.  
c. Prepare the **December 31, Year 1 period-end closing entry** for net income.  
d. Compute basic and diluted EPS for **Year 2**. How many contingent shares enter diluted EPS?  
e. Prepare a **two-year subsequent measurement schedule** (NI, basic WASO, contingent in diluted, diluted WASO, basic EPS, diluted EPS, dual?).  
f. Is there a **settlement / issuance JE** in Year 2 or Year 3? Why or why not?  
g. State Year 1 **income statement presentation** of EPS.

**Answer key:**  

**a. Year 1 period-end as-if test**

Agreement requires **Year 2** NI ≥ $340,000. Treat **December 31, Year 1** as if it were the end of the contingency period; use Year 1 current earnings as proxy:  
Year 1 NI **$360,000** ≥ $340,000 → **condition met under as-if rule**.  
Contingent shares in **diluted** EPS Year 1 = **5,000**.  
Contingent shares in **basic** EPS Year 1 = **0**.

**b. Year 1 EPS schedule**

| | Net income available to common | Weighted-average common shares | Per share |
|---|---:|---:|---:|
| **Basic EPS** | $360,000 | 60,000 | **$6.00** |
| Effect of contingently issuable stock: add shares | — | 5,000 | |
| **Diluted EPS** | $360,000 | 65,000 | **$5.54** |

Checks:  
Basic: $360,000 ÷ 60,000 = **$6.00**  
Diluted: $360,000 ÷ 65,000 = **$5.53846… → $5.54**  
Dilutive.

**c. December 31, Year 1 — period-end closing JE**

| Account | Debit | Credit |
|---|---:|---:|
| Income Summary | 360,000 | |
| Retained Earnings | | 360,000 |
| *Close Year 1 net income* | | |

**Check:** Dr = Cr = **360,000**. **Balanced.**

No equity adjusting JE for the 5,000 contingent shares.

**d. Year 2**

Actual Year 2 NI **$310,000** < $340,000 → conditions **not** satisfied.  
Contingent shares in diluted EPS Year 2 = **0**.  
Shares never issued → basic WASO still **60,000**.

Basic EPS = Diluted EPS = $310,000 ÷ 60,000 = **$5.166… → $5.17**

**e. Subsequent measurement schedule (Years 1–2)**

| Year | NI | Basic WASO | Contingent in diluted | Diluted WASO | Basic EPS | Diluted EPS | Dual? |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 360,000 | 60,000 | 5,000 | 65,000 | $6.00 | $5.54 | **Yes** |
| 2 | 310,000 | 60,000 | 0 | 60,000 | $5.17 | $5.17 | Same |

**f. Settlement JE**  
**No journal entry.** The performance condition failed; no shares are issued. Under the pure LO 20-8 contingent-EPS path, failure = zero shares and no equity issuance entry. (ASC 718 share-based compensation accounting, if the award were also a compensation arrangement, is a different LO.)

**g. Presentation Year 1**  
Report **basic EPS $6.00** and **diluted EPS $5.54** with equal prominence on the face of the income statement. Disclose the contingent arrangement (threshold, shares potentially issuable, as-if inclusion in diluted).

**Key insight:** Surpassing the dollar target in the **current** year pulls contingent shares into **diluted** EPS under the period-end as-if rule—even though the legal contingency still points at **next** year’s income. If next year misses, the subsequent measurement schedule drops the shares from diluted and **no issuance JE** is recorded. Period-end work is the diluted test + closing entry, not an equity reclass.

---

### Q3 — CORE alternate angle — Dual contingencies at period end; formula + market miss; closing + settlement
**LO:** LO 20-8  
**Concept:** Period-end determination of multiple contingency types (earnings threshold, earnings formula, market-price fail); basic vs diluted share counts; period-end closing JE; settlement issuance JE next year  
**Scenario:**  
**Pinnacle Braid Co.** has **40,000** common shares outstanding for the **entire** current year. No preferred stock and no other potentially dilutive securities. Net income for the year is **$220,000**. Common stock is **$2 par**.

Contingent stock agreement (in effect all year; any earned shares issuable **January 5 of the next year** as a stock dividend):

| Contingency | Terms | Period-end facts |
|---|---|---|
| A — Fixed earnings threshold | Issue **3,000** shares if current-year NI **exceeds $200,000** | NI = **$220,000** |
| B — Market price | Issue **2,000** shares if year-end market price is **at least $50** | Year-end price = **$48** |
| C — Earnings formula | Issue **100** shares for each **$10,000** of NI **in excess of $150,000** (whole increments only) | NI = **$220,000** |

Year-end market price used for the **settlement** FV next January 5 is **$46** (small stock dividend at FV).

**Required:**  
a. Prepare a **period-end contingent share determination schedule** for diluted EPS (each contingency).  
b. How many contingent shares enter **basic** EPS for the current year?  
c. Prepare a full **basic and diluted EPS computation schedule**.  
d. Show the **income statement presentation** of EPS for the current year.  
e. Prepare the **period-end closing entry** for net income. State whether any **additional period-end adjusting JE** is required for the contingent shares themselves.  
f. Assume next January 5 the board issues all earned shares at FV $46. Prepare the **settlement issuance JE** and confirm Dr = Cr.

**Answer key:**  

**a. Period-end contingent share schedule (diluted)**

| Contingency | Computation | Shares in diluted EPS |
|---|---|---:|
| A — NI > $200,000 | $220,000 > $200,000 → **met** | **3,000** |
| B — YE price ≥ $50 | $48 ≱ $50 → **not met** | **0** |
| C — Formula | Excess = $220,000 − $150,000 = **$70,000**; increments = 70,000 ÷ 10,000 = **7**; shares = 7 × 100 | **700** |
| **Total** | | **3,700** |

**b. Basic EPS contingent shares**  
**0** — shares not outstanding in the current year (issuable next year). Demo 20-8 / core path keeps them out of basic until issued.

**c. EPS computation schedule**

| | Numerator | Denominator | Per share |
|---|---:|---:|---:|
| **Basic EPS** | $220,000 | 40,000 | **$5.50** |
| Effect of contingently issuable stock: add shares | — | 3,700 | |
| **Diluted EPS** | $220,000 | 43,700 | **$5.03** |

Diluted: $220,000 ÷ 43,700 = **$5.034… → $5.03**. Dilutive (numerator unchanged).

**d. Financial statement presentation**

Pinnacle has a **complex capital structure** for EPS purposes because of dilutive contingently issuable shares.

**Income Statement (partial) — current year**

| | |
|---|---:|
| Net income | $220,000 |
| Basic earnings per share | **$5.50** |
| Diluted earnings per share | **$5.03** |

Disclose contingencies A–C, the **3,700** shares included in diluted EPS, the market contingency that failed the as-if test (2,000 potentially dilutive shares excluded), and a reconciliation of the basic-to-diluted denominator.

**e. Period-end closing JE; no contingent equity adjusting JE**

| Account | Debit | Credit |
|---|---:|---:|
| Income Summary | 220,000 | |
| Retained Earnings | | 220,000 |
| *Close current-year net income* | | |

**Check:** Dr = Cr = **220,000**. **Balanced.**

**No additional period-end adjusting JE** for the contingent shares under the LO 20-8 EPS path. The arrangement affects the **diluted EPS denominator and disclosure** now; equity accounts change when shares are **issued** (part f).

**f. Next-year settlement issuance JE (January 5)**

Shares issued = 3,000 + 700 = **3,700** (market contingency B failed — no shares).  
Fair value = 3,700 × $46 = **$170,200**  
Par = 3,700 × $2 = **$7,400**  
APIC = $170,200 − $7,400 = **$162,800**

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings | 170,200 | |
| Common Stock ($2 par) | | 7,400 |
| Additional Paid-in Capital—Common | | 162,800 |
| *Issue 3,700 earned contingent shares as stock dividend at FV $46* | | |

**Check:** Dr = **170,200**; Cr = 7,400 + 162,800 = **170,200**. **Balanced.**

**Key insight:** At period-end, test **each** contingency type separately under the as-if rule. Failed market tests contribute **zero** shares; met earnings/formula tests add to diluted only until issuance. The period-end closing entry always balances; settlement is a separate, balanced equity entry next period.

---

### Q4 — MC (classification / method) — When contingent shares enter diluted EPS
**LO:** LO 20-8  
**Concept:** Classification of when contingently issuable shares are included in diluted EPS under the as-if period-end rule  
**Question:**  
**Glacier Hollow Labs** has **80,000** common shares outstanding all year and net income of **$400,000**. In Year 1 it agreed that if Year 2 net income exceeds **$375,000**, it will issue **8,000** shares in Year 3. Year 1 net income is **$400,000**. No other potential common shares exist. Which statement is **correct** for Year 1?

- A) Include 8,000 shares in **basic** EPS only; diluted EPS is not reported.  
- B) Include 8,000 shares in **diluted** EPS (as-if contingency period ended at Year 1 year-end) because Year 1 NI exceeds $375,000; basic EPS uses 80,000 shares.  
- C) Include 8,000 shares in both basic and diluted EPS for the full year.  
- D) Exclude the 8,000 shares from both basic and diluted EPS because the legal condition refers to Year 2, not Year 1.

**Answer:** **B.**  
Under ASC 260 / Demo 20-8, if conditions have not yet been legally satisfied, diluted EPS still includes shares that would be issuable **if the end of the reporting period were the end of the contingency period**. Year 1 NI $400,000 > $375,000 → include 8,000 in diluted. Basic uses only outstanding shares (80,000). A reverses the treatment. C incorrectly puts shares in basic before issuance. D ignores the as-if diluted rule.

---

### Q5 — MC (presentation) — Conditions not met under as-if test; period-end presentation
**LO:** LO 20-8  
**Concept:** EPS presentation when contingently issuable shares fail the period-end as-if test  
**Question:**  
Same facts as Q4, except Year 1 net income is **$300,000** (below the $375,000 threshold). What is the correct Year 1 EPS reporting?

- A) Basic EPS $3.75; diluted EPS $3.41 (include 8,000 shares).  
- B) Basic EPS $5.00; diluted EPS $3.75.  
- C) Basic EPS = diluted EPS = $300,000 ÷ 80,000 = **$3.75**; contingent shares excluded from diluted because the as-if test fails.  
- D) No EPS is reported until Year 2 when the contingency is resolved.

**Answer:** **C.**  
$300,000 ≯ $375,000 → zero contingent shares in diluted. Basic = diluted = **$3.75**. A incorrectly includes shares. B uses wrong NI. D is false—EPS is reported every period. Period-end work is the as-if test (fail → no add-on) plus normal closing of NI; no settlement JE arises from a failed test.

---

### Self-check
- [x] Every JE balances (Q1 issuance $1,080,000; Q1 close $480,000; Q1 Y2 settlement $195,500; Q1 Y2 close $450,000; Q1 Y3 settlement $168,000; Q2 close $360,000; Q3 close $220,000; Q3 settlement $170,200)
- [x] Math recomputed (all EPS, share counts, FV/par/APIC splits double-checked)
- [x] Core demo path (Demo 20-8 / Review 20-8 / Problem 20-10 multi-type style / ASC 260-10-45-48)—not Expanding Your Knowledge sidebar
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5 classification/presentation only)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE (emphasis — closing + period-end diluted worksheet), disposal_maturity_or_settlement_JE (issuance)
- [x] Original companies/numbers (not textbook Gridley/Case demos; distinct from agents 122/253)
