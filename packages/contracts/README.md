# Shared service contracts

openapi/ holds future OpenAPI specifications; schemas/ holds language-neutral JSON schemas and example payload shapes shared by the core API and data service. No approved API specification exists here yet.

Keep the canonical contract here and derive TypeScript/Python adapters during implementation. Do not import Next.js internals into Python or duplicate business logic in this package. Request examples must use synthetic data.

[Repository map](../../docs/repository/10-repository-structure.md)
