# Python Library Boilerplate

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Description

**Python Library Boilerplate** is a production-ready starting point for building Python libraries from scratch. Instead of spending time setting up project structure, tooling, and architecture decisions every time you start a new library, this boilerplate gives you a solid, opinionated foundation that you can clone and build on top of immediately.

The project enforces a **layered architecture** where constants sit at the bottom, exceptions and utilities build on top of them, models handle input validation, and the main public class composes everything together. This separation ensures that each layer is independently testable and that concerns never leak across boundaries.

Out of the box you get a fully configured development environment: **Ruff** for linting and formatting with sensible rules, **pre-commit hooks** that run automatically before every commit, **Pydantic v2** for declarative data validation, a **structured logging setup** that avoids duplicate handlers, a **custom exception hierarchy** with machine-readable error codes and human-readable messages, and a **pytest suite** with coverage, parallelism, timeout, and environment variable support already wired up.

The intended workflow is: clone the repo, rename the package, delete or replace `template.py` and `template_model.py` with your own domain logic, and start building. Every scaffolding decision — file layout, import conventions, error handling strategy, test structure — has already been made following Python best practices so you do not have to.

## Technologies used

1. Python >= 3.11

## Libraries used

Dependencies are declared in `pyproject.toml` and split into optional groups so production installs stay minimal.

#### Runtime (`[project.dependencies]`)

```
pydantic>=2.11,<3
```

#### Dev (`[project.optional-dependencies]` dev)

```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
```

#### Test (`[project.optional-dependencies]` test)

```
pytest==8.4.2
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

## Getting Started

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Install all dependencies (runtime + dev + test) in editable mode: `pip install -e .[dev,test]`
6. (Optional) If your library reads environment variables, copy the example file: `cp .env.example .env` and fill in the values described in [Env Keys](#env-keys)
7. Run the demo: `python examples/basic_usage.py`
8. Or import as a library in Python: `from python_library_boilerplate import Template`

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Env Keys

This template does not use environment variables by default. However, if your library requires external configuration such as API keys, secrets, or service URLs, you can add them to the `.env` file following the `.env.example` structure.

```
# Example
MY_LIBRARY_API_KEY=your_api_key_here
MY_LIBRARY_BASE_URL=https://api.example.com
```

The consuming application is responsible for loading the `.env` file (e.g. using `python-dotenv`). The library itself should only read from `os.environ` via `os.getenv`.

## Project Structure

```
python_library_boilerplate/
├── .github/
│   └── workflows/
│       └── ci.yml
├── examples/
│   └── basic_usage.py
├── src/
│   └── python_library_boilerplate/
│       ├── __init__.py
│       ├── py.typed
│       ├── template.py
│       ├── configs/
│       │   ├── __init__.py
│       │   └── logger_config.py
│       ├── constants/
│       │   ├── __init__.py
│       │   ├── codes.py
│       │   └── messages.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── template_model.py
│       └── utils/
│           ├── __init__.py
│           └── exceptions.py
├── tests/
│   ├── configs/
│   │   ├── __init__.py
│   │   └── test_logger_config.py
│   ├── constants/
│   │   ├── __init__.py
│   │   ├── test_codes.py
│   │   └── test_messages.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── test_template_model.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── test_exceptions.py
│   ├── __init__.py
│   ├── conftest.py
│   └── test_template.py
├── .editorconfig
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
├── requirements.dev.txt
└── requirements.test.txt
```

1. `src/python_library_boilerplate` -> Root directory of the source code. Contains the full library logic following a **layered architecture** pattern.
2. `configs` -> Contains **logging setup** and any shared configuration utilities used across the library.
3. `constants` -> Holds **static values** such as error codes and user-facing messages, centralized to ensure consistency across the codebase.
4. `models` -> Defines **Pydantic models** for data validation and serialization.
5. `utils` -> Contains the **custom exception hierarchy** and other shared utilities used across multiple modules.
6. `template.py` -> The **main public class** of the library. This is the entry point that consumers interact with.
7. `tests` -> Contains **tests** organized to mirror the `src/` structure.
8. `conftest.py` -> Defines **shared pytest fixtures** used across all tests modules.
9. `pyproject.toml` -> **Unified project configuration** for setuptools, pytest, and ruff.
10. `examples/` -> Contains **runnable demos** showing how to use the public API.
11. `pyproject.toml` -> **Unified project configuration** including runtime deps, optional extras, and tool settings.
12. `requirements*.txt` -> Thin wrappers that delegate to `pyproject.toml` extras; kept for backward compatibility.

## Architecture & Design Patterns

The folder layout above maps directly onto the layered design described below — each top-level folder under `src/python_library_boilerplate/` corresponds to one layer.

### Layered Architecture

The library follows a **bottom-up layered architecture** where each layer depends only on the layers below it. This enforces clear separation of concerns and makes each layer independently testable.

```
┌─────────────────────────────────────┐
│         Template (Public API)       │  ← Layer 5: Business logic
├─────────────────────────────────────┤
│            models/                  │  ← Layer 4: Data validation (Pydantic)
├─────────────────────────────────────┤
│            configs/                 │  ← Layer 3: Infrastructure (logging)
├─────────────────────────────────────┤
│             utils/                  │  ← Layer 2: Exception hierarchy
├─────────────────────────────────────┤
│           constants/                │  ← Layer 1: Error codes & messages
└─────────────────────────────────────┘
```

**Layer 1 — `constants/`**: Single source of truth for all error codes (`codes.py`) and human-readable messages (`messages.py`). No other logic lives here; no imports from upper layers.

**Layer 2 — `utils/exceptions.py`**: Custom exception hierarchy rooted at `BaseError`. Each exception carries a `code` and a `message` pulled from the constants layer. Subclasses (`ValidationError`, `NotFoundError`, `AuthenticationError`, `ConflictError`, `BusinessError`, `InternalError`) represent distinct semantic error categories.

**Layer 3 — `configs/logger_config.py`**: Infrastructure setup. Exposes `setup_logger()`, which configures a `logging.Logger` with a consistent format and output stream. Depends only on the constants layer.

**Layer 4 — `models/`**: Pydantic `BaseModel` subclasses for declarative input validation. Validation rules (field constraints, type coercion) are declared here rather than scattered through business logic.

**Layer 5 — `template.py`**: The main `Template` class. This is the only public API surface (`__all__ = ["Template"]`). It composes all lower layers: uses the logger factory, raises typed exceptions, and validates inputs through models.

---

### Design Patterns

#### Factory Method — `setup_logger()`
`setup_logger(name)` is a factory function that creates and returns a fully configured `logging.Logger`. Consumers never instantiate loggers directly, ensuring a consistent format, level, and output stream across all modules.

#### Guard / Idempotent Initialization
Inside `setup_logger()`, the guard `if not logger.handlers:` prevents duplicate handlers from being attached when the function is called more than once with the same name. This is a common pattern when module-level loggers are used in libraries.

#### Custom Exception Hierarchy
All exceptions extend `BaseError`, which carries both a machine-readable `code` and a human-readable `message`. This enables callers to catch specific exception types (`except NotFoundError`) or the entire hierarchy (`except BaseError`), and to inspect structured error information programmatically.

```
Exception
└── BaseError
    ├── ValidationError
    ├── AuthenticationError
    ├── NotFoundError
    ├── ConflictError
    ├── BusinessError
    └── InternalError
```

#### Composition
The `Template` class does not inherit from lower-layer components. Instead, it **composes** them: the logger is obtained via `setup_logger()`, exceptions are raised using the exception hierarchy, and input validation is delegated to Pydantic models. This keeps the class focused on business logic and makes dependencies explicit.

#### Centralized Constants
Error codes and messages are defined once in `constants/` and imported wherever needed. This prevents magic strings from spreading through the codebase and makes updates (e.g., changing an error message) a single-file change.

#### Declarative Validation (Pydantic)
Input validation rules are expressed as field annotations on Pydantic models rather than imperative checks inside methods. This keeps the `Template` class lean and makes validation rules easy to read, test, and extend.

---

### Module Interaction Flow

```
Consumer Code
      │
      ▼
Template  ──► TemplateModel (validates input)
      │
      ├──► setup_logger()   (logging infrastructure)
      │
      ├──► NotFoundError / ValidationError / ...  (typed exceptions)
      │         └──► CODE_* / MESSAGE_*  (constants)
      │
      └──► CODE_* / MESSAGE_*  (constants, used directly when raising)
```

---

### Public API

Only `Template` is exported. All other modules (`constants`, `utils`, `configs`, `models`) are internal implementation details and should not be imported directly by consumers.

```python
from python_library_boilerplate import Template
```

## Testing

With the architecture in place, the test suite mirrors the `src/` layout so each layer can be exercised in isolation.

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Install test dependencies: `pip install -e .[test]`
6. Execute: `pytest --log-cli-level=INFO`

## Security Audit

Once the test suite is green, verify your dependencies for known vulnerabilities using **pip-audit** before producing any release artifact.

1. Go to the repository folder
2. Activate your virtual environment
3. Install dev dependencies: `pip install -e .[dev]`
4. Execute: `pip-audit`

## Build

When tests pass and the security audit is clean, build the distributable artifacts that will be uploaded in [Production](#production).

### 1. Bump the version

Update the `version` field in `pyproject.toml` following [Semantic Versioning](https://semver.org):

```
MAJOR.MINOR.PATCH
```

- `PATCH` — backwards-compatible bug fixes
- `MINOR` — new backwards-compatible functionality
- `MAJOR` — breaking changes

### 2. Build the package

```bash
pip install build
python -m build
```

This generates two files inside `dist/`:
- `*.tar.gz` — source distribution
- `*.whl` — built wheel

### 3. Validate the distribution

```bash
pip install twine
twine check dist/*
```

Fix any warnings before uploading.

## Production

Final checklist before publishing your library to [PyPI](https://pypi.org) so others can install it with `pip install <your-package>`. Each step links to the section that describes it in detail — this list only adds the production-only concerns (renaming, `.env.prod`, and the upload itself).

1. Run the full test suite — see [Testing](#testing).
2. Audit dependencies for known CVEs — see [Security Audit](#security-audit).
3. Bump the version and produce the artifacts in `dist/` — see [Build](#build).
4. **Configure production environment**: if your library exposes runtime configuration, duplicate `.env.example` as `.env.prod` and fill in the production values described in [Env Keys](#env-keys). The consuming application loads it; the library itself should only read from `os.environ`.
5. **Rename before publishing**: replace every occurrence of `python_library_boilerplate` / `python-library-boilerplate` in `pyproject.toml`, `src/`, and `tests/` with your actual package name. PyPI package names are global and permanent.
6. (Optional) Smoke-test on TestPyPI first:
   ```bash
   twine upload --repository testpypi dist/*
   pip install --index-url https://test.pypi.org/simple/ <your-package>
   ```
7. Upload to PyPI:
   ```bash
   twine upload dist/*
   ```
   You will be prompted for your PyPI credentials. It is recommended to use an [API token](https://pypi.org/manage/account/token/) instead of your password.

## Known Issues

None at the moment.

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/python-library-boilerplate`](https://www.diegolibonati.com.ar/#/project/python-library-boilerplate)
