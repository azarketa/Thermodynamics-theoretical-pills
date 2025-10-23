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

:::{admonition} Note: physical interpretation
:class: note, dropdown

The mass fraction expresses how much of the mixture’s total mass corresponds to each species, whereas the molar fraction expresses how many moles of that species are present relative to the total moles.
Both are fundamental when converting between molar and mass-based quantities in mixture calculations.
:::

---

(subsec_pvt_behaviour_ideal_mixtures)=
### P-v-T behaviour of mixtures of ideal gases

The definitions of $x_i$ and $y_i$ become particularly relevant when describing the pressure–volume–temperature ($P$–$v$–$T$) behavior of mixtures that obey the **ideal gas law**. When gases behave ideally, two empirical relations—**Dalton’s law** and **Amagat’s law**—connect the overall properties of the mixture to those of its individual components.

(eq_dalton_law)=
$$P_{\text{total}}{}={} \sum_{i=1}^{k} P_i(T_{\text{total}}, V_{\text{total}})$$

According to Dalton’s law, the **total pressure** of a mixture equals the sum of the **partial pressures** exerted by each component. Each partial pressure $P_i$ is calculated at the total temperature and total volume of the mixture, i.e., the thermodynamic state shared by all species.

In a parallel manner, **Amagat’s law** applies the same additive principle to volumes:

(eq_amagat_law)=
$$V_{\text{total}}{}={} \sum_{i=1}^{k} V_i(T_{\text{total}}, P_{\text{total}})$$

Amagat’s statement reflects that **volume is also an extensive property**, just like mass or moles. It follows that the total volume of the mixture equals the sum of the partial volumes each component would occupy if it alone existed at the mixture’s total pressure and temperature.

Now, introducing the **ideal gas law** for each component, we can establish the link between the ratios of partial and total quantities and the molar fractions. For any component $i$:

(eq_partial_pressure_ratio)=
$$\frac{P_i(T_{\text{total}}, V_{\text{total}})}{P_{\text{total}}}{}={} \frac{\left(\frac{N_i R_u T_{\text{total}}}{V_{\text{total}}}\right)}{\left(\frac{N_{\text{total}} R_u T_{\text{total}}}{V_{\text{total}}}\right)}{}={} \frac{N_i}{N_{\text{total}}}{}={}y_i$$

(eq_partial_volume_ratio)=
$$\frac{V_i(T_{\text{total}}, P_{\text{total}})}{V_{\text{total}}}{}={} \frac{\left(\frac{N_i R_u T_{\text{total}}}{P_{\text{total}}}\right)}{\left(\frac{N_{\text{total}} R_u T_{\text{total}}}{P_{\text{total}}}\right)}{}={} \frac{N_i}{N_{\text{total}}}{}={}y_i$$

Thus, the ratios of each component’s partial pressure and partial volume to the total mixture values both coincide with the component’s **molar fraction**:

(eq_y_relation)=
$$\frac{P_i}{P_{\text{total}}}{}={} \frac{V_i}{V_{\text{total}}}{}={} \frac{N_i}{N_{\text{total}}}{}={}y_i$$

:::{admonition} Tip: significance of molar fraction
:class: tip, dropdown

The molar fraction directly expresses how each species contributes to the overall pressure and volume of the gas mixture. It serves as the natural weighting factor for many other mixture properties and simplifies the formulation of state and energy equations.
:::

---

(subsec_properties_ideal_mixtures)=
### Properties of ideal gas mixtures

Once the $P$–$v$–$T$ relations for ideal mixtures are established, the same definitions of molar and mass fractions can be used to describe other thermodynamic properties. The **additivity principle** of extensive properties extends naturally to internal energy, enthalpy, entropy, and specific heats.

For the **specific molar heats** (expressed in $\mathrm{J/mol\cdot K}$), each property of the mixture is the molar-fraction-weighted sum of the corresponding properties of the individual gases:

(eq_molar_specific_heats)=
$$c_{p,\text{mixture}}{}={} \sum_{i=1}^{k} y_i{}c_{p,i} \qquad\text{and}\qquad c_{v,\text{mixture}}{}={} \sum_{i=1}^{k} y_i{}c_{v,i}$$

When specific heats are expressed on a **mass basis** (in $\mathrm{J/kg\cdot K}$), the weighting must be performed with the **mass fractions** instead:

(eq_mass_specific_heats)=
$$c_{p,\text{mixture}}{}={} \sum_{i=1}^{k} x_i{}c_{p,i} \qquad\text{and}\qquad c_{v,\text{mixture}}{}={} \sum_{i=1}^{k} x_i{}c_{v,i}$$

Similarly, the **molar mass** of the mixture—representing the equivalent mass per kilomole of mixture—is obtained through the molar-fraction-weighted sum of the molar masses of the components:

(eq_mixture_molar_mass)=
$$M_{\text{mixture}}{}={} \sum_{i=1}^{k} y_i{}M_i$$

The **gas constant of the mixture**, in turn, is obtained by performing a mass-fraction-weighted sum of the individual gas constants:

(eq_mixture_gas_constant)=
$$R_{\text{mixture}}{}={} \sum_{i=1}^{k} x_i{}R_i$$

Finally, the **state properties** of the mixture and their **variations** (such as internal energy, enthalpy, and entropy) are expressed as the mass-weighted sums of the corresponding specific state properties of each component:

(eq_state_property_changes)=
$$\Delta U_{\text{mixture}}{}={} \sum_{i=1}^{k} m_i{}\Delta u_i$$

(eq_enthalpy_change_mixture)=
$$\Delta H_{\text{mixture}}{}={} \sum_{i=1}^{k} m_i{}\Delta h_i$$

(eq_entropy_change_mixture)=
$$\Delta S_{\text{mixture}}{}={} \sum_{i=1}^{k} m_i{}\Delta s_i$$

:::{admonition} Note: interpretation of mixture properties
:class: note, dropdown

Each property of an ideal gas mixture—whether expressed per mole or per mass—results from **weighted averaging** of the component properties. The weighting factor depends on the reference basis:

* **Molar fraction $y_i$** for molar properties.
* **Mass fraction $x_i$** for mass-based properties.
  This distinction ensures dimensional consistency and accurate property predictions.
  :::

:::{admonition} Important: validity of additivity
:class: warning

All the relations above rely on the **ideal mixture assumption**, where interactions between different species are neglected. For real mixtures—especially under high pressure, low temperature, or when chemical reactions occur—these additivity rules must be replaced by non-ideal mixture models (e.g., equations of state with mixing rules or activity coefficients).
:::

---

(subsec_conceptual_closure_gas_mixtures)=
### Conceptual Closure

* **Mass and molar fractions** ({ref}`definitions <eq_mass_molar_fractions>`) serve as the cornerstone of mixture analysis. Their normalization ({ref}`constraint <eq_normalization_mass_molar>`) guarantees a complete composition description.
* **Dalton’s** ({ref}`law of pressures <eq_dalton_law>`) and **Amagat’s** ({ref}`law of volumes <eq_amagat_law>`) establish the additive behavior of ideal mixtures for pressure and volume.
* Both **partial pressures** and **partial volumes** scale with the **molar fraction** ({ref}`fundamental relation <eq_y_relation>`), explaining its central role in mixture formulations.
* **Property evaluation** follows the same additive logic: specific heats ({ref}`molar and mass basis <eq_molar_specific_heats>`–{ref}`<eq_mass_specific_heats>`), molar mass ({ref}`<eq_mixture_molar_mass>`), and gas constant ({ref}`<eq_mixture_gas_constant>`) are all weighted averages.
* **State-property variations** such as internal energy, enthalpy, and entropy ({ref}`<eq_state_property_changes>`–{ref}`<eq_entropy_change_mixture>`) are mass-weighted sums, extending the same principle to energy and entropy analysis.
