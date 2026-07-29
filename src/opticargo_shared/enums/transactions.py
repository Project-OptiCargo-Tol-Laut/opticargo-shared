from enum import StrEnum


class BookingStatus(StrEnum):
    pending = "pending"
    confirmed = "confirmed"
    paid = "paid"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"
    disputed = "disputed"


class PaymentStatus(StrEnum):
    pending = "pending"
    paid = "paid"
    failed = "failed"
    refunded = "refunded"


class PaymentMethod(StrEnum):
    bank_transfer = "bank_transfer"
    virtual_account = "virtual_account"
    e_wallet = "e_wallet"


class RecommendationStatus(StrEnum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
