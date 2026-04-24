# Contributing

## Development Setup

1. Create and activate a virtual environment.
2. Install dependencies from `requirements.txt`.
3. Run tests before opening a pull request.

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
```

## Pull Request Requirements

1. Keep changes scoped and documented.
2. Add or update tests for behavior changes.
3. Ensure CI passes on your branch.
4. Update `CHANGELOG.md` for notable changes.

## Security Expectations

1. Do not commit secrets or customer data.
2. Validate all external inputs.
3. Prefer deterministic and bounded processing for API calls.
