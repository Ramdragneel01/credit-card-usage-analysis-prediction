# Architecture

## Overview

This repository provides a lightweight ML inference API with deterministic demo training for local and CI validation.

## Components

1. `api/main.py`
2. `src/analysis.py`
3. `tests/test_analysis.py`

## Runtime Flow

1. API starts with trusted-host, optional CORS, and response-hardening middleware.
2. `POST /train/demo` generates synthetic records and trains models.
3. Trained artifacts are held in memory.
4. Prediction endpoints validate input and run feature transforms.

## Security and Validation

1. Input payload shape and feature ranges are validated with Pydantic.
2. Optional API key and in-memory throttling protect non-health endpoints.
3. Request body size is capped using `MAX_REQUEST_BYTES`.
4. Security headers and request-tracing headers are added at middleware level.
5. Trusted host filtering defends against host-header abuse.

## Accessibility and Operability

1. Endpoint and deployment docs are plain-text and screen-reader friendly.
2. `/health/liveness` and `/health/readiness` support container orchestrator probes.

## Efficiency

1. Uses vectorized NumPy/Pandas transforms for inference throughput.
2. Keeps API surface compact to reduce runtime and network overhead.
