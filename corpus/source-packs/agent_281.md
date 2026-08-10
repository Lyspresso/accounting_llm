# Agent 281 — CORE DEMO — LO 17-1

**Chapter:** 17  
**LO title:** Identify a lease, determine lease types for lessee, and classify leases using lease criteria  
**Critical gap LO:** yes  
**Emphasis:** period_end_adjusting_JE

## Concept list for this pack
- **Identify a lease:** contract (or part of a contract) conveying the **right to control** the use of an **identified asset** for a period of time in exchange for consideration (substantially all economic benefits + right to direct use; no substantive lessor substitution right)
- **Lessee lease types:** **finance** (≥1 of 5 classification criteria met) vs **operating** (none met); short-term exception is separate (LO 17-9)
- **Five classification criteria:** (1) ownership transfer, (2) purchase option reasonably certain to exercise, (3) lease term ≥ major part of remaining economic life (**75%**), (4) PV of lease payments ≥ substantially all of FV (**90%**), (5) no alternative use to lessor
- **Discount rate:** rate **implicit** in the lease if readily determinable; otherwise lessee’s **incremental borrowing rate**
- **Initial recognition JE:** at commencement, **ROU asset** and **lease liability** at PV of lease payments; first annuity-due payment reduces liability only (no interest yet)
- **Subsequent measurement schedule:** effective-interest **lease liability schedule**; ROU amortized **straight-line** over lease term (or useful life if ownership transfer / reasonably certain PO)
- **Period-end adjusting JE (emphasis):** accrue **interest expense** on the lease liability (effective interest) and record **ROU amortization** (finance: separate lines)
- **Disposal / maturity / settlement JE:** final payment settles remaining liability; final ROU amort zeros the asset when it reverts with no residual guarantee
- **Classification / presentation / disclosure:** finance vs operating at commencement; finance IS shows interest and amortization **separately**; current vs noncurrent lease liability split at year-end
- **Number-variant twin:** same pipeline with all amounts, rates, and terms changed

---

### Q1 — CORE — Identify & classify finance lease; initial JE; liability schedule; **period-end adjusting JEs (emphasis)**; maturity settlement; presentation
**LO:** LO 17-1  
**Concept:** Identify lease; apply five criteria (term + PV); measure ROU/liability; initial recognition; full liability schedule; **period-end interest and ROU amortization adjusting JEs**; maturity settlement; finance presentation  
**Scenario:**  
**Brookhaven Packaging Co.** (calendar-year lessee) enters a contract with **Summit Capital Equipment** on **January 1, Year 1** (commencement). Summit delivers a serial-numbered high-speed carton-sealing line for Brookhaven’s exclusive use. Brookhaven decides run schedules and product configurations. Summit has **no practical ability** to substitute a different machine during the term.

**Contract terms:**
| Item | Amount / fact |
|---|---|
| Fair value of equipment at commencement | **$180,000** |
| Remaining economic life | **5 years** |
| Noncancellable lease term | **4 years** |
| Annual lease payment (fixed) | **$48,000** due **Jan. 1** each year (annuity due); first payment **Jan. 1, Year 1** |
| Ownership transfer at end of term | **No** — asset reverts to Summit |
| Purchase option | **None** |
| Residual value guarantee | **None**; estimated residual at lease end treated as **$0** for Brookhaven’s analysis |
| Specialized / no alternative use | Equipment is **standard** sealing-line gear Summit routinely re-leases |
| Rate implicit in the lease | **6%**, **known** by Brookhaven |
| Brookhaven’s incremental borrowing rate | **8%** |
| Initial direct costs / lease incentives | **None** |
| Accounting policy | Credit ROU asset directly for amortization (textbook style); round to nearest cent; plug final-period interest residual so liability ends at zero |

**Required:**  
a. **Identify:** Does the contract contain a **lease** under ASC 842? Explain using the two control criteria and substitution.  
b. **Classify:** Evaluate **all five** lease classification criteria. Conclude finance vs operating for Brookhaven. Which discount rate does Brookhaven use?  
c. Compute the **lease liability** and **ROU asset** at commencement (before the first payment). Prepare the **January 1, Year 1** initial recognition JE and the **first payment** JE.  
d. Prepare the full **lease liability subsequent measurement schedule** (date, lease payment, interest on liability, liability reduction, ending liability).  
e. **(Emphasis)** Prepare **all Year 1 period-end adjusting JEs** (Dec. 31) and the **Jan. 1, Year 2** payment JE. Explain why the Dec. 31 interest entry is an **adjusting** entry.  
f. Prepare the **maturity / settlement path for Year 4**: Dec. 31, Year 3 interest accrual, Jan. 1, Year 4 final payment, and Dec. 31, Year 4 final ROU amortization. Show liability and ROU are zero after lease end.  
g. **Presentation:** For Dec. 31, Year 1, state (1) ROU asset carrying amount, (2) current lease liability, (3) noncurrent lease liability, and (4) how Year 1 lease-related expenses appear on the income statement for a **finance** lease.

**Answer key:**  

**a. Identify — contract contains a lease**

Yes. At inception/commencement analysis:
1. **Identified asset:** sealing line is **explicitly specified** (serial number).  
2. **Substantially all economic benefits:** Brookhaven has exclusive use for packaging operations over the term.  
3. **Right to direct use:** Brookhaven operates the line and decides output/configuration.  
4. **No substantive substitution right:** Summit cannot practically substitute without Brookhaven’s consent / does not have a substitution right that economically benefits Summit as described.

→ Brookhaven obtains the **right to control the use** of an identified asset for a period of time in exchange for consideration → **lease**.

**b. Classification (lessee) — finance lease**

| Criterion | Analysis | Met? |
|---|---|:---:|
| 1. Ownership transfer | Asset reverts to Summit; no automatic legal title transfer | No |
| 2. Purchase option | No purchase option | No |
| 3. Lease term length | Term 4 ÷ life 5 = **80% ≥ 75%** (major part of remaining economic life); commencement is not in the last 25% of total life | **Yes** |
| 4. PV of lease payments | PV (below) **$176,304.57** ≥ 90% × $180,000 = **$162,000** | **Yes** |
| 5. No alternative use | Standard equipment routinely re-leased — alternative use exists | No |

**Conclusion:** At least one criterion met → **finance lease** for Brookhaven.  
**Discount rate:** Use **implicit rate 6%** (readily determinable); ignore 8% IBR.

**PV of lease payments (annuity due, n = 4, i = 6%, PMT = $48,000):**  
Excel: `=PV(0.06,4,-48000,0,1)` = **$176,304.57**  
(Equivalently: \(48{,}000 \times \sum_{t=0}^{3} (1.06)^{-t}\).)

**c. Initial measurement and January 1, Year 1 JEs**

Lease liability = ROU asset = **$176,304.57** (basic lease: no prepaid, IDC, or incentives).

*January 1, Year 1 — recognize ROU asset and lease liability*

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 176,304.57 | |
| Lease Liability | | 176,304.57 |
| *Commencement — finance lease of carton-sealing line* | | |

**Check:** Dr 176,304.57 = Cr 176,304.57. **Balanced.**

*January 1, Year 1 — first lease payment (annuity due; no interest yet)*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 48,000.00 | |
| Cash | | 48,000.00 |
| *Payment 1 of 4 — all principal* | | |

**Check:** Dr 48,000 = Cr 48,000. **Balanced.**  
Liability after payment: $176,304.57 − $48,000.00 = **$128,304.57**.

**d. Subsequent measurement — lease liability schedule (effective interest, 6%)**

Interest each period after the first payment = **6% × liability balance after prior payment**.  
Principal reduction = payment − interest. Final period plugs residual so ending liability = $0.

| Date | Lease payment | Interest on liability (6%) | Liability reduction | Ending lease liability |
|---|---:|---:|---:|---:|
| Jan. 1, Y1 (commencement, before pmt) | — | — | — | **176,304.57** |
| Jan. 1, Year 1 | 48,000.00 | 0.00 | 48,000.00 | 128,304.57 |
| Jan. 1, Year 2 | 48,000.00 | 7,698.27 | 40,301.73 | 88,002.84 |
| Jan. 1, Year 3 | 48,000.00 | 5,280.17 | 42,719.83 | 45,283.01 |
| Jan. 1, Year 4 | 48,000.00 | 2,716.99 | 45,283.01 | **0.00** |
| **Totals** | **192,000.00** | **15,695.43** | **176,304.57** | |

**Schedule checks:**  
- Total reductions = initial PV = **$176,304.57**  
- Total interest = total cash − PV = $192,000.00 − $176,304.57 = **$15,695.43**  
- Ending balance after final payment = **$0**

**Interest computation detail:**  
- Year 1 interest (accrued Dec. 31, Y1 / paid as part of Jan. 1, Y2): $128,304.57 × 6% = **$7,698.27**  
- Year 2: $88,002.84 × 6% = **$5,280.17**  
- Year 3: plug so final reduction clears liability: $48,000.00 − $45,283.01 = **$2,716.99** (vs $45,283.01 × 6% = $2,716.98 before plug)

**ROU amortization (straight-line over 4-year lease term; no ownership transfer / PO):**  
Annual = $176,304.57 ÷ 4 → **$44,076.14** for Years 1–3; Year 4 **$44,076.15** (penny so cumulative = $176,304.57).

**e. Year 1 period-end adjusting JEs (emphasis) and Year 2 payment**

*Why adjusting?* Payments occur on **January 1**. During Year 1 the liability balance after the first payment ($128,304.57) accrues interest for the full year, and the ROU asset is consumed over the year. At **December 31**, Brookhaven must **adjust** the accounts before financial statements are issued — no cash changes hands on Dec. 31 for these accruals.

*December 31, Year 1 — interest on lease liability (period-end adjusting)*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 7,698.27 | |
| Lease Liability | | 7,698.27 |
| *Accrue interest: $128,304.57 × 6%* | | |

**Check:** Dr 7,698.27 = Cr 7,698.27. **Balanced.**  
Liability at Dec. 31, Y1: $128,304.57 + $7,698.27 = **$136,002.84**.

*December 31, Year 1 — ROU amortization (period-end adjusting)*

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 44,076.14 | |
| Right-of-Use Asset | | 44,076.14 |
| *SL amort: $176,304.57 / 4* | | |

**Check:** Dr 44,076.14 = Cr 44,076.14. **Balanced.**  
ROU at Dec. 31, Y1: $176,304.57 − $44,076.14 = **$132,228.43**.

*January 1, Year 2 — lease payment (settles accrued interest + principal; not an adjusting entry)*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 48,000.00 | |
| Cash | | 48,000.00 |
| *Payment 2: $7,698.27 interest portion + $40,301.73 principal* | | |

**Check:** Dr 48,000 = Cr 48,000. **Balanced.**  
Liability after payment: $136,002.84 − $48,000.00 = **$88,002.84**.

**f. Maturity / settlement — Year 4**

After Jan. 1, Year 3 payment, liability (before Year 3 interest) = **$45,283.01**.

*December 31, Year 3 — period-end interest accrual*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 2,716.99 | |
| Lease Liability | | 2,716.99 |

**Check:** Balanced. Liability at Dec. 31, Y3: $45,283.01 + $2,716.99 = **$48,000.00**.

*January 1, Year 4 — final payment (settlement of remaining liability)*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 48,000.00 | |
| Cash | | 48,000.00 |
| *Final payment — liability fully settled* | | |

**Check:** Dr 48,000 = Cr 48,000. **Balanced.** Ending liability = **$0**.

*December 31, Year 4 — final ROU amortization (asset reverts; no residual JE)*

ROU before final amort (after 3 × $44,076.14): $176,304.57 − $132,228.42 = **$44,076.15**.

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 44,076.15 | |
| Right-of-Use Asset | | 44,076.15 |
| *Final SL amort — ROU fully written off at lease end* | | |

**Check:** Dr 44,076.15 = Cr 44,076.15. **Balanced.**  
ROU ending balance = **$0**. No gain/loss on reversion (no residual guarantee for Brookhaven).

**g. Presentation — Dec. 31, Year 1 (finance lease)**

| Item | Amount |
|---|---:|
| ROU asset (net) | **$132,228.43** |
| Current lease liability | **$48,000.00** (= next payment = accrued interest $7,698.27 + principal reduction $40,301.73) |
| Noncurrent lease liability | **$88,002.84** (= total liability $136,002.84 − current $48,000.00) |
| Income statement — Year 1 | **Interest expense $7,698.27** and **amortization expense $44,076.14** reported **separately** (not a single “lease expense”) |

**Key insight:** LO 17-1 classification drives measurement. Meeting the **term** and/or **PV** test → **finance** lease: PV payments at the **implicit rate**, book ROU = liability, run the **effective-interest schedule**, and at **each period-end** adjust for **interest accrual** and **ROU amortization** separately before settling the liability to **zero** with the final payment.

---

### Q2 — CORE number variant — Classify, measure, full schedule, **mid-life period-end adjusting JEs**, final settlement
**LO:** LO 17-1  
**Concept:** Number-variant twin — reclassify with changed life/term/rate/payments; recompute PV; initial JEs; full liability schedule; **Year 2 period-end interest and ROU amort adjusting JEs**; final maturity settlement  
**Scenario:**  
**Ironvale Mining LLC** (calendar year) leases a serial-numbered haul truck from **Crestline Fleet Finance** commencing **January 1, Year 1**. Ironvale has exclusive use and directs routing and loads. Crestline has **no** substantive substitution right.

| Item | Amount / fact |
|---|---|
| Fair value of truck | **$265,000** |
| Remaining economic life | **6 years** |
| Lease term | **5 years** noncancellable |
| Annual payment | **$58,000** due **beginning** of each year (Jan. 1), first payment Jan. 1, Year 1 |
| Ownership transfer / purchase option | **Neither** |
| Residual guarantee | **None**; residual expected **$0** for lessee analysis |
| Alternative use to lessor | Truck is standard fleet unit — **yes**, alternative use |
| Implicit rate | **7%**, known by Ironvale |
| Incremental borrowing rate | **9%** |
| IDC / incentives | **None** |

**Required:**  
a. Classify the lease for Ironvale (evaluate all five criteria; state conclusion and discount rate).  
b. Compute PV / ROU / liability. Prepare **Jan. 1, Year 1** recognition and payment JEs.  
c. Prepare the **full 5-payment lease liability schedule**.  
d. **(Emphasis)** Prepare **Dec. 31, Year 2** period-end interest and ROU amortization adjusting JEs (after the Jan. 1, Year 2 payment has already been recorded). Show Dec. 31, Year 2 current / noncurrent liability split.  
e. Prepare the **Jan. 1, Year 5 final payment** JE (after Dec. 31, Year 4 interest has been accrued). State annual ROU amortization and that both balances zero at lease end.

**Answer key:**  

**a. Classification — finance lease**

| Criterion | Analysis | Met? |
|---|---|:---:|
| Ownership transfer | No | No |
| Purchase option | No | No |
| Lease term | 5 ÷ 6 = **83.33% ≥ 75%** | **Yes** |
| PV of payments | PV (below) **$254,458.25** ≥ 90% × $265,000 = **$238,500** | **Yes** |
| No alternative use | Standard fleet truck | No |

**Finance lease.** Discount rate = **implicit 7%** (known); ignore 9% IBR.

**b. Initial measurement and JEs**

`=PV(0.07,5,-58000,0,1)` = **$254,458.25**  
ROU asset = lease liability = **$254,458.25**.

*January 1, Year 1 — commencement*

| Account | Debit | Credit |
|---|---:|---:|
| Right-of-Use Asset | 254,458.25 | |
| Lease Liability | | 254,458.25 |

**Check:** Dr = Cr = 254,458.25. **Balanced.**

*January 1, Year 1 — first payment*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 58,000.00 | |
| Cash | | 58,000.00 |

**Check:** Balanced. Liability after payment: **$196,458.25**.

**c. Lease liability subsequent measurement schedule (7%)**

| Date | Lease payment | Interest (7%) | Liability reduction | Ending liability |
|---|---:|---:|---:|---:|
| Jan. 1, Y1 before pmt | — | — | — | **254,458.25** |
| Jan. 1, Year 1 | 58,000.00 | 0.00 | 58,000.00 | 196,458.25 |
| Jan. 1, Year 2 | 58,000.00 | 13,752.08 | 44,247.92 | 152,210.33 |
| Jan. 1, Year 3 | 58,000.00 | 10,654.72 | 47,345.28 | 104,865.05 |
| Jan. 1, Year 4 | 58,000.00 | 7,340.55 | 50,659.45 | 54,205.60 |
| Jan. 1, Year 5 | 58,000.00 | 3,794.40 | 54,205.60 | **0.00** |
| **Totals** | **290,000.00** | **35,541.75** | **254,458.25** | |

**Checks:** total interest = $290,000 − $254,458.25 = **$35,541.75**; final balance **$0**.  
Interest detail: $196,458.25 × 7% = **$13,752.08**; $152,210.33 × 7% = **$10,654.72**; $104,865.05 × 7% = **$7,340.55**; final plug $58,000 − $54,205.60 = **$3,794.40**.

**d. December 31, Year 2 period-end adjusting entries (emphasis)**

After Jan. 1, Year 2 payment, liability = **$152,210.33**.  
Year 2 interest (accrues during Year 2 for the Dec. 31 adjusting entry) = **$10,654.72**.

*December 31, Year 2 — interest (period-end adjusting)*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 10,654.72 | |
| Lease Liability | | 10,654.72 |
| *Accrue interest: $152,210.33 × 7%* | | |

**Check:** Balanced. Liability Dec. 31, Y2: $152,210.33 + $10,654.72 = **$162,865.05**.

ROU annual amort = $254,458.25 ÷ 5 = **$50,891.65** each year.

*December 31, Year 2 — ROU amortization (period-end adjusting)*

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 50,891.65 | |
| Right-of-Use Asset | | 50,891.65 |

**Check:** Balanced.  
ROU after 2 years: $254,458.25 − 2 × $50,891.65 = **$152,674.95**.

**Dec. 31, Year 2 presentation:**
| Item | Amount |
|---|---:|
| Current lease liability | **$58,000.00** (next payment) |
| Noncurrent lease liability | **$104,865.05** ($162,865.05 − $58,000.00) |
| ROU asset (net) | **$152,674.95** |

**e. Final settlement — January 1, Year 5**

After Dec. 31, Year 4 interest accrual of $3,794.40, liability = $54,205.60 + $3,794.40 = **$58,000.00**.

*January 1, Year 5 — final payment*

| Account | Debit | Credit |
|---|---:|---:|
| Lease Liability | 58,000.00 | |
| Cash | | 58,000.00 |
| *Maturity settlement — liability extinguished* | | |

**Check:** Balanced. Ending lease liability = **$0**.  
Annual ROU amort **$50,891.65** × 5 = **$254,458.25** → ROU = **$0** after Dec. 31, Year 5 amort (asset reverts; no residual settlement JE for lessee).

**Key insight:** Changing every input (FV, life, term, rate, payment) still follows the same LO 17-1 → measurement pipeline: **classify with 75%/90% bright lines**, discount at the **implicit rate when known**, build the **liability schedule**, and at **each year-end adjust** for interest and ROU amort before **settling to zero** at the final payment.

---

### Q3 — CORE alternate angle — Multi-scenario identification & classification; **period-end adjusting JEs** for a finance case; presentation contrast
**LO:** LO 17-1  
**Concept:** Identify lease vs service (substitution); multi-scenario five-criteria classification (operating vs finance); **period-end adjusting JEs only** for a short finance lease; finance vs operating expense presentation  
**Scenario:**  
**Pinnacle Lab Diagnostics Inc.** is reviewing equipment and facility arrangements. For each independent case, answer the questions posed. Use the **75%** term test and **90%** PV test unless stated otherwise. Pinnacle is the **lessee** (calendar year-end).

**Case A — Identify lease vs service**  
Pinnacle contracts with **AquaPure Logistics** for 4 years of “guaranteed cold-storage capacity.” AquaPure may fulfill the contract from **any** of its identical refrigerated bays in a large warehouse and **routinely reassigns** bays to optimize its own energy costs; Pinnacle cannot prevent reassignment. Pinnacle receives only a specified cubic-meter capacity, not a particular bay.

**Case B — Classification option set** (four separate negotiations for the same class of analytical instrument, FV **$120,000**, economic life **8 years**, no ownership transfer, no alternative-use restriction unless noted)

| Fact | Option 1 | Option 2 | Option 3 | Option 4 |
|---|---|---|---|---|
| Purchase option | None | None | Option to buy at end for **$8,000**; expected FV at end **$28,000** (Pinnacle reasonably certain to exercise) | None |
| Lease term | **3 years** | **6 years** | **3 years** | **3 years** |
| Annual payment | **$22,000** at **end** of each year | $22,000 end of year | $24,000 end of year | **$28,000** at **beginning** of each year |
| Rate known by lessee | IBR **8%** (implicit unknown) | IBR 8% | Implicit **6%** known | IBR 8% (implicit unknown) |
| Other | — | — | — | Specialized build; **no alternative use** to lessor at end |

**Case C — Period-end adjusting JEs (emphasis) for a basic finance lease**  
Assume a **separate** 3-year finance lease of a standard centrifuge (already classified finance because term = 3/3 = 100% of remaining life). Commencement **Jan. 1, Year 1**. Annual payment **$40,000** on **Jan. 1** each year (annuity due). Implicit rate **5%** known. PV at commencement = **$114,376.42**. After the Jan. 1, Year 1 payment, liability = **$74,376.42**. ROU amort is SL over 3 years.

**Case D — Presentation**  
Briefly contrast Year 1 **income statement** presentation for a **finance** vs a basic **operating** lease for the lessee.

**Required:**  
a. **Case A:** Does the contract contain a **lease**? Explain.  
b. **Case B:** For **each** of Options 1–4, evaluate relevant criteria and conclude **finance** or **operating**. Show PV where needed.  
c. **Case C:** Compute Year 1 interest and annual ROU amort. Prepare **only the Dec. 31, Year 1 period-end adjusting JEs**.  
d. **Case D:** Contrast finance vs operating **expense presentation**.

**Answer key:**  

**a. Case A — Not a lease (service arrangement)**

AquaPure has a **substantive substitution right**: practical ability to substitute alternative bays throughout the period of use **and** economic benefit from doing so. Pinnacle does **not** control an **identified asset** — only a capacity service.  
→ Account for as a **service contract** (expense as incurred); **no** ROU asset / lease liability under Topic 842 from this arrangement alone.

**b. Case B — Classification by option**

**Option 1 — Operating**

| Criterion | Result |
|---|---|
| Ownership / PO / no alt. use | Not met |
| Term | 3 ÷ 8 = **37.5% < 75%** → not met |
| PV | Ordinary annuity: `=PV(0.08,3,-22000,0,0)` = **$56,696.13** < 90% × $120,000 = **$108,000** → not met |

**No criteria met → operating lease.**

**Option 2 — Finance (term criterion)**

| Criterion | Result |
|---|---|
| Term | 6 ÷ 8 = **75% ≥ 75%** → **met** |
| Others | Not required once one criterion is met |

**≥1 criterion met → finance lease.**  
(Optional PV: `=PV(0.08,6,-22000,0,0)` = **$101,703.35** < $108,000 — term alone drives finance classification.)

**Option 3 — Finance (purchase option)**

Exercise price **$8,000** vs expected FV **$28,000** → significant economic incentive; lessee **reasonably certain** to exercise.  
**Purchase option criterion met → finance lease.**

**Option 4 — Finance (no alternative use; also check PV)**

Specialized build with **no alternative use to lessor** at end → **criterion 5 met → finance lease.**  
(Also: term 3/8 = 37.5% fails term test; PV annuity due `=PV(0.08,3,-28000,0,1)` = **$77,931.41** < $108,000 — PV fails, but no-alternative-use alone is enough.)

**Summary:**

| Option | Classification | Primary criterion met |
|---|---|---|
| 1 | **Operating** | None |
| 2 | **Finance** | Lease term |
| 3 | **Finance** | Purchase option reasonably certain |
| 4 | **Finance** | No alternative use |

**c. Case C — Period-end adjusting JEs only (emphasis)**

PV check: `=PV(0.05,3,-40000,0,1)` = **$114,376.42**; after first payment liability = **$74,376.42**.  
Year 1 interest = $74,376.42 × 5% = **$3,718.82**.  
ROU amort = $114,376.42 ÷ 3 = **$38,125.47** (Years 1–2); Year 3 **$38,125.48** so cumulative equals PV.

*December 31, Year 1 — interest accrual (adjusting)*

| Account | Debit | Credit |
|---|---:|---:|
| Interest Expense | 3,718.82 | |
| Lease Liability | | 3,718.82 |
| *Period-end accrual: $74,376.42 × 5%* | | |

**Check:** Dr 3,718.82 = Cr 3,718.82. **Balanced.**  
Liability after accrual: $74,376.42 + $3,718.82 = **$78,095.24**.

*December 31, Year 1 — ROU amortization (adjusting)*

| Account | Debit | Credit |
|---|---:|---:|
| Amortization Expense | 38,125.47 | |
| Right-of-Use Asset | | 38,125.47 |
| *SL amort of ROU over 3-year lease term* | | |

**Check:** Dr 38,125.47 = Cr 38,125.47. **Balanced.**  
ROU at Dec. 31, Y1: $114,376.42 − $38,125.47 = **$76,250.95**.

**Note:** The Jan. 1 payment is a **cash transaction**, not a period-end adjusting entry. Adjusting entries at year-end recognize **interest** and **amortization** that accrued since commencement / last payment.

**d. Case D — Presentation contrast (lessee)**

| | Finance lease | Operating lease (basic) |
|---|---|---|
| Balance sheet | ROU asset + lease liability | ROU asset + lease liability (both types) |
| Income statement | **Interest expense** (effective interest) **and amortization expense** (typically SL on ROU) — **two lines**, front-loaded total expense | Single **lease expense** on a **straight-line** basis over the term |
| Classification timing | At **commencement** using the five criteria | Same — if **zero** criteria met → operating |

**Key insight:** LO 17-1 is a **gate**: first confirm a **lease** exists (identified asset + control, no substantive substitution), then run the **five tests**. One “yes” → finance (separate interest + amort, with **period-end adjusting entries** each year); all “no” → operating (straight-line lease expense). The 75% and 90% thresholds are the standard assignment bright lines.

---

### Q4 — MC — Classification criterion when commencement is near end of life
**LO:** LO 17-1  
**Concept:** Term criterion not applied when commencement falls in the last 25% of total economic life  
**Question:**  
**Lakeshore Imaging Partners** leases a CT scanner with a **total economic life of 12 years**. The scanner is already **10 years old** at commencement (remaining life **2 years**). The noncancellable lease term is **2 years** (100% of remaining life). There is no ownership transfer, no purchase option, PV of payments is **65%** of fair value, and the asset has alternative use to the lessor. Which statement is **correct** under the reasonable approaches in ASC 842 (75% / last-25% guidance used in this course)?

- A) Finance lease solely because the term is 100% of remaining economic life (term criterion always uses remaining life, with no exception).  
- B) The **lease term length criterion is not used** for classification because commencement falls in the **last 25%** of the asset’s **total** economic life; if no other criterion is met, the lease is **operating**.  
- C) Operating lease because PV is only 65% of FV, and the term test is irrelevant whenever PV fails.  
- D) Finance lease under the “no alternative use” criterion because medical imaging equipment is always specialized.

**Answer:** **B.**  
When commencement is in the **last 25% of total economic life** (here, years 11–12 of a 12-year life), ASC 842 directs that the **major-part-of-life (term) criterion shall not be used**. With ownership, PO, PV (65% < 90%), and no-alternative-use all failing, the lessee classifies the lease as **operating**. A is wrong because of the last-25% exception. C misstates the interaction of tests (each criterion is independent). D invents a no-alternative-use conclusion not supported by the facts (alternative use to lessor exists).

---

### Q4b — MC — Identify lease (substantive substitution)
**LO:** LO 17-1  
**Concept:** Substantive substitution right — arrangement is not a lease  
**Question:**  
Which of the following arrangements is **least likely** to contain a lease under ASC 842?

- A) A 5-year contract for exclusive use of a specified delivery van (VIN identified); the customer routes and loads the van; the supplier cannot substitute another van without the customer’s consent.  
- B) A 4-year lease of a uniquely serial-numbered packaging machine that the lessee operates and reconfigures for its products; lessor has no substitution right.  
- C) A 3-year contract for “guaranteed forklift capacity” under which the supplier may freely swap any forklift from a large ready pool whenever it benefits the supplier, and the customer cannot prevent substitution.  
- D) A 6-year contract for a custom-fitted cleanroom suite identified by building and suite number; the lessee controls access and production activities inside the suite.

**Answer:** **C.**  
A substantive substitution right (practical ability to substitute **and** economic benefit to the supplier) means the customer does **not** have the right to use an **identified asset** throughout the period of use → **not a lease** (service arrangement). A, B, and D each describe an identified asset with customer control of use and no substantive substitution right → leases.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (PV annuity-due formulas; liability schedules roll to zero; ROU fully amortized)
- [x] Core demo not sidebar-only (Demo 17-1 classification criteria + lessee measurement path from chapter core)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (Q4 and Q4b only)
- [x] Emphasis on period_end_adjusting_JE (Q1e, Q2d, Q3c)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
