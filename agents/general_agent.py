# from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage
from loguru import logger
from utils.llm_config import llm
from state import WeddingState
from prompt.general_prompt import general_prompt

def general_agent_node(state: WeddingState) -> dict:
    """
    General agent node that handles queries which do not fall under
    fashion, venue, or catering. Uses LLM with a general-purpose prompt.
    """
#     logger.info("in general_agent_node")
#     logger.info(f"Query from state: {state['query']}")

        # Build chain (prompt + LLM)
    chain = general_prompt | llm
        # Get response from LLM
    response = chain.invoke({"query": state["query"]})

    logger.info(f"General agent response: {response.content}")

    # return response.content
    return{
        "response": response.content
    }

        # "response": response["messages"][-1].content
            # "messages": state.get("messages", []) + response["messages"]}