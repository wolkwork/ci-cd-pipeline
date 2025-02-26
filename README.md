# CI/CD Pipeline

A simple Python project demonstrating a complete CI/CD pipeline using GitHub Actions and `uv` package manager.

## CI/CD Pipeline Steps

This project uses GitHub Actions to implement a CI/CD pipeline with the following stages:

1. **Test**: Runs unit tests with code coverage
2. **Quality**: Performs code quality checks (linting and type checking)
3. **Security**: Scans for security vulnerabilities
4. **Deploy**: Simulates deployment to a staging environment

## CI/CD Pipeline Diagram

```mermaid
flowchart TD
    A[Push Code to Repo] --> B[Test]
    B --> C[Quality]
    B --> D[Security]
    C --> E[Deploy]
    D --> E

    style A fill:#d0e0ff,stroke:#0066cc
    style B fill:#d0ffe0,stroke:#00cc66
    style C fill:#ffcc99,stroke:#00cc66
    style D fill:#ffcc99,stroke:#00cc66
    style E fill:#ffe0d0,stroke:#cc6600
```

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/wolkwork/ci-cd-pipeline.git
   cd ci-cd-pipeline
   ```

2. Install uv (if not already installed):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. Create a virtual environment and install dependencies:
   ```bash
   uv sync
   ```

## Running Tests

```bash
uv run pytest
```

With coverage:

```bash
uv run pytest --cov=src
```

## Running Linters and Type Checking

```bash
uv run ruff check .
uv run mypy src/
```

## GitHub Actions Configuration

The workflow is configured to run automatically when:

- Pushing to the `main` or `dev` branch
- Creating a pull request targeting the `main` or `dev` branch

The deployment job only runs on the `main` branch and not on pull requests.

## Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                       GitHub Actions                        │
└─────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                          Test Job                           │
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌──-──────────--─┐   │
│  │  Run Tests  │ -> │  Coverage   │ -> │ Report Results │   │
│  └─────────────┘    └─────────────┘    └───-─────────--─┘   │
└─────────────────────────────────────────────────────────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
┌─────────────────────────-────┐  ┌───────────────────────────-──┐
│         Quality Job          │  │         Security Job         │
│                              │  │                              │
│  ┌─────────┐  ┌───────-────┐ │  │ ┌───────--─┐  ┌───────────┐  │
│  │ Linting │->│ Type Check │ │  │ │ Dep Scan │->│ Code Scan │  │
│  └─────────┘  └─────-──────┘ │  │ └─────-────┘  └───────────┘  │
└────────────────────────-─────┘  └────────────────────────-─────┘
                 │                           │
                 └─────────────┬─────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                        Deploy Job                           │
│                                                             │
│  ┌─────────┐  ┌──────-───┐  ┌───────-──┐  ┌─────────────┐   │
│  │  Build  │->│ Validate │->│  Deploy  │->│ Smoke Tests │   │
│  └─────────┘  └────────-─┘  └──────-───┘  └─────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## License

MIT
