from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("❌ OPENAI_API_KEY not found!")
else:
    print("✅ OpenAI Key loaded")

client = openai.OpenAI(api_key=OPENAI_API_KEY)
app = FastAPI()

class NarrativeRequest(BaseModel):
    change: int
    trend: str
    sentiment: str = "neutral"
    highlights: str = ""

@app.get("/")
def root():
    return {"message": "Language Agent is live. Use POST /narrative"}

@app.post("/narrative")
async def generate_narrative(request: NarrativeRequest):
    prompt = f"""
You are a professional financial assistant. Write a concise one-line summary for a portfolio manager using all the inputs below.

Inputs:
- Change in Asia tech exposure: {request.change}% ({request.trend})
- Regional Sentiment: {request.sentiment}
- Earnings Highlights:
{request.highlights}

Rules:
- Include all earnings surprises mentioned.
- Do not skip any company.
- Output should be one sentence only.
"""
    print("📝 Prompt to GPT:\n", prompt)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a financial analyst assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        summary = response.choices[0].message.content.strip()
        print("✅ GPT Response:", summary)
        return {"narrative": summary}
    except Exception as e:
        print("❌ OpenAI error:", str(e))
        return {"error": str(e)}
