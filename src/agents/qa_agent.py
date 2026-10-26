import json
import os

def carregar_dataset():
    caminho_dataset = os.path.join("data", "dataset_qa.json")
    if not os.path.exists(caminho_dataset):
        print("Dataset não encontrado!")
        return []
    
    with open(caminho_dataset, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    print("🤖 AI-QA Sentinel: Inicializando agente...")
    dados = carregar_dataset()
    print(f"✅ Dataset carregado com sucesso! Exemplos disponíveis: {len(dados)}")
    for i, item in enumerate(dados, 1):
        print(f"\n--- Exemplo {i} ---")
        print(f"Instrução: {item['instruction']}")