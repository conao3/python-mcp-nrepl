# mcp-nrepl

An MCP (Model Context Protocol) server that connects to nREPL servers, enabling AI assistants like Claude to evaluate Clojure code interactively.

## Overview

This server provides a bridge between MCP-compatible clients and nREPL, the standard network REPL protocol used in Clojure development. It allows AI assistants to connect to running Clojure processes and evaluate code in real-time.

## Features

- Connect to any nREPL server by host and port
- Evaluate Clojure code and return results
- Seamless integration with Claude Desktop and other MCP clients

## Requirements

- Python 3.13 or higher
- PDM (Python package manager)
- A running nREPL server to connect to

## Installation

```bash
pdm install
ln -s $(pdm run which mcp-nrepl) ~/.local/bin/
```

If `~/.local/bin` is not in your PATH, add the following to your shell configuration:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

## Configuration

### Claude Desktop

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "nrepl": {
      "command": "mcp-nrepl"
    }
  }
}
```

## Usage

Once configured, the MCP server provides an `action_nrepl` tool that accepts:

- `host`: The nREPL server hostname
- `port`: The nREPL server port
- `code`: The Clojure code to evaluate

The tool connects to the specified nREPL server, evaluates the code, and returns the result.

## Development

Run the server in development mode:

```bash
pdm run mcp-nrepl
```

### NixOS Users

If PDM fails with a missing virtualenv error, configure it to use the built-in venv module instead:

```bash
pdm config venv.backend venv
```

See [NixOS/nixpkgs#225730](https://github.com/NixOS/nixpkgs/issues/225730) for more details.

## License

Apache-2.0
