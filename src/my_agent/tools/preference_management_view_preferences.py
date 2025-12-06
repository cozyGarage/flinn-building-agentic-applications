from typing import Any
from langchain.tools import tool, ToolRuntime
from src.example_agent.agents.state import MealPlannerState

_tool_prompt = """\
Retrieve the current user's dietary preferences and restrictions.

Use this tool when you need to know what the user can or cannot eat before searching for or suggesting recipes. It helps ensure recommendations align with the user's needs.

Returns a formatted string listing all preference types (e.g., "Dietary Restrictions", "Dislikes") and their associated values.
"""


@tool(description=_tool_prompt)
def preference_management_view_preferences(
    runtime: ToolRuntime[Any, Any],
) -> str:
    state = MealPlannerState.from_raw_state(runtime.state)
    prefs = state.preferences

    if not prefs:
        return "No preferences set."

    return "\n".join([f"- {key.value}: {', '.join(values)}" for key, values in prefs.items()])
