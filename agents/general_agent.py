# from langchain.chat_models import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage
from loguru import logger
from utils.llm_config import llm
from state import WeddingState
from prompt.general_prompt import general_prompt

# def general_agent_node(state: WeddingState) -> dict:
#     """
#     General agent node that handles queries which do not fall under
#     fashion, venue, or catering. Uses LLM with a general-purpose prompt.
#     """
# #     logger.info("in general_agent_node")
# #     logger.info(f"Query from state: {state['query']}")

#         # Build chain (prompt + LLM)
#     chain = general_prompt | llm
#         # Get response from LLM
#     response = chain.invoke({"query": state["query"]})

#     logger.info(f"General agent response: {response.content}")
    
#     # Update messages in state for memory
#     previous_messages = state.get("messages", [])
#     new_messages = previous_messages + [AIMessage(content=response.content)]

#     # Return response and updated messages
#     return {
#         "response": response.content,
#         "messages": new_messages
#     }

#     # # return response.content
#     # return{
#     #     "response": response.content
#     # }

#         # "response": response["messages"][-1].content
#             # "messages": state.get("messages", []) + response["messages"]}

def general_agent_node(state: WeddingState) -> dict:
    """
    General agent node that handles queries which do not fall under
    fashion, venue,photographer or catering. Uses LLM with a general-purpose prompt.
    """
    try:
        if state.get('messages'):
            # Use the LLM with full conversation context
            response = llm.invoke(state['messages'] + [HumanMessage(content=state["query"])])
        else:
            # Fallback to original prompt-based approach
            chain = general_prompt | llm
            response = chain.invoke({"query":state["query"],"chat_history":state["messages"]})
        
        logger.info(f"General agent response: {response.content}")
        
        # Add messages directly to the existing state messages
        state['messages'].append(HumanMessage(content=state["query"]))
        state['messages'].append(AIMessage(content=response.content))
        
        return {
            "response": response.content
        }
    except Exception as e:
        
        error_msg = f"Sorry, I encountered an error: {str(e)}"
        
        # Add error messages to state
        state['messages'].append(HumanMessage(content=state["query"]))
        state['messages'].append(AIMessage(content=error_msg))
        
        return {
            "response": error_msg
        }