# State 1 - Scenario Construction

## Goal

Produce one or more executable development scenarios, including infrastructure and AI implications when applicable.

---

## State Owner

Delivery Owner

---

## Required Functions

- Delivery Owner
- Project / Product Lead
- Tech Lead
- Staffing / Capacity Manager
- AI Product Owner (Internal)
- AI Governance / AI Tech Owner (Internal)

---

**Entry Conditions**

- State 0 closed with inputs sufficient

---

**Exit Conditions**

- At least one delivery scenario produced

---

### **Actions**

**Action 1 — Build Base Delivery Scenario**

R: Project / Product Lead · A: Delivery Owner

Purpose: define a minimal viable execution scenario.

Result: roles, staffing, duration, risks defined (1 person per role baseline).

**Action 2 — Apply 15-Week Rule**

R: Tech Lead · A: Tech Lead

Purpose: keep delivery under 15 weeks.

Result:

- If ≤15 weeks: scenario validated
- If >15 weeks: additional scenario created with increased staffing

Non-standard infrastructure:

- Not Vercel + Supabase
- More than 2 environments
- Custom backend hosting (AWS, GCP, Kubernetes)
- Dedicated DB, VPC, private networking
- High compliance/security constraints
- Heavy third-party infra dependencies

**Action 3 — Integrate Infrastructure Estimation (if applicable)**

R: Staffing / Capacity Manager · A: Delivery Owner

Purpose: include required infrastructure setup or changes.

Result: infra needs, risks, and cost ranges integrated into the scenario.

**Action 4 — Integrate IA Estimation (if applicable)**

R: Tech Lead · A: Tech Lead

Purpose: assess IA-related complexity and constraints.

Result: IA-specific assumptions and risks integrated.