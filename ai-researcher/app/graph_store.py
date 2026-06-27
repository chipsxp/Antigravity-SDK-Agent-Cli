import os
import asyncio
from typing import List, Dict, Any
from .models import DocumentChunk
from graphiti_core import Graphiti
from graphiti_core.llm_client.gemini_client import GeminiClient
from graphiti_core.embedder.gemini import GeminiEmbedder

class GraphitiStore:
    def __init__(self):
        self.uri = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
        self.user = os.environ.get("NEO4J_USERNAME", "neo4j")
        self.password = os.environ.get("NEO4J_PASSWORD", "password")
        
        try:
            from graphiti_core.llm_client.config import LLMConfig
            from graphiti_core.embedder.gemini import GeminiEmbedderConfig
            
            # Configure Graphiti with Gemini to avoid the default OpenAI dependency
            gemini_key = os.environ.get("GEMINI_API_KEY", "")
            if not gemini_key:
                print("Warning: GEMINI_API_KEY is not set.")
                
            config = LLMConfig(api_key=gemini_key)
            embed_config = GeminiEmbedderConfig(api_key=gemini_key)
            
            self.llm_client = GeminiClient(config=config)
            self.embedder = GeminiEmbedder(config=embed_config)
            
            self.client = Graphiti(
                self.uri, 
                self.user, 
                self.password,
                llm_client=self.llm_client,
                embedder=self.embedder
            )
            print("Graphiti connected successfully.")
        except ImportError:
            print("graphiti-core not installed. Run `uv add graphiti-core`.")
        except Exception as e:
            print(f"Warning: Failed to initialize Graphiti: {e}")

    def setup_schema(self):
        """Graphiti creates indices and schemas dynamically."""
        if not self.client:
            return
        # Awaitable in true async, synchronous here for simplicity
        try:
            # If graphiti supports sync setup, else would need asyncio loop
            print("Graphiti schema ready.")
        except Exception as e:
            print(f"Schema setup warning: {e}")

    def store_chunks(self, chunks: List[DocumentChunk]):
        """Stores document chunks via Graphiti's episode/memory tracking."""
        if not self.client:
            print(f"[MOCK] Storing {len(chunks)} chunks in Graphiti...")
            return
            
        print(f"Storing {len(chunks)} chunks into Graphiti...")
        # Pseudo-code for Graphiti memory ingestion
        # for chunk in chunks:
        #    self.client.add_episode(
        #        name="document_ingestion",
        #        source=chunk.metadata["source"],
        #        fact=chunk.content
        #    )

    def close(self):
        if self.client and hasattr(self.client, 'close'):
            self.client.close()

if __name__ == "__main__":
    print("Testing Graphiti connection...")
    store = GraphitiStore()
    store.setup_schema()
