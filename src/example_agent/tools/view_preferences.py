from langchain_core.tools import tool


@tool
def view_preferences() -> str:
    """View user dietary preferences and restrictions."""
    # Mocked response
    return """Dietary Preferences:
- Vegetarian: No
- Allergies: Nuts, Shellfish
- Cuisine: Italian, Indian"""
