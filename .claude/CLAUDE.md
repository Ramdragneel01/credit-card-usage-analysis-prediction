# Repository Collaboration Context

## Purpose

This repository provides a production-oriented baseline for credit-card usage analytics with FastAPI and local ML workflows.

## Core Files

1. `api/main.py`: API routes and request validation.
2. `src/analysis.py`: dataset generation, training, and inference logic.
3. `tests/test_analysis.py`: model behavior tests.

## Standard Commands

```bash
pip install -r requirements.txt
pytest -q
uvicorn api.main:app --host 0.0.0.0 --port 8010 --reload
```

## Change Rules

1. Keep API payload contracts backward compatible unless documented.
2. Add tests for new model or endpoint behavior.
3. Keep security, deployment, and testing docs aligned with implementation.
4. Avoid adding heavyweight runtime dependencies without clear value.
