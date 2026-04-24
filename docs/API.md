# API Reference

Base URL (local): `http://127.0.0.1:8010`

## GET /health

Returns service readiness and model-training state.

Example response:

```json
{
  "status": "ok",
  "trained": false,
  "feature_columns": ["avg_ticket", "monthly_txn_count", "online_ratio", "weekend_ratio", "category_entropy", "chargeback_ratio"]
}
```

## POST /train/demo

Trains in-memory model artifacts from synthetic records.

Query params:

1. `samples` (default: `1500`)
2. `segment_count` (default: `4`)

## GET /segments/summary

Returns distribution of predicted segment IDs for synthetic sample records.

Query params:

1. `limit` (default: `600`)

## POST /predict/activity

Predicts active vs low-activity class and confidence per record.

Request body:

```json
{
  "records": [
    {
      "avg_ticket": 57.2,
      "monthly_txn_count": 22,
      "online_ratio": 0.71,
      "weekend_ratio": 0.32,
      "category_entropy": 1.6,
      "chargeback_ratio": 0.03
    }
  ]
}
```

## POST /predict/anomaly

Returns normalized anomaly score (`0.0` to `1.0`) per record using nearest segment-centroid distance.

## Error Responses

1. `400`: model artifacts not trained yet.
2. `422`: request schema or feature column validation errors.
