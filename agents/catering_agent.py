from langchain.agents import initialize_agent, AgentType
from loguru import logger
from tools.catering_tool import catering_search
from utils.llm_config import llm
from state import WeddingState
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage

# logger.add("catering_agent.log", rotation="10 MB", retention="7 days", level="INFO")

# def catering_agent_node(state: WeddingState) -> dict:

#     tools = [catering_search]
#     catering_agent = initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)

# # Call the executor
#     result = catering_agent.invoke({"input": state["query"]})

#      # If result is a dict, extract the string
#     if isinstance(result, dict):
#         response_text = result.get("output") or str(result)
#     else:
#         response_text = str(result)

#         # Update messages
#     updated_messages = state.get("messages", []) + [{"role": "assistant", "content": response_text}]

#     return {"response": response_text, "messages": updated_messages}
#     # return {"response": result,
#     #         "messages": state.get("messages", []) + result["messages"]}



def catering_agent_node(state: WeddingState) -> dict:
    logger.info("Processing catering query...")
    
    tools = [catering_search]
    catering_agent = initialize_agent(
        tools, llm, 
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True
    )

    try:
        result = catering_agent.invoke({"input": state["query"]})
        response_text = result.get("output", "No response from catering agent")
        
        # Add messages directly to the existing state messages
        state['messages'].append(HumanMessage(content=state["query"]))
        state['messages'].append(AIMessage(content=response_text))
        
        return {
            "response": response_text
        }
    except Exception as e:
        logger.error(f"Catering agent error: {e}")
        error_msg = f"Sorry, I encountered an error with catering search: {str(e)}"
        
        # Add error messages to state
        state['messages'].append(HumanMessage(content=state["query"]))
        state['messages'].append(AIMessage(content=error_msg))
        
        return {
            "response": error_msg
        }