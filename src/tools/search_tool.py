from langchain_community.tools.tavily_search import TavilySearchResults
from src.core.config import Config

def get_search_tool():
    """
    Initializes the Tavily Search tool.
    
    Returns:
        TavilySearchResults: A LangChain-compatible tool that searches the web.
    """
    # k=3 means "give me the top 3 results"
    return TavilySearchResults(
        api_wrapper={
            "tavily_api_key": Config.TAVILY_API_KEY
        },
        max_results=3
    )