from langchain_core.tools import tool
from src.mocks.database.recipe_utils import load_recipes
from src.example_agent.domain.recipe import Recipe

_tool_prompt = """\
Retrieve full details of a specific recipe using its ID.

Use this tool when the user asks for the ingredients or instructions of a saved recipe.

Returns a markdown-formatted string containing the recipe name, ingredients list, and step-by-step instructions.
"""


@tool(description=_tool_prompt)
def recipe_management_view_recipe(recipe_id: int) -> str:
    recipes = load_recipes()
    recipe_id_str = str(recipe_id)

    if recipe_id_str not in recipes:
        return f"Recipe with ID {recipe_id} not found."

    # Reconstruct Recipe object from data
    raw_recipe = recipes[recipe_id_str]
    recipe = Recipe(**raw_recipe)

    ingredients_md = "\n".join([f"- {ing.quantity}{ing.unit} {ing.name}" for ing in recipe.ingredients])

    return f"""\
# {recipe.name} (ID: {recipe.id})

## Ingredients
{ingredients_md}

## Instructions
{recipe.instructions}"""
