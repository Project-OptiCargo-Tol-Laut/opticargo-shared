from enum import StrEnum


class UserRole(StrEnum):
    admin = "admin"
    operator_kapal = "operator_kapal"
    distributor = "distributor"
    umkm = "umkm"
    pengepul = "pengepul"
    koperasi = "koperasi"
    pelabuhan = "pelabuhan"
    pemerintah = "pemerintah"
    eksportir = "eksportir"

    # Temporary source-code alias. Serialization remains canonical.
    operator = "operator_kapal"


class AccountStatus(StrEnum):
    pending = "pending"
    active = "active"
    suspended = "suspended"
    disabled = "disabled"
