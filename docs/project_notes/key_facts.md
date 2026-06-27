# Project Key Facts

### Tech Stack & Services
- **Agent Orchestration:** Google Antigravity (AGY) SDK
- **Knowledge Graph & Memory:** Graphiti (`graphiti-core`)
- **Graph Database:** Neo4j
- **Web Scraping:** Bright Data MCP

### Local Environment Configuration
- **Neo4j Default URI:** `bolt://localhost:7687` (requires Neo4j running locally)
- **Document Ingestion Target:** Local absolute paths pointing to markdown directories.

### Architecture Topology
- **Ingestion Pipeline:** Uses `ingestion.py` to route URLs via Bright Data to Markdown, then embeds and writes into Graphiti's Neo4j schema.
- **Validation Engine:** Exposed over FastMCP in `mcp_server.py`. Can be queried via standard agent harnesses.
