from langchain_core.tools import tool


@tool
def add_numbers(
    number1: int,
    number2: int,
) -> str:
    """Add two numbers together."""
    result = number1 + number2

    return f"{number1} + {number2} = {result}"
