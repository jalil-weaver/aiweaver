# Workflow - Allocate Delivery Resources

## **Purpose**

Transform a validated resource request into an assigned project team.

**Entry Conditions**

- [Delivery Team](../Related%20documents/Delivery%20Team%20301df27f895e8078b22ccd3ace623e43.md) or [Delivery scenario](../Related%20documents/Delivery%20Scenario%202fddf27f895e80fdaea1c975aa3cadfc.md) submitted by PM and Tech Lead

**Exit Conditions**

- All requested roles allocated
- Assigned project team formally onboarded
- Developers considered locked and unavailable for reassignment without a new workflow

---

## **States**

[**State 0 - Availability Assessment**](Workflow%20-%20Allocate%20Delivery%20Resources/State%200%20-%20Availability%20Assessment%20300df27f895e81e4b6becb254c2ec15e.md)

Assess whether required resources are available within defined constraints.

---

[**State 1 - Team Selection**](Workflow%20-%20Allocate%20Delivery%20Resources/State%201%20-%20Team%20Selection%20300df27f895e81db9c19f99eabb1647a.md)

Select a technically validated team from available resources.

---

[**State 2 - Assignment Confirmation**](Workflow%20-%20Allocate%20Delivery%20Resources/State%202%20-%20Assignment%20Confirmation%20300df27f895e81a7b030cb998a116e1a.md)

Formally assign and lock the project team.

---

## **Invariants**

- This workflow never starts without a validated resource request
- No hiring or recruitment is initiated inside this workflow
- Availability decisions are strictly binary (available / not available)
- Teams are not assigned partially
- Assigned developers cannot be reallocated without a new workflow
- States are irreversible