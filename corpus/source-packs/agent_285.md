# Agent 285 — CORE DEMO — LO 17-3

**Chapter:** 17  
**LO title:** Account for a basic operating lease for a lessee  
**Critical gap LO:** yes  
**Emphasis:** period_end_adjusting_JE

## Concept list for this pack
- **Operating classification:** none of the five ASC 842 lessee criteria met → operating lease
- **Initial recognition JE:** Dr Right-of-use asset / Cr Lease liability at PV of lease payments (basic case: ROU = liability; no IDC, prepaid, or incentives)
- **Discount rate:** rate implicit in the lease if known; otherwise lessee incremental borrowing rate
- **Subsequent measurement schedule:** lease liability roll-forward under the **effective interest** method; first annuity-due payment is **all principal**
- **Straight-line lease expense:** total undiscounted lease payments ÷ number of periods (= cash payment when only fixed periodic payments)
- **Period-end adjusting JE (emphasis):** single **Lease expense** entry — Dr Lease expense (SL amount), Cr Lease liability (‘interest’ accretion), Cr Right-of-use asset (plug = expense − interest). ‘Interest’ and ROU reduction are **not** separate income-statement lines
- **Optional two-part YE form:** (1) Dr ROU / Cr Lease liability for interest; (2) Dr Lease expense / Cr ROU for full SL amount — same net effect
- **Disposal / maturity / settlement:** final payment zeros liability; final-year YE entry is Dr Lease expense / Cr ROU only (no liability accretion after last payment)
- **Classification / presentation:** single lease expense in income from continuing operations; ROU and operating lease liabilities presented separately from finance leases; current vs noncurrent liability split
- **Number-variant twin:** same operating-lease life cycle with all amounts, rates, and terms changed

---

### Q1 — CORE — Basic operating lease full life cycle (emphasis: period-end adjusting JE)
**LO:** LO 17-3  
**Concept:** Classify as operating; measure ROU/liability; liability + ROU schedules; initial JEs; **period-end single lease-expense adjusting JE**; maturity; BS/IS presentation  
**Scenario:**  
On **January 1 of Year 1** (commencement), **Riverglen Industrial Supply Co.** (calendar-year lessee) enters a noncancellable lease with **Summit Asset Finance** for warehouse forklift equipment that Summit routinely leases to other customers. Facts:

1. **Lease term:** 4 years. Equipment reverts to Summit at end of term.  
2. **Four** annual lease payments of **$22,000**, payable **January 1** of Year 1, Year 2, Year 3, and Year 4 (**annuity due**).  
3. Fair value of equipment at commencement = **$140,000**.  
4. Estimated remaining economic life = **10 years**.  
5. No renewal option; no purchase option; no residual value guarantee by Riverglen.  
6. Summit’s **implicit rate = 5%**, **known** by Riverglen. Riverglen’s incremental borrowing rate = **6%**.  
7. No initial direct costs, prepaid rent, or lease incentives (basic case: ROU = lease liability at commencement before the first payment).  
8. Round the commencement PV and subsequent schedule amounts to the **nearest dollar**. Final-period interest is **plugged** so the liability clears exactly. Credit the ROU asset **directly** for the period reduction (chapter convention).

**Required:**  
a. Evaluate the five lease classification criteria and conclude finance vs **operating** for Riverglen. State the discount rate used.  
b. Measure the lease liability and right-of-use asset at commencement (before the first payment).  
c. Prepare the complete **lease liability schedule** and **right-of-use asset schedule**.  
d. Prepare **all Year 1 journal entries** (commencement recognition, first payment, and **December 31 period-end adjusting JE** — emphasize the single lease-expense form).  
e. Show **Year 1** income statement lease-related amount and **December 31, Year 1** balance sheet (ROU; current and noncurrent lease liability).  
f. Prepare lessee journal entries for **Year 2** and **Year 3** (payment + period-end adjusting).  
g. Prepare **Year 4 maturity / settlement** entries (final payment and final period-end ROU reduction) and confirm both accounts are zero after lease end.

**Answer key:**

**(a) Classification — operating lease**

| Criterion | Analysis | Met? |
|---|---|:---:|
| 1. Ownership transfer | Asset reverts to Summit | No |
| 2. Purchase option reasonably certain | None | No |
| 3. Lease term major part of economic life | 4 / 10 = **40% < 75%** | No |
| 4. PV of lease payments substantially all of FV | PV = **$81,911** < 90% × $140,000 = **$126,000** | No |
| 5. No alternative use to lessor | Equipment routinely re-leased; alternative uses exist | No |

→ **None** of the five criteria met → **operating lease** to Riverglen.  
**Discount rate:** **5%** implicit rate (known) — preferred over 6% IBR.

**(b) Initial measurement**  
Excel: `=PV(0.05,4,-22000,0,1)` → **$81,911.46** → rounded **$81,911**.

- Lease liability (commencement) = **$81,911**  
- ROU asset (basic case) = **$81,911**  
- Straight-line lease expense each year = total cash payments ÷ 4 = ($22,000 × 4) / 4 = **$22,000** (equals the periodic cash payment when only fixed payments exist)

**(c) Lease liability schedule (effective interest)**  
First payment on commencement day is **100% principal**. Later payments = interest on beginning liability + principal reduction. Final interest plugged so ending liability = 0.

| Date | Lease payment | Interest on liability (5%) | Liability change | Lease liability |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (commencement) | — | — | — | **81,911** |
| Jan 1, Y1 | 22,000 | 0 | 22,000 | 59,911 |
| Jan 1, Y2 | 22,000 | 2,996 | 19,004 | 40,907 |
| Jan 1, Y3 | 22,000 | 2,045 | 19,955 | 20,952 |
| Jan 1, Y4 | 22,000 | 1,048* | 20,952 | 0 |
| **Totals** | **88,000** | **6,089** | **81,911** | |

\*Plug: remaining liability $20,952; interest = $22,000 − $20,952 = **$1,048** (raw $20,952 × 5% = $1,047.60).  
Checks: $59,911 × 5% = $2,995.55 → **$2,996**; $40,907 × 5% = $2,045.35 → **$2,045**. Total interest = $88,000 − $81,911 = **$6,089**.

**Right-of-Use asset schedule**  
ROU reduction each year = straight-line lease expense − ‘interest’ on liability for that year (from the next payment’s interest column). Final year: after the last payment the liability is zero, so YE reduction of ROU = full expense (remaining ROU).

| Date | Lease expense (SL) | Interest on liability | ROU asset change | ROU asset |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (commencement) | — | — | — | **81,911** |
| Dec 31, Y1 | 22,000 | 2,996 | 19,004 | 62,907 |
| Dec 31, Y2 | 22,000 | 2,045 | 19,955 | 42,952 |
| Dec 31, Y3 | 22,000 | 1,048 | 20,952 | 22,000 |
| Dec 31, Y4 | 22,000 | 0 | 22,000 | 0 |
| **Totals** | **88,000** | **6,089** | **81,911** | |

**(d) Year 1 journal entries (emphasis: period-end adjusting JE)**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y1 | Right-of-Use Asset | 81,911 | |
| | Lease Liability | | 81,911 |
| | *Record ROU asset and lease liability at commencement* | | |
| Jan 1, Y1 | Lease Liability | 22,000 | |
| | Cash | | 22,000 |
| | *First lease payment (all principal)* | | |
| **Dec 31, Y1** | **Lease Expense** | **22,000** | |
| | **Lease Liability** | | **2,996** |
| | **Right-of-Use Asset** | | **19,004** |
| | *Period-end adjusting: single SL lease expense; accrete liability; reduce ROU* | | |

**Balance checks:** Dr = Cr on every entry ($81,911; $22,000; $22,000 = $2,996 + $19,004). **Balanced.**

*Optional two-part form of the same Dec 31 adjusting entry (same net effect):*

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 2,996 | |
| Lease Liability | | 2,996 |
| Lease Expense | 22,000 | |
| Right-of-Use Asset | | 22,000 |

**(e) Year 1 financial statement impact**

**Income statement — Year 1**  
- **Lease expense (single amount, operating expense / income from continuing operations):** **$22,000**  
- *Not* reported as separate interest expense + amortization expense (that pattern is for **finance** leases).

**Balance sheet — Dec 31, Year 1**  
- ROU asset: $81,911 − $19,004 = **$62,907**  
- Lease liability total: $59,911 + $2,996 = **$62,907**  
  - **Current** lease liability = next payment **$22,000**  
  - **Noncurrent** lease liability = $62,907 − $22,000 = **$40,907**  

(Note: in a basic operating lease with no commencement adjustments, YE ROU equals YE total lease liability.)

**(f) Year 2 and Year 3**

**Year 2**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y2 | Lease Liability | 22,000 | |
| | Cash | | 22,000 |
| Dec 31, Y2 | Lease Expense | 22,000 | |
| | Lease Liability | | 2,045 |
| | Right-of-Use Asset | | 19,955 |

After Dec 31, Y2: ROU = **$42,952**; total liability = $40,907 + $2,045 = **$42,952** (current $22,000; noncurrent $20,952).

**Year 3**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y3 | Lease Liability | 22,000 | |
| | Cash | | 22,000 |
| Dec 31, Y3 | Lease Expense | 22,000 | |
| | Lease Liability | | 1,048 |
| | Right-of-Use Asset | | 20,952 |

After Dec 31, Y3: ROU = **$22,000**; total liability = **$22,000** (all current).

**(g) Year 4 — maturity / settlement**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y4 | Lease Liability | 22,000 | |
| | Cash | | 22,000 |
| | *Final payment extinguishes liability* | | |
| Dec 31, Y4 | Lease Expense | 22,000 | |
| | Right-of-Use Asset | | 22,000 |
| | *Final SL lease expense; no liability accretion (liability already $0)* | | |

After Year 4 entries: **ROU = $0**, **Lease liability = $0**. Asset returns to Summit; no residual guarantee JE.

**Key insight:** Operating-lease **period-end** accounting forces a **straight-line single lease expense**. The liability still accretes under effective interest for BS measurement, but that ‘interest’ only splits the credit side of the YE entry between liability and ROU — it is **not** an income-statement interest line.

---

### Q2 — CORE number variant — Basic operating lease life cycle
**LO:** LO 17-3  
**Concept:** Number-variant twin — recompute PV, liability/ROU schedules, initial and period-end JEs, maturity  
**Scenario:**  
On **January 1 of Year 1**, **Oakridge Clinical Labs Inc.** leases a nonspecialized imaging console from **Prairie Capital Leasing**.

1. Noncancellable **3-year** lease; asset reverts to Prairie; no purchase/renewal option; no residual guarantee.  
2. **Three** annual payments of **$30,000** due **each January 1** beginning Year 1 (annuity due).  
3. Fair value at commencement = **$200,000**; economic life = **8 years**.  
4. Implicit rate **6%**, known by Oakridge. Oakridge’s IBR = **7.5%**.  
5. Fiscal year-end **December 31**. No ROU adjustments at commencement. Round to nearest dollar; plug final-period interest.

**Required:**  
a. Classify the lease for the lessee and state the discount rate.  
b. Measure commencement ROU asset and lease liability; state annual SL lease expense.  
c. Prepare the **full lease liability schedule** and **ROU asset schedule**.  
d. Journal entries for **Year 1** (commencement, payment, **Dec 31 period-end adjusting**).  
e. Dec 31, Year 1: ROU carrying amount; current vs noncurrent lease liability; Year 1 lease expense.  
f. Journal entries for **Year 3 only** (final payment Jan 1 and final Dec 31 lease expense), and confirm zero balances.  
g. State total ‘interest’ on the liability over the lease term from the schedule.

**Answer key:**

**(a) Classification — operating**

| Criterion | Analysis | Met? |
|---|---|:---:|
| 1. Ownership transfer | Reverts to lessor | No |
| 2. Purchase option | None | No |
| 3. Lease term length | 3 / 8 = **37.5% < 75%** | No |
| 4. PV substantially all of FV | PV **$85,002** < 90% × $200,000 = **$180,000** | No |
| 5. No alternative use | Nonspecialized; alternative uses | No |

→ **Operating lease.** Discount rate = **6%** implicit (known).

**(b) Measurement**  
`=PV(0.06,3,-30000,0,1)` → **$85,001.78** → **$85,002**.  
ROU = liability = **$85,002**.  
SL lease expense = ($30,000 × 3) / 3 = **$30,000** per year.

**(c) Schedules**

**Lease liability schedule**

| Date | Lease payment | Interest (6%) | Liability change | Lease liability |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (commencement) | — | — | — | **85,002** |
| Jan 1, Y1 | 30,000 | 0 | 30,000 | 55,002 |
| Jan 1, Y2 | 30,000 | 3,300 | 26,700 | 28,302 |
| Jan 1, Y3 | 30,000 | 1,698* | 28,302 | 0 |
| **Totals** | **90,000** | **4,998** | **85,002** | |

\*$55,002 × 6% = $3,300.12 → **$3,300**; final interest plug $30,000 − $28,302 = **$1,698** (raw $28,302 × 6% = $1,698.12).  
Total interest check: $90,000 − $85,002 = **$4,998**.

**ROU asset schedule**

| Date | Lease expense | Interest on liability | ROU change | ROU asset |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (commencement) | — | — | — | **85,002** |
| Dec 31, Y1 | 30,000 | 3,300 | 26,700 | 58,302 |
| Dec 31, Y2 | 30,000 | 1,698 | 28,302 | 30,000 |
| Dec 31, Y3 | 30,000 | 0 | 30,000 | 0 |
| **Totals** | **90,000** | **4,998** | **85,002** | |

**(d) Year 1 journal entries**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y1 | Right-of-Use Asset | 85,002 | |
| | Lease Liability | | 85,002 |
| Jan 1, Y1 | Lease Liability | 30,000 | |
| | Cash | | 30,000 |
| Dec 31, Y1 | Lease Expense | 30,000 | |
| | Lease Liability | | 3,300 |
| | Right-of-Use Asset | | 26,700 |

**Checks:** Dr = Cr ($85,002; $30,000; $30,000 = $3,300 + $26,700). **Balanced.**

**(e) Dec 31, Year 1 presentation**  
- ROU asset: **$58,302**  
- Total lease liability: $55,002 + $3,300 = **$58,302**  
  - Current: **$30,000**  
  - Noncurrent: **$28,302**  
- Year 1 **lease expense (single line):** **$30,000**

**(f) Year 3 maturity / settlement**

| Date | Account | Debit | Credit |
|---|---|---:|---:|
| Jan 1, Y3 | Lease Liability | 30,000 | |
| | Cash | | 30,000 |
| Dec 31, Y3 | Lease Expense | 30,000 | |
| | Right-of-Use Asset | | 30,000 |

After these entries: **ROU = $0**, **Lease liability = $0**.

**(g) Total ‘interest’ on liability over the term:** **$4,998**

**Key insight:** Changing term, payment, and rate changes the PV and the split between liability accretion and ROU reduction each year, but the **operating** pattern stays the same: one SL lease expense each period and zero balances at maturity when the asset reverts with no residual obligation.

---

### Q3 — CORE alternate angle — Period-end adjusting JEs only (emphasis)
**LO:** LO 17-3  
**Concept:** Given a liability schedule mid-life, prepare **period-end adjusting JEs** (single lease expense) and YE BS/IS amounts without re-deriving commencement  
**Scenario:**  
**Cedarline Printworks LLC** (calendar year) is the lessee on a basic **operating** lease of a commercial press. Commencement was **January 1, Year 1**. Payments of **$16,000** are due each **January 1** for **5 years** (annuity due). Discount rate **5%**. Commencement PV (and initial ROU) was measured at **$72,735**. No residual guarantee; asset reverts at end of Year 5.

Cedarline’s **lease liability schedule** (already prepared; nearest-dollar; final plug) is:

| Date | Lease payment | Interest on liability | Liability change | Lease liability |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (commencement) | — | — | — | 72,735 |
| Jan 1, Y1 | 16,000 | 0 | 16,000 | 56,735 |
| Jan 1, Y2 | 16,000 | 2,837 | 13,163 | 43,572 |
| Jan 1, Y3 | 16,000 | 2,179 | 13,821 | 29,751 |
| Jan 1, Y4 | 16,000 | 1,488 | 14,512 | 15,239 |
| Jan 1, Y5 | 16,000 | 761 | 15,239 | 0 |

Straight-line lease expense each year = **$16,000**.

**Required:**  
a. Prepare the **December 31, Year 1 period-end adjusting JE** (single lease-expense form). Show the composition of the credits.  
b. Prepare the **December 31, Year 2 period-end adjusting JE**.  
c. For **December 31, Year 2**, report: (1) ROU carrying amount, (2) total lease liability, (3) current lease liability, (4) noncurrent lease liability, (5) Year 2 lease expense on the income statement.  
d. Explain in one sentence why the Year 2 credit to Lease liability (**$2,179**) is **not** labeled Interest Expense on the income statement for an operating lease.  
e. Prepare the **December 31, Year 5** period-end entry only (assume the Jan 1, Year 5 payment already zeroed the liability).

**Answer key:**

**(a) Dec 31, Year 1 period-end adjusting JE**  
Interest on liability for Year 1 = interest column of next payment (Jan 1, Y2) = **$2,837**.  
ROU reduction = $16,000 − $2,837 = **$13,163**.

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 16,000 | |
| Lease Liability | | 2,837 |
| Right-of-Use Asset | | 13,163 |

**Check:** $16,000 = $2,837 + $13,163. **Balanced.**  
After entry: ROU = $72,735 − $13,163 = **$59,572**; total liability = $56,735 + $2,837 = **$59,572**.

**(b) Dec 31, Year 2 period-end adjusting JE**  
Interest for Year 2 = Jan 1, Y3 interest column = **$2,179**.  
ROU reduction = $16,000 − $2,179 = **$13,821**.

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 16,000 | |
| Lease Liability | | 2,179 |
| Right-of-Use Asset | | 13,821 |

**Check:** $16,000 = $2,179 + $13,821. **Balanced.**

**(c) December 31, Year 2 presentation**  
1. ROU: $59,572 − $13,821 = **$45,751**  
2. Total lease liability: $43,572 + $2,179 = **$45,751**  
3. Current lease liability: next payment **$16,000**  
4. Noncurrent lease liability: $45,751 − $16,000 = **$29,751**  
5. Year 2 income statement: **Lease expense $16,000** (single amount)

**(d)** For an operating lease, ASC 842 requires a **single lease cost** on a straight-line basis in income from continuing operations; liability accretion is used only to measure the BS liability and to compute the ROU reduction — it is **not** presented as interest expense.

**(e) Dec 31, Year 5 (maturity year, after final payment)**  
Liability already $0 after Jan 1, Y5 payment; remaining ROU before YE entry = $16,000 (equals final SL expense).

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 16,000 | |
| Right-of-Use Asset | | 16,000 |

**Balanced.** After entry: ROU = $0, liability = $0.

**Key insight (emphasis):** Once the liability schedule exists, every **period-end adjusting JE** is mechanical: Dr Lease expense for the constant SL amount; Cr Lease liability for that year’s schedule interest; Cr ROU for the residual. Exam traps include recording separate interest expense (finance pattern) or forgetting that the final year has **no** liability credit.

---

### Q4 — MC — Operating vs finance presentation (classification / presentation)
**LO:** LO 17-3  
**Concept:** Income-statement presentation of operating-lease cost vs finance-lease cost  
**Question:**  
Lessee Co. has a basic **operating** lease (none of the five classification criteria met). Annual cash lease payments are fixed and equal. Which description best matches lessee financial reporting **after commencement**?

- A) Two income-statement expenses each period: interest expense on the lease liability and amortization of the ROU asset; total expense typically **front-loaded**.  
- B) A **single** lease expense each period on a **straight-line** basis (equal amounts when only fixed payments exist), reported in income from continuing operations; ROU and lease liability still appear on the balance sheet.  
- C) No ROU asset or lease liability on the balance sheet; rent expense equal to cash paid each period only if the short-term lease election applies is irrelevant because operating leases never capitalize.  
- D) Lease liability accretes with interest expense on the income statement, but the ROU asset is not amortized until the final year.

**Answer:** **B.**  
Under ASC 842, a lessee operating lease still recognizes a ROU asset and lease liability, but subsequent P&L is a **single straight-line lease expense**. Choice A is the **finance** lease pattern. Choice C confuses pre-ASC 842 operating leases / the short-term exception (LO 17-9) with basic operating leases under current GAAP. Choice D mixes finance interest presentation with an incorrect ROU rule.

---

### Q5 — MC — Period-end credit split (method / amounts)
**LO:** LO 17-3  
**Concept:** Period-end adjusting JE composition for a basic operating lease  
**Question:**  
At December 31 of Year 2, a lessee on a basic operating lease has straight-line lease expense of **$30,000** for the year. The lease liability schedule shows interest on the liability for Year 2 of **$1,698**. Immediately before the adjusting entry, the ROU asset has a carrying amount greater than $30,000. What is the correct **period-end adjusting** entry (single-entry form)?

- A) Dr Interest Expense 1,698; Dr Amortization Expense 28,302; Cr Lease Liability 1,698; Cr Right-of-Use Asset 28,302  
- B) Dr Lease Expense 30,000; Cr Cash 30,000  
- C) Dr Lease Expense 30,000; Cr Lease Liability 1,698; Cr Right-of-Use Asset 28,302  
- D) Dr Lease Expense 30,000; Cr Lease Liability 30,000  

**Answer:** **C.**  
Operating-lease YE entry: Dr **Lease expense** for the full SL amount; Cr **Lease liability** for effective-interest accretion; Cr **ROU** for the difference ($30,000 − $1,698 = $28,302). Choice A is the **finance** dual-expense pattern. Choice B would double-count cash if payments are already recorded on payment dates (annuity due). Choice D ignores ROU reduction and overstates the liability credit.

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (PV, interest chain, plugs, ROU roll-forward, YE liability = after-payment balance + YE interest)
- [x] Core demo path for LO 17-3 (basic operating lessee — Demo 17-3 style), not sidebar-only
- [x] LO + Concept on every item
- [x] MC = 2 (classification/presentation + period-end method)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE (emphasis), disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
- [x] Original company names and numbers (not textbook Demo 17-3 figures)
