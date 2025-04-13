import asyncio
from fastmcp import Client

async def main():
    # Connect to your running FastMCP server
    async with Client("http://localhost:3000/sse") as client:
        # Call the "tool/add" tool
        result = await client.call_tool("add", {"a": 69, "b": 5})
        print(result)

        to_upper_result = await client.call_tool("to_upper", {"text": "hello"})
        print(to_upper_result)

        example_text = """
        This is a test text.
        It contains multiple lines.
        The length of this text will be calculated.
        """

        # Call the "tool/message_length" tool
        length = await client.call_tool("message_length", {"message": example_text})
        print(f"Length of the message: {length}")
        
        print(length)

        # Call the "tool/execute" tool
        execute_result = await client.call_tool("execute", {"command": "ls ."})
        print(execute_result)

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())
