# Workflow Playbook – Framing Change

> **Goal:** Express a requested change as a precise delta (functional, design, technical) ready for estimation, without rewriting the entire product documentation.

## 1. Quick Reference
- **Trigger:** Change request submitted for an existing product.
- **Exit:** Locked Change Specification, updated docs/design (delta only), routed to estimation.
- **Owner:** Project / Product Lead (States 0,1,3), Tech Lead (State 2).
- **SLA:** 5 business days.

## 2. Intake Checklist
- [ ] Change Specification received with requester, priority, rationale.
- [ ] Access to current product docs, design, technical notes confirmed.
- [ ] Impacted stakeholders identified.

## 3. Stage Instructions
### State 0 – Change Qualification & Lock (Owner: PPL, SLA 0.5 day)
**Checklist**
- [ ] Log request in Change Register (ID, date, source, urgency).
- [ ] Validate it fits maintenance/change scope (not net-new product).
- [ ] Decide outcome: **Accepted**, **Rejected**, or **Redirected**; communicate decision.

**Artifacts:** Qualification note + Change Register entry.

---

### State 1 – Change Scope Definition (Owner: PPL, SLA 2 days)
**Steps**
1. **Functional delta** – describe adds/mods/removals referencing Product Doc sections.
2. **Non-impacted scope** – explicitly state unaffected modules to avoid creep.
3. **Design decision** – mark whether UI/UX updates needed.
4. **Update Product Doc (delta only)** – use annotations or addenda, never rewrite whole doc.

**Exit:** Updated Change Specification + annotated Product Doc.

---

### State 2 – Technical Decision Gate (Owner: Tech Lead, SLA 1 day)
**Checklist**
- [ ] Technical impact documented (components, services, tests, data migrations).
- [ ] Infra impact classified: None / Potential / Confirmed.
- [ ] If design required, ensure updated screens/prototype attached before proceeding.
- [ ] Risks + dependencies logged.

**Outcome:** Tech note + infra classification. If infra confirmed → simultaneously trigger Infrastructure Change workflow.

---

### State 3 – Change Lock & Handover (Owner: PPL, SLA 1.5 days)
**Steps**
1. **Validation review** – PPL + Tech Lead verify all deltas captured and versioned.
2. **Lock specification** – mark doc read-only; changes require restart.
3. **Route to estimation** – send to Development Estimation (change path) or Development + Infrastructure (if infra flagged).
4. **Communicate** – notify Delivery Owner, Sales/client of next steps + ETA.

**Exit:** Locked change pack + estimation ticket ID.

## 4. Controls & KPIs
- **Turnaround time:** ≤5 business days per change.
- **Rework rate:** ≤10% of changes re-opened after lock.
- **Documentation hygiene:** 100% of changes linked to Product Doc sections via anchors.

## 5. Templates & Tools
- Change Register (Notion/Airtable) template.
- Change Specification form.
- Delta annotation guideline.
- Technical impact note template.
- Routing email template for estimation handover.

## 6. Escalations
- If change scope disputes arise → involve Delivery Owner + Client sponsor within 24h.
- If infra impact uncertain → pause handover and convene Tech Design review.
