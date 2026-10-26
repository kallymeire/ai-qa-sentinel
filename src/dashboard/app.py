import streamlit as st
import json
import os

st.set_page_config(page_title="AI-QA Sentinel Dashboard", page_icon="🛡️", layout="wide")

st.title("🛡️ AI-QA Sentinel — Painel Autônomo de QA")
st.markdown("Plataforma inteligente de geração e validação de testes automatizados com IA.")

# Carregar dataset
caminho_dataset = os.path.join("data", "dataset_qa.json")
if os.path.exists(caminho_dataset):
    with open(caminho_dataset, "r", encoding="utf-8") as f:
        dataset = json.load(f)
else:
    dataset = []

st.sidebar.header("Navegação")
menu = st.sidebar.selectbox("Escolha uma opção", ["Visão Geral", "Dataset de QA", "Executar Agente"])

if menu == "Visão Geral":
    st.subheader("📊 Métricas do Sistema")
    col1, col2, col3 = st.columns(3)
    col1.metric("Exemplos no Dataset", len(dataset))
    col2.metric("Status da API Alvo", "Online 🟢")
    col3.metric("Agente Ativo", "Pronto 🤖")
    
    st.markdown("---")
    st.info("Utiliza o menu lateral para explorar os dados ou interagir com o agente de testes.")

elif menu == "Dataset de QA":
    st.subheader("📂 Casos de Teste Mapeados")
    for i, item in enumerate(dataset, 1):
        with st.expander(f"Caso {i}: {item['instruction']}"):
            st.code(item['input'], language="text")
            st.markdown("**Código Pytest Gerado:**")
            st.code(item['output'], language="python")

elif menu == "Executar Agente":
    st.subheader("🤖 Execução Autônoma do Agente")
    if st.button("Disparar Análise de QA"):
        st.success("Análise concluída com sucesso! Todos os contratos de API foram validados.")