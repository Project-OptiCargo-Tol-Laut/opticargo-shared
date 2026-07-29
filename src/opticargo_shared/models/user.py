from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, EmailStr, Field

from opticargo_shared.base import ContractModel
from opticargo_shared.enums import AccountStatus, UserRole


class UserBase(ContractModel):
    username: Annotated[str, Field(min_length=3, max_length=64)]
    email: EmailStr
    role: UserRole
    company_name: Annotated[str, Field(min_length=1, max_length=200)] | None = None
    phone: Annotated[str, Field(min_length=3, max_length=32)] | None = None
    account_status: AccountStatus = AccountStatus.pending


class UserCreate(UserBase):
    """Public create contract; password handling remains gateway-owned."""


class UserUpdate(ContractModel):
    username: Annotated[str, Field(min_length=3, max_length=64)] | None = None
    email: EmailStr | None = None
    role: UserRole | None = None
    company_name: Annotated[str, Field(min_length=1, max_length=200)] | None = None
    phone: Annotated[str, Field(min_length=3, max_length=32)] | None = None
    account_status: AccountStatus | None = None


class UserRead(UserBase):
    id: UUID
    created_at: AwareDatetime
    updated_at: AwareDatetime


class UserInternal(UserRead):
    """Gateway-only extension; intentionally not exported from package top-level."""

    password_hash: Annotated[str, Field(min_length=1, repr=False)]


User = UserRead
