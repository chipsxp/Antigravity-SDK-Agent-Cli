import sys, builtins
__print = builtins.print
def print(*args, **kwargs):
    kwargs['file'] = sys.stderr
    __print(*args, **kwargs)

import os
import glob
from typing import List, Dict, Any
import google.generativeai as genai

from .graph_store import GraphitiStore
from .memory import ZepMemoryStore
from .models import DocumentChunk

# Setup Gemini API key
# Expects GEMINI_API_KEY environment variable to be set
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def simple_markdown_chunker(text: str, max_chunk_size: int = 1000) -> List[str]:
    """
    A very simple chunker that splits by double newlines (paragraphs) 
    and groups them up to max_chunk_size.
    """
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = ""
    
    for para in paragraphs:
        if len(current_chunk) + len(para) > max_chunk_size and current_chunk:
            chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"
        else:
            current_chunk += para + "\n\n"
            
    if current_chunk:
        chunks.append(current_chunk.strip())
        
    return chunks

class IngestionPipeline:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        # We use a Gemini embedding model
        self.embedding_model = "models/text-embedding-004"
        
        try:
            self.graph_store = GraphitiStore()
            self.graph_store.setup_schema()
            self.memory_store = ZepMemoryStore()
        except Exception as e:
            print(f"Warning: Could not initialize backing stores during ingestion setup. {e}")
            self.graph_store = None
            self.memory_store = None
        
    def load_documents(self) -> List[DocumentChunk]:
        """Loads all markdown and text documents from the data directory."""
        files = []
        for ext in ("*.md", "*.txt"):
            search_pattern = os.path.join(self.data_dir, f"**/{ext}")
            files.extend(glob.glob(search_pattern, recursive=True))
        
        all_chunks = []
        for file_path in files:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            filename = os.path.basename(file_path)
            
            # Chunk the document
            text_chunks = simple_markdown_chunker(content)
            
            for i, chunk_text in enumerate(text_chunks):
                chunk = DocumentChunk(
                    metadata={"source": filename, "chunk_index": i},
                    content=chunk_text
                )
                all_chunks.append(chunk)
                
        return all_chunks
        
    async def process_all(self) -> List[DocumentChunk]:
        """Runs the full ingestion and embedding pipeline using Graphiti."""
        print(f"Loading documents from {self.data_dir}...")
        chunks = self.load_documents()
        
        if not chunks:
            print("No documents found to ingest.")
            return []
            
        print(f"Loaded {len(chunks)} chunks. Storing chunks directly into Neo4j Graph Store (Graphiti handles extraction and embedding)...")
        if self.graph_store:
            await self.graph_store.store_chunks(chunks)
            
        if self.memory_store:
            print("Recording ingestion event in memory...")
            await self.memory_store.add_memory(
                user_input=f"Ingest documents from {self.data_dir}",
                agent_response=f"Successfully ingested {len(chunks)} chunks.",
                metadata={"type": "ingestion_event", "chunk_count": len(chunks)}
            )
            
        return chunks

def get_library_path() -> str:
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    default_path = os.path.join(current_dir, "data")
    
    # Do NOT use input() here because it breaks MCP stdio communication
    env_path = os.environ.get("DOCUMENT_LIBRARY_PATH")
    if env_path:
        return env_path
    
    return default_path

if __name__ == "__main__":
    # Test the pipeline
    data_dir = get_library_path()
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)
        print(f"Created library directory at {data_dir}. Please place markdown files there.")
        
    pipeline = IngestionPipeline(data_dir=data_dir)
    import asyncio
    chunks = asyncio.run(pipeline.process_all())
    
    for c in chunks:
        print(f"Chunk from {c.metadata['source']} (length: {len(c.content)})")
