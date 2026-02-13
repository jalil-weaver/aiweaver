# Workflow Playbook – Infrastructure Change

> **Goal:** Evaluate, design, and decide on infrastructure changes before execution to protect delivery timelines, cost, and reliability.

## 1. Quick Reference
- **Trigger:** Tech Lead submits Infrastructure Change Brief for an active delivery or maintenance project.
- **Exit:** Infrastructure Change Proposal decided (Approve / Reject / Adjust) with routed next steps.
- **Owner:** Tech Lead (States 0–2), Delivery Owner (State 3).
- **SLA:** 7 calendar days from brief acceptance.

## 2. Intake Checklist
- [ ] Infrastructure Change Brief complete (problem, impact, urgency, constraints).
- [ ] Access to current architecture, infra diagrams, monitoring, cost data.
- [ ] Stakeholders mapped (Tech Lead, Delivery Owner, Finance, Security).

## 3. Stage Instructions
### State 0 – Qualification (Owner: Tech Lead, SLA 0.5 day)
**Checklist**
- [ ] Validate trigger is infrastructure (scale, reliability, compliance, cost) vs. pure feature work.
- [ ] Confirm change cannot be handled inside regular backlog tasks.
- [ ] Decide Accept / Reject; document rationale.

**Exit Artifact:** Qualification log referencing brief ID.

---

### State 1 – Infrastructure Impact Analysis (Owner: Tech Lead, SLA 2 days)
**Steps**
1. **Current state review** – topology, capacity, SLAs, monitoring signals, incident history.
2. **Risk identification** – performance limits, SPOFs, compliance gaps, cost spikes.
3. **Required change list** – map each risk to potential infra responses.

**Artifacts:** Impact analysis memo, updated architecture diagram (current state), risk register entries.

---

### State 2 – Solution & Estimation (Owner: Tech Lead, SLA 3 days)
**Checklist**
- [ ] Target architecture drafted (diagram + narrative).
- [ ] Migration/runbook approach described (phases, rollback plan).
- [ ] Cost estimation (CapEx/OpEx, tooling/licensing, team effort) with assumptions.
- [ ] Risk & dependency matrix (security review, data migration, change windows).
- [ ] Draft Infrastructure Change Proposal compiled (PDF/Deck).

**Collaboration:** Finance validates cost ranges; Security reviews compliance items.

---

### State 3 – Decision & Routing (Owner: Delivery Owner, SLA 1.5 days)
**Checklist**
- [ ] Tech Lead presents proposal to Delivery Owner + stakeholders.
- [ ] Decision recorded:
  - **Approve** → define execution workflow (Development, DevOps run, vendor engagement) + funding source.
  - **Reject** → log reason; close brief.
  - **Adjust** → send back to State 2 with feedback + deadline.
- [ ] Communication sent to project + Finance + Ops.

**Exit Artifact:** Signed decision note + routing instructions.

## 4. Controls & KPIs
- **Approval lead time:** ≤7 days.
- **Proposal completeness score:** 100% of proposals include cost, risk, migration sections.
- **Execution alignment:** Approved proposals linked to downstream delivery tickets before work starts.

## 5. Templates & Tools
- Infrastructure Change Brief form.
- Impact analysis worksheet (capacity, risk, compliance tabs).
- Architecture diagram templates (C4 + infra layers).
- Costing spreadsheet (CapEx/OpEx + sensitivity analysis).
- Decision note template.

## 6. Escalations
- If new infra demands external vendor spend > budget threshold → involve Finance lead before approval.
- For security/compliance risks, notify Governance & Security team immediately; approval contingent on their signoff.
