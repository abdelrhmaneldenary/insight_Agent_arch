from fastapi.testclient import TestClient
from src.main import app

# This creates a fake browser to test our API without starting the server
client = TestClient(app)

def test_research_endpoint_validation():
    """
    Test that the API correctly rejects empty requests 
    before wasting API credits.
    """
    # Send an empty JSON payload
    response = client.post("/research", json={})
    
    # We expect a 422 Unprocessable Entity (Validation Error)
    assert response.status_code == 422
    
    # Check that it asks for the 'question' field
    data = response.json()
    assert data["detail"][0]["loc"] == ["body", "question"]