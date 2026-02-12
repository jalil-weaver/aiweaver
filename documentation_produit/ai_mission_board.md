# AI Mission Board – NFA
_Last update: 2026-02-12_

## Mission format
```
- id
- title
- status: Ready | In Progress | Blocked | Done
- owner_ai / owner_human
- description
- acceptance_criteria
- inputs
- constraints
- metrics
```

---

## Mission 1
- **id**: M1
- **title**: Head Office Catalogue module
- **status**: Ready
- **owner_ai**: Dev Squad (Web) + Test Sentinel
- **owner_human**: Tech Lead (Accountable)
- **description**: Build catalogue list, product detail, template visibility as per Product Doc §3.1 (Catalogue & Template Visibility). Includes search, filters, loading/empty states, detail view + ordering entity selection.
- **acceptance_criteria**:
  - Catalogue shows templates + standard products with filters (category, availability, visibility).
  - Loading, empty, error states implemented.
  - Detail view allows selecting ordering entity and adds to cart.
  - Template visibility page allows toggling per store + local price (markup 0-30%).
  - Playwright suite `catalogue.spec.ts` passes.
- **inputs**: `NFA_product_doc.md` §3.1, design PDFs (`Head office/Catalogue.pdf`, `Template.pdf`).
- **constraints**: use Supabase RPC `list_catalogue_items`, `get_product_detail`; respect price formula (Product Doc §4.1).
- **metrics**: API response <500ms for default filters; zero critical bugs in QA report.

## Mission 2
- **id**: M2
- **title**: Head Office Dashboard & Issues
- **status**: Ready
- **owner_ai**: Dev Squad (Web) + Release Auditor
- **owner_human**: Product Lead
- **description**: Implement dashboard widgets (KPI, Orders with Issues, Top Templates, Inventory Alerts) with live data.
- **acceptance_criteria**:
  - KPI cards display total orders, GMV, active stores, templates, conversion rate.
  - Orders with Issues widget shows last 20 blocker issues with status.
  - Top Templates monthly ranking rendered.
  - Inventory alert list from stock status `LOW/OUT/UNKNOWN`.
  - Metrics align with `get_dashboard_metrics` RPC test snapshot.
- **inputs**: Product Doc §3.1 (Dashboard), Technical Doc §4 (RPC), `Dashboard.pdf`.
- **constraints**: Use Supabase RPC; ensure role-based access (HO admins only).
- **metrics**: Dashboard load <1s; no accessibility violations (axe tests).

## Mission 3
- **id**: M3
- **title**: Mobile App – Catalogue & Ordering
- **status**: Ready
- **owner_ai**: Dev Squad (Mobile) + Test Sentinel
- **owner_human**: Mobile Lead
- **description**: Build React Native flows for catalogue browsing, product detail, cart, checkout, order history.
- **acceptance_criteria**:
  - Offline cache stores last 50 items.
  - Detail screen validates required fields, triggers `order_submit` edge function.
  - Cart groups items by supplier; handles stock status logic.
  - Detox E2E scenario "Place order" passes.
- **inputs**: Product Doc §§3.3, 4.2; design PDFs `Mobile appstore/*.pdf`.
- **constraints**: Use Expo + Supabase Realtime; enforce authentication guard.
- **metrics**: App cold start <3s; API errors <1% in QA run.

## Mission 4
- **id**: M4
- **title**: Admin Panel – Suppliers & Products
- **status**: Ready
- **owner_ai**: Dev Squad (Web/Admin)
- **owner_human**: Global Admin Lead
- **description**: Build admin pages for supplier CRUD, product master data, elevated login.
- **acceptance_criteria**:
  - Supplier form with lead time, feed URL, contact info.
  - Product master page editing base price, markup default, attachments.
  - Login requires MFA flag for admin users.
- **inputs**: Product Doc §3.2, Technical Doc §§2, 7; design PDFs `Admin panel/*.pdf`.
- **constraints**: Enforce RLS scope; audit actions logged in `events_audit`.
- **metrics**: All admin actions have audit record; Sentry alerts=0.

## Mission 5
- **id**: M5
- **title**: Edge Functions – Order, Inventory, FX
- **status**: Ready
- **owner_ai**: Backend Agent (Supabase Edge)
- **owner_human**: Tech Lead
- **description**: Implement `order_submit`, `inventory_ingest`, `fx_refresh`, `issue_monitor` functions with tests.
- **acceptance_criteria**:
  - Unit + integration tests passing.
  - Supplier feed ingestion handles CSV + API.
  - Issues severity logic triggers Slack via pg_notify.
- **inputs**: Technical Doc §§3, 10.
- **constraints**: TypeScript edge functions, 95% test coverage for critical paths.
- **metrics**: CI pipeline green; functions deploy to Supabase without errors.

## Mission 6
- **id**: M6
- **title**: Testing & QA Automation
- **status**: Ready
- **owner_ai**: Test Sentinel + Release Auditor
- **owner_human**: QA Lead
- **description**: Set up Playwright, Detox, unit tests per module. Integrate with CI, provide test suites for State 2 & 3.
- **acceptance_criteria**:
  - CI runs unit + E2E per PR.
  - Regression suite covers catalogue, order, admin flows.
  - QA report template generated for Final Validation.
- **inputs**: Technical Doc §8.
- **constraints**: Must run in GitHub Actions; fails block merges.
- **metrics**: Test coverage >80%; pipeline duration <15 min.

---
_Missions can be updated (status / new IDs). Agents read this board to pick Ready missions and update status/logs._
