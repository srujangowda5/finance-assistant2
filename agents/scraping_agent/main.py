from fastapi import FastAPI
from typing import Dict, List

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Scraping Agent is live"}

@app.get("/earnings", response_model=Dict[str, List[str]])
def get_earnings_surprises():
    # Simulated example (later can replace with BeautifulSoup/requests scraping)
    surprises = [
        "TSMC beat estimates by 4%",
        "Samsung missed by 2%",
        "Infosys exceeded expectations with 10% YoY revenue growth"
    ]
    return {"surprises": surprises}
