from enum import Enum


class ModelIdentifier(str, Enum):
    """Enumeration of model identifiers mapped to their string representations."""

    # GPT-5.1 Models
    GPT_5 = "openai:gpt-5"
    GPT_5_MINI = "openai:gpt-5-mini"
    GPT_5_NANO = "openai:gpt-5-nano"

    # Gemini Models
    GEMINI_2_5_PRO = "google_vertexai:gemini-2.5-pro"
    GEMINI_2_5_FLASH = "google_vertexai:gemini-2.5-flash"
    GEMINI_2_0_FLASH_EXP = "google_vertexai:gemini-2.0-flash-exp"
    GEMINI_1_5_PRO = "google_vertexai:gemini-1.5-pro"
    GEMINI_1_5_FLASH = "google_vertexai:gemini-1.5-flash"
