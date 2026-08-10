# Agent 269 — CORE DEMO — LO 14-6

**Chapter:** 14  
**LO title:** Accounting for Impairment Loss on AFS Investments  
**Critical gap LO:** yes  
**Emphasis angle:** period_end_adjusting_JE

## Concept list for this pack
- **AFS debt security impairment model (ASC 326-30):** assess impairment individually each reporting period when fair value < amortized cost
- **FV-OCI first:** period-end fair-value adjustment through OCI is recorded **before** impairment analysis (textbook Demo 14-6 assumption)
- **Intent-to-sell path:** if entity intends to sell (or more likely than not will be required to sell before recovery), write amortized cost down to fair value through **net income**; fair value becomes new cost basis; reverse related OCI/FVA
- **No-intent-to-sell path (period-end adjusting JE — emphasis):** credit-loss portion (amortized cost − PV of expected cash flows) recognized in **net income** with **Allowance for Credit Losses**, **limited** to the amount that fair value is less than amortized cost; noncredit residual stays in OCI via remaining FVA
- **HTM vs AFS vs equity-method contrast:** HTM uses CECL allowance; equity method OT TI write-down of investment (no subsequent reversal under textbook model)
- **Presentation/disclosure:** Allowance for Credit Losses contra to amortized cost; AFS rollforward of ACL; unrealized noncredit loss in AOCI
- **Disposal after impairment:** remove investment at amortized cost, clear FVA and ACL as applicable, recognize realized gain/loss in net income

---

### Q1 — CORE — AFS purchase, FV-OCI schedule, period-end impairment adjusting JE (no intent to sell), alternate intent-to-sell, and disposal
**LO:** LO 14-6  
**Concept:** Period-end adjusting JE for AFS impairment (credit vs noncredit); initial recognition; subsequent measurement FV-OCI schedule; intent-to-sell write-down; disposal JE  
**Scenario:**  
**Meridian Harbor Capital** (calendar-year) purchases **$200,000 par** of **Cascade Industrial 6% bonds** on **July 1, Year 1**, for **par**. Interest is paid **semiannually** on June 30 and December 31. Meridian classifies the bonds as **available-for-sale (AFS)** debt securities. Meridian’s reporting year ends December 31.

**December 31, Year 1 measurement data (after interest is recorded):**

| Item | Amount |
|---|---:|
| Amortized cost | $200,000 |
| Fair value | $185,000 |
| Present value of cash flows expected to be collected | $188,000 |
| Expected credit loss (amortized cost − PV of expected collections) | $12,000 |

Meridian has **already** recorded the year-end fair-value adjustment through **FV-OCI** for the full unrealized holding loss before analyzing impairment (per textbook Demo 14-6). Meridian **does not intend to sell** the bonds and it is **not more likely than not** that Meridian will be required to sell before recovery of amortized cost.

**Alternate assumption (part e only):** Same facts, except Meridian **intends to sell** the bonds after year-end.

**Year 2 disposal (part f):** Assume the **no-intent** accounting from parts c–d applies. On **March 15, Year 2**, Meridian sells the entire Cascade holding for **$187,500** cash. No interest is accrued between January 1 and March 15 for simplicity (focus on investment accounts). Immediately before sale, fair value still equals **$185,000** (so the December 31 Year 1 FVA and ACL balances are unchanged). Meridian updates any remaining FVA only as needed for the sale cleanup.

**Required:**  
a. Record the **July 1, Year 1 initial recognition** journal entry for the AFS purchase.  
b. Record the **December 31, Year 1 interest** receipt.  
c. Prepare the **subsequent measurement schedule** for the AFS investment at December 31, Year 1 (amortized cost, fair value, total unrealized holding loss, credit-loss component, noncredit residual). Then record the **period-end FV-OCI adjusting JE** for the full unrealized loss.  
d. **(Emphasis)** Determine the impairment loss to recognize in **net income** under the **no-intent-to-sell** path. Record the **December 31, Year 1 period-end impairment adjusting JE**. Show the net carrying amount after impairment (amortized cost − ACL ± FVA).  
e. Under the **intent-to-sell** alternate, determine the impairment loss in net income and record the **period-end impairment adjusting JE** (write-down of the investment; reverse full OCI/FVA). State the **new cost basis**.  
f. Using the **no-intent** balances from (d), record the **March 15, Year 2 disposal** journal entry(ies): clear the investment, FVA, and Allowance for Credit Losses; recognize any realized gain or loss.  
g. Briefly state how the **credit-loss** and **noncredit** portions of the Year 1 decline appear in the financial statements under the no-intent path.

**Answer key:**  

**a. July 1, Year 1 — initial recognition (purchase at par)**

| Account | Debit | Credit |
|---|---:|---:|
| Investment in AFS Securities—Cascade Bonds | 200,000 | |
| Cash | | 200,000 |
| *Purchase Cascade 6% bonds at par; classify as AFS* | | |

**Check:** Dr 200,000 = Cr 200,000. **Balanced.**

**b. December 31, Year 1 — interest revenue**

Cash interest = \(200{,}000 \times 0.06 \times 6/12 = \$6{,}000\)

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 6,000 | |
| Interest Revenue | | 6,000 |
| *Semiannual cash interest on AFS bonds* | | |

**Check:** Dr 6,000 = Cr 6,000. **Balanced.**

**c. Subsequent measurement schedule and FV-OCI period-end JE**

| AFS investment | Amortized cost | Fair value | Unrealized holding gain (loss) |
|---|---:|---:|---:|
| Cascade bonds | $200,000 | $185,000 | $(15,000)$ |
| Existing FVA balance | | | 0 |
| **Increase (decrease) needed in FVA** | | | **$(15,000)$** |

**Credit-loss / noncredit split (for impairment analysis):**

| Component | Computation | Amount |
|---|---|---:|
| Total FV shortfall | \(200{,}000 - 185{,}000\) | $15,000 |
| Expected credit loss | \(200{,}000 - 188{,}000\) | $12,000 |
| Noncredit residual | \(15{,}000 - 12{,}000\) | $3,000 |

**December 31, Year 1 — adjust AFS to fair value through OCI (before impairment)**

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—OCI | 15,000 | |
| Fair Value Adjustment—AFS | | 15,000 |
| *Record full unrealized holding loss in OCI; FVA valuation account* | | |

**Check:** Dr 15,000 = Cr 15,000. **Balanced.**  
After this entry: Investment (gross) $200,000 − FVA credit $15,000 = **$185,000** carrying amount; entire $15,000 still in OCI (pre-impairment).

**d. (Emphasis) No-intent-to-sell — impairment loss and period-end adjusting JE**

**Impairment loss in net income** = lesser of (i) expected credit loss **$12,000** and (ii) total FV shortfall **$15,000**  
→ **Impairment loss = $12,000** (full credit loss allowed; noncredit $3,000 remains in OCI).

**December 31, Year 1 — period-end adjusting JE for AFS credit impairment**

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 12,000 | |
| Fair Value Adjustment—AFS | 12,000 | |
| Allowance for Credit Losses—AFS | | 12,000 |
| Unrealized Gain or Loss—OCI | | 12,000 |
| *Reclassify credit portion of unrealized loss from OCI to NI; establish ACL* | | |

**Check:** Dr \(12{,}000 + 12{,}000 = 24{,}000\); Cr \(12{,}000 + 12{,}000 = 24{,}000\). **Balanced.**

**Account balances after impairment (no-intent path):**

| Account | Balance | Nature |
|---|---:|---|
| Investment in AFS—Cascade (amortized cost) | $200,000 | Asset |
| Allowance for Credit Losses—AFS | (12,000) | Contra asset |
| Fair Value Adjustment—AFS | (3,000) | Contra (remaining noncredit) |
| **Net carrying amount** | **$185,000** | Equals fair value |

OCI residual unrealized loss (AOCI) related to noncredit factors: **$3,000**.  
Year 1 **net income** includes Loss on Impairment **$12,000** (plus Interest Revenue $6,000).

**e. Intent-to-sell alternate — full write-down through NI**

Because Meridian intends to sell before recovery, the **entire** difference between amortized cost and fair value is recognized in **net income**. Fair value becomes the **new amortized cost basis**.

Impairment loss in NI = \(200{,}000 - 185{,}000 = \$15{,}000\).

**December 31, Year 1 — impairment when intent to sell (after FV-OCI entry in part c)**

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 15,000 | |
| Investment in AFS Securities—Cascade Bonds | | 15,000 |
| Fair Value Adjustment—AFS | 15,000 | |
| Unrealized Gain or Loss—OCI | | 15,000 |
| *Write amortized cost to FV through NI; reverse full OCI/FVA* | | |

**Check:** Dr \(15{,}000 + 15{,}000 = 30{,}000\); Cr \(15{,}000 + 15{,}000 = 30{,}000\). **Balanced.**

**New cost basis** of investment = **$185,000**. FVA and related OCI for this security are **zero**. (No separate ACL under this path in the textbook illustration—write-down is direct to the investment.)

**f. March 15, Year 2 — disposal under no-intent balances from (d)**

Pre-sale balances: Investment $200,000; ACL credit $12,000; FVA credit $3,000; cash proceeds $187,500.

Realized gain/loss vs **amortized cost net of ACL**:  
Net amortized cost = \(200{,}000 - 12{,}000 = 188{,}000\)  
Cash − net amortized cost = \(187{,}500 - 188{,}000 = \$(500)\) realized **loss**.

Clear FVA and reverse remaining noncredit OCI ($3,000).

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 187,500 | |
| Allowance for Credit Losses—AFS | 12,000 | |
| Fair Value Adjustment—AFS | 3,000 | |
| Loss on Sale of Investment | 500 | |
| Investment in AFS Securities—Cascade Bonds | | 200,000 |
| Unrealized Gain or Loss—OCI | | 3,000 |
| *Sell AFS bonds; clear ACL and residual FVA; realize loss vs net amortized cost* | | |

**Check:** Dr \(187{,}500 + 12{,}000 + 3{,}000 + 500 = 203{,}000\); Cr \(200{,}000 + 3{,}000 = 203{,}000\). **Balanced.**

*(Note: Over the holding period, total NI impact from price decline = impairment $12,000 in Y1 + sale loss $500 in Y2 − any prior OCI reclassifications already reflected; net cash shortfall vs original cost $200,000 is $12,500 = $200,000 − $187,500.)*

**g. Financial statement placement (no-intent path, Year 1)**  
- **Net income:** Loss on Impairment **$12,000** (credit-loss component, limited by FV shortfall).  
- **OCI / AOCI:** remaining unrealized **noncredit** loss **$3,000** (via residual FVA).  
- **Balance sheet:** AFS reported at **fair value $185,000**, presented as amortized cost **$200,000** less ACL **$12,000** less FVA **$3,000** (or equivalent note disclosure). Disclose ACL **rollforward** for AFS debt securities.

**Key insight:** For AFS debt, **always** mark to FV through OCI first; then at period-end, peel the **credit** portion into **Loss on Impairment** and **Allowance for Credit Losses** (capped by the FV shortfall) when there is **no intent to sell**. Noncredit declines stay in OCI. If management **intends to sell**, the **entire** AC − FV gap hits NI and resets cost basis—no residual OCI for that security.

---

### Q2 — CORE number variant — AFS impairment twin (all numbers changed)
**LO:** LO 14-6  
**Concept:** Number-variant twin: initial purchase JE; interest; FV-OCI subsequent measurement schedule; period-end AFS impairment adjusting JE (credit limited by FV shortfall); intent-to-sell contrast; sale cleanup  
**Scenario:**  
**Pinecrest Holdings LLC** (calendar-year) buys **$150,000 par** of **Redwood Utility 5% bonds** on **January 1, Year 1**, at **par**. Interest is paid **annually** each December 31. The bonds are classified as **AFS**. Year-end is December 31.

**December 31, Year 1 data (interest already recorded):**

| Item | Amount |
|---|---:|
| Amortized cost | $150,000 |
| Fair value | $136,000 |
| PV of cash flows expected to be collected | $141,000 |
| Expected credit loss | $9,000 |

Pinecrest records FV-OCI **before** impairment analysis. Pinecrest **does not intend to sell** and is **not more likely than not** required to sell before recovery.

**Alternate (part e):** Same facts except Pinecrest **intends to sell**.

**Year 2 sale (part f):** Under no-intent accounting, on **April 1, Year 2** Pinecrest sells the bonds for **$138,200** cash. Pre-sale ACL and FVA equal December 31 Year 1 balances (FV still $136,000 until sale).

**Required:**  
a. January 1 Year 1 purchase JE.  
b. December 31 Year 1 interest JE.  
c. Subsequent measurement schedule + FV-OCI adjusting JE.  
d. No-intent impairment amount in NI + period-end impairment adjusting JE + net carrying amount.  
e. Intent-to-sell impairment amount, JE, and new cost basis.  
f. April 1 Year 2 disposal JE (no-intent path).  
g. Amount of Year 1 unrealized loss remaining in AOCI after the no-intent impairment entry.

**Answer key:**  

**a. January 1, Year 1 — purchase**

| Account | Debit | Credit |
|---|---:|---:|
| Investment in AFS Securities—Redwood Bonds | 150,000 | |
| Cash | | 150,000 |

**Check:** Dr = Cr = 150,000. **Balanced.**

**b. December 31, Year 1 — interest**

Interest = \(150{,}000 \times 0.05 = \$7{,}500\)

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 7,500 | |
| Interest Revenue | | 7,500 |

**Check:** Dr = Cr = 7,500. **Balanced.**

**c. Subsequent measurement + FV-OCI JE**

| Item | Amount |
|---|---:|
| Amortized cost | $150,000 |
| Fair value | $136,000 |
| Total unrealized holding loss | $(14,000)$ |
| Expected credit loss | $9,000 |
| Noncredit residual | $5,000 |

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—OCI | 14,000 | |
| Fair Value Adjustment—AFS | | 14,000 |

**Check:** Dr = Cr = 14,000. **Balanced.**

**d. No-intent period-end impairment**

Credit loss **$9,000** ≤ FV shortfall **$14,000** → impairment in NI = **$9,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 9,000 | |
| Fair Value Adjustment—AFS | 9,000 | |
| Allowance for Credit Losses—AFS | | 9,000 |
| Unrealized Gain or Loss—OCI | | 9,000 |

**Check:** Dr 18,000 = Cr 18,000. **Balanced.**

Net carrying amount = \(150{,}000 - 9{,}000\ \text{ACL} - 5{,}000\ \text{FVA} = \$136{,}000\) (= FV).

**e. Intent-to-sell path**

Impairment in NI = full shortfall **$14,000**. New cost basis = **$136,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 14,000 | |
| Investment in AFS Securities—Redwood Bonds | | 14,000 |
| Fair Value Adjustment—AFS | 14,000 | |
| Unrealized Gain or Loss—OCI | | 14,000 |

**Check:** Dr 28,000 = Cr 28,000. **Balanced.**

**f. April 1, Year 2 disposal (no-intent balances)**

Net amortized cost = \(150{,}000 - 9{,}000 = 141{,}000\)  
Realized loss = \(141{,}000 - 138{,}200 = \$2{,}800\)  
Clear residual FVA $5,000 and related OCI.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 138,200 | |
| Allowance for Credit Losses—AFS | 9,000 | |
| Fair Value Adjustment—AFS | 5,000 | |
| Loss on Sale of Investment | 2,800 | |
| Investment in AFS Securities—Redwood Bonds | | 150,000 |
| Unrealized Gain or Loss—OCI | | 5,000 |

**Check:** Dr \(138{,}200 + 9{,}000 + 5{,}000 + 2{,}800 = 155{,}000\); Cr \(150{,}000 + 5{,}000 = 155{,}000\). **Balanced.**

**g. AOCI after no-intent impairment**  
Remaining noncredit unrealized loss in AOCI = **$5,000**.

**Key insight:** Changing every dollar amount does not change the decision tree: **cap the credit loss at the FV shortfall**, reclassify that amount from OCI into NI with ACL, and leave any noncredit gap in AOCI—until disposal clears the residual FVA.

---

### Q3 — CORE alternate angle — Three-scenario AFS impairment measurement, HTM CECL contrast, equity-method OTTI, presentation
**LO:** LO 14-6  
**Concept:** Classification of impairment measurement across AFS scenarios (including zero impairment when FV > AC); period-end adjusting JEs; HTM CECL allowance; equity-method permanent write-down; presentation/disclosure  
**Scenario:**  
**Lakeshore Analytics Inc.** holds several investments at December 31, Year 3. For each AFS scenario below, management **does not intend to sell** and it is **not more likely than not** that sale will be required before recovery. FV-OCI has already been recorded for any AFS positions.

**AFS bond — three separate scenarios (same security design, different year-end FVs):**

| | Scenario A | Scenario B | Scenario C |
|---|---:|---:|---:|
| Fair value | $95,000 | $78,000 | $72,000 |
| Amortized cost | 85,000 | 85,000 | 85,000 |
| Expected credit loss* | 10,000 | 10,000 | 10,000 |

\*Amortized cost − PV of expected collections = $10,000 in all three scenarios.

**HTM bond (separate holding):** Amortized cost **$60,000**. Using the CECL model, PV of amounts expected to be collected = **$52,000**. No fair-value adjustment is recorded for HTM.

**Equity-method investment (separate holding):** Carrying amount **$40,000**; fair value **$33,000**. Management concludes the decline is **other-than-temporary** (investee lost a major customer and cannot sustain earnings that justify the carrying amount).

**Required:**  
a. For **each AFS scenario (A, B, C)**, determine the impairment loss to recognize in **net income** and record the year-end **impairment adjusting JE** (or state none).  
b. Record the **HTM CECL period-end impairment JE**.  
c. Record the **equity-method OTTI JE**. State whether subsequent recovery may reverse the write-down under the textbook model.  
d. **Presentation:** For Scenario C after the impairment entry, show how the AFS investment is measured on the balance sheet (amortized cost, ACL, FVA, net) and identify which amounts affected **net income** vs **OCI** for the period’s fair-value decline.  
e. **Disclosure:** List two note disclosures specifically associated with AFS and HTM credit losses under LO 14-6.

**Answer key:**  

**a. AFS three-scenario measurement and JEs**

**Scenario A** — FV $95,000 > AC $85,000 → **not impaired**.  
Impairment loss in NI = **$0**. **No impairment entry.**  
(FV-OCI would already show an unrealized **gain** of $10,000; no credit-loss analysis.)

**Scenario B** — FV shortfall = \(85{,}000 - 78{,}000 = \$7{,}000\).  
Expected credit loss $10,000, but ACL/impairment **limited** to FV shortfall → NI impairment = **$7,000**.  
(Noncredit residual = $0; entire shortfall treated as credit for measurement because of the cap.)

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 7,000 | |
| Fair Value Adjustment—AFS | 7,000 | |
| Allowance for Credit Losses—AFS | | 7,000 |
| Unrealized Gain or Loss—OCI | | 7,000 |

**Check:** Dr 14,000 = Cr 14,000. **Balanced.**  
Net carrying = \(85{,}000 - 7{,}000\ \text{ACL} - 0\ \text{FVA} = \$78{,}000\).

**Scenario C** — FV shortfall = \(85{,}000 - 72{,}000 = \$13{,}000\).  
Credit loss recognized = min(\(10{,}000\), \(13{,}000\)) = **$10,000**.  
Noncredit residual in OCI = \(13{,}000 - 10{,}000 = \$3{,}000\).

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 10,000 | |
| Fair Value Adjustment—AFS | 10,000 | |
| Allowance for Credit Losses—AFS | | 10,000 |
| Unrealized Gain or Loss—OCI | | 10,000 |

**Check:** Dr 20,000 = Cr 20,000. **Balanced.**  
Pre-impairment FVA credit was $13,000; after debiting FVA $10,000, **FVA credit remaining $3,000**.  
Net carrying = \(85{,}000 - 10{,}000 - 3{,}000 = \$72{,}000\) (= FV).

**b. HTM CECL impairment**

Impairment = \(60{,}000 - 52{,}000 = \$8{,}000\).

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 8,000 | |
| Allowance for Credit Losses—HTM | | 8,000 |
| *CECL lifetime expected credit loss on HTM debt* | | |

**Check:** Dr 8,000 = Cr 8,000. **Balanced.**  
(No FVA or OCI for plain HTM amortized-cost accounting.)

**c. Equity-method OTTI**

Impairment = \(40{,}000 - 33{,}000 = \$7{,}000\).

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 7,000 | |
| Investment in Equity-Method Investee | | 7,000 |
| *Other-than-temporary decline; reduce carrying amount* | | |

**Check:** Dr 7,000 = Cr 7,000. **Balanced.**  
**Subsequent recovery:** Losses on impairment of equity-method investments are **not reversed** in future periods under the textbook model (new carrying amount is the basis going forward).

**d. Scenario C presentation after impairment**

| Balance sheet components | Amount |
|---|---:|
| Investment in AFS (amortized cost) | $85,000 |
| Less: Allowance for Credit Losses | (10,000) |
| Less: Fair Value Adjustment—AFS (noncredit) | (3,000) |
| **Carrying amount (= fair value)** | **$72,000** |

| Earnings vs OCI for the $13,000 total decline | Amount | Where reported |
|---|---:|---|
| Credit-loss component | $10,000 | **Net income** (Loss on Impairment) |
| Noncredit component | $3,000 | **OCI / AOCI** (residual unrealized loss) |

**e. Disclosures (LO 14-6)**  
1. **AFS:** prepare a **rollforward of the allowance for credit losses** on AFS debt securities.  
2. **HTM:** disclose information about **changes in factors** that influenced management’s estimate of expected credit losses (including reasons for those changes).  
(Also common: amortized cost vs fair value, contractual maturities, credit quality indicators—broader Ch. 14 investment disclosures.)

**Key insight:** AFS impairment is **not** “all of AC − FV to NI.” Scenario A shows **no impairment when FV ≥ AC**. Scenarios B and C show the **credit loss is always capped by the FV shortfall**. HTM uses a pure **CECL allowance** with no OCI; equity method writes the **investment account** itself for OTTI with **no later reverse**.

---

### Q4 — MC — Classification of AFS impairment amount in net income
**LO:** LO 14-6  
**Concept:** Classification/measurement — correct AFS impairment loss in NI when no intent to sell (credit loss limited by FV shortfall)  
**Question:**  
On December 31, **Summit Ridge Advisors** holds an AFS debt security with amortized cost **$110,000**, fair value **$98,000**, and expected credit loss (AC − PV of expected collections) **$15,000**. Summit does **not** intend to sell and it is not more likely than not that sale will be required before recovery. FV-OCI for the full unrealized loss has already been recorded. What amount of **impairment loss** should Summit recognize in **net income**?

- A) $0  
- B) $12,000  
- C) $15,000  
- D) $110,000  

**Answer:** **B.** FV shortfall = \(110{,}000 - 98{,}000 = \$12{,}000\). Expected credit loss is $15,000, but the allowance/impairment recognized in NI is **limited to the amount that fair value is less than amortized cost**, so NI impairment = **$12,000**. The remaining noncredit portion of any pre-impairment OCI relates only to the $12,000 total decline (all of which is treated as credit under the cap); there is no additional $3,000 noncredit residual beyond the FV shortfall.  
*(If the expected credit loss had been only $8,000, NI impairment would be $8,000 with $4,000 noncredit remaining in OCI.)*

---

### Q5 — MC — Intent to sell vs no intent: where the loss is recorded
**LO:** LO 14-6  
**Concept:** Classification — intent-to-sell AFS write-down hits full AC−FV in net income and resets cost basis  
**Question:**  
Same security as Q4 (**AC $110,000**, **FV $98,000**, expected credit loss **$15,000**), except now Summit **intends to sell** the AFS debt security. Which statement is correct?

- A) Impairment in NI is $15,000; new cost basis is $95,000.  
- B) Impairment in NI is $12,000; residual $3,000 stays in AOCI.  
- C) Impairment in NI is $12,000; fair value $98,000 becomes the new amortized cost basis; related OCI/FVA for the security is eliminated.  
- D) No impairment is recognized because AFS is already at fair value through OCI.  

**Answer:** **C.** When the entity **intends to sell** (or more likely than not will be required to sell before recovery), the **entire** difference between amortized cost and fair value (**$12,000**) is recognized in **net income**, the investment is written down so **FV becomes the new cost basis ($98,000)**, and the previously recorded OCI/FVA for that unrealized loss is reversed. Expected credit loss of $15,000 is **not** used as a separate larger charge once intent-to-sell drives a full write-down to FV.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on each entry)
- [x] Math recomputed (credit loss caps, FV shortfalls, disposal clearings)
- [x] Core demo path from Demo 14-6 / Review 14-6 (AFS primary; HTM & equity-method contrast in Q3) — not sidebar-only
- [x] **LO:** and **Concept:** on every item
- [x] MC ≤ 2 (Q4, Q5 classification/measurement only)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule, period_end_adjusting_JE (emphasis), disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
- [x] Original companies and numbers (not textbook Bold/Rush/Demo 14-6 figures)
