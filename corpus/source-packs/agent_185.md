# Agent 185 — CORE DEMO — LO 9-7

**Chapter:** 9  
**LO title:** Describe and compute the effect of LIFO liquidation  
**Critical gap LO:** no

## Concept list for this pack
- **LIFO liquidation** = under periodic LIFO, ending inventory **quantity** falls below beginning quantity so prior-year layer(s) are eliminated and charged to COGS
- In **rising prices**, liquidated layers have **lower historical unit costs** → COGS understates current cost → pretax (and after-tax) income is **higher** than if all units sold carried current replacement cost
- **Pretax liquidation effect** = Σ[(current replacement cost − liquidated layer unit cost) × units liquidated from that layer]; equivalently COGS@RC − COGS with liquidation
- **After-tax effect** = pretax × (1 − tax rate); incremental tax = pretax × tax rate (LIFO conformity)
- **Subsequent measurement schedule (emphasis):** multi-year LIFO **layer roll-forward** (base + incremental layers by year) through a liquidation year; COGS-by-layer schedule
- **Initial recognition JE:** summary Purchases entry; first recognition of liquidated-layer COGS at period-end close
- **Period-end adjusting JE:** periodic close (BI + Purchases → EI + COGS); interim accrual when temporary liquidation is expected to be restored before year-end
- **Disposal / settlement JE:** replacement purchase that restores the LIFO base quantity and clears the interim replacement liability
- **Voluntary vs involuntary** liquidation; material income effect requires **footnote or parenthetical disclosure** (ASC 330-10-S99-3)

---

### Q1 — CORE — Northvale Ceramics: multi-year LIFO layer schedule, Year 3 liquidation, pretax/after-tax effect, JEs
**LO:** LO 9-7  
**Concept:** Subsequent measurement (multi-year LIFO layer roll-forward); Year 3 liquidation COGS-by-layer schedule; pretax and after-tax income effect; initial purchases JE and period-end closing JE  
**Scenario:**  
**Northvale Ceramics Co.** uses a **periodic inventory system** and **LIFO** for tax and external reporting. Calendar year-end. Purchase prices have been rising. Income tax rate is **25%**.

On **January 1, Year 1**, beginning inventory is a **single base layer**:

| Layer | Units | Unit cost | Total cost |
|---|---:|---:|---:|
| Base (pre–Year 1) | 50,000 | $6.00 | $300,000 |

Activity (all purchases at the year’s current unit cost):

| Year | Units purchased | Unit cost | Ending inventory (physical units) |
|---|---:|---:|---:|
| Year 1 | 40,000 | $8.00 | 55,000 |
| Year 2 | 45,000 | 10.00 | 62,000 |
| Year 3 | 30,000 | 12.00 | 35,000 |

In Year 3, ending quantity falls below beginning quantity (LIFO liquidation). Current replacement cost in Year 3 equals the Year 3 purchase price of **$12.00**. Management did not rebuild inventory before year-end (supply constraint late in Year 3).

**Required:**  
a. Prepare a **subsequent measurement schedule** of LIFO inventory **layers** at December 31 of Year 1, Year 2, and Year 3 (units and dollars by layer; total EI). Also show units sold and COGS each year under periodic LIFO.  
b. For **Year 3 only**, prepare the **COGS-by-layer** schedule (newest first) identifying fully and partially liquidated beginning layers.  
c. Compute the **effect of the Year 3 LIFO liquidation on pretax income** and on **after-tax income**. Show both the by-layer (RC − layer cost) method and the full-COGS comparison method (Demo 9-7 style).  
d. Record **Year 3 journal entries**: (1) summary of purchases; (2) **December 31, Year 3 period-end closing entry** recognizing ending inventory and COGS under LIFO (must balance).  
e. State the **disclosure** required if the Year 3 income effect is material.

**Answer key:**  

**a. Subsequent measurement — LIFO layer roll-forward**

**Year 1**

| | Units | Unit cost | Total cost |
|---|---:|---:|---:|
| Beginning inventory (base) | 50,000 | $6.00 | $300,000 |
| Purchases | 40,000 | 8.00 | 320,000 |
| **Cost of goods available** | **90,000** | | **$620,000** |
| Ending inventory (LIFO) | 55,000 | | **$340,000** |
| Cost of goods sold | 35,000 | | **$280,000** |

Ending layers at Dec. 31, Year 1:

| Layer | Units | Unit cost | Total |
|---|---:|---:|---:|
| Base | 50,000 | $6.00 | $300,000 |
| Year 1 increment | 5,000 | 8.00 | 40,000 |
| **Total EI** | **55,000** | | **$340,000** |

COGS Year 1 = 35,000 × $8.00 = **$280,000** (all from current purchases; no liquidation).  
Check: $620,000 − $340,000 = **$280,000**.

**Year 2**

| | Units | Unit cost | Total cost |
|---|---:|---:|---:|
| Beginning inventory | 55,000 | | $340,000 |
| Purchases | 45,000 | $10.00 | 450,000 |
| **Cost of goods available** | **100,000** | | **$790,000** |
| Ending inventory (LIFO) | 62,000 | | **$410,000** |
| Cost of goods sold | 38,000 | | **$380,000** |

Ending layers at Dec. 31, Year 2:

| Layer | Units | Unit cost | Total |
|---|---:|---:|---:|
| Base | 50,000 | $6.00 | $300,000 |
| Year 1 | 5,000 | 8.00 | 40,000 |
| Year 2 increment | 7,000 | 10.00 | 70,000 |
| **Total EI** | **62,000** | | **$410,000** |

COGS Year 2 = 38,000 × $10.00 = **$380,000** (no liquidation).  
Check: $790,000 − $410,000 = **$380,000**.

**Year 3 (liquidation year)**

| | Units | Unit cost | Total cost |
|---|---:|---:|---:|
| Beginning inventory | 62,000 | | $410,000 |
| Purchases | 30,000 | $12.00 | 360,000 |
| **Cost of goods available** | **92,000** | | **$770,000** |
| Ending inventory (LIFO — base remainder) | 35,000 | 6.00 | **$210,000** |
| Cost of goods sold | 57,000 | | **$560,000** |

Ending layers at Dec. 31, Year 3:

| Layer | Units | Unit cost | Total |
|---|---:|---:|---:|
| Base (remainder of original 50,000) | 35,000 | $6.00 | $210,000 |
| Year 1 | 0 | — | 0 |
| Year 2 | 0 | — | 0 |
| **Total EI** | **35,000** | | **$210,000** |

Units liquidated from beginning inventory = 62,000 − 35,000 = **27,000**.  
Check: $770,000 − $210,000 = **$560,000**.

**b. Year 3 COGS by layer (LIFO — newest first)**

| Source | Units | Unit cost | Total cost | Liquidation status |
|---|---:|---:|---:|---|
| Year 3 purchases | 30,000 | $12.00 | $360,000 | Current layer (not a prior-year liquidation) |
| Year 2 layer | 7,000 | 10.00 | 70,000 | **Fully liquidated** |
| Year 1 layer | 5,000 | 8.00 | 40,000 | **Fully liquidated** |
| Base layer | 15,000 | 6.00 | 90,000 | **Partially liquidated** (15,000 of 50,000) |
| **Cost of goods sold** | **57,000** | | **$560,000** | |

Layer sum: 360,000 + 70,000 + 40,000 + 90,000 = **$560,000**.

**c. Income effect of Year 3 LIFO liquidation**

*Method 1 — by liquidated layer (RC − old unit cost):*

| Liquidated layer | Units | RC − layer cost | Pretax effect |
|---|---:|---:|---:|
| Year 2 | 7,000 | $12.00 − $10.00 = $2.00 | $14,000 |
| Year 1 | 5,000 | 12.00 − 8.00 = 4.00 | 20,000 |
| Base | 15,000 | 12.00 − 6.00 = 6.00 | 90,000 |
| **Total pretax increase** | **27,000** | | **$124,000** |

*Method 2 — full COGS comparison (Demo 9-7):*

| | Amount |
|---|---:|
| COGS if liquidation had **not** occurred (57,000 × $12.00) | $684,000 |
| COGS **with** liquidation (from schedule) | 560,000 |
| **Increase in pretax income** | **$124,000** |

| | Amount |
|---|---:|
| Increase in pretax income | $124,000 |
| Increase in income tax ($124,000 × 0.25) | 31,000 |
| **After-tax increase in income** ($124,000 × 0.75) | **$93,000** |

**d. Year 3 journal entries**

*(1) Purchases during Year 3 (summary)*

| Account | Debit | Credit |
|---|---:|---:|
| Purchases | 360,000 | |
| Accounts Payable (or Cash) | | 360,000 |
| *30,000 units × $12.00* | | |

**Check:** Dr 360,000 = Cr 360,000. **Balanced.**

*(2) December 31, Year 3 — period-end close (initial recognition of COGS including liquidated layers)*

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending) | 210,000 | |
| Cost of Goods Sold | 560,000 | |
| Inventory (beginning) | | 410,000 |
| Purchases | | 360,000 |
| *Close BI and Purchases; recognize LIFO EI and COGS with liquidated prior layers* | | |

**Check:** Dr = 210,000 + 560,000 = **770,000**; Cr = 410,000 + 360,000 = **770,000**. **Balanced.**  
After this entry, Inventory on the books equals LIFO EI of **$210,000**.

**e. Disclosure**  
If the income effect of LIFO liquidation is **material**, disclose the income realized from LIFO inventory liquidation so the financial statements are not misleading. Disclosure may be in a **footnote** or **parenthetically on the face of the income statement** (ASC 330-10-S99-3). Example: “Net income includes approximately $93,000 after tax from liquidation of LIFO inventory layers.”

**Key insight:** The multi-year **layer roll-forward** is the subsequent measurement engine—layers accumulate only when ending quantity rises. When quantity falls, prior layers flow into COGS at old costs. The pretax distortion equals Σ[(RC − layer cost) × liquidated units], and after-tax income rises by pretax × (1 − t). The year-end close is where that liquidated-layer COGS is recognized in the accounts.

---

### Q2 — CORE number variant — Lakewood Valve Works: multi-layer liquidation twin
**LO:** LO 9-7  
**Concept:** Number-variant twin — multi-layer LIFO liquidation schedule; pretax/after-tax effect at 21% tax; balanced period-end closing JE  
**Scenario:**  
**Lakewood Valve Works** uses **periodic LIFO**. Tax rate is **21%**. Current replacement cost is **$45** per unit.

Beginning inventory, January 1:

| Layer (oldest first) | Units | Unit cost | Total cost |
|---|---:|---:|---:|
| Base layer | 80,000 | $25.00 | $2,000,000 |
| Intermediate layer | 20,000 | 30.00 | 600,000 |
| Recent layer | 10,000 | 38.00 | 380,000 |
| **Total beginning inventory** | **110,000** | | **$2,980,000** |

Purchases during the year: **95,000** units @ **$45** = **$4,275,000**.  
Ending inventory physical count: **48,000** units.

**Required:**  
a. Prepare the COGAS / EI / COGS schedule and the **COGS-by-layer** schedule; identify units liquidated by layer.  
b. Compute pretax and after-tax income effect of the LIFO liquidation (both methods).  
c. Prepare the December 31 period-end closing JE.  
d. Compute the **incremental income tax** attributable solely to the liquidation effect.

**Answer key:**  

**a. Schedules**

Units available = 110,000 + 95,000 = **205,000**  
Units sold = 205,000 − 48,000 = **157,000**

| | Units | Unit cost | Total |
|---|---:|---:|---:|
| Beginning inventory | 110,000 | | $2,980,000 |
| Purchases | 95,000 | $45.00 | 4,275,000 |
| **COGAS** | **205,000** | | **$7,255,000** |
| Ending inventory (LIFO, base remainder) | 48,000 | 25.00 | 1,200,000 |
| **COGS** | **157,000** | | **$6,055,000** |

**COGS by layer:**

| Source | Units | Unit cost | Total |
|---|---:|---:|---:|
| Current purchases | 95,000 | $45.00 | $4,275,000 |
| Recent layer (**fully liquidated**) | 10,000 | 38.00 | 380,000 |
| Intermediate layer (**fully liquidated**) | 20,000 | 30.00 | 600,000 |
| Base layer (**partially liquidated**) | 32,000 | 25.00 | 800,000 |
| **COGS** | **157,000** | | **$6,055,000** |

EI: 48,000 × $25 = **$1,200,000** (of original 80,000 base).  
Units liquidated from BI: 110,000 − 48,000 = **62,000** (10k + 20k + 32k).

Checks: 7,255,000 − 1,200,000 = **6,055,000**; layer sum 4,275 + 380 + 600 + 800 = **6,055,000**.

**b. Income effect**

| Liquidated layer | Units | RC − cost | Pretax |
|---|---:|---:|---:|
| Recent | 10,000 | $45 − $38 = $7 | $70,000 |
| Intermediate | 20,000 | 45 − 30 = 15 | 300,000 |
| Base | 32,000 | 45 − 25 = 20 | 640,000 |
| **Total pretax increase** | **62,000** | | **$1,010,000** |

Cross-check: COGS if no liquidation = 157,000 × $45 = **$7,065,000**;  
7,065,000 − 6,055,000 = **$1,010,000**.

| | Amount |
|---|---:|
| Pretax increase | $1,010,000 |
| After-tax increase ($1,010,000 × 0.79) | **$797,900** |

**c. December 31 period-end closing JE**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending) | 1,200,000 | |
| Cost of Goods Sold | 6,055,000 | |
| Inventory (beginning) | | 2,980,000 |
| Purchases | | 4,275,000 |

**Check:** Dr = 1,200,000 + 6,055,000 = **7,255,000**; Cr = 2,980,000 + 4,275,000 = **7,255,000**. **Balanced.**

**d. Incremental tax from liquidation**  
$1,010,000 × 0.21 = **$212,100** additional income tax (LIFO conformity applies the same inventory method for tax).

**Key insight:** Same LO 9-7 mechanics with all new quantities, unit costs, and a **21%** tax rate. Always prove pretax two ways (by-layer gap vs. full COGS at RC) and prove the closing JE balances to COGAS.

---

### Q3 — CORE alternate angle — Summit Ridge Apparel: interim anticipated replacement JE, settlement on replacement, permanent year-end liquidation
**LO:** LO 9-7  
**Concept:** Period-end/interim adjusting JE when temporary LIFO liquidation is expected to be restored; settlement JE on replacement (disposal of temporary liquidation); permanent year-end liquidation schedule and disclosure  
**Scenario:**  
**Summit Ridge Apparel LLC** tracks units continuously but reports inventory under **LIFO**. Purchase prices have been rising. Tax rate is **25%**.

**Part A — Temporary (interim) involuntary liquidation expected to be restored**  
On **August 31, Year 4**, a port shutdown forces Summit Ridge to dip **6,000 units** into its LIFO base layer. Those units had a LIFO carrying cost of **$15** each. Management **expects full replacement before December 31** at the current replacement cost of **$28** per unit. Sales of the 6,000 units have already reduced Inventory and charged COGS at the **$15** LIFO cost under perpetual LIFO tracking.

**Part B — Settlement when replaced**  
On **October 20, Year 4**, Summit Ridge purchases **6,000** replacement units for **$28** cash each, restoring the LIFO base layer quantities.

**Part C — Permanent year-end liquidation (Year 5)**  
In **Year 5**, beginning LIFO inventory is a **single base layer** of **22,000 units @ $15 = $330,000**. Purchases are **40,000 @ $29**. Ending count is **14,000 units**. Liquidation is **permanent** (not restored before year-end). Current replacement cost = **$29**.

**Required:**  
a. **August 31, Year 4 interim adjusting entry** so interim statements do not overstate income from the temporary liquidation (accrue the excess of current RC over LIFO cost).  
b. **October 20, Year 4 settlement / replacement JE** that restores the LIFO layer and clears the liability (and records cash paid).  
c. For **Year 5 permanent liquidation**: prepare the COGAS/EI/COGS and COGS-by-layer schedules; compute pretax and after-tax income effect; prepare the **December 31, Year 5** periodic-style closing JE.  
d. Classify the Year 4 event as voluntary or involuntary; state required **presentation/disclosure** if Year 5’s effect is material.

**Answer key:**  

**a. August 31, Year 4 — interim adjusting JE (anticipated replacement)**

Excess of current cost over LIFO cost on liquidated units:  
6,000 × ($28 − $15) = **$78,000**

| Account | Debit | Credit |
|---|---:|---:|
| Cost of Goods Sold | 78,000 | |
| Accrued Liability for Inventory Replacement | | 78,000 |
| *Raise interim COGS to current RC for temporary LIFO liquidation expected to be restored before year-end* | | |

**Check:** Dr 78,000 = Cr 78,000. **Balanced.**  
Combined with the $15 LIFO cost already in COGS, the 6,000 units carry **$168,000** (= 6,000 × $28) of COGS in interim results — matching current revenue to current cost.

**b. October 20, Year 4 — settlement of temporary liquidation (replacement)**

| Account | Debit | Credit |
|---|---:|---:|
| Inventory | 90,000 | |
| Accrued Liability for Inventory Replacement | 78,000 | |
| Cash | | 168,000 |
| *Restore 6,000 base-layer units at LIFO cost $15; clear liability; pay current RC $28* | | |

**Check:** Dr = 90,000 + 78,000 = **168,000**; Cr = **168,000**. **Balanced.**  
After replacement: LIFO base quantity is restored (no permanent year-end liquidation from this episode); cash outlay equals current cost of the temporary dip.

**c. Year 5 — permanent LIFO liquidation**

Units available = 22,000 + 40,000 = **62,000**  
Units sold = 62,000 − 14,000 = **48,000**

| | Units | Unit cost | Total |
|---|---:|---:|---:|
| Beginning inventory (base) | 22,000 | $15.00 | $330,000 |
| Purchases | 40,000 | 29.00 | 1,160,000 |
| **COGAS** | **62,000** | | **$1,490,000** |
| Ending inventory (LIFO base remainder) | 14,000 | 15.00 | 210,000 |
| **COGS** | **48,000** | | **$1,280,000** |

**COGS by layer:**

| Source | Units | Unit cost | Total |
|---|---:|---:|---:|
| Purchases | 40,000 | $29.00 | $1,160,000 |
| Base (liquidated) | 8,000 | 15.00 | 120,000 |
| **COGS** | **48,000** | | **$1,280,000** |

Liquidated units = 22,000 − 14,000 = **8,000**  
Pretax effect = 8,000 × ($29 − $15) = **$112,000**  
Cross-check: COGS if no liquidation = 48,000 × $29 = $1,392,000; 1,392,000 − 1,280,000 = **$112,000**.  
After-tax effect = $112,000 × 0.75 = **$84,000**.  
Incremental tax = $112,000 × 0.25 = **$28,000**.

*December 31, Year 5 period-end closing JE:*

| Account | Debit | Credit |
|---|---:|---:|
| Inventory (ending) | 210,000 | |
| Cost of Goods Sold | 1,280,000 | |
| Inventory (beginning) | | 330,000 |
| Purchases | | 1,160,000 |

**Check:** Dr = 210,000 + 1,280,000 = **1,490,000**; Cr = 330,000 + 1,160,000 = **1,490,000**. **Balanced.**

**d. Classification and disclosure**  
- Year 4 port-shutdown dip: **involuntary** liquidation (uncontrollable cause). (A **voluntary** liquidation would be management’s deliberate decision to run inventory down—e.g., product change or lower expected demand.)  
- Year 5 permanent liquidation: if the **$84,000 after-tax** (or pretax $112,000) effect is material, disclose income realized from LIFO liquidation in the **notes** or **parenthetically** on the income statement so statements are not misleading.

**Key insight:** Temporary liquidations expected to be restored should not inflate interim earnings—accrue the RC−LIFO gap, then **settle** by restoring Inventory at old LIFO cost and clearing the liability when cash is paid at current prices. Permanent year-end liquidations remain in COGS at old layer costs; quantify and **disclose** the income effect.

---

### Q4 — MC — Classification and after-tax effect computation
**LO:** LO 9-7  
**Concept:** Voluntary vs involuntary LIFO liquidation classification and material disclosure; after-tax liquidation income effect  

**Question 1:**  
Which statement best describes an **involuntary** LIFO liquidation and the related reporting obligation when the income effect is material?

- A) Management deliberately reduces inventory for an anticipated product redesign; because the decision was intentional, no note disclosure is ever required.  
- B) Uncontrollable causes (e.g., strike, shortage, delayed deliveries, or unexpected demand) force inventory below beginning LIFO layers; if the income effect is material, disclose income realized from LIFO liquidation in a footnote or parenthetically on the income statement.  
- C) LIFO liquidation is defined solely as a decrease in the LIFO reserve contra account and must be presented as a separate liability on the balance sheet.  
- D) Involuntary liquidation occurs only when ending inventory quantity exceeds beginning quantity and always decreases pretax income in a rising-price environment.

**Answer:** **B.**  
Involuntary liquidation is forced by uncontrollable events that eliminate prior LIFO layers. In rising prices that lowers COGS and raises income; material amounts require disclosure (footnote or parenthetical) so statements are not misleading (ASC 330-10-S99-3). A describes a **voluntary** liquidation (disclosure may still be required if material). C confuses LIFO **reserve** mechanics with unit-layer liquidation. D is the opposite of liquidation (quantity increase builds layers) and misstates the income direction.

**Question 2:**  
**Pinnacle Outdoor Gear** has beginning LIFO inventory of **36,000 units @ $52**. During the year it sells more units than it purchases; ending inventory is **24,000 units**. Current replacement cost is **$70**. Tax rate is **25%**. What is the **after-tax** LIFO liquidation effect on income?

- A) $162,000  
- B) $216,000  
- C) $648,000  
- D) $540,000  

**Answer:** **A.**  
Units liquidated = 36,000 − 24,000 = **12,000**.  
Pretax effect = 12,000 × ($70 − $52) = 12,000 × $18 = **$216,000**.  
After-tax = $216,000 × (1 − 0.25) = **$162,000**.  
(B is pretax; C is 36,000 × $18; D is 12,000 × $45-style error.)

---

### Self-check
- [x] Every JE balances (Q1 purchases + close; Q2 close; Q3 interim, settlement, Year 5 close)
- [x] Math recomputed (layer sums, COGAS − EI = COGS, dual methods for pretax effect, after-tax × (1 − t), multi-year roll-forward)
- [x] Core demo not sidebar-only (Demo 9-7 / Review 9-7 path: liquidation effect, disclosure, interim replacement context)
- [x] LO + Concept on every item
- [x] MC ≤ 2 (two classification/computation items fitting LO 9-7)
- [x] Angles covered: initial_recognition_JE, subsequent_measurement_schedule (emphasis), period_end_adjusting_JE, disposal_maturity_or_settlement_JE, classification_presentation_or_disclosure, number_variant_twin
