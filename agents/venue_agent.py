from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv
from utils.llm_config import llm
from tools.venue_tool import venue_search
from state import WeddingState
from loguru import logger
from langchain_core.messages import HumanMessage, AIMessage

# Load environment variables
load_dotenv()

# logger.add("agents.log", rotation="10 MB", retention="7 days", level="INFO")

# def venue_agent_node(state: WeddingState) -> dict:
#     # logger.info("Creating venue_agent with search_venues tool...")

#     venue_agent = initialize_agent(
#         tools=[venue_search], 
#         llm=llm,
#         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#         verbose=True
#     )
#     result = venue_agent.invoke({"input": state["query"]})
   
#     # return {
#     #     "response": result.get("output", result.get("response", "No response from venue agent")),
#     #     "messages": state.get("messages", []) + [result]  # Simplified message handling
#     # }
#     return {
#     "response": result["output"],
#     "messages": state.get("messages", []) + result.get("messages", [])
# }
def venue_agent_node(state: WeddingState) -> dict:
    logger.info("Processing venue query...")
    
    venue_agent = initialize_agent(
        tools=[venue_search], 
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    
    try:
        result = venue_agent.invoke({"input": state["query"]})
        response_text = result.get("output", "No response from venue agent")
        
        # Add messages directly to the existing state messages
        state['messages'].append(HumanMessage(content=state["query"]))
        state['messages'].append(AIMessage(content=response_text))
        
        return {
            "response": response_text
        }
    except Exception as e:
        logger.error(f"Venue agent error: {e}")
        error_msg = f"Sorry, I encountered an error with venue search: {str(e)}"
        
        # Add error messages to state
        state['messages'].append(HumanMessage(content=state["query"]))
        state['messages'].append(AIMessage(content=error_msg))
        
        return {
            "response": error_msg
        }