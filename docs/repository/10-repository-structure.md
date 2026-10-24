# Repository structure · SDP-10

This is the tracked implementation scaffold for the architecture in SDP-6. Empty locations contain .gitkeep so Git retains them. Runtime code, dependency manifests and deployment configuration have not been implemented.

```text
student-digital-profile/
├── README.md                     project entry point
├── CONTRIBUTING.md               member / SDP task / short name
├── DESIGN.md                     design direction and tokens
├── UX-CONTRACT.md                interaction and implementation rules
├── Prototype.md                  team prototype guide and review record
├── .github/                      pull-request template
├── apps/
│   └── web/
│       ├── public/               public assets only
│       ├── prisma/
│       │   ├── migrations/       sole owner of core schema migrations
│       │   └── seeds/            fictional demonstration seed sources
│       └── src/
│           ├── app/
│           │   ├── login/
│           │   ├── student/      profile / academics / achievements
│           │   ├── teacher/      students
│           │   ├── admin/        users / groups / courses / assignments / grading
│           │   └── api/          auth / profiles / academic-records / grades /
│           │                     achievements / users / groups / courses /
│           │                     assignments / grading-policies
│           ├── features/         auth / profiles / academics / achievements /
│           │                     administration
│           ├── components/       ui / layout / charts
│           ├── lib/              api-client / validation
│           ├── server/           auth / services / repositories
│           └── styles/
├── services/
│   └── data/
│       └── app/
│           ├── api/              FastAPI adapters
│           ├── core/             configuration and service authentication
│           ├── schemas/          Pydantic input/output schemas
│           ├── repositories/     SQLAlchemy access to agreed tables
│           └── services/         imports / cleaning / analytics
├── packages/
│   └── contracts/                openapi / schemas
├── tests/
│   ├── unit/                     web / data
│   ├── integration/
│   ├── e2e/
│   └── fixtures/synthetic/
├── infra/                        docker / deploy
├── config/                       development / test / production
│   └── repository-layout.json    tracked directory manifest
├── scripts/                      check_repository.py
├── docs/
│   ├── project-proposal/         01-proposal.md · SDP-1
│   ├── literature-review/        02-literature-review.md · SDP-2
│   ├── existing-systems-comparison/ 03-existing-systems-comparison.md · SDP-3
│   ├── technology-comparison/    04-technology-comparison.md · SDP-4
│   ├── requirements/             05-requirements-specification.md · SDP-5
│   ├── architecture/             07-architecture.md · SDP-6
│   ├── diagrams/                 supplied PNGs and reserved src/
│   ├── ux/                       specification, artwork and prototype builder · SDP-7
│   ├── Verification & Evaluation Plan/ 08-verification-evaluation-plan.md · SDP-8
│   ├── project-management/       reserved task documents · SDP-9
│   ├── repository/               this structure guide · SDP-10
│   └── supervisor-feedback/      reserved feedback documents · SDP-11
└── prototype/                    acceptance review and SVG exports
```

## Where changes belong

| Work | Location | Initial responsibility |
| --- | --- | --- |
| Role pages, forms and academic charts | apps/web/src/app/, features/, components/ | Aimaut |
| Core REST API, authorization and GPA | apps/web/src/app/api/, src/server/ | Rakhat |
| Core database schema and migrations | apps/web/prisma/ | Rakhat; shared schema reviewed with data-service owner |
| Import/cleaning and aggregation | services/data/app/ | Damir; confirm implementation workload with the team |
| API schemas shared between services | packages/contracts/ | Core API and data-service owners together |
| Application verification | tests/ | Damir with the relevant implementation owner |
| Environment/deployment setup | config/, infra/ | Team decision before runtime setup |
| Diploma evidence and prototype | docs/, prototype/, Prototype.md | Existing SDP task owners in CONTRIBUTING.md |

The proposal and team justification disagree about Damir's implementation/QA workload; these locations clarify boundaries without claiming that the staffing decision is settled.

## Boundaries

The core API runs inside the Next.js application; a second independent core-backend directory is unnecessary. FastAPI is a separate data service. UI code must not import server repositories. Prisma owns core migrations; SQLAlchemy does not create a competing schema. Shared contracts carry data formats, not duplicated business logic.

An imports/ directory reserves the architecture's data-service capability; D-01 still controls whether CSV/Excel import is in the MVP. Actual grade rules, service authentication, storage and deployment settings still need implementation decisions. Certificates belong in protected storage with references in the database, never apps/web/public/.

Existing team document names, original PNGs, review records and the local Figma plugin directory are preserved. Prototype source and tests stay beside their builder so the existing manifest and relative imports continue to work. No local Figma plugin re-import is required by this structure change.

## Next implementation steps

1. Agree runtime versions and shared API contracts; add actual dependency manifests.
2. Add the web/core API and FastAPI entry points in their reserved locations.
3. Define Prisma schema, migrations and synthetic seed data; agree SQLAlchemy access.
4. Implement authentication, role/ownership checks and the agreed GPA policy.
5. Add meaningful application tests, then working setup/start/build instructions and deployment templates.

Check the scaffold with `python scripts/check_repository.py` from the repository root. This is a repository check, not an application test run.

[Documentation index](../README.md) · [Architecture](../architecture/07-architecture.md) · [Contributions](../../CONTRIBUTING.md)
