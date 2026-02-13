# Workflow Playbook – Development Estimation

> **Goal:** Deliver assumption-free, executable development scenarios (including infra/AI implications) for Sales within 5 business days.

## 1. Quick Reference
- **Trigger:** Product/change/infra inputs submitted for estimation.
- **Exit:** Scenario pack delivered to Sales **or** estimation blocked with documented gaps.
- **Owner:** Delivery Owner.
- **SLA:** 5 business days from acceptance of inputs.

## 2. Input Pathways
Choose one pathway; ensure all required artifacts exist.

| Path | Required Docs |
| --- | --- |
| **A – Full product scope** | Product doc, delivery scenario or roadmap, validated design. |
| **B – Change scope** | Change specification, updated design if impacted. |
| **C – Infra change** | Infrastructure change brief + relevant tech context. |

**Gate Checklist**
- [ ] Inputs mapped to Path A/B/C.
- [ ] Ownership + stakeholders confirmed.
- [ ] No assumptions required (if yes → request clarification).

## 3. Roles & RACI
| Activity | Delivery Owner | Project Lead | Tech Lead | Staffing Manager | AI PO / AI Tech | Sales (Client Interface) | Quality Guardian |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Input sufficiency review | **A/R** | C | C | C | C | C | I |
| Build scenarios | **A/R** | **R** | **R** | **R** | **R** | I | I |
| 15-week enforcement | C | C | **A/R** | C | I | I | I |
| Infra & staffing estimates | C | I | C | **A/R** | I | I | I |
| Package for Sales | **A/R** | C | C | C | C | **R** | **C** |

## 4. Phase Details
### State 0 – Estimation Readiness Check (Owner: Delivery Owner, SLA 0.5 day)
**Checklist**
- [ ] Inputs categorized (A/B/C) with source links.
- [ ] Ambiguities/questions logged.
- [ ] Decision recorded (Proceed / Blocked) with timestamp.

**If blocked:** send gap report to Sales within 4 hours.

---

### State 1 – Scenario Construction (Owner: Delivery Owner, SLA 3 days)
**Steps**
1. **Baseline scenario** – PPL drafts 1-person-per-role plan, timeline, dependencies, high-level risks.
2. **15-week rule** – Tech Lead validates duration ≤15 weeks. If longer, create alternative scenario with increased capacity; capture trade-offs.
3. **Infrastructure integration** – Staffing Manager + Tech Lead document infra setup, tooling, security/compliance, cost ranges (CapEx + OpEx).
4. **AI impact (if applicable)** – AI PO/Tech adds data, model, governance considerations, annotation needs.
5. **Risk scoring** – Use standard risk heatmap (complexity, dependency, environment, team availability).

**Artifacts**
- Scenario workbook (sheet) with baseline + accelerated options.
- Risk & assumption log.

---

### State 2 – Estimation Consolidation (Owner: Delivery Owner, SLA 1.5 days)
**Checklist**
- [ ] Internal coherence review with PPL + Tech Lead complete.
- [ ] Quality Guardian formats client-safe pack (no internal rates, includes scope summary, staffing profile, timeline, risks, infra notes).
- [ ] Sales brief prepared (talk-track, comparison between scenarios, blockers).
- [ ] Version stored in repository with date + author.

**Exit:** Sales acknowledges receipt; CRM updated.

## 5. KPIs & Controls
- **SLA adherence:** ≥90% estimations delivered within 5 business days.
- **Assumption-free rate:** 100%; if assumptions discovered post-handover, log incident.
- **Scenario accuracy:** Variance between estimated vs actual duration < ±20% (tracked quarterly).

## 6. Templates & References
- Input validation form.
- Scenario workbook template (includes 15-week calculator).
- Risk heatmap template.
- Sales handoff deck template.

## 7. Escalation Paths
- Missing inputs → escalate to Sales Director after 2 business days.
- Infra blockers → trigger Infrastructure Change workflow before publishing scenarios.
- AI compliance concerns → notify Governance/Legal.
