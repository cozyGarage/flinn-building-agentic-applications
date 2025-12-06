from typing import Dict, List, Any, Tuple
from collections import defaultdict
from langchain_core.tools import tool
from src.my_agent.data.sample_recipes import sample_recipes


def _find_recipe_by_id(recipe_id: str) -> Any:
    for r in sample_recipes:
        if r["id"] == recipe_id:
            return r
    return None


@tool
def generate_shopping_list(recipe_ids: List[str], servings: List[int]) -> List[Dict[str, Any]]:
    """Consolidate ingredients across recipes and return a shopping list.

    Args:
        recipe_ids: list of recipe ids to include
        servings: matched list of servings per recipe (same length as recipe_ids)

    Returns:
        consolidated list of {name, total_qty, unit}
    """
    if len(recipe_ids) != len(servings):
        raise ValueError("recipe_ids and servings must be the same length")

    totals: Dict[Tuple[str, str], Dict[str, Any]] = defaultdict(lambda: {"qty": 0.0, "unit": None})

    for rid, s in zip(recipe_ids, servings):
        r = _find_recipe_by_id(rid)
        if not r:
            continue
        base_servings = r.get("servings", 1)
        multiplier = s / base_servings
        for ing in r.get("ingredients", []):
            key = (ing["name"].lower(), ing["unit"])
            totals[key]["qty"] += ing["qty"] * multiplier
            totals[key]["unit"] = ing["unit"]

    result = []
    for (name, unit), val in totals.items():
        qty = float(val.get("qty", 0.0))
        result.append({"name": name, "qty": round(qty, 2), "unit": unit})
    return sorted(result, key=lambda r: r["name"])
