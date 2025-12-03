from typing import Optional
from pydantic import BaseModel
from langgraph.runtime import Runtime


class AgentContext(BaseModel):
    user_name: Optional[str] = None

    @staticmethod
    def from_runtime(runtime: Runtime["AgentContext"]) -> "AgentContext":
        ctx_raw = runtime.context
        ctx = AgentContext.model_validate(ctx_raw)
        return ctx
