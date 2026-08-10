# Agent 287 — CORE DEMO — LO 17-5

**Chapter:** 17  
**LO title:** Account for complex operating leases for a lessee  
**Critical gap LO:** yes  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **Initial recognition JE:** pre-commencement lease incentive liability and initial direct costs (IDC); commencement reclass into ROU asset and lease liability at PV of lease payments
- **Subsequent measurement schedule:** lease liability amortization (effective interest / annuity-due); ROU reduction = straight-line lease expense − period “interest”
- **Period-end adjusting JE (emphasis):** single **Lease expense** entry each year-end (Dr Lease Expense; Cr Lease Liability for accrued “interest”; Cr ROU for plug) so total cost is straight-line
- **Disposal / maturity / settlement JE:** final payment clears liability; final period-end entry zeros ROU (interest = 0 after last payment if paid at period start)
- **Classification / presentation / disclosure:** five ASC 842 criteria → operating; single lease expense in income from continuing operations; full cash payment in operating SCF; current vs noncurrent lease liability split
- **Number-variant twin:** same complex operating path with all different amounts
- **Total lease cost for SL expense:** (undiscounted fixed payments + IDC − incentives) ÷ number of periods

**Method note (complex operating vs basic operating / finance):**  
Measurement of liability and ROU at commencement is the same as a complex finance lease (IDC added, incentives subtracted). **After commencement**, the lessee records **one straight-line lease expense** each period (not separate interest + amortization). ROU is reduced only by the residual of that single expense after “interest” on the liability.

---

### Q1 — CORE — Complex operating lease with incentive, IDC, full schedules, period-end adjusting JEs, maturity

**LO:** LO 17-5  
**Concept:** Initial recognition of complex operating lease (incentive + IDC); liability and ROU schedules; **period-end adjusting JE** for straight-line lease expense; maturity zero-out  
**Scenario:**  
**Pinecrest Packaging Co.** (calendar year) leases specialized-looking but **routinely re-leased** packaging equipment from **Harbor Equipment LLC**. Lease commencement is **January 1, Year 1**. Pinecrest’s fiscal year ends **December 31**.

**Facts:**
1. Noncancellable **3-year** lease; three annual payments of **$50,000** each, payable **January 1 of Year 1, Year 2, and Year 3** (annuity due).
2. Estimated economic life of the equipment: **8 years**. Fair value at commencement: **$250,000**. Asset **reverts** to Harbor at lease end. **No** purchase option. Harbor regularly leases similar equipment to other customers (alternative use exists).
3. Unguaranteed residual value estimated by Harbor: **$70,000** (not guaranteed by Pinecrest).
4. Harbor’s implicit rate is **7%** and is **known** to Pinecrest. (Use this rate.)
5. **Before** commencement, Harbor paid Pinecrest **$8,000** cash as a lease incentive related to Pinecrest’s move from a prior facility. Pinecrest also paid **$2,000** cash in **initial direct costs** (legal fees to execute the lease).
6. Pinecrest has **not** elected the short-term lease expedient. Payments are fixed (no variable payments).

**Required:**  
a. Record journal entries **prior to** lease commencement for the incentive received and the IDC paid.  
b. Classify the lease for the **lessee** (support with all five criteria).  
c. Compute the **lease liability** and **right-of-use (ROU) asset** at commencement.  
d. Prepare the **lease liability schedule** and the **ROU asset schedule**.  
e. Prepare **all Year 1** journal entries (commencement, Jan 1 payment, **Dec 31 period-end adjusting JE**—emphasis).  
f. Show Year 1 **balance sheet** (ROU; current and noncurrent lease liability) and **income statement** (lease expense).  
g. Prepare **Year 2** journal entries (Jan 1 payment + Dec 31 period-end adjusting).  
h. Prepare **Year 3** journal entries through **maturity** (Jan 1 final payment + Dec 31 final adjusting that settles ROU).  
i. **Variant:** Assume instead that the **first** $50,000 payment was made **before** commencement (debit Prepaid Lease Payment). Prepare only the **revised January 1, Year 1 commencement-related entries** (recognition + reclass of prepayment).  

**Answer key:**  

**a. Prior to commencement**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 8,000 | |
| Lease Incentive Liability | | 8,000 |
| *Lease incentive received before commencement* | | |

**Check:** Dr 8,000 = Cr 8,000. **Balanced.**

| Account | Debit | Credit |
|---|---:|---:|
| Initial Direct Cost | 2,000 | |
| Cash | | 2,000 |
| *IDC (incremental legal fees to execute lease)* | | |

**Check:** Dr 2,000 = Cr 2,000. **Balanced.**

**b. Classification — operating lease** (none of the five criteria met)

| Criterion | Analysis | Met? |
|---|---|---|
| 1. Ownership transfer | Asset reverts to Harbor | No |
| 2. Purchase option | None | No |
| 3. Lease term length | 3 ÷ 8 = 37.5% < 75% | No |
| 4. PV of lease payments | PV of payments **$140,400.91** − incentive **$8,000** = **$132,400.91** < 90% × $250,000 = **$225,000** | No |
| 5. No alternative use | Harbor routinely re-leases similar equipment | No |

→ **Operating lease** for the lessee.

**c. Lease liability and ROU at commencement**

Lease liability = PV of annuity-due payments:  
\[
PV = 50{,}000 + \frac{50{,}000}{1.07} + \frac{50{,}000}{1.07^{2}} = \$140{,}400.91
\]  
(Excel: `=PV(0.07,3,-50000,0,1)`)

| Component | Amount |
|---|---:|
| Initial measurement of lease liability | $140,400.91 |
| − Lease incentive received | (8,000.00) |
| + Initial direct costs incurred | 2,000.00 |
| **Right-of-use asset** | **$134,400.91** |

**d. Schedules**

**Lease liability schedule**

| Date | Lease payment | Interest on liability | Liability reduction | Lease liability balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (start) | | | | 140,400.91 |
| Jan 1, Y1 | 50,000.00 | 0.00 | 50,000.00 | 90,400.91 |
| Jan 1, Y2 | 50,000.00 | 6,328.06 | 43,671.94 | 46,728.97 |
| Jan 1, Y3 | 50,000.00 | 3,271.03 | 46,728.97 | 0.00 |
| **Totals** | **150,000.00** | **9,599.09** | **140,400.91** | |

Interest checks: \(90{,}400.91 \times 0.07 = 6{,}328.0637 \rightarrow 6{,}328.06\); \(46{,}728.97 \times 0.07 = 3{,}271.0279 \rightarrow 3{,}271.03\).

**ROU asset schedule**  
Straight-line lease expense = total lease cost ÷ 3:  
Total cost = \(50{,}000 \times 3 + 2{,}000 - 8{,}000 = 144{,}000\);  
SL expense = \(144{,}000 / 3 = \$48{,}000\) per year.

| Date | Lease expense | Interest on liability | ROU reduction | ROU balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 (start) | | | | 134,400.91 |
| Dec 31, Y1 | 48,000.00 | 6,328.06 | 41,671.94 | 92,728.97 |
| Dec 31, Y2 | 48,000.00 | 3,271.03 | 44,728.97 | 48,000.00 |
| Dec 31, Y3 | 48,000.00 | 0.00 | 48,000.00 | 0.00 |
| **Totals** | **144,000.00** | **9,599.09** | **134,400.91** | |

**e. Year 1 journal entries**

**January 1, Year 1 — Commencement (reclass incentive & IDC; record ROU and liability)**

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 134,400.91 | |
| Lease Incentive Liability | 8,000.00 | |
| Lease Liability | | 140,400.91 |
| Initial Direct Cost | | 2,000.00 |
| *Recognize complex operating lease ROU and liability* | | |

**Check:** Dr 134,400.91 + 8,000.00 = 142,400.91; Cr 140,400.91 + 2,000.00 = 142,400.91. **Balanced.**

**January 1, Year 1 — Lease payment**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 50,000.00 | |
| Cash | | 50,000.00 |

**Check:** Dr = Cr = 50,000. **Balanced.**

**December 31, Year 1 — Period-end adjusting JE (emphasis)**  
Single lease cost; accrue “interest” on liability and reduce ROU for residual.

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 48,000.00 | |
| Lease Liability | | 6,328.06 |
| Right-of-Use Asset | | 41,671.94 |
| *Straight-line operating lease expense for Year 1* | | |

**Check:** Dr 48,000.00 = Cr 6,328.06 + 41,671.94 = 48,000.00. **Balanced.**

**f. Year 1 financial statement effects**

**Balance sheet — December 31, Year 1**  
- Right-of-use asset (operating): \(134{,}400.91 - 41{,}671.94 = \$92{,}728.97\)  
- Lease liability total: \(90{,}400.91 + 6{,}328.06 = \$96{,}728.97\)  
  - Current: **$50,000.00** (next payment)  
  - Noncurrent: \(96{,}728.97 - 50{,}000 = \$46{,}728.97\)

**Income statement — Year 1**  
- Lease expense (in income from continuing operations): **$48,000**

**g. Year 2 journal entries**

**January 1, Year 2 — Payment**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 50,000.00 | |
| Cash | | 50,000.00 |

**Check:** Dr = Cr = 50,000. **Balanced.**

**December 31, Year 2 — Period-end adjusting JE (emphasis)**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 48,000.00 | |
| Lease Liability | | 3,271.03 |
| Right-of-Use Asset | | 44,728.97 |

**Check:** Dr 48,000.00 = Cr 3,271.03 + 44,728.97. **Balanced.**

**h. Year 3 — maturity / settlement**

**January 1, Year 3 — Final payment**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 50,000.00 | |
| Cash | | 50,000.00 |

**Check:** Dr = Cr = 50,000. After payment, lease liability = **$0**.

**December 31, Year 3 — Final period-end adjusting JE (zeros ROU)**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 48,000.00 | |
| Right-of-Use Asset | | 48,000.00 |
| *No interest remaining; entire SL expense reduces ROU* | | |

**Check:** Dr = Cr = 48,000. ROU ends at **$0**. Liability remains **$0**.

**i. Prepaid first payment variant (commencement only)**  
Gross liability still $140,400.91; ROU still $134,400.91. After reclass of prepaid payment, **net** liability = \(140{,}400.91 - 50{,}000 = \$90{,}400.91\).

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 134,400.91 | |
| Lease Incentive Liability | 8,000.00 | |
| Lease Liability | | 140,400.91 |
| Initial Direct Cost | | 2,000.00 |

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 50,000.00 | |
| Prepaid Lease Payment | | 50,000.00 |
| *Apply prepayment against lease liability at commencement* | | |

**Check:** Both entries balance. Net liability after commencement = **$90,400.91**.

**Key insight:** Complex **operating** leases use finance-lease-style **initial** measurement (IDC ↑ ROU; incentives ↓ ROU), but **period-end adjusting entries** record a **single straight-line Lease Expense**. The “interest” computed on the liability is **not** Interest Expense—it only splits the single expense between increasing the liability and reducing the ROU asset.

---

### Q2 — CORE number variant — Complex operating lease (incentive + IDC), schedules, period-end adjusting, maturity

**LO:** LO 17-5  
**Concept:** Number-variant twin—complex operating lessee accounting with incentive, IDC, liability/ROU schedules, and period-end straight-line adjusting JEs  
**Scenario:**  
**Blue Mesa Outfitters** (calendar year) leases warehouse racking from **Summit Capital Leasing**. Commencement: **January 1, Year 1**.

**Facts:**
1. **3-year** noncancellable lease; payments of **$40,000** due **January 1** of each of Years 1–3.
2. Economic life **7 years**; fair value at commencement **$200,000**; asset reverts to lessor; **no** purchase option; lessor has alternative uses for the racking.
3. Implicit rate **5%**, known to Blue Mesa.
4. Before commencement: lessor paid Blue Mesa a **$6,000** cash lease incentive; Blue Mesa paid **$1,500** IDC (broker commission).
5. Residual is **unguaranteed**.

**Required:**  
a. Pre-commencement JEs (incentive + IDC).  
b. Lessee classification (brief support).  
c. Lease liability and ROU at commencement.  
d. Liability schedule and ROU schedule.  
e. Full Year 1 JEs including **Dec 31 period-end adjusting JE**.  
f. Year 1 BS (ROU; current/noncurrent liability) and IS (lease expense).  
g. Year 2 payment + period-end adjusting JE.  
h. Year 3 final payment + final period-end JE (maturity).

**Answer key:**  

**a. Pre-commencement**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 6,000 | |
| Lease Incentive Liability | | 6,000 |

| Account | Debit | Credit |
|---|---:|---:|
| Initial Direct Cost | 1,500 | |
| Cash | | 1,500 |

Both **balanced**.

**b. Classification — operating**  
- No ownership transfer; no PO.  
- Term 3/7 ≈ 42.9% < 75%.  
- PV of payments = **$114,376.42**; net of incentive for criterion 4: \(114{,}376.42 - 6{,}000 = \$108{,}376.42\) < 90% × $200,000 = **$180,000**.  
- Alternative use exists.  
→ **Operating lease**.

**c. Liability and ROU**  
\[
PV = 40{,}000 + \frac{40{,}000}{1.05} + \frac{40{,}000}{1.05^{2}} = \$114{,}376.42
\]  
(`=PV(0.05,3,-40000,0,1)`)

| Component | Amount |
|---|---:|
| Lease liability | $114,376.42 |
| − Incentive | (6,000.00) |
| + IDC | 1,500.00 |
| **ROU asset** | **$109,876.42** |

**d. Schedules**

Total lease cost = \(40{,}000 \times 3 + 1{,}500 - 6{,}000 = 115{,}500\);  
SL expense = \(115{,}500 / 3 = \$38{,}500\).

**Lease liability schedule**

| Date | Payment | Interest | Reduction | Balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 start | | | | 114,376.42 |
| Jan 1, Y1 | 40,000.00 | 0.00 | 40,000.00 | 74,376.42 |
| Jan 1, Y2 | 40,000.00 | 3,718.82 | 36,281.18 | 38,095.24 |
| Jan 1, Y3 | 40,000.00 | 1,904.76 | 38,095.24 | 0.00 |

Interest: \(74{,}376.42 \times 0.05 = 3{,}718.821 \rightarrow 3{,}718.82\); \(38{,}095.24 \times 0.05 = 1{,}904.762 \rightarrow 1{,}904.76\).

**ROU schedule**

| Date | Lease expense | Interest | ROU reduction | ROU balance |
|---|---:|---:|---:|---:|
| Jan 1, Y1 start | | | | 109,876.42 |
| Dec 31, Y1 | 38,500.00 | 3,718.82 | 34,781.18 | 75,095.24 |
| Dec 31, Y2 | 38,500.00 | 1,904.76 | 36,595.24 | 38,500.00 |
| Dec 31, Y3 | 38,500.00 | 0.00 | 38,500.00 | 0.00 |

**e. Year 1 JEs**

**Jan 1, Y1 — Commencement**

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 109,876.42 | |
| Lease Incentive Liability | 6,000.00 | |
| Lease Liability | | 114,376.42 |
| Initial Direct Cost | | 1,500.00 |

**Check:** Dr 115,876.42 = Cr 115,876.42. **Balanced.**

**Jan 1, Y1 — Payment**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 40,000 | |
| Cash | | 40,000 |

**Dec 31, Y1 — Period-end adjusting JE (emphasis)**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 38,500.00 | |
| Lease Liability | | 3,718.82 |
| Right-of-Use Asset | | 34,781.18 |

**Check:** Dr 38,500 = Cr 3,718.82 + 34,781.18. **Balanced.**

**f. Year 1 statements**  
- ROU: \(109{,}876.42 - 34{,}781.18 = \$75{,}095.24\)  
- Lease liability total: \(74{,}376.42 + 3{,}718.82 = \$78{,}095.24\)  
  - Current **$40,000**; noncurrent **$38,095.24**  
- Lease expense **$38,500**

**g. Year 2**

**Jan 1, Y2**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 40,000 | |
| Cash | | 40,000 |

**Dec 31, Y2 — Period-end adjusting**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 38,500.00 | |
| Lease Liability | | 1,904.76 |
| Right-of-Use Asset | | 36,595.24 |

**Check:** Dr 38,500 = Cr 1,904.76 + 36,595.24. **Balanced.**

**h. Year 3 maturity**

**Jan 1, Y3**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 40,000 | |
| Cash | | 40,000 |

Liability → **$0**.

**Dec 31, Y3 — Final period-end adjusting**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 38,500 | |
| Right-of-Use Asset | | 38,500 |

ROU → **$0**. Both entries **balanced**.

**Key insight:** Changing the payment, rate, incentive, and IDC changes every schedule cell, but the **mechanics** are identical: PV liability → ROU = liability − incentive + IDC → **period-end** single SL lease expense with ROU reduction = expense − liability “interest.”

---

### Q3 — CORE alternate angle — Period-end adjusting from open balances; presentation; prepayment; maturity cleanup

**LO:** LO 17-5  
**Concept:** Period-end adjusting JE emphasis from incomplete books; current/noncurrent split; SCF and income-statement presentation for operating leases; prepaid-payment commencement; final settlement  
**Scenario:**  
**Ironclad Fabrication Inc.** (calendar year) has a **complex operating lease** for a paint booth (commencement was **January 1, Year 1**). Relevant facts already determined by the company:

| Item | Amount |
|---|---:|
| Annual lease payment (due each Jan 1) | $35,000 |
| Discount rate (implicit, known) | 8% |
| Lease term | 3 years |
| Lease liability immediately **after** Jan 1, Year 2 payment | $32,407.41 |
| ROU carrying amount immediately **after** Jan 1, Year 2 payment (before YE adjusting) | $65,007.41 |
| Straight-line annual lease expense (already computed from total cost) | $33,800 |
| Initial direct costs (paid before commencement, Year 1) | $1,200 |
| Lease incentive received before commencement (Year 1) | $4,800 |
| Fair value of underlying asset at commencement | $180,000 |
| Economic life | 9 years |

Additional background: asset reverts to lessor; no purchase option; lessor has alternative uses. Payments are fixed. Ironclad classifies the lease as **operating** (confirm if asked).

**Required:**  
a. Compute the **“interest”** that accrues during Year 2 and prepare the **December 31, Year 2 period-end adjusting JE only** (emphasis).  
b. After the Year 2 adjusting entry, compute **current** and **noncurrent** lease liability and **ROU** for the Dec 31, Year 2 balance sheet.  
c. Prepare **January 1, Year 3** payment and **December 31, Year 3** final adjusting JE (maturity settlement of ROU).  
d. **Presentation:** For Year 2, state (i) where lease expense appears on the income statement, (ii) SCF classification of the $35,000 cash payment for an **operating** lease, and (iii) how total expense pattern would **differ** if the same lease were **finance**.  
e. **Prepayment twist (Year 1):** Reconstruct commencement measurement: compute original lease liability (PV) and ROU. Then assume the first payment was prepaid before commencement—prepare the two Jan 1, Year 1 entries (recognize ROU/liability; reclass prepaid).  

**Answer key:**  

**a. Year 2 period-end adjusting JE (emphasis)**  
Interest for Year 2 = \(32{,}407.41 \times 0.08 = \$2{,}592.5928 \rightarrow \$2{,}592.59\).  
ROU reduction = \(33{,}800.00 - 2{,}592.59 = \$31{,}207.41\).

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 33,800.00 | |
| Lease Liability | | 2,592.59 |
| Right-of-Use Asset | | 31,207.41 |
| *Period-end only: single operating lease cost for Year 2* | | |

**Check:** Dr 33,800.00 = Cr 2,592.59 + 31,207.41. **Balanced.**

**b. December 31, Year 2 balance sheet amounts**  
- Lease liability total after accrual: \(32{,}407.41 + 2{,}592.59 = \$35{,}000.00\)  
  - **Current** $35,000 (final payment due Jan 1, Y3)  
  - **Noncurrent** $0  
- ROU: \(65{,}007.41 - 31{,}207.41 = \$33{,}800.00\)

**c. Maturity Year 3**

**January 1, Year 3 — Final payment**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 35,000 | |
| Cash | | 35,000 |

**Check:** Dr = Cr = 35,000. Liability → **$0**.

**December 31, Year 3 — Final period-end adjusting (interest = 0)**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Expense | 33,800 | |
| Right-of-Use Asset | | 33,800 |

**Check:** Dr = Cr = 33,800. ROU → **$0**.

**d. Presentation / classification**  
(i) **Lease expense $33,800** is reported as a **single amount in income from continuing operations** (not split into interest and amortization).  
(ii) SCF (lessee, operating lease): the **entire $35,000** cash payment is an **operating** cash outflow.  
(iii) If **finance**: Year 2 would show **Interest expense $2,592.59** (other expense) + **amortization of ROU** on a straight-line of the ROU over the lease term (in operating income)—**front-loaded total expense** early in the lease versus flat $33,800 operating lease expense. Over the full term, **total expense equals total lease cost** under both classifications.

**e. Reconstruct commencement + prepaid first payment**

PV of 3 payments of $35,000 at 8% annuity due:  
\[
PV = 35{,}000 + \frac{35{,}000}{1.08} + \frac{35{,}000}{1.08^{2}} = \$97{,}414.27
\]  
(`=PV(0.08,3,-35000,0,1)`)

ROU = \(97{,}414.27 - 4{,}800 + 1{,}200 = \$93{,}814.27\).

Confirm SL expense: total cost = \(35{,}000\times 3 + 1{,}200 - 4{,}800 = 101{,}400\); \(101{,}400/3 = 33{,}800\) ✓.

**Jan 1, Y1 — Commencement**

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 93,814.27 | |
| Lease Incentive Liability | 4,800.00 | |
| Lease Liability | | 97,414.27 |
| Initial Direct Cost | | 1,200.00 |

**Check:** Dr 98,614.27 = Cr 98,614.27. **Balanced.**

**Jan 1, Y1 — Apply prepaid first payment**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 35,000 | |
| Prepaid Lease Payment | | 35,000 |

**Check:** Dr = Cr = 35,000. Net liability after commencement = **$62,414.27**.

**Key insight:** Exam emphasis often drops you **mid-lease** and asks only for the **period-end adjusting JE**: compute interest on the **post-payment** liability balance, credit liability for that interest, debit **Lease Expense** for the constant SL amount, and credit **ROU** for the difference. At maturity, after the last payment, the adjusting entry has **no interest credit**—only ROU write-off equal to remaining SL expense.

---

### Q4 — MC — Classification tip: residual guarantee vs operating

**LO:** LO 17-5  
**Concept:** Classification—when a residual value guarantee can cause a lessee lease that would otherwise be operating to fail criterion 4 (PV of payments)  
**Question:**  
Pinecrest’s lease in Q1 would remain an **operating** lease under the facts given (unguaranteed residual). Which **single** change, holding all other Q1 facts constant, is **most likely** to cause Pinecrest to classify the lease as a **finance** lease?

- A) Increasing the economic life of the equipment from 8 years to 10 years  
- B) Pinecrest guaranteeing a residual such that the **present value of lease payments including the residual guarantee** (before subtracting the incentive) equals the **$250,000** fair value of the asset  
- C) Paying an additional $500 of initial direct costs  
- D) Receiving a larger cash lease incentive before commencement  

**Answer:** **B.**  
Criterion 4 compares the PV of **lease payments** (for classification, reduced by incentives received before commencement) to substantially all (often 90%) of fair value. Including a **residual value guarantee** as a lease payment can push PV above the 90% threshold → **finance** lease.  
A lengthens life and makes the term test **harder** to meet (smaller %). C and D affect ROU measurement / total cost, not a classification tripwire on their own the way a large residual guarantee does.

---

### Q5 — MC — Period-end adjusting composition (operating)

**LO:** LO 17-5  
**Concept:** Period-end adjusting JE—composition of the single operating lease expense entry  
**Question:**  
On December 31 of Year 1 of a complex **operating** lease (annuity-due payments on January 1), the lessee’s period-end adjusting entry typically:

- A) Debits Interest Expense and Amortization Expense for separate amounts that sum to straight-line cost  
- B) Debits **Lease Expense** for the straight-line amount, credits **Lease Liability** for the period’s effective interest on the liability, and credits **Right-of-Use Asset** for the remainder  
- C) Debits Lease Liability and credits Cash for the annual payment  
- D) Debits ROU Asset and credits Lease Liability only (no income-statement account)

**Answer:** **B.**  
Operating lease period-end adjusting JEs record **one** Lease Expense (straight-line total cost). The liability is accreted by the effective interest amount (not labeled Interest Expense), and ROU is reduced for the plug. A describes **finance** lease expense pattern/presentation. C is the **payment** date entry (often Jan 1), not the Dec 31 adjusting entry. D is commencement measurement, not period-end.

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (PV annuity-due; interest = bal × r; SL = (Σ payments + IDC − incentive) / n; schedules roll to zero)
- [x] Core demo path (Demo 17-5 style complex operating lessee)—not sidebar-only
- [x] **LO:** and **Concept:** on every item
- [x] MC ≤ 2 (Q4, Q5)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE (emphasis), disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
