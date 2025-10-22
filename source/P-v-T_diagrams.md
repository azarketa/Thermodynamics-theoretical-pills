(sec_pvt_diagrams)=
## $P-v-T$ Diagrams

Thermodynamic states of a pure substance can be described by the **triad of variables** $P$, $v$, and $T$.
These quantities are linked by the {ref}`**state relation** <eq_general_state_equation>`, which defines the thermodynamic surface of the substance in a three-dimensional space.
Understanding how this surface behaves is essential for visualizing **phase changes** and **process paths** in real systems.

Mathematically, a single-variable function $y=f(x)$ is represented as a curve on the $x$–$y$ plane.
If, instead, the function depends on two independent variables, $z=f(x, y)$, its graphical representation is a **surface** in three-dimensional space.
In the same way, the $P-v$-T relation defines a surface: each point on this surface represents an equilibrium state of the substance.

A **quasi-static process**—a slow, reversible evolution between equilibrium states—traces a continuous **curve** along this surface.
The shape of this surface, and its projections on coordinate planes, provides insight into phase behavior.

---

(subsec_tv_projection)=
### The $T-v$ Projection

Let us examine a simple and familiar system: a **piston–cylinder** filled with liquid water at atmospheric pressure ($P \approx 101 \ \text{kPa}$) and at an initial temperature of $20^{\circ}\text{C}$.
The system is slowly heated by a thermal source such as a small burner.

1. **Heating the liquid:**
   As heat is supplied, the temperature of the water increases. The piston remains nearly still, showing that the liquid’s **specific volume** varies very little with temperature.

2. **Approaching saturation:**
   When the temperature reaches $100^{\circ}\text{C}$ (at this pressure), the liquid becomes **saturated**. Any further addition of heat now initiates a **phase change**—the formation of vapor.
   The water at this point is called **saturated liquid**, while the earlier state (below $100^{\circ}\text{C}$) is **subcooled** or **compressed liquid**.

3. **Phase change:**
   As the vapor forms, the piston begins to move upward. The temperature and pressure remain constant during the change, but the **specific volume** increases sharply.
   During this process, both liquid and vapor coexist — this is the **saturated liquid–vapor mixture**.
   Each intermediate state corresponds to a given fraction of vaporized mass, quantified by the **quality** $x$, defined later in this section.

4. **Saturated vapor:**
   When the last droplet of liquid evaporates, the system consists entirely of **saturated vapor**.
   Removing heat from this state would reverse the process, leading to **condensation**.

5. **Superheated vapor:**
   If heating continues beyond the saturated vapor state, the temperature rises above the saturation temperature.
   The vapor expands, the piston ascends further, and the gas approximately follows {ref}`the ideal-gas law <eq_ideal_gas_specific_form>`. The fluid in this region is the **superheated vapor**.

:::{admonition} Important: Key observations in the $T-v$ diagram
:class: warning

* The **specific volume** of liquid water remains nearly constant until boiling begins.
* The **phase change** appears as a **horizontal line** (constant $T$ and $P$).
* The **saturated vapor** region follows gas-like behavior, where $v$ increases markedly with $T$.
:::

---

(subsec_completing_tv_projection)=
### Completing the $T-v$ Projection

Repeating the experiment at different pressures reveals that:

* At **higher pressures**, the **phase change** occurs at **higher temperatures**.
* The difference in specific volume between the liquid and vapor phases **decreases** as pressure increases.

This leads to two major conclusions:

1. The **saturation temperature**, $T_{\text{sat}}$, **depends on pressure**.

   Higher pressures correspond to higher saturation temperatures.

2. The **volume change** during vaporization becomes smaller at higher $P$ and $T$, eventually vanishing at a unique point known as the **critical point**.

    At the **critical point**, the saturated liquid and saturated vapor states coincide.
    Beyond this point, no clear distinction exists between liquid and gas — the substance becomes a **supercritical fluid**.
    
    For water:

    (eq_critical_magnitudes_water)=
    $$
    T_{\text{cr}} = 373.95^{\circ}\text{C}, \quad P_{\text{cr}} = 22.06\text{MPa}
    $$
    
    Supercritical fluids exhibit properties intermediate between those of gases and liquids and are used in specialized applications such as solvent extraction and supercritical drying.

:::{admonition} Note: Pressure cookers and high-altitude boiling
:class: note, dropdown

* In a **pressure cooker**, the internal pressure exceeds atmospheric pressure, allowing water to remain liquid above $100,^{\circ}\text{C}$ and thus cook food faster.
* On the other hand, atop **Mount Everest**, where $P_{\text{atm}} \approx 34,\text{kPa}$, water boils at about $86,^{\circ}\text{C}$.
* At roughly $19{,}000,\text{m}$ (the **Armstrong line**), where the atmospheric pressure equals the vapor pressure of water at body temperature ($36,^{\circ}\text{C}$), the human body’s liquids would begin to boil without pressurization.

:::

---

(subsec_simplified_tv_projection)=
### The Simplified $T-v$ Diagram

If we plot all saturation points for both liquid and vapor and connect them, we obtain the **saturation line**, which forms an **inverted bell**.
The $T-v$ diagram can then be divided into distinct regions:

* **Inside the bell:** the **two-phase region** (liquid–vapor mixture).
* **To the left:** the **subcooled liquid** region.
* **To the right:** the **superheated vapor** region.
* **Above the bell:** the **supercritical region**.

This simplified $T-v$ diagram is a cornerstone of thermodynamic visualization — a compact map showing how matter transitions between its main phases.

---

(subsec_pv_projection)=
### The $P-v$ Projection

To complement the $T-v$ view, consider the same piston–cylinder system but now **maintain constant temperature** while varying pressure.

By applying or removing weights on the piston, the external pressure is changed, while heat exchange with the thermal bath keeps the temperature fixed.
The resulting **P-v diagram** shows similar features to the $T-v$ projection:

* As pressure decreases at constant $T$, the liquid begins to vaporize once $P_{\text{sat}}$ is reached.
* At higher pressures, condensation occurs.
* Both transformations trace a **horizontal phase-change line** on the $P-v$ diagram.

The bell-shaped envelope again separates the single-phase regions from the two-phase mixture.

:::{admonition} Note: Comparison between $T-v$ and $P-v$ diagrams
:class: note, dropdown

* In the **liquid region**, specific volume varies little with $T$ or $P$.
* In the **vapor region**, $P$ is inversely proportional to $v$ (Boyle–Mariotte law).
* Phase change appears as a horizontal line in both projections.
:::

---

(subsec_extending_pv_projection)=
### Extending the $P-v$ Projection

When extended to include the solid phase, the $P-v$ diagram displays additional features:

* **Substances that contract on freezing** (most materials) show a vertical solid–liquid transition line, since $v$ decreases sharply upon solidification.
* **Substances that expand on freezing** (like water) exhibit a slanted line: the solid phase has slightly greater specific volume than the liquid.

At still lower pressures, other transitions appear:

* The **triple point**, where solid, liquid, and vapor coexist in equilibrium.
  For water:

  (eq_triple_point_values_water)=
  $$
  T_{\text{tr}} = 0.01{^\circ}\text{C}, \quad P_{\text{tr}} = 0.6117 \ \text{kPa}
  $$

* The **sublimation process**, a direct transition from solid to vapor (or vice versa) at pressures below $P_{\text{tr}}$.

---

(subsec_pt_projection)=

### The $P-T$ Projection (Phase Diagram)

The **$P-T$ diagram**, or **phase diagram**, presents the phase boundaries more compactly.
It displays the three fundamental lines:

* **Sublimation line** (solid–vapor equilibrium),
* **Fusion line** (solid–liquid equilibrium), and
* **Vaporization line** (liquid–vapor equilibrium).

These three lines converge at the **triple point**, which appears as a single point on this projection.

The slope of the **fusion line** reveals whether a substance **expands** or **contracts** upon freezing:

* Positive slope: volume decreases upon solidification (most substances).
* Negative slope: volume increases (water).

:::{admonition} Note: Interpretation of process lines
:class: note, dropdown

* **Vertical lines** correspond to isothermal processes (constant $T$).
* **Horizontal lines** correspond to isobaric processes (constant $P$).
* For example:

  * Line I′: isothermal sublimation,
  * Line I″: isothermal fusion,
  * Line I‴: isothermal evaporation,
  * Line I: isobaric sublimation,
  * Line II: isobaric fusion,
  * Line III: isobaric evaporation.
:::

---

(subsec_evaporation_process)=
### The Evaporation Process and Vapor Quality

Evaporation plays a central role in many engineering systems — from **boilers** and **heat exchangers** to **thermal power plants**.
During evaporation, the liquid–vapor mixture is often modeled as **homogeneous**, which greatly simplifies analysis.

The degree of vaporization is quantified by the **vapor quality**, $x$, defined as:

(eq_quality_definition)=
$$
x = \frac{m_{\text{vapor}}}{m_{\text{liquid}} + m_{\text{vapor}}}
$$

This intensive parameter ranges from $x=0$ (saturated liquid) to $x=1$ (saturated vapor).
In the two-phase region, all other properties can be expressed as mass-weighted averages of their saturated-liquid and saturated-vapor values.

---

(subsec_error_tv_diagram)=
### Departure from Ideal-Gas Behavior

In the **$T-v$ diagram**, the deviation of real vapor behavior from the ideal gas law increases as we approach the **triple point**.
At low pressures and high temperatures, gases behave nearly ideally because their specific volume is large, making intermolecular forces negligible.
However, near saturation or condensation conditions, deviations become significant, and the use of **real-gas models** becomes essential.

:::{admonition} Important: Region of validity of the ideal-gas model
:class: warning
The **ideal-gas assumption** holds only when the distance between molecules is large (low $P$, high $T$).
Close to phase boundaries, intermolecular attractions dominate and the ideal-gas model fails.
This is the regime where **compressibility factors** and **cubic equations of state** become necessary.
:::

---

(subsec_conceptual_closure_pvt)=
### Conceptual Closure

* The **$P-v-T$ surface** represents the complete state space of a substance.
* **Projections** on coordinate planes ($T-v$, $P-v$, $P-T$) reveal the mechanisms of phase change and critical behavior.
* The **saturation line** forms an inverted bell that delineates subcooled, two-phase, and superheated regions.
* **Critical and triple points** define the limits of coexistence among phases.
* Understanding these diagrams is fundamental for interpreting thermodynamic cycles and energy conversion processes.
