# Workflow - Continuous delivery

## **Purpose**

Transform a validated multi-month roadmap into an operational delivery capacity, ready to enter continuous delivery without installation risk.

---

## **Entry Conditions**

- [Product Roadmap](../Related%20documents/Product%20Roadmap%20301df27f895e8021a83ccc7f2ead5334.md) available (complete, non-frozen)
- [Product Documentation](../Related%20documents/Product%20Documentation%202fddf27f895e80bba212d437b6395575.md) available and exploitable **(blocking)**
- [Technical Documentation](../Related%20documents/Technical%20Documentation%202fddf27f895e80a2b30dfb468cf8729b.md) available and exploitable **(blocking)**
- [Design](../Related%20documents/Design%202fddf27f895e8090a5c8e6a8a0fdbe95.md) available and exploitable **(blocking)**
- [Delivery Team](../Related%20documents/Delivery%20Team%20301df27f895e8078b22ccd3ace623e43.md) defined (minimum run capacity = 1 developer)
- Weaver PM assigned **and** back-up identified
- Minimum accesses possible (or explicit decision to standardize tools and infrastructure)

---

## **Exit Conditions**

- Minimal delivery capacity installed and activable
- Test and production environments operational
- Tools and repositories configured
- Kanban active with an exploitable backlog
- Next possible action is execution (no remaining installation task)

---

## **States**

---

[**State 0 - Ready to Start**](Workflow%20-%20Continuous%20delivery/State%200%20-%20Ready%20to%20Start%20300df27f895e80e693fcd2feefea013f.md)

Ensure all inputs are exploitable before any installation begins.

---

[**State 1 - Delivery Design**](Workflow%20-%20Continuous%20delivery/State%201%20-%20Delivery%20Design%20300df27f895e8006803ed94f3f06c3d4.md)

Define the delivery operating model and technical setup required for continuous execution.

---

[**State 2 - Capacity Installation**](Workflow%20-%20Continuous%20delivery/State%202%20-%20Capacity%20Installation%20300df27f895e80229b68f0cab369d89e.md)

Install the minimal delivery capacity and all required execution conditions.

---

[**State 3 - Run Activation**](Workflow%20-%20Continuous%20delivery/State%203%20-%20Run%20Activation%20300df27f895e8099b2c5e9d6ab46edb4.md)

Activate execution and formally close the installation workflow.

---

## **Invariants**

- Continuous delivery never starts before workflow completion
- Product Documentation and Technical Documentation are mandatory
- No commitment on velocity or deadlines
- Product arbitration is continuous and PM-driven
- PM role is mandatory and replaceable (back-up required)
- States are irreversible
- Any later scaling is handled outside this workflow