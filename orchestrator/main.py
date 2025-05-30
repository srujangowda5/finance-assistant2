from fastapi import FastAPI
import requests

app = FastAPI()

# Live agent URLs on Render
API_AGENT_URL = "https://api-agent-l7np.onrender.com/exposure"
ANALYTICS_AGENT_URL = "https://analytics-agent-47fk.onrender.com/analyze"
LANGUAGE_AGENT_URL = "https://language-agent.onrender.com/narrative"
SCRAPING_AGENT_URL = "https://scraping-agent-vvrf.onrender.com/earnings"
RETRIEVER_AGENT_URL = "https://retriever-agent-f2m2.onrender.com/search"

@app.get("/")
def root():
    return {"message": "Orchestrator Agent is live. Use POST /market-summary"}

@app.post("/market-summary")
def generate_market_summary():
    try:
        # STEP 1: API Agent
        try:
            print("📡 Calling API Agent:", API_AGENT_URL)
            exposure_resp = requests.get(API_AGENT_URL)
            print("🟡 API Agent Raw:", exposure_resp.text)
            exposure_data = exposure_resp.json()
        except Exception as e:
            return {"error": f"❌ API Agent JSON error: {str(e)}"}

        # STEP 2: Analytics Agent
        try:
            print("📡 Calling Analytics Agent:", ANALYTICS_AGENT_URL)
            analytics_resp = requests.get(ANALYTICS_AGENT_URL)
            print("🟡 Analytics Agent Raw:", analytics_resp.text)
            analytics_data = analytics_resp.json()
        except Exception as e:
            return {"error": f"❌ Analytics Agent JSON error: {str(e)}"}

        # STEP 3: Scraping Agent
        try:
            print("📡 Calling Scraping Agent:", SCRAPING_AGENT_URL)
            scraping_resp = requests.get(SCRAPING_AGENT_URL)
            print("🟡 Scraping Agent Raw:", scraping_resp.text)
            earnings_data = scraping_resp.json()
            earnings_highlights = "\n".join(earnings_data.get("surprises", []))
        except Exception as e:
            print("⚠️ Scraping Agent failed:", str(e))
            earnings_highlights = "Earnings data unavailable"

        # STEP 4: Retriever Agent
        try:
            print("📡 Calling Retriever Agent:", RETRIEVER_AGENT_URL)
            retriever_resp = requests.get(RETRIEVER_AGENT_URL, params={"q": "Asia tech earnings"})
            print("🟡 Retriever Agent Raw:", retriever_resp.text)
            retriever_data = retriever_resp.json()
            retrieved_chunks = "\n".join(retriever_data.get("matches", []))
        except Exception as e:
            print("⚠️ Retriever Agent failed:", str(e))
            retrieved_chunks = "No RAG context available"

        # STEP 5: Prepare Language Payload
        highlights = earnings_highlights + "\n" + retrieved_chunks
        payload = {
            "change": analytics_data.get("change", 0),
            "trend": analytics_data.get("trend", "no change"),
            "sentiment": "neutral",
            "highlights": highlights
        }

        # STEP 6: Language Agent
        try:
            print("📡 Sending to Language Agent:", LANGUAGE_AGENT_URL)
            print("📤 Payload:", payload)
            language_resp = requests.post(LANGUAGE_AGENT_URL, json=payload)
            print("🟡 Language Agent Raw:", language_resp.text)
            if language_resp.status_code != 200:
                return {
                    "error": f"Language agent failed with {language_resp.status_code}",
                    "details": language_resp.text
                }
            final_narrative = language_resp.json()
            return {"summary": final_narrative.get("narrative", "Summary generation failed")}
        except Exception as e:
            return {"error": f"❌ Language Agent JSON error: {str(e)}"}

    except Exception as e:
        return {"error": f"🔥 Orchestrator Internal Error: {str(e)}"}
