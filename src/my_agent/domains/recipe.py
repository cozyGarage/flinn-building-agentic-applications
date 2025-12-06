from typing import Optional
from pydantic import BaseModel
from src.my_agent.domains.ingredient import Ingredient


class Recipe(BaseModel):
    id: str
    name: str
    ingredients: list[Ingredient]
    instructions: str
    cuisine: Optional[str] = None
    source_url: Optional[str] = None
