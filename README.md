# credit-card-usage-analysis-prediction

Production-focused FastAPI repository for credit-card behavior segmentation, activity prediction, and anomaly scoring.

## Implemented Scope

1. Synthetic dataset generator for repeatable local model training.
2. Segment model using KMeans.
3. Activity classifier using RandomForest.
4. Batch anomaly scoring using centroid-distance normalization.
5. FastAPI endpoints for health, training, summaries, and inference.
6. Unit tests for training, activity prediction, anomaly scoring, and segment summaries.

## Quick Start

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --host 0.0.0.0 --port 8010 --reload
```

## Quality Gate (Local CI Equivalent)

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
# Start API in one shell:
uvicorn api.main:app --host 127.0.0.1 --port 8010
# Then run smoke command in another shell:
curl http://127.0.0.1:8010/health
```

## API Endpoints

1. GET `/health`
2. POST `/train/demo`
3. GET `/segments/summary`
4. POST `/predict/activity`
5. POST `/predict/anomaly`

Additional API details are in `docs/API.md`.

## Smoke Commands

```bash
curl http://127.0.0.1:8010/health
curl -X POST "http://127.0.0.1:8010/train/demo?samples=1200&segment_count=4"
curl -X GET "http://127.0.0.1:8010/segments/summary?limit=100"
```

## Demo Evidence

Expected health response after startup:

```json
{
	"status": "ok",
	"trained": false,
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
3. Supports API key and in-memory throttling controls, but no identity provider integration or role-based authorization.

## Next Roadmap

1. Add persisted model registry and versioned artifacts.
2. Integrate managed identity provider and role-based access control.
3. Add model drift checks and richer observability metrics.

