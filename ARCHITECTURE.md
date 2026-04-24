# Architecture

## Overview

This repository provides a lightweight ML inference API with deterministic demo training for local and CI validation.

## Components

1. `api/main.py`
2. `src/analysis.py`
3. `tests/test_analysis.py`

## Runtime Flow

1. API starts and exposes health endpoint.
2. `POST /train/demo` generates synthetic records and trains models.
3. Trained artifacts are held in memory.
4. Prediction endpoints validate input and run feature transforms.

## Security and Validation

1. Input payload shape is validated with Pydantic.
2. Required feature checks reject malformed records.
3. Batch payload size is bounded (`min_length=1`, `max_length=2000`) to reduce abuse risk.

## Accessibility and Operability

1. Endpoint and deployment docs are plain-text and screen-reader friendly.
2. `/health` exposes service readiness and model-training state.

## Efficiency

1. Uses vectorized NumPy/Pandas transforms for inference throughput.
2. Keeps API surface compact to reduce runtime and network overhead.
