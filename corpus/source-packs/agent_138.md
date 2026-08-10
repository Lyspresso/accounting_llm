# Agent 138 — CORE DEMO — LO 14-6

**Chapter:** 14  
**LO title:** Accounting for Impairment Loss on AFS Investments  
**Critical gap LO:** yes

## Concept list for this pack
- **AFS impairment trigger (ASC 326-30):** impaired when fair value < amortized cost, assessed at the individual security level each reporting period
- **Initial recognition JE:** purchase AFS debt at par; record cash interest in net income
- **Period-end sequence:** record full FV-OCI fair-value adjustment first, then reclassify the credit-loss portion into net income (textbook Demo 14-6 sequence)
- **No-intent-to-sell path:** NI impairment = min(expected credit loss, FV shortfall) via **Allowance for Credit Losses**; noncredit remainder stays in OCI (supported by residual FVA)
- **Intent-to-sell (or more-likely-than-not required-to-sell) path:** write amortized cost down to fair value through NI; FV becomes new cost basis; eliminate related FVA/OCI
- **Subsequent measurement schedule (emphasis):** multi-period allowance rollforward; favorable recoveries through NI (allowance never below zero); residual noncredit FVA updated so net carrying amount equals fair value
- **Disposal / settlement JE:** sale after impairment—gain or loss measured from post-impairment carrying amounts
- **Classification / presentation / disclosure:** Loss on Impairment in net income; allowance rollforward disclosure for AFS credit losses; contrast with HTM CECL and equity-method OTT impairment
- **Number-variant twin:** same multi-period decision tree with all amounts changed

---

### Q1 — CORE — Purchase, multi-period subsequent measurement schedule, allowance rollforward, residual FVA
**LO:** LO 14-6  
**Concept:** Initial recognition of AFS debt; period-end FV-OCI then credit impairment; multi-year subsequent measurement schedule (allowance rollforward and residual noncredit FVA)  
**Scenario:**  
**Vellum Partners Inc.** is a calendar-year investor. On **January 1, Year 1**, Vellum purchases at **par** **$250,000** face of **Cascade Rail 6% senior notes**, classified as **available-for-sale (AFS)**. Cash interest is paid annually each **December 31**. Because the bonds were purchased at par, amortized cost remains **$250,000** throughout (no premium/discount amortization).

Vellum does **not** intend to sell the notes and does **not** believe it is more likely than not that sale will be required before recovery of any unrealized loss in any year below. No prior allowance or FVA exists before Year 1 period-end processing.

**Period-end measurement data (each December 31):**

| Date | Fair value | PV of cash flows expected to be collected | Expected credit loss (AC − PV) |
|---|---:|---:|---:|
| Dec 31, Year 1 | $228,000 | $235,000 | $15,000 |
| Dec 31, Year 2 | 232,000 | 240,000 | 10,000 |
| Dec 31, Year 3 | 220,000 | 225,000 | 25,000 |

**Required:**  
a. Prepare the **January 1, Year 1 initial recognition JE** and the **December 31, Year 1 cash interest JE**.  
b. Prepare **December 31, Year 1 period-end adjusting entries** in textbook order: (1) full FV-OCI fair-value adjustment, then (2) credit-impairment entry (paired reclassification of the corresponding OCI loss). Compute NI impairment, noncredit residual, and net carrying amount.  
c. Prepare a **subsequent measurement schedule** for Years 1–3 with columns: FV shortfall, expected credit loss, required allowance (min), allowance beginning, provision/(recovery) through NI, allowance ending, residual noncredit FVA credit, net carrying amount.  
d. Prepare the **Year 2** and **Year 3** adjusting entries for the **allowance** and for any **change in residual noncredit FVA / OCI**.  
e. **Presentation:** State where Year 1–3 impairment (and recoveries) appear, and name one required **disclosure** when the AFS allowance model is used.

**Answer key:**  

**a. Initial recognition and interest**

*January 1, Year 1 — purchase AFS at par*

| Account | Debit | Credit |
|---|---:|---:|
| Investment in AFS—Cascade Rail Notes | 250,000 | |
| Cash | | 250,000 |
| *Purchase $250,000 face 6% notes at par; classify AFS* | | |

**Check:** Dr 250,000 = Cr 250,000. **Balanced.**

*December 31, Year 1 — cash interest*  
Cash interest = $250,000 × 6% = **$15,000**

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 15,000 | |
| Interest Revenue | | 15,000 |

**Check:** Dr = Cr = 15,000. **Balanced.**  
(Same interest JE pattern applies Years 2 and 3; omitted for brevity.)

**b. December 31, Year 1 — FV-OCI then credit impairment**

FV shortfall = $250,000 − $228,000 = **$22,000**  
Expected credit loss = **$15,000**  
NI impairment = min($15,000, $22,000) = **$15,000**  
Noncredit residual in OCI = $22,000 − $15,000 = **$7,000**

*(1) Full unrealized loss through FV-OCI*

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—OCI | 22,000 | |
| Fair Value Adjustment—AFS | | 22,000 |
| *Adjust AFS to FV before impairment analysis* | | |

**Check:** Dr = Cr = 22,000. **Balanced.**

*(2) Reclassify credit portion into NI via allowance (Demo 14-6 style)*

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 15,000 | |
| Fair Value Adjustment—AFS | 15,000 | |
| Allowance for Credit Losses—AFS | | 15,000 |
| Unrealized Gain or Loss—OCI | | 15,000 |
| *Credit impairment limited by FV shortfall; reverse related OCI* | | |

**Check:** Dr 15,000 + 15,000 = Cr 15,000 + 15,000. **Balanced.**

**After Year 1:**

| Component | Amount |
|---|---:|
| Investment in AFS (amortized cost) | $250,000 |
| Less: Allowance for Credit Losses | (15,000) |
| Less: residual FVA credit (noncredit) | (7,000) |
| **Net carrying amount (= FV)** | **$228,000** |

**c. Subsequent measurement schedule (emphasis)**

Required allowance each year = **min**(expected credit loss, FV shortfall). Residual noncredit FVA credit = FV shortfall − ending allowance (so AC − allowance − FVA = FV).

| Year | FV | FV shortfall (AC − FV) | Expected credit loss | Required allowance | Beg. allow. | Provision / (recovery) in NI | End. allow. | Residual FVA credit (noncredit) | Net carrying (= FV) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 228,000 | 22,000 | 15,000 | 15,000 | 0 | 15,000 | 15,000 | 7,000 | 228,000 |
| 2 | 232,000 | 18,000 | 10,000 | 10,000 | 15,000 | **(5,000)** | 10,000 | 8,000 | 232,000 |
| 3 | 220,000 | 30,000 | 25,000 | 25,000 | 10,000 | 15,000 | 25,000 | 5,000 | 220,000 |

**Schedule math checks:**  
- Y2: AC − allow − FVA = 250,000 − 10,000 − 8,000 = **232,000** ✓  
- Y3: 250,000 − 25,000 − 5,000 = **220,000** ✓  
- Y2 equity bridge: FV rose $4,000; NI recovery $5,000 + OCI noncredit increase $(1,000) = **+$4,000** ✓  
- Y3 equity bridge: FV fell $12,000; NI provision $15,000 + OCI noncredit decrease favorable $3,000 = **−$12,000** ✓  

**d. Year 2 and Year 3 adjusting entries**

*Year 2 — allowance recovery ($15,000 → $10,000)*

| Account | Debit | Credit |
|---|---:|---:|
| Allowance for Credit Losses—AFS | 5,000 | |
| Loss on Impairment (recovery) | | 5,000 |
| *Favorable change in expected credit loss; allowance not below zero* | | |

**Check:** Dr = Cr = 5,000. **Balanced.**

*Year 2 — residual noncredit FVA ($7,000 → $8,000)*  
After allowance, AC net of allowance = $240,000; FV = $232,000 → need FVA credit **$8,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—OCI | 1,000 | |
| Fair Value Adjustment—AFS | | 1,000 |
| *Increase residual noncredit unrealized loss in OCI* | | |

**Check:** Dr = Cr = 1,000. **Balanced.**

*Year 3 — increase allowance ($10,000 → $25,000)*

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 15,000 | |
| Allowance for Credit Losses—AFS | | 15,000 |
| *Increase credit-loss allowance through NI* | | |

**Check:** Dr = Cr = 15,000. **Balanced.**

*Year 3 — residual noncredit FVA ($8,000 → $5,000)*  
AC net of allowance = $225,000; FV = $220,000 → need FVA credit **$5,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Fair Value Adjustment—AFS | 3,000 | |
| Unrealized Gain or Loss—OCI | | 3,000 |
| *Reduce residual noncredit unrealized loss in OCI* | | |

**Check:** Dr = Cr = 3,000. **Balanced.**

**e. Presentation / disclosure**  
- **Loss on Impairment** (and favorable recoveries that reduce the allowance) are recognized in **net income**, not OCI.  
- Residual **noncredit** fair-value changes remain in **OCI / AOCI**, supported by the Fair Value Adjustment account.  
- For AFS debt securities under the allowance model, notes include a **rollforward of the allowance for credit losses** (and related credit-quality information). HTM uses the CECL lifetime model; equity-method OTT impairments write the investment down directly and are not reversed.

**Key insight:** After the initial FV-OCI → credit reclass sequence, **subsequent measurement** is driven by the **allowance rollforward** (provisions and recoveries through NI, floor at zero) while residual **noncredit FVA** is reset so the net asset always equals **fair value**.

---

### Q2 — CORE number variant
**LO:** LO 14-6  
**Concept:** Number-variant twin — multi-period AFS credit impairment schedule (allowance rollforward and residual FVA)  
**Scenario:**  
**Tidewater Holdings Corp.** purchases at **par** on **January 1, Year 1** **$180,000** face of **Summit Paper 4.5% bonds**, classified **AFS**. Interest is paid annually each December 31. Amortized cost remains **$180,000**. Tidewater has **no intent** (and no more-likely-than-not requirement) to sell before recovery in any year. No beginning allowance or FVA before Year 1 period-end.

| Date | Fair value | PV of expected collections | Expected credit loss |
|---|---:|---:|---:|
| Dec 31, Year 1 | $168,000 | $171,000 | $9,000 |
| Dec 31, Year 2 | 172,000 | 175,000 | 5,000 |
| Dec 31, Year 3 | 160,000 | 164,000 | 16,000 |

**Required:**  
a. Compute Year 1 NI impairment and record the paired FV-OCI then impairment entries (after noting purchase at par for $180,000 cash).  
b. Complete the **Years 1–3 subsequent measurement schedule** (same columns as Q1).  
c. Record Year 2 and Year 3 **allowance** and **residual FVA** adjusting entries.  
d. State ending net carrying amount at December 31, Year 3.

**Answer key:**  

**a. Year 1 measurement and entries**

Purchase (Jan 1, Y1): Dr Investment in AFS 180,000 / Cr Cash 180,000. **Balanced.**

FV shortfall = $180,000 − $168,000 = **$12,000**  
Credit loss = **$9,000**  
NI impairment = min(9,000, 12,000) = **$9,000**  
Noncredit residual = **$3,000**

*(1) FV-OCI*

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—OCI | 12,000 | |
| Fair Value Adjustment—AFS | | 12,000 |

**Check:** Dr = Cr = 12,000. **Balanced.**

*(2) Credit impairment reclass*

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 9,000 | |
| Fair Value Adjustment—AFS | 9,000 | |
| Allowance for Credit Losses—AFS | | 9,000 |
| Unrealized Gain or Loss—OCI | | 9,000 |

**Check:** Dr 18,000 = Cr 18,000. **Balanced.**  
Net carrying after Y1: 180,000 − 9,000 − 3,000 = **$168,000**.

**b. Subsequent measurement schedule**

| Year | FV | Shortfall | Credit loss | Req. allow. | Beg. | Prov. / (rec.) | End. allow. | Resid. FVA | Net (= FV) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 168,000 | 12,000 | 9,000 | 9,000 | 0 | 9,000 | 9,000 | 3,000 | 168,000 |
| 2 | 172,000 | 8,000 | 5,000 | 5,000 | 9,000 | **(4,000)** | 5,000 | 3,000 | 172,000 |
| 3 | 160,000 | 20,000 | 16,000 | 16,000 | 5,000 | 11,000 | 16,000 | 4,000 | 160,000 |

Checks: Y2 net 180 − 5 − 3 = 172; Y3 net 180 − 16 − 4 = 160.  
Y2 equity: FV +4,000 = NI recovery +4,000 + OCI FVA change 0.  
Y3 equity: FV −12,000 = NI provision −11,000 + OCI FVA increase −1,000.

**c. Year 2–3 JEs**

*Year 2 — allowance recovery*

| Account | Debit | Credit |
|---|---:|---:|
| Allowance for Credit Losses—AFS | 4,000 | |
| Loss on Impairment (recovery) | | 4,000 |

**Check:** Dr = Cr = 4,000. **Balanced.**  
Residual FVA already $3,000 and still needed ($175,000 − $172,000) → **no FVA entry** in Year 2.

*Year 3 — increase allowance*

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 11,000 | |
| Allowance for Credit Losses—AFS | | 11,000 |

**Check:** Dr = Cr = 11,000. **Balanced.**

*Year 3 — residual FVA ($3,000 → $4,000)*  
AC net of allowance = $164,000; FV = $160,000 → FVA credit needed **$4,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—OCI | 1,000 | |
| Fair Value Adjustment—AFS | | 1,000 |

**Check:** Dr = Cr = 1,000. **Balanced.**

**d. December 31, Year 3 net carrying amount = $160,000** (= fair value).

**Key insight:** Same decision tree as Q1—only the numbers change. Required allowance is always **min(credit loss, FV shortfall)**; recoveries reverse through NI without creating a debit allowance balance.

---

### Q3 — CORE alternate angle — Intent-to-sell write-down, disposal, classification
**LO:** LO 14-6  
**Concept:** Intent-to-sell AFS impairment (full write-down to FV through NI); period-end adjusting JE; disposal settlement JE; presentation/disclosure  
**Scenario:**  
On **January 1, Year 1**, **Ironwood Asset Management** purchases at **par** **$120,000** face of **Boreal Mining 5% bonds**, classified **AFS**. Interest is paid annually on December 31. Amortized cost remains $120,000 during Year 1.

**December 31, Year 1:**  
- Fair value of the Boreal bonds = **$105,000**.  
- PV of cash flows expected to be collected = **$110,000** (so expected credit loss would be $10,000 under the **no-intent** model).  
- Ironwood **has decided to sell** the bonds early in Year 2 (intent to sell before recovery of amortized cost).  
- Ironwood records the **FV-OCI adjustment first**, then the impairment analysis.

**March 5, Year 2:** Ironwood sells the entire position for cash proceeds of **$106,800**. After the Year 1 intent-to-sell write-down, the investment’s **new cost basis** is $105,000; related FVA and OCI for this security are zero; no allowance remains.

**Required:**  
a. Record the **January 1, Year 1 purchase JE**.  
b. Record the **December 31, Year 1 FV-OCI adjusting entry** (before impairment).  
c. Determine the **impairment loss in net income** under the **intent-to-sell** path and record the impairment JE. State the **new cost basis**.  
d. Contrast the NI impairment that would have been recognized if Ironwood did **not** intend to sell (using the credit-loss data).  
e. Record the **March 5, Year 2 disposal JE** and realized gain or loss.  
f. **Classification / presentation / disclosure:** Where is the Year 1 impairment reported? What disclosure is required when an AFS **allowance** (no-intent path) is used instead?

**Answer key:**  

**a. January 1, Year 1 — purchase**

| Account | Debit | Credit |
|---|---:|---:|
| Investment in AFS—Boreal Mining Bonds | 120,000 | |
| Cash | | 120,000 |

**Check:** Dr = Cr = 120,000. **Balanced.**

**b. December 31, Year 1 — FV-OCI (before impairment)**  
Unrealized holding loss = $120,000 − $105,000 = **$15,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Unrealized Gain or Loss—OCI | 15,000 | |
| Fair Value Adjustment—AFS | | 15,000 |

**Check:** Dr = Cr = 15,000. **Balanced.**

**c. Intent-to-sell impairment**  
Because Ironwood **intends to sell** before recovery, the **entire** difference between amortized cost and fair value is recognized in **net income**, and fair value becomes the **new amortized cost basis**. Any allowance would be written off; the write-down hits the **investment** account (not an allowance). Corresponding OCI/FVA for that loss is eliminated.

Impairment loss in NI = **$15,000**.  
New cost basis = **$105,000**.

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 15,000 | |
| Fair Value Adjustment—AFS | 15,000 | |
| Investment in AFS—Boreal Mining Bonds | | 15,000 |
| Unrealized Gain or Loss—OCI | | 15,000 |
| *Write AC down to FV; eliminate related FVA and OCI* | | |

**Check:** Dr 30,000 = Cr 30,000. **Balanced.**

After this entry: Investment **$105,000**; FVA **$0**; OCI related to this security **$0**; Allowance **$0**.

**d. No-intent counterfactual**  
If Ironwood did **not** intend to sell:  
NI impairment = min(credit loss $10,000, FV shortfall $15,000) = **$10,000** through **Allowance for Credit Losses**; noncredit **$5,000** would remain in OCI. Intent to sell accelerates the full **$15,000** into NI and resets cost basis to FV.

**e. March 5, Year 2 — disposal**  
Cash $106,800 − new cost basis $105,000 = **realized gain $1,800**.

| Account | Debit | Credit |
|---|---:|---:|
| Cash | 106,800 | |
| Investment in AFS—Boreal Mining Bonds | | 105,000 |
| Gain on Sale of Investment | | 1,800 |
| *Sell AFS; gain measured from post-impairment cost basis* | | |

**Check:** Dr 106,800 = Cr 105,000 + 1,800. **Balanced.**

**f. Presentation / disclosure**  
- Year 1 **Loss on Impairment $15,000** is reported in **net income** (earnings), not OCI.  
- After the write-down, the AFS asset is carried at the **new cost basis** of $105,000 until sale or further measurement.  
- When the **no-intent allowance model** applies, notes must include a **rollforward of the allowance for credit losses** on AFS debt securities (and credit-quality / estimate-factor information as applicable).

**Key insight:** Intent (or more-likely-than-not required sale) collapses AFS impairment to a **full earnings write-down to fair value** and a **new cost basis**; subsequent sale gain/loss is measured from that new basis, not original amortized cost.

---

### Q4 — MC (classification / measurement path)
**LO:** LO 14-6  
**Concept:** Classify which AFS impairment path applies and the amount recognized in net income  
**Question:**  
At December 31, **Quarry Bend Ltd.** holds one AFS debt security with amortized cost **$90,000** and fair value **$78,000**. Expected credit loss (amortized cost minus PV of expected collections) is **$15,000**. Quarry Bend does **not** intend to sell, and sale is **not** more likely than not required before recovery. FV-OCI adjustments for the full fair-value decline have already been recorded. What amount of **impairment loss** should Quarry Bend recognize in **net income**?

- A) $0, because all AFS unrealized losses remain in OCI until sale  
- B) $12,000, the full fair-value shortfall, because AFS is always written to FV through NI when FV < AC  
- C) $12,000, limited credit loss: min($15,000 credit loss, $12,000 FV shortfall)  
- D) $15,000, the full expected credit loss regardless of fair value  

**Answer:** **C.**  
AFS is impaired when FV < AC ($90,000 − $78,000 = **$12,000** shortfall). With **no intent to sell**, the credit-loss allowance is recognized in NI but **limited** by the amount that fair value is less than amortized cost: min($15,000, $12,000) = **$12,000**. The “extra” $3,000 of modeled credit loss above the market decline is not recognized (allowance cannot push carrying amount below fair value under ASC 326-30).  
- A is wrong: credit impairments on AFS go through **net income**.  
- B is wrong for the no-intent path (full shortfall through NI applies when the entity **intends to sell** / is more likely than not required to sell).  
- D ignores the fair-value ceiling on the AFS credit allowance.

---

### Q5 — CORE — Three-scenario measurement table (Demo 14-6 style) with balance-sheet build
**LO:** LO 14-6  
**Concept:** Period-end AFS impairment measurement across three scenarios; initial recognition of impairment JE; classification of credit vs noncredit; balance-sheet presentation  
**Scenario:**  
**Silverfern Mutual** holds a single AFS debt security (**Lakeport Industrial 5.25% notes**). Silverfern does **not** intend to sell and does **not** believe sale is more likely than not required before recovery. At December 31, Year 1, Silverfern has **already** adjusted the AFS investment to fair value through FV-OCI. Consider three mutually exclusive year-end fact patterns for the same amortized-cost basis:

|  | Scenario A | Scenario B | Scenario C |
|--|---:|---:|---:|
| Fair value, Dec 31 | $310,000 | $275,000 | $258,000 |
| Amortized cost, Dec 31 | 290,000 | 290,000 | 290,000 |
| Expected loss due to credit factors* | 28,000 | 28,000 | 28,000 |

\*Excess of amortized cost over the present value of cash flows expected to be collected.

**Required:**  
a. For each scenario, compute the **impairment loss in net income**. Show shortfall, credit loss, and the limit.  
b. Record the impairment JE (if any) for each scenario.  
c. For Scenario C only, prepare the **balance-sheet build** (AC, allowance, residual FVA, net) and identify the noncredit amount remaining in AOCI.

**Answer key:**  

**a. Measurement**

| Scenario | FV shortfall (AC − FV) | Expected credit loss | Impairment in NI | Reasoning |
|---|---:|---:|---:|---|
| A | 290,000 − 310,000 = **$(20,000)** (FV > AC) | 28,000 | **$0** | Not impaired |
| B | 290,000 − 275,000 = **$15,000** | 28,000 | **$15,000** | min(28,000, 15,000) = 15,000 |
| C | 290,000 − 258,000 = **$32,000** | 28,000 | **$28,000** | min(28,000, 32,000) = 28,000; noncredit $4,000 stays in OCI |

**b. Journal entries**

**Scenario A:** No impairment entry (existing FV-OCI unrealized **gain** of $20,000 remains in OCI).

**Scenario B — December 31**

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 15,000 | |
| Fair Value Adjustment—AFS | 15,000 | |
| Allowance for Credit Losses—AFS | | 15,000 |
| Unrealized Gain or Loss—OCI | | 15,000 |

**Check:** Dr 30,000 = Cr 30,000. **Balanced.**

**Scenario C — December 31**

| Account | Debit | Credit |
|---|---:|---:|
| Loss on Impairment | 28,000 | |
| Fair Value Adjustment—AFS | 28,000 | |
| Allowance for Credit Losses—AFS | | 28,000 |
| Unrealized Gain or Loss—OCI | | 28,000 |

**Check:** Dr 56,000 = Cr 56,000. **Balanced.**

**c. Scenario C balance-sheet build after impairment**

Before impairment, FVA credit (and OCI unrealized loss) for the full **$32,000** shortfall was already on the books. The impairment entry debits FVA **$28,000**, leaving **$4,000** FVA credit / OCI unrealized loss for the **noncredit** portion.

| Component | Amount |
|---|---:|
| Amortized cost (Investment in AFS) | $290,000 |
| Less: Allowance for Credit Losses | (28,000) |
| Amortized cost net of allowance | 262,000 |
| Less: residual FVA credit (noncredit) | (4,000) |
| **Carrying amount at fair value** | **$258,000** |

Net income absorbed **$28,000**; AOCI still holds **$(4,000)** noncredit unrealized loss.

**Key insight:** For AFS with no intent (or requirement) to sell, earnings absorb only the **credit** portion of the decline, capped by the **fair-value shortfall**; excess market decline is noncredit and remains in OCI under FV-OCI.

---

### Self-check
- [x] Every JE balances (Dr = Cr verified on all entries)
- [x] Math recomputed (min credit/FV-shortfall; multi-year equity bridges to FV changes)
- [x] Core demo not sidebar-only (Demo 14-6 / Review 14-6 AFS impairment model)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (one MC classification item)
- [x] Angles covered: initial_recognition_JE (Q1/Q2/Q3), subsequent_measurement_schedule (Q1/Q2 emphasis), period_end_adjusting_JE (Q1–Q3, Q5), disposal_maturity_or_settlement_JE (Q3), classification_presentation_or_disclosure (Q1e/Q3f/Q4), number_variant_twin (Q2)
