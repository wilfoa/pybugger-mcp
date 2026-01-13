"""Debug Adapter Protocol (DAP) models."""

from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field


class DAPMessage(BaseModel):
    """Base DAP message."""

    seq: int
    type: str


class DAPRequest(DAPMessage):
    """DAP request message."""

    type: str = "request"
    command: str
    arguments: dict[str, Any] = Field(default_factory=dict)


class DAPResponse(DAPMessage):
    """DAP response message."""

    type: str = "response"
    request_seq: int
    success: bool
    command: str
    message: Optional[str] = None
    body: dict[str, Any] = Field(default_factory=dict)


class DAPEvent(DAPMessage):
    """DAP event message."""

    type: str = "event"
    event: str
    body: dict[str, Any] = Field(default_factory=dict)


class LaunchConfig(BaseModel):
    """Configuration for launching a debug target."""

    program: Optional[str] = None
    module: Optional[str] = None  # Alternative to program (e.g., "pytest")
    args: list[str] = Field(default_factory=list)
    python_args: list[str] = Field(default_factory=list)  # Args to Python interpreter
    cwd: str = "."
    env: dict[str, str] = Field(default_factory=dict)
    python_path: Optional[str] = None
    stop_on_entry: bool = False
    stop_on_exception: bool = True
    console: str = "internalConsole"  # internalConsole, integratedTerminal, externalTerminal


class AttachConfig(BaseModel):
    """Configuration for attaching to a process."""

    process_id: Optional[int] = None
    host: str = "localhost"
    port: int = 5678


class SourceBreakpoint(BaseModel):
    """Breakpoint definition for a source file."""

    line: int
    column: Optional[int] = None
    condition: Optional[str] = None
    hit_condition: Optional[str] = None
    log_message: Optional[str] = None
    enabled: bool = True


class Breakpoint(BaseModel):
    """Verified breakpoint from debugpy."""

    id: Optional[int] = None
    verified: bool
    line: Optional[int] = None
    column: Optional[int] = None
    message: Optional[str] = None
    source: Optional[dict[str, Any]] = None


class Source(BaseModel):
    """Source file information."""

    name: Optional[str] = None
    path: Optional[str] = None
    source_reference: Optional[int] = Field(None, alias="sourceReference")

    class Config:
        populate_by_name = True


class StackFrame(BaseModel):
    """Stack frame information."""

    id: int
    name: str
    source: Optional[Source] = None
    line: int
    column: int = 0
    end_line: Optional[int] = Field(None, alias="endLine")
    end_column: Optional[int] = Field(None, alias="endColumn")
    module_id: Optional[str] = Field(None, alias="moduleId")

    class Config:
        populate_by_name = True


class Scope(BaseModel):
    """Variable scope."""

    name: str
    presentation_hint: Optional[str] = Field(None, alias="presentationHint")
    variables_reference: int = Field(alias="variablesReference")
    named_variables: Optional[int] = Field(None, alias="namedVariables")
    indexed_variables: Optional[int] = Field(None, alias="indexedVariables")
    expensive: bool = False

    class Config:
        populate_by_name = True


class Variable(BaseModel):
    """Variable information."""

    name: str
    value: str
    type: Optional[str] = None
    variables_reference: int = Field(0, alias="variablesReference")
    named_variables: Optional[int] = Field(None, alias="namedVariables")
    indexed_variables: Optional[int] = Field(None, alias="indexedVariables")
    evaluate_name: Optional[str] = Field(None, alias="evaluateName")

    class Config:
        populate_by_name = True


class Thread(BaseModel):
    """Thread information."""

    id: int
    name: str


class Module(BaseModel):
    """Module information."""

    id: str | int
    name: str
    path: Optional[str] = None
    version: Optional[str] = None
