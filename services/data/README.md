# Data processing service

Planned Python/FastAPI service from SDP-6. No runnable service, dependencies or database connection are supplied by this scaffold.

| Location | Responsibility |
| --- | --- |
| app/api/ | Thin FastAPI request/response adapters |
| app/core/ | Configuration and inter-service authentication |
| app/schemas/ | Pydantic request, row and result schemas |
| app/services/imports/ | Import jobs after scope decision D-01 |
| app/services/cleaning/ | Deduplication, validation and transformation |
| app/services/analytics/ | Agreed aggregation and bulk processing |
| app/repositories/ | SQLAlchemy access limited to agreed tables |

CSV/Excel import remains an unresolved scope decision; reserving its folder does not put it in the approved MVP. Core GPA policy and single-grade orchestration belong to the core API; agree any bulk-processing calculation contract before implementation.

Do not create independent core-schema migrations here: Prisma owns them in apps/web/prisma/. Never commit registrar exports or actual student records.

[Repository map](../../docs/repository/10-repository-structure.md) · [Architecture](../../docs/architecture/07-architecture.md)
