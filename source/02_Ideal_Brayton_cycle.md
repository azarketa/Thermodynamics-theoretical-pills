(sec_brayton_cycle_ideal)=
## The ideal gas power cycle: the Brayton cycle

The present lecture focuses on **power gas cycles**, that is, thermodynamic cycles designed to deliver a net mechanical power output while operating entirely in the gaseous phase. Even after restricting the analysis to **thermal receiver turbomachines**, a variety of gas cycles remain possible. Among them, the **Ericsson** and **Stirling** cycles constitute classical theoretical examples.

However, for reasons that will become clear throughout this section, these cycles are of limited practical relevance in large-scale power and propulsion systems. Instead, the **Brayton cycle** emerges as the paradigmatic gas cycle and constitutes the basis of modern gas turbines and aircraft engines.

---

(subsec_brayton_components)=
### Components and ideal processes of the Brayton cycle

The **simple ideal Brayton cycle** consists of three main components:

- a **compressor**,  
- a **combustion chamber**,  
- a **turbine**.

The working fluid flows continuously through these devices, and the cycle is defined in terms of four idealized thermodynamic processes:

- **Process $1 \rightarrow 2$ (compression):**  
  The flow enters the compressor at state $1$ and is compressed until reaching state $2$. In the ideal case, this process is **isentropic**.

- **Process $2 \rightarrow 3$ (heat addition):**  
  At state $2$, the flow enters the combustion chamber, where its enthalpy increases due to a chemical reaction. Ideally, heat addition occurs at **constant pressure**,
  leading the fluid to state $3$.

- **Process $3 \rightarrow 4$ (expansion):**  
  The high-enthalpy gas expands through the turbine, producing mechanical work and reaching state $4$. Ideally, this expansion is **isentropic**.

- **Process $4 \rightarrow 1$ (heat rejection):**  
  In order to close the cycle, heat is rejected at **constant pressure**, returning the working fluid to its initial thermodynamic state.

:::{important}

**IDEAL BRAYTON CYCLE**

The ideal Brayton cycle consists of two isentropic processes (compression and expansion) and two isobaric processes (heat addition and heat rejection). Each component may be analysed independently as a steady-flow open system.

:::

---

(subsec_brayton_diagrams)=
### The $p–v$ and $T–s$ diagrams of the ideal Brayton cycle

The structure of the Brayton cycle is clearly illustrated in the $p-v$ and
$T-s$ diagrams:

- In the **$p-v$ diagram**:
  - processes $2 \rightarrow 3$ and $4 \rightarrow 1$ appear as **horizontal straight lines** (isobaric),
  - processes $1 \rightarrow 2$ and $3 \rightarrow 4$ appear as **curved lines** (isentropic).

- In the **$T-s$ diagram**:
  - processes $1 \rightarrow 2$ and $3 \rightarrow 4$ appear as **vertical straight lines** (isentropic),
  - processes $2 \rightarrow 3$ and $4 \rightarrow 1$ appear as **curved lines** (isobaric).

These representations highlight the fundamental symmetry of the cycle.

---

(subsec_brayton_efficiency)=
### Thermal efficiency of the ideal Brayton cycle

To evaluate the thermal efficiency of the ideal Brayton cycle, kinetic and potential energy variations are assumed negligible. Applying the **$1^{\text{st}}$ law of thermodynamics** in its specific form yields:

(eq_first_law_brayton)=
$$
(q_{\text{in}} - q_{\text{out}}) + (w_{\text{in}} - w_{\text{out}}) = h_{\text{in}} - h_{\text{out}} .
$$

The evaluation of enthalpy changes requires specifying the model adopted for the working fluid. In gas turbines, the working fluid is predominantly air, and the products of combustion do not significantly alter its thermodynamic properties. This motivates the use of the **standard air model**, which assumes:

- air behaves as an **ideal gas**,
- all processes are **internally reversible**,
- the specific heats are evaluated at $25 \ ^{\circ}\text{C}$ and treated as constant (the **standard cold-air assumption**).

:::{note}

**STANDARD COLD-AIR ASSUMPTION**

Under this assumption, air is treated as a *perfect gas* with constant specific heats. Although approximate, this model provides accurate qualitative insight and reasonable quantitative results for many engineering applications.

:::

With these assumptions, the heat interactions are

(eq_brayton_qin)=
$$
q_{\text{in}} = h_3 - h_2 = c_p (T_3 - T_2),
$$

(eq_brayton_qout)=
$$
q_{\text{out}} = h_4 - h_1 = c_p (T_4 - T_1).
$$

The thermal efficiency becomes

(eq_eta_brayton_general)=
$$
\eta_{\text{th,Brayton}} = 1 - \frac{q_{\text{out}}}{q_{\text{in}}} = 1 - \frac{T_4 - T_1}{T_3 - T_2}.
$$

Because processes $1 \rightarrow 2$ and $3 \rightarrow 4$ are isentropic and $p_2 = p_3$, $p_4 = p_1$, it follows that:

(eq_brayton_isentropic_relations)=
$$
\frac{T_2}{T_1} = \left( \frac{p_2}{p_1} \right)^{\frac{\gamma - 1}{\gamma}} = \frac{T_3}{T_4}.
$$

Introducing the **pressure ratio**:

(eq_pressure_ratio)=
$$
r_p = \frac{p_2}{p_1},
$$

the thermal efficiency of the ideal Brayton cycle becomes:

(eq_eta_brayton_final)=
$$
\eta_{\text{th,Brayton}} = 1 - \frac{1}{r_p^{(\gamma - 1)/\gamma}} .
$$

This expression shows that the thermal efficiency increases with both the pressure ratio and the ratio of specific heats.


:::{note}

**TRADE-OFF BETWEEN THERMAL EFFICIENCY AND NET POWER OUTPUT**

In practical gas turbines, the maximum cycle temperature occurs at the turbine inlet (state $3$) and is limited by the thermal resistance of turbine blades and materials. For a fixed turbine inlet temperature, increasing the pressure ratio initially increases the net power output, but beyond a certain point the net power begins to decrease.

As a result, **maximum thermal efficiency** and **maximum net power output** do not occur at the same pressure ratio, leading to a necessary design compromise.

A lower net specific work requires a higher mass flow rate to achieve a given power output, which may be economically undesirable. In practical Brayton cycles, typical
pressure ratios lie in the range $11 \le r_p \le 16$.

:::

:::{tip}

**THE ROLE OF AIR IN GAS TURBINES**

In gas turbines, air fulfills two essential roles:

- it provides the oxidizer required for fuel combustion,
- it acts as a **cooling medium** to maintain acceptable temperatures in critical components.

To accomplish the second function, gas turbines operate with air–fuel mass ratios well above the stoichiometric requirement, often exceeding values of 50. This justifies modelling the combustion products as air with minimal error.

Since fuel is added downstream of the compressor, the mass flow rate through the turbine is slightly larger than that through the compressor. Assuming a constant mass flow rate throughout the cycle therefore constitutes a conservative approximation.

:::

---

(subsec_back_work_ratio)=
### Back-work ratio

In gas power cycles, a significant fraction of the turbine work is required to drive the compressor. The ratio between compressor work and turbine work is known as the **back-work ratio**, and it is typically high in gas turbines, often approaching $50 \ \%$.

Low isentropic efficiencies in the compressor or turbine further increase this ratio.

By contrast, in steam power plants the back-work ratio is much smaller (typically $1–5 \ \%$), since compressing a liquid requires far less work than compressing a gas.
As a consequence, for a given net power output, gas turbines must generally be larger than steam turbines.

---

(subsec_brayton_conceptual_closure)=
### Conceptual closure

- The Brayton cycle is the fundamental gas power cycle.
- It consists of two isentropic and two isobaric processes.
- Under the standard cold-air assumption, its efficiency depends only on the
  pressure ratio and $\gamma$.
- Increasing pressure ratio improves efficiency but not indefinitely increases
  net power.
- Air acts both as a reactant and as a cooling medium in gas turbines.
- Gas turbines exhibit a high back-work ratio compared to steam power plants.
