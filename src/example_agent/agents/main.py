from typing import Any
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph
from langgraph.checkpoint.memory import MemorySaver
from src.example_agent.tools.recipe_management_extract_recipe_from_url import (
    recipe_management_extract_recipe_from_url,
)
from src.example_agent.tools.recipe_management_list_recipes import recipe_management_list_recipes
from src.example_agent.tools.recipe_management_get_recipe import recipe_management_get_recipe
from src.example_agent.tools.recipe_management_upsert_recipe import recipe_management_upsert_recipe
from src.example_agent.tools.preference_management_view_preferences import (
    preference_management_view_preferences,
)
from src.example_agent.tools.preference_management_upsert_preference import (
    preference_management_upsert_preference,
)
from src.common.model_identifiers import ModelIdentifier
from src.example_agent.prompts.agent import SYSTEM_PROMPT
from src.common.tracing import tracer
from src.common.logging_config import logger
from src.common.middleware import handle_tool_errors, summarization_middleware
from src.example_agent.agents.state import MealPlannerState

try:
    _model = init_chat_model(
        model=ModelIdentifier.GPT_5,
        temperature=0.0,
        reasoning_effort="low",
        parallel_tool_calls=False,
        tracer=getattr(tracer, "client", None),
    )
except TypeError:
    _model = init_chat_model(model=ModelIdentifier.GPT_5, temperature=0.0, reasoning_effort="low", parallel_tool_calls=False)
_tools = [
    recipe_management_extract_recipe_from_url,
    recipe_management_list_recipes,
    recipe_management_get_recipe,
    recipe_management_upsert_recipe,
    preference_management_view_preferences,
    preference_management_upsert_preference,
]

# CREATE CHECKPOINTER FOR MEMORY (SHORT-TERM CONVERSATION HISTORY)
# MemorySaver persists conversation state in memory, enabling the agent to maintain
# context across multiple interactions within the same session
_checkpointer = MemorySaver()

# CREATE AGENT INSTANCE
agent: CompiledStateGraph[MealPlannerState, Any, Any, Any] = create_agent(  # type: ignore[assignment]
    _model,
    _tools,
    system_prompt=SYSTEM_PROMPT,
    middleware=[handle_tool_errors, summarization_middleware],
    state_schema=MealPlannerState,  # type: ignore[arg-type]
    checkpointer=_checkpointer,
)
logger.info("agent.created", extra={"tools": [getattr(t, "name", repr(t)) for t in _tools], "memory": "enabled"})
