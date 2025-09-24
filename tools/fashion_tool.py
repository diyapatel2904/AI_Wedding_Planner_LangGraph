
import os
import json
from dotenv import load_dotenv
from tavily import TavilyClient
from loguru import logger
from langchain.tools import tool

# Configure logger
logger.add("agents.log", rotation="10 MB", retention="7 days", level="INFO")

# Load environment variables
load_dotenv()

try:
    api_key = os.getenv("TAVILY_API_KEY")
    logger.info("Initializing Tavily client...")
    client = TavilyClient(api_key=api_key)
    logger.info("Tavily client initialized successfully.")
except Exception as e:
    logger.exception(f"Error initializing Tavily client: {e}")
    client = None


@tool("fashion_search", return_direct=True)
def fashion_search(query: str) -> str:
    """
    Search fashion-related images and articles using Tavily.
    Returns top results with titles, URLs, and images in JSON format.
    """
    logger.info(f"fashion_search called with query: '{query}'")
    try:
        results = client.search(query=query, search_depth="advanced", max_results=2)
        formatted = []
        for r in results["results"]:
            title = r.get("title")
            url = r.get("url")
            formatted.append(f"🔗 [{title}]({url})")   # clickable link in Streamlit

        response = "\n".join(formatted)
        logger.info(f"fashion_search response: {response}")
        return response

    except Exception as e:
        logger.exception(f"Error in fashion_search with query '{query}': {e}")
        return f"Error: {str(e)}"
