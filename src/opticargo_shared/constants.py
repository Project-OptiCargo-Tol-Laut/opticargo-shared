"""Stable values and pure transition helpers shared by consumers."""

from opticargo_shared.enums import BookingStatus

# API Pagination Defaults (Selaras dengan PageParams di api/pagination.py)
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# Graph Analysis Defaults (Selaras dengan GraphAnalysisInput)
DEFAULT_SEARCH_RADIUS_DAYS = 7

BOOKING_STATUS_TRANSITIONS: dict[BookingStatus, frozenset[BookingStatus]] = {
    BookingStatus.pending: frozenset({BookingStatus.confirmed, BookingStatus.cancelled}),
    BookingStatus.confirmed: frozenset({BookingStatus.paid, BookingStatus.cancelled}),
    BookingStatus.paid: frozenset({BookingStatus.in_progress, BookingStatus.disputed}),
    BookingStatus.in_progress: frozenset({BookingStatus.completed, BookingStatus.disputed}),
    BookingStatus.completed: frozenset(),
    BookingStatus.cancelled: frozenset(),
    BookingStatus.disputed: frozenset({BookingStatus.completed, BookingStatus.cancelled}),
}


def is_booking_transition_allowed(previous: BookingStatus, new: BookingStatus) -> bool:
    """Return whether the canonical booking state machine allows a transition."""

    return new in BOOKING_STATUS_TRANSITIONS[previous]
