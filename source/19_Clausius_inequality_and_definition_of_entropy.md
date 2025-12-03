(sec_clausius_inequality_entropy)=
## Clausius's inequality and the definition of entropy

Up to this point, the **$2^{\text{nd}}$ law** has been formulated for **cyclic devices** — heat engines, refrigerators, and heat pumps — where energy exchange occurs repeatedly between reservoirs.
However, thermodynamics applies not only to cycles but to **any transformation of state**.
Just as the **$1^{\text{st}}$ law** expresses energy conservation for all processes, the **$2^{\text{nd}}$ law** must also be expressible in a general, process-based form — one that holds even for **non-cyclic** transformations.

---

(subsec_clausius_inequality)=
### Clausius's inequality

To generalize the $2^{\text{nd}}$ law, **Rudolf Clausius** proposed a particularly insightful configuration:
he considered a **reversible heat engine** and a **separate auxiliary system** that absorbs the heat rejected by the engine and uses it to produce additional work.

Consider, then, a **reversible engine** that absorbs an infinitesimal amount of heat $\delta Q_R$ from a **thermal reservoir** at temperature $T_R$ and produces a small amount of **work** $\delta W_{\text{rev}}$.
The heat it rejects, $\delta Q$, is fed to a **piston–cylinder assembly** containing a gas at temperature $T$.
As the gas expands quasi-statically while absorbing this heat, it performs work $\delta W_{\text{sys}}$.

The **total work output** of the combined system is therefore

$$
\delta W_{\text{net}} = \delta W_{\text{rev}} + \delta W_{\text{sys}}.
$$

Applying the **$1^{\text{st}}$ law** to the whole (engine + cylinder) system yields

$$
\mathrm{d}E_{\text{net}} = \delta Q_R - \delta W_{\text{net}}.
$$

For a **cyclic** combined process, the total energy change is zero ($dE_{\text{net}} = 0$), and therefore

$$
\delta W_{\text{net}} = \delta Q_R.
$$

Because the engine is **reversible**, the Carnot relation applies to the heats and temperatures involved:

$$
\frac{\delta Q}{\delta Q_R} = \frac{T}{T_R}.
$$

Substituting this into the previous relation and integrating around a complete cycle gives

(eq_clausius_intermediate)=
$$
W_{\text{net}} = T_R \oint \frac{\delta Q}{T}.
$$

This equation appears to describe a system that receives heat from a single reservoir (at $T_R$) and converts it entirely into work — a clear **violation of the Kelvin–Planck postulate**.
Since such a process cannot occur, the integral must not correspond to a positive work output; therefore, it must satisfy

(eq_clausius_inequality)=
$$
\boxed{\oint \frac{\delta Q}{T} \leq 0.}
$$

This is the **Clausius's inequality**, a general statement of the **$2^{\text{nd}}$ law** applicable to any **cyclic process**.

:::{important}

**PHYSICAL INTERPRETATION OF THE INEQUALITY**

* For a **reversible cycle**, $\displaystyle \oint \frac{\delta Q}{T} = 0$.
* For an **irreversible cycle**, $\displaystyle \oint \frac{\delta Q}{T} < 0$.

Equality marks the ideal, quasi-static limit where no dissipative effects occur; inequality marks the **irreversibility** inherent to all real processes.
:::

:::{note}

**WHY CLAUSIUS'S CONFIGURATION MATTERS**

This conceptual setup is not arbitrary — it is a **thought experiment** designed to test the consistency of the $2^{\text{nd}}$ law.
By coupling a reversible engine to another system that reuses its rejected heat, Clausius was able to explore whether it would be possible, *in principle*, to build a device that takes heat from a single reservoir and converts it entirely into work — precisely the situation forbidden by the **Kelvin–Planck postulate**.

This construction therefore serves as a **consistency test**: if the resulting combined system ever produces a net positive work while exchanging heat with only one reservoir, the postulate would be violated.
Hence, the configuration provides a rigorous and didactic way to derive a **quantitative restriction** on all cycles — the **Clausius's inequality**.
:::

---

(subsec_entropy_definition)=
### From the cyclic form to a general process: the definition of entropy

The **Clausius's inequality** was first derived for cyclic transformations, but its implications reach much further.
If for a reversible cycle the integral

$$
\oint \frac{\delta Q}{T} = 0,
$$

then the integral of $\frac{\delta Q}{T}$ between two given states — *provided the process is reversible* — must depend **only on those states**, not on the path followed between them.
Mathematically, this means the integral defines a **state function**.

The **differential form** of that state function is therefore

(eq_entropy_differential)=
$$
\boxed{\mathrm{d}S = \left(\frac{\delta Q}{T}\right)_{\text{rev}}.}
$$

This new quantity, introduced by Clausius, is called **entropy** ($S$).
It provides a bridge between the **cycle-based** and **process-based** formulations of the $2^{\text{nd}}$ law.
Entropy measures both the **thermodynamic state** of a system and the **degree of irreversibility** of a process.

For a real (irreversible) process, the Clausius's inequality can then be written in general form as

(eq_entropy_inequality)=
$$
\boxed{\Delta S \ge \int \frac{\delta Q}{T}},
$$

where the equality holds only for **reversible** transformations.

:::{important}

**THE MEANING OF ENTROPY AND THE GENERALIZATION OF THE $2^{\text{nd}}$ LAW**

* Entropy is a **state property**, allowing the $2^{\text{nd}}$ law to be expressed for **non-cyclic processes**.
* For any **reversible process**, $\Delta S = \int \frac{\delta Q_{\text{rev}}}{T}$.
* For any **irreversible process**, $\Delta S > \int \frac{\delta Q_{\text{irrev}}}{T}$ — meaning that the **entropy of the universe increases**.
  :::

:::{note}

**UNITS OF ENTROPY**

Mind that, according to the {re}`above equation <eq_entropy_inequality>`, entropy (and specific entropy, i.e. entropy per unit mass) shares the same **dimensional structure** as the quotient of heat and temperature:

$$
\begin{gather*}
[S] = \frac{\text{kJ}}{\text{K}}, \\[10pt]
[s] = \frac{\text{kJ}}{\text{kg}{\cdot}\text{K}}.
\end{gather*}
$$

The units of $s$ match those of $c_p$ or $c_v$ — reflecting that both describe **energy per unit mass per unit temperature**.
:::

---

(subsec_principle_increasing_entropy)=
### The principle of increasing entropy

Having established **entropy** as a property that quantifies reversible heat transfer, we can now extend its use to **all real processes**.
The **Clausius inequality** provides the key: it allows comparing any actual (irreversible) transformation with a reversible one between the same two states.
Through this comparison, the $2^{\text{nd}}$ law reveals a universal rule governing the evolution of entropy in nature — the **principle of increasing entropy**.

Consider a **generic process** between two states, $(1)$ and $(2)$, which may be reversible or irreversible.
By appending to it an **internally reversible return path** $(2) \rightarrow (1)$, a complete cycle is formed, and the **Clausius inequality** applies:

$$
\oint \frac{\delta Q}{T} \le 0.
$$

Expanding the cyclic integral gives

$$
\int_1^2 \frac{\delta Q}{T} + \int_2^1 \left( \frac{\delta Q}{T} \right)_{\text{rev.}} \le 0,
$$

and since the second term equals $S_1 - S_2$, we obtain

$$
S_2 - S_1 \ge \int_1^2 \frac{\delta Q}{T},
\qquad \text{or equivalently,} \qquad
\mathrm{d}S \ge \frac{\delta Q}{T}.
$$

This inequality expresses that, for any real (irreversible) process, the **entropy increase of the system** is greater than the **entropy transferred** through heat alone.
The total entropy change can therefore be written as

(eq_entropy_generation)=
$$
\boxed{\Delta S_{\text{sys.}} = \int_1^2 \frac{\delta Q}{T} + S_{\text{gen.}}},
\qquad S_{\text{gen.}} \ge 0,
$$

where $S_{\text{gen}}$ represents the **entropy generated internally** due to irreversibilities.
For a reversible process, $S_{\text{gen}} = 0$; for an irreversible one, $S_{\text{gen}} > 0$.

In an **isolated system**, no heat or mass crosses the boundary ($\delta Q = 0$), so

$$
\Delta S_{\text{isolated}} = S_{\text{gen.}} \ge 0.
$$

Thus, entropy can only **remain constant** (for reversible processes) or **increase** (for irreversible ones).
Extending this idea to the **thermodynamic universe** — the system and its surroundings together — gives

(eq_entropy_universe)=
$$
\boxed{\Delta S_{\text{univ.}} = \Delta S_{\text{sys.}} + \Delta S_{\text{surr.}} = S_{\text{gen.,univ.}} \ge 0.}
$$

Local decreases in entropy are possible within subsystems, but they must always be offset by greater increases elsewhere, ensuring that the **total entropy of the universe never decreases**.

:::{important}

**PHYSICAL MEANING**

* Entropy is **conserved** only in reversible processes and **created** in irreversible ones.
* The increase of entropy defines the **natural direction of all processes** and establishes the **thermodynamic arrow of time**.
* While entropy can decrease locally, the **global balance** (system + surroundings) always satisfies $\Delta S_{\text{univ.}} \ge 0$.

:::

---

(subsec_conceptual_closure_clausius_entropy)=
### Conceptual closure

* The **Clausius configuration** transforms the $2^{\text{nd}}$ law from a qualitative limitation on cyclic devices into a **quantitative principle** valid for all processes.

* By coupling a reversible engine with another system, Clausius showed that complete heat-to-work conversion would **violate** the $2^{\text{nd}}$ law, leading to the **Clausius's inequality**

  $$
  \oint \frac{\delta Q}{T} \le 0.
  $$
  
* This relation distinguishes **reversible** ($=$) from **irreversible** ($<$) cycles and reveals that the reversible integral defines a new **state property** — **entropy**:
  
  $$
  \mathrm{d}S = \left( \frac{\delta Q}{T} \right)_{\text{rev.}}.
  $$
  
* Entropy extends the $2^{\text{nd}}$ law to **any process**, measuring both the **energy distribution** within a system and the **irreversibility** of real transformations.

* The **entropy balance**,
  
  $$
  \Delta S_{\text{sys.}} = \int \frac{\delta Q}{T} + S_{\text{gen.}},
  $$

  distinguishes entropy **transfer** (via heat) from entropy **generation** (via irreversibility).
  
* The **principle of increasing entropy** establishes that, for any isolated system or for the universe as a whole,

  $$
  \Delta S_{\text{univ.}} \ge 0,
  $$

  expressing the natural direction of all processes.
  
* Reversible transformations conserve entropy, while irreversible ones create it — defining both the **limit of ideal performance** and the **thermodynamic arrow of time**.

In summary, the $2^{\text{nd}}$ law attains its most general form: energy remains conserved, but its **quality** — measured by entropy — inevitably **degrades** in every real process.
