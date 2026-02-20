from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.core.config import Config

llm = ChatGroq(model=Config.MODEL_NAME, temperature=0.7)

def writer_node(state):
    """
    The Writer Agent.
    1. Takes the 'task' and 'research_data' from the State.
    2. Synthesizes a final answer.
    """
    print("--- WRITER AGENT WORKING ---")
    task = state['task']
    data = state['research_data']
    
    prompt = ChatPromptTemplate.from_template(
        """You are a senior technical writer. 
        Write a concise, professional report based ONLY on the following context.
        
        Question: {question}
        
        Research Data: 
        {data}
        
        Report:"""
    )
    
    chain = prompt | llm
    response = chain.invoke({"question": task, "data": data})
    
    return {"draft": response.content}