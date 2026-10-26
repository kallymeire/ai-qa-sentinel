import os
import json
import pytest
from fastapi.testclient import TestClient
from src.backend.main import app

client = TestClient(app)

def test_login_sucesso():
    response = client.post("/api/v1/auth/login", json={"email": "user@email.com", "password": "123456"})
    assert response.status_code == 200
    assert "token" in response.json()

def test_login_falha():
    response = client.post("/api/v1/auth/login", json={"email": "errado@email.com", "password": "wrong"})
    assert response.status_code == 401

def test_dataset_existe():
    caminho = os.path.join("data", "dataset_qa.json")
    assert os.path.exists(caminho)
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)
    assert len(dados) > 0