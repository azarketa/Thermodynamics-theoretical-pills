(sec_nozzles_intro)=
## Nozzles and diffusers in gas-turbine propulsion

The purpose of a **nozzle** is to transform the enthalpy of a flowing gas into kinetic energy by means of a properly shaped duct. In aircraft engines, nozzles accelerate the exhaust flow and generate the high exit velocities required to produce thrust.

The functional counterpart of a nozzle is the **diffuser**, which performs the inverse conversion: it decelerates a flow in order to increase its static pressure and adapt it to subsequent components (compressor, combustor, turbine) or, in the case of ramjet-type engines, to the combustion process itself.

Although the basic principle is simple, nozzle and diffuser behaviour depends strongly on the flow regime. In particular, **subsonic** and **supersonic** flows require fundamentally different area variations to achieve acceleration or deceleration.

---

(subsec_area_velocity_relation)=
### Area–velocity relation for steady, adiabatic flow

Consider a one-dimensional nozzle operating at steady state. Mass conservation implies:

(eq_nozzle_continuity)=
$$
\dot{m} = \rho A c = \text{const.}
$$

Taking the differential and rearranging:

(eq_nozzle_continuity_diff)=
$$
\frac{d\rho}{\rho} + \frac{dA}{A} + \frac{dc}{c} = 0.
$$

Assuming adiabatic flow and modelling air as an ideal gas undergoing an internally reversible process, the isentropic relation gives:

(eq_isentropic_dp_drho)=
$$
\frac{dp}{p} = \gamma \frac{d\rho}{\rho}.
$$

For an ideal gas, $p = \rho R T$, so:

(eq_ideal_gas_diff)=
$$
\frac{dp}{p} = \frac{d\rho}{\rho} + \frac{dT}{T}.
$$

Combining the two expressions above yields:

(eq_dT_drho)=
$$
\frac{dT}{T} = (\gamma - 1)\frac{d\rho}{\rho}.
$$

From the steady-flow energy equation for an adiabatic nozzle (neglecting potential energy):

(eq_energy_nozzle_diff)=
$$
cdc + dh = 0,
$$

and, for a perfect gas, $dh = c_p\,dT$, thus:

(eq_dT_dc)=
$$
c_p{}dT = -c{}dc \quad \Rightarrow \quad \frac{dT}{T} = -\frac{c{}dc}{c_p{}T}.
$$

Using $c_p = \dfrac{\gamma R}{\gamma - 1}$ and $c_s^2 = \gamma R T$, it follows that:

(eq_drho_dc)=
$$
\frac{d\rho}{\rho} = -\frac{c{}dc}{c_s^2}.
$$

Substituting this result into the continuity differential leads to the fundamental area–velocity relation

(eq_area_velocity_mach)=
$$
\frac{dA}{A} = -\frac{dc}{c}{}(1 - Ma^2),
$$

where the Mach number is $Ma = \dfrac{c}{c_s}$ and the speed of sound is $c_s = \sqrt{\gamma R T}$.

:::{important}

**GEOMETRY DEPENDS ON THE FLOW REGIME**

The sign of $(1-Ma^2)$ determines whether the area must increase or decrease to
accelerate or decelerate a flow.

{ref}`From the evolution of the area with the velocity of the flow <eq_area_velocity_mach>`, four operating cases follow:

- **Subsonic nozzle** ($Ma<1$, $dc>0$): $dA<0$ (converging duct accelerates the flow).
- **Supersonic nozzle** ($Ma>1$, $dc>0$): $dA>0$ (diverging duct accelerates the flow).
- **Supersonic diffuser** ($Ma>1$, $dc<0$): $dA<0$ (converging duct decelerates the flow).
- **Subsonic diffuser** ($Ma<1$, $dc<0$): $dA>0$ (diverging duct decelerates the flow).

:::

---

(subsec_back_pressure_effect)=
### Effect of discharge pressure and choking

In compressible flow, nozzle behaviour is strongly influenced by the discharge (back) pressure. As the discharge pressure decreases relative to the inlet pressure, the mass flow rate increases, but only up to a limit.

When the discharge pressure reaches a **critical value**, the flow becomes **choked** at the minimum-area section (the throat). At choking:

- the Mach number at the throat becomes $Ma=1$,
- the mass flow rate reaches a maximum value,
- further reductions in discharge pressure do not increase $\dot{m}$.

This saturation effect is particularly relevant in convergent–divergent (Laval) nozzles.

:::{note}

**WHY CHOKING MATTERS**

Once the throat is choked, the upstream flow is effectively decoupled from further changes in downstream pressure. Subsequent adjustments occur mainly in the divergent part and/or outside the nozzle through compressible-wave structures.

:::

---

(subsec_laval_nozzle_regimes)=
### Laval nozzle operating regimes

Consider a convergent–divergent nozzle designed to operate with supersonic expansion. As the discharge pressure is reduced progressively:

- Initially, the flow remains entirely **subsonic** and the divergent section acts as a diffuser.
- At the critical back pressure, the throat becomes choked ($Ma=1$).
- For lower discharge pressures, the flow becomes **supersonic** in part of the divergent section, but a **normal shock** may appear inside the nozzle. Downstream of the shock the flow becomes subsonic again, and the remainder of the divergent duct behaves as a diffuser.
- As the discharge pressure decreases further, the shock moves downstream and may eventually reach the nozzle exit.

Once the internal flow reaches its fully expanded isentropic pattern, further reductions of discharge pressure are compensated outside the nozzle. This leads to three classic regimes:

- **Overexpanded nozzle:** $p_e < p_{\text{amb}}$; oblique shocks form outside the nozzle to compress the jet. Typical at low altitude (high ambient pressure).
- **Ideally expanded nozzle:** $p_e = p_{\text{amb}}$; no external shock structure is needed.
- **Underexpanded nozzle:** $p_e > p_{\text{amb}}$; expansion continues outside the nozzle through expansion fans and shock cells. Typical at high altitude (low ambient pressure).

---

(subsec_isentropic_stagnation_relations)=
### Isentropic stagnation relations and throat conditions

For an adiabatic, isentropic nozzle with a perfect gas, the steady-flow energy equation yields:

(eq_stagnation_energy)=
$$
c_p T_0 = \frac{c^2}{2} + c_p T.
$$

Rearranging and using $c_s^2=\gamma R{}T$ leads to the standard stagnation-to-static temperature relation:

(eq_T0_T)=
$$
\frac{T_0}{T} = 1 + \frac{\gamma - 1}{2}Ma^2.
$$

The corresponding pressure and density ratios for isentropic flow are:

(eq_p0_p)=
$$
\frac{p_0}{p} = \left(1+\frac{\gamma - 1}{2}Ma^2\right)^{\gamma/(\gamma - 1)},
$$

(eq_rho0_rho)=
$$
\frac{\rho_0}{\rho} = \left(1+\frac{\gamma - 1}{2}Ma^2\right)^{1/(\gamma - 1)}.
$$

At the throat of a Laval nozzle, where $Ma=1$, the critical ratios become:

(eq_critical_T_ratio)=
$$
\frac{T_*}{T_0} = \frac{2}{\gamma+1},
$$

(eq_critical_P_ratio)=
$$
\frac{p_*}{p_0} = \left(\frac{2}{\gamma+1}\right)^{\gamma/(\gamma-1)},
$$

(eq_critical_rho_ratio)=
$$
\frac{\rho_*}{\rho_0} = \left(\frac{2}{\gamma+1}\right)^{1/(\gamma-1)}.
$$

The critical velocity at the throat is $c_* = c_{s,*}$ and may be written as

(eq_throat_velocity)=
$$
c_* = \sqrt{\gamma{}R{}T_*} = \sqrt{\frac{2\gamma}{\gamma+1}}{}\sqrt{R T_0}.
$$

When the inlet velocity is small compared with the exit velocity, the exit speed may be approximated from the enthalpy drop as

(eq_exit_velocity_approx)=
$$
c_2 \approx \sqrt{2{}(h_1 - h_2)}.
$$

:::{note}

**AREA-MACH NUMBER RELATION**

The nozzle area ratio can be expressed as a function of Mach number as:

(eq_area_mach)=
$$
\frac{A}{A_*} = \frac{1}{Ma} \left[\frac{2}{\gamma+1}\left(1+\frac{\gamma-1}{2}Ma^2\right)\right]^{\frac{\gamma+1}{2(\gamma-1)}}.
$$

This relation is obtained by combining continuity with the isentropic stagnation-to-static relations and expressing the mass flow both at a generic section and at the throat.

:::

---

(subsec_polytropic_nozzle)=
### Non-isentropic (polytropic) nozzle model

If the nozzle is not internally reversible, a polytropic approximation may be employed, written as $p v^n = \text{const.}$ In such a case, the critical ratios adopt forms analogous to the isentropic case, replacing $\gamma$ by $n$ where appropriate:

- $T_*/T_0 = 2/(n+1)$,
- $p_*/p_0 = \left(2/(n+1)\right)^{n/(n-1)}$,
- $\rho_*/\rho_0 = \left(2/(n+1)\right)^{1/(n-1)}$.

The throat velocity becomes:

(eq_throat_velocity_polytropic)=
$$
c_* = \sqrt{\frac{2\gamma}{n+1}{}\frac{n-1}{\gamma-1}}{}\sqrt{R T_0}.
$$

A practical way to account for losses is to relate the real exit velocity to the isentropic one through an efficiency factor $\eta$:

(eq_exit_velocity_eta)=
$$
c_2 \approx \sqrt{\eta}c_{2,\text{iso}}.
$$

The polytropic exponent can be linked to the efficiency through:

(eq_polytropic_n_eta)=
$$
n = \frac{\gamma+1+\eta(\gamma-1)}{\gamma+1-\eta(\gamma-1)}.
$$

---

(subsec_nozzles_conceptual_closure)=
### Conceptual closure

- Nozzles convert enthalpy into kinetic energy; diffusers perform the inverse conversion.
- The area variation required to accelerate or decelerate a flow depends on Mach number.
- The key relation is $\dfrac{dA}{A} = -\dfrac{dc}{c}(1-Ma^2)$.
- Choking occurs when the throat reaches $M=1$, limiting the mass flow rate.
- In Laval nozzles, discharge pressure controls whether shocks appear inside or outside the nozzle.
- Isentropic stagnation relations provide $T_0/T$, $p_0/p$, and $\rho_0/\rho$ as functions of $Ma$.
- Real nozzles may be modelled polytropically or through velocity/efficiency corrections.

