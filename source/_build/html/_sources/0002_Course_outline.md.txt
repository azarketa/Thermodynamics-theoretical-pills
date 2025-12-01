(sec_course_outline)=
# Course outline

The course develops progressively — from the **foundations of thermodynamic reasoning** to the **analysis of canonical thermal cycles** that underpin real energy-conversion systems.
Each block introduces a self-contained set of principles while remaining grounded in measurable quantities and engineering interpretation.

(subsec_fundamentals)=
## Fundamentals

This first block builds the conceptual and mathematical tools required to analyze any thermodynamic system, regardless of its nature or scale.

* **Systems, surroundings, and boundaries**
  Establishes how to define a *system* (control mass or control volume) and distinguish it from its *surroundings*.
  Introduces *boundaries* (fixed or moving) and the concept of *interaction* between system and surroundings via heat and work.

* **Properties and magnitudes**
  Distinguishes *intensive* (temperature, pressure) from *extensive* (mass, energy) properties.
  Defines *state*, *process*, and *cycle*; introduces the concept of *state functions* versus *path functions* (e.g., $U$ vs. $Q$, $W$).
  Presents equilibrium conditions and the notion of *quasi-static* processes as idealized reference transformations.

* **Models for substances**

  * *Perfect gas model*: the simplest, linear relation among $p$, $v$, and $T$, valid at low pressures; ideal-gas equation as a working model.
  * *Real gases*: deviations from ideality via compressibility factors; qualitative view of intermolecular effects.
  * *Pure substances*: phase-change behavior, $p–v–T$ diagrams, saturation dome, critical point, subcooled liquid, and superheated vapor.
  * *Mixtures and atmospheric air*: composition variables, mixture rules, and the idea of *psychrometric properties* (humidity, specific humidity, enthalpy of moist air).

* **Interactions: work and heat**
  Defines *work* and *heat* as energy in transit, associated respectively with *organized* and *disorganized* molecular motion.
  Emphasizes sign conventions and path dependence; includes mechanical (shaft, boundary, electrical) and flow work examples.

* **$1^{\text{st}}$ law of thermodynamics**

  * *Closed systems*: internal energy change as the net balance between heat added and work done, $\Delta U{}={}Q{}-{}W$.
    Introduces special processes — isochoric, isobaric, isothermal, adiabatic — and their energy implications.
  * *Open systems*: steady-flow energy equation (SFEE), showing the interplay between enthalpy, kinetic, and potential energies.
    Canonical devices: **turbine**, **compressor/pump**, **nozzle/diffuser**, **heat exchanger**, **mixing chamber**, **throttling valve**.
    Each device type is studied under simplifying assumptions that reveal its characteristic energy conversion.

* **$2^{\text{nd}}$ law of thermodynamics**
  Introduces the concepts of *directionality* and *limitation*.
  States the **Kelvin–Planck** and **Clausius** formulations; defines *entropy* as a property whose change quantifies irreversibility.
  Establishes *entropy balance*, *reversible* vs. *irreversible* processes, and device efficiencies (isentropic and overall).

* **Exergy and irreversibility**
  Combines the first and $2^{\text{nd}}$ laws to express the *useful portion of energy* relative to an environment (the *dead state*).
  Defines *flow exergy*, *non-flow exergy*, and *exergy destruction* $I{}={}T_0 S_{\text{gen}}$.
  Provides a unified framework for quantifying the *quality* of energy and losses across systems.

:::{admonition} Note: a summary of the Fundamentals outline
:class: note, dropdown

**Central idea:** The fundamentals establish a language — systems, states, energy forms, entropy, and exergy — that enables any real process or device to be expressed as a structured balance of *quantities* and *inefficiencies*.
This foundation supports every subsequent cycle analysis.
:::

(subsec_gas_cycles)=
## Gas cycles

This block applies the laws of thermodynamics to *continuous-flow* systems working primarily with gases as the working medium.
It explores both *idealized* cycles (as baselines) and *realistic* configurations (with losses and efficiencies).

* **General notions**
  Defines what a *cycle* is — a closed sequence of processes returning the working fluid to its initial state.
  Introduces *thermal efficiency*, *work ratio*, and *pressure ratio* as performance indicators.
  Differentiates *ideal* cycles (reversible, no losses) from *actual* ones (irreversibilities and component inefficiencies).

* **Usual types and applications**
  Presents the diversity of gas cycles: simple, regenerated, intercooled, reheat, and combined forms.
  Discusses where each appears — e.g., **power generation**, **aerospace propulsion**, **industrial turbines**.

* **Brayton cycle (Ideal)**
  Describes the sequence *compression → heat addition → expansion → heat rejection*.
  Develops relations for efficiency as a function of pressure ratio and temperature limits; explains the back-work ratio concept.

* **Real Brayton cycles**
  Introduces *isentropic efficiencies* for compressor and turbine, *pressure drops* in combustion and heat exchange, and *regenerator effectiveness*.
  Examines performance sensitivity and practical optimization (pressure ratio, turbine inlet temperature).

* **Stationary gas turbines**
  Discusses design trade-offs, part-load behavior, and regeneration/reheat effects.
  Highlights the distinction between *simple* and *complex* configurations (industrial vs. aeroderivative turbines).

* **Aircraft propulsion systems**
  Introduces turbojet, turbofan, and turboprop engines; explains *thrust* and *specific fuel consumption* qualitatively.
  Shows how bypass ratio and exhaust velocity shape efficiency and noise.

* **Nozzles and diffusers**
  Reviews isentropic expansion/compression; defines *choked flow*, *Mach number effects*, and *gross thrust* concepts.
  Explains pressure mismatch and efficiency trends in propulsion contexts.

:::{admonition} Note: a summary of the gas cycles outline
:class: note, dropdown

**Central idea:** Gas cycles translate thermodynamic principles into continuous-flow processes where energy is converted mainly by compression and expansion.
The *Brayton framework* provides the conceptual link between stationary and mobile (propulsive) systems.
:::

(subsec_ICREs)=
## ICREs

This block examines **reciprocating systems** where combustion occurs *inside* the working chamber.
They are modeled as **air-standard cycles**, providing idealized references for practical engine operation.

* **General notion**
  Describes ICREs as *periodic open systems* analyzed through ideal closed cycles for simplicity.
  Highlights their ubiquity — from small-scale generators to automotive and heavy-duty engines.

* **Usual types and applications**
  Differentiates **spark-ignition (SI)** and **compression-ignition (CI)** systems, noting their ignition methods, fuel types, and efficiency characteristics.
  Discusses aspiration modes: naturally aspirated vs. turbocharged.

* **Otto cycle (SI archetype)**
  Describes its four processes: isentropic compression, constant-volume heat addition, isentropic expansion, and constant-volume heat rejection.
  Explains how *compression ratio* governs efficiency and performance limits (knock onset, material constraints).

* **Diesel cycle (CI archetype)**
  Similar to Otto but with *constant-pressure* heat addition.
  Explores *cutoff ratio* and its influence on efficiency.
  Compares Diesel and Otto cycles at equivalent compression ratios; clarifies why Diesels can operate at higher efficiencies.

* **Loss models (Qualitative)**
  Recognizes deviations from the ideal: heat transfer, finite combustion duration, friction, pumping losses, and incomplete expansion.
  Introduces simple correction factors or empirical performance coefficients used in practical assessments.

:::{admonition} Note: a summary of the ICREs outline
:class: note, dropdown

**Central idea:** ICRE analysis connects ideal cyclic reasoning with real engine behavior.
Through compression, combustion, and expansion, these systems illustrate how chemical energy is cyclically converted into mechanical work — under the same **$1^{\text{st}}$ law** and **$2^{\text{nd}}$ law** constraints.
:::

(subsec_steam_cycles)=
## Steam cycles

This block focuses on **vapor cycles**, where the working substance undergoes *phase change* as part of the energy-conversion process.
It establishes the link between heat addition, expansion, condensation, and regeneration in systems that power much of modern electricity generation.

* **General notion**
  Defines vapor cycles as systems with *external heat input* and *internal fluid recirculation*.
  Highlights water/steam as the benchmark working fluid due to its well-known thermodynamic properties and favorable phase behavior.

* **Usual types and applications**
  Covers **Rankine-type** cycles for electric power, **industrial cogeneration** systems, and **heat recovery** schemes.
  Notes where vapor cycles dominate (utility plants, process steam, combined cycles).

* **Rankine cycle (Ideal)**
  Describes its four principal stages: *pumping (liquid pressurization)*, *boiling (heat addition)*, *expansion (turbine)*, and *condensation (heat rejection)*.
  Relates efficiency to the mean temperature of heat addition and the condenser pressure.
  Introduces *T–s* and *h–s* diagrams as diagnostic tools.

* **Cycle enhancements**

  * *Reheat*: improves dryness at turbine exit and slightly increases efficiency.
  * *Regeneration*: raises feedwater temperature to reduce irreversibility.
  * *Superheat*: increases average temperature of heat addition.

* **Thermal power plants**
  Discusses typical layouts: boiler, turbine train, condenser, cooling system.
  Notes environmental constraints and cooling methods (wet, dry, hybrid).

* **Cogeneration (CHP)**
  Explains how extraction/condensing or back-pressure turbines supply both power and useful heat.
  Introduces trade-offs between electrical and thermal outputs.

* **Organic Rankine cycle (ORC)**
  Describes use of organic fluids for low-temperature heat sources.
  Introduces qualitative working-fluid classification (dry, isentropic, wet) and matching to heat-source levels.

* **Dual and combined cycles**
  Presents *topping–bottoming* concepts, where high-temperature gas cycles drive low-temperature steam or ORC subsystems.
  Emphasizes overall efficiency gains through energy cascading and waste-heat utilization.

:::{admonition} Note: a summary of the steam cycles outline
:class: note, dropdown

**Central idea:** Steam and vapor cycles illustrate thermodynamics in its most practical form — turning heat into mechanical power within real technological and environmental constraints.
Through condensation, regeneration, and combination with gas cycles, they demonstrate how every joule of energy is progressively degraded but still *governed* by the same universal laws.
:::

---

:::{admonition} Important: a summary of the course
:class: warning

**Overall progression.**

1. The **Fundamentals** block provides the language of systems, energy, and entropy.
2. **Gas cycles** extend this to continuous-flow devices and propulsion.
3. **ICREs** show how cyclic reasoning applies to reciprocating, internal combustion systems.
4. **Steam cycles** close the loop by introducing phase change and large-scale power conversion.

Across all blocks, the same analytical pillars stand:

* **Conservation of energy ($1^{\text{st}}$ law).**
* **Directionality and limitation ($2^{\text{nd}}$ law).**
* **Quality and degradation of energy (Exergy).**

Together they form a coherent view of **Applied Thermodynamics** — from first principles to interconnected energy systems.
:::
