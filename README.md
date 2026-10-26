# 🛡️ AI-QA Sentinel

> Agente autónomo de testes e garantia de qualidade (QA) utilizando **LangGraph**, **FastAPI** e **SQLite**, com **100% de cobertura de código**.

---

## 📌 Sobre o Projeto

O **AI-QA Sentinel** é um pipeline inteligente de automação de testes QA concebido para carregar conjuntos de dados de teste, executar verificações autónomas e registar métricas de execução e histórico com persistência de dados.

A solução foi desenvolvida seguindo boas práticas de arquitetura de software, padrão RESTful API e testes unitários/de integração exaustivos.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Orquestração de Agentes:** LangGraph
- **Framework API:** FastAPI & Uvicorn
- **Base de Dados:** SQLite
- **Testes & Cobertura:** Pytest & Pytest-Cov (100% Total Coverage)
- **Documentação:** OpenAPI / Swagger UI

---

## ⚙️ Arquitetura do Agente

O agente foi modelado como um grafo de estado através do **LangGraph**: