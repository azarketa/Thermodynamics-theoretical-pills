(gas_mixtures)=
# GAS MIXTURES

(notion_of_gas_mixtures)=
## The notion of gas mixtures

The majority of substances in gaseous state found in nature do not comply with the category of "pure substance". Instead, they constitute **mixtures**, or **combinations of different gases**.

So far, the characterization of substances has been done on the premise that they were pure substances. Water has been the paradigm of one such pure substance, with its thermodynamic behaviour being determined by its corresponding $P-v-T$ diagram. The fact that **most gases encountered in engineering applications constitute mixtures**, however, sets forth the necessity of developing an understanding on the topic. The conceptual question that arises, hence, is the following: **how are mixtures characterized**?

It is intuitive to grasp the idea that **the properties of a mixture will depend on the properties of the individual gases** making up the mixture itself. Each of such individual gases is called a **component** or a **constituent** of the mixture. As in the case of water, it is possible to develop $P-v-T$ diagrams and tabulated property-series for mixtures, but **this approach seems quite impractical** at a first sight. Indeed, if those diagrams and tables depend on the composition of the mixture, and **infinitely many of such compositions** can be conceived in principle, that renders the task of elaborating $P-v-T$ diagrams and data-series rather nonsense. Nevertheless, this does not mean that no such data-series exist, nor that all of them can be regarded as useless. **Common mixtures, such as air**, are characterized thusly. For a vast majority of generic mixtures, though, it becomes necessary to develop **rules for determining mixture properties from a knowledge of mixture composition and the properties of individual components**.

(composition_gas_mixture)=
## Composition of a gas mixture: fraction-based analysis

How is the composition of a mixture **described** in terms of its individual components? This question can be answered by adopting two different analytical standpoints: the **molar** one, which specifies the **number of moles** of each component; and the **gravimetric one**, based on the **mass of each constituent**.

Regardless of the standpoint considered, the total number of moles and the toal mass of the mixture, termed $N_{\text{mix.}}$ and $m_{\text{mix.}}$ respectively, constitute **extensive properties** that are additive in each component. Expressed mathematically:

```{math}
:label: eq_total_mass_moles

\displaystyle{m_{\text{mix.}} = \sum_{i=1}^{k}m_{i}} \ \text{[kg]} \hspace{5mm} \text{and} \hspace{5mm} \displaystyle{N_{\text{mix.}} = \sum_{i=1}^{k}N_{i}} \ \text{[mol]} \ .
```

Those two expressions constitute the first descriptive characters of mixtures. They **relate mixture properties** (mass and amount of matter) **to their constituents**. This description can be complemented if the **mass fractions** ($x_{i}$) and **molar fractions** ($y_{i}$) are defined. If the total amount of matter and total mass are properties of the overall mixture, the mentioned fractions correspond to each of the individual components, i.e. they serve the purpose of giving **normalized information** (understood as mixture-relative) about the constituents. Again, mathematically:

\begin{equation*}
    \displaystyle{x_{i} = \frac{m_{i}}{m_{\text{mix.}}} \ [-] \hspace{5mm}} \text{and} \hspace{5mm} \displaystyle{y_{i} = \frac{N_{i}}{N_{\text{mix.}}} \ [-]} \ .
\end{equation*}

Notice that, in the equations above, the subindex $i$ stands for a **generic individual component** of the mixture, and that it is assumed that the mixture itself is constituted by a number $k$ of constituents (with $k\geq1$). The fact that the mass and molar fractions are normalized can be shown by dividing the two sides of the expressions in {eq}`eq_total_mass_moles` by $m_{\text{mix.}}$ and $N_{\text{mix.}}$, respectively:

```{math}
:label: eq_massfrac_normalization

    \displaystyle{1 = \frac{1}{m_{\text{mix.}}}\sum_{i=1}^{k}m_{i} = \sum_{i=1}^{k}\frac{m_{i}}{m_{\text{mix.}}} = \sum_{i=1}^{k}x_{i} \hspace{5mm} \Rightarrow \hspace{5mm} \sum_{i=1}^{k}x_{i} = 1},
```

```{math}
:label: eq_molfrac_normalization

    \displaystyle{1 = \frac{1}{N_{\text{mix.}}}\sum_{i=1}^{k}N_{i} = \sum_{i=1}^{k}\frac{N_{i}}{N_{\text{mix.}}} = \sum_{i=1}^{k}y_{i} \hspace{5mm} \Rightarrow \hspace{5mm} \sum_{i=1}^{k}y_{i} = 1}.
```

Finally, mixtures can be ascribed a **molar weight** ($\text{MW}_{\text{mix.}}$) and a **mixture-specific gas constant** ($R_{\text{mix.}}$) as done with pure gas substances. In the case of mixtures, such parameters constitute a sort of **averaged** cuantities. Expectedly, and given that the molar weight parameter is given in [kg/kmol] units, the averaging operation for calculating the mixture's molar weight must take into account the molar fractions of the constituents. In other words, $\text{MW}_{\text{mix.}}$ is a **molar-fraction-based weight averaged value**:

```{math}
:label: eq_molweight_mixture

    \displaystyle{\text{MW}_{\text{mix.}} = \frac{m_{\text{mix.}}}{N_{\text{mix.}}} = \frac{\sum_{i=1}^{k}m_{i}}{N_{\text{mix.}}} = \frac{\sum_{i=1}^{k}N_{i}\text{MW}_{i}}{N_{\text{mix.}}}=\sum_{i=1}^{k}y_{i}\text{MW}_{i}} \ [\text{kg}/\text{kmol}] .
```

The **mixture-specific gas constant** is obtained from its definition, minding that the molar weight to be considered is the mixture one:

```{math}
:label: eq_R_mixture

    \displaystyle{R_{\text{mix.}} = \frac{\text{R}_{\text{u}}}{\text{MW}_{\text{mix.}}} \ [\text{kJ}/(\text{kg}{\cdot}\text{K})] .}
```

Two final relationships may be of practical use. From the definition of the molar weight for the mixture, it is possible to relate it to the mass fractions, instead of considering the molar ones:

```{math}
:label: eq_molweight_mixture_massfrac

    \displaystyle{\text{MW}_{\text{mix.}}=\frac{m_{\text{mix.}}}{N_{\text{mix.}}}=\frac{m_{\text{mix.}}}{\sum_{i=1}^{k}\frac{m_{i}}{\text{MW}_{i}}} = \frac{1}{\sum_{i=1}^{k}\frac{m_{i}}{(m_{\text{mix.}}\text{MW}_{i})}} = \frac{1}{\sum_{i=1}^{k}\frac{x_{i}}{\text{MW}_{i}}} \ [\text{kg}/\text{kmol}]}.
```

The fact that $\text{MW}_{\text{mix.}}$ can be written in terms of either $x_{i}$ or $y_{i}$ indicates that the two fractions (molar and mass) are related. Indeed, such a relationship can be obtained from the definition of the molar fraction, considering that the mass can be expressed as the product of the molar weight and the number of moles. Thus:

```{math}
:label: eq_frac_relation

    \displaystyle{x_{i}=\frac{m_{i}}{m_{\text{mix.}}}=\frac{N_{i}\text{MW}_{i}}{N_{\text{mix.}}\text{MW}_{\text{mix.}}}=y_{i}\frac{\text{MW}_{i}}{\text{MW}_{\text{mix.}}} \ [-]}.
```

(pvt_behaviour)=
## $P-v-T$ behaviour of ideal gas mixtures

Ideal gases constituted by pure substances are known to behave as such under two main assumptions: negligible intermolecular forces between the gas particles, and negligible volume occupied by the particles with respect to the total volume. Those conditions are amply fulfilled at low pressures (particles sufficiently uncompressed and, hence, moving freely enough so that their aggregated volume is little in comparison to the container volume) and high temperatures (particles moving fast enough so that their kinetic energy turns the effect of intermolecular forces unimportant). Hence:

```{math}
:label: eq_ideal_gas_conditions

    \lim_{P\to0}P \hspace{2mm} \& \hspace{2mm} \lim_{T\to\infty}T \hspace{2mm} \implies \hspace{2mm} \text{ideal-gas model.}
```

Under such conditions, the most simple state-equation model that is known to relate the stable thermodynamic equilibrium properties of a gas corresponds to the well-known expression:

```{math}
:label: eq_ideal_gas_state_equation

    Pv=R_{\text{gas}}T \ [\text{kJ}/\text{kg}].
```

Notice that {eq}`eq_ideal_gas_state_equation`, insofar it relates the properties $P$, $v$ and $T$ with each other, codifies the $P-v-T$ relation of a substance. The information it provides is equivalent to the one gathered in tabular form for substances other than ideal gases, such as water. The upshot is that, whereas an easy mathematical expression cannot be found for the latter substances, the tabulated data can also be interpreted as codifying a sort of discretized $P-v-T$ relationship. Either with substances that can be modeled as ideal gases, or with those that manifest such a broader behaviour that must be asserted by other means, the two models employed (ideal-gas state-equation in the former; $P-v-T$ diagrams in the latter) are of the form $f(P, v, T)=0$. That is: they represent homogeneous functions of three variables (whichever complicated) in which every point of the surface represents a state of thermodynamic equilibrium. In fact, that's what the stable-state principle claims in the case of simple systems: it suffices with two independent intensive thermodynamic variables for fixing the overall (equilibrium) thermodynamic state of a system. 

That being said, and resuming the topic on gas mixtures, the ideal-gas behaviour can be equally assumed with the caveat that, in this case, **dissimilar molecules** exist in the substance considered. In addition to the low-pressures and high-temperatures conditions expressed in {eq}`eq_ideal_gas_conditions`, two other assumptions are necessary for making an ideal-gas-mixture model consistent: that the constituents of the mixture are nonreacting (i.e. that no chemical reactions occur within the mixture), and that the behaviour of the molecules of a constituent is not influenced by the presence of dissimilar molecules corresponding to the other components of the mixture. Hence:

```{math}
:label: eq_ideal_gas_mixture_state_equation

\begin{align}    
  \left.
  \begin{array}{r}
  \displaystyle{\lim_{P\to0}P \hspace{2mm} \& \hspace{2mm} \lim_{T\to\infty}T} \\
  \\
  \text{nonreacting} \\
  \\
  \text{dissimilar molecules} \\ \text{not affecting} \\ \text{each other}
  \end{array}
  \right\} &  \implies \text{ideal-gas-mixture model} \hspace{1mm} \implies \hspace{1mm} P_{\text{mix.}}V_{\text{mix.}} = N_{\text{mix.}}\text{R}_{\text{u}}T_{\text{mix.}} \ [\text{kJ}].
\end{align}
```

Notice that {eq}`eq_ideal_gas_mixture_state_equation` has been written in extensive terms (i.e. in [kJ], unlike {eq}`eq_ideal_gas_state_equation`, which is intensive and is written in [kJ/kg]). That's because the properties involved are those that correspond to the mixture itself ($P_{\text{mix.}}$, $V_{\text{mix.}}$...) which is the other relevant difference with respect to {eq}`eq_ideal_gas_state_equation`.

In cases where two intensive properties of the overall mixture are given as known data, determining the equilibrium thermodynamic states of the mixture becomes as trivial as dealing with pure substance ideal gases. However: what about the situations in which the composition of the mixture is provided, without specifying two of the independent variables required for determining the mixture properties? How can one deal with mixture descriptions in that case? In other words: is it possible to relate the overall mixture properties to the compositional information of the individual gases?

Fortunately, it turns out that the answer to the last question is affirmative, and can be solved out with a rather simple model when dealing with mixtures behaving as ideal gases. Two empirical laws constitute the basics of such a model:

- **Dalton's law of additive pressures**: _the pressure of a gas mixture is equal to the sum of the pressures each gas would exert **if it existed alone at the mixture temperature and volume**_.

    ```{math}
    :label: eq_Daltons_law
    
        \text{Dalton's law:} \hspace{5mm}  P_{\text{mix.}} = \sum_{i=1}^{k}P_{i}\left(T_{\text{mix.}}, V_{\text{mix.}}\right) \ [\text{Pa}].
    ```

- **Amagat's law of additive volumes:** _the volume of a gas mixture is equal to the sum of the volumes each gas would occupy **if it existed alone at the mixture temperature and pressure**_.

    ```{math}
    :label: eq_Amagats_law
    
        \text{Amagat's law:} \hspace{5mm}  V_{\text{mix.}} = \sum_{i=1}^{k}V_{i}\left(T_{\text{mix.}}, P_{\text{mix.}}\right) \ [\text{m}^{3}].
    ```

Equations {eq}`eq_Daltons_law` and {eq}`eq_Amagats_law` may sound intuitive due to their knowledge from previous courses on Physics and Chemistry, but they do not own a readily interpretable physical basis on their own. The fact that the contributions of individual pressures and volumes sum up to the overall pressure and volume of the mixture is far from being a straightforward idea; in fact, the validity of such laws has been sanctioned by means of empirical observations and, thus, they heavily rely on laboratory experiments. What's more: under the scope of the present course on Thermodynamics, and insofar the basic model being assumed is the ideal-gas one, the relationships {eq}`eq_Daltons_law` and {eq}`eq_Amagats_law` may be said to hold exactly. But it is noteworthy that they do so under the exclusive assumptions made in {eq}`eq_ideal_gas_mixture_state_equation`. Thus, although describing and modeling real gases lies out of the scope of the present course, it is necessary to state that the mentioned laws are **merely approximate** in the latter case, mainly due to the intermolecular forces acting upon the dissimilar molecules comprised in the mixture.

Presenting some specific terminology regarding the Dalton's and Amagat's laws is deemed necessary before proceeding. Thus:

- The variables $P_{i}$ and $V_{i}$ present in those laws are termed, respectively, **component pressure** and **component volume** of constituent $i$.

- Just as occurs with the mass and mole fractions, the ratios $P_{i}/P_{\text{mix.}}$ and $V_{i}/V_{\text{mix.}}$ are called, respectively, **pressure fraction** and **volume fraction** of constituent $i$.

Notice that, as {eq}`eq_Daltons_law` and {eq}`eq_Amagats_law` are not obtained by assuming an ideal-gas behaviour of the mixture, the terminology introduced above serves equally well for both ideal and real gases. Indeed, it is one thing to state that Dalton's and Amagat's laws hold exactly for ideal-gases, and another one to claim that such laws can only be applied to such gases. Although approximate, {eq}`eq_Daltons_law` and {eq}`eq_Amagats_law` can (and are) employed with real gases and, hence, the component-wise pressures and volumes (as well as the fractions) are valid for both models of a gas.

Instead, if the theoretical standpoint is restricted to ideal-gases, it turns possible to go further when it comes to the relationships between the component pressures and volumes (i.e. $P_{i}$ and $V_{i}$) and the overall pressure and volume (that is, $P_{\text{mix.}}$ and $V_{\text{mix.}}$). Indeed, one may write the following expressions for the pressure and volume fractions:

\begin{equation*}
    \displaystyle{\frac{P_{i}\left(T_{\text{mix.}}, V_{\text{mix.}}\right)}{P_{\text{mix.}}} = \frac{N_{i}\text{R}_{\text{u}}T_{\text{mix.}}/V_{\text{mix.}}}{N_{\text{mix.}}\text{R}_{\text{u}}T_{\text{mix.}}/V_{\text{mix.}}} = \frac{N_{i}}{N_{\text{mix.}}} = y_{i} \ [-] \ ,}
\end{equation*}

\begin{equation*}
    \displaystyle{\frac{V_{i}\left(T_{\text{mix.}}, P_{\text{mix.}}\right)}{V_{\text{mix.}}} = \frac{N_{i}\text{R}_{\text{u}}T_{\text{mix.}}/P_{\text{mix.}}}{N_{\text{mix.}}\text{R}_{\text{u}}T_{\text{mix.}}/P_{\text{mix.}}} = \frac{N_{i}}{N_{\text{mix.}}} = y_{i} \ [-] \ .}
\end{equation*}

Therefore, for ideal-gas mixtures exclusively:

```{math}
:label: eq_partial_pressures_volumes_moles

    \frac{P_{i}}{P_{\text{mix.}}} = \frac{V_{i}}{V_{\text{mix.}}} = \frac{N_{i}}{N_{\text{mix.}}} = y_{i} \ [-] \ .
```

The terminology, in this case, changes a little. Instead of using the terms **pressure component** and **volume component**, the quantities $P_{i}=y_{i}P_{\text{mix.}}$ and $V_{i}=y_{i}V_{\text{mix.}}$ that can be derived from {eq}`eq_partial_pressures_volumes_moles` are called **partial pressure** and **partial volume** of constituent $i$. It is noteworthy that, when assuming an ideal-gas behaviour for the mixture, Dalton's and Amagat's laws provide the same relative information about the constituents. In other words: the relationships between the overall properties and the individual ones are independent of the empirical operations considered, which constitutes an experimental oddity itself. In fact, it is known that, for real gases, Amagat's law provides more accurate results than Dalton's law. Such differences, however, do not ensue when the ideal-gas simplification is made.

Likewise, it is relevant to notice that the molar fractions are involved in the relationships between the overall and individual properties. This fact corroborates the character of fundamental magnitude endowed to the amount of substance, as it emerges as a surrogate extensive property relating the intensive properties required for determining the thermodynamic equilibrium state of a mixture system. Again, this also asserts the relevance of the mass and molar fraction analyses introduced before.

Lastly, it is remarkable that the ideal-gas model unifies the terminology employed so far. Indeed, talking about **mole fractions**, **pressure fractions** and **volume fractions** is equivalent for an ideal-gas mixture; in the same sense, the notions of **component pressure** and **partial pressure**, as well as **component volume** and **partial volume**, are identical.

(properties_ideal_gases)=
## Properties of ideal gas mixtures

With the {ref}`compositional notions desribed so far <composition_gas_mixture>`, together with the $P-v-T$ behaviour introduced in {ref}`the previous section <pvt_behaviour>`, it turns possible to present a simple way of evaluating both **extensive** and **intensive properties** of ideal-gas mixtures.

The relationships for the extensive properties are straighforward to obtain. Indeed, they come from summing up the contributions of the individual components. Skipping the trivial magnitudes of mass and amount of substance (already presented in {eq}`eq_total_mass_moles`), the rest of relevant properties read:

```{math}
:label: eq_internal_energy_mixture

    U_{\text{mix.}} = \sum_{i=1}^{k}U_{i} = \sum_{i=1}^{k}m_{i}u_{i} = \sum_{i=1}^{k}N_{i}\overline{u}_{i} \ [\text{kJ}] \ ,
```

```{math}
:label: eq_enthalpy_mixture

    H_{\text{mix.}} = \sum_{i=1}^{k}H_{i} = \sum_{i=1}^{k}m_{i}h_{i} = \sum_{i=1}^{k}N_{i}\overline{h}_{i} \ [\text{kJ}] \ ,
```

```{math}
:label: eq_entropy_mixture

    S_{\text{mix.}} = \sum_{i=1}^{k}S_{i} = \sum_{i=1}^{k}m_{i}s_{i} = \sum_{i=1}^{k}N_{i}\overline{s}_{i} \ [\text{kJ}/\text{K}] \ .
```

Notice that three expressions are given for each of the extensive properties considered above.

- The second term on the equations is expressed in terms of the individual contributions of such a property from the constituents (i.e. $U_{i}$, $H_{i}$ or $S_{i}$).

- The third term is a summatory over the mass-weighted contributions of the intensive, specific properties of the constituents (i.e. $u_{i}$, $h_{i}$ or $s_{i}$). As such, those **specific properties are expressed in terms of [kJ/kg]** (for the internal energy or the enthalpy) or **[kJ/kg·K]** (entropy). The product of such intensive, specific properties with the mass of each constituent, and the subsequent summation over the constituents, provides an extensive property.

- The last term is a summatory over the molar-weighted contributions of the intensive, molar properties of the constituents (i.e. $\overline{u}_{i}$, $\overline{h}_{i}$ or $\overline{s}_{i}$). As such, those **molar properties are expressed in [kJ/kmol]** (for the internal energy or the enthalpy) or **[kJ/kmol·K]** (entropy). The product of such intensive, molar properties with the number of moles of each constituent, and the subsequent summation over the constituents, provides an extensive property.

The expressions in {eq}`eq_internal_energy_mixture`, {eq}`eq_enthalpy_mixture` and {eq}`eq_entropy_mixture` are equally valid when considering **extensive property differences**. Thus:

```{math}
:label: eq_internal_energy_difference_mixture

    \Delta{}U_{\text{mix.}} = \sum_{i=1}^{k}\Delta{}U_{i} = \sum_{i=1}^{k}m_{i}\Delta{}u_{i} = \sum_{i=1}^{k}N_{i}\Delta{}\overline{u}_{i} \ [\text{kJ}] \ ,
```

```{math}
:label: eq_enthalpy_difference_mixture

    \Delta{}H_{\text{mix.}} = \sum_{i=1}^{k}\Delta{}H_{i} = \sum_{i=1}^{k}m_{i}\Delta{}h_{i} = \sum_{i=1}^{k}N_{i}\Delta{}\overline{h}_{i} \ [\text{kJ}] \ ,
```

```{math}
:label: eq_entropy_difference_mixture

    \Delta{}S_{\text{mix.}} = \sum_{i=1}^{k}\Delta{}S_{i} = \sum_{i=1}^{k}m_{i}\Delta{}s_{i} = \sum_{i=1}^{k}N_{i}\Delta{}\overline{s}_{i} \ [\text{kJ}/\text{K}] \ .
```

The approach is rather different when considering **intensive properties**, although it does not depart much from the averaging scheme presented in {eq}`eq_molweight_mixture`, i.e.: the intensive properties of the mixture are obtained either by mass-averaging the specific properties of each constituent (via mass fractions) or, alternatively, by molar-averaging the molar properties of each constituent (via molar fractions). Thus:

```{math}
:label: eq_specific_molar_internal_energy_mixture

    u_{\text{mix.}} = \sum_{i=1}^{k}x_{i}u_{i} \ [\text{kJ}/\text{kg}] \hspace{2mm} \text{;} \hspace{2mm} \overline{u}_{\text{mix.}} = \sum_{i=1}^{k}y_{i}\overline{u}_{i} \ [\text{kJ}/\text{kmol}] \ ,
```

```{math}
:label: eq_specific_molar_enthalpy_mixture

    h_{\text{mix.}} = \sum_{i=1}^{k}x_{i}h_{i} \ [\text{kJ}/\text{kg}] \hspace{2mm} \text{;} \hspace{2mm} \overline{h}_{\text{mix.}} = \sum_{i=1}^{k}y_{i}\overline{h}_{i} \ [\text{kJ}/\text{kmol}] \ ,
```

```{math}
:label: eq_specific_molar_entropy_mixture

    s_{\text{mix.}} = \sum_{i=1}^{k}x_{i}s_{i} \ [\text{kJ}/\text{kg}] \hspace{2mm} \text{;} \hspace{2mm} \overline{s}_{\text{mix.}} = \sum_{i=1}^{k}y_{i}\overline{s}_{i} \ [\text{kJ}/\text{kmol}{\cdot}\text{K}] \ .
```

And the same can be said about the specific heats that, together with the specific mixture constant defined in {eq}`eq_R_mixture`, close the description of the thermodynamic properties of ideal gas mixtures.

```{math}
:label: eq_cv_mixture

    c_{v,\text{mix.}} = \sum_{i=1}^{k}x_{i}c_{v,i} \ [\text{kJ}/\text{kg}{\cdot}\text{K}] \hspace{2mm} \text{;} \hspace{2mm} \overline{c}_{v,\text{mix.}} = \sum_{i=1}^{k}y_{i}\overline{c}_{v,i} \ [\text{kJ}/\text{kmol}{\cdot}\text{K}]
```

```{math}
:label: eq_cp_mixture

    c_{p,\text{mix.}} = \sum_{i=1}^{k}x_{i}c_{p,i} \ [\text{kJ}/\text{kg}{\cdot}\text{K}] \hspace{2mm} \text{;} \hspace{2mm} \overline{c}_{p,\text{mix.}} = \sum_{i=1}^{k}y_{i}\overline{c}_{p,i} \ [\text{kJ}/\text{kmol}{\cdot}\text{K}]
```

(example_problems)=
## Example problems: computing properties of mixtures

```{note}
An underlying idea behind the development of this manual has been the motivation to show the potential of scientific programming languaages for solving engineering problems. Complying with the philosophy of open-source code, it has been decided to show such a potential by providing the programming-based solutions to showcase problems via [Python{sup}`TM`](https://www.python.org/) scripts. The ultimate purpose is to induce the readers of the manual to download either a standard Python interpreter or a popular distribution (the one recommended is the community version of the [Anaconda distribution](https://www.anaconda.com/download)), and to try to reproduce the results shown herein on their own. Furthermore, the readers that decide to give a try to the code-based methodology are also compelled to play with the scripts, modifying the data given in the problem statements and challenging themselves to develop both customised and enhanced versions of the scripts provided.
```

Whoever has used Python should be familiar with the usual workflow when writing a code script:

- Typically, the first command lines are devoted to **importing the packages** (libraries) that will expectedly be used within the main code blocks.
- Afterwards, it is usual to define the values of the variables that will be constant along the code. The definition of any variable in a coding block is termed, in programming jargon, as **declaring a variable**, which is why this second step may be termed as **declaring the constants**.
- Next, the programmer writes down (codifies) all the logic that constitutes the solving procedure of the problem. In other words, it **develops the problem-specific algorithms**, including the **declaration of output variables** that will constitute the outcome of the code for the post-processing stage.
- The following step is to **run or execute the code**, which may include several iterative steps of debugging in case errors are found during the execution.
- Finally, the results are **post-processed and shown in the format specified by the user** (direct result display, figures...).

A flowchart may serve the purpose of illustrating the above procedure more clearly:

(flowchart_coding)=
:::{mermaid}
graph LR
  A[Importing packages];
  B[Declaring constants];
  C[Developing problem-specific algorithms];
  D[Running the code];
  E{Errors found?};
  F[Post-processing];
  
  A --> B
  B --> C
  C --> D
  D --> E
  E --> |Yes| C
  E --> |No| F
:::

The two code blocks shown below correspond, respectively, to the former steps shown in the flowchart. They have been rendered before the problem-specific algorithms developed in the test problems, as they constitute common code blocks for all of them.

:::{card}

**Package-importing code-block**
^^^

```{code} python
:linenos:
    
#####
##### Importing packages
#####

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl    
```

+++
**End of code-block**
:::

:::{card}

**Constant-variables declaration code-block**
^^^

```{code} python
:linenos:

#####
##### Problem-independent (constant) data.
#####

# Common (universal) data.
R_u = 8.31447

# Data for nitrogen.
MW_N2 = 28
cp_N2 = 1.039
cv_N2 = 0.743

# Data for oxygen.
MW_O2 = 32
cp_O2 = 0.918
cv_O2 = 0.658
```

+++
**End of code-block**
:::

The code-blocks above are written at the beginning of the scripts or, when using a [Jupyter Notebook](https://jupyter.org/), they can be coded in the first code-cells and run once. The code-blocks shown in the test problems below correspond to problem-specific algorithms, and they refer to the rightmost steps described in the {ref}`previous flowchart <flowchart_coding>`.

(properties_of_air)=
### Test problem 1

::::{card} 

**Computing the properties of air**
^^^
Assuming air at atmospheric pressure and 300 K to be composed of 79% of $\text{N}_{2}$ and 21% of $\text{O}_{2}$ (in a volumetric basis), and knowing the following data:

- Common (universal) data.
    - $\text{R}_{\text{u}} = 8.314 \ [\text{kJ}/\text{kmol}{\cdot}\text{K}]$ .

- $\text{N}_{2}$:
    - $\text{MW}_{\text{N}_2} = 28 \ [\text{kg}/\text{kmol}]$ ,
    - $c_{p,\text{N}_{2}} = 1.039 \ [\text{kJ}/\text{kg}{\cdot}\text{K}]$ ,
    - $c_{v,\text{N}_{2}} = 0.743 \ [\text{kJ}/\text{kg}{\cdot}\text{K}]$ .

- $\text{O}_{2}$:
    - $\text{MW}_{\text{O}_2} = 32 \ [\text{kg}/\text{kmol}]$ ,
    - $c_{p,\text{O}_{2}} = 0.918 \ [\text{kJ}/\text{kg}{\cdot}\text{K}]$ ,
    - $c_{v,\text{O}_{2}} = 0.658 \ [\text{kJ}/\text{kg}{\cdot}\text{K}]$ ,

calculate the mass and molar fractions of air, as well as its molar weight and specific heats (consider that the mixture behaves as an ideal gas). Compare the computed data with the data provided in tables for the nitrogen-oxygen mixture tabulated as "_Air_".

:::{card}

**Input code-block:**
^^^

```{code} python
:linenos:

#####
##### Problem-specific data.
#####

# Data for nitrogen.
v_frac_N2 = 0.79

# Data for oxygen.
v_frac_O2 = 0.21

#####
##### Mixture calculations.
#####

# By virtue of equation (14).
y_N2 = v_frac_N2 
y_O2 = v_frac_O2

# By virtue of equation (7).
MW_air = y_N2*MW_N2 + y_O2*MW_O2

# By virtue of equation (8).
x_N2 = y_N2*(MW_N2/MW_air)
x_O2 = y_O2*(MW_O2/MW_air)

# Checking mass and molar fraction normalizations (equations (3) and (4)).
if y_N2 + y_O2 == 1 and x_N2 + x_O2 == 1:
    print("Mass and molar fractions correctly computed")
    print("-----")
    print(f"y_N2 = {y_N2} [-]")
    print(f"y_O2 = {y_O2} [-]")
    print("-----")
    print(f"x_N2 = {np.round(x_N2, 3)} [-]")
    print(f"x_O2 = {np.round(x_O2, 3)} [-]")
    
# By virtue of equation (6).
R_air = R_u/MW_air

# By virtue of equations (24) and (25).
cp_air = x_N2*cp_N2 + x_O2*cp_O2
cv_air = x_N2*cv_N2 + x_O2*cv_O2

print("-------------------")
print("Mixture properties")
print("-----")
print(f"MW_air = {np.round(MW_air, 3)} [kg/kmol]")
print(f"R_air = {np.round(R_air, 3)} [kJ/kg·K]")
print(f"cp_air = {np.round(cp_air, 3)} [kJ/kg·K]")
print(f"cv_air = {np.round(cv_air, 3)} [kJ/kg·K]")

#####
##### Comparing with tabulate data.
####

# Reading air data from tables.
MW_air_table = 28.97
R_air_table = 0.287
cp_air_table = 1.005
cv_air_table = 0.718

# Computing the errors.
delta_MW = 100*(MW_air - MW_air_table)/MW_air_table
delta_R = 100*(R_air - R_air_table)/R_air_table
delta_cp = 100*(cp_air - cp_air_table)/cp_air_table
delta_cv = 100*(cv_air - cv_air_table)/cv_air_table
print("-------------------")
print("Differences with tabulated data")
print("-----")
print(f"Err. in MW = {np.round(delta_MW, 3)} [%]")
print(f"Err. in R = {np.round(delta_R, 3)} [%]")
print(f"Err. in cp = {np.round(delta_cp, 3)} [%]")
print(f"Err. in cv = {np.round(delta_cv, 3)} [%]")
```

+++
**End of input code-block**
:::

:::{card}

**Code output:**
^^^

    Mass and molar fractions correctly computed
    -----
    y_N2 = 0.79 [-]
    y_O2 = 0.21 [-]
    -----
    x_N2 = 0.767 [-]
    x_O2 = 0.233 [-]
    -------------------
    Mixture properties
    -----
    MW_air = 28.84 [kg/kmol]
    R_air = 0.288 [kJ/kg·K]
    cp_air = 1.011 [kJ/kg·K]
    cv_air = 0.723 [kJ/kg·K]
    -------------------
    Differences with tabulated data
    -----
    Err. in MW = -0.449 [%]
    Err. in R = 0.452 [%]
    Err. in cp = 0.578 [%]
    Err. in cv = 0.723 [%]
    
+++
**End of code output**
:::

```{note}
As observed, the calculation of molar and mass fractions does not pose any difficulties. Neither does the computation of the mixture properties, although certain differences are observed when comparing the obtained values with tabulated data. The sources of those errors may be traced down to two main factors:

- The fact that the assumed mixture composition is not identical to the one employed for computing the tabulated data. In fact, standard atmospheric air is not constituted by $\text{N}_{2}$ and $\text{O}_{2}$ exclusively, although such gases prevail in amount. However, tiny fractions of other constituents (argon, for instance) may play a significant role when comparing the data obtained with the simplified air composition with the real one.

- Rounding errors during the computations may also affect the final results, although this source is presumably playing a minor role compared to the compositional one.
```

+++
**End of Test Problem 1**
::::

(inverted_air)=
### Test problem 2

::::{card} 

**Computing the properties of inverted air**
^^^

Assume the same thermodynamic scenario as in the {ref}`previous problem <properties_of_air>`, but inverting the volume percentages of the constituents. Calculate the molar and mass fractions of this mixture, termed as "_inverted air_" herein, as well as its mixture properties. Compare them to the results obtained previously.

:::{card}

**Input code-block:**
^^^

```{code} python
:linenos:

#####
##### Problem-specific data.
#####

# Data for nitrogen.
v_frac_N2_inv = 0.21

# Data for oxygen.
v_frac_O2_inv = 0.79

#####
##### Mixture calculations.
#####

# By virtue of equation (14).
y_N2_inv = v_frac_N2_inv
y_O2_inv = v_frac_O2_inv

# By virtue of equation (7).
MW_air_inv = y_N2_inv*MW_N2 + y_O2_inv*MW_O2

# By virtue of equation (8).
x_N2_inv = y_N2_inv*(MW_N2/MW_air_inv)
x_O2_inv = y_O2_inv*(MW_O2/MW_air_inv)

# Checking mass and molar fraction normalizations (equations (3) and (4)).
if y_N2_inv + y_O2_inv == 1 and x_N2_inv + x_O2_inv == 1:
    print("Mass and molar fractions correctly computed")
    print("-----")
    print(f"y_N2_inv = {y_N2_inv} [-]")
    print(f"y_O2_inv = {y_O2_inv} [-]")
    print("-----")
    print(f"x_N2_inv = {np.round(x_N2_inv, 3)} [-]")
    print(f"x_O2_inv = {np.round(x_O2_inv, 3)} [-]")
    
# By virtue of equation (6).
R_air_inv = R_u/MW_air_inv

# By virtue of (24) and (25).
cp_air_inv = x_N2_inv*cp_N2 + x_O2_inv*cp_O2
cv_air_inv = x_N2_inv*cv_N2 + x_O2_inv*cv_O2

print("-------------------")
print("Mixture properties")
print("-----")
print(f"MW_air_inv = {np.round(MW_air_inv, 3)} [kg/kmol]")
print(f"R_air_inv = {np.round(R_air_inv, 3)} [kJ/kg·K]")
print(f"cp_air_inv = {np.round(cp_air_inv, 3)} [kJ/kg·K]")
print(f"cv_air_inv = {np.round(cv_air_inv, 3)} [kJ/kg·K]")

delta_MW = 100*(MW_air_inv - MW_air)/MW_air
delta_R = 100*(R_air_inv - R_air)/R_air
delta_cp = 100*(cp_air_inv - cp_air)/cp_air
delta_cv = 100*(cv_air_inv - cv_air)/cv_air
print("-------------------")
print("Differences with standard, simplified air")
print("-----")
print(f"Err. in MW = {np.round(delta_MW, 3)} [%]")
print(f"Err. in R = {np.round(delta_R, 3)} [%]")
print(f"Err. in cp = {np.round(delta_cp, 3)} [%]")
print(f"Err. in cv = {np.round(delta_cv, 3)} [%]")
```

+++
**End of input code-block**
:::

:::{card}

**Code output:**
^^^

    Mass and molar fractions correctly computed
    -----
    y_N2_inv = 0.21 [-]
    y_O2_inv = 0.79 [-]
    -----
    x_N2_inv = 0.189 [-]
    x_O2_inv = 0.811 [-]
    -------------------
    Mixture properties
    -----
    MW_air_inv = 31.16 [kg/kmol]
    R_air_inv = 0.267 [kJ/kg·K]
    cp_air_inv = 0.941 [kJ/kg·K]
    cv_air_inv = 0.674 [kJ/kg·K]
    -------------------
    Differences with standard, simplified air
    -----
    Err. in MW = 8.044 [%]
    Err. in R = -7.445 [%]
    Err. in cp = -6.922 [%]
    Err. in cv = -6.797 [%]
    
+++
**End of code output**
:::    

```{note}
Notice that, in this case, the molar weight has increased considerably. This makes sense insofar the molar weight of the mixture is a weighted average of the individual weights. The weights of the averaging are the molar fractions and, compared with the standard air composition, the inverted case owns a much larger molar fraction for oxygen than for nitrogen. Hence, the molar weight of the mixture will lie closer to the constituent whose molar fraction is higher (notice that, in case the mixture is equilibrated in its composition, the molar weight (as well as all the other properties) will match the arithmetic averages of the individual components' values). Indeed, the deviation from the standard air's value is of 8%, which is remarkable.

The same reasoning can be applied for the mixture's specific heats. Insofar they constitute weighted averages of the individual constituents' values, they will tend to lie closer to the constituent whose mass-fraction is higher (not the molar one in this case). Given that the specific heat values of $\text{O}_{2}$ are lower than those of $\text{N}_{2}$, the resulting mixture values also lie lower than in the standard case.

The fact that the specific gas constant for the mixture, $R_{\text{mix.}}$, is lower than in the standard case is a consequence of the molar weight being higher. Indeed, the specific gas constant is obtained as a division between the universal gas constant and the molar weight of the mixture.
```

+++
**End of Test Problem 2**
::::

(plotting_composition_properties)=
### Test Problem 3

::::{card} 

**Plotting composition-dependent properties**
^^^

Now assume that the volumetric composition of the mixture is variable, being possible to change it from 10% to 90% for both components. Obviously, there is a constraint in the values that the volumetric percentages of the constituents can adopt, as they must sum up to 100%: if the volumetric percentage of $\text{O}_{2}$ is of 10%, this means that the one of $\text{N}_{2}$ is of 90%, and _vice versa_.

Plot the composition-dependent mass and molar fractions against the volumetric percentage of $\text{N}_{2}$ present in the mixture, as well as the mixture's molar weight and specific constants.

:::{card}

**Input code-block:**
^^^

```{code} python
#####
##### Problem-specific data.
#####

# Data for nitrogen.
v_frac_N2_vars = np.linspace(0.1, 0.9, 9)

# Data for oxygen.
v_frac_O2_vars = 1 - v_frac_N2_vars

y_N2_vars = np.zeros(len(v_frac_N2_vars))
y_O2_vars = np.zeros(len(v_frac_N2_vars))
x_N2_vars = np.zeros(len(v_frac_N2_vars))
x_O2_vars = np.zeros(len(v_frac_N2_vars))
MW_air_vars = np.zeros(len(v_frac_N2_vars))
R_air_vars = np.zeros(len(v_frac_N2_vars))
cp_air_vars = np.zeros(len(v_frac_N2_vars))
cv_air_vars = np.zeros(len(v_frac_N2_vars))

#####
##### Mixture calculations.
#####

# Looping over the different volumetric percentages.
for idx, v_frac_N2_var in enumerate(v_frac_N2_vars):

    # By virtue of (14).
    y_N2_vars[idx] = v_frac_N2_vars[idx]
    y_O2_vars[idx] = v_frac_O2_vars[idx]

    # By virtue of (7).
    MW_air_vars[idx] = y_N2_vars[idx]*MW_N2 + y_O2_vars[idx]*MW_O2

    # By virtue of (8)
    x_N2_vars[idx] = y_N2_vars[idx]*(MW_N2/MW_air_vars[idx])
    x_O2_vars[idx] = y_O2_vars[idx]*(MW_O2/MW_air_vars[idx])

    # By virtue of (6).
    R_air_vars[idx] = R_u/MW_air_vars[idx]

    # By virtue of (24) and (25).
    cp_air_vars[idx] = x_N2_vars[idx]*cp_N2 + x_O2_vars[idx]*cp_O2
    cv_air_vars[idx] = x_N2_vars[idx]*cv_N2 + x_O2_vars[idx]*cv_O2
    
# Plotting.

# Getting default colors.
colors = mpl.rcParams['axes.prop_cycle'].by_key()['color']

#####
##### First figure.
#####
plt.figure()
plt.plot(v_frac_N2_vars, y_N2_vars, marker='o', color=colors[0], label="$y_{N_{2}}$")
plt.plot(v_frac_N2_vars, y_O2_vars, marker='o', color=colors[1], label="$y_{O_{2}}$")
plt.plot(v_frac_N2_vars, x_N2_vars, marker='o', color=colors[0], linestyle='--', label="$x_{N_{2}}$")
plt.plot(v_frac_N2_vars, x_O2_vars, marker='o', color=colors[1], linestyle='--', label="$x_{O_{2}}$")

plt.grid()
plt.legend(frameon=False, ncols=2)
plt.xlabel("$v_{N_{2}} \\ [-]$")
plt.ylabel("$y , x \\ [-]$")

#####
##### Second figure.
#####
plt.figure()
plt.plot(v_frac_N2_vars, MW_air_vars, marker='o', color=colors[0])
plt.grid(color=colors[0], axis='y')
plt.grid(axis='x')
plt.xlabel("$v_{N_{2}} \\ [-]$")
plt.ylabel("$MW_{air} \\ [kg/kmol]$")
plt.gca().spines['left'].set_color(colors[0])
plt.gca().yaxis.label.set_color(colors[0])
plt.gca().tick_params(axis='y', colors=colors[0])

plt.twinx()
plt.plot(v_frac_N2_vars, R_air_vars, marker='o', color=colors[1], label="$R_{air}$")
plt.plot(v_frac_N2_vars, cp_air_vars, marker='o', color=colors[1], linestyle='--', label="$c_{p,air}$")
plt.plot(v_frac_N2_vars, cv_air_vars, marker='o', color=colors[1], linestyle=':', label="$c_{v,air}$")
plt.legend(frameon=False)
plt.grid(color=colors[1], axis='y')
plt.ylabel("$R_{air} , c_{p,air}, c_{v,air} \\ [kg/kmol·K]$")
plt.gca().spines['right'].set_color(colors[1])
plt.gca().yaxis.label.set_color(colors[1])
plt.gca().tick_params(axis='y', colors=colors[1])

plt.show()
```

+++
**End of input code-block**
:::

:::{card}

**Code output**
^^^

(fig_1)=
```{image} Fig1.svg
:width: 700px
```

(fig_2)=
```{image} Fig2.svg
:width: 700px
```

+++
**End of code output**
:::

```{note}
Observing the figures above, notice how:

- The molar fractions vary linearly along the considered interval: the molar fraction of $\text{N}_{2}$ increases linearly, and the one of $\text{O}_{2}$ decreases accordingly, thus fulfilling the normalization constraint of adding up to 1.

- The evolution of the mass fractions is slightly different, as they show a slight bending on their linear tendency, resembling more to parabolic shapes. This is due to the fact that the mass fractions are computed by multiplying the molar fractions with the ratio of the molar weight of the constituent to the molar weight of the mixture (see equation {eq}`eq_frac_relation`). As both the molar fraction and the molar weight of the mixture follow linear trends (as observed in the second figure), a difference in their slopes results in a tendency for the mass fractions that departs slightly from a straight line.

- The mixture constants increase steadily throughout the considered interval, and they do so linearly (the counteracting parabolic trends of the mass fractions entering the computation of the weighted averages for the $c_{p}$ and $c_{v}$ cases cancel each other out, leading to a linear trend instead).
```

+++
**End of Test Problem 3**
::::
