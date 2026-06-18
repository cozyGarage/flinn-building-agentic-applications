"""Simple tracer shim used for demo and offline testing.
LangSmith/real tracing integrations should replace this in production.
"""
from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class _Tracer:
    def log_event(self, name: str, metadata: Dict[str, Any] | None = None) -> None:
        # Silently accept tracing calls. This can be extended to log to a file
        # or to a tracing backend like LangSmith.
        pass


tracer = _Tracer()

