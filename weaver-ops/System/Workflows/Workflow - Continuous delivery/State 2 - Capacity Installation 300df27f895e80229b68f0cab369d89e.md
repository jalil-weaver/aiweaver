# State 2 - Capacity Installation

### **Goal**

Install the minimal delivery capacity and ensure all operational prerequisites are in place to start execution.

---

## **State Owner**

Staffing / Capacity Manager

---

## **Required Functions**

- Staffing / Capacity Manager
- Project / Product Lead
- Tech Lead

---

**Entry conditions**

- State 1 marked as **Delivery Designed**

**Exit conditions (explicit and binary)**

- Minimal delivery capacity installed (≥ 1 developer)
- Resources onboarded on product, codebase, and delivery rules
- Tools and repositories operational
- Test and production environments operational
- State marked as **Capacity Installed**

---

### **Actions**

**Action 1 – Staff Minimal Capacity**

R: Staffing / Capacity Manager · A: Staffing / Capacity Manager

Purpose: staff the minimal delivery capacity defined in the Delivery Team.

Must be true after: at least one developer allocated and available for delivery.

---

**Action 2 – Onboard Delivery Capacity**

R: Project / Product Lead · A: Project / Product Lead

Purpose: onboard resources on product behavior, technical stack, delivery rules, and tooling.

Must be true after: no critical knowledge required to start delivery remains implicit.

---

**Action 3 – Deploy Required Environments**

R: Tech Lead · A: Tech Lead

Purpose: deploy and validate test and production environments.

Must be true after: environments operational and usable for delivery.