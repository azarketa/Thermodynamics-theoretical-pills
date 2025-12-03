(sec_reversible_irreversible_processes)=
## Reversible and irreversible processes

Thermodynamic processes can occur in two fundamentally different ways, depending on whether they can be perfectly undone or not. This distinction lies at the heart of the **$2^{\text{nd}}$ law**, since it separates **idealized behavior** (reversible) from **real behavior** (irreversible).

---

(subsec_definition_reversibility)=
### Definition of reversibility

A **reversible process** is one that can be *completely undone*: both the system and its surroundings could, in principle, return to their original states **without any net macroscopic change** in the environment.
Such processes must proceed **infinitely slowly** (quasi-statically) and **without dissipative effects** — that is, without friction, viscosity, turbulence, electrical resistance, or finite temperature differences during heat transfer.

Conversely, an **irreversible process** is one that **cannot be reversed** without leaving some permanent trace on the surroundings.
In these processes, **dissipation** is unavoidable: friction, viscous flow, spontaneous mixing, unrestrained expansion, or heat transfer through a finite temperature difference all contribute to the irreversibility of real phenomena.

:::{important}

**REVERSIBILITY AS AN IDEALIZATION**

Reversible processes are **ideal constructs**.
They do not occur in practice but serve as **theoretical limits** that real, irreversible processes can only approach — never attain.
:::

---

(subsec_internal_external_reversibility)=
### Internal and external reversibility

Reversibility may be considered from two complementary standpoints:

* A process is said to be **internally reversible** if *no dissipative effects occur within the system itself*.
  The system passes through a sequence of equilibrium states, and all internal interactions (mechanical, thermal, etc.) are ideal and lossless.

* A process is **externally reversible** if the **interactions between the system and its surroundings** — those across the **boundary** — occur **without finite gradients** or **net changes** in the environment.
  For instance, heat transfer between the system and its surroundings must occur through an **infinitesimal temperature difference** to be externally reversible.
  Conversely, if heat flows across a **finite temperature difference**, the process becomes **externally irreversible**, even if it remains **internally reversible** within the system.

In practice, most real processes may be **internally reversible** (if the system is idealized as free of internal friction, turbulence, or viscosity) but **externally irreversible**, since the exchanges of heat or work with the environment occur across **finite temperature or pressure gradients** that leave a detectable change in the surroundings.

:::{note}

**EXAMPLE OF AN IRREVERSIBLE PROCESS**

Consider a **can of soda** initially at $5 \ ^{\circ}\mathrm{C}$ placed in a room at $20 \ ^{\circ}\mathrm{C}$.
Heat naturally flows from the warmer air to the colder can until both reach the same temperature.
To restore the can to its initial condition, one would have to use a **refrigerator**, which removes heat from the can and expels it to the room air.

At the end of this restoration, the can regains its initial state, but the **room has warmed slightly** — it has absorbed the heat rejected by the refrigerator.
Hence, although the system (the can) is back to its initial condition, the **environment is not**.
The overall process is therefore **irreversible**.

However, the **heat transfer within the can** — that is, inside the system’s boundaries — can be approximated as **internally reversible** if it proceeds quasi-statically and without dissipative effects.
The **irreversibility** of the process arises from the **finite temperature difference** between the can and the room, i.e. from the **external interaction** between the system and its surroundings.

:::

---

(subsec_interest_reversibility)=
### Why reversibility matters

Even though reversible processes are idealizations, distinguishing them from irreversible ones is essential for two main reasons:

1. **Analytical simplicity:**
   Reversible processes evolve **quasi-statically**, passing through a continuous series of equilibrium states.
   This makes them **mathematically tractable** and allows us to apply the thermodynamic relations exactly at every step.

2. **Theoretical benchmarks:**
   Reversible processes serve as **reference limits** for real systems:

   * For **heat engines**, they yield the **maximum possible efficiency**.
   * For **refrigeration cycles and heat pumps**, they require the **minimum possible work input**.

Thus, reversible processes define the **upper and lower performance bounds** for all practical thermodynamic cycles, providing the standard against which **real, irreversible behavior** is measured.

:::{note}

**THE GLOBAL OR UNIVERSAL IRREVERSIBILITY**

Because one can always define a larger system that includes both the original **system and its environment**, it is conceptually possible to enclose *all interactions* within a single, **isolated system** — the so-called **thermodynamic universe**.
In this all-encompassing view, there is **no distinction between internal and external irreversibility**: every dissipative effect, whether inside the system or at its boundaries, contributes to the **overall irreversibility** of the universe.

This idea leads directly to one of the most profound implications of the $2^{\text{nd}}$ law:
the **total irreversibility of the universe increases** with every real process, and **no natural transformation can occur in a perfectly reversible way** when viewed as a whole.

:::

---

(subsec_conceptual_closure_reversibility)=
### Conceptual closure

* **Reversible processes** are **idealized** transformations that can be undone without leaving any macroscopic change in the surroundings. They proceed **quasi-statically** and **without dissipation**, allowing the system to pass continuously through equilibrium states.
* **Irreversible processes**, in contrast, are **real** and **spontaneous**: they involve friction, viscosity, turbulence, or finite temperature gradients that prevent exact retracing of the initial state.
* The distinction between **internal** and **external** reversibility clarifies whether dissipation occurs within the system or at its boundary with the environment. In reality, most processes are internally reversible but externally irreversible.
* Although true reversibility is unattainable, **reversible models** provide **theoretical reference limits** — defining the **maximum efficiency** of heat engines and the **minimum work input** for refrigeration cycles.

In essence, reversibility marks the **ideal boundary** of thermodynamic perfection, while the $2^{\text{nd}}$ law reminds us that **real processes always carry an irreversible cost** — the signature of the thermodynamic arrow of time.
