#analytics_agent

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests

app = FastAPI()

API_AGENT_URL = "https://api-agent-l7np.onrender.com/exposure"

class AnalyticsResult(BaseModel):
    change: int
    trend: str

@app.get("/")
def root():
    return {"message": "Analytics Agent is live"}

@app.get("/analyze", response_model=AnalyticsResult)
def analyze_exposure():
    try:
        response = requests.get(API_AGENT_URL)
        response.raise_for_status()
        data = response.json()

        today = data.get("asia_tech_allocation")
        yesterday = data.get("yesterday")

        if today is None or yesterday is None:
            raise ValueError("Missing keys in API response")

        raw_change = today - yesterday
        change = int(round(raw_change))  # ✅ FIX: ensure it's an integer
        trend = "up" if raw_change > 0 else "down" if raw_change < 0 else "no change"

        return {"change": change, "trend": trend}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
