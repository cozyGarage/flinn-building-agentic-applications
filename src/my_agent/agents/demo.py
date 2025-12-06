"""Simple demo runner for the meal planner tools.

Run with: poetry run python -m src.my_agent.agents.demo
"""

from pprint import pprint

from src.my_agent.tools.get_recipes import get_recipes
from src.my_agent.tools.suggest_meal_plan import suggest_meal_plan
from src.my_agent.tools.generate_shopping_list import generate_shopping_list
from src.common.logging_config import logger
from src.common.tracing import tracer
from src.common.token_utils import estimate_tokens_from_text, estimate_cost
from src.common.rate_limiter import rate_limiter


def main() -> None:
    print("=== Sample recipe search (dinner, vegetarian) ===")
    tracer.log_event("demo.start", {"demo": "meal-planner"})
    prompt_estimate_text = "search recipes for dinner vegetarian"
    tokens_est = estimate_tokens_from_text(prompt_estimate_text)
    cost_est = estimate_cost(tokens_est)
    if not rate_limiter.allow("demo_user", tokens_est):
        print("Rate limit exceeded for demo_user; skipping recipe search")
        return
    recipes = get_recipes.run({"meal_type": "dinner", "tags": ["vegetarian"], "limit": 5})
    pprint(recipes)

    print("\n=== Suggest a 3-day vegetarian plan ===")
    plan = suggest_meal_plan.run({"days": 3, "tags": ["vegetarian"]})
    pprint(plan)

    # Build shopping list from the plan for day_1 dinner + day_1 lunch
    print("\n=== Shopping list for first day's lunch & dinner ===")
    recipe_ids = [plan["day_1"]["lunch"]["id"], plan["day_1"]["dinner"]["id"]]
    servings = [plan["day_1"]["lunch"]["servings"], plan["day_1"]["dinner"]["servings"]]
    shopping = generate_shopping_list.run({"recipe_ids": recipe_ids, "servings": servings})
    tracer.log_event("demo.finish", {"recipes": len(recipes)})
    logger.info("demo.finish", extra={"recipes": len(recipes)})
    pprint(shopping)


if __name__ == "__main__":
    main()
