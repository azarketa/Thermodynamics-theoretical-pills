(sec_useful_work_reversibility_efficiency)=
## Useful work, reversibility, and $2^{\text{nd}}$-law efficiency

Having clarified the notions of **dead state**, **surroundings**, and **work potential**, we can now introduce the **work-related quantities** that serve as a bridge toward the **definition of exergy**. These magnitudes connect the **energy exchanges** of a system with the **quality** of those exchanges, showing how *irreversibilities* reduce the amount of *useful* work that can be obtained.

---

(subsec_surroundings_and_useful_work)=
### Surroundings work and useful work

The notions of **surroundings work** and **useful work** are introduced to separate the **total mechanical work** exerted at a system’s boundary from the **portion that represents usable energy**. Whenever a system interacts mechanically with its environment, part of the boundary work simply counteracts the **ambient (atmospheric) pressure**, maintaining equilibrium with the surroundings. Only the remaining part — the **useful work** — effectively contributes to changing the system’s energetic state and, therefore, to its **exergy** or **work potential**.

This distinction is best illustrated through a **piston–cylinder system**, the simplest and most representative configuration for mechanical interaction. The **piston face** is exposed to the **atmosphere**, which acts as the **surroundings** exerting a constant pressure $p_0$. When the system’s volume changes from $V_1$ to $V_2$, the surroundings perform **mechanical work** on the system corresponding to this environmental pressure, expressed as

(eq_work_surr)=
$$
\boxed{W_{\text{surr.}} = p_0 (V_2 - V_1)}
$$

This quantity expresses the **mechanical action of the ambient pressure** upon the boundary.

The **useful work** is then defined as the **net work** obtained after subtracting this unavoidable environmental contribution from the total boundary work $W$:

(eq_work_useful)=
$$
\boxed{W_u = W - W_{\text{surr.}}}
$$

This distinction clarifies that:

* For an **expanding system**, the surroundings work acts as a **resisting force** that must be overcome — it **reduces** the useful work output.
* For a **compressing system**, the surroundings work assists compression — it **reduces** the required external work input.

Hence, $W_u$ represents the **effective mechanical energy** that remains available for use once the environmental pressure effects are discounted.

:::{admonition} Note: boundary work in open systems
:class: note, dropdown
In **open systems**, where mass crosses the control surface, the concept of boundary work appears implicitly as **flow work**, defined per unit mass as $p v$.
Each fluid element must “push” the surrounding fluid as it enters or leaves the control volume, and this mechanical effect is already included in the **enthalpy** term $h = u + p v$.
Thus, the distinction between **total** and **useful** work remains valid — but it is embedded within the definition of enthalpy rather than appearing explicitly as $p_0(V_2 - V_1)$.
:::

---

(subsec_reversible_work_and_irreversibility)=
### Reversible work and irreversibility

Among all possible transformations between two given states, the **reversible process** yields the **maximum possible useful work** (or requires the **minimum input work**). This defines the **reversible work**, $W_{\text{rev.,out}}$.

The **irreversibility**, $I$, quantifies the **loss of useful work potential** due to the presence of dissipative effects. It is therefore expressed as

(eq_irreversibility)=
$$
\boxed{I = W_{\text{rev.,out}} - W_{u,\text{out}}}
$$

where the subscript **out** denotes that the quantities refer to **work output**.

In real systems, $I > 0$, and only in the **ideal reversible limit** does $I = 0$, indicating no loss of work potential.

:::{admonition} Note: distinction in the use of the term *irreversibility*
:class: note, dropdown
The word **irreversibility** is used in two related senses:

* Qualitatively, it refers to the **presence of dissipative effects** (such as friction, finite temperature differences, or mixing) that prevent a process from being reversible.
* Quantitatively, it designates the **magnitude $I$**, which measures the **energetic equivalent** of those effects — the *work potential destroyed* because of entropy generation.

Although both meanings are connected, the first is descriptive, while the second is **numerical** and **measurable** in joules.
:::

---

(subsec_second_law_efficiency)=
### $2^{\text{nd}}$-law efficiency and the measure of energy quality

The **$2^{\text{nd}}$-law efficiency**, also called **rational efficiency**, complements the **thermal efficiency** by taking into account not only the **quantity** but also the **quality** of the energy exchanged. While the **$1^{\text{st}}$ law** concerns itself with conservation of energy, the **$2^{\text{nd}}$ law** evaluates *how effectively* that energy can be converted into useful work.

To grasp this idea, imagine two heat engines operating under different temperature ranges but yielding the **same thermal efficiency**. Although their energy ratios ($W/Q_H$) are equal, their **thermodynamic contexts** differ: the engine operating between a smaller temperature difference works under less favorable conditions. When compared with the **reversible (Carnot) limit** corresponding to each temperature range, the engine that operates effectively under the more restrictive temperature difference shows a **higher $2^{\text{nd}}$-law efficiency**, since it comes **closer to its own ideal limit**.

Hence, the $2^{\text{nd}}$-law efficiency expresses how effectively a device approaches its **reversible benchmark**, regardless of the absolute temperature levels involved. Formally, for a heat engine:

(eq_eta_II_engines)=
$$
\boxed{\eta_{II} = \frac{\eta_{\text{th.}}}{\eta_{\text{th.,rev.}}}}
$$

To illustrate this quantitatively, consider two heat engines, **A** and **B**, each with a **thermal efficiency** of $\eta_{\text{th.}} = 0.30$. Engine **A** operates between $T_H = 600\ \text{K}$ and $T_L = 300\ \text{K}$, while engine **B** operates between $T_H = 1000\ \text{K}$ and $T_L = 300\ \text{K}$.

Their **reversible (Carnot) efficiencies** are:

$$
\begin{gather*}
\eta_{\text{th.,rev.,A}} = 1 - \frac{300}{600} = 0.50, \\[10pt]
\eta_{\text{th.,rev.,B}} = 1 - \frac{300}{1000} = 0.70.
\end{gather*}
$$

Accordingly, their **$2^{\text{nd}}$-law efficiencies** are:

$$
\begin{gather*}
\eta_{II,\text{A}} = \frac{0.30}{0.50} = 0.60, \\[10pt]
\eta_{II,\text{B}} = \frac{0.30}{0.70} \approx 0.43.
\end{gather*}
$$

Although both engines transform the same *fraction* of heat into work, engine **A** achieves its performance **under less favorable conditions** and thus operates **closer to its reversible limit**. This shows that $\eta_{II}$ measures not just *how much* energy is converted, but *how well* the system performs relative to its theoretical potential.

In general, depending on the system’s purpose, this efficiency can be expressed as:

:::{admonition} Important: general definitions of $2^{\text{nd}}$-law efficiency
:class: warning

| **Device type** | **Definition** | **Interpretation** |
| :- | :- | :- |
| **Work-producing device** | $\displaystyle \eta_{II} = \frac{\eta_{\text{th.}}}{\eta_{\text{th.,rev.}}} = \frac{W_u}{W_{\text{rev.}}}$ | Fraction of maximum work actually obtained |
| **Work-consuming device** | $\displaystyle \eta_{II} = \frac{\eta_{\text{th.}}}{\eta_{\text{th.,rev.}}} = \frac{W_{\text{rev.}}}{W_u}$ | Fractional closeness to the reversible minimum input |
| **Refrigerator / heat pump** | $\displaystyle \eta_{II} = \frac{\text{COP}}{\text{COP}_{\text{rev.}}} = \frac{\text{COP}}{\text{COP}_{\text{rev.}}}$ | Fraction of ideal performance achieved |

:::

:::{admonition} Note: interpreting the $2^{\text{nd}}$-law efficiency
:class: note, dropdown

The **$2^{\text{nd}}$-law efficiency** may also be viewed as a measure of the **room for improvement** of a real system. A value of $\eta_{II}$ close to 1 indicates that the process already operates **near its reversible limit**, leaving little potential for enhancement. Conversely, a low $\eta_{II}$ reveals a **large gap** between actual and ideal performance, quantifying the **scope for reducing irreversibilities** and **improving energy quality** within the device.

:::

---

(subsec_efficiency_comparison)=
### Comparison of efficiencies defined so far

At this stage, several **efficiency measures** have been introduced, each addressing a **different dimension of performance** and grounded in distinct principles:

* **Thermal efficiency**, $\eta_{\text{th.}}$, quantifies the **fraction of input heat converted to work**—the $1^{\text{st}}$-law (energy-balance) view for heat engines.
* **Carnot efficiency**, $\eta_{\text{Carnot}}=\eta_{\text{th.,rev.}}$, is the **thermal efficiency of a reversible heat engine**; it is the **maximum possible** $\eta_{\text{th.}}$ achievable between $T_H$ and $T_L$, hence a **particular (reversible) case** of thermal efficiency.
* **Isentropic efficiency**, $\eta_{\text{is.}}$, compares an **actual process** to its **adiabatic + reversible** (isentropic) counterpart— a **device-specific** measure for compressors, turbines, and nozzles.
* **$2^{\text{nd}}$-law efficiency**, $\eta_{II}$, compares **actual performance** to the **reversible limit** (Carnot or equivalent), merging **energy quantity** and **energy quality** in one nondimensional indicator.

:::{admonition} Important: summary and comparison of efficiency types
:class: warning

| **Efficiency type** | **Definition / ratio** | **Ideal reference** | **Physical meaning** |
| :- | :- | :- | :- |
| **Thermal efficiency** | $\displaystyle \eta_{\text{th.}} = \frac{W_{\text{out}}}{Q_{\text{in}}} = 1 - \frac{Q_L}{Q_H}$ | None (energy-balance based) | Measures energy conversion according to the $1^{\text{st}}$ law (quantity only) |
| **Carnot efficiency** | $\displaystyle \eta_{\text{Carnot}}=\eta_{\text{th.,rev.}} = 1 - \frac{T_L}{T_H}$ | Itself | Measures maximum achievable energy conversion according to the $1^{\text{st}}$ law (quantity only) |
| **Isentropic efficiency** | $\displaystyle \eta_{\text{is.}} = \frac{(\Delta h)_{\text{s}}}{(\Delta h)_{\text{a}}}$ or equivalent, depending on the process | Ideal adiabatic + reversible (isentropic) process | Device-specific comparison of real vs. isentropic performance |
| **$2^{\text{nd}}$-law efficiency** | $\displaystyle \eta_{II} = \frac{\eta_{\text{th.}}}{\eta_{\text{th.,rev.}}}$ | Reversible (Carnot or general) limit | Considers both energy quantity and quality — proximity to the reversible bound |

:::

---

(subsec_conceptual_closure_useful_work)=
### Conceptual closure

* **Surroundings work** isolates the mechanical effect of ambient pressure.
* **Useful work** measures the effective mechanical contribution after discounting that environmental effect.
* **Reversible work** represents the theoretical upper limit of usefulness; **irreversibility** measures how much of that potential is lost.
* The **$2^{\text{nd}}$-law efficiency** generalizes this idea into a nondimensional indicator, linking the $1^{\text{st}}$ and $2^{\text{nd}}$ laws.
* Together, these concepts establish the foundation for the next step: the definition of **exergy** as the unified measure of *usable energy* — the maximum useful work a system can deliver as it comes into equilibrium with its environment.
