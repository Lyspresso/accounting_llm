# Agent 7 — CORE DEMO — LO 14-6

**Chapter:** 14  
**LO title:** Accounting for Impairment Loss on AFS Investments  
**Critical gap LO:** yes

## Concept list for this pack
- AFS debt security impairment model (ASC 326-30): impaired when fair value < amortized cost, assessed individually each period
- Intent-to-sell (or more-likely-than-not required-to-sell) path: full write-down of amortized cost to fair value through net income
- No-intent-to-sell path: credit-loss portion of the unrealized loss through net income via Allowance for Credit Losses, limited to the fair-value shortfall; noncredit portion remains in OCI
- Sequence: record FV-OCI fair-value adjustment first, then reclassify credit (or full) impairment from OCI into net income
- Balance-sheet presentation: Allowance for Credit Losses contra to AFS amortized cost; FVA remains for residual noncredit FV-OCI
- Subsequent measurement / allowance rollforward and disposal after impairment
- Number-variant twin of the three-scenario core demo

---

### Q1 — CORE — Three-scenario AFS impairment measurement and initial recognition JEs
**LO:** LO 14-6  
**Concept:** AFS impairment loss measurement (credit vs noncredit; limited by FV shortfall) and initial recognition JE  
**Scenario:**  
Northridge Holdings holds a single AFS debt security (Mesa Industrial 6% bonds). Northridge does **not** intend to sell the bonds and does **not** believe it is more likely than not that it will be required to sell before recovery of any unrealized loss. At December 31, Year 1, Northridge has **already** adjusted the AFS investment to fair value through FV-OCI (LO 14-3). Consider three mutually exclusive year-end fact patterns for the same amortized-cost basis:

|  | Scenario A | Scenario B | Scenario C |
|--|------------|------------|------------|
| Fair value, Dec 31 | $85,000 | $72,000 | $65,000 |
| Amortized cost, Dec 31 | 80,000 | 80,000 | 80,000 |
| Expected loss due to credit factors* | 12,000 | 12,000 | 12,000 |

\*Excess of amortized cost over the present value of cash flows expected to be collected as of December 31.

Assume that immediately before the impairment analysis, the only FV-OCI balances related to this security are those needed to restate amortized cost to the scenario’s fair value (FVA—AFS and Unrealized Gain or Loss—OCI already recorded).

**Required:**  
a. For each scenario, compute the **impairment loss to recognize in net income** for Year 1. Show the fair-value shortfall, the credit-loss amount, and the limit applied.  
b. For each scenario, record the **December 31 impairment journal entry** (if any). Use the textbook’s paired reclassification of the corresponding OCI loss.  
c. For Scenario C only, after the impairment entry, compute the **carrying amount** of the investment on the balance sheet (amortized cost, allowance, FVA, net) and identify which portion of the total unrealized decline remains in AOCI (noncredit).

**Answer key:**  

**a. Measurement of impairment loss (no-intent-to-sell model)**  
General rule:  
- If FV ≥ amortized cost → **no impairment**.  
- If FV < amortized cost → impaired; credit loss recognized in NI = **min**(expected credit loss, amortized cost − FV). Noncredit remainder (if any) stays in OCI.

| Scenario | FV shortfall (AC − FV) | Expected credit loss | Impairment loss in NI | Reasoning |
|----------|------------------------|----------------------|-----------------------|-----------|
| A | $80,000 − $85,000 = **$(5,000)** (FV > AC) | $12,000 | **$0** | Not impaired; FV exceeds amortized cost |
| B | $80,000 − $72,000 = **$8,000** | $12,000 | **$8,000** | Credit loss capped at FV shortfall: min(12,000, 8,000) = 8,000 |
| C | $80,000 − $65,000 = **$15,000** | $12,000 | **$12,000** | Credit loss fully within FV shortfall: min(12,000, 15,000) = 12,000; noncredit $3,000 stays in OCI |

**b. Year-end impairment entries**

**Scenario A — no entry**  
No impairment (FV > AC). The existing FV-OCI unrealized gain of $5,000 remains in OCI; no Loss on Impairment and no Allowance for Credit Losses.

**Scenario B — December 31, Year 1**  
```
Dr  Loss on Impairment ..............................  8,000
Dr  Fair Value Adjustment—AFS .......................  8,000
    Cr  Allowance for Credit Losses—AFS .....................  8,000
    Cr  Unrealized Gain or Loss—OCI .........................  8,000
```  
(Dr = $16,000; Cr = $16,000 — balances.)  
Effect: credit-loss portion moves from OCI into net income; Allowance reduces net carrying amount; FVA debit reverses the corresponding OCI loss previously recorded for that $8,000.

**Scenario C — December 31, Year 1**  
```
Dr  Loss on Impairment .............................. 12,000
Dr  Fair Value Adjustment—AFS ....................... 12,000
    Cr  Allowance for Credit Losses—AFS .................... 12,000
    Cr  Unrealized Gain or Loss—OCI ........................ 12,000
```  
(Dr = $24,000; Cr = $24,000 — balances.)

**c. Scenario C balance-sheet carrying amount after impairment**

| Component | Amount |
|-----------|--------|
| Amortized cost (Investment in AFS) | $80,000 |
| Less: Allowance for Credit Losses | (12,000) |
| Amortized cost net of allowance | 68,000 |
| Less: remaining FVA credit for noncredit FV decline* | (3,000) |
| **Carrying amount at fair value** | **$65,000** |

\*Before impairment, FVA credit (and OCI unrealized loss) for the full $15,000 FV shortfall was already on the books. The impairment entry debits FVA $12,000 (and credits OCI $12,000), leaving a **$3,000** FVA credit / OCI unrealized loss for the **noncredit** portion.  
Net income absorbed $12,000; AOCI still holds $(3,000) noncredit unrealized loss.

**Key insight:** For AFS with no intent (or requirement) to sell, impairment through net income is only the **credit** portion of the decline, and it cannot exceed the **fair-value shortfall**. Any excess decline is noncredit and remains in OCI under FV-OCI.

---

### Q2 — CORE number variant
**LO:** LO 14-6  
**Concept:** AFS impairment loss measurement and initial recognition JE (number-variant twin)  
**Scenario:**  
Cedarline Mutual holds an AFS debt security (Prairie Telecom 5.5% notes). Cedarline does **not** intend to sell and does **not** believe sale will be required before recovery. Fair-value adjustments through FV-OCI have already been recorded. Three separate year-end scenarios:

|  | Scenario 1 | Scenario 2 | Scenario 3 |
|--|------------|------------|------------|
| Fair value, Dec 31 | $240,000 | $195,000 | $178,000 |
| Amortized cost, Dec 31 | 220,000 | 220,000 | 220,000 |
| Expected loss due to credit factors | 35,000 | 35,000 | 35,000 |

**Required:**  
a. Compute the Year 1 impairment loss in **net income** under each scenario.  
b. Record the impairment JE (if any) under each scenario.  
c. For Scenario 3, state the noncredit unrealized loss remaining in OCI after the impairment entry.

**Answer key:**  

**a.**

| Scenario | FV shortfall | Credit loss | NI impairment | Notes |
|----------|--------------|-------------|---------------|-------|
| 1 | $220,000 − $240,000 = **$(20,000)** | $35,000 | **$0** | FV > AC → no impairment |
| 2 | $220,000 − $195,000 = **$25,000** | $35,000 | **$25,000** | min(35,000, 25,000) = 25,000 |
| 3 | $220,000 − $178,000 = **$42,000** | $35,000 | **$35,000** | min(35,000, 42,000) = 35,000 |

**b. Journal entries**

**Scenario 1:** No impairment entry.

**Scenario 2 — December 31**  
```
Dr  Loss on Impairment ............................. 25,000
Dr  Fair Value Adjustment—AFS ...................... 25,000
    Cr  Allowance for Credit Losses—AFS .................... 25,000
    Cr  Unrealized Gain or Loss—OCI ........................ 25,000
```  
(Dr = $50,000; Cr = $50,000 — balances.)

**Scenario 3 — December 31**  
```
Dr  Loss on Impairment ............................. 35,000
Dr  Fair Value Adjustment—AFS ...................... 35,000
    Cr  Allowance for Credit Losses—AFS .................... 35,000
    Cr  Unrealized Gain or Loss—OCI ........................ 35,000
```  
(Dr = $70,000; Cr = $70,000 — balances.)

**c. Scenario 3 noncredit portion remaining in OCI**  
FV shortfall $42,000 − credit impairment $35,000 = **$7,000** unrealized noncredit loss remains in AOCI (supported by remaining FVA credit of $7,000).

**Key insight:** Changing only the numbers does not change the decision tree: first test FV vs AC; if impaired and no intent to sell, NI loss = min(credit loss, FV shortfall).

---

### Q3 — CORE alternate angle — Intent-to-sell write-down, subsequent period, and disposal
**LO:** LO 14-6  
**Concept:** Intent-to-sell AFS impairment (full write-down to FV), subsequent measurement / disposal after impairment  
**Scenario:**  
On January 1, Year 1, Summit Ridge Advisors purchased at par $100,000 face of Oakmont Energy 4% bonds (AFS classification). Interest is paid annually each December 31. Amortized cost remains $100,000 throughout Year 1 (purchased at par; no amortization).  

**Year 1 sequence (period-end):**  
1. Fair value of the Oakmont bonds on December 31, Year 1 is $88,000.  
2. Summit Ridge **has decided to sell** the bonds in early Year 2 (intent to sell before recovery).  
3. Present value of cash flows expected to be collected is $91,000 (so “credit loss” would have been $9,000 under the no-intent model — **not** used for measurement when intent to sell exists).  
4. Summit Ridge records the FV-OCI fair-value adjustment **first**, then the impairment analysis.

**Year 2:**  
On February 10, Year 2, Summit Ridge sells the entire position for cash proceeds of $89,500. Immediately before sale, carrying amounts (after Year 1 impairment) are: Investment in AFS $88,000 (new cost basis after write-down); no remaining Allowance; no remaining FVA related to this security (write-down went directly against the investment and the OCI loss was eliminated).

**Required:**  
a. Record the **December 31, Year 1 FV-OCI adjusting entry** (before impairment).  
b. Determine the **impairment loss in net income** under the **intent-to-sell** path and record the impairment JE.  
c. Briefly contrast what the NI impairment would have been if Summit Ridge did **not** intend to sell (using the credit-loss data given).  
d. Record the **February 10, Year 2 sale** JE and the realized gain or loss.  
e. **Classification / presentation:** Identify where the Year 1 impairment loss is reported and state one required AFS credit-loss disclosure when an allowance model is used (no-intent path).

**Answer key:**  

**a. December 31, Year 1 — adjust AFS to fair value (FV-OCI)**  
Unrealized holding loss = $100,000 − $88,000 = $12,000.  
```
Dr  Unrealized Gain or Loss—OCI .................... 12,000
    Cr  Fair Value Adjustment—AFS .......................... 12,000
```  
(Dr = $12,000; Cr = $12,000 — balances.)

**b. Intent-to-sell impairment**  
Because Summit Ridge intends to sell before recovery, the **entire** difference between amortized cost and fair value is recognized in **net income**, and fair value becomes the **new amortized cost basis**. Any allowance would be written off; amortized cost is written down to FV with incremental impairment in earnings. Corresponding OCI is eliminated.  
Impairment loss in NI = $100,000 − $88,000 = **$12,000**.

```
Dr  Loss on Impairment ............................. 12,000
Dr  Fair Value Adjustment—AFS ...................... 12,000
    Cr  Investment in AFS—Oakmont Bonds .................... 12,000
    Cr  Unrealized Gain or Loss—OCI ........................ 12,000
```  
(Dr = $24,000; Cr = $24,000 — balances.)  

After this entry:  
- Investment in AFS (new cost basis) = $88,000  
- FVA = $0  
- OCI unrealized loss related to this security = $0  
- Allowance for Credit Losses = $0 (not used; full write-down against investment)

**c. Contrast — no-intent-to-sell counterfactual**  
If Summit Ridge did **not** intend to sell: NI impairment = min(credit loss $9,000, FV shortfall $12,000) = **$9,000** through Allowance for Credit Losses; noncredit $3,000 would remain in OCI. Intent to sell accelerates the full $12,000 into NI and resets cost basis to FV.

**d. February 10, Year 2 — disposal**  
Cash $89,500 − new cost basis $88,000 = **realized gain $1,500**.  
```
Dr  Cash ........................................... 89,500
    Cr  Investment in AFS—Oakmont Bonds .................... 88,000
    Cr  Gain on Sale of Investment .........................  1,500
```  
(Dr = $89,500; Cr = $89,500 — balances.)

**e. Classification / presentation / disclosure**  
- Year 1 **Loss on Impairment $12,000** is reported in **net income** (earnings), not in OCI.  
- After write-down, the AFS asset is carried at the new cost basis of $88,000 until sale or further period-end measurement.  
- When the **allowance** model applies (no-intent path for AFS), notes must include a **rollforward of the allowance for credit losses** on AFS debt securities. (HTM uses CECL allowance disclosures about changes in estimate factors.)

**Key insight:** Intent (or more-likely-than-not required sale) collapses the AFS model to a full earnings write-down to fair value and a new cost basis; subsequent sale gain/loss is measured from that new basis, not original amortized cost.

---

### Q4 — MC (classification / measurement choice)
**LO:** LO 14-6  
**Concept:** Classify which AFS impairment path and amount hits net income  
**Question:**  
At December 31, Larkspur Corp. holds one AFS debt security with amortized cost $50,000 and fair value $44,000. Expected credit loss (AC minus PV of expected collections) is $9,000. Larkspur does **not** intend to sell and sale is **not** more likely than not required before recovery. FV-OCI adjustments are already recorded. What amount of **impairment loss** should Larkspur recognize in **net income**?

- A) $0, because AFS unrealized losses always stay in OCI until sale  
- B) $6,000 (fair-value shortfall only; credit loss is ignored under AFS)  
- C) $6,000, limited credit loss: min($9,000 credit loss, $6,000 FV shortfall)  
- D) $9,000, the full expected credit loss regardless of fair value  

**Answer:** C.  
AFS is impaired when FV < AC. With no intent to sell, the credit-loss allowance is recognized in NI but **limited** by the amount FV is less than AC: min(9,000, 50,000 − 44,000) = min(9,000, 6,000) = **$6,000**. The remaining $3,000 of “credit loss” above the market decline is not recognized (allowance cannot push carrying amount below fair value under ASC 326-30). Choice A is wrong (credit impairments go through NI). Choice B misstates the theory (credit analysis is required). Choice D ignores the fair-value limit.

---

### Q5 — CORE — Period-end sequence: FV-OCI then credit impairment (allowance path) with schedule
**LO:** LO 14-6  
**Concept:** Period-end adjusting JE sequence and subsequent measurement schedule (allowance rollforward)  
**Scenario:**  
Brightvale Insurance holds AFS municipal bonds with amortized cost $150,000 on December 31, Year 1. Fair value is $138,000. Brightvale does **not** intend to sell and is not more likely than not required to sell. PV of expected collections is $141,000 (expected credit loss = $150,000 − $141,000 = $9,000). No prior allowance exists. No prior FVA balance exists before the Year 1 closing process.

**Year 2 subsequent measurement:**  
On December 31, Year 2, amortized cost is still $150,000 (for simplicity). Fair value is $140,000. PV of expected collections is $143,000 (expected credit loss = $7,000). Brightvale still has no intent / required sale. Update the allowance and FVA as needed (credit losses can reverse but not below zero).

**Required:**  
a. Record Year 1 period-end entries: (1) FV-OCI fair-value adjustment, then (2) impairment (allowance) entry.  
b. Prepare a brief **allowance rollforward** schedule for Years 1–2 and the Year 2 adjusting entries for allowance and residual noncredit FVA.  
c. Show net carrying amount at December 31, Year 2.

**Answer key:**  

**a. Year 1 period-end**

(1) FV-OCI adjustment — full unrealized loss $12,000 ($150,000 − $138,000):  
```
Dr  Unrealized Gain or Loss—OCI .................... 12,000
    Cr  Fair Value Adjustment—AFS .......................... 12,000
```  
(Dr = Cr = $12,000.)

(2) Credit impairment — min(credit loss $9,000, FV shortfall $12,000) = **$9,000**:  
```
Dr  Loss on Impairment ..............................  9,000
Dr  Fair Value Adjustment—AFS .......................  9,000
    Cr  Allowance for Credit Losses—AFS .....................  9,000
    Cr  Unrealized Gain or Loss—OCI .........................  9,000
```  
(Dr = Cr = $18,000.)  

After Year 1: Allowance $9,000; remaining FVA credit $3,000 (noncredit); net assets = 150,000 − 9,000 − 3,000 = **$138,000** (= FV).

**b. Subsequent measurement schedule / Year 2**

**Allowance for Credit Losses — rollforward**

| Description | Amount |
|-------------|--------|
| Beginning allowance, Jan 1, Y2 | $9,000 |
| Credit loss (recovery) in NI for Y2* | (2,000) |
| **Ending allowance, Dec 31, Y2** | **$7,000** |

\*New required allowance = min(expected credit loss $7,000, FV shortfall $10,000) = $7,000. Decrease of $2,000 is a favorable change recognized in NI (allowance must not reverse past zero / create a debit balance).

Year 2 — reduce allowance:  
```
Dr  Allowance for Credit Losses—AFS .................  2,000
    Cr  Loss on Impairment (recovery) ......................  2,000
```  
(Dr = Cr = $2,000.)

**FVA residual (noncredit) analysis at Dec 31, Y2**  
Target net carrying amount = FV $140,000.  
Amortized cost net of allowance = 150,000 − 7,000 = 143,000.  
Required remaining FVA **credit** for noncredit = 143,000 − 140,000 = **$3,000**.  
Existing FVA credit after Year 1 = $3,000 → **no FVA change** needed in Year 2 for this security (noncredit gap still $3,000).

If the company re-runs the full FV-OCI “to fair value” mechanics portfolio-wide, the noncredit OCI / FVA for this bond remains $3,000; the Year 2 market improvement of $2,000 relative to Year 1 FV was absorbed by the $2,000 allowance recovery (both increase net assets toward / to the new FV).

**c. December 31, Year 2 carrying amount**

| Component | Amount |
|-----------|--------|
| Investment in AFS (amortized cost) | $150,000 |
| Less: Allowance for Credit Losses | (7,000) |
| Less: FVA—AFS (noncredit) | (3,000) |
| **Net carrying amount (= fair value)** | **$140,000** |

**Key insight:** After initial credit impairment, subsequent favorable or unfavorable changes in expected credit losses adjust the allowance through NI (not below zero). Net assets continue to equal fair value when FVA captures any remaining noncredit gap.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on all entries)
- [x] Math recomputed (min credit/FV-shortfall logic checked for all scenarios)
- [x] Core demo not sidebar-only (Demo 14-6 / Review 14-6 AFS path)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (one MC classification item)
- [x] Angles covered: initial_recognition_JE (Q1/Q2), subsequent_measurement_schedule (Q5), period_end_adjusting_JE (Q3/Q5), disposal_maturity_or_settlement_JE (Q3), classification_presentation_or_disclosure (Q3e/Q4), number_variant_twin (Q2)
