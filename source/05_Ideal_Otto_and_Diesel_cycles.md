(sec_icre_ideal_cycles)=
## Ideal thermodynamic cycles of ICREs: Otto, Diesel, and dual cycles

Once the main geometric, volumetric, and combustion-related parameters have been defined, the next step is to describe the **ideal thermodynamic cycles** used to model internal combustion reciprocating engines (ICREs). In this ideal framework, the objective is to capture the dominant thermo-mechanical transformations **without** yet accounting for real losses, friction, finite-rate combustion, heat transfer to walls, pressure drops, incomplete combustion, or other irreversibilities.

The idealization is based on the **air-standard model** introduced previously: the working fluid is treated as air undergoing a sequence of internally reversible processes, while combustion and exhaust are represented by equivalent **heat addition** and **heat rejection** processes.

---

(subsec_icre_otto_diesel_processes)=
### Otto cycle and Diesel cycle: ideal processes

Both the **Otto** and the **Diesel** cycles are built from the same four core processes. What distinguishes them is the idealized representation of the **combustion (heat-addition) process**.

#### The ideal Otto cycle

The Otto cycle (typically associated with spark-ignition engines) consists of four ideal processes:

- **Process $1 \rightarrow 2$ (isentropic compression):**  
  The piston moves upward after intake, compressing the charge.
  In the ideal cycle, compression is **adiabatic and reversible**, so it is isentropic.

- **Process $2 \rightarrow 3$ (heat addition at constant volume):**  
  Combustion is idealized as a rapid heat addition at **constant volume**.  
  The assumption is that heat release is fast enough that, ideally, the piston does not move appreciably during the combustion event.
  Therefore, $v_2 = v_3$.

- **Process $3 \rightarrow 4$ (isentropic expansion):**  
  The high-pressure gas expands as the piston moves downward, delivering work.
  Expansion is idealized as **adiabatic and reversible**, hence isentropic.

- **Process $4 \rightarrow 1$ (heat rejection at constant volume):**  
  Heat is rejected at **constant volume** when the gas is at the maximum cylinder volume,
  returning the working fluid to the initial thermodynamic state.
  Therefore, $v_4 = v_1$.

:::{important}

**THE IDEAL OTTO CYCLE IS A CLOSED THERMO-MECHANICAL MODEL**

The Otto cycle does **not** explicitly model intake and exhaust as open-system gas exchange.
Instead, the cycle focuses on the closed-system portion in which the working fluid remains inside the cylinder and undergoes compression, heat addition, expansion, and heat rejection.

:::

#### Intake and exhaust in the ideal picture

In a real four-stroke engine, the piston also performs **intake** and **exhaust** strokes. In the simplest ideal representation, these can be modelled as two constant-pressure paths at the intake/exhaust pressure (often close to atmospheric for naturally aspirated engines, or equal to intake manifold pressure for boosted engines). These two processes cover the full volume range between TDC and BDC and are commonly drawn as two overlapping horizontal lines on the $p-v$ diagram at pressure $p_0$.

The corresponding works are:

- intake (work done by the surroundings on the piston–gas system):

  $$
  w_{\text{in},0\rightarrow 1} = p_0 (v_1 - v_0),
  $$
  
- exhaust (work done by the system on the surroundings):

  $$
  w_{\text{out},1\rightarrow 0} = p_0 (v_1 - v_0).
  $$

Since these areas overlap and have opposite signs, they cancel in the ideal picture, so the net work of the ideal cycle is governed by the closed part ($1\rightarrow2\rightarrow3\rightarrow4\rightarrow1$).

:::{note}

**OPEN VS CLOSED OPERATION**

Even though the ideal Otto and Diesel cycles are usually presented as closed cycles,
a real engine alternates between:
- **open-system** operation during intake and exhaust,
- **closed-system** operation during compression, combustion, and expansion.

This distinction becomes essential when modelling pumping losses and real gas exchange.

:::

---

(subsec_icre_diesel_processes)=
### The ideal Diesel cycle

The Diesel cycle (typically associated with compression-ignition engines) shares three of the Otto processes and differs only in the heat-addition step.

- **Process $1 \rightarrow 2$ (isentropic compression):** same as the Otto cycle.
- **Process $2 \rightarrow 3$ (heat addition at constant pressure):**  
  In compression-ignition engines, fuel injection and combustion extend over a longer crank-angle interval and continue into the early part of the expansion stroke.
  A classical idealization is to model this extended combustion as **constant-pressure heat addition**, so $p_2 = p_3$.
- **Process $3 \rightarrow 4$ (isentropic expansion):** same physical meaning as in Otto.
- **Process $4 \rightarrow 1$ (constant-volume heat rejection):** same closure step as in Otto.

Thus, the Diesel cycle preserves the compression and expansion modelling but replaces **isochoric** combustion with **isobaric** combustion.

---

(subsec_icre_otto_efficiency)=
### Thermal efficiency of the ideal Otto cycle

For both Otto and Diesel cycles, neglecting kinetic and potential energy changes, the first law for a closed system over a process can be written in specific form as:

$$
(q_{\text{in}} - q_{\text{out}}) + (w_{\text{in}} - w_{\text{out}}) = \Delta u .
$$

For the Otto cycle, heat is added and rejected at **constant volume**, so heat transfer equals the change in internal energy:

Heat addition ($2 \rightarrow 3$):

$$
q_{\text{in}} = u_3 - u_2 = c_v (T_3 - T_2).
$$

Heat rejection ($4 \rightarrow 1$):

$$
q_{\text{out}} = u_4 - u_1 = c_v (T_4 - T_1).
$$

Therefore, the thermal efficiency is:

$$
\eta_{\text{th,Otto}} = \frac{w_{\text{net}}}{q_{\text{in}}} = 1 - \frac{q_{\text{out}}}{q_{\text{in}}} = 1 - \frac{T_4 - T_1}{T_3 - T_2}.
$$

To express this efficiency in terms of the compression ratio, use the isentropic relations for processes $1 \rightarrow 2$ and $3 \rightarrow 4$, together with $v_2=v_3$ and $v_4=v_1$:

$$
\frac{T_2}{T_1} = \left(\frac{v_1}{v_2}\right)^{\gamma-1} \quad \text{and} \quad \frac{T_3}{T_4} = \left(\frac{v_4}{v_3}\right)^{\gamma-1} = \left(\frac{v_1}{v_2}\right)^{\gamma-1}.
$$

Defining the compression ratio $r = v_1/v_2$, it follows that the Otto-cycle efficiency becomes:

$$
\eta_{\text{th,Otto}} = 1 - \frac{1}{r^{\gamma-1}} .
$$

This compact result shows that ideal Otto efficiency increases with:
- increasing compression ratio $r$,
- increasing ratio of specific heats $\gamma$.

:::{important}

**OTTO EFFICIENCY GROWS FAST AT LOW $r$ AND SLOWS DOWN AT HIGH $r$**

The function $1 - 1/r^{\gamma-1}$ rises steeply for small-to-moderate $r$,
but flattens as $r$ becomes large.
Therefore, pushing $r$ ever higher yields diminishing returns in ideal efficiency.

:::

#### Practical limitation in spark-ignition engines: knock

In spark-ignition engines, increasing $r$ raises the end-of-compression temperature. If the mixture reaches conditions that promote **auto-ignition** before the flame front propagates smoothly from the spark, parts of the mixture can ignite prematurely, producing rapid pressure rise and pressure waves. This is the phenomenon of **knock** (often perceived as a metallic pinging). Knock increases mechanical and thermal loading and is undesirable for durability.

As a result, spark-ignition engines typically operate with compression ratios in the range:

$$
8 \lesssim r \lesssim 11 .
$$

Historically, increasing octane rating through anti-knock additives allowed higher $r$. For example, tetraethyl lead $(\text{CH}_3\text{CH}_2)_4\text{Pb}$ was used widely in the early-to-mid 20th century to increase knock resistance, but was later phased out due to toxicity and environmental impact. Modern high-octane fuels and improved combustion control have allowed renewed increases in $r$ in some applications.

:::{note}

**THE ROLE OF $\gamma$**

For a fixed compression ratio, the Otto cycle efficiency increases as $\gamma$ increases.
Monatomic gases (e.g., argon or helium, with $\gamma \approx 1.667$) yield higher ideal efficiencies than diatomic air ($\gamma \approx 1.4$), and larger polyatomic gases yield lower values.

In real engines, the working fluid is not a fixed ideal gas: composition and temperature vary, and $\gamma$ is not constant. Nevertheless, the ideal trend remains a valuable design insight.

:::

Real spark-ignition engines typically achieve thermal efficiencies on the order of $25\%$ to $30\%$, with the actual value depending on many additional factors (heat losses, mixture strength, volumetric efficiency, friction, and combustion phasing).

---

(subsec_icre_otto_diagrams)=
### $p-v$ and $T-s$ diagrams of the ideal Otto cycle

The ideal Otto cycle can be interpreted visually through the standard thermodynamic diagrams:

- In the **$p-v$ diagram**:
  - $1 \rightarrow 2$ and $3 \rightarrow 4$ are isentropic curves,
  - $2 \rightarrow 3$ and $4 \rightarrow 1$ are vertical lines (constant volume).
  The net work output is the **area enclosed** by the cycle.

- In the **$T-s$ diagram**:
  - the isentropic processes appear as vertical lines (constant entropy),
  - heat addition and rejection at constant volume appear as curved paths.
  The net heat input equals the net work output over the cycle (first law), and the difference between heat added and rejected is interpretable through the areas under the respective paths.

A key point is that even though Otto and Diesel differ noticeably in the $p-v$ diagram during heat addition, their $T-s$ diagrams remain qualitatively similar: two isentropic vertical lines connected by two heat-transfer curves, with the heat-addition curve having different slope depending on whether the process is isochoric (Otto) or isobaric (Diesel).

---

(subsec_icre_diesel_efficiency)=
### Thermal efficiency of the ideal Diesel cycle

For the Diesel cycle, the heat-addition process occurs at **constant pressure**, and therefore boundary work occurs during combustion. Applying the first law to process $2 \rightarrow 3$:

$$
q_{\text{in}} - w_{b,\text{out}} = u_3 - u_2 .
$$

For an ideal-gas constant-pressure process, this leads to:

$$
q_{\text{in}} = (u_3 - u_2) + p_2(v_3 - v_2) = h_3 - h_2 = c_p (T_3 - T_2).
$$

Heat rejection ($4 \rightarrow 1$) is still modelled as constant-volume:

$$
q_{\text{out}} = u_4 - u_1 = c_v (T_4 - T_1).
$$

Thus, Diesel thermal efficiency is:

$$
\eta_{\text{th,Diesel}} = 1 - \frac{q_{\text{out}}}{q_{\text{in}}} = 1 - \frac{c_v (T_4 - T_1)}{c_p (T_3 - T_2)} = 1 - \frac{T_4 - T_1}{\gamma (T_3 - T_2)} .
$$

To express the result in terms of compression ratio and a new Diesel-specific parameter, define the **cutoff ratio**:

$$
r_c = \frac{v_3}{v_2}.
$$

Using isentropic relations and the structure of the Diesel cycle, one obtains the standard form:

$$
\eta_{\text{th,Diesel}} = 1 - \frac{1}{r^{\gamma-1}} \left[\frac{r_c^\gamma - 1}{\gamma (r_c - 1)}\right].
$$

The bracketed term is always greater than 1 for $r_c>1$, so for the same compression ratio:

$$
\eta_{\text{th,Otto}} > \eta_{\text{th,Diesel}} .
$$

:::{important}

**THE COST OF CONSTANT-PRESSURE COMBUSTION**

At fixed compression ratio, the Diesel cycle has lower ideal efficiency than the Otto cycle because heat is added while the gas expands, which increases $q_{\text{in}}$ relative to the work gained for the same initial compression.

However, Diesel engines typically operate at much higher compression ratios in practice, which can more than compensate for this ideal-cycle disadvantage.

:::

---

(subsec_icre_diesel_considerations)=
### Interpretation and practical trends for Diesel engines

From the Diesel efficiency expression, several key qualitative results follow:

- **Smaller cutoff ratio increases efficiency:**  
  As $r_c \rightarrow 1$, the heat-addition process approaches constant volume and the bracketed factor approaches 1.  
  This can be shown by the first-order approximation:
  
  $$
  r_c^\gamma - 1 \approx \gamma (r_c - 1),
  $$

  
  so Otto and Diesel efficiencies coincide in the limit $r_c \to 1$.

- **Diesel engines tolerate higher $r$ (and need it):**  
  Compression-ignition requires sufficiently high end-of-compression temperature to trigger auto-ignition of the injected fuel. Therefore Diesel engines operate with much larger compression ratios, commonly:

  $$
  12 \lesssim r \lesssim 23,
  $$

  
  which strongly increases efficiency through the $1 - 1/r^{\gamma-1}$ factor.

- **Typical Diesel efficiencies are higher in practice:**  
  Diesel engines also tend to operate with higher air–fuel ratios (lean operation) and often at lower rpm for a given application, which promotes more complete combustion and improves overall efficiency. Thermal efficiencies around $35\%$ to $40\%$ are typical for many applications.

Because of these characteristics, Diesel engines have been historically attractive for high-power, high-duty applications such as trucks, locomotives, ships, and auxiliary power units. The final price of fuels in real markets depends on many factors beyond production cost (refined product pricing, seasonal demand, logistics, and taxation), but the thermodynamic and operating advantages of Diesel engines remain central for heavy-duty use.

:::{note}

**ENGINE CHOICE IS NOT ONLY THERMODYNAMICS**

Even when Diesel engines provide higher efficiency, practical selection depends on:
- emissions regulations and aftertreatment requirements,
- noise/vibration constraints,
- fuel availability and price dynamics,
- maintenance, operating profile, and total cost of ownership.

These considerations motivate moving from ideal cycles to real-cycle losses.

:::

---

(subsec_icre_otto_diesel_comparisons)=
### Comparing Otto and Diesel cycles

Several comparison levels are useful in cycle analysis:

- **Same compression ratio ($r$):**  
  Otto yields higher ideal efficiency than Diesel because the Diesel heat-addition model includes the cutoff effect.

- **Variable compression ratio:**  
  As $r$ increases, both net work and efficiency increase, but:
  - SI engines face knock limits,
  - CI engines face mechanical and thermal design limits (peak pressures, component stresses).

- **Effect of mixture strength (excess-air factor):**  
  Richer mixtures (lower $\lambda$) can increase released chemical energy but may lead to incomplete combustion and higher emissions.  
  Lean mixtures (higher $\lambda$) tend to increase cycle efficiency partly through the effective thermophysical properties of the mixture and reduced dissociation and heat losses in some regimes.

In more advanced analyses, the dependence of the effective $\gamma$ on mixture composition can be introduced through mixture-averaged specific heats, making $\gamma$ an increasing function of the air–fuel ratio in many practical ranges.

---

(subsec_icre_dual_cycle)=
### The dual (mixed) cycle

Modern compression-ignition engines with fast injection and rapid pressure rise often exhibit combustion behaviour that is not well captured by a purely constant-pressure model.

In many engines:

- a fraction of heat release occurs very rapidly near the end of compression (approximately constant volume),
- followed by continued heat release into early expansion (approximately constant pressure).

This motivates the **dual (mixed) cycle**, which models heat addition as a combination of:

- **constant-volume heat addition** ($2 \rightarrow x$), followed by
- **constant-pressure heat addition** ($x \rightarrow 3$).

Two parameters are defined:

- a **pressure ratio** across the constant-volume portion:
  
  $$
  r_p = \frac{p_x}{p_2},
  $$
  
- a **cutoff ratio** across the constant-pressure portion:

  $$
  r_c = \frac{v_3}{v_x}.
  $$

The dual-cycle efficiency depends on $r$, $r_p$, $r_c$, and $\gamma$, and its expression is more involved than the Otto and Diesel results. Nevertheless, the dual cycle is often a more realistic idealization for modern CI engines than the pure Diesel cycle, while still preserving analytical tractability.

:::{tip}

**LIMITING CASES**

The dual cycle contains Otto and Diesel as special cases:

- If the constant-pressure part vanishes ($r_c \rightarrow 1$), the dual cycle approaches an Otto-like heat-addition model.
- If the constant-volume part vanishes ($r_p \rightarrow 1$), the dual cycle approaches the Diesel cycle.

This makes the dual cycle a convenient bridge between the two classical idealizations.

:::

---

(subsec_icre_ideal_cycles_closure)=
### Conceptual closure

- The ideal Otto cycle models combustion as constant-volume heat addition; the Diesel cycle models it as constant-pressure heat addition.
- Both cycles use isentropic compression and expansion and close with constant-volume heat rejection.
- Otto ideal efficiency depends only on $r$ and $\gamma$: $\eta_{\text{th,Otto}} = 1 - 1/r^{\gamma-1}$.
- Diesel ideal efficiency introduces the cutoff ratio $r_c$: $\eta_{\text{th,Diesel}} = 1 - \frac{1}{r^{\gamma-1}}\left[\frac{r_c^\gamma-1}{\gamma(r_c-1)}\right]$.
- At equal $r$, Otto is more efficient than Diesel, but Diesel engines operate at higher $r$ in practice and often reach higher real efficiencies.
- The dual cycle captures mixed constant-volume/constant-pressure heat addition and provides a more flexible ideal model for modern CI engines.
