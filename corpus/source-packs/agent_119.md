# Agent 119 — CORE DEMO — LO 20-5

**Chapter:** 20  
**LO title:** Compute EPS given share issuances, buybacks, dividends, and splits  
**Critical gap LO:** no

## Concept list for this pack
- **Basic EPS formula:** (Net income − preferred dividend claim) ÷ weighted-average common shares outstanding
- **Initial recognition JEs** for equity events that change shares: common issuance, treasury buyback, preferred cash dividend, large stock dividend (par)
- **Time-weighting** of share issuances and buybacks (fraction of year outstanding only)
- **Retroactive restatement** of stock dividends and stock splits to beginning of earliest period presented (and to all prior comparative periods)
- **Preferred dividends — cumulative:** deduct current-year claim whether or not declared
- **Preferred dividends — noncumulative:** deduct only dividends declared in the period
- **Common cash dividends:** no EPS numerator adjustment
- **Subsequent measurement schedule:** multi-row weighted-average common shares schedule (actual shares × retroactive factor × fraction of year)
- **Period-end / presentation:** single basic EPS line when capital structure is simple; disclose post-period split/dividend effects when restating
- **Stock split settlement (memo):** change in legal shares/par without RE transfer at fair value
- **Number-variant twin:** same structure, all different amounts and dates

---

### Q1 — CORE — Share issuance, buyback, preferred dividend, stock dividend: JEs + WAS + basic EPS
**LO:** LO 20-5  
**Concept:** Initial recognition JEs for issuance, treasury buyback, preferred dividend, and large stock dividend; weighted-average shares schedule with retroactive stock-dividend factor; basic EPS and income-statement presentation  
**Scenario:**  
**Northlake Precision Inc.** has a simple capital structure and a calendar year. On **January 1, 2025**, the company has:

| Item | Amount |
|---|---|
| Common stock outstanding | **120,000** shares, **$2** par |
| Cumulative preferred stock outstanding | **8,000** shares, **6%**, **$25** par (outstanding all year) |
| Net income for 2025 | **$378,000** |

Equity activity during 2025:

| Date | Event |
|---|---|
| **April 1** | Issued **30,000** common shares for cash at **$14** per share. |
| **July 1** | Purchased **6,000** common shares for the **treasury** at **$16** per share (shares remain outstanding legally but are not outstanding for EPS). |
| **September 30** | Declared and paid cash dividends equal to the **full annual preferred claim**. |
| **November 1** | Declared and distributed a **20%** common stock dividend. Market price that day is **$18**. Treat the 20% stock dividend as a **large** stock dividend and record at **par**. |

No common cash dividends affect the EPS numerator. Ignore income taxes.

**Required:**  
a. Prepare the **initial recognition journal entries** for April 1 (issuance), July 1 (buyback), September 30 (preferred dividend), and November 1 (stock dividend). Show Dr = Cr for each.  
b. Prepare a **weighted-average common shares schedule** for 2025, applying the **retroactive restatement** factor for the stock dividend to all periods before November 1.  
c. Compute **income available to common stockholders** and **basic EPS** for 2025 (round EPS to the nearest cent).  
d. Show how **basic EPS** is **presented** on the 2025 income statement (simple capital structure).  
e. Briefly explain why the stock dividend is treated differently from the April 1 cash issuance in the denominator.

**Answer key:**  

**a. Initial recognition journal entries**

*April 1 — Issue 30,000 common shares at $14*

| Account | Debit | Credit |
|---|---:|---:|
| Cash (30,000 × $14) | 420,000 | |
| Common Stock (30,000 × $2) | | 60,000 |
| Paid-in Capital in Excess of Par—Common (30,000 × $12) | | 360,000 |
| *Record cash issuance of common stock* | | |

**Check:** Dr = Cr = **420,000**. Shares outstanding become 120,000 + 30,000 = **150,000**.

*July 1 — Treasury buyback of 6,000 shares at $16 (cost method)*

| Account | Debit | Credit |
|---|---:|---:|
| Treasury Stock (6,000 × $16) | 96,000 | |
| Cash | | 96,000 |
| *Record purchase of treasury shares* | | |

**Check:** Dr = Cr = **96,000**. Shares outstanding for EPS become 150,000 − 6,000 = **144,000**.

*September 30 — Preferred dividend (full annual claim)*

Annual preferred claim = 6% × $25 × 8,000 = **$12,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings (or Preferred Dividends) | 12,000 | |
| Cash | | 12,000 |
| *Declare and pay cumulative preferred dividend claim* | | |

**Check:** Dr = Cr = **12,000**.  
(If declared earlier and paid later: Dr RE / Cr Dividends Payable, then Dr Dividends Payable / Cr Cash — same net effect.)

*November 1 — 20% large stock dividend at par*

New shares = 144,000 × 20% = **28,800**.  
Par transferred = 28,800 × $2 = **$57,600**.

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings | 57,600 | |
| Common Stock (28,800 × $2) | | 57,600 |
| *Record large 20% stock dividend at par* | | |

**Check:** Dr = Cr = **57,600**. Shares outstanding become 144,000 + 28,800 = **172,800**.  
(No cash; no EPS numerator effect. Market price is irrelevant for large stock dividend at par.)

**b. Weighted-average common shares schedule (retroactive factor 1.20)**

Stock dividend factor = 1 + 20% = **1.20**, applied to **all** share counts **before** November 1 (treated as if the stock dividend occurred at the beginning of the earliest period presented).

| Inclusive dates | Actual shares outstanding | Retroactive factor | Equivalent shares | Months | Fraction of year | Weighted-average shares |
|---|---:|---:|---:|---:|---:|---:|
| Jan 1 – Mar 31 | 120,000 | 1.20 | 144,000 | 3 | 3/12 | **36,000** |
| Apr 1 – Jun 30 | 150,000 | 1.20 | 180,000 | 3 | 3/12 | **45,000** |
| Jul 1 – Oct 31 | 144,000 | 1.20 | 172,800 | 4 | 4/12 | **57,600** |
| Nov 1 – Dec 31 | 172,800 | 1.00 | 172,800 | 2 | 2/12 | **28,800** |
| **Total** | | | | **12** | **100%** | **167,400** |

*Checks:*  
36,000 + 45,000 + 57,600 + 28,800 = **167,400**.  
Issuance (Apr 1) and buyback (Jul 1) are **time-weighted only** (not retroactive). Stock dividend is **fully retroactive**.

**c. Income available and basic EPS**

| | Amount |
|---|---:|
| Net income | $378,000 |
| Less: preferred dividends (cumulative current-year claim) | (12,000) |
| **Income available to common stockholders** | **$366,000** |
| ÷ Weighted-average common shares | 167,400 |
| **Basic EPS** | **$2.19** |

Computation: $366,000 ÷ 167,400 = 2.18638… → **$2.19** (nearest cent).

**d. Income-statement presentation (simple capital structure)**

```
Earnings per share:
  Basic earnings per share ...............  $2.19
```

Only **basic** EPS is required when there are no dilutive potential common shares. Preferred stock that is not convertible does not create a complex capital structure for diluted EPS purposes under this LO’s simple-structure demos.

**e. Why stock dividend ≠ cash issuance in the denominator**  
A **cash issuance** brings new capital that was available only for the portion of the year after issuance → **time-weight**. A **stock dividend** does not bring new capital; it merely subdivides ownership → treat as outstanding **from the beginning of the earliest period presented** (retroactive restatement), including comparative periods if presented.

**Key insight:** Build the **share timeline first**, then apply **retroactive stock-dividend/split factors** to every pre-event row, and **time-weight** only true capital changes (issuances and buybacks). Subtract the **preferred claim** (full year if cumulative) from net income before dividing.

---

### Q2 — CORE number variant — Issuance, buyback, preferred, stock dividend twin
**LO:** LO 20-5  
**Concept:** Number-variant twin of weighted-average basic EPS with cash issuance, treasury buyback, cumulative preferred dividends, and stock-dividend retroactive restatement; supporting equity JEs  
**Scenario:**  
**SummitRidge Labs Corp.** (calendar year, simple capital structure) begins **January 1, 2025** with:

| Item | Amount |
|---|---|
| Common stock outstanding | **90,000** shares, **$1** par |
| Cumulative preferred stock outstanding | **5,000** shares, **8%**, **$40** par (all year) |
| Net income for 2025 | **$256,000** |

| Date | Event |
|---|---|
| **May 1** | Issued **24,000** common shares for cash at **$20** per share. |
| **August 1** | Purchased **9,000** common shares for the treasury at **$22** per share. |
| **October 1** | Declared and paid cash dividends equal to the **full annual preferred claim**. |
| **December 1** | Declared and distributed a **25%** common stock dividend. Record as a **large** stock dividend at **par**. |

**Required:**  
a. Journal entries for May 1, August 1, October 1, and December 1 (balanced).  
b. Weighted-average common shares schedule with retroactive stock-dividend factor.  
c. Income available to common and basic EPS (nearest cent).  
d. State the single line amount reported for basic EPS on the income statement.

**Answer key:**  

**a. Journal entries**

*May 1 — Issue 24,000 shares at $20*

| Account | Debit | Credit |
|---|---:|---:|
| Cash (24,000 × $20) | 480,000 | |
| Common Stock (24,000 × $1) | | 24,000 |
| Paid-in Capital in Excess of Par—Common | | 456,000 |

**Check:** Dr = Cr = **480,000**. Outstanding → 90,000 + 24,000 = **114,000**.

*August 1 — Treasury purchase*

| Account | Debit | Credit |
|---|---:|---:|
| Treasury Stock (9,000 × $22) | 198,000 | |
| Cash | | 198,000 |

**Check:** Dr = Cr = **198,000**. Outstanding for EPS → 114,000 − 9,000 = **105,000**.

*October 1 — Preferred dividends*

Annual claim = 8% × $40 × 5,000 = **$16,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings | 16,000 | |
| Cash | | 16,000 |

**Check:** Dr = Cr = **16,000**.

*December 1 — 25% large stock dividend at par*

New shares = 105,000 × 25% = **26,250**.  
Par = 26,250 × $1 = **$26,250**.

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings | 26,250 | |
| Common Stock | | 26,250 |

**Check:** Dr = Cr = **26,250**. Outstanding → 105,000 + 26,250 = **131,250**.

**b. Weighted-average shares (factor 1.25)**

| Inclusive dates | Actual shares | Factor | Equivalent shares | Months | Fraction | WAS |
|---|---:|---:|---:|---:|---:|---:|
| Jan 1 – Apr 30 | 90,000 | 1.25 | 112,500 | 4 | 4/12 | **37,500** |
| May 1 – Jul 31 | 114,000 | 1.25 | 142,500 | 3 | 3/12 | **35,625** |
| Aug 1 – Nov 30 | 105,000 | 1.25 | 131,250 | 4 | 4/12 | **43,750** |
| Dec 1 – Dec 31 | 131,250 | 1.00 | 131,250 | 1 | 1/12 | **10,937.50** |
| **Total** | | | | **12** | | **127,812.50** |

**c. Basic EPS**

| | Amount |
|---|---:|
| Net income | $256,000 |
| Less: preferred dividends | (16,000) |
| Income available to common | **$240,000** |
| ÷ WAS | 127,812.50 |
| **Basic EPS** | **$1.88** |

$240,000 ÷ 127,812.50 = 1.87775… → **$1.88**.

**d. Presentation**  
Income statement reports **Basic earnings per share $1.88** (only basic line needed for simple capital structure).

**Key insight:** Same mechanics as Q1 with different dates and amounts — always recompute the **share timeline**, apply the **stock-dividend multiplier to every earlier band**, and deduct the **preferred claim** before dividing.

---

### Q3 — CORE alternate angle — Noncumulative preferred (undeclared), 2-for-1 split, comparative restatement, treasury settlement
**LO:** LO 20-5  
**Concept:** Noncumulative preferred with no declaration (no numerator deduction); 2-for-1 stock split retroactive restatement and memo/settlement of legal capital; comparative prior-year EPS restatement; optional year-end treasury reissuance JE  
**Scenario:**  
**Brightwater Media Co.** (calendar year) reports the following for **2025**:

| Item | Amount |
|---|---|
| Net income | **$480,000** |
| Common shares outstanding, Jan 1 | **100,000** ($5 par) |
| Noncumulative preferred stock | **6,000** shares, **7%**, **$50** par, outstanding all year |
| Preferred dividends declared in 2025 | **$0** |
| Basic EPS reported for **2024** (before any restatement) | **$3.00** (based on 100,000 weighted-average shares; no split in 2024) |

2025 equity events:

| Date | Event |
|---|---|
| **March 31** | Issued **20,000** common shares for cash at **$28** per share. |
| **June 30** | Purchased **10,000** common shares for the treasury at **$30** per share (cost method). |
| **October 31** | Effected a **2-for-1** common stock split. Par is reduced from $5 to **$2.50**; number of authorized/issued/outstanding shares doubles for legal capital. No transfer from retained earnings at fair value. |
| **December 31** | Reissued **2,000** treasury shares (post-split equivalent; cost basis **$15** per post-split share) for cash at **$17** per share. Because reissuance occurs on the last day of the year, the shares contribute **0/12** to 2025 WAS. |

**Required:**  
a. Compute the **preferred dividend adjustment** (if any) for basic EPS and contrast what the adjustment would have been if the preferred stock were **cumulative**.  
b. Prepare the **March 31** issuance JE, the **June 30** treasury purchase JE, the **October 31** stock-split entry (or memo), and the **December 31** treasury **reissuance (settlement)** JE. All must balance.  
c. Prepare the **2025 weighted-average common shares schedule** with the **2.0** retroactive split factor.  
d. Compute **2025 basic EPS** (nearest cent).  
e. Compute **restated 2024 basic EPS** for comparative presentation and state the disclosure concept.  
f. Classification/presentation: what EPS amount(s) appear on the face of the 2025 income statement for a simple capital structure?

**Answer key:**  

**a. Preferred dividend adjustment**

Noncumulative, **no dividends declared** → **$0** deducted from net income.  
Income available to common = **$480,000**.

*Contrast — if cumulative:* annual claim = 7% × $50 × 6,000 = **$21,000**, deducted even if undeclared → available = $480,000 − $21,000 = **$459,000**.  
*(Not used in the EPS calculation below; preferred is noncumulative.)*

**b. Journal entries**

*March 31 — Issue 20,000 shares at $28*

| Account | Debit | Credit |
|---|---:|---:|
| Cash (20,000 × $28) | 560,000 | |
| Common Stock (20,000 × $5) | | 100,000 |
| Paid-in Capital in Excess of Par—Common | | 460,000 |

**Check:** Dr = Cr = **560,000**. Outstanding → 120,000.

*June 30 — Treasury buyback (pre-split cost)*

| Account | Debit | Credit |
|---|---:|---:|
| Treasury Stock (10,000 × $30) | 300,000 | |
| Cash | | 300,000 |

**Check:** Dr = Cr = **300,000**. Outstanding for EPS → 110,000 (pre-split).  
Treasury cost total **$300,000** for 10,000 pre-split shares = **$30** pre-split = **$15** per post-split share after 2-for-1.

*October 31 — 2-for-1 stock split (legal capital reclass / memo)*

Pre-split common stock outstanding for legal capital tracking (excluding treasury complications for the reclass illustration): companies often reclassify the common stock account so total par capital is unchanged when par is halved and shares double.

Illustrative reclass for **outstanding** common (110,000 pre-split → 220,000 post-split at $2.50):

| Account | Debit | Credit |
|---|---:|---:|
| Common Stock ($5 par) — 110,000 × $5 | 550,000 | |
| Common Stock ($2.50 par) — 220,000 × $2.50 | | 550,000 |
| *2-for-1 split: double shares, half par; total legal capital unchanged* | | |

**Check:** Dr = Cr = **550,000**.  
(Many firms use a **memo entry only** if the common stock account is stated in shares without a formal par reclass; either approach leaves **no effect on total equity** and **no RE transfer**.)

Treasury shares also split: 10,000 → **20,000** treasury shares; carrying amount remains **$300,000** ($15 post-split unit cost).

*December 31 — Reissue 2,000 post-split treasury shares at $17 (settlement)*

Cost removed = 2,000 × $15 = **$30,000**.  
Cash = 2,000 × $17 = **$34,000**.  
APIC—Treasury = $4,000.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 34,000 | |
| Treasury Stock | | 30,000 |
| Paid-in Capital from Treasury Stock | | 4,000 |
| *Reissue treasury shares above cost* | | |

**Check:** Dr = Cr = **34,000**.  
WAS impact for 2025: **0** (outstanding 0 days in 2025).

**c. Weighted-average shares (split factor 2.0)**

| Inclusive dates | Actual shares (pre-restatement basis) | Factor | Equivalent shares | Months | Fraction | WAS |
|---|---:|---:|---:|---:|---:|---:|
| Jan 1 – Mar 31 | 100,000 | 2.0 | 200,000 | 3 | 3/12 | **50,000** |
| Apr 1 – Jun 30 | 120,000 | 2.0 | 240,000 | 3 | 3/12 | **60,000** |
| Jul 1 – Oct 31 | 110,000 | 2.0 | 220,000 | 4 | 4/12 | **73,333** |
| Nov 1 – Dec 31 | 220,000 | 1.0 | 220,000 | 2 | 2/12 | **36,667** |
| **Total** | | | | **12** | | **220,000** |

(Using exact fractions: 110,000 × 2 × 4/12 = 220,000/3 = 73,333⅓; 220,000 × 2/12 = 110,000/3 = 36,666⅔; sum = **220,000**.)

**d. 2025 basic EPS**

\[
\text{Basic EPS} = \frac{\$480{,}000 - \$0}{220{,}000} = \mathbf{\$2.18}
\]

($480,000 ÷ 220,000 = 2.1818… → **$2.18**)

**e. Comparative restatement of 2024**

2024 WAS must be restated for the 2025 split: 100,000 × 2 = **200,000**.  
Restated 2024 basic EPS = $3.00 × (100,000 / 200,000) = **$1.50**  
(equivalently, original numerator ÷ restated WAS).

**Disclosure concept:** If a stock split (or stock dividend) occurs **after the balance sheet date but before issuance** of the financial statements, EPS for the period just ended **and** any comparative periods must still reflect the split. Disclose that per-share amounts have been restated for the change in capital structure.

**f. Presentation**  
Face of 2025 income statement (simple capital structure):

```
Earnings per share:
  Basic earnings per share ...............  $2.18
```

Comparative column (if presented) shows restated **$1.50** for 2024. No diluted EPS line required under the simple-structure assumption of this LO pack.

**Key insight:** **Noncumulative** preferred with no declaration leaves the numerator untouched; **splits** multiply every pre-split share band (and prior periods) by the split factor without time-weighting the split itself; treasury **reissuance** is a settlement of treasury equity that changes shares only from the reissue date forward.

---

### Q4 — MC — Retroactive treatment of stock splits vs issuances
**LO:** LO 20-5  
**Concept:** Classification of denominator treatment — stock split/dividend (retroactive) versus cash share issuance (time-weighted)  
**Question:**  
In computing **basic EPS** for the current year, how should a **2-for-1 stock split** declared mid-year be reflected in the weighted-average common shares denominator, compared with a mid-year **cash sale of new common shares**?

- A) Both the split and the cash sale are weighted only from the date they occur.  
- B) The split is applied **retroactively** to all periods presented (as if outstanding from the beginning of the earliest period); the cash sale is **time-weighted** only for the fraction of the year the new shares are outstanding.  
- C) The cash sale is applied retroactively to the beginning of the year; the split is time-weighted from the split date.  
- D) Neither event affects basic EPS; both affect only diluted EPS.

**Answer:** **B.**  
Stock dividends and stock splits are restated **retroactively** for all periods presented because they do not bring new capital. Shares issued for cash (or reacquired) are outstanding only for the **portion of the period** after issuance (or before buyback) and are therefore **time-weighted**.

---

### Q5 — MC — Preferred dividend effect on the EPS numerator
**LO:** LO 20-5  
**Concept:** Classification of numerator adjustment — cumulative vs noncumulative preferred dividends  
**Question:**  
A company has **noncumulative** preferred stock outstanding all year and **declares no preferred dividends** this year. Separately, another company has **cumulative** preferred stock with the same annual dividend claim and also **declares no preferred dividends**. Which statement is correct for **basic EPS** numerators?

- A) Both companies deduct the full annual preferred claim.  
- B) Neither company deducts any preferred claim.  
- C) Only the company with **cumulative** preferred deducts the full current-year claim; the noncumulative company deducts **$0**.  
- D) Only the company with **noncumulative** preferred deducts the claim, because cumulative dividends are ignored until paid.

**Answer:** **C.**  
**Cumulative** preferred: subtract the **current-year** dividend claim whether or not declared (prior years’ arrears were already considered in prior EPS). **Noncumulative** preferred: subtract only dividends **declared** in the current period — if none declared, **no** numerator reduction. Common cash dividends never adjust the EPS numerator.

---

### Self-check
- [x] Every JE balances (Dr = Cr shown)
- [x] Math recomputed (WAS schedules and EPS verified)
- [x] Core demo not sidebar-only (Demo 20-5 path: issuances, buybacks, stock dividends/splits, preferred)
- [x] LO + Concept on every item
- [x] MC ≤ 2
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (WAS), period_end/presentation, disposal/settlement (treasury reissue + split reclass), classification/disclosure, number_variant_twin
