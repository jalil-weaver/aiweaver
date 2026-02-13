# Workflow Playbook – Allocate Delivery Resources

> **Goal:** Convert a validated resource request into an assigned and onboarded delivery team within 5 business days, without triggering new hiring.

## 1. Quick Reference
- **Trigger:** Delivery Scenario or Delivery Team definition approved.
- **Exit:** Team assigned, onboarded, and locked in staffing board.
- **Primary Owner:** Staffing / Capacity Manager.
- **Supporting Roles:** Project/Product Lead (PPL), Tech Lead, HR Ops (for tooling access).
- **Toolstack:** Staffing board (Notion), Availability spreadsheet, Slack #staffing, HRIS, Onboarding checklist template.

## 2. Entry Checklist
Tick every item before opening State 0.
- [ ] Validated request with roles, seniority, tech stack, allocation %.
- [ ] Start window ≤ 2 weeks away (or explicit approval for longer).
- [ ] Delivery documentation + project brief accessible.
- [ ] PM + Tech Lead identified and available for reviews.

If any box unchecked → send request back to requester. No partial starts.

## 3. Roles & RACI
| Activity | PPL | Tech Lead | Staffing / Capacity | HR Ops |
| --- | --- | --- | --- | --- |
| Validate request completeness | C | C | **A/R** | I |
| Assess availability | C | I | **A/R** | I |
| Validate technical fit | C | **A/R** | C | I |
| Communicate assignments | I | I | **A/R** | C |
| Onboard + accesses | **A/R** | C | C | **R** |
| Lock staffing board | I | I | **A/R** | C |

## 4. Execution Flow
### State 0 – Availability Assessment (≤1 day)
**Owner:** Staffing / Capacity Manager

**Checklist**
- [ ] Translate request into explicit criteria (role, seniority, skills, %FTE, duration, time zone).
- [ ] Update bench sheet with latest availability + planned vacations.
- [ ] Consult hiring pipeline (read-only) for near-start candidates.
- [ ] Produce a single availability table (Available / Under Consideration / Not Available) with rationale.

**Artifacts**
- Availability table (Google Sheet tab, versioned).
- Decision note: "Available" or "Unavailable" with supporting evidence.

**Go / No-Go**
- Go if ≥ 90% of requested capacity can start within window.
- No-Go if not; escalate to Delivery Owner with summary + options.

---

### State 1 – Team Selection (≤2 days)
**Owner:** Staffing / Capacity Manager

**Checklist**
- [ ] Draft concrete allocation (names, roles, % allocation, start date, overlap period, risk notes).
- [ ] Run 30-min review with Tech Lead → confirm stack coverage, previous project fit, language/availability constraints.
- [ ] Document validation outcome (Accepted / Rejected + reasons).
- [ ] If rejected, iterate within 24h; after two rejections escalate to Delivery Owner.

**Artifacts**
- Team proposal deck/table (slide or Notion) with per-role justification.
- Tech validation log (date, reviewer, verdict).

**Go / No-Go**
- Go only with explicit Tech Lead signoff captured in writing.

---

### State 2 – Assignment Confirmation (≤2 days)
**Owner:** Staffing / Capacity Manager

**Checklist**
- [ ] Send assignment pack to each developer (template includes project summary, role expectations, start date, cadence, escalation path). Capture written acknowledgment.
- [ ] PPL runs onboarding call + grants accesses within 48h.
- [ ] HR Ops updates HRIS + payroll allocations.
- [ ] Staffing board + Availability sheet updated to "Locked" status.
- [ ] Notify Finance if billing rates change.

**Artifacts**
- Assignment communication log.
- Onboarding checklist per dev (stored in project workspace).
- Updated staffing board screenshot or export.

**Exit Criteria**
- 100% of roles acknowledged and onboarded.
- Staffing board shows LOCKED status with workflow ID.

## 5. Operational Controls
- **SLA:** 5 business days end-to-end; daily reminder until closed.
- **KPIs:**
  - Fill rate (% workflows ending with full staffing) ≥ 95%.
  - Cycle time (State 0 → State 2) median ≤ 4 days.
- **Escalations:** If availability gap >2 weeks, inform Delivery Owner + Sales to renegotiate scenario.

## 6. Templates & Links
- Assignment email template.
- Onboarding checklist template.
- Staffing board URL.
- Availability sheet URL.

## 7. Post-Completion
- Schedule a 2-week staffing health check with PPL.
- Feed learnings (capacity gaps, repeated skills shortages) to Recruitment Planning deck.
