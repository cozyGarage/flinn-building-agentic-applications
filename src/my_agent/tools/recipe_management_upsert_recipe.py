from typing import Any
from langchain.tools import tool, ToolRuntime
from langgraph.types import Command
from langchain_core.messages import ToolMessage
from src.my_agent.domain.recipe import Recipe
from src.my_agent.agents.state import MealPlannerState

_tool_prompt = """\
Save a new recipe or update an existing one in the database.

Use this tool when the user wants to save a recipe they found (e.g., from a URL) or modified. It requires a complete `Recipe` object including name, ingredients, and instructions.

Returns a confirmation message with the recipe name and ID upon successful save.
"""


@tool(description=_tool_prompt)
def recipe_management_upsert_recipe(
    recipe: Recipe,
    runtime: ToolRuntime[Any, Any],
) -> Command[Any]:
    state = MealPlannerState.from_raw_state(runtime.state)
    recipes = state.recipes.copy()

    # Check if recipe with same ID exists and update it, otherwise append
    existing_index = next((index for (index, r) in enumerate(recipes) if r.id == recipe.id), None)

    if existing_index is not None:
        recipes[existing_index] = recipe
    else:
        recipes.append(recipe)

    new_messages = [
        *state.messages,
        ToolMessage(
            f"Recipe '{recipe.name}' (ID: {recipe.id}) saved successfully.",
            tool_call_id=runtime.tool_call_id,
        ),
    ]

    # Update the state
    state.recipes = recipes
    state.messages = new_messages

    return Command(update=state)
