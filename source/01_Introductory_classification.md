(sec_icre_introduction)=
## Introductory classification of ICREs

Alongside gas turbines operating on Brayton-type gas cycles, **internal combustion reciprocating engines (ICREs)** are the other major family of gas power cycles that dominate engineering practice. Their relevance is largely explained by a simple fact: they provide a compact and robust way to convert the chemical energy of a fuel into **mechanical work**, with high power density and wide operational flexibility. This is why they are pervasive in transportation (cars, motorcycles, ships, small aircraft and auxiliary power units), and also appear in many small-scale power generation and mobile machinery applications.

In the classical thermodynamic idealization, two cycles are used as reference models for most practical implementations:

- the **Otto cycle**, typically associated with spark-ignition (gasoline) engines, and  
- the **Diesel cycle**, typically associated with compression-ignition (diesel) engines.

These two ideal cycles do not describe the full complexity of real engines, but they provide a clean conceptual language: they explain, in a first approximation, how heat is added and rejected and how mechanical work is obtained from a cyclic sequence of states.

:::{important}

**WHY ICREs ARE STUDIED SEPARATELY FROM GAS TURBINES**

Gas turbines are typically steady-flow turbomachines, where the working fluid evolves through rotating components in a continuous manner.
ICREs, instead, are *unsteady* by nature: the working fluid is confined in a cylinder and undergoes cyclic compression, combustion, and expansion with large temporal variations of pressure and temperature. This difference is essential for both modelling and design.

:::

Because of their widespread use, ICREs come in many technological forms. Engines that share the same thermodynamic “family resemblance” may still differ strongly in:

- mechanical layout and kinematics,
- system-level configuration (cooling, lubrication, intake/exhaust),
- number of cylinders and their arrangement,
- intake pressure level (naturally aspirated vs boosted),
- and even the working sequence used to complete a cycle (two-stroke vs four-stroke).

This diversity motivates a **layered approach** to the topic. Before entering the thermodynamic study of the Otto and Diesel cycles (ideal and real), it is useful to establish a coherent descriptive basis:

1. a mechanical description of how motion is produced and transmitted,
2. a classification based on piston motion and number of strokes,
3. a system-level classification that does not depend on the thermodynamic cycle itself,
4. and a survey of the main components, so that later thermodynamic concepts can be anchored to physical hardware.

:::{note}

**A PRACTICAL REASON FOR THIS ORDER**

Many non-ideal effects that appear later in the thermodynamic analysis (heat losses, incomplete combustion, friction, pumping work, pressure drops, finite-time combustion) are not abstract phenomena: they are directly connected to geometry, components, and system architecture. Understanding the “machine” first makes the thermodynamics more meaningful.

:::
