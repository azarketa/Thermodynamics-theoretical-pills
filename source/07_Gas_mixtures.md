(sec_gas_mixtures)=
## Gas mixtures

Gas mixtures often serve as the working fluid in thermodynamic systems. Unlike pure substances, which consist of a single molecular species, a gas mixture is composed of several pure components. Each of these components contributes to the overall properties of the mixture, and their interaction must be described through specific definitions that extend the concepts used for single substances.

The two most fundamental composition descriptors are the **mass fraction** and the **molar fraction**, both of which quantify how each component contributes to the total mass and total number of moles of the mixture. Understanding these definitions is essential for expressing mixture properties and formulating the equation of state that governs their thermodynamic behavior.

---

(subsec_mass_and_molar_fractions)=
### Mass and molar fractions

Consider a gas mixture composed of $k$ different substances (e.g., oxygen and carbon monoxide). Since **mass** and **amount of substance** are *extensive* properties, their total values are the sums of the contributions from each component. Using the subscript $i$ to denote a specific component, we can write:

(eq_total_moles_mass)=
$$N_{\text{total}}{}={} \sum_{i=1}^{k} N_i \qquad\text{and}\qquad m_{\text{total}}{}={} \sum_{i=1}^{k} m_i$$

Each component of the mixture is characterized by two fractions:

* The **mass fraction** $x_i$, which represents the proportion of the total mass belonging to component $i$.
* The **molar fraction** $y_i$, which represents the proportion of the total number of moles corresponding to that same component.

They are defined as follows:

(eq_mass_molar_fractions)=
$$x_i{}={} \frac{m_i}{m_{\text{total}}} \qquad\text{and}\qquad y_i{}={} \frac{N_i}{N_{\text{total}}}$$

Since they are fractions, they must satisfy the normalization condition:

(eq_normalization_mass_molar)=
$${\sum_{i=1}^{k} x_i}{}={}1 \qquad\text{and}\qquad {\sum_{i=1}^{k} y_i}{}={}1$$

:::{note}

**PHYSICAL INTERPRETATION**

The mass fraction expresses how much of the mixture’s total mass corresponds to each species, whereas the molar fraction expresses how many moles of that species are present relative to the total moles.
Both are fundamental when converting between molar and mass-based quantities in mixture calculations.
:::

---

(subsec_pvt_behaviour_ideal_mixtures)=
### $p-v-T$ behaviour of mixtures of ideal gases

The definitions of $x_i$ and $y_i$ become particularly relevant when describing the pressure–volume–temperature ($p–v–T$) behavior of mixtures that obey the **ideal gas law**. When gases behave ideally, two empirical relations—**Dalton’s law** and **Amagat’s law**—connect the overall properties of the mixture to those of its individual components.

(eq_dalton_law)=
$$p_{\text{total}}{}={} \sum_{i=1}^{k} p_i(T_{\text{total}}, V_{\text{total}})$$

According to Dalton’s law, the **total pressure** of a mixture equals the sum of the **partial pressures** exerted by each component. Each partial pressure $p_i$ is calculated at the total temperature and total volume of the mixture, i.e., the thermodynamic state shared by all species.

In a parallel manner, **Amagat’s law** applies the same additive principle to volumes:

(eq_amagat_law)=
$$V_{\text{total}}{}={} \sum_{i=1}^{k} V_i(T_{\text{total}}, p_{\text{total}})$$

Amagat’s statement reflects that **volume is also an extensive property**, just like mass or moles. It follows that the total volume of the mixture equals the sum of the partial volumes each component would occupy if it alone existed at the mixture’s total pressure and temperature.

Now, introducing the **ideal gas law** for each component, we can establish the link between the ratios of partial and total quantities and the molar fractions. For any component $i$:

(eq_partial_pressure_ratio)=
$$\frac{p_i(T_{\text{total}}, V_{\text{total}})}{p_{\text{total}}}{}={} \frac{\left(\frac{N_i R_u T_{\text{total}}}{V_{\text{total}}}\right)}{\left(\frac{N_{\text{total}} R_u T_{\text{total}}}{V_{\text{total}}}\right)}{}={} \frac{N_i}{N_{\text{total}}}{}={}y_i$$

(eq_partial_volume_ratio)=
$$\frac{V_i(T_{\text{total}}, p_{\text{total}})}{V_{\text{total}}}{}={} \frac{\left(\frac{N_i R_u T_{\text{total}}}{p_{\text{total}}}\right)}{\left(\frac{N_{\text{total}} R_u T_{\text{total}}}{p_{\text{total}}}\right)}{}={} \frac{N_i}{N_{\text{total}}}{}={}y_i$$

Thus, the ratios of each component’s partial pressure and partial volume to the total mixture values both coincide with the component’s **molar fraction**:

(eq_y_relation)=
$$\frac{p_i}{p_{\text{total}}}{}={} \frac{V_i}{V_{\text{total}}}{}={} \frac{N_i}{N_{\text{total}}}{}={}y_i$$

:::{tip}

**THE SIGNIFICANCE OF MOLAR FRACTION**

The molar fraction directly expresses how each species contributes to the overall pressure and volume of the gas mixture. It serves as the natural weighting factor for many other mixture properties and simplifies the formulation of state and energy equations.
:::

---

(subsec_properties_ideal_mixtures)=
### Properties of ideal gas mixtures

Once the $p$–$v$–$T$ relations for ideal mixtures are established, the same definitions of molar and mass fractions can be used to describe other thermodynamic properties. The **additivity principle** of extensive properties extends naturally to internal energy, enthalpy, entropy, and specific heats.

For the **specific molar heats** (expressed in $[\mathrm{J/mol\cdot K}]$), each property of the mixture is the molar-fraction-weighted sum of the corresponding properties of the individual gases:

(eq_molar_specific_heats)=
$$\overline{c_{p}}_{\text{mixture}}{}={} \sum_{i=1}^{k} y_i{}\overline{c_{p}}_{i} \qquad\text{and}\qquad \overline{c_{v}}_{\text{mixture}}{}={} \sum_{i=1}^{k} y_i{}\overline{c_{v}}_{i}$$

When specific heats are expressed on a **mass basis** (in $[\mathrm{J/kg\cdot K}]$), the weighting must be performed with the **mass fractions** instead:

(eq_mass_specific_heats)=
$$c_{p_{\text{mixture}}}{}={} \sum_{i=1}^{k} x_i{}c_{p_{i}} \qquad\text{and}\qquad c_{v_{\text{mixture}}}{}={} \sum_{i=1}^{k} x_i{}c_{v_{i}}$$

Similarly, the **molar mass** of the mixture—representing the equivalent mass per kilomole of mixture—is obtained through the molar-fraction-weighted sum of the molar masses of the components:

(eq_mixture_molar_mass)=
$$\text{MW}_{\text{mixture}}{}={} \sum_{i=1}^{k} y_i{}\text{MW}_i$$

Finally, the **gas constant of the mixture**, in turn, is obtained by performing a mass-fraction-weighted sum of the individual gas constants:

(eq_mixture_gas_constant)=
$$R_{\text{mixture}}{}={} \sum_{i=1}^{k} x_i{}R_i$$

Finally, the **extensive properties** of a mixture can be expressed either as the **molar-weighted** or the **mass-weighted** sums of the corresponding molar/specific properties of each component:

$$
\Phi_{\text{mixture}} = \sum_{i=1}^{k} N_i\overline{\phi}_i = \sum_{i=1}^{k} m_i\phi_i
$$

where

* $\Phi_{\text{mixture}}$ is the total (extensive) property of the mixture,
* $\overline{\phi}_i$ and $\phi_i$ are the **molar** and **specific** properties, respectively, of component $i$,
* $N_i$ and $m_i$ are the **moles** and **mass** of that component, and
* $k$ is the total number of components in the mixture.

This formulation applies to any **extensive quantity** — such as total volume — and ensures that the mixture property reflects the collective contribution of all components, each weighted by its mass fraction.

:::{note}

**VALIDITY OF ADDITIVITY**

All the relations above rely on the **ideal mixture assumption**, where interactions between different species are neglected. For real mixtures—especially under high pressure, low temperature, or when chemical reactions occur—these additivity rules must be replaced by non-ideal mixture models (e.g., equations of state with mixing rules or activity coefficients).
:::

:::{important}

**UNIT-CONSISTENCY OF MIXTURE PROPERTIES**

Each property of an ideal gas mixture—whether expressed per mole or per mass—results from **weighted averaging** of the component properties. The weighting factor depends on the reference basis:

* **Molar fraction $y_i$** for molar properties.
* **Mass fraction $x_i$** for mass-based properties.
This distinction ensures dimensional consistency and accurate property predictions.

Note that the molar and mass quantities show a different nomenclature. If $\phi$ is a generic quantity being symbolized (i.e. $\phi$ can be a specific heat or a molar weight):
* The **molar quantities** are expressed by **overlined** symbols, i.e. $\overline{\phi}$ (e.g. $\overline{c}_{p,\text{mixture}}$). When a weighted-sum formula is employed, the molar quantities will show up with the **molar fractions $y_{i}$**.
* The **mass quantities** are expressed with **bare** symbols, i.e. $\phi$ (e.g. $c_{p,\text{mixture}}$). When a weighted-sum formula is employed, the mass quantities will show up with the **mass fractions $x_{i}$**.
:::

::::{important}

**WORKED EXAMPLE — MIXTURE PROPERTIES OF STANDARD AIR**

**Problem statement**

Air is a common mixture that usually described as having a volumetric composition of $21 \ \%$ $\text{O}_{2}$ and $79 \ \%$ $\text{N}_{2}$. The molar weights of those components can be obtained from standard chemical tables, as well as the values for the universal gas constant ($\text{R}_{\text{u}}$) and the specific heat constants of the components at particular temperatures. Assuming that the system being analyzed is composed of standard air at a temperature of $25 \ ^{\circ}\text{C}$, calculate its effective molar weight, as well as its specific heat constants, and compare them to the standard tabulated values.

**Synthesis**

“Standard air” is modeled as an ideal gas **mixture** with **mole fractions** $y_{\mathrm{O_2}} = 0.21$, $y_{\mathrm{N_2}}=0.79$ at $T=25 \ ^\circ\text{C}$, and the following magnitudes are computed:

* **Effective molar mass**, $\text{MW}_{\text{air}}$,
* **Mixture** $\overline{c_{p}}_{\text{air}}$ and $\overline{c_{v}}_{\text{air}}$ (molar basis), then **mass-based** $c_{p_{\text{air}}}$, $c_{v_{\text{air}}}$, $R_{\text{air}}$, and $\gamma_{\text{air}}=c_{p_{\text{air}}}/c_{v_{\text{air}}}$,
* Compare to common **tabulated “standard air”** values at $\approx 300 \ \text{K}$.

---

**Problem data**{cite}`2015Cengel`

| Quantity                                    |                  Symbol                  | Value                                                                                                  |
| :------------------------------------------ | :--------------------------------------: | :----------------------------------------------------------------------------------------------------- |
| Mole fractions                              |   $\left(y_{\mathrm{O_2}}, \ y_{\mathrm{N_2}}\right)$   | $\left(0.21, \ 0.79\right)$                                                                                          |
| Molar masses                                |   $\left(\text{MW}_{\mathrm{O_2}}, \ \text{MW}_{\mathrm{N_2}}\right)$   | $\left(31.998, \ 28.0134\right) \ \text{g/mol}$                                                                       |
| Universal gas constant                      |                   $R_u$                  | $8.314462618 \ \text{J mol}^{-1}\text{K}^{-1}$                                                          |
| Component $\overline{c_{p}}$ at $25^\circ\text{C}$ | $\left(\overline{c_{p}}_{\mathrm{O_2}}, \ \overline{c_{p}}_{\mathrm{N_2}}\right)$ | $\left(29.355, \ 29.124\right) \ \text{J mol}^{-1}\text{K}^{-1}$                                                      |
| Reference standard air (tabulated) | $\left(\text{MW}_{\text{air}_{\text{tb}}}, \ R_{\text{air}_{\text{tb}}}, \ c_{p_{\text{air}_{\text{tb}}}}, \ c_{v_{\text{air}_{\text{tb}}}}, \ \gamma_{\text{air}_{\text{tb}}}\right)$ | $\left(28.965, \ 287.058, \ 1005, \ 718, \ 1.400\right)$ |

---

**Calculations**

1. **Effective molar mass (ideal mixture):**

    $$
    \text{MW}_{\text{air}} = \sum_i y_i M_i = 0.21(31.998) + 0.79(28.0134) = 28.850166\ \text{g/mol}.
    $$
    
    $$
    \boxed{\text{MW}_{\text{air}} = 28.850 \ \text{g/mol}}
    $$

2. **Mixture molar heat capacities (ideal gas mixture, Lewis rule):**

    $$
    \overline{c_{p}}_{\text{air}}=\sum_i y_i \overline{c_{p}}_{i} = 0.21(29.355) + 0.79(29.124) = 29.17251 \ \text{J mol}^{-1}\text{K}^{-1},
    $$
    
    $$
    \overline{c_{v}}_{\text{air}} = \overline{c_{p}}_{\text{air}} - R_u = 29.17251 - 8.314462618 = 20.85805 \ \text{J mol}^{-1}\text{K}^{-1}.
    $$
    
    $$
    \boxed{\overline{c_{p}}_{\text{air}} = 29.173\ \text{J mol}^{-1}\text{K}^{-1}}, \qquad \boxed{\overline{c_{v}}_{\text{air}} = 20.858\ \text{J mol}^{-1}\text{K}^{-1}}
    $$

3. **Mass-based properties** (using $\text{MW}_{\text{air}}$ in $\text{kg/mol}$):

    Convert $\text{MW}_{\text{air}}$ to $\text{kg/mol}$: $ \ \text{MW}_{\text{air}} = 28.850166\times10^{-3}\ \text{kg/mol}$.

   * Specific gas constant:

        $$
        R_{\text{air}} = \frac{R_u}{\text{MW}_{\text{air}}} = \frac{8.314462618}{28.850166\times10^{-3}} = 288.1946\ \text{J kg}^{-1}\text{K}^{-1}.
        $$

    * Mass-based heat capacities:
    
        $$
        c_{p_{\text{air}}}=\frac{\overline{c_{p}}_{\text{air}}}{\text{MW}_{\text{air}}} = \frac{29.17251}{28.850166\times10^{-3}} = 1.011 \ \text{kJ kg}^{-1}\text{K}^{-1},
        $$
    
        $$
        c_{v_{\text{air}}}=\frac{\overline{c_{v}}_{\text{air}}}{\text{MW}_{\text{air}}} = \frac{20.85805}{28.850166\times10^{-3}} = 0.723 \ \text{kJ kg}^{-1}\text{K}^{-1}.
        $$

    * Isentropic exponent:

        $$
        \gamma_{\text{air}}=\frac{c_{p_{\text{air}}}}{c_{v_{\text{air}}}} = \frac{1.011}{0.723} = 1.39862.
        $$

    $$
    \boxed{R_{\text{air}} = 288.195\ \text{J kg}^{-1}\text{K}^{-1}},\quad
    \boxed{c_{p_{\text{air}}} = 1.011 \ \text{kJ kg}^{-1}\text{K}^{-1}},
    $$

    $$
    \boxed{c_{v_{\text{air}}} = 0.723 \ \text{kJ kg}^{-1}\text{K}^{-1}},\quad
    \boxed{\gamma_{\text{air}} = 1.3986}
    $$

---

**Comparison to tabulated “standard air”**

| Property  | Present calculations | Tabulated |  Rel. diff |
| :-------------------------- | --------: | --------: | ---------: |
| $\text{MW} \ [\text{g}/\text{mol}]$                    |  $28.850$ |  $28.965$ | $-0.40 \ \%$ |
| $R_{\text{air}} \ [\text{J kg}^{-1}K^{-1}]$            | $288.195$ | $287.058$ | $+0.40 \ \%$ |
| $c_{p_{\text{air}}} \ [\text{kJ kg}^{-1}K^{-1}]$       | $1.011$ |    $1.005$ | $+0.61 \ \%$ |
| $c_{v_{\text{air}}} \ [\text{J kg}^{-1}K^{-1}]$        |  $0.723$ |     $0.718$ | $+0.69 \ \%$ |
| $\gamma_{\text{air}} \ [–]$                            |  $1.3986$ |   $1.400$ | $-0.10 \ \%$ |

---

:::{tip}

**INTERPRETATION**

Differences are **sub-percent** and stem from:
1. The simplified binary composition (no $\text{Ar}$, $\text{CO}_{2}$, etc.; argon alone shifts $\text{MW}_{\text{air}}$ upward).
2. Mild temperature dependencies of $c_{p}$ for real gases around $300\ \text{K}$.

Including minor species (e.g., $\sim0.93 \ \% \ \text{Ar}$) and using high-precision $c_p(T)$ polynomials would bring the results essentially into line with the tabulated “standard air” values.
:::

::::

---

(subsec_conceptual_closure_gas_mixtures)=
### Conceptual closure

* {ref}`Mass and molar fractions <eq_mass_molar_fractions>` serve as the cornerstone of mixture analysis. Their {ref}`normalization constraint <eq_normalization_mass_molar>` guarantees a complete composition description.
* {ref}`Dalton’s law of pressures <eq_dalton_law>` and {ref}`Amagat’s law of volumes <eq_amagat_law>` establish the additive behavior of ideal mixtures for pressure and volume.
* Both **partial pressures** and **partial volumes** {ref}`scale with the molar fraction <eq_y_relation>`, which explains its central role in mixture formulations.
* **Property evaluation** follows the same additive logic: specific heats (in their {ref}`molar <eq_molar_specific_heats>` and {ref}`mass <eq_mass_specific_heats>` formulations), {ref}`molar mass <eq_mixture_molar_mass>`, and {ref}`gas constant <eq_mixture_gas_constant>` are all weighted averages.
* **State-property variations** such as {ref}`internal energy <eq_state_property_changes>`, {ref}`enthalpy <eq_enthalpy_change_mixture>` and {ref}`entropy <eq_entropy_change_mixture>` are mass-weighted sums, extending the same principle to energy and entropy analysis.
