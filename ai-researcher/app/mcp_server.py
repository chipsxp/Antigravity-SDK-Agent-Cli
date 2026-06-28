import asyncio
from mcp.server.fastmcp import FastMCP
from .agent import app as researcher_app

# Create the FastMCP Server
mcp = FastMCP("AI_Researcher_Deep_Agent")

import sys
from google.adk.runners import InMemoryRunner

@mcp.tool()
async def ask_researcher(query: str) -> str:
    """
    Ask the AI Document Library Researcher a question about a framework or coding scenario.
    The researcher will query its Neo4j knowledge graph and its Zep memory to provide a detailed, validated solution.
    """
    print(f"[MCP Server] Received query for AI Researcher: {query}", file=sys.stderr)
    
    try:
        from google.genai import types
        # Run the ADK Agent via InMemoryRunner's run_debug helper
        runner = InMemoryRunner(app=researcher_app)
        response_text = ""
        
        events = await runner.run_debug(query, quiet=True)
        for event in events:
            if getattr(event, 'content', None):
                if hasattr(event.content, 'parts') and event.content.parts:
                    for part in event.content.parts:
                        if hasattr(part, 'text') and part.text:
                            response_text += part.text
                else:
                    response_text += str(event.content)
                
        return response_text
    except Exception as e:
        return f"The AI Researcher encountered an error processing your query: {e}"

@mcp.tool()
async def trigger_ingestion() -> str:
    """
    Triggers the AI Researcher to re-ingest markdown documents from the data directory into its Neo4j graph.
    """
    print("[MCP Server] Triggering document ingestion pipeline...", file=sys.stderr)
    try:
        from .ingestion import IngestionPipeline, get_library_path
        
        data_dir = get_library_path()
        pipeline = IngestionPipeline(data_dir=data_dir)
        chunks = await pipeline.process_all()
        
        return f"Successfully ingested {len(chunks)} chunks into Neo4j and Zep memory."
    except Exception as e:
        return f"Failed to ingest documents: {e}"

if __name__ == "__main__":
    # print to stderr if needed, or don't print
    mcp.run()
