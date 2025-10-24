(sec_first_law_closed_systems)=
## 1st law in closed systems

Thermodynamics describes how energy moves and changes form within and across systems.
When dealing with a **closed system**, the **mass remains constant** — no substance crosses the system boundary.
However, energy can still be transferred in the form of **work** or **heat**.
This section formulates the **first law of thermodynamics** for such systems, expressing the balance between energy storage and energy transfer.

---

(subsec_energy_balance_closed_system)=
### Energy balance for a closed system

A **closed system** exchanges **energy**, but not **mass**, with its surroundings.
If energy is neither created nor destroyed — only transformed — and the **only transfer modes** are heat and work, the total energy balance is written as:

(eq_first_law_basic)=
$$
\Delta{}E{}={}Q{}-{}W
$$

where:

* $Q$ is the **net heat** transferred *to* the system,
* $W$ is the **net work** done *by* the system,
* $\Delta{}E$ is the **total change in energy** of the system.

:::{admonition} Sign convention for $Q$ and $W$
:class: note, dropdown

* If the **system receives heat**, then $Q>0$.
* If the **system loses heat**, then $Q<0$.
* If the **system performs work on the surroundings**, $W>0$.
* If **work is done on the system**, $W<0$.
  :::

The total energy variation of the system may be decomposed into its **macroscopic** and **microscopic** components:

(eq_first_law_components)=
$$
\Delta{}E{}={} \Delta{}E_k{}+{}\Delta{}E_p{}+{}\Delta{}U{}={}Q{}-{}W
$$

where:

* $\Delta E_k$ corresponds to the **kinetic energy change**,
* $\Delta E_p$ to the **potential energy change**,
* $\Delta U$ to the **change in internal energy**.

In the absence of **chemical** or **nuclear** reactions, $\Delta U$ represents solely **thermal effects** — that is, variations in the system’s temperature.

:::{admonition} Note — Flow energy and work
:class: note, dropdown
In closed systems, **flow energy** ($P,V$) is not stored as part of the system; it represents **boundary work** and therefore appears in $W$.
The energy forms that remain *contained* within the system are kinetic, potential, and internal.
:::

---

(subsec_first_law_simplified)=
### Simplified form: negligible kinetic and potential changes

For most stationary systems (no significant motion or elevation change), kinetic and potential energy variations are negligible:

(eq_first_law_reduced)=
$$
\Delta{}U{}={}Q{}-{}W
$$

This reduced form — widely used in thermodynamics — expresses that **all energy transfers as heat or work** manifest as **changes in internal energy**.
Thus, if a closed system receives heat or performs work, its **temperature** (and hence its internal energy) will change accordingly.

:::{admonition} Tip — Interpreting $\Delta U = Q - W$
:class: tip, dropdown

* When $Q>W$, the system’s **internal energy increases** (it warms up).
* When $W>Q$, the system’s **internal energy decreases** (it cools down).
  This intuitive balance helps identify the direction of energy flow in simple processes.
  :::

---

(subsec_first_law_enthalpy)=
### First law: particularization with enthalpy

The combination of internal energy and the flow term, $P,V$, appears so often that it is defined as a separate thermodynamic property — the **enthalpy**:

(eq_enthalpy_def)=
$$
H{}={}U{}+{}PV
$$

The **enthalpy**, $H$, represents the **total useful energy** of a fluid, combining the *thermal capacity to perform work* (through $U$) and the *flow capacity* ($P,V$).
While internal energy $U$ tracks temperature-related effects, enthalpy incorporates both **temperature** and **pressure** effects, making it a more practical measure in processes involving fluids and flow.

Differentiating the definition of $H$:

(eq_differential_enthalpy)=
$$
\mathrm{d}H{}={} \mathrm{d}U{}+{}P\mathrm{d}V{}+{}V\mathrm{d}P
$$

Substituting the **first law differential form**, $\mathrm{d}U{}={} \delta Q{}-{}P,\mathrm{d}V$, into this expression gives:

(eq_heat_enthalpy_relation1)=
$$
\delta Q{}={} \mathrm{d}H{}-{}V\mathrm{d}P
$$

This relation provides a direct link between **heat transfer** and **enthalpy change**, highlighting how $P$ and $V$ variations affect the overall heat exchange.

For processes at **constant pressure**, the last term disappears:

(eq_heat_const_p)=
$$
\delta Q_p{}={} \mathrm{d}H
$$

which means the **heat transferred at constant pressure** equals the **change in enthalpy** of the system.

:::{admonition} Note — Heat capacity at constant pressure
:class: note, dropdown
At constant pressure, the specific heat $c_p$ is defined as:

$$
c_p{}={} \left(\frac{\partial h}{\partial T}\right)_P
$$

so that $\delta q_p{}={}c_p\mathrm{d}T$ and, in finite form, $\Delta h{}={}c_p\Delta T$ for ideal gases.
:::

---

(subsec_conceptual_closure_firstlaw_closed)=
### Conceptual closure
* A **closed system** exchanges energy but **not mass** with its surroundings.
* The **first law** expresses the **conservation of energy** between internal storage and transfer:
  $\Delta E{}={}Q{}-{}W$.
* When kinetic and potential effects are negligible, the simplified form $\Delta U{}={}Q{}-{}W$ suffices.
* The **enthalpy**, $H{}={}U{}+{}PV$, naturally emerges when dealing with processes at constant pressure or in open-system extensions.
* Under constant-pressure conditions, **heat transfer equals the enthalpy change**, $\delta Q_p{}={} \mathrm{d}H$.
