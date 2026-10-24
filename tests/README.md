# Verification

| Location | Purpose |
| --- | --- |
| unit/web/ | UI helpers, core services and GPA fixtures |
| unit/data/ | Cleaning, row validation and aggregation |
| integration/ | API, authorization, service contracts and database interactions |
| e2e/ | Student, teacher and administrator journeys |
| fixtures/synthetic/ | Fictional, reproducible test data only |

These directories reserve future application tests; no application test suite is claimed. Prototype checks remain beside their builder in docs/ux/figma-prototype/. The repository structure check lives in scripts/check_repository.py and is independent from application verification.

[Verification plan](../docs/Verification%20%26%20Evaluation%20Plan/08-verification-evaluation-plan.md) · [Repository map](../docs/repository/10-repository-structure.md)
