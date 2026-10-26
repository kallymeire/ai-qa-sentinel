from fastapi.testclient import TestClient
from src.backend.main import app

# Inicializa o cliente de teste para o FastAPI
client = TestClient(app)

def test_read_root():
    """Testa a rota GET / (a raiz da API)."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bem-vindo ao AI-QA Sentinel API!"}

def test_trigger_qa_agent():
    """Testa o endpoint POST do agente de QA."""
    response = client.post("/api/v1/run-qa")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "results" in data
    def test_qa_agent_missing_dataset(monkeypatch):
        """Testa o comportamento do agente quando o dataset não é encontrado."""
    from src.agents.qa_agent import load_dataset_node
    
    # Simula um estado com um caminho de dataset inválido/inexistente
    fake_state = {
        "dataset_path": "caminho/nao/existente.json",
        "test_cases": [],
        "results": [],
        "status": ""
    }
    
    updated_state = load_dataset_node(fake_state)
    assert updated_state["test_cases"] == []
    assert "Erro" in updated_state["status"]