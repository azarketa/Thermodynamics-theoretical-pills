(sec_other_configurations)=
## Other configurations: beyond the standard Rankine cycle

Having explored the ideal and real Rankine cycles, along with modifications like reheat and regeneration, we now turn to alternative configurations used in industry. These designs address specific needs, such as utilizing low-temperature heat sources or maximizing efficiency by combining different thermodynamic cycles.

---

(subsec_cogeneration)=
### Cogeneration

In the standard power cycles discussed so far, the sole objective is to convert heat into **work** (electricity), which is the most valuable form of energy. The remaining heat is rejected to the environment (lake, ocean, atmosphere) because its quality is considered too low to be useful.

However, many industries require massive inputs of heat energy, known as **process heat**.
* **Industries:** chemical, paper, oil refining, steel, food processing, and textiles.
* **Requirements:** steam typically between $5$ and $7\ \text{atm}$ and temperatures of $150\text{--}200 \ ^\circ\text{C}$.

**The thermodynamic problem:**
Traditionally, these industries burn fuel (coal, gas, oil) just to generate this low-temperature steam. This is highly inefficient because fuel combustion generates very high temperatures (high-quality energy), which is then immediately degraded to produce low-temperature steam (low-quality energy). Using high-quality potential to perform a low-quality task is a waste of exergy.

**The solution:**
Since these industries need both **electricity** and **process heat**, it makes sense to produce the electricity first and use the "waste" heat from that process to supply the factory floor.

**Definition:**
**Cogeneration** is the production of more than one form of useful energy (usually process heat + electricity) from a single energy source.

---

(subsec_combined_cycle)=
### Combined cycle (gas-steam)

The relentless pursuit of higher thermal efficiency led engineers to combine different cycles. The most important configuration is the **combined gas-steam cycle**, which places a gas power cycle on top of a steam power cycle.

**The synergy:**
* **Gas cycle (Brayton):** operates at very high temperatures. Modern gas turbines handle inlet temperatures up to $1425 \ ^\circ\text{C}$ (thanks to ceramic coatings and blade cooling). However, they exhaust gas at relatively high temperatures ($>500 \ ^\circ\text{C}$), representing wasted potential.
* **Steam cycle (Rankine):** limited by metallurgical constraints to roughly $620\ ^\circ\text{C}$.

**How it works:**
Instead of wasting the hot exhaust from the gas turbine, it is routed into a heat exchanger that acts as the **boiler** (evaporator) for a steam cycle located "beneath" it.
1.  **Top:** gas turbine produces work and hot exhaust.
2.  **Bottom:** steam cycle uses that exhaust to boil water and produce more work.

**Result:**
The combined cycle utilizes the high-temperature capabilities of gas turbines and the heat-recovery capabilities of steam cycles. Thermal efficiencies can exceed **$60\%$**, significantly higher than either cycle operating alone.

---

(subsec_working_fluid_characteristics)=
### Desirable characteristics of a working fluid

Water is the most common fluid because it is cheap and available, but it is not thermodynamically "ideal." An ideal working fluid would possess the following wish-list of properties:

1.  **High critical temperature:** this allows isothermal heat transfer at high temperatures (closer to Carnot efficiency).
2.  **Safe maximum pressure:** high temperatures should not require dangerously high pressures that stress materials.
3.  **Low triple point:** must be below the temperature of the surroundings to prevent the fluid from freezing during shutdowns or in cold condensers.
4.  **Manageable condenser pressure:** saturation pressure at ambient temperature should not be extremely low (vacuum). Pressures far below atmospheric allow air to leak into the system, which is detrimental.
5.  **High enthalpy of vaporization:** allows large heat transfer with low mass flow rates (smaller pumps/pipes).
6.  **"Inverted U" saturation dome:** the shape of the dome should encourage dry expansion, eliminating the need for reheat or excessive superheating to avoid moisture in the turbine.
7.  **Physical properties:** high thermal conductivity, non-toxic, chemically inert, and inexpensive.

---

(subsec_organic_rankine)=
### Organic Rankine cycle (ORC)

Since no single fluid is perfect, engineers select fluids based on the application. For **low-temperature heat sources** (waste industrial heat, geothermal, solar collectors), water is often poor because boiling it requires high temperatures or vacuum pressures.

**The solution:**
**Organic Rankine cycles** replace water with organic fluids (refrigerants, hydrocarbons).

**Advantages:**
* They boil at lower temperatures, making them perfect for recovering low-grade heat.
* **The saturation dome:** many organic fluids have a saturation dome shaped such that isentropic expansion naturally stays in the "dry" superheated region. This eliminates the risk of turbine blade erosion and removes the need for superheating.

---

(subsec_binary_cycle)=
### Binary cycle

A **binary cycle** uses two Rankine loops with different fluids: one for high temperatures and one for lower temperatures.
* **Top cycle:** uses a fluid with a very high critical temperature (e.g., mercury, sodium, potassium).
* **Bottom cycle:** uses water.
* **Interface:** the condenser of the top cycle serves as the boiler for the bottom cycle.

**The mercury example:**
Mercury has a critical temperature of $898 \ ^\circ\text{C}$ (excellent for high-temp heat absorption) and low critical pressure.
* *Why not use mercury alone?* At ambient temperatures ($32 \ ^\circ\text{C}$), mercury's saturation pressure is virtually zero ($0.07\ \text{Pa}$). Maintaining such a vacuum is impossible.
* *The fix:* use mercury only for the high-temperature loop. Condense it at roughly $237 \ ^\circ\text{C}$ (where its pressure is manageable), and use that heat to boil water for the bottom loop.

**Outcome:**
Binary cycles approximate the Carnot cycle more closely than a single water cycle, achieving efficiencies $>50\%$. However, due to the toxicity and cost of fluids like mercury, they have largely been superseded by **combined cycles** (gas-steam), which are safer and even more efficient.

---

(subsec_configurations_closure)=
### Conceptual closure

* **Cogeneration** stops the waste of low-grade heat by generating electricity *before* supplying process steam to industries, maximizing the total utility of the fuel.
* **Combined cycles** represent the current gold standard for efficiency ($>60\%$) by stacking a high-temp gas cycle on top of a medium-temp steam cycle.
* **Working fluids:** water is the standard, but **organic fluids** are superior for low-grade heat recovery (ORC), and liquid metals (mercury/sodium) were historically used in **binary cycles** to push temperature limits before gas turbines became dominant.
* **The goal:** every configuration—whether modifying the cycle layout or changing the fluid—aims to better match the heat source to the thermodynamic process, minimizing exergy destruction.
