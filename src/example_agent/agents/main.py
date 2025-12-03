from typing import Any
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph
from langchain.agents.middleware.types import AgentState
from src.example_agent.tools.add_numbers import add_numbers
from src.example_agent.tools.multiply_numbers import multiply_numbers
from src.common.model_identifiers import ModelIdentifier
from src.example_agent.agents.context import AgentContext
from src.example_agent.agents.state import CustomAgentState
from src.common.middleware import handle_tool_errors
from src.example_agent.prompts.agent import SYSTEM_PROMPT

_model = init_chat_model(model=ModelIdentifier.GPT_5, temperature=0.0, reasoning_effort="low")
_tools = [add_numbers, multiply_numbers]


# CREATE AGENT INSTANCE
agent: CompiledStateGraph[AgentState[Any], Any, Any, Any] = create_agent(
    _model,
    _tools,
    middleware=[handle_tool_errors],
    context_schema=AgentContext,
    state_schema=CustomAgentState,  # type: ignore[arg-type]
    system_prompt=SYSTEM_PROMPT,
)
