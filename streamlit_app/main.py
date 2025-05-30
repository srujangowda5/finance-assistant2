import streamlit as st
import yfinance as yf
import requests
import io

# 🌐 Page config
st.set_page_config(page_title="Market Briefing Assistant", page_icon="📈", layout="centered")

# 🚧 Initial Toast - Whisper info
st.toast(
    "🚧 Voice Assistant using Whisper is disabled due to Render memory limits. Click '📊 Get Market Summary' to proceed.",
    icon="⚠️"
)

# 🎯 Title
st.markdown("""
# 📈 AI Market Briefing Assistant  
Welcome, Portfolio Manager 👋  
Get live Asia Tech insights — in text and audio.
""")

st.markdown("---")

# 🧠 Morning Market Summary
st.subheader("🧠 Morning Market Summary")

if st.button("📊 Get Market Summary"):
    st.toast("⚡ Waking up sleeping servers... please hold tight!", icon="⏳")
    with st.spinner("Generating market summary..."):
        try:
            res = requests.post("https://finance-assistant2-orchestrator-production.up.railway.app/market-summary")
            full_response = res.json()
            summary = full_response.get("summary", "No summary available.")
            
            if summary == "No summary available.":
                st.warning("🧊 Servers might be cold-starting. Please click again in a few seconds.")
            else:
                st.success("✅ Summary Generated")
                st.markdown(f"""
                    <div style='background-color:#ecf0f1;padding:15px;border-radius:10px;margin-top:10px;font-size:16px; color:#111827'>
                    <b>📝 Summary:</b><br>{summary}
                    </div>
                """, unsafe_allow_html=True)

                # 🔊 Voice Summary (TTS)
                st.markdown("---")
                st.subheader("🔊 Voice Summary")
                try:
                    voice_res = requests.post(
                        "https://finance-assistant2-voiceagent-production.up.railway.app/speak-text",
                        data={"summary": summary}
                    )
                    if voice_res.status_code == 200:
                        audio_bytes = io.BytesIO(voice_res.content)
                        st.audio(audio_bytes, format="audio/mp3")
                    else:
                        st.warning("Voice generation failed.")
                except Exception as e:
                    st.warning(f"Voice summary error: {e}")
        except Exception as e:
            st.error(f"⚠️ Something went wrong: {e}")
            st.info("🧊 Some agents may still be waking up. Please retry in 10–15 seconds.")

# 🌏 Asia Tech Snapshot
st.markdown("---")
st.subheader("🌏 Asia Tech Snapshot")

if st.button("📊 Get Asia Tech Data"):
    try:
        res = requests.get("https://api-agent-l7np.onrender.com/exposure")
        if res.status_code == 200:
            data = res.json()
            st.markdown(f"**Total Allocation:** {data['asia_tech_allocation']}")
            st.markdown(f"**Yesterday:** {data['yesterday']}")
            st.markdown(f"**Change %:** {data['change_percent']}%")
        else:
            st.error("Failed to fetch Asia tech data.")
    except Exception as e:
        st.error(f"Error: {e}")

# 🚀 Top 5 Gainers
st.markdown("---")
st.subheader("🚀 Top 5 Gainers Today")

if st.button("🔥 Show Top Stocks"):
    with st.spinner("Fetching top stock data..."):
        try:
            res = requests.get("https://top-stocks-agent.onrender.com/top-stocks")
            if res.status_code == 200:
                top_stocks = res.json().get("top_5_stocks", [])
                if not top_stocks:
                    st.warning("No stock data received.")
                else:
                    for stock in top_stocks:
                        st.markdown(f"- **{stock['symbol']}**: {stock['yesterday']} → {stock['today']} ({stock['change_pct']}%)")
                    st.success("Top stock data retrieved ✅")
            else:
                st.error("Failed to fetch top stocks.")
        except Exception as e:
            st.error(f"Error fetching top stocks: {e}")

# 🔍 Custom Tracker
st.markdown("---")
st.subheader("🔍 Custom Stock Tracker")

tickers_input = st.text_input("Enter comma-separated stock symbols (e.g., AAPL, TSLA, NVDA)")

if st.button("📥 Get Stock Data"):
    with st.spinner("Fetching data..."):
        try:
            symbols = [sym.strip().upper() for sym in tickers_input.split(",") if sym.strip()]
            if not symbols:
                st.warning("Please enter at least one valid ticker.")
            else:
                data = []
                for symbol in symbols:
                    stock = yf.Ticker(symbol)
                    hist = stock.history(period="2d")
                    if len(hist) == 2:
                        today = hist["Close"].iloc[1]
                        yesterday = hist["Close"].iloc[0]
                        change = round(((today - yesterday) / yesterday) * 100, 2)
                        data.append((symbol, round(yesterday, 2), round(today, 2), change))

                if not data:
                    st.warning("No data could be retrieved.")
                else:
                    st.markdown("#### 📈 Stock Performance:")
                    for sym, yest, today, change in data:
                        st.markdown(f"- **{sym}**: {yest} → {today} ({change}%)")
                    st.success("Custom stock data retrieved ✅")
        except Exception as e:
            st.error(f"Error: {e}")

# 📝 Footer
st.markdown("---")
st.markdown("*Built with FastAPI, OpenAI, Whisper, FAISS & Streamlit*")
st.markdown("👨‍💻 Developed by KH SRUJAN GOWDA &nbsp;&nbsp;|&nbsp;&nbsp;📎 [GitHub](https://github.com/srujangowda5)", unsafe_allow_html=True)
