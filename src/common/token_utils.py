from typing import Any, Optional

tiktoken: Optional[Any] = None
try:
    import tiktoken

    _HAS_TIKTOKEN = True
except Exception:
    tiktoken = None
    _HAS_TIKTOKEN = False


def estimate_tokens_from_text(text: str, model: str = "gpt-4o") -> int:
    """Estimate tokens for a text using tiktoken if available; otherwise fallback to a word-based heuristic."""
    if _HAS_TIKTOKEN and tiktoken is not None:
        try:
            enc = tiktoken.encoding_for_model(model)
            return len(enc.encode(text))
        except Exception:
            # fallback heuristic
            return max(1, len(text.split()))
    else:
        return max(1, len(text.split()))


def estimate_cost(tokens: int, price_per_1k: float = 0.03) -> float:
    """Estimate cost in USD for a given token count and model price per 1k tokens."""
    return (tokens / 1000.0) * price_per_1k
