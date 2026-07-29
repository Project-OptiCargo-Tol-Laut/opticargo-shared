from datetime import UTC, datetime
from uuid import uuid4

from opticargo_shared.enums import BookingStatus
from opticargo_shared.events import DomainEvent, EventType
from opticargo_shared.events.payloads import BookingCreatedPayload

payload = BookingCreatedPayload(
    booking_id=uuid4(),
    voyage_id=uuid4(),
    cargo_listing_id=uuid4(),
    booked_volume_ton="12.5",
    status=BookingStatus.pending,
)
event = DomainEvent(
    event_id=uuid4(),
    event_type=EventType.booking_created,
    occurred_at=datetime.now(UTC),
    producer="opticargo-gateway-api",
    entity_type="booking",
    entity_id=payload.booking_id,
    correlation_id=uuid4(),
    idempotency_key="booking:create:example",
    payload=payload.model_dump(mode="json"),
)
print(event.model_dump_json(indent=2))
