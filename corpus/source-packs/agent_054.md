# Agent 54 — CORE DEMO — LO 9-7

**Chapter:** 9  
**LO title:** Describe and compute the effect of LIFO liquidation  
**Critical gap LO:** no

## Concept list for this pack
- **LIFO liquidation** = ending inventory quantity under periodic LIFO falls below beginning quantity, eliminating prior-year layer(s)
- In rising prices, liquidated layers carry **lower historical unit costs** → lower COGS → higher pretax (and after-tax) income vs. matching current revenue to current cost
- **Pretax liquidation effect** = (current replacement cost − liquidated layer cost) × units liquidated (by layer)
- Equivalently: COGS if no liquidation (units sold × current RC) − COGS with liquidation
- **After-tax effect** = pretax effect × (1 − tax rate); taxes also rise by pretax × tax rate (LIFO conformity)
- **Voluntary** vs **involuntary** liquidation; material income effect requires **note (or parenthetical) disclosure** (ASC 330-10-S99-3)
- **Initial recognition / period-end JE:** periodic close that first books COGS composed of current purchases plus liquidated old layers
- **Interim anticipated replacement JE:** when temporary liquidation is expected to be restored before year-end, accrue extra COGS so interim income is not overstated; clear liability and restore LIFO layer when inventory is replaced
- **Settlement of temporary liquidation:** replacement purchase that restores prior LIFO layers (no permanent year-end liquidation)

---

### Q1 — CORE — Hearthstone Candle Co.: LIFO liquidation layers, income effect, initial year-end COGS recognition
**LO:** LO 9-7  
**Concept:** Compute multi-layer LIFO liquidation; pretax/after-tax income effect; initial recognition of period-end COGS under periodic LIFO (emphasis)  
**Scenario:**  
**Hearthstone Candle Co.** uses a **periodic inventory system** and the **LIFO** cost-flow assumption for financial reporting and tax. Year-end is December 31. Rising purchase prices have built three LIFO layers. Current-year **replacement cost** (unit purchase price) is **$9.00**. Income tax rate is **25%**.

Beginning inventory, January 1, Year 1:

| Layer (oldest first) | Units | Unit cost | Total cost |
|---|---:|---:|---:|
| Base layer | 25,000 | $4.00 | $100,000 |
| Year −1 layer | 8,000 | 5.50 | 44,000 |
| Year 0 layer | 3,000 | 7.00 | 21,000 |
| **Total beginning inventory** | **36,000** | | **$165,000** |

During Year 1, Hearthstone purchased **50,000** units at **$9.00** each (cash/AP). Physical count at December 31 shows **12,000** units on hand. Management did not rebuild inventory to beginning levels (involuntary supply constraint late in the year).

**Required:**  
a. Prepare a **subsequent measurement / layer schedule**: cost of goods available, ending inventory at LIFO, cost of goods sold by layer, and units liquidated from each beginning layer.  
b. Compute the **effect of the LIFO liquidation on pretax income** and on **after-tax income**. Show both the full-COGS comparison method and the by-layer (RC − layer cost) method.  
c. Record the **initial recognition** journal entries: (1) Year 1 purchases; (2) **December 31, Year 1 period-end closing entry** that recognizes ending inventory and COGS under LIFO (balanced).  
d. State the **disclosure** required if the income effect is material.

**Answer key:**  

**a. Layer schedule (periodic LIFO)**

| | Units | Unit cost | Total cost |
|---|---:|---:|---:|
| Beginning inventory | 36,000 | | $165,000 |
| Add: Purchases | 50,000 | $9.00 | 450,000 |
| **Cost of goods available for sale** | **86,000** | | **$615,000** |
| Less: Ending inventory (LIFO — oldest costs) | 12,000 | 4.00 | 48,000 |
| **Cost of goods sold** | **74,000** | | **$567,000** |

**Goods sold (74,000 units) from (newest first under LIFO):**

| Source | Units | Unit cost | Total cost |
|---|---:|---:|---:|
| Year 1 purchases layer | 50,000 | $9.00 | $450,000 |
| Year 0 layer (**fully liquidated**) | 3,000 | 7.00 | 21,000 |
| Year −1 layer (**fully liquidated**) | 8,000 | 5.50 | 44,000 |
| Base layer (**partially liquidated**) | 13,000 | 4.00 | 52,000 |
| **Cost of goods sold** | **74,000** | | **$567,000** |

**Ending inventory composition:** 12,000 base-layer units × $4.00 = **$48,000** (remainder of original 25,000-unit base).

**Units liquidated from beginning inventory:** 36,000 − 12,000 = **24,000 units** (all of Year 0 + all of Year −1 + 13,000 of base).

Checks: COGAS $615,000 − EI $48,000 = COGS **$567,000**; layer sum 450 + 21 + 44 + 52 = **567**.

**b. Income effect of LIFO liquidation**

*Method 1 — full COGS comparison (Demo 9-7 style):*

| | Amount |
|---|---:|
| COGS assuming liquidation had **not** occurred (74,000 × $9.00 current RC) | $666,000 |
| COGS **with** liquidation (from schedule) | 567,000 |
| **Increase in pretax income** | **$99,000** |

*Method 2 — by liquidated layer (RC − old unit cost):*

| Liquidated layer | Units | RC − layer cost | Pretax effect |
|---|---:|---:|---:|
| Year 0 | 3,000 | $9.00 − $7.00 = $2.00 | $6,000 |
| Year −1 | 8,000 | 9.00 − 5.50 = 3.50 | 28,000 |
| Base | 13,000 | 9.00 − 4.00 = 5.00 | 65,000 |
| **Total pretax increase** | **24,000** | | **$99,000** |

| | Amount |
|---|---:|
| Increase in pretax income | $99,000 |
| Increase in income tax ($99,000 × 0.25) | 24,750 |
| **After-tax increase in income** ($99,000 × 0.75) | **$74,250** |

**c. Journal entries — initial recognition emphasis**

*(1) Purchases during Year 1 (summary)*

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 450,000 | |
| Accounts Payable (or Cash) | | 450,000 |
| *50,000 units × $9.00* | | |

**Check:** Dr = Cr = **450,000**. Balanced.

*(2) December 31, Year 1 — period-end close (first recognition of COGS including liquidated layers)*

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending) | 48,000 | |
| Cost of Goods Sold | 567,000 | |
| Inventory (beginning) | | 165,000 |
| Purchases | | 450,000 |
| *Close BI and Purchases; recognize EI and LIFO COGS with liquidated layers* | | |

**Check:** Dr = 48,000 + 567,000 = **615,000**; Cr = 165,000 + 450,000 = **615,000**. Balanced.

(After this entry, Inventory on the books equals LIFO EI of $48,000.)

**d. Disclosure**  
If the income effect of LIFO liquidation is **material**, disclose the income realized as a result of LIFO inventory liquidation so the financial statements are not misleading. Disclosure may be in a **footnote** or **parenthetically on the face of the income statement** (ASC 330-10-S99-3). Example wording: “Net income includes approximately $74,250 after tax from liquidation of LIFO inventory layers.”

**Key insight:** Under periodic LIFO, a drop in physical units forces prior-year (lower-cost) layers into COGS. That **understates COGS relative to current replacement cost** and **overstates income**. Measure the distortion as Σ[(RC − layer cost) × liquidated units], then apply (1 − t) for the after-tax effect. The year-end closing entry is where that liquidated-layer COGS is first recognized in the accounts.

---

### Q2 — CORE number variant — Ironridge Fasteners Inc.: multi-layer liquidation twin
**LO:** LO 9-7  
**Concept:** Number-variant twin — multi-layer LIFO liquidation schedule, pretax/after-tax effect, balanced period-end JE  
**Scenario:**  
**Ironridge Fasteners Inc.** uses **periodic LIFO**. Tax rate is **21%**. Current replacement cost is **$22** per unit.

Beginning inventory, January 1:

| Layer (oldest first) | Units | Unit cost | Total cost |
|---|---:|---:|---:|
| Base layer | 40,000 | $12.00 | $480,000 |
| Intermediate layer | 15,000 | 15.00 | 225,000 |
| Recent layer | 5,000 | 18.00 | 90,000 |
| **Total beginning inventory** | **60,000** | | **$795,000** |

Purchases during the year: **80,000** units @ **$22** = **$1,760,000**.  
Ending inventory physical count: **22,000** units.

**Required:**  
a. Layer schedule for EI and COGS under LIFO; identify units liquidated by layer.  
b. Pretax and after-tax income effect of the LIFO liquidation.  
c. December 31 period-end closing JE (Inventory EI, COGS, remove BI and Purchases).  
d. Compute income tax incremental to the liquidation effect only.

**Answer key:**  

**a. Schedule**

Units available = 60,000 + 80,000 = **140,000**  
Units sold = 140,000 − 22,000 = **118,000**

| | Units | Unit cost | Total |
|---|---:|---:|---:|
| Beginning inventory | 60,000 | | $795,000 |
| Purchases | 80,000 | $22.00 | 1,760,000 |
| **COGAS** | **140,000** | | **$2,555,000** |
| Ending inventory (LIFO, base layer) | 22,000 | 12.00 | 264,000 |
| **COGS** | **118,000** | | **$2,291,000** |

**COGS by layer:**

| Source | Units | Unit cost | Total |
|---|---:|---:|---:|
| Current purchases | 80,000 | $22.00 | $1,760,000 |
| Recent layer (**fully liquidated**) | 5,000 | 18.00 | 90,000 |
| Intermediate layer (**fully liquidated**) | 15,000 | 15.00 | 225,000 |
| Base layer (**partially liquidated**) | 18,000 | 12.00 | 216,000 |
| **COGS** | **118,000** | | **$2,291,000** |

EI: 22,000 × $12 = **$264,000** (of original 40,000 base).  
Units liquidated from BI: 60,000 − 22,000 = **38,000** (5k + 15k + 18k).

Checks: 2,555,000 − 264,000 = **2,291,000**; layer sum 1,760 + 90 + 225 + 216 = **2,291,000**.

**b. Income effect**

| Liquidated layer | Units | RC − cost | Pretax |
|---|---:|---:|---:|
| Recent | 5,000 | $22 − $18 = $4 | $20,000 |
| Intermediate | 15,000 | 22 − 15 = 7 | 105,000 |
| Base | 18,000 | 22 − 12 = 10 | 180,000 |
| **Total pretax increase** | **38,000** | | **$305,000** |

Cross-check: COGS if no liquidation = 118,000 × $22 = **$2,596,000**;  
2,596,000 − 2,291,000 = **$305,000**.

| | Amount |
|---|---:|
| Pretax increase | $305,000 |
| After-tax increase ($305,000 × 0.79) | **$240,950** |

**c. December 31 period-end closing JE**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending) | 264,000 | |
| Cost of Goods Sold | 2,291,000 | |
| Inventory (beginning) | | 795,000 |
| Purchases | | 1,760,000 |

**Check:** Dr = 264,000 + 2,291,000 = **2,555,000**; Cr = 795,000 + 1,760,000 = **2,555,000**. Balanced.

**d. Incremental tax from liquidation**  
$305,000 × 0.21 = **$64,050** additional income tax (because LIFO conformity applies the same inventory method for tax).

**Key insight:** Same mechanics as Q1 with all new quantities, unit costs, and tax rate. Always verify pretax effect two ways (by-layer gap vs. full COGS at RC) and prove the closing JE balances to COGAS.

---

### Q3 — CORE alternate angle — Copperleaf Packaging: interim anticipated replacement JE, settlement on replacement, permanent liquidation, disclosure
**LO:** LO 9-7  
**Concept:** Period-end/interim adjusting JE for temporary LIFO liquidation expected to be restored; settlement JE when inventory is replaced; permanent year-end liquidation measurement and classification/disclosure  
**Scenario:**  
**Copperleaf Packaging LLC** accounts for a major raw material under **LIFO** (perpetual records for unit tracking; external reporting LIFO). Current replacement cost has been rising. Tax rate is **25%**.

**Part A — Temporary (interim) involuntary liquidation expected to be restored**  
On **September 30, Year 5**, a supplier strike causes Copperleaf to dip **4,000 units** into its LIFO base layer. Those units had a LIFO carrying cost of **$8** each. Management **expects full replacement before December 31** at the current replacement cost of **$20** per unit. Sales of the 4,000 units have already reduced Inventory and charged COGS at the **$8** LIFO cost under perpetual LIFO.

**Part B — Settlement when replaced**  
On **November 12, Year 5**, Copperleaf purchases **4,000** replacement units for **$20** cash each, restoring the LIFO base layer quantities.

**Part C — Permanent year-end liquidation (different year)**  
In **Year 6**, beginning LIFO inventory is a **single base layer** of **18,000 units @ $8 = $144,000**. Purchases are **30,000 @ $21**. Ending count is **11,000 units**. Liquidation is **permanent** (not restored).

**Required:**  
a. **September 30, Year 5 interim adjusting entry** so interim statements do not overstate income from the temporary liquidation (accrue the excess of current RC over LIFO cost).  
b. **November 12, Year 5 settlement / replacement JE** that restores the LIFO layer and clears the liability (and cash paid).  
c. For **Year 6 permanent liquidation**: compute pretax and after-tax income effect; prepare the **December 31, Year 6** periodic-style closing JE (assume Copperleaf closes with BI/Purchases/EI for external LIFO measurement).  
d. Classify the Year 5 event as voluntary or involuntary; state required **presentation/disclosure** if Year 6’s effect is material.

**Answer key:**  

**a. September 30, Year 5 — interim adjusting JE (anticipated replacement)**

Excess of current cost over LIFO cost on liquidated units:  
4,000 × ($20 − $8) = **$48,000**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 48,000 | |
| Accrued Liability for Inventory Replacement | | 48,000 |
| *Raise interim COGS to current RC for temporary LIFO liquidation expected to be restored before year-end* | | |

**Check:** Dr = Cr = **48,000**. Balanced.  
Combined with the $8 LIFO cost already in COGS, the 4,000 units carry **$80,000** (= 4,000 × $20) of COGS in interim results — matching current revenue to current cost.

**b. November 12, Year 5 — disposal/settlement of temporary liquidation (replacement)**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 32,000 | |
| Accrued Liability for Inventory Replacement | 48,000 | |
| Cash | | 80,000 |
| *Restore 4,000 base-layer units at LIFO cost $8; clear liability; pay current RC $20* | | |

**Check:** Dr = 32,000 + 48,000 = **80,000**; Cr = **80,000**. Balanced.  
After replacement: LIFO base quantity is restored (no permanent year-end liquidation from this episode); cash outlay equals current cost of the temporary dip.

**c. Year 6 — permanent LIFO liquidation**

Units available = 18,000 + 30,000 = 48,000  
Units sold = 48,000 − 11,000 = **37,000**

| | Units | Unit cost | Total |
|---|---:|---:|---:|
| Beginning inventory (base) | 18,000 | $8.00 | $144,000 |
| Purchases | 30,000 | 21.00 | 630,000 |
| **COGAS** | **48,000** | | **$774,000** |
| Ending inventory (LIFO base remainder) | 11,000 | 8.00 | 88,000 |
| **COGS** | **37,000** | | **$686,000** |

COGS by layer: purchases 30,000 × $21 = $630,000; base liquidated 7,000 × $8 = $56,000; total **$686,000**.

Liquidated units = 18,000 − 11,000 = **7,000**  
Pretax effect = 7,000 × ($21 − $8) = **$91,000**  
Cross-check: COGS if no liquidation = 37,000 × $21 = $777,000; 777,000 − 686,000 = **$91,000**.  
After-tax effect = $91,000 × 0.75 = **$68,250**.

*December 31, Year 6 period-end closing JE:*

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending) | 88,000 | |
| Cost of Goods Sold | 686,000 | |
| Inventory (beginning) | | 144,000 |
| Purchases | | 630,000 |

**Check:** Dr = 88,000 + 686,000 = **774,000**; Cr = 144,000 + 630,000 = **774,000**. Balanced.

**d. Classification and disclosure**  
- Year 5 strike-driven dip: **involuntary** liquidation (uncontrollable cause). (A **voluntary** liquidation would be management’s deliberate decision to run inventory down.)  
- Year 6 permanent liquidation: if the **$68,250 after-tax** (or pretax $91,000) effect is material, disclose income realized from LIFO liquidation in the **notes** or **parenthetically** on the income statement so statements are not misleading.

**Key insight:** Temporary liquidations that will be restored should not inflate interim earnings — accrue the RC−LIFO gap, then **settle** by restoring Inventory at old LIFO cost and clearing the liability when cash is paid at current prices. Permanent year-end liquidations remain in COGS at old layer costs; quantify and **disclose** the income effect.

---

### Q4 — MC — Classification of liquidation type and disclosure
**LO:** LO 9-7  
**Concept:** Voluntary vs involuntary LIFO liquidation; required disclosure of material liquidation income effect  

**Question 1:**  
Which statement best describes a **voluntary** LIFO liquidation and the related reporting obligation when the income effect is material?

- A) A supplier strike forces inventory below beginning layers; the company may omit any note disclosure because the event was outside management’s control.  
- B) Management deliberately reduces inventory quantities (e.g., expected product change or lower demand), eliminating prior LIFO layers; if the income effect is material, disclose income realized from LIFO liquidation in a footnote or parenthetically on the income statement.  
- C) Any reduction in the LIFO reserve allowance account is a LIFO liquidation and must always be presented as a separate line on the face of the balance sheet.  
- D) Voluntary liquidation occurs only when ending inventory quantity exceeds beginning quantity; no income effect is possible in rising-price environments.

**Answer:** **B.**  
Voluntary liquidation is management’s choice to reduce normal inventory quantities, which can eliminate older LIFO layers. In rising prices that lowers COGS and raises income; material amounts require disclosure (footnote or parenthetical) so statements are not misleading. A describes an **involuntary** liquidation (still may require disclosure if material). C confuses LIFO **reserve** mechanics with unit-layer liquidation. D is the opposite of liquidation (quantity increase builds layers).

**Question 2:**  
**Millcreek Outfitters** has beginning LIFO inventory of **28,000 units @ $40**. During the year it sells more units than it purchases; ending inventory is **19,000 units**. Current replacement cost is **$55**. Tax rate is **25%**. What is the **after-tax** LIFO liquidation effect on income?

- A) $99,000  
- B) $132,000  
- C) $101,250  
- D) $385,000  

**Answer:** **C.**  
Units liquidated = 28,000 − 19,000 = **9,000**.  
Pretax effect = 9,000 × ($55 − $40) = **$135,000**.  
After-tax = $135,000 × (1 − 0.25) = **$101,250**.  
(A is pretax × 0.75 with wrong pretax 132k; B is 9,000 × 14.67-style error or 135k × approx; D is 28,000 × something incorrect.)

---

### Self-check
- [x] Every JE balances (Q1 purchases + close; Q2 close; Q3 interim, settlement, Year 6 close)
- [x] Math recomputed (layer sums, COGAS − EI = COGS, dual methods for pretax effect, after-tax × (1 − t))
- [x] Core demo not sidebar-only (Demo 9-7 / Review 9-7 path: liquidation effect, disclosure, interim replacement context)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (two classification/computation items fitting LO 9-7)
- [x] Angles covered: initial_recognition_JE (emphasis), subsequent_measurement_schedule, period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
