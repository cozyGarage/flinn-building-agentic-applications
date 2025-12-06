"""
Sample recipes dataset for demo and unit tests.
This is intentionally simple and used by tools in `my_agent`.
"""
sample_recipes = [
    {
        "id": "r_bf_1",
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
        "id": "r_lu_1",
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
        "id": "r_di_1",
        "name": "Spaghetti Bolognese",
        "servings": 4,
        "meal_type": "dinner",
        "tags": ["family-friendly"],
        "ingredients": [
            {"name": "Spaghetti", "qty": 400, "unit": "g"},
            {"name": "Ground Beef", "qty": 500, "unit": "g"},
            {"name": "Tomato Sauce", "qty": 2.0, "unit": "cups"},
        ],
        "nutrition_per_serving": {"calories": 650},
    },
    {
        "id": "r_bf_2",
        "name": "Oatmeal with Banana",
        "servings": 1,
        "meal_type": "breakfast",
        "tags": ["vegan"],
        "ingredients": [
            {"name": "Rolled Oats", "qty": 0.5, "unit": "cup"},
            {"name": "Banana", "qty": 1.0, "unit": "each"},
            {"name": "Almond Milk", "qty": 1.0, "unit": "cup"},
        ],
        "nutrition_per_serving": {"calories": 300},
    },
    {
        "id": "r_lu_2",
        "name": "Veggie Wrap",
        "servings": 1,
        "meal_type": "lunch",
        "tags": ["vegetarian"],
        "ingredients": [
            {"name": "Tortilla", "qty": 1.0, "unit": "each"},
            {"name": "Spinach", "qty": 1.0, "unit": "cup"},
            {"name": "Hummus", "qty": 0.25, "unit": "cup"},
        ],
        "nutrition_per_serving": {"calories": 350},
    },
    {
        "id": "r_di_2",
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
