(sec_carnot_cycles_temperature_scale_postulates)=
## Carnot cycles, thermodynamic temperature scale, and Carnot’s postulates

The previous discussion distinguished **reversible** and **irreversible** processes, showing that reversible ones represent **ideal limits** of real behavior. We now turn to the **Carnot cycle**, a theoretical construction that embodies a *perfectly reversible* heat engine and establishes the **maximum efficiency** any real engine can achieve.

This ideal model allows the introduction of **Carnot’s postulates** and the **thermodynamic temperature scale**, both of which arise directly from the principles of the $2^{\text{nd}}$ law.

---

(subsec_carnot_cycle)=
### The Carnot cycle

A **Carnot cycle** is the **idealized reversible cycle** of a heat engine. It consists of four reversible processes — **two isothermal** and **two adiabatic** — executed in such a way that the working substance (for example, an ideal gas) passes through a sequence of **equilibrium states**.

1. **Isothermal expansion (1–2):**
   The system is in contact with a **hot reservoir** at temperature $T_H$.
   It expands slowly while absorbing a heat $Q_H$, keeping its temperature constant.
   Any infinitesimal cooling due to expansion is compensated by an equivalent heat inflow, ensuring reversibility.

2. **Adiabatic expansion (2–3):**
   The system is isolated from the reservoir and continues expanding **without heat exchange**.
   Its temperature decreases from $T_H$ to $T_L$ as it performs work on the surroundings.

3. **Isothermal compression (3–4):**
   The system is placed in contact with a **cold reservoir** at temperature $T_L$ and is slowly compressed.
   It rejects a heat $Q_L$ while remaining at constant temperature.

4. **Adiabatic compression (4–1):**
   The system is again isolated, and compression continues **adiabatically** until the temperature rises back to $T_H$, returning to the initial state.

During one complete cycle, the system absorbs $Q_H$ from the high-temperature reservoir, rejects $Q_L$ to the low-temperature reservoir, and delivers a **net work output**

$$
W_{\text{net,out}} = Q_H - Q_L.
$$

Even though every step is reversible, the **$2^{\text{nd}}$ law** is fully respected:
some energy must always be rejected as heat, so the total conversion of $Q_H$ into work is impossible.

:::{important}

**THE REVERSIBLE IDEAL**

A Carnot cycle represents the **reversible limit** of a heat engine — a process that proceeds without any dissipative effects.
It defines the **maximum theoretical efficiency** achievable between two temperature levels $T_H$ and $T_L$.
All real engines are **irreversible**, and thus their efficiencies are **lower** than that of the Carnot engine operating between the same reservoirs.
:::

---

(subsec_inverse_carnot_cycle)=
### Inverse Carnot cycle

Because the Carnot cycle is **reversible**, it can be **operated in reverse**. When the sequence of processes is inverted, the result is an **inverse Carnot cycle**, representing an **ideal refrigerator or heat pump**.

* The system **receives work input** $W_{\text{in}}$.
* It **absorbs heat** $Q_L$ from a low-temperature reservoir.
* It **rejects heat** $Q_H$ to a high-temperature reservoir.

The process satisfies the **Clausius postulate**: heat can flow from cold to hot **only if external work is supplied**.

:::{note}

**THE RELATION BETWEEN DIRECT AND INVERSE CYCLES**

Both the **direct** and **inverse** Carnot cycles operate between the same two reservoirs, $T_H$ and $T_L$. They differ only in the **direction of energy flow**: the direct cycle produces work by exploiting the natural flow of heat (hot → cold), whereas the inverse one consumes work to reverse that flow (cold → hot).
:::

---

(subsec_carnot_postulates)=
### Carnot’s postulates

The analysis of Carnot cycles leads to two fundamental propositions that form the basis of the $2^{\text{nd}}$ law.

* **$1^{\text{st}}$ Carnot postulate:**

   :::{epigraph}
   No real (irreversible) heat engine operating between two thermal reservoirs can be more efficient than a reversible one operating between the same reservoirs.
   :::

* **$2^{\text{nd}}$ Carnot postulate:**

   :::{epigraph}
   All reversible heat engines operating between the same two reservoirs have the same efficiency, regardless of the working fluid or construction details.
   :::

---

(subsec_thermodynamic_temperature_scale)=
### The thermodynamic temperature scale

The **Carnot postulates** make it possible to define a **temperature scale** that depends solely on the **laws of thermodynamics**, rather than on the properties of any particular substance.

Consider three **reversible heat engines**, labeled A, B, and C, arranged in cascade between three thermal reservoirs at temperatures $T_1$, $T_2$, and $T_3$, with $T_1 > T_2 > T_3$.
Engine A operates between $T_1$ and $T_2$, engine B between $T_2$ and $T_3$, and engine C between $T_1$ and $T_3$.

For any reversible heat engine, the thermal efficiency is expressed as

$$
\eta_{\text{th.}} = 1 - \frac{Q_L}{Q_H},
$$

where $Q_H$ and $Q_L$ are the heats absorbed and rejected at the high and low temperatures, respectively.
Because the Carnot postulates state that the efficiency depends **only** on the temperatures of the reservoirs, we may express the heat ratio in functional form as

$$
\frac{Q_L}{Q_H} = f(T_L, T_H),
$$

where $f$ is a yet-unknown function that captures the dependence of the heat ratio on the temperatures of the two reservoirs.

For each of the three engines, the efficiency may therefore be written as

$$
\begin{gather*}
\eta_{\text{th.},A} = 1 - \frac{Q_2}{Q_1} = 1 - f(T_2, T_1), \\[10pt]
\eta_{\text{th.},B} = 1 - \frac{Q_3}{Q_2} = 1 - f(T_3, T_2), \\[10pt]
\eta_{\text{th.},C} = 1 - \frac{Q_3}{Q_1} = 1 - f(T_3, T_1).
\end{gather*}
$$

Now, if engines A and B operate **in series**, the heat rejected by A ($Q_2$) becomes the heat absorbed by B.
From energy conservation applied to the combined system (A+B), the overall heat ratio between the extreme reservoirs ($T_1$ and $T_3$) satisfies

(eq_carnot_combined_ratio)=
$$
\frac{Q_3}{Q_1} = \frac{Q_3}{Q_2} \cdot \frac{Q_2}{Q_1}.
$$

Substituting the functional expressions for each term gives

(eq_carnot_functional_relation)=
$$
f(T_1, T_3) = f(T_1, T_2), f(T_2, T_3).
$$

This condition — that the overall heat ratio equals the **product** of the intermediate ones — must hold for any intermediate temperature $T_2$.
The only type of function that satisfies this requirement for arbitrary temperature values is one that can be **separated** into a ratio of two single-variable functions:

(eq_carnot_functional_form)=
$$
\boxed{f(T_L, T_H) = \frac{\phi(T_L)}{\phi(T_H)}.}
$$

Indeed, if $f$ takes this form, the multiplicative relation is automatically verified:

$$
\frac{\phi(T_3)}{\phi(T_1)} = \frac{\phi(T_3)}{\phi(T_2)} \cdot \frac{\phi(T_2)}{\phi(T_1)}.
$$

This result implies that the heat ratio between two reservoirs in a reversible cycle depends solely on a **monotonic property** of temperature $\phi(T)$, ensuring that heat flows naturally from higher to lower temperature values.

The simplest and most direct choice for $\phi(T)$, proposed by **Lord Kelvin**, is to make it **proportional to the absolute temperature** itself:

(eq_carnot_kelvin_choice)=
$$
\phi(T) = T.
$$

With this choice, the heat ratio becomes

(eq_carnot_temperature_relation)=
$$
\boxed{\frac{Q_L}{Q_H} = \frac{T_L}{T_H}.}
$$

This equation defines the **thermodynamic temperature scale**, also known as the **Kelvin scale**, where the ratio of temperatures between two reservoirs equals the ratio of heats exchanged in a reversible cycle.

:::{important}

**FEATURES OF THE THERMODYNAMIC SCALE**

* The thermodynamic temperature scale arises **purely from the $2^{\text{nd}}$ law**, independently of any particular working substance. Its universal nature comes from the fact that it connects the temperature property to an energy-transfer-related physical process (heat transfer). This gets rid of the operational dependency on a device-dependent scale.
* For reversible cycles, **temperature ratios** equal **heat ratios**.
* The simplest form, $\phi(T)=T$, defines a **linear, absolute scale**, with the **Kelvin $\text{K}$** as its unit.
* Zero kelvin ($0 \ \text{K}$) corresponds to the theoretical limit where all thermodynamic activity ceases.
:::

---

(subsec_carnot_efficiency_and_COP)=
### Carnot efficiency and its implications

For a reversible heat engine operating between $T_H$ and $T_L$, the **Carnot efficiency** is

(eq_carnot_efficiency)=
$$
\boxed{\eta_{\text{th,rev}} = \eta_{\text{Carnot}} = 1 - \frac{T_L}{T_H}}.
$$

No real engine can exceed this value.
Similarly, for the **inverse Carnot cycle**, the **coefficients of performance** are

(eq_carnot_COPs)=
$$
\boxed{\text{COP}_{\text{R,rev}} = \text{COP}_{\text{R,Carnot}} = \frac{T_L}{T_H - T_L}}, \qquad
\boxed{\text{COP}_{\text{HP,rev}} = \text{COP}_{\text{HP,Carnot}} = \frac{T_H}{T_H - T_L}}.
$$

These represent the **maximum theoretical values** attainable by any refrigeration or heat-pump system operating between the same temperatures.

:::{important}

**CARNOT CYCLES AS REFERENCE LIMITS**

A comparison between real and ideal devices follows directly:

| **Device type**              | **Criterion**                             | **Interpretation**                        |
| :--------------------------- | :---------------------------------------- | :---------------------------------------- |
| **Heat engine**              | $\eta_{\text{th}} < \eta_{\text{Carnot}}$ | Irreversible engine (real)                |
|                              | $\eta_{\text{th}} = \eta_{\text{Carnot}}$ | Reversible engine (ideal)                 |
|                              | $\eta_{\text{th}} > \eta_{\text{Carnot}}$ | Impossible (violates $2^{\text{nd}}$ law) |
| **Refrigerator / heat pump** | $\text{COP} < \text{COP}_{\text{Carnot}}$ | Irreversible (real)                       |
|                              | $\text{COP} = \text{COP}_{\text{Carnot}}$ | Reversible (ideal)                        |
|                              | $\text{COP} > \text{COP}_{\text{Carnot}}$ | Impossible (violates $2^{\text{nd}}$ law) |

Thus, the Carnot limits distinguish **three regimes** of operation:

1. **Real devices** are always less efficient or less performant than Carnot’s ideal.
2. **Reversible devices** attain Carnot’s efficiency but are only conceptual.
3. **Hypothetical devices** exceeding Carnot’s values would contradict the $2^{\text{nd}}$ law.
:::

The analysis of **Carnot cycles** has revealed that the efficiency of any reversible process depends solely on the **temperature ratio** between its reservoirs.
This insight naturally raises a deeper question:

:::{epigraph}
Is there any intrinsic property of a system that governs the direction and limitation of these energy transfers? If so: which is such a property?
:::

To answer this, we must introduce a new thermodynamic quantity — **entropy** — which provides a universal measure of **energy dispersal** and **process irreversibility**.
The next section will therefore develop the concept of **entropy** and derive its mathematical foundation through the **Clausius inequality**.

---

(subsec_conceptual_closure_carnot)=
### Conceptual closure

* The **Carnot cycle** represents the *ideal reversible model* of a heat engine and establishes the **upper limit** of thermodynamic performance.
* Its **inverse cycle** defines the **ideal refrigerator or heat pump**, both operating in full accordance with the $2^{\text{nd}}$ law.
* **Carnot’s postulates** demonstrate that efficiency depends **only** on the temperatures of the reservoirs, leading naturally to the **thermodynamic temperature scale**.
* The **Kelvin scale** emerges from this reasoning, connecting temperature ratios to heat ratios in reversible cycles.
* The **Carnot efficiency** and **Carnot COPs** set absolute performance limits — no real process can exceed them.

In summary, Carnot cycles reveal the **quantitative boundary** of the $2^{\text{nd}}$ law: they define what is *thermodynamically possible*, and by contrast, expose what the irreversible nature of reality forbids.
