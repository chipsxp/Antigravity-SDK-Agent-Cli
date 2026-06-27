# AI Researcher (MCP Server)

The AI Researcher is a local development Model Context Protocol (MCP) server that ingests SDK documentation into a local Neo4j Graph database and uses Google Gemini to answer coding architecture and structural questions.

> **Note:** This project is explicitly designed for **local development MCP servers**. All Google Cloud (gcloud) Vertex AI integrations and authentication loops have been stripped out to ensure it can run entirely locally without cloud credentials.

## 1. Cloning the Project

```bash
git clone <repository_url>
cd antigravity-sdk-python/ai-researcher
```

## 2. Python Environment Setup (.venv)

This project uses `uv` for dependency management. Create and activate your virtual environment:

```bash
# Create the virtual environment
uv venv

# Activate it (Windows)
.venv\Scripts\activate
# Activate it (macOS/Linux)
source .venv/bin/activate

# Install dependencies
uv sync
```

## 3. Environment Variables (.env)

Create a `.env` file in the root of the `ai-researcher` directory. You will need the following credentials to run the local Neo4j graph and the Gemini agent:

```env
# Gemini configuration (Local AI Studio key, NOT Vertex AI)
GEMINI_API_KEY="your-api-key"

# Neo4j Local Graphiti Database
NEO4J_URI="bolt://localhost:7687"
NEO4J_USERNAME="neo4j"
NEO4J_PASSWORD="your-password"

# Zep Graphiti Memory
ZEP_API_URL="http://localhost:8000"
```

## 4. Connecting to your IDE (MCP Configuration)

To expose the AI Researcher directly inside your Antigravity IDE (or Claude Desktop / Cursor), add the following JSON block to your global IDE `mcp.json` settings:

```json
{
  "mcpServers": {
    "ai-researcher": {
      "command": "uv",
      "args": [
        "run",
        "--env-file",
        "C:\\absolute\\path\\to\\ai-researcher\\.env",
        "python",
        "C:\\absolute\\path\\to\\ai-researcher\\app\\mcp_server.py"
      ],
      "env": {
        "PYTHONPATH": "C:\\absolute\\path\\to\\ai-researcher"
      }
    }
  }
}
```
*Note: Make sure to replace `C:\\absolute\\path\\to` with your actual filesystem path.*

## 5. Ongoing Development

**Next Dev Task:** This project is undergoing active development. We are currently devising a way for the Agent Code Editor to recall the AI Researcher repetitively via a hook or prompt to autonomously validate code and structural changes against the ingested documents and past Zep Graphiti experiences.
