# Contributing

## One task, one branch

Aimaut's existing task branches are:

| Task | Branch |
| --- | --- |
| SDP-5 | `SDP-5-requirements-specification` |
| SDP-7 | `SDP-7-ux-prototype` |
| SDP-10 | `SDP-10-github-readme-repository-structure` |

Keep changes in their owning branch. Do not commit task work directly to `main`, mix another task's files into a commit, rewrite another member's branch or copy documents between branches to make links appear to work. Existing teammates' branches retain their names.

## Editing in VS Code

1. Run `git status` and ensure you understand any existing changes.
2. Switch to the correct task branch using `git switch <branch>` or the status-bar branch selector.
3. Edit the task's Markdown and preview it with **Ctrl+Shift+V**.
4. Stage explicit paths, inspect `git diff --cached` and run `git diff --check`.
5. Commit with the matching task identifier.

```powershell
git switch SDP-5-requirements-specification
git add docs/requirements/SDP-5-requirements-specification.md
git diff --cached --stat
git diff --check
git commit -m "docs(SDP-5): clarify requirement acceptance criteria"
```

Use similarly scoped messages for SDP-7 and SDP-10. Comments and review descriptions should explain the change, its evidence and unresolved decisions, without claiming implementation or testing that has not happened.

## Markdown conventions

- One descriptive H1, task ID, author, date and honest document status.
- Short sections, tables for comparisons, numbered steps for procedures.
- Stable requirement IDs; explicitly label assumptions, targets and open decisions.
- Use repository-relative links only when the destination exists on that branch.
- Link to external reference repositories and describe the specific lesson; do not copy their prose or broaden the product scope to match them.
- Keep private source documents, real student data and secrets out of Git.
- Check boxes only for completed work; “draft written” is different from “approved”.

## Publication and review

Local commits do not publish branches. Before pushing, confirm the remote with `git remote -v` and the diff with `git diff origin/main...HEAD --stat`. This checkout currently points to `Rakhat2434/student-digital-profile`; do not silently replace it with the organization URL from earlier project discussion.

When publication is intended, push the specific task branch and open its own pull request. Use the [PR template](.github/pull_request_template.md). Never force-push shared work. On 24 October 2026 the project owner requested final consolidation: SDP-10 now locally merges current main and the related SDP-5/7 histories. Keep source task ownership and explicitly disclose those dependencies during review; avoid bundling unrelated future work.

Reviewers should check scope consistency, requirement/test traceability, truthful completion claims, links and the absence of sensitive data. Update YouTrack status only when the actual task acceptance criteria are met and reviewed.
