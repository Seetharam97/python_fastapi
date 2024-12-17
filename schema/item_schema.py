from pydantic import BaseModel
from typing import Optional

class ItemValidationSchema(BaseModel):
    # id:int
    name: str
    description: Optional[str] = None
    price: float
    on_offer: bool

class Config:
    orm_mode = True