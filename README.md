
# 🧠 Multi-Agent Finance Assistant

An open-source, voice-enabled market assistant that delivers real-time financial summaries using multiple AI agents, web scraping, and vector search.

---

## 📌 Use Case: Morning Market Brief

> _"What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?"_

**Voice Output:**
> "Today, your Asia tech allocation is 22% of AUM, up from 18% yesterday. TSMC beat estimates by 4%, Samsung missed by 2%. Regional sentiment is neutral with a cautionary tilt due to rising yields."

---

## 🧩 Architecture Overview

Each agent is a FastAPI microservice:

| Agent              | Purpose                                                |
|-------------------|--------------------------------------------------------|
| `api_agent`        | Retrieves Asia tech data via yFinance API             |
| `analytics_agent`  | Computes change in tech exposure                      |
| `language_agent`   | Uses OpenAI (GPT) to summarize market info            |
| `voice_agent`      | Converts summary to speech using gTTS                 |
| `retriever_agent`  | Uses FAISS to retrieve financial context from text    |
| `scraping_agent`   | Extracts earnings data from filings/web               |
| `top_stocks_agent` | Returns top 5 stock gainers using yFinance            |
| `orchestrator`     | Main router that connects all agents                  |
| `streamlit_app`    | Frontend interface for users                          |

---

## ⚙️ Features

✅ Live risk exposure from Yahoo Finance (TSM, INFY, BABA...)  
✅ Natural language summary generation via GPT-3.5  
✅ Real-time voice output (TTS with gTTS)  
✅ Retrieval-Augmented Generation with FAISS  
✅ Fully modular microservices using FastAPI  
✅ Clean Streamlit dashboard with custom tracker input  

---

## 📦 Project Structure

```
finance-assistant2/
├── agents/
│   ├── api_agent/
│   ├── analytics_agent/
│   ├── language_agent/
│   ├── voice_agent/
│   ├── retriever_agent/
│   ├── scraping_agent/
│   └── top_stocks_agent/
├── orchestrator/
├── streamlit_app/
├── data_ingestion/
├── docs/
├── .env (excluded in .gitignore)
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🚀 Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/finance-assistant2
   cd finance-assistant2
   ```

2. Create virtual environment  
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run each agent in separate terminals  
   ```bash
   uvicorn agents.api_agent.main:app --port 8001
   uvicorn agents.analytics_agent.main:app --port 8002
   uvicorn agents.language_agent.main:app --port 8003
   uvicorn agents.scraping_agent.main:app --port 8005
   uvicorn agents.retriever_agent.main:app --port 8006
   uvicorn agents.voice_agent.main:app --port 8007
   uvicorn agents.top_stocks_agent.main:app --port 8008
   uvicorn orchestrator.main:app --port 8004
   ```

4. Launch Streamlit app  
   ```bash
   streamlit run streamlit_app/main.py
   ```

---

## 🛠️ Deployment

This app can be deployed to **Streamlit Cloud** or run locally with Docker. Ensure `.env` is excluded and API keys are secured.

---

## 📑 Documentation

See [`docs/ai_tool_usage.md`](docs/ai_tool_usage.md) for a detailed log of prompts, tools, and configurations.

---

## 🧠 AI Tools Used

- **LLM**: OpenAI GPT-3.5 Turbo
- **STT**: Whisper base
- **TTS**: gTTS (Google Text-to-Speech)
- **Retriever**: FAISS + OpenAI Embeddings
- **Frontend**: Streamlit
- **Backend**: FastAPI Microservices

---

## 👨‍💻 Author

**Srujan Gowda**  
Deployed version, documentation, and code available on [GitHub](https://github.com/srujangowda5/finance-assistant2)
