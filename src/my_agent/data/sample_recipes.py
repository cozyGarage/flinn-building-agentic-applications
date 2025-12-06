# Sample recipe dataset for the meal planner agent

sample_recipes = [
    {
        "id": "chicken_salad",
        "name": "Chicken Avocado Salad",
        "meal_type": "lunch",
        "tags": ["gluten-free"],
        "servings": 2,
        "ingredients": [
            {"name": "chicken breast", "qty": 300, "unit": "g"},
            {"name": "avocado", "qty": 1, "unit": "unit"},
            {"name": "mixed greens", "qty": 150, "unit": "g"},
            {"name": "olive oil", "qty": 2, "unit": "tbsp"},
            {"name": "lemon juice", "qty": 1, "unit": "tbsp"},
        ],
        "nutrition_per_serving": {"calories": 420, "protein": 32, "carbs": 8, "fat": 28},
        "steps": [
            "Cook chicken and slice",
            "Toss with greens, avocado, lemon and olive oil",
            "Serve chilled",
        ],
    },
    {
        "id": "veg_stir_fry",
        "name": "Tofu Veg Stir Fry",
        "meal_type": "dinner",
        "tags": ["vegetarian"],
        "servings": 2,
        "ingredients": [
            {"name": "tofu", "qty": 250, "unit": "g"},
            {"name": "broccoli", "qty": 150, "unit": "g"},
            {"name": "carrot", "qty": 1, "unit": "unit"},
            {"name": "soy sauce", "qty": 2, "unit": "tbsp"},
            {"name": "sesame oil", "qty": 1, "unit": "tbsp"},
        ],
        "nutrition_per_serving": {"calories": 360, "protein": 18, "carbs": 20, "fat": 16},
        "steps": ["Cube and brown tofu", "Stir-fry veggies and toss with tofu and sauce", "Serve warm"],
    },
    {
        "id": "oatmeal_bowl",
        "name": "Oatmeal Breakfast Bowl",
        "meal_type": "breakfast",
        "tags": ["vegan"],
        "servings": 1,
        "ingredients": [
            {"name": "rolled oats", "qty": 60, "unit": "g"},
            {"name": "almond milk", "qty": 200, "unit": "ml"},
            {"name": "banana", "qty": 1, "unit": "unit"},
            {"name": "maple syrup", "qty": 1, "unit": "tbsp"},
            {"name": "chia seeds", "qty": 1, "unit": "tbsp"},
        ],
        "nutrition_per_serving": {"calories": 330, "protein": 8, "carbs": 56, "fat": 8},
        "steps": ["Cook oats with almond milk", "Top with banana and maple syrup", "Serve warm"],
    },
]
