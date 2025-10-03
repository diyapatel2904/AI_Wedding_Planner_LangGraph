from langgraph.graph import StateGraph, END
from state import WeddingState
from loguru import logger
from agents.router_agent import classify_intent
from agents.catering_agent import catering_agent_node
from agents.fashion_agent import fashion_agent_node
from agents.venue_agent import venue_agent_node
from agents.general_agent import general_agent_node
from agents.photo_agent import photographer_agent_node
from langgraph.checkpoint.memory import InMemorySaver

# from langchain_core.runnables import RunnableConfig

def build_workflow():
    """
    Build the full Wedding Planner workflow with router and agents.
    """
    logger.info("Building Wedding Planner workflow...")

    graph_builder = StateGraph(WeddingState)

    # Add router + agent nodes
    graph_builder.add_node("router", classify_intent)
    graph_builder.add_node("fashion", fashion_agent_node)
    graph_builder.add_node("venue", venue_agent_node)
    graph_builder.add_node("catering", catering_agent_node)
    graph_builder.add_node("general", general_agent_node)
    graph_builder.add_node("photographer_agent", photographer_agent_node)
    # Set entry point
    graph_builder.set_entry_point("router")

    # Conditional routing from router → agents
    graph_builder.add_conditional_edges(
        "router",
        lambda state: state["intent"],
        {
            "fashion": "fashion",
            "venue": "venue",
            "catering": "catering",
            "general": "general",
            "photographer":"photographer_agent"
        },
    )

    # All agents go to END
    graph_builder.add_edge("fashion", END)
    graph_builder.add_edge("venue", END)
    graph_builder.add_edge("catering", END)
    graph_builder.add_edge("general", END)
    graph_builder.add_edge("photographer_agent", END)

    logger.info("Wedding Planner workflow built successfully.")
    # graph = graph_builder.compile() 
    memory = InMemorySaver()
    graph = graph_builder.compile(checkpointer=memory)
    # print(graph.get_graph().draw_mermaid())    #debug the workflow visualization)

    return graph

# 5. Run Example
if __name__ == "__main__":
    app = build_workflow()

    # Example test queries
    queries = [
        # "Suggest bridal Indian wedding outfits",
        # "Find me a resort in Ahmedabad under 10 lakhs for 200 guests",
        # "What catering options do you suggest?",
        # "Tell me about wedding traditions",
    ]


    # thread_config = {"configurable": {"thread_id": "1234"}}
    # result = app.invoke({"query": queries[0], "intent": "", "response": "",  "messages": []}, config=thread_config)
    app.invoke({"query": queries[0], "intent": "", "response": "",  "messages": []})
    
    

 

 
 