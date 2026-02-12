# NFA – Function & Component Blueprint
_Last update: 2026-02-12_

## 1. Backend (Supabase Postgres + Edge Functions)

| ID | Function | Type | Inputs | Outputs | Notes / Agent |
|----|----------|------|--------|---------|----------------|
| BF-01 | `list_catalogue_items` | RPC (SQL) | Filters: search, category, availability, visibility, store_id | Array of items `{id, type, name, status, price_local, stock_status}` + pagination | Used by HO web + mobile catalogue (Mission M1 & M3). Implements visibility rules + price calc. |
| BF-02 | `get_product_detail` | RPC | `{item_id, item_type, store_id}` | Full detail (metadata, images, local price, allowed stores) | Used by HO detail & mobile detail. |
| BF-03 | `get_dashboard_metrics` | RPC | `{head_office_id, period}` | KPIs: totals, GMV, stores active, top templates, issues list, inventory alerts | Feeds HO Dashboard (M2). |
| BF-04 | `list_orders_with_issues` | RPC | `{head_office_id}` | Issues array `{order_id, severity, reason, updated_at}` | Dashboard widget. |
| BF-05 | `order_submit` | Edge Function (TS) | Cart payload `{store_id, items[], payment_info}` | Creates `orders`, `order_lines`, `suborders`, returns order_id; triggers notifications | Validates stock, splits per supplier, handles issue creation. |
| BF-06 | `inventory_ingest` | Edge Function | Supplier feed (CSV/API) payload, API token | Upsert `inventory_snapshots`, emit events for low/out/unknown | Called via webhook/cron. |
| BF-07 | `fx_refresh` | Edge Function (scheduled) | none (fetches external API) | Updates `fx_rates`, recalculates cached local prices | Runs daily; logs errors to Slack. |
| BF-08 | `issue_monitor` | Edge Function (trigger on suborder status) | Row change event | Inserts into `issues` table, updates `orders.issue_severity`, notifies Slack | Implements severity rules. |
| BF-09 | `template_visibility_upsert` | RPC | `{template_id, store_id, visibility_flag, markup_pct}` | Upserts `template_visibility`, returns computed price | Enforces markup bounds. |
| BF-10 | `stock_status_view` | Materialized view or RPC | `head_office_id` | Aggregated stock per store/product with status | Backing data for inventory alerts. |
| BF-11 | `audit_log_insert` | Trigger | table, action, actor | Insert row in `events_audit` | Called on admin-critical tables. |

## 2. Web Front (Next.js)

| ID | Component / Page | Inputs | Outputs/UI | Notes |
|----|-------------------|--------|-----------|------|
| WF-01 | Login (HO/Admin) | Email, password, MFA token | Session, Supabase auth | Implements states: idle, error, locked. |
| WF-02 | Dashboard page | `get_dashboard_metrics` data | KPI cards, issues list, top templates, alerts | Mission M2. |
| WF-03 | Catalogue list | RPC `list_catalogue_items` results | List view with filters, infinite scroll, states | Mission M1. |
| WF-04 | Product detail drawer | `get_product_detail`, store selections | UI with metadata, ordering entity selector, add-to-cart hook | Links to ordering. |
| WF-05 | Template visibility manager | `template_visibility` records | Table per store, toggle switches, markup input | Validates markup 0-30%. |
| WF-06 | Orders list (Global) | `/rest/v1/orders` + filters | Table, status chips, search | Includes issue badges. |
| WF-07 | Order detail | order + suborders | Timeline, items, supplier info, issue management | Allows admin overrides (role-based). |
| WF-08 | Stock dashboard | `stock_status_view` | Cards + list of low/out items | Links to supplier contact. |
| WF-09 | Stores management | `stores` table | CRUD forms, assign managers | Audit logging. |
| WF-10 | Head Office account settings | `head_offices` data | Billing, notification prefs, API keys | Includes final payment confirmation step. |
| WF-11 | Admin Panel – Suppliers | `suppliers` table | Form/edit pages | Mission M4. |
| WF-12 | Admin Panel – Products | `products` table | Master data form + attachments | Mission M4. |
| WF-13 | Admin Panel – Orders | `/rest/v1/orders` | global oversight + export | Elevated permissions. |
| WF-14 | Admin Panel – Accounts | `users` table | Admin user CRUD, role assign, MFA toggle | Logs to audit. |

## 3. Mobile (React Native)

| ID | Screen / Module | Inputs | Outputs/UI | Notes |
|----|------------------|--------|-----------|------|
| MF-01 | Login | Email/password (Supabase) | Auth session | Stores token securely (secure store). |
| MF-02 | Catalogue list | `list_catalogue_items` (cached) | List filters, offline indicator | Mission M3. |
| MF-03 | Product detail | `get_product_detail`, store context | Detail UI, add to cart | Validates stock status, quantity. |
| MF-04 | Cart | Local storage + server data | Grouped by supplier, totals | Applies price formula + taxes. |
| MF-05 | Checkout | Cart payload | Calls `order_submit`, handles success/failure states | Shows order summary. |
| MF-06 | Order history | `/rest/v1/orders` (filtered) | Timeline view, status icons | Realtime updates. |
| MF-07 | Order detail | order + lines | Tracking info, re-order option | Handles issue display. |
| MF-08 | Profile | `stores` data, user info | Store details, notifications | Logout, biometric toggle. |
| MF-09 | Offline cache manager | Last query results | Provide fallback data | Clears after 48h or logout. |

## 4. Testing & QA Components

| ID | Suite | Inputs | Outputs | Notes |
|----|-------|--------|---------|------|
| QA-01 | Unit tests (web/backend) | Functions (price, stock, issue severity) | Pass/fail | Jest/TS. |
| QA-02 | Playwright E2E (web) | Scenarios (catalogue, dashboard, orders) | Reports, screenshots | Blocks merge if fail. |
| QA-03 | Detox E2E (mobile) | Mobile flows (login, catalogue, checkout) | Pass/fail logs | Runs on CI. |
| QA-04 | Load test (catalogue API) | RPC `list_catalogue_items` under load | Latency metrics | k6 optional. |
| QA-05 | QA report generator | Test results, mission status | Markdown/Notion summary for Final Validation | Owned by Release Auditor agent. |

## 5. Observability & Ops

| ID | Function | Inputs | Outputs | Notes |
|----|----------|--------|---------|------|
| OP-01 | Log pipeline | Supabase logs, Edge logs | Forward to Sentry/Logtail | Alert on errors. |
| OP-02 | Alerts notifier | Edge events (`issue_monitor`, FX fail) | Slack messages (#nfa-alerts) | Reliability monitoring. |
| OP-03 | Deployment orchestrator | GitHub Actions pipeline | Deploy to dev/stage/prod, status updates | Aligns with Workflow State 4.
| OP-04 | Mission board updater | Agent writes status updates | `ai_mission_board.md` changes + PR | Keeps missions in sync. |

## 6. Dependencies Matrix (excerpt)

| Component | Depends on |
|-----------|------------|
| WF-02 Dashboard | BF-03, BF-04, BF-10 |
| WF-03 Catalogue | BF-01, BF-09 |
| MF-05 Checkout | BF-05 |
| BF-05 order_submit | tables `orders`, `order_lines`, `suborders`, RLS policy |
| QA-02 Playwright | WF-02/03/06 |

## 7. Implementation Plan Snapshot

Align missions avec les fonctions ci-dessus :
- M1 couvre WF-03/04/05 + BF-01/09 tests.
- M2 couvre WF-02 + BF-03/04/10.
- M3 couvre MF modules + BF-05 integration.
- M4 couvre WF-11/12/14 + RLS/audit.
- M5 couvre BF-05..08.
- M6 couvre QA-01..05.

---
Ce blueprint complète NFA_product_doc & NFA_technical_doc et sert de check-list pour les agents IA (Dev, Backend, QA, Ops).
