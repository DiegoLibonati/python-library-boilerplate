# CHANGELOG


## v0.1.0 (2026-05-14)

### Bug Fixes

- Apply best practice improvements across project
  ([`d162bcf`](https://github.com/DiegoLibonati/python-library-boilerplate/commit/d162bcf62d322d9d49517337520359c927a312a0))

- Better demo with pyproject command
  ([`164632d`](https://github.com/DiegoLibonati/python-library-boilerplate/commit/164632dfe473923572313d19fb17cddbcc84b295))

- Better repository name/description and better system test
  ([`7607cc9`](https://github.com/DiegoLibonati/python-library-boilerplate/commit/7607cc936ea85d735786be8a31ad863bc36ba55c))

- Better tests
  ([`dfd7c23`](https://github.com/DiegoLibonati/python-library-boilerplate/commit/dfd7c23221d3f9d5976b0765ff9e8902aab12507))

- Dependencies vulnerabilities fixed
  ([`148ebf6`](https://github.com/DiegoLibonati/python-library-boilerplate/commit/148ebf62caceae6c033321149c65141938c0fcd2))

- Pydantic model fix
  ([`d0c5dc4`](https://github.com/DiegoLibonati/python-library-boilerplate/commit/d0c5dc4f4466f5eea5454083b15cea9b10d32bf5))

- Remove migrations folder exclude from pre-commit-config
  ([`90c1f5a`](https://github.com/DiegoLibonati/python-library-boilerplate/commit/90c1f5a1d79717af58db149c4940b1a1b94e0f86))

- Title app
  ([`e43168e`](https://github.com/DiegoLibonati/python-library-boilerplate/commit/e43168edff41e7352b454dd10b94aac4080accdf))

- Update comment in demo.py
  ([`483c613`](https://github.com/DiegoLibonati/python-library-boilerplate/commit/483c6139bf4be8cf28e913e8bb9466894a49956b))

### Chores

- Migrate to pyproject.toml-based dependency management and improve project structure
  ([`917ca02`](https://github.com/DiegoLibonati/python-library-boilerplate/commit/917ca02aa575906de95cffe5ee60beb18f357c14))

- Declare runtime, dev, and test dependencies as pyproject.toml extras; requirements*.txt now
  delegate to them - Add GitHub Actions CI workflow with lint, build, and audit steps across Python
  3.11–3.13 - Add .editorconfig for consistent editor settings - Add py.typed marker and expose
  __version__ via importlib.metadata - Add CHANGELOG.md following Keep a Changelog format - Move
  main() entrypoint to examples/basic_usage.py - Expand ruff ruleset with B, SIM, RUF, C4 rules -
  Relax pydantic pin from ==2.11.9 to >=2.11,<3 range - Fix BaseError.__init__ argument order (code
  before message) - Remove stale # type: ignore comments from tests

### Continuous Integration

- Add automated changelog and versioning with python-semantic-release
  ([`9cf5cd2`](https://github.com/DiegoLibonati/python-library-boilerplate/commit/9cf5cd2584bb3b7ba7a8b4d2afbd6184baedf435))

- Split single job into lint-and-audit, testing, and build
  ([`174588c`](https://github.com/DiegoLibonati/python-library-boilerplate/commit/174588c45da9d8e48dc269a1d074ebc6681d3848))

Replaces the monolithic lint-and-build job with three chained jobs: lint-and-audit runs ruff and
  pip-audit on Python 3.13; testing runs pytest with coverage across the 3.11/3.12/3.13 matrix;
  build produces the distribution and asserts the .tar.gz artifact exists.

### Features

- .python-version file added
  ([`a4c7c8f`](https://github.com/DiegoLibonati/python-library-boilerplate/commit/a4c7c8f89015567b88f2c136febdeaec705a3f48))

- Added new section to readme: publishing to PyPI
  ([`07cec7c`](https://github.com/DiegoLibonati/python-library-boilerplate/commit/07cec7cb46501cd7c3a3c2e7b3be282687384938))

- Better readme
  ([`283bb68`](https://github.com/DiegoLibonati/python-library-boilerplate/commit/283bb6866648ab4f185145dbc96415bda0764e3c))

- Tests added
  ([`39a6f63`](https://github.com/DiegoLibonati/python-library-boilerplate/commit/39a6f63d03fdf70965b819e920e37b23ce7273bd))
