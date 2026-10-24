# Web application and core API

Planned Next.js/React/TypeScript application from SDP-6. This is a directory scaffold; no web runtime or dependency manifest is implemented yet.

| Location | Responsibility |
| --- | --- |
| src/app/ | Role pages and thin HTTP Route Handlers under api/ |
| src/features/ | Authentication, profiles, academics, achievements and administration UI |
| src/components/ | Reusable UI, layout and chart components |
| src/lib/ | Browser API client and shared validation helpers; no database credentials |
| src/server/ | Server-only authorization, business services (including GPA) and database repositories |
| src/styles/ | Shared styles and design tokens |
| public/ | Public static assets only; never certificates or student uploads |
| prisma/ | Core database schema, migrations and synthetic seed sources |

Route Handlers call server services after validation and role/ownership checks. UI components must not access Prisma or the data-service database directly. Business logic belongs in server/services/, not in page components or route adapters.

Prisma owns core schema migrations. Python repositories use the agreed schema; do not introduce a second migration owner without an architecture decision. The folder names reserve areas; they do not approve final endpoint URLs or implement screens.

[Repository map](../../docs/repository/10-repository-structure.md) · [Architecture](../../docs/architecture/07-architecture.md)
