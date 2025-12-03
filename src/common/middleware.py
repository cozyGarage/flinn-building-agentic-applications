from typing import Any, Callable, Awaitable
from langchain_core.messages import ToolMessage
from langgraph.prebuilt.tool_node import ToolCallRequest
from langgraph.types import Command
from langchain.agents.middleware import AgentMiddleware, SummarizationMiddleware
from src.common.model_identifiers import ModelIdentifier


class HandleToolErrors(AgentMiddleware):
    """Middleware to handle tool execution errors with custom messages."""

    def wrap_tool_call(
        self,
        request: ToolCallRequest,
        handler: Callable[[ToolCallRequest], ToolMessage | Command[Any]],
    ) -> ToolMessage | Command[Any]:
        """Synchronous tool error handler."""
        try:
            return handler(request)
        except Exception as e:
            return ToolMessage(
                content=f"Tool error: Use the error message to understand if you can fix the issue: {str(e)}",
                tool_call_id=request.tool_call["id"],
            )

    async def awrap_tool_call(
        self,
        request: ToolCallRequest,
        handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command[Any]]],
    ) -> ToolMessage | Command[Any]:
        """Asynchronous tool error handler."""
        try:
            return await handler(request)
        except Exception as e:
            return ToolMessage(
                content=f"Tool error: Use the error message to understand if you can fix the issue: {str(e)}",
                tool_call_id=request.tool_call["id"],
            )


# Create an instance for use in agents
handle_tool_errors = HandleToolErrors()

# Summarization middleware to compact message history
summarization_middleware = SummarizationMiddleware(
    model=ModelIdentifier.GPT_5_MINI,
    trigger=("tokens", 10000),
    keep=("messages", 20),
)
