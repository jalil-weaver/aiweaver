# Observed Issues

## **Structural problems**

- Infrastructure work has no explicit start gate
- Infra design and infra execution are mixed
- Environment strategy is not tied to product maturity
- Infrastructure scope is never formally frozen
- Infra cost is not treated as a first-class constraint
- Infra decisions are made under delivery pressure
- Infra knowledge is concentrated on individuals
- No formal closure separates infra setup from maintenance

---

## **Symptoms**

- Servers and environments are created reactively
- Architecture choices are made while deploying
- Over-engineered setups for early-stage products
- Under-engineered setups for live products
- Late discovery of infra costs
- Infra changes absorbed silently during delivery
- Staging or prod decisions vary by habit, not rule
- Performance or scaling issues discovered post go-live
- Client questions infra costs after deployment
- Maintenance starts without a clear infra baseline

---

## **SPOF**

- Single DevOps profile owning architecture, setup, and fixes
- Infra decisions relying on oral context or Slack messages
- Founder or senior tech intervening to arbitrate infra urgency
- No document allowing a third party to understand the infra
- No system rule to block infra execution when inputs are missing

---

## **Boundaries**

### **Infrastructure start (current state)**

- *Infra starts when someone decides it’s needed.*
- *No formal input defines what must be built.*
- *Design and setup often happen at the same time.*

---

### **Infrastructure end (current state)**

- *Infra is considered done once “it works”.*
- *No explicit handover to maintenance.*
- *No frozen reference architecture exists.*

---

## **Core insight**

Infrastructure problems are not technical.

They are caused by the **absence of a system separating infra thinking from infra execution**.

The system currently allows infrastructure to be **designed, deployed, and modified without a clear scope, cost frame, or lifecycle boundary**.