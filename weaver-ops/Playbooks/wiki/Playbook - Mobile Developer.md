# Function Playbook – Mobile Developer

## Mission
Build and maintain native or cross-platform mobile applications that mirror the validated product experience, ensuring stability across devices, stores, and environments.

## Ready-to-Start Checklist
- [ ] Access to mobile repositories, certificates/provisioning profiles, app store consoles, and CI pipelines confirmed.
- [ ] Mobile-specific product/design specs reviewed (platform guidelines, gestures, offline expectations).
- [ ] API contracts + mobile-specific endpoints validated with Backend.
- [ ] Device matrix defined (OS versions, screen sizes); simulators/emulators configured.
- [ ] Crash/analytics tooling (Firebase, Sentry, etc.) connected to project.
- [ ] Release process (beta channel, store submission steps) documented.

## Operating Rhythm
### Daily
- Sync with Frontend/Backend on shared components and API changes.
- Keep feature branches short; ensure builds stay green on CI.
- Triage mobile crash/analytics alerts.

### Weekly
- Run device lab smoke tests on current development build.
- Align with QA on exploratory tests and automation coverage.
- Review store feedback and surface product insights.

## Execution Guidance
1. **Architect features** respecting platform guidelines (navigation stacks, lifecycle events, background tasks).
2. **Optimize performance & battery**; profile heavy flows before merging.
3. **Handle offline & error states** explicitly per documentation.
4. **Implement feature flags/remote config** for staged rollout.
5. **Automate tests** (unit + UI) and run on target OS versions.
6. **Prepare builds** – update versioning, changelog, and release notes for each increment.

## Collaboration Interfaces
| Partner | Topics |
| --- | --- |
| Tech Lead | Architecture choices, libraries, native module decisions. |
| Backend Devs | API evolution, pagination, push notifications. |
| QA / Tester | Device coverage, exploratory testing, test data. |
| Product Lead | Rollout plans, store submission timelines, feature gating. |

## Quality & KPIs
- **Crash-free sessions** ≥ 99%.
- **App start time** within platform benchmarks (<2s cold start if possible).
- **Store rating** impact monitored; respond to regressions within 48h.
- **Release cadence adherence** (as defined in delivery plan).

## Guardrails
- Do not ship without running builds on minimum + latest OS versions.
- All new permissions require explicit Product + Security approval.
- Store submissions must include QA signoff and Delivery Owner approval.
- Keep secrets/certificates out of repo; rotate according to Ops policy.

## Handoffs
- Provide compiled beta builds to QA before release candidate.
- Update release notes + store listing assets when UI changes.
- Document new mobile-specific monitoring alerts or dashboards.
