from typing import Optional
from pydantic import BaseModel
from src.example_agent.domain.ingredient import Ingredient


class Recipe(BaseModel):
    id: int
    name: str
    ingredients: list[Ingredient]
    instructions: str
    cuisine: Optional[str] = None
    source_url: Optional[str] = None
