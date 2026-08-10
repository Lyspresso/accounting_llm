# Agent 20 — CORE DEMO — LO 17-11

**Chapter:** 17  
**LO title:** Explain lease modifications and lease remeasurements  
**Critical gap LO:** yes

## Concept list for this pack
- Separate lease vs single modified lease (standalone-price test)
- Lease classification reassessment triggers (term change; purchase-option assessment)
- Remeasurement-only triggers (residual probable amount; contingency → fixed)
- Remeasurement JE: adjust Lease Liability against ROU asset
- Discount-rate update rules (when to use new IBR vs original rate)
- Subsequent measurement after remeasurement (interest + ROU amort schedule)
- Settlement / exercise of purchase option after remeasurement
- Lessor reassessment only on modification

---

### Q1 — CORE — Northstar Laminating: finance lease PO reassessment, remeasurement JE, schedule, settlement
**LO:** LO 17-11  
**Concept:** Purchase-option reassessment → remeasure lease liability (updated rate) against ROU; subsequent schedule; PO settlement  
**Scenario:**  
On **January 1, Year 1**, **Northstar Laminating Co.** (lessee) leases specialty laminating equipment from Apex Equipment Finance:

| Item | Detail |
|------|--------|
| Economic life of equipment | 6 years |
| Lease term | 5 years (no renewal option) |
| Annual lease payment | **$75,000** due **beginning** of each year (Jan 1) |
| Purchase option at end of Year 5 | **$35,000** — **not** reasonably certain of exercise at commencement |
| Lessee incremental borrowing rate | **5%** (lessor’s implicit rate unknown) |
| Initial direct costs / prepayments / incentives | none |
| Classification at commencement | **Finance lease** (lease term = 5/6 of economic life ≥ 75%) |

At commencement Northstar does **not** include the purchase option in lease payments. ROU is amortized straight-line over the **5-year lease term** while the PO is not reasonably certain.

On **January 1, Year 3** (immediately **before** the Year 3 payment), product demand has strengthened and Northstar is now **reasonably certain** to exercise the $35,000 purchase option. After reassessing classification criteria, the lease **remains a finance lease**. Northstar’s current incremental borrowing rate is **4%**. The original 5% rate did **not** already reflect the purchase option, so the discount rate is **updated** to 4% for remeasurement.

**Required:**  
(a) Record the **commencement** entry on January 1, Year 1 (before the first payment) and the **first payment**.  
(b) Prepare the **lease liability amortization** through January 1, Year 3 **before** remeasurement (show interest for Years 1–2 and payments). Compute the **ROU carrying amount** on January 1, Year 3.  
(c) Compute the **remeasured lease liability** on January 1, Year 3 (3 remaining beginning-of-period payments of $75,000 plus $35,000 PO at end of Year 5, discounted at **4%**). Record the **remeasurement** entry.  
(d) Record the January 1, Year 3 **lease payment** after remeasurement. Prepare the **post-remeasurement liability schedule** through exercise of the PO, and the **December 31, Year 3** adjusting entries (interest + ROU amortization). State the remaining economic life used for ROU amortization after the PO becomes reasonably certain.  
(e) Record the **settlement** entry when the purchase option is exercised at the end of Year 5 (clear the liability). Briefly state the ROU/PPE presentation effect.

**Answer key:**

**(a) Commencement and first payment — January 1, Year 1**

PV of annuity-due lease payments (n=5, i=5%, no PO):  
\[
PV = 75{,}000 + \frac{75{,}000}{1.05} + \frac{75{,}000}{1.05^{2}} + \frac{75{,}000}{1.05^{3}} + \frac{75{,}000}{1.05^{4}} = \mathbf{\$340{,}946}
\]

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 340,946 | |
| Lease Liability | | 340,946 |

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 75,000 | |
| Cash | | 75,000 |

Liability after payment = $340,946 − $75,000 = **$265,946**.

**(b) Liability roll-forward to January 1, Year 3 (before remeasurement / before payment)**

| Date | Interest (5%) | Payment | Liability balance |
|------|-------------:|--------:|------------------:|
| Jan 1, Y1 (after pmt) | — | 75,000 | 265,946 |
| Dec 31, Y1 | 13,297 | — | 279,243 |
| Jan 1, Y2 | — | 75,000 | 204,243 |
| Dec 31, Y2 | 10,212 | — | **214,455** |

Interest checks: \(265{,}946 \times 0.05 = 13{,}297.30 \to 13{,}297\); \(204{,}243 \times 0.05 = 10{,}212.15 \to 10{,}212\).

ROU amortization Years 1–2 (over 5-year term): \(340{,}946 / 5 = 68{,}189.20 \to \mathbf{\$68{,}189}\) per year.  
ROU CA on Jan 1, Y3 = \(340{,}946 - 2 \times 68{,}189 = \mathbf{\$204{,}568}\).

**(c) Remeasurement — January 1, Year 3 (before payment)**

Remeasured liability at **4%** (updated rate; PO now included):  
\[
LL = 75{,}000 + \frac{75{,}000}{1.04} + \frac{75{,}000}{1.04^{2}} + \frac{35{,}000}{1.04^{3}} = \mathbf{\$247{,}572}
\]  
(Excel-equivalent: `PV(0.04,3,-75000,-35000,1)`.)

Increase = \(247{,}572 - 214{,}455 = \mathbf{\$33{,}117}\).

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 33,117 | |
| Lease Liability | | 33,117 |

Post-remeasurement balances: LL **$247,572**; ROU \(204{,}568 + 33{,}117 = \mathbf{\$237{,}685}\).

**(d) Payment, schedule, Year 3 adjusting entries**

January 1, Year 3 payment:

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 75,000 | |
| Cash | | 75,000 |

Post-remeasurement liability schedule (i = 4%; PO settles at **$35,000**):

| Date | Interest (4%) | Payment / PO | Liability balance |
|------|-------------:|-------------:|------------------:|
| Jan 1, Y3 (after remeas & pmt) | — | 75,000 | 172,572 |
| Dec 31, Y3 | 6,903 | — | 179,475 |
| Jan 1, Y4 | — | 75,000 | 104,475 |
| Dec 31, Y4 | 4,179 | — | 108,654 |
| Jan 1, Y5 | — | 75,000 | 33,654 |
| Dec 31, Y5 | 1,346 | — | **35,000** |

Interest checks: \(172{,}572 \times 0.04 = 6{,}902.88 \to 6{,}903\); \(104{,}475 \times 0.04 = 4{,}179\); \(33{,}654 \times 0.04 = 1{,}346.16 \to 1{,}346\).

Because the PO is now reasonably certain, amortize ROU over the **remaining economic life of the underlying asset** = 6 − 2 = **4 years** (not the remaining contractual lease term alone).  
Annual ROU amortization ≈ \(237{,}685 / 4 = 59{,}421.25\) → **$59,421** for three years and **$59,422** in the final year (or $59,421/year with a $1 plug).

December 31, Year 3 adjusting entries:

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 6,903 | |
| Lease Liability | | 6,903 |

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 59,421 | |
| Right-of-Use Asset | | 59,421 |

**(e) Settlement — exercise of purchase option at end of Year 5**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 35,000 | |
| Cash | | 35,000 |

Presentation: after exercise, reclassify the remaining ROU carrying amount to the appropriate **PPE (equipment)** account and depreciate any residual book value over the asset’s remaining useful life (here, about one year if 4-year post-remeasurement life was used through end of Year 6). Liability is fully settled (Dr = Cr).

**Key insight:** A change in whether the lessee is reasonably certain to exercise a purchase option triggers **classification reassessment and remeasurement**; the liability is remeasured at the **updated** discount rate (when the original rate did not already reflect the option), and the entire adjustment hits **ROU**, not earnings. Subsequent accounting uses the new liability path, including settlement of the PO.

---

### Q2 — CORE number variant — Meridian Biotech: PO reassessment remeasurement twin
**LO:** LO 17-11  
**Concept:** Purchase-option reassessment remeasurement (number-variant twin of Q1)  
**Scenario:**  
On **January 1, Year 1**, **Meridian Biotech Labs** leases a cold-chain packaging line:

| Item | Detail |
|------|--------|
| Economic life | 6 years |
| Lease term | 5 years |
| Annual payment | **$90,000** in advance (Jan 1) |
| Purchase option (end of Year 5) | **$45,000** — not reasonably certain at commencement |
| Lessee IBR at commencement | **6%** |
| Classification | Finance lease (term ≥ 75% of life) |

On **January 1, Year 3** (before payment), Meridian becomes reasonably certain it will exercise the PO. Classification remains finance. Current IBR is **5%**; original rate did not reflect the PO → **update rate to 5%**.

**Required:**  
(a) Initial PV, commencement JE, and first payment (Jan 1, Y1).  
(b) Lease liability on Jan 1, Y3 **before** remeasurement/payment, and ROU CA (2 years of SL amort over 5-year term).  
(c) Remeasured liability at 5%, remeasurement JE, and post-remeasurement balances.  
(d) Jan 1, Y3 payment and Dec 31, Y3 interest on the remeasured liability.

**Answer key:**

**(a)**  
\[
PV = 90{,}000 + \frac{90{,}000}{1.06} + \frac{90{,}000}{1.06^{2}} + \frac{90{,}000}{1.06^{3}} + \frac{90{,}000}{1.06^{4}} = \mathbf{\$401{,}860}
\]

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 401,860 | |
| Lease Liability | | 401,860 |

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 90,000 | |
| Cash | | 90,000 |

LL after payment = **$311,860**.

**(b) Roll to Jan 1, Y3 before remeasurement**

| Date | Interest (6%) | Payment | Liability |
|------|-------------:|--------:|----------:|
| Jan 1, Y1 (after pmt) | — | 90,000 | 311,860 |
| Dec 31, Y1 | 18,712 | — | 330,572 |
| Jan 1, Y2 | — | 90,000 | 240,572 |
| Dec 31, Y2 | 14,434 | — | **255,006** |

ROU amort/year = \(401{,}860 / 5 = \mathbf{\$80{,}372}\).  
ROU Jan 1, Y3 = \(401{,}860 - 2 \times 80{,}372 = \mathbf{\$241{,}116}\).

**(c) Remeasurement at 5%**  
\[
LL = 90{,}000 + \frac{90{,}000}{1.05} + \frac{90{,}000}{1.05^{2}} + \frac{45{,}000}{1.05^{3}} = \mathbf{\$296{,}220}
\]  
Increase = \(296{,}220 - 255{,}006 = \mathbf{\$41{,}214}\).

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 41,214 | |
| Lease Liability | | 41,214 |

Balances after remeasurement: LL **$296,220**; ROU \(241{,}116 + 41{,}214 = \mathbf{\$282{,}330}\).

**(d)**  
Jan 1, Y3 payment:

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 90,000 | |
| Cash | | 90,000 |

LL after payment = \(296{,}220 - 90{,}000 = \mathbf{\$206{,}220}\).  
Year 3 interest = \(206{,}220 \times 0.05 = 10{,}311\) → **$10,311**.

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 10,311 | |
| Lease Liability | | 10,311 |

(Post-remeasurement ROU amortizes over remaining **4-year** economic life: \(282{,}330 / 4 = \mathbf{\$70{,}582.50}\) per year.)

**Key insight:** Same PO-reassessment mechanics as Q1—only the payment, rates, and PO amount change. Always remeasure **before** the current payment, book ROU/LL adjustment, then record cash.

---

### Q3 — CORE alternate angle — Orchard Precision: residual-value remeasurement + modification classification map
**LO:** LO 17-11  
**Concept:** Remeasurement-only (guaranteed residual probable amount) at original rate; classify modification vs remeasurement events  
**Scenario:**  
On **January 1, Year 1**, **Orchard Precision Tools** (lessee) enters a **finance lease** for a CNC finishing cell:

| Item | Detail |
|------|--------|
| Lease term | 4 years, no renewal |
| Annual payment | **$52,000** in advance (Jan 1) |
| Guaranteed residual value | $20,000 |
| Probable amount owed under GRV at commencement | **$0** (expected residual ≥ guarantee) |
| Lessee discount rate | **7%** |
| Classification | Finance lease (assume criterion met; remains finance) |

**Event 1 — January 1, Year 3 (before payment):** Technology shift lowers expected residual; probable amount owed under the GRV becomes **$9,000**. Current market borrowing rate is 5%.  

**Event 2 (independent classification cases — no dollar computation required):**  
State whether each is (1) **new separate lease**, (2) **remeasurement only**, or (3) **classification reassessment and remeasurement**:  
- A. Add adjacent warehouse bay at **standalone** market rent  
- B. Extend term by 2 years via contract amendment (not a standalone add-on)  
- C. Contingency resolves so variable usage rent becomes **fixed**  
- D. Lessee now reasonably certain to exercise a purchase option  

**Required:**  
(a) Initial PV (no residual in lease payments), commencement JE, first payment.  
(b) Liability on Jan 1, Y3 before residual remeasurement/payment; ROU CA.  
(c) Classify Event 1 (remeasure only vs reassess). Compute remeasured LL (2 remaining advance payments + $9,000 residual) at the **correct** rate; record remeasurement and the Y3 payment.  
(d) Complete the Event 2 classification table. One sentence: lessor reassessment rule.

**Answer key:**

**(a)**  
\[
PV = 52{,}000 + \frac{52{,}000}{1.07} + \frac{52{,}000}{1.07^{2}} + \frac{52{,}000}{1.07^{3}} = \mathbf{\$188{,}464}
\]

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 188,464 | |
| Lease Liability | | 188,464 |

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 52,000 | |
| Cash | | 52,000 |

LL after payment = **$136,464**.

**(b)**

| Date | Interest (7%) | Payment | Liability |
|------|-------------:|--------:|----------:|
| Jan 1, Y1 (after pmt) | — | 52,000 | 136,464 |
| Dec 31, Y1 | 9,552 | — | 146,016 |
| Jan 1, Y2 | — | 52,000 | 94,016 |
| Dec 31, Y2 | 6,581 | — | **100,597** |

ROU amort/year = \(188{,}464 / 4 = \mathbf{\$47{,}116}\).  
ROU Jan 1, Y3 = \(188{,}464 - 2 \times 47{,}116 = \mathbf{\$94{,}232}\).

**(c) Event 1**  
Change in **probable amount owed under a residual value guarantee** → **remeasurement only** (no classification reassessment). Discount rate remains the **original 7%** (do **not** use the 5% market rate).

Remeasured LL:  
\[
LL = 52{,}000 + \frac{52{,}000}{1.07} + \frac{9{,}000}{1.07^{2}} = \mathbf{\$108{,}459}
\]  
Increase = \(108{,}459 - 100{,}597 = \mathbf{\$7{,}862}\).

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 7,862 | |
| Lease Liability | | 7,862 |

Balances: LL **$108,459**; ROU \(94{,}232 + 7{,}862 = \mathbf{\$102{,}094}\).

January 1, Year 3 payment:

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 52,000 | |
| Cash | | 52,000 |

LL after payment = **$56,459**.  
(Subsequent path at 7%: interest Y3 \(56{,}459 \times 0.07 = 3{,}952.13 \to 3{,}952\) → before Y4 payment $60,411; after Y4 payment $8,411; interest Y4 $589 → residual liability **$9,000** settles the GRV.)

**(d) Classification map**

| Event | Outcome |
|-------|---------|
| A. Add warehouse bay at standalone price | **(1) New separate lease** |
| B. Extend term by 2 years (modification) | **(3) Reassess classification and remeasure** |
| C. Contingency → variable becomes fixed | **(2) Remeasurement only** |
| D. Now reasonably certain to exercise PO | **(3) Reassess classification and remeasure** |

**Lessor rule:** A **lessor** reassesses lease classification only when the lease contract is **modified**—not merely because the lessee remeasures for residual or contingency events.

**Key insight:** Residual-probable and contingency-resolution events remeasure at the **original** discount rate with no automatic reclassification; term/PO assessment changes and non-standalone modifications reassess classification and generally update the rate when the original rate did not already embed the optionality.

---

### Q4 — MC — Modification / remeasurement classification
**LO:** LO 17-11  
**Concept:** Separate lease vs modified lease vs remeasurement-only triggers  

**Question 1:**  
Lessee Pine & Copper Retail leases 8,000 sq ft of store space. Mid-lease, the parties amend the contract to add 3,000 sq ft in the same building. The incremental rent equals the current market (standalone) rate for comparable space. How should the lessee treat the amendment?

- A) Remeasure the original lease liability only; do not reassess classification  
- B) Account for a **new separate lease** for the additional space; original lease accounting unchanged  
- C) Always reclassify the entire arrangement as a finance lease  
- D) Expense the incremental rent as incurred with no ROU impact  

**Answer:** **B.** Additional right-of-use at a **standalone price** → separate contract (ASC 842-10-25-8). Original lease continues as before; new space is analyzed as a new lease.

**Question 2:**  
Which event requires the lessee to **update the discount rate** when remeasuring (assuming the original rate did not already reflect the optionality)?

- A) Increase in probable amount owed under a residual value guarantee  
- B) Resolution of a contingency that makes variable payments fixed  
- C) Change in assessment so the lessee is now reasonably certain to exercise a purchase option  
- D) Both A and B  

**Answer:** **C.** PO (or lease-term) assessment changes generally **update** the discount rate unless the original rate already reflected that optionality. Residual-probable changes and contingency resolutions keep the **original** rate (ASC 842-20-35-5 exceptions).

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (PV annuity-due, interest roll-forwards, remeasurement increases)
- [x] Core demo path (Demo 17-11 / App. 17B): separate lease, modified lease, PO remeasurement, residual remeasurement — not sidebar-only
- [x] LO + Concept on every item
- [x] MC = 2 (classification/method only)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
