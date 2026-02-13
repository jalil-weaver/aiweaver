# Workflow Playbook – Continuous Delivery Installation

> **Goal:** Stand up a safe, minimal continuous-delivery engine (people + tooling + environments) so execution can start without installation risk.

## 1. Quick Reference
- **Trigger:** Product, technical, and design packages validated + roadmap available.
- **Exit:** Kanban live, backlog actionable, capacity installed, environments ready.
- **Owner:** Project / Product Lead (PPL).
- **Target Duration:** ≤ 10 business days from Ready-to-Start to Run Activation.

## 2. Input Gate Checklist
- [ ] Product documentation validated.
- [ ] Technical documentation validated.
- [ ] Design package validated (prototype + design system).
- [ ] Product roadmap prioritized (≥ 3 months horizon).
- [ ] Delivery Team definition approved (incl. PM + backup).
- [ ] Access/security decisions documented.

**If any unchecked → pause.**

## 3. Roles & RACI
| Activity | PPL | Tech Lead | Staffing Manager | Head of Ops | Delivery Owner |
| --- | --- | --- | --- | --- | --- |
| Validate inputs | **A/R** | C | C | I | I |
| Delivery design (backlog + rules) | **A/R** | C | C | I | I |
| Staffing authorization | C | I | **R** | **A** | I |
| Capacity installation | C | C | **A/R** | I | I |
| Environments/tooling | C | **A/R** | I | I | I |
| Run activation | **A/R** | C | C | I | C |

## 4. Phase Playbook
### State 0 – Ready to Start (Owner: PPL, SLA 1 day)
**Checklist**
- [ ] Review each input doc for completeness + last updated date.
- [ ] Confirm PM backup + escalation tree.
- [ ] Log blocking ambiguities with deadline/owner.

**Artifacts**: Input validation memo (Notion), risk log entries.

---

### State 1 – Delivery Design (Owner: PPL, SLA 3 days)
**Deliverables**
1. **Global backlog** (Notion/Jira): prioritized, tagged by theme, dependencies flagged.
2. **Execution rulebook**: Kanban columns, WIP limits, cadences, Definition of Ready/Done, QA gates.
3. **Staffing go**: Staffing Manager prepares sourcing plan; Head of Ops signs.

**Checklist**
- [ ] Backlog covers entire roadmap (use import template).
- [ ] Execution rulebook reviewed with Tech Lead + QA.
- [ ] Staffing authorization email filed.

---

### State 2 – Capacity Installation (Owner: Staffing Manager, SLA 4 days)
**Steps**
1. **Staff minimal run team** (≥1 dev) via Allocate Delivery Resources workflow.
2. **Onboard team**: PPL runs product walkthrough; Tech Lead demos architecture + tooling; document in onboarding tracker.
3. **Tooling & envs**: Tech Lead confirms repositories, CI/CD, monitoring, staging/prod parity.

**Exit criteria**
- [ ] Named developers active in tooling.
- [ ] Smoke tests pass on staging + prod.
- [ ] Access matrix signed off.

---

### State 3 – Run Activation (Owner: PPL, SLA 2 days)
**Steps**
1. **Kanban go-live** – move top backlog items into "Ready"; schedule standups/reviews; communicate cadence.
2. **Responsibility map** – publish R&R grid (PM, TL, QA, Ops, Escalations).
3. **Activation note** – send to stakeholders with board links, SLA, first sprint goals.

**Exit:** Kanban contains committed work; team acknowledges kickoff; no open installation task remains.

## 5. Governance Controls
- **KPIs:**
  - Installation lead time ≤ 10 business days.
  - % of inputs re-opened post-run < 5%.
- **Health Checks:** Weekly for first month (backlog health, env stability, staffing churn).
- **Stop Rules:** Missing documentation, no PM backup, or failed environment smoke tests.

## 6. Templates & Links
- Input validation memo template.
- Delivery Operating Model template (pulled from Governance/System Guide).
- Staffing authorization email template.
- Run activation announcement template.

## 7. Post-Completion Actions
- Capture retrospective within 2 weeks to update standards.
- Feed environment learnings into Infrastructure repository.
- Ensure backlog grooming cadence scheduled for next 4 weeks.
