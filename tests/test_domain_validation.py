from datetime import UTC, date, datetime, timedelta
from decimal import Decimal
from uuid import uuid4

import pytest
from pydantic import ValidationError

from opticargo_shared.agent_state import ScoreBreakdown
from opticargo_shared.enums import (
    BookingStatus,
    CargoListingStatus,
    DocumentIngestionStatus,
    DocumentType,
    ModelMode,
    NotificationChannel,
    NotificationStatus,
    PaymentMethod,
    PaymentStatus,
    RecommendationStatus,
    RouteType,
    VoyageStatus,
)
from opticargo_shared.models import (
    BookingCreate,
    CargoCapacityCreate,
    CargoListingCreate,
    DocumentCreate,
    NotificationCreate,
    PaymentCreate,
    RecommendationContent,
    RecommendationCreate,
    RouteCreate,
    TemperatureRange,
    VoyageCreate,
)

NOW = datetime.now(UTC)


def test_route_listing_and_temperature_cross_field_validation() -> None:
    port_id = uuid4()
    with pytest.raises(ValidationError, match="must differ"):
        RouteCreate(
            origin_port_id=port_id,
            destination_port_id=port_id,
            distance_nm="10",
            estimated_days=1,
            route_type=RouteType.toll_sea,
        )
    with pytest.raises(ValidationError, match="available_until"):
        CargoListingCreate(
            supplier_id=uuid4(),
            commodity_id=uuid4(),
            volume_ton="1",
            available_from=date(2026, 8, 2),
            available_until=date(2026, 8, 1),
            origin_port_id=uuid4(),
            destination_port_id=uuid4(),
            asking_price_per_ton="0",
            status=CargoListingStatus.open,
        )
    with pytest.raises(ValidationError, match="min_celsius"):
        TemperatureRange(min_celsius=5, max_celsius=1)
    with pytest.raises(ValidationError, match="duplicates"):
        CargoCapacityCreate(
            voyage_id=uuid4(),
            available_weight_ton="1",
            available_volume_m3="1",
            cargo_type_allowed=["Dry", " dry "],
        )


def test_voyage_and_booking_capacity_time_validation() -> None:
    with pytest.raises(ValidationError, match="remaining_capacity"):
        VoyageCreate(
            ship_id=uuid4(),
            route_id=uuid4(),
            departure_date=NOW,
            arrival_date=NOW + timedelta(days=1),
            total_capacity_ton="10",
            used_capacity_ton="4",
            remaining_capacity_ton="5",
            status=VoyageStatus.scheduled,
        )
    with pytest.raises(ValidationError, match="confirmation_date"):
        BookingCreate(
            voyage_id=uuid4(),
            cargo_listing_id=uuid4(),
            booked_volume_ton="1",
            agreed_price_per_ton="10",
            status=BookingStatus.confirmed,
            booking_date=NOW,
            confirmation_date=NOW - timedelta(seconds=1),
            booking_ref="BOOK-1",
        )


def test_payment_document_and_notification_lifecycle_validation() -> None:
    with pytest.raises(ValidationError, match="paid_at"):
        PaymentCreate(
            booking_id=uuid4(),
            amount="100",
            method=PaymentMethod.bank_transfer,
            status=PaymentStatus.paid,
        )
    with pytest.raises(ValidationError, match="ingestion_error"):
        DocumentCreate(
            doc_type=DocumentType.regulation,
            title="Regulation",
            object_key="private/regulation.pdf",
            file_size=10,
            mime_type="application/pdf",
            uploaded_by=uuid4(),
            ingestion_status=DocumentIngestionStatus.failed,
        )
    with pytest.raises(ValidationError, match="sent_at"):
        NotificationCreate(
            user_id=uuid4(),
            channel=NotificationChannel.in_app,
            title="Ready",
            body="Report ready",
            status=NotificationStatus.sent,
        )


def test_persisted_recommendation_response_rules() -> None:
    breakdown = ScoreBreakdown(
        total_score="0.8",
        economic_value="0.8",
        schedule_fit="0.8",
        capacity_fit="0.8",
        distance_fit="0.8",
        risk_score="0.2",
        model_mode=ModelMode.heuristic,
    )
    content = RecommendationContent(
        summary="Recommended cargo",
        score_breakdown=breakdown,
        confidence="0.8",
        recommended_human_action="Review and confirm booking",
    )
    recommendation = RecommendationCreate(
        voyage_id=uuid4(),
        recommendation_type="backhaul",
        content=content,
        score=Decimal("0.8"),
        status=RecommendationStatus.pending,
        generated_at=NOW,
        trace_id=uuid4(),
    )
    assert recommendation.responded_at is None
    with pytest.raises(ValidationError, match="responded_at"):
        RecommendationCreate(
            **{
                **recommendation.model_dump(),
                "status": RecommendationStatus.accepted,
            }
        )
