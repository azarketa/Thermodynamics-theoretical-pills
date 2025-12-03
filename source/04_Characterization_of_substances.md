(sec_characterization_of_substances)=
## Characterization of substances

Once the basic concepts of {ref}`equilibrium, temperature scales and processes<sec_equilibrium_temperature_processes>` have been established,
the next step is to understand how these notions apply to the **real materials** that make up thermodynamic systems.
Every system consists of *substances*, and the task of Thermodynamics is to characterize their states and transformations.

The key questions are:

* What do we mean by a *substance*?
* How can we describe the *state changes* that substances undergo?

---

(subsec_classification_substances)=
### Classification of substances

Substances are categorized according to their **chemical composition** and **homogeneity**.

* **Pure substances**: uniform and invariable chemical composition.

  * *Simple*: composed of a single chemical element (e.g. $\text{H}_2$, $\text{O}_2$).
  * *Compound*: composed of more than one element (e.g. $\text{H}_2\text{O}$, $\text{CO}_2$).

* **Mixtures**: physical combinations of two or more pure substances.

  * *Homogeneous mixtures*: uniform composition throughout (e.g. air, aqueous solutions).
  * *Heterogeneous mixtures*: composition varies spatially (e.g. oil and water).

The **phase** of a substance refers to a spatial region where its physical properties are uniform.
In thermodynamics, *phase changes* always imply *state changes* — the two notions are considered synonymous.

:::{note}

**PHASES AS THERMODYNAMIC DOMAINS**

A *phase* defines a region of physical uniformity in both composition and properties.
When a substance changes phase, its thermodynamic state changes discontinuously.
:::

Although Thermodynamics can describe any phase of any substance, the emphasis here will be on **fluids** — particularly **gases** — since they constitute the working media of most thermal systems.

---

(subsec_state_postulate)=
### State postulate

The study of thermodynamic systems aims to describe their equilibrium states through measurable properties.
The central question is: **how many independent properties are required to define the state of a system?** This is answered by the **State Postulate**, formulated by Kline and Köenig back in 1957:

:::{epigraph}
The equilibrium state of a system is completely specified when $n + 1$ independent thermodynamic variables are known,
where $n$ is the number of independent ways to perform quasi-static, reversible work on the system.
:::

In practice:

* For most **fluids**, the relevant form of reversible work is **compression or expansion work**.
* A **simple system** is one that allows reversible work in **only one way** (e.g. by changing its volume).
* Systems capable of multiple kinds of work (electrical, elastic, magnetic, etc.) are **compound systems**, but these can often be divided into simple subsystems whose only reversible work is of the compression/expansion type.

:::{important}

**COROLLARY OF THE STATE POSTULATE**

**Simple compressible systems** — the main focus of this course — require only **two independent properties** to define their equilibrium state.
:::

:::{note}

**INDEPENDENT VARIABLES**

The properties chosen to describe a state must be *intensive* (independent of system size and geometry) and *mutually independent*.
For fluid systems, the primary variables are **pressure** ($p$), **specific volume** ($v = 1/\rho$), and **temperature** ($T$).
:::

---

(subsec_equation_of_state)=
### Equation of state (EOS)

If any one of the three fundamental variables ($p$, $v$, $T$) can be expressed as a function of the other two, the system is fully characterized, and the **state postulate** is satisfied. Such a relation is known as the **equation of state (EOS)**.

(eq_general_state_equation)=
$$
f(p, v, T) = 0
$$

This general expression defines how the thermodynamic properties of a substance are interrelated.
Specific forms of this function — such as the **model of perfect gases** — will be explored next.

:::{tip}

**WHY EQUATIONS OF STATE MATTER**

Equations of state provide the bridge between theory and measurable reality.
They make it possible to compute one property (e.g. pressure) from others (e.g. temperature and volume),
thereby connecting the abstract framework of Thermodynamics to experimental data.
:::

---

(subsec_conceptual_closure_characterization_substances)=
### Conceptual closure

* Substances define the physical basis of thermodynamic systems; their composition and phase determine how they behave and transform.
* The **State Postulate** specifies how many independent variables are required to describe a system completely.
* For **simple compressible systems**, two independent intensive properties (commonly $p$, $v$, and $T$) are sufficient.
* Expressing one of these properties as a function of the other two gives the **EOS**, the mathematical link between measurable quantities.
* These principles provide the foundation for the study of {ref}`Models of Gases<sec_models_gases>`,
  where specific functional forms of the EOS are introduced.
