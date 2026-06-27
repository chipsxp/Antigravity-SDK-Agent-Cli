# Architectural Decision Records

### ADR-001: Use Graphiti-Core for Neo4j Integration (2026-06-25)

**Context:**
- Need a robust temporal knowledge graph and memory layer backed by Neo4j.
- Initially planned to use `zep-python` and mock graph stores.

**Decision:**
- Use the official `graphiti-core` Python SDK.

**Alternatives Considered:**
- Manual Neo4j node/edge tracking → Rejected: too complex to maintain bi-temporal schemas manually.
- Standard Zep vector store → Rejected: doesn't leverage the full temporal capabilities of Graphiti.

**Consequences:**
- ✅ Automatic extraction of nodes and edges.
- ✅ Handles temporal context (valid_at, invalid_at).
- ❌ Requires ensuring the environment matches the Graphiti dependencies exactly.

### ADR-002: Use Bright Data MCP for Web Scraping (2026-06-25)

**Context:**
- Need to ingest live SDK documentation and frameworks into the agent's knowledge base.

**Decision:**
- Integrate the Bright Data MCP server for scraping URLs into LLM-optimized Markdown.

**Alternatives Considered:**
- Custom Python scraping with BeautifulSoup → Rejected: prone to bot-blocking and formatting issues.
- Third-party APIs like Jina Reader → Rejected: Bright Data MCP provides deep integration with our existing agent harness tools.

**Consequences:**
- ✅ Direct Markdown output ready for chunking and ingestion.
- ❌ Requires `PRO_MODE=true` and an API token.

### ADR-003: Expose ADK Agent via MCP using InMemoryRunner.run_debug (2026-06-27)

**Context:**
- We need to expose the AI Researcher agent to external clients (like Claude Desktop or the IDE harness) via the Model Context Protocol (MCP).
- ADK Agents do not have a generic `.run()` method; they require a Session and an Event Runner to stream results asynchronously, which adds heavy boilerplate to synchronous server tools.

**Decision:**
- Wrap the ADK Agent inside an MCP Server (`FastMCP`), utilizing `InMemoryRunner.run_debug(query)` as the execution bridge.
- Strictly redirect all diagnostic output (e.g. `print`) to `sys.stderr` to prevent JSON-RPC protocol corruption over standard I/O.

**Alternatives Considered:**
- Deploy via Google Cloud Run with A2A (Agent-to-Agent) endpoints → Rejected: Too heavy for local iteration and testing.
- Manual `InMemoryRunner.run_async` streaming → Rejected: Requires manually composing `types.Content` objects and managing session IDs boilerplate just for a simple synchronous tool bridge.

**Consequences:**
- ✅ Exposes the full agent reasoning loop via standard MCP protocol.
- ✅ `run_debug` abstracts all session management, making the MCP tool code extremely concise.
- ❌ Raw text extraction is required (`event.content.parts[0].text`) to strip binary thought signatures from the Gemini API before returning to the MCP client.
