(sec_aircraft_gas_turbines)=
## Aircraft gas turbines

Gas-turbine technology is employed in two broad and conceptually distinct applications: **stationary power generation** and **aeronautical propulsion**. While both rely on gas cycles derived from the Brayton cycle, their objectives, performance metrics, and design constraints differ fundamentally.

In **stationary gas turbines**, the primary goal is the generation of a net mechanical or electrical power output. These systems are typically installed in power plants or large ships, where size and weight are secondary concerns and continuous operation at near-design conditions is common. The search for higher thermal efficiencies in such applications has led to advanced configurations, including combined gas–vapor cycles.

In contrast, **aircraft gas turbines** are propulsion systems. Their purpose is not to deliver shaft power directly, but to generate **thrust** by accelerating a working fluid. Weight, frontal area, noise, fuel consumption, and performance over wide ranges of speed and altitude become dominant design constraints. These differences motivate a separate analysis of aircraft engines, even though the underlying thermodynamic principles remain closely related to those of stationary gas turbines.

---

(subsec_aircraft_power_orders)=
### Orders of magnitude in aircraft propulsion

The power levels involved in aircraft propulsion are extremely large when compared with conventional ground vehicles. As an illustration, a wide-body commercial aircraft such as the Boeing 777, equipped with two General Electric GE90-115B engines, requires on the order of $23\ \text{MW}$ per engine during cruise at full load.

Recalling that $1\ \text{hp} = 0.7457\ \text{kW}$, a single engine operating at this level corresponds to approximately $31\,000\ \text{hp}$. For comparison, a Formula 1 car develops roughly $1\,000\ \text{hp}$, while a typical passenger car delivers about $100\ \text{hp}$. Even larger power levels are reached during take-off: for instance, the Airbus A380, equipped with four GP7200 engines, may require a total power in excess of $300\ \text{MW}$.

These figures highlight the extraordinary energy flows involved in aircraft propulsion systems.

---

(subsec_aircraft_engine_types)=
### Main types of aircraft gas-turbine engines

Aircraft gas turbines are designed according to the intended operating regime, leading to several distinct engine architectures.

- **Turbojet engines**

    The **turbojet** represents the simplest form of gas-turbine propulsion and is directly based on the Brayton cycle. Proceeding in the direction of the flow, a turbojet consists of:
    
    - a **diffuser**, which decelerates the incoming air,
    - a **compressor**, which raises the pressure of the flow,
    - a **combustion chamber**, where heat is added,
    - a **turbine**, which drives the compressor and auxiliary systems,
    - a **nozzle**, which converts enthalpy into kinetic energy.
    
    Turbojets are compact and capable of operating at very high flight speeds. However, they exhibit high fuel consumption, elevated noise levels, and poor efficiency at low speeds.

<br/>

- **Turboprop engines**

    In a **turboprop**, the turbine drives a shaft connected to a reduction gearbox and a propeller. Most of the propulsion is provided by the propeller rather than by the exhaust jet.
    
    This configuration results in:
    
    - lower exhaust velocities,
    - higher propulsive efficiency at low speeds,
    - significantly reduced fuel consumption compared to turbojets.
    
    Turboprops are well suited for low-speed and low-altitude flight, such as in cargo aircraft and helicopters. Their main limitations arise from the weight of the gearbox–propeller assembly and from the onset of sonic conditions at the propeller blade tips, which restricts their maximum operating speed.

<br/>

- **Turbofan engines**

    The **turbofan** combines features of turbojets and turboprops and is the most widely used propulsion system in commercial aviation. A portion of the incoming air bypasses the core engine and is accelerated by a large fan.
    
    This configuration:
    
    - increases propulsive efficiency,
    - reduces noise levels,
    - provides additional cooling for engine components.
    
    Turbofans are more efficient than turbojets over a wide range of subsonic speeds, though their larger frontal area and higher weight reduce effectiveness at very high altitudes.

---

(subsec_high_speed_engines)=
### Propulsion at high subsonic and supersonic speeds

At higher flight speeds, alternative propulsion concepts are employed.

- **Ramjets** (stato-reactors) operate without compressors or turbines. Compression is achieved through the deceleration of the incoming high-speed flow. Fuel is
  injected, combustion occurs, and expansion takes place through a nozzle. Ramjets are effective at high subsonic and supersonic speeds but cannot operate from rest.

- **Scramjets** (supersonic combustion ramjets) are a variation in which combustion occurs at supersonic flow conditions. These engines contain no rotating machinery and consist essentially of a shaped duct. Scramjets do not operate according to a Brayton cycle and represent the simplest architecture from a mechanical standpoint.

- **Rocket engines** differ fundamentally from air-breathing engines. They carry both fuel and oxidizer and do not rely on atmospheric air. Their operating principles lie outside the scope of gas-turbine Brayton-cycle analysis.

---

(subsec_propulsion_parameters)=
### Performance parameters of aircraft gas turbines

To evaluate and compare propulsion systems, several characteristic quantities are defined.

The **thrust** produced by the engine is given by:

(eq_thrust)=
$$
F = \dot{m}{}(c_{\text{out}} - c_{\text{in}}),
$$

where $\dot{m}$ is the mass flow rate and $c$ denotes flow velocity.

The **thermal power supplied** by the fuel is:

(eq_thermal_power)=
$$
\dot{Q}_{\text{th}} = \dot{m}_{\text{fuel}}{\cdot}\text{LHV},
$$

where $\text{LHV}$ is the lower heating value of the fuel.

The **power added to the flow** is associated with the kinetic energy change:

(eq_power_flow)=
$$
\dot{W}_{\text{flow}} = \frac{1}{2}{}\dot{m}{}(c_{\text{out}}^2 - c_{\text{in}}^2).
$$

The **propulsive power** is defined as:

(eq_propulsive_power)=
$$
\dot{W}_{\text{prop}} = c_{\text{flight}}{\cdot}F,
$$

where $c_{\text{flight}}$ is the flight speed.

---

(subsec_efficiencies)=
### Efficiencies in aircraft propulsion

From the previous definitions, three efficiencies are introduced:

- **Thermal efficiency:**
  $$
  \eta_{\text{th}} = \frac{\dot{W}_{\text{flow}}}{\dot{Q}_{\text{th}}}.
  $$

- **Propulsive efficiency:**
  $$
  \eta_{\text{prop}} = \frac{\dot{W}_{\text{prop}}}{\dot{W}_{\text{flow}}}.
  $$

- **Overall (motopropulsive) efficiency:**
  $$
  \eta_{\text{global}} = \frac{\dot{W}_{\text{prop}}}{\dot{Q}_{\text{th}}} = \eta_{\text{th}}{\cdot}\eta_{\text{prop}}.
  $$

Different propulsion systems exhibit distinct efficiency trends as functions of flight speed. Turboprops are most efficient at low speeds, turbofans dominate a broad subsonic regime, and turbojets become advantageous at very high speeds.

---

(subsec_specific_impulse)=
### Specific impulse and fuel consumption

An additional performance indicator is the **specific impulse**, $I_{\text{sp}}$, defined as:

(eq_specific_impulse)=
$$
I_{\text{sp}} = \frac{F}{g_0{\cdot}\dot{m}},
$$

where $g_0$ is the standard gravitational acceleration and $\dot{m}$ is the fuel or propellant mass flow rate.

The specific impulse measures how efficiently a propulsion system uses its propellant. A high specific impulse implies lower fuel consumption for a given thrust and operating time.

Specific impulse is inversely related to **specific fuel consumption**, which quantifies the fuel required to produce a given thrust over a given time interval.

---

(subsec_aircraft_conceptual_closure)=
### Conceptual closure

- Aircraft gas turbines are propulsion systems, not power generators.
- Their design priorities differ fundamentally from those of stationary gas   turbines.
- Turbojets, turboprops, and turbofans address different flight regimes.
- Ramjets and scramjets operate without rotating machinery and do not follow a Brayton cycle.
- Thrust, efficiencies, and specific impulse are key performance metrics.
- Turbofans provide the highest efficiency over most subsonic commercial flight conditions.
