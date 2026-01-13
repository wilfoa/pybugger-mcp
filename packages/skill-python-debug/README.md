# OpenCode Python Debug Skill

An OpenCode agent skill that provides instructions for debugging Python code via the OpenCode Debug Relay Server.

## Installation

Copy the `SKILL.md` file to your OpenCode skills directory:

### Project-level (recommended)
```bash
mkdir -p .opencode/skill/python-debug
cp SKILL.md .opencode/skill/python-debug/
```

### Global installation
```bash
mkdir -p ~/.config/opencode/skill/python-debug
cp SKILL.md ~/.config/opencode/skill/python-debug/
```

## Prerequisites

The OpenCode Debug Relay Server must be running for this skill to work:

```bash
# Install the debug server
pip install opencode-debugger

# Start the server
python -m opencode_debugger.main
```

The server runs on `http://127.0.0.1:5679` by default.

## Usage

Once installed, the skill will be available to OpenCode agents. They can load it when debugging Python code is needed.

The skill provides:
- API endpoint documentation for the debug server
- Step-by-step debugging workflows
- Examples for setting breakpoints, stepping, inspecting variables
- Event types and session state explanations

## What's Included

The skill teaches agents how to:
- Create and manage debug sessions
- Set breakpoints (including conditional breakpoints)
- Control execution (continue, step over/into/out, pause)
- Inspect program state (threads, stack traces, variables)
- Evaluate expressions in the debugger context
- Poll for events and capture program output

## License

MIT
