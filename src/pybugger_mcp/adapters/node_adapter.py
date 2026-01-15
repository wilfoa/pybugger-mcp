"""Node.js debug adapter (vscode-js-debug).

This is a STUB showing how a Node.js adapter would be implemented.
It is NOT functional - just a template for future implementation.

To make this work, you would need:
1. Install vscode-js-debug: npm install -g @vscode/js-debug
2. Implement the actual DAP communication

The vscode-js-debug adapter supports:
- Node.js
- Chrome/Edge debugging
- TypeScript (with source maps)
- Deno
"""

import asyncio
import logging
from typing import Any

from pybugger_mcp.adapters.base import (
    AttachConfig,
    DebugAdapter,
    Language,
    LaunchConfig,
)
from pybugger_mcp.adapters.dap_client import DAPClient
from pybugger_mcp.adapters.factory import register_adapter
from pybugger_mcp.models.dap import (
    Breakpoint,
    Scope,
    SourceBreakpoint,
    StackFrame,
    Thread,
    Variable,
)

logger = logging.getLogger(__name__)


# Uncomment to enable registration (currently disabled as it's a stub)
# @register_adapter(Language.JAVASCRIPT)
# @register_adapter(Language.TYPESCRIPT)
class NodeAdapter(DebugAdapter):
    """Debug adapter for Node.js using vscode-js-debug.

    This adapter communicates with the vscode-js-debug DAP server
    to debug JavaScript and TypeScript applications.

    NOTE: This is a STUB implementation for reference.
    """

    @property
    def language(self) -> Language:
        return Language.JAVASCRIPT

    @property
    def is_connected(self) -> bool:
        return self._client is not None and self._client.is_connected

    @property
    def is_launched(self) -> bool:
        return self._launched

    @property
    def capabilities(self) -> dict[str, Any]:
        return self._capabilities

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self._client: DAPClient | None = None
        self._process: asyncio.subprocess.Process | None = None
        self._capabilities: dict[str, Any] = {}
        self._launched = False

    async def initialize(self) -> dict[str, Any]:
        """Start vscode-js-debug and initialize DAP connection.

        The js-debug adapter can be started in several ways:
        1. Inline mode (stdio): js-debug-adapter
        2. Server mode: js-debug-adapter --server=<port>

        Returns:
            Debug adapter capabilities
        """
        raise NotImplementedError(
            "Node.js adapter is a stub. To implement:\n"
            "1. Start js-debug-adapter process\n"
            "2. Create DAPClient with process streams\n"
            "3. Send 'initialize' request\n"
            "4. Store capabilities"
        )

    async def launch(self, config: LaunchConfig | Any, **kwargs: Any) -> None:
        """Launch a Node.js program for debugging.

        Node-specific launch options (in config.extra):
        - runtimeExecutable: Path to node/ts-node/etc.
        - runtimeArgs: Arguments to runtime (e.g., --inspect)
        - skipFiles: Glob patterns to skip
        - sourceMaps: Enable source map support
        - outFiles: Where to find compiled JS
        """
        raise NotImplementedError("Node.js adapter is a stub")

    async def attach(self, config: AttachConfig | Any, **kwargs: Any) -> None:
        """Attach to a running Node.js process.

        Node supports attaching via:
        - Inspector port (--inspect=<port>)
        - Process ID (requires --inspect on start)
        """
        raise NotImplementedError("Node.js adapter is a stub")

    async def disconnect(self, terminate: bool = False) -> None:
        raise NotImplementedError("Node.js adapter is a stub")

    async def terminate(self) -> None:
        raise NotImplementedError("Node.js adapter is a stub")

    async def set_breakpoints(
        self,
        source_path: str,
        breakpoints: list[SourceBreakpoint],
    ) -> list[Breakpoint]:
        raise NotImplementedError("Node.js adapter is a stub")

    async def set_function_breakpoints(self, names: list[str]) -> list[Breakpoint]:
        raise NotImplementedError("Node.js adapter is a stub")

    async def set_exception_breakpoints(self, filters: list[str]) -> None:
        """Configure exception breakpoints.

        Node.js exception filters:
        - "all": Break on all exceptions
        - "uncaught": Break on uncaught exceptions
        """
        raise NotImplementedError("Node.js adapter is a stub")

    async def continue_execution(self, thread_id: int | None = None) -> None:
        raise NotImplementedError("Node.js adapter is a stub")

    async def pause(self, thread_id: int | None = None) -> None:
        raise NotImplementedError("Node.js adapter is a stub")

    async def step_over(self, thread_id: int | None = None) -> None:
        raise NotImplementedError("Node.js adapter is a stub")

    async def step_into(self, thread_id: int | None = None) -> None:
        raise NotImplementedError("Node.js adapter is a stub")

    async def step_out(self, thread_id: int | None = None) -> None:
        raise NotImplementedError("Node.js adapter is a stub")

    async def get_threads(self) -> list[Thread]:
        raise NotImplementedError("Node.js adapter is a stub")

    async def get_stack_trace(
        self,
        thread_id: int,
        start_frame: int = 0,
        levels: int = 20,
    ) -> list[StackFrame]:
        raise NotImplementedError("Node.js adapter is a stub")

    async def get_scopes(self, frame_id: int) -> list[Scope]:
        raise NotImplementedError("Node.js adapter is a stub")

    async def get_variables(
        self,
        variables_reference: int,
        start: int = 0,
        count: int = 0,
    ) -> list[Variable]:
        raise NotImplementedError("Node.js adapter is a stub")

    async def evaluate(
        self,
        expression: str,
        frame_id: int | None = None,
        context: str = "repl",
    ) -> dict[str, Any]:
        raise NotImplementedError("Node.js adapter is a stub")
