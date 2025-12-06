from typing import List, Dict, Any, Optional, cast
from langchain_core.tools import tool
from src.my_agent.data.sample_recipes import sample_recipes


def _filter_by_tags_and_mealtype(meal_type: str, tags: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    tags = tags or []
    results: List[Dict[str, Any]] = []
    for r in sample_recipes:
        if r.get("meal_type") != meal_type:
            continue
        recipe_tags: List[str] = cast(List[str], r.get("tags", []))
        if not all(t in recipe_tags for t in tags):
            continue
        results.append(r)
    return results


@tool
def suggest_meal_plan(days: int = 3, tags: Optional[List[str]] = None) -> Dict[str, Dict[str, Any]]:
    """Suggest a simple meal plan for a given number of days using sample recipes.

    Args:
        days: number of days in plan
        tags: dietary tags to match (e.g., vegetarian, vegan, gluten-free)

    Returns:
        dict mapping day -> meals
    """
    tags = tags or []
    # For each meal_type: pick a recipe that matches tags
    plan = {}
    meal_types = ["breakfast", "lunch", "dinner"]
    for day in range(1, days + 1):
        day_plan = {}
        for mt in meal_types:
            candidates = _filter_by_tags_and_mealtype(mt, tags)
            if not candidates:
                # fallback to any recipe matching meal_type
                candidates = [r for r in sample_recipes if r["meal_type"] == mt]
            recipe = candidates[(day - 1) % len(candidates)]
            day_plan[mt] = {"id": recipe["id"], "name": recipe["name"], "servings": recipe["servings"]}
        plan[f"day_{day}"] = day_plan
    return plan
