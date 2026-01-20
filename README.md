# 💸 Planejamento Financeiro Automatizado

> Sistema de controle de gastos pessoais integrado ao Google Sheets, desenvolvido com foco em mobilidade e automação.

![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Backend-FastAPI-blue)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FJS-orange)
![Database](https://img.shields.io/badge/Database-Google_Sheets-green)

---

## 🎯 Objetivo

Substituir o preenchimento manual e complexo de planilhas Excel por uma interface web ágil e responsiva (**Mobile First**). O sistema captura lançamentos de despesas de múltiplos usuários (ex: casal) e sincroniza automaticamente com uma base de dados na nuvem (**Google Sheets**), mantendo dashboards e fórmulas financeiras sempre atualizados.

---

## 🏗 Arquitetura

O projeto segue o princípio de **Separação de Responsabilidades**, utilizando o Google Sheets como banco de dados relacional e camada de BI.

- **Frontend (View):**
  - SPA (Single Page Application)
  - Hospedada na **Vercel**
  - Interface simples e rápida para lançamentos em mobilidade

- **Backend (Controller):**
  - API RESTful em **Python (FastAPI)**
  - Hospedada no **Render**
  - Responsável por validação de dados, regras de negócio e autenticação com a Google Cloud

- **Database (Model):**
  - **Google Sheets**
  - Aba oculta: `BD_Lancamentos`
  - Abas visuais alimentadas por fórmulas (`QUERY`, `SUMIFS`, etc.)

---

## 🛠 Tecnologias Utilizadas

### Backend
- Python 3.10+
- FastAPI
- Gspread
- Pydantic

### Frontend
- HTML5 & CSS3 (tema escuro, Mobile First)
- JavaScript Vanilla
  - `Fetch API`
  - `LocalStorage`

### DevOps & Infraestrutura
- GitHub (versionamento e CI/CD)
- Render (Backend)
- Vercel (Frontend)
- Google Cloud Platform (Service Accounts e APIs)

---

## 🚀 Como rodar localmente

### Pré-requisitos
- Python instalado
- Conta no Google Cloud Platform
- API do Google Sheets habilitada
- Arquivo `credentials.json` da Service Account

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/financeiro-casal.git
cd financeiro-casal
```

### 2️⃣ Configuração do Backend

Entre na pasta do backend:

```bash
cd backend
```

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

🔒 **Segurança**

Coloque o arquivo `credentials.json` (gerado no Google Cloud) dentro da pasta `backend/`.

> ⚠️ Este arquivo **não é versionado** e está ignorado no Git.

### 3️⃣ Rodar a API

```bash
uvicorn app:app --reload
```

A API estará disponível em:

```
http://localhost:8000
```

### 4️⃣ Configurar o Frontend

Abra o arquivo:

```
frontend/index.html
```

Localize a função `enviarDados()` e ajuste a URL do backend para ambiente local:

```javascript
const response = await fetch('http://localhost:8000/api/lancar', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(dados)
})
```

Abra o `index.html` no navegador.

---

## ☁️ Deploy (Produção)

### Backend (Render)

1. Crie um **Web Service** no Render
2. Conecte ao repositório
3. Defina o **Root Directory** como `backend`
4. Adicione o `credentials.json` como **Secret File**
5. Comando de start:

```bash
uvicorn app:app --host 0.0.0.0 --port 10000
```

### Frontend (Vercel)

1. Importe o repositório na Vercel
2. Defina o **Root Directory** como `frontend`
3. Atualize a URL da API no `index.html`:

```javascript
https://sua-api.onrender.com/api/lancar
```

---

## 🗂 Estrutura de Pastas

```text
financeiro-casal/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── credentials.json   # Não versionado
│
├── frontend/
│   ├── index.html
│   └── style.css
│
└── README.md
```

---

## 🔒 Segurança

- Credenciais protegidas por variáveis de ambiente e Secret Files
- Nenhuma chave sensível é exposta no repositório público

---

## 👨‍💻 Autor

**Breno Rodrigues de Farias**

