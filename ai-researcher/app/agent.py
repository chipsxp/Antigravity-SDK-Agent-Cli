# ruff: noqa
# Copyright 2026 Google LLC

import os
import google.auth

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

from .retrieval import RetrievalEngine
from .graph_store import GraphitiStore
from .memory import ZepMemoryStore

# Initialize backing stores
try:
    graph_store = GraphitiStore()
    retrieval_engine = RetrievalEngine(graph_store)
    memory_store = ZepMemoryStore()
except Exception as e:
    print(f"Warning: Backing stores not initialized. Ensure environment variables are set. {e}")
    # Still creating dummies so the agent file can be loaded by tools
    graph_store = None
    retrieval_engine = None
    memory_store = None

def query_library_framework(query: str) -> str:
    """
    Searches the developer's framework library (stored in Neo4j) for information.
    Use this tool when you need to understand how a framework works or find documentation.
    """
    if not retrieval_engine: return "Database connection error."
    results = retrieval_engine.graph_rag_search(query)
    
    if not results.get("best_match_chunk"):
        return "No relevant framework documentation found."
        
    context = results.get("full_document_context", "")
    return f"Found documentation context:\n\n{context}"

def recall_past_experience(scenario: str) -> str:
    """
    Searches the Zep memory store for past solutions and experiences related to a scenario.
    Use this tool to see if you have solved a similar problem before.
    """
    if not memory_store: return "Database connection error."
    results = memory_store.search_memory(scenario)
    if not results:
        return "No past experience found for this scenario."
        
    formatted = [f"Past experience: {r.get('content')} (Metadata: {r.get('metadata')})" for r in results]
    return "\n\n".join(formatted)

def record_solution_outcome(scenario: str, solution: str, successful: bool) -> str:
    """
    Records an experience into the Zep memory store for future Graphiti validation.
    Use this tool after you provide a solution to track its outcome.
    """
    if not memory_store: return "Database connection error."
    memory_store.record_experience(scenario, solution, successful)
    return "Successfully recorded experience to memory."


root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model="gemini-flash-latest",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=(
        "You are an AI Document Library Researcher. "
        "Your goal is to help the developer match scenarios with solutions by "
        "absorbing documentation from a scraped framework library and recalling past experiences. "
        "When asked a question, you should first check `recall_past_experience` to see if a solution exists. "
        "If not, use `query_library_framework` to find the relevant documentation. "
        "Once a solution is found and verified, you MUST use `record_solution_outcome` to record it."
    ),
    tools=[query_library_framework, recall_past_experience, record_solution_outcome],
)

app = App(
    root_agent=root_agent,
    name="app",
)
