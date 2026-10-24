# Technology Comparison

**Project:** Student Digital Profile Information System
**YouTrack task:** SDP-4 — Technology Comparison
**Author:** Rakhat Dosmagambetov (Backend Developer)
**Date:** 2026-10-23

---

## 1. Purpose

This document compares alternatives for the key technical decisions of the Student Digital Profile Information System and justifies the selected technology stack. Each decision is evaluated against the project requirements listed in Section 2, not against general popularity.

Seven decisions are compared:

1. Frontend framework
2. Core backend platform (profile module and REST API)
3. Data processing service (import, cleaning, aggregation)
4. Database
5. Component interaction (API style)
6. Authentication and role-based access control
7. Data visualization library

(Decisions 1–4 cover the mandatory "at least three key decisions"; 5–7 are included because they directly affect requirements on access control and dashboards.)

## 2. Requirements that drive the choice

The criteria below are taken from the Project Proposal (`docs/01-proposal.md`, Sections 5–8).

| ID | Driver | Source in proposal |
|---|---|---|
| D1 | Strongly related data: students, groups, courses, semesters, grades, credits, achievements | 7.1 B, C |
| D2 | Correct, reproducible GPA and indicator calculations with configurable grading rules | 5.2 (6), 7.1 C, 8 |
| D3 | Role-based access: student, teacher (only assigned students), administrator | 5.2 (4), 7.1 A |
| D4 | Interactive dashboards: GPA over semesters, academic statistics | 5.2 (7), 7.1 D |
| D5 | Import and processing of educational data (CSV/Excel), synthetic test data | 7.2, 8 |
| D6 | Adaptable to other universities (configurable rules, modular architecture) | 2, 8 |
| D7 | Personal data must be protected (validation, least privilege, no secrets in code) | 7.1 A, NFR |
| D8 | Team of three with existing skills in TypeScript/React/Next.js and Python; limited time | 1, 8, team background |

**Evaluation criteria used in every table:** advantages, disadvantages, performance, scalability, security, maintainability, and fit with the team's skills (D8).

Rating scale in the summary tables: **High / Medium / Low** fit for this project.

---

## 3. Decision 1 — Frontend framework

**Alternatives:** Next.js (React), Angular, Nuxt (Vue).

| Criterion | Next.js (React + TypeScript) | Angular | Nuxt (Vue 3) |
|---|---|---|---|
| Advantages | Largest ecosystem of chart and UI libraries; server-side rendering and routing out of the box; frontend and backend routes in one project | Complete framework (DI, forms, router, HTTP client); strict structure suits large teams | Simple learning curve; good SSR; clear single-file components |
| Disadvantages | App Router concepts (server/client components) add complexity; many ways to do the same thing | Steep learning curve; verbose; smaller choice of modern chart wrappers | Smaller ecosystem than React; team has no Vue experience |
| Performance | SSR and static generation reduce first load; good for dashboards with cached data | Good runtime performance; larger initial bundle | Comparable to Next.js |
| Scalability | Scales by splitting into routes and components; easy deployment to Vercel or Docker | Designed for large enterprise apps | Scales well for medium apps |
| Security | Server-side code is not shipped to the browser; built-in protection against XSS in JSX | Built-in sanitisation, strong typing | Built-in escaping in templates |
| Maintainability | TypeScript, large community, many examples | Very consistent code structure | Readable, but fewer team members can maintain it |
| Team fit (D8) | **High** — all three members have React/TypeScript experience; Rakhat used Next.js 14 in practice | Low | Low |

**Decision:** **Next.js (React + TypeScript)**. It best supports dashboards (D4) through the React chart ecosystem and matches the team's existing skills (D8), which is the main risk factor for a short diploma timeline.

---

## 4. Decision 2 — Core backend platform (digital profile module, REST API)

**Alternatives:** Next.js API Routes / Route Handlers (Node.js), NestJS (Node.js), Django REST Framework (Python).

| Criterion | Next.js Route Handlers (Node.js) | NestJS (Node.js) | Django REST Framework (Python) |
|---|---|---|---|
| Advantages | Same language and repository as the frontend; shared TypeScript types and Zod schemas between client and server; no separate deployment | Clear modular architecture (modules, controllers, services); built-in guards for roles; good for large APIs | Mature ORM, admin panel and permissions out of the box |
| Disadvantages | Less structure by default; long-running jobs are not suitable for serverless functions | Extra service to deploy; more boilerplate | Second language for the profile module; frontend types must be duplicated |
| Performance | Sufficient for CRUD and calculation endpoints at university scale; cold starts on serverless | Good; long-lived server, no cold starts | Good; synchronous by default |
| Scalability | Horizontal scaling through serverless or containers | Horizontal scaling through containers | Horizontal scaling through containers |
| Security | Validation with Zod; role checks in middleware; integrates with NextAuth.js | Guards and pipes for validation and roles | Strong built-in auth, CSRF protection and permissions |
| Maintainability | Simple for a small team; one codebase | High for big teams; more code for a small team | High, but split knowledge across two stacks |
| Team fit (D8) | **High** — Rakhat's practical experience (Next.js, NextAuth.js, Zod) | Medium | Medium |

**Decision:** **Next.js Route Handlers with TypeScript and Zod** for the core profile API (users, profiles, grades, achievements, GPA calculation). Shared types reduce mismatches between the API and dashboards (D2, D4), and role checks are applied in one place (D3). To avoid the lack of structure, the code will be organised in layers: `route → validation (Zod) → service → repository`.

---

## 5. Decision 3 — Data processing service (import, cleaning, aggregation)

**Alternatives:** FastAPI + Pandas (Python), processing inside the Node.js backend (SheetJS/Papaparse), Django + Celery (Python).

| Criterion | FastAPI + Pandas + SQLAlchemy | Inside Node.js backend | Django + Celery |
|---|---|---|---|
| Advantages | Pandas is the standard tool for cleaning and transforming tabular data; automatic OpenAPI documentation; async support; type validation with Pydantic | No extra service; one language | Background task queue for heavy imports; mature ecosystem |
| Disadvantages | Separate service and deployment; two languages in the project | Weak libraries for data cleaning and statistics; long imports block serverless functions | Heavy for a small service; needs a message broker (Redis/RabbitMQ) |
| Performance | Vectorised Pandas operations handle thousands of rows of grades quickly; async I/O | Adequate for small files only | Good for very large or scheduled jobs |
| Scalability | Stateless service, scaled in Docker independently of the web app | Limited by serverless time limits | High, but with extra infrastructure |
| Security | Pydantic validation of every input row; isolated service with its own DB role | Same as core backend | Strong, but larger surface |
| Maintainability | Small, focused codebase; pytest for tests | Mixed responsibilities in one service | More components to maintain |
| Team fit (D8) | **High** — Damir's planned stack (Python, FastAPI, Pandas, pytest) | Medium | Low |

**Decision:** **FastAPI + Pandas + SQLAlchemy** as a separate data processing service. It covers import, cleaning and aggregation of educational data (D5) and indicator calculations over many records (D2) with the right tools, while the core API stays simple. The two services share one PostgreSQL database with separate database roles.

---

## 6. Decision 4 — Database

**Alternatives:** PostgreSQL, MySQL, MongoDB.

| Criterion | PostgreSQL | MySQL | MongoDB |
|---|---|---|---|
| Advantages | Full relational model with foreign keys and constraints; window functions and CTEs for GPA and trend queries; JSONB for flexible profile attributes; row-level security | Widely used, simple to operate | Flexible schema; easy to store documents such as certificates |
| Disadvantages | Slightly more complex administration than MySQL | Fewer analytical features; weaker JSON support | No joins/foreign keys in the relational sense; grade and credit integrity must be enforced in code; aggregation pipelines are harder to verify |
| Performance | Very good for analytical queries across semesters and groups | Very good for simple reads/writes | Very good for document reads; weaker for multi-collection reports |
| Scalability | Vertical scaling plus read replicas; enough for one or several universities | Similar to PostgreSQL | Horizontal sharding built in |
| Security | Roles and privileges per schema/table, row-level security for "teacher sees only assigned students" | Roles and privileges | Role-based access per collection |
| Maintainability | Schema migrations (Prisma/Alembic) keep structure versioned | Same | Schema drift risk without discipline |
| Fit with requirements | **High** — D1, D2, D3, D6 | Medium | Low (D1, D2) |

**Decision:** **PostgreSQL**. Academic data is strongly relational (D1), GPA correctness depends on constraints and reliable aggregation (D2), and row-level security can enforce teacher access rules at the database level (D3). Flexible fields (for example, achievement metadata or university-specific grading rules, D6) are stored in JSONB columns.

---

## 7. Decision 5 — Component interaction (API style)

**Alternatives:** REST (JSON over HTTP, OpenAPI), GraphQL, tRPC.

| Criterion | REST + OpenAPI | GraphQL | tRPC |
|---|---|---|---|
| Advantages | Simple, universal; works the same for Node.js and Python services; easy to test with Postman and document with OpenAPI | Client requests exactly the needed fields; one endpoint for complex dashboards | End-to-end type safety without schemas |
| Disadvantages | Several requests may be needed for a dashboard | Extra schema layer; caching and authorisation per field are harder | Works only between TypeScript client and server — not usable for the Python service or external systems |
| Performance | Good; HTTP caching works out of the box | Fewer round trips, but risk of expensive queries | Good |
| Scalability | Stateless, easy to scale | Needs query cost limits | Stateless |
| Security | Clear per-endpoint role checks | Authorisation must be checked per resolver | Per-procedure checks |
| Maintainability | Familiar to all members; contract documented by OpenAPI | Higher learning cost | Low cost, but locks the project into TypeScript |
| Fit with requirements | **High** — two services in two languages, future integration with university systems (7.2) | Medium | Low |

**Decision:** **REST with JSON and OpenAPI documentation**. It is the only option that works naturally between the Next.js and FastAPI services and for future integration with external university systems. Dashboard round trips are reduced by dedicated aggregate endpoints (for example, `GET /api/students/{id}/dashboard`).

---

## 8. Decision 6 — Authentication and role-based access control

**Alternatives:** Auth.js / NextAuth.js (JWT sessions), Keycloak, custom JWT implementation.

| Criterion | Auth.js (NextAuth.js) | Keycloak | Custom JWT |
|---|---|---|---|
| Advantages | Native integration with Next.js; credentials and OAuth providers; role stored in the session/JWT | Full identity server: SSO, user federation, fine-grained roles | Full control |
| Disadvantages | Roles and permissions beyond basic session data must be implemented by the team | Separate Java service to deploy and configure; heavy for an MVP | High risk of security mistakes (token storage, expiry, refresh, hashing) |
| Performance | Lightweight | Extra network hop to the identity server | Lightweight |
| Scalability | Stateless JWT sessions | Designed for large organisations | Depends on implementation |
| Security | Maintained library, secure cookie handling, CSRF protection | Very strong, industry standard | Lowest — not recommended |
| Maintainability | Small configuration | Requires administration | All code owned by the team |
| Fit with requirements | **High** for MVP (D3, D7, D8) | Medium (good for future SSO with a university) | Low |

**Decision:** **Auth.js (NextAuth.js) with JWT sessions** and three roles (student, teacher, administrator). The FastAPI service verifies the same signed JWT. Keycloak or university SSO is recorded as a future enhancement if the system is integrated with an existing university identity provider.

---

## 9. Decision 7 — Data visualization library

**Alternatives:** Apache ECharts, Chart.js, Recharts.

| Criterion | Apache ECharts | Chart.js | Recharts |
|---|---|---|---|
| Advantages | Very wide range of chart types (line, bar, radar, heatmap); built-in zoom, tooltips and data filtering; handles large datasets | Small and simple; quick to start | React components; declarative API |
| Disadvantages | Larger bundle; configuration objects can be verbose | Fewer advanced chart types and interactions | SVG rendering slows with many points; fewer chart types |
| Performance | Canvas/WebGL rendering, suitable for many data points | Canvas, good for small datasets | SVG, best for small datasets |
| Scalability | Suitable for group- and faculty-level dashboards | Suitable for single-student views | Suitable for single-student views |
| Security | Client-side only; no specific risks | Same | Same |
| Maintainability | Apache project, active development | Active community | Active community |
| Fit with requirements | **High** — semester trends, radar chart of competencies, group statistics (D4) | Medium | Medium |

**Decision:** **Apache ECharts** (through the `echarts-for-react` wrapper). Radar charts for profile competencies, GPA trends over semesters and group comparisons are all covered by one library.

---

## 10. Final technology stack

| Layer | Selected technology | Main reason |
|---|---|---|
| Frontend | Next.js + React + TypeScript, Tailwind CSS | Team skills, React ecosystem for dashboards |
| Visualization | Apache ECharts | Chart variety and interactivity for D4 |
| Core backend | Next.js Route Handlers (Node.js), Zod validation | One TypeScript codebase, shared types, simple deployment |
| Data processing | Python FastAPI, Pandas, SQLAlchemy | Data import and cleaning (D5), heavy aggregation (D2) |
| Database | PostgreSQL (Prisma migrations for core, SQLAlchemy for data service) | Relational integrity and analytical queries (D1, D2) |
| Interaction | REST + JSON, OpenAPI documentation | Works across both languages and external systems |
| Authentication | Auth.js (NextAuth.js), JWT, role-based access | Secure, integrated, low effort (D3, D7) |
| Testing | Jest (frontend/core), pytest (data service), Postman (API) | Standard tools for each language |
| Infrastructure | Docker Compose for local development; Vercel (web) and a container host (data service) for demo | Reproducible setup, simple demo deployment |
| Version control & tracking | GitHub (feature branches + pull requests), YouTrack | Required by the diploma rules |

### Overall justification

- **Requirements first.** The relational nature of academic data and the need for verifiable GPA calculations (D1, D2) led to PostgreSQL; the need for interactive semester-based dashboards (D4) led to React and ECharts.
- **Two services, one database.** Splitting the system into a TypeScript web application and a Python data service follows each member's responsibility (frontend, profile module, data processing) and uses the strongest tool for each task. REST keeps the contract between them simple.
- **Security by default.** Using a maintained authentication library, schema validation on every input (Zod, Pydantic), database roles and environment variables instead of committed secrets addresses D3 and D7.
- **Realistic for the timeline.** Every chosen technology is already known by at least one team member (D8), which reduces delivery risk.

### Risks of the selected stack

| Risk | Mitigation |
|---|---|
| Two languages increase integration effort | Shared OpenAPI contract; integration tests for the main endpoints |
| Serverless time limits for long operations | Long-running imports are handled only by the FastAPI service |
| Schema changes from two ORMs | Prisma owns the core schema; the data service uses read/write access only to agreed tables; migrations reviewed in pull requests |

## 11. References

- Next.js documentation — https://nextjs.org/docs
- Angular documentation — https://angular.dev
- Nuxt documentation — https://nuxt.com/docs
- NestJS documentation — https://docs.nestjs.com
- Django REST Framework — https://www.django-rest-framework.org
- FastAPI documentation — https://fastapi.tiangolo.com
- pandas documentation — https://pandas.pydata.org/docs
- PostgreSQL documentation (Row Security Policies) — https://www.postgresql.org/docs/current/ddl-rowsecurity.html
- MySQL documentation — https://dev.mysql.com/doc
- MongoDB documentation — https://www.mongodb.com/docs
- OpenAPI Specification — https://spec.openapis.org/oas/latest.html
- GraphQL documentation — https://graphql.org/learn
- tRPC documentation — https://trpc.io/docs
- Auth.js documentation — https://authjs.dev
- Keycloak documentation — https://www.keycloak.org/documentation
- Apache ECharts — https://echarts.apache.org
- Chart.js — https://www.chartjs.org/docs
- Recharts — https://recharts.org
