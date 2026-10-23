# Student Digital Profile

**An academic profile that connects student results, calculated indicators and achievement evidence.**

Diploma project · Software Engineering · Planning and design stage

[Project tracker](https://student-digital-profile.youtrack.cloud/projects/SDP/issues) · [Figma design](https://www.figma.com/design/hOhNtoHcIS5VW5UfHqD0fC) · [Documentation index](docs/README.md) · [Contribution guide](CONTRIBUTING.md)

## About the project

**Development of an Information System for Creating and Visualizing Student Digital Profiles** is a web-based system for organizing academic records, calculating performance indicators and presenting a student's progress across semesters.

The problem being investigated is fragmented educational information: course results, achievements and certificates may be stored separately, making a coherent view of progress difficult. The proposed system brings selected information together and makes calculated indicators traceable to their source records. Stakeholder research and evaluation are still required to validate the problem and the solution.

Russian diploma title: **Разработка информационной системы формирования и визуализации цифрового профиля обучающегося**.

## Who it serves

| User | Main task | Access boundary |
| --- | --- | --- |
| Student | Review their profile, course results, GPA and achievements | Own information |
| Teacher | Maintain results and inspect performance for assigned courses | Assigned student/course records |
| Administrator | Manage test accounts, groups, course assignments and configuration | Explicitly authorized administrative operations |

The justification also mentions advisers. Their mapping to the teacher role and wider profile access must be agreed before implementation. Real university data access is not assumed; demonstrations use synthetic or authorized test data.

## MVP and later scope

| Initial MVP | Later enhancements |
| --- | --- |
| Login/logout with test accounts and server-enforced role access | University SSO and external system integration |
| Basic student profile and enrolled courses | Advanced competency and project portfolios |
| Grades, credits and configurable GPA calculation | CSV/Excel import, subject to scope agreement |
| Semester dashboard and transparent academic charts | Extended analytics and reporting |
| Selected achievements and certificates | PDF export and extracurricular activity tracking |
| Account, group and assignment administration | Full Kazakh/Russian/English localization |

Native mobile apps, replacing an LMS and unauthorized access to university databases are outside the initial scope. The architecture branch describes import as MVP while the Proposal lists it as a later enhancement; SDP-5 records this disagreement for review.

## Current status

This repository contains planning documentation. **There is no runnable application, package manifest, database migration or deployment configuration in the reviewed baseline.** Do not run invented `npm` or Docker setup commands.

Aimaut's deliverables are isolated in local task branches and have not been merged into `main`:

| Task | Branch | Main deliverable |
| --- | --- | --- |
| [SDP-5 · Requirements Specification](https://student-digital-profile.youtrack.cloud/issue/SDP-5) | `SDP-5-requirements-specification` | `docs/requirements/SDP-5-requirements-specification.md` |
| [SDP-7 · UX / Prototype](https://student-digital-profile.youtrack.cloud/issue/SDP-7) | `SDP-7-ux-prototype` | `docs/ux/SDP-7-ux-prototype.md`, `DESIGN.md`, `UX-CONTRACT.md` and Figma |
| [SDP-10 · GitHub README & Repository Structure](https://student-digital-profile.youtrack.cloud/issue/SDP-10) | `SDP-10-github-readme-repository-structure` | This README, documentation index and repository contribution conventions |

The Figma file contains 13 editable screens and predefined prototype journeys. Final screenshot/structural verification was blocked by the Figma Starter tool limit. It is a design deliverable, not a deployed application. Detailed YouTrack card descriptions were inaccessible; acceptance criteria in the authored documents remain proposed for team review.

## Technology direction

The existing [technology comparison](docs/technology-comparison/05-technology-comparison.md) proposes:

| Layer | Selected direction |
| --- | --- |
| Web interface | Next.js, React, TypeScript, Tailwind CSS |
| Charts | Apache ECharts |
| Profile API | Next.js Route Handlers, Zod |
| Data processing | Python, FastAPI, Pandas, SQLAlchemy |
| Storage | PostgreSQL |
| Contracts and identity | REST/JSON, OpenAPI, Auth.js / NextAuth.js with role checks |
| Verification | Jest, pytest and API checks |

These are design choices, not installed or verified dependencies. Token verification between services, database ownership and production file storage still need concrete implementation decisions. The data-processing architecture does not automatically make import an approved MVP requirement.

## Repository layout

Files present on **this SDP-10 branch**:

```text
student-digital-profile/
├── README.md
├── CONTRIBUTING.md
├── .github/
│   └── pull_request_template.md
└── docs/
    ├── README.md
    ├── repository/
    │   └── SDP-10-repository-guide.md
    └── technology-comparison/
        └── 05-technology-comparison.md
```

Other task documents remain in their respective branches. The [documentation index](docs/README.md) explains how to inspect them. The [repository guide](docs/repository/SDP-10-repository-guide.md) distinguishes current files from a proposed future code layout.

## Open locally in VS Code

For the existing checkout, open its folder in VS Code and select a task branch in the Git status bar. From the integrated terminal:

```powershell
git status
git branch --list
git switch SDP-5-requirements-specification
```

Save or commit your own changes before switching. To inspect a document without switching:

```powershell
git show SDP-5-requirements-specification:docs/requirements/SDP-5-requirements-specification.md
git show SDP-7-ux-prototype:docs/ux/SDP-7-ux-prototype.md
```

For a fresh clone, the verified remote of this checkout is:

```powershell
git clone https://github.com/Rakhat2434/student-digital-profile.git
cd student-digital-profile
git branch -a
```

Local task branches are available to a fresh clone only after they have been pushed. The previously mentioned organization repository is not this checkout's configured `origin`; verify the intended destination before publication. GitHub App installation is not required for ordinary local Git editing.

## Team

| Member | Contribution described in the supplied justification |
| --- | --- |
| Aimaut Bolatkhanuly (`aimautb`) | Frontend, UX prototypes, educational-data visualization; tasks SDP-5, SDP-7, SDP-10 |
| Rakhat Dosmagambetov | Backend digital-profile module, calculations and API |
| Damir Ushkempir | Backend/data processing; the Proposal also lists system analysis and QA |

Academic supervisor: **Gulzhan Soltan**. Final division of Damir's responsibilities should be reconciled in project planning. Personal contact details and GPA from the justification are intentionally excluded from repository documentation.

## Validation and contribution

Requirements define observable checks for GPA correctness, authorization, visualization consistency and usability. These checks are a future implementation/evaluation plan, not a passing test report. For documentation changes, verify relative links, Markdown formatting, source provenance and task isolation with `git diff --check` and a branch diff.

Use one task branch per deliverable, task-prefixed commits and a pull request with a concise validation note. See [CONTRIBUTING.md](CONTRIBUTING.md). No license has been selected in the reviewed repository; do not infer a reuse license from public visibility.
