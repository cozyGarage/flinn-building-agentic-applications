from typing import Any
import os
from langchain.chat_models import init_chat_model
from src.common.dummy_model import DummyChatModel
from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph
from src.my_agent.tools.recipe_management_extract_recipe_from_url import (
    recipe_management_extract_recipe_from_url,
)
from src.my_agent.tools.recipe_management_list_recipes import recipe_management_list_recipes
from src.my_agent.tools.recipe_management_get_recipe import recipe_management_get_recipe
from src.my_agent.tools.recipe_management_upsert_recipe import recipe_management_upsert_recipe
from src.my_agent.tools.preference_management_view_preferences import (
    preference_management_view_preferences,
)
from src.my_agent.tools.preference_management_upsert_preference import (
    preference_management_upsert_preference,
)
from src.my_agent.tools.get_recipes import get_recipes
from src.my_agent.tools.generate_shopping_list import generate_shopping_list
from src.my_agent.tools.suggest_meal_plan import suggest_meal_plan
from src.common.model_identifiers import ModelIdentifier
from src.my_agent.prompts.agent import SYSTEM_PROMPT
from src.common.middleware import handle_tool_errors, summarization_middleware
from src.my_agent.agents.state import MealPlannerState

try:
    if os.getenv("USE_DUMMY_MODEL") == "true":
        _model = DummyChatModel(model="dummy-model")
    else:
        _model = init_chat_model(
            model=ModelIdentifier.GPT_5,
            temperature=0.0,
            reasoning_effort="low",
            parallel_tool_calls=False,
        )
except TypeError:
    _model = init_chat_model(
        model=ModelIdentifier.GPT_5, temperature=0.0, reasoning_effort="low", parallel_tool_calls=False
    )
_tools = [
    recipe_management_extract_recipe_from_url,
    recipe_management_list_recipes,
    recipe_management_get_recipe,
    recipe_management_upsert_recipe,
    preference_management_view_preferences,
    preference_management_upsert_preference,
    get_recipes,
    generate_shopping_list,
    suggest_meal_plan,
]


# CREATE AGENT INSTANCE
_checkpointer = None
try:
    from langgraph.checkpoint.memory import MemorySaver

    # Only use a custom checkpointer when explicitly enabled. LangGraph dev warns
    # that platform handles persistence automatically in the cloud - passing a custom
    # checkpointer can be ignored/deprecated. Use USE_CUSTOM_CHECKPOINTER=true to enable.
    if os.getenv("USE_CUSTOM_CHECKPOINTER") == "true":
        _checkpointer = MemorySaver()
except Exception:
    _checkpointer = None

agent: CompiledStateGraph[MealPlannerState, Any, Any, Any] = create_agent(  # type: ignore[assignment]
    _model,
    _tools,
    system_prompt=SYSTEM_PROMPT,
    middleware=[handle_tool_errors, summarization_middleware],
    state_schema=MealPlannerState,  # type: ignore[arg-type]
    checkpointer=_checkpointer if _checkpointer is not None else None,
)
