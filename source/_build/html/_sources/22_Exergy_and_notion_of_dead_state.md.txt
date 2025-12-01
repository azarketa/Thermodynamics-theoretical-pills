(sec_exergy_and_dead_state)=
## Exergy and the notion of dead state

The **$1^{\text{st}}$** and **$2^{\text{nd}}$ laws of thermodynamics** express two fundamental but distinct aspects of all physical transformations.

* The **$1^{\text{st}}$ law** concerns the **quantity of energy**, establishing that energy is conserved — it can neither be created nor destroyed, only transformed.
* The **$2^{\text{nd}}$ law** concerns the **quality of energy**, stating that every real process generates **entropy**, which remains constant only under perfectly reversible conditions.

These two principles together distinguish **how much energy** exists from **how useful** that energy is.
While energy is conserved, its *usefulness* continuously diminishes as entropy increases.

Because entropy introduces a **direction to time** — the irreversible “arrow” of natural processes — the $1^{\text{st}}$ law is a *quantitative* principle, and the second is a *qualitative* one.
However, these quantities are **incommensurable**:
energy is measured in **joules $\text{J}$**, whereas entropy is expressed in **joules per Kelvin $\text{J}/\text{K}$**.
Thus, one cannot directly compare or combine them in their native form.

This raises a key question:

:::{epigraph}
Can the *quality* of energy — as expressed by the $2^{\text{nd}}$ law — be translated into an **energetic measure**?
:::

If so, we could quantify **irreversibilities** in energy terms, assessing how much of the total energy remains *useful* for producing work.

The answer lies in combining the $1^{\text{st}}$ and $2^{\text{nd}}$ laws.
By doing so, we obtain a new quantity — the **exergy** — which measures the **maximum useful work** that can be extracted as a system comes into equilibrium with its environment.
Exergy is therefore **not an independent principle**, but a **derived property**, a synthesis of both laws that expresses the energetic *value* of energy itself.

However, defining exergy requires understanding what it means for a system to be in *equilibrium* with its environment — the concept of the **dead state**.

::::{admonition} Note: exergy and availability
:class: note, dropdown

The notion of **exergy** first appeared under the name **availability**, reflecting an early attempt to quantify how much of a system’s energy could be **converted into useful work** under the conditions set by its **environment**; or, in other words, the concern that guided the conception of the term **availability** was:

:::{epigraph}
How much energy can be extracted from a system placed in a given environment?
:::

The answer depends not only on the system’s internal state but also on that of its surroundings. When the two are in **complete equilibrium** — the **dead state** — no spontaneous processes can occur, and the system’s energy, though present, is **unavailable**. A clear example is the **atmosphere**, which contains immense energy but cannot deliver work as long as it remains uniform. Only when **gradients** of temperature, pressure, or composition exist does the system possess **exergy** — the measurable *potential to produce work*.
::::

---

(subsec_dead_state_and_work_potential)=
### The dead state and work potential

A system is said to be in its **dead state** when it is in **complete thermodynamic equilibrium with the environment** — that is, when no gradients of temperature, pressure, or chemical potential exist between them.
At that point, **no more work** can be extracted from the system.

The **atmosphere** illustrates this well: although it contains an immense amount of energy, a device in equilibrium with it cannot extract any work, since there are no property differences to exploit.
To generate work, a system must first be **out of equilibrium** — having a higher temperature, pressure, or some other potential difference relative to its surroundings.

Hence, extracting energy from a system effectively means extracting **organized, useful energy** — that which can perform **mechanical work**.
The **maximum work** obtainable as a system passes from a given *initial state* to the *dead state* is called its **work potential**.

Formally, since work is a **path function**, one may write:

$$
W = f(\text{initial state}, \text{process path}, \text{final state})
$$

In an **exergetic analysis**:

* The **initial state** is given and fixed.
* The **final state** corresponds to the **dead state**, where equilibrium with the environment is achieved.
* The **process path** is assumed **reversible**, since only reversible transformations yield **maximum work**.

Any **irreversibility** within the system or its immediate surroundings reduces this theoretical maximum, resulting in **exergy destruction**.

:::{admonition} Important: meaning of exergy
:class: warning
Exergy quantifies the **maximum useful work** obtainable as a system moves reversibly from its initial state to the **dead state**.
It represents the **upper limit** of performance permitted by thermodynamic laws — the boundary between the *usable* and *unusable* portions of energy.
:::

---

(subsec_boundaries_and_dead_state_considerations)=
### Boundaries, irreversibilities, and final considerations on the dead state

When studying **exergy**, it is essential to define precisely what is meant by the **system**, its **surroundings**, and its **environment**, since these distinctions determine **where irreversibilities occur** and **how work potential is lost**.

* The **surroundings** comprise everything outside the system’s boundary.
* The **immediate surroundings** are the portion of those surroundings directly affected by the process — where gradients of temperature, pressure, or velocity exist.
* The **environment** refers to the large, unaffected reservoir that defines the **reference conditions** for the **dead state**.

Irreversibilities appear both **within the system** and in its **immediate surroundings**, where finite differences in temperature or pressure drive transfers of heat or mass.
It is in these regions of non-equilibrium that **entropy generation** and, consequently, **exergy destruction** take place.

The concept of **exergy** extends beyond systems that directly produce mechanical work.
Even if a device performs no shaft work, as long as it is **not in equilibrium** with its environment, it possesses a **potential to do work** — a stored capacity for useful energy conversion.

Indeed:

* If the system’s **temperature** is greater than that of the environment ($T_f > T_{\text{env.}}$), a **heat engine** could, in principle, operate between them to produce work.
* If its **pressure** is higher than the ambient value ($P_f > P_{\text{env.}}$), expansion could yield mechanical energy.
* If the system possesses **kinetic**, **potential**, or **chemical energy**, these can likewise be transformed into useful work — for instance, when motion ($c_f > 0$) or elevation ($z_f > 0$) differences exist.

Once all such property differences vanish, the system reaches the **dead state** — full thermodynamic equilibrium with the environment, where no further work can be obtained.
The **reversible process** that brings a system from its initial condition to this equilibrium defines the **maximum useful work** it can deliver, that is, its **exergy**.

:::{admonition} Important: the role of the dead state
:class: warning
The **dead state** serves as the universal **reference condition** for all exergy evaluations.
At this state, no gradients remain, no process can occur spontaneously, and no work can be extracted.
Exergy therefore measures how far a system stands from equilibrium — and quantifies the **work potential** lost as it approaches that state.
:::

---

(subsec_conceptual_closure_exergy)=
### Conceptual closure

* **Exergy** bridges the two laws of thermodynamics, expressing the quality of energy in **energetic terms**.
* The **dead state** defines the condition of **complete equilibrium** with the environment — where all potential for work has vanished.
* The **maximum reversible work** obtainable between an initial state and the dead state is the system’s **exergy**.
* **Irreversibilities** reduce this maximum, representing **exergy destruction** or **loss of work potential**.
* Exergy thus provides a **quantitative measure** of how the degradation of energy quality translates into **energetic inefficiency** — closing the conceptual link between the $1^{\text{st}}$ and $2^{\text{nd}}$ laws.
