(sec_canonical_open_systems)=
## Canonical open systems

The canonical open systems presented below are standard **steady-flow devices** in which the **$1^{\text{st}}$ law for open systems** — {ref}`in its specific, enthalpy-based form <eq_1st_law_open_systems_enthalpy_terms_single_inlet_outlet>` — applies directly:

Each of these systems performs a characteristic type of **energy conversion** or **transfer** between heat, work, and mass flow, depending on the physical configuration and process conditions.

---

(subsec_turbines_compressors)=
### Turbines and compressors

**Turbines** and **compressors** are mechanical devices in which **enthalpy** and **shaft work** are interconverted.

* In a **turbine**, the fluid expands, its enthalpy decreases, and part of this energy is extracted as **shaft power**.
* In a **compressor**, the opposite occurs: external work is supplied to the system to increase the fluid enthalpy (and thus pressure and temperature).

In both devices, **heat transfer** to the surroundings is small compared to the mechanical energy exchange, and **changes in kinetic and potential energies** are negligible.

Starting from the steady-flow expression of the $1^{\text{st}}$ law under these assumptions ($q \simeq 0$, $\Delta c^2 \simeq 0$, $\Delta z \simeq 0$):

(eq_turbine_compressor)=
$$
0 - w_{\text{shaft}} = (h_2 - h_1)
\quad\Longrightarrow\quad
\boxed{h_2 - h_1 = -w_{\text{shaft}}} \ .
$$

This indicates that the **specific enthalpy change** equals the **negative of the shaft work per unit mass**.

:::{important}

**PHYSICAL INTERPRETATION**

* For a **turbine**, $w_{\text{shaft}} > 0$, meaning **work is produced**, so $h_2 < h_1$.
* For a **compressor**, $w_{\text{shaft}} < 0$, meaning **work is consumed**, so $h_2 > h_1$.
  In both cases, adiabatic operation makes the enthalpy change directly representative of the work exchange.
:::

---

(subsec_nozzles_diffusers)=
### Nozzles and diffusers

**Nozzles** and **diffusers** are aerodynamic devices that convert energy between **enthalpy** and **kinetic energy**.

* In a **nozzle**, enthalpy decreases as the fluid accelerates (increasing its speed $c$).
* In a **diffuser**, kinetic energy decreases and enthalpy increases as the fluid slows down.

Assuming **adiabatic operation** ($q \simeq 0$), **no shaft work** ($w_{\text{shaft}} = 0$), and **negligible elevation change** ($\Delta z \simeq 0$), the steady-flow energy balance becomes:

(eq_nozzle_diffuser)=
$$
\boxed{(h_2 - h_1) + \frac{c_2^2 - c_1^2}{2} = 0} \ .
$$

This expression shows that the **drop or gain in enthalpy** is entirely converted into **kinetic energy** (or vice versa).

:::{tip}

**ON FLOW GEOMETRY**

The detailed relationship between **geometry** (convergent or divergent) and **flow regime** (subsonic or supersonic) depends on compressibility effects.
These conditions — crucial in the design of **aerodynamic nozzles** and **diffusers** — will be analyzed later in the study of **compressible flow**.
:::

---

(subsec_heaters)=
### Heaters

**Heaters** are devices where the fluid temperature (and therefore enthalpy) increases by **heat addition**.
Typical examples include **electric heaters**, **boilers**, and **superheaters**.

These systems generally operate with **no shaft work** ($w_{\text{shaft}} = 0$) and **negligible changes in kinetic and potential energy**.
Under these assumptions, the $1^{\text{st}}$ law simplifies to:

(eq_heater)=
$$
\boxed{h_2 - h_1 = q} \ .
$$

This means that the **heat supplied to the control volume** directly increases the **enthalpy** of the flowing fluid, primarily as an increase in **internal energy** and **temperature**.

:::{note}

**PRACTICAL MEANING**

For perfect gases, $h \approx c_p (T - T_{0})$ with $c_{p} = \text{const.} \neq f(T)$, so this balance becomes $q = c_p (T_{2} - T_{1})$, showing that the temperature rise is proportional to the supplied heat.
:::

---

(subsec_throttling_valves)=

### Throttling (expansion) valves

**Throttling valves** — also called **expansion valves** or **control valves** — reduce the pressure of a flowing fluid through a sharp restriction.
These processes are modeled as **adiabatic** ($q \simeq 0$), **without shaft work**, and with **negligible changes in kinetic and potential energies**.

Applying these assumptions to the steady-flow form yields:

(eq_throttling_valve)=
$$
0 = (h_2 - h_1) \implies \boxed{h_2 = h_1} \ .
$$

Thus, throttling is an **isoenthalpic process**: total enthalpy remains constant even though its two components — **internal energy** ($u$) and **flow work** ($Pv$) — change in opposite directions.

We can express this explicitly as:

(eq_throttling_valve_decomposition)=
$$
h = u + pv \implies u_2 - u_1 = -(p_2v_2 - p_1v_1).
$$

This means that a **decrease in flow work** (drop in $Pv$) must be balanced by an **increase in internal energy** ($u$), or vice versa.
In practice, the pressure drop usually causes the **temperature to decrease**, as part of the internal energy is expended to perform the pressure–volume work.

:::{note}

**PHYSICAL INTERPRETATION**

The **isoenthalpic condition** does not imply constant temperature.
In real fluids where $u=u(T,p)$, lowering the pressure during throttling may cause cooling (Joule–Thomson effect), widely exploited in **refrigeration** and **liquefaction** processes.
For ideal gases, by contrast, $u$ depends only on $T$, so temperature remains unchanged during throttling.
:::

---

(subsec_heat_exchangers)=
### Heat exchangers

**Heat exchangers** transfer heat between two or more flowing fluids separated by a solid wall, without direct mixing. They are modeled as **adiabatic to the surroundings** and with **no shaft work**. Notice that:
* Unlike in the previous devices, the single-inlet/single-outlet paradigm is not applicable in a heat exchanger. By definition, these devices mix two fluids together, so the **simplest configuration** conceivable must take into account **two inlets and two outlets**. For the purposes of this exposition, those two streams will be subscripted as $a$ and $b$.
* Needless to say, the **continuity equation** will hold equally.
    * The **total mass** entering the system will have to be equal to the total mass coming out of it $\implies (\dot{m}_{a} + \dot{m}_{b})_{\text{in}} = (\dot{m}_{a} + \dot{m}_{b})_{\text{out}}$
    * Each of the individual streams will fulfill the continuity equation as well $\implies \dot{m}_{a_{\text{in}}} = \dot{m}_{a_{\text{out}}}, \quad \dot{m}_{b_{\text{in}}} = \dot{m}_{b_{\text{out}}}$.
    * The adiabatic condition of the device with respect to the surroundings means that, when considering the system as a whole, **no heat flow is observed to enter or leave the device** $\implies q=0$.

For each fluid stream, applying the steady-flow energy equation gives:

(eq_heat_exchanger_energy_balance)=
$$
\dot m_a (h_{a_{\text{out}}} - h_{a_{\text{in}}}) + \dot m_b (h_{b_{\text{out}}} - h_{b_{\text{in}}}) = 0
\implies
\boxed{\dot m_a \Delta h_a = -\dot m_b \Delta h_b} \ .
$$

Hence, the **enthalpy increase of one fluid** equals the **enthalpy decrease of the other**.

:::{note}

**PRACTICAL EXAMPLES**

This idealization applies to condensers, economizers, evaporators, and other industrial heat exchangers.
In real systems, thermal losses, wall conduction, and imperfect counterflow slightly modify this balance.
:::

---

(subsec_mixing_chambers)=
### Mixing chambers

**Mixing chambers** combine multiple streams into a single homogeneous outlet stream. They are typically **adiabatic**, **without shaft work**, and have **negligible kinetic and potential energy changes**. As occurs with heat exchangers, the single-inlet/single-outlet paradigm is not applicable here. The **simplest configuration** conceivable is that in which two inlet streams mix into a single outlet stream. Subscripting the streams, respectively, as $(1, 2)$ (inlets) and $3$ (outlet):

From **mass conservation**:

(eq_mixing_chamber_mass_conservation)=
$$
\dot m_1 + \dot m_2 = \dot m_3.
$$

and from **energy conservation**:

(eq_mixing_chamber_energy_balance)=
$$
\dot m_1 h_1 + \dot m_2 h_2 = \dot m_3 h_3
\implies
\boxed{h_3 = \frac{\dot m_1 h_1 + \dot m_2 h_2}{\dot m_1 + \dot m_2}} \ .
$$

The resulting outlet enthalpy $h_3$ represents a **mass-weighted average** of the inlet enthalpies.

:::{tip}

**APPLICATIONS**

Mixing devices are found in **combustion chambers**, **humidifiers**, and **steam injectors**, where energy uniformity across the outlet stream is essential.
:::

---

(subsec_summary_table_canonical_systems)=

### Summary of canonical steady-flow systems

| **Device**            | **Main energy interaction** | **Simplified form of the $1^{\text{st}}$ law** | **Typical assumptions**                                           | **Main physical effect**                                  |
| :-------------------- | :-------------------------- | :--------------------------------------------- | :---------------------------------------------------------------- | :-------------------------------------------------------- |
| **Turbine**           | Shaft work (output)         | $h_2 - h_1 = -w_{\text{shaft}}$               | Adiabatic, $\Delta c^2 \simeq 0$, $\Delta z \simeq 0$             | Converts enthalpy drop into mechanical power              |
| **Compressor / Pump** | Shaft work (input)          | $h_2 - h_1 = -w_{\text{shaft}}$               | Adiabatic, $\Delta c^2 \simeq 0$, $\Delta z \simeq 0$             | Increases enthalpy (and pressure) through mechanical work |
| **Nozzle / Diffuser** | Kinetic energy exchange     | $(h_2 - h_1) + \tfrac{c_2^2 - c_1^2}{2} = 0$   | Adiabatic, $w_{\text{shaft}}=0$, $\Delta z \simeq 0$              | Converts enthalpy ↔ kinetic energy                        |
| **Heater**            | Heat addition               | $h_2 - h_1 = q$                                | $w_{\text{shaft}}=0$, $\Delta c^2, \Delta z \simeq 0$             | Raises fluid temperature via heat transfer                |
| **Throttling valve**  | Isoenthalpic flow           | $h_2 = h_1$                                    | Adiabatic, $w_{\text{shaft}}=0$, $\Delta c^2, \Delta z \simeq 0$  | Pressure drop induces internal energy–flow work exchange  |
| **Heat exchanger**    | Inter-stream heat exchange  | $\dot m_a \Delta h_a = -\dot m_b \Delta h_b$   | Adiabatic overall, no $w_{\text{shaft}}$                          | Heat transfer between two fluids without mixing           |
| **Mixing chamber**    | Enthalpy averaging          | $\dot m_1 h_1 + \dot m_2 h_2 = \dot m_3 h_3$   | Adiabatic, no $w_{\text{shaft}}$, $\Delta c^2, \Delta z \simeq 0$ | Produces a uniform mixture of incoming streams            |

---

(subsec_conceptual_closure_canonical)=

### Conceptual closure

The canonical open systems presented above are all **steady-flow applications** of the same physical law.
Their differences lie in the **dominant energy mechanism** and in the **simplifications** that make one term of the $1^{\text{st}}$ law more relevant than others.

* **Turbines** and **compressors** exchange enthalpy with mechanical work.
* **Nozzles** and **diffusers** convert energy between enthalpy and kinetic form.
* **Heaters** and **heat exchangers** modify enthalpy through heat transfer.
* **Throttling valves** are isoenthalpic but display pressure–temperature coupling through internal energy and flow work redistribution.
* **Mixing chambers** merge multiple flows, conserving both mass and total enthalpy.

Each device type exemplifies one way in which the **same conservation principle** manifests in engineering:
**energy cannot be created or destroyed — it only changes form as mass flows through the system boundaries.**

