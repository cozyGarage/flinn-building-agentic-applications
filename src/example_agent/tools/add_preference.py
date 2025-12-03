from langchain_core.tools import tool


@tool
def add_preference(preference_type: str, preference_value: str) -> str:
    """Add a new dietary preference or restriction."""
    # Mocked response
    return f"Preference '{preference_type}: {preference_value}' added successfully"
