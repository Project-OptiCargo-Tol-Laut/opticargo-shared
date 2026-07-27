import pytest
from uuid import uuid4
from datetime import datetime
from decimal import Decimal
from pydantic import ValidationError

from opticargo_shared.models.user import User
from opticargo_shared.models.ship import Ship
from opticargo_shared.enums import UserRole, ShipStatus

def test_user_valid_instantiation():
    """Test instansiasi User dengan data yang valid."""
    user = User(
        id=uuid4(),
        username="operator_01",
        email="operator@opticargo.id",
        role=UserRole.operator,
        created_at=datetime.now()
    )
    assert user.username == "operator_01"
    assert user.role == UserRole.operator

def test_user_invalid_email():
    """Test validasi gagal jika email tidak sesuai format."""
    with pytest.raises(ValidationError):
        User(
            id=uuid4(),
            username="operator_01",
            email="bukan-email-valid",
            role=UserRole.operator,
            created_at=datetime.now()
        )

def test_ship_valid_instantiation():
    """Test instansiasi Ship dengan data yang valid."""
    ship = Ship(
        id=uuid4(),
        name="KM Nusantara Jaya",
        imo_number="IMO9123456",
        ship_type="General Cargo",
        gross_tonnage=Decimal("5000.50"),
        deadweight_tonnage=Decimal("7000.00"),
        cargo_capacity_m3=Decimal("8500.00"),
        operator_id=uuid4(),
        flag="Indonesia",
        status=ShipStatus.active,
        created_at=datetime.now()
    )
    assert ship.name == "KM Nusantara Jaya"
    assert ship.status == ShipStatus.active

def test_ship_missing_required_field():
    """Test validasi gagal jika field wajib (seperti status) tidak diisi."""
    with pytest.raises(ValidationError):
        Ship(  # type: ignore
            id=uuid4(),
            name="KM Nusantara Jaya",
            imo_number="IMO9123456",
            ship_type="General Cargo",
            gross_tonnage=Decimal("5000.50"),
            deadweight_tonnage=Decimal("7000.00"),
            cargo_capacity_m3=Decimal("8500.00"),
            operator_id=uuid4(),
            flag="Indonesia",
            # status tidak diisi, seharusnya error
            created_at=datetime.now()
        )