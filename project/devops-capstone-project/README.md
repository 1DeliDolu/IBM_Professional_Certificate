<<<<<<< HEAD

# devops-capstone-project

Customer Accounts RESTful microservice for DevOps Capstone: simple API to manage user accounts, suitable for CI/CD and deployment exercises.

[CI Build](https://github.com/1DeliDolu/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg?branch=main)(https://github.com/1DeliDolu/devops-capstone-project/actions/workflows/ci-build.yaml)

## Status

The project is complete. All CD pipeline changes were applied in `tekton/pipeline.yaml` and deployment manifests are located under `deploy/`.

Report: [Build an Automated CD DevOps Pipeline Using Tekton and OpenShift.pdf](Build%20an%20Automated%20CD%20DevOps%20Pipeline%20Using%20Tekton%20and%20OpenShift.pdf)

If you want any other updates to the README, tell me and I'll apply them.

## Quickstart

Clone the repository:

```
git clone https://github.com/1DeliDolu/devops-capstone-project.git
cd devops-capstone-project
```

Prerequisites:

- Python 3.9+
- pip
- Docker (for building images)
- OpenShift CLI (`oc`) if you plan to run the `deploy` task locally

Run locally (development):

```
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
# Start with gunicorn (bind to 0.0.0.0:8080):
gunicorn "service:app" -b 0.0.0.0:8080
```

Run tests:

```
pip install -r requirements.txt
pytest -q
```

CI / CD notes:

- Tekton pipeline configuration is in `tekton/pipeline.yaml` and uses ClusterTasks `buildah` and `openshift-client` to build and deploy the image.
- Manifests for deployment are under the `deploy/` directory. The pipeline replaces `IMAGE_NAME_HERE` in `deploy/deployment.yaml` with the built image tag.

If you want, I can commit and push these README changes for you.

## Submission Evidence

This repository includes the files and placeholders used for the final submission. Add the required screenshots and output files to the repository (or provide public URLs) and they will be referenced here.

- README (this file): README.md (public URL: https://github.com/1DeliDolu/devops-capstone-project/blob/main/README.md)
- CI workflow output: `ci-workflow-done` (terminal output file)
- CI workflow config: `.github/workflows/ci-build.yaml` or `ci-build.yaml` in repo
- Tekton pipeline config: `tekton/pipeline.yaml`
- Deployment manifests: `deploy/deployment.yaml` and files under `deploy/`
- Dockerfile: `Dockerfile` (root)
- Kubernetes outputs: `kube-app-output`, `kube-images`, `kube-deploy-accounts` (if generated)
- Tekton logs: `pipelinerun.txt` (save pipeline run logs here)

# Account Service — DevOps Capstone

A small RESTful microservice for managing customer accounts, designed for CI/CD and Kubernetes/OpenShift deployment exercises.

## Overview

A Flask-based microservice exposing CRUD endpoints for an `Account` resource, persisting data in PostgreSQL via SQLAlchemy. The repository includes unit tests, linting, a Dockerfile, Kubernetes/OpenShift manifests, and a Tekton pipeline for automated build & deploy.

## Features

- CRUD API for `Account` (create, list, read, update, delete)
- Health check and root metadata endpoints
- SQLAlchemy models with serialize/deserialize and basic validation
- Unit tests using `nose` and `factory-boy`
- Linting/formatting with `flake8`, `pylint`, `black`
- Docker image and Kubernetes/OpenShift manifests
- Tekton pipeline for CI/CD in-cluster

## Tech Stack

- Python 3.9
- Flask, Flask‑SQLAlchemy
- PostgreSQL
- Gunicorn (WSGI)
- honcho (Procfile runner)
- Testing: `nose`, `factory-boy`
- Linting/formatting: `flake8`, `pylint`, `black`
- Container build: Docker / buildah (Tekton)
- CI/CD: Tekton pipeline

## Repository Structure (key files)

- [service/](service) — Flask app, models and routes
  - [service/**init**.py](service/__init__.py)
  - [service/routes.py](service/routes.py)
  - [service/models.py](service/models.py)
  - [service/config.py](service/config.py)
  - [service/common/](service/common)
- [requirements.txt](requirements.txt)
- [Dockerfile](Dockerfile)
- [Procfile](Procfile)
- [Makefile](Makefile)
- [deploy/](deploy) — Kubernetes/OpenShift manifests
  - [deploy/deployment.yaml](deploy/deployment.yaml)
  - [deploy/service.yaml](deploy/service.yaml)
  - [deploy/ingress.yaml](deploy/ingress.yaml)
- [tekton/pipeline.yaml](tekton/pipeline.yaml)
- [k8s/postgresql-ephemeral.yaml](k8s/postgresql-ephemeral.yaml)
- [tests/](tests) — unit tests and factories
- [LICENSE](LICENSE)

Representative tree:

```
service/
	__init__.py
	routes.py
	models.py
	config.py
deploy/
	deployment.yaml
	service.yaml
Dockerfile
Makefile
requirements.txt
tekton/pipeline.yaml
tests/
	test_routes.py
	test_models.py
	factories.py
```

## Prerequisites

- Python 3.9+
- pip
- Docker (optional — build/run images)
- kubectl / oc / k3d (optional — local Kubernetes/OpenShift)
- make (optional — `Makefile` targets)

## Quickstart

Clone and start locally:

```bash
git clone https://github.com/1DeliDolu/devops-capstone-project.git
cd devops-capstone-project
python -m venv .venv
. .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
make run                    # starts app via honcho (reads Procfile)
# or run gunicorn directly:
gunicorn --bind 0.0.0.0:8080 --log-level=info service:app
```

Start a local Postgres for development (optional):

```bash
make db
```

Build Docker image:

```bash
make build
# or
docker build --rm --pull --tag accounts:1.0 .
```

## Local Development

Install

```bash
pip install -r requirements.txt
# or
make install
```

Run

- Development via `honcho` (reads `Procfile`):

```bash
make run
# or
honcho start
```

- Direct WSGI (Gunicorn):

```bash
gunicorn --bind 0.0.0.0:8080 --log-level=info service:app
```

Environment variables / configuration

Configuration is read from environment variables in [service/config.py](service/config.py):

- `DATABASE_URI` — full SQLAlchemy URL (overrides others)
- If `DATABASE_URI` is unset, the app builds a URI using:
  - `DATABASE_USER` (default: `postgres`)
  - `DATABASE_PASSWORD` (default: `postgres`)
  - `DATABASE_NAME` (default: `postgres`)
  - `DATABASE_HOST` (default: `localhost`)
  - default DB port: `5432`
- `SECRET_KEY` — default `s3cr3t-key-shhhh`
- `PORT` — used by `Procfile` / honcho

Notes:

- `Dockerfile` exposes port `8080` and runs `gunicorn` binding to `0.0.0.0:8080`.

## Testing

Run unit tests (repository uses `nose`):

```bash
nosetests -vv --with-spec --spec-color
# or via Makefile:
make tests
```

Tests expect a reachable PostgreSQL instance. Default test DB URI (used if `DATABASE_URI` unset):

`postgresql://postgres:postgres@localhost:5432/postgres`

See [tests/test_routes.py](tests/test_routes.py) and [tests/test_models.py](tests/test_models.py).

## Linting / Formatting

Run linting via Makefile:

```bash
make lint
```

`requirements.txt` includes `flake8`, `pylint`, and `black`.

## Docker

- `Dockerfile` uses `python:3.9-slim`, installs dependencies from [requirements.txt](requirements.txt), copies `service/`, and runs `gunicorn service:app`.
- Container exposes port `8080`.

Run locally:

```bash
docker build -t accounts:1.0 .
docker run -p 8080:8080 accounts:1.0
```

## Kubernetes / OpenShift

Manifests are in [deploy/](deploy):

- [deploy/deployment.yaml](deploy/deployment.yaml) — template with placeholder `IMAGE_NAME_HERE`
- [deploy/service.yaml](deploy/service.yaml)
- [deploy/ingress.yaml](deploy/ingress.yaml)

Local ephemeral Postgres manifest: [k8s/postgresql-ephemeral.yaml](k8s/postgresql-ephemeral.yaml) (contains a `Secret` with demo credentials for local testing only).

Makefile helpers:

- `make cluster` — create a k3d cluster (requires k3d)
- `make tekton` — install Tekton into cluster
- `make clustertasks` — create Tekton ClusterTasks

## CI/CD

Tekton pipeline: [tekton/pipeline.yaml](tekton/pipeline.yaml). Pipeline steps:

- clone repo (`git-clone`)
- lint (`flake8`)
- run tests (`nose`)
- build image (`buildah` ClusterTask)
- deploy (`openshift-client` ClusterTask) — pipeline replaces `IMAGE_NAME_HERE` in `deploy/deployment.yaml` with the built image

The pipeline requires ClusterTasks such as `git-clone`, `flake8`, `nose`, `buildah`, and `openshift-client` to be available in the cluster.

## API Documentation

Endpoints implemented in [service/routes.py](service/routes.py):

- `GET /` — service metadata
- `GET /health` — health check
- `POST /accounts` — create account
- `GET /accounts` — list accounts
- `GET /accounts/<id>` — retrieve account
- `PUT /accounts/<id>` — update account
- `DELETE /accounts/<id>` — delete account

Example `curl` calls:

Create an account:

```bash
curl -sS -X POST http://localhost:8080/accounts \
	-H "Content-Type: application/json" \
	-d '{"name":"Alice","email":"alice@example.com","address":"123 Main St","phone_number":"555-0100","date_joined":"2020-01-01"}'
```

List accounts:

```bash
curl -sS http://localhost:8080/accounts
```

Get account:

```bash
curl -sS http://localhost:8080/accounts/1
```

Update account:

```bash
curl -sS -X PUT http://localhost:8080/accounts/1 \
	-H "Content-Type: application/json" \
	-d '{"name":"Alice Updated","email":"alice@new.example","address":"123 Main St"}'
```

Delete account:

```bash
curl -sS -X DELETE http://localhost:8080/accounts/1
```

## Troubleshooting

- DB connection errors:
  - Verify `DATABASE_URI` or `DATABASE_HOST` / `DATABASE_USER` / `DATABASE_PASSWORD` are correct.
  - For local testing, start a PostgreSQL container via `make db`.
- Port conflicts:
  - App defaults to bind on port `8080` (containerized) or `PORT` env var when using `honcho`/Procfile.
- Tests failing due to DB:
  - Confirm test DB is reachable at `postgresql://postgres:postgres@localhost:5432/postgres` or set `DATABASE_URI` for test runs.
- Secrets in manifests:
  - Do not use demo secrets from [k8s/postgresql-ephemeral.yaml](k8s/postgresql-ephemeral.yaml) in production.

## Contributing

- No `CONTRIBUTING.md` present. Suggested workflow:
  - Fork → feature branch → PR.
  - Run `make lint` and `make tests` locally before submitting a PR.
  - Validate pipeline/manifest changes in a safe test cluster.

## Security

- The repo contains demo default credentials and a local `Secret` manifest for convenience. Do not use these values in production.
- Use secure secret management for DB credentials in production; [deploy/deployment.yaml](deploy/deployment.yaml) expects secrets.

## License

See [LICENSE](LICENSE).

## Assumptions / TODO

- No GitHub Actions workflows found under `.github/workflows/` in this repository; README does not include CI badges. (Checked repository root and `tekton/`.)
- `deploy/deployment.yaml` contains placeholder `IMAGE_NAME_HERE`; image registry and tagging strategy are not defined. Tekton pipeline replaces this with the provided `build-image` parameter. (Checked [deploy/deployment.yaml](deploy/deployment.yaml) and [tekton/pipeline.yaml](tekton/pipeline.yaml).)
- No `CONTRIBUTING.md` or `CODEOWNERS` — maintainers and PR process are unspecified. (Checked repository root.)
- Ingress host/TLS is not configured in [deploy/ingress.yaml](deploy/ingress.yaml). (Checked file.)
- No `docker-compose.yml` present. (Checked repository root.)
- Tests require a running Postgres instance; only local helpers are `make db` and [k8s/postgresql-ephemeral.yaml](k8s/postgresql-ephemeral.yaml). (Checked [Makefile](Makefile), [k8s/postgresql-ephemeral.yaml](k8s/postgresql-ephemeral.yaml), and tests.)
- If you want, I can:
  - Add a `CONTRIBUTING.md`.
  - Provide example image tag substitutions in `deploy/deployment.yaml` and commit them.
  - Add a GitHub Actions workflow for quick CI (requires confirmation).

>>>>>>> 0ae7321 (Update README.md)
>>>>>>>
>>>>>>
>>>>>
>>>>
>>>
>>
