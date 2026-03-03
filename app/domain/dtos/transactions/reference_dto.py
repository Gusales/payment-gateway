from pydantic import BaseModel

class ReferenceDto(BaseModel):
    type: str
    id: str