from typing import Annotated, Self
from uuid import UUID

from pydantic import AwareDatetime, Field, model_validator

from opticargo_shared.base import ContractModel
from opticargo_shared.enums import NotificationChannel, NotificationStatus


class NotificationBase(ContractModel):
    user_id: UUID
    channel: NotificationChannel
    title: Annotated[str, Field(min_length=1)]
    body: Annotated[str, Field(min_length=1)]
    status: NotificationStatus = NotificationStatus.queued
    related_entity_type: str | None = None
    related_entity_id: UUID | None = None
    is_read: bool = False
    read_at: AwareDatetime | None = None
    template_version: str | None = None
    last_error: str | None = None
    sent_at: AwareDatetime | None = None

    @model_validator(mode="after")
    def validate_delivery_and_read_state(self) -> Self:
        if self.is_read != (self.read_at is not None):
            raise ValueError("is_read must be consistent with read_at")
        if self.status == NotificationStatus.sent and self.sent_at is None:
            raise ValueError("sent_at is required when notification is sent")
        if self.status != NotificationStatus.sent and self.sent_at is not None:
            raise ValueError("sent_at is only allowed when notification is sent")
        if self.status == NotificationStatus.failed and not self.last_error:
            raise ValueError("last_error is required when notification failed")
        return self


class NotificationCreate(NotificationBase):
    pass


class NotificationUpdate(ContractModel):
    status: NotificationStatus | None = None
    is_read: bool | None = None
    read_at: AwareDatetime | None = None
    last_error: str | None = None
    sent_at: AwareDatetime | None = None


class NotificationRead(NotificationBase):
    id: UUID
    created_at: AwareDatetime


Notification = NotificationRead
