from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

# Choose your top stocks (you can adjust or fetch dynamically later)
STOCKS = ["AAPL", "NVDA", "MSFT", "GOOGL", "TSLA", "META", "AMZN", "NFLX", "INTC", "AMD"]

@app.get("/")
def root():
    return {"message": "Top Stocks Agent is live. Use /top-stocks to get data."}

@app.get("/top-stocks")
def get_top_stocks():
    results = []

    for symbol in STOCKS:
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="2d")

            if len(hist) < 2:
                continue  # skip if not enough data

            today = hist["Close"].iloc[-1]
            yesterday = hist["Close"].iloc[-2]
            change = round(((today - yesterday) / yesterday) * 100, 2)

            results.append({
                "symbol": symbol,
                "yesterday": round(yesterday, 2),
                "today": round(today, 2),
                "change_pct": change
            })

        except Exception as e:
            results.append({"symbol": symbol, "error": str(e)})

    # Sort by highest gainers
    top = sorted(results, key=lambda x: x.get("change_pct", -999), reverse=True)
    return {"top_5_stocks": top[:5]}
