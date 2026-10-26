# 🛡️ AI-QA Sentinel

**AI-QA Sentinel** é uma plataforma de automação de testes de garantia de qualidade (QA) baseada em Agentes de Inteligência Artificial. O projeto visa a geração, execução e análise autônoma de testes de API usando uma arquitetura moderna em Python.

---

## 🚀 Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Backend API:** FastAPI & Uvicorn
- **Agentes de IA:** LangGraph
- **Framework de Testes:** Pytest & Requests / HTTPX
- **Dashboard:** Streamlit & Plotly
- **Ambiente Virtual:** venv

---

## 📁 Estrutura do Projeto

```text
ai-qa-sentinel/
├── data/
│   └── dataset_qa.json       # Dataset de treino/exemplos de testes QA
├── src/
│   ├── agents/
│   │   └── qa_agent.py       # Lógica principal do agente de QA
│   ├── backend/
│   │   └── main.py           # API REST em FastAPI para testes de contrato
│   └── dashboard/            # Painel visual em Streamlit
├── tests/                    # Suíte de testes automatizados
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação do repositório
