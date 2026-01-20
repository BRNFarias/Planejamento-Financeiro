import os
import gspread
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# --- CONFIGURAÇÃO DE CORS (Importante para o Frontend funcionar) ---
# Permite que seu site na Vercel (e localhost) converse com esse backend
origins = [
    "http://localhost:5500",    # Para testes locais
    "http://127.0.0.1:5500",
    "https://seu-projeto.vercel.app" # Depois você troca pelo link real da Vercel
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Pode deixar "*" no início para facilitar, depois restrinja
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODELO DE DADOS (Validação) ---
class Lancamento(BaseModel):
    responsavel: str  # Breno ou Rebeca
    data: str         # YYYY-MM-DD vindo do HTML
    descricao: str
    valor: float
    tipo: str         # Fixo, Variável, Lazer
    meio: str         # Cartão, Pix

# --- CONEXÃO COM GOOGLE SHEETS ---
def get_worksheet():
    try:
        # O Render vai procurar um arquivo chamado 'credentials.json'
        # No desenvolvimento local, você deixa esse arquivo na pasta.
        # No Render, vamos usar "Secret Files" para criar ele lá.
        gc = gspread.service_account(filename="credentials.json")
        
        # IMPORTANTE: Coloque o NOME EXATO da sua planilha no Google Sheets aqui
        sh = gc.open("Planejamento Financeiro 2026-2") 
        
        # Seleciona a aba de Banco de Dados
        return sh.worksheet("BD_Lancamentos")
    except Exception as e:
        print(f"Erro ao conectar no Google Sheets: {e}")
        return None

# --- ENDPOINTS ---

@app.get("/")
def home():
    return {"message": "API Financeira está ON! 🚀"}

@app.post("/api/lancar")
def adicionar_lancamento(dado: Lancamento):
    ws = get_worksheet()
    if not ws:
        raise HTTPException(status_code=500, detail="Erro interno: Não foi possível conectar na planilha.")

    try:
        # Formata a data para o padrão Brasileiro (DD/MM/YYYY) antes de salvar
        data_obj = datetime.strptime(dado.data, "%Y-%m-%d")
        data_formatada = data_obj.strftime("%d/%m/%Y")

        # Prepara a linha para o Google Sheets
        # Ordem das colunas: [Data, Responsável, Tipo, Meio, Descrição, Valor]
        nova_linha = [
            data_formatada,
            dado.responsavel,
            dado.tipo,
            dado.meio,
            dado.descricao,
            dado.valor
        ]

        # Adiciona na última linha
        ws.append_row(nova_linha)

        return {"message": "Sucesso", "dado_salvo": nova_linha}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Se for rodar localmente com "python app.py"
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)