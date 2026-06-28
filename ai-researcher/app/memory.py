import sys, builtins
__print = builtins.print
def print(*args, **kwargs):
    kwargs['file'] = sys.stderr
    __print(*args, **kwargs)

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

    async def add_memory(self, user_input: str, agent_response: str, metadata: Dict[str, Any] = None):
        """Adds a conversational turn to Graphiti episodic memory."""
        if not self.client:
            print(f"[MOCK] Adding memory: {user_input} -> {agent_response[:50]}...")
            return
            
        print(f"Adding episode to Graphiti memory...")
        from graphiti_core.nodes import EpisodeType
        import datetime
        from datetime import timezone
        import uuid
        
        await self.client.add_episode(
            name=f"conversation_{uuid.uuid4().hex[:8]}",
            episode_body=f"User: {user_input}\nAgent: {agent_response}",
            source=EpisodeType.message,
            reference_time=datetime.datetime.now(timezone.utc),
            source_description="Agent memory"
        )

    def search_memory(self, query: str, limit: int = 3) -> List[Dict[str, Any]]:
        """Searches past sessions for similar resolutions using Graphiti."""
        if not self.client:
            print(f"[MOCK] Searching memory for: {query}")
            return []
            
        return []

    async def record_experience(self, scenario: str, solution: str, successful: bool):
        """Records an outcome for future Graphiti validation."""
        metadata = {
            "type": "experience",
            "successful": successful,
            "scenario": scenario
        }
        await self.add_memory(
            user_input=f"Scenario: {scenario}",
            agent_response=f"Solution provided: {solution}",
            metadata=metadata
        )
        
if __name__ == "__main__":
    print("Testing Graphiti Memory Store...")
    zep = ZepMemoryStore()
    zep.record_experience("How to start FastAPI", "uvicorn main:app", True)
