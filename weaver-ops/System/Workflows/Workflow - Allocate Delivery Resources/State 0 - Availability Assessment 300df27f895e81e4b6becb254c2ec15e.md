# State 0 - Availability Assessment

## Goal

Determine whether required resources are available within defined constraints.

---

## State Owner

Staffing / Capacity Manager

---

## Required Functions

- Staffing / Capacity Manager
- Project / Product Lead

---

**Entry conditions**

- Validated resource request available
- Project documentation available

**Exit conditions (explicites et binaires)**

- Required resources available within constraints (≤ 2 weeks)
    
    **OR**
    
- Resources confirmed not available

---

### Actions

**Action 1 – Extract Resource Criteria**

R: Project / Product Lead · A: Project / Product Lead

Purpose: translate the validated resource request into explicit allocation criteria.

Must be true after:

Roles, quantities, skill requirements, availability constraints, and project duration are clearly defined.

---

**Action 2 – Identify Internal Availability**

R: Staffing / Capacity Manager · A: Staffing / Capacity Manager

Purpose: identify developers currently available inside the company matching the criteria.

Must be true after:

All internally available matching developers are listed with availability dates.

---

**Action 3 – Check Hiring Pipeline Availability (Read-only)**

R: Staffing / Capacity Manager · A: Staffing / Capacity Manager

Purpose: assess whether candidates already in the hiring pipeline can meet requirements within constraints.

Must be true after:

Pipeline availability is confirmed or explicitly absent.

---

**Action 4 – Consolidate Availability List**

R: Staffing / Capacity Manager · A: Staffing / Capacity Manager

Purpose: produce the definitive list used for the state decision.

Must be true after:

A single consolidated list of developers matching criteria and availability exists.