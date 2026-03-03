from pydantic import BaseModel

class CustomerDto(BaseModel):
    id: str
    name: str
    document: str
    email: str