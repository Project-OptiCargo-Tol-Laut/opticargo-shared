from datetime import UTC, datetime
from decimal import Decimal
from pathlib import Path
from uuid import uuid4

import pytest
from pydantic import ValidationError

from opticargo_shared.dataset import DatasetManifest, RecordProvenance, ValidationStatus
from opticargo_shared.enums import DocumentIngestionStatus, ModelMode
from opticargo_shared.events import DomainEvent, EventType
from opticargo_shared.events.payloads import (
    DocumentIngestionResultPayload,
    EntityChangedPayload,
    EntityChangeType,
)
from opticargo_shared.ml import (
    CargoCandidateFeatures,
    CargoScoringRequest,
    CargoScoringResponse,
    ModelStatus,
    RouteScheduleFeatures,
    SupplierRiskFeatures,
    VoyageCapacitySummary,
)
from opticargo_shared.schema import generate_json_schemas, public_contract_models

NOW = datetime.now(UTC)


def test_domain_event_and_typed_payload_serialization() -> None:
    entity_id = uuid4()
    payload = EntityChangedPayload(
        entity_type="booking",
        entity_id=entity_id,
        change_type=EntityChangeType.updated,
        changed_fields=["status"],
        entity_version="1",
        lookup_hint={"booking_id": str(entity_id)},
    )
    event = DomainEvent(
        event_id=uuid4(),
        event_type=EventType.entity_changed,
        occurred_at=NOW,
        producer="opticargo-gateway-api",
        entity_type="booking",
        entity_id=entity_id,
        correlation_id=uuid4(),
        idempotency_key="event-1",
        payload=payload.model_dump(mode="json"),
    )
    assert event.model_dump(mode="json")["event_version"] == "1.0"
    with pytest.raises(ValidationError):
        DomainEvent.model_validate({**event.model_dump(), "secret": "forbidden"})


def test_document_ingestion_event_result_rules() -> None:
    indexed = DocumentIngestionResultPayload(
        document_id=uuid4(),
        status=DocumentIngestionStatus.indexed,
        chunk_count=2,
        indexed_at=NOW,
    )
    assert indexed.chunk_count == 2
    with pytest.raises(ValidationError, match="error_code"):
        DocumentIngestionResultPayload(
            document_id=uuid4(),
            status=DocumentIngestionStatus.failed,
            chunk_count=0,
        )


def test_ml_scoring_and_model_status_contracts() -> None:
    correlation_id = uuid4()
    request = CargoScoringRequest(
        correlation_id=correlation_id,
        voyage=VoyageCapacitySummary(
            voyage_id=uuid4(), remaining_weight_ton="10", remaining_volume_m3="20"
        ),
        candidate=CargoCandidateFeatures(cargo_listing_id=uuid4(), cargo_weight_ton="5"),
        route_schedule=RouteScheduleFeatures(distance_nm="100", schedule_compatible=True),
        supplier_risk=SupplierRiskFeatures(supplier_id=uuid4(), supplier_rating="4.5"),
    )
    response = CargoScoringResponse(
        correlation_id=correlation_id,
        score="0.9",
        model_mode=ModelMode.heuristic,
        fallback_used=True,
        inference_timestamp=NOW,
    )
    status = ModelStatus(
        model_name="cargo-match",
        model_mode=ModelMode.heuristic,
        metrics={},
        fallback_available=True,
        healthy=True,
    )
    assert request.candidate.cargo_weight_ton == 5
    assert response.score == Decimal("0.9")
    assert status.healthy is True


def test_dataset_provenance_and_all_public_schemas_generate() -> None:
    manifest = DatasetManifest(
        dataset_name="seed",
        dataset_version="1",
        created_at=NOW,
        source_type="synthetic",
        is_synthetic=True,
        record_count=1,
        schema_package_version="1.0.0",
        checksum="sha256:test",
    )
    provenance = RecordProvenance(
        source="generator",
        collected_or_generated_at=NOW,
        transformation_version="1",
        is_synthetic=True,
        generator_seed=42,
        validation_status=ValidationStatus.valid,
    )
    schemas = generate_json_schemas()
    assert manifest.is_synthetic and provenance.generator_seed == 42
    assert len(schemas) == len(public_contract_models())
    assert all("$defs" in schema or "properties" in schema for schema in schemas.values())
    assert Path("schemas/snapshots/v1.0.0").is_dir()
