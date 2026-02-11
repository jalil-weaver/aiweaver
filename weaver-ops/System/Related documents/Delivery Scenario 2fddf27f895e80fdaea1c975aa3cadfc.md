# Delivery Scenario

## **Purpose**

Define the delivery setup and commitments so execution can start without re-deciding team composition, timeline assumptions, delivery rhythm, or infrastructure.

---

## **Content**

### **Delivery mode**

- Delivery mode:
    - ☐ Project-based (bounded)
    - ☐ Continuous delivery (open-ended)
- The selected mode determines how commitments apply (timeline vs capacity).

---

### **Product scope reference**

- Reference to the **Product Roadmap**
- Explicit identification of:
    - In-scope initiatives
    - Out-of-scope initiatives (if any)

---

### **Team setup**

For each role, specify:

- Role name
- Mandatory or optional
- Number of people
- Indicative seniority

Example:

- Backend Developer — mandatory — 1 — senior
- Frontend Developer — optional — 1 — mid
- QA — optional — 1 — mid
- DevOps — optional — on-demand

---

### **Technologies**

For each role, specify required technologies with **mandatory / optional** status.

Example:

- Backend
    - Node.js — mandatory
    - NestJS — mandatory
    - PostgreSQL — mandatory
- Frontend
    - React — mandatory
    - TypeScript — mandatory

---

### **Frameworks & methodologies**

For each role, specify required practices with **mandatory / optional** status.

Example:

- Developers
    - Kanban — mandatory
    - Continuous delivery principles — mandatory
    - Code review workflow — mandatory
- QA
    - Exploratory testing — mandatory
    - Regression testing — mandatory

---

### **Delivery assumptions**

### **Capacity assumptions**

- Minimal delivery capacity: ≥ 1 developer
- Capacity can evolve over time
- No implicit promise of speed unless explicitly stated below

### **Timeline estimation**

- High-level timeline estimation based on:
    - Roadmap size
    - Assumed capacity
- Timeline expressed as:
    - Ranges
    - Scenarios
- No guarantee unless explicitly committed

Example:

- Scenario A (1 dev): ~X–Y months
- Scenario B (2 devs): ~X–Y months

---

### **Delivery rhythm**

- Execution model:
    - Continuous flow (Kanban)
    - Or time-boxed iterations (if project-based)
- Rituals frequency (review, sync, planning)

---

### **Infrastructure assumptions**

- Environment model:
    - Staging + Production (default)
- Hosting stack assumptions
- Key constraints or risks
- Order-of-magnitude infrastructure cost (if relevant)

---

### **Constraints**

- Fixed constraints sold to the client (if any)
- Explicitly flexible elements
- Conditions triggering:
    - Re-estimation
    - Scenario update

---

### **Acceptance**

- Scenario reviewed during Framing
- Scenario validated internally
- Scenario accepted by the client
- Scenario executable as-is by Delivery

---

## **Outcome**

- Delivery starts without re-discussing team, timeline, or setup
- Continuous delivery can start immediately if selected
- Any change requires an updated Delivery Scenario