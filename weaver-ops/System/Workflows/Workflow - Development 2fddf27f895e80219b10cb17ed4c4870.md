# Workflow - Development

## **Purpose**

Deliver the agreed product from ready-to-start inputs to production release, in stable and controlled execution conditions.

**Entry Conditions**

- Commercial agreement signed
- [Product documentation](../Related%20documents/Product%20Documentation%202fddf27f895e80bba212d437b6395575.md) validated
- [Technical documentation](../Related%20documents/Technical%20Documentation%202fddf27f895e80a2b30dfb468cf8729b.md) validated
- [Design](../Related%20documents/Design%202fddf27f895e8090a5c8e6a8a0fdbe95.md) validated
- [Delivery scenario](../Related%20documents/Delivery%20Scenario%202fddf27f895e80fdaea1c975aa3cadfc.md) validated

**Exit Conditions**

- All planned features developed
- No blocking or critical bugs
- Final payment received
- Product deployed in production

---

## **States**

[**State 0 - Ready to Start**](Workflow%20-%20Development/State%200%20-%20Ready%20to%20Start%202fddf27f895e8050b1a1e411dfee7717.md)

Ensure all prerequisites are available before any execution begins.

---

[**State 1 - Parallel Setup**](Workflow%20-%20Development/State%201%20-%20Parallel%20Setup%202fddf27f895e8042a8dbe297dc7a6c7a.md)

Prepare all execution conditions in parallel to avoid delivery downtime.

---

[**State 2 - Development Execution**](Workflow%20-%20Development/State%202%20-%20Development%20Execution%202fddf27f895e80938542e3052c5bdc03.md)

Develop all planned features with continuous quality control.

---

[**State 3 - Final Validation**](Workflow%20-%20Development/State%203%20-%20Final%20Validation%202fddf27f895e801b869ce38457c644cd.md)

Stabilize the product and confirm readiness for production.

---

[**State 4 - Production Switch**](Workflow%20-%20Development/State%204%20-%20Production%20Switch%202fddf27f895e80a3b226c2d3aa5c00c2.md)

Deploy the product to production and close the delivery.

---

## **Invariants**

- Development never starts without validated inputs
- Setup activities must not block development execution
- Production is never deployed before final payment
- States are irreversible