# Function Playbook – Frontend Developer

## Mission
Deliver user-facing experiences that match validated design and behavior specs across web clients. Frontend Developers are primary actors during Development Execution and Continuous Delivery runs.

## Ready-to-Start Checklist
- [ ] Repo + design system access granted; Figma shared libraries synced.
- [ ] Product/Design specs reviewed; open questions documented for the PPL/Designer.
- [ ] Shared API contracts understood; mock data available.
- [ ] Local environment aligned with staging (feature flags, environment vars, browsers).
- [ ] Performance budgets, accessibility targets, and analytics requirements known.
- [ ] Definition of Ready/Done acknowledged (UI states, testing, documentation).

## Operating Rhythm
### Daily
- Pull highest priority tickets that meet Definition of Ready.
- Pair with Backend on API/schema changes before coding.
- Validate UI against design system tokens; no ad hoc styling.
- Demo completed work to Designer/QA before moving to “Ready for Test.”

### Weekly
- Participate in design QA sessions to catch drift early.
- Run Lighthouse/perf audits on new experiences.
- Update component library with reusable patterns discovered during sprint.

## Execution Guidance
### Build Flow
1. **Understand UX** – review prototype, motion, and states (loading, error, empty).
2. **Plan architecture** – decide on state management, routing, and component boundaries; confirm with Tech Lead if pattern is new.
3. **Implement** – follow coding conventions, Storybook/component library usage, and hydration rules.
4. **Test** – write unit + integration/UI tests; include accessibility checks (axe) and responsiveness validation.
5. **Analytics & Logging** – implement required events/telemetry.
6. **PR & Review** – include GIF/video + testing evidence.

### Collaboration Interfaces
| Partner | Alignment Topics |
| --- | --- |
| UX/UI Designer | Pixel parity, UX questions, design debt backlog. |
| Backend Developer | API evolution, error handling contracts, caching. |
| QA / Tester | UI regression suites, cross-browser coverage. |
| Product Lead | Scope clarifications, progressive release strategy. |

## Quality & KPIs
- **UI defect escape rate** < 2 per sprint.
- **Core Web Vitals** within target (LCP < 2.5s, CLS < 0.1, INP < 200ms) for new features.
- **Accessibility**: WCAG AA for all interactive flows.
- **Code review response**: ≤4 working hours.

## Guardrails
- Never merge without design QA signoff for user-visible changes.
- Keep design tokens canonical; escalate if token gaps appear.
- Feature flags required for risky releases.
- Document any deviation from validated design before shipping.

## Handoffs
- Update Storybook/component catalog for new reusable pieces.
- Provide release note bullets (user-facing impact + screenshots if applicable).
- Ensure analytics dashboards/event catalogs reflect new events.
