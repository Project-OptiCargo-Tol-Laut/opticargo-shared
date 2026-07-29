from enum import StrEnum


class DocumentType(StrEnum):
    manifest = "manifest"
    bill_of_lading = "bill_of_lading"
    regulation = "regulation"
    certificate = "certificate"
    invoice = "invoice"


class DocumentIngestionStatus(StrEnum):
    queued = "queued"
    processing = "processing"
    indexed = "indexed"
    failed = "failed"


class NotificationChannel(StrEnum):
    email = "email"
    whatsapp = "whatsapp"
    in_app = "in_app"


class NotificationStatus(StrEnum):
    queued = "queued"
    sent = "sent"
    failed = "failed"


class ReportStatus(StrEnum):
    queued = "queued"
    processing = "processing"
    completed = "completed"
    failed = "failed"


class ExportFormat(StrEnum):
    pdf = "pdf"
    xlsx = "xlsx"
