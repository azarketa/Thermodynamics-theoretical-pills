(sec_exergy_destruction)=
## Principle of decreasing exergy; entropy and exergy balances

Exergy, as a quantity derived from the **$1^{\text{st}}$** and **$2^{\text{nd}}$ laws**, inherits their physical meaning:
the first ensures **energy conservation**, while the second imposes **quality degradation** through **entropy generation**.
Accordingly, one may state a complementary **principle of decreasing exergy**, which mirrors the principle of increasing entropy.

While **entropy** measures the *irreversible dispersal of energy*, **exergy** quantifies the *loss of its usefulness* — that is, the energetic value destroyed by irreversibility.
Just as *entropy is always generated and never destroyed*, *exergy is always destroyed and never generated*.

---

(subsec_isolated_exergy_destruction)=
### Derivation for an isolated system

The principle may be demonstrated by considering an **isolated system**, one that **exchanges neither energy nor mass** with its surroundings. In practice, this can be interpreted as the **combined system + environment**, often referred to as the **thermodynamic universe** — the ultimate isolated system.

For such a composite, **no external boundary interactions** exist. Any mechanical or thermal exchange between the system and the environment becomes **internal** to the overall isolated whole. In particular, the **ambient pressure work** term $p_0(V_2 - V_1)$, which appears when analyzing the system *alone*, now vanishes from the global balance because the work **done by the system** on the environment is **exactly balanced** by the opposite work **done by the environment** on the system. Hence, their effects **cancel out**, leaving only the total internal energy change of the combined universe.

Accordingly, the **$1^{\text{st}}$ law** for the isolated composite reads:

(eq_first_law_isolated)=
$$
E_{\text{in}} - E_{\text{out}} = \Delta E_{\text{sys.}} = 0
\quad \Rightarrow \quad
E_2 - E_1 = 0
$$

The **$2^{\text{nd}}$ law**, applied to the same system, gives:

(eq_second_law_isolated)=
$$
S_{\text{in}} - S_{\text{out}} + S_{\text{gen.}} = \Delta S_{\text{sys.}}
\quad \Rightarrow \quad
S_{\text{gen.}} = S_2 - S_1
$$

Multiplying the second law by the environmental temperature $T_0$ and subtracting it from the first law yields:

(eq_combined_laws_isolated)=
$$
T_0 S_{\text{gen.}} = (E_2 - E_1) - T_0 (S_2 - S_1)
$$

Recalling that the **change in exergy** is defined as

(eq_exergy_change_general)=
$$
\Delta X = X_2 - X_1 = (E_2 - E_1) - T_0 (S_2 - S_1),
$$

comparison of both expressions gives the key relation:

(eq_exergy_destruction_principle)=
$$
\boxed{
\Delta X = - T_0 S_{\text{gen.}} \le 0
}
$$

This proves mathematically that **exergy can only decrease** (or remain constant in reversible processes), establishing the **principle of decreasing exergy**.

:::{important}

**THE DESTRUCTION OF EXERGY**

Entropy is a measure of **energy degradation**; exergy quantifies the **energetic cost** of that degradation. Whenever entropy is generated ($S_{\text{gen.}} > 0$), an equivalent amount of exergy is **destroyed** ($X_{\text{dest.}} = T_0 S_{\text{gen.}}$). Thus, *irreversibility* and *exergy destruction* are two descriptions of the same physical phenomenon — one in entropic terms, the other in energetic ones.
:::

:::{note}

**RELATION BETWEEN ENTROPY AND EXERGY**

The $2^{\text{nd}}$ law, written in terms of **entropy generation**, establishes whether a process is *reversible*, *irreversible*, or *impossible*.
When combined with the $1^{\text{st}}$ law, the same classification can be expressed in **energetic (exergy)** terms, as summarized below:

| **Criterion** | **Generated entropy** $S_{\text{gen.}}$ | **Destroyed exergy** $X_{\text{dest.}}$ | **Process type** |
| :- | :- | :-: | :- |
| $> 0$ | Positive | Positive | **Irreversible** |
| $= 0$ | Zero | Zero | **Reversible** |
| $< 0$ | Negative | Negative | **Impossible** |

Thus, **entropy generation** and **exergy destruction** are *two sides of the same phenomenon*:
entropy quantifies the *disorder increase*, while exergy quantifies the *useful-energy loss* associated with it.
:::

---

(subsec_entropy_exergy_balance_forms)=
### Entropy and exergy balance forms

The **entropy** and **exergy** balances express the two complementary aspects of the $2^{\text{nd}}$ law:

* The **entropy balance** describes how *entropy is transferred and generated* within a system — a **qualitative measure** of irreversibility.
* The **exergy balance** describes how *useful energy (work potential)* is transferred and destroyed — a **quantitative measure** of that same irreversibility.

| **Formulation type** | **Entropy balance** | **Exergy balance** | **Interpretation** |
| :- | :- | :- | :- |
| **General form** | $\displaystyle S_{\text{in}} - S_{\text{out}} + S_{\text{gen.}} = \Delta S_{\text{sys.}}$ | $\displaystyle X_{\text{in}} - X_{\text{out}} - X_{\text{dest.}} = \Delta X_{\text{sys.}}$ | Tracks total transfer, storage, and internal generation/destruction. |
| **Rate form** | $\displaystyle \dot{S}_{\text{in}} - \dot{S}_{\text{out}} + \dot{S}_{\text{gen.}} = \frac{\mathrm{d}S_{\text{sys.}}}{\mathrm{d}t}$ | $\displaystyle \dot{X}_{\text{in}} - \dot{X}_{\text{out}} - \dot{X}_{\text{dest.}} = \frac{\mathrm{d}X_{\text{sys.}}}{\mathrm{d}t}$ | Expresses the same balance per unit time (rate basis).               |
| **Specific (intensive) form** | $\displaystyle s_{\text{in}} - s_{\text{out}} + s_{\text{gen.}} = \Delta s_{\text{sys.}}$ | $\displaystyle x_{\text{in}} - x_{\text{out}} - x_{\text{dest.}} = \Delta x_{\text{sys.}}$ | Entropy or exergy change expressed per unit mass. |

:::{note}

**CONNECTION AND MEANING**

* **Entropy generation** $S_{\text{gen.}}$ measures the *degree of irreversibility* in entropic terms.
* **Exergy destruction** $X_{\text{dest.}} = T_0 S_{\text{gen}}$ translates that irreversibility into *energy-quality loss*.
* For **reversible processes**, $S_{\text{gen.}} = 0$ and $X_{\text{dest.}} = 0$.
* For **irreversible processes**, both terms are positive.
* Both balances apply to **closed** and **open systems**, provided that the proper expressions for entropy and exergy transfers are used.
:::

---

(subsec_conceptual_closure_exergy)=
### Conceptual closure

* The **principle of decreasing exergy** complements the **principle of increasing entropy**: while entropy quantifies the *degradation of energy quality*, exergy quantifies the *loss of useful work potential* that accompanies it.

* In **reversible processes**, entropy generation is null and **no exergy is destroyed** ($S_{\text{gen.}} = 0 \implies X_{\text{dest.}} = 0$). In **irreversible processes**, entropy generation is positive and **exergy decreases** ($S_{\text{gen.}} > 0 \implies \Delta X < 0$).

* The **exergy balance** extends the logic of the **energy balance** by explicitly incorporating irreversibility through the destruction term $T_0 S_{\text{gen.}}$. It therefore provides a **quantitative measure of the penalty** imposed by the $2^{\text{nd}}$ law.

* Entropy and exergy represent **two complementary views** of the same physical limitation: entropy focuses on **direction and feasibility**, whereas exergy focuses on **usefulness and performance**.
