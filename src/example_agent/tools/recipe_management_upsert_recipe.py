from langchain_core.tools import tool
from src.example_agent.domain.recipe import Recipe
from src.mocks.database.recipe_utils import load_recipes, save_recipes

_tool_prompt = """\
Save a new recipe or update an existing one in the database.

Use this tool when the user wants to save a recipe they found (e.g., from a URL) or modified. It requires a complete `Recipe` object including name, ingredients, and instructions.

Returns a confirmation message with the recipe name and ID upon successful save.
"""


@tool(description=_tool_prompt)
def recipe_management_upsert_recipe(recipe: Recipe) -> str:
    recipes = load_recipes()

    # Use ID as string key for JSON storage
    recipe_id_str = str(recipe.id)

    # Serialize the Pydantic model to a dictionary
    recipes[recipe_id_str] = recipe.model_dump()

    save_recipes(recipes)

    return f"Recipe '{recipe.name}' (ID: {recipe.id}) saved successfully."
