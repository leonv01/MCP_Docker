import uvicorn
from mcp.server.fastmcp import FastMCP

from test import get_str_length

mcp = FastMCP("docker-mcp")
app = mcp.sse_app()

# Define a simple function called 'add' to be used with the MCP
@mcp.tool("add")
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool("to_upper")
def to_upper(text: str) -> str:
    """Convert text to uppercase"""
    return text.upper()

@mcp.tool("execute")
def execute(command: str) -> str:
    """Execute a shell command"""
    import subprocess
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

@mcp.tool("message_length")
def print_message(message: str) -> None:
    """Print the length of a message"""
    return get_str_length(message)

@mcp.tool("parse")
def parse_esalqi(message: str) -> None:
    """Parse a code sequence"""
    # call parser
    return message

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=3000, reload=True)
