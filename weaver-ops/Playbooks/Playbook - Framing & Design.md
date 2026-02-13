# Workflow Playbook – Framing & Design

> **Goal:** Turn a signed client need into validated product documentation, design, technical definition, delivery scenarios, and delivery team blueprint.

## 1. Quick Reference
- **Trigger:** Commercial agreement signed + Expression of Need available.
- **Exit:** Product doc, technical doc, design system/prototype, delivery scenarios, delivery team all validated and stored.
- **Owner:** Project / Product Lead (PPL) except Technical Definition (Tech Lead).
- **Target Timeline:** 4–6 weeks.

## 2. Intake Checklist
- [ ] Expression of Need uploaded + versioned.
- [ ] Client stakeholders + decision cadence documented.
- [ ] Budget / commercial guardrails captured.
- [ ] PPL, Delivery Owner, Tech Lead, UX/UI designer assigned.

## 3. Stage Blueprint
### State 0 – Need Clarification & Scope Intent Lock (Owner: PPL, SLA 1 week)
**Checklist**
- [ ] Review Expression of Need; capture objectives, constraints, success metrics.
- [ ] Conduct stakeholder interviews (Client Sponsor, Ops, Tech) – log notes.
- [ ] Draft Scope Intent doc (in/out of scope, assumptions, success criteria, risks).
- [ ] Secure written client approval; store signed PDF.

**Artifacts:** Scope Intent, stakeholder map.

---

### State 1 – Product Definition (Owner: PPL, SLA 1.5 weeks)
**Steps**
1. **Feature inventory** – map personas vs. journeys vs. features.
2. **Behavior specs** – write Gherkin scenarios for critical flows.
3. **Business rules** – document calculations, thresholds, edge cases.
4. **Roadmap** – prioritize features over 3–6 months with dependencies.
5. **Validation** – run alignment session with client; freeze scope.

**Exit:** Product Documentation + Roadmap signed off.

---

### State 2 – Design Definition (Owner: PPL + UX/UI, SLA 1 week)
**Checklist**
- [ ] UX journeys + UI screens for every feature (desktop/mobile variants as needed).
- [ ] Animated prototype (Figma) covering golden paths + key edge cases.
- [ ] Design system (components, typography, spacing, states).
- [ ] Traceability sheet linking design components to Product Doc sections.
- [ ] Client signoff recorded.

---

### State 3 – Technical Definition (Owner: Tech Lead, SLA 1 week)
**Steps**
1. **Architecture** – diagrams (C4 level), responsibilities, data flow.
2. **Stack decisions** – languages, frameworks, services, rationale.
3. **Data & integrations** – ERDs, API contracts, third-party touchpoints.
4. **Infra assumptions** – environments, hosting, security/compliance.
5. **Delivery team definition** – Staffing Manager defines minimal run team (roles, seniority, availability).
6. **Validation** – internal review; signoff recorded.

**Artifacts:** Technical Documentation, Delivery Team definition.

---

### State 4 – Delivery Scenarios Definition (Owner: PPL + Delivery Owner, SLA 0.5 week)
**Checklist**
- [ ] Baseline scenario (1 person per role) with duration, risks, internal cost.
- [ ] Duration check; if >3 months, produce accelerated scenario.
- [ ] Delivery Owner validation; mark INTERNAL ONLY.
- [ ] Package shared with Sales + Delivery Estimation.

## 4. Governance & KPIs
- **Scope churn:** ≤ 2% of features reopen after State 1.
- **Design completeness:** 100% of Product Doc sections mapped to design components.
- **Technical clarity:** Zero open technical questions at handover.

## 5. Tooling & Templates
- Scope Intent template.
- Product Documentation template (NFA format).
- Gherkin behavior template.
- Design traceability sheet.
- Technical architecture template (C4 + ADRs).
- Delivery scenario workbook.

## 6. Handoffs
- Store artifacts in `documentation_produit/NFA/...` with version numbers.
- Notify Development Estimation + Allocation teams when State 4 closes.
- Update Governance registers with key assumptions and risks.
