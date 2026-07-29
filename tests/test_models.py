from datetime import UTC, datetime
from decimal import Decimal
from uuid import uuid4

import pytest
from pydantic import ValidationError

from opticargo_shared.enums import AccountStatus, ShipStatus, UserRole
from opticargo_shared.models import ShipRead, UserRead

NOW = datetime.now(UTC)


def test_user_read_is_safe_and_uses_final_role() -> None:
    user = UserRead(
        id=uuid4(),
        username="operator_01",
        email="operator@opticargo.id",
        role=UserRole.operator,
        account_status=AccountStatus.active,
        created_at=NOW,
        updated_at=NOW,
    )
    assert user.role.value == "operator_kapal"
    assert "password_hash" not in UserRead.model_json_schema()["properties"]
    with pytest.raises(ValidationError):
        UserRead.model_validate({**user.model_dump(), "password_hash": "secret"})


def test_ship_validates_numbers_and_aware_time() -> None:
    ship_data = {
        "id": uuid4(),
        "name": "KM Nusantara Jaya",
        "imo_number": "IMO9123456",
        "ship_type": "General Cargo",
        "gross_tonnage": Decimal("5000.50"),
        "deadweight_tonnage": Decimal("7000.00"),
        "cargo_capacity_m3": Decimal("8500.00"),
        "operator_id": uuid4(),
        "flag": "Indonesia",
        "status": ShipStatus.active,
        "created_at": NOW,
        "updated_at": NOW,
    }
    assert ShipRead(**ship_data).name == "KM Nusantara Jaya"
    with pytest.raises(ValidationError):
        ShipRead(**{**ship_data, "gross_tonnage": "NaN"})
    with pytest.raises(ValidationError):
        ShipRead(**{**ship_data, "created_at": datetime.now()})
