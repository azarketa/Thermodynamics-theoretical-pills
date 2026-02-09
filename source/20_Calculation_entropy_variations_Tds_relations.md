(sec_entropy_variations_Tds_relations)=
## Calculation of entropy variations and the $T\mathrm{d}s$ relations

Having established the **definition of entropy** as $\mathrm{d}S = (\delta Q/T)_{\text{int.,rev.}}$, we now turn to how this property **changes between two equilibrium states**. Quantifying entropy variations is essential because it lets us

* identify **irreversibility** in real processes,
* measure the **energy degradation** associated with heat transfer, and
* evaluate **efficiency limits** for engines and refrigerators.

To do so, we need relationships that link $\delta Q$ and $T$ to measurable properties of the system. These are the **$T\mathrm{d}s$ relations**, which express the $2^{\text{nd}}$ law in differential, calculable form.

---

(subsec_Tds_relations)=
### Derivation of the $T\mathrm{d}s$ relations

We begin with a **closed, stable, internally reversible system**. This configuration isolates the essential thermodynamic mechanisms: since the mass remains constant, only **heat** and **boundary work** cross the boundary.

For such a system, the $1^{\text{st}}$ law gives

$$
\mathrm{d}E = \delta Q_{\text{int.,rev.}} - \delta W_{\text{int.,rev.,out.}}.
$$

Neglecting macroscopic kinetic and potential energy changes, $\mathrm{d}E = \mathrm{d}U$, and hence

$$
\mathrm{d}U = \delta Q_{\text{int.,rev.}} - \delta W_{\text{int.,rev.,out.}}.
$$

Because the process is internally reversible, we can substitute
$\delta Q_{\text{int.,rev.}} = T\mathrm{d}S$ and $\delta W_{\text{int.,rev.,out.}} = p\mathrm{d}V$, obtaining

(eq_Tds_internal_energy)=
$$
\begin{gather*}
\mathrm{d}U = T{}\mathrm{d}S - p{}\mathrm{d}V, \\[10pt]
\mathrm{d}u = T{}\mathrm{d}s - p{}\mathrm{d}v
\end{gather*}
$$

This is the **first $T\mathrm{d}s$ relation**, in both extensive and specific forms.

Introducing the **enthalpy**, $h = u + Pv$, differentiating, then substituting $\mathrm{d}U = T{}\mathrm{d}S - p{}\mathrm{d}V$ gives

(eq_Tds_enthalpy)=
$$
\begin{gather*}
T{}\mathrm{d}S = \mathrm{d}H- V{}\mathrm{d}p, \\[10pt]
T{}\mathrm{d}s = \mathrm{d}h - v{}\mathrm{d}p.
\end{gather*}
$$

Together, these yield the fundamental **$T\mathrm{d}s$ relations** which, usually, are written in specific form:

(eq_Tds_relations)=
$$
\boxed{
\begin{gather*}
T\mathrm{d}s &= \mathrm{d}u + p\mathrm{d}v, \\[10pt]
T\mathrm{d}s &= \mathrm{d}h - v\mathrm{d}p.
\end{gather*}
}
$$

:::{important}

**SCOPE OF THE CLOSED-SYSTEM FORMULATION**

The closed-system approach isolates the relationship between **energy** and **entropy** in its simplest form. For **open systems**, the same $T\mathrm{d}s$ relations hold **locally**, but an additional term must be included to account for **entropy transported by mass flow**. This extension leads to the **steady-flow energy and entropy equations** used in turbomachinery and heat exchangers.
:::

---

(subsec_entropy_variation_model)=
### Entropy variations depending on substance model

The evaluation of entropy changes depends on how the **working substance** behaves. Since the $T\mathrm{d}s$ relations are general, their practical use requires specifying the **substance model** — whether an **ideal gas**, a **perfect gas**, or a **real (pure) substance**. Each case involves a different relation between $p$, $v$, and $T$, and thus a distinct expression for the entropy variation.

(subsubsec_entropy_variation_ideal_gas)=
### Entropy variation of ideal gases

For an **ideal gas**,

$$
\begin{gather*}
pv = RT, \\[10pt]
\mathrm{d}u = c_v(T)\mathrm{d}T, \\[10pt]
\mathrm{d}h = c_p(T)\mathrm{d}T.
\end{gather*}
$$

Substituting these into the $Tds$ relations gives:

$$
\begin{gather*}
\mathrm{d}s = c_v(T)\frac{\mathrm{d}T}{T} + R\frac{\mathrm{d}v}{v}, \\[10pt]
\mathrm{d}s = c_p(T)\frac{\mathrm{d}T}{T} - R\frac{\mathrm{d}p}{p}.
\end{gather*}
$$

Integrating between two states $(1)$ and $(2)$:

(eq_entropy_ideal_gas)=
$$
\boxed{
\begin{gather*}
s_2 - s_1 = \int_{T_1}^{T_2}\frac{c_v(T)}{T}\mathrm{d}T + R\ln\frac{v_2}{v_1}, \\[10pt]
s_2 - s_1 = \int_{T_1}^{T_2}\frac{c_p(T)}{T}\mathrm{d}T - R\ln\frac{p_2}{p_1}.
\end{gather*}
}
$$

The first form applies when specific volumes are known, and the second when pressures are known. They are equivalent through the ideal-gas law.

:::{note}

**INTERPRETATION OF THE INTEGRAL**

The integral term $\displaystyle \int \frac{c(T)}{T}\mathrm{d}T$ represents the **entropy change due to temperature variation**, while the logarithmic term captures the **effect of expansion or compression**.
:::

(subsubsec_entropy_variation_perfect_gas)=
#### Entropy variation of perfect gases

If the specific heats are constant ($c_p$, $c_v = \text{const.}$), the integrations become analytical:

(eq_entropy_perfect_gas)=
$$
\boxed{
\begin{gather*}
s_2 - s_1 &= c_v \ln\frac{T_2}{T_1} + R\ln\frac{v_2}{v_1}, \\[10pt]
s_2 - s_1 &= c_p \ln\frac{T_2}{T_1} - R\ln\frac{p_2}{p_1}.
\end{gather*}
}
$$

These **logarithmic forms** are widely employed for air and combustion gases under moderate conditions.

(subsubsec_entropy_variation_pure_substances)=
#### Entropy variation of pure substances

When the working substance does **not behave as an ideal gas**, the analytical forms derived above no longer apply. For **pure substances** such as water or refrigerants, entropy values must be obtained from **thermodynamic property tables** or **experimental correlations**.

Since entropy $s$ is a **state property**, its value is determined uniquely once **two independent intensive variables** are fixed (e.g., $T$ and $p$), as stated by the **state postulate**. Accordingly, $s$ can be tabulated in the same way as $u$, $h$, or $v$.

Thus, for real substances, entropy variations are computed by reading $s_1$ and $s_2$ directly from the tables or interpolating between nearby states.

:::{important}

**SUMMARY OF ENTROPY VARIATION CALCULATIONS**

| **Model / Substance type** | **Specific-heat behavior** | **Entropy expression**           | **Integration / Data source** |
| :------------------------- | :------------------------- | :------------------------------- | :---------------------------- |
| **Ideal gas**              | $c_p(T)$, $c_v(T)$         | Integral form                    | Requires $c(T)$ correlation   |
| **Perfect gas**            | Constant $c_p$, $c_v$      | Logarithmic form                 | Direct analytical integration |
| **Pure substance**         | Non-ideal / tabulated      | $s(T,p)$ or $s(T,v)$ from tables | Empirical / interpolated      |
:::

---

(subsec_the_isentropic_condition)=
### The isentropic condition

Before exploring the mathematical form of isentropic relations, it is essential to clarify the physical meaning of the **isentropic condition** itself.
A process is said to be *isentropic* when it proceeds without any **entropy change**.

Such transformations represent the **ideal reference limit** for real compressions and expansions, especially in gases, turbines, compressors, or nozzles. By applying the $T\mathrm{d}s$ relations to a **perfect gas**, the isentropic condition provides analytical connections among pressure, temperature, and specific volume that describe how these magnitudes evolve when entropy remains constant. These relations will later serve as the foundation for evaluating the performance of devices and cycles where adiabatic, nearly reversible behavior is a valid approximation.

A process is called **isentropic** when the **net entropy change of the system is zero**:

$$
\Delta S_{\text{sys.}} = 0
$$

This condition simply means that, between the initial and final equilibrium states, the **total entropy content** of the system remains unchanged — although energy may still be exchanged in various forms.

Entropy within a system can change for two distinct reasons:

1. **Entropy transfer** due to **heat exchange** across the system boundary.
2. **Entropy generation** due to **irreversibilities** within the system (such as friction, mixing, or finite temperature differences).

Mathematically, this can be expressed as:

$$
\Delta S_{\text{sys.}} = \Delta S = \int \frac{Q}{T} + S_{\text{gen.}} = \Delta S_{\text{transf.}} + S_{\text{gen.}},
$$

where $S_{\text{gen.}} \ge 0$ represents the entropy generated internally.

The **simplest way** to achieve $\Delta S = 0$ is to enforce **adiabaticity** ($ Q = 0$) *and* **reversibility** ($S_{\text{gen.}} = 0$). In this case, neither heat crosses the boundary nor entropy is produced inside, and the process remains truly isentropic. This combination defines the **ideal isentropic process** — the one typically used in the analysis of turbines, compressors, and nozzles.

However, **adiabatic and reversible** is only **one possible route** to isentropy, not the only one. Other combinations can, under special conditions, also yield $\Delta S = 0$:

* A **non-adiabatic but irreversible** process can be isentropic if the entropy increase due to irreversibility is *exactly balanced* by an entropy loss through heat transfer.
* Likewise, a **non-adiabatic and reversible** process is generally *not* isentropic, since entropy is exchanged with the surroundings even without generation.

:::{important}

**THE ROUTES TO ISENTROPIC CONDITION**

| **Type of process**                    | **Adiabatic?** | **Reversible?** | **Isentropic?**  | **Comments**                                                          |
| :------------------------------------- | :------------- | :-------------- | :--------------- | :-------------------------------------------------------------------- |
| Adiabatic + Reversible                 | Yes            | Yes             | Yes              | Ideal isentropic (no heat, no generation).                            |
| Non-adiabatic + Irreversible           | No             | No              | Yes (special case) | Possible if  $\Delta S_{\text{transf.}} + S_{\text{gen.}} = 0$. |
| Adiabatic + Irreversible               | Yes            | No              | No                | Entropy generated internally.                                         |
| Non-adiabatic + Reversible             | No             | Yes             | No                | Entropy exchanged with surroundings.                                  |
| Non-adiabatic + Irreversible (general) | No             | No              | No                | Most real processes fall here.                                        |

:::

Hence, **isentropic $\neq$ adiabatic + reversible**, although that is the **most direct and idealized path**.
An isentropic process is, in essence, one where **the total entropy balance is zero**, regardless of the mechanism by which that balance is achieved.

---

(subsec_closed_form_relations_ideal_gases)=
### Closed-form relations for ideal gases

With the **isentropic condition** clarified ($\Delta S_{\text{sys}}=0$), the most practical route to analytical formulas is the **adiabatic + reversible** case. For ideal gases this leads, via the $T\mathrm{d}s$ relations, to **closed-form power laws** linking $T$, $p$, and $v$. These expressions are invaluable in sizing and benchmarking **turbines, compressors, and nozzles**, because they give state-to-state changes without path integration—provided we can model the gas as **perfect** (constant $c_p$, $c_v$, hence constant $\gamma$). When $c_p(T)$ and $c_v(T)$ vary (ideal gas, not perfect), the same condition holds but the relations require **temperature integrals** rather than simple power laws.

For deriving such closed-form relations, we start from the **perfect-gas** differential forms (constant $c_p$, $c_v$; $R=c_p-c_v$) and either of the $T\mathrm{d}s$ relations:

1. Using $(T,v)$:

    $$
    \mathrm{d}s = c_v\frac{\mathrm{d}T}{T} + R\frac{\mathrm{d}v}{v}.
    $$

    Isentropic condition $\mathrm{d}s=0$ gives

    $$
    c_v\frac{\mathrm{d}T}{T} = -R\frac{\mathrm{d}v}{v}.
    $$
    
    Integrate from $(1)$ to $(2)$:

    $$
    c_v\ln\frac{T_2}{T_1} = -R\ln\frac{v_2}{v_1}.
    $$
    
    Using $\displaystyle \frac{R}{c_v}=\gamma-1$ (with $\gamma=\tfrac{c_p}{c_v}$):

    $$
    \ln\frac{T_2}{T_1} = -(\gamma-1)\ln\frac{v_2}{v_1} \implies \frac{T_2}{T_1} = \Big(\frac{v_1}{v_2}\Big)^{\gamma-1}.
    $$
    
    Rewriting as a state relation,

    $$
    \boxed{Tv^{\gamma-1}=\text{const.}}
    $$

3. Using $(T,p)$:

   $$
   \mathrm{d}s = c_p\frac{\mathrm{d}T}{T} - R\frac{\mathrm{d}p}{p}.
   $$

    Again set $\mathrm{d}s=0$:

    $$
    c_p\frac{\mathrm{d}T}{T} = R\frac{\mathrm{d}p}{p} \implies \ln\frac{T_2}{T_1} = \frac{R}{c_p}\ln\frac{p_2}{p_1}.
    $$
    
    Since $\displaystyle \frac{R}{c_p}=1-\frac{1}{\gamma}=\frac{\gamma-1}{\gamma}$,

    $$
    \frac{T_2}{T_1}=\Big(\frac{p_2}{p_1}\Big)^{(\gamma-1)/\gamma} \implies \boxed{Tp^{(1-\gamma)/\gamma}=\text{const.}}
    $$

4. Getting the $(p,v)$ form directly:
    
    Starting with

    $$
    \begin{gather*}
    Tv^{\gamma-1}=\text{const.}, \\[10pt]
    Tp^{(1-\gamma)/\gamma}=\text{const.}
    \end{gather*}
    $$

    write each as an explicit proportionality for (T):

    $$
    \begin{gather*}
    T=C_1v^{1-\gamma}, \\[10pt]
    T=C_2p^{,(\gamma-1)/\gamma}.
    \end{gather*}
    $$

    Equate the two expressions for (T) and rearrange:

    $$
    C_1v^{1-\gamma}=C_2p^{,(\gamma-1)/\gamma} \implies p^{(\gamma-1)/\gamma}v^{\gamma-1}=\text{const.}
    $$

    Raise both sides to the power $\gamma/(\gamma-1)$:

    $$
    \big(p^{(\gamma-1)/\gamma}v^{\gamma-1}\big)^{\gamma/(\gamma-1)}=\text{const.} \implies \boxed{pv^{\gamma}=\text{const.}}.
    $$

Hence, we can express the isentropic condition for perfect gases as a set of three equivalent relationships:

(eq_isentropic_relations)=
$$
\boxed{
\begin{gather*}
T v^{\gamma-1} = \text{const.}, \\[10pt]
T p^{(1-\gamma)/\gamma} = \text{const.}, \\[10pt]
p v^{\gamma} = \text{const.}
\end{gather*}
}
$$

:::{important}

**WHY THE ISENTROPIC CONDITION ENFORCES $pv^{\gamma}=\text{const.}$**

Notice that the relation $pv^{\gamma}=\text{const.}$ has been derived from the isentropic condition applied to a perfect gas. That same expression has been used before, when calculating the work of a perfect gas in a simple compressible system and constrained to an **adiabatic** process.

Mind that enforcing adiabaticity already forbids the entropy transfer via heat exchange (i.e. $Q = 0 \implies \Delta S_{\text{transf.}} = 0$). Besides, the calculation of the work was performed under the additional constrain of the process being **quasi-static**, which means that is **reversible**. Hence, implicitly, the $pv^{\gamma}=\text{const.}$ relation applied before was imposing an isentropic condition.

An **adiabatic and quasi-static** process is also an **isentropic** process.
:::

---

(subsec_Ts_diagram)=
### The $T-s$ diagram and graphical interpretation

Having defined entropy changes (via the $T\mathrm{d}s$ relations), evaluated them for different **substance models** (ideal/perfect gases and real pure substances), and clarified the **isentropic condition** (including its ideal adiabatic–reversible specialization), we now introduce the **$T!-!s$ diagram**. This diagram is the natural **complement** to the **$p!-!v$ diagram**: just as **work** is represented by areas in $p!-!v$ space, **reversible heat** is represented by areas in $T!-!s$ space. Together, these two planes provide a clean, geometric bookkeeping of the two fundamental “process magnitudes.”

* **Graphical complementarity: $p-v$ (work) vs. $T-s$ (reversible heat)**

    For any **quasi-static** (boundary) work interaction,
    
    $$
    \delta W_{\text{rev.}} = p\mathrm{d}V \implies W_{\text{rev.}}=\int p\mathrm{d}V,
    $$
    
    so the **area under the path** in a $p-v$ diagram equals the **reversible work** (and the area enclosed by a cycle equals the **net** work). For any **internally reversible** heat interaction,
    
    $$
    \delta Q_{\text{rev.}} = T\mathrm{d}S \implies Q_{\text{rev.}}=\int T\mathrm{d}S,
    $$
    
    so the **area under the path** in a $T-s$ diagram equals the **reversible heat** (and the area enclosed by a cycle equals the **net** reversible heat). These two integrals are the differential expressions of the **$1^{\text{st}}$** and **$2^{\text{nd}}$** laws in their most useful, path-integral forms.

* **Explicit $T-s$ forms for perfect gases (constant $c_p, c_v$)**
   For a **perfect gas** ($c_p, c_v=$ const.; $R=c_p-c_v$), the $T\mathrm{d}s$ relations integrate to the familiar logarithmic forms:
   
    $$
    \mathrm{d}s = c_v\frac{\mathrm{d}T}{T} + R\frac{\mathrm{d}v}{v} \implies s - s_0 = c_v\ln\frac{T}{T_0} + R\ln\frac{v}{v_0},
    $$
    
    $$
    \mathrm{d}s = c_p\frac{\mathrm{d}T}{T} - R\frac{\mathrm{d}p}{p} \implies s - s_0 = c_p\ln\frac{T}{T_0} - R\ln\frac{p}{p_0}.
    $$
    
    From these, we get **exponential** (explicit) forms that are especially convenient for plotting/process-parametrization in $T-s$:
    
    * **$(T,v,s)$ form:**
    
        $$
        T = T_0e^{\frac{s-s_0}{c_v}}\Big(\frac{v_0}{v}\Big)^{R/c_v}
        $$
    
    * **$(T,p,s)$ form:**
    
        $$
        T = T_0e^{\frac{s-s_0}{c_p}}\Big(\frac{p}{p_0}\Big)^{R/c_p}
        $$

    * Useful **special cases** (perfect gas):    
        * **Isochoric** ($v=$ const.): $s-s_0=c_v\ln(T/T_0) \implies T=T_0e^{(s-s_0)/c_v}$.
        * **Isobaric** ($p=$ const.): $s-s_0=c_p\ln(T/T_0) \implies T=T_0e^{(s-s_0)/c_p}$.
        * **Isothermal** ($T=$ const.): horizontal line.
        * **Isentropic** ($s=$ const.): vertical line.

* **Using the $T-s$ diagram in practice**

    * For **perfect/ideal gases**, the relations above let you **parametrize the path** in $T-s$ and compute $Q_{\text{rev.}}=\int T,\mathrm{d}S$ directly from the curve’s area.
      
    * For **pure substances** (non-ideal), $s(T,p)$ (or $s(T,v)$) comes from **tables**, but the **area rule still holds**: $Q_{\text{rev.}}=\int T,\mathrm{d}S$. The $T-s$ map includes the **saturation dome** (subcooled liquid, two-phase region, superheated vapor). Across vaporization, $s$ **increases**; across condensation, $s$ **decreases**—the corresponding **rectangles/curvilinear areas** in $T-s$ quantify reversible heat.
 
:::{note} 

**ENTROPY INCREASE IN ISOCHORIC AND ISOBARIC PROCESSES**

According to the expressions derived above, in isochoric and isobaric processes the temperature evolves as $\propto e^{s/c_v}$ and $\propto e^{s/c_p}$, respectively. We have already shown that $c_{p} > c_{v}$. Hence, $1/c_{v} > 1/c_{p}$ and, consequently, the $T(s)$ relation is steeper in the isochoric case than in the isobaric one. For the same temperature difference $\Delta{}T$, the entropy increase $\Delta{}S$ will be larger in the isobaric case than in the isochoric one.

This deduction, based exclusively in the functional relation $T(s)$, could have already been deduced from the notion of heat as an entropy-transferring mechanism. Indeed, it has already been discussed that:
* in a closed system subjected to an isochoric process (i.e. a rigid container), an amount of heat is required to increase its internal energy.
* In a closed system subjected to an isobaric process (i.e. a piston-cylinder system), an amount of heat is required to increase its enthalpy.
* The enthalpy increase always requires more heat than the internal energy increase. In the isobaric process, part of the heat is converted into the mechanical work required to rise the piston. In the isochoric one, all the heat input goes to increasing the internal energy of the system.
* As more heat is required in the isobaric case, a larger energy transfer will accompany the same temperature rise.
:::

---

(subsec_conceptual_closure_entropy_Tds)=
### Conceptual closure

* The **$T\mathrm{d}s$ relations** are the **differential expression** of the $2^{\text{nd}}$ law for a simple compressible substance.

* These relations are **local** and extend to **open systems** by adding **entropy transport with mass flow**; they underpin the steady-flow energy/entropy equations used in turbines, compressors, nozzles, and heat exchangers.

* Computing **entropy changes** requires a **substance model**:

  * **Ideal gas** ($c_p(T), c_v(T)$): integral forms with $\displaystyle \int \frac{c(T)}{T}\mathrm{d}T$ plus logarithmic $p–v$ terms.
  * **Perfect gas** (constant $c_p, c_v$): closed **logarithmic** expressions (analytical).
  * **Pure (real) substances**: values from **tables**; $s$ is fixed by any two independent intensive properties.

* The **isentropic condition** means **zero net entropy change** of the system ($\Delta S=0$). The **simplest route** is **adiabatic + reversible** ($ Q=0$, $S_{\text{gen.}}=0$), but other special balances (non-adiabatic + irreversible) can also yield $\Delta S=0$.

* For **perfect gases**, the adiabatic–reversible (ideal isentropic) specialization gives the classic **power laws**:

\begin{equation*}
    \text{Isentropic evolution} \implies
    \begin{cases}
        Tv^{\gamma - 1} = \text{const.}\\[1ex]
        Tp^{(1 - \gamma)/\gamma}=\text{const.}\\[1ex]
        pv^{\gamma}=\text{const.}
    \end{cases}
\end{equation*}

* The **$p-v$** and **$T-s$** planes are **graphically complementary**. This duality provides a clean geometric accounting of **work** and **(reversible) heat** in processes and cycles.
