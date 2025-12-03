from typing import Any, List
from langchain.tools import tool, ToolRuntime
from langgraph.types import Command
from langchain_core.messages import ToolMessage
from src.example_agent.domain.preference_type import PreferenceType
from src.example_agent.agents.state import MealPlannerState

_tool_prompt = """\
Update or insert user dietary preferences or restrictions. 

Use this tool when the user wants to change their preferences (e.g., "I am vegan" or "I don't like mushrooms").
It overwrites the existing list for a specific preference type. To add to an existing list, you must know the current values and include them in the new list.

Returns a confirmation message indicating the update was successful.
"""


@tool(description=_tool_prompt)
def preference_management_upsert_preference(
    preference_type: PreferenceType,
    preference_values: List[str],
    runtime: ToolRuntime[Any, Any],
) -> Command[Any]:
    # Get current preferences copy to avoid mutation issues before update
    state = MealPlannerState.from_raw_state(runtime.state)
    current_prefs = state.preferences

    # Update the specific preference type
    current_prefs[preference_type] = preference_values
    new_preferences = current_prefs

    new_messages = [
        *state.messages,
        ToolMessage(
            f"Updated {preference_type.value} preferences successfully.",
            tool_call_id=runtime.tool_call_id,
        ),
    ]

    # Update the state
    state.preferences = new_preferences
    state.messages = new_messages

    return Command(update=state)
