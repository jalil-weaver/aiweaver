# NFA – Product Documentation (AI-ready)

_Last update: 2026-02-12_

## 1. Product Vision

Build a unified purchasing platform named **NFA** that connects Head Office teams, local stores and suppliers around a single catalogue of templates (predefined bundles) and standard products. The platform must cover:

1. **Head Office Web App** – drives catalogue management, template visibility, stock & store monitoring, order orchestration.
2. **Admin Panel** – back-office for global admins (Weaver team) to operate head-office accounts, suppliers and elevated controls.
3. **Mobile App Store** – lightweight React Native application used by store managers to browse catalogue, place orders, follow statuses and manage their profile/cart.

## 2. Personas & Roles

| Persona | Description | Access Surface | Key Goals |
|---------|-------------|----------------|-----------|
| Global Admin | Internal platform owner, manages head offices, suppliers, catalogues globally | Admin Panel | Ensure data integrity, onboard head offices, monitor escalations |
| Head Office Manager | Runs the retail network for a brand/country. Owns catalogue configuration and oversees orders per store | Head Office Web | Manage templates, pricing, visibility, stock, issues |
| Store Manager | Operates a single physical shop. Places orders, tracks deliveries, manages cart | Mobile App Store | Quickly find products, order, follow order state |
| Supplier Operator | Receives purchase orders, updates fulfillment state | Admin Panel / external integration | Deliver products on time |

## 3. Functional Scope by Module

### 3.1 Head Office Web

1. **Authentication**
   - Email + password login with clear error states.
   - Enforces MFA when flagged by Admin (see Technical Doc for policy).

2. **Dashboard**
   - KPIs: total orders (period selectable), GMV, stores active, templates live, conversion rate.
   - Widgets: "Orders with Issues" (list + reason + severity), "Top Templates of the Month", "Inventory Alerts" (below threshold).

3. **Catalogue Management**
   - Combined view of **Templates** and **Standard Products** with filters: Category, Availability, Visibility status, Tags.
   - Supports empty/loading/error states.
   - Detail view exposes product metadata, images, dimensions, lead time, and allows selecting **Ordering Entity** (store or group) before adding to cart/order.

4. **Template Visibility**
   - Toggle template visibility per boutique, assign local price per currency, set minimum order quantity.
   - Rules: local price = base price (from supplier) * FX rate + local markup (percentage set by HO). Markup defaults to 0 if not set.

5. **Orders**
   - "Global Orders" list with filters (status, supplier, store, issue flag) and quick search.
   - Order detail shows lines, fulfillment status, logistics data, documents.
   - Issue management: statuses = `NO_ISSUE`, `INFO`, `BLOCKER`. Blockers displayed in dashboard widget.

6. **Stock Management**
   - Synced inventory per product per store. Reorder threshold set per store.
   - Stock status derived as:
     - `OK` if quantity >= threshold
     - `LOW` if threshold > qty > 0
     - `OUT` if qty = 0
     - `UNKNOWN` if supplier has not provided data within SLA (24h)

7. **Stores & Accounts**
   - CRUD for store records, assign managers, manage shipping addresses.
   - Head Office Account settings: billing info, payment method, notifications.

### 3.2 Admin Panel

1. **Authentication** – same as Head Office but with Admin role. Supports password reset & session management.
2. **Head Offices** – create/update HO profiles, assign plan, toggle access, reset passwords.
3. **Suppliers** – onboard supplier records, define lead times, attach product catalogues.
4. **Products** – master data for templates & standard SKUs; manages status, categories, attachments.
5. **Orders** – view all global orders, override statuses, escalate issues, export data.
6. **Accounts** – manage admin users, roles, and audit login events.

### 3.3 Mobile App Store

1. **Authentication** – store managers login via email/pass, optional biometric once session established.
2. **Catalogue** – search + filters (category, availability, supplier). Differentiates templates vs products. Handles offline caching (last sync).
3. **Product Detail & Ordering**
   - Shows description, price (local currency), available stores, lead time.
   - Validates required fields (quantity > 0, store, delivery slot). Adds to cart or direct order.
4. **Cart** – list items grouped by supplier; recalculates totals with taxes. Allows edit/remove.
5. **Orders** – history (status timeline: Draft → Submitted → Confirmed → In Preparation → Shipped → Delivered → Issue).
6. **Profile** – store info, contact, notifications, logout.

## 4. Acceptance Rules (Global)

1. **Price Calculation**
   - Base supplier price in EUR stored in product master.
   - FX rate table per currency updated daily (Supabase function `fx_refresh`).
   - Local price = round((base_price * fx_rate) * (1 + local_markup_pct), 2).
   - Markup range enforced 0–30%. Out-of-range triggers validation error.

2. **Order Totals**
   - Line total = local_price * quantity.
   - Order subtotal = sum(line totals).
   - Taxes = subtotal * tax_rate (per store). Taxes stored separately.
   - Grand total = subtotal + taxes + shipping (if applicable).

3. **Stock Sync**
   - Suppliers provide stock feed per SKU/store via API or CSV. Latest feed timestamp stored; `UNKNOWN` status if >24h stale.

4. **Issue Tracking**
   - Issue severity computed from supplier flag or logistic event. `BLOCKER` requires admin action.
   - Dashboard shows last 20 blocker issues + link to order detail.

5. **Visibility**
   - Template visible in store only if: template_status = ACTIVE AND store assigned AND visibility flag = true AND local price set.

6. **Cart Validation (Mobile)**
   - Cannot checkout if stock status `OUT` or `UNKNOWN` (warn). Option to request manual approval for `UNKNOWN`.
   - Mixed suppliers allowed; backend splits order per supplier automatically.

## 5. Backlog Snapshot

| Epic | Description | Key stories |
|------|-------------|-------------|
| HO Dashboard | Provide operational KPIs & issue tracking | HO-001 KPI view, HO-002 Orders with Issues widget, HO-003 Top Templates widget |
| Catalogue & Templates | Manage templates/products lifecycle & visibility | CAT-010 Catalogue list, CAT-020 Product detail, CAT-030 Template visibility per store |
| Ordering & Fulfillment | Head Office monitors orders, stores place orders | ORD-100 Global orders list, ORD-110 Order detail, ORD-200 Mobile order placement |
| Stock & Stores | Track inventory, manage store master data | STK-050 Stock sync & alerts, STR-060 Store CRUD |
| Admin Operations | Onboard HO, suppliers, master data | ADM-001 Admin login, ADM-020 Supplier CRUD, ADM-030 Product master |

(Full backlog lives in Jira/Linear; this doc is the static reference.)

## 6. Dependencies & Constraints

- Payments handled outside scope (manual confirmation via Final Validation state).
- Localization: app must support FR/EN (extendable); currency formatting derived from store locale.
- Accessibility: WCAG 2.1 AA for web interfaces.
- Offline support (mobile): caching last 50 catalogue items + drafts orders.

## 7. Glossary

- **Template**: curated set of products sold together; can be toggled per store.
- **Standard Product**: single SKU available across stores.
- **Head Office**: brand/country-level administrator entity.
- **Store**: physical shop placing orders.
- **Global Order**: aggregated order possibly containing multiple supplier-specific suborders.

---
_Next: see `NFA_technical_doc.md` for architecture & implementation plan._
