# Agent 263 — CORE DEMO — LO 14-1

**Chapter:** 14  
**LO title:** Account for debt securities measured at amortized cost  
**Critical gap LO:** yes  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **HTM classification:** positive intent **and** ability to hold a debt security to maturity; measured at **amortized cost**
- **Initial recognition JE:** record Investment in HTM at acquisition cost (par, discount, or premium); no separate premium/discount accounts in net method
- **Subsequent measurement schedule:** effective-interest amortization table (cash interest, interest revenue, discount/premium amortization, amortized cost)
- **Period-end adjusting JE (emphasis):** accrue interest receivable and amortize discount/premium when the reporting date falls between interest payment dates
- **Disposal / maturity JE:** collect face at maturity (or sell before maturity for realized gain/loss when justified by unforeseen circumstances)
- **Classification / presentation / disclosure:** HTM carried at amortized cost (ignore FV for carrying amount); aggregate fair value and unrealized holding gains/losses disclosed in notes
- **Number-variant twin:** same HTM discount + period-end accrual pattern with different face, rates, and fractions of year

---

### Q1 — CORE — HTM discount: purchase, amort schedule, period-end accrual (emphasis), maturity
**LO:** LO 14-1  
**Concept:** Initial recognition of HTM at discount; effective-interest amortization schedule; **period-end adjusting JE** when year-end is between interest dates; maturity settlement  
**Scenario:**  
**Northvale Logistics Inc.** (calendar-year reporter) has idle cash and the **positive intent and ability** to hold debt securities until maturity. On **October 1, Year 1**, Northvale purchases **$400,000 face** of **Oakridge Utilities Corp.** 6% bonds. Interest is paid **annually each October 1**. The bonds mature on **October 1, Year 4** (three years from purchase). The market (effective) yield for similar risk is **8%**. Northvale uses the **effective interest method** and records the HTM investment **net** (no separate discount account).

**Required:**  
a. Compute the **October 1, Year 1 purchase price** (round to the nearest whole dollar) and prepare the **initial recognition journal entry**. State the investment’s classification and why.  
b. Prepare the **complete effective-interest amortization schedule** for the three annual interest periods (October 1 → October 1). Round interest revenue each period to the nearest dollar; plug the final period so amortized cost equals face.  
c. Prepare the **December 31, Year 1 period-end adjusting journal entry** for accrued interest and discount amortization (**emphasis**). Use effective interest for **3/12** of the first annual period. Show Dr = Cr.  
d. Prepare the **October 1, Year 2** entry when the full annual cash interest is received (clear the accrual; recognize remaining first-period interest revenue and remaining first-period discount amortization).  
e. Prepare the **October 1, Year 4 maturity** entry to collect face value (assume the final period’s interest entry was already recorded).  
f. **Classification / disclosure:** At December 31, Year 1, the bonds’ fair value is **$382,000**. At what amount is the investment **reported on the balance sheet**? What, if anything, is disclosed about fair value?

**Answer key:**  

**a. Purchase price and initial recognition**

Classification: **Held-to-maturity (HTM)** — Northvale has both the **positive intent and ability** to hold to maturity. HTM debt securities are measured at **amortized cost**; subsequent fair-value changes are **not** recognized in the accounts.

Semiannual/period setup (annual interest):  
- Annual market rate = **8%**  
- Periods = **3**  
- Annual cash interest = 6% × $400,000 = **$24,000**

Purchase price (PV of cash interest + PV of principal at 8%):  
\[
\text{Price} = \$24{,}000 \times \text{PVAF}(8\%,3) + \$400{,}000 \times \text{PVF}(8\%,3)
\]
Excel: `=−PV(0.08,3,24000,400000)` → **$379,383** (rounded).

Discount at acquisition = $400,000 − $379,383 = **$20,617**.

| Account | Debit | Credit |
|---|---:|---:|
| Investment in HTM Securities—Oakridge Bonds | 379,383 | |
| Cash | | 379,383 |
| *Purchase Oakridge 6% bonds as HTM at discount* | | |

**Check:** Dr = Cr = **379,383**. **Balanced.**

**b. Effective-interest amortization schedule (subsequent measurement)**

| Date | Cash interest (6% × face) | Interest revenue (8% × beg. amortized cost) | Discount amortization | Amortized cost (end) |
|---|---:|---:|---:|---:|
| Oct. 1, Y1 | — | — | — | **379,383** |
| Oct. 1, Y2 | 24,000 | 30,351 | 6,351 | 385,734 |
| Oct. 1, Y3 | 24,000 | 30,859 | 6,859 | 392,593 |
| Oct. 1, Y4 | 24,000 | 31,407 | 7,407 | **400,000** |
| **Totals** | **72,000** | **92,617** | **20,617** | |

Computations (first two periods):  
- Y1→Y2 interest revenue: \(379{,}383 \times 0.08 = 30{,}350.64\) → **30,351**; amort. = 30,351 − 24,000 = **6,351**; end CV = 379,383 + 6,351 = **385,734**.  
- Y2→Y3: \(385{,}734 \times 0.08 = 30{,}858.72\) → **30,859**; amort. = **6,859**; end CV = **392,593**.  
- Final period: amort. forced to \(400{,}000 − 392{,}593 = \mathbf{7{,}407}\); interest revenue = 24,000 + 7,407 = **31,407**.

**Roll-forward check:** beginning discount 20,617 = total amortization 20,617; ending amortized cost = face.

**c. December 31, Year 1 — period-end adjusting JE (EMPHASIS)**

From Oct. 1 to Dec. 31 = **3 months** = **3/12** of the first annual interest period.

- Interest revenue (effective): \(379{,}383 \times 0.08 \times 3/12 = 7{,}587.66\) → **$7,588**  
- Cash interest accrued (stated): \(24{,}000 \times 3/12 = \mathbf{\$6{,}000}\)  
- Discount amortization: \(7{,}588 − 6{,}000 = \mathbf{\$1{,}588}\)

| Account | Debit | Credit |
|---|---:|---:|
| Interest Receivable | 6,000 | |
| Investment in HTM Securities—Oakridge Bonds | 1,588 | |
| Interest Revenue | | 7,588 |
| *Accrue 3 months interest and amortize discount to YE* | | |

**Check:** Dr = 6,000 + 1,588 = **7,588**; Cr = **7,588**. **Balanced.**

Amortized cost at Dec. 31, Year 1 = 379,383 + 1,588 = **$380,971**.

**d. October 1, Year 2 — cash interest received (clear accrual; complete first period)**

Remaining **9/12** of first period:  
- Remaining interest revenue = 30,351 − 7,588 = **22,763**  
- Remaining discount amortization = 6,351 − 1,588 = **4,763**  
- Cash received = **24,000** (includes the $6,000 previously accrued)

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 24,000 | |
| Investment in HTM Securities—Oakridge Bonds | 4,763 | |
| Interest Receivable | | 6,000 |
| Interest Revenue | | 22,763 |
| *Collect annual interest; clear accrual; finish first-period amort.* | | |

**Check:** Dr = 24,000 + 4,763 = **28,763**; Cr = 6,000 + 22,763 = **28,763**. **Balanced.**  
Amortized cost after this entry = 380,971 + 4,763 = **385,734** (matches schedule).

**e. October 1, Year 4 — maturity (final interest already recorded)**

After the final interest/amortization entry, amortized cost = face = **$400,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 400,000 | |
| Investment in HTM Securities—Oakridge Bonds | | 400,000 |
| *Collect face value at maturity; derecognize HTM* | | |

**Check:** Dr = Cr = **400,000**. **Balanced.**

**f. Classification / presentation / disclosure at Dec. 31, Year 1**

- **Balance sheet carrying amount:** amortized cost **$380,971** (not fair value).  
- **Fair value $382,000** is **not** used to adjust the investment account under LO 14-1.  
- **Note disclosure:** aggregate fair value of HTM securities and any **unrecognized holding gain** of \(382{,}000 − 380{,}971 = \mathbf{\$1{,}029}\) (and related amortized cost) are disclosed in the notes.

**Key insight:** HTM debt securities are recognized at amortized cost. Between interest dates, the **period-end adjusting entry** must accrue **Interest Receivable** for the stated-rate portion **and** update amortized cost for effective-interest amortization (discount ↑ investment / premium ↓ investment). Fair-value changes do not affect carrying amount—only note disclosure (unless impaired under other LOs).

---

### Q2 — CORE number variant — HTM discount twin with different period-end fraction
**LO:** LO 14-1  
**Concept:** Number-variant twin of HTM discount life cycle: initial recognition, effective-interest schedule, **period-end adjusting JE** (4/12), interest-date clearing entry, maturity  
**Scenario:**  
**Riverbend Foods Co.** (calendar year) buys **$250,000 face** of **Summit Railroad Inc.** 5% bonds on **September 1, Year 1**. Interest is paid **annually each September 1**. Bonds mature **September 1, Year 5** (four years). Market yield is **7%**. Riverbend has the **intent and ability** to hold to maturity and uses the **effective interest method** (net method). Year-end is **December 31**.

**Required:**  
a. Compute the **September 1, Year 1 purchase price** (nearest dollar) and record the **initial recognition JE**.  
b. Prepare the **4-period effective-interest amortization schedule** (round interest revenue to nearest dollar; plug final period to face).  
c. Prepare the **December 31, Year 1 period-end adjusting JE** for **4/12** of the first annual period.  
d. Prepare the **September 1, Year 2** entry when annual cash interest is collected.  
e. Prepare the **September 1, Year 5 maturity** entry (final interest already recorded).

**Answer key:**  

**a. Purchase price and initial recognition**

Annual cash interest = 5% × $250,000 = **$12,500**.  
Price = `=−PV(0.07,4,12500,250000)` → **$233,064**.  
Discount = 250,000 − 233,064 = **$16,936**.  
Classification: **HTM** at amortized cost.

| Account | Debit | Credit |
|---|---:|---:|
| Investment in HTM Securities—Summit Bonds | 233,064 | |
| Cash | | 233,064 |
| *Purchase Summit 5% bonds as HTM at discount* | | |

**Check:** Dr = Cr = **233,064**. **Balanced.**

**b. Effective-interest amortization schedule**

| Date | Cash (5% × face) | Interest revenue (7% × beg. CV) | Discount amort. | Amortized cost (end) |
|---|---:|---:|---:|---:|
| Sep. 1, Y1 | — | — | — | **233,064** |
| Sep. 1, Y2 | 12,500 | 16,314 | 3,814 | 236,878 |
| Sep. 1, Y3 | 12,500 | 16,581 | 4,081 | 240,959 |
| Sep. 1, Y4 | 12,500 | 16,867 | 4,367 | 245,326 |
| Sep. 1, Y5 | 12,500 | 17,174 | 4,674 | **250,000** |
| **Totals** | **50,000** | **66,936** | **16,936** | |

Checks: \(233{,}064 \times 0.07 = 16{,}314.48 → 16{,}314\); amort. 16,314 − 12,500 = 3,814; end 233,064 + 3,814 = 236,878. Final amort. plugged: \(250{,}000 − 245{,}326 = 4{,}674\). Total amort. = discount = **16,936**.

**c. December 31, Year 1 — period-end adjusting JE (4 months)**

- Interest revenue: \(233{,}064 \times 0.07 \times 4/12 = 5{,}437.82 → \mathbf{\$5{,}438}\)  
- Interest receivable: \(12{,}500 \times 4/12 = 4{,}166.67 → \mathbf{\$4{,}167}\)  
- Discount amortization: \(5{,}438 − 4{,}167 = \mathbf{\$1{,}271}\)

| Account | Debit | Credit |
|---|---:|---:|
| Interest Receivable | 4,167 | |
| Investment in HTM Securities—Summit Bonds | 1,271 | |
| Interest Revenue | | 5,438 |
| *Accrue 4 months interest and amortize discount* | | |

**Check:** Dr = 4,167 + 1,271 = **5,438**; Cr = **5,438**. **Balanced.**  
CV at Dec. 31, Y1 = 233,064 + 1,271 = **$234,335**.

**d. September 1, Year 2 — collect annual interest**

Remaining first-period amounts:  
- Interest revenue = 16,314 − 5,438 = **10,876**  
- Discount amort. = 3,814 − 1,271 = **2,543**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 12,500 | |
| Investment in HTM Securities—Summit Bonds | 2,543 | |
| Interest Receivable | | 4,167 |
| Interest Revenue | | 10,876 |
| *Collect interest; clear accrual; finish first-period amort.* | | |

**Check:** Dr = 12,500 + 2,543 = **15,043**; Cr = 4,167 + 10,876 = **15,043**. **Balanced.**  
CV after entry = 234,335 + 2,543 = **236,878**.

**e. September 1, Year 5 — maturity**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 250,000 | |
| Investment in HTM Securities—Summit Bonds | | 250,000 |
| *Collect face at maturity* | | |

**Check:** Dr = Cr = **250,000**. **Balanced.**

**Key insight:** Same HTM amortized-cost model as Q1 with **all numbers changed**. The period-end adjusting entry always pairs **Interest Receivable** (stated × time) with **investment amortization** so that Interest Revenue equals **effective rate × beginning amortized cost × time**.

---

### Q3 — CORE alternate angle — HTM premium: period-end interest JE, presentation, early sale, maturity
**LO:** LO 14-1  
**Concept:** HTM purchased at a **premium**; effective-interest amortization reducing investment and interest revenue; period-end interest JE on an interest date; BS presentation; sale before maturity; maturity settlement  
**Scenario:**  
**Cascade Harbor Holdings** purchases **$200,000 face** of **Meridian Telecom Corp.** 8% bonds on **January 1, Year 1**, when the market yield is **5%**. Interest is paid **annually each December 31**. Bonds mature **December 31, Year 3**. Cascade has the intent and ability to hold to maturity and uses the **effective interest method**. Cascade’s reporting year ends December 31 (interest date).

**Required:**  
a. Compute the **January 1, Year 1 purchase price** (nearest dollar) and record the **initial recognition JE**.  
b. Prepare the **3-period effective-interest amortization schedule** (premium).  
c. Prepare the **December 31, Year 1 period-end journal entry** for cash interest and premium amortization. Show the investment amount on the **December 31, Year 1 balance sheet** and interest revenue on the **Year 1 income statement**.  
d. **Disposal alternative:** Assume instead that on **January 1, Year 3** (after the Dec. 31, Year 2 interest entry), Cascade sells the bonds for **$204,800** because of a **significant unforeseen deterioration in Meridian’s creditworthiness**. Record the sale.  
e. **Maturity path:** Assume Cascade instead holds the bonds. After the final Dec. 31, Year 3 interest entry, record **maturity collection** of face value.

**Answer key:**  

**a. Purchase at premium — initial recognition**

Annual cash interest = 8% × $200,000 = **$16,000**.  
Price = `=−PV(0.05,3,16000,200000)` → **$216,339**.  
Premium = 216,339 − 200,000 = **$16,339**.  
Classification: **HTM** at amortized cost (market rate **<** stated rate → premium).

| Account | Debit | Credit |
|---|---:|---:|
| Investment in HTM Securities—Meridian Bonds | 216,339 | |
| Cash | | 216,339 |
| *Purchase Meridian 8% bonds as HTM at premium* | | |

**Check:** Dr = Cr = **216,339**. **Balanced.**

**b. Effective-interest amortization schedule — premium**

| Date | Cash (8% × face) | Interest revenue (5% × beg. CV) | Premium amort. | Amortized cost (end) |
|---|---:|---:|---:|---:|
| Jan. 1, Y1 | — | — | — | **216,339** |
| Dec. 31, Y1 | 16,000 | 10,817 | 5,183 | 211,156 |
| Dec. 31, Y2 | 16,000 | 10,558 | 5,442 | 205,714 |
| Dec. 31, Y3 | 16,000 | 10,286 | 5,714 | **200,000** |
| **Totals** | **48,000** | **31,661** | **16,339** | |

First period: \(216{,}339 \times 0.05 = 10{,}816.95 → 10{,}817\); premium amort. = 16,000 − 10,817 = **5,183**; end CV = 216,339 − 5,183 = **211,156**.  
Final period plugged so end CV = face; total premium amort. = **16,339**.

**c. December 31, Year 1 — period-end interest + premium amortization (interest date)**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 16,000 | |
| Investment in HTM Securities—Meridian Bonds | | 5,183 |
| Interest Revenue | | 10,817 |
| *Receive annual interest; amortize premium (reduces revenue & CV)* | | |

**Check:** Dr = **16,000**; Cr = 5,183 + 10,817 = **16,000**. **Balanced.**

**Financial statement presentation — Dec. 31 / Year 1**

| Balance sheet (assets) | | Income statement | |
|---|---:|---|---:|
| Investment in HTM securities | **$211,156** | Interest revenue | **$10,817** |

No fair-value adjustment is recorded for HTM under amortized cost.

**d. January 1, Year 3 — sale before maturity (unforeseen credit deterioration)**

Amortized cost after Dec. 31, Year 2 entry = **$205,714**.  
Cash proceeds = **$204,800**.  
Realized **loss** = 205,714 − 204,800 = **$914**.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 204,800 | |
| Loss on Sale of Investment | 914 | |
| Investment in HTM Securities—Meridian Bonds | | 205,714 |
| *Sell HTM before maturity; recognize realized loss in NI* | | |

**Check:** Dr = 204,800 + 914 = **205,714**; Cr = **205,714**. **Balanced.**

*Note:* Sale due to significant issuer credit deterioration is an example of an **unforeseen circumstance** that is **not inconsistent** with the original HTM classification for remaining securities (ASC 320 guidance summarized in the chapter). Realized gain/loss is recognized in **net income**.

**e. Maturity path — December 31, Year 3**

After the final interest/premium entry, CV = **$200,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 200,000 | |
| Investment in HTM Securities—Meridian Bonds | | 200,000 |
| *Collect face at maturity* | | |

**Check:** Dr = Cr = **200,000**. **Balanced.**

**Key insight:** At a **premium**, cash interest **exceeds** effective interest revenue; the excess **reduces** both Interest Revenue and the HTM carrying amount until amortized cost equals face at maturity. Period-end on an interest date books cash + amortization in one JE. Early sale compares **proceeds to amortized cost** (not original cost); holding to maturity settles at face with no gain/loss after full amortization.

---

### Q4 — MC — HTM classification and measurement method
**LO:** LO 14-1  
**Concept:** Classification criteria for amortized-cost (HTM) debt securities vs. other debt categories  

**Question:**  
On March 1, **Pinnacle Marine Corp.** acquires corporate bonds. Management states it has **both** the positive intent and the ability to hold the bonds until contractual maturity and does **not** plan to sell them to manage liquidity or interest-rate risk. Under U.S. GAAP as applied in this chapter’s LO 14-1, how should Pinnacle **initially and subsequently measure** these debt securities (absent impairment and absent a fair-value option election)?

- A) Fair value each period, with unrealized holding gains and losses in **net income** (FV-NI / trading-type)  
- B) Fair value each period, with unrealized holding gains and losses in **OCI** (FV-OCI / AFS-type)  
- C) **Amortized cost** (acquisition cost adjusted for premium or discount amortization); ignore fair-value changes for carrying amount  
- D) Lower of amortized cost or fair value each period, with all declines in net income  

**Answer:** **C.**  
Debt securities that the investor has the **positive intent and ability** to hold to maturity are classified as **held-to-maturity** and measured at **amortized cost**. Changes in fair value are not recognized in the accounts (they are disclosed). FV-NI and FV-OCI apply to other debt classifications (LO 14-2 / LO 14-3), not to plain HTM amortized-cost accounting under LO 14-1.

---

### Q5 — MC — Period-end adjusting entry components for HTM at discount
**LO:** LO 14-1  
**Concept:** Period-end adjusting JE when year-end falls between interest payment dates (discount HTM)  

**Question:**  
An investor holds an HTM bond investment purchased at a **discount**, accounted for under the **effective interest method**. The company’s year-end falls **two months after** the last interest payment date and **ten months before** the next interest payment date. Which description correctly states the **year-end adjusting entry** (ignore income taxes)?

- A) Debit Interest Revenue and credit Investment in HTM for two months of discount amortization only; no Interest Receivable  
- B) Debit Interest Receivable (stated interest × 2/12), debit Investment in HTM (discount amort. for 2/12), and credit Interest Revenue (effective interest for 2/12)  
- C) Debit Fair Value Adjustment and credit Unrealized Gain—OCI for the increase in fair value since purchase  
- D) Debit Cash and credit Interest Revenue for two months of stated interest  

**Answer:** **B.**  
Between interest dates, the investor accrues **Interest Receivable** for the contractual (stated) interest earned and recognizes **Interest Revenue** using the **effective rate × beginning amortized cost × time**. For a **discount**, the difference increases the **Investment in HTM** account. Fair-value adjustments are **not** recorded for HTM under amortized cost (eliminates C). Cash is not debited until interest is actually received (eliminates D).

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on all entries)
- [x] Math recomputed (PV, amortization schedules roll to face; period-end fractions reconcilable to full-period schedule)
- [x] Core demo not sidebar-only (HTM amortized cost path: purchase → schedule → period-end → disposal/maturity — Demo 14-1A/B/C style)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (exactly 2 classification/method MCs)
- [x] Emphasis angle **period_end_adjusting_JE** featured in Q1, Q2, Q3, and Q5
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
- [x] Original company names/numbers (not textbook Bold/Rush $100,000 demos)
