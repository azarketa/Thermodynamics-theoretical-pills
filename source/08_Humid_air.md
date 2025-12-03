(sec_humid_air)=
## Humid air

Humid air is ordinary atmospheric air that carries a variable amount of water vapor. For analysis, it is convenient to regard it as a **binary mixture** of **dry air** (whose composition is nearly constant) and **water vapor** (whose amount changes with environmental conditions). Under typical atmospheric ranges, both constituents can be modeled as **ideal gases**, which lets us reuse the mixture tools introduced earlier while keeping calculations simple and accurate.

Psychrometry focuses on a few core ideas: how much vapor the air contains (its **moisture content**), how that compares with the maximum it *could* contain at the same temperature (its **relative humidity**), how the **pressure** splits between dry air and vapor (via partial pressures), and how to compute **enthalpy** on a clear reference basis (usually per unit mass of dry air). These concepts provide a compact, practical language for problems in comfort, drying, cooling, dehumidification, and atmospheric processes.

(subsec_air_vapor_mixture_atmospheric_air)=
### Air–vapor mixture: atmospheric air

Air is composed mainly of nitrogen and oxygen, and to a lesser extent, other gases such as argon and carbon dioxide. This composition corresponds to **dry air**, which does not contain any water vapor.

In reality, **atmospheric air** usually contains some amount of water vapor (moisture) that varies depending on temperature and environmental conditions. For most practical analyses, it is convenient to model atmospheric air as a **mixture of dry air and water vapor**. The composition of dry air remains approximately constant, while the amount of water vapor fluctuates due to **evaporation** and **condensation** phenomena in the atmosphere.

Therefore, the challenge arises: *how can atmospheric air be characterized?*
If both the dry air and the water vapor are assumed to behave as **ideal gases**, the concepts and relations previously established for gas mixtures can be directly applied to the analysis of humid air.

This is, in essence, the objective of **psychrometry** — the study of the thermodynamic properties of **humid air**.

---

(subsec_air_vapor_pressure_and_enthalpy)=
### Air–vapor mixture: pressure and enthalpy under ideal-gas assumptions

Under typical atmospheric conditions, air temperature ranges approximately from $-10 \ ^{\circ}\text{C}$ to $50 \ ^{\circ}\text{C}$. Within this range, **dry air** behaves very closely to an **ideal gas**. As we shall see, this means that its thermodynamic properties depend almost entirely on temperature. This allows us to introduce a simple, practical link between temperature and energy content through two related quantities: the **specific heat** and the **enthalpy**.

The **specific heat at constant pressure**, $c_p$, acts as a proportionality factor connecting temperature and energy: it indicates how much energy is required, per kilogram of substance, to raise its temperature one Kelvin while the pressure remains constant.

(eq_cp_dry_air)=
$$c_p = 1.005 \ [\mathrm{kJ/(kg\cdot K)}]$$

In this context, the **specific enthalpy** $h$ serves as a convenient measure of the specific energy content of the gas, combining both its internal energy and the energy associated with the pressure it exerts. As occurs with the specific heat, the specific enthalpy of an ideal gas depends only on temperature, making it straightforward to compute.

Taking a reference temperature of $0 \ ^{\circ}\mathrm{C}$, the **specific enthalpy** of dry air can be expressed as

(eq_h_dry_air)=
$$h = c_p T$$

and the corresponding **enthalpy difference** between two states as

(eq_delta_h_dry_air)=
$$\Delta h_{i\to f} = c_p \Delta T_{i\to f}.$$

If both **air** and **water vapor** are treated as ideal gases, then, according to **Dalton’s law of partial pressures**, the total pressure is the sum of the individual partial pressures:

(eq_dalton_air_vapor)=
$$p{}={}p_a{}+{}p_{\text{v}}$$

In the $T$–$s$ diagram of water, lines of constant enthalpy and constant temperature overlap below $50 \ ^{\circ}\mathrm{C}$, confirming that enthalpy depends primarily on temperature in this range. Therefore, the enthalpy of water vapor in air may be taken as that of **saturated vapor at the same temperature**:

(eq_hv_hg_relation)=
$$h_{\text{v}}(T, \text{low }p) \simeq h_g(T)$$

Given that the enthalpy of saturated water vapor at $0 \ ^{\circ}\mathrm{C}$ is $2500.9\ \mathrm{kJ/kg}$ and that its average specific heat is $c_p{}={}1.82\ \mathrm{kJ/kg\cdot K}$, one may write:

(eq_hg_approximation)=
$$h_g(T) \simeq h_g(0 \ ^{\circ}\mathrm{C}){}+{}1.82T{}={}2500.9{}+{}1.82{}T \ [\mathrm{kJ/kg}]$$

:::{note}

**IDEAL-GAS ASSUMPTION FOR WATER VAPOR**

Treating water vapor as an ideal gas implies a small accuracy loss, but it is negligible under typical atmospheric conditions. At $50 \ ^{\circ}\mathrm{C}$, the saturation pressure of water is $12.3 \ \mathrm{kPa}$. Below this pressure, water vapor behaves as an **ideal gas** with an error below $0.2 \ \%$, even in saturated states.
Thus, water vapor enthalpy depends **only on temperature**, $h_{\text{v}}{}={}h(T)$.

:::

:::{note}

**THE TEMPERATURE REFERENCE FOR ENTHALPY CALCULATION**

The expression for {ref}`the enthalpy variation of dry air <eq_h_dry_air>` shows, apparently, that the enthalpy at a given thermodynamic state can be computed **in absolute terms**. Thermodynamics, however, does not provide any means of calculating absolute energetic values, but **differences of energies** (or enthalpies, or entropies). Indeed, as the reference temperature is set at $0 \ ^{\circ}\text{C}$, and there is a **linear relationship** between $^{\circ}\text{C}$ and $K$ (a temperature difference of $X \ ^{\circ}\text{C}$ is the same as a difference of $X \ \text{K}$), it is possible to **drop the reference temperature** term from the expression. Formally, though, the expression should have read:

$$\Delta{}h_{0\to{}i}={}c_p{}(T_{i} - T_{0})\left[^{\circ}\text{C}\right]$$

Then the rigorous expression for the {ref}`enthalpy change between arbitrary initial and final states <eq_delta_h_dry_air>` would be:

$$\Delta{}h_{i\to{}f} = c_p{}\left(\Delta{}T_{0\to{}f} - \Delta{}T_{0\to{}i}\right) = c_p{}\left(T_{f} - T_{0} - \left(T_{i} - T_{0}\right)\right) = c_p\left(T_{f} - T_{i}\right) = c_p\Delta{}T_{i\to{}f}$$

:::

:::{tip}

**APPROXIMATE EVALUATION OF HUMID-AIR ENTHALPY**

When performing psychrometric calculations, use {ref}`dry-air enthalpy <eq_h_dry_air>` for the dry portion and {ref}`water-vapor enthalpy <eq_hg_approximation>` for the vapor portion. Both can be combined later to express the total enthalpy of humid air per unit mass of dry air.
:::

---

(subsec_humidities)=
### Air–vapor mixture: humidities

The **amount of water vapor** in air can be quantified in several ways. The most intuitive is the **specific humidity** $\omega$, which represents the mass of water vapor per unit mass of dry air:

(eq_specific_humidity)=
$$
\omega{}={} \frac{m_{\text{v}}}{m_a}{}={}
\frac{\left(p_{\text{v}} V / R_{\text{v}} T\right)}{\left(p_a V / R_a T\right)}{}={}
\frac{(p_{\text{v}}/R_{\text{v}})}{(p_a/R_a)}{}={}
0.622\frac{p_{\text{v}}}{p_a}
\quad\left[\frac{\text{kg water vapor}}{\text{kg dry air}}\right]
$$

For perfectly dry air ($m_{\text{v}}{}={}0$), $\omega{}={}0$. As more vapor is added, $\omega$ increases until the air reaches **saturation** — the condition where it can hold no additional moisture.

At saturation, any extra water vapor condenses. The specific humidity of **saturated air** at a given temperature and pressure can thus be computed by replacing $p_{\text{v}}$ in {ref}`the specific humidity relation <eq_specific_humidity>` with the **saturation pressure** $p_g$ of water at that temperature.

The **relative humidity** $\phi$ compares the actual vapor content to the maximum possible vapor content at the same temperature:

(eq_relative_humidity)=
$$
\phi{}={} \frac{m_{\text{v}}}{m_g}{}={}
\frac{(p_{\text{v}} V / R_{\text{v}} T)}{(p_g V / R_{\text{v}} T)}{}={}
\frac{p_{\text{v}}}{p_g}
\quad[-]
$$

where $p_g{}={}p_{\text{sat @ }T}$ is the saturation pressure of water at temperature $T$.

For an air–vapor mixture, the **enthalpy** per unit mass of dry air combines the contributions from both components:

(eq_total_enthalpy_mixture)=
$$H{}={}H_a{}+{}H_{\text{v}}{}={}m_a h_a{}+{}m_{\text{v}} h_{\text{v}}$$

and, dividing by $m_a$:

(eq_specific_enthalpy_humid_air)=
$$h{}={}h_a{}+{}\frac{m_{\text{v}}}{m_a}{}h_{\text{v}}{}={}h_a{}+{}\omega{}h_{\text{v}} \quad [\mathrm{kJ/kg_{dry,air}}]$$

:::{note}

**REFERENCE BASIS FOR HUMID-AIR PROPERTIES**

In psychrometric calculations, properties are commonly expressed **per kilogram of dry air** rather than per kilogram of total mixture.
This simplifies comparisons, since $m_a$ remains constant while $m_{\text{v}}$ varies with humidity and temperature.
:::

:::{important}

**PHYSICAL MEANING OF RELATIVE HUMIDITY**

The relative humidity $\phi$ ranges from 0 (dry air) to 1 (saturated air). As temperature increases, the capacity of air to hold water vapor grows, so $\phi$ changes even when $\omega$ (the actual vapor content) remains constant.
:::

---

(subsec_dew_point_temperature)=
### Dew-point temperature

Humid environments often give rise to **dew formation**, such as finding grass wet on summer mornings even when no rain has fallen. This phenomenon occurs when **moist air** cools down until its capacity to hold water vapor equals its actual vapor content.

During the day, evaporation increases the vapor content of the air. As the temperature drops at night, the **moisture-holding capacity** decreases. Eventually, the air becomes **saturated**, meaning that its **relative humidity** reaches $100 \%$. Any further temperature decrease causes condensation — this is the onset of dew formation.

The **dew-point temperature**, $T_{\text{dp}}$, is defined as the temperature at which condensation begins when air is cooled at constant pressure.
In thermodynamic terms, it is the **saturation temperature** of water corresponding to the **current vapor pressure** $p_{\text{v}}$ of the mixture:

(eq_dew_point_definition)=
$$T_{\text{dp}}{}={}T_{\text{sat. @ }p_{\text{v}}}$$

:::{note}

**MEANING OF DEW-POINT TEMPERATURE**

The dew point reflects the **actual moisture content** of air: higher $T_{\text{dp}}$ values imply greater vapor content. When air is cooled to its dew point, condensation begins, marking the transition from unsaturated to saturated conditions.
:::

::::{important}

**WORKED EXAMPLE - WATER AND AIR CONTENTS IN A SAUNA**

**Problem statement**

A sauna room is $5 \ \text{m}$ wide, $3 \ \text{m}$ deep and $2 \ \text{m}$ high. An ambient conditions transmitter device is housed inside, providing the combined reading of absolute pressure, temperature and relative humidity. Under nominal operation conditions of the sauna, the device shows an absolute pressure of $1 \ \text{atm}$, a temperature of $70 \ ^{\circ}\text{C}$, and a relative humidity of $75 \ \%$. Calculate the specific humidity, as well as the total air and water contents in the room. Compare such values to the case in which the sauna is off and its temperature drops (keeping the other variables constant) until reaching equilibrium with the quiescent environment, which is at $20 \ ^{\circ}\text{C}$. Likewise, calculate and compare the dew-point temperatures of the system at both operation conditions. Discuss the results.

**Synthesis**

Two conditions for the same room of volume $5\times3\times2\ \text{m}^3$ are to be evaluated:

* **Nominal operation:** $p=1 \ \text{atm}$, $T=70 \ ^\circ\text{C}$, $\phi=75 \ \%$.
* **Sauna off (equilibrium with environment):** $p=1\ \text{atm}$, $T=20 \ ^\circ\text{C}$, $\phi=75 \ \%$.

---

**Problem data**{cite}`2015Cengel`

| Quantity                       |           Symbol           | Value                                                                      |
| :----------------------------- | :------------------------: | :------------------------------------------------------------------------- |
| Room volume                    |             $V$            | $30 \ \text{m}^3$                                                           |
| Absolute pressure              |             $p$            | $101.325 \ \text{Pa}$                                                     |
| Relative humidity (both cases) |           $\phi$           | $0.75$                                                                     |
| Temperatures                   |         $\left(T_1, \ T_2\right)$         | $\left(70 \ ^\circ\text{C}=343.15 \ \text{K}, \ 20 \ ^\circ\text{C}=293.15 \ \text{K}\right)$ |
| Saturation vapor pressure      | $p_{\text{g}}(70^\circ\text{C})$ | $\approx 31.2 \ \text{kPa}$                                                 |
| Saturation vapor pressure      | $p_{\text{g}}(20^\circ\text{C})$ | $\approx 2.339 \ \text{kPa}$                                                |
| Gas constants                  |        $\left(R_{\text{a}}, \ R_{\text{v}}\right)$       | $\left(287.058, \ 461.5\right) \ \text{J}{}\text{kg}^{-1}\text{K}^{-1}$                    |

---

**Solution strategy**

We treat humid air as an ideal binary mixture (dry air + water vapor). For each state, compute:

1. **Partial pressures**

$$
p_{\text{v}}=\phi{}p_{\text{g}}, \qquad p_{\text{a}}=p-p_{\text{v}} .
$$

2. **Humidity ratio**

$$
\omega = 0.62198{}\frac{p_{\text{v}}}{p-p_{\text{v}}}\quad [\text{kg}_{\text{v}}/\text{kg}_{\text{a}}].
$$

3. **Masses in the room**

$$
m_{\text{a}}=\frac{p_{\text{a}}V}{R_{\text{a}}T}, \qquad m_{\text{v}}=\frac{p_{\text{v}} V}{R_{\text{v}} T}, \qquad m_{\text{tot}} = m_{\text{a}} + m_{\text{v}} .
$$

---

1. **Nominal operation**

    * **Partial pressures**

        $$
        p_{\text{v}} = 0.75\times 31.2 \ \text{kPa} = 23.4 \ \text{kPa},
        $$
        
        $$
        p_{\text{a}} = 101.325 - 23.4 = 77.925 \ \text{kPa}.
        $$
        
        $$
        \boxed{p_{\text{v}} = 23.4 \ \text{kPa}}, \qquad \boxed{p_{\text{a}}=77.925 \ \text{kPa}}.
        $$

    * **Humidity ratio:**

        $$
        \omega = 0.62198{}\frac{23.4}{101.325-23.4} =
        $$

        $$
        = 0.62198{}\frac{23.4}{77.925} = 0.62198\times 0.3004 = 0.1868.
        $$
        
        $$
        \boxed{\omega_{70} = 0.1868 \ \text{kg}_{\text{v}}/\text{kg}_{\text{a}}}.
        $$

    * **Masses in the room:**

        $$
        m_{\text{a}}=\frac{77.925{\cdot}10^{3} \times 30}{287.058 \times 343.15}
        = \frac{2.338{\cdot}10^{6}}{98.45{\cdot}10^{3}} \approx 23.73 \ \text{kg},
        $$
        
        $$
        m_{\text{v}}=\frac{23.4{\cdot}10^{3} \times 30}{461.5\times 343.15}
        = \frac{7.02{\cdot}10^{5}}{1.58{\cdot}10^{5}} \approx 4.433 \ \text{kg},
        $$
        
        $$
        m_{\text{tot}}= 23.73 + 4.433 \approx 28.17\ \text{kg}.
        $$
        
        $$
        \boxed{m_{\text{a},70} = 23.73 \ \text{kg}},\quad
        \boxed{m_{\text{v},70} = 4.433 \ \text{kg}},\quad
        \boxed{m_{\text{tot},70} = 28.17\ \text{kg}}.
        $$
  
    * **Dew-point temperature:**

        The **dew point** is the temperature at which the *saturation pressure* equals this vapor pressure:

        $$
        p_{\text{g}}(T_{\text{dp}}) = p_{\text{v}} = 23.4\ \text{kPa}.
        $$

        From standard steam tables{cite}`2015Cengel`:
        
        | $T$ $[^{\circ}\text{C}]$ | $p_{\text{g}}$ $[\text{kPa}]$ |
        | :------: | :------------: |
        |    60    |      19.94     |
        |    65    |      25.04     |
        |    70    |      31.15     |

        Interpolating between $60 \ {^\circ}\text{C}$ and $65 \ {^\circ}\text{C}$:
  
        $$
        T_{\text{dp},70} = 60 + (23.4 - 19.94)\frac{65 - 60}{25.04 - 19.94} =        
        $$

        $$
        = 60 + 3.46\times 0.98 \approx 63.4 \ ^\circ\text{C}.
        $$

        $$
        \boxed{T_{\text{dp},70} \approx 63.4 \ ^\circ\text{C}}.
        $$
  
---

2. **Sauna off**

    * **Partial pressures (substitute numbers first):**

        $$
        p_{\text{v}}=0.75\times 2.339 \ \text{kPa} = 1.75425 \ \text{kPa},
        $$

        $$
        p_{\text{a}}=101.325 - 1.75425 = 99.57075 \ \text{Pa}.
        $$
        
        $$
        \boxed{p_{\text{v}} = 1.754 \ \text{kPa}}, \qquad \boxed{p_{\text{a}}=99.57075 \ \text{kPa}}.
        $$

    * **Humidity ratio:**

        $$
        \omega = 0.62198{}\frac{1.754}{101.325 - 1.754} =        
        $$

        $$
        = 0.62198{}\frac{1.754}{99.57075} = 0.62198 \times 0.01762 = 0.01096.
        $$
        
        $$
        \boxed{\omega_{20} = 0.01096\ \text{kg}_{\text{v}}/\text{kg}_{\text{a}}}.
        $$

    * **Masses in the room:**

        $$
        m_{\text{a}} = \frac{99.57075{\cdot}10^{3} \times 30}{287.058\times 293.15}
        = \frac{2.99{\cdot}10^{6}}{84.16{\cdot}10^{3}} \approx 35.50 \ \text{kg},
        $$
        
        $$
        m_{\text{v}}=\frac{1.754{\cdot}10^{3} \times 30}{461.5 \times 293.15}
        = \frac{5.26{\cdot}10^{4}}{1.35{\cdot}10^{5}}\approx 0.389 \ \text{kg},
        $$
        
        $$
        m_{\text{tot}} = 35.50 + 0.389\approx 35.89\ \text{kg}.
        $$
        
        $$
        \boxed{m_{\text{a},20} = 35.50 \ \text{kg}},\quad
        \boxed{m_{\text{v},20} = 0.389 \ \text{kg}},\quad
        \boxed{m_{\text{tot},20} = 35.89\ \text{kg}}.
        $$

    * **Dew-point temperature:**

        Here,
  
        $$p_{\text{v}} = 0.75 \times p_{\text{g}}(20^\circ\text{C}) = 1.754\ \text{kPa}.$$
        
        From tables{cite}`2015Cengel`:

        | $T$ $[^{\circ}\text{C}]$ | $p_{\text{g}}$ $[\text{kPa}]$ |
        | :------: | :------------: |
        |    15    |      1.705     |
        |    20    |      2.339     |

        Interpolating between $15 \ ^{\circ}\text{C}$ and $20 \ ^{\circ}\text{C}$:
  
        $$
        T_{\text{dp},20} = 15 + (1.754 - 1.705)\frac{20 - 15}{2.339 - 1.705} =        
        $$

        $$
        = 15 + 0.049\times 7.87 \approx 15.4 \ ^\circ\text{C}.
        $$

        $$
        \boxed{T_{\text{dp},20} \approx 15.4 \ ^\circ\text{C}}.
        $$

---

3. **Comparative table**

| Case | $T$ $[^{\circ}\text{C}]$ | $\phi$ $[–]$ | $p_{\text{v}}$ $[\text{kPa}]$ | $p_{\text{a}}$ $[\text{kPa}]$ | $\omega$ $[\text{kg}_{\text{v}}/\text{kg}_{\text{a}}]$ | $m_{\text{a}}$ $[\text{kg}]$ | $m_{\text{v}}$ $[\text{kg}]$ | $m_{\text{tot}}$ $[\text{kg}]$ | $T_{\text{dp}}$ $[^{\circ}\text{C}]$ |
| :------------------------------------ | :------: | :--------: | :---------: | :------------: | :--------------------: | ------------: | ---------: | ----------------------: | :------: |
| **Nominal operation** | $70$ | $0.75$ | $23.4$  | $77.93$ | $0.1868$ | $23.73$ | $4.433$ | $28.17$ | $63.4$ |
| **Sauna off** | $20$ | $0.75$ | $1.754$ | $99.57$ | $0.01096$ | $35.50$ | $0.389$ | $35.89$ | $15.4$ |
| **Relative change**<br/>(vs. nominal) | $-71.4 \ \%$ | $—$ | $−92.5 \ \%$ | $+27.8 \ \%$ | $−94.1 \ \%$ | $+49.6 \ \%$ | $−91.2 \ \%$ | $+27.4 \ \%$ | $-75.7 \ \%$ |

---

4. **Discussion of results**

    * **Sharp collapse of vapor pressure and humidity ratio:** when cooled from $70 \ ^{\circ}\text{C}$ to $20  \ ^{\circ}\text{C}$ (keeping $\phi = 75 \ \%$), the vapor partial pressure $p_{\text{v}}$ drops by more than **$90 \ \%$**, and the specific humidity $w$ decreases by roughly **$94 \ \%$** $\Longrightarrow$ The air’s capacity to hold water vapor dramatically declines at low temperature.
    
    * **Substantial reduction in vapor mass.**
       Water vapor mass in the room falls from **$4.43 \ \text{kg}$** to **$0.39 \ \text{kg}$** ($\approx -91 \ \%$). The warm-air condition thus contains more than ten times as much moisture per cubic meter as the cool condition.
    
    * **Increase in total and dry-air mass.**
       Cooling at constant pressure and volume increases the gas density, so $m_{\text{a}}$ rises by **$\approx 50 \ \%$**, and total moist-air mass by **$\approx 27 \ \%$**.
    
    * **Drop in the dew-point temperature.**
        In the **hot sauna**, the dew point is extremely high ($\approx 63 \ ^{\circ}\text{C}$), meaning condensation will occur on any surface below this temperature — practically all metallic or glass elements near room boundaries. In the **cooled condition**, the dew point drops to $\approx 15 \ ^{\circ}\text{C}$, consistent with typical indoor humidity levels. The $48 \ ^{\circ}\text{C}$ difference in dew points reflects the **strong exponential dependence** of vapor pressure on temperature — the essence of why saunas maintain such dense, moisture-rich atmospheres.

---

:::{tip}

**PHYSICAL IMPLICATION OF REAL COOLING**

In practice, if the $70 \ ^{\circ}\text{C}$ air were cooled in a closed volume without dehumidification, most of the water vapor could not remain in the gaseous phase; about **$4 \ \text{kg}$** of liquid water would **condense** on walls and benches to re-establish saturation at low temperature.
:::

::::

---

(subsec_conceptual_closure_humid_air)=
### Conceptual closure

* **Atmospheric air** is modeled as a **mixture of dry air and water vapor**, where dry air composition remains constant but water vapor content varies.
* Assuming **ideal-gas behavior** allows the use of {ref}`Dalton’s law <eq_dalton_air_{\text{v}}apor>` and simple relations for {ref}`dry air <eq_h_dry_air>` and {ref}`humid air enthalpies <eq_hg_approximation>`.
* {ref}`Specific humidity <eq_specific_humidity>` ($\omega$) quantifies vapor mass per unit dry air, while {ref}`relative humidity <eq_relative_humidity>` ($\phi$) expresses the ratio of current to maximum vapor content.
* The {ref}`enthalpy of humid air <eq_specific_enthalpy_humid_air>` is calculated per unit mass of dry air, combining dry-air and vapor contributions.
* The {ref}`dew-point temperature <eq_dew_point_definition>` indicates when condensation begins and serves as a key measure of actual moisture in air.
