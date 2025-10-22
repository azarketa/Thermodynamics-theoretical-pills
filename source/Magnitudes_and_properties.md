Thermodynamics deals with **physical systems** and their measurable characteristics.
To describe any fluid, we need to know *which quantities* define its behavior and *how* those quantities are measured.
This section introduces the **magnitudes** and **properties** that allow us to characterize fluids in macroscopic terms,
laying the groundwork for later laws and state relations.

---

(subsec_physical_magnitudes_units)=
## Physical Magnitudes and Measurement Units

A **magnitude** is any measurable physical quantity associated with a system — such as mass, volume, temperature, or pressure.
Every magnitude must be accompanied by a **measurement unit**, which serves as a fixed reference.

A valid measurement unit must satisfy three essential conditions:

1. It must be **constant** in time and independent of where it is used.
2. It must be **universal**, applicable under all physical conditions.
3. It must be **reproducible**, so that any laboratory can realize it.

:::{admonition} Note: Magnitudes vs. units
A magnitude expresses *what* we measure (e.g., energy or pressure); a unit expresses *how* we measure it (joule, pascal).
Thermodynamics requires both to describe the state of a system quantitatively.
:::

---

(subsec_international_system_units)=
### The International System (SI)

The **International System of Units (SI)** defines seven fundamental magnitudes, from which all others are derived.
In thermodynamics, we commonly employ five of them:

| **Fundamental Magnitude** | **Symbol** | **Unit (SI)** | **Symbol (Unit)** |
| :------------------------ | :--------: | :-----------: | :---------------: |
| Length                    |     $L$    |     metre     |    $[\text{m}]$   |
| Time                      |     $t$    |     second    |    $[\text{s}]$   |
| Mass                      |     $m$    |    kilogram   |   $[\text{kg}]$   |
| Temperature               |     $T$    |     kelvin    |    $[\text{K}]$   |
| Amount of substance       |     $n$    |      mole     |   $[\text{mol}]$  |

From these fundamental ones, many other **derived magnitudes** can be built:

| **Derived Magnitude** | **Definition** | **SI Unit**              | **Unit Expression**                                  |
| :-------------------- | :------------- | :----------------------- | :--------------------------------------------------- |
| Density ($\rho$)      | $\rho = m/V$   | kilogram per cubic metre | $[\text{kg}/\text{m}^{3}]$                           |
| Force ($F$)           | $F = m , a$    | newton                   | $[\text{N}] = [\text{kg}\cdot\text{m}/\text{s}^{2}]$ |
| Pressure ($p$)        | $p = F/A$      | pascal                   | $[\text{Pa}] = [\text{N}/\text{m}^{2}]$              |
| Energy ($E$)          | —              | joule                    | $[\text{J}] = [\text{N}\cdot\text{m}]$               |
| Power ($\dot{W}$)     | —              | watt                     | $[\text{W}] = [\text{J}/\text{s}]$                   |

:::{admonition} Tip: Dimensional reasoning
Knowing how derived units depend on the fundamental ones allows quick error checks and conversion between magnitudes.
Dimensional consistency is a built-in verification of physical correctness.
:::

---

(subsec_extensive_intensive_properties)=
### Extensive and Intensive Properties

Thermodynamic properties can be grouped according to how they depend on the system’s size.

* **Extensive properties** scale with system size; they are *additive*:

  $$
  X_\text{total} = \sum_i X_i
  $$

  Examples: **mass** ($m$), **volume** ($V$), **total energy** ($E$).

* **Intensive properties** are *independent* of system size; they remain unchanged when subsystems are combined.
  Examples: **pressure** ($p$), **temperature** ($T$), **density** ($\rho$).

:::{admonition} Important: Additivity vs. independence
:class: warning
Extensive properties describe *quantities of substance*; intensive properties describe *conditions of substance*.
Thermodynamics relates them through ratios such as “per mass,” “per volume,” or “per mole,” which convert extensives into intensives.
:::

---

(subsec_conversion_extensive_intensive)=
### From Extensive to Intensive: Reference Conversions

Extensive magnitudes can be turned into intensive ones by dividing them by a **reference extensive**:
volume, mass, or amount of substance.
The resulting quantities are densities, specific magnitudes, or molar magnitudes, respectively.

| **Reference Magnitude**     | **Extensive Magnitude**     | **Resulting Intensive Property** | **Expression**     | **Unit (SI)**               |
| :-------------------------- | :-------------------------- | :------------------------------- | :----------------- | :-------------------------- |
| Volume $V$ $[\text{m}^{3}]$ | Mass $m$ $[\text{kg}]$      | Density $\rho$                   | $\rho = m/V$       | $[\text{kg}/\text{m}^{3}]$  |
| Volume $V$ $[\text{m}^{3}]$ | Energy $E$ $[\text{J}]$     | Energy density $e$               | $e = E/V$          | $[\text{J}/\text{m}^{3}]$   |
| Mass $m$ $[\text{kg}]$      | Volume $V$ $[\text{m}^{3}]$ | Specific volume $v$              | $v = V/m = 1/\rho$ | $[\text{m}^{3}/\text{kg}]$  |
| Amount $n$ $[\text{mol}]$   | Volume $V$ $[\text{m}^{3}]$ | Molar volume $v_m$               | $v_m = V/n$        | $[\text{m}^{3}/\text{mol}]$ |

:::{admonition} Tip: Normalization by reference quantity
Relating an extensive magnitude to a reference (mass, volume, or mole) allows property comparison among different systems.
For example, energy per unit mass (specific energy) or per mole (molar energy) are standard thermodynamic descriptors.
:::

---

(subsec_measurable_fundamental_properties)=
### Measurable Fundamental Properties

* **Volume**

    For fluids, **volume** is the only geometrical property of interest.
    Shape and surface area are secondary; the total space occupied by the substance is what matters.
    It is measured in cubic metres $[\text{m}^{3}]$.

* **Mass**

    **Mass** measures the amount of matter and is expressed in kilograms $[\text{kg}]$.
    It is a conserved extensive quantity in all non-reactive processes.

* **Amount of Substance**

    The **amount of substance**, measured in moles $[\text{mol}]$, connects macroscopic and molecular descriptions.
    By definition, one mole of any substance contains the same number of entities (atoms, molecules, ions)
    as there are atoms in $0.012\ \text{kg}$ of carbon-12:

    (eq_mol_def)=
    $$    
    1\ \text{mol} = N_A = 6.022\times10^{23}\ \text{entities}.
    $$

    Thus, $1\ \text{mol}$ of $\text{H}_{2}\text{O}$ contains $6.022\times10^{23}$ water molecules.

:::{admonition} Note: Why the mole matters
Many physical and chemical processes scale with the **number of particles**, not their mass.
At the same temperature and pressure, one mole of any gas occupies the same volume, regardless of its molecular mass.
This makes the mole a natural unit for describing proportionality in reactions and equations of state.
:::

---

(subsec_pressure)=
### Complex Measurable Properties: Pressure

* **Definition**

    **Pressure ($p$)** is the **normal force per unit area** that a system exerts on its boundaries or on another system:

    (eq_pressure_def)=
    $$    
    p = \frac{F_\perp}{A}.
    $$

    Although **force** is a vector, **pressure** is a scalar because it acts normal to the surface element.

* **Units and Scales**

    The SI unit of pressure is the **pascal** $[\text{Pa}] = [\text{N}/\text{m}^{2}]$.
    It is a small unit: a 70 $\text{kg}$ person standing on a $0.3\times0.3\ \text{m}^{2}$ tile exerts
    
    $$
    p = \frac{m g}{A} = \frac{70\text{kg}\times9.81\text{m}/\text{s}^{2}}{0.09\text{m}^{2}} \approx 8\times10^{3}\text{Pa} = 8\text{kPa}.
    $$
    
    Hence, larger multiples are used in practice:
    
    | **Unit**                       |    **Symbol**    |          **Equivalent in Pa**          | **Typical Usage**             |
    | :----------------------------- | :--------------: | :------------------------------------: | :---------------------------- |
    | kilopascal                     |       $[\text{kPa}]$      |          $10^{3}$ $\text{Pa}$          | Engineering and laboratory    |
    | megapascal                     |       $[\text{MPa}]$      |          $10^{6}$ $\text{Pa}$          | High-pressure applications    |
    | atmosphere                     |       $[\text{atm}]$      |    $1.01325\times10^{5}$ $\text{Pa}$   | Standard sea-level pressure   |
    | bar                            |       $[\text{bar}]$      |          $10^{5}$ $\text{Pa}$          | Industrial and meteorological |
    | millibar                       |      $[\text{mbar}]$      |          $10^{2}$ $\text{Pa}$          | Weather data                  |
    | millimetre of mercury          | $[\text{mmHg}]$ or $[\text{torr}]$ |           $133.3$ $\text{Pa}$          | Manometry and medicine        |
    | kilogram per square centimetre |     $[\text{kg}/\text{cm}^{2}]$     | $\approx 9.81\times10^{4}$ $\text{Pa}$ | Legacy (non-SI) unit          |

:::{admonition} Important: Interpretation of 1 atm
:class: warning
At sea level, atmospheric pressure equals approximately $1.013\times10^{5}$ $\text{Pa}$.
This corresponds to the weight of an air column of mass about $200$ $\text{kg}$ pressing on the area of an outstretched human hand ($\approx0.02\ \text{m}^{2}$).
We do not feel this load because internal body pressure counterbalances it; only *pressure differences* are perceptible.
:::

---

(subsec_local_relative_pressures)=
### Local and Relative Pressure Measurements

When measuring pressure, what instruments record is often the **difference** between the local pressure and the surrounding atmospheric one.
Thus, we distinguish four related quantities:

| **Type of Pressure**            | **Definition / Expression**                                 | **Typical Measuring Device** |
| :------------------------------ | :---------------------------------------------------------- | :--------------------------- |
| **Atmospheric pressure**        | Local ambient pressure                                      | Barometer                    |
| **Absolute pressure**           | $p_\text{abs}$ — total pressure relative to absolute vacuum | Barometer                    |
| **Gauge (manometric) pressure** | $p_\text{man} = p_\text{abs} - p_\text{atm}$                | Manometer                    |
| **Vacuum pressure**             | $p_\text{vac} = p_\text{atm} - p_\text{abs}$                | Vacuum gauge                 |

:::{admonition} Tip: Understanding what the gauge shows
Pressure gauges and manometers report the **difference** from the current atmospheric value.
When a tire reads “2 bar,” it means 2 bar *above* ambient, not 2 bar absolute.
:::

---

(subsec_complex_measurable_properties_temperature)=
### Complex Measurable Properties: Temperature

(subsubsec_microscopic_macroscopic_temperature)=
#### Microscopic and Macroscopic Perspectives

From the **microscopic** viewpoint, temperature measures the **average kinetic energy** of particles:
the higher their mean velocity, the higher the temperature.
This parallels the notion of microscopic pressure as the collective effect of countless particle impacts on boundaries.

From the **macroscopic** standpoint, temperature is a **state variable** that indicates the degree of thermal equilibrium between systems.

:::{admonition} Important: Intensive nature of temperature
:class: warning
Unlike extensive quantities such as mass or energy, **temperature is an intensive property** — it does not add up.
Combining two bodies of water at $100\ ^\circ\text{C}$ does not yield $200\ ^\circ\text{C}$;
the final temperature lies between them, depending on heat capacities and masses.
:::

---

(subsubsec_operational_definition_temperature)=
#### Operational Definition

Because temperature cannot be measured by simple addition or direct comparison, two requirements are needed:

1. A **measurement unit** — the kelvin $[\text{K}]$ — defined as a fundamental SI magnitude.
2. A **reference procedure** to compare temperatures, based on equilibrium and reproducible reference points (e.g., triple point of water).

The establishment of such procedures leads directly to the notion of **thermodynamic equilibrium**,
a condition where no net macroscopic changes occur and temperature is uniform throughout the system.

:::{admonition} Note: Why equilibrium matters
Defining temperature requires that the system be at equilibrium; otherwise, local variations prevent consistent measurement.
Thermodynamic temperature scales are founded on equilibrium states, which provide reproducible reference conditions.
:::

---

(subsec_conceptual_closure_magnitudes_properties)=
### Conceptual Closure

* Magnitudes and properties provide the measurable framework for describing thermodynamic systems.
* Fundamental and derived quantities, together with their units, form the basis of all thermodynamic analysis.
* The distinction between extensive and intensive properties defines how system size affects measurable quantities.
* Pressure and temperature serve as key intensive variables that connect directly to equilibrium and energy exchange.
* These concepts prepare the ground for the study of equilibrium, temperature scales or processes, as done {ref}`in the next section <sec_equilibrium_temperature_processes>`, where the conditions of balance and transformation between states are formally introduced.


```python

```
