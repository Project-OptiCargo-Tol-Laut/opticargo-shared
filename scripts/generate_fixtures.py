"""Generate deterministic, non-sensitive canonical serialization fixtures."""

from __future__ import annotations

import json
from datetime import UTC, date, datetime, timedelta
from pathlib import Path
from typing import Any
from uuid import UUID

from opticargo_shared.agent_state import RecommendationOutput
from opticargo_shared.api import ErrorResponse
from opticargo_shared.enums import (
    AccountStatus,
    BookingStatus,
    ConfidenceLevel,
    DocumentIngestionStatus,
    DocumentType,
    ModelMode,
    PaymentMethod,
    PaymentStatus,
    QueryIntent,
    RecommendationStatus,
    ReportStatus,
    UserRole,
    VoyageStatus,
)
from opticargo_shared.events import DomainEvent, EventType
from opticargo_shared.events.payloads import (
    BookingCreatedPayload,
    BookingStatusChangedPayload,
    DocumentIngestionResultPayload,
    DocumentUploadedPayload,
    EntityChangedPayload,
    EntityChangeType,
    ModelStatusPayload,
    PaymentCreatedPayload,
    PaymentStatusChangedPayload,
    RecommendationCreatedPayload,
    ReportPayload,
    ReviewCreatedPayload,
)
from opticargo_shared.ml import ModelStatus
from opticargo_shared.models import (
    BookingRead,
    DocumentRead,
    PaymentRead,
    UserRead,
    VoyageRead,
)

FIXTURE_TIME = datetime(2026, 7, 29, 10, 0, tzinfo=UTC)
IDS = [UUID(int=index) for index in range(1, 40)]


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if hasattr(value, "model_dump"):
        value = value.model_dump(mode="json")
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def event(event_type: EventType, entity_id: UUID, payload: Any) -> DomainEvent:
    return DomainEvent(
        event_id=IDS[0],
        event_type=event_type,
        occurred_at=FIXTURE_TIME,
        producer="opticargo-fixture-generator",
        entity_type=event_type.value.split(".", 1)[0],
        entity_id=entity_id,
        correlation_id=IDS[1],
        idempotency_key=f"fixture:{event_type.value}",
        payload=payload.model_dump(mode="json"),
    )


def event_fixtures() -> dict[EventType, DomainEvent]:
    booking_created = BookingCreatedPayload(
        booking_id=IDS[2],
        voyage_id=IDS[3],
        cargo_listing_id=IDS[4],
        booked_volume_ton="5",
        status=BookingStatus.pending,
    )
    booking_changed = BookingStatusChangedPayload(
        booking_id=IDS[2],
        previous_status=BookingStatus.pending,
        new_status=BookingStatus.confirmed,
        voyage_id=IDS[3],
        cargo_listing_id=IDS[4],
        actor_id=IDS[5],
    )
    payment_created = PaymentCreatedPayload(
        payment_id=IDS[6],
        booking_id=IDS[2],
        amount="1000",
        status=PaymentStatus.pending,
    )
    payment_changed = PaymentStatusChangedPayload(
        payment_id=IDS[6],
        booking_id=IDS[2],
        previous_status=PaymentStatus.pending,
        new_status=PaymentStatus.paid,
        provider_event_id="provider-event-example",
        amount="1000",
    )
    document_uploaded = DocumentUploadedPayload(
        document_id=IDS[7],
        object_key="documents/example.pdf",
        mime_type="application/pdf",
        checksum="sha256:example",
        document_version="1",
    )
    ingestion_completed = DocumentIngestionResultPayload(
        document_id=IDS[7],
        status=DocumentIngestionStatus.indexed,
        chunk_count=3,
        indexed_at=FIXTURE_TIME,
    )
    ingestion_failed = DocumentIngestionResultPayload(
        document_id=IDS[7],
        status=DocumentIngestionStatus.failed,
        chunk_count=0,
        error_code="PARSER_ERROR",
        error_message="Document structure is unsupported",
    )
    recommendation = RecommendationCreatedPayload(
        recommendation_id=IDS[8],
        voyage_id=IDS[3],
        score="0.8",
        status=RecommendationStatus.pending,
        recipient_user_ids=[IDS[5]],
        threshold_triggered=True,
    )
    review = ReviewCreatedPayload(
        review_id=IDS[9],
        booking_id=IDS[2],
        reviewer_id=IDS[5],
        reviewee_id=IDS[10],
        rating=5,
    )
    entity_changed = EntityChangedPayload(
        entity_type="booking",
        entity_id=IDS[2],
        change_type=EntityChangeType.updated,
        changed_fields=["status"],
        entity_version="1",
        lookup_hint={"booking_id": str(IDS[2])},
    )
    report_requested = ReportPayload(
        report_id=IDS[11],
        report_type="voyage_utilization",
        format="xlsx",
        status=ReportStatus.queued,
        requested_by=IDS[5],
    )
    report_completed = report_requested.model_copy(
        update={"status": ReportStatus.completed, "completed_at": FIXTURE_TIME}
    )
    report_failed = report_requested.model_copy(
        update={"status": ReportStatus.failed, "error": "Generation failed"}
    )
    model_promoted = ModelStatusPayload(
        model_name="cargo-match",
        model_version="1.0",
        model_mode=ModelMode.trained,
        dataset_version="2026.07",
        promoted_at=FIXTURE_TIME,
    )
    model_drift = model_promoted.model_copy(
        update={"promoted_at": None, "drift_detected_at": FIXTURE_TIME}
    )
    payloads = {
        EventType.entity_changed: (IDS[2], entity_changed),
        EventType.booking_created: (IDS[2], booking_created),
        EventType.booking_status_changed: (IDS[2], booking_changed),
        EventType.payment_created: (IDS[6], payment_created),
        EventType.payment_status_changed: (IDS[6], payment_changed),
        EventType.document_uploaded: (IDS[7], document_uploaded),
        EventType.document_ingestion_completed: (IDS[7], ingestion_completed),
        EventType.document_ingestion_failed: (IDS[7], ingestion_failed),
        EventType.recommendation_created: (IDS[8], recommendation),
        EventType.review_created: (IDS[9], review),
        EventType.report_requested: (IDS[11], report_requested),
        EventType.report_completed: (IDS[11], report_completed),
        EventType.report_failed: (IDS[11], report_failed),
        EventType.model_promoted: (IDS[12], model_promoted),
        EventType.model_drift_detected: (IDS[12], model_drift),
    }
    return {
        event_type: event(event_type, entity_id, payload)
        for event_type, (entity_id, payload) in payloads.items()
    }


def critical_fixtures() -> dict[str, Any]:
    user = UserRead(
        id=IDS[5],
        username="fixture_operator",
        email="fixture@example.com",
        role=UserRole.operator_kapal,
        account_status=AccountStatus.active,
        created_at=FIXTURE_TIME,
        updated_at=FIXTURE_TIME,
    )
    voyage = VoyageRead(
        id=IDS[3],
        ship_id=IDS[13],
        route_id=IDS[14],
        departure_date=FIXTURE_TIME,
        arrival_date=FIXTURE_TIME + timedelta(days=2),
        total_capacity_ton="100",
        used_capacity_ton="25",
        remaining_capacity_ton="75",
        status=VoyageStatus.scheduled,
        created_at=FIXTURE_TIME,
        updated_at=FIXTURE_TIME,
    )
    booking = BookingRead(
        id=IDS[2],
        voyage_id=IDS[3],
        cargo_listing_id=IDS[4],
        booked_volume_ton="5",
        agreed_price_per_ton="200",
        status=BookingStatus.pending,
        booking_date=FIXTURE_TIME,
        booking_ref="FIXTURE-BOOKING-1",
        created_by=IDS[5],
        created_at=FIXTURE_TIME,
        updated_at=FIXTURE_TIME,
    )
    payment = PaymentRead(
        id=IDS[6],
        booking_id=IDS[2],
        amount="1000",
        method=PaymentMethod.bank_transfer,
        status=PaymentStatus.pending,
        created_at=FIXTURE_TIME,
        updated_at=FIXTURE_TIME,
    )
    document = DocumentRead(
        id=IDS[7],
        doc_type=DocumentType.regulation,
        title="Fixture regulation",
        object_key="documents/example.pdf",
        file_size=1024,
        mime_type="application/pdf",
        uploaded_by=IDS[5],
        issuer="Fixture Authority",
        document_version="1",
        effective_date=date(2026, 7, 29),
        ingestion_status=DocumentIngestionStatus.queued,
        created_at=FIXTURE_TIME,
        updated_at=FIXTURE_TIME,
    )
    recommendation = RecommendationOutput(
        correlation_id=IDS[1],
        voyage_id=IDS[3],
        intent=QueryIntent.unknown,
        summary="Insufficient evidence",
        confidence="0.1",
        confidence_level=ConfidenceLevel.low,
        abstained=True,
        abstention_reason="No authoritative source retrieved",
    )
    error = ErrorResponse(
        code="VALIDATION_ERROR",
        message="Invalid input",
        details={"field": "booking_ref"},
        trace_id=IDS[1],
    )
    model_status = ModelStatus(
        model_name="cargo-match",
        model_mode=ModelMode.heuristic,
        metrics={},
        fallback_available=True,
        healthy=True,
    )
    return {
        "UserRead": user,
        "VoyageRead": voyage,
        "BookingRead": booking,
        "PaymentRead": payment,
        "DocumentRead": document,
        "RecommendationOutput": recommendation,
        "ErrorResponse": error,
        "ModelStatus": model_status,
    }


def main() -> None:
    root = Path("tests/fixtures")
    for event_type, fixture in event_fixtures().items():
        write_json(root / "events" / f"{event_type.value.replace('.', '_')}.json", fixture)
    for name, fixture in critical_fixtures().items():
        write_json(root / "contracts" / f"{name}.json", fixture)
    print("Generated canonical contract and event fixtures")


if __name__ == "__main__":
    main()
