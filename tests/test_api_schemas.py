import pytest
from pydantic import ValidationError
from opticargo_shared.api.pagination import PageParams, PaginatedResponse
from opticargo_shared.api.errors import ErrorResponse, ErrorDetail

def test_page_params_valid():
    """Test instansiasi parameter paginasi."""
    params = PageParams(page=2, page_size=50)
    assert params.page == 2
    assert params.page_size == 50

def test_page_params_default():
    """Test nilai default paginasi."""
    params = PageParams()
    assert params.page == 1
    assert params.page_size == 20

def test_paginated_response_valid():
    """Test respons paginasi generik."""
    # Menggunakan list of strings sebagai tipe generik (T)
    response = PaginatedResponse[str](
        items=["item1", "item2"],
        total=100,
        page=1,
        page_size=20
    )
    assert len(response.items) == 2
    assert response.total == 100

def test_error_response_valid():
    """Test instansiasi error response API."""
    detail = ErrorDetail(field="email", message="Format email tidak valid")
    error = ErrorResponse(
        error_code="VALIDATION_ERR",
        message="Terjadi kesalahan validasi",
        details=[detail]
    )
    assert error.error_code == "VALIDATION_ERR"
    assert len(error.details) == 1

def test_error_response_missing_field():
    """Test validasi gagal jika error_code tidak diisi."""
    with pytest.raises(ValidationError):
        ErrorResponse(  # type: ignore
            message="Terjadi kesalahan",
            details=[]
        )