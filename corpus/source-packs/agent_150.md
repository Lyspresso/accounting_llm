# Agent 150 — CORE DEMO — LO 17-1

**Chapter:** 17  
**LO title:** Identify a lease, determine lease types for lessee, and classify leases using lease criteria  
**Critical gap LO:** yes

## Concept list for this pack
- **Identify a lease:** contract (or part of a contract) that conveys the **right to control** the use of an **identified asset** for a period of time in exchange for consideration (substantially all economic benefits + right to direct use; no substantive lessor substitution right)
- **Lease types for lessee:** **finance** (meets ≥1 of 5 classification criteria) vs **operating** (meets none); short-term exception is separate (LO 17-9)
- **Five classification criteria:** (1) ownership transfer, (2) purchase option reasonably certain to exercise, (3) lease term ≥ major part of remaining economic life (use **75%**), (4) PV of lease payments ≥ substantially all of FV (use **90%**), (5) no alternative use to lessor
- **Discount rate:** rate **implicit** in the lease if readily determinable by lessee; otherwise lessee’s **incremental borrowing rate**
- **Initial recognition JE:** at commencement, lessee records **ROU asset** and **lease liability** at PV of lease payments; first annuity-due payment reduces liability (no interest yet)
- **Subsequent measurement schedule:** effective-interest **lease liability schedule** (payment, interest, principal reduction, ending balance); ROU amortized **straight-line** over lease term (or useful life if ownership transfer / reasonably certain purchase option)
- **Period-end adjusting JE:** accrue interest on lease liability; record ROU amortization (finance: separate interest + amortization expense)
- **Disposal / maturity / settlement JE:** final payment settles remaining liability; final amortization zeros ROU when asset reverts with no residual obligation
- **Classification / presentation / disclosure:** finance vs operating classification at commencement; finance IS shows **interest** and **amortization** separately; current vs noncurrent lease liability split
- **Number-variant twin:** same classification → measurement path with all amounts, rates, and terms changed

---

### Q1 — CORE — Identify & classify finance lease; initial JE; liability schedule; Year 1–4 entries through maturity
**LO:** LO 17-1  
**Concept:** Identify lease contract; apply five classification criteria (term + PV); measure ROU/liability; initial recognition JEs; subsequent measurement (liability schedule + SL ROU amort); period-end adjusting JEs; maturity settlement when asset reverts  
**Scenario:**  
**Meridian Forge Inc.** (calendar-year lessee) enters a contract with **Harborline Equipment Leasing** on **January 1, Year 1** (commencement date). Harborline delivers a serial-numbered CNC machining cell for Meridian’s exclusive use. Meridian decides what products to run on the cell and operates it for its manufacturing. Harborline has **no practical ability** to substitute a different machine during the term.

**Contract terms:**
| Item | Amount / fact |
|---|---|
| Fair value of CNC equipment at commencement | **$200,000** |
| Remaining economic life | **5 years** |
| Noncancellable lease term | **4 years** |
| Annual lease payment (fixed) | **$55,000** due **Jan. 1** each year (annuity due), first payment **Jan. 1, Year 1** |
| Ownership transfer at end of term | **No** — asset reverts to Harborline |
| Purchase option | **None** |
| Residual value guarantee | **None**; estimated residual at lease end **$0** for Meridian’s analysis |
| Specialized / no alternative use | Equipment is **standard** CNC routinely re-leased by Harborline to other manufacturers |
| Rate implicit in the lease | **7%**, **known** by Meridian |
| Meridian’s incremental borrowing rate | **9%** |
| Initial direct costs / lease incentives | **None** |
| Accounting policy | Credit ROU asset directly for amortization (textbook style); round to nearest cent |

**Required:**  
a. **Identify:** Does the contract contain a **lease** under ASC 842? Explain using the two control criteria and substitution.  
b. **Classify:** Evaluate **all five** lease classification criteria. Conclude finance vs operating for Meridian. Which discount rate does Meridian use?  
c. Compute the **lease liability** and **ROU asset** at commencement (before the first payment). Prepare the **January 1, Year 1** initial recognition JE and the **first payment** JE.  
d. Prepare the full **lease liability subsequent measurement schedule** (columns: date, lease payment, interest on liability, liability reduction, ending liability).  
e. Prepare **all Year 1 period-end adjusting JEs** (Dec. 31) and the **Jan. 1, Year 2** payment JE.  
f. Prepare the **maturity / settlement path for Year 4**: Jan. 1, Year 4 payment and Dec. 31, Year 4 final ROU amortization. Show that liability and ROU are zero after lease end.  
g. **Presentation:** For Dec. 31, Year 1, state (1) ROU asset carrying amount, (2) current lease liability, (3) noncurrent lease liability, and (4) how Year 1 lease-related expenses appear on the income statement for a **finance** lease.

**Answer key:**  

**a. Identify — contract contains a lease**

Yes. At inception/commencement analysis:
1. **Identified asset:** CNC cell is **explicitly specified** (serial number).  
2. **Substantially all economic benefits:** Meridian has exclusive use for operations over the term.  
3. **Right to direct use:** Meridian operates the cell and decides output.  
4. **No substantive substitution right:** Harborline cannot practically substitute without Meridian’s consent / does not have a substitution right that benefits Harborline economically as described.

→ Meridian obtains the **right to control the use** of an identified asset for a period of time in exchange for consideration → **lease**.

**b. Classification (lessee) — finance lease**

| Criterion | Analysis | Met? |
|---|---|:---:|
| 1. Ownership transfer | Asset reverts to Harborline; no automatic legal title transfer | No |
| 2. Purchase option | No purchase option | No |
| 3. Lease term length | Term 4 ÷ life 5 = **80% ≥ 75%** (major part of remaining economic life); commencement is not in the last 25% of total life | **Yes** |
| 4. PV of lease payments | PV (below) **$199,337.38** ≥ 90% × $200,000 = **$180,000** | **Yes** |
| 5. No alternative use | Standard equipment routinely re-leased — alternative use exists | No |

**Conclusion:** At least one criterion met → **finance lease** for Meridian.  
**Discount rate:** Use **implicit rate 7%** (readily determinable); ignore 9% IBR.

**PV of lease payments (annuity due, n = 4, i = 7%, PMT = $55,000):**  
Excel: `=PV(0.07,4,-55000,0,1)` = **$199,337.38**

**c. Initial measurement and January 1, Year 1 JEs**

Lease liability = ROU asset = **$199,337.38** (basic lease: no prepaid, IDC, or incentives).

*January 1, Year 1 — recognize ROU asset and lease liability*

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 199,337.38 | |
| Lease Liability | | 199,337.38 |
| *Commencement — finance lease of CNC equipment* | | |

**Check:** Dr 199,337.38 = Cr 199,337.38. **Balanced.**

*January 1, Year 1 — first lease payment (annuity due; no interest yet)*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 55,000.00 | |
| Cash | | 55,000.00 |
| *Payment 1 of 4 — all principal* | | |

**Check:** Dr 55,000 = Cr 55,000. **Balanced.**  
Liability after payment: $199,337.38 − $55,000.00 = **$144,337.38**.

**d. Subsequent measurement — lease liability schedule (effective interest, 7%)**

Interest each period (except first payment) = **7% × liability balance after prior payment**.  
Principal reduction = payment − interest.

| Date | Lease payment | Interest on liability (7%) | Liability reduction | Ending lease liability |
|---|---:|---:|---:|---:|
| Jan. 1, Y1 (commencement, before pmt) | — | — | — | **199,337.38** |
| Jan. 1, Year 1 | 55,000.00 | 0.00 | 55,000.00 | 144,337.38 |
| Jan. 1, Year 2 | 55,000.00 | 10,103.62 | 44,896.38 | 99,441.00 |
| Jan. 1, Year 3 | 55,000.00 | 6,960.87 | 48,039.13 | 51,401.87 |
| Jan. 1, Year 4 | 55,000.00 | 3,598.13 | 51,401.87 | **0.00** |
| **Totals** | **220,000.00** | **20,662.62** | **199,337.38** | |

**Schedule checks:**  
- Total reductions = initial PV = $199,337.38  
- Total interest = total cash payments − PV = $220,000.00 − $199,337.38 = $20,662.62  
- Ending balance after final payment = **$0**

**Interest computation detail:**  
- Year 1 interest (accrued Dec. 31, Y1 / paid as part of Jan. 1, Y2): $144,337.38 × 7% = **$10,103.62**  
- Year 2: $99,441.00 × 7% = **$6,960.87**  
- Year 3: $51,401.87 × 7% = **$3,598.13**

**ROU amortization (straight-line over 4-year lease term; no ownership transfer / PO):**  
Annual = $199,337.38 ÷ 4 → **$49,834.35** for Years 1–3; Year 4 **$49,834.33** (penny rounding so cumulative = $199,337.38).

**e. Year 1 period-end adjusting JEs and Year 2 payment**

*December 31, Year 1 — interest on lease liability*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 10,103.62 | |
| Lease Liability | | 10,103.62 |
| *Accrue interest: $144,337.38 × 7%* | | |

**Check:** Dr 10,103.62 = Cr 10,103.62. **Balanced.**  
Liability at Dec. 31, Y1: $144,337.38 + $10,103.62 = **$154,441.00**.

*December 31, Year 1 — ROU amortization*

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 49,834.35 | |
| Right-of-Use Asset | | 49,834.35 |
| *SL amort: $199,337.38 / 4* | | |

**Check:** Dr 49,834.35 = Cr 49,834.35. **Balanced.**  
ROU at Dec. 31, Y1: $199,337.38 − $49,834.35 = **$149,503.03**.

*January 1, Year 2 — lease payment (settles accrued interest + principal)*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 55,000.00 | |
| Cash | | 55,000.00 |
| *Payment 2: $10,103.62 interest portion + $44,896.38 principal* | | |

**Check:** Dr 55,000 = Cr 55,000. **Balanced.**  
Liability after payment: $154,441.00 − $55,000.00 = **$99,441.00**.

**f. Maturity / settlement — Year 4**

After Jan. 1, Year 3 payment, liability (before Year 3 interest) = **$51,401.87**.  
*December 31, Year 3 — interest (for completeness of path to Year 4)*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 3,598.13 | |
| Lease Liability | | 3,598.13 |

Liability at Dec. 31, Y3: $51,401.87 + $3,598.13 = **$55,000.00**.

*January 1, Year 4 — final payment (settlement of remaining liability)*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 55,000.00 | |
| Cash | | 55,000.00 |
| *Final payment — liability fully settled* | | |

**Check:** Dr 55,000 = Cr 55,000. **Balanced.** Ending liability = **$0**.

*December 31, Year 4 — final ROU amortization (asset reverts; no residual JE)*

ROU before final amort (after 3 years × $49,834.35): $199,337.38 − $149,503.05 = **$49,834.33**.

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 49,834.33 | |
| Right-of-Use Asset | | 49,834.33 |
| *Final SL amort — ROU fully written off at lease end* | | |

**Check:** Dr 49,834.33 = Cr 49,834.33. **Balanced.**  
ROU ending balance = **$0**. No gain/loss on reversion (unguaranteed residual is lessor’s; Meridian has no residual guarantee to settle).

**g. Presentation — Dec. 31, Year 1 (finance lease)**

| Item | Amount |
|---|---:|
| ROU asset (net) | **$149,503.03** |
| Current lease liability | **$55,000.00** (= next payment = accrued interest $10,103.62 + principal reduction $44,896.38) |
| Noncurrent lease liability | **$99,441.00** (= total liability $154,441.00 − current $55,000.00) |
| Income statement — Year 1 | **Interest expense $10,103.62** and **amortization expense $49,834.35** reported **separately** (not a single “lease expense”) |

**Key insight:** LO 17-1 classification drives the entire measurement path. Meeting the **term** and/or **PV** test makes this a **finance** lease: PV the payments with the **implicit rate**, book ROU = liability, run an **effective-interest liability schedule**, accrue interest and amortize ROU **separately**, and settle the liability to **zero** with the final payment when the asset reverts.

---

### Q2 — CORE number variant — Classify, measure, full schedule, mid-life period-end & payment, final settlement
**LO:** LO 17-1  
**Concept:** Number-variant twin — reclassify with changed life/term/rate/payments; recompute PV; initial JEs; full liability schedule; period-end interest and ROU amort; final maturity settlement  
**Scenario:**  
**Cedarline Logistics Corp.** (calendar year) leases a serial-numbered refrigerated trailer from **Apex Fleet Partners** commencing **January 1, Year 1**. Cedarline has exclusive use and directs routing and cargo. Apex has **no** substantive substitution right.

| Item | Amount / fact |
|---|---|
| Fair value of trailer | **$140,000** |
| Remaining economic life | **6 years** |
| Lease term | **5 years** noncancellable |
| Annual payment | **$32,000** due **beginning** of each year (Jan. 1), first payment Jan. 1, Year 1 |
| Ownership transfer / purchase option | **Neither** |
| Residual guarantee | **None**; residual expected **$0** for lessee analysis |
| Alternative use to lessor | Trailer is standard fleet unit — **yes**, alternative use |
| Implicit rate | **8%**, known by Cedarline |
| Incremental borrowing rate | **10%** |
| IDC / incentives | **None** |

**Required:**  
a. Classify the lease for Cedarline (evaluate term and PV tests at minimum; state conclusion).  
b. Compute PV / ROU / liability. Prepare **Jan. 1, Year 1** recognition and payment JEs.  
c. Prepare the **full 5-payment lease liability schedule**.  
d. Prepare **Dec. 31, Year 2** period-end interest and ROU amortization JEs (after Year 2 has already had its Jan. 1 payment recorded).  
e. Prepare the **Jan. 1, Year 5 final payment** JE and state ending liability. State annual ROU amortization and final-year amount.

**Answer key:**  

**a. Classification — finance lease**

| Criterion | Analysis | Met? |
|---|---|:---:|
| Ownership transfer | No | No |
| Purchase option | No | No |
| Lease term | 5 ÷ 6 = **83.33% ≥ 75%** | **Yes** |
| PV of payments | PV (below) **$137,988.06** ≥ 90% × $140,000 = **$126,000** | **Yes** |
| No alternative use | Standard fleet trailer | No |

**Finance lease.** Discount rate = **implicit 8%** (known).

**b. Initial measurement and JEs**

`=PV(0.08,5,-32000,0,1)` = **$137,988.06**  
ROU asset = lease liability = **$137,988.06**.

*January 1, Year 1 — commencement*

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 137,988.06 | |
| Lease Liability | | 137,988.06 |

**Check:** Dr = Cr = 137,988.06. **Balanced.**

*January 1, Year 1 — first payment*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 32,000.00 | |
| Cash | | 32,000.00 |

**Check:** Balanced. Liability after payment: **$105,988.06**.

**c. Lease liability subsequent measurement schedule (8%)**

| Date | Lease payment | Interest (8%) | Liability reduction | Ending liability |
|---|---:|---:|---:|---:|
| Jan. 1, Y1 before pmt | — | — | — | **137,988.06** |
| Jan. 1, Year 1 | 32,000.00 | 0.00 | 32,000.00 | 105,988.06 |
| Jan. 1, Year 2 | 32,000.00 | 8,479.04 | 23,520.96 | 82,467.10 |
| Jan. 1, Year 3 | 32,000.00 | 6,597.37 | 25,402.63 | 57,064.47 |
| Jan. 1, Year 4 | 32,000.00 | 4,565.16 | 27,434.84 | 29,629.63 |
| Jan. 1, Year 5 | 32,000.00 | 2,370.37 | 29,629.63 | **0.00** |
| **Totals** | **160,000.00** | **22,011.94** | **137,988.06** | |

**Checks:** total interest = $160,000 − $137,988.06 = **$22,011.94**; final balance **$0**.

Interest details:  
- $105,988.06 × 8% = **$8,479.04**  
- $82,467.10 × 8% = **$6,597.37**  
- $57,064.47 × 8% = **$4,565.16**  
- $29,629.63 × 8% = **$2,370.37**

**d. December 31, Year 2 period-end entries**

After Jan. 1, Year 2 payment, liability = **$82,467.10**.  
Year 2 interest (accrues during Year 2) = **$6,597.37**.

*December 31, Year 2 — interest*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 6,597.37 | |
| Lease Liability | | 6,597.37 |

**Check:** Balanced. Liability Dec. 31, Y2: $82,467.10 + $6,597.37 = **$89,064.47**.

ROU annual amort = $137,988.06 ÷ 5 = **$27,597.61** (Years 1–4); Year 5 = **$27,597.62**.

*December 31, Year 2 — ROU amortization*

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 27,597.61 | |
| Right-of-Use Asset | | 27,597.61 |

**Check:** Balanced.  
ROU after 2 years: $137,988.06 − 2 × $27,597.61 = **$82,792.84**.

**e. Final settlement — January 1, Year 5**

After Dec. 31, Year 4 interest accrual of $2,370.37, liability = $29,629.63 + $2,370.37 = **$32,000.00**.

*January 1, Year 5 — final payment*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 32,000.00 | |
| Cash | | 32,000.00 |
| *Maturity settlement — liability extinguished* | | |

**Check:** Balanced. Ending lease liability = **$0**.  
Final ROU amort Year 5: **$27,597.62** → ROU = **$0** after Dec. 31, Year 5 entry (asset reverts; no residual settlement JE for lessee).

**Key insight:** Changing every input (FV, life, term, rate, payment) still follows the same LO 17-1 → measurement pipeline: **classify with 75%/90% bright lines**, discount at the **implicit rate when known**, build the **liability schedule**, and **settle to zero** at the final payment.

---

### Q3 — CORE alternate angle — Multi-scenario identification & classification; presentation contrast
**LO:** LO 17-1  
**Concept:** Identify whether a contract is a lease (control vs service / substitution); apply all five classification criteria across scenarios; determine finance vs operating; classification-driven presentation differences  
**Scenario:**  
**Redrock Analytics LLC** is negotiating equipment and facility arrangements. For each independent case, answer the questions posed. Use the **75%** term test and **90%** PV test unless stated otherwise. Redrock is the **lessee**.

**Case A — Identify lease vs service**  
Redrock contracts with **CloudRail Hosting** for 3 years of “guaranteed computing capacity.” CloudRail may fulfill the contract from **any** of its identical servers in a large pool and **routinely reallocates** servers for its own cost savings; Redrock cannot prevent substitution. Redrock receives only a specified level of processing capacity, not a particular machine.

**Case B — Classification Option Set (four separate negotiations for the same class of equipment, FV $250,000, economic life 10 years, no ownership transfer, no alternative-use restriction unless noted)**

| Fact | Option 1 | Option 2 | Option 3 | Option 4 |
|---|---|---|---|---|
| Purchase option | None | None | Option to buy at end for **$15,000**; expected FV at end **$55,000** (Redrock reasonably certain to exercise) | None |
| Lease term | **6 years** | **8 years** | **6 years** | **6 years** |
| Annual payment | **$40,000** at **end** of each year | $40,000 end of year | $42,000 end of year | **$45,000** at **beginning** of each year |
| Rate known by lessee | IBR **6%** (implicit unknown) | IBR 6% | Implicit **5.5%** known | IBR 6% (implicit unknown) |
| Other | — | — | — | — |

**Case C — Presentation**  
Assume Option 2 is classified as a finance lease and a different short warehouse lease meets **none** of the five criteria (operating). Briefly contrast Year 1 **income statement** presentation for finance vs operating lessee accounting (basic leases).

**Required:**  
a. **Case A:** Does the contract contain a **lease**? Explain.  
b. **Case B:** For **each** of Options 1–4, evaluate the relevant criteria and conclude **finance** or **operating**. Show PV computations where the PV test is needed or informative.  
c. **Case C:** Contrast finance vs operating **expense presentation** for the lessee.

**Answer key:**  

**a. Case A — Not a lease (service arrangement)**

CloudRail has a **substantive substitution right**: practical ability to substitute alternative servers throughout the period of use **and** economic benefit from doing so. Redrock does **not** have the right to control an **identified asset** — only a capacity service.  
→ Account for as a **service contract** (expense as incurred); **no** ROU asset / lease liability under Topic 842 from this arrangement alone.

**b. Case B — Classification by option**

**Option 1 — Operating**

| Criterion | Result |
|---|---|
| Ownership / PO / no alt. use | Not met |
| Term | 6 ÷ 10 = **60% < 75%** → not met |
| PV | Ordinary annuity: `=PV(0.06,6,-40000,0,0)` = **$196,692.97** < 90% × $250,000 = **$225,000** → not met |

**No criteria met → operating lease.**

**Option 2 — Finance (term criterion)**

| Criterion | Result |
|---|---|
| Term | 8 ÷ 10 = **80% ≥ 75%** → **met** |
| Others | Not needed once one criterion is met |

**≥1 criterion met → finance lease.**  
(Optional PV check: `=PV(0.06,8,-40000,0,0)` = **$248,391.75** ≥ $225,000 — PV also met.)

**Option 3 — Finance (purchase option)**

Bargain / significant economic incentive: exercise price **$15,000** vs expected FV **$55,000** → lessee is **reasonably certain** to exercise.  
**Purchase option criterion met → finance lease.**  
(Lease term for measurement would include the PO path; renewal analysis is secondary once a reasonably certain PO exists.)

**Option 4 — Finance (PV criterion)**

Term 6/10 = 60% fails term test.  
PV annuity due: `=PV(0.06,6,-45000,0,1)` = **$234,556.37** ≥ **$225,000** (90% of FV) → **PV criterion met → finance lease.**

**Summary:**

| Option | Classification | Primary criterion met |
|---|---|---|
| 1 | **Operating** | None |
| 2 | **Finance** | Lease term (also PV) |
| 3 | **Finance** | Purchase option reasonably certain |
| 4 | **Finance** | PV of lease payments |

**c. Case C — Presentation contrast (lessee)**

| | Finance lease | Operating lease (basic) |
|---|---|---|
| Balance sheet | ROU asset + lease liability (both types) | ROU asset + lease liability (both types) |
| Income statement | **Interest expense** (effective interest on liability) **and amortization expense** (typically SL on ROU) — **two lines**, front-loaded total expense | Single **lease expense** on a **straight-line** basis over the term (interest and ROU reduction are combined into one lease expense pattern) |
| Classification timing | Determined at **commencement** using the five criteria | Same — if **zero** criteria met |

**Key insight:** LO 17-1 is a **gate**: first confirm a **lease** exists (identified asset + control, no substantive substitution), then run the **five tests**. One “yes” → finance (separate interest + amort); all “no” → operating (straight-line lease expense). The 75% and 90% thresholds are the standard assignment bright lines.

---

### Q4 — MC — Classification criterion application
**LO:** LO 17-1  
**Concept:** Apply lease classification criteria (term test and when term test is ignored near end of life)  
**Question:**  
**Summit Ridge Dental Group** leases imaging equipment with a **total economic life of 10 years**. The equipment is already **8 years old** at commencement (remaining life **2 years**). The noncancellable lease term is **2 years** (100% of remaining life). There is no ownership transfer, no purchase option, PV of payments is **70%** of fair value, and the asset has alternative use to the lessor. Which statement is **correct** under the reasonable approaches in ASC 842 (75% / last-25% guidance used in this course)?

- A) Finance lease solely because the term is 100% of remaining economic life (term criterion always uses remaining life, with no exception).  
- B) The **lease term length criterion is not used** for classification because commencement falls in the **last 25%** of the asset’s **total** economic life; if no other criterion is met, the lease is **operating**.  
- C) Operating lease because PV is only 70% of FV, and the term test is irrelevant whenever PV fails.  
- D) Finance lease under the “no alternative use” criterion because the asset is used in a specialized dental practice.

**Answer:** **B.**  
When commencement is in the **last 25% of total economic life** (here, years 9–10 of a 10-year life), ASC 842 directs that the **major-part-of-life (term) criterion shall not be used**. With ownership, PO, PV (70% < 90%), and no-alternative-use all failing, the lessee classifies the lease as **operating**. A is wrong because of the last-25% exception. C misstates the interaction of tests (each criterion is independent). D invents a no-alternative-use conclusion not supported by the facts (alternative use to lessor exists).

---

### Q4b — MC — Identify lease (substitution)
**LO:** LO 17-1  
**Concept:** Substantive substitution right prevents lease identification  
**Question:**  
Which arrangement is **least likely** to contain a lease for the customer under ASC 842?

- A) Lease of a **named** delivery van (VIN specified); customer decides routes and keeps substantially all benefits of use for 4 years; lessor cannot substitute.  
- B) Contract for use of a **specific floor** of a warehouse, explicitly identified; customer controls operations on that floor; landlord cannot relocate the customer.  
- C) Contract for **shipping capacity** on a carrier’s network where the carrier may use **any** of its interchangeable trailers and regularly substitutes units to optimize its fleet, benefiting economically, and the customer cannot prevent substitution.  
- D) Lease of customized production equipment **explicitly identified**, with no substitution rights, for 6 years.

**Answer:** **C.**  
A substantive lessor substitution right (practical ability + economic benefit) means the customer does **not** control an **identified asset** throughout the period of use → typically a **service**, not a lease. A, B, and D describe identified assets with customer control and no substantive substitution.

---

### Self-check
- [x] Every JE balances (Dr = Cr)
- [x] Math recomputed (PV factors, interest = rate × carrying amount, schedules roll to zero, ROU amort sums to initial ROU)
- [x] Core demo not sidebar-only (Demo 17-1 classification criteria + lessee finance measurement path from chapter core)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4 and Q4b only)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (emphasis), period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
