# SDP-10 repository guide

Updated 24 October 2026. Owner: Aimaut Bolatkhanuly. Status: documentation published in PR #8; independent review pending.

Task: [SDP-10](https://student-digital-profile.youtrack.cloud/issue/SDP-10/GitHub-README-Repository-Structure).

## Repository and history

The project owner confirmed Rakhat2434/student-digital-profile as the target. The team checkout is D:/diploma/githubOfProject/secondgit/student-digital-profile; the SDP-10 branch is checked out in C:/Users/abola/AppData/Local/Temp/sdp10-acceptance-20261023.

After fetching origin, the reviewed main tip is ed0b682. It includes proposal, existing-systems comparison, technology decisions, architecture/diagrams and the verification plan, with the team's latest document renames preserved. See the [earlier branch and commit audit](project-review-2026-10-24.md).

The SDP-10 branch merges origin/main, SDP-5 and SDP-7 with the original histories intact. It supplies the root README, documentation index, short team-contribution table, PR template, ignore rules and guidance for the future code/config/test directories. Source task branches and remote main were not rewritten.

## Acceptance matrix

The authenticated YouTrack criteria were read on 24 October 2026.

| Criterion | Evidence | Status |
| --- | --- | --- |
| README includes required project information | Title, description, problem, users, outcomes, scope, status, team, supervisor, selected stack, links and truthful setup | Prepared |
| Directories are logically organised | docs/ by topic; prototype/ exports; apps/web/, services/data/, config/ and tests/ contain implementation guidance | Prepared |
| .gitignore configured | Environment overrides, credentials, keys, dependencies, builds, caches, local databases and private datasets excluded | Checked locally |
| No committed passwords, keys or confidential data | Local diff/filename/content inspection and synthetic prototype fixtures | No credential values identified by the targeted check; not a complete history-security audit |
| All team members have appropriate access | Author/merge history establishes contribution, not current permissions; connector permission reads returned 403 | Owner verification pending |
| GitHub and YouTrack traceability | Task links in README/docs, issue IDs in commits, PR links in YouTrack | Published in PRs #8, #9 and #10 |
| Another team member reviewed changes | No independent review link recorded | Pending |

Setup, startup and application-test instructions are conditional on runnable code in the task itself. There is no application manifest, database migration or runtime to execute yet, so those instructions are explicitly deferred rather than invented.

## Scope and consistency findings

- Proposal defers CSV/Excel import; architecture labels it MVP; SDP-8 gives it Should priority. Resolve with the requirements/architecture owners.
- The requirements and SDP-8 traceability tables need an agreed final ID/target mapping.
- Teacher visibility and certificate storage remain explicit decisions.
- Current diagram PNG paths are linked correctly. Editable PlantUML sources and SVG diagram exports were not found.
- The team Figma handoff is revision 03 in hOhNtoHcIS5VW5UfHqD0fC. Earlier cloud-file and installation-pending notices were reconciled with the recorded native verification. Remaining teacher/admin/mobile and administrative-flow gaps are retained.

## Handoff

Keep SDP-5, SDP-7 and SDP-10 In Progress while independent review or functional acceptance gaps remain. Review the owning PRs #9 and #10 before the consolidated PR #8; its description discloses those dependencies. Consolidation in SDP-10 does not merge the PRs into main.

The project owner subsequently authorised commits, pushes and PR creation. The branches are published and all three PRs remain open and unmerged. No external reviewer request was sent.
