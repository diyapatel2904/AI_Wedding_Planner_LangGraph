
# from langchain.chat_models import ChatOpenAI
from loguru import logger
from langchain_core.messages import AIMessage, HumanMessage
from utils.llm_config import llm
from dotenv import load_dotenv
from prompt.router_prompt import router_prompt
from agents.fashion_agent import fashion_agent_node 
from agents.venue_agent import venue_agent_node
from agents.catering_agent import catering_agent_node
from agents.general_agent import general_agent_node
from agents.photo_agent import photographer_agent_node
from state import WeddingState

# Dictionary of agents
agents = {
    "fashion": fashion_agent_node,
    "venue": venue_agent_node,
    "catering": catering_agent_node,
    "general": general_agent_node,
    "photographer":photographer_agent_node,
}

def classify_intent(state: WeddingState) -> WeddingState:
    """
    Router agent node that classifies the query intent using LLM
    and updates state['intent'] for conditional routing in LangGraph.
    """

       
    logger.info("in classify intent")
        # Classify query
    logger.info(f" Query from state {state['query']}")

        # category = llm(router_prompt.format(query=state["query"])).strip().lower()
    chain = router_prompt | llm
    category =  chain.invoke({"query":state["query"],"chat_history":state["messages"][-6:]})
    logger.info(f"history :{state['messages'][-6:]}")
        
    logger.info(f"category : {category}")

        # Ensure valid category
    if category.content not in agents:
            category = "general"

    return {"intent":category.content}
