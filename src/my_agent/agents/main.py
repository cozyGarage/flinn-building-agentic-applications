from typing import Any
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph
from langchain.agents.middleware.types import AgentState
from src.my_agent.tools.get_recipes import get_recipes
from src.my_agent.tools.generate_shopping_list import generate_shopping_list
from src.my_agent.tools.suggest_meal_plan import suggest_meal_plan
from src.common.model_identifiers import ModelIdentifier
from src.my_agent.prompts.agent import SYSTEM_PROMPT

_model = init_chat_model(model=ModelIdentifier.GPT_5, temperature=0.0, reasoning_effort="low")
_tools = [get_recipes, generate_shopping_list, suggest_meal_plan]


# CREATE AGENT INSTANCE
agent: CompiledStateGraph[AgentState[Any], Any, Any, Any] = create_agent(
    _model,
    _tools,
    system_prompt=SYSTEM_PROMPT,
)
