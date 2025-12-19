(sec_icre_parameters)=
## Fundamental parameters and characteristics of ICREs

After describing and classifying **internal combustion reciprocating engines (ICREs)** and introducing their main components, the narrative can now be narrowed to what matters most for a thermodynamics course: the **thermo-mechanical cycle** itself. From this point on, the goal is to describe the evolution of pressure, temperature, and volume inside the cylinder in a way that allows ideal-cycle modelling (Otto/Diesel) and, later, the inclusion of real-cycle losses.

To do so, we introduce the main **geometric**, **volumetric**, **combustion**, and **power-related** parameters that characterize the engine.

---

(subsec_icre_geometric_parameters)=
### Geometric parameters

The core kinematic system of a reciprocating engine is the **combustion chamber–piston–connecting rod–crankshaft** mechanism. The standard geometric parameters used to describe it are:

- $\theta$: **crank angle**, defined as $\theta=0^\circ$ when the connecting rod and crank are aligned at their maximum extension.
- **TDC (top dead center)**: piston position corresponding to $\theta=0^\circ$.
- **BDC (bottom dead center)**: piston position corresponding to $\theta=180^\circ$.
- $b$: **bore**, i.e., piston diameter.
- $l$: **connecting rod length**, typically modelled as a rigid straight bar.
- $a$: **crank radius**.
- $s = 2a$: **stroke**, the piston travel between TDC and BDC.

The **stroke-to-bore ratio**, $s/b$, is an important geometric indicator. Typical values are:

- automotive **spark-ignition (SI)** engines: $0.6 \le s/b \le 1.1$,
- automotive **compression-ignition (CI)** engines: $0.9 \le s/b \le 1.2$,
- larger slow four-stroke CI engines (e.g., trucks and small ships): $1.2 \le s/b \le 1.4$,
- very large two-stroke CI marine engines: $1.8 \le s/b \le 3$.

:::{note}

**WHY $s/b$ MATTERS**

The stroke-to-bore ratio influences:
- piston mean speed for a given rpm (and thus friction and wear),
- heat-transfer area-to-volume ratios,
- mechanical packaging and achievable rpm,
- and, indirectly, combustion characteristics through chamber geometry.

:::

---

(subsec_icre_volumes_compression_displacement)=
### Volumes, compression ratio, and displacement

Beyond length-scale parameters, engine geometry is often described through **volumes** and **volume ratios**:

- $V_1$: cylinder volume at **BDC** (maximum volume).
- $V_2$: cylinder volume at **TDC** (minimum volume, clearance volume).
- $V_d$: **displacement volume** (swept volume), defined as:
  
  $$
  V_d = V_1 - V_2 = \frac{\pi}{4} b^2 s .
  $$

The **compression ratio** is defined as:

$$
r = \frac{V_1}{V_2}.
$$

:::{important}

**COMPRESSION RATIO IS A VOLUME RATIO**

In ICREs, $r$ is a ratio of **volumes**, not pressures.  
This contrasts with the Brayton cycle, where the key ratio is the **pressure ratio**.

:::

The **engine displacement** (total swept volume) is:

$$
V_{d,\text{eng}} = Z\,V_d,
$$

where $Z$ is the number of cylinders.

---

(subsec_icre_heat_input_combustion_parameters)=
### Heat input and combustion parameters

To connect engine operation with thermodynamic cycle modelling, it is useful to relate fuel energy release to an equivalent **heat input**.

#### Standard cold-air model (air-standard assumptions)

A common starting point is the **air-standard cold-air model**, which assumes:

- air is the working fluid, modelled as an **ideal gas**,
- all processes are internally reversible,
- combustion is replaced by an equivalent **heat addition** process,
- exhaust and intake are replaced by a **heat rejection** process restoring air to the initial state,
- air has constant specific heats equal to their values at $25^\circ\text{C}$.

Under these assumptions, the heat input per unit mass of air can be expressed using the fuel lower heating value and the air–fuel ratio.

#### Heat input with air–fuel mixture

Let:

- $q_{\text{in}}$ be the heat added (units commonly: $\text{kJ/kg air}$ or $\text{kJ/kg mixture}$),
- $\text{LHV}$ be the fuel **lower heating value** ($\text{kJ/kg fuel}$),
- $A_s$ be the **stoichiometric** air–fuel ratio ($\text{kg air}/\text{kg fuel}$),
- $A$ be the actual air–fuel ratio ($\text{kg air}/\text{kg fuel}$),
- $\lambda$ be the **relative air–fuel ratio** (excess-air factor), so that

  $$
  A = \lambda A_s .
  $$

Then, when working per unit mass of air:

$$
q_{\text{in}} = \frac{\text{LHV}}{A}
= \frac{\text{LHV}}{\lambda A_s}.
$$

If the working fluid is considered as the **air–fuel mixture** instead of air alone, then per unit mass of mixture:

$$
q_{\text{in}} = \frac{\text{LHV}}{1 + A}
= \frac{\text{LHV}}{1 + \lambda A_s}.
$$

:::{tip}

**CHOOSING THE BASIS ($\text{kg air}$ vs $\text{kg mixture}$)**

Both definitions are used in practice.  
For ideal Otto/Diesel cycle analysis, it is often convenient to work per unit mass of air, because the air-standard model treats the working fluid as air throughout the cycle.

:::

---

(subsec_icre_power)=
### Power output and air mass flow rate

A key performance quantity is the **power output**, defined as:

$$
\text{Pot} = \dot{m}_{\text{air}}\, w_{\text{net}},
$$

where:

- $\text{Pot}$ is the power ($\text{kW}$),
- $w_{\text{net}}$ is the **specific net work** ($\text{kJ/kg}$),
- $\dot{m}_{\text{air}}$ is the air mass flow rate ($\text{kg/s}$).

A practical estimate of $\dot{m}_{\text{air}}$ can be built from geometry and operating speed. Approximating the inducted air mass flow as:

- density times volume per cycle times number of cycles per second,

one obtains:

$$
\dot{m}_{\text{air}} = \rho \left(\frac{\pi}{4} b^2\right) s \left(\frac{N}{60}\right)iZ,
$$

and therefore:

$$
\text{Pot}
= w_{\text{net}} \, \rho \left(\frac{\pi}{4} b^2\right) s \left(\frac{N}{60}\right)iZ .
$$

Here:

- $\rho$ is the intake air density ($\text{kg/m}^3$),
- $N$ is the engine speed in rpm,
- $Z$ is the number of cylinders,
- $i$ is a factor that accounts for how often a cylinder inducts fresh charge:
  - $i = \frac{1}{2}$ for **four-stroke** engines (one intake event every two revolutions),
  - $i = 1$ for **two-stroke** engines (one intake event every revolution).

:::{note}

**WHAT THIS POWER MODEL CAPTURES (AND WHAT IT DOES NOT)**

This expression captures the scaling of power with:
- specific work $w_{\text{net}}$,
- displacement volume ($b^2 s$),
- speed $N$,
- number of cylinders $Z$,
- and intake density $\rho$ (which links directly to altitude and boosting).

It does not include volumetric efficiency, flow restrictions, residual gases, or detailed gas exchange modelling, which are introduced later when moving beyond ideal cycles.

:::

---

(subsec_icre_fuel_consumption)=
### Fuel consumption

Fuel consumption is commonly tied to the **air–fuel ratio**:

$$
A = \frac{\dot{m}_{\text{air}}}{\dot{m}_{\text{fuel}}}.
$$

Therefore:

$$
\dot{m}_{\text{fuel}} = \frac{\dot{m}_{\text{air}}}{A} = \frac{\dot{m}_{\text{air}}}{\lambda A_s}.
$$

This expression highlights the key dependencies:

- for fixed $\dot{m}_{\text{air}}$, richer operation (lower $\lambda$) increases fuel flow,
- increasing inducted air mass flow (higher $\rho$, higher displacement, higher rpm, boosting) increases fuel flow for a given mixture strength.

:::{important}

**LINK TO EFFICIENCY**

Once $q_{\text{in}}$ and $\dot{m}_{\text{fuel}}$ are defined consistently, the bridge to efficiency metrics becomes direct:
- higher $w_{\text{net}}$ at fixed $q_{\text{in}}$ means higher thermal efficiency,
- lower $\dot{m}_{\text{fuel}}$ for the same power means lower specific fuel consumption.

These connections will be made explicit when introducing the ideal Otto and Diesel cycles and their real-cycle corrections.

:::

---

(subsec_icre_parameters_closure)=
### Conceptual closure

- The thermo-mechanical cycle of ICREs is described through crank-angle-based geometry and volume evolution.
- The key volumetric quantities are $V_1$, $V_2$, $V_d$, and the compression ratio $r = V_1/V_2$.
- Heat input can be expressed per unit mass of air or per unit mass of mixture, using $\text{LHV}$ and the air–fuel ratio.
- Power scales with inducted air mass flow and specific net work: $\text{Pot}=\dot{m}_{\text{air}} w_{\text{net}}$.
- Fuel mass flow follows directly from $\dot{m}_{\text{fuel}}=\dot{m}_{\text{air}}/(\lambda A_s)$.
