from typing import Any
from langchain.tools import tool, ToolRuntime
from src.my_agent.agents.state import MealPlannerState

_tool_prompt = """\
Retrieve full details of a specific recipe using its ID.

Use this tool when the user asks for the ingredients or instructions of a saved recipe.

Returns a markdown-formatted string containing the recipe name, ingredients list, and step-by-step instructions.
"""


@tool(description=_tool_prompt)
def recipe_management_get_recipe(
    recipe_id: str,
    runtime: ToolRuntime[Any, Any],
) -> str:
    state = MealPlannerState.from_raw_state(runtime.state)
    recipes = state.recipes

    # Find recipe
    recipe = next((r for r in recipes if r.id == recipe_id), None)

    if not recipe:
        return f"Recipe with ID {recipe_id} not found."

    ingredients_md = "\n".join([f"- {ing.qty}{ing.unit} {ing.name}" for ing in getattr(recipe, "ingredients", [])])

    return f"""\
# {recipe.name} (ID: {recipe.id})

## Ingredients
{ingredients_md}

## Instructions
{recipe.instructions}"""
