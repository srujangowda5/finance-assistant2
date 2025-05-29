from fastapi import FastAPI
import requests

app = FastAPI()

# Agent URLs
API_AGENT_URL = "https://api-agent-l7np.onrender.com/exposure"
ANALYTICS_AGENT_URL = "https://analytics-agent-47fk.onrender.com/analyze"
LANGUAGE_AGENT_URL = "https://language-agent.onrender.com/narrative"
RETRIEVER_AGENT_URL = "https://retriever-agent-f2m2.onrender.com/search"
SCRAPING_AGENT_URL = "https://scraping-agent-vvrf.onrender.com/earnings"

@app.get("/")
def root():
    return {"message": "Orchestrator Agent is live. Use /market-summary"}

@app.get("/market-summary")
def generate_market_summary():
    try:
        # Step 1: Get exposure data
        try:
            exposure_resp = requests.get(API_AGENT_URL)
            exposure_data = exposure_resp.json()
        except Exception as e:
            return {"error": f"Failed to get data from API Agent: {str(e)}"}

        # Step 2: Get trend analysis
        try:
            analytics_resp = requests.get(ANALYTICS_AGENT_URL)
            analytics_data = analytics_resp.json()
        except Exception as e:
            return {"error": f"Failed to get data from Analytics Agent: {str(e)}"}

        # Step 3: Get earnings surprises
        try:
            scraping_resp = requests.get(SCRAPING_AGENT_URL)
            earnings_data = scraping_resp.json()
            earnings_highlights = "\n".join(earnings_data.get("surprises", []))
        except Exception:
            earnings_highlights = "Earnings data unavailable"

        # Step 4: Get RAG context
        try:
            retriever_resp = requests.get(RETRIEVER_AGENT_URL, params={"q": "Asia tech earnings"})
            retriever_data = retriever_resp.json()
            retrieved_chunks = "\n".join(retriever_data.get("matches", []))
        except Exception:
            retrieved_chunks = "No RAG context available"

        # Combine highlights
        highlights = earnings_highlights + "\n" + retrieved_chunks

        # Step 5: Language Agent payload
        payload = {
            "change": analytics_data.get("change", 0),
            "trend": analytics_data.get("trend", "no change"),
            "sentiment": "neutral",
            "highlights": highlights
        }

        try:
            language_resp = requests.post(LANGUAGE_AGENT_URL, json=payload)
            print("LangResp", language_resp.status_code, language_resp.text)
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
