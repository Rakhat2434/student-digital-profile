# Student Digital Profile

**Development of an Information System for Creating and Visualizing Student Digital Profiles**

A diploma project that brings a student's academic records, GPA, semester progress and selected achievements into one web workspace.

## Current status

Planning, requirements and interactive prototyping. The team has integrated the proposal, system comparison, technology decisions, architecture, three diagram exports and verification plan into `main`. This local SDP-10 branch additionally consolidates the SDP-5 requirements and SDP-7 prototype materials through merge commits.

The repository does not yet contain an implemented web application, backend service, database migrations or application dependency manifests. Prototype screens use fictional data and scripted transitions. Publication and independent review of our task branches remain pending.

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

CSV/Excel import is **not settled**: the proposal places it in future scope, architecture includes it in the MVP and the verification plan assigns it Should priority. The team must resolve this before implementation. Teacher visibility, certificate storage and academic grading rules also need agreement; see the [requirements decision log](docs/requirements/SDP-5-requirements-specification.md).

## Team

| Member | Responsibility |
| --- | --- |
| Aimaut Bolatkhanuly (`aimautb`) | Frontend, UX prototype and academic visualisation |
| Rakhat Dosmagambetov | Digital-profile backend, calculations and API |
| Damir Ushkempir | System analysis and QA in the proposal; data processing and backend in the team justification |
| Gulzhan Soltan | Academic supervisor |

The final implementation ownership should reconcile the proposal and team justification.

## Selected technology direction

The [technology comparison](docs/technology-comparison/05-technology-comparison.md) and [architecture](docs/architecture/07-architecture.md) describe the following choices. They are design decisions, not installed dependencies.

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
- [Existing systems comparison](docs/existing-systems-comparison/existing-systems-comparison.md)
- [Technology comparison](docs/technology-comparison/05-technology-comparison.md)
- [Requirements and acceptance criteria](docs/requirements/SDP-5-requirements-specification.md)
- [System architecture and use cases](docs/architecture/07-architecture.md)
- [Verification and evaluation plan](docs/Verification%20%26%20Evaluation%20Plan/verification-evaluation-plan.md)
- [Prototype entry point and exports](prototype/README.md)
- [Prototype acceptance evidence and remaining gaps](prototype/acceptance-review.md)
- [Repository audit and task status](docs/repository/project-review-2026-10-24.md)
- [Contribution workflow](CONTRIBUTING.md)

[Figma design file](https://www.figma.com/design/hOhNtoHcIS5VW5UfHqD0fC) · [Revision 03 prototype](https://www.figma.com/proto/hOhNtoHcIS5VW5UfHqD0fC?node-id=14-639&page-id=14%3A173&starting-point-node-id=14%3A639) · [YouTrack project](https://student-digital-profile.youtrack.cloud/projects/SDP/issues)

The current team prototype package contains 41 screens and 288 predefined transitions. Its recorded verification distinguishes local browser tests from sampled Figma Present checks. Native teacher/admin/mobile verification and incomplete administrative workflows remain acceptance gaps. The earlier 31-state Figma file belongs to the other local repository and is not the current team handoff.

## Repository structure

```text
.github/pull_request_template.md
.gitignore
README.md
CONTRIBUTING.md
DESIGN.md
UX-CONTRACT.md
apps/web/                  Planned web/core API location; guidance only
services/data/             Planned data service location; guidance only
config/                    Configuration guidance; no secrets or runtime config
tests/                     Cross-service test guidance; no application tests yet
docs/
  README.md
  project-proposal/
  existing-systems-comparison/
  technology-comparison/
  requirements/
  architecture/
  diagrams/                Current PNG diagram exports
  Verification & Evaluation Plan/
  ux/                      UX specification and local prototype builder
  repository/              Repository guide, audit and acceptance status
prototype/
  README.md
  acceptance-review.md
  exports/                 Five SVG review boards
```

The code/config/test directories contain ownership guidance only. Add runtime files and executable checks when implementation begins.

## Open and verify locally

Clone the team repository and inspect the branch you actually received:

```powershell
git clone https://github.com/Rakhat2434/student-digital-profile.git
cd student-digital-profile
git status --short --branch
git branch -a
```

The command above downloads published work. Our local SDP-5/7/10 commits have not been pushed, so cloning today will not include this consolidated branch. In the existing local checkout/worktree, select `SDP-10-github-readme-repository-structure` to review this package.

Open Markdown in VS Code and preview it with Ctrl+Shift+V. Open `docs/ux/figma-prototype/preview.html` in a browser for the local clickable demonstration. Figma installation and package-only checks are documented in the [prototype builder guide](docs/ux/figma-prototype/README.md).

Documentation checks:

```powershell
git diff --check
git log --oneline --decorate -12
git diff origin/main...HEAD --stat
```

There is no application install/start/build command yet. Add verified runtime versions, dependency installation, environment examples, migrations, seed data, startup and test instructions once their implementation exists.

## Workflow and acceptance

Use one owning branch per YouTrack task and include the task ID in commits and pull requests. SDP-10 is the local consolidation branch requested on 24 October; the SDP-5/7 merge commits preserve their original histories. Review and publish the dependency branches before the final SDP-10 PR, or explicitly disclose those dependencies in the PR.

The [repository guide](docs/repository/SDP-10-repository-guide.md) maps SDP-10 acceptance criteria to evidence. Team access and independent review require evidence from the repository owner/reviewers. Keep all three tasks In Progress until their remaining criteria are met.

Do not commit credentials or private student records. No project licence has been supplied; the team must choose one before licensing claims are added.
