# Python Backend Development – Learning Plan

## Teaching Guidelines (Apply to Every Bullet Point)

For each topic/bullet, the AI teacher must:

1. **Explain the concept**
   - Use simple, clear language.
   - Relate to real-world backend scenarios (e.g., REST APIs, microservices, data APIs).

2. **Show Python code examples**
   - Use realistic FastAPI apps, `asyncio`, `uvicorn`, etc.
   - Keep it minimal, working, and idiomatic.

3. **Explain what the code does**
   - Walk through it step by step.
   - Highlight the “Pythonic” and “production-grade” practices.

4. **Give practical notes**
   - Why it matters for robust, scalable backends.
   - Dev pitfalls, performance caveats, testing strategies.

5. **End with a short summary + optional “Try it yourself”**
   - Example: *“Try creating a FastAPI route that accepts a JSON payload and returns a filtered response.”*

---

## 1. FastAPI Fundamentals

### What Is FastAPI?
- Modern, async-first Python web framework.
- Type hints + OpenAPI out of the box.
- Give explanations about what asyncio and Starlette is.
- Give explanations about what Pydantic is.
- Ideal for microservices, REST APIs, and ML inference endpoints.

### Getting Started
- `fastapi`, `uvicorn`, basic app layout.
- `@app.get`, `@app.post`, Pydantic models.
- Swagger UI and Redoc generation.

### Pythonic API Design
- Path vs query parameters.
- Status codes, response models, validation.
- Versioning and route structure.

---

## 2. Asynchronous Programming with `asyncio`

### Why Async Matters
- Handling thousands of concurrent requests (non-blocking).
- The FastAPI + `async def` model.

### Core Concepts
- `async def`, `await`, event loop.
- `asyncio.gather`, `asyncio.sleep`, `to_thread`.

### Async in Practice
- Writing async endpoints.
- Calling I/O-heavy services (HTTP calls, DBs).
- Mixing sync and async safely.

---

## 3. Dev Tooling: uv, Linters, Typing

### Project Setup
- Using `uv`, `pyenv`, `venv`, `poetry` or `pdm`.
- Dependency groups for prod/dev/tests.

### Static Analysis
- `mypy`: strict typing, `py.typed`.
- `pylint`, `ruff`, `black`, `isort`: formatting + linting.

### CI Practices
- Running linters and type checks in CI.
- Example: GitHub Actions or GitLab CI config.
- Pre-commit hooks and fast fail.

---

## 4. Testing with `pytest`

### Unit and Integration Testing
- Writing testable FastAPI apps.
- `TestClient`, fixtures, mocking.

### Coverage and Structure
- Directory structure: `tests/`, `conftest.py`.
- `pytest-cov`, marking slow/async tests.

### Testing Practices
- Database test isolation.
- API contract testing and schema validation.

---

## 5. Docker and Deployment

### Dockerizing FastAPI
- `Dockerfile`, multi-stage builds.
- `uvicorn` in production mode.
- `.dockerignore`, `.env`, `volumes`.

### Docker Compose
- API + DB (Postgres, Redis) setup.
- Health checks and startup dependencies.

### CI/CD for Docker Apps
- Building and pushing images.
- Deploy workflows (Heroku, Fly.io, AWS ECS, etc.).

---

## 6. Observability & Monitoring

### Logging Best Practices
- `logging`, `structlog`, log formatters.
- Correlation IDs, request tracing.

### Metrics and Dashboards
- `prometheus_fastapi_instrumentator`.
- Grafana dashboards, custom metrics.

### Log Aggregation
- Elastic Stack (ELK), OpenTelemetry.
- Logtail, Loki, Sentry, BetterStack.

### Health & Error Monitoring
- Liveness/readiness endpoints.
- FastAPI exception handlers + alerts.

---

## 7. Advanced Topics

### Middleware
- Auth, logging, CORS, rate limiting.
- Custom middleware for business logic.

### Dependency Injection
- `Depends`, state injection, lifespan events.

### Background Tasks
- `BackgroundTasks` vs Celery/RQ.
- Use cases: async email, webhook retry.

### Scalability Patterns
- Load balancing with Gunicorn + Uvicorn workers.
- Caching with Redis.
- Async ORMs (Tortoise, Gino) vs sync (SQLAlchemy).

---

## Kickoff Instruction

👉 Begin teaching immediately with **Section 1 (FastAPI Fundamentals)**.

Talk about the **whole section**, following the teaching guidelines.

At the end, ask:

> **“Would you like me to continue to Section 2 (Asynchronous Programming with asyncio)?”**

If the student asks a question mid-topic, finish the answer and offer to resume the next section.