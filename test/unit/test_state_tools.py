from types import SimpleNamespace
from src.my_agent.tools.recipe_management_upsert_recipe import recipe_management_upsert_recipe
from src.my_agent.domain.recipe import Recipe
from src.my_agent.domain.ingredient import Ingredient
from src.my_agent.tools.preference_management_upsert_preference import preference_management_upsert_preference
from src.my_agent.domain.preference_type import PreferenceType


def test_recipe_upsert_updates_state():
    recipe = Recipe(
        id="soup_1",
        name="Tomato Soup",
        ingredients=[Ingredient(id="i1", name="Tomato", qty=200.0, unit="g")],
        instructions="Boil",
    )
    runtime = SimpleNamespace(tool_call_id="t1", state={"messages": [], "recipes": [], "preferences": {}})
    cmd = recipe_management_upsert_recipe.func(recipe, runtime)
    assert cmd.update.recipes[0].id == "soup_1"
    assert any("Recipe 'Tomato Soup'" in m.content for m in cmd.update.messages)


def test_preferences_upsert_updates_state():
    runtime = SimpleNamespace(tool_call_id="p1", state={"messages": [], "recipes": [], "preferences": {}})
    cmd = preference_management_upsert_preference.func(PreferenceType.FAVOURITE_INGREDIENTS, ["tomato"], runtime)
    assert list(cmd.update.preferences.keys())[0] == PreferenceType.FAVOURITE_INGREDIENTS
    assert any("Updated" in m.content for m in cmd.update.messages)

