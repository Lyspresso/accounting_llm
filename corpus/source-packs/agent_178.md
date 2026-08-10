# Agent 178 — CORE DEMO — LO 8-9

**Chapter:** 8  
**LO title:** Account for impairment of noncurrent receivables  
**Critical gap LO:** no  
**Emphasis angle:** subsequent_measurement_schedule

## Concept list for this pack
- **CECL / note impairment (ASC 326):** measure expected credit losses over the life of the note using historical, current, and reasonable and supportable forecast information; even remote loss risk is considered
- **Discounted cash flow method:** expected future principal and interest cash flows discounted at the note’s **original effective interest rate** (not the current market rate for similar risk)
- **Impairment loss:** excess of amortized cost (carrying amount) over PV of expected cash flows → **Dr Bad Debt Expense, Cr Allowance for Doubtful Accounts** (and write off uncollectible interest receivable when appropriate)
- **Subsequent measurement schedule (emphasis):** after impairment, accrete net carrying amount using the **effective interest method** at the original effective rate; interest revenue often recorded by **debiting AFDA** when no cash interest is expected
- **Period-end adjusting JEs:** interest accrual before impairment; impairment entry; post-impairment effective-interest accruals each period-end
- **Settlement / maturity:** cash collected + remaining AFDA + any final interest revenue (and loss if shortfall) clear the note receivable
- **Troubled debt restructuring (creditor):** settlement by assets/equity at FV, or modification treated as continuation of existing loan → remeasure impairment at original effective rate; capitalize forgiven accrued interest into note when applicable

---

### Q1 — CORE — Note impairment lifecycle with subsequent measurement schedule
**LO:** LO 8-9  
**Concept:** Initial recognition of note receivable; period-end interest; DCF impairment at original effective rate; multi-year subsequent measurement (net carrying amount / AFDA) schedule; settlement at maturity  
**Scenario:**  
**Northline Supply Co.** is a calendar-year firm. On **January 1, Year 1**, Northline sold merchandise to **Bristol Fabricators** and accepted a **four-year, 5%, $60,000** note receivable issued at face (market rate also **5%**). Annual interest of **$3,000** is due each **December 31**. The note principal is due **December 31, Year 4**.

Northline collected the **Year 1** interest on schedule. At **December 31, Year 1**, after reviewing Bristol’s financial distress, Northline concludes it will collect **no further interest** and will collect only **$45,000** of principal on the original due date (**December 31, Year 4**). The current market rate for notes of similar risk is **11%** (do **not** use this rate for the impairment measurement).

Northline uses the **discounted cash flow** method and the **effective interest method** after impairment. On **December 31, Year 4**, Northline collects **$43,800** cash and expects no further payments.

**Required:**  
(a) Record the **January 1, Year 1** initial recognition of the note (ignore COGS).  
(b) Record the **December 31, Year 1** receipt of interest.  
(c) Compute the **present value of expected cash flows** at December 31, Year 1, and record the **impairment** (period-end adjusting JE). Round PV to the nearest dollar in a manner that produces a clean subsequent schedule ending at the expected $45,000 (**use PV = $38,872**).  
(d) Prepare a **subsequent measurement schedule** (emphasis) of the **net carrying amount** of the note from December 31, Year 1 (after impairment) through December 31, Year 4 **before** settlement, showing interest revenue each year at **5%**. Also roll forward **AFDA**.  
(e) Record the **December 31, Year 2** and **December 31, Year 3** effective-interest accruals.  
(f) Record the **December 31, Year 4** settlement, combining final interest accretion with the cash receipt (and any loss).  
(g) Briefly explain why the **11%** market rate is not used to discount expected cash flows.

**Answer key:**

**(a) January 1, Year 1 — Initial recognition**

| Account | Debit | Credit |
|---|---:|---:|
| Note Receivable | 60,000 | |
| Sales Revenue | | 60,000 |
| *Accept 4-year 5% note for merchandise sale* | | |

**Check:** Dr 60,000 = Cr 60,000. **Balanced.**

**(b) December 31, Year 1 — Interest receipt**

Interest = \(60{,}000 \times 0.05 = \mathbf{\$3{,}000}\).

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 3,000 | |
| Interest Revenue | | 3,000 |
| *Collect Year 1 contractual interest* | | |

**Check:** Dr 3,000 = Cr 3,000. **Balanced.**

**(c) December 31, Year 1 — Impairment (DCF at original effective rate 5%)**

Expected cash flow: single principal collection of **$45,000** in **3 years**; no interest.

\[
PV = \frac{45{,}000}{(1.05)^{3}} = \frac{45{,}000}{1.157625} \approx 38{,}872.45 \rightarrow \mathbf{\$38{,}872}
\]

(Use **$38,872** so the effective-interest schedule rolls cleanly to the $45,000 expected amount.)

Allowance = amortized cost − PV = \(60{,}000 - 38{,}872 = \mathbf{\$21{,}128}\).

| Account | Debit | Credit |
|---|---:|---:|
| Bad Debt Expense | 21,128 | |
| Allowance for Doubtful Accounts | | 21,128 |
| *Impair note: carrying amount $60,000 to PV of expected CF $38,872 at original 5%* | | |

**Check:** Dr 21,128 = Cr 21,128. **Balanced.**

**Do not** discount at 11%. Net note receivable reported = **$38,872**.

**(d) Subsequent measurement schedule (emphasis) — net carrying amount & AFDA**

Interest each year = beginning net CA × **5%** (original effective rate). No cash interest is collected after Year 1; accretion increases net CA by reducing AFDA.

| Date | Net CA (beg) | Interest revenue (5%) | Cash interest | Net CA (end) | AFDA balance (end) |
|---|---:|---:|---:|---:|---:|
| Dec 31, Y1 (after impairment) | 38,872 | — | — | **38,872** | **21,128** |
| Dec 31, Y2 | 38,872 | **1,944** | 0 | **40,816** | **19,184** |
| Dec 31, Y3 | 40,816 | **2,041** | 0 | **42,857** | **17,143** |
| Dec 31, Y4 (before settlement) | 42,857 | **2,143** | 0 | **45,000** | **15,000** |

**Math checks:**  
\(38{,}872 \times 0.05 = 1{,}943.60 \rightarrow \$1{,}944\); \(38{,}872 + 1{,}944 = 40{,}816\).  
\(40{,}816 \times 0.05 = 2{,}040.80 \rightarrow \$2{,}041\); \(40{,}816 + 2{,}041 = 42{,}857\).  
\(42{,}857 \times 0.05 = 2{,}142.85 \rightarrow \$2{,}143\); \(42{,}857 + 2{,}143 = 45{,}000\).  
AFDA: \(21{,}128 - 1{,}944 = 19{,}184\); \(19{,}184 - 2{,}041 = 17{,}143\); \(17{,}143 - 2{,}143 = 15{,}000\).  
Gross NR \(60{,}000 -\) AFDA \(15{,}000 =\) net \(45{,}000\).

**(e) December 31, Year 2 and Year 3 — Effective interest (period-end adjusting)**

| Account | Debit | Credit |
|---|---:|---:|
| Allowance for Doubtful Accounts | 1,944 | |
| Interest Revenue | | 1,944 |
| *Y2 effective interest on net CA $38,872 × 5%* | | |

**Check:** Dr 1,944 = Cr 1,944. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Allowance for Doubtful Accounts | 2,041 | |
| Interest Revenue | | 2,041 |
| *Y3 effective interest on net CA $40,816 × 5%* | | |

**Check:** Dr 2,041 = Cr 2,041. **Balanced.**

**(f) December 31, Year 4 — Settlement (disposal/maturity)**

Combine final interest accretion with collection. Cash received **$43,800** vs. expected net **$45,000** → additional loss **$1,200**. AFDA immediately before final interest entry = **$17,143**.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 43,800 | |
| Loss on Settlement of Note Receivable | 1,200 | |
| Allowance for Doubtful Accounts | 17,143 | |
| Note Receivable | | 60,000 |
| Interest Revenue | | 2,143 |
| *Collect $43,800; accrete final interest; clear NR and remaining AFDA; recognize shortfall loss* | | |

**Check:** Dr \(43{,}800 + 1{,}200 + 17{,}143 = 62{,}143\); Cr \(60{,}000 + 2{,}143 = 62{,}143\). **Balanced.**

**(g) Rate choice**  
ASC 326 requires discounting expected cash flows at the **financial asset’s original effective interest rate**. Changes in general rates or risk premiums are **not** reflected by changing the discount rate; only changes in **expected cash flows** affect the allowance.

**Key insight:** Impairment sets net CA to PV of expected CF at the **original** effective rate; the **subsequent measurement schedule** then accretes that net amount to the expected collection date using effective interest, typically by debiting AFDA rather than Interest Receivable when no cash interest is expected.

---

### Q2 — CORE number variant — Same lifecycle, all numbers changed
**LO:** LO 8-9  
**Concept:** Number-variant twin — initial recognition, DCF impairment, subsequent measurement schedule, period-end effective-interest accruals, settlement  
**Scenario:**  
**Meridian Trading Co.** (calendar year) sold equipment-related inventory to **Cedar Ridge LLC** on **January 1, Year 1** and accepted a **three-year, 10%, $50,000** note at face (market rate **10%**). Interest of **$5,000** is due each December 31; principal is due **December 31, Year 3**.

Meridian collected Year 1 interest. At **December 31, Year 1**, Meridian expects **no further interest** and only **$40,000** of principal on **December 31, Year 3**. The current similar-risk market rate is **15%** (ignore for discounting). On **December 31, Year 3**, Meridian collects **exactly $40,000**.

**Required:**  
(a) Initial recognition JE (Jan 1, Y1) and Year 1 interest receipt.  
(b) Impairment computation and JE at Dec 31, Y1 (PV rounded to **$33,058**).  
(c) **Subsequent measurement schedule** of net CA and AFDA through Dec 31, Y3 before settlement.  
(d) Period-end effective-interest JE for Year 2.  
(e) Combined settlement JE at Dec 31, Y3 (include final interest accretion).

**Answer key:**

**(a) Initial recognition and Year 1 interest**

| Account | Debit | Credit |
|---|---:|---:|
| Note Receivable | 50,000 | |
| Sales Revenue | | 50,000 |

**Check:** Dr 50,000 = Cr 50,000. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 5,000 | |
| Interest Revenue | | 5,000 |

**Check:** Dr 5,000 = Cr 5,000. **Balanced.**

**(b) Impairment Dec 31, Year 1**

\[
PV = \frac{40{,}000}{(1.10)^{2}} = \frac{40{,}000}{1.21} = 33{,}057.85 \rightarrow \mathbf{\$33{,}058}
\]

AFDA = \(50{,}000 - 33{,}058 = \mathbf{\$16{,}942}\).

| Account | Debit | Credit |
|---|---:|---:|
| Bad Debt Expense | 16,942 | |
| Allowance for Doubtful Accounts | | 16,942 |

**Check:** Dr 16,942 = Cr 16,942. **Balanced.**

**(c) Subsequent measurement schedule (emphasis)**

| Date | Net CA (beg) | Interest rev (10%) | Cash int. | Net CA (end) | AFDA (end) |
|---|---:|---:|---:|---:|---:|
| Dec 31, Y1 (after impair) | 33,058 | — | — | **33,058** | **16,942** |
| Dec 31, Y2 | 33,058 | **3,306** | 0 | **36,364** | **13,636** |
| Dec 31, Y3 (before settlement) | 36,364 | **3,636** | 0 | **40,000** | **10,000** |

**Checks:** \(33{,}058 \times 0.10 = 3{,}305.80 \rightarrow \$3{,}306\); \(33{,}058 + 3{,}306 = 36{,}364\).  
\(36{,}364 \times 0.10 = 3{,}636.40 \rightarrow \$3{,}636\); \(36{,}364 + 3{,}636 = 40{,}000\).  
AFDA: \(16{,}942 - 3{,}306 = 13{,}636\); \(13{,}636 - 3{,}636 = 10{,}000\).

**(d) December 31, Year 2 — Effective interest**

| Account | Debit | Credit |
|---|---:|---:|
| Allowance for Doubtful Accounts | 3,306 | |
| Interest Revenue | | 3,306 |

**Check:** Dr 3,306 = Cr 3,306. **Balanced.**

**(e) December 31, Year 3 — Settlement**

AFDA before final interest = **$13,636**. Cash = **$40,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 40,000 | |
| Allowance for Doubtful Accounts | 13,636 | |
| Note Receivable | | 50,000 |
| Interest Revenue | | 3,636 |

**Check:** Dr \(40{,}000 + 13{,}636 = 53{,}636\); Cr \(50{,}000 + 3{,}636 = 53{,}636\). **Balanced.**

**Key insight:** Changing face, rate, remaining life, and expected recovery changes the PV and the entire **subsequent measurement schedule**, but the structure is identical: impair to PV at original rate, then accrete net CA each period-end.

---

### Q3 — CORE alternate angle — Troubled debt restructure (extension of existing loan) with subsequent schedule
**LO:** LO 8-9  
**Concept:** Period-end interest accrual; restructure treated as continuation of existing loan; impairment at original effective rate; subsequent measurement schedule with partial cash interest; principal settlement  
**Scenario:**  
**Oakridge Credit LLC** (calendar year) sold merchandise to **Sable Industries** on **January 1, Year 1** for a **three-year, 12%, $200,000** note at face. Interest of **$24,000** is due each December 31; principal due **December 31, Year 3**.

Sable **fails to pay** the December 31, Year 1 interest. Oakridge **accrues** that interest at year-end. On **January 1, Year 2**, the parties restructure the debt (terms are **not** market terms for a new customer → treat as **continuation of the existing loan**):

- Year 1 accrued interest is **forgiven**
- Face reduced to **$160,000**
- Maturity extended so principal is due **December 31, Year 3** (two years from restructure)
- Stated interest reduced to **6%** of the new face → cash interest **$9,600** due December 31, Year 2 and Year 3

Oakridge uses the DCF method at the **original 12%** effective rate and the effective interest method after restructuring. Sable pays all restructured amounts as scheduled.

**Required:**  
(a) Record Oakridge’s **December 31, Year 1** interest accrual.  
(b) Compute PV of restructured expected cash flows at **12%** and record the **January 1, Year 2** impairment / restructure entries (capitalize forgiven interest into the note receivable per textbook approach). Round PV to **$143,776**.  
(c) Prepare a **subsequent measurement schedule** of net CA from restructure through Dec 31, Year 3 (after interest, before principal collection).  
(d) Record **December 31, Year 2** cash interest / effective interest.  
(e) Record **December 31, Year 3** cash interest / effective interest and the **principal settlement**.

**Answer key:**

**(a) December 31, Year 1 — Period-end interest accrual**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Receivable | 24,000 | |
| Interest Revenue | | 24,000 |
| *Accrue contractual interest (unpaid)* | | |

**Check:** Dr 24,000 = Cr 24,000. **Balanced.**

Carrying amount before restructure = Note \(200{,}000\) + Interest receivable \(24{,}000\) = **$224,000**.

**(b) January 1, Year 2 — Restructure impairment**

Expected CF: annuity **$9,600** for 2 years + **$160,000** principal at end of Year 3.

\[
\begin{align*}
PV &= 9{,}600 \times \frac{1-(1.12)^{-2}}{0.12} + 160{,}000 \times (1.12)^{-2} \\
&= 9{,}600 \times 1.690051 + 160{,}000 \times 0.797194 \\
&= 16{,}224.49 + 127{,}551.04 = 143{,}775.53 \rightarrow \mathbf{\$143{,}776}
\end{align*}
\]

Impairment = \(224{,}000 - 143{,}776 = \mathbf{\$80{,}224}\).

Capitalize accrued interest into note (textbook pattern):

| Account | Debit | Credit |
|---|---:|---:|
| Note Receivable | 24,000 | |
| Interest Receivable | | 24,000 |
| *Transfer unpaid interest into note receivable* | | |

**Check:** Dr 24,000 = Cr 24,000. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Bad Debt Expense | 80,224 | |
| Allowance for Doubtful Accounts | | 80,224 |
| *Impair restructured note: gross $224,000 to PV $143,776 at original 12%* | | |

**Check:** Dr 80,224 = Cr 80,224. **Balanced.**

After entries: NR **$224,000**; AFDA **$80,224**; net **$143,776**.

**(c) Subsequent measurement schedule (emphasis)**

Interest revenue = beginning net CA × **12%**. Cash interest **$9,600** reduces net CA; the plug reduces AFDA.

| Date | Net CA (beg) | Interest rev (12%) | Cash interest | Increase in net CA | Net CA (end) | AFDA (end) |
|---|---:|---:|---:|---:|---:|---:|
| Jan 1, Y2 (after restructure) | 143,776 | — | — | — | **143,776** | **80,224** |
| Dec 31, Y2 | 143,776 | **17,253** | **9,600** | **7,653** | **151,429** | **72,571** |
| Dec 31, Y3 (after interest, before principal) | 151,429 | **18,171** | **9,600** | **8,571** | **160,000** | **64,000** |

**Checks:** \(143{,}776 \times 0.12 = 17{,}253.12 \rightarrow \$17{,}253\); \(143{,}776 + 17{,}253 - 9{,}600 = 151{,}429\).  
\(151{,}429 \times 0.12 = 18{,}171.48 \rightarrow \$18{,}171\); \(151{,}429 + 18{,}171 - 9{,}600 = 160{,}000\).  
AFDA: \(80{,}224 - 7{,}653 = 72{,}571\); \(72{,}571 - 8{,}571 = 64{,}000\).  
Gross NR \(224{,}000 - 64{,}000 = 160{,}000\) (equals restructured principal to collect).

**(d) December 31, Year 2 — Cash interest and effective interest**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 9,600 | |
| Allowance for Doubtful Accounts | 7,653 | |
| Interest Revenue | | 17,253 |
| *Receive restructured cash interest; accrete net CA at 12%* | | |

**Check:** Dr \(9{,}600 + 7{,}653 = 17{,}253\) = Cr 17,253. **Balanced.**

**(e) December 31, Year 3 — Interest and principal settlement**

Interest:

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 9,600 | |
| Allowance for Doubtful Accounts | 8,571 | |
| Interest Revenue | | 18,171 |

**Check:** Dr \(9{,}600 + 8{,}571 = 18{,}171\) = Cr 18,171. **Balanced.**

Principal settlement:

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 160,000 | |
| Allowance for Doubtful Accounts | 64,000 | |
| Note Receivable | | 224,000 |
| *Collect restructured principal; clear gross NR and remaining AFDA* | | |

**Check:** Dr \(160{,}000 + 64{,}000 = 224{,}000\) = Cr 224,000. **Balanced.**

**Key insight:** A modification that continues the existing loan is still measured for impairment at the **original effective rate**. The **subsequent measurement schedule** accretes net CA toward the restructured principal while cash interest below effective interest reduces AFDA each period.

---

### Q4 — MC — Discount rate for DCF impairment of a note
**LO:** LO 8-9  
**Concept:** Original effective rate vs. current market rate for measuring note receivable impairment  
**Question:**  
When a creditor measures impairment of a long-term note receivable using a discounted cash flow method under ASC 326, expected future cash flows should be discounted using:

- A) The current market rate for notes of similar credit risk  
- B) The note’s **original effective interest rate**  
- C) The risk-free rate plus a current credit spread  
- D) The creditor’s incremental borrowing rate  

**Answer:** **B.** Standards require use of the financial asset’s original effective interest rate so that the allowance reflects changes in **expected cash flows**, not changes in market interest rates or risk premiums.

---

### Q5 — MC — Post-impairment interest recognition
**LO:** LO 8-9  
**Concept:** Effective interest after impairment when no cash interest is expected  
**Question:**  
After a note is impaired and no further cash interest is expected, how does the creditor typically recognize interest revenue under the effective interest method?

- A) Debit Interest Receivable and credit Interest Revenue for contractual stated interest  
- B) Debit **Allowance for Doubtful Accounts** and credit Interest Revenue for beginning net carrying amount × original effective rate  
- C) No interest revenue is recognized after an impairment  
- D) Credit Allowance for Doubtful Accounts for the full contractual interest each period  

**Answer:** **B.** Net carrying amount is accreted at the original effective rate; when cash interest is not expected, the offset is usually a **debit to AFDA**, increasing the net receivable toward the expected recovery amount (as in the subsequent measurement schedule).

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (PV factors, interest accretion, AFDA rollforwards, settlement plugs)
- [x] Core demo not sidebar-only (Appendix 8B LO 8-9 Demo 8-9A/B path: impairment, subsequent effective interest, restructure, settlement)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4, Q5 only)
- [x] Emphasis angle **subsequent_measurement_schedule** covered in Q1–Q3
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE
