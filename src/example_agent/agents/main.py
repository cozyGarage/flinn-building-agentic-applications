from typing import Any
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph
from langchain.agents.middleware.types import AgentState
from src.example_agent.tools.extract_recipe_from_url import extract_recipe_from_url
from src.example_agent.tools.list_recipes import list_recipes
from src.example_agent.tools.view_recipe import view_recipe
from src.example_agent.tools.save_recipe import save_recipe
from src.example_agent.tools.view_preferences import view_preferences
from src.example_agent.tools.add_preference import add_preference
from src.example_agent.tools.update_preference import update_preference
from src.common.model_identifiers import ModelIdentifier
from src.example_agent.prompts.agent import SYSTEM_PROMPT

_model = init_chat_model(model=ModelIdentifier.GPT_5, temperature=0.0, reasoning_effort="low")
_tools = [
    extract_recipe_from_url,
    list_recipes,
    view_recipe,
    save_recipe,
    view_preferences,
    add_preference,
    update_preference,
]


# CREATE AGENT INSTANCE
agent: CompiledStateGraph[AgentState[Any], Any, Any, Any] = create_agent(
    _model,
    _tools,
    system_prompt=SYSTEM_PROMPT,
)
