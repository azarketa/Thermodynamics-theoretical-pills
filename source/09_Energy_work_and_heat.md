(sec_energy_work_heat)=
## Energy, work and heat

Thermodynamic systems do not remain motionless; they experience **processes** that transform or transfer energy. While equilibrium analysis provides a snapshot of a system’s state, **energy and its modes of transfer** describe how systems evolve between states. This section introduces the fundamental notions of **work**, **heat**, and **energy** — the building blocks of the **first law of thermodynamics**, which states that energy can neither be created nor destroyed, only converted from one form to another.

---

(subsec_notions_of_work_and_energy)=
### Notions of work and energy

Thermodynamics is built around the concept of **energy conservation**. The familiar phrase — *“energy is neither created nor destroyed, but transformed”* — captures the essence of the **first law**. Yet, energy is not a tangible object: it is an **abstract bookkeeping quantity** that links different forms of motion, interaction, and transformation.

In every process, energy may appear in diverse forms — mechanical, thermal, chemical, electrical — but the **total** always remains constant. What changes is its **distribution** among those forms.

:::{admonition} Note: energy is relative
:class: note, dropdown
Thermodynamics does not provide absolute energy values, only **differences** between states.
A convenient reference (e.g. setting $E=0$ at a defined state) allows consistent comparisons and energy balances.
:::

---

(subsec_physical_definition_of_work)=
### Physical definition of work

At the infinitesimal level, **mechanical work** is defined as:

(eq_work_def)=
$$
\delta W = \vec{F}\cdot\text{d}\vec{r}.
$$

Work is a **scalar** (dot product of vectors) and is **path-dependent**: it depends on how the process is carried out, not just the end states.
Hence, $\delta W$ uses the inexact differential symbol $\delta$, rather than $\mathrm{d}$.

The SI unit of work is the joule ($\text{J}$):

(eq_joule_unit)=
$$
1\ \mathrm{J} = 1\ \text{N}\cdot\text{m}.
$$

:::{admonition} Tip: interpreting the Joule
:class: tip, dropdown
A single joule corresponds to the work required to lift a $100\ \mathrm{g}$ mass through $1\ \mathrm{m}$. Because thermodynamic processes involve much larger energy exchanges, kilojoules ($\text{kJ}$) or megajoules ($\text{MJ}$) are typically used.
:::

:::{admonition} Note: sign convention
:class: note, dropdown
In this text, **work done by the system** on its surroundings is taken as **positive** ($\delta W>0$). Conversely, **work done on the system** is negative. The same convention will apply in the formulation of the **first law**.
:::

---

(subsec_types_of_energy)=
### Types of energy

The total energy of a system, $E$, encompasses several forms:

(eq_energy_split)=
$$
E = U + E_k + E_p (+ E_f \ \text{if applicable}),
$$

where $U$ is **internal energy**, $E_k$ **kinetic**, $E_p$ **potential**, and $E_f$ the **flow energy** that appears in open systems.

We distinguish between **macroscopic (organized)** and **microscopic (disorganized)** forms.

(subsec_macroscopic_energy)=
#### Macroscopic energy (organized)

These are energies associated with the **bulk motion or position** of the system relative to an external frame:

* **Kinetic energy:**

  (eq_Ek)=
  $$
  E_k = \tfrac{1}{2}{}mV^2.
  $$

  It depends on the system’s center-of-mass velocity $V$.

* **Potential energy:**

  (eq_Ep)=
  $$
  E_p = m g (z - z_0),
  $$

  where $(z - z_0)$ is the elevation relative to a reference plane and $g$ is gravitational acceleration.

* **Flow energy:**

  (eq_Ef)=
  $$
  E_f = PV
  $$

  the energy required to push fluid across a boundary, which appears explicitly in **open-system** analyses (control volumes).

(subsec_microscopic_energy)=
#### Microscopic energy (disorganized)

The **internal energy**, $U$, accounts for the random microscopic motions and interactions of molecules:
translation, rotation, vibration, and potential energy between particles.

In systems with no chemical or phase change, variations in $U$ correspond mainly to changes in **thermal energy**, which correlates with **temperature**.

:::{admonition} Important: organized vs. disorganized energy
:class: warning
“Organized” energy (macroscopic motion or position) can be completely converted into “disorganized” energy (microscopic agitation $\to$ heat). The reverse is **not fully possible** — no process can transform all heat into work. This asymmetry anticipates the **second law of thermodynamics** and the concept of efficiency limits.
:::

---

(subsec_flow_work)=
### Work in simple compressible systems

For a **quasi-static** process involving a compressible substance, the infinitesimal **boundary (flow) work** is:

(eq_flow_work_diff)=
$$
\delta W = P\mathrm{d}V,
$$

or, per unit mass,

$$
\delta w = P\mathrm{d}v.
$$

The total work over a process between states 1 and 2 is obtained by integration:

(eq_flow_work_int)=
$$
W = \int_{1}^{2} P\mathrm{d}V.
$$

Graphically, this is the **area under the process curve** on a $P$–$V$ diagram.

Different processes (isobaric, isothermal, polytropic) lead to **different work values**, even if the initial and final states are the same — a clear indication of **path dependence**.

:::{admonition} Note: analytical forms of $W$
:class: note, dropdown

* **Isobaric** ($P=\text{const}$): $W = P,(V_2 - V_1)$
* **Isothermal ideal gas**: $W = nRT\ln(V_2/V_1)$
* **Polytropic** ($P V^n = \text{const}$, $n \neq 1$): $W = \tfrac{P_2 V_2 - P_1 V_1}{1 - n}$
:::

---

(subsec_heat)=
### Notion of heat

**Heat**, denoted $Q$, represents the **energy transferred solely due to a temperature difference** between systems. It always flows spontaneously from higher to lower temperature:

(eq_heat_direction)=
$$
T_{\text{hot}} > T_{\text{cold}}
\quad \Longrightarrow \quad
Q_{\text{hot}\to\text{cold}} > 0.
$$

Heat, like work, is a **process quantity** and not a property of the system. Once it crosses the boundary, it changes the system’s **internal energy** or other energy forms.

:::{admonition} Note: heat vs. thermal energy
:class: note, dropdown
“Heat” refers to **transfer**, not storage. Once transferred into a system, it becomes part of its **internal energy** $U$ (or **enthalpy** $h$ for open systems). Never describe the energy *contained* in a system as “heat”.
:::

---

(subsec_rates_specifics)=
### Rates and specific/molar forms

In practice, it is often convenient to express work and heat on a **specific (per unit mass)** basis, or as **rates (per unit time)**:

$$
\delta w = \frac{\delta W}{m}, \qquad
\delta q = \frac{\delta Q}{m}.
$$

and

$$
\dot{W} = \frac{\mathrm{d}W}{\mathrm{d}t}, \qquad
\dot{Q} = \frac{\mathrm{d}Q}{\mathrm{d}t}.
$$

These normalized forms simplify comparisons and are essential for **steady-flow** analyses.

---

(subsec_conceptual_closure_energy_work_heat)=
### Conceptual closure

* Energy changes describe **how** systems evolve, not just **what** they are.
* **Work** is the organized energy transferred through mechanical effects; **heat** is the disorganized energy transferred due to temperature difference.
* **Boundary work** in simple compressible systems satisfies $\delta W = P\mathrm{d}V$ and integrates to $W = \int P\mathrm{d}V$, making it explicitly **path-dependent**.
* The **first law** unifies all these forms through conservation: any energy entering or leaving a system as work or heat must correspond to a change in its total energy.
