(sec_icre_losses)=
## Losses

Ideal Otto, Diesel, and dual cycles are valuable because they isolate the main thermodynamic mechanisms and yield compact efficiency trends. Real engines, however, deviate from those idealizations in systematic ways. Understanding **where** and **why** the deviations occur is essential for two reasons:

1. It provides a physically meaningful explanation for the gap between ideal-cycle predictions and measured performance.
2. It guides engineering strategies to mitigate losses through design (geometry, materials, gas exchange) and control (spark timing, injection, valve timing).

In this section, losses are organized into two broad families:

- **Thermodynamic-cycle losses**, associated with how the in-cylinder processes differ from the ideal cycle.
- **Mechanical and auxiliary losses**, associated with friction and the power absorbed by supporting subsystems.

---

(subsec_icre_losses_overview)=
### Classification of losses

#### Losses associated with the thermodynamic cycle

- **Heat-transfer losses** (to cylinder walls, head, piston, coolant, and oil)
- **Finite-time (combustion-duration) losses** (“time losses”)
- **Pumping losses** (gas exchange work during intake and exhaust)

#### Losses associated with mechanical and auxiliary subsystems

- **Mechanical friction** (piston rings, bearings, valve train, etc.)
- **Auxiliary loads** (water/oil pumps, alternator, air conditioning, etc.)
- **Boosting devices** (supercharger or turbocharger, when present, and their associated back-pressure / drive power)

:::{important}

**WHY THIS SPLIT MATTERS**

Thermodynamic-cycle losses reshape the **indicated** cycle (the in-cylinder $p-v$ loop),
whereas mechanical and auxiliary losses reduce the **brake** output at the shaft.
Keeping these concepts separate prevents mixing “cycle efficiency” effects with “drivetrain/engine hardware” effects.

:::

In what follows, the emphasis is placed on the three main thermodynamic-cycle losses, because they are the ones that directly deform the Otto/Diesel ideal cycles into measured engine indicator diagrams.

---

(subsec_icre_heat_losses)=
### Heat-transfer losses

Heat-transfer losses are a defining feature of real reciprocating engines. In the ideal cycles, compression and expansion are treated as adiabatic (or at least internally reversible with no heat exchange). In real engines, the working gases reach very high temperatures and are confined by metal boundaries, so significant heat flows from the gas to:

- the **cylinder head** (and valve region),
- the **piston crown**,
- the **cylinder liner**,
- the **coolant** and **lubricating oil** circuits.

These losses reduce the net work because the thermodynamic state during expansion is altered: a lower in-cylinder temperature implies a lower pressure, and thus a smaller expansion work for a given volume change.

#### Where and when heat losses concentrate

Heat losses are not uniform across the cycle:

- During **compression**, gas temperatures are relatively lower and the duration is short; heat transfer is present but often less dominant than during expansion.
- During **combustion and early expansion**, gas temperatures peak and the temperature difference between gas and metal boundaries is largest, so heat transfer becomes very intense.
- During **exhaust**, the products leave at high temperature, representing another strong channel of energy leaving the engine system.

In a typical comparison between an ideal cycle and a measured indicator cycle, heat-transfer losses appear primarily as a reduction of the pressure level along the expansion path, shrinking the enclosed $p-v$ area (and hence indicated work).

:::{note}

**HEAT TRANSFER IS NOT “WASTED” IN AN ABSOLUTE SENSE**

A significant portion of the heat transferred to the **coolant** is deliberately removed to keep the engine near its design operating temperature (“temperature of regime”). This is not optional: without it, thermal expansion, thermal stresses, lubricant breakdown, and component damage would rapidly degrade performance and may lead to seizure.

:::

---

(subsec_icre_heat_loss_modeling)=
### Modeling the fuel energy balance in the presence of heat losses

In real operation, the chemical energy released by the fuel must supply:

1. the useful effective output,
2. the energy rejected to coolant and oil,
3. the energy carried away by the exhaust,
4. additional irreversibilities (including incomplete combustion, radiation, etc.).

A practical decomposition of the **equivalent heat input** associated with the supplied fuel can therefore be written conceptually as:

- **Useful term:** the portion of released energy that becomes effective power output.
- **Coolant heat transfer:** heat removed by the cooling circuit (necessary for thermal regulation).
- **Exhaust enthalpy:** energy leaving with the exhaust gases (not fully convertible into piston work).
- **Incomplete combustion:** unburned fuel or partially oxidized products (when present).
- **Oil heat transfer:** heat absorbed by lubricant (distinct from coolant heat removal).
- **Radiation:** heat transfer by radiation, which grows rapidly with temperature (approximately with $T^4$).

:::{important}

**THE EXHAUST IS A THERMODYNAMIC “EXIT”**

Even if an engine were perfectly insulated from its walls, the exhaust would still carry away substantial energy. This is a fundamental limitation: the cycle must reject energy to return to the initial state, and real exhaust processes typically reject energy at higher temperatures than the ideal constant-volume heat-rejection model suggests.

:::

---

(subsec_icre_heat_loss_magnitudes)=
### Representative magnitudes and qualitative implications

Representative component temperatures help explain why some parts dominate heat loss pathways:

- The **exhaust valve** can reach temperatures on the order of **$700^\circ\text{C}$**, and is exposed to the hottest gases during blowdown and early exhaust.
- The **piston crown** can reach high temperatures (hundreds of degrees Celsius), with large gradients across the material.

Because hot combustion products tend to occupy the upper region of the combustion chamber (lower density, buoyancy-driven stratification, and flow patterns), the **cylinder head** often accounts for the largest fraction of heat losses. Typical qualitative breakdowns used in engine heat-loss discussions are:

- cylinder head: **about 50–60%** of wall heat losses,
- cylinder walls: **about 8–22%**,
- exhaust gas energy leaving the cylinder: **about 16–26%** of the released heat (as a separate energy channel).

Losses are also strongly concentrated in time:

- a large share occurs during **expansion** (often quoted as **30–50%** of the wall-transfer losses, depending on engine and regime),
- and during **exhaust**, where hot gases leave without allowing full thermal-to-work conversion.

These values are not universal constants; they vary with engine size, load, speed, cooling strategy, and combustion phasing. Their purpose is to anchor the physical intuition: **head and exhaust-side regions are thermally critical**.

---

(subsec_icre_time_losses)=
### Finite-time (combustion-duration) losses

In the ideal Otto cycle, heat addition is modeled as **instantaneous constant-volume** heat input. Real combustion is never instantaneous. It takes a finite crank-angle interval for the flame to propagate (SI) or for mixing-controlled burning to occur (CI). During that interval, the piston is moving, so the heat-addition process is neither purely isochoric (Otto) nor purely isobaric (Diesel); it is a mixed, finite-time transformation.

In an idealized $p-v$ overlay, finite-time losses appear as a rounding and spreading of the sharp ideal heat-addition line around TDC. The result is typically a reduction in the effective pressure rise at the most favorable crank angles for work extraction.

#### Why losses increase with engine speed

As rotational speed increases:

- the **time** spent near TDC decreases,
- the same combustion duration (in milliseconds) corresponds to a **larger crank-angle span**,
- therefore a larger fraction of heat release occurs when the piston is already moving away from TDC.

This reduces the portion of heat release that contributes to high mean effective pressure during early expansion, lowering efficiency and indicated work.

:::{important}

**COMBUSTION PHASING IS A WORK-EXTRACTION PROBLEM**

The goal is not simply “fast combustion” in isolation. The goal is to release most of the heat when the volume is still small (near TDC) so that the pressure rise translates into high expansion work, without inducing abnormal combustion (knock in SI, excessive pressure rise and noise in CI).

:::

---

(subsec_icre_spark_advance)=
### Mitigating time losses: spark/injection timing and combustion phasing

A classical way to compensate finite-time combustion is to start combustion **before** TDC so that the peak pressure and the main heat release occur near the desired crank angle.

For spark-ignition engines this is done through **spark advance**; for compression-ignition engines, analogous control is achieved by injection timing and rate shaping.

However, excessive advance can create severe problems:

- non-optimal flame development,
- excessive peak pressures,
- increased heat transfer to walls (hotter earlier),
- increased tendency to knock or abnormal combustion.

Hence, timing must be tuned as a function of operating conditions, especially **engine speed**.

---

(subsec_icre_wiebe_model)=
### Modeling combustion duration: the Wiebe function

A widely used empirical model for the cumulative burned fraction (or equivalently, released heat fraction) is the **Wiebe function**:

$$
x_b(\theta)
= 1 - \exp \left[-a \left(\frac{\theta - \theta_s}{\theta_d}\right)^{n}\right],
$$

where:

- $x_b$ is the **fraction of fuel mass burned** (or fraction of total heat released),
- $\theta$ is the **crank angle**,
- $\theta_s$ is the crank angle at **start of combustion**,
- $\theta_d$ is the **combustion duration** expressed as crank-angle span,
- $a$ and $n$ are **shape/efficiency parameters** fitted to experimental data for each engine and operating regime.

The model reflects a key experimental observation: burning typically starts slowly, accelerates to a peak rate, and then tapers as the remaining unburned mixture decreases.

:::{note}

**INTERPRETING WIEBE PARAMETERS**

- Increasing $\theta_d$ spreads combustion over more crank angle, generally increasing time losses.
- Shifting $\theta_s$ (advance/retard) moves the combustion window relative to TDC.
- Parameters $a$ and $n$ tune how “peaky” or “smooth” the burn rate is.

The model is simple enough for cycle simulations yet flexible enough to match measured burn profiles.

:::

---

(subsec_icre_wiebe_low_speed)=
### Wiebe-based intuition at low engine speed

At low rotational speed, the piston remains near TDC for a longer time, so combustion can be reasonably concentrated near the most favorable volume range. A typical illustrative value is a combustion duration around:

- $\theta_d \approx 30^\circ$ (order-of-magnitude example for low speed).

If $\theta_s$ is **too late** (little or no advance), much of the heat release occurs after TDC at larger volumes, reducing peak pressure and work extraction.

If $\theta_s$ is **too early**, combustion may peak before TDC, increasing negative work during the last part of compression and raising knock tendency.

An intermediate advance tends to maximize both indicated work and efficiency by aligning the steepest part of the burn curve with the crank-angle region where pressure rise is most beneficial.

---

(subsec_icre_wiebe_high_speed)=
### Wiebe-based intuition at high engine speed

At high rotational speed, the same physical combustion time corresponds to a larger crank-angle span; combustion can extend to:

- $\theta_d \approx 60^\circ$ (illustrative value at high speed).

In that regime, an advance that was optimal at low speed is typically insufficient: combustion would effectively occur “too late” in crank-angle terms. Therefore, a larger advance (more negative $\theta_s$ relative to TDC) is required to maintain the desired phasing.

This dependence is the reason ignition/injection timing maps in engine control units must vary with rpm and load.

:::{important}

**ADVANCE IS SPEED-DEPENDENT**

Optimal ignition/injection advance is not a fixed number.
It is a function of:
- speed (rpm),
- load,
- mixture composition,
- residual-gas fraction,
- boosting and intake conditions,
- knock/pressure-rise constraints.

:::

---

(subsec_icre_pumping_losses)=
### Pumping losses

Pumping losses arise from the fact that intake and exhaust are not frictionless, quasi-static processes. Real gas exchange requires overcoming:

- flow restrictions at **valves**,
- pressure drops across **filters** and **intake plumbing**,
- losses in **manifolds**, bends, and throttles,
- losses across aftertreatment devices (catalyst, particulate filter),
- mufflers and exhaust plumbing backpressure.

On a real $p-v$ diagram, intake and exhaust strokes no longer appear as overlapping horizontal lines at a single pressure. Instead, they form a **closed pumping loop** (often an oval-like loop). The area of that loop represents net work that must be supplied to move gases in and out of the cylinder, reducing the net indicated work available from the main cycle.

Pumping losses also reduce the fresh charge admitted, contributing to incomplete cylinder filling, often captured via a **volumetric efficiency**.

:::{tip}

**ENGINE BRAKING**

The same mechanism that creates pumping work losses during part-load operation can be exploited for deceleration: closing the throttle (SI engines) increases pumping work, producing a retarding torque commonly known as engine braking.

:::

---

(subsec_icre_pumping_SI)=
### Pumping losses in spark-ignition engines: quantitative (throttle-based) control

In traditional spark-ignition operation, combustion requires a mixture within flammability limits, often near stoichiometric conditions. A typical range for the excess-air factor is:

- $\lambda \approx 1.0$ to $1.1$ in many passenger-car conditions (illustrative).

In **quantitative control**, power is controlled by changing the **mass of mixture** admitted while keeping mixture composition roughly similar. This is achieved by restricting intake air with a **throttle**, which lowers intake manifold pressure.

That restriction produces large pumping losses, especially when:

- fuel consumption is significant,
- demanded power is low (city driving, light load).

As a result, throttled SI engines can exhibit disproportionately high fuel consumption at low load.

#### Engineering strategies to reduce SI pumping losses

Several technological developments aim to reduce these throttle-induced pumping losses:

- **Variable valve timing / variable valve lift (variable distribution):**  
  Adjusting opening/closing times of intake and exhaust valves changes effective breathing and can reduce the need for strong throttling.  
  The classical timing concepts include:
  - **AAA** (advanced intake opening),
  - **RCA** (retarded intake closing),
  - **AAE** (advanced exhaust opening),
  - **RCE** (retarded exhaust closing).
  
  These overlaps create a **valve overlap** interval (both valves open), whose optimal value depends strongly on rpm and load. Larger overlap can assist scavenging and reduce pumping work in some regimes, but may be detrimental in others (reversion, residuals).

- **Direct injection (SI):**  
  Injecting fuel directly into the cylinder enables more flexible mixture formation and can reduce pumping penalties by allowing different load-control strategies and improved combustion stability.

- **Stratified charge operation:**  
  Concentrating richer mixture near the spark plug while keeping the bulk mixture lean can sustain stable ignition with less throttling and lower pumping work in certain operating windows, while also affecting combustion duration and efficiency.

:::{note}

**WHY THROTTLING HURTS**

A throttle reduces intake pressure, so the piston must do extra work during the intake stroke to draw air into a low-pressure manifold, and must also push exhaust out against a pressure that may be higher than the intake pressure. That pressure mismatch creates the pumping loop area.

:::

---

(subsec_icre_pumping_SI_regimes)=
### Pumping loss trends across SI load regimes (qualitative)

When comparing typical operating regimes:

- **Idle:**  
  Throttle nearly closed → high intake restriction → poor filling.  
  The engine supplies just enough work to overcome pumping and friction.  
  Pumping losses can become a large fraction of the indicated work (values up to ~45% are often cited as an order-of-magnitude illustration in throttled idle conditions).

- **Medium load:**  
  Throttle partially open → lower restriction → improved filling.  
  Pumping loss fraction decreases significantly (single-digit percentages may be typical), but higher rpm can increase time losses.

- **Full load:**  
  Throttle wide open → minimal intake restriction → best filling.  
  Pumping losses can drop to a few percent, while other constraints (knock, thermal limits) dominate.

These trends explain why traditional throttled SI engines are relatively inefficient in low-load urban operation and why modern SI technologies target pumping-loss reduction.

---

(subsec_icre_pumping_CI)=
### Pumping losses in compression-ignition engines: qualitative (fuel-based) control

Diesel engines do not rely on a spark and therefore are not constrained to maintain a near-stoichiometric mixture for ignition. They can operate over a broader range of excess-air factors. In practice, values above 1 are typical and can become very large at light load.

In **qualitative control**, the engine admits approximately the same amount of air (no throttle in the classical configuration), and power is regulated by injecting more or less fuel:

- low power demand → small fuel quantity → very lean mixture (high $\lambda$),
- high power demand → larger fuel quantity → less lean (lower $\lambda$, still often >1).

Because intake air is not throttled, Diesel pumping losses associated with intake restriction are typically smaller than in throttled SI engines.

A further benefit is that at low load, high $\lambda$ tends to reduce the effective cutoff behaviour and can improve thermal efficiency trends, consistent with the qualitative discussion of Diesel-cycle efficiency.

:::{important}

**WHY DIESEL PART-LOAD IS THERMODYNAMICALLY FRIENDLY**

At low load, a Diesel engine can keep airflow high and reduce fuel, producing a very lean mixture.
This avoids throttling and often yields better part-load efficiency than traditional SI engines.

:::

---

(subsec_icre_pumping_CI_disadvantages)=
### Limitations and sources of pumping losses in Diesel engines

Despite the advantage of avoiding throttle restriction, Diesel engines are not free of pumping losses. Pressure drops can be significant due to:

- intake filters and ducting losses,
- flow turning and manifold friction,
- exhaust-side restrictions (valve flow areas, manifolds),
- aftertreatment devices (oxidation catalysts, particulate filters),
- mufflers and exhaust routing.

Some of these elements exist in SI engines as well, but Diesel aftertreatment and high-flow requirements can make certain contributions larger in specific configurations. Moreover, pumping losses still grow with rpm and mass flow.

---

(subsec_icre_losses_closure)=
### Conceptual closure

- Real ICRE cycles deviate from ideal Otto/Diesel/dual cycles primarily through **heat transfer**, **finite combustion duration**, and **pumping work**.
- Heat-transfer losses shrink the expansion pressure level and must be managed through cooling and materials; they are strongest near peak temperatures and often dominate through the cylinder head.
- Finite-time combustion makes heat addition non-isochoric/non-isobaric; optimal combustion phasing depends strongly on rpm and is often modeled with the **Wiebe function**.
- Pumping losses originate in real gas exchange pressure drops and appear as a pumping loop on the $p-v$ diagram.
- Traditional SI throttle-based (quantitative) control increases pumping losses at low load; Diesel fuel-based (qualitative) control reduces them but does not eliminate them due to intake/exhaust restrictions.
- Mechanical friction and auxiliary loads further reduce shaft output and must be treated separately from indicated cycle deformations.
