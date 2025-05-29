import streamlit as st
import yfinance as yf
import requests
import io

# 🌐 Page config
st.set_page_config(page_title="Market Briefing Assistant", page_icon="📈", layout="centered")

# 🎯 Title
st.markdown("""
# 📈 AI Market Briefing Assistant
Welcome, Portfolio Manager 👋  
Get live Asia Tech insights — in text and audio.
""")

st.markdown("---")

# 🧠 Market Summary Section
st.subheader("🧠 Morning Market Summary")

if st.button("📊 Get Market Summary"):
    with st.spinner("Generating market summary..."):
        try:
            res = requests.get("https://orchestrator-8bib.onrender.com/market-summary")
            summary = res.json().get("summary", "No summary available.")
            st.success("Summary Generated ✅")

            # 🔹 Styled block for summary
            st.markdown(f"""
    <div style='background-color:#ecf0f1;padding:15px;border-radius:10px;margin-top:10px;font-size:16px; color:#111827'>
    <b>📝 Summary:</b><br>{summary}
    </div>
""", unsafe_allow_html=True)


            st.markdown("---")
            st.markdown("🔊 **Voice Summary:**")

            voice_res = requests.post(
                "https://voice-agent-k0rf.onrender.com/speak-text",
                data={"summary": summary}
            )

            if voice_res.status_code == 200:
                audio_bytes = io.BytesIO(voice_res.content)
                st.audio(audio_bytes, format="audio/mp3")
            else:
                st.warning("Voice generation failed.")

        except Exception as e:
            st.error(f"Something went wrong: {e}")

# 🌏 Asia Tech Snapshot
st.markdown("---")
st.subheader("🌏 Asia Tech Snapshot")

if st.button("📊 Get Asia Tech Data"):
    res = requests.get("https://api-agent-l7np.onrender.com/exposure")
    if res.status_code == 200:
        data = res.json()
        st.markdown(f"**Total Allocation:** {data['asia_tech_allocation']}")
        st.markdown(f"**Yesterday:** {data['yesterday']}")
        st.markdown(f"**Change %:** {data['change_percent']}%")
    else:
        st.error("Failed to fetch Asia tech data.")

# 🔍 Custom Stock Tracker
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
