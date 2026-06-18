"""
Sample recipes dataset for my_agent demo and unit tests.
"""
sample_recipes = [
    {
        "id": "chicken_salad",
        "name": "Grilled Chicken Salad",
        "servings": 2,
        "meal_type": "lunch",
        "tags": ["gluten-free"],
        "ingredients": [
            {"name": "Chicken Breast", "qty": 200, "unit": "g"},
            {"name": "Mixed Greens", "qty": 2.0, "unit": "cups"},
            {"name": "Cherry Tomatoes", "qty": 0.5, "unit": "cup"},
        ],
        "nutrition_per_serving": {"calories": 400},
    },
    {
        "id": "yogurt_parfait",
        "name": "Yogurt Parfait",
        "servings": 1,
        "meal_type": "breakfast",
        "tags": ["vegetarian"],
        "ingredients": [
            {"name": "Greek Yogurt", "qty": 1.0, "unit": "cup"},
            {"name": "Granola", "qty": 0.5, "unit": "cup"},
            {"name": "Blueberries", "qty": 0.5, "unit": "cup"},
        ],
        "nutrition_per_serving": {"calories": 250},
    },
    {
        "id": "stir_fry_tofu",
        "name": "Stir-Fried Tofu and Vegetables",
        "servings": 2,
        "meal_type": "dinner",
        "tags": ["vegan", "gluten-free"],
        "ingredients": [
            {"name": "Tofu", "qty": 250, "unit": "g"},
            {"name": "Bell Pepper", "qty": 1.0, "unit": "each"},
            {"name": "Soy Sauce", "qty": 2.0, "unit": "tbsp"},
        ],
        "nutrition_per_serving": {"calories": 400},
    },
]
