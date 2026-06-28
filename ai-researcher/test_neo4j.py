import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

uri = os.environ.get("NEO4J_URI")
user = os.environ.get("NEO4J_USERNAME")
password = os.environ.get("NEO4J_PASSWORD")

print(f"Testing connection to {uri} as user {user}...")

try:
    driver = GraphDatabase.driver(uri, auth=(user, password))
    driver.verify_connectivity()
    print("Connection successful!")
    driver.close()
except Exception as e:
    print(f"Connection failed: {e}")

# Now test with 'neo4j' user
print(f"\nTesting connection to {uri} as user 'neo4j'...")
try:
    driver2 = GraphDatabase.driver(uri, auth=("neo4j", password))
    driver2.verify_connectivity()
    print("Connection successful with user 'neo4j'!")
    driver2.close()
except Exception as e:
    print(f"Connection failed: {e}")
