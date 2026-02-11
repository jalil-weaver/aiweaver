# State 4 - Production Switch

### **Goal**

Deploy the validated product to production, confirm immediate stability, and formally close delivery.

---

## **State Owner**

Delivery Owner

---

## **Required Functions**

- Delivery Owner
- Tech Lead
- Project / Product Lead
- Client Interface (Delivery Side)

---

**Entry conditions**

- State 3 closed
- Production switch authorized

**Exit conditions**

- Product deployed in production
- Production environment stable and accessible
- Delivery officially closed

---

## **Actions**

**Action 1 – Deploy to Production**

R: Tech Lead · A: Tech Lead

Purpose: deploy the validated release to the production environment.

Must be true after: production deployment completed; application accessible in production.

---

**Action 2 – Perform Post-Deployment Verification**

R: Tech Lead · A: Tech Lead

Purpose: verify production stability immediately after deployment.

Must be true after: no blocking or critical issues detected; rollback not required.

---

**Action 3 – Close Delivery and Handover**

R: Project / Product Lead · A: Delivery Owner

Purpose: formally close the delivery and confirm handover to the client.

Must be true after: delivery marked as closed; client informed; ownership and next steps clearly identified.