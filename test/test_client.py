import asyncio
from fastmcp import Client

async def main():
    # Connect with MCP server
    async with Client("http://localhost:3000/sse") as client:

        # Call the "tool/add" tool        
        a: int = 50
        b: int = 5
        print(f"Testing 'add' MCP tool with following values: a={a} b={b}")
        add_result: list = await client.call_tool("add", {"a": a, "b": b})
        assert str(a + b) == add_result[0].text
        print("'add' test passed")
        
        # Call the "tool/to_upper" tool        
        to_upper_text: str = "hello"
        print(f"Testing 'to_upper' MCP tool with following values: text={to_upper_text}")
        to_upper_result: list = await client.call_tool("to_upper", {"text": to_upper_text})
        assert to_upper_text.upper() == to_upper_result[0].text
        print("'to_upper' test passed")


        # Call the "tool/message_length" tool        
        example_text: str = """
        This is a test text.
        It contains multiple lines.
        The length of this text will be calculated.
        """
        print(f"Testing 'message_length' MCP tool with following values: text={example_text}")
        length: list = await client.call_tool("message_length", {"message": example_text})
        assert str(len(example_text)) == length[0].text
        print("'message_length' test passed")

        # Call the "tool/parse" tool        
        print(f"Testing 'parse' MCP tool with following values: text={example_text}")
        parse_result: list = await client.call_tool("parse", {"message": example_text})
        assert example_text == parse_result[0].text
        print("'parse' test passed")

        # Call the "tool/execute_shell" tool        
        shell_command_content: str = "hello\n"
        shell_command: str = f"echo {shell_command_content}"
        print(f"Testing 'execute_shell' MCP tool with following values: text={shell_command}")
        exec_shell_result: list = await client.call_tool("execute_shell", {"command": shell_command})
        assert shell_command_content == exec_shell_result[0].text
        print("'execute_shell' test passed")
 
        # Call the "tool/execute" tool  
        command_content: str = "hello"
        command: str = f"print(\"{command_content}\")"
        print(f"Testing 'execute' MCP tool with following values: text={command}")
        exec_result = await client.call_tool("execute", {"code": command})
        assert (command_content + '\n') == exec_result[0].text
        print("'execute' test passed")

        print("All tests passed")

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())
