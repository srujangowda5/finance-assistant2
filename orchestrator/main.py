from fastapi import FastAPI
import requests

app = FastAPI()

# Agent URLs
API_AGENT_URL = "http://localhost:8001/exposure"
ANALYTICS_AGENT_URL = "http://localhost:8002/analyze"
LANGUAGE_AGENT_URL = "http://localhost:8003/narrative"

@app.get("/")
def root():
    return {"message": "Orchestrator Agent is live. Use /market-summary"}

@app.get("/market-summary")
def generate_market_summary():
    try:
        # Step 1: Get exposure data
        exposure_resp = requests.get(API_AGENT_URL)
        exposure_data = exposure_resp.json()

        # Step 2: Get trend analysis
        analytics_resp = requests.get(ANALYTICS_AGENT_URL)
        analytics_data = analytics_resp.json()

        # Step 3: Get earnings surprises
        scraping_resp = requests.get("http://localhost:8005/earnings")
        earnings_data = scraping_resp.json()
        earnings_highlights = "\n".join(earnings_data.get("surprises", []))

        # Step 4: Query Retriever Agent
        retriever_resp = requests.get("http://localhost:8006/search?q=Asia tech earnings")
        retriever_data = retriever_resp.json()
        retrieved_chunks = "\n".join(retriever_data.get("matches", []))

        # Combine all highlights
        highlights = earnings_highlights + "\n" + retrieved_chunks

        # Step 5: Generate summary via Language Agent
        payload = {
            "change": analytics_data.get("change"),
            "trend": analytics_data.get("trend"),
            "sentiment": "neutral",
            "highlights": highlights
        }

        language_resp = requests.post(LANGUAGE_AGENT_URL, json=payload)
        final_narrative = language_resp.json()

        return {"summary": final_narrative.get("narrative")}

    except Exception as e:
        return {"error": str(e)}
