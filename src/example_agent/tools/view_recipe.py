from langchain_core.tools import tool


@tool
def view_recipe(recipe_id: int) -> str:
    """View a specific recipe by ID in markdown format."""
    # Mocked response
    return f"""# Recipe #{recipe_id}: Chicken Tikka Masala

## Ingredients
- 500g chicken
- 200ml cream
- Spices

## Instructions
1. Marinate chicken
2. Cook in sauce"""
