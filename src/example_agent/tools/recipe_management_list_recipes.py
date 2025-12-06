from langchain_core.tools import tool
from src.example_agent.domain.recipe import Recipe
from src.mocks.database.recipe_utils import load_recipes

_tool_prompt = """\
List all stored recipes in the database.

Use this tool when the user wants to see what recipes they have saved or when you need to find a recipe's ID by its name.

Returns a list of recipe names and their corresponding IDs (e.g., "Pasta Carbonara (ID: 123)").
"""


@tool(description=_tool_prompt)
def recipe_management_list_recipes() -> str:
    recipes = load_recipes()

    if not recipes:
        return "No recipes found in the recipe book."

    validated_recipies = [Recipe(**data) for data in recipes.values()]
    name_id_pairs = [(recipe.name, recipe.id) for recipe in validated_recipies]

    return "\n".join([f"{name} (ID: {id})" for name, id in name_id_pairs])
