(sec_rankine_ideal_detailed)=
## The Ideal Rankine Cycle: A Steady-Flow Analysis

In the **Ideal Rankine Cycle**, the analysis assumes a flow in a **steady-state regime**. We typically disregard any contribution from the fluid's kinetic and potential energy, as these are generally negligible compared to the thermal and work energy transfers occurring within the system.

Applying the **First Law of Thermodynamics**, we analyze the energy balance for each component. We proceed with the knowledge that:
1.  No work is performed in the heat exchangers (the evaporators and condensers).
2.  The turbomachinery (turbines and pumps) are assumed to be **isentropic** (perfectly reversible and adiabatic).

The energy variations for each process can be written as follows:

* **Pump ($q=0$):**
    The pump increases the pressure of the liquid.

    $$w_{\text{pump,in}} = h_2 - h_1 \ ,$$

    where $w$ represents work and $h$ represents enthalpy.

* **Evaporator ($w=0$):**
    Heat is added to the fluid at constant pressure.

    $$q_{\text{in}} = h_3 - h_2$$

* **Turbine ($q=0$):**
    The fluid expands, producing work.

    $$w_{\text{turb,out}} = h_3 - h_4$$

* **Condenser ($w=0$):**
    Heat is rejected from the fluid to the surroundings.

    $$q_{\text{out}} = h_4 - h_1$$

The **thermal efficiency** ($\eta_{\text{th}}$) of the cycle maintains its standard thermodynamic definition:

$$\eta_{\text{th}} = \frac{w_{\text{net}}}{q_{\text{in}}} = 1 - \frac{q_{\text{out}}}{q_{\text{in}}}$$

---

(subsec_rankine_real_losses)=
### The Real Rankine Cycle: Understanding Irreversibilities

The **Real Rankine Cycle** differs from the ideal model due to **irreversibilities** that occur in its various components. While the ideal cycle is a useful theoretical benchmark, real-world engineering must account for losses. The two primary sources of these irreversibilities are **fluid friction** and **heat loss** to the environment.

1. Fluid friction (pressure drops):

    Friction causes the pressure of the fluid to drop as it moves through the evaporator, the condenser, and the piping connecting these components (known as **head loss**).
    * **The Consequence:** The steam leaves the evaporator at a pressure slightly lower than the design pressure. It then enters the turbine at an even lower pressure due to friction in the connecting pipes.
    * **The Compensation:** While pressure drops in the condenser are usually small, the overall system losses mean the water must be pumped to a **relatively higher pressure** than required in the ideal case. This necessitates larger pumps and greater work input ($w_{\text{pump,in}}$).

2. Heat losses:

    As the steam travels through components and piping, heat is inevitably transferred to the cooler surroundings.

    * **The Consequence:** To maintain the same level of net work output, more heat must be transferred to the steam in the evaporator to compensate for these losses.
    * **The Result:** Since $q_{\text{in}}$ increases to produce the same work, the thermal efficiency of the cycle decreases.

3. Other real-world constraints:

    Several other factors cause the real cycle to deviate from the ideal:

    * **Subcooling:** In almost all condensers, the liquid is subcooled (cooled below saturation temperature) to prevent **cavitation**—the rapid formation and collapse of vapor bubbles in the pump's low-pressure suction line, which can cause structural damage.
    * **Mechanical Losses:** Bearings and seals are subject to friction.
    * **Leakage:** Steam may leak out of the cycle, and air may leak into the condenser (breaking the vacuum).
    * **Auxiliary Power:** The energy consumed by support devices, such as fans that provide air to the combustion bank, represents a loss that should be computed in the final efficiency balance.

:::{important}
**PUMP AND TURBINE EFFICIENCIES**

The deviations in the pump and turbine are particularly relevant. Real pumps require more energy input, and real turbines produce less work output. We account for this non-isentropic behavior using **isentropic efficiencies**:

$$\eta_{\text{pump}} = \frac{w_s}{w_a} = \frac{h_{2s} - h_1}{h_{2a} - h_1}$$

$$\eta_{\text{turb}} = \frac{w_a}{w_s} = \frac{h_3 - h_{4a}}{h_3 - h_{4s}}$$

Here, states **$2a$** and **$4a$** correspond to the **actual** processes, while **$2s$** and **$4s$** correspond to the **ideal** (isentropic) processes.
:::

---

(subsec_rankine_efficiency_methods)=
### Methods to Improve Rankine Cycle Efficiency

Steam power cycles are responsible for a vast portion of global electricity production. Consequently, any improvement in thermal efficiency translates to significant savings in fuel (nuclear, fossil, or otherwise).

The fundamental concept behind all modifications to the Rankine cycle is the same: **Increase the thermal efficiency**. To do this, we must obey one thermodynamic "golden rule":
* Increase the **average temperature** at which heat is added to the fluid ($T_{\text{avg,in}}$).
* Or decrease the **average temperature** at which heat is rejected ($T_{\text{avg,out}}$).

In practice, there are three main ways to achieve this:

1. Decreasing the condenser pressure:

    This method focuses on the "heat rejection" side of the equation.
   
    * **The Mechanism:** Inside the condenser, steam exists as a two-phase mixture. Its temperature is locked to its pressure (saturation state). Therefore, lowering the operating pressure automatically lowers the temperature at which heat is rejected.
    * **The Effect:** This increases the **net work** (represented by the area enclosed in the $T-s$ diagram). Although the heat input requirements increase slightly, the overall efficiency rises.
    * **Practical Constraints:**
        * **Vacuum Limits:** Condensers usually operate below atmospheric pressure. The lower limit is dictated by the temperature of the cooling medium (river, lake, or ambient air).
        * **Air Infiltration:** Extremely low pressures increase the risk of air leaking into the condenser.
        * **Moisture Content:** Lowering pressure shifts the expansion line to the left. This increases the moisture (droplets) at the turbine exit (state $4'$).

:::{note}
**THE EROSION PROBLEM**

The presence of significant moisture at the turbine exhaust is damaging. Water droplets erode the turbine blades and reduce their aerodynamic performance. This physical limitation prevents us from lowering the condenser pressure indefinitely.
:::

2. Superheating the steam:

    This method focuses on the "heat addition" side.

    * **The Mechanism:** We continue to heat the steam after it has vaporized, raising its temperature well above the saturation point.
    * **The Effect:** This raises the average temperature of heat addition without changing the system pressure. Both net work and heat input increase, but the efficiency improves.
    * **Additional Benefit:** Superheating moves the expansion line to the right, significantly **decreasing the moisture content** at the turbine exit, which protects the blades.
    * **Practical Constraints:** We are limited by metallurgy. The maximum temperature current turbine materials can withstand is approximately **$620 \ ^\circ\text{C}$**. Exceeding this requires advanced ceramics or new alloy innovations.

3. Increasing the evaporator pressure:

    This method also targets the "heat addition" side.

    * **The Mechanism:** Increasing pressure raises the boiling temperature of water.
    * **The Effect:** This automatically raises the average temperature of heat addition, boosting thermal efficiency.
    * **The Side Effect:** As seen in $T\!-\!s$ diagrams, higher pressure shifts the cycle to the left. This **increases the moisture content** at the turbine exit.
    * **The Solution:** Because of this moisture issue, high-pressure cycles almost always require **reheating** the steam (extracting it, heating it again, and re-expanding it) to keep the turbine blades safe.

---

(subsec_rankine_supercritical)=
### The Supercritical Rankine Cycle

The drive for efficiency has led to a steady increase in evaporator operating pressures. Many modern power plants now operate at **supercritical pressures** (often near **$30 \ \text{MPa}$**).

In these cycles:
* There is no distinct phase change process (no boiling bubbles).
* The fluid transitions continuously from a liquid-like density to a gas-like density.
* Thermal efficiencies can reach approximately **$40\%$**.

---

(subsec_rankine_closure)=
### Conceptual closure

* **Ideal vs. Real:** The Ideal Rankine cycle is calculated using simple enthalpy differences assuming isentropic components. The Real cycle must account for **friction** (pressure drops) and **heat losses**, utilizing isentropic efficiencies to quantify component performance.
* **The Goal:** All modifications aim to increase thermal efficiency to save fuel resources.
* **The Levers:** Efficiency is improved by widening the temperature gap:
    1.  **Lowering condenser pressure** (limited by blade erosion from moisture).
    2.  **Superheating steam** (limited by material melting points, approx $620 \ ^\circ\text{C}$).
    3.  **Increasing boiler pressure** (limited by moisture, often requiring reheat).
* **State of the Art:** Supercritical cycles operate at very high pressures ($>22 \ \text{MPa}$) to maximize the average temperature of heat addition, achieving superior efficiency.
