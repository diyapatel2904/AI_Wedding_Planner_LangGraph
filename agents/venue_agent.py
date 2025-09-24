from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv
from agents import catering_agent
import state
from utils.llm_config import llm
from tools.venue_tool import venue_search
from state import WeddingState
from loguru import logger

# Load environment variables
load_dotenv()

# logger.add("agents.log", rotation="10 MB", retention="7 days", level="INFO")

def venue_agent_node(state: WeddingState) -> dict:
    # logger.info("Creating venue_agent with search_venues tool...")

    venue_agent = initialize_agent(
        tools=[venue_search], 
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    result = venue_agent.invoke({"input": state["query"]})
   
    return {
        "response": result.get("output", result.get("response", "No response from venue agent")),
        "messages": state.get("messages", []) + [result]  # Simplified message handling
    }
#     return {
#     "response": result["output"],
#     "messages": state.get("messages", []) + result.get("messages", [])
# }
