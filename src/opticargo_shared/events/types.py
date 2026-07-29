from enum import StrEnum


class EventType(StrEnum):
    entity_changed = "entity.changed"
    booking_created = "booking.created"
    booking_status_changed = "booking.status_changed"
    payment_created = "payment.created"
    payment_status_changed = "payment.status_changed"
    document_uploaded = "document.uploaded"
    document_ingestion_completed = "document.ingestion_completed"
    document_ingestion_failed = "document.ingestion_failed"
    recommendation_created = "recommendation.created"
    review_created = "review.created"
    report_requested = "report.requested"
    report_completed = "report.completed"
    report_failed = "report.failed"
    model_promoted = "model.promoted"
    model_drift_detected = "model.drift_detected"


EVENT_VERSION = "1.0"
