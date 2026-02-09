(sec_systems_surroundings_boundaries)=
## Systems, surroundings, and boundaries

Thermodynamics begins by defining *what* we are studying and *how* we separate it from the rest of the universe.
This section establishes the fundamental language for that task: **systems**, their **boundaries**, and the **surroundings** that interact with them.
We will learn how to classify systems according to the exchanges that occur across their boundaries,
and how boundary properties themselves determine the type of thermodynamic interaction possible — mass, heat, or work.

---

(subsec_defining_the_system)=
### Defining the system

Thermodynamic analysis always starts by deciding what part of the physical world we want to study. This portion is called the **system**, and it is the central object of thermodynamic reasoning.

To carry out a thermodynamic analysis, the first step is to decide **what the system actually is**. A **system** is any defined region of space or quantity of matter that we isolate — physically or conceptually — to study how it behaves under given conditions. This choice depends entirely on the question we want to answer.

* If we want to know **how the temperature of a classroom changes** during a lesson, the system is **the air contained within the room**.
* If we want to know **how a freezer cools**, the system is **the air or refrigerant inside the freezer cavity**.
* If we want to determine **the power produced by a combustion engine**, the system is **the mixture of air and fuel inside the piston–cylinder set**.
* If we want to study **how a steel block heats up** inside a furnace, the system is **the piece of steel itself**.

These examples show that what matters is not *what the system is made of*, but *why we are analyzing it*.
The definition of “system” is both **functional** and **operational**, not intrinsic: we choose it according to the purpose of the analysis.

---

(subsec_boundaries_and_environment)=
### Boundaries and environment

Once the system is defined, we conceptually surround it with an **imaginary surface** that separates it from everything else. Everything external to the system is called the **surroundings**, and the surface that separates them is called the **boundary**. This boundary determines what can or cannot cross between the system and its surroundings.

* For the air in a room → **walls, windows, and objects** inside form the boundary.
* For the freezer → the **insulated box and door** act as the boundary.
* For the piston–cylinder system → **metal walls and the moving piston face** are the boundary.
* For the steel piece → the **external surface** of the metal is the boundary.

Everything outside that surface is the **surroundings**.
The combination of the system and its surroundings is known as the **thermodynamic universe** — the entire domain involved in a process.

:::{note}

**BOUNDARIES CAN BE REAL OR IMAGINARY**

A boundary does not have to be a tangible surface. It can be purely conceptual — an abstract division that helps us track what crosses between the system and its environment.
Thermodynamics works precisely because such a separation can always be defined.
:::

---

(subsec_the_role_of_interactions)=
### The role of interactions

Thermodynamics focuses on **changes that occur within a system** — changes in temperature, pressure, volume, or internal energy.
But those changes exist *only* because of interactions with the surroundings.
Energy and, in some cases, matter pass through the boundary and cause transformations inside.

We can therefore think of the thermodynamic system as a **black box**:
we are not concerned with every microscopic event inside, only with the *inputs* and *outputs* that cross the boundary.

* We do not need to know the detailed mechanisms of molecular motion.
* We only need to quantify what **enters and leaves** as heat, work, or mass.
* By observing those exchanges, we can infer the internal evolution of the system.

:::{tip}

**TREAT THE SYSTEM AS A "BLACK BOX"**

By focusing on boundary interactions — not inner mechanisms — thermodynamics can analyze extremely complex systems (reactors, turbines, biological cells) using the same universal laws.
If you can identify what crosses the boundary, you can apply thermodynamics.
:::

---

(subsec_simplifications_and_the_macroscopic_conception)=
### Simplifications and the macroscopic conception

Because our aim is to understand and model engineering systems, we introduce several **simplifications** that make the analysis tractable and meaningful.

1. **Typical fluids:** we will use **air and water** as the standard fluids representing gases and liquids, respectively. They are paradigmatic in energy systems and cover most practical applications.

2. **Excluded effects:** we will neglect phenomena that fall outside the mechanical or thermal domain — such as rheological (viscous time-dependent), electrical, magnetic, or chemical reactions — unless explicitly stated.

3. **Macroscopic viewpoint:** our approach will be **classical or phenomenological** thermodynamics. We are interested in the *average* or *overall* behavior of systems rather than their atomic details. This contrasts with the **microscopic conception**, used in *statistical thermodynamics*, which explains the same laws in terms of molecular behavior.

:::{important}

**CLASSICAL VS. MICROSCOPIC VIEWPOINTS**

Classical thermodynamics describes **macroscopic behavior** using measurable properties (pressure, temperature, volume, etc.) without referring to the microscopic structure of matter.
Statistical or microscopic thermodynamics explains *why* those macroscopic laws emerge.
:::

---

(subsec_types_of_systems)=
### Types of systems

Depending on what the boundary allows to cross, we classify systems as **isolated**, **closed**, or **open**.
This classification reflects which kinds of interactions — energy and/or mass — are possible with the surroundings.

1. **Isolated system:**

   * Exchanges **neither mass nor energy** with the surroundings.
   * The boundary is *impermeable* (no mass flow), *rigid* (no work), and *adiabatic* (no heat).
   * It is an *idealization* — in practice, no system is perfectly isolated, though a Dewar flask is a close approximation.

2. **Closed system** (control mass):

   * Exchanges **energy** (heat and/or work) but **not mass** with its surroundings.
   * At least one part of the boundary allows thermal or mechanical interaction.
   * Example: a piston–cylinder assembly.

3. **Open system** (control volume):

   * Exchanges **both energy and mass** with its surroundings.
   * Boundaries may be *flexible*, *diathermic*, or *permeable* depending on the specific process.
   * Example: a fluid stream in a pipe, a compressor, or a turbine.

::::{important}

**CLASSIFICATION BY BOUNDARY INTERACTION**

The essential difference lies in what can cross the boundary. We can name $E_{\text{sys.}}$ the total energy of the system, and $m_{\text{sys.}}$ the mass contained in it. Their variations are represented by the $\Delta$ symbol, i.e. $\Delta E_{\text{sys.}}$ and $\Delta m_{\text{sys.}}$. The different types of boundaries are constraied by different interaction modes: 

* **Isolated:**  no energy, no mass $\rightarrow \Delta E_{\text{sys.}} = 0$, $\Delta m_{\text{sys.}} = 0$
* **Closed:**  energy only $\rightarrow \Delta E_{\text{sys.}} \neq 0$, $\Delta m_{\text{sys.}} = 0$
* **Open:**  energy and mass $\rightarrow \Delta E_{\text{sys.}} \neq 0$, $\Delta m_{\text{sys.}} \neq 0$

So, as a tabular-form summary:

| **System Type** | $\Delta E_{\text{sys.}}$ | $\Delta m_{\text{sys.}}$ |
| :-------------- | :----------------------: | :----------------------: |
| **Isolated** | $= 0$ | $= 0$ |
| **Closed** | $\neq 0$ | $= 0$ |
| **Open** | $\neq 0$ | $\neq 0$ |

The figure below shows the types of boundaries in an illustrative way, attending to the types of interactions with the surroundings.

:::{figure} 1_fundamentals_figs/system_boundary_types.svg
:name: fig-system-boundaries
:width: 90%
:align: center

Generic system classification according to the interchange constraints imposed by the boundaries.
:::

::::

---

(subsec_terminology_of_boundary_behavior)=
### Terminology of boundary behavior

To describe the physical nature of boundaries more precisely, thermodynamics uses a simple and systematic terminology:

| Interaction Type | Boundary that **prevents** it | Boundary that **allows** it |
| ---------------- | ----------------------------- | --------------------------- |
| **Mass** | Impermeable | Permeable |
| **Heat** | Adiabatic | Diathermic |
| **Work** | Rigid | Flexible |

:::{note}

**MEANING OF BOUNDARY DESCRIPTORS**

Each term describes *how the boundary behaves* with respect to a specific mode of interaction.
For instance, a **rigid, adiabatic, impermeable** wall defines an ideal **isolated system**.
Conversely, a **flexible, diathermic, permeable** boundary defines the most general — and most realistic — case, that of an **open system**.
With the notions developed so far, we can conceive a combined table that establishes the relationships between the conceptual boundary types and the physical realizations they either allow or constrain.

| **System Type** | $\Delta E_{\text{sys.}}$ | $\Delta m_{\text{sys.}}$ | **Boundary — Mass** |   **Boundary — Heat**   | **Boundary — Work** |
| :-------------- | :----------------------: | :----------------------: | :-----------------: | :---------------------: | :-----------------: |
| **Isolated**    |           $= 0$          |           $= 0$          |     Impermeable     |        Adiabatic        |        Rigid        |
| **Closed**      |         $\neq 0$         |           $= 0$          |     Impermeable     | Diathermic or Adiabatic |  Flexible or Rigid  |
| **Open**        |         $\neq 0$         |         $\neq 0$         |      Permeable      | Diathermic or Adiabatic |  Flexible or Rigid  |

:::

---

(subsec_fluid_systems_and_the_coninuum_hypothesis)=
### Fluid systems and the continuum hypothesis

Although thermodynamics applies to solids, liquids, and gases, engineering practice concentrates on **fluids**, because they are the working media in almost all energy systems — turbines, compressors, engines, pumps, condensers, and heat exchangers.

For these analyses, we adopt the **continuum hypothesis**:
we assume that a fluid can be treated as a continuous medium in which properties such as density, pressure, and temperature vary smoothly in space and time.

Mathematically, we consider that within a small representative volume large enough to contain many molecules but small compared to the whole system,

(eq_continuum_hypothesis_exps)=
$$
\rho(\mathbf{x}) ; T(\mathbf{x}) ; P(\mathbf{x})
$$

are well-defined, continuous functions.

:::{tip}

**THE CONTINUUM HYPOTHESIS AS A BRIDGE**

The continuum approximation is what links thermodynamics with fluid mechanics.
It allows us to define macroscopic fields, apply differential relations, and treat real gases and liquids as continuous media obeying the same conservation principles.
:::

---

(subsec_systems_surroundings_boundaries_conceptual_closure)=
### Conceptual closure

The basic elements of thermodynamic analysis are now in place:

* The **system**, the portion of the universe under study.
* The **boundary**, which may be physical or imaginary.
* The **surroundings**, everything else capable of interacting with the system.
* The **types of system**, defined by which exchanges (energy, mass) are possible.
* The **simplifications** that focus our study on mechanical and thermal phenomena, mainly in **fluid systems** treated as **continuous media**.

:::{important}

**ESSENCE OF THE MACROSCOPIC APPROACH**

Classical thermodynamics does not attempt to describe atomic mechanisms.
It studies how systems exchange energy and matter with their surroundings and how those exchanges determine the macroscopic state of the system — temperature, pressure, volume, and energy content.
:::
