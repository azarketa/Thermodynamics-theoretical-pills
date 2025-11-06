(sec_isentropic_efficiency)=
## The isentropic efficiency

The **thermal efficiency** measures how effectively a *cyclic* system converts heat into work. Once the **second law** was extended through **Clausius’s inequality**, the concept of **irreversibility** could be applied to individual, *non-cyclic* transformations. This made possible the definition of the **isentropic efficiency** — a measure of how closely a real process approaches the **ideal reversible (isentropic)** limit.

Whereas **thermal efficiency** applies to entire **cycles operating between reservoirs**, the **isentropic efficiency** applies to **single processes**, open or closed, whenever an **isentropic reference path** can be defined between the same inlet and outlet pressures.

---

(subsec_isentropic_irreversibility)=

### The isentropic efficiency as a measure of irreversibility
From **Clausius’s inequality**, every process satisfies

$$
s_2 - s_1 \ge \int_1^2 \frac{\delta q}{T},
$$

and equality holds for **reversible** processes.
If, in addition, the process is **adiabatic** ($\delta q=0$), then

$$
\Delta s = 0,
$$

and the transformation is **isentropic**, defining the *ideal limit* of performance.

To measure how far a real process departs from this limit, we compare two transformations between the **same inlet and outlet pressures** — an operational constraint common to most open steady-flow devices:

* The **actual (irreversible)** process, subscript **a**, ends at $(h_{2a}, s_{2a})$.
* The **isentropic (ideal)** process, subscript **s**, ends at $(h_{2s}, s_{2s}=s_1)$.

Both start from the same inlet conditions $(p_1, T_1, h_1, s_1)$, but the actual one shows $s_{2a}>s_{2s}$ due to **entropy generation**, requiring or delivering a different enthalpy change.

The **isentropic efficiency** $(\eta_{\text{is.}})$ is thus the **ratio between the ideal and actual enthalpy (or work) changes** corresponding to the same pressure variation — a normalized indicator of irreversibility $(0 < \eta_{\text{is.}} < 1)$.

---

(subsec_isentropic_open_systems)=
### Applications to open systems and the $h-s$ diagram

In **open steady-flow devices** such as **compressors**, **turbines**, and **nozzles**, the working fluid exchanges **enthalpy** and **entropy** with its surroundings.
For these systems, the **$h–s$ diagram** is the **natural representation choice** to visualize both energy exchange and irreversibility:

* Changes in **enthalpy ($h$)** represent **energy transfers** (as shaft work or kinetic energy).
* Changes in **entropy ($s$)** quantify **irreversibility** and the distance from the isentropic limit.

When comparing the **actual** and **isentropic** transformations, both are considered to operate between the **same inlet and outlet pressures**.
This reflects the **operational constraints** of these devices: the compressor must deliver a prescribed pressure rise, the turbine must expand the flow to a fixed exhaust pressure, and the nozzle must discharge into an environment with a given back pressure.
Enforcing the same pressure change ensures that both processes perform the **same functional duty**, and that any difference between them arises solely from **irreversibilities** within the device.

In this diagram, an **isentropic process** appears as a **vertical line** ($\Delta s=0$), while the **actual process** curves to the right ($\Delta s>0$), revealing the internal entropy generation.

:::{admonition} Note: the Mollier diagram
:class: note, dropdown
The **$h–s$ diagram** (or **Mollier diagram**) is a key graphical tool in thermodynamics.
It allows visual comparison between:

* **Isentropic lines** — vertical, $\Delta s = 0$ (ideal).
* **Real processes** — rightward-curving, $\Delta s > 0$ (irreversible).
* **Energy exchanges** — proportional to enthalpy differences.

This makes it particularly suited for devices like turbines, compressors, and nozzles, where **enthalpy variations dominate** the energy conversion process.
:::

:::{admonition} Note: choice of operational constraint
:class: note, dropdown

The **isentropic reference process** must always be defined under the **same boundary or end conditions** as the real one. The appropriate **operational constraint**—such as constant pressure, volume, or temperature—depends on the system’s configuration and purpose:

* In **open steady-flow systems**, this condition is typically a fixed **outlet pressure**, as mentioned above.
* In **closed systems**, however, other constraints (like a prescribed **volume** or **temperature change**) may apply.

By enforcing identical end conditions, the **isentropic efficiency** isolates the impact of **irreversibilities**, ensuring that any deviation from the ideal reflects only **entropy generation**, not differing operating targets.
:::

<br/>

(subsubsec_eta_compressor)=
#### Compressors

A single-inlet/single-outlet **compressor** increases the pressure of a gas through **work input**. Neglecting kinetic and potential energy effects, and writing the steady-state energy balance equation in specific terms:

$$
w_{\text{in}} = h_2 - h_1.
$$

The **isentropic efficiency of a compressor** is defined as:

:::{epigraph}
The ratio of the *work input required to raise the pressure of a gas to a specified value in an isentropic manner* to the *actual work input*.
:::

(eq_eta_comp)=
$$
\boxed{\eta_{\text{is., comp.}} = \frac{h_{2s} - h_1}{h_{2a} - h_1}}
$$

Here the numerator represents the *ideal* (minimum) energy input, and the denominator the *actual* one. The difference in signs and the order of integration limits follow from the fact that both energy and entropy **increase** during compression. Thus, the enthalpy differences are **positive** in the above expression.

For specific substance models:

* **Generic (tabulated) substances:** enthalpies from $h(p,T)$ or $h(p,s)$.

* **Ideal gases:**

  $$
  \begin{gather*}
  h_{2s} - h_1 = \int_{T_1}^{T_{2s}} c_p(T)\mathrm{d}T, \\[10pt]
  h_{2a} - h_1 = \int_{T_1}^{T_{2a}} c_p(T)\mathrm{d}T,
  \end{gather*}
  $$

  so that

  $$
  \boxed{\eta_{\text{is., comp.}} = \frac{\int_{T_1}^{T_{2s}} c_p(T)\mathrm{d}T}{\int_{T_1}^{T_{2a}} c_p(T)\mathrm{d}T}} \ .
  $$
  
* **Perfect gases ($c_p = \text{const.}$):**

  $$
  \boxed{\eta_{\text{is., comp.}} = \frac{T_{2s} - T_1}{T_{2a} - T_1}} \ .
  $$

<br/>

(subsubsec_eta_turbine)=

#### Turbines

A single-inlet/single-outlet **turbine** expands a high-pressure gas to a lower pressure, producing **shaft work**. Neglecting kinetic and potential energy changes, and writing the steady-state energy balance in specific terms:

$$
w_{\text{out}} = h_1 - h_2.
$$

The **isentropic efficiency of a turbine** is defined as:

:::{epigraph}
The ratio of the *actual work output* of the turbine to the *work output that would be obtained if the process between the same inlet state and exit pressure were isentropic.*
:::

(eq_eta_turb)=
$$
\boxed{\eta_{\text{is., turb.}} = \frac{h_1 - h_{2a}}{h_1 - h_{2s}}} \ .
$$

In expansions, energy and enthalpy **decrease**, so the sign and integration limits invert compared to compression, thus enforcing **positive** enthalpy differences.

* **Ideal gases:**
  
  $$
  \begin{gather*}
  h_{2a} - h_1 = \int_{T_1}^{T_{2a}} c_p(T)\mathrm{d}T, \\[10pt]
  h_{2s} - h_1 = \int_{T_1}^{T_{2s}} c_p(T)\mathrm{d}T,
  \end{gather*}
  $$

  yielding

  $$
  \boxed{\eta_{\text{is., turb.}} = \frac{\int_{T_{1}}^{T_{2a}} c_p(T)\mathrm{d}T}{\int_{T_{1}}^{T_{2s}} c_p(T)\mathrm{d}T}} \ .
  $$
  
* **Perfect gases ($c_p = \text{const.}$):**

  $$
  \boxed{\eta_{\text{is., turb.}} = \frac{T_1 - T_{2a}}{T_1 - T_{2s}}} \ .
  $$

<br/>

(subsubsec_eta_nozzle)=
#### Nozzles

A **nozzle** converts **enthalpy** into **kinetic energy** of a fluid stream. The steady-flow energy equation (neglecting heat and potential energy) in specific terms gives:

$$
h_1 + \frac{c_1^2}{2} = h_2 + \frac{c_2^2}{2}.
$$

The **isentropic efficiency of a nozzle** is defined as:

:::{epigraph}
The ratio of the *actual kinetic energy* of the fluid at the nozzle exit to the *kinetic energy* that would be achieved if the same process (from the same inlet state to the same exit pressure) were isentropic.
:::

(eq_eta_noz)=
$$
\boxed{\eta_{\text{is., noz.}} = \frac{c_{2a}^2}{c_{2s}^2} = \frac{h_1 - h_{2a}}{h_1 - h_{2s}}} \ .
$$

For an **ideal gas:**

$$
\begin{gather*}
h_1 - h_{2a} = \int_{T_{2a}}^{T_1} c_p(T)\mathrm{d}T, \\[10pt]
h_1 - h_{2s} = \int_{T_{2s}}^{T_1} c_p(T)\mathrm{d}T,
\end{gather*}
$$

so that

$$
\boxed{\eta_{\text{is., noz.}} = \frac{c_{2a}^2}{c_{2s}^2} = \frac{\int_{T_{2a}}^{T_1} c_p(T)\mathrm{d}T}{\int_{T_{2s}}^{T_1} c_p(T)\mathrm{d}T}} \ .
$$

For **perfect gases ($c_p = \text{const.}$):**

$$
\boxed{\eta_{\text{is., noz.}} = \frac{c_{2a}^2}{c_{2s}^2} = \frac{T_1 - T_{2a}}{T_1 - T_{2s}}} \ .
$$

<br/>

:::{admonition} Important: summary of isentropic efficiency expressions
:class: warning

| **Device** | **Generic / tabulated substances** | **Ideal gases ($c_p(T)$)** | **Perfect gases ($c_p$ const.)** | **Interpretation** |
| :-  | :- | :- | :- | :- |
| **Compressor** | $\dfrac{h_{2s}-h_1}{h_{2a}-h_1}$   | $\dfrac{\int_{T_1}^{T_{2s}} c_p(T)\mathrm{d}T}{\int_{T_1}^{T_{2a}} c_p(T)\mathrm{d}T}$     | $\dfrac{T_{2s}-T_1}{T_{2a}-T_1}$ | Fraction of ideal compression work achieved |
| **Turbine**    | $\dfrac{h_1-h_{2a}}{h_1-h_{2s}}$   | $\dfrac{\int_{T_{2a}}^{T_{1}} c_p(T)\mathrm{d}T}{\int_{T_{2s}}^{T_{1}} c_p(T)\mathrm{d}T}$ | $\dfrac{T_1-T_{2a}}{T_1-T_{2s}}$ | Fraction of ideal expansion work delivered  |
| **Nozzle**     | $\dfrac{c_{2a}^2}{c_{2s}^2}=\dfrac{h_1-h_{2a}}{h_1-h_{2s}}$   | $\dfrac{c_{2a}^2}{c_{2s}^2}=\dfrac{\int_{T_{2a}}^{T_1} c_p(T)\mathrm{d}T}{\int_{T_{2s}}^{T_1} c_p(T)\mathrm{d}T}$     | $\dfrac{c_{2a}^2}{c_{2s}^2}=\dfrac{T_1-T_{2a}}{T_1-T_{2s}}$ | Fraction of ideal kinetic energy conversion |
:::

---

(subsec_conceptual_closure_isentropic_eff)=
### Conceptual closure

* The **isentropic efficiency** generalizes the **second law** from cyclic to single processes, quantifying the **departure from reversibility**.
* It expresses how closely a real transformation approaches its **isentropic (adiabatic and reversible)** counterpart.
* By construction, both real and ideal processes are compared under the **same operational constraint** (e.g. identical outlet pressure in open systems).
* **Entropy generation** increases the required input (in compressors) or reduces the useful output (in turbines and nozzles), lowering $\eta_{\text{is.}}$.
* For **generic or tabulated substances**, efficiency is evaluated from **enthalpy differences**; for **ideal gases**, through **temperature-dependent heat capacities**; and for **perfect gases**, by **temperature ratios**.
* The **$h-s$ (Mollier) diagram** provides an intuitive visualization: the vertical line represents the **isentropic limit**, and the deviation to the right reflects **irreversibility**.
* All isentropic efficiencies satisfy $0 < \eta_{\text{is.}} < 1$, with $\eta_{\text{is.}} = 1$ defining the **reversible adiabatic limit**.
* In essence, $\eta_{\text{is.}}$ bridges **energy** and **entropy** analyses — linking **useful work** and **irreversibility** within a single, dimensionless measure of performance.
