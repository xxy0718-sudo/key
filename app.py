import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import random
import requests

# ------------------------
# Page setup
# ------------------------
st.set_page_config(page_title="KOSPI200 Stock Recommendation System", layout="wide")

st.title("📈 KOSPI200 Stock Recommendation System")
st.caption("Easily understand the Korean stock market with AI-powered insights.")

# ------------------------
# Sidebar settings
# ------------------------
st.sidebar.header("⚙️ Analysis Settings")
num_stocks = st.sidebar.slider("Number of recommended stocks", 3, 10, 5)
min_volume = st.sidebar.number_input("Minimum trade volume", 0, 1000000, 100000)
run_analysis = st.sidebar.button("🚀 Start Analysis")

# ------------------------
# Dummy stock data generator
# ------------------------
def generate_fake_data(n=5):
    stock_names = ["Samsung Electronics", "Hyundai Motor", "Kakao", "NAVER", "SK Hynix",
                   "LG Chem", "POSCO", "Kia", "Samsung C&T", "KT&G"]
    data = []
    for i in range(n):
        name = random.choice(stock_names)
        price = random.randint(40000, 300000)
        score = round(random.uniform(6, 10), 1)
        recent_return = round(random.uniform(-5, 10), 1)
        volume = random.randint(min_volume, min_volume + 500000)
        data.append([name, price, score, recent_return, volume])
    df = pd.DataFrame(data, columns=["Stock", "Price (₩)", "Score", "Recent Return (%)", "Volume"])
    return df

# ------------------------
# Stock chart (plotly)
# ------------------------
def make_chart(stock_name):
    days = pd.date_range(end=pd.Timestamp.today(), periods=30)
    price = np.cumsum(np.random.randn(30)) + random.randint(50000, 150000)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=days, y=price, mode='lines+markers', name='Price'))
    fig.update_layout(title=f"{stock_name} - 30 Days Price Trend",
                      xaxis_title="Date",
                      yaxis_title="Price (₩)",
                      template="plotly_white",
                      height=300)
    return fig

# ------------------------
# Fake news summary (could be replaced with real API)
# ------------------------
def fake_news_summary(stock_name):
    summaries = [
        f"{stock_name} shows strong rebound after recent market correction.",
        f"Analysts expect {stock_name} to outperform due to solid earnings.",
        f"Investors are optimistic about {stock_name}'s expansion in AI sector.",
        f"{stock_name} faces temporary decline amid global uncertainty."
    ]
    return random.choice(summaries)

# ------------------------
# Main section
# ------------------------
if run_analysis:
    st.subheader("📊 Recommended Stocks")
    df = generate_fake_data(num_stocks)
    st.dataframe(df, use_container_width=True)

    for i, row in df.iterrows():
        st.markdown(f"### 🏆 {i+1}. {row['Stock']}")
        col1, col2 = st.columns([2, 3])

        with col1:
            st.metric(label="Current Price", value=f"{row['Price (₩)']:,}₩")
            st.metric(label="AI Score", value=f"{row['Score']} / 10")
            st.metric(label="Recent Return", value=f"{row['Recent Return (%)']}%")
            st.metric(label="Trade Volume", value=f"{row['Volume']:,}")

        with col2:
            fig = make_chart(row['Stock'])
            st.plotly_chart(fig, use_container_width=True)

        st.info(fake_news_summary(row['Stock']))
        st.markdown("---")

else:
    st.markdown("👈 Adjust settings on the sidebar and click **Start Analysis** to begin.")
