# python-mcp-nrepl

# Usage

## Install

```bash
pdm install
ln -s $(pdm run which mcp-nrepl) ~/.local/bin/
```

If you haven't configure `$PATH` to `~/.local/bin/`, you should add your bashrc.

```bash
PATH="$HOME/.local/bin:$PATH"
```

## Configure MCP client
Add below config for `claude_desktop_config.json`.

```json
{
    "mcpServers": {
        "nrepl": {
            "command": "mcp-nrepl"
        }
    }
}
```

# Development

## Run (develop)
```bash
pdm run mcp-nrepl
```

## NixOS tips

### pdm fails missing virtualenv
`pdm` uses `virtualenv` to create virtual env but Python which installed by NixOS don't have it, pdm fails.

ref: https://github.com/NixOS/nixpkgs/issues/225730

```bash
pdm config venv.backend venv
```
