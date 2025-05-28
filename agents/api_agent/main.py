from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

#from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API Agent is running"}

ASIA_TECH = ["TSM", "INFY", "BABA", "JD", "NTES"]

@app.get("/exposure")
def get_asia_tech_exposure():
    total_today = 0
    total_yesterday = 0

    for ticker in ASIA_TECH:
        try:
            data = yf.Ticker(ticker).history(period="2d")
            if len(data) < 2:
                continue
            total_yesterday += data["Close"].iloc[0]
            total_today += data["Close"].iloc[1]
        except:
            continue

    change = total_today - total_yesterday
    change_pct = round((change / total_yesterday) * 100, 2)

    return {
        "asia_tech_allocation": round(total_today, 2),
        "yesterday": round(total_yesterday, 2),
        "change_percent": change_pct
    }
