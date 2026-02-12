# NFA – Test Strategy & Suites
_Last update: 2026-02-12_

## 1. Testing stack

| Layer | Tooling | Purpose |
|-------|---------|---------|
| Unit (web/mobile/backend) | Jest + ts-jest + React Testing Library + Supabase emulator | Cover pure functions, hooks, SQL/edge logic |
| Integration backend | Supabase CLI test runner + k6 (optional) | Validate RPC + edge functions end-to-end |
| Web E2E | Playwright (Chromium/WebKit/Firefox) | Head Office + Admin Panel flows |
| Mobile E2E | Detox (Expo-managed) | Catalogue > Cart > Checkout > Orders |
| Workflow runner | GitHub Actions (node + supabase + expo), caching to keep pipeline <15min | Auto-runs on PR and schedule |

Tests executed via `npm run test`, `npm run test:e2e:web`, `npm run test:e2e:mobile`, etc. GitHub Actions pipeline orchestrates all suites + reports to Slack.

## 2. Unit test suites (initial backlog)

| ID | Target | Description |
|----|--------|-------------|
| UT-01 | `priceCalculator` (TS & SQL) | Verify markup bounds, FX rounding, store-specific behavior |
| UT-02 | `stockStatus` util | Ensures status mapping (OK/LOW/OUT/UNKNOWN) per quantity + snapshot age |
| UT-03 | `issueSeverity` helper | Tests severity from supplier flags, SLA breaches, payment pending |
| UT-04 | Frontend hooks (`useCatalogue`, `useDashboard`) | Mock RPC responses, ensure loading/error states |
| UT-05 | Mobile state stores (Zustand) | Cart grouping, offline cache serialization |
| UT-06 | Edge function validators (`order_submit`) | Schema validation, splitting logic, rejection cases |
| UT-07 | RLS policies (SQL tests) | Ensure store manager cannot access other HO data (Supabase policy tests) |

## 3. Integration tests (backend)

| ID | Scenario | Steps |
|----|----------|-------|
| IT-01 | Order submission happy path | Seed store/products -> call `order_submit` -> expect orders + suborders inserted, Slack notification stub called |
| IT-02 | Order blocked by stock | Force stock = OUT -> expect error `STOCK_OUT` |
| IT-03 | Inventory ingest CSV | Upload sample CSV -> expect inventory snapshots updated, alerts created |
| IT-04 | FX refresh | Mock ECB endpoint -> run function -> fx_rates updated, template prices recalculated |
| IT-05 | Issue monitor | Update suborder to "Delayed" >48h -> expect issue record + severity BLOCKER |

## 4. Web E2E scenarios (Playwright)

| ID | Flow | Steps |
|----|------|-------|
| E2E-W-01 | HO login & dashboard | Login → verify KPI cards, issues widget data |
| E2E-W-02 | Catalogue browse & detail | Apply filters → open detail → change ordering entity → add to cart (mock) |
| E2E-W-03 | Template visibility | Toggle visibility, set markup, confirm price update |
| E2E-W-04 | Global orders list & detail | Search order, open detail, view timeline, mark issue resolved |
| E2E-W-05 | Admin supplier management | Admin login (MFA) → create supplier → edit feed URL → verify audit log |
| E2E-W-06 | Admin product master | Create/modify product, attach asset, ensure HO sees update |
| E2E-W-07 | Stock dashboard | Trigger inventory ingest → verify alerts appear → open store detail |

Each scenario uses seeded Supabase data. Playwright config handles multi-role auth (fixtures).

## 5. Mobile E2E scenarios (Detox)

| ID | Flow | Steps |
|----|------|-------|
| E2E-M-01 | Login + sync | Launch app, login, verify offline cache created |
| E2E-M-02 | Catalogue search | Search template, apply filter, open detail |
| E2E-M-03 | Add to cart & checkout | Add product, edit quantity, checkout → expect success view |
| E2E-M-04 | Stock restriction | Attempt to order OUT-of-stock item → expect block message |
| E2E-M-05 | Order history updates | Place order, navigate to history, see status timeline, simulate realtime update |
| E2E-M-06 | Profile & logout | Update notification toggle, logout, ensure session cleared |

## 6. QA automation sequencing

1. **Pre-commit** – run UT-01..UT-07 locally (husky hook optional).
2. **PR pipeline** –
   - Jest + integration tests (Supabase emulator).
   - Playwright smoke (E2E-W-01..W-03 at minimum).
   - Detox smoke (E2E-M-01..M-03 on Android emulator headless).
3. **Nightly** – full Playwright/Detox suites + k6 load on `list_catalogue_items`.
4. **State 3 (Final Validation)** – Release Auditor triggers full regression and exports QA report (QA-05).

## 7. Tooling setup

- **GitHub Actions** workflow `.github/workflows/tests.yml`:
  1. `setup-node`, `setup-supabase`, `setup-expo`.
  2. Cache npm + supabase downloads.
  3. Jobs: `unit`, `integration`, `playwright`, `detox` (matrix per OS).
  4. Upload artifacts (screenshots, logs) on failure.
  5. Notify Slack (#nfa-builds) via webhook.

- **Configs**:
  - Playwright config in `/apps/web/playwright.config.ts` (multi-role fixtures, baseURL per env).
  - Detox config in `apps/mobile/.detoxrc.js` with build/test commands.
  - Supabase emulator config `supabase/config.json` for integration tests.

## 8. Ownership

- **Test Sentinel agent** runs automated suites, reports status to Mission Board.
- **Release Auditor agent** compiles QA report before Final Validation (State 3).
- Humans: QA Lead accountable for M6 mission, approves test coverage.

---
Use this plan to scaffold test directories and CI workflow immediately. Update as missions progress.
