# OpenCode Debug Relay Server

An HTTP relay server that enables AI coding agents to perform full interactive debugging of Python applications via debugpy/DAP (Debug Adapter Protocol).

## Features

- **Full debugging capabilities** - Set breakpoints, step through code, inspect variables
- **REST API** - Simple HTTP/JSON interface for AI agents
- **Multiple sessions** - Support up to 10 concurrent debug sessions
- **Breakpoint persistence** - Breakpoints are saved per-project
- **Output capture** - Capture stdout/stderr with 50MB buffer
- **Polling-based events** - No WebSocket required

## Installation

```bash
# Clone the repository
git clone https://github.com/opencode/opencode-debugger.git
cd opencode-debugger

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install the package
pip install -e ".[dev]"
```

## Quick Start

### Start the Server

```bash
# Start with default settings (localhost:5679)
opencode-debugger

# Or with uvicorn directly
uvicorn opencode_debugger.main:app --reload
```

### Basic Debug Session

```bash
# 1. Create a session
curl -X POST http://localhost:5679/api/v1/sessions \
  -H "Content-Type: application/json" \
  -d '{"project_root": "/path/to/your/project"}'

# Response: {"id": "sess_abc12345", "state": "created", ...}

# 2. Set a breakpoint
curl -X POST http://localhost:5679/api/v1/sessions/sess_abc12345/breakpoints \
  -H "Content-Type: application/json" \
  -d '{"source": "/path/to/your/script.py", "breakpoints": [{"line": 10}]}'

# 3. Launch the program
curl -X POST http://localhost:5679/api/v1/sessions/sess_abc12345/launch \
  -H "Content-Type: application/json" \
  -d '{"program": "/path/to/your/script.py"}'

# 4. Poll for events (will return when breakpoint is hit)
curl "http://localhost:5679/api/v1/sessions/sess_abc12345/events?timeout=30"

# 5. Get stack trace
curl http://localhost:5679/api/v1/sessions/sess_abc12345/stacktrace

# 6. Get variables
curl "http://localhost:5679/api/v1/sessions/sess_abc12345/scopes?frame_id=0"
curl "http://localhost:5679/api/v1/sessions/sess_abc12345/variables?ref=1000"

# 7. Continue execution
curl -X POST http://localhost:5679/api/v1/sessions/sess_abc12345/continue

# 8. Terminate session
curl -X DELETE http://localhost:5679/api/v1/sessions/sess_abc12345
```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:5679/docs
- ReDoc: http://localhost:5679/redoc
- OpenAPI JSON: http://localhost:5679/openapi.json

## API Endpoints

### Sessions
- `POST /api/v1/sessions` - Create a new debug session
- `GET /api/v1/sessions` - List all sessions
- `GET /api/v1/sessions/{id}` - Get session details
- `DELETE /api/v1/sessions/{id}` - Terminate a session

### Program Control
- `POST /api/v1/sessions/{id}/launch` - Launch a program
- `POST /api/v1/sessions/{id}/attach` - Attach to a running process

### Breakpoints
- `POST /api/v1/sessions/{id}/breakpoints` - Set breakpoints for a file
- `GET /api/v1/sessions/{id}/breakpoints` - List all breakpoints
- `DELETE /api/v1/sessions/{id}/breakpoints` - Clear all breakpoints

### Execution Control
- `POST /api/v1/sessions/{id}/continue` - Continue execution
- `POST /api/v1/sessions/{id}/pause` - Pause execution
- `POST /api/v1/sessions/{id}/step-over` - Step to next line
- `POST /api/v1/sessions/{id}/step-into` - Step into function
- `POST /api/v1/sessions/{id}/step-out` - Step out of function

### Inspection
- `GET /api/v1/sessions/{id}/threads` - List threads
- `GET /api/v1/sessions/{id}/stacktrace` - Get stack trace
- `GET /api/v1/sessions/{id}/scopes` - Get variable scopes
- `GET /api/v1/sessions/{id}/variables` - Get variables
- `POST /api/v1/sessions/{id}/evaluate` - Evaluate expression

### Output
- `GET /api/v1/sessions/{id}/output` - Get captured output
- `GET /api/v1/sessions/{id}/events` - Poll for debug events

### Server
- `GET /api/v1/health` - Health check
- `GET /api/v1/info` - Server info

## Configuration

Environment variables (prefix with `OPENCODE_DEBUG_`):

| Variable | Default | Description |
|----------|---------|-------------|
| `HOST` | `127.0.0.1` | Server bind address |
| `PORT` | `5679` | Server port |
| `MAX_SESSIONS` | `10` | Maximum concurrent sessions |
| `SESSION_TIMEOUT_SECONDS` | `3600` | Session idle timeout |
| `OUTPUT_BUFFER_MAX_BYTES` | `52428800` | Output buffer size (50MB) |
| `DATA_DIR` | `~/.opencode-debugger` | Data directory |
| `LOG_LEVEL` | `INFO` | Log level |

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=opencode_debugger --cov-report=html

# Type checking
mypy src/opencode_debugger

# Linting
ruff check src tests
ruff format src tests
```

## Architecture

```
┌─────────────┐     HTTP/JSON      ┌─────────────────┐     DAP      ┌──────────┐
│  AI Agent   │ <----------------> │  Debug Relay    │ <----------> │  debugpy │
│  (Claude)   │                    │  Server         │              │          │
└─────────────┘                    └─────────────────┘              └──────────┘
```

The relay server:
1. Receives HTTP requests from AI agents
2. Translates them to DAP protocol messages
3. Communicates with debugpy subprocess
4. Returns results as JSON responses

## OpenCode Integration

This project includes OpenCode agent skill and plugin packages for seamless integration with OpenCode AI coding agents.

### Agent Skill

The skill provides instructions and API documentation for agents to debug Python code.

**Installation:**
```bash
# Project-level
mkdir -p .opencode/skill/python-debug
cp packages/skill-python-debug/SKILL.md .opencode/skill/python-debug/

# Or global
mkdir -p ~/.config/opencode/skill/python-debug
cp packages/skill-python-debug/SKILL.md ~/.config/opencode/skill/python-debug/
```

### Plugin

The plugin provides custom tools (`debug-*`) that agents can call directly.

**Installation (local):**
```bash
# Project-level
mkdir -p .opencode/plugin
cp packages/plugin-python-debugger/index.ts .opencode/plugin/python-debugger.ts

# Create package.json for dependencies
echo '{"dependencies": {"@opencode-ai/plugin": "latest"}}' > .opencode/package.json
```

**Installation (npm - when published):**
```json
{
  "plugin": ["opencode-python-debugger"]
}
```

### Available Tools (Plugin)

| Tool | Description |
|------|-------------|
| `debug-session-create` | Create a new debug session |
| `debug-sessions` | List all active sessions |
| `debug-launch` | Launch a program in debug mode |
| `debug-breakpoints` | Set breakpoints in a file |
| `debug-continue` | Continue execution |
| `debug-step-over` | Step to next line |
| `debug-step-into` | Step into function |
| `debug-step-out` | Step out of function |
| `debug-status` | Get session state and events |
| `debug-stacktrace` | Get call stack |
| `debug-variables` | Get variables in scope |
| `debug-evaluate` | Evaluate expression |
| `debug-output` | Get program output |
| `debug-terminate` | Terminate session |

## License

MIT License
