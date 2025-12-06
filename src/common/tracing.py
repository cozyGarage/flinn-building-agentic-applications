import os
import json
from typing import Any, Dict, Optional
from datetime import datetime

_TRACE_FILE = os.path.join(os.getcwd(), "traces.log")


class LocalTracer:
    """Simple local tracer that appends JSON events to a file.
    Optionally calls LangSmith tracer if available.
    """

    def __init__(self, project: Optional[str] = None):
        self.project = project
        self.client = None
        # Try to import LangSmith tracer if available
        try:
            from langsmith import LangSmithTracer

            # Create a tracer using env config if available
            try:
                self.client = LangSmithTracer(project=project)
            except Exception:
                # If the SDK signature differs, keep client None and proceed with local tracing
                self.client = None
        except Exception:
            self.client = None

    def log_event(self, name: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        metadata = metadata or {}
        event = {
            "time": datetime.utcnow().isoformat() + "Z",
            "event": name,
            "project": self.project,
            "metadata": metadata,
        }
        try:
            with open(_TRACE_FILE, "a") as fh:
                fh.write(json.dumps(event) + "\n")
        except Exception:
            pass

        # If we initialized LangSmith tracer, try to record it (best-effort).
        if self.client is not None:
            try:
                # Attempting a generic method; real API may differ - this is best-effort
                if hasattr(self.client, "record_event"):
                    self.client.record_event(name=name, metadata=metadata)
                elif hasattr(self.client, "log"):
                    self.client.log(name=name, metadata=metadata)
            except Exception:
                # Fall back silently if LangSmith API differs
                pass


# Instantiate a global tracer using environment overrides
def create_tracer() -> LocalTracer:
    project = os.getenv("LANGSMITH_PROJECT")
    return LocalTracer(project=project)


tracer = create_tracer()
