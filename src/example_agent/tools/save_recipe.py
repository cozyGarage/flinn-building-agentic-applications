from langchain_core.tools import tool


@tool
def save_recipe(recipe_name: str, recipe_content: str) -> str:
    """Add a recipe to the recipe book."""
    # Mocked response - in reality would save the recipe_content
    _ = recipe_content  # Recipe content would be stored in database
    return f"Recipe '{recipe_name}' saved successfully with ID: 4"
