import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import yfinance as yf
import random

# ------------------------
# Page setup
# ------------------------
st.set_page_config(page_title="KOSPI200 Stock Recommendation System", layout="wide")

st.title("📈 KOSPI200 Stock Recommendation System")
st.caption("Analyze real-time Korean stocks using Yahoo Finance API")

# ------------------------
# Sidebar: API authentication (symbolic)
# ------------------------
st.sidebar.header("🔑 API Authentication")
api_key = st.sidebar.text_input("Enter your API Key (optional)", type="password")
if api_key:
    st.sidebar.success("✅ API Key successfully added!")
else:
    st.sidebar.info("ℹ️ Using public Yahoo Finance API (no key required)")

# ------------------------
# Sidebar: Analysis settings
# ------------------------
st.sidebar.header("⚙️ Analysis Settings")
num_stocks = st.sidebar.slider("Number of recommended stocks", 3, 10, 5)
run_analysis = st.sidebar.button("🚀 Start Analysis")

# ------------------------
# Define some KOSPI200 stock symbols (Yahoo format)
# ------------------------
kospi_symbols = {
    "Samsung Electronics": "005930.KS",
    "SK Hynix": "000660.KS",
    "Hyundai Motor": "005380.KS",
    "Kia": "000270.KS",
    "LG Chem": "051910.KS",
    "POSCO Holdings": "005490.KS",
    "NAVER": "035420.KS",
    "Kakao": "035720.KS",
    "Samsung Biologics": "207940.KS",
    "LG Energy Solution": "373220.KS"
}

# ------------------------
# Function: fetch data from Yahoo Finance
# ------------------------
@st.cache_data
def fetch_stock_data(symbol, days=30):
    data = yf.download(symbol, period=f"{days}d", interval="1d", progress=False)
    return data

# ------------------------
# Function: make chart
# ------------------------
def make_chart(df, stock_name):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines+markers', name='Close'))
    fig.update_layout(
        title=f"{stock_name} - Last 30 Days Price Trend",
        xaxis_title="Date",
        yaxis_title="Price (₩)",
        template="plotly_white",
        height=300
    )
    return fig

# ------------------------
# Main logic
# ------------------------
if run_analysis:
    st.subheader("📊 Recommended KOSPI200 Stocks")

    selected_stocks = random.sample(list(kospi_symbols.items()), num_stocks)

    for i, (name, symbol) in enumerate(selected_stocks, 1):
        st.markdown(f"### 🏆 {i}. {name}")

        try:
            df = fetch_stock_data(symbol)
            if df.empty:
                st.warning(f"No data found for {name}.")
                continue

            current_price = round(df['Close'].iloc[-1], 2)
            change_percent = round(((df['Close'].iloc[-1] - df['Close'].iloc[-2]) / df['Close'].iloc[-2]) * 100, 2)
            score = round(random.uniform(6, 10), 1)

            col1, col2 = st.columns([2, 3])
            with col1:
                st.metric(label="Current Price", value=f"{current_price:,} ₩", delta=f"{change_percent}%")
                st.metric(label="AI Score", value=f"{score} / 10")
                st.metric(label="Ticker", value=symbol)
            with col2:
                fig = make_chart(df, name)
                st.plotly_chart(fig, use_container_width=True)

            # Simulated news
            st.info(f"{name} shows {random.choice(['strong recovery', 'stable growth', 'temporary volatility'])} based on recent trends.")

        except Exception as e:
            st.error(f"Error loading {name}: {e}")

        st.markdown("---")

else:
    st.markdown("👈 Adjust settings on the sidebar and click **Start Analysis** to begin.")
