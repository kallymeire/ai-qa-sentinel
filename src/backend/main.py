from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="AI-QA Sentinel Target API")

class LoginPayload(BaseModel):
    email: str
    password: str

class ProdutoPayload(BaseModel):
    nome: str
    preco: float

@app.post("/api/v1/auth/login")
def login(payload: LoginPayload):
    if payload.email == "user@email.com" and payload.password == "123456":
        return {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.dummy_token"}
    raise HTTPException(status_code=401, detail="Credenciais inválidas")

@app.post("/api/v1/produtos")
def criar_produto(payload: ProdutoPayload):
    return {"status": "sucesso", "produto": payload.nome, "preco": payload.preco}