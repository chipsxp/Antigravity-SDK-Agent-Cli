from typing import Dict, Any, List

class DocumentChunk:
    def __init__(self, metadata: Dict[str, Any], content: str, embedding: List[float] = None):
        self.metadata = metadata
        self.content = content
        self.embedding = embedding
