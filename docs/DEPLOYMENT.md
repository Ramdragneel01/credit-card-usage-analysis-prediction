# Deployment Guide

## Local Deployment

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn api.main:app --host 0.0.0.0 --port 8010 --workers 1
```

Health check:

```bash
curl http://127.0.0.1:8010/health/liveness
```

## Environment Variables

Use `.env.example` as a starter:

1. `ENVIRONMENT` (`development` or `production`)
2. `HOST` and `PORT`
3. `UVICORN_WORKERS` (default `1`; increase only when you externalize shared state)
4. `LOG_LEVEL`
5. `API_KEY` (optional; enables API key protection on non-health endpoints)
6. `RATE_LIMIT_MAX` and `RATE_LIMIT_WINDOW_SECONDS`
7. `MAX_REQUEST_BYTES` (rejects oversized request bodies with `413`)
8. `TRUSTED_HOSTS` (comma-separated, strongly recommended in production)
9. `CORS_ALLOW_ORIGINS` (comma-separated; empty disables CORS headers)
10. `ENABLE_API_DOCS` (defaults to `false` in production)
11. `REQUIRE_MODEL_FOR_READINESS` (optional readiness gate)
12. `AUTO_TRAIN_ON_STARTUP`, `STARTUP_TRAIN_SAMPLES`, `STARTUP_TRAIN_SEGMENT_COUNT`

## Container Deployment

Build image:

```bash
docker build -t credit-card-usage-analysis-prediction:latest .
```

Run container:

```bash
docker run --rm -p 8010:8010 \
	--env-file .env \
	credit-card-usage-analysis-prediction:latest
```

Container liveness check:

```bash
curl http://127.0.0.1:8010/health/liveness
```

## Kubernetes Deployment

Apply deployment and service:

```bash
kubectl apply -f deploy/k8s/deployment.yaml
```

Create or update API key secret (PowerShell):

```powershell
$apiKey = (Get-Content .env.production | Where-Object { $_ -like 'API_KEY=*' } | ForEach-Object { $_.Split('=',2)[1] })
kubectl create secret generic credit-card-usage-secrets --from-literal=API_KEY="$apiKey" --dry-run=client -o yaml | kubectl apply -f -
```

Probe wiring:

1. `livenessProbe` uses `/health/liveness`.
2. `readinessProbe` uses `/health/readiness`.
3. `startupProbe` uses `/health/liveness`.

Verify probes and rollout:

```bash
kubectl rollout status deployment/credit-card-usage-api
kubectl get pods -l app=credit-card-usage-api
kubectl describe pod -l app=credit-card-usage-api
```

## Production Checklist

1. Set `ENVIRONMENT=production`.
2. Set a strong `API_KEY` if the API is internet-exposed.
3. Replace wildcard `TRUSTED_HOSTS=*` with explicit hostnames.
4. Configure `CORS_ALLOW_ORIGINS` explicitly for frontend callers.
5. Tune `RATE_LIMIT_MAX`, `RATE_LIMIT_WINDOW_SECONDS`, and `MAX_REQUEST_BYTES`.
6. Keep `UVICORN_WORKERS=1` until moving model and rate-limit state to shared backends.

## CI and Release

1. CI workflow: `.github/workflows/ci.yml`
2. Release workflow: `.github/workflows/release.yml`

Release tags use semantic versioning (`vX.Y.Z`).
