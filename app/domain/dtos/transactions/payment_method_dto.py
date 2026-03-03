from pydantic import BaseModel, field_validator
from ...enums.payment_method_type import PaymentMethodType

class PaymentMethodDto(BaseModel):
    @field_validator("type", mode="before")
    @classmethod
    def normalize_type(cls, value):
        if isinstance(value, str):
            return value.upper()
        return value
    
    type: PaymentMethodType