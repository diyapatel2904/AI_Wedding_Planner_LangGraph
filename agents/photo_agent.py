from loguru import logger
import json
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, PointStruct
from utils.llm_config import llm, emb_client
from state import WeddingState
from langchain_core.messages import HumanMessage, AIMessage


# Configure logger (optional: save logs to file as well)
logger.add("photographer_agent.log", rotation="1 MB", retention="7 days", level="DEBUG")

# # Initialize Qdrant (in-memory; replace with Qdrant URL if needed)
qdrant = QdrantClient(":memory:")

# Connect to Qdrant running in Docker (localhost:6333)
logger.info("Connecting to Qdrant on localhost:6333...")

# qdrant = QdrantClient(url="http://qdrant_db:6333")

# Create collection for photographers
logger.info("Creating collection: photographers")
qdrant.create_collection(
    collection_name="photographers",
    vectors_config=VectorParams(size=1536, distance="Cosine"),
)

# Load and push JSON data into Qdrant
logger.info("Loading photographer JSON data...")
with open("data/photographer.json", "r") as f:
    photographers = json.load(f)

logger.info(f"Loaded {len(photographers)} photographers.")

#  loop to embed and store
for idx, p in enumerate(photographers):
    # Create text representation for embedding
    text = f"{p['name']} in {p['city']} with budget {p['budget']}"

# calls OpenAI API to convert text into a vector
    emb = emb_client.embeddings.create(
                input=text,
                model="text-embedding-3-small"
            ).data[0].embedding  #extracts the actual vector from the API response

# Why upsert instead of insert? If a point with the same ID exists, Qdrant updates it instead of duplicating.
# upsert : stores vector + payload in Qdrant for fast semantic search
# Insert if new, update if ID already exists
    qdrant.upsert(
        collection_name="photographers",
        points=[PointStruct(      # List of points to store
                id=idx,
                vector=emb,
                payload=p
            )]
    )


# Define Photographer Agent Node
def photographer_agent_node(state: WeddingState) -> dict:
    query = state["query"]

    # Embed user query
    query_emb = emb_client.embeddings.create(
            input=query,
            model="text-embedding-3-small"
        ).data[0].embedding

    # Search Qdrant for best matches
    results = qdrant.search(
        collection_name="photographers",
        query_vector=query_emb,
        limit=3  # return top 3 photographers
    )

    # Format results
    suggestions = []
    for r in results:
        p = r.payload  # full JSON data
        suggestions.append(
            f"- {p['name']} ({p['city']}, Budget: ₹{p['budget']}, Contact: {p['contact']})"
        )

    response_text = "\n".join(suggestions)

    # Add to conversation history
    state["messages"].append(HumanMessage(content=query))
    state["messages"].append(AIMessage(content=response_text))
    # state["messages"].append({"role": "assistant", "content": response_text})
    return {
        "response": response_text
    }


# if __name__ == "__main__":
#     # Initialize state with a user query
#     state = {
#         "query": "Find photographers in surat under 150000",
#         "messages": []  # conversation history
#     }

#     # Call your agent node
#     final_state = photographer_agent_node(state)

#     # Print the assistant's response
#     print("Assistant Response:\n")
#     print(final_state["messages"][-1]["content"])
