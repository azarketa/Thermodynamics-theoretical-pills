(sec_models_gases)=
## Ideal and real Gases

Modeling gases is one of the key aspects of Thermodynamics. Gases differ by composition and molecular structure — air, carbon monoxide, hydrogen, methane, butane, or ethanol vapor all behave differently.
However, under suitable conditions, all gases exhibit comparable patterns that can be captured through mathematical models.

This section first develops the **ideal gas model**, valid at low pressures and high temperatures, and then introduces **real-gas models** that extend predictive accuracy under dense or cold conditions. A quantitative example illustrates their differences. The intensive variables used here connect directly to {ref}`the previous section <sec_characterization_substances>`, and the final forms satisfy {ref}`the general state relation eq_general_state_equation`.

---

(subsec_ideal_gas_assumptions)=
### Assumptions of the ideal gas model

The **ideal gas model** rests on two simplifying postulates:

1. **Negligible molecular volume.**
   Molecules occupy a negligibly small portion of the total volume. This approximation is sound at **low pressures**.

2. **Negligible intermolecular forces.**
   Intermolecular attractions and repulsions are disregarded. This is reasonable at **high temperatures**, where kinetic energy dominates.

:::{admonition} Important: validity of the ideal gas approximation
:class: warning
The ideal gas model describes gases under the limit of low density and high temperature, where molecular interactions vanish.
In this regime, all gases behave similarly, regardless of their chemical nature.
:::

---

(subsec_ideal_gas_equation)=
### The ideal gas equation

The relationship among pressure, volume, temperature, and amount of substance is expressed by the **ideal gas law**.

(eq_ideal_gas_molar_form)=
$$
P{}V = n{}R_u{}T
$$

where

* $P$ is the absolute pressure ($\text{Pa}$),
* $V$ is the volume ($\text{m}^3$),
* $n$ is the amount of substance ($\text{mol}$),
* $T$ is the absolute temperature ($\text{K}$), and
* $R_u = 8.314 \ [\text{J}/(\text{mol}\cdot\text{K})]$ is the universal gas constant.

The **specific gas constant** $R$ is

(eq_specific_gas_constant)=
$$
R = \frac{R_u}{M}
$$

where $M$ is the molar mass ($\text{kg}/\text{mol}$). Since $M = m/n$, the **mass form** follows as

(eq_ideal_gas_mass_form)=
$$
P{}V = m{}R{}T
$$

Dividing by mass $m$ yields the **specific form**

(eq_ideal_gas_specific_form)=
$$
P{}v = R{}T
$$

where $v = V/m$ is the specific volume ($\text{m}^3/\text{kg}$).

:::{admonition} Note: relation to the state postulate
:class: note, dropdown
The relation $P{}v = R{}T$ connects the three intensive variables introduced in {ref}`the previous section <sec_characterization_substances>` and is a particular realization of {ref}`the generic state relation <eq_general_state_equation>`.
:::

---

(subsec_real_gases)=
### Real gases and deviations from ideal behavior

When gases are compressed or cooled, their behavior departs from that predicted by the ideal gas law. These deviations occur because real molecules **occupy finite space** and **exert forces** on each other — effects neglected in the ideal model. To quantify such departures, we introduce the **compressibility factor**:

(eq_compressibility_factor)=
$$
Z = \frac{P{}v}{R{}T}
$$

For an ideal gas, $Z = 1$. If $Z < 1$, attractive interactions dominate; if $Z > 1$, repulsive effects prevail. The compressibility factor thus provides a compact, dimensionless measure of real-gas deviation.

:::{admonition} Note: the meaning of $Z$
:class: note, dropdown
The compressibility factor $Z$ quantifies how far a real gas deviates from the ideal law under a given combination of $P$ and $T$.
Plotting $Z$ versus $P$ for several gases at various temperatures reveals a common trend —
they all approach $Z=1$ at low pressure, showing that ideal-gas behavior is the limiting case of real gases.
:::

---

(subsec_reduced_variables)=
### Critical properties and reduced variables

Experimental studies show that every substance exhibits a **critical point** beyond which the distinction between liquid and vapor disappears. This point is defined by three characteristic magnitudes: the **critical pressure** $P_c$, **critical temperature** $T_c$, and **critical specific volume** $v_c$.

These values are experimentally measurable and provide a natural reference frame for comparing substances.
Although the detailed meaning of “critical point” will be addressed later,
we can already define the **reduced variables**:

(eq_reduced_variables)=
$$
T_r = \frac{T}{T_c}, \qquad P_r = \frac{P}{P_c}, \qquad v_r = \frac{v}{v_c}
$$

Expressing thermodynamic relationships in terms of $(T_r, P_r, v_r)$ makes the behavior of different gases **comparable on a universal basis**, which is the essence of the **law of corresponding states**.

:::{admonition} Tip: law of corresponding states
:class: tip, dropdown
When data for various gases are plotted in terms of the reduced variables $(T_r, P_r, v_r)$, their compressibility curves collapse onto nearly the same surface. This empirical observation implies that the thermodynamic behavior of gases is fundamentally governed by non-dimensional ratios, not by their absolute properties.
:::

---

(subsec_cubic_models)=
### Classical and modern real gas models

While $Z$ serves as an excellent descriptor of real-gas behavior, we still need **explicit equations** linking $P$, $v$, and $T$ to calculate states and processes.
To this end, several **semi-empirical EOS** have been developed. These equations modify the ideal gas law by including corrective terms
for **finite molecular volume** and **intermolecular attractions**.

:::{admonition} Note: why cubic equations appear
:class: note, dropdown
When the ideal gas law is corrected by one term proportional to $1/v^2$ (to model attractions) and another that subtracts a finite volume $b$ (to model repulsions),
the resulting expression becomes **cubic in specific volume** $v$. That is why most classical EOS — van der Waals, Redlich–Kwong, Peng–Robinson —
belong to the family of **cubic EOS**. They are the simplest algebraic forms capable of reproducing the experimentally observed S-shaped $P$–$v$ curves
near phase transitions while remaining solvable in closed form.
:::

* **The van der Waals Equation**

  The first equation introducing both types of molecular corrections:

  (eq_vanderwaals)=
  $$
  \bigl(P + a{}\tfrac{n^{2}}{V^{2}}\bigr)\bigl(V - n{}b\bigr) = n{}R_u{}T
  $$

  where:

  * $a$ corrects for *intermolecular attractions*,
  * $b$ corrects for *finite molecular size*.

  When $a = b = 0$, the ideal gas law is recovered.

* **The Redlich–Kwong Equation**

  An improvement introducing a temperature-dependent attraction term:

  (eq_redlich_kwong)=
  $$
  P = \frac{R_u{}T}{V_m - b} - \frac{a}{T^{1/2}{}V_m{}(V_m + b)}
  $$

  This model performs well for moderate pressures and high temperatures
  and remains algebraically simple.

* **The Peng–Robinson Equation**

  Developed to improve accuracy near the critical and liquid regions:

  (eq_peng_robinson)=
  $$
  P = \frac{R_u{}T}{V_m - b} - \frac{a\alpha(T)}{V_m(V_m + b) + b(V_m - b)}
  $$

  with:
  * $\alpha(T) = [1 + \kappa(1 - \sqrt{T/T_c})]^2$,
  * $\kappa = 0.37464 + 1.54226\omega - 0.26992\omega^2$,
  * and $\omega$ the **acentric factor** of the gas.

  The Peng–Robinson model is particularly effective for calculating vapor–liquid equilibria
  and is widely used in engineering thermodynamics.

:::{admonition} Note: comparative accuracy
:class: note, dropdown

* **van der Waals** — qualitative but oversimplified.
* **Redlich–Kwong** — improved temperature behavior, moderate accuracy.
* **Peng–Robinson** — high accuracy across vapor–liquid regions and near the critical point.

Each of these equations can later be expressed in terms of the compressibility factor $Z$
for cross-comparison and connection to theoretical expansions.
:::

---

(subsec_virial_equation)=
### The Virial EOS

Although cubic models offer practical engineering correlations, a more fundamental theoretical approach emerges from **statistical mechanics**, where the pressure of a gas is expanded in powers of density. This leads to the **Virial EOS**, expressed in terms of the compressibility factor:

(eq_virial_expansion)=
$$
Z = 1 + \frac{B(T)}{v} + \frac{C(T)}{v^{2}} + \frac{D(T)}{v^{3}} + \cdots
$$

The coefficients $B(T)$, $C(T)$, and $D(T)$ are known as the **Virial coefficients**,
each corresponding to increasingly complex molecular interactions:

* $B(T)$ — pairwise interactions,
* $C(T)$ — three-body interactions,
* $D(T)$ — four-body and higher effects.

At large $v$ (low density), the higher-order terms vanish, and the ideal gas law is recovered. At moderate densities, the first few terms suffice to capture real-gas deviations.

:::{admonition} Note: connection with cubic equations
:class: note, dropdown

Expanding any cubic EOS — van der Waals, Redlich–Kwong, or Peng–Robinson — for small pressures ($P_r \ll 1$) or large specific volumes yields a **Virial-type series**. In that limit, the constants $a$ and $b$ from those cubic models can be expressed in terms of the Virial coefficients $B(T)$ and $C(T)$. Therefore, the Virial equation represents the **universal low-pressure limit** of all real-gas models.

In engineering practice, the series is often truncated after the first correction term:

(eq_virial_first_order)=
$$
Z \approx 1 + \frac{B(T)}{v}
$$

Substituting into the ideal gas law yields:

(eq_virial_pressure_correction)=
$$
P \approx \frac{R{}T}{v}\left(1 + \frac{B(T)}{v}\right)
$$

This **first-order Virial approximation** provides a convenient correction for real-gas effects at moderate pressures while remaining computationally simple.

The truncated Virial expansion is accurate at **low to moderate pressures**, where intermolecular interactions are limited to short-range effects.

At higher pressures or near the critical point, cubic equations such as Peng–Robinson offer better accuracy and thermodynamic consistency.
:::

:::{admonition} Note: the meaning and origin of the word *Virial*
:class: note, dropdown

The word **“Virial”** comes from the Latin term *vis*, meaning *force* or *strength*. It was first introduced by the German physicist **Rudolf Clausius** in 1870
in the context of his studies on the mechanical theory of heat. Clausius used the expression *“virialis”* to denote the *energy associated with molecular forces*,
and from it he formulated what is now known as the **Virial Theorem**.

In essence, the Virial theorem relates the **average kinetic energy** of the molecules in a system to the **average potential energy** arising from their mutual interactions. From this mechanical relationship, Clausius derived a connection between microscopic forces and macroscopic pressure — a link that later gave birth to the **Virial EOS**, which expresses the pressure of a gas as a power series in density.

So the term *Virial* refers to the “force-energy content” (*vis*) of a system, not to variance or series expansion. Each coefficient in the Virial equation represents the cumulative effect of molecular forces: two-body, three-body, and higher interactions. Thus, the name emphasizes the mechanical origin of the equation — it is fundamentally a **force-derived** expression of state.
:::

---

::::{card}
**WORKED EXAMPLE — pressure and compressibility of $\text{CO}_2$ at $300 \ \text{K}$**
^^^

**Problem statement**

Determine the **pressure** and the **compressibility factor** $Z$ for **carbon dioxide** under specified thermodynamic conditions, using both **ideal** and **real gas models**. The gas occupies a **molar volume** of $V_m = 0.01 \ \text{m}^3/\text{mol}$ and is held at a **temperature** of $T = 300 \ \text{K}$. This corresponds to a near-critical condition for $\text{CO}_2$, making it a meaningful case for evaluating model fidelity.

The following models are considered:

1. Ideal Gas
2. van der Waals
3. Redlich–Kwong
4. Peng–Robinson
5. Virial (first-order approximation)
6. Virial (second-order approximation)

**Synthesis**

Different gas models are applied for computing the pressure of a mole of $\text{CO}_{2}$ that occupies a $0.01 \ \text{m}^{3}$ volume at a temperature of $T = 300 \ \text{K}$.

---

**Problem data**{cite}`weast1972handbook, mit_virial`

| Quantity               |                   Symbol                  |                    Value                   |
| :--------------------- | :---------------------------------------: | :----------------------------------------: |
| Temperature            |                    $T$                    |               $300 \ \text{K}$               |
| Molar volume           |                   $V_m$                   |        $0.01 \ \text{m}^3/\text{mol}$        |
| Universal gas constant |                   $R_u$                   | $8.314 \ \text{J}/(\text{mol}\cdot\text{K})$ |
| $a$ (vdW–RK–PR)        |                    $a$                    | $0.364 \ \text{Pa}{\cdot}\text{m}^6/\text{mol}^2$ |
| $b$ (vdW–RK–PR)        |                    $b$                    | $4.27\times10^{-5} \ \text{m}^3/\text{mol}$ |
| Critical temperature   |                   $T_c$                   |              $304.2 \ \text{K}$              |
| Critical pressure      |                   $P_c$                   |         $7.38\times10^6 \ \text{Pa}$         |
| Acentric factor        |                  $\omega$                 |                   $0.225$                  |
| **2nd Virial coefficient** (at $300 \ \text{K}$) | $B$ | $-121.5\times10^{-6} \ \text{m}^3/\text{mol}$ |
| **3rd Virial coefficient** (at $300 \ \text{K}$) | $C$ |  $5.2\times10^{-9} \ \text{m}^6/\text{mol}^2$ |

---

1. **Computing Reduced Properties**

(eq_example_reduced_props)=
$$
T_r = \frac{T}{T_c} = 0.986,
\qquad
P_r = \frac{P}{P_c}.
$$

Because $P$ is to be determined, $P_r$ will be evaluated separately for each model.

---

2. Calculating Model Predictions

    * **Ideal Gas Model**
    
        (eq_example_ideal_gas)=
        $$
        \boxed{P = \frac{R_u{}T}{V_m} = 2.49\times10^{5} \ \text{Pa}} \ ,
        $$
        
        $$
        \boxed{Z = \frac{P{}V_m}{R_u{}T} = 1.000} \ .
        $$

    ---

    * **van der Waals Equation**
    
        (eq_example_vdw)=
        $$
        \boxed{P = \frac{R_u{}T}{V_m - b} - a{}\frac{1}{V_m^2}
        = 2.13\times10^{5} \ \text{Pa}} \ ,
        $$
        
        $$
        \boxed{Z = \frac{P{}V_m}{R_u{}T} = 0.857} \ .
        $$

    ---
   
    * **Redlich–Kwong Equation**
    
        (eq_example_rk)=
        $$
        \boxed{P = \frac{R_u{}T}{V_m - b} - \frac{a}{T^{1/2}{}V_m(V_m + b)} = 2.20\times10^{5} \ \text{Pa}} \ ,
        $$
        
        $$
        \boxed{Z = 0.885} \ .
        $$

    ---
   
    * **Peng–Robinson Equation**
    
        (eq_example_pr)=
        $$
        P =
        \frac{R_u{}T}{V_m - b} = \frac{a\alpha(T)}{V_m(V_m + b) + b(V_m - b)},
        $$
        
        where:
        
        $$
        \alpha(T) = [1 + \kappa(1 - \sqrt{T/T_c})]^2,
        \qquad
        \kappa = 0.37464 + 1.54226\omega - 0.26992\omega^2.
        $$
        
        Numerically:
        
        $$
        \boxed{P = 2.25\times10^{5} \ \text{Pa}} \ ,
        $$
      
        $$
        \boxed{Z = 0.905} \ .
        $$

    ---
    
    * **Virial Equation (First-Order Approximation)**
        
        (eq_example_virial)=
        $$
        \boxed{P = \frac{R_u{}T}{V_m}{}\left(1 + \frac{B}{V_m}\right) = 2.47\times10^{5}{} \ \text{Pa}} \ ,
        $$
        
        $$
        \boxed{Z = 1 + \frac{B}{V_m} = 0.994} \ .
        $$

   ---

   * **Virial Equation (Second-Order Approximation)**

        (eq_example_virial2)=
        $$
        \frac{C}{V_m^{2}} = \frac{5.2\times10^{-9}}{(0.01)^2} = 5.2\times10^{-5},
        $$
        
        $$
        \boxed{Z = 1 - 0.01215 + 5.2\times10^{-5} = 0.98790} \ ,
        $$
        
        $$
        \boxed{P = \frac{R_u{}T}{V_m}{}Z \approx 2.4642\times10^{5}{}\text{Pa}} \ .
        $$


---

3. **Reduced-Pressure Evaluation**

    (eq_example_reduced_pressure)=
    $$
    P_r = \frac{P}{P_c}.
    $$
    
    | Model           |      $P$ [$\text{Pa}$]      |  $Z$  |  $P_r$ | $\Delta{}P$ [%] vs Peng-Robinson |
    | :-------------- | :----------------: | :---: | :----: | :----------: |
    | Ideal Gas       | $2.49{\times}10^5$ | 1.000 | 0.0337 |     +10.7    |
    | van der Waals   | $2.13{\times}10^5$ | 0.857 | 0.0288 |     −5.3     |
    | Redlich–Kwong   | $2.20{\times}10^5$ | 0.885 | 0.0298 |     −2.2     |
    | Peng–Robinson   | $2.25{\times}10^5$ | 0.905 | 0.0305 |      0.0     |
    | Virial (1-term) | $2.47{\times}10^5$ | 0.994 | 0.0335 |     +9.8     |
    | Virial (2-term) | $2.4642{\times}10^5$ | 0.98790 | 0.0334 | +9.5 |

---

:::{admonition} Tip: interpretation
:class: tip, dropdown

At $T_r \approx 0.99$, $\text{CO}_2$ lies close to its critical region.

* The **ideal gas model** overestimates pressure by about 10 %, since it neglects molecular attractions.

* The **van der Waals model** underestimates it slightly, as it overcorrects for cohesion.

* **Redlich–Kwong** and **Peng–Robinson** capture both repulsion and attraction more accurately, with the latter providing the best agreement.

* Finally, the **Virial model** nearly reproduces the ideal-gas prediction — a clear indication that it is reliable mainly at low pressures, where intermolecular forces become negligible.

* The one-term Virial approximation reduces the ideal-gas pressure only slightly (to $Z{}\approx{}0.988$), still **overestimating** by $\sim 9.5%$ vs **Peng–Robinson**. Adding the **third virial term** changes $Z$ by only $5.2\times10^{-5}$, so the two-term Virial approximation is practically identical here.

* Near-critical curvature of the $P$–$v$–$T$ surface is captured much better by **cubic EOS** (Redlich-Kwong/Peng-Robinson) than by **low-order Virial truncations**.
:::

+++
END OF WORKED EXAMPLE
::::

---

(subsec_conceptual_closure_gases)=
### Conceptual closure

* The **ideal gas law** ($P{}v = R{}T$) describes the low-density limit and satisfies {ref}`the generic state relation <eq_general_state_equation>`.
* **Real-gas** behavior requires corrections for finite size and interactions — via {ref}`van der Waals <eq_vanderwaals>`, {ref}`Redlich–Kwong <eq_redlich_kwong>`, {ref}`Virial <eq_virial_equation>`, and {ref}`Peng–Robinson <eq_peng_robinson>`.
* For broad engineering conditions, **Peng–Robinson** typically offers the best accuracy–simplicity balance; **Redlich–Kwong** is a solid lighter-weight alternative.
* Truncated **virial** forms remain valuable for dilute gases but are not the most accurate at moderate densities or near phase boundaries.

---

(subsec_references_ideal_and_real_gases)=
### References
```{bibliography}
:filter: docname in docnames
