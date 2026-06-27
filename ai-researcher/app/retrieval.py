from typing import List, Dict, Any
from .graph_store import GraphitiStore
import google.generativeai as genai
import os

class RetrievalEngine:
    def __init__(self, graph_store: GraphitiStore):
        self.store = graph_store
        self.embedding_model = "models/text-embedding-004"
        genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
        
    def _get_embedding(self, query: str) -> List[float]:
        result = genai.embed_content(
            model=self.embedding_model,
            content=query,
            task_type="retrieval_query"
        )
        return result["embedding"]

    def vector_search(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Performs a semantic vector search across the stored chunks."""
        query_embedding = self._get_embedding(query)
        
        with self.store.driver.session() as session:
            result = session.run("""
            CALL db.index.vector.queryNodes('document_chunk_index', $top_k, $embedding)
            YIELD node, score
            MATCH (d:Document)-[:HAS_CHUNK]->(node)
            RETURN node.text AS text, node.index AS index, d.name AS document, score
            """, top_k=top_k, embedding=query_embedding)
            
            records = []
            for record in result:
                records.append({
                    "text": record["text"],
                    "document": record["document"],
                    "chunk_index": record["index"],
                    "score": record["score"]
                })
            return records

    def graph_rag_search(self, query: str) -> Dict[str, Any]:
        """
        An advanced query that combines vector search and extracts neighboring nodes
        (like other chunks from the same document) to provide larger context.
        """
        # First, find the best matching chunk
        vector_results = self.vector_search(query, top_k=1)
        if not vector_results:
            return {"results": []}
            
        best_match = vector_results[0]
        
        # Then, get the full document context (or adjacent chunks)
        with self.store.driver.session() as session:
            result = session.run("""
            MATCH (d:Document {name: $doc_name})-[:HAS_CHUNK]->(c:Chunk)
            RETURN c.text AS text, c.index AS index
            ORDER BY c.index
            """, doc_name=best_match["document"])
            
            full_context = [record["text"] for record in result]
            
        return {
            "best_match_chunk": best_match,
            "full_document_context": "\n\n".join(full_context)
        }

if __name__ == "__main__":
    print("Testing Retrieval Engine...")
    store = GraphitiStore()
    engine = RetrievalEngine(store)
    print("Engine instantiated.")
    # engine.vector_search("How do I use FastAPI?")
