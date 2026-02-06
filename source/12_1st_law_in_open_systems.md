(sec_open_systems)=
## $1^{\text{st}}$ law in open systems

While the $1^{\text{st}}$ law for **closed systems** expresses the balance between energy transfer as heat and work ($\Delta E = Q - W$), real engineering devices rarely operate in isolation.
**Turbines**, **compressors**, **pumps**, **nozzles**, and **heat exchangers** are all examples of **open systems**, in which **mass** and **energy** continuously cross the system boundaries.

The aim of this section is to extend the $1^{\text{st}}$ law to these **flow systems**, beginning with the principle of **mass conservation**, introducing the concept of **flow work**, and finally deriving the **steady-flow energy equation** expressed in terms of **enthalpy**.

---

(subsec_mass_conservation_open_systems)=
### Mass conservation

The starting point in any open-system analysis is the **continuity equation**, which expresses that the **rate of change of mass** within a control volume (CV) equals the **difference between the inflowing and outflowing mass rates**:

(eq_continuity_equation)=
$$
\frac{\mathrm{d}m_{\text{cv}}}{\mathrm{d}t} = \frac{\mathrm{d}m}{\mathrm{d}t}
= \sum_{\text{in}} \dot{m} - \sum_{\text{out}} \dot{m}.
$$

This equation is the formal statement of **mass conservation**. As we will be dealing with control volumes throughout the formulation of equations that correspond to open systems, we will drop off the CV subscript hereon for the sake of clarity, just as done after the first equality {ref}`in the expression above <eq_continuity_equation>`.

If the properties of the control volume **do not change in time**, the system is said to operate under **steady-state conditions**:

(eq_continuity_steady_state)=
$$
\frac{\mathrm{d}m}{\mathrm{d}t} = 0
\quad\Longrightarrow\quad
\sum_{\text{in}} \dot{m} = \sum_{\text{out}} \dot{m}.
$$

A **steady system** is therefore one in which the **mass inside the control volume remains constant**, even though individual fluid particles continuously enter and leave.
This assumption is valid for most engineering devices working under design conditions, where the inlet and outlet flows remain stable with time.

:::{important}

**SINGLE INLET-SINGLE OUTLET (STEADY)**

With one inlet (1) and one outlet (2) at steady state,

(eq_continuity_single_inlet_outlet)=
$$
\boxed{\dot m_1 = \dot m_2 \equiv \dot m} \ ,
$$

which means that **all the mass flux entering** from the inlet **must be coming out** from the outlet.
:::

:::{note}

**STEADY-STATE MEANING**

A steady state does not imply that the **flow is static** — it only means that, when observed over time, the **average properties** (mass, pressure, temperature, etc.) within the control volume remain constant.
:::

---

(subsec_flow_work_notion)=
### The flow-work notion

In closed systems, work is associated with boundary movement ($p\mathrm{d}V$). In open systems, however, mass crosses the control surface, and a **pressure force** must act to push it through. This required mechanical effort is called **flow work** (or **flow energy**).

Consider an imaginary piston pushing fluid into the system.
If the piston face has area $A$, the pressure on the fluid is $p$, and the velocity normal to the surface is $V_\perp=c$, the force and power associated with the inflow are:

(eq_flow_work)=
$$
F = p A,
\qquad
\dot{W}_\text{flow} = Fc = pAc = \dot{m}(pv),
$$

where $\dot{m} = \rho{}A{}c$ and $v = 1/\rho$ is the specific volume.

Thus, each mass flow crossing the boundary carries an **associated rate of mechanical work** equal to $pv$.

:::{important}

**PHYSICAL MEANING OF FLOW WORK**

Flow work represents the **pressure effort required to drive the fluid** across a control boundary.
It is not an independent form of energy but rather part of the **mechanical work** involved in maintaining steady flow through the device.
:::

---

(subsec_first_law_open_systems)=
### Derivation of the $1^{\text{st}}$ law for open systems

We start from the **balance principle**: the **rate of change of energy in the control volume** equals the **rate of energy in** minus the **rate of energy out** (all extensive rates):

(eq_1st_law_open_systems_general)=
$$ \frac{\mathrm{d}E}{\mathrm{d}t} = \Big(\dot Q_{\text{in}} - \dot W_{\text{in}} + \sum_{\text{in}} \dot m e\Big) - \Big(\dot Q_{\text{out}} - \dot W_{\text{out}} + \sum_{\text{out}} \dot m e\Big),
$$

where the **specific total energy** of a flowing stream is

(eq_total_energy_specific)=
$$
e = u + \frac{c^2}{2} + g z.
$$

It is convenient to define **net** heat and work rates for the control volume:

(eq_definitions_heat_work_rates_open_systems)=
$$
\dot Q \equiv \dot Q_{\text{in}} - \dot Q_{\text{out}}, \qquad \dot W \equiv \dot W_{\text{out}} - \dot W_{\text{in}}
$$

so that, being both heat **to** the CV and work **from** the CV positive:

(eq_1st_law_open_systems_simplified_ver1)=
$$
\frac{\mathrm{d}E}{\mathrm{d}t} = \dot Q - \dot W + \sum_{\text{in}} \dot m e - \sum_{\text{out}} \dot m e.
$$

---

(subsec_steady_state_open_systems_internal_energy)=
### Steady-state formulation (internal-energy-based)

In a **steady-flow process**, the energy content of the control volume remains constant over time:

(eq_condition_steady_state)=
$$
\frac{\mathrm{d}E}{\mathrm{d}t} = 0.
$$

Hence,

(eq_1st_law_open_systems_simplified_energy_terms)=
$$
\boxed{\dot{Q} - \dot{W} = \sum_{\text{out}} \dot{m} \left(u + \frac{c^2}{2} + g z\right) + \sum_{\text{in}} \dot{m} \left(u + \frac{c^2}{2} + g z\right)} \ .
$$

:::{important}

**SINGNLE INLET-SINGLE OUTLET (SPECIFIC FORM, ENERGY-BASED)**

With $\dot m_1=\dot m_2=\dot m$ and dividing by $\dot m$,

(eq_1st_law_open_systems_simplified_energy_terms_single_inlet_outlet)=
$$
\boxed{q - w = \big(u_2 - u_1\big) + \frac{c_2^2 - c_1^2}{2} + g(z_2 - z_1)} \ .
$$

:::

---

(subsec_steady_state_open_systems_enthalpy)=
### Steady-state formulation (enthalpy-based)

In most open-system devices, not all the mechanical work results from pushing the fluid through the boundaries. Part of it appears as **useful mechanical power** transmitted through a rotating shaft, as in **turbines**, **compressors**, or **pumps**. This component is called **shaft work**, and together with the **flow work** it makes up the total mechanical interaction across the system boundary. Thus, the total work rate contains **shaft** and **flow** parts:

(eq_decomposition_work_contributions_open_systems)=
$$
\dot W = \dot W_{\text{shaft}} + \dot W_{\text{flow}}, \qquad \dot W_{\text{flow}} = \sum \dot m pv.
$$

Substituting and regrouping (moving flow work into the stream energies) gives the **general unsteady open-system form** in internal-energy variables:

(eq_1st_law_open_systems_simplified_ver2)=
$$
\frac{\mathrm{d}E}{\mathrm{d}t} =\dot Q - \dot W_{\text{shaft}} +\sum_{\text{in}}\dot m\left(u + pv + \frac{c^2}{2}+g z\right)
-\sum_{\text{out}}\dot m\left(u + pv + \frac{c^2}{2}+g z\right).
$$

Since $h \equiv u + p v$, the steady balance becomes

(eq_1st_law_open_systems_enthalpy_terms)=
$$
\boxed{\dot Q - \dot W_{\text{shaft}} = \sum_{\text{out}} \dot m \left(h + \frac{c^2}{2} + g z\right) + \sum_{\text{in}} \dot m \left(h + \frac{c^2}{2} + g z\right)} \ .
$$

:::{important}

**SINGLE INLET-SINGLE OUTLET (SPECIFIC FORM, ENTHALPY-BASED)**

With $\dot m_1=\dot m_2=\dot m$ and dividing by $\dot m$,

(eq_1st_law_open_systems_enthalpy_terms_single_inlet_outlet)=
$$
\boxed{q - w_{\text{shaft}} = (h_2 - h_1) + \frac{c_2^2 - c_1^2}{2} + g(z_2 - z_1)} \ .
$$

:::

::::{important}

**COMPARATIVE FORMULATION OF CLOSED AND OPEN SYSTEMS**

| **Formulation** | **Closed system** | **Open system under steady flow (single inlet-outlet when applies)** |
| :-  | :-  | :- |
| **General form of the $1^{\text{st}}$ law** | $\displaystyle \Delta{}E = \Delta{U} + \Delta{E_{\text{k}}} + \Delta{E_{\text{p}}} = Q - W$ | $\displaystyle \dot{Q} - \dot{W} = \sum_{\text{out}} \dot{m} \left(u + \frac{c^2}{2} + g z\right) + \sum_{\text{in}} \dot{m} \left(u + \frac{c^2}{2} + g z\right)$ <br/> $\displaystyle \dot{Q} - \dot{W}_{\text{shaft}} = \sum_{\text{out}} \dot{m} \left(h + \frac{c^2}{2} + g z\right) + \sum_{\text{in}} \dot{m} \left(h + \frac{c^2}{2} + g z\right)$ |
| **Work components** | Boundary work only $\displaystyle \int p\mathrm{d}v$ | Shaft work $\displaystyle \left(-\int v\mathrm{d}p\right)$ + flow work $\displaystyle (\Delta(pv))$|
| **Specific form** | $\displaystyle \Delta{u} + \Delta{e_{\text{k}}} + \Delta{e_{\text{p}}} = q - w$ | $\displaystyle q - w = (u_2 - u_1) + \tfrac{c_2^2 - c_1^2}{2} + g(z_2 - z_1)$ <br/> $\displaystyle q - w_{\text{shaft}} = (h_2 - h_1) + \tfrac{c_2^2 - c_1^2}{2} + g(z_2 - z_1)$ |
| **Typical examples**  | Piston–cylinder, rigid tank | Compressor, turbine, diffuser, nozzle, heat exchanger, mixer, valve|

:::{note}

**DIFFERENTIAL FORM OF THE SHAFT WORK**

Due to the {ref}`work decomposition relation <eq_decomposition_work_contributions_open_systems>`, such a relation can be written for differential work-like energy transfers. As $\delta{}w=p\mathrm{d}v$ in simple compressible systems, and $\delta{}w_{\text{flow}}=\mathrm{d}(pv)$

(eq_shaft_work_expression)=
$$
\delta{}w = \delta{}w_{\text{shaft}} + \delta{}w_{\text{flow}} \implies p\mathrm{d}v = \delta{}w_{\text{shaft}} + \mathrm{d}(pv) = \delta{}w_{\text{shaft}} + p\mathrm{d}v + v\mathrm{d}p \implies
$$

$$
\implies \boxed{\delta{}w_{\text{shaft}} = -v(p)\mathrm{d}p} \ , \qquad \boxed{w_{\text{shaft}} = -\int_{p_1}^{p_2} v(p)\mathrm{d}p} \ .
$$

:::

::::

---

(subsec_conceptual_closure_open_systems)=
### Conceptual closure

The $1^{\text{st}}$ law for open systems shows how energy conservation applies when **mass** and **energy** cross system boundaries. Its key ideas can be summarized as follows:

* **Mass conservation** — At steady state, the mass entering and leaving the control volume is the same, ensuring no net accumulation.
* **Flow work** — A pressure force must act to drive the fluid across each boundary; this mechanical effort accompanies every mass flow.
* **Work types** — The total work divides into **shaft work**, representing useful mechanical power, and **flow work**, representing the energy carried with the mass flow.
* **Steady operation** — In steady conditions, the heat and shaft work interactions exactly balance the energy changes between the inlet and outlet streams.
* **Role of enthalpy** — Combining internal energy and flow work into **enthalpy** simplifies open-system analysis, making it easier to express energy balances.

The upshot is that energy remains conserved, but in open systems it moves not only as heat or work, but also **with the mass** that continuously flows through the control volume.
