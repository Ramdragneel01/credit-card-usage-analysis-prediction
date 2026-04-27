# Changelog

All notable changes to this project are documented in this file.

## [0.2.0] - 2026-04-27

### Added

1. Runtime hardening middleware for response security headers and request tracing (`X-Request-ID`, `X-Process-Time-Ms`).
2. Request size enforcement via `MAX_REQUEST_BYTES`.
3. New health probe endpoints: `GET /health/liveness` and `GET /health/readiness`.
4. Feature-level payload validation model for inference requests.
5. Deployment container artifacts: `Dockerfile` and `.dockerignore`.
6. Additional API hardening tests covering readiness, headers, and body-size limits.

### Changed

1. `GET /health` now includes environment and uptime metadata.
2. Untrained-model error status changed from `400` to `503` for inference/segment endpoints.
3. Deployment and API docs updated for new environment variables and production checklist.

## [0.1.0] - 2026-04-24

### Added

1. Governance baseline files (`ARCHITECTURE.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CODEOWNERS`, `.env.example`).
2. Repository collaboration guidance in `.claude/CLAUDE.md`.
3. Operational docs in `docs/API.md`, `docs/DEPLOYMENT.md`, and `docs/TESTING.md`.
4. GitHub Actions workflows for CI and release tagging.
5. README production-evidence, smoke commands, limitations, and roadmap sections.
