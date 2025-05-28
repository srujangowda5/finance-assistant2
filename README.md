# 📈 AI Market Briefing Assistant

A voice-enabled, multi-agent finance assistant that delivers real-time Asia Tech market briefings through a beautiful Streamlit interface.

---

## 🧠 Use Case: Morning Market Brief

> “What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?”

**The system responds with:**
- A GPT-generated one-line summary
- A voice response using gTTS
- Real-time exposure data using yFinance
- Earnings context via retrieval

---

## 🧩 Architecture Overview

Each agent is a FastAPI microservice:

| Agent             | Purpose                                                |
|------------------|--------------------------------------------------------|
| `api_agent`       | Retrieves Asia tech data via yFinance API             |
| `analytics_agent` | Computes change in tech exposure                      |
| `language_agent`  | Uses OpenAI (GPT) to summarize market info            |
| `voice_agent`     | Converts summary to speech using gTTS                 |
| `retriever_agent` | Uses FAISS to retrieve financial context from text    |
| `orchestrator`    | Main router that connects all agents                  |
| `streamlit_app`   | Frontend interface for users                          |

---

## ⚙️ Features

✅ Live risk exposure from Yahoo Finance (TSM, INFY, BABA...)  
✅ Natural language summary generation via GPT-3.5  
✅ Real-time voice output (TTS with gTTS)  
✅ Retrieval-Augmented Generation with FAISS  
✅ Fully modular microservices using FastAPI  
✅ Clean Streamlit dashboard with custom tracker input  

---

## 💻 Run the Project Locally

1. **Clone the repo**:
```bash
git clone https://github.com/yourname/finance-assistant
cd finance-assistant2
```

2. **Set up virtual env and install dependencies**:
```bash
python -m venv venv
venv\Scripts\activate  # on Windows
pip install -r requirements.txt
```

3. **Run agents** (each in a separate terminal):
```bash
uvicorn agents.api_agent.main:app --port 8001
uvicorn agents.analytics_agent.main:app --port 8002
uvicorn agents.language_agent.main:app --port 8003
uvicorn orchestrator.main:app --port 8004
uvicorn agents.scraping_agent.main:app --port 8005
uvicorn agents.retriever_agent.main:app --port 8006
uvicorn agents.voice_agent.main:app --port 8007
uvicorn agents.top_stocks_agent.main:app --port 8008
```

4. **Run the frontend**:
```bash
streamlit run streamlit_app/main.py
```

---

## 📝 AI Tool Usage

- **LLM**: GPT-3.5 (OpenAI API)
- **TTS**: gTTS (Google Text-to-Speech)
- **STT (optional)**: Whisper (used if `/speak` with file)
- **Retriever**: Langchain + FAISS + TextLoader
- **Data Source**: yFinance (live stock prices)

---

## 📸 Screenshots

> Add your screenshots here for Market Summary, Voice, and Tracker view

---

## 📦 Deployment

You can deploy to Streamlit Cloud or HuggingFace Spaces. Just make sure to include:

- `requirements.txt`
- `README.md`
- `streamlit_app/main.py`

---

## 👨‍💻 Developer

Made with ❤️ by [Your Name]  
🔗 GitHub: [github.com/yourname](https://github.com/yourname)