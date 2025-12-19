(sec_icre_mechanical_classification)=
## Mechanical classification of ICREs

Before introducing thermodynamic modelling (Otto/Diesel cycles, ideal vs real), it is convenient to classify ICREs using criteria that depend only on **mechanical motion** and on the way the engine completes a working sequence. This classification is independent of how heat addition is idealized, and therefore it provides a neutral descriptive layer.

The mechanical classification is organised around two main questions:

- *How is useful work produced and transmitted?*  
- *How many mechanical strokes are required to complete one cycle?*

---

### Classification by motion of the working element

A first criterion concerns the motion of the element that interacts with the working fluid and ultimately delivers mechanical work.

- **Reciprocating engines:**  
  The working element is a piston moving linearly inside a cylinder. The piston is connected to a connecting rod and a crankshaft, converting reciprocating motion into rotation. This is the dominant configuration in most road vehicles and a wide range of practical machines.

- **Rotary engines:**  
  The piston is replaced by a rotor that turns continuously. The classical representative is the **Wankel engine**, which uses a triangular rotor moving inside a chamber of approximately epitrochoidal geometry.

:::{important}

**RECIPROCATING VS ROTARY: A CORE MECHANICAL DISTINCTION**

Reciprocating engines inherently involve alternating acceleration and deceleration of masses, which produces vibration and imposes mechanical constraints at high speeds.
Rotary engines avoid reciprocating inertia but introduce other challenges, notably sealing and combustion chamber geometry control.

:::

---

### Classification by number of strokes (reciprocating engines)

Reciprocating engines are further classified by the number of piston strokes required to complete one thermo-mechanical cycle:

- **Four-stroke engines**
- **Two-stroke engines**

The term *stroke* refers to a piston travel from one extreme position to the other:

- from **top dead center** (TDC) to **bottom dead center** (BDC),
- or from BDC to TDC.

---

### Four-stroke internal combustion engines

Four-stroke engines are named as such because one cycle requires **four piston strokes**, corresponding to two crankshaft revolutions.

To describe the cycle, it is useful to recall the main components involved:

- **piston**, moving inside the cylinder,  
- **wrist pin**, connecting piston and connecting rod,  
- **connecting rod**, transmitting force to the crankshaft,  
- **crankshaft**, converting linear motion into rotation,  
- **intake and exhaust valves**, controlling charge exchange,  
- and either a **spark plug** (spark-ignition) or a **fuel injector** (compression-ignition).

The four strokes are:

- **Intake stroke:**  
  The piston moves from TDC to BDC while the intake valve is open. Fresh charge enters the cylinder:
  - a fuel–air mixture in spark-ignition engines,
  - air alone in compression-ignition engines.

- **Compression stroke:**  
  The piston moves from BDC to TDC with both valves closed. The charge is compressed, raising pressure and temperature.

- **Combustion and expansion (power stroke):**  
  Near TDC, combustion occurs:
  - spark ignition in SI engines,
  - fuel injection and auto-ignition in CI engines.  
  The rapid release of chemical energy increases pressure and drives the piston toward BDC, delivering mechanical work.

- **Exhaust stroke:**  
  The piston returns from BDC to TDC while the exhaust valve is open, expelling the burned gases.

:::{note}

**MECHANICAL SEPARATION OF FUNCTIONS**

In four-stroke engines, intake, compression, power production, and exhaust are mechanically separated into distinct strokes. This improves control of gas exchange and reduces direct short-circuiting of fresh charge to the exhaust, which supports efficiency and emissions control.

:::

---

### Two-stroke internal combustion engines

Two-stroke engines complete one cycle with only **two strokes** (one crankshaft revolution). The same physical sequence (intake, compression, combustion, exhaust) still exists, but it is achieved through a different mechanical arrangement.

Instead of poppet valves controlling intake and exhaust, two-stroke engines commonly rely on ports:

- an **intake port** and an **exhaust port** are opened and closed by the piston’s position,
- the engine layout typically integrates crankcase scavenging or other methods to deliver the fresh charge.

A simplified description is:

- **Downward stroke (expansion + scavenging):**  
  Combustion occurs near TDC, then expansion pushes the piston down. Near the end of the stroke, the exhaust port opens and then intake/scavenge ports open, allowing fresh gases to enter and push out exhaust gases.

- **Upward stroke (compression + ignition preparation):**  
  The piston moves upward, compressing the fresh charge. Near TDC, ignition occurs (SI) or fuel is injected and auto-ignites (CI), starting the next expansion.

Because intake and exhaust overlap, part of the fresh charge may escape through the exhaust. This tends to increase fuel consumption and emissions.

Lubrication often differs from four-stroke engines. A separate oil sump is not always feasible, and oil may be mixed with fuel or delivered in a simplified manner, which can cause oil to burn and increase pollutant emissions.

:::{important}

**WHY TWO-STROKE ENGINES ARE A TRADE-OFF**

Two-stroke engines can deliver high specific power because a power stroke occurs every revolution.
However, scavenging losses and lubrication constraints often reduce efficiency and increase emissions compared with four-stroke designs.

:::

Modern developments (direct injection, electronically controlled scavenging, stratified combustion) have significantly reduced short-circuiting losses and have revived interest in two-stroke concepts in specialized applications.

---

### Rotary engines (Wankel engines)

The Wankel engine replaces the piston-cylinder arrangement with:

- a **triangular rotor**,
- rotating within an approximately oval chamber.

As the rotor turns, three separate volumes form between rotor faces and the housing. Each volume undergoes intake, compression, combustion, and exhaust, but the processes occur in different spatial regions of the housing rather than in distinct time-separated strokes.

Advantages commonly include:

- smooth operation and low vibration (absence of reciprocating masses),
- compactness and high power-to-weight ratio,
- ability to operate at high rotational speeds.

Disadvantages include:

- sealing challenges at rotor apexes,
- higher fuel consumption in many configurations,
- and potential difficulties in controlling combustion chamber shape and heat losses.

:::{note}

**SPATIAL STROKES**

A Wankel engine can be thermodynamically compared to a four-stroke engine, but mechanically it is fundamentally different: the “strokes” are spatially distributed rather than temporally separated.

:::

---

### Conceptual closure

- Mechanical classification describes how motion is produced and transmitted, independently of thermodynamic modelling.
- Reciprocating and rotary engines differ primarily in kinematics, inertia effects, and sealing constraints.
- Four-stroke engines prioritize separated functions and better control of gas exchange.
- Two-stroke engines prioritize simplicity and high power density but face scavenging and lubrication challenges.
- This mechanical basis prepares the analysis of broader, system-level engine classifications.
