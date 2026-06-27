import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_mcp_test():
    print("Starting MCP Client Test...")
    
    # Parameters to connect to your local MCP server
    server_params = StdioServerParameters(
        command="uv",
        args=[
            "--directory",
            "C:/Users/Grah/ChipsXP/Git-Repo/antigravity-sdk-python/ai-researcher",
            "run",
            "--env-file",
            ".env",
            "python",
            "-m",
            "app.mcp_server"
        ],
        env=None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("Connected to AI Researcher MCP Server!")
            
            # List available tools
            tools = await session.list_tools()
            print("\nAvailable Tools:")
            for tool in tools.tools:
                print(f"- {tool.name}: {tool.description}")

            # Test trigger_ingestion tool
            print("\nTesting trigger_ingestion tool...")
            try:
                result = await session.call_tool("trigger_ingestion", arguments={})
                print(f"Result: {result.content}")
            except Exception as e:
                print(f"Tool call failed: {e}")

if __name__ == "__main__":
    asyncio.run(run_mcp_test())
