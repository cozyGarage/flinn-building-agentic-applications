from langchain_core.tools import tool


@tool
def update_preference(preference_type: str, new_value: str) -> str:
    """Update an existing dietary preference or restriction."""
    # Mocked response
    return f"Preference '{preference_type}' updated to '{new_value}'"
