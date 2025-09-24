from langchain.agents import initialize_agent, AgentType
from loguru import logger
from tools.catering_tool import catering_search
from utils.llm_config import llm
from state import WeddingState
from dotenv import load_dotenv

# logger.add("catering_agent.log", rotation="10 MB", retention="7 days", level="INFO")

def catering_agent_node(state: WeddingState) -> dict:

    tools = [catering_search]
    catering_agent = initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)

# Call the executor
    result = catering_agent.invoke({"input": state["query"]})
    return {"response": result,
            "messages": state.get("messages", []) + result["messages"]}

        # return "catering agent okay"