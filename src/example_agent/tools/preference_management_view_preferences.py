from langchain_core.tools import tool
from src.mocks.database.preferences_utils import load_preferences

_tool_prompt = """\
Retrieve the current user's dietary preferences and restrictions.

Use this tool when you need to know what the user can or cannot eat before searching for or suggesting recipes. It helps ensure recommendations align with the user's needs.

Returns a formatted string listing all preference types (e.g., "Dietary Restrictions", "Dislikes") and their associated values.
"""


@tool(description=_tool_prompt)
def preference_management_view_preferences() -> str:
    prefs = load_preferences()

    output = []
    for key, values in prefs.items():
        display_key = key.replace("_", " ").title()
        val_str = ", ".join(values) if values else "None"
        output.append(f"- {display_key}: {val_str}")

    return "Current Preferences:\n" + "\n".join(output)
