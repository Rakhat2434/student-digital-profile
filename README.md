<div align="center">

# Student Digital Profile

### An Information System for Creating and Visualizing Student Digital Profiles

Software Engineering Diploma Project · 2026

[Overview](#overview) · [Documentation](#documentation) · [Figma Prototype](https://www.figma.com/design/hOhNtoHcIS5VW5UfHqD0fC) · [YouTrack](https://student-digital-profile.youtrack.cloud/projects/SDP/issues)

</div>

---

## Overview

Student Digital Profile is a proposed web-based information system that brings academic records, performance indicators and achievement evidence into a unified student profile. It is designed to help students understand their progress, support teachers in maintaining assigned academic records, and provide administrators with tools for managing accounts and academic assignments.

The project addresses the fragmentation of educational information across separate records and services. Its objective is to present a coherent view of student progress while keeping indicators traceable to the grades, credits and grading policies from which they are calculated.

**Project stage:** requirements specification and interactive prototyping. Application implementation and deployment are planned.

## Objectives

- Define a structured digital profile combining academic information and selected achievements.
- Calculate semester and cumulative GPA using explicit, versioned grading rules.
- Visualize academic progress with consistent charts and supporting records.
- Apply role-based access and student ownership boundaries throughout the system.
- Evaluate the interface through representative user scenarios and measurable acceptance criteria.

## Users and Responsibilities

| Role | Primary responsibilities | Access scope |
| --- | --- | --- |
| **Student** | Review academic progress, inspect results and maintain personal achievements | Own profile and records |
| **Teacher** | Review assigned students and maintain course results | Assigned courses and student enrolments |
| **Administrator** | Manage test accounts, groups, assignments and grading configuration | Authorized administrative operations |

Demonstrations use synthetic data. Institutional integrations and additional adviser permissions require a separate scope agreement.

## Project Scope

### Minimum Viable Product

| Area | Planned capabilities |
| --- | --- |
| Authentication | Test-account sign-in, sign-out and role-scoped access |
| Student profiles | Student information, programme, group and enrolled courses |
| Academic records | Semester-based grades, credits and result status |
| Performance indicators | Configurable GPA calculation and academic progress visualization |
| Achievements | Personal achievement records with certificate evidence |
| Administration | Account, group, course and teacher-assignment management |

### Future Extensions

CSV/Excel import, external learning-system integration, advanced competency portfolios, PDF reporting and full Kazakh/Russian/English localization are candidates for later development. Import scope is subject to reconciliation between the proposal and architecture documents.

Native mobile applications and replacement of an institutional learning management system are outside the initial scope.

## Interface and Prototype

The [Figma design file](https://www.figma.com/design/hOhNtoHcIS5VW5UfHqD0fC) presents the proposed interface. The SDP-7 branch also provides a redesigned interactive package with **41 screens and 288 predefined transitions**, covering:

- Student overview, academic records, course details and profile navigation.
- Achievement browsing, certificate evidence, validation, saving and deletion scenarios.
- Teacher grade correction and the corresponding GPA update.
- Administrator account and access-policy views.
- Mobile navigation, empty states and error recovery.

The prototype uses scripted sample inputs and predefined states. It does not provide production authentication, persistent storage or real file uploads. Local Figma setup has been reported complete; final verification of the installed revision in Figma Present remains pending.

Prototype exports and the review checklist are maintained in `prototype/` on `SDP-7-ux-prototype`. The offline preview and Figma builder are in `docs/ux/figma-prototype/` on the same branch.

## Technology Stack

The following direction is documented in the [technology comparison](docs/technology-comparison/05-technology-comparison.md). These technologies describe the planned implementation.

| Layer | Technologies |
| --- | --- |
| Frontend | Next.js, React, TypeScript, Tailwind CSS |
| Data visualization | Apache ECharts |
| Profile API | Next.js Route Handlers, Zod |
| Data processing | Python, FastAPI, Pandas, SQLAlchemy |
| Database | PostgreSQL |
| API contracts | REST/JSON, OpenAPI |
| Authentication | Auth.js / NextAuth.js with role checks |
| Testing | Jest, pytest and API acceptance checks |

## Documentation

[Browse the documentation index](docs/README.md) for document locations, branch references and inspection commands.

| Deliverable | Task | Location |
| --- | --- | --- |
| Project proposal and scope | [SDP-1](https://student-digital-profile.youtrack.cloud/issue/SDP-1) | `docs/project-proposal/01-proposal.md` on the proposal branch |
| Technology comparison | [SDP-4](https://student-digital-profile.youtrack.cloud/issue/SDP-4) | [Technology comparison](docs/technology-comparison/05-technology-comparison.md) |
| Requirements specification | [SDP-5](https://student-digital-profile.youtrack.cloud/issue/SDP-5) | `docs/requirements/` on `SDP-5-requirements-specification` |
| Architecture and diagrams | [SDP-6](https://student-digital-profile.youtrack.cloud/issue/SDP-6) | `07-architecture.md` and diagrams on `SDP-6` |
| UX and interactive prototype | [SDP-7](https://student-digital-profile.youtrack.cloud/issue/SDP-7) | `prototype/` and `docs/ux/` on `SDP-7-ux-prototype` |
| Repository organization | [SDP-10](https://student-digital-profile.youtrack.cloud/issue/SDP-10) | [Repository guide](docs/repository/SDP-10-repository-guide.md) |

Task deliverables remain in their respective branches until reviewed and merged. Cross-branch paths are listed explicitly to distinguish them from files available in the current checkout.

## Repository Structure

The SDP-10 documentation branch contains:

```text
student-digital-profile/
├── .github/
│   └── pull_request_template.md
├── docs/
│   ├── repository/
│   │   └── SDP-10-repository-guide.md
│   ├── technology-comparison/
│   │   └── 05-technology-comparison.md
│   └── README.md
├── .gitignore
├── CONTRIBUTING.md
└── README.md
```

The [repository guide](docs/repository/SDP-10-repository-guide.md) describes the proposed source-code, service, test and infrastructure layout for the implementation phase.

## Getting Started

### Explore the Repository

Git is required to clone the repository. A Markdown-capable editor such as Visual Studio Code is sufficient to review the current documentation.

```bash
git clone https://github.com/Rakhat2434/student-digital-profile.git
cd student-digital-profile
git branch -a
```

Open `README.md` and follow the documentation links. In Visual Studio Code, use **Ctrl+Shift+V** to preview Markdown. Task branches appear in a fresh clone after they have been published.

### Application Setup

The reviewed baseline does not yet include a runnable application. Dependency installation, environment configuration, database setup, execution and test commands will be added alongside the corresponding implementation.

For the existing prototype package, switch to `SDP-7-ux-prototype` when that branch is available and follow its `prototype/README.md`.

## Quality and Evaluation

The requirements specification defines acceptance checks for:

- GPA calculation, rounding and missing-data handling.
- Role, ownership and teacher-assignment restrictions.
- Agreement between chart values and academic records.
- Form validation, failed saves and error recovery.
- Responsive presentation, accessibility and usability.

Local prototype checks cover route reachability, reaction construction and representative browser journeys. They are distinct from application tests and final Figma Present verification. Independent team review is required before the related tasks are closed.

## Team

| Team member | Responsibilities |
| --- | --- |
| **Aimaut Bolatkhanuly** (`aimautb`) | Frontend development, UX prototyping, educational-data visualization; SDP-5, SDP-7 and SDP-10 |
| **Rakhat Dosmagambetov** | Digital-profile backend, calculations and API development |
| **Damir Ushkempir** | Data processing and backend development; system analysis and quality assurance |

**Academic supervisor:** Gulzhan Soltan

## Contribution Workflow

Use a dedicated branch for each YouTrack task, include its identifier in commit messages, and submit changes through a pull request for review. Keep requirements, prototype and repository-organization changes scoped to their owning tasks.

See [CONTRIBUTING.md](CONTRIBUTING.md) for branch conventions, documentation checks and publication procedures. Pull requests use the [review template](.github/pull_request_template.md).

Credentials, private source documents and real student records must remain outside the repository. An owner must confirm appropriate repository access for every team member before the repository-setup task is accepted.

## License

A project license has not yet been selected.
