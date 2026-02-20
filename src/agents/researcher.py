from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from src.core.config import Config
from src.tools.search_tool import get_search_tool
import json

# Initialize the LLM
llm = ChatGroq(model=Config.MODEL_NAME, temperature=0)
search_tool = get_search_tool()

def researcher_node(state):
    """
    The Researcher Agent.
    1. Looks at the user's task.
    2. Searches the web using Tavily.
    3. Summarizes the findings.
    """
    print("--- RESEARCHER AGENT WORKING ---")
    task = state['task']
    
    # Step 1: Search the web
    try:
        search_results = search_tool.invoke(task)
    except Exception as e:
        return {"research_data": f"Search failed with error: {str(e)}"}
    
    # DEBUGGING: Print what we actually got back
    print(f"DEBUG: Search Tool Output Type: {type(search_results)}")
    # print(f"DEBUG: Search Tool Output: {search_results}")  # Uncomment if needed

    # Step 2: Extract content safely
    research_summary = ""
    
    # Case A: It's a list (Normal behavior)
    if isinstance(search_results, list):
        try:
            research_summary = "\n".join([f"- {res.get('content', 'No content')}" for res in search_results])
        except (TypeError, AttributeError):
            # Fallback if the list contains strings, not dicts
            research_summary = str(search_results)
            
    # Case B: It's a string (Error message or raw text)
    elif isinstance(search_results, str):
        research_summary = search_results
        
    # Case C: It's something else (Edge case)
    else:
        research_summary = str(search_results)
    
    # Fallback if summary is empty
    if not research_summary:
        research_summary = "No relevant search results found."

    return {"research_data": research_summary}