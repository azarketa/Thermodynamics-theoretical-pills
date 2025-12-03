(sec_refrigeration_cycles_COP_clausius)=
## Refrigeration cycles, COP, and the Clausius postulate

The $2^{\text{nd}}$ law shows that **heat engines** can convert only part of the heat they receive into work, rejecting the remainder to a cooler reservoir.
If this principle is **reversed**, we obtain devices that use external work to make heat flow *against* its natural direction — from a colder region to a warmer one.
Such **refrigeration systems** and **heat pumps** embody the complementary operation of heat engines: they do not produce work from heat, but **consume work** to drive a non-spontaneous heat transfer.

---

(subsec_refrigeration_cycles_definition)=
### Refrigeration cycles and heat pumps

A **reversed heat-engine cycle** forms the basis of both refrigerators and heat pumps.
Their operation can be summarized as follows:

1. **Heat extraction:** the device absorbs heat $Q_L$ from a **low-temperature region**.
2. **Work input:** an external work $W_{\text{net,in}}$ is supplied (by a compressor or motor).
3. **Heat rejection:** the device expels heat $Q_H$ to a **high-temperature region**.
4. **Cyclic operation:** the working fluid returns to its initial state at the end of each cycle.

The two devices differ only in purpose:

* a **refrigerator** removes heat from a low-temperature space,
* a **heat pump** delivers heat to a warm space.

:::{important}

**REVERSED-DIRECTION OPERATION**

While a **heat engine** converts part of the natural heat flow (hot → cold) into work,
a **reversed heat engine** consumes work to make heat flow **cold → hot**.
This constitutes the essential difference between both classes of cyclic devices.

:::

---

(subsec_COP_definition)=
### Coefficient of performance

The **coefficient of performance $(\text{COP})$** plays for refrigeration devices the same conceptual role that **efficiency** plays for heat engines: it measures the ratio between the **useful effect obtained** and the **energy required** to achieve it.

However, while a heat engine produces work and thus its useful output is the *net work delivered* ($W_{\text{net,out}}$), a **reversed device** (refrigerator or heat pump) **consumes** work. In heat engines, multiple work interactions may occur within the cycle, so the **net work output** $W_{\text{net,out}}$ represents their overall balance. Reversed cycles usually involve a **single dominant work input** (e.g., compressor power), so it is denoted simply as $W_{\text{in}}$.

* **Refrigeration cycle:**

    For a **refrigerator**, the useful effect is the **heat absorbed** from the low-temperature region ($Q_L$). From the **energy balance** of a reversed cycle:

    (eq_energy_balance_reversed_cycle)=
    $$
    Q_H = Q_L + W_{\text{in}},
    \qquad \text{so that} \qquad W_{\text{in}} = Q_H - Q_L.
    $$

    By definition:

    (eq_COP_refrigerator)=
    $$
    \text{COP}_{\text{R}} = \frac{Q_L}{W_{\text{in}}} = \frac{Q_L}{Q_H - Q_L} \implies \boxed{\text{COP}_{\text{R}} = \frac{1}{Q_H/Q_L - 1}} \ .
    $$

* **Heat pump cycle:**

    For a **heat pump**, the useful effect is the **heat delivered** to the high-temperature region ($Q_H$). Following the same reasoning as before:

    (eq_COP_heatpump)=
    $$
    \text{COP}_{\text{HP}} = \frac{Q_H}{W_{\text{in}}} = \frac{Q_H}{Q_H - Q_L} \implies \boxed{\text{COP}_{\text{HP}} = \frac{1}{1 - Q_L/Q_H}} \ .
    $$

Both $\text{COP}$ values can be shown to be related:

$$
\text{COP}_{\text{HP}}=\frac{Q_H}{Q_H-Q_L} = \frac{Q_L}{Q_H-Q_L} + 1 = \text{COP}_{\text{R}} + 1 \implies \boxed{\text{COP}_{\text{HP}} = \text{COP}_{\text{R}} + 1} \ .
$$

:::{important}

**PHYSICAL INTERPRETATION OF COP VALUES**

The **coefficient of performance** follows the *same conceptual logic* as **efficiency**: both express a **ratio between what is obtained and what it costs** to obtain it. In the case of the $\text{COP}$, such a ratio expresses how much heat transfer is achieved per unit of work supplied:

* $\text{COP} > 1$ — the **normal condition** for practical devices.
  It means that each unit of input work transfers *more than one unit* of heat between reservoirs.
  For example, $\text{COP}_{\text{R}} = 4$ implies that $1$ unit of electrical work removes $4$ units of heat from the cold space — three units coming from the transferred heat and one from the work itself.

* $\text{COP} = 1$ — the limiting case where the system merely **converts work into an equal amount of heat transfer**; it no longer provides an energetic advantage.

* $\text{COP} < 1$ — indicates an **inefficient or defective process**, where more work is consumed than the amount of heat transferred; the device would no longer be practical as a refrigerator or heat pump.

In contrast to the efficiency of heat engines (bounded by 1), the $\text{COP}$ can exceed unity because refrigeration and heat-pump systems **do not create energy** — they **redistribute** it, using mechanical work as a facilitator of heat transfer.
:::

---

(subsec_clausius_postulate)=
### The Clausius postulate

Refrigeration cycles rely on **forcing heat to move from cold to hot**, a process that can occur only if **external work** is supplied.
This restriction is expressed by the **Clausius postulate**, the complementary formulation of the $2^{\text{nd}}$ law:

:::{epigraph}
**No cyclic process can transfer heat from a colder body to a hotter body without consuming external work.**
:::

The Clausius postulate conveys the same physical limitation as the **Kelvin–Planck** statement but viewed from the opposite perspective:
the latter forbids total conversion of heat into work, while the former forbids spontaneous heat transfer from cold to hot.

---

(subsec_complementarity_postulates)=
### Complementarity of both postulates

The **Kelvin–Planck** and **Clausius** formulations describe the same fundamental constraint on cyclic processes: one concerns **work production**, the other **heat transfer**.
Their equivalence can be shown through the following reasoning.

Assume a **heat engine** capable of violating the Kelvin–Planck postulate, converting all absorbed heat $Q_H$ entirely into work ($Q_L = 0$).
If this work drives a **refrigeration cycle** operating between the same two reservoirs, that cycle would absorb $Q_L$ from the cold reservoir and expel $Q_H + Q_L$ to the hot one.
The overall effect would be a **net transfer of $Q_L$ from cold to hot without any external work** — a direct violation of the **Clausius postulate**.
The inverse argument leads to the same conclusion, proving that both postulates are **logically equivalent** and impose identical restrictions on thermodynamic cycles.

:::{important}

**SUMMARY OF POSTULATE COMPLEMENTARITY**

| **Aspect**                | **Kelvin–Planck (Heat engines)**              | **Clausius (Refrigerators / Heat pumps)**                                                 |
| :------------------------ | :-------------------------------------------- | :---------------------------------------------------------------------------------------- |
| **Cycle type**            | Direct (produces work)                        | Reversed (consumes work)                                                                  |
| **Heat flow**             | Natural: hot → cold                           | Forced: cold → hot                                                                        |
| **Work interaction**      | Output ($W_{\text{net,out}}$)                 | Input ($W_{\text{in}}$)                                                               |
| **Performance measure**   | $\eta_{\text{th.}} = 1 - Q_L/Q_H$             | $\text{COP}_{\text{R}} = Q_L/W_{\text{in}}$, $\text{COP}_{\text{HP}} = Q_H/W_{\text{in}}$ |
| **Limitation**            | Total conversion of heat into work impossible | Heat cannot move from cold to hot without work                                            |
| **Energetic requirement** | Part of heat must be rejected                 | External work must be supplied                                                            |
| **Physical meaning**      | Directionality of energy degradation          | Directionality of energy recovery                                                         |

:::

Both postulates express a single truth: **no cyclic process can occur without an energetic cost**.
For heat engines, this cost is the **unavoidable heat rejection**; for refrigeration cycles, it is the **work input** needed to reverse heat flow.
Together they reveal an inherent **asymmetry of energy transformation** — work can always degrade into heat, but reversing that transformation demands compensation.

This equivalence sets the stage for the next fundamental question:

:::{epigraph}
**What is the maximum performance attainable by a thermodynamic cycle that still satisfies the $2^{\text{nd}}$ law?**
:::

Answering it requires distinguishing between **reversible** and **irreversible** processes.

---

(subsec_conceptual_closure_refrigeration)=
### Conceptual closure

* **Refrigerators** and **heat pumps** are reversed heat engines that use work to move heat *against* its natural direction.
* Their performance is measured through the **coefficient of performance (COP)** — the useful heat transfer achieved per unit of supplied work.
* The **Clausius postulate** states that such a reversed transfer cannot occur spontaneously.
* The **Kelvin–Planck** and **Clausius** statements are complementary expressions of the same $2^{\text{nd}}$-law restriction.
* Together, they define the **directionality and limits** of all cyclic energy transformations: every process carries an energetic cost, and perfect conversion remains physically unattainable.
