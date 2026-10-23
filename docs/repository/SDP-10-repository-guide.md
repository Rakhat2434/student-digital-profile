# SDP-10 · GitHub README & Repository Structure

Author: Aimaut Bolatkhanuly (`aimautb`) · 23 October 2026

Status: **Documentation prepared for review**

Task: [SDP-10](https://student-digital-profile.youtrack.cloud/issue/SDP-10)

## 1. Deliverable

The root README now explains the diploma project, users, MVP, future scope, technology direction, team, documentation locations and real local setup. A documentation index, contribution guide and PR template establish a clear handoff for the three task branches.

These files are scoped to SDP-10. Requirements remain in SDP-5; UX documentation and design contracts remain in SDP-7. `main` and teammates' branches were not changed.

## 2. Branch inspection

The following snapshot was obtained after `git fetch origin`:

| Ref | Commit | Finding |
| --- | --- | --- |
| `origin/main` | `7e04f9e` | Minimal README and organized technology-comparison document |
| `origin/SDP-1-Project-Proposal-&-Scope` | `5b34023` | Adds `docs/project-proposal/01-proposal.md` |
| `origin/SDP-2-Literature-Review` | `7e04f9e` | Same tip as baseline; no additional task artifact |
| `origin/SDP-3-Existing-Systems-Comparison` | `7e04f9e` | Same tip as baseline; no additional task artifact |
| `origin/SDP-4-technology-comparison` | `bdc635e` | Earlier uploaded technology material; current organized version is in main |
| `origin/SDP-6` | `9104c87` | Architecture Markdown and three PNG diagrams at root |
| `origin/SDP-9-Project-Management-&-Risks` | `7e04f9e` | Same tip as baseline; no additional task artifact |

The architecture document refers to diagram-source/export paths that are absent from that branch's observed tree; its images are actually at the root. Record this for the SDP-6 owner rather than silently rewriting their work in SDP-10. Its import-as-MVP statement also conflicts with Proposal section 7.2.

This checkout's configured remote is `https://github.com/Rakhat2434/student-digital-profile.git`. Publication to `digital-profile-diploma-project/student-digital-profile` was not assumed or performed.

## 3. Repository structure decisions

| Location | Ownership and purpose |
| --- | --- |
| `README.md` | Project entry point; concise scope and truthful project status |
| `CONTRIBUTING.md` | Branch, commit and review conventions |
| `.github/pull_request_template.md` | Reviewer-facing task, validation and open-decision prompts |
| `docs/README.md` | Documentation map, including explicit cross-branch locations |
| `docs/requirements/` | SDP-5 requirements after its branch is merged |
| `docs/ux/` | SDP-7 prototype, state ledger and review evidence after its branch is merged |
| `docs/repository/` | SDP-10 repository decisions and research notes |
| `docs/technology-comparison/` | Existing technology-choice document |

No code folders were created merely to imply progress. A **proposed future** implementation layout is:

```text
apps/web/               # Next.js UI and core API
services/data/          # FastAPI data-processing service
docs/api/              # Agreed API contracts when available
tests/                 # Cross-service acceptance/integration checks
infra/                 # Local/deployment configuration when implemented
```

This is a proposal for the backend/architecture owners, not an existing structure or a final architecture decision. Keep app-specific tests close to their implementation; use the top-level test directory only for cross-service scenarios. Choose one owner for database migrations before introducing two ORM stacks.

## 4. Comparable public repositories reviewed

References were used to study documentation organization. They are not substitutes for this project's requirements, verified implementations or university policies. No source code or README prose was copied.

| Repository / source | Relevance | Lesson applied here | Boundary |
| --- | --- | --- | --- |
| [StudentPortfolio README](https://github.com/sayedalimohamad/studentPortfolio/blob/main/README.md) | Student portfolios, supervisors, roles and file evidence | Explain users, role-specific capabilities and technology responsibilities | Its AI assistant, events and collaboration features are not added to our MVP |
| [Acadion Academic Dashboard README](https://github.com/natasyaruilla/academic-dashboard/blob/main/README.md) | Academic capstone workflow with student/admin interfaces | Separate project description, user features, repository structure and team contributions | Its capstone-team/worksheet workflow differs from our GPA/profile scope |
| [Student results dashboard](https://github.com/neromtoobad/student-results-dashboard) | Academic indicators, period-based results and sample data | Make numerical inputs, credit meaning and demo data visible in requirements | Its grading bands and import workflow are not adopted as university policy |

The first two READMEs were read through the GitHub connector. The third was inspected through web search results and is a supplementary reference, not a reviewed implementation. A separate search result for Student-E-Portfolio returned no accessible root README; no claims are based on it.

## 5. Review and validation

Documentation checks: Markdown whitespace, relative-link targets, existence of cross-branch documents and diff isolation. GPA examples were checked against the authored fixture. There are no application build or test commands in this baseline; reporting a successful application build would be inaccurate.

The SDP-7 strict static design audit reported no findings on the documentation-only branch. It does not establish browser accessibility or visual correctness. Figma verification calls were blocked by the Starter limit, which remains visible in the README and UX document.

- [x] Explain the project, users, scope and selected technology direction.
- [x] Provide actual branch/file locations and local Git instructions.
- [x] Separate the real repository tree from a proposed future code layout.
- [x] Review comparable documentation and record specific lessons with attribution.
- [x] Provide task-scoped commit and PR conventions.
- [ ] Reconcile detailed YouTrack acceptance criteria with the task owner.
- [ ] Review and publish each task branch when the destination is confirmed.
- [ ] Update the index to relative task-document links after their independent merges.

**Prepared review comment:** “SDP-10 replaces the placeholder README with the project overview, scoped MVP, technology direction, team contributions and real setup instructions. It adds a documentation index, contribution guide and PR template. Other task documents remain in their own branches; the guide records source conflicts and the exact repository state. No application implementation, deployment or completed usability study is claimed.”

The comment is saved locally for review and has not been posted to GitHub or YouTrack.
