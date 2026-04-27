# API Reference

Base URL (local): `http://127.0.0.1:8010`

## GET /health

Returns service runtime summary and model-training state.

This endpoint is intentionally public and does not require API key auth.

Example response:

```json
{
  "status": "ok",
  "environment": "development",
  "trained": false,
  "uptime_seconds": 12.74,
  "docs_enabled": true,
  "feature_columns": ["avg_ticket", "monthly_txn_count", "online_ratio", "weekend_ratio", "category_entropy", "chargeback_ratio"]
}
```

## GET /health/liveness

Lightweight liveness probe for orchestrators and load balancers.

## GET /health/readiness

Readiness probe. When `REQUIRE_MODEL_FOR_READINESS=true`, this endpoint returns `503` until `POST /train/demo` runs (or startup auto-training is enabled).

## POST /train/demo

Trains in-memory model artifacts from synthetic records.

Security behavior:

1. Requires `X-API-Key` header when `API_KEY` is configured.
2. Subject to in-memory request throttling using `RATE_LIMIT_MAX` and `RATE_LIMIT_WINDOW_SECONDS`.

Query params:

1. `samples` (default: `1500`)
2. `segment_count` (default: `4`)

## GET /segments/summary

Returns distribution of predicted segment IDs for synthetic sample records.

Security behavior:

1. Requires `X-API-Key` header when `API_KEY` is configured.
2. Subject to in-memory request throttling.

Query params:

1. `limit` (default: `600`)

## POST /predict/activity

Predicts active vs low-activity class and confidence per record.

Security behavior:

1. Requires `X-API-Key` header when `API_KEY` is configured.
2. Subject to in-memory request throttling.

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

Feature constraints:

1. `avg_ticket`: `> 0` and `<= 10000`
2. `monthly_txn_count`: `>= 0` and `<= 100000`
3. `online_ratio`: `0.0` to `1.0`
4. `weekend_ratio`: `0.0` to `1.0`
5. `category_entropy`: `0.0` to `10.0`
6. `chargeback_ratio`: `0.0` to `1.0`

## POST /predict/anomaly

Returns normalized anomaly score (`0.0` to `1.0`) per record using nearest segment-centroid distance.

Security behavior:

1. Requires `X-API-Key` header when `API_KEY` is configured.
2. Subject to in-memory request throttling.

## Error Responses

1. `401`: missing/invalid API key when auth is enabled.
2. `413`: request body exceeds `MAX_REQUEST_BYTES`.
3. `422`: request schema or feature validation errors.
4. `429`: request rate limit exceeded.
5. `503`: model artifacts not trained yet (prediction and segment endpoints).

## Transport Hardening

All responses include baseline security and observability headers:

1. `X-Request-ID`
2. `X-Process-Time-Ms`
3. `X-Content-Type-Options: nosniff`
4. `X-Frame-Options: DENY`
5. `Referrer-Policy: no-referrer`
6. `Permissions-Policy: camera=(), geolocation=(), microphone=()`
