# AI Tool Usage Log – Finance Assistant

This document records all AI tools used throughout the project, along with prompt formats, parameters, and relevant notes.

---

## 1. 🎯 Language Agent – OpenAI GPT (LLM)
- **Model Used:** gpt-3.5-turbo
- **API:** `openai.ChatCompletion.create()`
- **Prompt Template:** ```Today, your Asia tech exposure changed by {change}% and the trend is {trend}.
Earnings highlights: {highlights}
Regional sentiment is {sentiment}.
Write a professional one-line market summary.```
- **Temperature:** 0.3
- **Use Case:** Summarizing financial briefings in plain English

---

## 2. 🎤 Voice Agent – Whisper (STT)
- **Library:** OpenAI Whisper (base model)
- **Usage:**
- Input: MP3 file
- Output: Transcribed text
- **Reason:** High-accuracy offline speech-to-text

---

## 3. 🔊 Voice Agent – gTTS (TTS)
- **Tool:** `gtts` Python package
- **Usage:**
- Converts LLM-generated summary to MP3
- **Reason:** Lightweight, language-supported TTS

---

## 4. 🔍 Retriever Agent – FAISS + LangChain
- **Tool:** FAISS (via `langchain_community.vectorstores.FAISS`)
- **Text Loader:** `TextLoader("tech_earnings.txt")`
- **Embedder:** `OpenAIEmbeddings`
- **Search Query Format:** `/search?q={user_question}`
- **Use Case:** Retrieve top-K financial context chunks

---

## 5. 🧠 Frameworks/Orchestration
- **LangChain**: Used in Retriever Agent
- **FastAPI**: Used to expose all agents as microservices
- **Streamlit**: Used to build the frontend
- **Uvicorn**: ASGI server to run each microservice

---

## 📝 Additional Notes
- All models were run locally via CPU.
- `ffmpeg` installed separately to support Whisper’s audio decoding.

