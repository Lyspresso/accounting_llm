# Agent 151 — CORE DEMO — LO 17-11

**Chapter:** 17  
**LO title:** Explain lease modifications and lease remeasurements  
**Critical gap LO:** yes

## Concept list for this pack
- Separate (new) lease vs single modified lease — **standalone-price** test (ASC 842-10-25-8)
- Classification **reassessment + remeasurement** triggers: lease-term change; purchase-option assessment change; modification not a separate contract
- **Remeasurement-only** triggers: change in probable amount under residual-value guarantee; contingency resolution making variable payments fixed
- Remeasurement JE: adjust **Lease Liability** with offset to **Right-of-Use Asset** (not P&L)
- Discount-rate rules: **update** rate for term/PO reassessment (when original rate did not already reflect optionality); **keep original** rate for residual-probable and contingency resolution (ASC 842-20-35-5)
- **Subsequent measurement schedule** after remeasurement (liability amortization + ROU amortization path)
- Period-end adjusting entries (interest accretion; ROU amortization)
- Settlement: exercise purchase option or pay residual guarantee at maturity
- Classification / presentation / disclosure; lessor reassesses only on modification

---

### Q1 — CORE — Helix Conveyor: PO reassessment, remeasurement, full subsequent schedule, settlement
**LO:** LO 17-11  
**Concept:** Purchase-option reassessment → remeasure LL at updated rate against ROU; subsequent multi-period liability and ROU schedules; period-end adjusting JEs; PO settlement  
**Scenario:**  
On **January 1, Year 1**, **Helix Conveyor Systems Inc.** (lessee) leases a specialty packaging line from Westbrook Equipment Finance:

| Item | Detail |
|------|--------|
| Economic life of equipment | **6 years** |
| Lease term | **5 years** (no renewal option) |
| Annual lease payment | **$105,000** due **beginning** of each year (January 1) |
| Purchase option at end of Year 5 | **$35,000** — **not** reasonably certain of exercise at commencement |
| Lessee incremental borrowing rate | **6%** (lessor’s implicit rate unknown) |
| Initial direct costs / prepayments / incentives | none |
| Classification at commencement | **Finance lease** (lease term = 5/6 of economic life ≥ 75%) |

At commencement Helix does **not** include the purchase option in lease payments. While the PO is not reasonably certain, the ROU asset is amortized straight-line over the **5-year lease term**.

On **January 1, Year 3** (immediately **before** the Year 3 payment), strengthened product demand makes Helix **reasonably certain** it will exercise the $35,000 purchase option. After reassessing classification criteria, the lease **remains a finance lease**. Helix’s current incremental borrowing rate is **5%**. The original 6% rate did **not** already reflect the purchase option, so the discount rate is **updated to 5%** for remeasurement.

**Required:**  
(a) Record the **commencement** entry on January 1, Year 1 (before the first payment) and the **first payment**.  
(b) Prepare the **lease liability amortization schedule** through January 1, Year 3 **before** remeasurement (show interest for Years 1–2 and payments). Compute the **ROU carrying amount** on January 1, Year 3.  
(c) Compute the **remeasured lease liability** on January 1, Year 3 (3 remaining beginning-of-period payments of $105,000 plus $35,000 PO at end of Year 5, discounted at **5%**). Record the **remeasurement** entry.  
(d) Record the January 1, Year 3 **lease payment** after remeasurement. Prepare the **full post-remeasurement liability schedule** through exercise of the PO (emphasis: subsequent measurement schedule). State the remaining economic life used for ROU amortization after the PO becomes reasonably certain, and the annual ROU amortization amount.  
(e) Record the **December 31, Year 3** period-end adjusting entries (interest + ROU amortization).  
(f) Record the **settlement** entry when the purchase option is exercised at the end of Year 5. Briefly state ROU/PPE presentation.

**Answer key:**

**(a) Commencement and first payment — January 1, Year 1**

PV of annuity-due lease payments (n = 5, i = 6%, no PO):  
\[
PV = 105{,}000 \times \frac{1-(1.06)^{-5}}{0.06}\times(1.06) = \mathbf{\$468{,}836}
\]  
(Excel-equivalent: `=PV(0.06,5,-105000,0,1)`.)

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 468,836 | |
| Lease Liability | | 468,836 |
| *Commencement — finance lease ROU and liability (PO not reasonably certain)* | | |

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 105,000 | |
| Cash | | 105,000 |
| *First lease payment (reduces principal)* | | |

**Check:** Dr = Cr on each entry. Liability after payment = $468,836 − $105,000 = **$363,836**.

**(b) Liability roll-forward to January 1, Year 3 (before remeasurement / before payment)**

| Date | Interest (6%) | Payment | Liability balance |
|------|-------------:|--------:|------------------:|
| Jan 1, Y1 (after pmt) | — | 105,000 | 363,836 |
| Dec 31, Y1 | 21,830 | — | 385,666 |
| Jan 1, Y2 | — | 105,000 | 280,666 |
| Dec 31, Y2 | 16,840 | — | **297,506** |

Interest checks: \(363{,}836 \times 0.06 = 21{,}830.16 \to \mathbf{21{,}830}\); \(280{,}666 \times 0.06 = 16{,}839.96 \to \mathbf{16{,}840}\).

ROU amortization Years 1–2 (over 5-year term): \(468{,}836 / 5 = 93{,}767.20 \to \mathbf{\$93{,}767}\) per year (rounded).  
ROU CA on Jan 1, Y3 = \(468{,}836 - 2 \times 93{,}767 = \mathbf{\$281{,}302}\).

**(c) Remeasurement — January 1, Year 3 (before payment)**

Change in assessment of whether the lessee is reasonably certain to exercise a purchase option → **lease classification reassessment and remeasurement**. Discount rate **updated to 5%** (original rate did not already reflect the PO).

Remeasured liability at **5%** (3 remaining advance payments + $35,000 PO at end of n = 3):  
\[
LL = PV(0.05,\,3,\,-105{,}000,\,-35{,}000,\,1) = \mathbf{\$330{,}472}
\]

Increase = \(330{,}472 - 297{,}506 = \mathbf{\$32{,}966}\).

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 32,966 | |
| Lease Liability | | 32,966 |
| *Remeasure LL for PO now reasonably certain; entire adjustment to ROU* | | |

**Check:** Dr = Cr = **$32,966**.  
Post-remeasurement balances: LL **$330,472**; ROU \(281{,}302 + 32{,}966 = \mathbf{\$314{,}268}\).

**(d) Payment and full subsequent measurement schedule (emphasis)**

January 1, Year 3 payment:

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 105,000 | |
| Cash | | 105,000 |

Post-remeasurement **lease liability amortization schedule** (i = 5%; PO settles at **$35,000**):

| Date | Interest (5%) | Payment / PO | Liability balance |
|------|-------------:|-------------:|------------------:|
| Jan 1, Y3 (after remeas & pmt) | — | 105,000 | 225,472 |
| Dec 31, Y3 | 11,274 | — | 236,746 |
| Jan 1, Y4 | — | 105,000 | 131,746 |
| Dec 31, Y4 | 6,587 | — | 138,333 |
| Jan 1, Y5 | — | 105,000 | 33,333 |
| Dec 31, Y5 | 1,667 | — | **35,000** |

Interest checks: \(225{,}472 \times 0.05 = 11{,}273.60 \to 11{,}274\); \(131{,}746 \times 0.05 = 6{,}587.30 \to 6{,}587\); \(33{,}333 \times 0.05 = 1{,}666.65 \to 1{,}667\). Ending balance equals PO **$35,000** (rolls forward cleanly).

Because the PO is now reasonably certain, amortize ROU over the **remaining economic life of the underlying asset** = 6 − 2 = **4 years** (not merely the remaining contractual lease term alone).

**Post-remeasurement ROU amortization schedule:**

| Year | Beg. ROU | Amortization | End. ROU |
|---:|---:|---:|---:|
| 3 | 314,268 | **78,567** | 235,701 |
| 4 | 235,701 | 78,567 | 157,134 |
| 5 | 157,134 | 78,567 | 78,567 |
| 6 | 78,567 | 78,567 | 0 |

Annual ROU amortization = \(314{,}268 / 4 = \mathbf{\$78{,}567}\).

**(e) December 31, Year 3 period-end adjusting entries**

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 11,274 | |
| Lease Liability | | 11,274 |
| *Accrete lease liability at updated 5%* | | |

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 78,567 | |
| Right-of-Use Asset | | 78,567 |
| *ROU amort over remaining 4-year economic life* | | |

**Check:** Each entry Dr = Cr.

**(f) Settlement — exercise of purchase option at end of Year 5**

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 35,000 | |
| Cash | | 35,000 |
| *Exercise purchase option; clear remaining liability* | | |

**Presentation:** After exercise, reclassify any remaining ROU carrying amount to the appropriate **PPE (equipment)** account and depreciate residual book value over the asset’s remaining useful life (here, Year 6 if the 4-year post-remeasurement life runs through end of Year 6). Liability is fully settled.

**Key insight:** A change in whether the lessee is reasonably certain to exercise a purchase option triggers **classification reassessment and remeasurement**. Remeasure the liability at the **updated** discount rate (when the original rate did not already embed the optionality); the entire LL change adjusts **ROU**, not earnings. Subsequent measurement uses the new liability path (interest + payments + PO settlement) and a revised ROU amortization horizon equal to remaining economic life.

---

### Q2 — CORE number variant — Glacier Lab: PO reassessment twin
**LO:** LO 17-11  
**Concept:** Purchase-option reassessment remeasurement (number-variant twin of Q1) — subsequent interest and schedule path  
**Scenario:**  
On **January 1, Year 1**, **Glacier Lab Analytics LLC** leases a cold-chain bottling cell:

| Item | Detail |
|------|--------|
| Economic life | **6 years** |
| Lease term | **5 years** |
| Annual payment | **$80,000** in advance (January 1) |
| Purchase option (end of Year 5) | **$30,000** — not reasonably certain at commencement |
| Lessee IBR at commencement | **7%** |
| Classification | Finance lease (term ≥ 75% of life) |

On **January 1, Year 3** (before payment), Glacier becomes reasonably certain it will exercise the PO. Classification remains finance. Current IBR is **5%**; original rate did not reflect the PO → **update rate to 5%**.

**Required:**  
(a) Initial PV, commencement JE, and first payment (Jan 1, Y1).  
(b) Lease liability on Jan 1, Y3 **before** remeasurement/payment, and ROU CA (2 years of SL amort over 5-year term).  
(c) Remeasured liability at 5%, remeasurement JE, and post-remeasurement balances.  
(d) Jan 1, Y3 payment and the **full post-remeasurement liability schedule** through the PO; Dec 31, Y3 interest JE.  
(e) State annual ROU amortization after remeasurement (remaining economic life).

**Answer key:**

**(a)**  
\[
PV = 80{,}000 \times \frac{1-(1.07)^{-5}}{0.07}\times(1.07) = \mathbf{\$350{,}977}
\]  
(`=PV(0.07,5,-80000,0,1)`.)

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 350,977 | |
| Lease Liability | | 350,977 |

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 80,000 | |
| Cash | | 80,000 |

LL after payment = **$270,977**. **Check:** Dr = Cr on each entry.

**(b) Roll to Jan 1, Y3 before remeasurement**

| Date | Interest (7%) | Payment | Liability |
|------|-------------:|--------:|----------:|
| Jan 1, Y1 (after pmt) | — | 80,000 | 270,977 |
| Dec 31, Y1 | 18,968 | — | 289,945 |
| Jan 1, Y2 | — | 80,000 | 209,945 |
| Dec 31, Y2 | 14,696 | — | **224,641** |

Interest: \(270{,}977 \times 0.07 = 18{,}968.39 \to 18{,}968\); \(209{,}945 \times 0.07 = 14{,}696.15 \to 14{,}696\).

ROU amort/year = \(350{,}977 / 5 = 70{,}195.40 \to \mathbf{\$70{,}195}\).  
ROU Jan 1, Y3 = \(350{,}977 - 2 \times 70{,}195 = \mathbf{\$210{,}587}\).

**(c) Remeasurement at 5%**  
\[
LL = PV(0.05,\,3,\,-80{,}000,\,-30{,}000,\,1) = \mathbf{\$254{,}668}
\]  
Increase = \(254{,}668 - 224{,}641 = \mathbf{\$30{,}027}\).

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 30,027 | |
| Lease Liability | | 30,027 |

Balances after remeasurement: LL **$254,668**; ROU \(210{,}587 + 30{,}027 = \mathbf{\$240{,}614}\). **Check:** Dr = Cr = 30,027.

**(d) Payment and subsequent liability schedule**

Jan 1, Y3 payment:

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 80,000 | |
| Cash | | 80,000 |

Post-remeasurement liability schedule (i = 5%; PO = **$30,000**):

| Date | Interest (5%) | Payment / PO | Liability balance |
|------|-------------:|-------------:|------------------:|
| Jan 1, Y3 (after remeas & pmt) | — | 80,000 | 174,668 |
| Dec 31, Y3 | 8,733 | — | 183,401 |
| Jan 1, Y4 | — | 80,000 | 103,401 |
| Dec 31, Y4 | 5,170 | — | 108,571 |
| Jan 1, Y5 | — | 80,000 | 28,571 |
| Dec 31, Y5 | 1,429 | — | **30,000** |

Dec 31, Y3 interest:

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 8,733 | |
| Lease Liability | | 8,733 |

**(e)** Remaining economic life after remeasurement = 6 − 2 = **4 years**.  
Annual ROU amortization = \(240{,}614 / 4 = \mathbf{\$60{,}153.50}\) (e.g., **$60,153** for three years and **$60,155** in the final year, or $60,154/$60,153 with a $1 plug so totals equal $240,614).

**Key insight:** Same PO-reassessment mechanics as Q1—only payments, rates, and PO amount change. Always remeasure **before** the current payment, book the ROU/LL adjustment, then record cash and run the **new** subsequent measurement schedule to the PO.

---

### Q3 — CORE alternate angle — Redwood CNC: residual-value remeasurement + modification classification map
**LO:** LO 17-11  
**Concept:** Remeasurement-only (guaranteed residual probable amount) at **original** discount rate; classify modification vs remeasurement events; residual settlement path  
**Scenario:**  
On **January 1, Year 1**, **Redwood CNC Works** (lessee) enters a **finance lease** for a precision milling cell:

| Item | Detail |
|------|--------|
| Lease term | **4 years**, no renewal |
| Annual payment | **$70,000** in advance (January 1) |
| Guaranteed residual value | $20,000 (contractual guarantee) |
| Probable amount owed under GRV at commencement | **$0** (expected residual ≥ guarantee) |
| Lessee discount rate | **8%** |
| Classification | Finance lease (assume criterion met; remains finance) |

**Event 1 — January 1, Year 3 (before payment):** A technology shift lowers the expected residual; the **probable amount owed** under the GRV becomes **$10,000**. The current market borrowing rate is **5%** (a red herring for rate selection).

**Event 2 (independent classification cases — no dollar computation required):**  
State whether each is (1) **new separate lease**, (2) **remeasurement only**, or (3) **classification reassessment and remeasurement**:  
- A. Add adjacent warehouse bay at **standalone** market rent  
- B. Extend term by 2 years via contract amendment (not a standalone add-on right at standalone price)  
- C. Contingency resolves so variable usage rent becomes **fixed**  
- D. Lessee now reasonably certain to exercise a purchase option  
- E. Lessee’s estimate of residual probable amount increases (no contract modification)

**Required:**  
(a) Initial PV (no residual in lease payments), commencement JE, first payment.  
(b) Liability on Jan 1, Y3 before residual remeasurement/payment; ROU CA.  
(c) Classify Event 1 (remeasure only vs reassess). Compute remeasured LL (2 remaining advance payments + $10,000 residual) at the **correct** rate; record remeasurement and the Y3 payment.  
(d) Complete the **subsequent liability schedule** from after the Y3 payment through residual settlement at end of Year 4; record the GRV settlement JE.  
(e) Complete the Event 2 classification table. One sentence: lessor reassessment rule. How is the remeasurement adjustment presented?

**Answer key:**

**(a)**  
\[
PV = 70{,}000 \times \frac{1-(1.08)^{-4}}{0.08}\times(1.08) = \mathbf{\$250{,}397}
\]  
(`=PV(0.08,4,-70000,0,1)`.)

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 250,397 | |
| Lease Liability | | 250,397 |

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 70,000 | |
| Cash | | 70,000 |

LL after payment = **$180,397**. **Check:** Dr = Cr.

**(b)**

| Date | Interest (8%) | Payment | Liability |
|------|-------------:|--------:|----------:|
| Jan 1, Y1 (after pmt) | — | 70,000 | 180,397 |
| Dec 31, Y1 | 14,432 | — | 194,829 |
| Jan 1, Y2 | — | 70,000 | 124,829 |
| Dec 31, Y2 | 9,986 | — | **134,815** |

Interest: \(180{,}397 \times 0.08 = 14{,}431.76 \to 14{,}432\); \(124{,}829 \times 0.08 = 9{,}986.32 \to 9{,}986\).

ROU amort/year = \(250{,}397 / 4 = 62{,}599.25 \to \mathbf{\$62{,}599}\).  
ROU Jan 1, Y3 = \(250{,}397 - 2 \times 62{,}599 = \mathbf{\$125{,}199}\).

**(c) Event 1**  
Change in **probable amount owed under a residual value guarantee** → **remeasurement only** (no classification reassessment). Discount rate remains the **original 8%** (do **not** use the 5% market rate — ASC 842-20-35-5 exception).

Remeasured LL:  
\[
LL = PV(0.08,\,2,\,-70{,}000,\,-10{,}000,\,1) = \mathbf{\$143{,}388}
\]  
Increase = \(143{,}388 - 134{,}815 = \mathbf{\$8{,}573}\).

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 8,573 | |
| Lease Liability | | 8,573 |
| *Remeasure for higher probable GRV amount; original rate retained* | | |

Balances: LL **$143,388**; ROU \(125{,}199 + 8{,}573 = \mathbf{\$133{,}772}\).

January 1, Year 3 payment:

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 70,000 | |
| Cash | | 70,000 |

LL after payment = **$73,388**.

**(d) Subsequent schedule through residual settlement**

| Date | Interest (8%) | Payment / GRV | Liability balance |
|------|-------------:|--------------:|------------------:|
| Jan 1, Y3 (after remeas & pmt) | — | 70,000 | 73,388 |
| Dec 31, Y3 | 5,871 | — | 79,259 |
| Jan 1, Y4 | — | 70,000 | 9,259 |
| Dec 31, Y4 | 741 | — | **10,000** |

Interest: \(73{,}388 \times 0.08 = 5{,}871.04 \to 5{,}871\); \(9{,}259 \times 0.08 = 740.72 \to 741\). Ending balance = GRV probable amount **$10,000**.

Settlement of residual guarantee at end of Year 4:

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 10,000 | |
| Cash | | 10,000 |
| *Pay probable amount owed under residual value guarantee* | | |

**Check:** Dr = Cr = 10,000. Liability fully settled.

**(e) Classification map**

| Event | Outcome |
|-------|---------|
| A. Add warehouse bay at standalone price | **(1) New separate lease** |
| B. Extend term by 2 years (modification, not separate) | **(3) Reassess classification and remeasure** |
| C. Contingency → variable becomes fixed | **(2) Remeasurement only** |
| D. Now reasonably certain to exercise PO | **(3) Reassess classification and remeasure** |
| E. Residual probable amount increases | **(2) Remeasurement only** |

**Lessor rule:** A **lessor** reassesses lease classification only when the lease contract is **modified**—not merely because the lessee remeasures for residual-probable or contingency events.

**Presentation:** Remeasurement of the lease liability is recognized as an **adjustment to the ROU asset** (balance-sheet only at the remeasurement date); subsequent interest and ROU amortization affect the income statement prospectively (change-in-estimate style).

**Key insight:** Residual-probable and contingency-resolution events remeasure at the **original** discount rate with no automatic reclassification. Term/PO assessment changes and non-standalone modifications **reassess classification** and generally **update** the rate when the original rate did not already embed the optionality. Additional space at a **standalone price** is a **separate new lease**; the original lease is untouched.

---

### Q4 — MC — Modification / remeasurement classification
**LO:** LO 17-11  
**Concept:** Separate lease vs modified lease vs remeasurement-only; discount-rate update rules  

**Question 1:**  
Lessee **Bayfront Outfitters** leases 12,000 sq ft of retail space. Mid-lease, the parties amend the contract to add 4,000 sq ft in the same building. The incremental rent equals the current market (standalone) rate for comparable space. How should the lessee treat the amendment?

- A) Remeasure the original lease liability only; do not reassess classification  
- B) Account for a **new separate lease** for the additional space; original lease accounting unchanged  
- C) Always reclassify the entire arrangement as a finance lease  
- D) Expense the incremental rent as incurred with no ROU impact  

**Answer:** **B.** Additional right-of-use at a **standalone price** → separate contract (ASC 842-10-25-8). Original lease continues as before; new space is analyzed as a new lease (classification, measurement, etc.).

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
- [x] Math recomputed (PV annuity-due, interest roll-forwards, remeasurement increases; schedules end at PO/GRV)
- [x] Core demo path (Demo 17-11 / App. 17B): separate lease, modified lease, PO remeasurement, residual remeasurement — not sidebar-only
- [x] LO + Concept on every item
- [x] MC = 2 (classification/method only)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
- [x] Emphasis: subsequent_measurement_schedule (full post-remeasurement liability + ROU schedules in Q1; full post paths in Q2/Q3)
