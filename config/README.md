# Shared configuration

development/, test/ and production/ reserve documented non-secret configuration defaults. Component-specific runtime configuration stays with its component; deployment templates stay in infra/.

repository-layout.json defines the tracked scaffold. No runtime environment-variable contract has been approved yet. Add component-local .env.example files when implementation establishes actual variables; use placeholders and keep real .env files out of Git.
