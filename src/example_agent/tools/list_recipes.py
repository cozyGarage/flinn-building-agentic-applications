from langchain_core.tools import tool


@tool
def list_recipes() -> str:
    """Return a list of all stored recipes."""
    # Mocked response
    return """1. Spaghetti Carbonara
2. Chicken Tikka Masala
3. Caesar Salad"""
