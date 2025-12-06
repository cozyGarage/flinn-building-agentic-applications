from typing import Any
from langchain.tools import tool, ToolRuntime
from src.example_agent.agents.state import MealPlannerState

_tool_prompt = """\
List all stored recipes in the database.

Use this tool when the user wants to see what recipes they have saved or when you need to find a recipe's ID by its name.

Returns a list of recipe names and their corresponding IDs (e.g., "Pasta Carbonara (ID: 123)").
"""


@tool(description=_tool_prompt)
def recipe_management_list_recipes(
    runtime: ToolRuntime[Any, Any],
) -> str:
    state = MealPlannerState.from_raw_state(runtime.state)
    recipes = state.recipes

    if not recipes:
        return "No recipes found in the recipe book."

    return "\n".join([f"{recipe.name} (ID: {recipe.id})" for recipe in recipes])
