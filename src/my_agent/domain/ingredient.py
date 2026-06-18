from pydantic import BaseModel


class Ingredient(BaseModel):
    id: str
    name: str
    qty: float
    unit: str
