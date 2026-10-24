# Student Digital Profile

**Development of an Information System for Creating and Visualizing Student Digital Profiles**

A diploma project that brings a student's academic records, GPA, semester progress and selected achievements into one web workspace.

## Current status

Planning, requirements and interactive prototyping. The team has integrated the proposal, literature/system comparisons, technology decisions, requirements, architecture, diagram exports, verification plan and prototype baseline into main. This SDP-10 follow-up adds the tracked implementation scaffold and the repository map.

The repository does not yet contain an implemented web application, backend service, database migrations or application dependency manifests. Prototype screens use fictional data and scripted transitions. Existing baseline approval is preserved; the new structure needs its own review.

## Problem and aim

Academic results, achievements and educational progress may be spread across separate systems. Students and teachers then lack a single view of progress over time. The project aims to combine those records into a structured digital profile, calculate academic indicators using documented rules, and present the underlying results alongside understandable visualisations.

## Users and planned capabilities

| User | Planned capability |
| --- | --- |
| Student | View their own profile, courses, grades, credits, GPA and semester trends; manage selected personal achievements |
| Teacher | View students within their authorised course/assignment scope and enter or update academic results |
| Administrator | Manage test accounts, roles, profile metadata, groups, courses and teacher assignments; administer agreed grading configuration |

Protected data and edits require backend role and ownership checks. A Figma demonstration does not verify those checks.

## Scope and expected outcomes

The proposed MVP includes test-account authentication, digital profiles, academic records, configurable weighted GPA, academic charts, achievements with certificate evidence, and account/assignment administration.

Expected project outcomes are a functional web application, a structured database, documented APIs, role-based access, accurate academic calculations, interactive dashboards, technical documentation and recorded verification results. These are delivery goals; the current repository provides planning and prototype artefacts.

PDF export, advanced competency portfolios, attendance, full Kazakh/Russian/English localisation and external university integrations are future enhancements. Native mobile applications and replacement of the university LMS are outside the initial scope.

CSV/Excel import is **not settled**: the proposal places it in future scope, architecture includes it in the MVP and the verification plan assigns it Should priority. The team must resolve this before implementation. Teacher visibility, certificate storage and academic grading rules also need agreement; see the [requirements decision log](docs/requirements/05-requirements-specification.md).

## Team

| Member | Responsibility |
| --- | --- |
| Aimaut Bolatkhanuly | Frontend, UX prototype and academic visualisation |
| Rakhat Dosmagambetov | Digital-profile backend, calculations and API |
| Damir Ushkempir | System analysis and QA in the proposal; data processing and backend in the team justification |
| Gulzhan Soltan | Academic supervisor |

The final implementation ownership should reconcile the proposal and team justification.

## Selected technology direction

The [technology comparison](docs/technology-comparison/04-technology-comparison.md) and [architecture](docs/architecture/07-architecture.md) describe the following choices. They are design decisions, not installed dependencies.

| Area | Selected direction |
| --- | --- |
| Web UI | Next.js, React, TypeScript, Tailwind CSS |
| Charts | Apache ECharts |
| Core API | Next.js Route Handlers, Zod |
| Data processing | Python, FastAPI, Pandas, SQLAlchemy |
| Database | PostgreSQL; Prisma owns the proposed core migrations |
| Authentication | Auth.js / NextAuth.js, JWT sessions and server-enforced roles |
| Integration | REST, JSON and OpenAPI |
| Planned checks | Jest, pytest, API tests and Playwright; performance/security checks in SDP-8 |
| Planned infrastructure | Docker Compose locally; web/container hosting to be finalised |

The proposed architecture separates the web/core API from the data service and uses one PostgreSQL database. API contracts, token verification between services, migration ownership and certificate storage must be agreed before implementation.

## Documentation and prototype

- [Documentation index](docs/README.md)
- [Project proposal and scope](docs/project-proposal/01-proposal.md)
- [Literature review](docs/literature-review/02-literature-review.md)
- [Existing systems comparison](docs/existing-systems-comparison/03-existing-systems-comparison.md)
- [Technology comparison](docs/technology-comparison/04-technology-comparison.md)
- [Requirements](docs/requirements/05-requirements-specification.md)
- [System architecture and use cases](docs/architecture/07-architecture.md)
- [Verification and evaluation plan](docs/testing/08-verification-evaluation-plan.md)
- [Prototype guide](Prototype.md) and [SVG exports](prototype/exports/)
- [Prototype review notes](prototype/acceptance-review.md)
- [Repository structure and implementation locations](docs/repository/10-repository-structure.md)
- [Team contributions](CONTRIBUTING.md)

[Figma design file](https://www.figma.com/design/hOhNtoHcIS5VW5UfHqD0fC) · [Revision 03 prototype](https://www.figma.com/proto/hOhNtoHcIS5VW5UfHqD0fC?node-id=14-639&page-id=14%3A173&starting-point-node-id=14%3A639) · [YouTrack project](https://student-digital-profile.youtrack.cloud/projects/SDP/issues)

This branch preserves the accepted revision-03 prototype package: 41 screens and 288 predefined transitions. The separate [SDP-7 revision-04 PR #11](https://github.com/Rakhat2434/student-digital-profile/pull/11) adds 85 screens/686 locally checked transitions; its native installation and verification remain separate work.

## Repository locations

| Folder | Purpose |
| --- | --- |
| apps/web/ | Next.js interface and core REST API; Prisma schema/migrations |
| services/data/ | Python/FastAPI data processing |
| packages/contracts/ | Shared OpenAPI and JSON schemas |
| tests/ | Unit, integration, end-to-end tests and synthetic fixtures |
| infra/ and config/ | Deployment templates and non-secret configuration |
| docs/ and prototype/ | Diploma documents, diagrams, prototype sources and review exports |
| scripts/ | Repository validation utilities |

The [full folder map](docs/repository/10-repository-structure.md) describes each layer and where new work belongs. Empty implementation folders are tracked with .gitkeep; they do not contain a runnable application yet.

## Open and verify locally

Clone the team repository and inspect the branch you actually received:

```powershell
git clone https://github.com/Rakhat2434/student-digital-profile.git
cd student-digital-profile
git status --short --branch
git branch -a
```

The command above downloads published work. Select `codex/sdp-10-repository-structure` with `git switch --track origin/codex/sdp-10-repository-structure` to review this structure after a fresh clone. In an existing checkout with that local branch, use `git switch codex/sdp-10-repository-structure`.

Open Markdown in VS Code and preview it with Ctrl+Shift+V. Open `docs/ux/figma-prototype/preview.html` in a browser for the local clickable demonstration. Figma installation and package-only checks are documented in the [prototype builder guide](docs/ux/figma-prototype/README.md).

Documentation checks:

```powershell
python scripts/check_repository.py
git diff --check
git log --oneline --decorate -12
git diff origin/main...HEAD --stat
```

There is no application install/start/build command yet. Add verified runtime versions, dependency installation, environment examples, migrations, seed data, startup and test instructions once their implementation exists.

## Contributions

See [team contributions by task](CONTRIBUTING.md).

Project licence: not yet selected.

[All-task YouTrack review and remaining work](docs/repository/youtrack-review-2026-10-24.md)
