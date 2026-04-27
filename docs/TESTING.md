# Testing Guide

## Unit Tests

```bash
pytest -q
```

Current tests validate:

1. Training and prediction output shape.
2. Anomaly score bounds (`0.0` to `1.0`).
3. Segment summary count consistency.
4. API key enforcement and rate limiting.
5. Security headers and request tracing headers.
6. Readiness behavior when model training is required.
7. Request-size limits and feature-range validation.

## API Smoke Test

```bash
# Start API in one shell:
uvicorn api.main:app --host 127.0.0.1 --port 8010
# Then run smoke command in another shell:
curl http://127.0.0.1:8010/health/liveness
```

## CI Notes

CI runs tests and a health smoke check on push and pull request events.
