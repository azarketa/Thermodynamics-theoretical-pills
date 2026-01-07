(sec_rankine_modifications)=
## Modified Rankine Cycles: Reheat and Regeneration

We have previously established that increasing the boiler pressure improves efficiency but introduces a dangerous side effect: **excessive moisture** (wetness) in the final stages of the turbine.

How can we utilize high pressures to gain efficiency without destroying turbine blades with water droplets? The text presents two primary pathways to solve this and further optimize the cycle: **Reheating** and **Regeneration**.

---

(subsec_rankine_reheated)=
### The reheated Rankine cycle

To handle the moisture problem caused by high pressure, one might initially suggest simply superheating the steam to *extremely* high temperatures before the turbine. While this raises the average heat-addition temperature, it is practically impossible due to **metallurgical limits** (materials melt or fail).

The practical engineering solution is the **reheat cycle**.

**How it works:**
Instead of expanding the steam in one continuous drop from boiler pressure to condenser pressure, the expansion is split into two (or more) stages:
1.  **High-Pressure expansion:** steam expands in a high-pressure turbine until it reaches an intermediate pressure.
2.  **Reheating:** the steam is sent back to the boiler (or a dedicated heat exchanger) where it is reheated at constant pressure, typically back to the inlet temperature of the first turbine.
3.  **Low-pressure expansion:** the reheated steam expands in a second turbine down to the condenser pressure.

**Thermodynamic impact:**
The inclusion of states 5 and 6 (in the $T-s$ diagram) shifts the expansion process to the right, significantly reducing the moisture content at the final exit.

The energy equations are adjusted to account for the two stages:

* **Total Heat Input ($q_{\text{in}}$):** includes the primary boiler heat plus the reheat energy.
    $$q_{\text{in}} = q_{\text{primary}} + q_{\text{reheat}} = (h_{\text{primary,out}} - h_{\text{pump,out}}) + (h_{\text{reheat,out}} - h_{\text{reheat,in}})$$

* **Net Turbine Work ($w_{\text{turb,out}}$):** sum of work from both turbines.
    $$w_{\text{turb,out}} = w_{\text{turb,I}} + w_{\text{turb,II}} = (h_{\text{inlet,I}} - h_{\text{outlet,I}}) + (h_{\text{inlet,II}} - h_{\text{outlet,II}})$$

:::{note}
**THE RULE OF DIMINISHING RETURNS**

A single reheat stage can improve cycle efficiency by **4% to 5%** by raising the average temperature of heat addition. One might think: why not add 10 reheat stages?

As the number of stages increases, the expansion and reheat processes approximate an **isothermal** (constant temperature) process at the maximum cycle temperature, which is ideal. However, the efficiency gain from a second stage is only half that of the first, and a third stage offers half that of the second.

**Practical Limit:** Because of this rapid diminishing return and the complexity of piping/pressure drops, power plants rarely exceed **two stages** of reheat, and double-reheat is usually reserved for supercritical plants.
:::

---

(subsec_rankine_regeneration_)=
### The regenerative Rankine cycle

If we examine the Ideal Rankine $T-s$ diagram, we see a flaw: the "feedwater" (the liquid leaving the pump) enters the boiler at a relatively low temperature. This means a significant portion of the heat transfer occurs just to bring this cold liquid up to boiling point. This **lowers the average temperature** of heat addition, dragging down efficiency.

**The solution: regeneration**
To fix this, we pre-heat the feedwater (the water leaving the pump) *before* it enters the main boiler.

While we could use a separate heat exchanger, the most practical method is to **bleed (extract) steam** from various points in the turbine. This extracted steam, which could have produced more work, is instead used to heat the feedwater in a device called a **Regenerator** or **Feedwater Heater (FWH)**.

**Benefits of regeneration:**
1.  **Increases thermal efficiency:** raises the average feedwater temperature entering the boiler.
2.  **Deaeration:** helps remove air from the water, preventing corrosion in the boiler.
3.  **Flow control:** reduces the volume of steam passing through the final, large blades of the low-pressure turbine (since some mass was extracted earlier).

There are two main types of Feedwater Heaters: **open** and **closed**.

---

(subsec_rankine_open_fwh)=
### Open feedwater heaters (O-FWH or direct mixing)

An **O-FWH** is essentially a mixing chamber.
* **Process:** extracted steam mixes directly with the cold feedwater from the pump.
* **Ideal outcome:** the mixture leaves the heater as **saturated liquid** at the heater's pressure.

**Analyzing Mass Flow:**
In regenerative cycles, the mass flow rate is not constant throughout the entire loop. We analyze based on **1 kg** of steam flowing through the boiler.
* Let $y$ be the fraction of steam extracted for the heater.
* Then $(1 - y)$ is the fraction that continues to the condenser.

**Energy Analysis (per unit mass of boiler steam):**
* **Heat Input:** $q_{\text{in}} = h_{\text{turb,in}} - h_{\text{boiler,in}}$
* **Heat Rejection:** $q_{\text{out}} = (1 - y)(h_{\text{turb,exit}} - h_{\text{cond,exit}})$
* **Turbine Work:**
    $$w_{\text{turb}} = (h_{\text{in}} - h_{\text{extract}}) + (1-y)(h_{\text{extract}} - h_{\text{exit}})$$
* **Pump Work:** We now have two pumps (one before the mixer, one after).

:::{tip}
**OPTIMIZING HEATERS**

Efficiency increases as we add more heaters. Large power plants may use up to **8 feedwater heaters**. The limit is economic: you stop adding heaters when the fuel savings no longer cover the cost of the equipment.
:::

---

(subsec_rankine_closed_fwh)=
### Closed feedwater heaters (C-FWH)

In a **C-FWH**, the streams **do not mix**. It functions like a standard shell-and-tube heat exchanger.
* **Process:** hot extracted steam flows over tubes carrying the cold feedwater.
* **Pressure:** because they don't mix, the two streams can be at different pressures.

**Ideal vs. Real:**
* *Ideal:* feedwater is heated to the exact exit temperature of the extracted steam.
* *Real:* feedwater leaves slightly cooler than the steam (due to finite heat transfer capability).

**Handling the Condensate:**
After the extracted steam condenses in the shell, it must go somewhere. It is usually routed through a **trap**—a throttling device that drops the pressure (keeping enthalpy constant) and dumps the fluid into a lower-pressure line or the condenser.

---

(subsec_rankine_fwh_comparison)=
### Comparison and real systems

| Feature | Open feedwater heater | Closed feedwater heater |
| :--- | :--- | :--- |
| **Complexity** | Simple, cheap. | Complex (internal tubing), expensive. |
| **Heat Transfer** | Excellent (direct mixing). | Less efficient (indirect). |
| **Pump Needs** | Requires a pump for each heater (pressure changes at mix). | No separate pumps needed (pressures are independent). |
| **Outcome** | Deaerates water effectively. | Requires separate deaeration. |

**Real-World Application:**

Modern steam power plants rarely choose just one. They typically use a **combination** of open and closed heaters to balance cost, efficiency, and deaeration needs.

---

(subsec_modified_rankine_closure)=
### Conceptual closure

* **Reheat cycles** solve the "wet steam" problem caused by high boiler pressures. By reheating steam between turbine stages, we keep the expansion line in the dry region and improve efficiency by approximating isothermal heat addition.
* **Regenerative cycles** solve the "cold feedwater" problem. By using extracted steam to pre-heat the water, we raise the average temperature of heat addition.
* **Mass fraction ($y$):** in regenerative cycles, math becomes dependent on mass fractions, as flow rates differ in different parts of the loop.
* **Open vs. closed:** open heaters mix fluids (efficient but need pumps); Closed heaters exchange heat through walls (simpler piping, less efficient heat transfer).
* **The modern standard:** a typical large-scale power plant combines **supercritical pressures**, **multiple reheat stages**, and **multiple feedwater heaters** (regenerators) to maximize thermal efficiency.
