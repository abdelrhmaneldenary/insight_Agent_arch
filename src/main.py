from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.graph import app as agent_graph

app = FastAPI(title="InsightArchitect Agent")

class QueryRequest(BaseModel):
    question: str

@app.post("/research")
async def run_research(request: QueryRequest):
    """
    Endpoint to trigger the agentic workflow.
    """
    try:
        # Initialize the state with the user's question
        initial_state = {"task": request.question, "research_data": "", "draft": ""}
        
        # Run the graph
        result = agent_graph.invoke(initial_state)
        
        return {
            "status": "success",
            "final_report": result["draft"],
            "raw_research": result["research_data"]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Run the server
    uvicorn.run(app, host="0.0.0.0", port=8000)