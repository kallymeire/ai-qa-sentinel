from fastapi import FastAPI
from src.agents.qa_agent import run_qa_sentinel_agent

app = FastAPI(
    title="AI-QA Sentinel API",
    description="API de automação de testes QA com Agentes de IA e LangGraph",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao AI-QA Sentinel API!"}

@app.post("/api/v1/run-qa")
def trigger_qa_agent():
    """Endpoint para acionar autonomamente o agente de QA."""
    result = run_qa_sentinel_agent()
    return {
        "status": "success",
        "agent_status": result.get("status"),
        "total_tests": len(result.get("results", [])),
        "results": result.get("results")
    }