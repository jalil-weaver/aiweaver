# NFA – Technical Documentation

_Last update: 2026-02-12_

## 1. Architecture Overview

| Layer | Stack | Description |
|-------|-------|-------------|
| Web Front (Head Office) | **Next.js 14 / React 18**, TypeScript, Tailwind, Zustand, SSR on Vercel | Responsive web console for head offices; consumes Supabase APIs via RPC / REST. |
| Admin Panel | Same Next.js project with admin routes & RBAC | Admin-specific UI shells, uses same API surface with elevated scopes. |
| Mobile | **React Native (Expo)** targeting iOS/Android | Offline-first catalogue + ordering app; syncs with Supabase via GraphQL subscription + REST fallback. |
| Backend / DB | **Supabase (Postgres 15 + Edge Functions)** | Auth, RLS, database, storage. Business logic in SQL functions + Typescript edge functions (for heavy workflows). |
| Integrations | Supabase webhooks + Edge Functions | Supplier stock feed ingestion, FX rate refresh, notification dispatch. |
| Observability | Supabase logs + Sentry + Logtail | Captures API errors, client logs, performance metrics. |

### Logical Diagram

```
[React / Next.js] --- https ---> [Supabase REST/RPC]
[React Native]  --- https/ws ---> [Supabase REST/RPC + Realtime]
[Edge Functions] <---> External APIs (FX, Suppliers, Notification)
```

## 2. Data Model (Supabase / Postgres)

| Table | Purpose | Key fields |
|-------|---------|------------|
| `head_offices` | Brand/country entity | id (uuid), name, locale, currency, status |
| `stores` | Physical shops | id, head_office_id FK, name, address, time_zone, manager_user_id, status |
| `users` | Supabase auth users (extended) | id, email, role (`GLOBAL_ADMIN`, `HO_ADMIN`, `STORE_MANAGER`), store_id nullable |
| `suppliers` | Supplier profiles | id, name, lead_time_days, contact_info, data_feed_url |
| `products` | Standard products | id, sku, name, description, base_price_eur, default_markup_pct, category, supplier_id, status |
| `templates` | Bundled offerings | id, code, name, description, base_price_eur, image_urls[], components jsonb |
| `template_visibility` | Template availability per store | template_id, store_id, visibility_flag, local_markup_pct, local_currency_price_cache |
| `inventory_snapshots` | Stock per store/product | id, product_id, store_id, quantity, snapshot_at |
| `orders` | Global orders (aggregate) | id (uuid), head_office_id, store_id, grand_total, status, issue_severity, created_at |
| `order_lines` | Line items | id, order_id FK, product_or_template_id, item_type, quantity, unit_price, supplier_id |
| `suborders` | Supplier-specific splits | id, order_id, supplier_id, status, tracking_info |
| `fx_rates` | Currency exchange rates | currency_code, rate_vs_eur, fetched_at |
| `issues` | Logged issues | id, order_id, severity, description, resolved_at |
| `events_audit` | Activity log (admin actions, logins, etc.) | id, actor_user_id, action, payload jsonb, created_at |

### Row-Level Security

- `GLOBAL_ADMIN` full access.
- `HO_ADMIN`: limited to rows with same `head_office_id`.
- `STORE_MANAGER`: limited to store-specific rows (`orders`, `template_visibility`, etc.).
- RLS policies defined per table using Supabase policies referencing `auth.uid()`.

## 3. Business Logic & Edge Functions

1. **`price_calculator` (SQL function)**
   - Input: product_id/template_id, store_id.
   - Output: computed local_price using formula described in product doc.
   - Validates markup range (0–30%).

2. **`order_submit` (Edge Function)**
   - Validates cart payload, checks stock statuses.
   - Splits order into `suborders` per supplier.
   - Triggers notifications (email/webhook) to supplier + head office.

3. **`inventory_ingest` (Edge Function)**
   - Called by suppliers (Bearer token) or scheduled CSV import.
   - Upserts `inventory_snapshots`, computes stock status, emits events for `LOW`/`OUT`/`UNKNOWN`.

4. **`fx_refresh` (Scheduled)**
   - Pulls FX rates (ECB API), updates `fx_rates`, re-runs cached price for affected template_visibility rows.

5. **`issue_monitor` (Edge Function)**
   - Listens to `suborders` status changes; if SLA breached, inserts record into `issues` with severity logic.

6. **Notifications**
   - Supabase `pg_notify` → Edge Function to send Slack/Email for blockers and for final validation readiness.

## 4. API Surface

### REST/RPC Endpoints (via Supabase)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/rpc/get_dashboard_metrics` | POST | Returns aggregated KPIs for HO dashboard. |
| `/rpc/list_catalogue_items` | POST | Filtered list of templates/products with pagination and states. Supports `search`, `category`, `availability`, `visibility`. |
| `/rpc/get_product_detail` | POST | Returns unified detail for product or template, including allowed stores and price. |
| `/rpc/update_template_visibility` | POST | Toggle visibility & markup; enforces role HO_ADMIN+. |
| `/rest/v1/orders` | GET/POST/PATCH | Standard operations (built-in Supabase). Insert uses `order_submit`. |
| `/rest/v1/stores` | CRUD for stores (admin scopes). |
| `/rest/v1/inventory_snapshots` | supplier ingestion (service role). |
| `/rpc/list_orders_with_issues` | POST | Feeds "Orders with Issues" widget. |

### Mobile Sync

- **Realtime**: subscribe to `orders` and `order_lines` via Supabase Realtime for live updates.
- **Offline cache**: use `expo-sqlite` to persist last catalogue query + draft cart.

## 5. Frontend Architecture

- **State management**: Zustand stores per domain (auth, catalogue, orders).
- **Design system**: shared component library; mobile + web align on tokens (Figma sync).
- **Forms**: React Hook Form + Zod validation.
- **Internationalization**: `next-intl` on web, `i18next` on mobile.
- **Testing**: React Testing Library + Playwright for Next.js; Detox for React Native flows.

## 6. DevOps & Environments

| Env | Purpose | Notes |
|-----|---------|-------|
| Local | Developer machines (Supabase local CLI, Expo) | seeded data, mocked supplier feeds |
| Dev | Shared for integration | auto-deploy from `develop` branch, resets nightly |
| Staging | Pre-prod, mirrors prod configs | manual promotion, used for Final Validation state |
| Prod | Live environment | deploy via GitHub Actions after approvals |

### CI/CD

- **GitHub Actions** pipeline:
  1. Lint + unit tests (web + mobile + edge functions).
  2. DB migrations via Supabase CLI (preview → apply).
  3. Build artifacts (Next.js, Expo EAS) and upload to respective stores.
  4. On `main` tag, deploy to Staging; manual approval for Prod.

- **IaC**: Supabase config stored in repo (`supabase/config.toml`). Infrastructure (monitoring, secrets) tracked via Terraform Cloud (optional extension).

## 7. Security & Compliance

- **Auth**: Supabase email/password + optional magic link; MFA enforced for Admin roles (stored in `user_metadata` flag `mfa_required`).
- **RBAC**: Role assigned at signup or via Admin panel; enforced by RLS + frontend route guards.
- **Encryption**: HTTPS everywhere; Supabase storage used for assets with signed URLs.
- **Audit**: All admin actions logged in `events_audit` + pushed to Logtail.
- **PII**: Stores and user data limited to operational info; no payment data stored.

## 8. Testing Strategy

- **Unit**: Functions (pricing, stock status) fully covered.
- **Integration**: Edge functions tested via Supabase emulator.
- **E2E**: Playwright scenarios for HO/Admin flows; Detox for mobile order journey.
- **Performance**: Synthetic tests on key APIs (catalogue list < 500ms for top filters).
- **QA automation**: Hook into Workflow State 2 “Test Sentinel” agent to run regression suite every merge.

## 9. Deployment & Monitoring

- Deployments triggered via GitHub Actions; `release` branch maps to Prod.
- Monitoring: Sentry for frontend/mobile, Supabase log drains for backend, UptimeRobot for public endpoints.
- Alerting: Slack channel `#nfa-alerts` (blocker issues, deployment failures, FX sync fail, supplier feed stale >24h).

## 10. Appendix – Key Functions & Formulas

- **Stock status**
  ```sql
  CASE
    WHEN quantity IS NULL OR (now() - snapshot_at) > interval '24 hours' THEN 'UNKNOWN'
    WHEN quantity = 0 THEN 'OUT'
    WHEN quantity < reorder_threshold THEN 'LOW'
    ELSE 'OK'
  END
  ```
- **Issue severity**
  - Supplier flag `critical` OR logistic SLA > 48h OR payment pending > 5d ⇒ `BLOCKER`
  - Supplier flag `warning` OR SLA 24–48h ⇒ `INFO`
  - Else `NO_ISSUE`

- **Order status transitions**
  - Draft → Submitted → Confirmed → In_Preparation → Shipped → Delivered
  - Issue states overlay; cannot move to Delivered if issue severity `BLOCKER`.

---
This document plus `NFA_product_doc.md` constitute the full Framing output used by Estimation & Development workflows.
