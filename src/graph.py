from typing import TypedDict
from langgraph.graph import StateGraph, END
from src.agents.researcher import researcher_node
from src.agents.writer import writer_node

# 1. Define the State
# This is the "Parcel" that gets passed around.
# Every agent can read from this and write to this.
class AgentState(TypedDict):
    task: str           # The user's original question
    research_data: str  # The raw data found by the researcher
    draft: str          # The final answer written by the writer

# 2. Initialize the Graph
workflow = StateGraph(AgentState)

# 3. Add Nodes (The Workers)
workflow.add_node("researcher", researcher_node)
workflow.add_node("writer", writer_node)

# 4. Define Edges (The Logic)
# Start at the Researcher
workflow.set_entry_point("researcher")

# From Researcher, go to Writer
workflow.add_edge("researcher", "writer")

# From Writer, go to END (Finish the job)
workflow.add_edge("writer", END)

# 5. Compile the Graph
# This creates the runnable application
app = workflow.compile()