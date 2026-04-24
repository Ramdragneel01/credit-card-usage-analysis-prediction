# Deployment Guide

## Local Deployment

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn api.main:app --host 0.0.0.0 --port 8010
```

Health check:

```bash
curl http://127.0.0.1:8010/health
```

## Environment Variables

Use `.env.example` as a starter:

1. `HOST`
2. `PORT`
3. `LOG_LEVEL`
4. `API_KEY` (optional; enables API key protection on non-health endpoints)
5. `RATE_LIMIT_MAX` (max requests per client and endpoint in a window)
6. `RATE_LIMIT_WINDOW_SECONDS` (rate-limit window size in seconds)

## CI and Release

1. CI workflow: `.github/workflows/ci.yml`
2. Release workflow: `.github/workflows/release.yml`

Release tags use semantic versioning (`vX.Y.Z`).
