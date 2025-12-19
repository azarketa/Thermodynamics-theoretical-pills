(sec_icre_system_classification_components)=
## System-level classification and main components of ICREs

Mechanical classification (reciprocating vs rotary, two-stroke vs four-stroke) explains *how* motion is produced, but it does not fully describe *how the engine is implemented as a system*. In practice, engines that share the same mechanical architecture may still differ strongly in performance, efficiency, reliability, noise, maintenance needs, and operating envelope because of system-level design choices.

For this reason, a second classification block is commonly adopted: a **non strictly thermo-mechanical classification**, based not on the idealized thermodynamic cycle, but on the **layout and global characteristics** of the engine. These criteria are essential because they determine whether the engine can operate near its intended **steady operating temperature**, whether it can be packaged and balanced properly, and whether it can deliver the demanded air and fuel flow under real conditions.

---

(subsec_icre_non_thermomechanical_classification)=
### Non strictly thermo-mechanical classification

#### Classification by cooling system

A first system-level criterion concerns the **cooling system**. Its purpose is to keep the engine operating near the so-called **normal operating temperature** (or *steady operating temperature*), that is, the temperature range where the engine tends to reach its best performance and durability conditions.

A cooling system must satisfy two practical requirements:

- it must allow the engine to reach the normal operating temperature rapidly after start-up, and  
- it must maintain that temperature regardless of environmental conditions and engine load.

This is not a minor detail. Combustion may involve gas temperatures as high as $2000\ ^\circ\text{C}$, and a large fraction of the chemical energy released by fuel burning (on the order of $70\%$ in many practical situations) appears as heat. If this heat is not properly dissipated, component temperatures rise, materials expand, thermal stresses grow, lubrication quality deteriorates, and engine performance drops. In extreme cases, excessive overheating may lead to mechanical seizure.

:::{important}

**WHY COOLING IS A PERFORMANCE REQUIREMENT**

An engine is not designed to be “as cold as possible”, but to operate in a *controlled thermal regime*.  
Too hot: excessive expansion, oil breakdown, loss of tolerances, risk of seizure.  
Too cold: poor lubrication conditions, higher friction, incomplete vaporization and poorer combustion in SI engines, and generally worse efficiency.

:::

Two main cooling approaches exist.

- **Liquid cooling (coolant cooling):**  
  A coolant circulates through channels and passages in the engine block and cylinder head. As it flows through the hot regions, it absorbs heat. The heated coolant then passes through a radiator (heat exchanger), where it transfers thermal energy to ambient air forced through the radiator. After cooling down, the fluid returns to the engine and the loop repeats.

  A **thermostat** plays a key role: it restricts or blocks coolant circulation when the engine is cold, enabling faster warm-up, and later regulates flow to keep the engine near its normal operating temperature. This control improves both engine performance and lubrication conditions.

  Liquid cooling is typically:
  - more effective and stable from the thermal standpoint,
  - quieter (the coolant provides a damping effect),
  - but heavier, more expensive, and more complex,
  - and it demands more maintenance due to pumps, hoses, channels, radiator, and fittings.

- **Air cooling:**  
  Air cooling relies on airflow over the cylinder and head surfaces, often enhanced by fins that increase heat-transfer area. A fan driven by the crankshaft generates a forced air stream that is guided toward the cylinders. As engine speed increases, airflow generally increases as well, improving heat removal.

  Air-cooled systems may also incorporate thermostatic devices that regulate airflow by shutters or flaps, preventing excessive cooling when the engine is cold and supporting faster warm-up.

  Air cooling is typically:
  - simpler (no radiator, no coolant pump, fewer components),
  - lighter and cheaper,
  - and easier to maintain,
  - but potentially less stable, since it depends strongly on ambient temperature and airflow conditions.
  It may be insufficient under certain climates and operating loads, producing overheating risk.
  Additionally, finned cylinders and the absence of hydraulic damping tend to make air-cooled engines noisier.

:::{note}

**ENGINEERING TRADE-OFF**

Liquid cooling generally maximizes temperature control and acoustic comfort, at the cost of mass and complexity.  
Air cooling maximizes simplicity and low mass, at the cost of thermal stability and often higher noise.

:::

---

#### Classification by cylinder number and arrangement

A second system-level criterion is the **number and arrangement of cylinders**, which affects compactness, balance, vibration, cooling layout, and structural design. Common arrangements include:

- **Inline (straight) engines**,  
- **V engines**,  
- **Boxer (flat) engines**, among other less common configurations.

The arrangement is not only a packaging choice: it has direct mechanical and structural consequences.

- Inline configurations often produce fewer vibration issues and allow simpler construction, but they may require longer blocks, reducing compactness.
- V configurations reduce engine length and can improve packaging, but may introduce stronger vibration modes (depending on firing order, bank angle, and balancing).
- Boxer engines can be interpreted as a V configuration with a $180^\circ$ bank angle. They yield a lower engine height and a lower center of gravity and can reduce vibration, but they often require duplicated head and valve-train components, increasing cost and complexity.

Engine size and application strongly influence typical cylinder counts. Small motorcycles often remain below 4 cylinders, passenger cars typically lie around 4–6 cylinders (sometimes 8 in high-performance vehicles), heavy-duty diesel trucks may use larger V configurations, and large marine or railway diesel engines may employ very high cylinder counts to meet power requirements.

:::{tip}

**WHY CYLINDER LAYOUT MATTERS FOR THERMODYNAMICS**

Later, when discussing real-cycle losses, it is useful to remember that cylinder arrangement affects:
- heat transfer area-to-volume ratios,
- cooling efficiency and thermal gradients,
- friction and mechanical losses,
- and gas exchange paths (intake/exhaust manifolds).

:::

---

#### Classification by intake pressure level

A third criterion is the **intake pressure**, which distinguishes between:

- **Naturally aspirated (atmospheric) engines**, where the cylinder filling relies on near-atmospheric intake conditions and pressure differences generated by piston motion.
- **Supercharged engines**, where a compressor raises intake pressure.

Boosting can be achieved by:

- a mechanically driven compressor (**supercharger**), or  
- a turbine-driven compressor (**turbocharger**).

Although the thermodynamic analysis of boosting will be treated later, the system-level distinction is already important: raising intake pressure increases the mass of air admitted per cycle, allowing higher torque and power for a given displacement, while also increasing thermal and mechanical loads and strengthening the role of cooling and lubrication.

---

(subsec_icre_components)=
### Main components of reciprocating ICREs

Once the principal classifications are established, it becomes useful to identify the most typical components found in ICREs. Real engines include many interacting parts, and a full mechanical description can be complex. For that reason, the focus here is on the most common components of **four-stroke reciprocating engines**, which represent the standard configuration in many practical applications.

:::{important}

**COMPONENTS AS A “MAP” FOR LOSSES**

The later study of real Otto/Diesel cycles involves losses (heat transfer, friction, pressure drops, imperfect sealing, finite-time combustion).  
Each of these phenomena can be connected directly to specific components (walls, rings, valves, manifolds, cooling passages, etc.).  
Learning the components now makes later thermodynamic modelling physically grounded.

:::

---

* **Cylinder:**

    The **cylinder** houses the piston and guides its motion. Because the piston slides continuously, the cylinder requires:
    
    - good surface finish,
    - strict manufacturing tolerances,
    - high wear resistance.
    
    Thermal and mechanical loads are significant, so cylinders frequently employ liners (dry or wet sleeves). A dry liner acts as a wear-resistant surface, while a wet liner can incorporate coolant contact and improve heat removal.

<br/>

* **Engine block:**

    The **engine block** houses the cylinders and supports the piston–connecting rod–crankshaft assembly. It must be structurally rigid and it often integrates cooling passages.
    
    Materials are selected to balance strength, thermal behavior, and weight. Cast iron and aluminum alloys are common: aluminum alloys reduce mass and improve thermal conductivity, benefiting cooling, but may require liners or treatments for wear resistance.
    
    The engine block design strongly depends on cylinder arrangement:
    
    - inline blocks are longer,
    - V blocks are shorter but split into banks,
    - boxer blocks are wide and low, lowering center of gravity.

<br/>

* **Crankcase (oil sump):**

    The **crankcase** typically serves as an oil reservoir and oil collector, positioned below the engine block. It is often bolted to the block. Because it is usually not a primary structural element, it is commonly made from light alloys or thin steel sheets.

<br/>

* **Cylinder head:**

    The **cylinder head** is mounted on top of the block and contains:
    
    - the combustion chamber geometry,
    - intake and exhaust ports,
    - valves (or valve seats),
    - and spark plugs or injectors.
    
    It operates under high thermal and mechanical stress. Heat losses are often significant here, especially near the exhaust region.
    
    A key sealing component is the **head gasket**, placed between the head and the block. Its purpose is to ensure tight sealing against:
    
    - combustion gases,
    - coolant leakage,
    - oil leakage.
    
    The gasket must be deformable enough to conform to surfaces yet strong enough to withstand high pressures and temperatures. Failure leads to severe issues: loss of compression, cross-contamination of oil and coolant, and eventual engine damage.

<br/>

* **Piston:**

    The **piston** is the moving element that receives pressure forces from the working fluid and transmits them to the connecting rod. It must:
    
    - ensure sealing together with piston rings,
    - remain lightweight (reducing inertia),
    - withstand high temperatures and thermal gradients,
    - resist corrosion and wear.
    
    Pistons experience especially high temperatures near their crown and must be designed for controlled thermal expansion.

<br/>

* **Piston rings:**

    **Piston rings** sit in grooves around the piston perimeter. Their main roles are:
    
    - sealing the combustion chamber (limiting blow-by),
    - controlling oil distribution on the cylinder wall,
    - transferring heat from the piston to the cylinder wall.
    
    A typical set may include:
    
    - **compression rings** (also called fire rings): seal combustion gases and limit leakage into the crankcase, while also aiding heat transfer,
    - an **oil control ring** (scraper): spreads lubricant uniformly and removes excess oil,
    - an **expander** element: acts like a spring supporting oil rings and maintaining contact pressure.
    
    Ring selection and coatings are driven by wear, temperature, friction reduction, and sealing requirements. Ring design differs between two-stroke and four-stroke engines due to lubrication strategy and operating constraints.

<br/>

* **Connecting rod:**

    The **connecting rod** transmits forces between piston and crankshaft. It must combine low mass with high stiffness and strength, and it must satisfy strict tolerance requirements to ensure proper alignment and load transfer. It is typically made from forged steel, special steels, light alloys, or more advanced cast materials.

<br/>

* **Crankshaft:**

    The **crankshaft** converts the connecting rod motion into rotation. It is subjected to torsion and bending loads and commonly includes:
    
    - journals and crankpins,
    - bearings,
    - counterweights to reduce vibration.
    
    Crankshafts often include internal oil passages to ensure lubrication of bearings and moving contacts. Materials include forged steel and ductile cast iron (spheroidal graphite cast iron).

* **Valves:**

    **Valves** regulate intake and exhaust flows. Exhaust valves, in particular, experience very high temperatures (often several hundreds of degrees Celsius). Multi-valve designs can reduce thermal loads and improve flow capacity. Materials are chosen for high-temperature resistance, commonly using chromium/nickel alloy steels.

<br/>

* **Camshaft:**

    The **camshaft** actuates the intake and exhaust valves following a prescribed timing law. It is typically located in the cylinder head and is mechanically driven in synchrony with the crankshaft.

<br/>

* **Timing belt / transmission belt:**

    A belt (or chain) connects the crankshaft to the camshaft, ensuring correct valve timing. In addition, belts may drive auxiliary devices such as:
    
    - fans in air-cooled engines,
    - mechanically driven compressors in supercharged engines.

<br/>

* **Starter motor:**

    An internal combustion engine is not self-starting: it requires an external energy source to initiate rotation. The **starter motor** is a small electric machine powered by the vehicle battery. It converts electrical power into mechanical rotation by engaging a pinion with the flywheel, forcing the crankshaft to rotate until combustion becomes self-sustaining.

    In small devices (chainsaws, outboards), this function is performed manually by pull-cords or similar mechanisms, which provide the initial crankshaft rotation.

---

(subsec_icre_system_closure)=
### Conceptual closure

- System-level classification complements mechanical classification by describing engine architecture beyond the thermo-mechanical ideal cycle.
- Cooling strategy is essential to guarantee operation at a controlled normal operating temperature and to prevent overheating failure modes.
- Cylinder arrangement shapes packaging, vibration behavior, and structural complexity.
- Intake pressure classification distinguishes naturally aspirated from boosted engines, strongly impacting achievable power density.
- A component-level map (cylinder, head, gasket, piston, rings, valve train, cranktrain, starter) provides the physical basis needed to interpret real-cycle losses later on.
