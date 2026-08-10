# Agent 309 — CORE DEMO — LO 8-9

**Chapter:** 8  
**LO title:** Account for impairment of noncurrent receivables  
**Critical gap LO:** no  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **CECL / noncurrent note impairment (ASC 326):** estimate expected credit losses over the life of the note (historical, current, and reasonable and supportable forecasts); remote loss risk is still considered
- **Discounted cash flow method:** discount expected future principal and interest cash flows at the note’s **original effective interest rate** (not the current market rate for similar risk)
- **Impairment period-end AJE:** excess of amortized cost over PV of expected cash flows → **Dr Bad Debt Expense, Cr Allowance for Doubtful Accounts**; write off **Interest Receivable** that will not be collected when impairment is recognized
- **Period-end adjusting JEs (emphasis):** (1) contractual interest accrual before impairment, (2) impairment adjusting entry, (3) post-impairment **effective-interest** accruals each reporting date (often **Dr AFDA / Cr Interest Revenue** when no cash interest is expected)
- **Subsequent measurement schedule:** net carrying amount accretes at the original effective rate toward the expected recovery amount
- **Settlement / maturity:** cash + remaining AFDA (+ loss if shortfall) clear Note Receivable; final period interest may be combined with settlement or recorded as a separate period-end AJE first
- **Troubled debt restructure (creditor):** modification treated as continuation of the existing loan → remeasure impairment at original effective rate; capitalize forgiven accrued interest into the note when applicable

---

### Q1 — CORE — Note impairment lifecycle with period-end adjusting JEs (emphasis)
**LO:** LO 8-9  
**Concept:** Initial recognition; contractual interest collection; period-end interest accrual; DCF impairment AJE (including write-off of interest receivable); subsequent measurement schedule; post-impairment period-end interest AJEs; maturity settlement  
**Scenario:**  
**Cascade Forge Co.** is a calendar-year creditor. On **January 1, Year 1**, Cascade sold merchandise to **Riverton Tools LLC** and accepted a **three-year, 8%, $75,000** note receivable issued at face (market rate also **8%**). Annual interest of **$6,000** is due each **December 31**. Principal is due **December 31, Year 3**.

Cascade collected the **Year 1** contractual interest on schedule. At **December 31, Year 2**, Riverton fails to pay Year 2 interest. Cascade first **accrues** the contractual Year 2 interest as a period-end adjusting entry. After reviewing Riverton’s financial distress, Cascade concludes:

- The **Year 2 interest will not be collected**
- **No further interest** will be collected
- Only **$50,000** of principal will be collected, and that amount will be received on **December 31, Year 4** (one year after original maturity)

The current market rate for notes of similar risk is **14%** (do **not** use this rate for impairment measurement). Cascade uses the **discounted cash flow** method and the **effective interest method** after impairment. On **December 31, Year 4**, Cascade collects **$48,500** cash and expects no further payments.

**Required:**  
(a) Record the **January 1, Year 1** initial recognition of the note (ignore COGS).  
(b) Record the **December 31, Year 1** receipt of interest.  
(c) Record the **December 31, Year 2 period-end adjusting entry** to accrue contractual interest (before impairment).  
(d) Compute the PV of expected cash flows at December 31, Year 2, and record the **impairment period-end adjusting JE** (write off Interest Receivable and establish AFDA). Use **PV = $42,867**.  
(e) Prepare a **subsequent measurement schedule** of net carrying amount and AFDA from December 31, Year 2 (after impairment) through December 31, Year 4 **before** settlement.  
(f) Record the **December 31, Year 3** effective-interest period-end AJE.  
(g) Record the **December 31, Year 4** effective-interest period-end AJE, then the **settlement** entry (or one combined settlement entry that includes final interest).  
(h) Briefly explain why the **14%** market rate is not used.

**Answer key:**

**(a) January 1, Year 1 — Initial recognition**

| Account | Debit | Credit |
|---|---:|---:|
| Note Receivable | 75,000 | |
| Sales Revenue | | 75,000 |
| *Accept 3-year 8% note for merchandise sale* | | |

**Check:** Dr 75,000 = Cr 75,000. **Balanced.**

**(b) December 31, Year 1 — Interest receipt**

Interest = \(75{,}000 \times 0.08 = \mathbf{\$6{,}000}\).

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 6,000 | |
| Interest Revenue | | 6,000 |
| *Collect Year 1 contractual interest* | | |

**Check:** Dr 6,000 = Cr 6,000. **Balanced.**

**(c) December 31, Year 2 — Period-end adjusting JE (accrue unpaid contractual interest)**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Receivable | 6,000 | |
| Interest Revenue | | 6,000 |
| *Accrue Year 2 contractual interest (not paid)* | | |

**Check:** Dr 6,000 = Cr 6,000. **Balanced.**

Carrying amount before impairment = Note \(75{,}000\) + Interest receivable \(6{,}000\) = **$81,000**.

**(d) December 31, Year 2 — Impairment period-end adjusting JE (DCF at original 8%)**

Expected cash flow: single principal collection of **$50,000** in **2 years**; no interest.

\[
PV = \frac{50{,}000}{(1.08)^{2}} = \frac{50{,}000}{1.1664} \approx 42{,}866.94 \rightarrow \mathbf{\$42{,}867}
\]

| Item | Amount |
|---|---:|
| Amortized cost of note (face) | $75,000 |
| PV of expected cash flows @ **8%** | 42,867 |
| **Allowance for Doubtful Accounts** | **32,133** |
| Interest receivable written off | 6,000 |
| **Bad Debt Expense** (\(32{,}133 + 6{,}000\)) | **38,133** |

**Do not** discount at 14%.

| Account | Debit | Credit |
|---|---:|---:|
| Bad Debt Expense | 38,133 | |
| Interest Receivable | | 6,000 |
| Allowance for Doubtful Accounts | | 32,133 |
| *Impair note to PV of expected CF; write off uncollectible interest receivable* | | |

**Check:** Dr \(38{,}133\) = Cr \(6{,}000 + 32{,}133\). **Balanced.**

Net note receivable reported = **$42,867** (\(75{,}000 - 32{,}133\)).

**(e) Subsequent measurement schedule — net CA & AFDA**

Interest each year = beginning net CA × **8%**. No cash interest after impairment; accretion reduces AFDA.

| Date | Net CA (beg) | Interest revenue (8%) | Cash interest | Net CA (end) | AFDA (end) |
|---|---:|---:|---:|---:|---:|
| Dec 31, Y2 (after impairment) | 42,867 | — | — | **42,867** | **32,133** |
| Dec 31, Y3 | 42,867 | **3,429** | 0 | **46,296** | **28,704** |
| Dec 31, Y4 (before settlement) | 46,296 | **3,704** | 0 | **50,000** | **25,000** |

**Math checks:**  
\(42{,}867 \times 0.08 = 3{,}429.36 \rightarrow \$3{,}429\); \(42{,}867 + 3{,}429 = 46{,}296\).  
Final-year interest **plugged** so terminal net equals expected principal: \(50{,}000 - 46{,}296 = \$3{,}704\) (vs. \(46{,}296 \times 0.08 = 3{,}703.68\)).  
AFDA: \(32{,}133 - 3{,}429 = 28{,}704\); \(28{,}704 - 3{,}704 = 25{,}000\).  
Gross NR \(75{,}000 -\) AFDA \(25{,}000 =\) net \(50{,}000\).

**(f) December 31, Year 3 — Effective-interest period-end AJE**

| Account | Debit | Credit |
|---|---:|---:|
| Allowance for Doubtful Accounts | 3,429 | |
| Interest Revenue | | 3,429 |
| *Y3 effective interest on net CA $42,867 × 8%* | | |

**Check:** Dr 3,429 = Cr 3,429. **Balanced.**

**(g) December 31, Year 4 — Period-end interest AJE, then settlement**

*Period-end interest AJE first:*

| Account | Debit | Credit |
|---|---:|---:|
| Allowance for Doubtful Accounts | 3,704 | |
| Interest Revenue | | 3,704 |
| *Y4 effective interest to accrete net CA to expected $50,000* | | |

**Check:** Dr 3,704 = Cr 3,704. **Balanced.**

After this entry: AFDA = **$25,000**; net CA = **$50,000**.

*Settlement (cash $48,500 vs. expected net $50,000 → shortfall loss $1,500):*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 48,500 | |
| Loss on Settlement of Note Receivable | 1,500 | |
| Allowance for Doubtful Accounts | 25,000 | |
| Note Receivable | | 75,000 |
| *Collect $48,500; clear NR and remaining AFDA; recognize shortfall* | | |

**Check:** Dr \(48{,}500 + 1{,}500 + 25{,}000 = 75{,}000\) = Cr 75,000. **Balanced.**

*Optional combined form (interest + settlement in one entry; AFDA still at pre-Y4-interest balance of $28,704):*

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 48,500 | |
| Loss on Settlement of Note Receivable | 1,500 | |
| Allowance for Doubtful Accounts | 28,704 | |
| Note Receivable | | 75,000 |
| Interest Revenue | | 3,704 |

**Check:** Dr \(48{,}500 + 1{,}500 + 28{,}704 = 78{,}704\); Cr \(75{,}000 + 3{,}704 = 78{,}704\). **Balanced.**

**(h) Rate choice**  
ASC 326 requires discounting expected cash flows at the financial asset’s **original effective interest rate**. The allowance reflects changes in **expected cash flows**, not changes in market rates or risk premiums; therefore the **14%** current market rate is not used.

**Key insight:** Period-end work is the exam spine of LO 8-9: accrue contractual interest if earned, then **adjust** for impairment (BDE / AFDA / interest receivable write-off), then each later period-end **accrete** net CA at the original effective rate—usually by debiting AFDA when cash interest is not expected.

---

### Q2 — CORE number variant — Same lifecycle, all numbers changed
**LO:** LO 8-9  
**Concept:** Number-variant twin — initial recognition, period-end interest, DCF impairment AJE, subsequent measurement schedule, period-end effective-interest accruals, settlement  
**Scenario:**  
**Harborline Merchants** (calendar year) sold inventory to **Dunecrest Packaging** on **January 1, Year 1** and accepted a **four-year, 6%, $80,000** note at face (market rate **6%**). Interest of **$4,800** is due each December 31; principal is due **December 31, Year 4**.

Harborline collected Year 1 interest. At **December 31, Year 1**, after collecting interest, Harborline expects **no further interest** and only **$54,000** of principal on the original due date (**December 31, Year 4**). The current similar-risk market rate is **12%** (ignore for discounting). On **December 31, Year 4**, Harborline collects **exactly $54,000**.

**Required:**  
(a) Initial recognition JE (Jan 1, Y1) and Year 1 interest receipt.  
(b) Impairment computation and **period-end impairment AJE** at Dec 31, Y1 (use **PV = $45,339**).  
(c) Subsequent measurement schedule of net CA and AFDA through Dec 31, Y4 before settlement.  
(d) Period-end effective-interest AJEs for Year 2 and Year 3.  
(e) Combined settlement JE at Dec 31, Y4 (include final interest accretion).

**Answer key:**

**(a) Initial recognition and Year 1 interest**

| Account | Debit | Credit |
|---|---:|---:|
| Note Receivable | 80,000 | |
| Sales Revenue | | 80,000 |

**Check:** Dr 80,000 = Cr 80,000. **Balanced.**

Interest = \(80{,}000 \times 0.06 = \mathbf{\$4{,}800}\).

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 4,800 | |
| Interest Revenue | | 4,800 |

**Check:** Dr 4,800 = Cr 4,800. **Balanced.**

**(b) Impairment Dec 31, Year 1 (period-end AJE)**

Expected CF: **$54,000** in **3 years**; no further interest.

\[
PV = \frac{54{,}000}{(1.06)^{3}} = \frac{54{,}000}{1.191016} \approx 45{,}339.44 \rightarrow \mathbf{\$45{,}339}
\]

AFDA = \(80{,}000 - 45{,}339 = \mathbf{\$34{,}661}\).

| Account | Debit | Credit |
|---|---:|---:|
| Bad Debt Expense | 34,661 | |
| Allowance for Doubtful Accounts | | 34,661 |
| *Impair note: $80,000 to PV of expected CF $45,339 at original 6%* | | |

**Check:** Dr 34,661 = Cr 34,661. **Balanced.**

**(c) Subsequent measurement schedule**

| Date | Net CA (beg) | Interest rev (6%) | Cash int. | Net CA (end) | AFDA (end) |
|---|---:|---:|---:|---:|---:|
| Dec 31, Y1 (after impair) | 45,339 | — | — | **45,339** | **34,661** |
| Dec 31, Y2 | 45,339 | **2,720** | 0 | **48,059** | **31,941** |
| Dec 31, Y3 | 48,059 | **2,884** | 0 | **50,943** | **29,057** |
| Dec 31, Y4 (before settlement) | 50,943 | **3,057** | 0 | **54,000** | **26,000** |

**Checks:** \(45{,}339 \times 0.06 = 2{,}720.34 \rightarrow \$2{,}720\); \(45{,}339 + 2{,}720 = 48{,}059\).  
\(48{,}059 \times 0.06 = 2{,}883.54 \rightarrow \$2{,}884\); \(48{,}059 + 2{,}884 = 50{,}943\).  
Final interest \(54{,}000 - 50{,}943 = \$3{,}057\) (vs. \(50{,}943 \times 0.06 = 3{,}056.58\)).  
AFDA: \(34{,}661 - 2{,}720 = 31{,}941\); \(31{,}941 - 2{,}884 = 29{,}057\); \(29{,}057 - 3{,}057 = 26{,}000\).

**(d) December 31, Year 2 and Year 3 — Effective-interest period-end AJEs**

| Account | Debit | Credit |
|---|---:|---:|
| Allowance for Doubtful Accounts | 2,720 | |
| Interest Revenue | | 2,720 |

**Check:** Dr 2,720 = Cr 2,720. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Allowance for Doubtful Accounts | 2,884 | |
| Interest Revenue | | 2,884 |

**Check:** Dr 2,884 = Cr 2,884. **Balanced.**

**(e) December 31, Year 4 — Settlement (includes final interest)**

AFDA before final interest = **$29,057**. Cash = **$54,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 54,000 | |
| Allowance for Doubtful Accounts | 29,057 | |
| Note Receivable | | 80,000 |
| Interest Revenue | | 3,057 |

**Check:** Dr \(54{,}000 + 29{,}057 = 83{,}057\); Cr \(80{,}000 + 3{,}057 = 83{,}057\). **Balanced.**

**Key insight:** Changing face, rate, remaining life, and expected recovery changes the PV and every period-end AJE amount, but the structure is fixed: impair to PV at original rate at period-end, then accrete net CA with period-end effective-interest entries until settlement.

---

### Q3 — CORE alternate angle — Period-end accrual + restructure as continuation of existing loan
**LO:** LO 8-9  
**Concept:** Period-end interest accrual; restructure treated as continuation of existing loan; impairment at original effective rate; subsequent measurement schedule with partial cash interest; principal settlement  
**Scenario:**  
**Westvale Credit Corp.** (calendar year) sold merchandise to **Ironclad Fabrication Inc.** on **January 1, Year 1** for a **three-year, 10%, $250,000** note at face. Interest of **$25,000** is due each December 31; principal due **December 31, Year 3**.

Ironclad **fails to pay** the December 31, Year 1 interest. Westvale records the **period-end interest accrual**. On **January 1, Year 2**, the parties restructure the debt (terms are **not** market terms for a new customer → treat as **continuation of the existing loan**):

- Year 1 accrued interest is **forgiven**
- Face reduced to **$200,000**
- Maturity remains **December 31, Year 3** (two years from restructure)
- Stated interest reduced to **5%** of the new face → cash interest **$10,000** due December 31, Year 2 and Year 3

Westvale uses the DCF method at the **original 10%** effective rate and the effective interest method after restructuring. Ironclad pays all restructured amounts as scheduled.

**Required:**  
(a) Record Westvale’s **December 31, Year 1 period-end interest accrual**.  
(b) Compute PV of restructured expected cash flows at **10%** and record the **January 1, Year 2** restructure / impairment entries (capitalize forgiven interest into the note receivable per textbook approach). Round PV to **$182,645**.  
(c) Prepare a **subsequent measurement schedule** of net CA from restructure through Dec 31, Year 3 (after interest, before principal collection).  
(d) Record **December 31, Year 2** period-end cash interest / effective interest.  
(e) Record **December 31, Year 3** period-end cash interest / effective interest and the **principal settlement**.  
(f) Optionally, if instead on January 1, Year 2 Ironclad transferred land (FV **$45,000**) and a building (FV **$90,000**) in **full settlement** of the note and accrued interest, record the **creditor’s settlement JE** (no restructure).

**Answer key:**

**(a) December 31, Year 1 — Period-end interest accrual**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Receivable | 25,000 | |
| Interest Revenue | | 25,000 |
| *Accrue contractual interest (unpaid)* | | |

**Check:** Dr 25,000 = Cr 25,000. **Balanced.**

Carrying amount before restructure = Note \(250{,}000\) + Interest receivable \(25{,}000\) = **$275,000**.

**(b) January 1, Year 2 — Restructure impairment**

Expected CF: annuity **$10,000** for 2 years + **$200,000** principal at end of Year 3.

\[
\begin{align*}
PV &= 10{,}000 \times \frac{1-(1.10)^{-2}}{0.10} + 200{,}000 \times (1.10)^{-2} \\
&= 10{,}000 \times 1.735537 + 200{,}000 \times 0.826446 \\
&= 17{,}355.37 + 165{,}289.26 = 182{,}644.63 \rightarrow \mathbf{\$182{,}645}
\end{align*}
\]

Impairment = \(275{,}000 - 182{,}645 = \mathbf{\$92{,}355}\).

Capitalize accrued interest into note (textbook pattern):

| Account | Debit | Credit |
|---|---:|---:|
| Note Receivable | 25,000 | |
| Interest Receivable | | 25,000 |
| *Transfer unpaid interest into note receivable* | | |

**Check:** Dr 25,000 = Cr 25,000. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Bad Debt Expense | 92,355 | |
| Allowance for Doubtful Accounts | | 92,355 |
| *Impair restructured note: gross $275,000 to PV $182,645 at original 10%* | | |

**Check:** Dr 92,355 = Cr 92,355. **Balanced.**

After entries: NR **$275,000**; AFDA **$92,355**; net **$182,645**.

**(c) Subsequent measurement schedule**

Interest revenue = beginning net CA × **10%**. Cash interest **$10,000** reduces net CA; excess of interest revenue over cash reduces AFDA.

| Date | Net CA (beg) | Interest rev (10%) | Cash interest | Increase in net CA | Net CA (end) | AFDA (end) |
|---|---:|---:|---:|---:|---:|---:|
| Jan 1, Y2 (after restructure) | 182,645 | — | — | — | **182,645** | **92,355** |
| Dec 31, Y2 | 182,645 | **18,264** | **10,000** | **8,264** | **190,909** | **84,091** |
| Dec 31, Y3 (after interest, before principal) | 190,909 | **19,091** | **10,000** | **9,091** | **200,000** | **75,000** |

**Checks:** \(182{,}645 \times 0.10 = 18{,}264.50 \rightarrow \$18{,}264\); \(182{,}645 + 18{,}264 - 10{,}000 = 190{,}909\).  
\(190{,}909 \times 0.10 = 19{,}090.90 \rightarrow \$19{,}091\); \(190{,}909 + 19{,}091 - 10{,}000 = 200{,}000\).  
AFDA: \(92{,}355 - 8{,}264 = 84{,}091\); \(84{,}091 - 9{,}091 = 75{,}000\).  
Gross NR \(275{,}000 - 75{,}000 = 200{,}000\) (equals restructured principal to collect).

**(d) December 31, Year 2 — Period-end cash interest and effective interest**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 10,000 | |
| Allowance for Doubtful Accounts | 8,264 | |
| Interest Revenue | | 18,264 |
| *Receive restructured cash interest; accrete net CA at 10%* | | |

**Check:** Dr \(10{,}000 + 8{,}264 = 18{,}264\) = Cr 18,264. **Balanced.**

**(e) December 31, Year 3 — Period-end interest and principal settlement**

Interest:

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 10,000 | |
| Allowance for Doubtful Accounts | 9,091 | |
| Interest Revenue | | 19,091 |

**Check:** Dr \(10{,}000 + 9{,}091 = 19{,}091\) = Cr 19,091. **Balanced.**

Principal settlement:

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 200,000 | |
| Allowance for Doubtful Accounts | 75,000 | |
| Note Receivable | | 275,000 |
| *Collect restructured principal; clear gross NR and remaining AFDA* | | |

**Check:** Dr \(200{,}000 + 75{,}000 = 275{,}000\) = Cr 275,000. **Balanced.**

**(f) Alternate settlement by asset transfer (instead of restructure)**

Carrying amount settled = NR \(250{,}000\) + Interest receivable \(25{,}000\) = **$275,000**.  
FV of assets received = \(45{,}000 + 90{,}000 = \mathbf{\$135{,}000}\).  
Loss = \(275{,}000 - 135{,}000 = \mathbf{\$140{,}000}\).

| Account | Debit | Credit |
|---|---:|---:|
| Land | 45,000 | |
| Building | 90,000 | |
| Loss on Settlement of Receivable* | 140,000 | |
| Note Receivable | | 250,000 |
| Interest Receivable | | 25,000 |

\*May also debit Bad Debt Expense or offset Allowance for Doubtful Accounts.

**Check:** Dr \(45{,}000 + 90{,}000 + 140{,}000 = 275{,}000\) = Cr \(250{,}000 + 25{,}000\). **Balanced.**

**Key insight:** A modification that continues the existing loan is still measured for impairment at the **original effective rate**. Period-end entries first establish the pre-restructure carrying amount (interest accrual), then the restructure impairment sets net CA; subsequent period-ends accrete net CA while cash interest below effective interest reduces AFDA.

---

### Q4 — MC — Accounts in the period-end impairment adjusting entry
**LO:** LO 8-9  
**Concept:** Classification of period-end impairment AJE when accrued interest will not be collected  
**Question:**  
At year-end a creditor has already accrued contractual interest on a long-term note (Dr Interest Receivable / Cr Interest Revenue). Management then concludes that the accrued interest will not be collected and that principal collections will be less than face. Using the DCF method at the original effective rate, the **period-end impairment adjusting entry** typically:

- A) Debits Interest Revenue only, for the full contractual interest previously accrued  
- B) Debits **Bad Debt Expense** for the sum of (allowance needed on the note + uncollectible interest receivable), credits **Interest Receivable** for the uncollectible accrued interest, and credits **Allowance for Doubtful Accounts** for face minus PV of expected cash flows  
- C) Debits Allowance for Doubtful Accounts and credits Note Receivable for the impairment amount  
- D) Discounts expected cash flows at the current market rate and adjusts fair value through OCI  

**Answer:** **B.** Per Demo 8-9A-style accounting, bad debt expense covers both the valuation allowance needed to bring the note to PV of expected cash flows **and** the write-off of interest receivable that will not be collected. The current market rate is not used for the DCF discount rate under ASC 326.

---

### Q5 — MC — Post-impairment period-end interest recognition
**LO:** LO 8-9  
**Concept:** Period-end effective interest after DCF impairment when no cash interest is expected  
**Question:**  
After a noncurrent note is impaired and **no further cash interest is expected**, how does the creditor typically record the **period-end** effective-interest adjusting entry?

- A) Debit Interest Receivable and credit Interest Revenue for contractual stated interest  
- B) Debit **Allowance for Doubtful Accounts** and credit Interest Revenue for beginning net carrying amount × original effective rate  
- C) No interest revenue is recognized after an impairment until cash is collected  
- D) Credit Allowance for Doubtful Accounts and debit Interest Expense for the contractual interest  

**Answer:** **B.** Net carrying amount is accreted at the original effective rate each period-end; when cash interest is not expected, the offset is usually a **debit to AFDA**, increasing the net receivable toward the expected recovery amount (as shown in the subsequent measurement schedule).

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (PV factors, interest accretion, AFDA rollforwards, settlement plugs)
- [x] Core demo not sidebar-only (Appendix 8B LO 8-9 Demo 8-9A/B path: impairment, period-end AJEs, subsequent effective interest, restructure, settlement)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5 only)
- [x] Emphasis angle **period_end_adjusting_JE** covered heavily in Q1–Q3 (accrual, impairment AJE, post-impairment interest AJEs)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE
