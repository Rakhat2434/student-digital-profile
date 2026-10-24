# SDP-10 repository guide

Updated 24 October 2026. Owner: Aimaut Bolatkhanuly. Status: local documentation complete for review; task acceptance pending.

Task: [SDP-10](https://student-digital-profile.youtrack.cloud/issue/SDP-10/GitHub-README-Repository-Structure).

## Repository and history

The project owner confirmed Rakhat2434/student-digital-profile as the target. The team checkout is D:/diploma/githubOfProject/secondgit/student-digital-profile; the SDP-10 branch is checked out in C:/Users/abola/AppData/Local/Temp/sdp10-acceptance-20261023.

After fetching origin, the reviewed main tip is d39dbb3. It includes proposal, existing-systems comparison, technology decisions, architecture/diagrams and the verification plan. See the [branch and commit audit](project-review-2026-10-24.md).

The SDP-10 branch locally merges origin/main, SDP-5 and SDP-7 with the original histories intact. It supplies the root README, documentation index, contribution workflow, PR template, ignore rules and guidance for the future code/config/test directories. Source task branches and remote main were not rewritten.

## Acceptance matrix

The authenticated YouTrack criteria were read on 24 October 2026.

| Criterion | Evidence | Status |
| --- | --- | --- |
| README includes required project information | Title, description, problem, users, outcomes, scope, status, team, supervisor, selected stack, links and truthful setup | Prepared |
| Directories are logically organised | docs/ by topic; prototype/ exports; apps/web/, services/data/, config/ and tests/ contain implementation guidance | Prepared |
| .gitignore configured | Environment overrides, credentials, keys, dependencies, builds, caches, local databases and private datasets excluded | Checked locally |
| No committed passwords, keys or confidential data | Local diff/filename/content inspection and synthetic prototype fixtures | No credential values identified by the targeted check; not a complete history-security audit |
| All team members have appropriate access | Author/merge history establishes contribution, not current permissions; connector permission reads returned 403 | Owner verification pending |
| GitHub and YouTrack traceability | Task links in README/docs, issue IDs in commits, scoped acceptance updates | Prepared; local commits are not yet published |
| Another team member reviewed changes | No independent review link recorded | Pending |

Setup, startup and application-test instructions are conditional on runnable code in the task itself. There is no application manifest, database migration or runtime to execute yet, so those instructions are explicitly deferred rather than invented.

## Scope and consistency findings

- Proposal defers CSV/Excel import; architecture labels it MVP; SDP-8 gives it Should priority. Resolve with the requirements/architecture owners.
- The requirements and SDP-8 traceability tables need an agreed final ID/target mapping.
- Teacher visibility and certificate storage remain explicit decisions.
- Current diagram PNG paths are linked correctly. Editable PlantUML sources and SVG diagram exports were not found.
- The team Figma handoff is revision 03 in hOhNtoHcIS5VW5UfHqD0fC. Earlier cloud-file and installation-pending notices were reconciled with the recorded native verification. Remaining teacher/admin/mobile and administrative-flow gaps are retained.

## Handoff

Keep SDP-5, SDP-7 and SDP-10 In Progress while publication/review or functional acceptance gaps remain. Publish/review the owning branches before the final SDP-10 PR, or disclose the branch dependencies in a stacked review. The local consolidation is not evidence of a remote merge.

The project owner requested no GitHub push. No PR, remote branch change or external reviewer request was performed.
