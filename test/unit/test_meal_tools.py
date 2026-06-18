from src.my_agent.tools.get_recipes import get_recipes
from src.my_agent.tools.generate_shopping_list import generate_shopping_list
from src.my_agent.tools.suggest_meal_plan import suggest_meal_plan


def test_get_recipes_by_meal_type():
    result = get_recipes.run({"meal_type": "dinner"})
    assert isinstance(result, list)
    assert all(r["meal_type"] == "dinner" for r in result)


def test_suggest_meal_plan_basic():
    plan = suggest_meal_plan.run({"days": 2, "tags": []})
    assert "day_1" in plan
    assert "day_2" in plan
    assert all("breakfast" in plan[d] for d in plan)


def test_generate_shopping_list_aggregates():
    plan = suggest_meal_plan.run({"days": 1})
    rid_lunch = plan["day_1"]["lunch"]["id"]
    rid_dinner = plan["day_1"]["dinner"]["id"]
    servings = [plan["day_1"]["lunch"]["servings"], plan["day_1"]["dinner"]["servings"]]
    shopping = generate_shopping_list.run({"recipe_ids": [rid_lunch, rid_dinner], "servings": servings})
    assert isinstance(shopping, list)
    assert any(isinstance(i["qty"], float) or isinstance(i["qty"], int) for i in shopping)

