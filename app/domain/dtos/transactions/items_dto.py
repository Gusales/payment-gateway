from pydantic import BaseModel

class ItemDto(BaseModel):
    name: str
    quantity: int
    unit_price: float