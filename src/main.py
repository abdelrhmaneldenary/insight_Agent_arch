from fastapi import FastAPI
from fastapi.responses import HTMLResponse  
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.graph import app as agent_graph

app = FastAPI(title="InsightArchitect Agent")

class QueryRequest(BaseModel):
    question: str


@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Insight Architect</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #f9fafb; color: #111827; display: flex; flex-direction: column; align-items: center; padding: 50px 20px; }
            .container { max-width: 800px; width: 100%; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
            h1 { font-size: 24px; margin-bottom: 8px; color: #1f2937; }
            p { color: #6b7280; margin-bottom: 24px; }
            .input-group { display: flex; gap: 10px; margin-bottom: 20px; }
            input { flex: 1; padding: 12px; border: 1px solid #d1d5db; border-radius: 6px; font-size: 16px; outline: none; }
            input:focus { border-color: #3b82f6; outline: 2px solid #3b82f6; }
            button { background: #111827; color: white; border: none; padding: 12px 24px; border-radius: 6px; font-size: 16px; cursor: pointer; font-weight: 500; transition: background 0.2s; }
            button:hover { background: #374151; }
            #loader { display: none; color: #3b82f6; font-weight: 500; margin-bottom: 20px; }
            #result { white-space: pre-wrap; line-height: 1.6; color: #374151; background: #f3f4f6; padding: 20px; border-radius: 8px; display: none;}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Insight Architect AI</h1>
            <p>Enter a topic to generate an autonomous, multi-agent research report.</p>
            <div class="input-group">
                <input type="text" id="query" placeholder="e.g., What are the security risks of LLMs?">
                <button onclick="runResearch()" id="btn">Research</button>
            </div>
            <div id="loader">Agent is researching and writing... (This takes about 20-30 seconds)</div>
            <div id="result"></div>
        </div>
        <script>
            async function runResearch() {
                const query = document.getElementById('query').value;
                if (!query) return;
                
                document.getElementById('loader').style.display = 'block';
                const resultDiv = document.getElementById('result');
                resultDiv.style.display = 'none';
                resultDiv.innerText = '';
                document.getElementById('btn').disabled = true;
                
                try {
                    const response = await fetch('/research', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ question: query })
                    });
                    const data = await response.json();
                    resultDiv.innerText = data.final_report || data.detail || "Error generating report.";
                    resultDiv.style.display = 'block';
                } catch (err) {
                    resultDiv.innerText = "An error occurred connecting to the agent.";
                    resultDiv.style.display = 'block';
                } finally {
                    document.getElementById('loader').style.display = 'none';
                    document.getElementById('btn').disabled = false;
                }
            }
        </script>
    </body>
    </html>
    """
    return html_content

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