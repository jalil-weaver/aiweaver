# Workflow Playbook – Development Delivery

> **Goal:** Deliver the validated product scope from ready-to-start through production release with zero critical incidents.

## 1. Quick Reference
- **Trigger:** All docs/design validated + commercial agreement signed.
- **Exit:** Product deployed to production, final payment received, delivery closed.
- **Owner:** Project / Product Lead (States 0–2), Delivery Owner (States 3–4).
- **Target Timeline:** 4–12 weeks depending on scope; stage gates enforced.

## 2. Preconditions Checklist
- [ ] Product + Technical documentation approved.
- [ ] Design package approved.
- [ ] Delivery scenario validated.
- [ ] Payment schedule + legal conditions confirmed.
- [ ] Governance trackers set up (risk log, RAID, change log).

## 3. Roles & Collaboration
| Role | Responsibilities |
| --- | --- |
| Project / Product Lead | Owns readiness, backlog, scope control, client comms. |
| Tech Lead | Owns engineering workflow, quality, deployments. |
| Delivery Owner | Owns final validation, payment + production authorization. |
| Developers (FE/BE/Mobile) | Build features per Definition of Done. |
| QA/Test Lead | Continuous testing + release signoff. |
| Client Interface | Approvals, payments, UAT. |

## 4. Stage Instructions
### State 0 – Ready to Start (Owner: PPL | SLA 2 days)
**Checklist**
- [ ] Functional + technical docs cross-reviewed; questions resolved.
- [ ] Design-prototype parity confirmed; missing flows flagged.
- [ ] Readiness note signed by PPL + Tech Lead.

**Artifacts:** Readiness memo, updated risk log.

---

### State 1 – Parallel Setup (Owner: PPL | SLA 5 days)
**Streams & Deliverables**
1. **Work organization** – Kanban/Jira board, cadences, Definition of Ready/Done, review calendar.
2. **Infrastructure & environments** – TL ensures infra-as-code, CI/CD, monitoring.
3. **Staffing** – run "Allocate Delivery Resources"; ensure contracts signed.
4. **Tooling & repos** – repo structure, branch strategy, code quality gates, secrets management.
5. **External access** – APIs, analytics, vendor accounts.

**Exit check:** Board + tooling live, people allocated, infra ready, access matrix complete.

---

### State 2 – Development Execution (Owner: Tech Lead | Duration variable)
**Operating Rules**
- Sprint/Kanban cadence documented; every card has acceptance criteria.
- Branch strategy enforced (PR review, CI checks mandatory).
- QA runs continuous regression; bug SLA: blocker <1d, critical <2d.
- Scope changes use Framing Change + Development Estimation before entering backlog.
- Weekly delivery review: burn-up, quality, risks.

**Exit criteria:** 100% planned scope built; no blocker/critical bugs; release notes drafted.

---

### State 3 – Final Validation (Owner: Delivery Owner | SLA 3 days)
**Steps**
1. **Technical validation** – TL signs stability + performance, security checklist.
2. **Functional validation / UAT** – PPL + client review vs. acceptance criteria.
3. **Commercial gate** – Finance confirms payment; Delivery Owner records go/no-go.

**Artifacts:** Validation report, payment confirmation, deployment plan.

---

### State 4 – Production Switch (Owner: Delivery Owner | SLA 2 days)
**Checklist**
- [ ] Deploy release to production following runbook.
- [ ] Post-deploy verification (monitoring, smoke tests, key user check).
- [ ] Handover pack shared (runbooks, admin access, support contacts).
- [ ] Delivery closure note sent; project archived.

**Exit:** Production stable, support owner acknowledged, closure recorded.

## 5. Monitoring & KPIs
- **Delivery predictability:** Actual vs planned end date ±10%.
- **Quality:** ≤2 critical bugs per release window.
- **Customer satisfaction:** Client NPS at closure ≥8/10.

## 6. Templates & Tools
- Readiness memo template.
- Setup checklist workbook.
- Sprint/Kanban board template.
- QA signoff form.
- Deployment + rollback runbook.
- Closure communication template.

## 7. Risk Controls
| Risk | Mitigation |
| --- | --- |
| Starting dev with missing inputs | Enforce State 0 approval; escalate to Governance. |
| Setup delays blocking execution | Run weekly setup standups; escalate blockers >48h. |
| Scope creep | Mandatory change workflow; maintain change log. |
| Payment missing pre-production | Delivery Owner blocks State 4 until Finance confirmation. |

## 8. Post-Delivery
- Run post-mortem within 10 business days.
- Feed improvements into System Guide + playbooks.
- Update maintenance/continuous delivery workflows with lessons learned.
