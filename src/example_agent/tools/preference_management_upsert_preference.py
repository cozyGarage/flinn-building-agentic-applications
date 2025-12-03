from typing import List
from langchain_core.tools import tool
from src.mocks.database.preferences_utils import load_preferences, save_preferences
from src.example_agent.domain.preference_type import PreferenceType

_tool_prompt = """\
Update or insert user dietary preferences or restrictions. 

Use this tool when the user wants to change their preferences (e.g., "I am vegan" or "I don't like mushrooms").
It overwrites the existing list for a specific preference type. To add to an existing list, you must know the current values and include them in the new list.

Returns a confirmation message indicating the update was successful.
"""


@tool(description=_tool_prompt)
def preference_management_upsert_preference(
    preference_type: PreferenceType, preference_values: List[str]
) -> str:
    prefs = load_preferences()
    pt_value = preference_type.value if isinstance(preference_type, PreferenceType) else preference_type

    # Overwrite the entire list for this key
    prefs[pt_value] = preference_values
    save_preferences(prefs)

    return f"Updated {pt_value} preferences successfully."
