# Student Digital Profile

A web-based academic profile for student records, progress and achievements.

> Development of an Information System for Creating and Visualizing Student Digital Profiles.

**Status:** requirements and prototyping. The final README and repository structure will be consolidated after the team's task deliverables are completed and reviewed in YouTrack.

## About

Student Digital Profile brings course results, GPA and achievement evidence into one place. Students review their progress, teachers maintain results for assigned courses, and administrators manage accounts and academic assignments.

## Problem and users

- **Problem:** academic records and achievements are stored separately, making student progress difficult to review as a whole.
- **Users:** students, teachers and administrators.
- **Expected outcomes:** a role-based web application, traceable academic indicators, an interactive prototype and project documentation.

## Scope

The planned MVP includes test-account authentication, student profiles, semester results, configurable GPA, academic charts, achievements and account/assignment administration.

CSV/Excel import, external integrations, advanced competency portfolios and PDF export are proposed future extensions. Import scope remains subject to team agreement.

## Team

| Member | Responsibility |
| --- | --- |
| Aimaut Bolatkhanuly (`aimautb`) | Frontend, UX prototype and data visualization |
| Rakhat Dosmagambetov | Digital-profile backend, calculations and API |
| Damir Ushkempir | Data processing, backend, analysis and QA |
| Gulzhan Soltan | Academic supervisor |

## Planned stack

Next.js, React, TypeScript, Tailwind CSS, Apache ECharts, FastAPI, Pandas and PostgreSQL. See the [technology comparison](docs/technology-comparison/05-technology-comparison.md) for the proposed stack and trade-offs.

## Links and documentation

- [YouTrack project](https://student-digital-profile.youtrack.cloud/projects/SDP/issues)
- [Figma prototype](https://www.figma.com/design/hOhNtoHcIS5VW5UfHqD0fC)
- [Documentation index](docs/README.md)
- [Contribution guide](CONTRIBUTING.md)

Requirements and prototype materials remain in their SDP-5 and SDP-7 branches until review and merge. The prototype uses scripted demonstration states; it is not a deployed application.

## Structure and setup

The final directory map and verified setup/test commands will be added after the team's deliverables are integrated. The reviewed baseline currently contains documentation rather than a runnable application.

## Contributing

- Use a separate branch for each YouTrack task.
- Include the task ID in commit messages and pull requests.
- Describe validation and obtain review from another team member.
- Keep secrets and real student records outside the repository.
