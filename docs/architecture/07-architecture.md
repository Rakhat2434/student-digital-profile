# System Architecture

**Project:** Student Digital Profile Information System
**YouTrack task:** SDP-6 — System Architecture & Diagrams
**Author:** Rakhat Dosmagambetov (Backend Developer)
**Status:** Draft for review (initial architecture, pre-defense 1)
**Date:** 2026-10-23

---

## 1. Architecture overview

The system is a web application built as a **three-tier, service-oriented architecture** with two backend services that share one relational database:

1. **Web Client** — Next.js (React, TypeScript) application with role-specific interfaces for students, teachers and administrators, and interactive dashboards (Apache ECharts).
2. **Core Backend** — Next.js Route Handlers (Node.js, TypeScript) that expose the REST API for authentication, digital profiles, academic records, GPA calculation, achievements and administration.
3. **Data Processing Service** — Python FastAPI service that imports, cleans, transforms and aggregates educational data (CSV/Excel) with Pandas.
4. **PostgreSQL database** — single source of truth for users, students, courses, grades, achievements, grading rules and calculated indicators.

All communication between components uses **REST over HTTPS with JSON**. Authentication is handled by Auth.js (NextAuth.js) with signed JWT sessions; the same token is verified by the Data Processing Service. The choice of each technology is justified in [`05-technology-comparison.md`](05-technology-comparison.md).

Diagram sources are written in **PlantUML** (`docs/diagrams/src/*.puml`, editable in any text editor or the VS Code "PlantUML" extension). Readable exports are in `docs/diagrams/export/` (PNG and SVG).

| Diagram | Source | Export |
|---|---|---|
| System Context | [`system-context.puml`](diagrams/src/system-context.puml) | [PNG](diagrams/export/system-context.png) · [SVG](diagrams/export/system-context.svg) |
| Use Case | [`use-case.puml`](diagrams/src/use-case.puml) | [PNG](diagrams/export/use-case.png) · [SVG](diagrams/export/use-case.svg) |
| Component (draft) | [`component.puml`](diagrams/src/component.puml) | [PNG](diagrams/export/component.png) · [SVG](diagrams/export/component.svg) |

---

## 2. System Context Diagram

![System Context Diagram](diagrams/export/system-context.png)

**System boundary.** The Student Digital Profile Information System is one system that stores and processes student profile data, calculates academic indicators and presents them in dashboards.

**External actors**

| Actor | Interaction with the system |
|---|---|
| Student | Views own digital profile, academic records, GPA dashboard and semester trends; manages own achievements and certificates |
| Teacher | Views students enrolled in own courses, enters and updates grades, analyses student performance |
| System Administrator | Manages user accounts and roles, groups, courses, teacher assignments and grading rules; imports data |

**External systems**

| External system | Interaction | Scope |
|---|---|---|
| CSV / Excel files (registrar exports, synthetic test data) | Uploaded by the administrator and processed by the Data Processing Service | MVP |
| University information systems / LMS (e.g. Platonus, Moodle) | Source of academic data through export or API | Future enhancement (proposal 7.2), requires authorised access |
| University identity provider (SSO) | User authentication through OAuth 2.0 / OpenID Connect | Future enhancement |

Because access to official university systems is not available (proposal, Section 8), the MVP works with synthetic or authorised test data loaded from files.

---

## 3. Use Case Diagram

![Use Case Diagram](diagrams/export/use-case.png)

The abstract actor **User** represents any authenticated person; Student, Teacher and System Administrator inherit the "Log in / log out" use case.

| ID | Use case | Actor | Proposal scope |
|---|---|---|---|
| UC-01 | Log in / log out | All users | 7.1 A |
| UC-02 | View digital profile | Student | 7.1 B |
| UC-03 | View academic records (courses, grades, credits) | Student | 7.1 B |
| UC-04 | View GPA dashboard and semester trends | Student | 7.1 D |
| UC-05 | Manage achievements and certificates | Student | 7.1 B |
| UC-06 | View assigned students (own courses only) | Teacher | 7.1 A |
| UC-07 | Enter / update grades | Teacher | 7.1 C |
| UC-08 | Analyse student performance and profile | Teacher | 4.2, 7.1 D |
| UC-09 | Manage user accounts and roles | Administrator | 4.3, 7.1 A |
| UC-10 | Manage groups, courses and teacher assignments | Administrator | 4.3 |
| UC-11 | Configure grading rules | Administrator | 7.1 C, 8 |
| UC-12 | Import data from CSV / Excel | Administrator | 7.2, 8 |
| UC-13 | Calculate GPA and indicators | System (included) | 7.1 C |

**Relationships**

- UC-07, UC-12 and UC-04 `<<include>>` UC-13: GPA and indicators are recalculated whenever grades change or are imported, and the dashboard always shows current values.
- UC-06 enforces the access rule from the proposal: a teacher sees only students enrolled in the teacher's courses.

---

## 4. Component Diagram (draft)

![Component Diagram](diagrams/export/component.png)

### 4.1 Component responsibilities

**Web Client (Next.js, React, TypeScript)**

| Component | Responsibility |
|---|---|
| Student Dashboard UI | Profile page, academic records, GPA and semester trend charts, achievements management |
| Teacher Workspace UI | List of assigned students, grade entry forms, performance analysis views |
| Admin Panel UI | CRUD for users, roles, groups, courses, teacher assignments, grading rules; file upload for import |
| Chart Components (Apache ECharts) | Reusable charts: GPA line chart by semester, grade distribution, radar of indicators |
| API Client | Typed functions that call the Core Backend REST API and attach the session |

**Core Backend (Next.js Route Handlers, Node.js)**

| Component | Responsibility |
|---|---|
| Auth Module (Auth.js, JWT) | Login with test accounts, password hashing, issuing and verifying JWT sessions with the user's role |
| RBAC Middleware | Checks role and ownership for every request (student — own data, teacher — assigned students, administrator — all) |
| Validation (Zod) | Validates request bodies and parameters before they reach services |
| Profile Service | Builds the student's digital profile from personal data, academic records, achievements and indicators |
| Academic Records Service | Courses, enrollments, grades and credits; triggers recalculation when grades change |
| GPA & Indicator Calculation Service | Calculates GPA and other indicators per semester using configurable grading rules; stores results as indicator snapshots for trend analysis |
| Achievements Service | CRUD for achievements and certificates, links to uploaded files |
| Administration Service | Users, roles, groups, courses, teacher assignments, grading rules; starts data imports |
| Data Access Layer (Prisma) | Database access and schema migrations for the core schema |

**Data Processing Service (Python, FastAPI)**

| Component | Responsibility |
|---|---|
| Import API | Accepts import jobs (CSV/Excel) from the Administration Service; returns job status and validation report |
| Cleaning & Transformation (Pandas, Pydantic) | Validates rows, removes duplicates, normalises grade scales and identifiers, maps columns to the database model |
| Aggregation & Analytics | Group- and course-level statistics, bulk recalculation of indicators after import |
| Data Access Layer (SQLAlchemy) | Writes cleaned data and aggregates to agreed tables |

**Data and storage**

| Component | Responsibility |
|---|---|
| PostgreSQL | Tables for users/roles, students/groups, courses/enrollments/grades, achievements, grading rules and indicator snapshots (history of indicators over time) |
| File Storage (to be decided) | Stores certificate files and uploaded import files; the database keeps only references |

### 4.2 How the parts interact

| From | To | Protocol / format | Purpose |
|---|---|---|---|
| Browser | Web Client | HTTPS | Pages and dashboards |
| Web Client (API Client) | Core Backend | REST, JSON, session JWT in secure cookie | All business operations |
| Core Backend (Administration Service) | Data Processing Service | REST, JSON, service JWT | Start import and bulk recalculation |
| Core Backend | PostgreSQL | SQL through Prisma | Read/write core data |
| Data Processing Service | PostgreSQL | SQL through SQLAlchemy | Write imported data and aggregates |
| Core Backend | File Storage | HTTPS API | Upload/download certificates |

### 4.3 Example scenario: teacher enters a grade (UC-07 → UC-13)

1. The teacher submits a grade in the Teacher Workspace UI.
2. The API Client sends `POST /api/grades` with the session cookie.
3. RBAC Middleware checks that the user is a teacher and the student is enrolled in that teacher's course.
4. Zod validates the grade value and course ID.
5. The Academic Records Service saves the grade and calls the GPA & Indicator Calculation Service.
6. The calculation service reads the active grading rules, recalculates the semester and cumulative GPA and stores a new indicator snapshot.
7. The student sees the updated GPA and trend on the next dashboard request.

---

## 5. Consistency with scope and requirements

| Proposal objective / scope item | Covered by |
|---|---|
| Objective 4 — authentication and role-based access | UC-01, UC-06, UC-09; Auth Module, RBAC Middleware |
| Objective 5 — create, view, manage digital profiles | UC-02, UC-08; Profile Service, Student Dashboard UI |
| Objective 6 — academic records and automated GPA | UC-03, UC-07, UC-11, UC-13; Academic Records Service, GPA & Indicator Calculation Service |
| Objective 7 — dashboards and visualisations | UC-04, UC-08; Chart Components, Student Dashboard UI, Teacher Workspace UI |
| Objective 8 — achievements and certificates | UC-05; Achievements Service, File Storage |
| Tracking changes over time | Indicator snapshots in PostgreSQL; semester trend charts |
| Import of CSV/Excel data (planned enhancement, used for test data) | UC-12; Data Processing Service |
| Out of scope: mobile app, LMS replacement, direct integration without access | Shown only as future external systems in the context diagram |

The requirement IDs (FR-xx, NFR-xx) from the Requirements Specification (`docs/06-requirements.md`) will be added to this table once that document is merged.

## 6. Open decisions

- File storage for certificates (local volume, S3-compatible storage or Cloudinary).
- Whether indicator recalculation after a single grade change runs synchronously in the Core Backend (current design) or always in the Data Processing Service.
- Hosting of the Data Processing Service for the demo (container platform).

## 7. How to edit the diagrams

1. Install the **PlantUML** extension in VS Code (by jebbs) and Java.
2. Open a file in `docs/diagrams/src/` and press `Alt+D` to preview.
3. Export: right-click in the editor → *PlantUML: Export Current Diagram* → choose PNG and SVG, and save them into `docs/diagrams/export/`.
   Command line alternative: `java -jar plantuml.jar -tpng -o ../export docs/diagrams/src/*.puml` (and `-tsvg`).
