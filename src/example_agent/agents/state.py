from typing import Annotated, Any, List, Mapping

from pydantic import BaseModel

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

from src.example_agent.domain.preference_type import PreferenceType
from src.example_agent.domain.recipe import Recipe


class MealPlannerState(BaseModel):
    messages: Annotated[list[BaseMessage], add_messages]
    recipes: List[Recipe] = []
    preferences: dict[PreferenceType, list[str]] = {}

    @staticmethod
    def from_raw_state(state: Mapping[str, Any]) -> "MealPlannerState":
        """Validate a TypedDict/dict state into this Pydantic model."""
        return MealPlannerState.model_validate(state)
