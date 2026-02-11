# Workflow - Infrastructure change

## **Purpose**

Assess, define, and decide on an infrastructure change before any execution, to protect delivery, costs, and operations.

---

## **Entry Conditions**

- An [**Infrastructure Change Brief**](../Related%20documents/Infrastructure%20Change%20Brief%202fedf27f895e808fa87ecc5701267958.md) created by a Tech Lead
- Project in one of the following states:
    - Ongoing delivery
    - Maintenance / Continuous Delivery
- Relevant technical context available:
    - Technical documentation
    - Delivery scenario (if applicable)
    - Access to current infrastructure

---

## **Exit Conditions**

- **Infrastructure Change Proposal** completed and explicitly decided:
    - Approved
    - Rejected
    - Needs adjustment

---

## **States**

---

[**State 0 - Infrastructure Change Qualification**](Workflow%20-%20Infrastructure%20change/State%200%20-%20Infrastructure%20Change%20Qualification%202fedf27f895e8008b020e8bd09506228.md)

Confirm that the request justifies an infrastructure study.

---

[**State 1 - Infrastructure Impact Analysis**](Workflow%20-%20Infrastructure%20change/State%201%20-%20Infrastructure%20Impact%20Analysis%202fedf27f895e80bba23bd2a9ed912137.md)

Understand the current infra and identify required changes.

---

[**State 2 - Infrastructure Solution & Estimation**](Workflow%20-%20Infrastructure%20change/State%202%20-%20Infrastructure%20Solution%20&%20Estimation%202fedf27f895e802ebb6dee9c618e97dd.md)

Define the target solution and estimate costs and risks.

---

[**State 3 - Decision & Routing**](Workflow%20-%20Infrastructure%20change/State%203%20-%20Decision%20&%20Routing%202fedf27f895e801d9e3bd5a4cbbf2b0b.md)

Make a clear decision and route the outcome.

---

## **Invariants**

- No infrastructure work without an approved proposal
- DevOps is never engaged without a technical trigger
- No cost or solution is communicated without documentation
- States are irreversible