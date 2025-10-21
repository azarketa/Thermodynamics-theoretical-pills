(sec_ideal_real_gases)=
## Ideal and Real Gases

When modeling gases, the first challenge arises from their **diversity**.
* Do air and carbon monoxide behave alike?
* Does hydrogen act the same way as methane, or butane as ethanol vapor?

Although the molecules composing these gases differ, their **macroscopic behavior** can often be described through common trends — provided certain simplifications are made.
These simplifications define the **ideal gas model**, which serves as a reference for understanding and quantifying the deviations exhibited by **real gases**.

---

(subsec_ideal_gas_assumptions)=
### Assumptions of the Ideal Gas Model

Two physical assumptions allow us to treat gases as ideal:

1. **Negligible molecular volume** —
   The individual particles occupy a vanishingly small portion of the total volume.
   This approximation holds well at **low pressures**, where the mean distance between molecules is large.

2. **Negligible intermolecular forces** —
   Interactions between molecules are weak compared to their kinetic energy.
   This assumption becomes valid at **high temperatures**, where motion dominates attraction or repulsion.

:::{admonition} Important: Domain of validity
:class: warning
The ideal gas model applies accurately under conditions of **low density and high temperature**.
Under these limits, all gases tend to exhibit similar thermodynamic behavior, regardless of their molecular structure.
:::

---

(subsec_ideal_gas_equation)=
### The Ideal Gas Equation

The state relation for an ideal gas is expressed by the equation:

:::{math}
:label: eq_ideal_gas_molar_form
P{\cdot}V = n{\cdot}R_u{\cdot}T \ \Longrightarrow \ PV = nR_uT
:::

where
$P$ = pressure $[\text{Pa}]$,
$V$ = volume $[\text{m}^3]$,
$n$ = amount of substance $[\text{mol}]$,
$T$ = temperature $[\text{K}]$,
and $R_u$ = universal gas constant $8.314,[\text{J}/(\text{mol}{\cdot}\text{K})]$.

The **specific gas constant** $R$ is defined as

:::{math}
:label: eq_specific_gas_constant
R = \frac{R_u}{M}
:::

where $M$ is the **molar mass** of the gas $[\text{kg}/\text{mol}]$.
Since $M = m/n$, we can rewrite the ideal gas equation in its **mass-based** form:

:::{math}
:label: eq_ideal_gas_mass_form
PV = mRT
:::

and, dividing by the mass $m$, in its **specific** form:

:::{math}
:label: eq_ideal_gas_specific_form
Pv = RT
:::

where $v = V/m$ is the **specific volume** $[\text{m}^3/\text{kg}]$.

:::{admonition} Note: Connection with the state postulate
This relation links the three **intensive properties** $p$, $v$, and $T$ identified in {ref}`in the previous section <sec_characterization_substances>`.
It satisfies the generic state condition {ref}`expressed before <eq_general_state_equation>`.
:::

---

(subsec_real_gases)=
### Real Gases and Deviations from Ideal Behavior

In real conditions, gases deviate from ideality because **molecules occupy volume** and **interact** through attractive or repulsive forces.
To quantify such deviations, the **compressibility factor** $Z$ is introduced:

:::{math}
:label: eq_compressibility_factor
Z = \frac{Pv}{RT}
:::

For an ideal gas, $Z=1$.
For real gases, $Z$ differs from unity — being typically **less than 1** near condensation (due to attraction) and **greater than 1** at very high pressures (due to repulsion).

#### Empirical and semi-theoretical models

Several equations of state have been developed to capture these deviations:

* **Van der Waals equation** — introduces corrections for finite molecular size and intermolecular attraction:

  :::{math}
  :label: eq_van_der_waals
  \left(P + a\frac{1}{v^2}\right)(v - b) = RT
  :::

  where $a$ and $b$ are empirical constants depending on the gas.
  The term $a/v^2$ accounts for attractive forces; $b$ represents the excluded molecular volume.

* **Virial equation** — expresses deviations as a power series in $1/v$:

  :::{math}
  :label: eq_virial_equation
  \frac{Pv}{RT} = 1 + \frac{B(T)}{v} + \frac{C(T)}{v^2} + \dots
  :::

  where $B(T)$, $C(T)$, $\ldots$ are temperature-dependent **virial coefficients**.
  This form is especially useful for experimental data fitting and for gases near the ideal limit.

:::{admonition} Tip: Interpreting real-gas corrections

* The **Van der Waals** model gives a simple physical interpretation of molecular attraction and repulsion.
* The **Virial** form provides flexible, accurate representation of measured data.
* Both reduce to the ideal-gas law when $a=b=0$ or when $B=C=\dots=0$.
  :::

---

(subsec_interpretation_ideal_real_gas)=

### Interpretation

The ideal-gas law describes the simplest limit of gas behavior, while real-gas models add successive layers of correction.
Together they define a continuous conceptual ladder from pure theory to practical reality.

:::{admonition} Important: Continuity between ideal and real models
:class: warning
The **ideal gas** is not a separate physical entity but the **limiting case** of a real gas under dilute conditions.
Every real gas approaches ideal behavior as pressure → 0 and temperature → ∞.
:::

---

(subsec_conceptual_closure_ideal_real_gases)=

### Conceptual Closure

* The **ideal gas model** arises from neglecting molecular volume and interactions, leading to the law $Pv = RT$.
* **Real gases** deviate from this law due to finite particle size and intermolecular forces.
* Corrective models — **Van der Waals**, **Virial**, and **compressibility-factor** formulations — quantify these deviations.
* At low pressures and high temperatures, all gases converge toward the **ideal limit**, providing a consistent reference for thermodynamic analysis.

---

