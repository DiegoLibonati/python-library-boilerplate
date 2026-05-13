# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2024-01-01

### Added

- Initial release of Python Library Boilerplate.
- Layered architecture: constants → utils/exceptions → configs/logger → models → Template.
- Custom exception hierarchy (`BaseError` and six semantic subclasses).
- Pydantic v2 model for input validation.
- Structured logger factory (`setup_logger`) with duplicate-handler guard.
- pytest suite with coverage, parallelism, timeout, and environment-variable support.
- Ruff lint and format, pre-commit hooks.
- `src/` layout with `pyproject.toml`-based build.
