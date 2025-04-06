import nrepl
import mcp.server.fastmcp

app = mcp.server.fastmcp.FastMCP("mcp-nrepl")

@app.tool()
def action_nrepl(host: str, port: int, code: str) -> str:
    nrepl_connection = nrepl.connect(f"nrepl://{host}:{port}")
    nrepl_connection.write(
        {
            "op": "eval",
            "code": code,
        }
    )
    return nrepl_connection.read()

def main():
    app.run()

if __name__ == '__main__':
    main()
