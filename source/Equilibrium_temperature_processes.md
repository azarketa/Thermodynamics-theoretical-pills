(sec_equilibrium_temperature_processes)=
## Equilibrium, Temperature Scales, and Processes

This section builds upon the foundations introduced in {ref}`the previous section<sec_magnitudes_properties>` and formalizes how systems reach **equilibrium**, how we define and measure **temperature**, and how we characterize **states** and **processes**.
Thermodynamic equilibrium serves as the conceptual bridge between observable properties and the laws that govern their transformations.

---

(subsec_thermodynamic_equilibrium)=
### Thermodynamic Equilibrium

A system is in **equilibrium** when no measurable changes occur in its macroscopic properties while it is isolated from its surroundings.
In such a state, every possible internal imbalance — mechanical, thermal, or chemical — has been cancelled out.

:::{admonition} Important: Meaning of equilibrium
:class: warning
Thermodynamic equilibrium means that the system has reached a condition where no spontaneous internal evolution occurs.
It represents a state of **maximum stability** under the given constraints.
:::

Intuitively, all systems tend toward equilibrium when left undisturbed.
Mathematically, this natural tendency is described by the **Second Law of Thermodynamics**, which introduces **entropy ($S$)** as the magnitude that quantifies how systems evolve toward equilibrium.

To verify whether a system is in equilibrium, we must examine the following aspects:

* **Mechanical equilibrium:** absence of relative motion or unbalanced forces.
  Since pressure is force per unit area, mechanical equilibrium requires that pressures be uniform throughout the system ($p_1 = p_2$).

* **Thermal equilibrium:** uniform temperature throughout the system and between interacting systems ($T_1 = T_2$).

* **Chemical equilibrium:** uniform composition; chemical concentrations remain constant in time.

A system in full equilibrium satisfies all three conditions simultaneously.

---

(subsec_zeroth_law)=
### Zeroth Law of Thermodynamics and Empirical Definition of Temperature

Chronologically, the **Zeroth Law** was formulated after the other laws, but it is **more fundamental** because it allows temperature to be defined as a measurable property.

It can be stated as follows:

:::{admonition} Important: The Zeroth Law
:class: warning
If two systems are each in thermal equilibrium with a third system, then they are in thermal equilibrium with each other.
:::

Formally, if system $A$ (at temperature $T_A$) is in equilibrium with system $B$ ($T_B$), and $B$ is in equilibrium with $C$ ($T_C$), then:

(eq_zeroth_law_consequence)=
$$
T_A = T_B \quad \text{and} \quad T_B = T_C \ \Longrightarrow \ T_A = T_C
$$

This transitive property implies that temperature is a **well-defined property** independent of system size or composition.
The Zeroth Law does not define a *numerical scale* for temperature but proves that **temperature is a property that can be measured** — it legitimizes the concept of a **thermometer**.

:::{admonition} Note: Empirical meaning of temperature
Temperature is the property that determines whether two systems are in thermal equilibrium.
If no heat flow occurs between them when placed in contact, they share the same temperature.
:::

---

(subsec_temperature_scales)=
### Temperature Scales

Once the Zeroth Law is established, we can build **temperature scales** as comparative protocols.
Any reproducible physical phenomenon that varies monotonically with temperature (such as volume of a liquid, resistance of a wire, or pressure of a gas) can serve as a basis for a scale.

The choice of a scale is conventional — multiple temperature scales coexist, though two are dominant in engineering and science.

(subsubsec_celsius_scale)=
#### The Celsius Scale

The **Celsius scale** (symbol $[^\circ\text{C}]$) was proposed by Anders Celsius, taking as fixed points:

* the **melting point of water**, $0\ [^\circ\text{C}]$, and
* the **boiling point of water**, $100\ [^\circ\text{C}]$,

both measured at standard atmospheric pressure ($1\ \text{atm} = 101325\ \text{Pa}$).

Its main advantage lies in its practical range: it gives convenient numbers for everyday phenomena.

(subsubsec_Kelvin_scale)=
#### The Kelvin Scale

The **Kelvin scale** is the **thermodynamic temperature scale**, forming part of the International System (SI).
It is directly related to the Celsius scale by:

(eq_C_to_K)=
$$
T\left(\text{K}\right) = T\left(^\circ\text{C}\right) + 273.15
$$

William Thomson (Lord Kelvin) deduced the concept of **absolute zero**, the temperature at which molecular motion would theoretically cease.
This lower limit, $0\ \text{K}$, corresponds to $-273.15\ [^\circ\text{C}]$.
While absolute zero cannot be reached (as prohibited by quantum mechanics and the Third Law), it provides a universal reference.

:::{admonition} Important: Absolute temperature
:class: warning
The absolute temperature scale is independent of material properties.
Zero Kelvin represents the limit of complete molecular rest (conceptually), though quantum uncertainty prevents its realization.
This universality makes the Kelvin scale the foundation for scientific and engineering applications.
:::

:::{admonition} Tip: Units and notation
The unit of thermodynamic temperature is the **Kelvin** ($[\text{K}]$), not “degree Kelvin.”
The symbol $^\circ$ is used only for the Celsius scale.
:::

---

(subsec_states_processes)=
### States and Processes

Having introduced the basic measurable quantities and the notion of equilibrium, we can now define the final foundational concepts of Thermodynamics: **states** and **processes**.

A **state** represents the set of physical conditions describing a system at a given moment — each property has a definite value ($p$, $T$, $V$, etc.).
A system’s state can either change with time or remain constant:

* **Steady state:** properties do not vary with time, $\frac{dX}{dt}=0$.
* **Transient state:** properties evolve in time, $\frac{dX}{dt}\neq0$.

A **process** represents the *transition between two states*.
It can be viewed as a path that links an initial state $(1)$ and a final state $(2)$.

:::{admonition} Important: Definition of process
:class: warning
A thermodynamic process is any transformation that carries a system from one equilibrium state to another.
The **path** followed and the **time** required to reach the final state define the type of process.
:::

---

(subsubsec_relaxation_time)=
#### Relaxation Time

When a system is perturbed, it needs a certain time to reach a new equilibrium.
This characteristic duration is known as the **relaxation time** ($\tau$).

Empirically:

* $\tau$ increases with system **volume** ($V$); larger systems take longer to equilibrate.
* $\tau$ decreases with **boundary surface area** ($A$); larger surfaces allow faster exchange.

:::{admonition} Tip: Interpreting relaxation time
A large bath takes longer to heat up because of its larger volume,
but increasing the heating surface reduces the time needed to reach equilibrium.
:::

---

(subsec_typical_processes)=
### Typical Thermodynamic Processes

Although countless processes exist, only a few idealized cases have analytical importance:

1. **Cyclic processes (cycles):**
   Repetitive transformations that start and end at the same state.
   Examples include power and refrigeration cycles.

2. **Quasi-static (reversible) processes:**
   Infinitely slow transformations in which the system remains infinitesimally close to equilibrium at all times.
   In practice, no process is truly quasi-static, but this idealization allows us to derive fundamental relationships among state variables.

:::{admonition} Important: Quasi-static as an ideal limit
:class: warning
A quasi-static process is not real but serves as a **reference model**.
Because equilibrium holds at every stage, the system passes through a continuous series of equilibrium states,
making it possible to define and integrate its thermodynamic properties.
:::

---

(subsec_equilibrium_temperature_processes_conceptual_closure)=
### Conceptual Closure

* Equilibrium means absence of macroscopic changes.
* The Zeroth Law defines temperature as the property indicating thermal equilibrium.
* Temperature scales translate this concept into measurable quantities.
* States describe the condition of a system; processes describe transformations between states.
* Relaxation time connects dynamics with equilibrium.
* Quasi-static processes, though idealized, form the analytical foundation of Thermodynamics.
