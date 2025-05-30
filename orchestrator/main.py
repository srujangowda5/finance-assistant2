from fastapi import FastAPI
import requests

app = FastAPI()

# Agent URLs
#API_AGENT_URL = "https://api-agent-l7np.onrender.com/exposure"
#ANALYTICS_AGENT_URL = "https://analytics-agent-47fk.onrender.com/analyze"
#LANGUAGE_AGENT_URL = "https://language-agent.onrender.com/narrative"
#RETRIEVER_AGENT_URL = "https://retriever-agent-f2m2.onrender.com/search"
#SCRAPING_AGENT_URL = "https://scraping-agent-vvrf.onrender.com/earnings"

@app.get("/")
def root():
    return {"message": "Orchestrator Agent is live. Use /market-summary"}

@app.get("/market-summary")
def generate_market_summary():
    try:
        # Step 1: Get exposure data
        try:
            print("📡 Calling API Agent:",https://api-agent-l7np.onrender.com/exposure)
            exposure_resp = requests.get(https://api-agent-l7np.onrender.com/exposure)
            print("✅ API Agent response:", exposure_resp.status_code, exposure_resp.text)
            exposure_data = exposure_resp.json()
        except Exception as e:
            return {"error": f"Failed to get data from API Agent: {str(e)}"}

        # Step 2: Get trend analysis
        try:
            print("📡 Calling Analytics Agent:",https://analytics-agent-47fk.onrender.com/analyze)
            analytics_resp = requests.get(https://analytics-agent-47fk.onrender.com/analyze)
            print("✅ Analytics Agent response:", analytics_resp.status_code, analytics_resp.text)
            analytics_data = analytics_resp.json()
        except Exception as e:
            return {"error": f"Failed to get data from Analytics Agent: {str(e)}"}

        # Step 3: Get earnings surprises
        try:
            print("📡 Calling Scraping Agent:",https://scraping-agent-vvrf.onrender.com/earnings)
            scraping_resp = requests.get(https://scraping-agent-vvrf.onrender.com/earnings)
            print("✅ Scraping Agent response:", scraping_resp.status_code, scraping_resp.text)
            earnings_data = scraping_resp.json()
            earnings_highlights = "\n".join(earnings_data.get("surprises", []))
        except Exception as e:
            print("❌ Scraping Agent failed:", str(e))
            earnings_highlights = "Earnings data unavailable"

        # Step 4: Get RAG context
        try:
            print("📡 Calling Retriever Agent:",https://retriever-agent-f2m2.onrender.com/search?q=Asia tech earnings)
            retriever_resp = requests.get(https://retriever-agent-f2m2.onrender.com/search?q=Asia tech earnings)
            print("✅ Retriever Agent response:", retriever_resp.status_code, retriever_resp.text)
            retriever_data = retriever_resp.json()
            retrieved_chunks = "\n".join(retriever_data.get("matches", []))
        except Exception as e:
            print("❌ Retriever Agent failed:", str(e))
            retrieved_chunks = "No RAG context available"

        # Combine highlights
        highlights = earnings_highlights + "\n" + retrieved_chunks

        # Step 5: Language Agent
        payload = {
            "change": analytics_data.get("change", 0),
            "trend": analytics_data.get("trend", "no change"),
            "sentiment": "neutral",
            "highlights": highlights
        }

        try:
            print("📡 Sending to Language Agent:",https://language-agent.onrender.com/narrative)
            print("📤 Payload:", payload)
            language_resp = requests.post(https://language-agent.onrender.com/narrative, json=payload)
            print("✅ Language Agent response:", language_resp.status_code, language_resp.text)

            if language_resp.status_code != 200:
                return {
                    "error": f"Language agent failed: {language_resp.status_code}",
                    "details": language_resp.text
                }

            final_narrative = language_resp.json()
            return {"summary": final_narrative.get("narrative", "Summary generation failed")}
        except Exception as e:
            return {"error": f"Failed to get summary from Language Agent: {str(e)}"}

    except Exception as e:
        return {"error": f"Unexpected Orchestrator error: {str(e)}"}
