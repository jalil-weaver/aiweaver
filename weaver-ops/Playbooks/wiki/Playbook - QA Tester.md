# Function Playbook – QA / Tester

## Mission
Detect defects before production by validating functional, technical, and regression scenarios across the delivery lifecycle. QA/Testers enforce quality gates in Development Execution (State 2) and Final Validation (State 3).

## Ready-to-Start Checklist
- [ ] Access to staging/prod read-only, test accounts, feature flags, and monitoring dashboards confirmed.
- [ ] Product, technical, and design specs reviewed; acceptance criteria imported into the test management tool.
- [ ] Test data strategy defined (seed scripts, anonymized datasets, mock services).
- [ ] Automation framework configured; pipeline permissions granted.
- [ ] Incident history reviewed to focus on high-risk areas.

## Operating Rhythm
### Daily
- Review new tickets entering “Ready for Test”; clarify gaps immediately.
- Execute regression + exploratory tests on completed stories; log defects with full repro details.
- Sync with Developers on fixes and retests.
- Monitor automated test runs and unblock failures.

### Weekly
- Update regression suite coverage; retire obsolete cases.
- Present quality metrics during delivery review (defect trends, automation health, environment issues).
- Refresh test data and reset environments if needed.

## Execution Guidance
1. **Test Planning** – derive test cases directly from acceptance criteria and business rules; prioritize critical paths.
2. **Automation First** – add/maintain automated checks (API, UI, contract) for stable flows.
3. **Manual & Exploratory** – focus manual effort on new, complex, or high-risk functionality.
4. **Defect Lifecycle** – log severity, steps, expected vs actual, environment, screenshots; verify fixes promptly.
5. **Release Qualification** – ensure blocking/critical defects = 0 before Final Validation signoff.
6. **Post-Deployment Smoke** – coordinate with Tech Lead to validate production after release.

## Collaboration Interfaces
| Partner | Collaboration |
| --- | --- |
| Project/Product Lead | Clarify acceptance criteria, scope changes, go/no-go decisions. |
| Developers | Reproduction steps, fix verification, automation hooks. |
| Tech Lead | Test strategy, tooling, environment stability, incident response. |
| Delivery Owner | Release readiness reporting. |

## Quality & KPIs
- **Defect detection rate**: ≥ 80% of total defects found pre-production.
- **Test coverage**: 100% of critical flows under automated or manual regression.
- **Bug turnaround**: blockers retested within 1 business day of fix.
- **Escaped defects**: < 1 blocker/critical per release.

## Guardrails
- No ticket passes QA without documented test evidence.
- Escalate environment instability immediately; do not sign off on compromised runs.
- Separate accounts for testing vs production; never share credentials.
- Automation suite failures must be investigated before deploying.

## Handoffs
- Maintain living regression catalog + automation report links.
- Provide release quality summary (open defects, test coverage, risks) before Final Validation.
- Archive test cases when features sunset; update documentation_produit with learnings.
