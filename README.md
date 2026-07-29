# opticargo-shared

`opticargo-shared` v1.0.0 is the framework-independent contract package for
OptiCargo AI. It contains Pydantic v2 models, canonical enums, domain event
payloads, agent/ML state, API envelopes, dataset provenance, and versioned JSON
Schema snapshots. It performs no I/O on import and contains no ORM or service
dependencies.

## Requirements and installation

- Python 3.11+
- `pydantic>=2,<3`

```bash
python -m pip install -e ".[dev]"
```

Consumers must pin an immutable release, for example:

```text
opticargo-shared==1.0.0
```

## Quick start

```python
from opticargo_shared.events import DomainEvent
from opticargo_shared.models import BookingRead
from opticargo_shared.agent_state import RecommendationOutput

booking = BookingRead.model_validate(booking_payload)
event = DomainEvent.model_validate(event_payload)
recommendation = RecommendationOutput.model_validate(ai_payload)
```

All critical contracts reject unknown fields. Timestamps are timezone-aware,
IDs are UUIDs, precise business numbers use `Decimal`, and wire field names use
`snake_case`.

## Public contract areas

- `opticargo_shared.models`: 17 entity families, including `CargoCapacity`
- `opticargo_shared.enums`: identity, operations, transaction, knowledge, AI/ML
- `opticargo_shared.events`: versioned envelope and typed event payloads
- `opticargo_shared.agent_state`: citations, candidates, scoring, optimization,
  recommendation output, and orchestrator state
- `opticargo_shared.ml`: scoring, forecast, anomaly, and model status contracts
- `opticargo_shared.api`: error, page/cursor pagination, export, idempotency
- `opticargo_shared.dataset`: dataset manifest and record provenance

Legacy entity names such as `Booking` remain aliases of their `*Read` contract.
New integrations should use explicit `*Create`, `*Update`, and `*Read` names.
`UserInternal` is deliberately not exported from the package model namespace.

## Quality and compatibility

```bash
ruff check .
ruff format --check .
mypy src/opticargo_shared
pytest --cov=opticargo_shared --cov-fail-under=90
python scripts/generate_schemas.py schemas/current
python scripts/check_compatibility.py schemas/snapshots/v1.0.0 schemas/current
python -m build
```

Examples are available in [`examples/`](examples/). Current schemas live in
[`schemas/current/`](schemas/current/) and the immutable v1 baseline in
[`schemas/snapshots/v1.0.0/`](schemas/snapshots/v1.0.0/).

## Versioning policy

- MAJOR: remove/rename fields, incompatible type or requiredness changes, enum
  removal/change, event semantic change.
- MINOR: additive optional fields, new models/helpers/event types.
- PATCH: validator, documentation, or typing fixes that preserve the wire
  contract.

Every contract change requires tests, regenerated current schemas, a compatibility
check, and a CHANGELOG entry. See [`CONTRIBUTING.md`](CONTRIBUTING.md).
