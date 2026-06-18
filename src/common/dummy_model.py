"""A very small Dummy Chat Model to run locally without contacting external APIs.
This is intentionally minimal — it only provides the methods used by the demo agent
and returns a deterministic string response to make testing easier.
"""
from typing import Any
import asyncio


class DummyChatModel:
    def __init__(self, model: str = "dummy"):  # pragma: no cover - simple shim
        self.model = model

    def __repr__(self) -> str:  # pragma: no cover - convenience
        return f"DummyChatModel(model={self.model})"

    def generate(self, *args: Any, **kwargs: Any) -> Any:  # pragma: no cover - shim
        # Return a simple object with a `.generations` attribute compatible with
        # what a real chat model returns (lightweight shim)
        class _Gen:
            def __init__(self, text: str):
                self.text = text

        class _Result:
            def __init__(self, gens: list[_Gen]):
                self.generations = gens

        return _Result([_Gen("Dummy response")])

    async def agenerate(self, *args: Any, **kwargs: Any) -> Any:  # pragma: no cover - shim
        return self.generate(*args, **kwargs)

    def chat(self, *args: Any, **kwargs: Any) -> Any:  # pragma: no cover - shim
        return self.generate(*args, **kwargs)

    async def achat(self, *args: Any, **kwargs: Any) -> Any:  # pragma: no cover - shim
        return self.agenerate(*args, **kwargs)

    # Tools binding API expected by LangChain agents
    def bind_tools(self, tools: list[Any]):  # pragma: no cover - shim
        """Store bound tools for later use. Real models implement this
        method to expose tools to the agent. For the dummy model we simply
        keep a reference for debug / validation."""
        self._bound_tools = tools
        return self

    def _llm_type(self) -> str:  # pragma: no cover - shim
        return "dummy"
