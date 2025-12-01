(sec_exergy_closed_open)=
## Exergy of closed and open systems

Having defined the concepts of **useful work**, **reversible work**, and **irreversibility**, we are now ready to formalize the **notion of exergy**.
Exergy represents the **maximum theoretical work** obtainable as a system evolves **reversibly** from a given initial state to the **dead state** — the condition of **thermodynamic equilibrium** with its environment. It therefore quantifies, in energetic terms, the **quality** of a system’s energy and the **degradation** caused by irreversibilities.

---

(subsec_exergy_closed)=
### Definition of exergy for a closed system

To illustrate the derivation of exergy in the most direct and transparent way, it is convenient to examine a **piston–cylinder system**. This configuration provides the **simplest representation of mechanical and thermal interactions** between a system and its surroundings: pressure–volume work at a movable boundary, and heat transfer to or from the environment. It therefore serves as a **paradigm for reversible energy exchange**, allowing the exergy concept to be derived explicitly from the $1^{\text{st}}$ and $2^{\text{nd}}$ laws before extending it to more complex systems.

Hence, consider a **piston–cylinder system** acting as the **source** of a **heat engine**, initially at $(p > p_0, T > T_0)$. As it expands **reversibly** to the **dead state** $(p_f = p_0, T_f = T_0)$, the system:

* Performs **boundary work** $\delta W_{\text{b.,useful}}$,
* Releases a **heat quantity** $\delta Q$ that drives the heat engine,
* Allows the engine to deliver an **additional work** $\delta W_{\text{HE}}$.

Applying the **$1^{\text{st}}$ law** to the closed system:

$$
\delta E_{\text{in}} - \delta E_{\text{out}} = \mathrm{d}E_{\text{sys.}} \quad \Rightarrow \quad \delta Q - \delta W = \mathrm{d}U
$$

The **differential work** exerted at the boundary may be decomposed as:

$$
\delta W = p\mathrm{d}V = (p - p_0)\mathrm{d}V + p_0 \mathrm{d}V = \delta W_{\text{b.,useful}} + \delta W_{\text{surr.}}
$$

The **work delivered by the heat engine** operating between the system (at $T$) and the environment (at $T_0$) is:

$$
\delta W_{\text{HE}} = \left(1 - \frac{T_0}{T}\right)\delta Q = \delta Q - T_0\frac{\delta Q}{T} = \delta Q - T_0 \mathrm{d}S
$$

Substituting and rearranging yields the **total differential useful work** obtainable from the combined system–engine arrangement:

(eq_exergy_differential)=
$$
\delta W_{\text{total,useful}} = -\mathrm{d}U - p_0 \mathrm{d}V + T_0 \mathrm{d}S
$$

Integrating between the initial state and the **dead state** gives:

(eq_exergy_closed)=
$$
W_{\text{total,useful}} = (U - U_0) + p_0 (V - V_0) - T_0 (S - S_0).
$$

This quantity represents the **maximum useful work potential** of the system, attainable only through a **reversible process**.

However, this formulation only includes **microscopic energy modes** ($U$, $S$, $V$).
To obtain the **total exergy**, the **macroscopic energy contributions** — kinetic and potential — must be added:

(eq_exergy_closed_total)=
$$
\boxed{X = (U - U_0) + p_0 (V - V_0) - T_0 (S - S_0) + \frac{m c^2}{2} + m g z} \ .
$$

Equivalently, by grouping the internal, kinetic and potential energies into a single specific term $E$ (the macroscopic energy):

(eq_exergy_closed_total)=
$$
\boxed{X = (E - E_0) + p_0 (V - V_0) - T_0 (S - S_0)} \ .
$$

Thus, **exergy** quantifies the **maximum useful work** extractable as the system moves reversibly from its initial state to equilibrium with the environment. If the system is already at the dead state and has no kinetic or potential energy, $X=0$: **no further useful work can be obtained.**

Expressing exergy per unit mass yields its **specific (intensive)** form:

(eq_exergy_specific_simplified)=
$$
\boxed{\phi = (e - e_0) + p_0 (v - v_0) - T_0 (s - s_0)}
$$

The **change in specific exergy** for a process between two arbitrary states $(1)$ and $(2)$ is therefore:

(eq_exergy_change_specific)=
$$
\boxed{\Delta \phi = \phi_2 - \phi_1 = (e_2 - e_1) + p_0 (v_2 - v_1) - T_0 (s_2 - s_1)}
$$

---

(subsec_exergy_open)=
### Definition of exergy for an open system

When dealing with **open systems**, the proper exergy formulation must include the **flow work** — the work required to push mass into or out of the system.

If a moving fluid exerts pressure $p$ as it crosses the boundary, the **flow exergy** is given by:

(eq_flow_exergy)=
$$
x_{\text{flow}} = (p - p_0)v
$$

This term represents the **work needed to displace** the volume of atmospheric air occupied by the flowing fluid.
It plays the same role here as the $p_0(v - v_0)$ term in the closed-system expression.

Adding the flow term to the closed-system exergy gives the **specific exergy for open systems**:

(eq_exergy_open)=
$$
\boxed{\psi = (h - h_0) - T_0 (s - s_0) + \frac{c^2}{2} + g z}
$$

where $h = u + pv$ is the specific enthalpy. The corresponding **change in specific exergy** is:

(eq_exergy_change_open)=
$$
\boxed{\Delta \psi = \psi_2 - \psi_1 = (h_2 - h_1) - T_0 (s_2 - s_1) + \frac{c_2^2 - c_1^2}{2} + g (z_2 - z_1)}
$$

---

(subsec_exergy_transfer_terms)=
### Exergy transfer mechanisms

Because exergy is a **transferable quantity**, it can cross system boundaries through **heat**, **work**, or **mass** transfer.
The associated exergy terms are:

(eq_exergy_heat_work_mass)=
$$
\begin{aligned}
X_{\text{heat}} &= \left(1 - \frac{T_0}{T}\right) Q, \\[10pt]
X_{\text{work}} &=
\begin{cases}
W - W_{\text{surr}}, & \text{for boundary work}, \\[6pt]
W & \text{for other work modes},
\end{cases} \\[10pt]
X_{\text{mass}} &= \dot{m}\psi.
\end{aligned}
$$

:::{admonition} Important: exergy transfer interpretation
:class: warning
Each exergy transfer mechanism corresponds to a **potential for useful work**:

* **Heat exergy** decreases with the temperature level of the source.
* **Work exergy** equals the *useful* part of the work done.
* **Mass exergy** reflects the *energetic and entropic state* carried by flowing matter.
:::

---

(subsec_conceptual_closure_exergy_closed_open)=
### Conceptual closure

* **Exergy** represents the **maximum useful work** that a system can deliver as it moves **reversibly** toward equilibrium with its **environment** — the **dead state**.
* In **closed systems**, exergy depends on the internal, kinetic, potential, and $p_0V$–$T_0S$ terms that express the system’s energetic deviation from its surroundings.
* In **open systems**, the inclusion of **flow work** and **enthalpy** terms reflects the capacity of **moving matter** to transport useful energy.
* Exergy transfer through **heat**, **work**, or **mass** represents the flow of *work potential* across boundaries.
* When a system reaches the **dead state**, its exergy — and therefore its capacity to do useful work — **vanishes**.

In essence, exergy provides a **quantitative measure of how far a system stands from complete equilibrium**. The next step is to formalize how this potential diminishes in all real processes — leading to the **principle of decreasing exergy** and the **definition of exergy destruction**.
