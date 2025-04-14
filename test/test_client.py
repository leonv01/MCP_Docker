import asyncio
from fastmcp import Client

async def main():
    # Connect to your running FastMCP server
    async with Client("http://localhost:3000/sse") as client:
        # Call the "tool/add" tool
        result = await client.call_tool("add", {"a": 50, "b": 5})
        assert '55' == result[0].text
        

        to_upper_result = await client.call_tool("to_upper", {"text": "hello"})
        assert 'HELLO' == to_upper_result[0].text

        example_text = """
        This is a test text.
        It contains multiple lines.
        The length of this text will be calculated.
        """

        # Call the "tool/message_length" tool
        length = await client.call_tool("message_length", {"message": example_text})
        assert '126' == length[0].text

        # Call the "tool/execute" tool
        parse_result = await client.call_tool("parse", {"message": example_text})
        assert example_text == parse_result[0].text

        exec_shell_result = await client.call_tool("execute_shell", {"command": "ls ."})
        print(exec_shell_result[0].text)
 
        exec_result = await client.call_tool("execute", {"code": "for i in range(3): print(i)"})
        print(exec_result[0].text)
        #assert "hello" == exec_result[0].text
        print("All tests passed")

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())
