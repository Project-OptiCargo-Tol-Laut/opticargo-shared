from pydantic import BaseModel

class ErrorDetail(BaseModel):
    field: str | None = None
    message: str

class ErrorResponse(BaseModel):
    error_code: str
    message: str
    details: list[ErrorDetail] = []