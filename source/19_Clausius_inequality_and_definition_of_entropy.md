(sec_clausius_inequality_entropy)=
## Clausius inequality and the definition of entropy

Up to this point, the **$2^{\text{nd}}$ law** has been formulated for **cyclic devices** — heat engines, refrigerators, and heat pumps — where energy exchange occurs repeatedly between reservoirs.
However, thermodynamics applies not only to cycles but to **any transformation of state**.
Just as the **$1^{\text{st}}$ law** expresses energy conservation for all processes, the **$2^{\text{nd}}$ law** must also be expressible in a general, process-based form — one that holds even for **non-cyclic** transformations.

---

(subsec_clausius_inequality)=
### Clausius inequality

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
dE_{\text{net}} = \delta Q_R - \delta W_{\text{net}}.
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

This is the **Clausius inequality**, a general statement of the **$2^{\text{nd}}$ law** applicable to any **cyclic process**.

:::{admonition} Important: physical interpretation of the inequality
:class: warning

* For a **reversible cycle**, $\displaystyle \oint \frac{\delta Q}{T} = 0$.
* For an **irreversible cycle**, $\displaystyle \oint \frac{\delta Q}{T} < 0$.

Equality marks the ideal, quasi-static limit where no dissipative effects occur; inequality marks the **irreversibility** inherent to all real processes.
:::

:::{admonition} Note: why Clausius's configuration matters
:class: note, dropdown

This conceptual setup is not arbitrary — it is a **thought experiment** designed to test the consistency of the $2^{\text{nd}}$ law.
By coupling a reversible engine to another system that reuses its rejected heat, Clausius was able to explore whether it would be possible, *in principle*, to build a device that takes heat from a single reservoir and converts it entirely into work — precisely the situation forbidden by the **Kelvin–Planck postulate**.

This construction therefore serves as a **consistency test**: if the resulting combined system ever produces a net positive work while exchanging heat with only one reservoir, the postulate would be violated.
Hence, the configuration provides a rigorous and didactic way to derive a **quantitative restriction** on all cycles — the **Clausius inequality**.
:::

---

(subsec_entropy_definition)=
### From the cyclic form to a general process: the definition of entropy

The **Clausius inequality** was first derived for cyclic transformations, but its implications reach much further.
If for a reversible cycle the integral

$$
\oint \frac{\delta Q}{T} = 0,
$$

then the integral of $\frac{\delta Q}{T}$ between two given states — *provided the process is reversible* — must depend **only on those states**, not on the path followed between them.
Mathematically, this means the integral defines a **state function**.

The **differential form** of that state function is therefore

(eq_entropy_differential)=
$$
\boxed{dS = \left(\frac{\delta Q}{T}\right)_{\text{rev}}.}
$$

This new quantity, introduced by Clausius, is called **entropy** ($S$).
It provides a bridge between the **cycle-based** and **process-based** formulations of the $2^{\text{nd}}$ law.
Entropy measures both the **thermodynamic state** of a system and the **degree of irreversibility** of a process.

For a real (irreversible) process, the Clausius inequality can then be written in general form as

(eq_entropy_inequality)=
$$
\boxed{\Delta S \ge \int \frac{\delta Q}{T}},
$$

where the equality holds only for **reversible** transformations.

:::{admonition} Important: significance of entropy and generalization of the 2nd law
:class: warning

* Entropy is a **state property**, allowing the $2^{\text{nd}}$ law to be expressed for **non-cyclic processes**.
* For any **reversible process**, $\Delta S = \int \frac{\delta Q_{\text{rev}}}{T}$.
* For any **irreversible process**, $\Delta S > \int \frac{\delta Q_{\text{irrev}}}{T}$ — meaning that the **entropy of the universe increases**.
  :::

---

(subsec_conceptual_closure_clausius_entropy)=
### Conceptual closure

* The **Clausius configuration** transforms the $2^{\text{nd}}$ law from a qualitative limitation on cyclic devices into a **quantitative principle** valid for all processes.
* By coupling a reversible engine with another system, Clausius showed that complete heat-to-work conversion would **violate** the $2^{\text{nd}}$ law, leading to the **Clausius inequality**

  $$
  \oint \frac{\delta Q}{T} \le 0.
  $$
  
* This relation distinguishes **reversible** ($=$) from **irreversible** ($<$) cycles and reveals that the reversible integral defines a new **state property** — **entropy**:
  
  $$
  dS = \left( \frac{\delta Q}{T} \right)_{\text{rev}}.
  $$
  
* Entropy extends the $2^{\text{nd}}$ law to **any process**, measuring both the **energy distribution** within a system and the **irreversibility** of real transformations.
* For the **isolated universe**, entropy can only **increase**, expressing the natural direction of all spontaneous change.

In essence, Clausius provided the **universal formulation** of the $2^{\text{nd}}$ law — one that applies not only to cycles, but to **every process in nature**.
