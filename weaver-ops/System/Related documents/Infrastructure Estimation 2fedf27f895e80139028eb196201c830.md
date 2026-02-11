# Infrastructure Estimation

## **Purpose**

Describe and quantify **non-standard infrastructure requirements** so delivery and operations can execute safely, and Sales can price the impact **without exposing internal complexity**.

---

## **When this document exists**

This document is created **only if** infrastructure assumptions cannot be covered by the standard stack.

If infrastructure is standard, assumptions are documented **directly in the Delivery Scenario** and this document does not exist.

---

## **Content**

### **Context**

- Reason for non-standard infrastructure
    
    (e.g. scale, security, performance, compliance, legacy constraints)
    
- Related project or delivery scenario
- Trigger type
    - New project
    - Scale-up
    - Infra evolution / Tech-as-a-Service

---

### **Environment model**

- Number of environments
    - Development
    - Staging
    - Production
- Isolation requirements
- Environment parity constraints

---

### **Infrastructure architecture (high level)**

- Hosting model
    - Managed services
    - Cloud provider (AWS / GCP / others)
- Backend hosting approach
- Database type and topology
- Networking requirements (if any)
- External services dependencies

⚠️ No low-level design. No provisioning steps.

---

### **Operational constraints**

- Availability expectations
- Performance or latency constraints
- Security or compliance requirements
- Data sensitivity considerations
- Monitoring or alerting expectations (high level)

---

### **Cost impact (order of magnitude)**

- Estimated monthly infrastructure cost range
- Main cost drivers
- Known cost volatility risks
- Explicit exclusions (what is not covered)

⚠️ No exact pricing. No provider invoices.

---

### **Risks & assumptions**

- Key technical risks
- Known unknowns
- Assumptions required for estimation validity
- Conditions under which this estimation becomes invalid