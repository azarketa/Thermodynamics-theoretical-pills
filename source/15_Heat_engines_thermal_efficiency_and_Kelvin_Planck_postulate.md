(sec_heat_engines_efficiency_kelvin_planck)=
## Heat engines, thermal efficiency, and the Kelvin–Planck postulate

The preceding discussion showed that many natural processes, while fully consistent with the $1^{\text{st}}$ law, occur only in **one direction**.
This observation revealed the existence of a deeper restriction — the **$2^{\text{nd}}$ law** — which governs the *directionality* and *degradation* of energy transformations.

One of the clearest manifestations of this limitation arises when **heat** is used as a means to produce **work**.
Although work can be entirely transformed into heat, the inverse transformation — the complete conversion of heat into work — is **never observed**.
To analyze this limitation quantitatively, we introduce the concept of **heat engines**, the devices through which such transformations take place cyclically.

It is through the study of these engines that the **$2^{\text{nd}}$ law** was first formalized, and that its practical consequences — notably, the **Kelvin–Planck postulate** — became evident.


---

(subsec_heat_engines_definition)=
### Heat engines: transforming heat into work

It is easy to transform **work into heat**.
For example, stirring a glass of water with a spoon warms it: the mechanical work applied through friction is converted into internal energy, raising the temperature of the fluid.
Such transformations — from work to heat — are straightforward and complete.

However, the **reverse process** is not possible in its entirety: one cannot convert all the **absorbed heat** into **mechanical work**.
To transform part of the heat into work in a **cyclic and controlled manner**, we require special devices known as **heat engines**.

Despite their many technological forms — internal‐combustion engines, steam turbines, gas turbines, or power plants — all heat engines share the same **conceptual scheme**:

1. They **absorb heat** from a **high-temperature thermal reservoir**. We will address this heat as $Q_{H}$.
2. They **convert part of that heat into mechanical work**. Such a work will correpsond to the net work output from the system, i.e. $W_{\text{net,out}}$.
3. They **reject the remaining heat** to a **low-temperature reservoir**. We will symbolize it as $Q_L$.
4. They operate **cyclically**, returning their working fluid to its initial state after each cycle.

:::{admonition} Important: the cyclic condition
:class: warning
Because a heat engine returns to its initial thermodynamic state after each cycle, its **net change in energy** is zero:

$$
\Delta E_{\text{cycle}} = 0.
$$

The only energetic transfers occurring in the heat-engine system are $Q_{H}$, $Q_{L}$ and $W_{\text{net,out}}$. Consequently, by the $1^{\text{st}}$ law:

(eq_energetic_balance_heat_engine_ver1)=
$$
\Delta E_{\text{cycle}} = 0 = Q_{\text{net}} - W_{\text{net}}
$$

As:

(eq_energetic_balance_heat_engine_ver2)=
$$
\begin{gather*}
Q_{\text{net}} = Q_{\text{in}} - Q_{\text{out}} = Q_{H} - Q_{L} , \\[10pt]
W_{\text{net}} = W_{\text{net,out}} - W_{\text{net,in}} = W_{\text{net,out}} , \\[10pt]
\end{gather*}
$$

we get:

(eq_energetic_balance_heat_engine_ver3)=
$$
\boxed{Q_H - Q_L = W_{\text{net,out}}} \ .
$$

:::

---

(subsec_impossibility_of_total_conversion)=
### Why total conversion of heat into work is impossible

In the previous discussion, we established that a **heat engine** operates cyclically, exchanging energy with its surroundings in three distinct ways:

* it **absorbs heat** from a high-temperature reservoir,
* it **produces work**,
* and **rejects heat** to a lower-temperature reservoir.

This cyclic structure is essential, because the working substance must return to its initial thermodynamic state after each cycle.

Let us now ask whether the rejection of heat is truly unavoidable.

:::{epigraph}

Could one, in principle, design a cyclic process in which *all* the absorbed heat is transformed into work, leaving no remainder to be expelled?

:::

Imagine an idealized system that receives a finite amount of heat $Q_H$ from a high-temperature source and delivers a certain amount of work $W_{\text{out}}$ to the surroundings — for instance, by lifting a weight or moving a load. If the process is to be **cyclic**, the system must end exactly as it began: same temperature, same internal energy, same configuration. By the $1^{\text{st}}$ law, the total energy balance over a complete cycle reads

$$
Q_{\text{net}} = W_{\text{net,out}},
$$

so that, for a hypothetical complete conversion of heat into work,

$$
Q_H = W_{\text{net,out}}, \qquad Q_L = 0.
$$

However, to return to its initial state, the system must release any internal energy gained during the transformation. This requires a **reverse flow of heat** from the system back to its surroundings. If the surroundings are at the same temperature as the source, such a transfer would imply heat flowing *spontaneously from a colder to a hotter body* — a violation of the observed direction of natural processes.

Hence, it is **impossible** for a cyclic device to restore its initial state while converting the entirety of the absorbed heat into work. To close the cycle, a portion of the input heat must be **rejected** to another body at a **lower temperature**, ensuring that heat flows in the natural direction (from hot to cold). This expelled fraction $Q_L$ constitutes the part of energy that has become **degraded** — still present, but no longer available for producing work.

:::{admonition} Note: a toy example with a piston-cylinder system
:class: note, dropdown

A **piston–cylinder** arrangement provides a simple, tangible example of the general reasoning above.
Suppose the cylinder contains a gas initially at $30 \ ^{\circ}\mathrm{C}$ and is placed in contact with a **hot reservoir** at $100 \ ^{\circ}\mathrm{C}$.
During expansion, the gas absorbs **$100 \ \text{kJ}$** of heat and performs **$15 \ \text{kJ}$** of work by lifting a weight.

Even if the process is ideal — frictionless, quasi-static, and perfectly reversible — the gas becomes warmer than it started: not all absorbed heat becomes work; part increases its internal energy.
To **close the cycle**, the gas must cool back to $30 \ ^{\circ}\mathrm{C}$, restoring its initial state.
But this requires releasing the excess **$85 \ \text{kJ}$** of energy to a **colder reservoir** (below $30 \ ^{\circ}\mathrm{C}$), since heat cannot flow spontaneously from a cooler body to a hotter one.

Thus, even in this idealized case, **part of the absorbed heat must be rejected** — precisely as the $2^{\text{nd}}$ law dictates. The remaining $Q_L = 85 \text{kJ}$ represents **degraded energy**, unavailable for conversion into work.

$$
Q_H = 100~\text{kJ}, \quad W_{\text{out}} = 15~\text{kJ}, \quad Q_L = 85~\text{kJ}.
$$

This example illustrates in concrete form the **general limitation** just discussed: no cyclic process — no matter how ideal — can transform all the absorbed heat into mechanical work.

:::

:::{admonition} Important: $Q_{L}$ as a thermodynamic necessity
:class: warning
Every heat engine must **reject a portion of its absorbed heat** to a reservoir at lower temperature. This rejection is not a technical flaw but a **fundamental thermodynamic necessity**, expressing the directionality of energy transformations and marking the direct manifestation of the $2^{\text{nd}}$ law.
:::

---

(subsec_efficiency_heat_engines)=
### Thermal efficiency

The notion of **thermal efficiency** is meaningful only for systems that behave as **heat engines** — that is, devices operating **cyclically** while exchanging heat with **two thermal reservoirs** at different temperatures. Such engines absorb energy as heat from the **high-temperature source**, convert part of it into **mechanical work**, and reject the remainder to the **low-temperature sink** to complete the cycle. The **thermal efficiency** ($\eta$) quantifies this **conversion capability** by comparing the useful output (net work) to the energy input (heat absorbed from the hot source).

(eq_efficiency_def)=
$$
\eta_{\text{th.}} = \frac{W_{\text{net,out}}}{Q_H}.
$$

From the **cyclic energy balance** of any engine, the total work output equals the difference between the heat absorbed ($Q_H$) and the heat rejected ($Q_L$):

(eq_efficiency_substitution)=
$$
\eta_{\text{th.}} = \frac{Q_H - Q_L}{Q_H} = 1 - \frac{Q_L}{Q_H}.
$$

This simple relation expresses a fundamental limitation: only the portion of heat that is *not rejected* can be converted into work. The efficiency therefore depends on the ratio between the heats exchanged with the high- and low-temperature reservoirs.

:::{admonition} Important: the generalized notion of efficiency
:class: warning

**Efficiency**, in its most general sense, expresses the **ratio between what a process yields and what it consumes** — that is, the useful effect obtained relative to the energy (or resource) required to produce it.
It serves as a **measure of performance**: the closer this ratio is to unity, the more effectively the process converts its input into the intended output.

This abstract notion applies to any transformation — mechanical, electrical, thermal, or otherwise — and provides a common language for comparing how well different systems use energy.

In the specific case of **heat engines**, this general concept becomes the **thermal efficiency**, where the useful output is the *work produced* and the cost is the *heat absorbed* from the high-temperature source.
:::

---

(subsec_kelvin_planck_postulate)=
### The Kelvin–Planck postulate

The conclusions drawn so far — the necessity of two heat reservoirs and the impossibility of completely transforming heat into work — are compactly expressed by the **Kelvin–Planck postulate**, one of the foundational formulations of the $2^{\text{nd}}$ law of thermodynamics.

:::{epigraph}
:class: theorem

It is impossible to construct a device that operates in a cycle and produces no other effect than the extraction of heat from a single thermal reservoir and its complete conversion into work.
:::

This statement formalizes the limitation inherent to all heat engines: a **cyclic device** cannot transform into work the entire quantity of heat it absorbs from a single source.
Part of that energy must always be rejected as heat to a lower-temperature sink.

:::{admonition} Important: implications of the Kelvin–Planck statement
:class: warning

The Kelvin–Planck postulate establishes several fundamental consequences:

* Even though a process that converts all absorbed heat into work **could satisfy the $1^{\text{st}}$ law**, it **violates** the $2^{\text{nd}}$ law.
* A true heat engine must exchange heat with **two reservoirs** at different temperatures — one from which heat is absorbed ($Q_H$) and another to which part of that energy is rejected ($Q_L$).
* The **thermal efficiency** of such an engine, $\eta_{\text{th.}} = 1 - Q_L/Q_H$, is therefore always **less than unity**, i.e. $\eta_{\text{th.}} < 1$.
* The smaller the temperature difference between reservoirs, the lower the achievable efficiency. Increasing this temperature gap improves performance, but **no finite difference can yield $\eta = 1$**.
:::

---

(subsec_conceptual_closure_heat_engines)=
### Conceptual closure

* A **heat engine** is a cyclic system that transforms part of the heat absorbed from a **hot reservoir** into **useful work**, rejecting the rest to a **cold reservoir** to close the cycle.
* The **thermal efficiency** $\eta_{\text{th.}} = 1 - Q_L/Q_H$ expresses the fraction of the heat input that becomes work, setting a **quantitative measure** of the conversion limit.
* The **Kelvin–Planck postulate** expresses the **qualitative boundary**: total conversion of heat into work in a cyclic process is **impossible**.
* This limitation arises because **heat transfer is inherently directional** — it flows naturally from hot to cold, and any cyclic conversion requires this asymmetry.
* The rejected heat $Q_L$ constitutes **degraded energy**, an inevitable consequence of the loss of energy quality during transformation.

In essence, the $2^{\text{nd}}$ law introduces a **hierarchy of energy quality**: while all forms of energy are equivalent in amount (as stated by the $1^{\text{st}}$ law), not all are **equally convertible**.
It establishes a fundamental **limit to the efficiency of all cyclic processes**, defining the directional nature of real thermodynamic transformations.
