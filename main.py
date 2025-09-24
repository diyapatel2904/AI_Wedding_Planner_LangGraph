# main.py
from workflow import build_workflow
from loguru import logger

def main():
    # Build the workflow graph
    workflow_graph = build_workflow()

    # Example test queries
    test_queries = [
        # "Suggest bridal Indian wedding outfits",
        # "Find me a resort in Ahmedabad under 10 lakhs for 200 guests",
        # "What will be price for idli sambhar for 40 guests",
        # "what is capital of india ?"
    ]

    for query in test_queries:
        logger.info(f"Invoking workflow for query: {query}")
        
        # Initial state for the workflow
        initial_state = {
            "query": query,
            "intent": "",      
            "response": "", 
            "messages": []      
        }

        # Invoke the workflow
        result = workflow_graph.invoke(initial_state)

        # Print the workflow output
        print(f"\nQuery: {query}")
        print(f"Response: {result.get('response', 'No response generated')}")

if __name__ == "__main__":
    main()
