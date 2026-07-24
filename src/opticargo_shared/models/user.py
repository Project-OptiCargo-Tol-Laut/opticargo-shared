from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr
from opticargo_shared.enums import UserRole

class User(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    role: UserRole
    company_name: str | None = None
    phone: str | None = None
    created_at: datetime
    is_active: bool = True

class UserCreate(BaseModel):
    """Payload untuk pembuatan user baru — tanpa id/created_at, dengan password plain (di-hash di BE)."""
    username: str
    email: EmailStr
    password: str
    role: UserRole
    company_name: str | None = None
    phone: str | None = None