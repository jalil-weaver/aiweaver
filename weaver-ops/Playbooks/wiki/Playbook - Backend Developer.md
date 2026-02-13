# Function Playbook – Backend Developer

## Mission
Build and maintain the product’s server-side logic so that validated features ship with predictable quality, security, and performance. Backend Developers execute inside the Development workflow (State 2 – Development Execution) and support Continuous Delivery runs once activated.

## Ready-to-Start Checklist
Complete this checklist before accepting any ticket in a new project:
- [ ] Access to repositories, CI/CD, secrets manager, and observability stack confirmed.
- [ ] Read validated Product & Technical documentation relevant to owned domains.
- [ ] Design/behavior specs for upcoming backlog items reviewed; ambiguities logged with the Project/Product Lead (PPL).
- [ ] Local environment mirrors staging (env vars, feature flags, sample data).
- [ ] Definition of Ready / Definition of Done understood and acknowledged.
- [ ] Security & compliance requirements (PII handling, logging rules, retention) noted.

## Operating Rhythm
### Daily
- Pull highest-priority items from Kanban “Ready” column only.
- Pair with Frontend/Mobile peers on API contracts before implementation.
- Keep PRs small (≤400 LOC diff) and request review within the same day.
- Update ticket status + blockers in delivery tooling before stand-up.

### Weekly
- Participate in backlog refinement to anticipate complex integrations.
- Review observability dashboards for error trends; propose fixes.
- Align with QA on upcoming test scenarios and data fixtures.

## Execution Guidance
### Build & Review Flow
1. **Clarify behavior** – confirm acceptance criteria and integration points; push back if documentation is incomplete (no guesswork).
2. **Design first** – outline data models, service boundaries, and failure modes; document decisions in ADRs when material.
3. **Implement** – follow branching strategy, linters, and commit conventions.
4. **Self-test** – unit + integration tests mandatory; ensure automated tests cover edge cases.
5. **Security scan** – run dependency and secret scanners locally before PR.
6. **Pull Request** – include context, screenshots/traces when relevant, and testing evidence.
7. **Review others** – aim for ≥2 peer reviews per day to keep flow moving.

### Collaboration Interfaces
| Partner | Touchpoints |
| --- | --- |
| Tech Lead | Architecture decisions, code reviews for complex changes, incident response. |
| Frontend / Mobile | API design, feature toggles, shared DTOs. |
| QA / Tester | Test data, defect triage, reproduction steps. |
| DevOps / Infra | Environment readiness, deployment validations. |

## Quality & KPIs
- **Lead time per ticket** ≤ 3 days average.
- **Escaped bugs** (post-production) < 2 per sprint attributable to backend.
- **Automated test coverage** ≥ 70% on critical services.
- **Code review SLAs**: respond within 4 business hours.

## Guardrails
- Never merge without at least one peer review + green CI.
- Raise a change request if scope deviates from validated documentation.
- No direct hotfixes on main unless Delivery Owner approves incident mode.
- Secrets, credentials, and API keys must stay outside source control.

## Handoffs & Documentation
- Update swagger/OpenAPI specs after each API change.
- Document new environment variables, migrations, and runbooks in the repo wiki.
- Provide release notes bullet for every backend-impacting deployment.
