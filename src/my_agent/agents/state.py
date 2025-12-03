from typing import Any, Annotated, Mapping
from pydantic import BaseModel
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class CustomAgentState(BaseModel):
    messages: Annotated[list[BaseMessage], add_messages]

    @staticmethod
    def from_raw_state(state: Mapping[str, Any]) -> "CustomAgentState":
        """Validate a TypedDict/dict state into this Pydantic model."""
        return CustomAgentState.model_validate(state)
