import json
from pathlib import Path

from opticargo_shared.events import DomainEvent, EventType


def test_every_event_type_has_a_valid_canonical_fixture() -> None:
    fixtures = Path("tests/fixtures/events")
    found_types = {
        DomainEvent.model_validate_json(path.read_text(encoding="utf-8")).event_type
        for path in fixtures.glob("*.json")
    }
    assert found_types == {event_type.value for event_type in EventType}


def test_fixtures_contain_no_sensitive_field_names() -> None:
    forbidden = {"password", "password_hash", "cvv", "api_key", "access_token"}
    for path in Path("tests/fixtures").rglob("*.json"):
        payload = json.loads(path.read_text(encoding="utf-8"))
        serialized = json.dumps(payload).lower()
        assert all(field not in serialized for field in forbidden), path
