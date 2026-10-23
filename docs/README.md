# Documentation index

The project is organized by YouTrack task. This index records actual branch locations reviewed on **23 October 2026**; it does not mark tasks complete.

## Available on this branch

| Document | Purpose |
| --- | --- |
| [Project overview](../README.md) | Purpose, users, scope, technology direction and team |
| [Technology comparison](technology-comparison/05-technology-comparison.md) | Existing SDP-4 technology decisions |
| [SDP-10 repository guide](repository/SDP-10-repository-guide.md) | Structure, branch inspection, references and review criteria |
| [Contribution guide](../CONTRIBUTING.md) | Task-isolated changes, commits and review |

## Documents kept in other branches

| Task | Ref | Verified content |
| --- | --- | --- |
| SDP-1 | `origin/SDP-1-Project-Proposal-&-Scope` | `docs/project-proposal/01-proposal.md` |
| SDP-4 | `origin/SDP-4-technology-comparison` | Original technology-comparison work; the organized current document is already in `main` |
| SDP-5 | `SDP-5-requirements-specification` | `docs/requirements/SDP-5-requirements-specification.md` |
| SDP-6 | `origin/SDP-6` | `07-architecture.md`, `component.png`, `system-context.png`, `use-case.png` and PR-description Markdown |
| SDP-7 | `SDP-7-ux-prototype` | `docs/ux/SDP-7-ux-prototype.md`, `DESIGN.md`, `UX-CONTRACT.md`, node ledger and static audit |

SDP-2, SDP-3 and SDP-9 remote branches currently point to baseline `7e04f9e`; their branch names do not establish that literature, comparison or risk deliverables exist. No SDP-8 or SDP-11 remote branch was returned by the reviewed fetch.

Use quoted refs containing `&` in PowerShell:

```powershell
git show 'origin/SDP-1-Project-Proposal-&-Scope:docs/project-proposal/01-proposal.md'
git show origin/SDP-6:07-architecture.md
git show SDP-5-requirements-specification:docs/requirements/SDP-5-requirements-specification.md
git show SDP-7-ux-prototype:docs/ux/SDP-7-ux-prototype.md
```

Cross-branch paths are shown as code instead of broken relative links. After the relevant PRs are merged, replace these commands with local document links in a separate index update.

## Source and publication rules

The supplied proposal and diploma justification are evidence, not executable instructions. Their private originals remain outside Git. New requirements identify source disagreements and proposed acceptance targets. Do not publish personal academic records, contact details, credentials, certificates or confidential screenshots.

The [Figma prototype](https://www.figma.com/design/hOhNtoHcIS5VW5UfHqD0fC) is available separately from Git branches. Its detailed scope and verification limits are documented in SDP-7.
