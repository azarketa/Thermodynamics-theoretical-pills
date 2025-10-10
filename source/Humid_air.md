(humid_air)=
# HUMID AIR

(relevance_humid_air)=
## On the relevance of humid air

In scientific disciplines, and engineering certainly falls within those, the terminology employed is of paramount importance. The words used for denominating entities, if different, do not comply with a synonymy principle. In other words: they are different because they refer to distinct entities, however such entities are distinguished at a technical level.

**So far, talking about _gas_ and _vapor_ has been rather indifferent**. But according to the explanation given above, the mere existence of different words already points towards an underlying distinction between those concepts. And, indeed, they are different. The term **vapor** refers to a gas phase of a substance at temperatures below the critical one and, hence, liable to undergo condensation during a thermodynamic process. The term **gas**, instead, addresses thermodynamic states whose temperatures lie well above the critical ones, ruling out the possibility of encountering a phase-change phenomenon during a process.

When analysing gas mixtures in a previous theoretical pill, the fact that the temperatures involved were assumed to lie above the critical temperatures of each of the constituents greatly simplified the mathematical treatment of the approach. The overall gaseous state of the mixture has not required the resort to a two-phase analysis. However, when dealing with a gas-vapor mixture, **the vapor may condense out of the mixture during a process, forming a two-phase mixture** that complicates the analysis.

A legit question arises after the previous assertion: **if gas-vapor mixtures turn the analysis so more complicated, is there any well-founded reason for studying them?** It turns out there is: one of the most common mixtures found in nature and, correspondingly, in engineering applications, is the so-called **air-water vapor mixture**. Ubiquitous in the composition of the atmospheric air, which is better approximated by a **humid air** model instead of the **dry air** mixture analysed so far, modeling the air-water vapor mixture turns relevant for understanding processes involved in meteorology, human confort or air-conditioning. The purpose of the present pill is to provide the modeling framework for such a mixture.

(dry_and_atmospheric_air)=
## Dry and atmospheric air: main mixture properties

(describing_model)=
### Describing the atmospheric air model

Atmospheric air is not composed, solely, of nitrogen and oxygen. Although the canonical mixture of 79% $\text{N}_{2}$ and 21% $\text{O}_{2}$ constitutes a good approximation, such a model fails when analysing certain phenomena in an everyday basis. The condensation of water during nighttime, which gives birth to the **dew drops** (**frost**, when the temperature lies below the freezing point of water at the given conditions) deposited in the surfaces that lie outdoors. This phenomenon sets forth a trivial question: **where does such water come from?** The answer is equally trivial: **it is part of the atmospheric air's composition**, showing that such air cannot be modeled as being merely composed of $\text{N}_{2}$ and $\text{O}_{2}$.

The above distinction between two different types of air turns necessary, once again, to refine the terminology employed. Thus:

- The denomination of **dry air** will be used to address air that contains no water vapor within.
- The denomination of **atmospheric air** will be used to refer to the air that contains some water vapor (i.e. **moisture**) within, and which is the usual mixture encountered in the atmosphere.

However, if an approximation based on dry air has served the calculation purposes acceptably, at least so far: **what is the point of needing to reconsider its modelization?** It is trivial to deduce that, according to the dry air composition and its acceptable correspondence with atmospheric air, **the amount of water vapor in the air is small**. Hence: **is it relevant to take that water into account?** Well, it turns out it is, as such an amount of $\text{H}_{2}\text{O}$, however little one may be tempted to consider it, is one of the responsible factors (as mentioned before) for a range of complex phenomena such as **corrotion**, **meteorological predictions** or, in a much more engineering-related scope, **human confort** and **air conditioning**.

The point of stressing that such phenomena occur in a daily basis is far from being trivial. The temperatures encountered at a global scope can vary greatly depending on the region considered, but it may constitute a well-educated guess to assert that, usually, **they fall between the $\left[-10, 50\right] ^{\circ}\text{C}$ interval**. When dealing with dry air, stating that the possible temperatures the substance will be facing stand within the mentioned interval leads to two main particularities on the behaviour of the nitrogen-oxygen mixture:

- The considered temperature range falls well above the critical point of the two constituents and, _a fortiori_, of the mixture itself. This means that, as long as the mentioned temperature range is considered (and assuming that the pressure deviations are minimal with respect to the standard pressure values found at sea-level), the **dry air can be considered to follow the ideas-gas model**.
- Insofar the mentioned temperature range is a limited one, **considering that the $c_{p}$ value of the mixture does not change much is also a sound assumption**. In other words, the dry air can be modeled as a **perfect gas** with a constant $c_{p}$ value of $c_{p} = 1.005 \ \text{kJ}/\left(\text{kg}{\cdot}^{\circ}\text{C}\right)$.

Notice that, when specifying the value of $c_{p}$ above, its units have been referred to $^{\circ}\text{C}$, instead of employing the usual temperature unit of $\text{K}$. As long as the relationship between those two scales is linear (in fact, the conversion between them is a mere shift of 273.15 units, as is well known), referring the $c_{p}$ value to any of the temperature units is indifferent. Then: **why bother changing the units in the first place?** Well, it turns out that the mentioned shift is pretty convenient for easing the calculations, as the $0 \ ^{\circ}\text{C}$ value lies within the temperature interval at which typical atmospheric air is found. Notice that this is not the case for the $0 \ K$ case, a temperature that is not achievable in everyday applications (in fact, it is not  even reachable on physical grounds). But if the $^{\circ}\text{C}-K$ conversion is made, it turns possible to take the $0 \ ^{\circ}\text{C}$ point as the reference temperature, i.e. $T_{0}=0 \ ^{\circ}\text{C}$. With such a change, and having specified the $c_{p}$ value of dry air above, the property enthalpy, as well as its variations, can be expressed as:

```{math}
:label: eq_enthalpy_dry_air

\displaystyle{h_{\text{dry air}} = c_{p}\left(T - T_{0}\right) = c_{p}T = \left(1.005 \ \text{kJ}/\left(\text{kg}^{\circ}\text{C}\right)\right)T \ [\text{kJ}/\text{kg}]}
```

```{math}
:label: eq_delta_enthalpy_dry_air

\displaystyle{\Delta{}h_{\text{dry air}} = c_{p}\Delta{}T = \left(1.005 \ \text{kJ}/\left(\text{kg}^{\circ}\text{C}\right)\right)\Delta{}T \ [\text{kJ}/\text{kg}]}
```

The dry air description given above, as well as the equations {eq}`eq_enthalpy_dry_air` and {eq}`eq_delta_enthalpy_dry_air`, are the simplest ones possibly conceivable. As such, they constitute an approximate (though a powerful) tool for modeling the two main constituents of the mixture being analysed. However, a trivial question arises: **if dry air can be modeled as a perfect gas, can the same be done with water vapor?** That would certainly ease the treatment of the mixture. But, as long as the term **vapor** refers to a gas whose temperature lies below the critical point, and if that condition goes in parallel with a non-negligible possibility of observing condensation during thermodynamic processes, it seems contradictory to state that water vapor can be treated as an ideal-gas. Obviously, making such an assumption is not prohibited, as long as it is recognised that the resultant model will not be as accurate as treating the vapor as a real substance, with its properties being determined by the empirical $P-v-T$ relations.

However, **how large would the error be if, instead of using the $P-v-T$ tables, an ideal-gas model were assumed for the water vapor?** Fortunately, not so large. It is recalled that, when comparing the empirical ($P-v-T$) and approximate (ideal-gas) models, the largest deviations are found in the vicinity of the critical point and, afterwards, close to the saturation lines. It turns out that, at $50 \ ^{\circ}C$, **the saturation pressure of water is of 12.3 kPa and that, below such value, water vapor may be treated as an ideal-gas with negligible error $(< 0.2\%)$, even when being in a saturated vapor state**. Hence, the mixture that comprises what has been called as **atmospheric air can be assumed to follow the ideal-gas relation $Pv=RT$ overall, i.e. for all of its constituents (dry air and water vapor)**. In addition, the Dalton's law of partial pressures is also fulfilled; using the subscript "_a_" for denoting dry-air-related properties, and subscript "_v_" to address the ones corresponding to water vapor, **the total pressure of the mixture can be decomposed as**:

```{math}
:label: eq_dalton_atmospheric_air

P = P_{\text{a}} + P_{\text{v}} \ [\text{kPa}].
```

It is remarked that, in the equation {eq}`eq_dalton_atmospheric_air` above, the $P_{\text{v}}$ term represents **the pressure that water vapor would exert if it existed alone at the temperature and volume of atmospheric air**; accordingly, it is called the **vapor pressure**.

The last property of interest, when it comes to determine the overall thermodynamic state of the dry-air/water-vapor mixture, is the enthalpy of the vapor. Indeed, equation {eq}`eq_enthalpy_dry_air` allows computing the specific enthalpy of dry air, and equation {eq}`eq_dalton_atmospheric_air` provides the relationship between the overall and partial pressures. Recalling that the state-principle requires two independent intensive variables for fixing the thermodynamic state of a simple system, what rests is to provide a way for calculating the specific enthalpy of the vapor.

Such a calculation can be simplified greatly by noticing that, in the empirical $P-v-T$ relationships for water, **the isoenthalpic (constant-enthalpy) lines adopt the shape of straight lines in the superheated vapor region for temperatures below $50 \ ^{\circ}\text{C}$**. Therefore, **the enhtalpy of water vapor in air can be taken to be equal to the enthalpy of saturated vapor at the same temperature, i.e.:**

```{math}
:label: eq_vapor_enthalpy_approx

h_{\text{v}}\left(T, \text{low} \ P\right) \cong h_{\text{g}}\left(T\right) \ [\text{kJ}/\text{kg}].
```

Equation {eq}`eq_vapor_enthalpy_approx` can be simplified even further, as it is possible to break down the $h_{\text{g}}\left(T\right)$ term by referring it to the baseline temperature of $0 \ ^{\circ}\text{C}$ employed for the dry air constituent above. Thus, it can be checked that the specific enthalpy of water vapor at the reference temperature being considered is of $2500.9 \ \text{kJ}/\text{kg}$, a value that is readable from the tables. Besides, the dependence of the enthalpy on temperature is taken into account by noticing that the average $c_{p}$ value of wtaer vapor in the $[-10, 50]^{\circ}\text{C}$ range is of $1.82 \ \text{kJ}/\left(\text{kg}^{\circ}\text{C}\right)$. Hence:

```{math}
:label: eq_vapor_enthalpy_approx_numbers

h_{\text{g}}\left(T\right) \cong 2500.9 + 1.82T \ [\text{kJ}/\text{kg}] \hspace{2mm} ; \hspace{2mm} T \ \text{in} \ ^{\circ}\text{C}.
```

(summarising_model)=
### Summarising the atmospheric air model

The model described by the equations {eq}`eq_enthalpy_dry_air`, {eq}`eq_dalton_atmospheric_air` and {eq}`eq_vapor_enthalpy_approx_numbers` above allows treating the atmospheric air as an ideal-gas mixture, despite the presence of a constituent ($\text{H}_{2}\text{O}$) that, in principle, does not strictly follow the ideal-gas modelisation. During the conception of such a model, a number of assumptions have been necessary for simplifying the treatment. Such assumptions may sound contradictory at a first glance, as it seems that the notions of ideal-gas and $P-v-T$ relationships are being involved in a rather messy way. Let's break down those assumptions carefully, so that the consistency of the model is put upon a solid ground:

- The temperature interval considered is constrained to the $[-10, 50]^{\circ}\text{C}$. This allows performing a number of simplifications:
    - The constituents of dry air are far from their respective critical points for such a temperature range and the typical pressure values encountered in an everyday basis. _A fortiori_, the same can be said about the dry air mixture itself. Correspondingly, dry air can be treated as a perfect gas, i.e. an ideal gas with a $c_{p}$ value that does not depend on temperature.
    - The fact that the temperature interval considered comprises the $0 \ ^{\circ}\text{C}$ point within allows taking such a point as the reference temperature, simplifying the expression for the specific enthalpy of dry air.
    - The saturation pressure of water at the upper bound of the temperature interval considered is of 12.3 kPa. Usually, the relatively little moisture content in the atmospheric air results in much lower pressure values of the water vapor, which allows asserting that the thermodynamic states of $\text{H}_{2}\text{O}$ present in the air lie at the overly superheated vapor region of its $P-v-T$ diagram. Hence, it is safe to assume that the water vapor behaves as an ideal-gas. Correspondingly, the overall atmospheric-air mixture also follows the ideal-gas model.
    - When represented in a $T-s$ diagram (an additional projection resultant from the $P-v-T$ relationships), the specific enthalpy lines of the water vapor at the superheated region become straight lines for temperatures below $50 \ ^{\circ}\text{C}$. This allows approximating the specific enthalpy of the water vapor in its superheated state by a simpler expression. Indeed, it can be stated that the enthalpy of water vapor in air is equal to the enthalpy of saturated vapor at the same temperature, $h_{\text{v}}\left(T, \text{low} \ P\right) \cong h_{\text{g}}\left(T\right)$. The $h_{\text{g}}\left(T\right)$ term, when referred to the baseline temperature of $0 \ ^{\circ}\text{C}$ employed for dry air, can be broken down to two terms:
        - The enthalpy of water vapor at such a baseline temperature, i.e. $h_{\text{g}}|_{@T=T_{0}}=2500.9 \ \text{kJ}/\text{kg}$. This value is read, straightforwardly, from the $P-v-T$ tables of water and, as such, it is a reminder that the model being employed is an approximation of the empirical $P-v-T$ relationships.
        - The temperature-dependent term, which is analogous to the specific enthalpy expression for dry air given in {eq}`eq_enthalpy_dry_air`, i.e. $h_{\text{g}}|_{@T\neq{}T_{0}}\left(T\right)=c_{p_{\text{H}_{2}\text{O}}}T \cong 1.82T \ \text{kJ}/\text{kg}$. This temperature-dependent part is a reminder that the model being employed for the water vapor is a perfect-gas model, with a constant $c_{p_{\text{H}_{2}\text{O}}}$ value that coincides with the average value for the $[-10, 50]^{\circ}\text{C}$ range, i.e. $c_{p_{\text{H}_{2}\text{O}}}=\overline{c_{p_{\text{H}_{2}\text{O}}}}|_{@T\in[-10,50]^{\circ}\text{C}}$. Hence, equation {eq}`eq_vapor_enthalpy_approx_numbers` ensues, i.e. $h_{\text{g}}\left(T\right) \cong 2500.9 + 1.82T \ [\text{kJ}/\text{kg}]$. In this expression, the first term provides the value of the isoenthalpic line at $T=T_{0}=0 \ ^{\circ}\text{C}$, and the second one is the term that allows shifting between such a reference line and any other isoenthalpic line in the $[-10, 50]^{\circ}\text{C}$ interval.
- Due to the ideal-gas behaviour of the mixture, the Dalton's law of additive partial pressures is fulfilled.

(specific_relative_humidities)=
## Specific and relative humidities

The effort devoted to the conception of {ref}`the model described <dry_and_atmospheric_air>` has resulted in a set of equations that are simple enough to be solved analytically. However, such a model requires some additional information before beginning the calculations. Indeed, the $P_{\text{v}}$ term present in {eq}`eq_dalton_atmospheric_air` strongly depends on the amount of moisture present in the atmospheric air. So far, however, no comments have been made on how to determine such an amount of moisture. In other words: **how is the water vapor content present in the atmospheric air characterised?**

It turns out that there are two main properties that desribe such an amount. The two of them show similar denominations, and they point towards a notion that is prertty familiar on an everyday basis: **humidity**. Thus, humidity measurements indicate amounts of water vapor present in the air. But there are different ways in which such amounts can be specified. The straightforward one is to refer the mass of water vapor in the air to the mass of dry air. That is the definition of **absolute or specific humidity**, which is symbolised by $\omega$:

```{math}
:label: eq_specific_humidity

\omega = \frac{m_{\text{v}}}{m_{\text{a}}} \ \left[\frac{\text{kg water vapor}}{\text{kg dry air}}\right].
```

If the ideal (perfect) gas model is assumed for both constituents (i.e. dry air and water vapor), then equation {eq}`eq_specific_humidity` can be developed further, yielding:

```{math}
:label: eq_specific_humidity_pres_ratio

\omega = \frac{m_{\text{v}}}{m_{\text{a}}} = \frac{P_{\text{v}}V/R_{\text{v}}T}{P_{\text{a}}V/R_{\text{a}}T} = \frac{P_{\text{v}}/R_{\text{v}}}{P_{\text{a}}/R_{\text{a}}} = 0.622\frac{P_{\text{v}}}{P_{\text{a}}} \ \left[\frac{\text{kg water vapor}}{\text{kg dry air}}\right],
```

where the last equality comes from the fact that the ratio of specific-gas constants results in a constant value, given that $R_{\text{a}}$ and $R_{\text{v}}$ do not vary, i.e. $R_{\text{a}}/R_{\text{v}}=0.622$. Using Dalton's law of additive pressures expressed in equation {eq}`eq_dalton_atmospheric_air`:

```{math}
:label: eq_specific_humidity_pres_ratio_dalton

\omega = \frac{0.622P_{\text{v}}}{P - P_{\text{v}}} \ \left[\frac{\text{kg water vapor}}{\text{kg dry air}}\right],
```

where $P$ in {eq}`eq_specific_humidity_pres_ratio_dalton` stands for the total pressure of the mixture, or the pressure measured by a barometer (easily determined in comparison to the partial pressures).

However, the specific humidity is not the only magnitude that can provide information about how much moisture is present in atmospheric air, nor the best-suited one in some cases. Indeed, $\omega$ is a ratio between two mass quantities, and one may be tempted to draw the wrong conclusion that the amount of water content in atmospheric air can increase without limits. Certainly, and as far as the definition of $\omega$ is concerned, a zero value of specific humidity refers to dry air (i.e. no water content present). Parting from such a value, it is possible to conceive an experiment in which water vapor is gradually incorporated into a container filled with 1 kg of air; the specific humidity would rise accordingly, until reaching a thermodynamic state in which the air can sustain no more moisture. At such a point, the value of $\omega$ would saturate, as adding up more moisture would result in its condensation as liquid water. Hence, even though the mathematical definition of $\omega$ given in equation {eq}`eq_specific_humidity` admits an unbounded increment of the water content present in dry air, such an increment encounters thermo-physical constraints under real situations. That's why it turns relevant to conceive another humidity definition that takes into account such burdens.

The fact that the water present in atmospheric air begins to condense after reaching a threshold value of specific humidity is not independent of the atmospheric air's thermodynamic state. Indeed, it is known that the beginning of the vapor-liquid phase-change is fixed whenever the pressure, or the temperature, are specified. Thus (and resuming the experiment described above), for a given temperature of the atmospheric air, the increasing amounts of moisture that fill up the container will rise the vapor pressure steadily, until reaching the saturation pressure of water that corresponds to such a temperature. At this point, the air is said to be saturated with moisture and, correspondingly, is called **saturated air**; it is the point at which the specific humidity also saturates, as adding up more moisture will condense part of the water present in the air. The saturation value of $\omega$ can be obtained by simply replacing the variable $P_{\text{v}}$ by $P_{\text{g}}$ in equations {eq}`eq_specific_humidity_pres_ratio` or {eq}`eq_specific_humidity_pres_ratio_dalton`, with $P_{\text{g}}$ being the saturation pressure of water for the temperature being considered.

But more important than the amount of moisture content hold by atmospheric air at a given temperature is the fact that such an amount directly affects the comfort level we experience in an environment. However, such a comfort level has more to do with the amount of moisture that air holds (namely, $m_{\text{v}}$ so far) relative to the maximum amount of moisture assumable at the same temperature (i.e. $m_{\text{g}}$, or the moisture content when the air is saturated). The ratio of those two quantities constitutes the second humidity magnitude that is relevant to define, the so-called **relative humidity**, which is symbolysed as **$\phi$**:

```{math}
:label: eq_relative_humidity

\phi = \frac{m_{\text{v}}}{m_{\text{g}}}=\frac{P_{\text{v}}V/R_{\text{v}}T}{P_{\text{g}}V/R_{\text{v}}T}=\frac{P_{\text{v}}}{P_{\text{g}}} \ [-],
```

where, as stated before:

```{math}
:label: eq_saturation_pressure

P_{\text{g}} = P_{\text{sat.}@T} \ [\text{kPa}].
```

If equations {eq}`eq_specific_humidity_pres_ratio_dalton` and {eq}`eq_relative_humidity` are combined, $\omega$ and $\phi$ can be expressed in terms of each other:

```{math}
:label: eq_phi_terms_omega

\phi = \frac{\omega{}P}{\left(0.622 + \omega\right)P_{\text{g}}} \ [-],
```

```{math}
:label: eq_omega_terms_phi

\omega = \frac{0.622\phi{}P_{\text{g}}}{P - \phi{}P_{\text{g}}} \ \left[\frac{\text{kg water vapor}}{\text{kg dry air}}\right].
```

Notice that, although the specific humidity does not show any restriction with respect to the values it can adopt (in principle), the relative humidity is a normalized parameter, i.e. its values fall in the range $\phi\in\left[0, 1\right]$. A value of $\phi=0$ stands for dry air, whereas $\phi=1$ represents saturated air. Likewise, and as stated before, the relative humidity depends on the temperature at which the atmospheric air is specified to be, due to the fact that the saturation pressure of the water depends on such a temperature. As such, it is noteworthy that a shift in temperature may leave the specific humidity unchanged, but that the relative humidity will vary accordingly.

Having presented the definitions of the two main humidities employed for specifying the moisture content of atmospheric air at given conditions, it is due time to relate such moisture quantifications to the remaining property that determines the thermodynamic state of atmospheric air: enthalpy. As long as the atmospheric air is a recognised mixture of dry air and water vapor, its extensive enthalpy will be the sum of the enthalpies of its constituents, i.e.:

```{math}
:label: eq_extensive_enthalpy_atmospheric_air

H = H_{\text{a}} + H_{\text{v}} = m_{\text{a}}h_{\text{a}} + m_{\text{v}}h_{\text{v}} \ [\text{kJ}].
```

In usual practical applications, though, the amount of dry air in the air-water mixture remains constant, and it is the amount of water the magnitude that varies. For that reason, it is convenient to express the enthalpy values **per unit mass of dry air**, instead of doing it per unit mass of air-water mixture. This can be done by expressing equation {eq}`eq_extensive_enthalpy_atmospheric_air` in intensive terms, which is achieved via dividing the expression by $m_{\text{a}}$:

```{math}
:label: eq_intensive_enthalpy_atmospheric_air

h = \frac{H}{m_{\text{a}}} = h_{\text{a}} + \frac{m_{\text{v}}}{m_{\text{a}}}h_{\text{v}} = h_{\text{a}} + \omega{}h_{\text{v}} \cong h_{\text{a}} + \omega{}h_{\text{g}} \ \left[\frac{\text{kJ}}{\text{kg dry air}}\right],
```

where the last equality (i.e. symbolised as $\cong$) results from the fact that $h_{\text{v}} \cong h_{\text{g}}$.

It is to notice that, on the model description of atmospheric air given so far, the temperature employed refers to a temperature that an ordinary thermometer would register when placed on a still atmospheric air. This temperature is called **dry-bulb temperature**, and is different from other thermometric measurements that can be performed upon atmospheric air which, accordingly, will be given different denominations.

(dew_point_temperature)=
## Dew-point temperature

At the {ref}`introductory section of the model description on atmospheric air <describing_model>`, it has been stated that a typical situation in which the water content present in such an air becomes manifest corresponds to the dew drops that show up at the outdoor surfaces during the early morning hours.

With the explanations about the behaviour of the air-water mixture given so far, it is straightforward to describe how such drops are formed: during daytime, a considerable amount of water vaporises due to the warmer temperatures induced by sunlight. Such an increase in temperature rises the saturation pressure of the water vapor and, hence, the atmospheric air can hold a larger amount of moisture within. When the temperatures drop during nighttime, this trend is reversed, reducing the moisture capacity of the atmospheric air due to the lowering of the saturation pressure value. If the thermal drop is considerable, it may eventually reach the saturation temperature of the water vapor at the atmospheric pressure being considered. Beyond such a point, any additional decrease in temperature will cause the moisture in the atmospheric air to condense, and dew drops will show up at the surfaces whose temperature matches the saturation temperature. If the thermal drop happens to fall lower than the freezing point of water, a **frost layer** will be formed instead of dew drops.

Assuming that the above process takes place at a constant atmospheric pressure, the point at which the atmopsheric temperature reaches the saturation temperature  provides a way of determining the relative humidity during any stage of such an isobaric process. Here's how that measurement becomes possible:

- Initially, both the pressure and the temperature of the atmospheric air are measured by means of a barometer and a thermometer. However, assume that neither the partial pressure of the moisture nor the relative humidity are known.
- The air-water mixture is cooled down gradually, keeping the overall pressure constant. This is the process described when explaining the mechanism of dew formation. As neither the dry-air pressure nor the overall pressure change, Dalton's law asserts that the vapor pressure of the moisture remains constant. Hence, the isobaric process being described is a process at $P_{\text{v}}=\text{const}$.
- When the first dew drops are observed to form, the temperature registered by the thermometer marks the saturation temperature for the $P_{\text{v}}$ at which the cooling process is being carried out. In fact, at such a point $P_{\text{v}}=P_{\text{g}}$, as the partial pressure corresponds to the saturation pressure (the air can sustain no more moisture, i.e. it is saturated).
- The $P_{\text{v}}$ value, which was unknown initially, can be determined by going to the $P-v-T$ tables and reading the saturation pressure that corresponds to the temperature at which the first dew drops have formed.
- Likewise, the saturation pressure for the initial temperature can be obtained equally, as the initial temperature has been registered by the thermometer. As the water vapor pressure at the initial state equals the saturation pressure determined when the dew drops have begun to form, the two pressure values present in {eq}`eq_relative_humidity` are known; the relative humidity, $\phi$, can hence be obatined.

The procedure described above corresponds to a set of operations that, given an initial thermodynamic state, determine a unique value for the temperature at which the dew drops are formed. Accordingly, such a temperature can be used as a descriptive indicator of thermodynamic states. Any such descriptor, which is uniquely defined by a set of operations, is what adopts the name of **property** on physical grounds. As such, the mentioned temperature constitutes a thermodynamic property of the air-water mixture, and merits a name different from the **dry-bulb temperature** employed for denoting the more usual measurements of the thermometer used in the experiment. By convention, the newly described property is named the **dew-point temperature**, and is symbolysed by $T_{\text{dp}}$. Its mathematical definition reads:

```{math}
:label: eq_dew_point_temperature

T_{\text{dp}} = T_{\text{sat.}@P_{\text{v}}} \ [^{\circ}\text{C}].
```

(adiabatic_saturation_and_wet_bulb)=
## Two additional temperatures: adiabatic saturation and wet-bulb

(adiabatic_saturation_process)=
### The adiabatic saturation process

{ref}`The procedure described above <dew_point_temperature>` for determining $\phi$ via $T_{\text{dp}}$ may sound straightforward, but is actually quite impractical for a number of reasons:

- It requires a **controlled cooling**, which may be challenging to achieve and maintain during the process.
- The measurement equipment required, such as **dew-point hygrometers** or **chilled mirrors**, are relatively expensive and need regular calibrations due to their sensitiveness to different kinds of contamination.
- It is a **time-consuming** method, since air must be cooled gradually; likewise, each measurement requires a **separate cooling cycle**, which rules out the possibility of performing a **continuous monitoring** of the processes, thus increasing the time-cost of the method.
- **Supercooling can occur, where air cools below its dew point without condensation**, leading to inaccurate readings and experimental errors. Supercooling happens because condensation requires not just low temperatures, but also nucleation sites (like dust particles) for water vapor to condense onto (recall that dew drops are formed at the outdoor surfaces which, as may be deduced, act as nucleation sites). The sensitiveness of the measurement devices to particles other than water (i.e. nucleation sites), and the need for such particles so that condensation occurs effectively are two contradictory requirements.

**Is there another way of determining either the specific or the relative humidity by operational means?** Fortunately, there is. One such process, much more practical than the determination of $T_{\text{db}}$, is the so-called **adiabatic saturation process**. The operations that need to be carried out in order to saturate an air/water mixture adiabatically are the following:

- An experimental device consisting of a long insulated channel is set up. The insulation is required for avoiding any energetic exchange with the environment in the form of heat.
- Liquid water is introduced to the channel from an opening at the bottom, filling the channel until a pool is formed. It is important to leave room in the channel so that air is allowed to enter and exit the device from two additional openings that act as inlet and outlet, respectively.
- The air entering the channel is the atmospheric air whose thermodynamic state is to be determined by means of the adiabatic saturation process. It is assumed that its initial condition is given by the triplet $(T_{1}, \omega_{1}, \phi_{1})$. Additionally, such an air is circulated in a continuous manner, so that the open system constituted by the channel is ensured to operate in a steady state.
- As the stream of unsaturated air flows over the pool of water, some of that water will evaporate and mix with the airstream. As a result, two main thermodynamic processes will be observed in the air/water mixture:
    - The moisture content of air/water mixture will increase steadily, due to the evaporation of some of the surface water in the pool.
    - The temperature of the mixture will drop, as part of the latent heat required to vaporise the water comes from the air.
- If the channel is long enough, the air/water mixture will exit the system as saturated air ($\phi_{2}=1$) at a temperature $T_{2}$, which is called the **adiabatic saturation temperature**. The equilibrium thermodynamic state at the outlet will be determined by the triplet $(T_{2}, \omega_{2}, \phi_{2}=1)$.
- For the overall process to operate under steady-state conditions, the water that is vaporised into the air and, consequently, expelled from the channel must be replaced somehow. The opening employed for forming the pool in the first place must supply such a makeup water, and it must do so at the rate of evaporation at the temperature $T_{2}$ so that a steady-state operation ensues.
- Under such circumstances, the overall process can be assumed to involve no heat or work interactions, nor significant variations of kinetic and potential energies. Hence, the two conservation laws (mass and energy) adopt pretty simple forms for the two-inlet, one-exit steady-flow system described. Indeed:

<center> <b>Mass balances:</b> </center>

<br/>

The mass flow rate of dry air remains constant

```{math}
:label: eq_mass_cons_air_adsat

\dot{m}_{\text{a}_{1}} = \dot{m}_{\text{a}_{2}} = \dot{m}_{\text{a}} \ [\text{kg}/\text{s}]
```

The mass flow rate of vapor in the air increases by an amount equal to the rate of evaporation $\dot{m}_{\text{f}}$.

```{math}
:label: eq_mass_cons_water_adsat

\dot{m}_{\text{w}_{1}} + \dot{m}_{\text{f}} = \dot{m}_{\text{w}_{2}} \hspace{2mm} \implies \hspace{2mm} \dot{m}_{\text{a}}\omega_{1} + \dot{m}_{\text{f}} = \dot{m}_{\text{a}}\omega_{2} \hspace{2mm} \implies \hspace{2mm} \dot{m}_{\text{f}} = \dot{m}_{\text{a}}\left(\omega_{2} - \omega_{1}\right) \ [\text{kg}/\text{s}]
```

<center> <b>Energy balance:</b> </center>

<br/>

There are no heat and work interactions $\left(\dot{Q}=\dot{W}=0\right)$, and the kinetic and potential energy variations are assumed to be negligible $\left(\Delta\dot{E}_{\text{kin.}}=\Delta\dot{E}_{\text{pot.}} \cong 0\right)$, so the only contributions to the energy balance are the enthalpic terms (as it is an open system):
```{math}
:label: eq_energy_cons_adsat

\Delta\dot{H}=0 \hspace{2mm} \implies \hspace{2mm} \dot{H}_{\text{in}} = \dot{H}_{\text{out}} \hspace{2mm} \implies \hspace{2mm} \dot{H}_{1} + \dot{H}_{\text{f}} = \dot{H}_{2} \hspace{2mm} \implies \hspace{2mm} \dot{m}_{\text{a}}h_{1} + \dot{m}_{\text{f}}h_{\text{f}_{2}} = \dot{m}_{\text{a}}h_{2} \ [\text{kJ}].
```

Combining {eq}`eq_mass_cons_water_adsat` and {eq}`eq_energy_cons_adsat` above:

```{math}
:label: eq_energy_cons_spec_adsat

\dot{m}_{\text{a}}h_{1} + \dot{m}_{\text{a}}\left(\omega_{2} - \omega_{1}\right)h_{\text{f}_{2}} = \dot{m}_{\text{a}}h_{2} \hspace{2mm} \overset{/\dot{m}_{\text{a}}}{\implies} \hspace{2mm} h_{1} + \left(\omega_{2} - \omega_{1}\right)h_{\text{f}_{2}} = h_{2} \ [\text{kJ}/\text{kg}].
```

Assuming that a prefect-gas model is applicable to the dry air, so that its enthalpy can be referenced to a $0 \ ^{\circ}\text{C}$ temperature by means of $h_{\text{a}}|_{@T}=c_{p}T$, {eq}`eq_energy_cons_spec_adsat` adopts the form:

```{math}
:label: eq_energy_cons_spec_enthalpy_adsat

\left(c_{p}T_{1} + \omega{}h_{\text{g}_{1}}\right) + \left(\omega_{2} - \omega_{1}\right)h_{\text{f}_{2}} = \left(c_{p}T_{2} + \omega_{2}h_{\text{g}_{2}}\right) \ [\text{kJ}/\text{kg}].
```

The specific humidity at the inlet, $\omega_{1}$, can be obtained from {eq}`eq_energy_cons_spec_enthalpy_adsat`:

```{math}
:label: eq_specific_humidity_adsat

\omega_{1} = \frac{c_{p}\left(T_{2} - T_{1}\right) + \omega_{2}h_{\text{fg}_{2}}}{h_{\text{g}_{1}} - h_{\text{f}_{2}}} \ \left[\frac{\text{kg water vapor}}{\text{kg dry air}}\right],
```

where:
- $h_{\text{g}_{1}}$ is the enthalpy of saturated gas at the inlet temperature $T_{1}$.
- $h_{\text{fg}_{2}}$ is the vaporisation enthalpy of water at the outlet temperature $T_{2}$.
- $h_{\text{f}_{2}}$ is the enthalpy of saturated liquid at the same temperature.
- $\omega_{2}$ is determined from the condition of saturated air at the exit, namely from {eq}`eq_omega_terms_phi` with $\phi_{2}=1$:
```{math}
:label: eq_specific_humidity_exit_adsat

\omega_{2} = \frac{0.622P_{\text{g}_{2}}}{P_{2} - P_{\text{g}_{2}}} \ \left[\frac{\text{kg water vapor}}{\text{kg dry air}}\right]
```

Thus, the above procedure allows calculating the specific humidity $\omega_{1}$ (and, consequently, also the relative humidity $\phi_{1}$) by measuring the pressure and temperature at the inlet and outlet of the channel. That's the reason why these type of channels are called **adiabatic saturators**.

It is noteworthy that the process of adiabatic saturation is different from the one described to explain the phenomena of dew drop formation. Indeed, the process leading to the dew-point temperature has been assumed to occur at a constant partial pressure of the water vapor ($P_{\text{v}}=\text{const.}$), considering that such a partial pressure does not vary much when the system analysed corresponds to the atmosphere. Instead, the process leading to adiabatic saturation takes place in a confined space (the channel or saturator) whereby the progressive increment of the relative humidity rises the partial pressure of the water vapor. **The adiabatic saturation process does not occur at $P_{\text{v}}=\text{const.}$, as happens for the dewing phenomenon**. In general, hence, the two temperatures will not be the same, although both of them constitute properties that determine the thermodynamic state of an air/water mixture.

(wet_bulb_temperature)=
### The wet-bulb device

As occurs with the dew-point determination, the process of adiabatic saturation also shows some disadvantages:

- The channel required to saturate the mixture may be exceedingly long.
- The spraying mechanism to achieve such a saturation may turn too complex to design.

A more practical (and, indeed, employed) approach for determining the humidity of the air/water mixture is by a so-called **wet-bulb thermometer**. These type of devices are similar to the conventional dry-bulb thermometers, but they show the particularity of having their bulb covered with a cotton wick saturated with water. Air is then blown over the wick, and part of the water present in the cotton is evaporated in {ref}`a process identical to the one occurring in an adiabatic saturator <adiabatic_saturation_process>`. In fact, the air/water mixture located in the immediate surroundings of the wick can be assumed to be in a state of saturation. Again, evaporating the water requires energy and, as a result of such an extraction, the temperature of the water drops. This temperature difference constitutes the driving force for the heat transfer between air and water. After a while, the heat loss due to evaporation equals the heat gain from the air, and the temperature of the water stabilises at a given value. Such a temperature is called the **wet-bulb tmeperature**, and is symbolysed by $T_{\text{wb}}$. As mentioned, its easy measurement turns it into the most employed parameter in applications such as air-conditioning.

(psychrometric_chart)=
## The psychrometric chart

As occurs with any other simple system constituted by a gas mixture, **two independent intensive properties** are enough for determining the thermodynamic state of atmospheric air. Once again, that's what the stable equilibrium state principle (or, shortly said, the **state principle**) asserts; in any of such states, the rest of the properties are related to the chosen two by univocal relationships, which allows determining them once that two of those independent intensive variables are specified.

The dimensioning of typical systems involving atmoshperic air, such as **air-conditioning** devices, may require a number of calculations that become cumbersome fast enough. 
