import streamlit as st
import pandas as pd
import random

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="KOSPI200 Stock Recommendation System", layout="wide")

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.header("⚙️ Settings")

num_stocks = st.sidebar.slider("Number of recommended stocks", 3, 10, 5)
min_volume = st.sidebar.number_input("Minimum trading volume", value=100, step=10)

if st.sidebar.button("Start Analysis"):
    st.session_state["analyze"] = True

if st.sidebar.button("Reset"):
    st.session_state["analyze"] = False

# -------------------------------
# Title
# -------------------------------
st.title("📊 KOSPI200 Stock Recommendation System")
st.markdown("Easily understandable stock analysis tool for beginners and professionals.")

# -------------------------------
# Fake Data Generator
# -------------------------------
def generate_fake_data(n):
    companies = ["NAVER", "Samsung Electronics", "Kakao", "Hyundai Motors", "LG Chem",
                 "POSCO", "SK Hynix", "Kia", "AmorePacific", "Celltrion"]
    data = []
    for i in range(n):
        company = random.choice(companies)
        price = random.randint(50000, 300000)
        score = round(random.uniform(6.5, 9.5), 1)
        recent_return = round(random.uniform(-3, 5), 1)
        volume = random.randint(50, 500)
        data.append({
            "rank": i + 1,
            "company": company,
            "price": price,
            "score": score,
            "recent_return": recent_return,
            "volume": volume
        })
    return pd.DataFrame(data)

# -------------------------------
# Analysis Results
# -------------------------------
if st.session_state.get("analyze", False):
    st.subheader(f"🏅 Top {num_stocks} Recommended Stocks")
    df = generate_fake_data(num_stocks)

    cols = st.columns(num_stocks)
    for i, col in enumerate(cols):
        with col:
            row = df.iloc[i]
            st.markdown(f"### {row['rank']}. {row['company']}")
            st.metric("Current Price", f"₩{row['price']:,}")
            st.metric("Score", f"{row['score']}/10")
            st.metric("Recent Return", f"{row['recent_return']}%")
            st.write("**Key Insights:**")
            st.markdown("- ✅ Strong short-term momentum")
            st.markdown("- ✅ High trading volume")
            st.markdown("- ✅ Positive investor sentiment")
else:
    st.info("Please set analysis conditions on the left and click **Start Analysis**.")

# -------------------------------
# Market Summary Section
# -------------------------------
st.divider()
st.subheader("📈 Market Summary")
st.write("""
The KOSPI200 index has shown mild fluctuations today. 
Technology and automotive sectors lead the gains, while chemical and energy stocks face slight declines.
""")

# Example table
market_data = pd.DataFrame({
    "Sector": ["Technology", "Automobile", "Chemicals", "Finance", "Energy"],
    "Change (%)": [1.8, 1.2, -0.4, 0.5, -0.7]
})
st.dataframe(market_data, use_container_width=True)

# -------------------------------
# News Section
# -------------------------------
st.divider()
st.subheader("📰 Recent Market News")
news_items = [
    "KOSPI gains 1.2% as global markets rally.",
    "Foreign investors continue net buying of blue-chip stocks.",
    "Analysts expect tech rebound amid AI demand growth.",
    "Won strengthens slightly against USD amid policy optimism."
]
for news in news_items:
    st.markdown(f"- {news}")

# -------------------------------
# Footer
# -------------------------------
st.divider()
st.markdown(
    "<p style='text-align:center; color:gray;'>© 2025 Sungkyunkwan University | Developed for educational purposes.</p>",
    unsafe_allow_html=True
)
