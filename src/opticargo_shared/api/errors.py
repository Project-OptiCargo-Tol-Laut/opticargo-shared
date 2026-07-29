from enum import StrEnum
from typing import Any
from uuid import UUID

from pydantic import AliasChoices, Field

from opticargo_shared.base import ContractModel


class ErrorCode(StrEnum):
    validation_error = "VALIDATION_ERROR"
    authentication_required = "AUTHENTICATION_REQUIRED"
    forbidden = "FORBIDDEN"
    object_access_denied = "OBJECT_ACCESS_DENIED"
    resource_not_found = "RESOURCE_NOT_FOUND"
    conflict = "CONFLICT"
    booking_invalid_transition = "BOOKING_INVALID_TRANSITION"
    capacity_exceeded = "CAPACITY_EXCEEDED"
    payment_invalid_signature = "PAYMENT_INVALID_SIGNATURE"
    payment_duplicate_event = "PAYMENT_DUPLICATE_EVENT"
    document_ingestion_failed = "DOCUMENT_INGESTION_FAILED"
    ai_insufficient_evidence = "AI_INSUFFICIENT_EVIDENCE"
    dependency_unavailable = "DEPENDENCY_UNAVAILABLE"
    internal_error = "INTERNAL_ERROR"


class ErrorDetail(ContractModel):
    field: str | None = None
    message: str


class ErrorResponse(ContractModel):
    code: str = Field(validation_alias=AliasChoices("code", "error_code"))
    message: str
    details: dict[str, Any] = Field(default_factory=dict)
    trace_id: UUID

    @property
    def error_code(self) -> str:
        """Deprecated source compatibility alias; serialized field is ``code``."""

        return self.code
