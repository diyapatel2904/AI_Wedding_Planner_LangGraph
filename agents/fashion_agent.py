
from loguru import logger
from state import WeddingState
from utils.llm_config import llm
from tools.fashion_tool import fashion_search
from prompt.fashion_prompt import fashion_prompt
from langchain.agents import create_agent
from langchain_core.messages import ToolMessage, AIMessage,HumanMessage

# Configure logger
logger.add("fashion_agent.log", rotation="10 MB", retention="7 days", level="INFO")

# def fashion_agent_node(state: WeddingState) -> dict:
#     """
#     Workflow node for the Fashion Agent.
#     Runs the fashion agent and extracts only the tool output (URLs).
#     """
#     fashion_agent = create_react_agent(
#             model=llm,
#             tools=[fashion_search],
#             prompt=fashion_prompt.partial(
#                 tools="FashionSearch: Fetch bridal inspirations",
#                 tool_names="FashionSearch"
#                 )
#             )
# # Call the executor
#     result = fashion_agent.invoke({"input": state["query"]})
    
#     # logger.info(f"result from fashion agent{result}")
#     logger.info(f"result from fashion agent{result['messages'][-1]}")

#     # Sync LangChain messages with LangGraph state
#     return {"response": result["messages"][-1].content,
#             "messages": state.get("messages", []) + result["messages"]
#         }



def fashion_agent_node(state: WeddingState) -> dict:
    """
    Workflow node for the Fashion Agent.
    Runs the fashion agent and extracts only the tool output (URLs).
    """
    fashion_agent = create_agent(
        model=llm,
        tools=[fashion_search],
        system_prompt=fashion_prompt.partial(
            tools="FashionSearch: Fetch bridal inspirations",
            tool_names="FashionSearch"
        )
    )

    # agent_input = {"input": state["query"]}
    # if state.get('messages'):
    #     agent_input["messages"] = state['messages']
        
    result = fashion_agent.invoke({"query":state["query"],"chat_history":state["messages"]})
    
    logger.info(f"result from fashion agent{result['messages'][-1]}")
    
    response_text = result["messages"][-1].content
    
    # Add messages directly to the existing state messages
    state['messages'].append(HumanMessage(content=state["query"]))
    state['messages'].append(AIMessage(content=response_text))
    
    return {
        "response": response_text
    }
    
# The function receives the current state (including the query and chat history).
# It runs the fashion agent with this context.
# It logs and extracts the agent’s reply.
# It updates the chat history with both the user’s and agent’s messages.
# It returns the agent’s response for further use in the workflow.
