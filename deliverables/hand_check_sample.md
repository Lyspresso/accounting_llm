# Hand-check sample — 20 items

Composition: 10 machine-passed, 5 parity flips, 5 KEY_SILENT-heavy.
Confirmations feed `goldens/` and make the false-positive floor real.

For each item: read the Required parts, check the solver's figures against
the key, and mark the verdict. **Where you disagree with the machine verdict,
that is the finding** — it is the only measurement of the comparator's
false-positive rate that does not come from the comparator itself.

| # | item | ch | category | machine verdict | your verdict | notes |
|---|---|---|---|---|---|---|
| 1 | `agent_295#02` | 22 | machine_passed | machine_passed |  |  |
| 2 | `agent_119#00` | 20 | machine_passed | machine_passed |  |  |
| 3 | `agent_254#00` | 20 | machine_passed | machine_passed |  |  |
| 4 | `agent_381#02` | 20 | machine_passed | machine_passed |  |  |
| 5 | `agent_229#00` | 15 | machine_passed | machine_passed |  |  |
| 6 | `agent_392#00` | 22 | machine_passed | machine_passed |  |  |
| 7 | `agent_219#05` | 13 | machine_passed | machine_passed |  |  |
| 8 | `agent_279#01` | 16 | machine_passed | machine_passed |  |  |
| 9 | `agent_135#01` | 14 | machine_passed | machine_passed |  |  |
| 10 | `agent_016#00` | 16 | machine_passed | machine_passed |  |  |
| 11 | `agent_032#01` | 18 | flip | machine_passed |  |  |
| 12 | `agent_043#00` | 8 | flip | machine_passed |  |  |
| 13 | `agent_053#01` | 9 | flip | machine_passed |  |  |
| 14 | `agent_107#02` | 19 | flip | failed |  |  |
| 15 | `agent_130#00` | 22 | flip | machine_passed |  |  |
| 16 | `agent_303#02` | 8 | key_silent_heavy | machine_passed |  |  |
| 17 | `agent_333#02` | 11 | key_silent_heavy | failed |  |  |
| 18 | `agent_268#00` | 14 | key_silent_heavy | failed |  |  |
| 19 | `agent_204#02` | 11 | key_silent_heavy | machine_passed |  |  |
| 20 | `agent_183#01` | 9 | key_silent_heavy | machine_passed |  |  |

---

## 1. `agent_295#02` — chapter 22 — machine_passed

**Machine verdict:** baseline `machine_passed`, trim `machine_passed`  
**Required parts detected:** a, b, c, d, e  
**Coverage:** baseline 1.0, trim 1.0

### Question

### Q3 — CORE alternate angle — Period-end adjusting JEs, edge classifications, cash composition, reverse reconciliation
**LO:** LO 22-1  
**Concept:** Period-end cash (cash + equivalents + restricted cash) reconciliation; period-end adjusting JEs (interest accrual, dividend declaration) vs cash settlement; edge-case classification (trading securities; finance-lease principal; noncash land-for-note); disposal of building and maturity settlement of bonds; solve for beginning cash  
**Scenario:**  
**Tidewater Specialty Brands LLC** is closing its books for the year ended **December 31, 2027**. Controllers prepared both cash events and period-end adjustments.

**Selected cash and noncash events:**

1. Sold a building for **$140,000** cash. Original cost $220,000; accumulated depreciation at sale **$95,000**.  
2. On maturity date, paid **$80,000** cash to settle bonds payable at face (no gain/loss).  
3. During the year, paid **$9,600** cash interest on those bonds (before maturity).  
4. **Period-end adjusting JE:** accrued **$2,400** unpaid interest (Dr Interest Expense / Cr Interest Payable) — no cash on Dec 31.  
5. Purchased production equipment for **$55,000** cash.  
6. Acquired land by issuing a **$90,000** long-term note payable (no cash exchanged).  
7. Borrowed **$50,000** cash on a long-term bank note (nontrade).  
8. Paid **$12,000** cash principal on a finance lease liability.  
9. **Period-end adjusting JE:** declared **$10,000** cash dividends payable in January 2028 (Dr RE / Cr Dividends Payable) — no cash on Dec 31.  
10. Paid **$7,500** cash dividends that had been declared in the **prior** year.  
11. Cash collections from customers **$285,000**; cash paid to suppliers and employees **$240,000**; cash paid for income taxes **$14,000**.  
12. Purchased short-term **trading** equity securities (held specifically for resale / trading profits) for **$16,000** cash.

**Period-end cash composition (Dec 31, 2027):**

| Account | Amount |
|---|---:|
| Cash in bank (unrestricted) | $71,000 |
| Money-market cash equivalents | 9,500 |
| Restricted cash (compensating balance) | 4,000 |
| Short-term equity investments (not cash equivalents; not trading inventory for this table) | 19,000 |

**Required:**  
a. Prepare journal entries for items **1** (disposal), **2** (maturity settlement), **4** (period-end interest accrual), **5** (PPE purchase), **7** (debt issuance), and **9** (period-end dividend declaration). Prove each balances.  
b. Classify the **cash** effect of items 1–3, 5, 7–8, and 10–12 as O / I / F (inflow or outflow). State how items **4, 6, and 9** are reported (or not) on the SCF.  
c. Compute the **ending cash total** that appears on the SCF reconciliation. Compute net cash from **operating**, **investing**, and **financing**; net change in cash; solve for **beginning** cash.  
d. Present SCF section order and the three-line cash reconciliation (change + beginning = ending).  
e. True/False with correction: “Investing cash flows may be reported net (purchases net of sales of PPE) to simplify the SCF.”

### The key's answer

**Answer key:**

**a. Journal entries**

**1 — Disposal of building**  
Book value = $220,000 − $95,000 = **$125,000**; gain = $140,000 − $125,000 = **$15,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 140,000 | |
| Accumulated Depreciation—Building | 95,000 | |
| Building | | 220,000 |
| Gain on Sale of Building | | 15,000 |

**Check:** Dr 140,000 + 95,000 = Cr 220,000 + 15,000 → **$235,000 = $235,000**. **Balanced.**

**2 — Maturity settlement of bonds**

| Account | Debit | Credit |
|---|---:|---:|
| Bonds Payable | 80,000 | |
| Cash | | 80,000 |

**Check:** Dr = Cr = 80,000. **Balanced.**

**4 — Period-end interest accrual (emphasis)**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 2,400 | |
| Interest Payable | | 2,400 |

**Check:** Dr = Cr = 2,400. **Balanced.**  
**SCF cash:** none.

**5 — Purchase equipment**

| Account | Debit | Credit |
|---|---:|---:|
| Equipment | 55,000 | |
| Cash | | 55,000 |

**Check:** Dr = Cr = 55,000. **Balanced.**

**7 — Issue long-term bank note**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 50,000 | |
| Notes Payable—Long-term | | 50,000 |

**Check:** Dr = Cr = 50,000. **Balanced.**

**9 — Period-end dividend declaration (emphasis)**

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings (or Dividends) | 10,000 | |
| Dividends Payable | | 10,000 |

**Check:** Dr = Cr = 10,000. **Balanced.**  
**SCF cash:** none in 2027; financing outflow when paid in 2028.

**b. Cash classification**

| Item | Cash effect | Class |
|---|---|---|
| 1 Sale of building | Inflow $140,000 | **Investing** |
| 2 Bond principal at maturity | Outflow $80,000 | **Financing** |
| 3 Interest paid | Outflow $9,600 | **Operating** |
| 4 Interest accrual | **No cash** | Not a cash line on SCF |
| 5 Purchase equipment | Outflow $55,000 | **Investing** |
| 6 Land for LT note | **No cash** | Disclose as **noncash investing and financing** activity (supplemental) |
| 7 LT bank borrowing | Inflow $50,000 | **Financing** |
| 8 Finance lease principal paid | Outflow $12,000 | **Financing** |
| 9 Dividend declaration | **No cash** | Not a cash line on SCF |
| 10 Prior-year dividends paid | Outflow $7,500 | **Financing** |
| 11 Customer collections | Inflow $285,000 | **Operating** |
| 11 Suppliers/employees | Outflow $240,000 | **Operating** |
| 11 Income taxes paid | Outflow $14,000 | **Operating** |
| 12 Purchase of **trading** securities | Outflow $16,000 | **Operating** (trading / held for resale) |

**c. Ending cash, section nets, and beginning cash**

SCF “cash” total at Dec 31, 2027:  
$71,000 + $9,500 + $4,000 = **$84,500**  
*(Exclude $19,000 short-term equity investments — not cash, cash equivalents, or restricted cash.)*

**Operating:**  
Inflows: customer collections $285,000  
Outflows: suppliers/employees $240,000 + income taxes $14,000 + interest $9,600 + trading securities purchase $16,000 = **$279,600**  
Net cash provided by operating activities = $285,000 − $279,600 = **$5,400**

**Investing:**  
Inflow: building sale $140,000  
Outflow: equipment $55,000  
Net cash provided by investing activities = $140,000 − $55,000 = **$85,000**

**Financing:**  
Inflow: bank note $50,000  
Outflows: bond principal $80,000 + lease principal $12,000 + dividends paid $7,500 = **$99,500**  
Net cash used by financing activities = $50,000 − $99,500 = **$(49,500)**

**Change in cash:**  
$5,400 + $85,000 − $49,500 = **$40,900** increase.

**Beginning cash:**  
Ending $84,500 − increase $40,900 = **$43,600**.  
Check: $43,600 + $40,900 = $84,500.

| | Amount |
|---|---:|
| Net cash provided by operating activities | $5,400 |
| Net cash provided by investing activities | 85,000 |
| Net cash used by financing activities | (49,500) |
| Net increase in cash | 40,900 |
| Cash at beginning of period | 43,600 |
| **Cash at end of period** | **$84,500** |

**d. Format / reconciliation**

Order on SCF: **(1) Operating → (2) Investing → (3) Financing**, then:

### Blind solver (baseline) — figures

- `b: cash-effect classification of item 1` = **I - inflow $140,000 (proceeds from sale of building; reported gross)**
- `b: cash-effect classification of item 2` = **F - outflow $80,000 (repayment of bond principal at maturity)**
- `b: cash-effect classification of item 3` = **O - outflow $9,600 (interest paid)**
- `b: cash-effect classification of item 5` = **I - outflow $55,000 (purchase of production equipment)**
- `b: cash-effect classification of item 7` = **F - inflow $50,000 (proceeds from long-term nontrade bank note)**
- `b: cash-effect classification of item 8` = **F - outflow $12,000 (finance lease principal; lease interest would be O)**
- `b: cash-effect classification of item 10` = **F - outflow $7,500 (cash dividends paid)**
- `b: cash-effect classification of item 11` = **O - inflow $285,000 collections; O - outflow $240,000 suppliers/employees; O - outflow $14,000 income taxes**
- `b: cash-effect classification of item 12` = **O - outflow $16,000 (trading securities bought for resale are operating, not investing)**
- `b: SCF reporting of item 4` = **Item 4 (accrued $2,400 interest): no cash effect, so it is NOT a cash flow line. Under the indirect method it appears only as a reconciling add-back (increase in interest payable) within operating activities; under the direct method it does not appear at all.**
- `b: SCF reporting of item 6` = **Item 6 (land acquired for a $90,000 note): noncash investing and financing transaction. Excluded from the body of the SCF; disclosed in the supplemental schedule of noncash investing and financing activities.**
- `b: SCF reporting of item 9` = **Item 9 (declared $10,000 dividends payable in Jan 2028): no cash effect, so it is NOT reported in financing activities this year. It is a noncash declaration (disclosed / reflected as an increase in dividends payable); the cash outflow will be a financing outflow in 2028 when paid.**
- `c: ending cash total on the SCF reconciliation (cash + cash equivalents + restricted cash, Dec 31 2027)` = **84500**
- `c: net cash provided by operating activities` = **5400**
- `c: net cash provided by investing activities` = **85000**
- `c: net cash used by financing activities` = **-49500**
- `c: net change in cash` = **40900**
- `c: beginning cash (Jan 1, 2027), solved` = **43600**
- `d: SCF section order and three-line cash reconciliation` = **SCF section order: (1) Cash flows from operating activities; (2) Cash flows from investing activities; (3) Cash flows from financing activities; then net increase (decrease) in cash, cash equivalents, and restricted cash; plus cash, cash equivalents, and restricted cash at January 1, 2027; equals cash, cash equivalents, and restricted cash at December 31, 2027. Supplemental disclosures follow: noncash investing and financing activities (land acquired by issuing a $90,000 note) and, under the indirect method, interest paid and income taxes paid. Three-line reconciliation: net change $40,900.00 + beginning $43,600.00 = ending $84,500.00.**
- `e: True/False with correction` = **False. Investing (and financing) cash flows must generally be reported GROSS - cash receipts and cash payments are shown separately (ASC 230-10-45-26), e.g. proceeds from the sale of the building ($140,000) shown apart from the purchase of equipment ($55,000), not netted to $85,000 on one line. The only exception (ASC 230-10-45-8/45-9) is net reporting for items with quick turnover, large amounts, and original maturities of three months or less - certain investments other than cash equivalents, loans receivable, and debt (e.g. a revolving line of credit) - which does not cover purchases and sales of PPE.**

### Blind solver (trim) — figures

- `a: item 1 JE proof - total debits = total credits` = **235000**
- `a: item 2 JE proof - total debits = total credits` = **80000**
- `a: item 4 JE proof - total debits = total credits` = **2400**
- `a: item 5 JE proof - total debits = total credits` = **55000**
- `a: item 7 JE proof - total debits = total credits` = **50000**
- `a: item 9 JE proof - total debits = total credits` = **10000**
- `a: item 1 supporting - book value of building at sale (cost - accum. dep.)` = **125000**
- `a: item 1 supporting - gain on sale of building` = **15000**
- `b: item 1 - sale of building, $140,000` = **Investing INFLOW (I, +$140,000); the $15,000 gain is not a cash flow**
- `b: item 2 - bonds paid at maturity, $80,000` = **Financing OUTFLOW (F, -$80,000)**
- `b: item 3 - interest paid in cash, $9,600` = **Operating OUTFLOW (O, -$9,600)**
- `b: item 5 - equipment purchased, $55,000` = **Investing OUTFLOW (I, -$55,000)**
- `b: item 7 - long-term bank note borrowed, $50,000` = **Financing INFLOW (F, +$50,000)**
- `b: item 8 - finance lease principal paid, $12,000` = **Financing OUTFLOW (F, -$12,000)**
- `b: item 10 - prior-year dividends paid, $7,500` = **Financing OUTFLOW (F, -$7,500)**
- `b: item 11 - collections from customers, $285,000` = **Operating INFLOW (O, +$285,000)**
- `b: item 11 - cash paid to suppliers and employees, $240,000` = **Operating OUTFLOW (O, -$240,000)**
- `b: item 11 - income taxes paid, $14,000` = **Operating OUTFLOW (O, -$14,000)**
- `b: item 12 - trading securities purchased, $16,000` = **Operating OUTFLOW (O, -$16,000); securities held for resale/trading are classified by the nature/purpose for which they are held, so they are operating, not investing**
- `b: item 4 - accrued interest, $2,400` = **NOT a cash flow on Dec 31 - no cash moved. Under the indirect method it appears only as a noncash add-back / increase in interest payable in the operating reconciliation; under the direct method it is simply excluded (only the $9,600 actually paid is shown).**
- `b: item 6 - land acquired by issuing a $90,000 note` = **NOT in any of the three sections - a noncash investing and financing transaction; disclosed in the supplemental noncash schedule (or notes) at $90,000**
- `b: item 9 - dividends declared, $10,000` = **NOT a financing cash outflow in 2027 - declaration only; no cash on Dec 31. It becomes a financing outflow when paid in January 2028; the dividends payable increase is a noncash item.**
- `c: ending cash total per SCF reconciliation (cash + equivalents + restricted cash)` = **84500**
- `c: short-term equity investments excluded from the SCF cash total` = **19000**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 2. `agent_119#00` — chapter 20 — machine_passed

**Machine verdict:** baseline `machine_passed`, trim `machine_passed`  
**Required parts detected:** a, b, c, d, e  
**Coverage:** baseline 0.8, trim 1.0

### Question

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

### The key's answer

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

### Blind solver (baseline) — figures

- `b: weighted-average common shares outstanding for 2025` = **167400**
- `c: income available to common stockholders` = **366000**
- `c: basic earnings per share` = **2.19**
- `d: basic EPS as presented on the 2025 income statement (single line, 'Earnings per common share')` = **2.19**

### Blind solver (trim) — figures

- `a: Apr 1 - cash received on common issuance` = **420000**
- `a: Apr 1 - credit to Common Stock at $2 par` = **60000**
- `a: Apr 1 - credit to Paid-in Capital in Excess of Par` = **360000**
- `a: Jul 1 - Treasury Stock debit at cost` = **96000**
- `a: Sep 30 - preferred cash dividend paid` = **12000**
- `a: Nov 1 - stock dividend shares distributed` = **28800**
- `a: Nov 1 - stock dividend recorded at par` = **57600**
- `b: retroactive stock-dividend restatement factor` = **1.2**
- `b: Jan 1 - Mar 31 - actual shares outstanding` = **120000**
- `b: Jan 1 - Mar 31 - restatement factor` = **1.2**
- `b: Jan 1 - Mar 31 - fraction of year (months/12)` = **3/12**
- `b: Jan 1 - Mar 31 - weighted restated shares` = **36000**
- `b: Apr 1 - Jun 30 - actual shares outstanding` = **150000**
- `b: Apr 1 - Jun 30 - restatement factor` = **1.2**
- `b: Apr 1 - Jun 30 - fraction of year (months/12)` = **3/12**
- `b: Apr 1 - Jun 30 - weighted restated shares` = **45000**
- `b: Jul 1 - Oct 31 - actual shares outstanding` = **144000**
- `b: Jul 1 - Oct 31 - restatement factor` = **1.2**
- `b: Jul 1 - Oct 31 - fraction of year (months/12)` = **4/12**
- `b: Jul 1 - Oct 31 - weighted restated shares` = **57600**
- `b: Nov 1 - Dec 31 - actual shares outstanding` = **172800**
- `b: Nov 1 - Dec 31 - restatement factor` = **1**
- `b: Nov 1 - Dec 31 - fraction of year (months/12)` = **2/12**
- `b: Nov 1 - Dec 31 - weighted restated shares` = **28800**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 3. `agent_254#00` — chapter 20 — machine_passed

**Machine verdict:** baseline `machine_passed`, trim `machine_passed`  
**Required parts detected:** a, b, c, d, e, f  
**Coverage:** baseline 1.0, trim 1.0

### Question

### Q1 — CORE — Multi-security ranking schedule, sequential diluted EPS, initial recognition & period-end JEs (emphasis: subsequent measurement schedule)
**LO:** LO 20-9  
**Concept:** Initial recognition of convertible securities; subsequent measurement ranking and sequential diluted EPS schedules; period-end preferred dividend and bond interest JEs; dual face presentation of basic and diluted EPS  
**Scenario:**  
**Meridian Cascade Holdings Inc.** is a calendar-year public company with a **complex capital structure**. For the year ended December 31, Year 1:

| Item | Amount |
|---|---:|
| Net income | $380,000 |
| Weighted-average common shares outstanding (entire year) | 200,000 |
| Income tax rate | 25% |

There are **no** discontinued operations. On **January 1, Year 1**, Meridian issued the following securities (all outstanding the entire year; none exercised or converted during Year 1). Common stock has a **$1 par** value.

1. **Employee stock options:** 10,000 options to purchase one common share each at an exercise price of **$20**. Average market price of common stock during Year 1: **$40**.
2. **5% cumulative convertible preferred stock:** 4,000 shares, **$100 par**, issued at par. Each preferred share is convertible into **3** common shares. Preferred dividends for the full year were declared and paid on December 31.
3. **Series X convertible bonds:** **$500,000** face, **4%** coupon, issued at par on January 1. Each **$1,000** bond is convertible into **25** common shares. Interest was paid in cash for the full year.
4. **Series Y convertible bonds:** **$300,000** face, **10%** coupon, issued at par on January 1. Each **$1,000** bond is convertible into **8** common shares. Interest was paid in cash for the full year.

**Required:**  
a. Prepare the **January 1, Year 1 initial recognition journal entries** for (1) the convertible preferred stock issuance and (2) the Series X convertible bond issuance. Show Dr = Cr.  
b. Compute the **numerator effect**, **denominator effect**, and **earnings per incremental share** for each potentially dilutive security. **Rank** the securities from most dilutive to least dilutive.  
c. Compute **basic EPS** for Year 1.  
d. Prepare the **sequential diluted EPS subsequent measurement schedule** (most dilutive → least dilutive). Identify which securities are dilutive vs antidilutive and state **diluted EPS**.  
e. Prepare the **December 31, Year 1 period-end journal entries** for (1) the annual preferred dividend (cash paid same day) and (2) full-year cash interest on Series X bonds. Show Dr = Cr.  
f. Show the **financial statement presentation** of basic and diluted EPS on the face of the income statement.

### The key's answer

**Answer key:**  

**a. January 1, Year 1 — initial recognition JEs**

**(1) Convertible preferred stock issued at par**

Cash proceeds = 4,000 × $100 = **$400,000**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 400,000 | |
| Convertible Preferred Stock ($100 par) | | 400,000 |
| *Issue 4,000 shares of 5% cumulative convertible preferred at par* | | |

**Check:** Dr = Cr = **400,000**. **Balanced.**

**(2) Series X convertible bonds issued at par**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 500,000 | |
| Bonds Payable—Series X (convertible) | | 500,000 |
| *Issue $500,000 of 4% convertible bonds at par* | | |

**Check:** Dr = Cr = **500,000**. **Balanced.**

**b. Incremental effects and ranking (setup for subsequent measurement)**

**Stock options (treasury stock method)**  
Proceeds if exercised = 10,000 × $20 = **$200,000**  
Shares assumed repurchased = $200,000 ÷ $40 = **5,000**  
Incremental shares = 10,000 − 5,000 = **5,000**  
Numerator effect = **$0**  
Earnings per incremental share = $0 ÷ 5,000 = **$0.00**

**Series X convertible bonds (if-converted)**  
Pretax interest = $500,000 × 4% = **$20,000**  
After-tax interest add-back = $20,000 × (1 − 0.25) = **$15,000**  
Conversion shares = 500 bonds × 25 = **12,500**  
Earnings per incremental share = $15,000 ÷ 12,500 = **$1.20**

**Convertible preferred (if-converted)**  
Preferred dividends add-back = 4,000 × $100 × 5% = **$20,000**  
Conversion shares = 4,000 × 3 = **12,000**  
Earnings per incremental share = $20,000 ÷ 12,000 = **$1.67** (exactly $1.666…; rank uses $1.67)

**Series Y convertible bonds (if-converted)**  
Pretax interest = $300,000 × 10% = **$30,000**  
After-tax interest add-back = $30,000 × 0.75 = **$22,500**  
Conversion shares = 300 bonds × 8 = **2,400**  
Earnings per incremental share = $22,500 ÷ 2,400 = **$9.375**

**Ranking (most dilutive → least dilutive)**

| Rank | Security | Δ Income | Δ Shares | Earnings per incremental share |
|---:|---|---:|---:|---:|
| 1 | Stock options | $0 | 5,000 | **$0.00** |
| 2 | Series X convertible bonds | 15,000 | 12,500 | **1.20** |
| 3 | Convertible preferred stock | 20,000 | 12,000 | **1.67** |
| 4 | Series Y convertible bonds | 22,500 | 2,400 | **9.375** |

**c. Basic EPS**

Income available to common = $380,000 − $20,000 = **$360,000**

\[
\text{Basic EPS} = \frac{\$360{,}000}{200{,}000} = \mathbf{\$1.80}
\]

**d. Sequential diluted EPS subsequent measurement schedule (emphasis)**

| Step | Net income available to common | Weighted-average shares | Per share | Assessment |
|---|---:|---:|---:|---|
| Basic EPS | $360,000 | 200,000 | **$1.80** | — |
| + Stock options | 360,000 | 205,000 | **1.76** | Dilutive ($1.7561 < $1.80) |
| + Series X bonds | 375,000 | 217,500 | **1.72** | Dilutive ($1.7241 < $1.7561) |
| + Convertible preferred | 395,000 | 229,500 | **1.72** | Dilutive ($1.7211 < $1.7241) |
| + Series Y bonds | 417,500 | 231,900 | **1.80** | **Antidilutive** ($1.8003 > $1.7211) |

Detail:
- Options: $360,000 / 205,000 = **$1.7561** → dilutive  
- Series X: ($360,000 + $15,000) / (205,000 + 12,500) = $375,000 / 217,500 = **$1.7241** → dilutive  
- Preferred: ($375,000 + $20,000) / (217,500 + 12,000) = $395,000 / 229,500 = **$1.7211** → dilutive  
- Series Y: ($395,000 + $22,500) / (229,500 + 2,400) = $417,500 / 231,900 = **$1.8003** → **antidilutive** (exclude)

**Diluted EPS** uses income **$395,000** and shares **229,500**:

\[
\text{Diluted EPS} = \frac{\$395{,}000}{229{,}500} = \mathbf{\$1.72}
\]

Series Y is **excluded** from diluted EPS (disclose as potentially dilutive / antidilutive for the period).

**e. December 31, Year 1 — period-end adjusting / cash settlement JEs**

**(1) Annual preferred dividend**

| Account | Debit | Credit |
|---|---:|---:|
| Preferred Dividends (or Retained Earnings) | 20,000 | |
| Cash | | 20,000 |
| *Declare and pay annual 5% cumulative convertible preferred dividend* | | |

**Check:** Dr = Cr = **20,000**. **Balanced.**

**(2) Full-year cash interest on Series X bonds**

Interest = $500,000 × 4% = **$20,000**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 20,000 | |
| Cash | | 20,000 |
| *Pay annual interest on Series X 4% convertible bonds* | | |

**Check:** Dr = Cr = **20,000**. **Balanced.**

*Note:* EPS is a **presentation** measure derived from net income and share counts; there is no journal entry that “books” EPS itself. Preferred dividends reduce income available to common for **basic** EPS; bond interest is already in net income and is added back **net of tax** only in the diluted EPS computation when the bonds are dilutive.

**f. Income statement presentation (face)**

| | |
|---|---:|
| Basic earnings per share | **$1.80** |
| Diluted earnings per share | **1.72** |

(Complex capital structure → dual presentation with **equal prominence**.)

**Key insight:** Maximum dilution requires ranking by **lowest earnings per incremental share** first, then building a **subsequent measurement schedule** that adds securities **only while** tentative EPS continues to fall. A high-coupon, low-conversion Series Y bond can be **antidilutive after** more dilutive securities are already in the schedule—even if a student might assume every convertible is always included.

---

### Blind solver (baseline) — figures

- `b: Employee stock options - numerator effect` = **0**
- `b: Employee stock options - denominator effect (incremental shares)` = **5000**
- `b: Employee stock options - earnings per incremental share` = **0**
- `b: Employee stock options - rank (1 = most dilutive)` = **1**
- `b: Series X convertible bonds (4%) - numerator effect` = **15000**
- `b: Series X convertible bonds (4%) - denominator effect (incremental shares)` = **12500**
- `b: Series X convertible bonds (4%) - earnings per incremental share` = **1.2**
- `b: Series X convertible bonds (4%) - rank (1 = most dilutive)` = **2**
- `b: 5% cumulative convertible preferred stock - numerator effect` = **20000**
- `b: 5% cumulative convertible preferred stock - denominator effect (incremental shares)` = **12000**
- `b: 5% cumulative convertible preferred stock - earnings per incremental share` = **1.6667**
- `b: 5% cumulative convertible preferred stock - rank (1 = most dilutive)` = **3**
- `b: Series Y convertible bonds (10%) - numerator effect` = **22500**
- `b: Series Y convertible bonds (10%) - denominator effect (incremental shares)` = **2400**
- `b: Series Y convertible bonds (10%) - earnings per incremental share` = **9.375**
- `b: Series Y convertible bonds (10%) - rank (1 = most dilutive)` = **4**
- `c: basic EPS` = **1.8**
- `d: diluted EPS` = **1.72**
- `f: face of income statement - basic EPS` = **1.8**
- `f: face of income statement - diluted EPS` = **1.72**

### Blind solver (trim) — figures

- `a: Cash received on preferred stock issuance (4,000 sh x $100 par, at par)` = **400000.0**
- `a: Preferred Stock credited (par)` = **400000.0**
- `a: Cash received on Series X convertible bond issuance (at par)` = **500000.0**
- `a: Bonds Payable - Series X credited (face)` = **500000.0**
- `b: Options - assumed proceeds (10,000 x $20)` = **200000.0**
- `b: Options - treasury shares assumed repurchased ($200,000 / $40)` = **5000.0**
- `b: Options - numerator effect` = **0.0**
- `b: Options - denominator effect (incremental shares)` = **5000.0**
- `b: Options - earnings per incremental share` = **0.0**
- `b: Series X bonds - annual cash interest ($500,000 x 4%)` = **20000.0**
- `b: Series X bonds - numerator effect (interest net of 25% tax)` = **15000.0**
- `b: Series X bonds - denominator effect (500 bonds x 25 shares)` = **12500.0**
- `b: Series X bonds - earnings per incremental share` = **1.2**
- `b: Convertible preferred - numerator effect (dividends added back, no tax effect)` = **20000.0**
- `b: Convertible preferred - denominator effect (4,000 sh x 3)` = **12000.0**
- `b: Convertible preferred - earnings per incremental share` = **1.6667**
- `b: Series Y bonds - annual cash interest ($300,000 x 10%)` = **30000.0**
- `b: Series Y bonds - numerator effect (interest net of 25% tax)` = **22500.0**
- `b: Series Y bonds - denominator effect (300 bonds x 8 shares)` = **2400.0**
- `b: Series Y bonds - earnings per incremental share` = **9.375**
- `b: Rank 1 (most dilutive to least dilutive) - Employee stock options, earnings per incremental share` = **0.0**
- `b: Rank 2 (most dilutive to least dilutive) - Series X convertible bonds (4%), earnings per incremental share` = **1.2**
- `b: Rank 3 (most dilutive to least dilutive) - 5% cumulative convertible preferred stock, earnings per incremental share` = **1.6667**
- `b: Rank 4 (most dilutive to least dilutive) - Series Y convertible bonds (10%), earnings per incremental share` = **9.375**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 4. `agent_381#02` — chapter 20 — machine_passed

**Machine verdict:** baseline `machine_passed`, trim `machine_passed`  
**Required parts detected:** a, b, c, d, e, f  
**Coverage:** baseline 1.0, trim 1.0

### Question

### Q3 — CORE alternate angle — 100% stock dividend retroactive restatement; issuance; buyback; noncumulative preferred
**LO:** LO 20-5  
**Concept:** Weighted-average shares with **retroactive restatement** for a large stock dividend; mid-year issuance and buyback JEs; large stock dividend capitalization JE; noncumulative preferred dividends (subtract only when declared); basic EPS schedule  
**Scenario:**  
**Lakeshore Fiber Optics Ltd.** is a calendar-year public company. No convertibles, options, or warrants. No noncontrolling interest.

**Beginning of Year 1 (already outstanding):**
- **50,000** shares of **$1 par** common stock
- **5,000** shares of **6%, $100 par noncumulative** preferred stock (outstanding all year)

**Year 1 equity transactions:**
| Date | Event |
|---|---|
| **April 1** | Issues **10,000** shares of $1 par common for **$20** cash per share |
| **July 1** | Purchases **5,000** common shares for the **treasury** at **$22** cash per share (cost method) |
| **October 1** | Distributes a **100% common stock dividend** (one new share for each share then outstanding). Fair value is irrelevant for this large stock dividend; capitalize **par** of shares issued. Market price on October 1 is $24 (given for context only). |
| **December 10** | Declares and immediately pays **$30,000** cash dividends on the **noncumulative** preferred stock (the full stated annual amount). No common cash dividend is declared. |

**Finalized Year 1 net income** (after all income-statement items, including tax) is **$360,000**. (Treat NI as given—no separate income AJs required in this item.)

**Required:**  
a. Prepare the **April 1** common stock **issuance** journal entry.  
b. Prepare the **July 1** treasury stock **purchase** journal entry.  
c. Prepare the **October 1 large stock dividend** journal entry (par capitalization). State shares outstanding immediately before and after the dividend.  
d. Prepare the **December 10** preferred dividend **declaration and payment** (may be combined or shown as two entries).  
e. Prepare the **weighted-average common shares schedule** applying the **retroactive restatement factor** for the 100% stock dividend to all periods **before** October 1.  
f. Prepare the **basic EPS computation schedule**. Explain in one sentence why the noncumulative preferred dividend is subtracted and how stock-dividend treatment differs from the April cash issuance.

### The key's answer

**Answer key:**

**a. April 1 — common stock issuance**

Cash = 10,000 × $20 = **$200,000**  
Par = 10,000 × $1 = **$10,000**  
APIC = **$190,000**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 200,000 | |
| Common Stock ($1 par) | | 10,000 |
| Additional Paid-in Capital—Common | | 190,000 |
| *Issue 10,000 shares of $1 par common at $20* | | |

**Check:** Dr = **200,000**; Cr = 10,000 + 190,000 = **200,000**. **Balanced.**

Shares outstanding after issuance = 50,000 + 10,000 = **60,000**.

**b. July 1 — treasury stock purchase**

Cost = 5,000 × $22 = **$110,000**

| Account | Debit | Credit |
|---|---:|---:|
| Treasury Stock | 110,000 | |
| Cash | | 110,000 |
| *Purchase 5,000 common shares for treasury at $22* | | |

**Check:** Dr = Cr = **110,000**. **Balanced.**

Shares outstanding after buyback = 60,000 − 5,000 = **55,000**.

**c. October 1 — 100% large stock dividend**

Shares outstanding immediately **before** dividend = **55,000**  
New shares issued = 55,000 × 100% = **55,000**  
Shares outstanding **after** dividend = 55,000 + 55,000 = **110,000**  
Par capitalization = 55,000 × $1 = **$55,000**

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings | 55,000 | |
| Common Stock ($1 par) | | 55,000 |
| *Distribute 100% large stock dividend (capitalize par of 55,000 new shares)* | | |

**Check:** Dr = Cr = **55,000**. **Balanced.**

Retroactive restatement factor for periods before October 1 = **2.0** (100% stock dividend ≡ doubling shares).

**d. December 10 — noncumulative preferred cash dividend (declaration and settlement)**

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings (or Preferred Dividends Declared) | 30,000 | |
| Cash | | 30,000 |
| *Declare and pay $30,000 cash dividend on noncumulative preferred* | | |

**Check:** Dr = Cr = **30,000**. **Balanced.**

*(If recorded in two steps: Dr RE 30,000 / Cr Dividends Payable 30,000; then Dr Dividends Payable 30,000 / Cr Cash 30,000. Each balances.)*

**e. Weighted-average common shares schedule (with retroactive restatement)**

| Inclusive dates | Actual shares outstanding | Retroactive factor | Equivalent shares | Months | Fraction | Weighted shares |
|---|---:|---:|---:|---:|---:|---:|
| Jan. 1 – Mar. 31 | 50,000 | 2.0 | 100,000 | 3 | 3/12 | 25,000 |
| Apr. 1 – June 30 | 60,000 | 2.0 | 120,000 | 3 | 3/12 | 30,000 |
| July 1 – Sept. 30 | 55,000 | 2.0 | 110,000 | 3 | 3/12 | 27,500 |
| Oct. 1 – Dec. 31 | 110,000 | — | 110,000 | 3 | 3/12 | 27,500 |
| **Totals** | | | | **12** | **100%** | **110,000** |

**Weighted-average common shares outstanding = 110,000**

*Checks:*  
50,000 × 2.0 × 3/12 = 25,000; 60,000 × 2.0 × 3/12 = 30,000;  
55,000 × 2.0 × 3/12 = 27,500; 110,000 × 3/12 = 27,500;  
25,000 + 30,000 + 27,500 + 27,500 = **110,000**.

**f. Basic EPS computation schedule**

Noncumulative preferred: subtract only the **$30,000 declared** (if none had been declared, **no** preferred subtraction).  
Net income available to common = $360,000 − $30,000 = **$330,000**

| Component | Amount |
|---|---:|
| Net income | $360,000 |
| Less: Preferred dividends declared (noncumulative) | (30,000) |
| **Net income available to common stockholders** | **$330,000** |
| Weighted-average common shares outstanding | 110,000 |
| **Basic EPS** | **$3.00** |

\[
\text{Basic EPS} = \frac{\$360{,}000 - \$30{,}000}{110{,}000} = \frac{\$330{,}000}{110{,}000} = \mathbf{\$3.00}
\]

*Check:* \(110{,}000 \times \$3.00 = \$330{,}000\).

**Why preferred is subtracted / how stock dividend differs from cash issuance:**  
Noncumulative preferred reduces the numerator only for dividends **declared** this period ($30,000). The **100% stock dividend** does not bring in capital and is treated as if it occurred at the **beginning of the year** (factor 2.0 applied to all pre-dividend share counts), whereas the **April cash issuance** is weighted only from April 1 (then restated by the stock-dividend factor for pre-October periods).

**Key insight:** Stock dividends and stock splits change the **unit of ownership**, not the capital available for the year; GAAP therefore **restates** all pre-change periods. Cash issuances and buybacks are weighted only for the **time outstanding**. Noncumulative preferred affects EPS only when dividends are **declared**; cumulative preferred always claims one year in the numerator.

---

### Blind solver (baseline) — figures

- `c: common shares outstanding immediately BEFORE the 100% stock dividend` = **55000**
- `c: common shares outstanding immediately AFTER the 100% stock dividend` = **110000**
- `e: weighted-average common shares outstanding for Year 1` = **110000**
- `f: net income available to common stockholders` = **330000**
- `f: basic earnings per share` = **3**

### Blind solver (trim) — figures

- `a: April 1 issuance - Cash debit` = **200000.0**
- `a: April 1 issuance - Common Stock credit (par)` = **10000.0**
- `a: April 1 issuance - Paid-in Capital in Excess of Par credit` = **190000.0**
- `b: July 1 treasury stock cost (5,000 x $22)` = **110000.0**
- `c: Common shares outstanding immediately BEFORE the stock dividend` = **55000.0**
- `c: Shares issued in the 100% stock dividend` = **55000.0**
- `c: Amount capitalized (par of shares issued)` = **55000.0**
- `c: Common shares outstanding immediately AFTER the stock dividend` = **110000.0**
- `d: Preferred cash dividend declared and paid (5,000 x $100 x 6%)` = **30000.0**
- `e: Retroactive restatement factor for periods before Oct 1` = **2.0**
- `e: Jan 1 - Mar 31 (3 months) - actual shares outstanding` = **50000.0**
- `e: Jan 1 - Mar 31 (3 months) - restatement factor` = **2.0**
- `e: Jan 1 - Mar 31 (3 months) - restated shares` = **100000.0**
- `e: Jan 1 - Mar 31 (3 months) - weighted portion (x 3/12)` = **25000.0**
- `e: Apr 1 - Jun 30 (3 months) - actual shares outstanding` = **60000.0**
- `e: Apr 1 - Jun 30 (3 months) - restatement factor` = **2.0**
- `e: Apr 1 - Jun 30 (3 months) - restated shares` = **120000.0**
- `e: Apr 1 - Jun 30 (3 months) - weighted portion (x 3/12)` = **30000.0**
- `e: Jul 1 - Sep 30 (3 months) - actual shares outstanding` = **55000.0**
- `e: Jul 1 - Sep 30 (3 months) - restatement factor` = **2.0**
- `e: Jul 1 - Sep 30 (3 months) - restated shares` = **110000.0**
- `e: Jul 1 - Sep 30 (3 months) - weighted portion (x 3/12)` = **27500.0**
- `e: Oct 1 - Dec 31 (3 months) - actual shares outstanding` = **110000.0**
- `e: Oct 1 - Dec 31 (3 months) - restatement factor` = **1.0**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 5. `agent_229#00` — chapter 15 — machine_passed

**Machine verdict:** baseline `machine_passed`, trim `machine_passed`  
**Required parts detected:** a, b, c, d, e, f, g  
**Coverage:** baseline 0.857, trim 1.0

### Question

### Q1 — CORE — Multi-year assurance warranty: sale, accruals, claims, liability schedule (emphasis)
**LO:** LO 15-5  
**Concept:** Assurance-type warranty loss contingency — initial recognition of sales and estimated liability; subsequent measurement schedule (warranty liability rollforward); period-end adjusting accruals; settlement of claims against the liability  
**Scenario:**  
**Cedarline Outdoor Gear** (calendar-year company) sells camping equipment that includes a **two-year assurance-type warranty** (not sold separately; protects against manufacturing defects). Management estimates warranty costs at **1.5% of sales** based on historical experience. Actual warranty costs are paid in cash when claims are processed. Ignore cost of goods sold.

| Year | Product sales (cash) | Actual warranty claims paid |
|---:|---:|---:|
| 1 | $2,400,000 | $12,000 |
| 2 | 2,800,000 | 48,000 |
| 3 | 3,000,000 | 55,000 |

Warranty estimates remain 1.5% of that year’s sales each year. No service-type (extended) warranties are sold.

**Required:**  
a. Record the **Year 1** journal entry for **product sales** (initial revenue recognition).  
b. Record the **December 31, Year 1 period-end adjusting entry** to accrue estimated warranty cost.  
c. Record the **Year 1** entry to **settle / pay** actual warranty claims.  
d. Prepare a complete **subsequent measurement schedule** for the **warranty liability** for Years 1–3 showing beginning balance, accruals, claims, and ending balance (**emphasis**).  
e. Record the **December 31, Year 2** period-end adjusting entry for the Year 2 warranty accrual.  
f. Record the **Year 3** entry to pay Year 3 warranty claims (using the liability first).  
g. In one or two sentences, explain why an assurance-type warranty is treated as a **loss contingency** rather than deferred revenue.

### The key's answer

**Answer key:**  

**a. Initial recognition — Year 1 sales**

*Year 1 — Product sales (assurance warranty included in price)*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 2,400,000 | |
| Sales Revenue | | 2,400,000 |
| *Record product sales; assurance warranty not separately priced* | | |

**Check:** Dr 2,400,000 = Cr 2,400,000. **Balanced.**

**b. Period-end adjusting JE — Year 1 warranty accrual**

Estimated warranty cost = \(\$2{,}400{,}000 \times 0.015 = \$36{,}000\).

*December 31, Year 1 — Accrue assurance-type warranty*

| Account | Debit | Credit |
|---|---:|---:|
| Warranty Expense | 36,000 | |
| Warranty Liability | | 36,000 |
| *Accrue probable and reasonably estimable warranty loss contingency* | | |

**Check:** Dr 36,000 = Cr 36,000. **Balanced.**

**c. Settlement of Year 1 claims**

*Year 1 — Pay warranty claims*

| Account | Debit | Credit |
|---|---:|---:|
| Warranty Liability | 12,000 | |
| Cash | | 12,000 |
| *Settle claims against estimated warranty liability* | | |

**Check:** Dr 12,000 = Cr 12,000. **Balanced.**

**d. Subsequent measurement schedule (emphasis) — Warranty liability rollforward**

| Year | Beginning liability | + Accrual (1.5% × sales) | − Claims paid | Ending liability |
|---:|---:|---:|---:|---:|
| 1 | 0 | 36,000 | 12,000 | **24,000** |
| 2 | 24,000 | 42,000 | 48,000 | **18,000** |
| 3 | 18,000 | 45,000 | 55,000 | **8,000** |
| **Totals** | | **123,000** | **115,000** | |

**Computations:**  
- Y2 accrual = \(\$2{,}800{,}000 \times 0.015 = \$42{,}000\)  
- Y3 accrual = \(\$3{,}000{,}000 \times 0.015 = \$45{,}000\)  
- Y2 end: \(24{,}000 + 42{,}000 - 48{,}000 = 18{,}000\)  
- Y3 end: \(18{,}000 + 45{,}000 - 55{,}000 = 8{,}000\)  

**Roll-forward check:** Total accruals − total claims = ending liability when beg = 0: \(123{,}000 - 115{,}000 = \$8{,}000\). **OK.**

**e. Period-end adjusting JE — Year 2**

*December 31, Year 2 — Accrue warranty*

| Account | Debit | Credit |
|---|---:|---:|
| Warranty Expense | 42,000 | |
| Warranty Liability | | 42,000 |

**Check:** Dr 42,000 = Cr 42,000. **Balanced.**

**f. Settlement of Year 3 claims**

*Year 3 — Pay warranty claims \( \$55{,}000 \)*  
Beginning Y3 liability after Y3 accrual = \(18{,}000 + 45{,}000 = 63{,}000\) (claims still reduce the liability; accrual timing within the year does not change the net YE schedule). Claims of $55,000 do not exceed the liability available under the year-end rollforward model used in (d); record full reduction of liability:

| Account | Debit | Credit |
|---|---:|---:|
| Warranty Liability | 55,000 | |
| Cash | | 55,000 |

**Check:** Dr 55,000 = Cr 55,000. **Balanced.**  
(If claims were recorded before the Y3 accrual and temporarily exceeded the unadjusted liability, any excess would be charged to Warranty Expense as a change in estimate; the year-end schedule in (d) still holds.)

**g. Why assurance-type is a loss contingency**  
An assurance-type warranty relates to **existing but unidentified defects** in products already sold; the obligation is estimated and **accrued as expense** in the period of sale when the loss is probable and reasonably estimable. It is **not** a separate performance obligation, so cash is not deferred as unearned warranty revenue.

**Key insight:** The **warranty liability subsequent measurement schedule** is the core control: every period’s accrual increases the liability; claims reduce it; the ending balance must equal beginning + accruals − claims. Assurance warranties load estimated cost into **expense of the sale year**, even when cash repairs occur later.

---

### Blind solver (baseline) — figures

- `d: Year 1 warranty liability beginning balance` = **0**
- `d: Year 1 warranty accrual (1.5% of sales)` = **36000**
- `d: Year 1 actual claims paid (charged to liability)` = **12000**
- `d: Year 1 warranty liability ending balance` = **24000**
- `d: Year 2 warranty liability beginning balance` = **24000**
- `d: Year 2 warranty accrual (1.5% of sales)` = **42000**
- `d: Year 2 actual claims paid (charged to liability)` = **48000**
- `d: Year 2 warranty liability ending balance` = **18000**
- `d: Year 3 warranty liability beginning balance` = **18000**
- `d: Year 3 warranty accrual (1.5% of sales)` = **45000**
- `d: Year 3 actual claims paid (charged to liability)` = **55000**
- `d: Year 3 warranty liability ending balance` = **8000**

### Blind solver (trim) — figures

- `a: Year 1 product sales - Cash debited (= Sales revenue credited)` = **2400000**
- `b: Dec 31, Year 1 adjusting accrual - Warranty expense (1.5% x Year 1 sales)` = **36000**
- `c: Year 1 warranty claims paid - Warranty liability debited / Cash credited` = **12000**
- `d: Year 1 warranty liability - beginning balance` = **0**
- `d: Year 1 warranty liability - add accrual (1.5% of sales)` = **36000**
- `d: Year 1 warranty liability - less actual claims paid` = **12000**
- `d: Year 1 warranty liability - ending balance` = **24000**
- `d: Year 2 warranty liability - beginning balance` = **24000**
- `d: Year 2 warranty liability - add accrual (1.5% of sales)` = **42000**
- `d: Year 2 warranty liability - less actual claims paid` = **48000**
- `d: Year 2 warranty liability - ending balance` = **18000**
- `d: Year 3 warranty liability - beginning balance` = **18000**
- `d: Year 3 warranty liability - add accrual (1.5% of sales)` = **45000**
- `d: Year 3 warranty liability - less actual claims paid` = **55000**
- `d: Year 3 warranty liability - ending balance` = **8000**
- `e: Dec 31, Year 2 adjusting accrual - Warranty expense (1.5% x Year 2 sales)` = **42000**
- `f: Year 3 warranty claims paid - Warranty liability debited / Cash credited` = **55000**
- `g: Assurance-type warranty is a loss contingency, not deferred revenue` = **It is not a separate performance obligation - it is not sold separately and simply guarantees the product already delivered meets agreed specifications, so no transaction price is allocated to it and no revenue is deferred. Instead it is a probable, reasonably estimable future sacrifice arising from the past sale, so the full estimated cost is expensed and accrued as a liability in the year of sale (matching), and later claims are charged against that liability.**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 6. `agent_392#00` — chapter 22 — machine_passed

**Machine verdict:** baseline `machine_passed`, trim `machine_passed`  
**Required parts detected:** a, b, c, d, e, f  
**Coverage:** baseline 0.833, trim 0.833

### Question

### Q1 — CORE — Full cash T-account method with period-end depreciation AJE emphasis
**LO:** LO 22-8  
**Concept:** Reconstruct entries from comparative BS and IS; subsequent measurement schedules; period-end depreciation AJE (noncash emphasis); complete cash T-account; direct-method SCF  
**Scenario:**  
**Northpine Logistics Corp.** (calendar year-end) provides the following comparative balance sheets, income statement, and additional information for the current year.

**Comparative Balance Sheets — December 31**

| Account | Prior Year | Current Year |
|---|---:|---:|
| Cash and cash equivalents | $140,000 | $95,000 |
| Restricted cash | 30,000 | 45,000 |
| Accounts receivable, net | 400,000 | 310,000 |
| Inventory | 180,000 | 280,000 |
| Equipment | 2,800,000 | 3,500,000 |
| Accumulated depreciation—equipment | (350,000) | (620,000) |
| **Total assets** | **$3,200,000** | **$3,610,000** |
| Accounts payable | $220,000 | $185,000 |
| Salaries payable | 60,000 | 35,000 |
| Bonds payable | 800,000 | 950,000 |
| Common stock, no-par | 1,600,000 | 1,750,000 |
| Retained earnings | 520,000 | 690,000 |
| **Total liabilities and equity** | **$3,200,000** | **$3,610,000** |

**Income Statement — Year Ended December 31, Current Year**

| | Amount |
|---|---:|
| Sales revenue | $4,200,000 |
| Cost of goods sold | (2,400,000) |
| Salary expense | (210,000) |
| Interest expense | (84,000) |
| Depreciation expense | (340,000) |
| Loss on sale of equipment | (90,000) |
| **Net income** | **$1,076,000** |

**Additional information (current year):**
1. Equipment with **original cost $550,000** and **accumulated depreciation $70,000** was sold for **$390,000 cash**.
2. All equipment purchases were for **cash**.
3. All dividends declared were **paid in cash** during the year.
4. Bonds and common stock changes were **cash** transactions.
5. No accrued interest payable at either year-end (interest expense equals cash interest paid).
6. Depreciation is recorded only as a **December 31 period-end adjusting entry**.

**Required:**  
a. Prepare a **schedule of account changes** and compute the change in **cash + cash equivalents + restricted cash**.  
b. Prepare **subsequent measurement schedules** for: (1) accounts receivable (solve collections), (2) inventory and accounts payable (solve payments to suppliers), (3) salaries payable (solve payments to employees), (4) equipment, (5) accumulated depreciation, and (6) retained earnings (solve dividends).  
c. Reconstruct the **journal entries** (labeled a–j, Demo 22-8 style) that explain all income statement accounts and balance sheet changes. Every cash-impacting entry must balance. **Highlight** the period-end depreciation adjusting entry.  
d. Complete the **cash T-account** (operating / investing / financing) and prove it to the change in cash + restricted cash. Explicitly state which reconstructed entry **does not** post to the cash T-account and why.  
e. Prepare the **statement of cash flows** using the **direct method** for operating activities.  
f. **Classification:** Why is the $90,000 loss **not** a separate cash outflow on the SCF prepared from the cash T-account? Where does the equipment disposal appear?

### The key's answer

**Answer key:**  

**a. Account changes and cash change**

| Account | Prior | Current | Change |
|---|---:|---:|---:|
| Cash and cash equivalents | 140,000 | 95,000 | ↓ 45,000 |
| Restricted cash | 30,000 | 45,000 | ↑ 15,000 |
| Accounts receivable, net | 400,000 | 310,000 | ↓ 90,000 |
| Inventory | 180,000 | 280,000 | ↑ 100,000 |
| Equipment | 2,800,000 | 3,500,000 | ↑ 700,000 |
| Accumulated depreciation (credit bal.) | 350,000 | 620,000 | ↑ 270,000 |
| Accounts payable | 220,000 | 185,000 | ↓ 35,000 |
| Salaries payable | 60,000 | 35,000 | ↓ 25,000 |
| Bonds payable | 800,000 | 950,000 | ↑ 150,000 |
| Common stock | 1,600,000 | 1,750,000 | ↑ 150,000 |
| Retained earnings | 520,000 | 690,000 | ↑ 170,000 |

Cash + cash equivalents + restricted cash:  
Beginning \(140{,}000 + 30{,}000 = \mathbf{\$170{,}000}\)  
Ending \(95{,}000 + 45{,}000 = \mathbf{\$140{,}000}\)  
**Net decrease = $30,000** (target for cash T-account).

**b. Subsequent measurement schedules**

**(1) Accounts receivable — collections**

| | Amount |
|---|---:|
| Beginning AR, net | $400,000 |
| Sales revenue | 4,200,000 |
| Cash collections (plug) | (4,290,000) |
| **Ending AR, net** | **$310,000** |

Check: collections \(= \) sales \(+ \) AR decrease \(= 4{,}200{,}000 + 90{,}000 = \mathbf{\$4{,}290{,}000}\).

**(2) Inventory / AP — payments to suppliers**

| Inventory | Amount |
|---|---:|
| Beginning inventory | $180,000 |
| Purchases (plug) | 2,500,000 |
| COGS | (2,400,000) |
| **Ending inventory** | **$280,000** |

Purchases \(= \) COGS \(+ \) inventory increase \(= 2{,}400{,}000 + 100{,}000 = \mathbf{\$2{,}500{,}000}\).

| Accounts payable | Amount |
|---|---:|
| Beginning AP | $220,000 |
| Purchases | 2,500,000 |
| Cash to suppliers (plug) | (2,535,000) |
| **Ending AP** | **$185,000** |

Cash to suppliers \(= \) purchases \(+ \) AP decrease \(= 2{,}500{,}000 + 35{,}000 = \mathbf{\$2{,}535{,}000}\).

**(3) Salaries payable — payments to employees**

| | Amount |
|---|---:|
| Beginning salaries payable | $60,000 |
| Salary expense | 210,000 |
| Cash to employees (plug) | (235,000) |
| **Ending salaries payable** | **$35,000** |

Cash paid \(= \) expense \(+ \) payable decrease \(= 210{,}000 + 25{,}000 = \mathbf{\$235{,}000}\).

**(4) Equipment**

| | Amount |
|---|---:|
| Beginning balance | $2,800,000 |
| Cash purchases (plug) | 1,250,000 |
| Cost of equipment sold | (550,000) |
| **Ending balance** | **$3,500,000** |

Purchases \(= \) ending \(-\) beginning \(+ \) cost sold \(= 3{,}500{,}000 - 2{,}800{,}000 + 550{,}000 = \mathbf{\$1{,}250{,}000}\).

**(5) Accumulated depreciation (period-end AJE rollforward)**

| | Amount |
|---|---:|
| Beginning balance | $350,000 |
| Depreciation expense (**period-end AJE**) | 340,000 |
| AD removed on sale | (70,000) |
| **Ending balance** | **$620,000** |

Check: \(350{,}000 + 340{,}000 - 70{,}000 = 620{,}000\) ✓.

**(6) Retained earnings — dividends**

| | Amount |
|---|---:|
| Beginning balance | $520,000 |
| Net income | 1,076,000 |
| Cash dividends (plug) | (906,000) |
| **Ending balance** | **$690,000** |

Dividends \(= 520{,}000 + 1{,}076{,}000 - 690{,}000 = \mathbf{\$906{,}000}\).

**c. Reconstructed journal entries**

*(a) Collections from customers* — **initial recognition of sales cash cycle**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 4,290,000 | |
| Accounts Receivable | | 90,000 |
| Sales Revenue | | 4,200,000 |

**Check:** Dr 4,290,000 = Cr 90,000 + 4,200,000. **Balanced.**

*(b) Cost of goods sold / inventory / AP — payments to suppliers*

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 2,400,000 | |
| Inventory | 100,000 | |
| Accounts Payable | 35,000 | |
| Cash | | 2,535,000 |

**Check:** Dr 2,400,000 + 100,000 + 35,000 = Cr 2,535,000. **Balanced.**

*(c) Salary expense / salaries payable — payments to employees*

| Account | Debit | Credit |
|---|---:|---:|
| Salary Expense | 210,000 | |
| Salaries Payable | 25,000 | |
| Cash | | 235,000 |

**Check:** Dr 210,000 + 25,000 = Cr 235,000. **Balanced.**

*(d) Interest paid*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 84,000 | |
| Cash | | 84,000 |

**Check:** Dr = Cr = 84,000. **Balanced.**

*(e) Disposal (sale) of equipment*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 390,000 | |
| Accumulated Depreciation—Equipment | 70,000 | |
| Loss on Sale of Equipment | 90,000 | |
| Equipment | | 550,000 |

**Check:** Dr 390,000 + 70,000 + 90,000 = Cr 550,000. **Balanced.**  
Book value \(= 550{,}000 - 70{,}000 = 480{,}000\); proceeds \(390{,}000\) → loss \(90{,}000\).

*(f) Purchase of equipment (cash) — initial recognition of PPE*

| Account | Debit | Credit |
|---|---:|---:|
| Equipment | 1,250,000 | |
| Cash | | 1,250,000 |

**Check:** Dr = Cr = 1,250,000. **Balanced.**

*(g) Issuance of bonds (cash)*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 150,000 | |
| Bonds Payable | | 150,000 |

**Check:** Dr = Cr = 150,000. **Balanced.**

*(h) Issuance of common stock (cash)*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 150,000 | |
| Common Stock | | 150,000 |

**Check:** Dr = Cr = 150,000. **Balanced.**

*(i) Cash dividends*

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings | 906,000 | |
| Cash | | 906,000 |

**Check:** Dr = Cr = 906,000. **Balanced.**

*(j) Period-end adjusting JE — depreciation (EMPHASIS; noncash)*

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 340,000 | |
| Accumulated Depreciation—Equipment | | 340,000 |

**Check:** Dr = Cr = 340,000. **Balanced.**  
**Does not post to the cash T-account.** This period-end AJE only updates the **accumulated depreciation** subsequent measurement schedule (part b.5). It is **not** an operating cash outflow under the direct/T-account approach.

**d. Cash T-account** (cash + cash equivalents + restricted cash)

| Debit (inflows) | | Credit (outflows) | |
|---|---:|---|---:|
| **Operating activities** | | **Operating activities** | |
| (a) From custo

### Blind solver (baseline) — figures

- `a: change in cash + cash equivalents + restricted cash (decrease; $170,000 -> $140,000)` = **-30000**
- `b(1): cash collected from customers` = **4290000**
- `b(2): cash paid to suppliers` = **2535000**
- `b(3): cash paid to employees` = **235000**
- `b(4): equipment acquired for cash` = **1250000**
- `b(5): accumulated depreciation—equipment, ending balance (350,000 + 340,000 - 70,000)` = **620000**
- `b(6): dividends declared and paid` = **906000**
- `d/e: net cash provided by operating activities (direct method)` = **1436000**
- `d/e: net cash used in investing activities` = **-860000**
- `d/e: net cash used in financing activities` = **-606000**
- `d/e: net decrease in cash, cash equivalents, and restricted cash` = **-30000**
- `e: cash paid for interest` = **84000**
- `e: proceeds from sale of equipment (investing inflow)` = **390000**
- `e: proceeds from issuing bonds payable` = **150000**
- `e: proceeds from issuing common stock` = **150000**
- `e: cash, cash equivalents, and restricted cash — beginning of year` = **170000**
- `e: cash, cash equivalents, and restricted cash — end of year` = **140000**

### Blind solver (trim) — figures

- `a: Change in Cash and cash equivalents (current less prior)` = **-45000**
- `a: Change in Restricted cash (current less prior)` = **15000**
- `a: Change in Accounts receivable, net (current less prior)` = **-90000**
- `a: Change in Inventory (current less prior)` = **100000**
- `a: Change in Equipment (current less prior)` = **700000**
- `a: Change in Accumulated depreciation-equipment (current less prior)` = **-270000**
- `a: Change in Accounts payable (current less prior)` = **-35000**
- `a: Change in Salaries payable (current less prior)` = **-25000**
- `a: Change in Bonds payable (current less prior)` = **150000**
- `a: Change in Common stock, no-par (current less prior)` = **150000**
- `a: Change in Retained earnings (current less prior)` = **170000**
- `a: Beginning cash + cash equivalents + restricted cash` = **170000**
- `a: Ending cash + cash equivalents + restricted cash` = **140000**
- `a: Change in cash + cash equivalents + restricted cash (decrease)` = **-30000**
- `b1: Accounts receivable - beginning balance` = **400000**
- `b1: Accounts receivable - add sales revenue on account` = **4200000**
- `b1: Accounts receivable - less cash collections from customers (SOLVED)` = **4290000**
- `b1: Accounts receivable - ending balance` = **310000**
- `b2: Inventory - beginning balance` = **180000**
- `b2: Inventory - add purchases (SOLVED)` = **2500000**
- `b2: Inventory - less cost of goods sold` = **2400000**
- `b2: Inventory - ending balance` = **280000**
- `b2: Accounts payable - beginning balance` = **220000**
- `b2: Accounts payable - add purchases on account` = **2500000**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 7. `agent_219#05` — chapter 13 — machine_passed

**Machine verdict:** baseline `machine_passed`, trim `machine_passed`  
**Required parts detected:** a, b, c  
**Coverage:** baseline 1.0, trim 1.0

### Question

### QL — CORE long multi-period — Full life cycle: acquire → amortize → impair → amortize → dispose
**LO:** LO 13-3  
**Concept:** Integrated subsequent measurement schedule across acquisition, amortization, impairment, post-impairment amortization, and cash disposal  
**Scenario:**  
**Meridian Optics Corp.** acquired a **process patent** on **January 1, Year 1** for **$96,000** cash. Useful life **8 years**, residual **$0**, straight-line; credits Patent directly. Year-end **December 31**.

- **December 31, Year 3:** After Year 3 amortization, an adverse legal/business change is an **indicator**. Undiscounted future net cash inflows = **$52,000**; fair value = **$48,000**. Remaining life after impairment = **5 years**.  
- **October 1, Year 6:** Meridian **sells** the patent for **$18,500 cash**. Year 6 amortization has not yet been recorded for any months.

**Required:**  
a. Full **subsequent measurement schedule** from Year 1 through Year 5 (include impairment row at end of Year 3 and post-impairment amortization).  
b. All **journal entries** for: (1) acquisition; (2) Year 3 amortization; (3) Year 3 impairment; (4) Year 4 amortization; (5) amortization to Oct 1, Year 6; (6) disposal on Oct 1, Year 6.  
c. Compute **gain or loss** on disposal.

### The key's answer

**Answer key:**

**(a) Subsequent measurement schedule**

Pre-impairment annual amort = \(96{,}000 / 8 = \mathbf{\$12{,}000}\).

| Date / Year | Beg. CA | Amort. | Impairment | End CA | Notes |
|---|---:|---:|---:|---:|---|
| Y1 | $96,000 | $12,000 | — | $84,000 | |
| Y2 | 84,000 | 12,000 | — | 72,000 | |
| Y3 (amort) | 72,000 | 12,000 | — | 60,000 | CA before impairment test |
| Y3 (impair) | 60,000 | — | **12,000** | **48,000** | Recover: \(52k < 60k\); loss \(60k-48k\) |
| Y4 | 48,000 | 9,600 | — | 38,400 | \(48{,}000/5 = 9{,}600\) |
| Y5 | 38,400 | 9,600 | — | **28,800** | |

Post-impairment amort/year = \(48{,}000 / 5 = \mathbf{\$9{,}600}\).

**(b) Journal entries**

*(1) Jan 1, Year 1 — Acquisition*

| Account | Debit | Credit |
|---|---:|---:|
| Patent | 96,000 | |
| Cash | | 96,000 |

**Check:** 96,000 = 96,000.

*(2) Dec 31, Year 3 — Amortization*

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 12,000 | |
| Patent | | 12,000 |

**Check:** 12,000 = 12,000.

*(3) Dec 31, Year 3 — Impairment*  
Recoverability fails (\(52{,}000 < 60{,}000\)). Loss = \(60{,}000 - 48{,}000 = \mathbf{\$12{,}000}\).

| Account | Debit | Credit |
|---|---:|---:|
| Impairment Loss | 12,000 | |
| Patent | | 12,000 |

**Check:** 12,000 = 12,000. New basis **$48,000**.

*(4) Dec 31, Year 4 — Amortization*

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 9,600 | |
| Patent | | 9,600 |

**Check:** 9,600 = 9,600.

*(5) Oct 1, Year 6 — Amortize 9 months of Year 6*  
CA Jan 1, Year 6 (end of Year 5) = **$28,800**.  
Year 6 amort through Oct 1 = \(9{,}600 \times 9/12 = \mathbf{\$7{,}200}\).

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 7,200 | |
| Patent | | 7,200 |

**Check:** 7,200 = 7,200.  
Adjusted CA at sale = \(28{,}800 - 7{,}200 = \mathbf{\$21{,}600}\).

*(6) Oct 1, Year 6 — Disposal*  
Adjusted CA **$21,600** − proceeds **$18,500** = **loss \(21{,}600 - 18{,}500 = \$3{,}100\)**.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 18,500 | |
| Loss on Sale of Patent | 3,100 | |
| Patent | | 21,600 |
| *Remove CA; recognize loss as part of income from continuing operations* | | |

**Check:** Dr \(18{,}500 + 3{,}100 = \mathbf{21{,}600}\); Cr **21,600**. Balanced.

**(c) Loss on disposal** = **$3,100**.

**Proof roll-forward of CA at disposal:**  
\(96{,}000 - 12{,}000\times3 - 12{,}000 - 9{,}600\times2 - 7{,}200 = 96{,}000 - 36{,}000 - 12{,}000 - 19{,}200 - 7{,}200 = \mathbf{\$21{,}600}\). ✓

**Key insight:** The subsequent measurement schedule is the spine of LO 13-3: amortize → test recoverability when indicated → write down to fair value → amortize the new basis → on disposal, amortize to date and clear the residual carrying amount against proceeds.

---

### Blind solver (baseline) — figures

- `a: Year 1 amortization expense` = **12000**
- `a: Year 1 carrying amount, 12/31` = **84000**
- `a: Year 2 amortization expense` = **12000**
- `a: Year 2 carrying amount, 12/31` = **72000**
- `a: Year 3 amortization expense` = **12000**
- `a: Year 3 impairment loss` = **12000**
- `a: Year 3 carrying amount, 12/31 after impairment` = **48000**
- `a: Year 4 amortization expense` = **9600**
- `a: Year 4 carrying amount, 12/31` = **38400**
- `a: Year 5 amortization expense` = **9600**
- `a: Year 5 carrying amount, 12/31` = **28800**
- `c: loss on disposal of patent, 10/1/Year 6` = **3100**

### Blind solver (trim) — figures

- `a: Year 1 — beginning carrying amount` = **96000**
- `a: Year 1 — amortization expense` = **12000**
- `a: Year 1 — ending carrying amount` = **84000**
- `a: Year 2 — beginning carrying amount` = **84000**
- `a: Year 2 — amortization expense` = **12000**
- `a: Year 2 — ending carrying amount` = **72000**
- `a: Year 3 — beginning carrying amount` = **72000**
- `a: Year 3 — amortization expense` = **12000**
- `a: Year 3 — ending carrying amount` = **60000**
- `a: 12/31 Year 3 impairment row — carrying amount before impairment` = **60000**
- `a: 12/31 Year 3 impairment row — undiscounted future net cash inflows (recoverability test)` = **52000**
- `a: 12/31 Year 3 impairment row — impairment loss` = **12000**
- `a: 12/31 Year 3 impairment row — carrying amount after impairment (new basis = fair value)` = **48000**
- `a: post-impairment annual amortization (Years 4-8, 5-year remaining life)` = **9600**
- `a: Year 4 — beginning carrying amount` = **48000**
- `a: Year 4 — amortization expense` = **9600**
- `a: Year 4 — ending carrying amount` = **38400**
- `a: Year 5 — beginning carrying amount` = **38400**
- `a: Year 5 — amortization expense` = **9600**
- `a: Year 5 — ending carrying amount` = **28800**
- `c: carrying amount at Oct 1, Year 6 (after 9 months of Year 6 amortization)` = **21600**
- `c: gain (positive) or loss (negative) on disposal — loss` = **-3100**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 8. `agent_279#01` — chapter 16 — machine_passed

**Machine verdict:** baseline `machine_passed`, trim `machine_passed`  
**Required parts detected:** a, b, c, d  
**Coverage:** baseline 1.0, trim 1.0

### Question

### Q2 — CORE number variant — Copper Ridge Utilities: different face, yield, retirement fraction, call price
**LO:** LO 16-7  
**Concept:** Number-variant twin — effective-interest life cycle with 50% early extinguishment at 103 after period-end update  
**Scenario:**  
On January 1, Year 1, Copper Ridge Utilities issued **$400,000** face of **4-year, 6%** bonds. Cash interest is payable annually each December 31. Bonds were priced to yield **8%** and sold for **$373,503** (discount **$26,497**). Effective interest method; year-end December 31.

On **December 31, Year 2**, after the period-end interest entry and cash interest payment, Copper Ridge retires **50%** of the bonds in the open market at **103**. The remaining 50% is held through maturity.

**Required:**  
a. Record issuance on January 1, Year 1.  
b. Prepare the full effective-interest amortization schedule (Years 1–4).  
c. Record December 31, Year 2 period-end interest, then the 50% extinguishment (show gain/loss computation).  
d. Prepare the remaining-half interest entries conceptually for Year 3 and Year 4 and the maturity entry on December 31, Year 4.

### The key's answer

**Answer key:**  

**a. Issuance**  

| Account | Debit | Credit |
|---------|------:|-------:|
| Cash | 373,503 | |
| Discount on Bonds Payable | 26,497 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Bonds Payable | | 400,000 |

*Dr 400,000 = Cr 400,000. Cash interest each year = $400,000 × 6% = **$24,000**.*

**b. Amortization schedule**  

| Date | Cash (6%) | Interest exp. (8% × beg. CV) | Discount amort. | Unamort. discount | Carrying amount |
|------|----------:|-----------------------------:|----------------:|------------------:|----------------:|
| Jan. 1, Y1 | | | | **26,497** | **373,503** |
| Dec. 31, Y1 | 24,000 | 29,880 | 5,880 | 20,617 | 379,383 |
| Dec. 31, Y2 | 24,000 | 30,351 | 6,351 | 14,266 | 385,734 |
| Dec. 31, Y3 | 24,000 | 30,859 | 6,859 | 7,407 | 392,593 |
| Dec. 31, Y4 | 24,000 | 31,407 | 7,407 | 0 | 400,000 |
| **Totals** | **96,000** | **122,497** | **26,497** | | |

Checks: 373,503 × 0.08 = 29,880.24 → **29,880**; 379,383 × 0.08 = 30,350.64 → **30,351**; 385,734 × 0.08 = 30,858.72 → **30,859**; Year 4 plugs amort **7,407** so CV → face. Discount total amortizes **26,497**.

**c. December 31, Year 2 — Interest then extinguishment**  

**Period-end interest (full issue)**  

| Account | Debit | Credit |
|---------|------:|-------:|
| Interest Expense | 30,351 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Discount on Bonds Payable | | 6,351 |
| &nbsp;&nbsp;&nbsp;&nbsp;Cash | | 24,000 |

*Dr 30,351 = Cr 6,351 + 24,000. CV = $385,734; unamortized discount = $14,266.*

**50% early extinguishment at 103**  

| Item | Amount |
|------|-------:|
| Face retired (50% × $400,000) | 200,000 |
| Discount retired (50% × $14,266) | 7,133 |
| Carrying amount retired | 192,867 |
| Cash paid ($200,000 × 1.03) | 206,000 |
| **Loss** ($206,000 − $192,867) | **13,133** |

| Account | Debit | Credit |
|---------|------:|-------:|
| Bonds Payable | 200,000 | |
| Loss on Extinguishment of Debt | 13,133 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Discount on Bonds Payable | | 7,133 |
| &nbsp;&nbsp;&nbsp;&nbsp;Cash | | 206,000 |

*Dr 213,133 = Cr 213,133.*

**d. Remaining 50% — subsequent measurement and maturity**  

Beginning remaining CV after extinguishment = **$192,867**; remaining unamortized discount = **$7,133**; remaining face = **$200,000**. Cash interest each year on remaining bonds = **$12,000**.

| Date | Cash | Interest exp. | Discount amort. | Unamort. disc. | Carrying amount |
|------|-----:|--------------:|----------------:|---------------:|----------------:|
| After extinguishment (end Y2) | | | | **7,133** | **192,867** |
| Dec. 31, Y3 | 12,000 | 15,429 | 3,429 | 3,704 | 196,296 |
| Dec. 31, Y4 | 12,000 | 15,704 | 3,704 | 0 | 200,000 |

Year 3 interest: 192,867 × 0.08 = 15,429.36 → **15,429**. Year 4 plugs amort **3,704**.

**Dec. 31, Y3 interest**  

| Account | Debit | Credit |
|---------|------:|-------:|
| Interest Expense | 15,429 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Discount on Bonds Payable | | 3,429 |
| &nbsp;&nbsp;&nbsp;&nbsp;Cash | | 12,000 |

**Dec. 31, Y4 interest**  

| Account | Debit | Credit |
|---------|------:|-------:|
| Interest Expense | 15,704 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Discount on Bonds Payable | | 3,704 |
| &nbsp;&nbsp;&nbsp;&nbsp;Cash | | 12,000 |

**Maturity settlement**  

| Account | Debit | Credit |
|---------|------:|-------:|
| Bonds Payable | 200,000 | |
| &nbsp;&nbsp;&nbsp;&nbsp;Cash | | 200,000 |

*All entries balance. No gain/loss at maturity.*

**Key insight:** Changing face, market rate, call price, and fraction retired changes the loss magnitude, but the **sequence** never changes: schedule → period-end update of CV → compare reacquisition price to CV of portion retired.

---

### Blind solver (baseline) — figures

- `b: Year 1 cash interest` = **24000**
- `b: Year 1 interest expense` = **29880**
- `b: Year 1 discount amortized` = **5880**
- `b: Year 1 ending carrying value` = **379383**
- `b: Year 2 cash interest` = **24000**
- `b: Year 2 interest expense` = **30351**
- `b: Year 2 discount amortized` = **6351**
- `b: Year 2 ending carrying value` = **385734**
- `b: Year 3 cash interest` = **24000**
- `b: Year 3 interest expense` = **30859**
- `b: Year 3 discount amortized` = **6859**
- `b: Year 3 ending carrying value` = **392593**
- `b: Year 4 cash interest` = **24000**
- `b: Year 4 interest expense` = **31407**
- `b: Year 4 discount amortized` = **7407**
- `b: Year 4 ending carrying value` = **400000**
- `c: carrying value of the 50% retired (Dec 31, Year 2)` = **192867**
- `c: reacquisition price paid (50% at 103)` = **206000**
- `c: loss on extinguishment of 50% of the bonds` = **13133**
- `d: Year 3 interest expense (remaining 50%)` = **15429**
- `d: Year 3 discount amortized (remaining 50%)` = **3429**
- `d: Year 3 cash interest (remaining 50%)` = **12000**
- `d: Year 4 interest expense (remaining 50%)` = **15704**
- `d: Year 4 discount amortized (remaining 50%)` = **3704**

### Blind solver (trim) — figures

- `a: Cash debited on issuance (Jan 1, Year 1)` = **373503.0**
- `a: Discount on Bonds Payable debited on issuance` = **26497.0**
- `a: Bonds Payable credited on issuance` = **400000.0**
- `b: Year 1 beginning carrying value` = **373503.0**
- `b: Year 1 interest expense (8% x beginning carrying value)` = **29880.0**
- `b: Year 1 cash interest paid (6% x face)` = **24000.0**
- `b: Year 1 discount amortization` = **5880.0**
- `b: Year 1 ending carrying value` = **379383.0**
- `b: Year 1 unamortized discount at year-end` = **20617.0**
- `b: Year 2 beginning carrying value` = **379383.0**
- `b: Year 2 interest expense (8% x beginning carrying value)` = **30351.0**
- `b: Year 2 cash interest paid (6% x face)` = **24000.0**
- `b: Year 2 discount amortization` = **6351.0**
- `b: Year 2 ending carrying value` = **385734.0**
- `b: Year 2 unamortized discount at year-end` = **14266.0**
- `b: Year 3 beginning carrying value` = **385734.0**
- `b: Year 3 interest expense (8% x beginning carrying value)` = **30859.0**
- `b: Year 3 cash interest paid (6% x face)` = **24000.0**
- `b: Year 3 discount amortization` = **6859.0**
- `b: Year 3 ending carrying value` = **392593.0**
- `b: Year 3 unamortized discount at year-end` = **7407.0**
- `b: Year 4 beginning carrying value` = **392593.0**
- `b: Year 4 interest expense (8% x beginning carrying value)` = **31407.0**
- `b: Year 4 cash interest paid (6% x face)` = **24000.0**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 9. `agent_135#01` — chapter 14 — machine_passed

**Machine verdict:** baseline `machine_passed`, trim `machine_passed`  
**Required parts detected:** a, b, c, d, e, f, g, h  
**Coverage:** baseline 1.0, trim 1.0

### Question

### Q2 — CORE number variant twin
**LO:** LO 14-3  
**Concept:** number_variant_twin — same AFS FV-OCI path (purchase, interest, FVA schedule, sale reclass) with all new amounts  
**Scenario:**  
On **January 1 of Year 1**, **Riverton Mutual Fund Services** purchased for **par $55,000** of **Oakmont Industries 9%** bonds that mature on **December 31 of Year 4**. Cash interest is paid **annually** each December 31. Riverton classifies the bonds as **AFS** (FV-OCI). Year-end is December 31. Beginning AOCI related to AFS is zero. No other AFS activity except as stated.

**Fair values and sale:**
| Date | Fair value / event |
|---|---|
| Dec 31, Year 1 | Fair value **$52,250** |
| Dec 31, Year 2 | Fair value **$57,200** (no sales in Year 2) |
| Jan 1, Year 3 | Sold entire holding for **$57,750** cash |

**Required:**  
(a) Purchase entry on January 1 of Year 1.  
(b) Cash interest entry on December 31 of Year 1.  
(c) Subsequent measurement (FVA) schedule for Dec 31 Y1, Dec 31 Y2, and Jan 1 Y3 sale date (same columns as Q1).  
(d) Period-end FV-OCI adjusting JE for Year 1.  
(e) Year 1 IS / SCI / BS presentation for this investment.  
(f) Period-end FV-OCI adjusting JE for Year 2.  
(g) January 1 Year 3: (i) sale-date FV-OCI adjust; (ii) sale + reclass + eliminate FVA.  
(h) Year 3 AOCI reconciliation after the sale.

### The key's answer

**Answer key:**  

**(a) January 1, Year 1 — Purchase**

| Account | Debit | Credit |
|---|---:|---:|
| Investment in AFS Securities—Oakmont Bonds | 55,000 | |
| Cash | | 55,000 |

**Check:** Dr = Cr = **$55,000**. **Balanced.**

**(b) December 31, Year 1 — Interest**  
Interest = \(55{,}000 \times 0.09 \times 12/12 = \mathbf{\$4{,}950}\)

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 4,950 | |
| Interest Revenue | | 4,950 |

**Check:** Dr = Cr = **$4,950**. **Balanced.**

**(c) Subsequent measurement schedule — FVA rollforward**

| Measurement date | Amortized cost | Fair value / sale price | Required FVA | Existing FVA | Increase/(decrease) | FVA after adj. |
|---|---:|---:|---:|---:|---:|---:|
| Dec 31, Year 1 | 55,000 | 52,250 | (2,750) | 0 | **(2,750)** | (2,750) |
| Dec 31, Year 2 | 55,000 | 57,200 | 2,200 | (2,750) | **4,950** | 2,200 |
| Jan 1, Year 3 (sale) | 55,000 | 57,750 | 2,750 | 2,200 | **550** | 2,750 |

**Checks:**  
- Y1: 52,250 − 55,000 = **(2,750)**.  
- Y2: required 2,200 − existing (−2,750) = **4,950** increase.  
- Sale: required 2,750 − existing 2,200 = **550** increase.  
- Realized gain at sale = 57,750 − 55,000 = **2,750**.

**(d) December 31, Year 1 — FV-OCI loss**

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—OCI | 2,750 | |
| Fair Value Adjustment—AFS | | 2,750 |

**Check:** Dr = Cr = **$2,750**. **Balanced.** BS carrying amount = **$52,250**.

**(e) Year 1 presentation**  
- **IS:** Interest revenue **$4,950** (no unrealized AFS loss in NI).  
- **SCI:** Unrealized holding loss on AFS **$(2,750)** in OCI.  
- **BS:** Investment in AFS **$52,250**; AOCI **$(2,750)**.

**(f) December 31, Year 2 — FVA rollforward entry**

| Account | Debit | Credit |
|---|---:|---:|
| Fair Value Adjustment—AFS | 4,950 | |
| Unrealized Gain or Loss—OCI | | 4,950 |

**Check:** Dr = Cr = **$4,950**. **Balanced.** FVA ending = **$2,200 debit**. AOCI = **$2,200**.

**(g) January 1, Year 3 — Sale**

**(i) Sale-date adjust**

| Account | Debit | Credit |
|---|---:|---:|
| Fair Value Adjustment—AFS | 550 | |
| Unrealized Gain or Loss—OCI | | 550 |

**Check:** Dr = Cr = **$550**. **Balanced.**

**(ii) Sale + reclass + eliminate FVA**  
Realized gain = **$2,750**.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 57,750 | |
| Unrealized Gain or Loss—OCI | 2,750 | |
| Investment in AFS—Oakmont Bonds | | 55,000 |
| Gain on Sale of Investment | | 2,750 |
| Fair Value Adjustment—AFS | | 2,750 |

**Proof:** Debits \(57{,}750 + 2{,}750 = \mathbf{\$60{,}500}\); Credits \(55{,}000 + 2{,}750 + 2{,}750 = \mathbf{\$60{,}500}\). **Balanced.**

**(h) Year 3 AOCI reconciliation**

| | Amount |
|---|---:|
| AOCI, January 1, Year 3 | $2,200 |
| Current period unrealized gain (sale-date adj) | 550 |
| Reclassification adjustment for gain included in NI | (2,750) |
| AOCI, December 31, Year 3 | **$0** |

Lifecycle check: Y1 \((2{,}750)\) + Y2 \(4{,}950\) + Y3 \(550\) − reclass \((2{,}750)\) = **$0**.

**Key insight:** Same FV-OCI control logic as Q1—**required FVA − existing FVA**—with fully changed face, coupon pattern (annual), fair values, and sale price so the arithmetic is practiced without reusing Q1 or textbook demo numbers.

---

### Blind solver (baseline) — figures

- `c: Dec 31 Y1 — amortized cost` = **55000**
- `c: Dec 31 Y1 — fair value` = **52250**
- `c: Dec 31 Y1 — cumulative unrealized holding gain (loss) = required FVA balance` = **-2750**
- `c: Dec 31 Y1 — existing FVA balance` = **0**
- `c: Dec 31 Y1 — increase (decrease) to FVA needed` = **-2750**
- `c: Dec 31 Y2 — amortized cost` = **55000**
- `c: Dec 31 Y2 — fair value` = **57200**
- `c: Dec 31 Y2 — cumulative unrealized holding gain (loss) = required FVA balance` = **2200**
- `c: Dec 31 Y2 — existing FVA balance` = **-2750**
- `c: Dec 31 Y2 — increase (decrease) to FVA needed` = **4950**
- `c: Jan 1 Y3 sale date — amortized cost` = **55000**
- `c: Jan 1 Y3 sale date — fair value` = **57750**
- `c: Jan 1 Y3 sale date — cumulative unrealized holding gain (loss) = required FVA balance` = **2750**
- `c: Jan 1 Y3 sale date — existing FVA balance` = **2200**
- `c: Jan 1 Y3 sale date — increase (decrease) to FVA needed` = **550**
- `e: Year 1 income statement — Interest revenue` = **4950**
- `e: Year 1 statement of comprehensive income — Unrealized holding gain (loss) on AFS securities, OCI` = **-2750**
- `e: Dec 31 Y1 balance sheet — Investment in available-for-sale securities (at fair value)` = **52250**
- `e: Dec 31 Y1 balance sheet — Accumulated other comprehensive income (loss)` = **-2750**
- `h: Accumulated OCI, January 1, Year 3` = **2200**
- `h: Current period unrealized gain (loss) on AFS securities` = **550**
- `h: Reclassification adjustment for gain included in net income` = **-2750**
- `h: Net change in AOCI during Year 3` = **-2200**
- `h: Accumulated OCI, December 31, Year 3` = **0**

### Blind solver (trim) — figures

- `a: Debit — Investment in Oakmont bonds (AFS/FV-OCI), Jan 1 Y1` = **55000.0**
- `a: Credit — Cash paid on purchase, Jan 1 Y1` = **55000.0**
- `b: Cash interest received Dec 31 Y1 (= $55,000 x 9%)` = **4950.0**
- `b: Interest income recognized Dec 31 Y1` = **4950.0**
- `c: Dec 31 Y1 — amortized cost` = **55000.0**
- `c: Dec 31 Y1 — fair value` = **52250.0**
- `c: Dec 31 Y1 — required FVA balance (credit)` = **-2750.0**
- `c: Dec 31 Y1 — prior FVA balance` = **0.0**
- `c: Dec 31 Y1 — FVA adjustment required (credit FVA / OCI loss)` = **-2750.0**
- `c: Dec 31 Y1 — carrying amount after adjustment` = **52250.0**
- `c: Dec 31 Y2 — amortized cost` = **55000.0**
- `c: Dec 31 Y2 — fair value` = **57200.0**
- `c: Dec 31 Y2 — required FVA balance (debit)` = **2200.0**
- `c: Dec 31 Y2 — prior FVA balance (credit)` = **-2750.0**
- `c: Dec 31 Y2 — FVA adjustment required (debit FVA / OCI gain)` = **4950.0**
- `c: Dec 31 Y2 — carrying amount after adjustment` = **57200.0**
- `c: Jan 1 Y3 sale date — amortized cost` = **55000.0**
- `c: Jan 1 Y3 sale date — fair value (= proceeds)` = **57750.0**
- `c: Jan 1 Y3 sale date — required FVA balance (debit)` = **2750.0**
- `c: Jan 1 Y3 sale date — prior FVA balance (debit)` = **2200.0**
- `c: Jan 1 Y3 sale date — FVA adjustment required (debit FVA / OCI gain)` = **550.0**
- `c: Jan 1 Y3 sale date — carrying amount after adjustment` = **57750.0**
- `d: Year 1 unrealized holding loss recognized in OCI (Dr)` = **2750.0**
- `d: Year 1 credit to Fair value adjustment (AFS)` = **2750.0**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 10. `agent_016#00` — chapter 16 — machine_passed

**Machine verdict:** baseline `machine_passed`, trim `machine_passed`  
**Required parts detected:** a, b, c, d, e  
**Coverage:** baseline 1.0, trim 1.0

### Question

### Q1 — CORE — Interest-bearing note issued for cash at a discount (full lifecycle)
**LO:** LO 16-6  
**Concept:** Initial recognition JE + effective-interest schedule + period-end interest JE + maturity settlement  
**Scenario:** On January 1, Year 1, **Redwood Metalworks Inc.** borrows cash by issuing a **3-year, $80,000** note payable to Northshore Bank. The note pays **5%** cash interest annually each December 31. The market rate for notes of similar risk is **9%**. Redwood’s fiscal year ends December 31. Redwood uses the **effective interest method**.

**Required:**  
(a) Compute the cash proceeds (issue price) of the note on January 1, Year 1. Round the present value to the nearest cent.  
(b) Record the **initial recognition** journal entry on January 1, Year 1.  
(c) Prepare the complete **effective-interest amortization schedule** over the 3-year term (show cash interest, interest expense, discount amortization, and carrying amount). Plug any final-period rounding difference so the carrying amount equals face at maturity.  
(d) Record the **December 31, Year 1** interest entry (period-end).  
(e) Record the **December 31, Year 3** interest entry and the **maturity settlement** entry (principal only may be shown separately from interest).

### The key's answer

**Answer key:**  

**(a) Issue price (PV of cash flows at 9%)**  
Annual cash interest = \(80{,}000 \times 5\% = \$4{,}000\).

\[
\begin{align*}
PV &= 4{,}000 \times PVA_{9\%,3} + 80{,}000 \times PVF_{9\%,3} \\
PVA_{9\%,3} &= \frac{1-(1.09)^{-3}}{0.09} \approx 2.531294666\\
PVF_{9\%,3} &= (1.09)^{-3} \approx 0.772183480\\
PV_{\text{raw}} &= 4{,}000(2.531294666) + 80{,}000(0.772183480) \approx 71{,}899.857
\end{align*}
\]

\(PV = \mathbf{\$71{,}899.86}\) (ROUND_HALF_UP to cent).  
**Discount on Note Payable** = \(80{,}000 - 71{,}899.86 = \mathbf{\$8{,}100.14}\).

**(b) January 1, Year 1 — Initial recognition**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 71,899.86 | |
| Discount on Note Payable | 8,100.14 | |
| Note Payable | | 80,000.00 |

*Check:* Dr \(71{,}899.86 + 8{,}100.14 = 80{,}000.00\) = Cr. Carrying amount = \(80{,}000 - 8{,}100.14 = \$71{,}899.86\).

**(c) Effective-interest amortization schedule (market 9%)**

| Date | Cash (5%) | Interest expense (9% × CA) | Discount amort. | Carrying amount |
|---|---:|---:|---:|---:|
| Jan. 1, Y1 | — | — | — | 71,899.86 |
| Dec. 31, Y1 | 4,000.00 | 6,470.99 | 2,470.99 | 74,370.85 |
| Dec. 31, Y2 | 4,000.00 | 6,693.38 | 2,693.38 | 77,064.23 |
| Dec. 31, Y3 | 4,000.00 | 6,935.77* | 2,935.77* | 80,000.00 |
| **Totals** | **12,000.00** | **20,100.14** | **8,100.14** | |

\*Year 3: discount amort. plugged = \(80{,}000.00 - 77{,}064.23 = 2{,}935.77\); interest expense = cash + amort. = \(4{,}000 + 2{,}935.77 = 6{,}935.77\).  
*Roll-forward checks:* \(71{,}899.86 + 2{,}470.99 = 74{,}370.85\); \(74{,}370.85 + 2{,}693.38 = 77{,}064.23\); \(77{,}064.23 + 2{,}935.77 = 80{,}000.00\).  
Interest expense total \(20{,}100.14 = \) cash interest \(12{,}000 + \) discount \(8{,}100.14\).

**(d) December 31, Year 1 — Period-end interest**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 6,470.99 | |
| Discount on Note Payable | | 2,470.99 |
| Cash | | 4,000.00 |

*Check:* \(6{,}470.99 = 2{,}470.99 + 4{,}000.00\).

**(e) December 31, Year 3 — Final interest + maturity**

Interest:

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 6,935.77 | |
| Discount on Note Payable | | 2,935.77 |
| Cash | | 4,000.00 |

Maturity settlement (principal):

| Account | Debit | Credit |
|---|---:|---:|
| Note Payable | 80,000.00 | |
| Cash | | 80,000.00 |

(After Year 3 amortization, Discount on Note Payable is fully amortized to zero; net liability = face.)

**Key insight:** When the stated rate is below the market rate, cash proceeds are less than face—the **discount is interest cost recognized over the term** via effective interest (not cash coupons alone). Initial measurement is always **PV of future cash flows at the market rate at inception**.

---

### Blind solver (baseline) — figures

- `a: cash proceeds (issue price) of the note on January 1, Year 1` = **71899.86**
- `c: Year 1 carrying amount at beginning of year` = **71899.86**
- `c: Year 1 cash interest paid` = **4000.0**
- `c: Year 1 interest expense` = **6470.99**
- `c: Year 1 discount amortization` = **2470.99**
- `c: Year 1 carrying amount at end of year` = **74370.85**
- `c: Year 2 carrying amount at beginning of year` = **74370.85**
- `c: Year 2 cash interest paid` = **4000.0**
- `c: Year 2 interest expense` = **6693.38**
- `c: Year 2 discount amortization` = **2693.38**
- `c: Year 2 carrying amount at end of year` = **77064.23**
- `c: Year 3 carrying amount at beginning of year` = **77064.23**
- `c: Year 3 cash interest paid` = **4000.0**
- `c: Year 3 interest expense` = **6935.77**
- `c: Year 3 discount amortization` = **2935.77**
- `c: Year 3 carrying amount at end of year` = **80000.0**

### Blind solver (trim) — figures

- `a: Cash proceeds (issue price) of the note, Jan 1 Year 1` = **71899.86**
- `a: Discount on note payable at issuance (face - proceeds)` = **8100.14**
- `a: Annual cash interest payment (80,000 x 5%)` = **4000.0**
- `c: Carrying amount at Jan 1, Year 1 (schedule opening balance)` = **71899.86**
- `c: Year 1 - cash interest paid` = **4000.0**
- `c: Year 1 - interest expense (9% x beginning carrying amount)` = **6470.99**
- `c: Year 1 - discount amortization` = **2470.99**
- `c: Year 1 - ending carrying amount` = **74370.85**
- `c: Year 2 - cash interest paid` = **4000.0**
- `c: Year 2 - interest expense (9% x beginning carrying amount)` = **6693.38**
- `c: Year 2 - discount amortization` = **2693.38**
- `c: Year 2 - ending carrying amount` = **77064.23**
- `c: Year 3 - cash interest paid` = **4000.0**
- `c: Year 3 - interest expense (9% x beginning carrying amount)` = **6935.77**
- `c: Year 3 - discount amortization` = **2935.77**
- `c: Year 3 - ending carrying amount` = **80000.0**
- `c: Totals - cash interest over 3 years` = **12000.0**
- `c: Totals - interest expense over 3 years` = **20100.14**
- `c: Totals - discount amortization over 3 years` = **8100.14**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 11. `agent_032#01` — chapter 18 — flip

**Machine verdict:** baseline `machine_passed`, trim `failed`  
**Required parts detected:** a, b, c, d  
**Coverage:** baseline 1.0, trim 1.0

### Question

### Q2 — CORE number variant — Harborline Ceramics: NOL carryforward twin
**LO:** LO 18-7  
**Concept:** NOL carryforward initial recognition and Year-2 utilization with valuation allowance (number-variant twin of Q1)  
**Scenario:**  
**Harborline Ceramics LLC** reports a tax operating loss of **$(120,000)** in Year 1. Enacted tax rate is **25%** for all years. No temporary differences other than the NOL carryforward. Carryforward only (no carryback); **80%** utilization limit applies. At December 31, Year 1, realization of the full DTA is **more likely than not**. In Year 2, actual taxable income is **$30,000**. At December 31, Year 2 (after utilization), management concludes it is MLTN that **only 75%** of the remaining DTA will be realized (VA beginning balance $0).

**Required:**  
(a) Compute DTA at 12/31/Y1 and record the initial recognition JE.  
(b) Show Year 1 partial IS (operating loss, tax benefit, net loss).  
(c) Record the Year 2 income tax JE (utilization + payable).  
(d) Record the Year 2 valuation allowance JE. State net DTA reported.

### The key's answer

**Answer key:**

**(a)**  
DTA = \(120{,}000 \times 25\% = \mathbf{\$30{,}000}\).

| Account | Debit | Credit |
|---|---:|---:|
| Deferred Tax Asset | 30,000 | |
| Income Tax Expense | | 30,000 |

**(b)**  

| | Amount |
|---|---:|
| Operating loss before income taxes | $(120,000) |
| Income tax benefit | 30,000 |
| Net loss | **$(90,000)** |

**(c) Year 2**  
NOL used = \(30{,}000 \times 80\% = \mathbf{\$24{,}000}\).  
Remaining NOL = \(120{,}000 - 24{,}000 = \mathbf{\$96{,}000}\).  
Ending DTA = \(96{,}000 \times 25\% = \mathbf{\$24{,}000}\).  
DTA reduction = \(30{,}000 - 24{,}000 = \mathbf{\$6{,}000}\).  
Income tax payable = \(30{,}000 \times 20\% \times 25\% = \mathbf{\$1{,}500}\).  
Income tax expense = \(6{,}000 + 1{,}500 = \mathbf{\$7{,}500}\).

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 7,500 | |
| Deferred Tax Asset | | 6,000 |
| Income Tax Payable | | 1,500 |

**(d) Valuation allowance**  
Unrealizable portion = \(25\% \times 24{,}000 = \mathbf{\$6{,}000}\).

| Account | Debit | Credit |
|---|---:|---:|
| Income Tax Expense | 6,000 | |
| Valuation Allowance for Deferred Tax Asset | | 6,000 |

Net DTA reported = \(24{,}000 - 6{,}000 = \mathbf{\$18{,}000}\).

**Key insight:** Same mechanics as Q1 with scaled numbers—always recompute DTA as **remaining NOL × rate**, tax payable on the **non-offset** slice of TI, and VA as a separate judgment after the gross DTA is updated.

---

### Blind solver (baseline) — figures

- `a: Deferred tax asset at 12/31/Year 1` = **30000**
- `b: Year 1 operating loss before income taxes` = **-120000**
- `b: Year 1 income tax benefit (deferred)` = **30000**
- `b: Year 1 net loss` = **-90000**
- `d: Net deferred tax asset reported at 12/31/Year 2` = **18000**

### Blind solver (trim) — figures

- `a: NOL carryforward at 12/31/Y1` = **120000**
- `a: Deferred tax asset at 12/31/Y1 (120,000 x 25%)` = **30000**
- `a: Valuation allowance at 12/31/Y1 (full realization MLTN)` = **0**
- `b: Operating loss before income taxes, Year 1` = **-120000**
- `b: Income tax benefit, Year 1` = **30000**
- `b: Net loss, Year 1` = **-90000**
- `c: Year 2 taxable income before NOL deduction` = **30000**
- `c: NOL deduction allowed in Year 2 (80% x 30,000)` = **24000**
- `c: Taxable income after NOL deduction` = **6000**
- `c: Income tax payable, Year 2 (6,000 x 25%)` = **1500**
- `c: DTA reduction from NOL utilization (24,000 x 25%)` = **6000**
- `c: Total income tax expense recorded in Year 2 entry (c)` = **7500**
- `d: NOL carryforward remaining at 12/31/Y2` = **96000**
- `d: Gross DTA at 12/31/Y2 before valuation allowance` = **24000**
- `d: Valuation allowance required at 12/31/Y2 (25% of 24,000)` = **6000**
- `d: Increase in valuation allowance recorded (additional tax expense)` = **6000**
- `d: Net DTA reported at 12/31/Y2` = **18000**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 12. `agent_043#00` — chapter 8 — flip

**Machine verdict:** baseline `machine_passed`, trim `failed`  
**Required parts detected:** a, b, c, d, e  
**Coverage:** baseline 1.0, trim 1.0

### Question

### Q1 — CORE — Cascade Outfitters: zero-interest NR for inventory (initial JE, schedule, YE accruals, maturity)
**LO:** LO 8-5  
**Concept:** Initial recognition of 0% stated / 10% market noncurrent NR for inventory; effective-interest amortization; interim YE allocation; face settlement  
**Scenario:**  
On **June 30, Year 1**, **Cascade Outfitters Co.** sells inventory with a clearly determinable fair value of **$11,269** and receives in exchange a **three-year, noninterest-bearing** note with face (stated) value of **$15,000**. Principal is due in a single payment on **June 30, Year 4**. There are **no** periodic cash interest receipts (stated rate = **0%**). The market rate for notes of similar risk is **10%**. Ignore cost of goods sold.

The present value of the note equals the fair value of the inventory exchanged:

\[
PV = \frac{15{,}000}{(1.10)^{3}} = \mathbf{\$11{,}269}
\]

(Excel-equivalent: `PV(0.10,3,0,15000)` absolute value; or `RATE(3,0,-11269,15000)` confirms **10%**.)

**Required:**  
(a) Record the **June 30, Year 1** journal entry for receipt of the note (initial recognition). Compute the initial **Discount on Note Receivable**.  
(b) Prepare the **effective-interest amortization schedule** for the full term (cash interest, interest revenue, discount amortization, carrying amount).  
(c) Assume Cascade has a **June 30** fiscal year-end (note anniversary). Record all **interest accrual** entries on June 30 of Years 2, 3, and 4, and the **settlement** entry on June 30, Year 4 when face is collected.  
(d) Assume instead Cascade has a **December 31** year-end. The initial recognition and final cash collection entries are unchanged. Allocate the amortization schedule into reporting periods and record interest accruals on **December 31 of Years 1, 2, and 3** and on **June 30, Year 4**. Verify total interest revenue equals the original discount.  
(e) Briefly state how the note is **presented** on the December 31, Year 1 balance sheet (current vs noncurrent).

### The key's answer

**Answer key:**

**(a) Initial recognition — June 30, Year 1**

Discount = face − PV = \(15{,}000 - 11{,}269 = \mathbf{\$3{,}731}\).

| Account | Debit | Credit |
|---|---:|---:|
| Note Receivable | 15,000 | |
| Discount on Note Receivable | | 3,731 |
| Sales Revenue | | 11,269 |

Check: Dr 15,000 = Cr 3,731 + 11,269. Net note receivable (carrying amount) = **$11,269**.

**(b) Effective-interest amortization schedule (market = 10%; stated cash interest = $0)**

| Date | Cash interest (stated 0%) | Interest revenue (CA × 10%) | Discount amortization | Note receivable, net (CA) |
|------|--------------------------:|----------------------------:|----------------------:|--------------------------:|
| June 30, Year 1 | — | — | — | **11,269** |
| June 30, Year 2 | 0 | 1,127 | 1,127 | 12,396 |
| June 30, Year 3 | 0 | 1,240 | 1,240 | 13,636 |
| June 30, Year 4 | 0 | 1,364 | 1,364 | **15,000** |
| **Totals** | **0** | **3,731** | **3,731** | |

Interest checks: \(11{,}269 \times 0.10 = 1{,}126.9 \to 1{,}127\); \(12{,}396 \times 0.10 = 1{,}239.6 \to 1{,}240\); \(13{,}636 \times 0.10 = 1{,}363.6 \to 1{,}364\).  
\(11{,}269 + 1{,}127 + 1{,}240 + 1{,}364 = 15{,}000\). Sales revenue \(11{,}269\) + total interest revenue \(3{,}731\) = total cash \(15{,}000\).

**(c) June 30 year-end accruals and settlement**

June 30, Year 2 — amortize discount / recognize interest:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 1,127 | |
| Interest Revenue | | 1,127 |

June 30, Year 3:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 1,240 | |
| Interest Revenue | | 1,240 |

June 30, Year 4 — final interest:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 1,364 | |
| Interest Revenue | | 1,364 |

June 30, Year 4 — collect face (after discount is fully amortized; net CA = face):

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 15,000 | |
| Note Receivable | | 15,000 |

**(d) December 31 year-end — allocate schedule amounts to reporting periods**

Half-year splits of each annual interest amount (first half of each note year gets the ceiling when odd):

| Note-year interest (ended June 30) | Amount | Allocated to prior Dec 31 | Allocated to next period |
|------------------------------------|-------:|----------------------------:|-------------------------:|
| Year ended June 30, Y2 | 1,127 | Dec 31, Y1: **564** | first half Y2: **563** |
| Year ended June 30, Y3 | 1,240 | Dec 31, Y2: **620** | first half Y3: **620** |
| Year ended June 30, Y4 | 1,364 | Dec 31, Y3: **682** | June 30, Y4: **682** |

Reporting-period interest revenue:

| Reporting date | Interest revenue | Build-up |
|----------------|-----------------:|----------|
| Dec 31, Year 1 | **564** | 564 |
| Dec 31, Year 2 | **1,183** | 563 + 620 |
| Dec 31, Year 3 | **1,302** | 620 + 682 |
| June 30, Year 4 | **682** | 682 |
| **Total** | **3,731** | equals original discount |

Journal entries:

December 31, Year 1:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 564 | |
| Interest Revenue | | 564 |

December 31, Year 2:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 1,183 | |
| Interest Revenue | | 1,183 |

December 31, Year 3:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 1,302 | |
| Interest Revenue | | 1,302 |

June 30, Year 4:

| Account | Debit | Credit |
|---|---:|---:|
| Discount on Note Receivable | 682 | |
| Interest Revenue | | 682 |

(Settlement Cash / Note Receivable same as part c.)

**(e) Classification / presentation — December 31, Year 1**

After the Dec 31, Y1 accrual, carrying amount = \(11{,}269 + 564 = \mathbf{\$11{,}833}\).  
Principal is not due until June 30, Year 4 (more than one year from Dec 31, Y1), so the **entire net note receivable of $11,833** is reported as a **noncurrent asset**. Discount on Note Receivable is a **contra-asset** deducted from Note Receivable (face) to arrive at the net carrying amount; it is not a liability.

**Key insight:** A 0% stated-rate note still has interest — the entire discount amortizes into interest revenue under the effective-interest method (CA × market rate). Initial sales revenue is limited to the **present value**, not face; cash interest is zero so Dr Discount = Cr Interest Revenue each period.

---

### Blind solver (baseline) — figures

- `a: Discount on Note Receivable at June 30, Year 1 (initial)` = **3731**
- `b: carrying amount at June 30, Year 1 (schedule opening balance)` = **11269**
- `b: cash interest, note year 1 (ended June 30, Year 2)` = **0**
- `b: interest revenue, note year 1 (ended June 30, Year 2)` = **1127**
- `b: discount amortization, note year 1 (ended June 30, Year 2)` = **1127**
- `b: carrying amount at June 30, Year 2` = **12396**
- `b: cash interest, note year 2 (ended June 30, Year 3)` = **0**
- `b: interest revenue, note year 2 (ended June 30, Year 3)` = **1240**
- `b: discount amortization, note year 2 (ended June 30, Year 3)` = **1240**
- `b: carrying amount at June 30, Year 3` = **13636**
- `b: cash interest, note year 3 (ended June 30, Year 4)` = **0**
- `b: interest revenue, note year 3 (ended June 30, Year 4)` = **1364**
- `b: discount amortization, note year 3 (ended June 30, Year 4)` = **1364**
- `b: carrying amount at June 30, Year 4` = **15000**
- `b: total cash interest over term` = **0**
- `b: total interest revenue over term` = **3731**
- `b: total discount amortization over term` = **3731**
- `d: interest revenue recognized December 31, Year 1` = **564**
- `d: interest revenue recognized December 31, Year 2` = **1183**
- `d: interest revenue recognized December 31, Year 3` = **1302**
- `d: interest revenue recognized June 30, Year 4` = **682**
- `d: total interest revenue over term (equals initial discount)` = **3731**
- `e: unamortized Discount on Note Receivable at December 31, Year 1` = **3167**
- `e: net Note Receivable presented at December 31, Year 1 (noncurrent asset)` = **11833**

### Blind solver (trim) — figures

- `a: PV of note / fair value of inventory recorded (sales revenue), Jun 30 Yr 1` = **11269.0**
- `a: Face (maturity) value of note receivable` = **15000.0**
- `a: Initial Discount on Note Receivable (face less PV)` = **3731.0**
- `a: Cash interest received each period (0% stated rate)` = **0.0**
- `b: Period 1 (Jun 30 Yr1-Jun 30 Yr2) carrying amount, beginning` = **11269.0**
- `b: Period 1 cash interest` = **0.0**
- `b: Period 1 interest revenue (10% x carrying amount)` = **1126.9**
- `b: Period 1 discount amortization` = **1126.9**
- `b: Period 1 carrying amount, ending (Jun 30 Yr2)` = **12395.9**
- `b: Period 2 cash interest` = **0.0**
- `b: Period 2 interest revenue` = **1239.59**
- `b: Period 2 discount amortization` = **1239.59**
- `b: Period 2 carrying amount, ending (Jun 30 Yr3)` = **13635.49**
- `b: Period 3 cash interest` = **0.0**
- `b: Period 3 interest revenue (plug to close to face)` = **1364.51**
- `b: Period 3 discount amortization` = **1364.51**
- `b: Period 3 carrying amount, ending (Jun 30 Yr4) = face` = **15000.0**
- `b: Total cash interest over term` = **0.0**
- `b: Total interest revenue over term` = **3731.0**
- `b: Total discount amortized over term (= initial discount)` = **3731.0**
- `c: Interest revenue accrued Jun 30 Yr2` = **1126.9**
- `c: Interest revenue accrued Jun 30 Yr3` = **1239.59**
- `c: Interest revenue accrued Jun 30 Yr4` = **1364.51**
- `c: Cash collected at maturity Jun 30 Yr4` = **15000.0**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 13. `agent_053#01` — chapter 9 — flip

**Machine verdict:** baseline `machine_passed`, trim `failed`  
**Required parts detected:** a, b, c, d, e  
**Coverage:** baseline 1.0, trim 1.0

### Question

### Q2 — CORE number variant — Northfork Merchandising: LIFO reserve twin
**LO:** LO 9-6  
**Concept:** Number-variant twin — create LIFO reserve, multi-year Δ-reserve schedule, period-end JEs, and BS net presentation  
**Scenario:**  
**Northfork Merchandising LLC** uses **average cost** for internal records and converts to **LIFO** at year-end for external reporting. Year 1 is the first year of operations. Adjustments are recognized **in the accounts**.

| Date | Ending inventory at average cost | Ending inventory at LIFO |
|---|---:|---:|
| Dec 31, Year 1 | $90,000 | $55,000 |
| Dec 31, Year 2 | 105,000 | 62,000 |
| Dec 31, Year 3 | 98,000 | 70,000 |

**Required:**  
a. Compute LIFO reserve each year and Δ reserve; prepare the measurement schedule.  
b. Journal entry December 31, Year 1 (create allowance).  
c. Journal entries December 31, Year 2 and Year 3.  
d. Show Inventory on the Dec 31, Year 3 balance sheet (gross internal method, allowance, net LIFO).  
e. Compute cumulative effect on COGS over Years 1–3 from LIFO reserve entries (net Dr or Cr to COGS).

### The key's answer

**Answer key:**  

**a. Schedule**

LIFO reserve = internal (average) inventory − LIFO inventory

| Date | Avg-cost EI | LIFO EI | LIFO reserve | Δ reserve | Effect on COGS |
|---|---:|---:|---:|---:|---|
| Dec 31, Y1 | $90,000 | $55,000 | **$35,000** | +35,000 | +COGS $35,000 |
| Dec 31, Y2 | 105,000 | 62,000 | **43,000** | +8,000 | +COGS $8,000 |
| Dec 31, Y3 | 98,000 | 70,000 | **28,000** | −15,000 | −COGS $15,000 |

Checks:  
- Y1: 90,000 − 55,000 = **35,000**  
- Y2: 105,000 − 62,000 = **43,000**; Δ = 43,000 − 35,000 = **+8,000**  
- Y3: 98,000 − 70,000 = **28,000**; Δ = 28,000 − 43,000 = **−15,000**

**b. December 31, Year 1 — Create allowance**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 35,000 | |
| Allowance to Reduce Inventory to LIFO Basis | | 35,000 |
| *Initial LIFO reserve: $90,000 − $55,000* | | |

**Check:** Dr = Cr = **35,000**.

**c. Subsequent period-end adjustments**

*December 31, Year 2*

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 8,000 | |
| Allowance to Reduce Inventory to LIFO Basis | | 8,000 |
| *Δ reserve +$8,000* | | |

**Check:** Dr = Cr = **8,000**. Allowance bal. = 35,000 + 8,000 = **$43,000**.

*December 31, Year 3*

| Account | Debit | Credit |
|---|---:|---:|
| Allowance to Reduce Inventory to LIFO Basis | 15,000 | |
| Cost of Goods Sold | | 15,000 |
| *Δ reserve −$15,000* | | |

**Check:** Dr = Cr = **15,000**. Allowance bal. = 43,000 − 15,000 = **$28,000**.

**d. Balance sheet — December 31, Year 3**

| | Amount |
|---|---:|
| Inventory (at average cost) | $98,000 |
| Less: Allowance to Reduce Inventory to LIFO Basis | (28,000) |
| **Inventory, net (at LIFO)** | **$70,000** |

**e. Cumulative COGS effect (Years 1–3)**  
Net debit to COGS = 35,000 + 8,000 − 15,000 = **$28,000**  
(Equals ending LIFO reserve of $28,000 — the cumulative amount by which COGS has been increased relative to the internal method.)

**Key insight:** Regardless of whether the internal method is FIFO or average cost, the mechanics are the same: **reserve = internal EI − LIFO EI**; book **only Δ reserve** after Year 1. Ending allowance always equals the current-year reserve, and cumulative COGS charges equal the ending reserve balance.

---

### Blind solver (baseline) — figures

- `a: LIFO reserve at December 31, Year 1` = **35000**
- `a: LIFO reserve at December 31, Year 2` = **43000**
- `a: LIFO reserve at December 31, Year 3` = **28000**
- `a: change in LIFO reserve, Year 1 (increase)` = **35000**
- `a: change in LIFO reserve, Year 2 (increase)` = **8000**
- `a: change in LIFO reserve, Year 3 (decrease)` = **-15000**
- `d: Inventory at average cost (gross), December 31, Year 3` = **98000**
- `d: Less allowance to reduce inventory to LIFO basis, December 31, Year 3` = **28000**
- `d: Inventory at LIFO (net), December 31, Year 3` = **70000**
- `e: cumulative effect on Cost of Goods Sold, Years 1-3 (net debit / increase)` = **28000**

### Blind solver (trim) — figures

- `a: Year 1 — ending inventory at average cost` = **90000**
- `a: Year 1 — ending inventory at LIFO` = **55000**
- `a: Year 1 — LIFO reserve (allowance) required ending balance` = **35000**
- `a: Year 1 — allowance beginning balance` = **0**
- `a: Year 1 — change in LIFO reserve (Delta reserve; + = increase)` = **35000**
- `a: Year 2 — ending inventory at average cost` = **105000**
- `a: Year 2 — ending inventory at LIFO` = **62000**
- `a: Year 2 — LIFO reserve (allowance) required ending balance` = **43000**
- `a: Year 2 — allowance beginning balance` = **35000**
- `a: Year 2 — change in LIFO reserve (Delta reserve; + = increase)` = **8000**
- `a: Year 3 — ending inventory at average cost` = **98000**
- `a: Year 3 — ending inventory at LIFO` = **70000**
- `a: Year 3 — LIFO reserve (allowance) required ending balance` = **28000**
- `a: Year 3 — allowance beginning balance` = **43000**
- `a: Year 3 — change in LIFO reserve (Delta reserve; + = increase)` = **-15000**
- `b: Dec 31, Year 1 entry amount (Dr COGS / Cr Allowance 35000)` = **35000**
- `c: Dec 31, Year 2 entry amount (Dr COGS / Cr Allowance 8000)` = **8000**
- `c: Dec 31, Year 3 entry amount (Dr Allowance / Cr COGS 15000)` = **15000**
- `d: BS Dec 31, Year 3 — Inventory at average cost (gross, internal method)` = **98000**
- `d: BS Dec 31, Year 3 — Less: Allowance to reduce inventory to LIFO` = **28000**
- `d: BS Dec 31, Year 3 — Inventory, net (at LIFO)` = **70000**
- `e: Cumulative net effect on COGS, Years 1-3 (net DEBIT = increase in COGS)` = **28000**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 14. `agent_107#02` — chapter 19 — flip

**Machine verdict:** baseline `failed`, trim `machine_passed`  
**Required parts detected:** a, b, c, d  
**Coverage:** baseline 0.75, trim 1.0

### Question

### Q3 — CORE alternate angle — Lump-sum issuance (proportional vs incremental) and classification
**LO:** LO 19-2  
**Concept:** Lump-sum (combined) stock issuance — proportional allocation when both FVs known; incremental allocation when only one FV known; classification of allocated amounts to CS/PS and PIC; settlement of proceeds among classes  
**Scenario:**  
**Bayline Packaging Co.** completes a **combined (lump-sum) offering** on March 1, Year 1, receiving a single cash package for both common and preferred stock. Two independent cases (do not combine).

**Case A — Proportional (both fair values known)**  
Issues **2,000** shares of common stock, **$5 par**, and **1,000** shares of preferred stock, **$10 par**, for a **lump-sum cash price of $95,000**.  
At issuance, common stock sells separately at **$36** per share and preferred stock at **$28** per share.

**Case B — Incremental (only common FV known)**  
Issues **2,000** shares of common stock, **$5 par**, and **1,000** shares of preferred stock, **$10 par**, for a **lump-sum cash price of $100,000**.  
Common stock market price is **$38** per share; preferred stock has **no** reliable market price.

**Required:**  
a. **Case A:** Compute relative fair values, allocation percentages, allocated proceeds to common and preferred, and prepare the **March 1 journal entry**.  
b. **Case B:** Compute incremental allocation and prepare the **March 1 journal entry**.  
c. For Case A only, show how the **equity accounts** would be **classified/presented** immediately after issuance (paid-in capital lines).  
d. Explain in one sentence why stock issue costs (if any had been incurred on the lump-sum offering) would **not** appear as an expense.

### The key's answer

**Answer key:**  

**a. Case A — proportional allocation**

| Security | Fair value | Weight |
|---|---:|---:|
| Common (2,000 × $36) | $72,000 | 72,000 / 100,000 = **72%** |
| Preferred (1,000 × $28) | 28,000 | 28,000 / 100,000 = **28%** |
| **Total FV** | **$100,000** | **100%** |

Allocated proceeds of **$95,000**:  
Common = $95,000 × 72% = **$68,400**  
Preferred = $95,000 × 28% = **$26,600**  
Check: $68,400 + $26,600 = **$95,000**.

Common Stock (par) = 2,000 × $5 = **$10,000**  
PIC—Common = $68,400 − $10,000 = **$58,400**  
Preferred Stock (par) = 1,000 × $10 = **$10,000**  
PIC—Preferred = $26,600 − $10,000 = **$16,600**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 95,000 | |
| Common Stock (2,000 × $5) | | 10,000 |
| Paid-In Capital in Excess of Par—Common Stock | | 58,400 |
| Preferred Stock (1,000 × $10) | | 10,000 |
| Paid-In Capital in Excess of Par—Preferred Stock | | 16,600 |
| *Lump-sum issuance — proportional (relative FV) allocation* | | |

**Check:** Dr 95,000 = Cr 10,000 + 58,400 + 10,000 + 16,600 = 95,000. **Balanced.**

**b. Case B — incremental allocation**

Common allocation (known FV) = 2,000 × $38 = **$76,000**  
Preferred allocation (residual) = $100,000 − $76,000 = **$24,000**

Common Stock = 2,000 × $5 = **$10,000**  
PIC—Common = $76,000 − $10,000 = **$66,000**  
Preferred Stock = 1,000 × $10 = **$10,000**  
PIC—Preferred = $24,000 − $10,000 = **$14,000**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 100,000 | |
| Common Stock (2,000 × $5) | | 10,000 |
| Paid-In Capital in Excess of Par—Common Stock | | 66,000 |
| Preferred Stock (1,000 × $10) | | 10,000 |
| Paid-In Capital in Excess of Par—Preferred Stock | | 14,000 |
| *Lump-sum issuance — incremental allocation* | | |

**Check:** Dr 100,000 = Cr 10,000 + 66,000 + 10,000 + 14,000 = 100,000. **Balanced.**

**c. Case A — classification / presentation immediately after issuance**

| | Amount |
|---|---:|
| Preferred stock, $10 par, 1,000 shares issued and outstanding | $10,000 |
| Common stock, $5 par, 2,000 shares issued and outstanding | 10,000 |
| Additional paid-in capital (PIC—PS $16,600 + PIC—CS $58,400) | 75,000 |
| **Total paid-in capital** | **$95,000** |

(Often PIC accounts are aggregated as one “Additional paid-in capital” line on the face of the balance sheet.)

**d. Issue costs and income**  
Stock issue costs are reductions of paid-in capital (capital transactions in the entity’s own stock) and are **excluded from the determination of net income**.

**Key insight:** A lump-sum sale is a single **settlement of cash** that must be **allocated** to each class before applying the usual par/PIC split. Use **proportional** allocation when both market values are known; use **incremental** when only one class has a reliable FV.

---

### Blind solver (baseline) — figures

- `a: Case A relative fair value of common (2,000 x $36)` = **72000**
- `a: Case A relative fair value of preferred (1,000 x $28)` = **28000**
- `a: Case A total relative fair value` = **100000**
- `a: Case A allocation percentage to common (0.72 = 72%)` = **0.72**
- `a: Case A allocation percentage to preferred (0.28 = 28%)` = **0.28**
- `a: Case A proceeds allocated to common stock` = **68400**
- `a: Case A proceeds allocated to preferred stock` = **26600**
- `b: Case B proceeds allocated to common stock (2,000 x $38 known FV)` = **76000**
- `b: Case B proceeds allocated to preferred stock (remainder)` = **24000**
- `c: Preferred Stock, $10 par, 1,000 shares issued and outstanding` = **10000**
- `c: Common Stock, $5 par, 2,000 shares issued and outstanding` = **10000**
- `c: Paid-in Capital in Excess of Par - Preferred Stock` = **16600**
- `c: Paid-in Capital in Excess of Par - Common Stock` = **58400**
- `c: Total paid-in capital` = **95000**

### Blind solver (trim) — figures

- `a: Case A - fair value of common issued (2,000 sh x $36)` = **72000.0**
- `a: Case A - fair value of preferred issued (1,000 sh x $28)` = **28000.0**
- `a: Case A - total relative fair value` = **100000.0**
- `a: Case A - allocation percentage to common (%)` = **72.0**
- `a: Case A - allocation percentage to preferred (%)` = **28.0**
- `a: Case A - proceeds allocated to common stock` = **68400.0**
- `a: Case A - proceeds allocated to preferred stock` = **26600.0**
- `a: Case A - Common Stock at par (2,000 sh x $5)` = **10000.0**
- `a: Case A - Paid-in Capital in Excess of Par - Common` = **58400.0**
- `a: Case A - Preferred Stock at par (1,000 sh x $10)` = **10000.0**
- `a: Case A - Paid-in Capital in Excess of Par - Preferred` = **16600.0**
- `a: Case A - cash debited March 1` = **95000.0**
- `b: Case B - proceeds allocated to common stock (2,000 sh x $38, incremental)` = **76000.0**
- `b: Case B - residual proceeds allocated to preferred stock ($100,000 - $76,000)` = **24000.0**
- `b: Case B - Common Stock at par (2,000 sh x $5)` = **10000.0**
- `b: Case B - Paid-in Capital in Excess of Par - Common` = **66000.0**
- `b: Case B - Preferred Stock at par (1,000 sh x $10)` = **10000.0**
- `b: Case B - Paid-in Capital in Excess of Par - Preferred` = **14000.0**
- `b: Case B - cash debited March 1` = **100000.0**
- `c: Case A presentation - Preferred stock, $10 par, 1,000 shares issued and outstanding` = **10000.0**
- `c: Case A presentation - Common stock, $5 par, 2,000 shares issued and outstanding` = **10000.0**
- `c: Case A presentation - Paid-in capital in excess of par - preferred` = **16600.0**
- `c: Case A presentation - Paid-in capital in excess of par - common` = **58400.0**
- `c: Case A presentation - Total paid-in capital` = **95000.0**

### What the comparator flagged

- `SOLVER_MISMATCH` a: Case A allocation percentage to common (0.72 = 72%)
- `SOLVER_MISMATCH` a: Case A allocation percentage to preferred (0.28 = 28%)

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 15. `agent_130#00` — chapter 22 — flip

**Machine verdict:** baseline `machine_passed`, trim `failed`  
**Required parts detected:** a, b, c, d, e, f  
**Coverage:** baseline 0.833, trim 1.0

### Question

### Q1 — CORE — Full cash T-account method (direct operating section)
**LO:** LO 22-8  
**Concept:** Reconstruct all cash and noncash entries from comparative balance sheets and the income statement; complete the cash T-account; prepare the statement of cash flows (direct method for operating activities)  
**Scenario:**  
**Ridgeview Outfitters Inc.** (calendar year-end) provides the following comparative balance sheets, income statement, and additional information for the current year.

**Comparative Balance Sheets — December 31**

| Account | Prior Year | Current Year |
|---|---:|---:|
| Cash and cash equivalents | $80,000 | $55,000 |
| Restricted cash | 15,000 | 25,000 |
| Accounts receivable, net | 220,000 | 150,000 |
| Inventory | 90,000 | 240,000 |
| Equipment | 1,600,000 | 2,200,000 |
| Accumulated depreciation—equipment | (160,000) | (420,000) |
| **Total assets** | **$1,845,000** | **$2,250,000** |
| Accounts payable | $200,000 | $160,000 |
| Salaries payable | 40,000 | 20,000 |
| Bonds payable | 500,000 | 650,000 |
| Common stock, no-par | 900,000 | 1,000,000 |
| Retained earnings | 205,000 | 420,000 |
| **Total liabilities and equity** | **$1,845,000** | **$2,250,000** |

**Income Statement — Year Ended December 31, Current Year**

| | Amount |
|---|---:|
| Sales revenue | $2,400,000 |
| Cost of goods sold | (1,350,000) |
| Salary expense | (100,000) |
| Interest expense | (48,000) |
| Depreciation expense | (320,000) |
| Loss on sale of equipment | (160,000) |
| **Net income** | **$422,000** |

**Additional information (current year):**
1. Equipment with **original cost $320,000** and **accumulated depreciation $60,000** was sold for **$100,000 cash**.
2. All equipment purchases were for **cash**.
3. All dividends declared were **paid in cash** during the year.
4. Bonds and common stock changes, if any, were **cash** transactions.
5. There was no accrued interest payable at either year-end (interest expense equals cash interest paid).

**Required:**  
a. Prepare a **schedule of account changes** (increase/decrease) and compute the change in **cash + cash equivalents + restricted cash**.  
b. Reconstruct the **journal entries** (labeled a–j as in Demo 22-8 style) that explain all income statement accounts and all balance sheet account changes for the year. Every cash-impacting entry must balance.  
c. Prepare the **equipment** and **accumulated depreciation** rollforward schedules and the **retained earnings** rollforward (solve for dividends).  
d. Complete the **cash T-account** (operating / investing / financing sections) and prove it to the change in cash + restricted cash.  
e. Prepare the **statement of cash flows** for the current year using the **direct method** for operating activities.  
f. **Classification / presentation:** Why is the $160,000 loss **not** listed as a separate cash outflow on the statement prepared from the cash T-account? Where does the equipment disposal appear?

### The key's answer

**Answer key:**  

**a. Account changes and cash change**

| Account | Prior | Current | Change (↑ / ↓) |
|---|---:|---:|---:|
| Cash and cash equivalents | 80,000 | 55,000 | ↓ 25,000 |
| Restricted cash | 15,000 | 25,000 | ↑ 10,000 |
| Accounts receivable, net | 220,000 | 150,000 | ↓ 70,000 |
| Inventory | 90,000 | 240,000 | ↑ 150,000 |
| Equipment | 1,600,000 | 2,200,000 | ↑ 600,000 |
| Accumulated depreciation | 160,000 | 420,000 | ↑ 260,000 (credit balance) |
| Accounts payable | 200,000 | 160,000 | ↓ 40,000 |
| Salaries payable | 40,000 | 20,000 | ↓ 20,000 |
| Bonds payable | 500,000 | 650,000 | ↑ 150,000 |
| Common stock | 900,000 | 1,000,000 | ↑ 100,000 |
| Retained earnings | 205,000 | 420,000 | ↑ 215,000 |

Cash + cash equivalents + restricted cash:  
Beginning \(80{,}000 + 15{,}000 = \mathbf{\$95{,}000}\)  
Ending \(55{,}000 + 25{,}000 = \mathbf{\$80{,}000}\)  
**Net decrease = $15,000** (target for cash T-account).

**b. Reconstructed journal entries**

*(a) Collections from customers*  
Cash collections \(= \) sales \(+ \) decrease in AR \(= 2{,}400{,}000 + 70{,}000 = 2{,}470{,}000\)

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 2,470,000 | |
| Accounts Receivable | | 70,000 |
| Sales Revenue | | 2,400,000 |

**Check:** Dr 2,470,000 = Cr 70,000 + 2,400,000. **Balanced.**

*(b) Cost of goods sold / inventory / AP — payments to suppliers*  
Purchases \(= \) COGS \(+ \) inventory increase \(= 1{,}350{,}000 + 150{,}000 = 1{,}500{,}000\)  
Cash paid to suppliers \(= \) purchases \(+ \) AP decrease \(= 1{,}500{,}000 + 40{,}000 = 1{,}540{,}000\)

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 1,350,000 | |
| Inventory | 150,000 | |
| Accounts Payable | 40,000 | |
| Cash | | 1,540,000 |

**Check:** Dr 1,350,000 + 150,000 + 40,000 = Cr 1,540,000. **Balanced.**

*(c) Salary expense / salaries payable — payments to employees*  
Cash paid \(= \) salary expense \(+ \) decrease in salaries payable \(= 100{,}000 + 20{,}000 = 120{,}000\)

| Account | Debit | Credit |
|---|---:|---:|
| Salary Expense | 100,000 | |
| Salaries Payable | 20,000 | |
| Cash | | 120,000 |

**Check:** Dr 120,000 = Cr 120,000. **Balanced.**

*(d) Interest paid*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 48,000 | |
| Cash | | 48,000 |

**Check:** Dr = Cr = 48,000. **Balanced.**

*(e) Disposal (sale) of equipment*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 100,000 | |
| Accumulated Depreciation—Equipment | 60,000 | |
| Loss on Sale of Equipment | 160,000 | |
| Equipment | | 320,000 |

**Check:** Dr 100,000 + 60,000 + 160,000 = Cr 320,000. **Balanced.**  
Book value \(= 320{,}000 - 60{,}000 = 260{,}000\); proceeds \(100{,}000\) → loss \(160{,}000\).

*(f) Purchase of equipment (cash)*  
Net equipment increase \(600{,}000 = \) purchases \(-\) cost sold \(320{,}000\) → purchases \(= \mathbf{\$920{,}000}\)

| Account | Debit | Credit |
|---|---:|---:|
| Equipment | 920,000 | |
| Cash | | 920,000 |

**Check:** Dr = Cr = 920,000. **Balanced.**

*(g) Issuance of bonds (cash)*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 150,000 | |
| Bonds Payable | | 150,000 |

**Check:** Dr = Cr = 150,000. **Balanced.**

*(h) Issuance of common stock (cash)*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 100,000 | |
| Common Stock | | 100,000 |

**Check:** Dr = Cr = 100,000. **Balanced.**

*(i) Cash dividends*  
See RE rollforward in part (c): dividends \(= \mathbf{\$207{,}000}\)

| Account | Debit | Credit |
|---|---:|---:|
| Retained Earnings | 207,000 | |
| Cash | | 207,000 |

**Check:** Dr = Cr = 207,000. **Balanced.**

*(j) Period-end depreciation (noncash)*

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 320,000 | |
| Accumulated Depreciation—Equipment | | 320,000 |

**Check:** Dr = Cr = 320,000. **Balanced.**  
**Does not post to the cash T-account.**

**c. Subsequent measurement / rollforward schedules**

**Equipment**

| | Amount |
|---|---:|
| Beginning balance | $1,600,000 |
| Cash purchases | 920,000 |
| Cost of equipment sold | (320,000) |
| **Ending balance** | **$2,200,000** |

**Accumulated depreciation**

| | Amount |
|---|---:|
| Beginning balance | $160,000 |
| Depreciation expense (period-end) | 320,000 |
| AD removed on sale | (60,000) |
| **Ending balance** | **$420,000** |

**Retained earnings**

| | Amount |
|---|---:|
| Beginning balance | $205,000 |
| Net income | 422,000 |
| Cash dividends (plug) | (207,000) |
| **Ending balance** | **$420,000** |

**d. Cash T-account** (cash + cash equivalents + restricted cash)

| Debit (inflows) | | Credit (outflows) | |
|---|---:|---|---:|
| **Operating activities** | | **Operating activities** | |
| (a) From customers | 2,470,000 | (b) To suppliers | 1,540,000 |
| | | (c) To employees | 120,000 |
| | | (d) For interest | 48,000 |
| **Investing activities** | | **Investing activities** | |
| (e) Sale of equipment | 100,000 | (f) Purchase of equipment | 920,000 |
| **Financing activities** | | **Financing activities** | |
| (g) Issuance of bonds | 150,000 | (i) Payment of dividends | 207,000 |
| (h) Issuance of common stock | 100,000 | | |
| | | **Net decrease in cash** | **15,000** |
| **Totals** | **2,820,000** | **Totals** | **2,820,000** |

Proof of net change:  
Operating net \(= 2{,}470{,}000 - 1{,}540{,}000 - 120{,}000 - 48{,}000 = \mathbf{\$762{,}000}\) provided  
Investing net \(= 100{,}000 - 920{,}000 = \mathbf{\$(820{,}000)}\) used  
Financing net \(= 150{,}000 + 100{,}000 - 207{,}000 = \mathbf{\$43{,}000}\) provided  
\(762{,}000 - 820{,}000 + 43{,}000 = \mathbf{\$(15{,}000)}\) ✓ matches part (a).

**e. Statement of cash flows (direct method — operating)**

**Ridgeview Outfitters Inc.**  
**Statement of Cash Flows**  
**For the Year Ended December 31, Current Year**

| | Amount |
|---|---:|
| **Cash flows from operating activities** | |
| Collections from customers | $2,470,000 |
| Payments to suppliers | (1,540,000) |
| Payments to employees | (120,000) |
| In

### Blind solver (baseline) — figures

- `a: change in Cash and cash equivalents` = **-25000**
- `a: change in Restricted cash` = **10000**
- `a: change in Accounts receivable, net` = **-70000**
- `a: change in Inventory` = **150000**
- `a: change in Equipment` = **600000**
- `a: change in Accumulated depreciation—equipment (credit balance increase)` = **260000**
- `a: change in Accounts payable` = **-40000**
- `a: change in Salaries payable` = **-20000**
- `a: change in Bonds payable` = **150000**
- `a: change in Common stock, no-par` = **100000**
- `a: change in Retained earnings` = **215000**
- `a: change in cash + cash equivalents + restricted cash (decrease)` = **-15000**
- `c: Equipment purchased for cash (equipment rollforward plug)` = **920000**
- `c: Equipment, ending balance` = **2200000**
- `c: Accumulated depreciation removed on disposal` = **60000**
- `c: Accumulated depreciation, ending balance` = **420000**
- `c: Dividends declared and paid (retained earnings rollforward plug)` = **207000**
- `c: Retained earnings, ending balance` = **420000**
- `d: Cash T-account — net cash provided by operating activities` = **762000**
- `d: Cash T-account — net cash used in investing activities` = **-820000**
- `d: Cash T-account — net cash provided by financing activities` = **43000**
- `d: Cash T-account — net decrease in cash, cash equivalents and restricted cash` = **-15000**
- `e: Operating — cash collected from customers` = **2470000**
- `e: Operating — cash paid to suppliers` = **-1540000**

### Blind solver (trim) — figures

- `a: Change in Cash and cash equivalents (decrease)` = **-25000**
- `a: Change in Restricted cash (increase)` = **10000**
- `a: Change in Accounts receivable, net (decrease)` = **-70000**
- `a: Change in Inventory (increase)` = **150000**
- `a: Change in Equipment (increase)` = **600000**
- `a: Change in Accumulated depreciation-equipment (contra increase of 260,000; net asset change)` = **-260000**
- `a: Change in Accounts payable (decrease)` = **-40000**
- `a: Change in Salaries payable (decrease)` = **-20000**
- `a: Change in Bonds payable (increase)` = **150000**
- `a: Change in Common stock, no-par (increase)` = **100000**
- `a: Change in Retained earnings (increase)` = **215000**
- `a: Beginning cash + cash equivalents + restricted cash` = **95000**
- `a: Ending cash + cash equivalents + restricted cash` = **80000**
- `a: Change in cash + cash equivalents + restricted cash (decrease)` = **-15000**
- `c: Equipment rollforward - beginning balance` = **1600000**
- `c: Equipment rollforward - less original cost of equipment sold` = **-320000**
- `c: Equipment rollforward - add equipment purchased for cash (derived)` = **920000**
- `c: Equipment rollforward - ending balance` = **2200000**
- `c: Accumulated depreciation rollforward - beginning balance` = **160000**
- `c: Accumulated depreciation rollforward - add depreciation expense` = **320000**
- `c: Accumulated depreciation rollforward - less accumulated depreciation on equipment sold` = **-60000**
- `c: Accumulated depreciation rollforward - ending balance` = **420000**
- `c: Book value of equipment sold (cost 320,000 less accumulated depreciation 60,000)` = **260000**
- `c: Loss on sale of equipment (book value less 100,000 proceeds)` = **160000**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 16. `agent_303#02` — chapter 8 — key_silent_heavy

**Machine verdict:** baseline `machine_passed`, trim `failed`  
**Required parts detected:** a, b, c, d, e, f  
**Coverage:** baseline 1.0, trim 1.0

### Question

### Q3 — CORE alternate angle — Silverbrook Home Appliances: subsequent-year true-up, schedule, settlement

**LO:** LO 8-3  
**Concept:** subsequent_measurement_schedule; **period_end_adjusting_JE** (emphasis); disposal_maturity_or_settlement_JE; classification/presentation  
**Scenario:**  
**Silverbrook Home Appliances LLC** grants a 45-day return privilege. Cost of merchandise is **60%** of selling price. Silverbrook records **all actual returns during the year as if they arise from the current year** (debit Sales Returns), then adjusts Refund Liability at year-end so the **ending** balance equals estimated returns on **current-year** sales still expected next period. (This is the subsequent-period approach in Review 8-3.)

**January 1, Year 2 balances:**

| Account | Balance |
|---|---:|
| Refund Liability | **$11,500** |
| Inventory—Estimated Returns | **$6,900** |

**Year 2 activity:**

| Item | Amount |
|------|--------:|
| Credit sales | **$550,000** |
| COGS (60%) | **$330,000** |
| Actual returns (cash refunds), recorded as current-year Sales Returns | **$19,800** |
| Sales allowances on account | **$1,650** |
| Year-end estimate of returns related to Year 2 sales | **4.5%** of Year 2 credit sales |

Assume actual return rates are reasonably consistent with management’s estimates on average.

**Required:**  
(a) Record Year 2 sales and COGS.  
(b) Record actual returns (both sides) and sales allowances.  
(c) Compute the **target ending Refund Liability** and the year-end **period-end adjusting entries** for estimated returns (sales-side and cost-side) — **emphasis**.  
(d) Prepare a full **Refund Liability rollforward schedule** from beginning to ending balance. Also roll forward Inventory—Estimated Returns and confirm ending Inv—Est Returns = ending Refund Liability × 60%.  
(e) **Settlement alternate:** Suppose instead that on **January 18, Year 2**, Silverbrook identifies **$7,200** of cash returns (cost **$4,320**) as returns of Year 1 sales that had already been accrued in Refund Liability / Inventory—Estimated Returns. Record the **settlement** entries that reduce the liability and the estimated-returns asset (do **not** debit Sales Returns for this portion).  
(f) Report Net Sales for Year 2 under the main (Review 8-3) method in parts (a)–(d), and state balance-sheet presentation of the two estimated-return accounts.

### The key's answer

**Answer key:**

**(a) Year 2 sales and COGS**

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 550,000 | |
| Sales Revenue | | 550,000 |

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 330,000 | |
| Inventory | | 330,000 |

**Check:** \(550{,}000 \times 0.60 = 330{,}000\). **Balanced.**

**(b) Actual returns and allowances (main method — charge Sales Returns)**

Sales-side returns:

| Account | Debit | Credit |
|---|---:|---:|
| Sales Returns | 19,800 | |
| Cash | | 19,800 |

Cost-side: \(19{,}800 \times 0.60 = \mathbf{\$11{,}880}\)

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 11,880 | |
| Cost of Goods Sold | | 11,880 |

Allowances:

| Account | Debit | Credit |
|---|---:|---:|
| Sales Allowances | 1,650 | |
| Accounts Receivable | | 1,650 |

**Check:** All entries balance. Refund Liability is **not** reduced when actual returns are recorded under this method; the YE true-up handles it. **Balanced.**

**(c) Period-end adjusting entries — December 31, Year 2 (emphasis)**

Estimated returns on Year 2 sales = \(0.045 \times 550{,}000 = \mathbf{\$24{,}750}\).

Target ending Refund Liability (Review 8-3 identity):  
\[
\begin{align*}
\text{Ending RL} &= \text{Beg RL} - \text{Actual returns} + \text{Est. on current-year sales} \\
&= 11{,}500 - 19{,}800 + 24{,}750 = \mathbf{\$16{,}450}
\end{align*}
\]

Adjusting plug to Refund Liability = \(16{,}450 - 11{,}500 = \mathbf{+\$4{,}950}\)  
(equivalently: \(24{,}750 - 19{,}800 = 4{,}950\)).

| Account | Debit | Credit |
|---|---:|---:|
| Sales Returns | 4,950 | |
| Refund Liability | | 4,950 |
| *YE true-up: set RL to remaining expected returns on Y2 sales* | | |

Cost-side plug: \(4{,}950 \times 0.60 = \mathbf{\$2{,}970}\)

| Account | Debit | Credit |
|---|---:|---:|
| Inventory—Estimated Returns | 2,970 | |
| Cost of Goods Sold | | 2,970 |
| *YE true-up of estimated-returns inventory* | | |

**Check:** Dr = Cr. Total Year 2 Sales Returns (main method) = \(19{,}800 + 4{,}950 = 24{,}750\) (= estimate on current-year sales).  
If the plug had been negative (actual returns > estimate on current sales), debit Refund Liability and credit Sales Returns (as can occur in Review 8-3). **Balanced.**

**(d) Subsequent measurement schedules**

**Refund Liability rollforward — Year 2**

| Date / component | Debit (decrease) | Credit (increase) | Balance |
|---|---:|---:|---:|
| Jan 1, Year 2 beginning | | | 11,500 |
| Actual returns (not charged to RL under main method) | — | — | 11,500 |
| Dec 31 YE true-up (est. on Y2 sales − actual) | | 4,950 | **16,450** |
| **Memo reconciling identity** | Actual 19,800 | Est. on Y2 sales 24,750 | Beg 11,500 − 19,800 + 24,750 = **16,450** |

**Inventory—Estimated Returns rollforward — Year 2**

| Component | Amount |
|---|---:|
| Beginning Inventory—Estimated Returns | $6,900 |
| + YE cost-side true-up | 2,970 |
| **Ending Inventory—Estimated Returns** | **$9,870** |

Confirm: ending Refund Liability × cost % = \(16{,}450 \times 0.60 = \mathbf{\$9{,}870}\). ✓

**(e) Settlement of prior-period estimate (alternate recording of returns of Year 1 sales)**

When a return is explicitly identified with amounts already accrued:

| Account | Debit | Credit |
|---|---:|---:|
| Refund Liability | 7,200 | |
| Cash | | 7,200 |
| *Settle accrued refund obligation for prior-year sales* | | |

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 4,320 | |
| Inventory—Estimated Returns | | 4,320 |
| *Reclassify estimated-returns asset to physical inventory recovered* | | |

**Check:** Dr = Cr on each entry. **Sales Returns is not debited** for this settlement—doing so would double-count the reduction already recognized when the estimate was accrued. After settlement, Refund Liability would be \(11{,}500 - 7{,}200 = 4{,}300\) before any further Year 2 true-up; Inventory—Estimated Returns would be \(6{,}900 - 4{,}320 = 2{,}580\). **Balanced.**

**(f) Net Sales (main method) and presentation**

| | Amount |
|---|---:|
| Sales Revenue | $550,000 |
| − Sales Returns (\(19{,}800 + 4{,}950\)) | (24,750) |
| − Sales Allowances | (1,650) |
| **Net Sales** | **$523,600** |

**Classification / presentation**  
- **Refund Liability $16,450** — current liability (refund obligation for consideration the entity does not expect to be entitled to).  
- **Inventory—Estimated Returns $9,870** — current asset (inventory expected to be recovered).

**Key insight:** In a subsequent year, the **period-end true-up** does not merely “add remaining returns”—it forces the Refund Liability ending balance to equal **estimated returns still outstanding on current-year sales** (beg − actual charged to current period + estimate on current sales). Settlement of prior accruals debits the **liability**, not Sales Returns.

---

### Blind solver (baseline) — figures

- `c: target ending Refund Liability at December 31, Year 2` = **16450**
- `d: Refund Liability rollforward — beginning balance (Jan 1, Year 2)` = **11500**
- `d: Refund Liability rollforward — less actual returns taken during Year 2` = **19800**
- `d: Refund Liability rollforward — add estimated returns on Year 2 sales` = **24750**
- `d: Refund Liability rollforward — ending balance (Dec 31, Year 2)` = **16450**
- `d: Inventory—Estimated Returns rollforward — beginning balance (Jan 1, Year 2)` = **6900**
- `d: Inventory—Estimated Returns rollforward — less cost of actual returns` = **11880**
- `d: Inventory—Estimated Returns rollforward — add cost of estimated returns` = **14850**
- `d: Inventory—Estimated Returns rollforward — ending balance (Dec 31, Year 2)` = **9870**
- `f: Net Sales for Year 2` = **523600**

### Blind solver (trim) — figures

- `a: Accounts receivable debited for Year 2 credit sales` = **550000.0**
- `a: Sales revenue credited` = **550000.0**
- `a: Cost of goods sold recorded (60% of sales)` = **330000.0**
- `a: Inventory credited for cost of sales` = **330000.0**
- `b: Sales Returns debited for actual cash refunds` = **19800.0**
- `b: Cash credited for actual refunds` = **19800.0**
- `b: Inventory restored on actual returns (60% of $19,800)` = **11880.0**
- `b: Cost of goods sold credited on actual returns` = **11880.0**
- `b: Sales allowances on account` = **1650.0**
- `c: Target ending Refund Liability (4.5% x $550,000)` = **24750.0**
- `c: Beginning Refund Liability` = **11500.0**
- `c: Year-end adjusting entry - Sales Returns debit / Refund Liability credit (increase)` = **13250.0**
- `c: Target ending Inventory-Estimated Returns (60% of target liability)` = **14850.0**
- `c: Year-end adjusting entry - Inventory-Estimated Returns debit / COGS credit (increase)` = **7950.0**
- `d: Refund Liability rollforward - beginning balance Jan 1, Yr 2` = **11500.0**
- `d: Refund Liability rollforward - actual returns charged against the liability` = **0.0**
- `d: Refund Liability rollforward - year-end adjustment (true-up)` = **13250.0**
- `d: Refund Liability rollforward - ending balance Dec 31, Yr 2` = **24750.0**
- `d: Inventory-Estimated Returns rollforward - beginning balance Jan 1, Yr 2` = **6900.0**
- `d: Inventory-Estimated Returns rollforward - amounts relieved for actual returns` = **0.0**
- `d: Inventory-Estimated Returns rollforward - year-end adjustment (true-up)` = **7950.0**
- `d: Inventory-Estimated Returns rollforward - ending balance Dec 31, Yr 2` = **14850.0**
- `d: Confirmation - ending Refund Liability x 60%` = **14850.0**
- `d: Confirmation - ending Inv-Est Returns equals liability x 60% (1 = yes)` = **1**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 17. `agent_333#02` — chapter 11 — key_silent_heavy

**Machine verdict:** baseline `failed`, trim `failed`  
**Required parts detected:** a, b, c, d, e, f  
**Coverage:** baseline 1.0, trim 1.0

### Question

### Q3 — CORE alternate angle — Life extension (reduction of accum. dep. vs capitalization); no advance accrual; machine replacement with disposal-date dep. update

**LO:** LO 11-6  
**Concept:** **Period-end adjusting JE emphasis** after life-extending electrical upgrade (reduction of accumulated depreciation method vs capitalization alternative); prohibition on accruing planned major maintenance; equipment substitution with partial-period dep. update through disposal date  
**Scenario:**  
**Northline Processors Corp.** (calendar year-end) has the following PPE at **January 1, 20X7**:

**Building**

| Item | Amount |
|---|---:|
| Cost | $2,400,000 |
| Accumulated depreciation | 960,000 |
| Book value | 1,440,000 |
| Remaining useful life | 12 years |
| Residual | $0 |
| Pre-change annual depreciation | $120,000 |

**Production machine (separate asset)**

| Item | Amount |
|---|---:|
| Cost | $84,000 |
| Accumulated depreciation | 60,000 |
| Book value | 24,000 |
| Remaining useful life | 2 years |
| Residual | $0 |
| Annual depreciation | $12,000 |

Events in **20X7**:

1. In **January**, management budgets **$180,000** for a planned major maintenance overhaul of the building in August.  
2. **August 1** — Completes an **electrical system modernization** that **extends the useful life of the building by 4 years**. Cost **$192,000** cash. Old electrical component costs are **not** separately tracked. Improved quality is **not** the primary result (life extension is). Northline uses the **reduction of accumulated depreciation** method.  
   - *Simplifying assumption for annual reporting:* after recording the August 1 expenditure, Northline computes **full-year** revised building depreciation for 20X7 based on post-expenditure book value and the new remaining life (12 + 4 = **16 years**).  
3. **August 1** — Replaces the production machine:  
   - Update depreciation on the old machine through August 1 (7/12 of annual).  
   - Sell the old machine for **$2,000** cash.  
   - Purchase a new machine for **$96,000** cash; residual **$0**; useful life **8 years**.  
4. **December 31** — Record period-end depreciation on the building and on the new machine.

**Required:**  
(a) Is any journal entry required in January (or before the overhaul begins) for the **planned major maintenance** budget? Explain.  
(b) Record the **August 1** entry for the electrical modernization under the **reduction of accumulated depreciation** method. Compute **revised full-year 20X7 building depreciation** and the **December 31 period-end adjusting JE** for the building.  
(c) **Alternative presentation:** if Northline instead used the **capitalization** method for the electrical upgrade, prepare that August 1 entry and show that **20X7 depreciation expense is the same** (same post-expenditure BV and life). Contrast balance-sheet presentation (gross cost vs accum. dep.).  
(d) Record all **August 1 machine** entries: update dep. through disposal, dispose of old machine, capitalize new machine.  
(e) Record the **December 31 period-end adjusting JE** for depreciation of the **new machine**. Prepare a brief subsequent measurement snapshot of the new machine at Dec. 31, 20X7.  
(f) Prepare a **building subsequent measurement schedule** for 20X7 under the reduction-of-accum.-dep. method (from Jan. 1 through Dec. 31 after period-end dep.).

### The key's answer

**Answer key:**

**(a) Planned major maintenance — no advance accrual**

**No journal entry** in January (and none to accrue before the work is performed).  
Under ASC 360-10-25-5, the **accrue-in-advance method** for planned major maintenance is **prohibited**. Before the maintenance activity is initiated, the company has **no present obligation**. Costs are recognized when incurred (and classified as ordinary repair expense or capital improvement based on LO 11-6 criteria).

**(b) Electrical modernization — reduction of accumulated depreciation + period-end building dep.**

*August 1 — Reduction of accum. dep. (life extension; old costs unknown)*

| Account | Debit | Credit |
|---|---:|---:|
| Accumulated Depreciation—Building | 192,000 | |
| Cash | | 192,000 |
| *Life-extending electrical upgrade: reduce accum. dep. (BV increases by $192,000)* | | |

**Check:** Dr 192,000 = Cr 192,000. **Balanced.**

Post-expenditure book value = \(1{,}440{,}000 + 192{,}000 =\) **$1,632,000**  
New remaining life = \(12 + 4 =\) **16 years**  
Revised full-year 20X7 building depreciation = \(1{,}632{,}000 / 16 =\) **$102,000**

*December 31, 20X7 — period-end adjusting JE (building) — emphasis*

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense—Building | 102,000 | |
| Accumulated Depreciation—Building | | 102,000 |
| *Revised SL dep. after life-extending subsequent cost* | | |

**Check:** Dr 102,000 = Cr 102,000. **Balanced.**

**(c) Capitalization method alternative (same economic dep.)**

*August 1 — Capitalization method*

| Account | Debit | Credit |
|---|---:|---:|
| Building | 192,000 | |
| Cash | | 192,000 |

**Check:** Dr 192,000 = Cr 192,000. **Balanced.**

Post-expenditure BV = \(2{,}400{,}000 + 192{,}000 - 960{,}000 =\) **$1,632,000** (same)  
Life **16 years** → depreciation **$102,000** (same expense).

| Presentation at Aug. 1 (before YE dep.) | Reduction of accum. dep. | Capitalization |
|---|---:|---:|
| Building (gross) | $2,400,000 | $2,592,000 |
| Accumulated depreciation | 768,000 | 960,000 |
| Book value | **$1,632,000** | **$1,632,000** |

*(Accum under reduction method: \(960{,}000 - 192{,}000 = 768{,}000\).)*

**(d) Machine: update dep., dispose, capitalize replacement**

*August 1 — Update depreciation through disposal date (7/12)*

Depreciation = \(12{,}000 \times 7/12 =\) **$7,000**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense—Machine | 7,000 | |
| Accumulated Depreciation—Machine | | 7,000 |
| *Partial-period adjusting JE through disposal date* | | |

**Check:** Dr 7,000 = Cr 7,000. **Balanced.**  
Updated accum. dep. = \(60{,}000 + 7{,}000 =\) **$67,000**; updated BV = \(84{,}000 - 67{,}000 =\) **$17,000**.

*August 1 — Dispose of old machine for $2,000 cash*

Loss = \(17{,}000 - 2{,}000 =\) **$15,000**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 2,000 | |
| Accumulated Depreciation—Machine | 67,000 | |
| Loss on Disposal of Machine | 15,000 | |
| Machine | | 84,000 |
| *Remove old machine (substitution / replacement path)* | | |

**Check:** Dr \(2{,}000 + 67{,}000 + 15{,}000 = 84{,}000\) = Cr 84,000. **Balanced.**

*August 1 — Capitalize new machine (initial recognition)*

| Account | Debit | Credit |
|---|---:|---:|
| Machine | 96,000 | |
| Cash | | 96,000 |
| *Acquire replacement machine* | | |

**Check:** Dr 96,000 = Cr 96,000. **Balanced.**

**(e) Period-end dep. on new machine (5/12 of year)**

Annual = \(96{,}000 / 8 =\) $12,000; 20X7 = \(12{,}000 \times 5/12 =\) **$5,000**

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense—Machine | 5,000 | |
| Accumulated Depreciation—Machine | | 5,000 |
| *Period-end dep. on new machine (Aug. 1–Dec. 31)* | | |

**Check:** Dr 5,000 = Cr 5,000. **Balanced.**

| New machine at Dec. 31, 20X7 | Amount |
|---|---:|
| Cost | $96,000 |
| Accumulated depreciation | 5,000 |
| Book value | **$91,000** |

**(f) Building subsequent measurement schedule — reduction of accum. dep. method (20X7)**

| | Building (gross) | Accum. depreciation | Book value |
|---|---:|---:|---:|
| Jan. 1, 20X7 | $2,400,000 | $960,000 | $1,440,000 |
| Aug. 1 reduce accum. dep. (electrical) | — | (192,000) | 192,000 |
| Subtotal before YE dep. | 2,400,000 | 768,000 | 1,632,000 |
| Dec. 31 period-end dep. | — | 102,000 | (102,000) |
| **Dec. 31, 20X7** | **$2,400,000** | **$870,000** | **$1,530,000** |

**Checks:** Accum \(768{,}000 + 102{,}000 = 870{,}000\); BV \(2{,}400{,}000 - 870{,}000 = 1{,}530{,}000\); also \(1{,}632{,}000 - 102{,}000 = 1{,}530{,}000\).

**Key insight:** Life-extending subsequent costs with **unknown** old component costs are often recorded by **reducing accumulated depreciation** (or by capitalizing to the asset). Both methods raise book value by the expenditure and yield the **same** future depreciation if residual is zero and life is revised identically—presentation of gross cost vs. accum. dep. differs. **Planned** major maintenance is **not** accrued in advance. Replacing a separately tracked asset still requires a **partial-period adjusting JE** through the disposal date, then a balanced disposal JE, then capitalization and period-end dep. on the new asset.

---

### Blind solver (baseline) — figures

- `a: journal entries required in January for the planned major maintenance budget (count; accrue-in-advance prohibited)` = **0**
- `a: amount recorded in January for the $180,000 planned overhaul` = **0**
- `b: building book value immediately after the Aug 1 expenditure (reduction of accum. dep. method)` = **1632000**
- `b: revised full-year 20X7 building depreciation expense` = **102000**
- `c: 20X7 building depreciation expense under the capitalization method (same as reduction method)` = **102000**
- `c: building gross cost at Dec 31, 20X7 under capitalization` = **2592000**
- `c: building accumulated depreciation at Dec 31, 20X7 under capitalization` = **1062000**
- `c: building carrying amount at Dec 31, 20X7 under capitalization` = **1530000**
- `e: new machine cost at Dec 31, 20X7` = **96000**
- `e: new machine accumulated depreciation at Dec 31, 20X7` = **5000**
- `e: new machine carrying amount at Dec 31, 20X7` = **91000**
- `f: building cost at Jan 1, 20X7` = **2400000**
- `f: building accumulated depreciation at Jan 1, 20X7` = **960000**
- `f: building carrying amount at Jan 1, 20X7` = **1440000**
- `f: reduction of accumulated depreciation, Aug 1, 20X7` = **192000**
- `f: building accumulated depreciation after Aug 1, 20X7` = **768000**
- `f: building carrying amount after Aug 1, 20X7` = **1632000**
- `f: 20X7 building depreciation expense recorded Dec 31` = **102000**
- `f: building cost at Dec 31, 20X7 (unchanged under reduction method)` = **2400000**
- `f: building accumulated depreciation at Dec 31, 20X7` = **870000**
- `f: building carrying amount at Dec 31, 20X7` = **1530000**

### Blind solver (trim) — figures

- `a: Journal entry required in January (or before overhaul begins) for the $180,000 planned major maintenance budget — none; planned future maintenance is not a present obligation and may not be accrued in advance; the cost is recorded only when incurred. Amount recorded in January ($)` = **0**
- `b: Building accumulated depreciation immediately after Aug 1 reduction ($)` = **768000**
- `b: Building book value immediately after Aug 1 expenditure ($)` = **1632000**
- `b: New remaining useful life of building (years)` = **16**
- `b: Revised full-year 20X7 building depreciation ($)` = **102000**
- `c: Building gross cost after Aug 1 under capitalization method ($)` = **2592000**
- `c: Building book value immediately after Aug 1 under capitalization method ($)` = **1632000**
- `c: 20X7 building depreciation expense under capitalization method ($)` = **102000**
- `c: Difference in 20X7 depreciation expense, capitalization vs reduction of accumulated depreciation ($)` = **0**
- `c: Dec 31, 20X7 balance-sheet gross cost — reduction method ($)` = **2400000**
- `c: Dec 31, 20X7 balance-sheet gross cost — capitalization method ($)` = **2592000**
- `c: Dec 31, 20X7 accumulated depreciation — reduction method ($)` = **870000**
- `c: Dec 31, 20X7 accumulated depreciation — capitalization method ($)` = **1062000**
- `c: Dec 31, 20X7 building carrying amount — reduction method ($)` = **1530000**
- `c: Dec 31, 20X7 building carrying amount — capitalization method ($)` = **1530000**
- `c: Difference in Dec 31, 20X7 carrying amount between the two methods ($)` = **0**
- `c: Presentation contrast — gross cost is higher under capitalization by ($)` = **192000**
- `c: Presentation contrast — accumulated depreciation is higher under capitalization by ($)` = **192000**
- `d: Old machine depreciation update through Aug 1 (7/12 of $12000 annual) ($)` = **7000**
- `d: Old machine accumulated depreciation at Aug 1 disposal date ($)` = **67000**
- `d: Old machine book value at Aug 1 disposal date ($)` = **17000**
- `d: Proceeds on sale of old machine ($)` = **2000**
- `d: Loss on disposal of old machine ($)` = **15000**
- `d: Cost capitalized for new machine ($)` = **96000**

### What the comparator flagged

- `SOLVER_MISMATCH` a: journal entries required in January for the planned major maintenance budget (count; accrue-in-advance prohibited)
- `SOLVER_MISMATCH` a: amount recorded in January for the $180,000 planned overhaul

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 18. `agent_268#00` — chapter 14 — key_silent_heavy

**Machine verdict:** baseline `failed`, trim `failed`  
**Required parts detected:** a, b, c, d, e  
**Coverage:** baseline 1.0, trim 1.0

### Question

### Q1 — CORE — Equity method with basis difference: initial recognition, period-end adjusting JEs, and investment schedule (emphasis)
**LO:** LO 14-5  
**Concept:** Period-end equity-method adjusting entries (share of NI, excess depreciation on basis difference, dividends as return of investment) and investment account rollforward  
**Scenario:**  
**Cascade Harbor Holdings** (calendar-year) acquires a long-term equity interest in **Meridian Forge Co.** on **January 1, Year 1**. Cascade can exercise **significant influence** and applies the **equity method**.

| Fact | Amount / term |
|---|---|
| Cash purchase price (Jan 1, Year 1) | **$240,000** |
| Ownership interest | **30%** of Meridian’s voting common stock |
| Meridian stockholders’ equity (book value of net assets) at acquisition | **$700,000** |
| Fair value of Meridian’s net assets exceeds book value solely due to undervalued **equipment** | Equipment undervalued by **$40,000** total on Meridian’s books |
| Remaining useful life of the undervalued equipment | **8 years**, straight-line, no residual |
| Remainder of Cascade’s cost over share of fair value of net assets | Attributable to **goodwill** (not amortized) |
| Meridian net income for Year 1 | **$80,000** |
| Meridian cash dividends declared and paid Dec 31, Year 1 | **$20,000** |
| Fair value of Cascade’s 30% interest at Dec 31, Year 1 | **$255,000** |

**Required:**  
a. Record the **January 1, Year 1 initial recognition** journal entry. Briefly support why the equity method applies.  
b. Allocate the **$240,000** cost among share of book value, depreciable basis difference, and goodwill.  
c. Record all **December 31, Year 1 period-end adjusting** journal entries under the equity method (share of NI, excess depreciation, dividends). State whether any fair-value adjustment is recorded.  
d. Prepare the **subsequent measurement (Investment) schedule** for Year 1 and compute the Dec 31 carrying amount.  
e. Compute **net equity-method income** recognized in Year 1 (investment income after excess depreciation).

### The key's answer

**Answer key:**  

**a. Initial recognition**

*January 1, Year 1 — Purchase equity-method investment*

| Account | Debit | Credit |
|---|---:|---:|
| Investment in Meridian Forge Stock | 240,000 | |
| Cash | | 240,000 |
| *Acquisition at cost; significant influence → equity method* | | |

**Check:** Dr 240,000 = Cr 240,000. **Balanced.**

**Why equity method:** 30% voting interest is within the 20%–50% range that **presumes significant influence** (rebuttable). Cascade does not control Meridian (would require consolidation), so equity method is the core measurement model.

**b. Cost allocation**

| Component | Computation | Amount |
|---|---|---:|
| Share of Meridian book value (stockholders’ equity) | \(0.30 \times \$700{,}000\) | **210,000** |
| Share of equipment undervaluation (depreciable basis difference) | \(0.30 \times \$40{,}000\) | **12,000** |
| Goodwill (plug) | \(240{,}000 - 210{,}000 - 12{,}000\) | **18,000** |
| **Total cost** | | **240,000** |

**Annual excess depreciation (equipment only):** \( \$12{,}000 \div 8 = \mathbf{\$1{,}500}\) per year.  
Goodwill: **not amortized**.

**c. Period-end adjusting JEs (emphasis)**

*December 31, Year 1 — Share of investee net income*

| Account | Debit | Credit |
|---|---:|---:|
| Investment in Meridian Forge Stock | 24,000 | |
| Investment Income | | 24,000 |
| *\(0.30 \times \$80{,}000\)* | | |

**Check:** Dr 24,000 = Cr 24,000. **Balanced.**

*December 31, Year 1 — Excess depreciation on depreciable basis difference*

| Account | Debit | Credit |
|---|---:|---:|
| Investment Income | 1,500 | |
| Investment in Meridian Forge Stock | | 1,500 |
| *\( \$12{,}000 \div 8 \)* | | |

**Check:** Dr 1,500 = Cr 1,500. **Balanced.**

*December 31, Year 1 — Investor’s share of dividends (return of investment, not revenue)*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 6,000 | |
| Investment in Meridian Forge Stock | | 6,000 |
| *\(0.30 \times \$20{,}000\)* | | |

**Check:** Dr 6,000 = Cr 6,000. **Balanced.**

**Fair value at Dec 31 ($255,000):** **No entry.** Under the equity method, unrealized changes in fair value are ignored (contrast with FV-NI).

**d. Subsequent measurement schedule — Investment in Meridian Forge**

| Item | Amount |
|---|---:|
| January 1, Year 1 cost | 240,000 |
| + Share of Meridian NI | 24,000 |
| − Excess depreciation (equipment basis difference) | (1,500) |
| − Share of dividends | (6,000) |
| **December 31, Year 1 carrying amount** | **256,500** |

**Roll-forward check:** \(240{,}000 + 24{,}000 - 1{,}500 - 6{,}000 = \mathbf{\$256{,}500}\). ✓  
(Note: market value $255,000 is **not** the carrying amount.)

**e. Net equity-method income (Year 1)**  
\( \$24{,}000 - \$1{,}500 = \mathbf{\$22{,}500} \).

**Key insight:** Period-end equity-method adjusting entries **increase** the investment for the investor’s share of earnings and **decrease** it for excess depreciation on depreciable FV–BV differences and for dividends. Dividends are **not** dividend revenue when significant influence exists. Fair value is ignored unless impaired.

---

### Blind solver (baseline) — figures

- `b: share of book value of net assets acquired (30% x $700,000)` = **210000**
- `b: depreciable basis difference — undervalued equipment (30% x $40,000)` = **12000**
- `b: goodwill (not amortized)` = **18000**
- `c: fair-value adjustment recorded at Dec 31, Year 1 (equity method — none)` = **0**
- `d: investment schedule — cost at Jan 1, Year 1` = **240000**
- `d: investment schedule — add share of investee net income` = **24000**
- `d: investment schedule — less excess depreciation on basis difference` = **-1500**
- `d: investment schedule — less dividends received` = **-6000**
- `d: Investment in Meridian Forge Co. carrying amount, Dec 31, Year 1` = **256500**
- `e: net equity-method income recognized in Year 1 (after excess depreciation)` = **22500**

### Blind solver (trim) — figures

- `a: Initial recognition — Dr Investment in Meridian Forge Co. (cash cost, Jan 1 Year 1)` = **240000.0**
- `a: Initial recognition — Cr Cash` = **240000.0**
- `b: Share of book value of net assets acquired (30% x $700,000)` = **210000.0**
- `b: Basis difference allocated to undervalued equipment (30% x $40,000)` = **12000.0**
- `b: Goodwill (residual, not amortized)` = **18000.0**
- `b: Total cost allocated (share of FV of net assets $222,000 + goodwill)` = **240000.0**
- `c: Share of investee net income recognized (30% x $80,000)` = **24000.0**
- `c: Excess depreciation on equipment basis difference ($12,000 / 8 yrs)` = **1500.0**
- `c: Dividends received — return of investment (30% x $20,000)` = **6000.0**
- `c: Fair-value adjustment recorded at Dec 31 (none under the equity method)` = **0.0**
- `d: Investment schedule — beginning balance / cost, Jan 1 Year 1` = **240000.0**
- `d: Investment schedule — add share of net income` = **24000.0**
- `d: Investment schedule — running balance after share of net income` = **264000.0**
- `d: Investment schedule — less excess depreciation` = **1500.0**
- `d: Investment schedule — running balance after excess depreciation` = **262500.0**
- `d: Investment schedule — less dividends received` = **6000.0**
- `d: Investment carrying amount, Dec 31 Year 1` = **256500.0**
- `e: Net equity-method income recognized in Year 1 ($24,000 - $1,500)` = **22500.0**

### What the comparator flagged

- `SOLVER_MISMATCH` c: fair-value adjustment recorded at Dec 31, Year 1 (equity method — none)

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 19. `agent_204#02` — chapter 11 — key_silent_heavy

**Machine verdict:** baseline `machine_passed`, trim `failed`  
**Required parts detected:** a, b, c, d  
**Coverage:** baseline 1.0, trim 1.0

### Question

### Q3 — CORE alternate angle — equipment donation mid-year; partial-year schedule; scrap disposal
**LO:** LO 11-8  
**Concept:** Contributed equipment at FV; partial-year depreciation schedule; period-end adjusting JEs; disposal at scrap value  
**Scenario:**  
On **April 1, Year 1**, a nonprofit foundation unconditionally donated specialized packaging equipment to **Cedar Ridge Bottling LLC**. Reliable fair value of the equipment is **$180,000**. Cedar Ridge paid **$3,000 cash** for legal title transfer. The foundation received nothing of equivalent value.  

Equipment: estimated life **6 years**, residual value **$12,000**, **straight-line**, calendar year-end. Depreciation is taken for the **fraction of the year held**.  

On **December 31, Year 3**, after recording Year 3 depreciation, Cedar Ridge **scrapped** the equipment and received **$9,500 cash** from a salvage dealer.

**Required:**  
a. Record the April 1, Year 1 contribution JE.  
b. Prepare a **subsequent measurement schedule** for Years 1–3 showing annual depreciation expense, year-end accum. dep., and year-end NBV (use months held for Year 1).  
c. Record the **December 31, Year 1** and **December 31, Year 2** period-end depreciation adjusting entries.  
d. Record the **December 31, Year 3** depreciation adjusting entry and the **scrap disposal** entry (two entries).

### The key's answer

**Answer key:**  

**a. April 1, Year 1 — initial recognition**  

Contribution revenue = \(180{,}000 - 3{,}000 = 177{,}000\)

| Account | Debit | Credit |
|---|---:|---:|
| Equipment | 180,000 | |
| Cash | | 3,000 |
| Contribution Revenue | | 177,000 |
| *Unconditional contribution of equipment at FV* | | |

**Check:** Dr 180,000 = Cr \(3{,}000 + 177{,}000\). Balanced.

**b. Subsequent measurement schedule (Years 1–3)**  

Full-year depreciation = \((180{,}000 - 12{,}000) / 6 = 168{,}000 / 6 = 28{,}000\)  
Year 1 (Apr 1–Dec 31 = 9 months): \(28{,}000 \times 9/12 = 21{,}000\)  
Years 2 and 3: full \(28{,}000\) each

| Year | Months | Dep. expense | Accum. dep. (EOY) | NBV (EOY) |
|-----:|-------:|-------------:|------------------:|----------:|
| 1 | 9 | **$21,000** | $21,000 | **$159,000** |
| 2 | 12 | **28,000** | 49,000 | **131,000** |
| 3 | 12 | **28,000** | **77,000** | **$103,000** |

Checks:  
- Total months by end of Y3: \(9 + 12 + 12 = 33\); \(28{,}000 \times 33/12 = 77{,}000\)  
- NBV: \(180{,}000 - 77{,}000 = 103{,}000\)

**c. Period-end adjusting JEs**  

December 31, Year 1:

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 21,000 | |
| Accumulated Depreciation—Equipment | | 21,000 |

December 31, Year 2:

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 28,000 | |
| Accumulated Depreciation—Equipment | | 28,000 |

**Check:** Each JE balances (Dr = Cr).

**d. December 31, Year 3 — depreciation then disposal**  

Year 3 depreciation:

| Account | Debit | Credit |
|---|---:|---:|
| Depreciation Expense | 28,000 | |
| Accumulated Depreciation—Equipment | | 28,000 |

**Check:** Dr = Cr = 28,000.

Disposal (scrap): cash $9,500; NBV $103,000 → **loss $93,500**.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 9,500 | |
| Accumulated Depreciation—Equipment | 77,000 | |
| Loss on Disposal of Equipment | 93,500 | |
| Equipment | | 180,000 |
| *To scrap contributed equipment and recognize loss* | | |

**Check:** Dr \(9{,}500 + 77{,}000 + 93{,}500 = 180{,}000\) = Cr 180,000. Balanced.

**Key insight:** Mid-year contributions still use **FV at receipt** for the asset and **net contribution revenue**. Subsequent measurement prorates the first year’s depreciation; disposal removes **gross cost and all accum. dep.** built on the contributed basis.

---

### Blind solver (baseline) — figures

- `b: Year 1 depreciation expense` = **21000**
- `b: Year 1 year-end accumulated depreciation` = **21000**
- `b: Year 1 year-end net book value` = **159000**
- `b: Year 2 depreciation expense` = **28000**
- `b: Year 2 year-end accumulated depreciation` = **49000**
- `b: Year 2 year-end net book value` = **131000**
- `b: Year 3 depreciation expense` = **28000**
- `b: Year 3 year-end accumulated depreciation` = **77000**
- `b: Year 3 year-end net book value` = **103000**

### Blind solver (trim) — figures

- `a: Equipment capitalized (Dr) = $180,000 FV + $3,000 title cost` = **183000**
- `a: Contribution revenue (Cr)` = **180000**
- `a: Cash paid (Cr)` = **3000**
- `b: Depreciable base (cost - residual)` = **171000**
- `b: Full-year straight-line depreciation` = **28500**
- `b: Months held in Year 1 (Apr 1 - Dec 31)` = **9**
- `b: Year 1 depreciation expense` = **21375**
- `b: Year 1 year-end accumulated depreciation` = **21375**
- `b: Year 1 year-end net book value` = **161625**
- `b: Year 2 depreciation expense` = **28500**
- `b: Year 2 year-end accumulated depreciation` = **49875**
- `b: Year 2 year-end net book value` = **133125**
- `b: Year 3 depreciation expense` = **28500**
- `b: Year 3 year-end accumulated depreciation` = **78375**
- `b: Year 3 year-end net book value` = **104625**
- `c: Dec 31, Year 1 depreciation adjusting entry amount` = **21375**
- `c: Dec 31, Year 2 depreciation adjusting entry amount` = **28500**
- `d: Dec 31, Year 3 depreciation adjusting entry amount` = **28500**
- `d: NBV immediately before scrapping` = **104625**
- `d: Cash received from salvage dealer` = **9500**
- `d: Loss on disposal (scrapping)` = **95125**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

## 20. `agent_183#01` — chapter 9 — key_silent_heavy

**Machine verdict:** baseline `machine_passed`, trim `machine_passed`  
**Required parts detected:** a, b, c, d  
**Coverage:** baseline 0.5, trim 0.75

### Question

### Q2 — CORE number variant — Harborline Tools: perpetual MA, FIFO, LIFO
**LO:** LO 9-5  
**Concept:** Number-variant twin — perpetual subsequent measurement schedules under MA, FIFO, and LIFO; purchase recognition; LIFO sale settlement JEs  
**Scenario:**  
**Harborline Tools Corp.** maintains perpetual inventory records for a portable work-light SKU. Purchases are on account (gross method). November activity:

| Date | Transaction | Units | Unit cost / SP |
|---|---|---:|---:|
| Nov 1 | Beginning inventory | 800 | $6 cost |
| Nov 4 | Purchase on account | 400 | $9 cost |
| Nov 10 | Credit sale | 600 | $15 selling price |
| Nov 15 | Purchase on account | 600 | $11 cost |
| Nov 22 | Credit sale | 450 | $16 selling price |
| Nov 28 | Purchase on account | 250 | $15 cost |

**Required:**  
(a) Compute November **ending inventory** and **COGS** under (1) **moving average**, (2) **FIFO**, and (3) **LIFO** perpetual. Show the inventory balance (unit cost or layers) after each purchase and after each sale.  
(b) Prepare **initial recognition** journal entries for the three purchases.  
(c) Prepare **sales and COGS** journal entries for Nov 10 and Nov 22 **under LIFO**.  
(d) Confirm COGAS − EI = COGS for all three methods.

### The key's answer

**Answer key:**

**COGAS**  
BI \(800\times\$6=\$4{,}800\); purchases \(400\times\$9 + 600\times\$11 + 250\times\$15 = \$3{,}600 + \$6{,}600 + \$3{,}750 = \$13{,}950\)  
**COGAS = \$18{,}750**  
Units available \(800+400+600+250=2{,}050\); sold \(600+450=1{,}050\); **EI units = 1,000**.

**(a1) Moving average**

| Date | Event | Inventory balance / COGS |
|---|---|---|
| Nov 1 | BI | 800 × $6 = $4,800 |
| Nov 4 | +400 @ $9 | 1,200 × **$7.00** = $8,400 *(4,800+3,600)/1,200* |
| Nov 10 | Sale 600 @ $7.00 | COGS **$4,200**; bal 600 × $7 = $4,200 |
| Nov 15 | +600 @ $11 | 1,200 × **$9.00** = $10,800 *(4,200+6,600)/1,200* |
| Nov 22 | Sale 450 @ $9.00 | COGS **$4,050**; bal 750 × $9 = $6,750 |
| Nov 28 | +250 @ $15 | 1,000 × **$10.50** = **$10,500** *(6,750+3,750)/1,000* |

**MA: EI = \$10,500; COGS = \$4,200 + \$4,050 = \$8,250**

**(a2) FIFO perpetual**

| Date | COGS layers | Ending layers |
|---|---|---|
| Nov 1 | | 800 @ $6 |
| Nov 4 | | 800 @ $6; 400 @ $9 |
| Nov 10 | 600 @ $6 = **$3,600** | 200 @ $6; 400 @ $9 = $4,800 |
| Nov 15 | | 200 @ $6; 400 @ $9; 600 @ $11 |
| Nov 22 | 200 @ $6 + 250 @ $9 = **$3,450** | 150 @ $9; 600 @ $11 = $7,950 |
| Nov 28 | | 150 @ $9 + 600 @ $11 + 250 @ $15 |

**FIFO EI:** \(150\times\$9 + 600\times\$11 + 250\times\$15 = \$1{,}350 + \$6{,}600 + \$3{,}750 = \mathbf{\$11{,}700}\)  
**FIFO COGS:** \(\$3{,}600 + \$3{,}450 = \mathbf{\$7{,}050}\)

**(a3) LIFO perpetual**

| Date | COGS layers | Ending layers |
|---|---|---|
| Nov 1 | | 800 @ $6 |
| Nov 4 | | 800 @ $6; 400 @ $9 |
| Nov 10 | 400 @ $9 + 200 @ $6 = **$4,800** | 600 @ $6 = $3,600 |
| Nov 15 | | 600 @ $6; 600 @ $11 |
| Nov 22 | 450 @ $11 = **$4,950** | 600 @ $6; 150 @ $11 = $5,250 |
| Nov 28 | | 600 @ $6 + 150 @ $11 + 250 @ $15 |

**LIFO EI:** \(600\times\$6 + 150\times\$11 + 250\times\$15 = \$3{,}600 + \$1{,}650 + \$3{,}750 = \mathbf{\$9{,}000}\)  
**LIFO COGS:** \(\$4{,}800 + \$4{,}950 = \mathbf{\$9{,}750}\)

**(b) Initial recognition — purchases**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Nov 4 | Inventory | 3,600 | |
| | Accounts Payable | | 3,600 |
| Nov 15 | Inventory | 6,600 | |
| | Accounts Payable | | 6,600 |
| Nov 28 | Inventory | 3,750 | |
| | Accounts Payable | | 3,750 |

**Check:** Each entry balances (Dr = Cr).

**(c) Settlement under LIFO**

Nov 10 (\(600\times\$15=\$9{,}000\) revenue; LIFO COGS \$4,800):

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 9,000 | |
| Sales Revenue | | 9,000 |
| Cost of Goods Sold | 4,800 | |
| Inventory | | 4,800 |
| *LIFO layers: 400 @ $9 + 200 @ $6* | | |

Nov 22 (\(450\times\$16=\$7{,}200\) revenue; LIFO COGS \$4,950):

| Account | Debit | Credit |
|---|---:|---:|
| Accounts Receivable | 7,200 | |
| Sales Revenue | | 7,200 |
| Cost of Goods Sold | 4,950 | |
| Inventory | | 4,950 |
| *LIFO layers: 450 @ $11* | | |

**Check:** All JEs balance (Dr = Cr on each pair).

**(d) Verification**

| Method | EI | COGS | COGAS − EI |
|---|---:|---:|---:|
| Moving average | $10,500 | $8,250 | 18,750 − 10,500 = 8,250 |
| FIFO | $11,700 | $7,050 | 18,750 − 11,700 = 7,050 |
| LIFO | $9,000 | $9,750 | 18,750 − 9,000 = 9,750 |

**Key insight:** Same purchase and sale **quantities**, different cost assignments only. Purchase recognition always debits Inventory at invoice cost; the cost-flow method only changes **which cost leaves inventory** when COGS is recorded on each sale date under perpetual LIFO (or MA/FIFO).

---

### Blind solver (baseline) — figures

- `a1: ending inventory - moving average perpetual` = **10500**
- `a1: COGS - moving average perpetual` = **8250**
- `a2: ending inventory - FIFO perpetual` = **11700**
- `a2: COGS - FIFO perpetual` = **7050**
- `a3: ending inventory - LIFO perpetual` = **9000**
- `a3: COGS - LIFO perpetual` = **9750**

### Blind solver (trim) — figures

- `a1 moving average: inventory balance after Nov 1 beginning inventory (800 units)` = **4800.0**
- `a1 moving average: moving-average unit cost after Nov 1 beginning inventory` = **6.0**
- `a1 moving average: inventory balance after Nov 4 purchase (1,200 units)` = **8400.0**
- `a1 moving average: moving-average unit cost after Nov 4 purchase` = **7.0**
- `a1 moving average: COGS on Nov 10 sale (600 units @ $7.00)` = **4200.0**
- `a1 moving average: inventory balance after Nov 10 sale (600 units @ $7.00)` = **4200.0**
- `a1 moving average: inventory balance after Nov 15 purchase (1,200 units)` = **10800.0**
- `a1 moving average: moving-average unit cost after Nov 15 purchase` = **9.0**
- `a1 moving average: COGS on Nov 22 sale (450 units @ $9.00)` = **4050.0**
- `a1 moving average: inventory balance after Nov 22 sale (750 units @ $9.00)` = **6750.0**
- `a1 moving average: inventory balance after Nov 28 purchase (1,000 units)` = **10500.0**
- `a1 moving average: moving-average unit cost after Nov 28 purchase` = **10.5**
- `a1 moving average: November ending inventory (1,000 units)` = **10500.0**
- `a1 moving average: November COGS` = **8250.0**
- `a2 FIFO perpetual: inventory balance after Nov 1 beginning inventory (layers 800 @ $6)` = **4800.0**
- `a2 FIFO perpetual: inventory balance after Nov 4 purchase (layers 800 @ $6 + 400 @ $9)` = **8400.0**
- `a2 FIFO perpetual: COGS on Nov 10 sale (600 units)` = **3600.0**
- `a2 FIFO perpetual: inventory balance after Nov 10 sale (layers 200 @ $6 + 400 @ $9)` = **4800.0**
- `a2 FIFO perpetual: inventory balance after Nov 15 purchase (layers 200 @ $6 + 400 @ $9 + 600 @ $11)` = **11400.0**
- `a2 FIFO perpetual: COGS on Nov 22 sale (450 units)` = **3450.0**
- `a2 FIFO perpetual: inventory balance after Nov 22 sale (layers 150 @ $9 + 600 @ $11)` = **7950.0**
- `a2 FIFO perpetual: inventory balance after Nov 28 purchase (layers 150 @ $9 + 600 @ $11 + 250 @ $15)` = **11700.0**
- `a2 FIFO perpetual: ending layer 150 units @ $9` = **1350.0**
- `a2 FIFO perpetual: ending layer 600 units @ $11` = **6600.0**

**Your verdict:** ☐ agree with machine  ☐ machine wrong (false positive)  ☐ machine wrong (missed a real error)

**Notes:**

---

