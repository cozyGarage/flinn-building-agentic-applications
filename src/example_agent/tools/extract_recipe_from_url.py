from langchain_core.tools import tool


@tool
def extract_recipe_from_url(url: str) -> str:
    """Extract a recipe from a URL and return it in markdown format."""
    # Mocked response - in reality would fetch from the URL
    _ = url  # URL would be used to fetch the recipe
    return """# Spaghetti Carbonara

## Ingredients
- 400g spaghetti
- 200g pancetta
- 4 eggs
- 100g parmesan

## Instructions
1. Cook pasta
2. Fry pancetta
3. Mix eggs and cheese
4. Combine all"""
