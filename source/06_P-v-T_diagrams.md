(sec_pvt_diagrams)=
## $p-v-T$ diagrams

Thermodynamic states of a pure substance can be described by the **triad of variables** $p$, $v$, and $T$.
These quantities are linked by the {ref}`state relation <eq_general_state_equation>`, which defines the thermodynamic surface of the substance in a three-dimensional space.
Understanding how this surface behaves is essential for visualizing **phase changes** and **process paths** in real systems.

Mathematically, a single-variable function $y=f(x)$ is represented as a curve on the $x$–$y$ plane.
If, instead, the function depends on two independent variables, $z=f(x, y)$, its graphical representation is a **surface** in three-dimensional space.
In the same way, the $p-v$-T relation defines a surface: each point on this surface represents an equilibrium state of the substance.

A **quasi-static process**—a slow, reversible evolution between equilibrium states—traces a continuous **curve** along this surface.
The shape of this surface, and its projections on coordinate planes, provides insight into phase behavior.

---

(subsec_tv_projection)=
### The $T-v$ projection

Let us examine a simple and familiar system: a **piston–cylinder** filled with liquid water at atmospheric pressure ($p \approx 101 \ \text{kPa}$) and at an initial temperature of $20 \ ^{\circ}\text{C}$.
The system is slowly heated by a thermal source such as a small burner.

1. **Heating the liquid:**

   As heat is supplied, the temperature of the water increases. The piston remains nearly still, showing that the liquid’s **specific volume** varies very little with temperature.

2. **Approaching saturation:**

    When the temperature reaches $100 \ ^{\circ}\text{C}$ (at this pressure), the liquid becomes **saturated**. Any further addition of heat now initiates a **phase change**—the formation of vapor.
   The water at this point is called **saturated liquid**, while the earlier state (below $100 \ ^{\circ}\text{C}$) is **subcooled** or **compressed liquid**.

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

:::{important}

**KEY OBSERVATIONS IN THE $T-v$ DIAGRAM**

* The **specific volume** of liquid water remains nearly constant until boiling begins.
* The **phase change** appears as a **horizontal line** (constant $T$ and $p$).
* The **saturated vapor** region follows gas-like behavior, where $v$ increases markedly with $T$.
:::

---

(subsec_completing_tv_projection)=
### Completing the $T-v$ projection

Repeating the experiment at different pressures reveals that:

* At **higher pressures**, the **phase change** occurs at **higher temperatures**.
* The difference in specific volume between the liquid and vapor phases **decreases** as pressure increases.

This leads to two major conclusions:

1. The **saturation temperature**, $T_{\text{sat}}$, **depends on pressure**.

   Higher pressures correspond to higher saturation temperatures.

2. The **volume change** during vaporization becomes smaller at higher $p$ and $T$, eventually vanishing at a unique point known as the **critical point**.

    At the **critical point**, the saturated liquid and saturated vapor states coincide.
    Beyond this point, no clear distinction exists between liquid and gas — the substance becomes a **supercritical fluid**.
    
    For water:

    (eq_critical_magnitudes_water)=
    $$
    T_{\text{cr}} = 373.95 \ ^{\circ}\text{C}, \quad p_{\text{cr}} = 22.06\text{MPa}
    $$
    
    Supercritical fluids exhibit properties intermediate between those of gases and liquids and are used in specialized applications such as solvent extraction and supercritical drying.

:::{note}

**PRESSURE COOKERS AND HIGH-ALTITUDE BOILING**

* In a **pressure cooker**, the internal pressure exceeds atmospheric pressure, allowing water to remain liquid above $100 \ ^{\circ}\text{C}$ and thus cook food faster.
* On the other hand, atop **Mount Everest**, where $p_{\text{atm}} \approx 34 \ \text{kPa}$, water boils at about $86 \ ^{\circ}\text{C}$.
* At roughly $19,000 \ \text{m}$ (the **Armstrong line**), where the atmospheric pressure equals the vapor pressure of water at body temperature ($36 \ ^{\circ}\text{C}$), the human body’s liquids would begin to boil without pressurization.

:::

---

(subsec_simplified_tv_projection)=
### The simplified $T-v$ projection

If we plot all saturation points for both liquid and vapor and connect them, we obtain the **saturation line**, which forms an **inverted bell**.
The $T-v$ diagram can then be divided into distinct regions:

* **Inside the bell:** the **two-phase region** (liquid–vapor mixture).
* **To the left:** the **subcooled liquid** region.
* **To the right:** the **superheated vapor** region.
* **Above the bell:** the **supercritical region**.

This simplified $T-v$ diagram is a cornerstone of thermodynamic visualization — a compact map showing how matter transitions between its main phases.

---

(subsec_pv_projection)=
### The $p-v$ projection

To complement the $T-v$ view, consider the same piston–cylinder system but now **maintain constant temperature** while varying pressure.

By applying or removing weights on the piston, the external pressure is changed, while heat exchange with the thermal bath keeps the temperature fixed.
The resulting **$p-v$ diagram** shows similar features to the $T-v$ projection:

* As pressure decreases at constant $T$, the liquid begins to vaporize once $p_{\text{sat}}$ is reached.
* At higher pressures, condensation occurs.
* Both transformations trace a **horizontal phase-change line** on the $p-v$ diagram.

The bell-shaped envelope again separates the single-phase regions from the two-phase mixture.

:::{note}

**COMPARISON BETWEEN $T-v$ AND $p-v$ DIAGRAMS**

* In the **liquid region**, specific volume varies little with $T$ or $p$.
* In the **vapor region**, $p$ is inversely proportional to $v$ (Boyle–Mariotte law).
* Phase change appears as a horizontal line in both projections.
:::

---

(subsec_extending_pv_projection)=
### Extending the $p-v$ projection

When extended to include the solid phase, the $p-v$ diagram displays additional features:

* **Substances that contract on freezing** (most materials) show a vertical solid–liquid transition line, since $v$ decreases sharply upon solidification.
* **Substances that expand on freezing** (like water) exhibit a slanted line: the solid phase has slightly greater specific volume than the liquid.

At still lower pressures, other transitions appear:

* The **triple point**, where solid, liquid, and vapor coexist in equilibrium.
  For water:

  (eq_triple_point_values_water)=
  $$
  T_{\text{tr}} = 0.01{\ ^\circ}\text{C}, \quad p_{\text{tr}} = 0.6117 \ \text{kPa}
  $$

* The **sublimation process**, a direct transition from solid to vapor (or vice versa) at pressures below $p_{\text{tr}}$.

---

(subsec_pt_projection)=
### The $p-T$ projection (phase diagram)

The **$p-T$ diagram**, or **phase diagram**, presents the phase boundaries more compactly.
It displays the three fundamental lines:

* **Sublimation line** (solid–vapor equilibrium),
* **Fusion line** (solid–liquid equilibrium), and
* **Vaporization line** (liquid–vapor equilibrium).

These three lines converge at the **triple point**, which appears as a single point on this projection.

The slope of the **fusion line** reveals whether a substance **expands** or **contracts** upon freezing:

* Positive slope: volume decreases upon solidification (most substances).
* Negative slope: volume increases (water).

:::{note}

**INTERPRETATION OF PROCESS LINES**

* **Vertical lines** correspond to isothermal processes (constant $T$).
* **Horizontal lines** correspond to isobaric processes (constant $p$).
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
### The evaporation process and vapor quality

Evaporation plays a central role in many engineering systems — from **boilers** and **heat exchangers** to **thermal power plants**.
During evaporation, the liquid–vapor mixture is often modeled as **homogeneous**, which greatly simplifies analysis.

The degree of vaporization is quantified by the **vapor quality**, $x$, defined as:

(eq_quality_definition)=
$$
x = \frac{m_{\text{vapor}}}{m_{\text{liquid}} + m_{\text{vapor}}}
$$

This intensive parameter ranges from $x=0$ (saturated liquid) to $x=1$ (saturated vapor).
In the two-phase region, all other properties can be expressed as mass-weighted averages of their saturated-liquid and saturated-vapor values.

::::{important}

**WORKED EXAMPLE — LOCATING WATER STATES ON THE $p–v–T$ DIAGRAM**

**Problem statement**

For each thermodynamic state of **water**, determine the requested properties by locating the state on the $p–v–T$ surface using tabulated data{cite}`2015Cengel`:

1. $p=150~\mathrm{bar}$, $T=693~\mathrm{K}$ ($=420\ ^\circ\mathrm{C}$). Find $v$.
2. $p=0.5~\mathrm{bar}$, $u=340.49~\text{kJ}/\text{kg}$. Find $v$ and $T$.
3. $p=6~\mathrm{bar}$, $x=0.65$. Find $v$ and $T$.
4. $p=25~\mathrm{bar}$, $v=0.095~\text{m}^{3}/\text{kg}$. Find $T$.

---

**Synthesis**

| Case | Given                                                | To find  |
| :--- | :--------------------------------------------------- | :------- |
| 1  | $p=150~\mathrm{bar}$, $T=420\ ^\circ\mathrm{C}$        | $v$      |
| 2  | $p=0.5~\mathrm{bar}$, $u=340.49~\text{kJ}/\text{kg}$ | $v$, $T$ |
| 3  | $p=6~\mathrm{bar}$, $x=0.65$                         | $v$, $T$ |
| 4  | $p=25~\mathrm{bar}$, $v=0.095~\text{m}^{3}/\text{kg}$  | $T$      |

---

**Solution strategy**

1. **State check**: at a given $p$ or $T$, compare with saturation properties $(T_\text{sat}(p)$, $p_\text{sat}(T)$; $v_f,v_g$; $u_f,u_g$) to decide **region**: subcooled/compressed liquid, saturated mixture, or superheated vapor.
2. **Mixture**: if saturated, $T=T_\text{sat}(p)$ and $v=v_f+x(v_g-v_f)$, $u=u_f+x(u_g-u_f)$.
3. **Superheated / subcooled**: interpolate in the appropriate superheated/compressed tables:

   $$y(T)=y(T_1)+\dfrac{y_2-y_1}{T_2-T_1}(T-T_1)\quad\text{at fixed }p.$$

---

**Calculations**

1. **$p=150~\mathrm{bar},\ T=420\ ^\circ\mathrm{C}$:**

   * **Check state:**

        $T_\text{sat}(150~\mathrm{bar})\approx 349\ ^\circ\mathrm{C}<420\ ^\circ\mathrm{C}\Rightarrow \boxed{\text{superheated vapor}}$ .

   * **Interpolate:**

        * At $p=150~\mathrm{bar}$ between:
  
            * $T_1 = 400\ ^\circ\mathrm{C}$ ,
            * $v_1 = 0.015671 \ \text{m}^{3}/\text{kg}$ ,
            * $T_2=450\ ^\circ\mathrm{C}$ ,
            * $v_1 = 0.01847 \ \text{m}^{3}/\text{kg}$.

        $$
        v(T)=v_1+\frac{v_2-v_1}{T_2-T_1}(T-T_1)
        \quad\Rightarrow\quad
        v=\boxed{0.01679~\text{m}^{3}/\text{kg}} \ (16.79~\text{dm}^{3}/\text{kg}).
        $$

2. **$p=0.5~\mathrm{bar},\ u=340.49~\text{kJ}/\text{kg}$:**

   * **Check state:**

     $T_\text{sat}(0.5~\mathrm{bar})=81.32\ ^\circ\mathrm{C}$ and $u_f\simeq340.49~\text{kJ}/\text{kg}$.
     Since $u\approx u_f \Rightarrow \boxed{\text{saturated liquid}}$.

   * **Evaluate:**

     $$T=\boxed{81.32\ ^\circ\mathrm{C}} \ ,\quad v=v_f(p=0.5~\mathrm{bar})=\boxed{0.00103~\text{m}^3/\text{kg}}\ (1.03~\text{dm}^{3}/\text{kg}).$$

3. **$p=6~\mathrm{bar},\ x=0.65$**

   * **Check state:**

     Given quality $x$, the state is on the saturation dome $\Rightarrow \boxed{\text{saturated mixture}}$ :
  
    $$\text{saturated mixture} \implies T=T_\text{sat}(6~\mathrm{bar})=\boxed{158.83\ ^\circ\mathrm{C}} \ .$$

   * **Mixture relation:**

     Using $v=v_f+x,(v_g-v_f)$ at $p=6~\mathrm{bar}$ with $v_f=0.001091$ and $v_g=0.3156\ \text{m}^{3}/\text{kg}$,
   
     $$
     v=0.001091+0.65(0.3156-0.001091) = \boxed{0.20553~\text{m}^{3}/\text{kg}}\ (205.53~\text{dm}^{3}/\text{kg}).
     $$

4. **$p=25~\mathrm{bar} \ v=0.095~\text{m}^{3}/\text{kg}$**

   * **Check state:**

     At $25~\mathrm{bar}$, $v_g(p)\approx0.0795~\text{m}^{3}/\text{kg}$.
     Since $v=0.095>v_g \Rightarrow \boxed{\text{superheated vapor}}$ .

   * **Interpolate (at fixed $p=25~\mathrm{bar}$):**
  
        * At $p=25~\mathrm{bar}$ between:
  
            * $T_1 = 250\ ^\circ\mathrm{C}$ ,
            * $v_1 = 0.08705 \ \text{m}^{3}/\text{kg}$ ,
            * $T_2=300\ ^\circ\mathrm{C}$ ,
            * $v_1 = 0.09894 \ \text{m}^{3}/\text{kg}$.     
  
        $$
        T=T_1+\frac{v-v_1}{v_2-v_1}(T_2-T_1) \Rightarrow T = \boxed{283.43\ ^\circ\mathrm{C}}.
        $$

---

**Summary and insights**

|   Case  | Phase Region      | Results                                                                                                |
| :-----: | :---------------- | :----------------------------------------------------------------------------------------------------- |
| 1 | Superheated vapor | $v = 0.01679~\text{m}^{3}/\text{kg}\ (16.79~\text{dm}^{3}/\text{kg})$                                  |
| 2 | Saturated liquid  | $T = 81.32~^\circ\text{C},\quad v = 0.00103~\text{m}^{3}/\text{kg}\ (1.03~\text{dm}^{3}/\text{kg})$    |
| 3 | Saturated mixture | $T = 158.83~^\circ\text{C},\quad v = 0.20553~\text{m}^{3}/\text{kg}\ (205.53~\text{dm}^{3}/\text{kg})$ |
| 4 | Superheated vapor | $T = 283.43~^\circ\text{C}$                                                                            |

* Comparing given states with **saturation properties** allows immediate phase identification.
* Mixture states (case c) lie **inside the dome**; subcooled and superheated states (a, b, d) lie **outside** it.
* Linear interpolation across tabulated data provides accurate intermediate values for both $v$ and $T$.

---

:::{tip}
 
**READING THE $p-v-T$ SURFACE**

* Fixing $p$ and $T$ (case a) selects an **isobar–isotherm** point; comparing $T$ with $T_\text{sat}(p)$ tells whether the state lies **inside** (mixture) or **outside** (superheated/subcooled) the dome.
* Fixing $p$ and $u$ (case b) near $u_f$ pins the state to the **saturated liquid** line at $T_\text{sat}(p)$, so $v=v_f(p)$.
* Specifying $p$ and $x$ (case c) places the state **on the dome** at $T_\text{sat}(p)$, with $v$ a linear blend of $v_f$ and $v_g$.
* Fixing $p$ and a large $v$ (case d) typically means **superheated vapor**; interpolate in superheated tables to obtain $T$.
  Together, these patterns show how simple state checks against saturation properties let you navigate the $p$–$v$–$T$ surface quickly and accurately.
  :::

::::

---

(subsec_error_tv_diagram)=
### Departure from ideal gas behavior

In the **$T-v$ diagram**, the deviation of real vapor behavior from the ideal gas law increases as we approach the **triple point**.
At low pressures and high temperatures, gases behave nearly ideally because their specific volume is large, making intermolecular forces negligible.
However, near saturation or condensation conditions, deviations become significant, and the use of **real-gas models** becomes essential.

:::{warning} Important: region of validity of the ideal gas model
The **ideal-gas assumption** holds only when the distance between molecules is large (low $p$, high $T$).
Close to phase boundaries, intermolecular attractions dominate and the ideal-gas model fails.
This is the regime where **compressibility factors** and **cubic equations of state** become necessary.
:::

---

(subsec_conceptual_closure_pvt)=
### Conceptual closure

* The **$p-v-T$ surface** represents the complete state space of a substance.
* **Projections** on coordinate planes ($T-v$, $p-v$, $p-T$) reveal the mechanisms of phase change and critical behavior.
* The **saturation line** forms an inverted bell that delineates subcooled, two-phase, and superheated regions.
* **Critical and triple points** define the limits of coexistence among phases.
* Understanding these diagrams is fundamental for interpreting thermodynamic cycles and energy conversion processes.
