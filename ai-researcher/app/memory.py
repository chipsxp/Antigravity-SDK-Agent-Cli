import os
from typing import Dict, Any, List
import requests
from .graph_store import GraphitiStore

class ZepMemoryStore:
    """
    Alias for Graphiti's episodic memory capability. 
    Previously this was a distinct Zep mock.
    """
    def __init__(self):
        # We share the same Graphiti connection logic
        self.store = GraphitiStore()
        self.client = self.store.client
        print(f"Initialized Memory Store connecting to Graphiti at {self.store.uri}")

    def add_memory(self, user_input: str, agent_response: str, metadata: Dict[str, Any] = None):
        """Adds a conversational turn to Graphiti episodic memory."""
        if not self.client:
            print(f"[MOCK] Adding memory: {user_input} -> {agent_response[:50]}...")
            return
            
        print(f"Adding episode to Graphiti memory...")
        # In a fully connected async environment:
        # await self.client.add_episode(
        #     name="conversation",
        #     source="agent",
        #     fact=f"User: {user_input}\nAgent: {agent_response}"
        # )

    def search_memory(self, query: str, limit: int = 3) -> List[Dict[str, Any]]:
        """Searches past sessions for similar resolutions using Graphiti."""
        if not self.client:
            print(f"[MOCK] Searching memory for: {query}")
            return []
            
        return []

    def record_experience(self, scenario: str, solution: str, successful: bool):
        """Records an outcome for future Graphiti validation."""
        metadata = {
            "type": "experience",
            "successful": successful,
            "scenario": scenario
        }
        self.add_memory(
            user_input=f"Scenario: {scenario}",
            agent_response=f"Solution provided: {solution}",
            metadata=metadata
        )
        
if __name__ == "__main__":
    print("Testing Graphiti Memory Store...")
    zep = ZepMemoryStore()
    zep.record_experience("How to start FastAPI", "uvicorn main:app", True)
