from langchain_core.tools import tool


@tool
def multiply_numbers(
    number1: int,
    number2: int,
) -> str:
    """Multiply two numbers together."""
    result = number1 * number2

    return f"{number1} * {number2} = {result}"
