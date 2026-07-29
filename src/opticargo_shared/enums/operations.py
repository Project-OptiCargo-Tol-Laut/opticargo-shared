from enum import StrEnum


class ShipStatus(StrEnum):
    active = "active"
    maintenance = "maintenance"
    inactive = "inactive"
    decommissioned = "decommissioned"


class VoyageStatus(StrEnum):
    scheduled = "scheduled"
    in_transit = "in_transit"
    completed = "completed"
    cancelled = "cancelled"
    delayed = "delayed"


class RouteType(StrEnum):
    toll_sea = "toll_sea"
    commercial = "commercial"
    private = "private"


class CargoListingStatus(StrEnum):
    open = "open"
    matched = "matched"
    closed = "closed"
    expired = "expired"
