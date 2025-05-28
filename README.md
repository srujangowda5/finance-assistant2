# 💹 Multi-Agent Finance Assistant

🔗 [🌐 Live App on Streamlit](https://multi-agent-finance-assistant-srujangowda5.streamlit.app/)

This project is a modular, voice-enabled financial assistant that delivers daily Asia tech market briefings using AI agents.

---
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
## 🚀 Deployment

This Streamlit app is live at:  
🔗 [https://multi-agent-finance-assistant-srujangowda5.streamlit.app/](https://multi-agent-finance-assistant-srujangowda5.streamlit.app/)

To run locally:

```bash
git clone https://github.com/srujangowda5/finance-assistant2
cd finance-assistant2
pip install -r requirements.txt
streamlit run streamlit_app/main.py
```

Ensure individual FastAPI agents are running locally if not using mocked responses.

---

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
