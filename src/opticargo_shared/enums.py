from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    operator = "operator"
    supplier = "supplier"
    distributor = "distributor"

class ShipStatus(str, Enum):
    active = "active"
    maintenance = "maintenance"
    inactive = "inactive"

class RouteType(str, Enum):
    toll_sea = "toll_sea"
    commercial = "commercial"
    private = "private"

class VoyageStatus(str, Enum):
    scheduled = "scheduled"
    in_transit = "in_transit"
    completed = "completed"
    cancelled = "cancelled"

class CargoListingStatus(str, Enum):
    open = "open"
    matched = "matched"
    closed = "closed"
    expired = "expired"

class BookingStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"
    completed = "completed"

class DocumentType(str, Enum):
    manifest = "manifest"
    bill_of_lading = "bill_of_lading"
    regulation = "regulation"
    certificate = "certificate"

class RecommendationStatus(str, Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"