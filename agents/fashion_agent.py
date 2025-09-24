
from loguru import logger
from state import WeddingState
from langgraph.prebuilt import create_react_agent
from utils.llm_config import llm
from tools.fashion_tool import fashion_search
from prompt.fashion_prompt import fashion_prompt
from langchain_core.messages import ToolMessage, AIMessage

# Configure logger
logger.add("fashion_agent.log", rotation="10 MB", retention="7 days", level="INFO")

def fashion_agent_node(state: WeddingState) -> dict:
    """
    Workflow node for the Fashion Agent.
    Runs the fashion agent and extracts only the tool output (URLs).
    """
    fashion_agent = create_react_agent(
            model=llm,
            tools=[fashion_search],
            prompt=fashion_prompt.partial(
                tools="FashionSearch: Fetch bridal inspirations",
                tool_names="FashionSearch"
                )
            )
# Call the executor
    result = fashion_agent.invoke({"input": state["query"]})
    
    # logger.info(f"result from fashion agent{result}")
    logger.info(f"result from fashion agent{result['messages'][-1]}")

    # Sync LangChain messages with LangGraph state
    return {"response": result["messages"][-1].content,
            "messages": state.get("messages", []) + result["messages"]
        }