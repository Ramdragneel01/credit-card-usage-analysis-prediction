# credit-card-usage-analysis-prediction

Production-focused FastAPI repository for credit-card behavior segmentation, activity prediction, and anomaly scoring.

## Implemented Scope

1. Synthetic dataset generator for repeatable local model training.
2. Segment model using KMeans.
3. Activity classifier using RandomForest.
4. Batch anomaly scoring using centroid-distance normalization.
5. FastAPI endpoints for liveness, readiness, training, summaries, and inference.
6. API hardening with request-size limits, trusted-host filtering, security headers, API-key auth, and rate limiting.
7. Unit tests for model behavior and API security controls.

## Quick Start

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --host 0.0.0.0 --port 8010 --workers 1
```

## Container Quick Start

```bash
docker build -t credit-card-usage-analysis-prediction:latest .
docker run --rm -p 8010:8010 --env-file .env credit-card-usage-analysis-prediction:latest
```

## Testing

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
# Start API in one shell:
uvicorn api.main:app --host 127.0.0.1 --port 8010
# Then run smoke command in another shell:
curl http://127.0.0.1:8010/health/liveness
```

## API Endpoints

1. GET `/health`
2. GET `/health/liveness`
3. GET `/health/readiness`
4. POST `/train/demo`
5. GET `/segments/summary`
6. POST `/predict/activity`
7. POST `/predict/anomaly`

Additional API details are in `docs/API.md`.

## Smoke Commands

```bash
curl http://127.0.0.1:8010/health
curl http://127.0.0.1:8010/health/liveness
curl http://127.0.0.1:8010/health/readiness
curl -X POST "http://127.0.0.1:8010/train/demo?samples=1200&segment_count=4"
curl -X GET "http://127.0.0.1:8010/segments/summary?limit=100"
```

## Demo Evidence

Expected health response after startup:

```json
{
	"status": "ok",
	"environment": "development",
	"trained": false,
	"uptime_seconds": 5.31,
	"docs_enabled": true,
	"feature_columns": [
		"avg_ticket",
		"monthly_txn_count",
		"online_ratio",
		"weekend_ratio",
		"category_entropy",
		"chargeback_ratio"
	]
}
```

After `POST /train/demo`, `trained` becomes `true` and segment distribution is returned.

## Limitations

1. Uses synthetic data only; no production data integration yet.
2. Uses in-memory model artifacts without persistence.
3. Uses in-memory throttling, which is per-process and should be replaced by shared-rate-limiting for horizontally scaled deployments.

## Roadmap

1. Add persisted model registry and versioned artifacts.
2. Integrate managed identity provider and role-based access control.
3. Add model drift checks and richer observability metrics.

