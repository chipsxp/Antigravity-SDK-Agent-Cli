# Local LLM Migration Plan for Graphiti (Ollama / LM Studio)

## Background
The Gemini API rate limits (15 RPM) proved too restrictive for bulk ingestion of the markdown library (which generated nearly 3,000 chunks). To bypass this, we are migrating the Graphiti knowledge graph extraction to a local, unrestricted LLM running on a high-powered desktop PC.

## Requirements
1. **Local LLM Server**: Ollama or LM Studio running locally.
2. **Models**: 
   - A large instruction-tuned model for JSON extraction (e.g., `llama3:70b`, `gemma2:27b`, or `qwen2.5`). *Do not use models smaller than 8B as they fail to structure Graphiti JSON properly.*
   - An embedding model (e.g., `nomic-embed-text`).

## Implementation Steps

### 1. Update `graph_store.py`
Swap out the Gemini clients for Graphiti's OpenAI-compatible clients.

```python
from graphiti_core.llm_client.openai_client import OpenAIClient
from graphiti_core.embedder.openai import OpenAIEmbedder
from graphiti_core.llm_client.config import LLMConfig

# Example configuration for local Ollama
config = LLMConfig(
    api_key="ollama", # Dummy key required by OpenAI client
    base_url=os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434/v1"),
    model=os.environ.get("OLLAMA_MODEL", "gemma2")
)

embed_config = LLMConfig(
    api_key="ollama",
    base_url=os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434/v1"),
    model=os.environ.get("OLLAMA_EMBED_MODEL", "nomic-embed-text")
)

self.llm_client = OpenAIClient(config=config)
self.embedder = OpenAIEmbedder(config=embed_config)
```

### 2. Update `.env` File (On the New PC)
Add the local endpoints and update the Neo4j credentials. Ensure you use `neo4j+ssc://` for Neo4j to bypass Windows SSL interception.

```env
OLLAMA_BASE_URL="http://localhost:11434/v1"
OLLAMA_MODEL="gemma2"
OLLAMA_EMBED_MODEL="nomic-embed-text"

# Neo4j configuration from Aura
NEO4J_URI="neo4j+ssc://2eeeb123.databases.neo4j.io"
NEO4J_USERNAME="2eeeb123"
NEO4J_PASSWORD="your-new-password"
```

### 3. Run Ingestion
Trigger the ingestion using the CLI or the `ai-researcher` MCP Server once the local models are loaded into memory.
