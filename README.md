# credit-card-usage-analysis-prediction

MVP repository for customer segmentation, activity prediction, and anomaly scoring on credit-card usage patterns.

## Implemented Scope

1. Synthetic data generator for behavior simulation and local testing.
2. Clustering workflow for customer segmentation.
3. Activity prediction model for active vs low-activity users.
4. Anomaly scoring endpoint based on distance from learned customer segments.
5. FastAPI service for training, prediction, and segment summaries.
6. Basic unit tests for training and scoring paths.

## Run Locally

```bash
python -m venv .venv
# Windows PowerShell: .\\.venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --host 0.0.0.0 --port 8010 --reload
```

## API Endpoints

1. GET /health
2. POST /train/demo
3. GET /segments/summary
4. POST /predict/activity
5. POST /predict/anomaly

## Tests

```bash
pytest -q
```
