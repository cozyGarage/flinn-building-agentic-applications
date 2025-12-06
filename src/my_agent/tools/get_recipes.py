from typing import List, Optional, Any, Dict, cast
from langchain_core.tools import tool
from src.my_agent.data.sample_recipes import sample_recipes


@tool
def get_recipes(
    meal_type: Optional[str] = None,
    tags: Optional[List[str]] = None,
    max_calories: Optional[int] = None,
    limit: int = 5,
) -> List[Dict[str, Any]]:
    """Return recipes that match the provided filters.

    Args:
        meal_type: breakfast, lunch, dinner
        tags: e.g. vegetarian, vegan, gluten-free
        max_calories: max calories per serving
        limit: number of recipes to return

    Returns:
        list of recipe dicts matching the query
    """
    tags = tags or []
    results: List[Dict[str, Any]] = []
    for r in sample_recipes:
        recipe = cast(Dict[str, Any], r)
        if meal_type and recipe.get("meal_type") != meal_type:
            continue
        if tags:
            # ensure all requested tags are present
            recipe_tags: List[str] = cast(List[str], recipe.get("tags", []))
            if not all(t in recipe_tags for t in tags):
                continue
        if (
            max_calories is not None
            and recipe.get("nutrition_per_serving", {}).get("calories") > max_calories
        ):
            continue
        results.append(
            {
                "id": recipe["id"],
                "name": recipe["name"],
                "servings": recipe["servings"],
                "meal_type": recipe["meal_type"],
                "nutrition_per_serving": recipe["nutrition_per_serving"],
            }
        )
        if len(results) >= limit:
            break
    return results
