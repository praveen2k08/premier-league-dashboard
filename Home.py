import streamlit as st
import pandas as pd

st.set_page_config(page_title="🏠 EPL Dashboard", layout="wide")

st.markdown("<h1 style='text-align: center;'>⚽ Welcome to Premier League 2024/25 Dashboard</h1>", unsafe_allow_html=True)
st.markdown("### 📊 Built with Python + Streamlit")

# Optional Image Banner
st.image("pl_logo.png", width=150)

st.markdown("""
Welcome to the **Premier League Player Stats Dashboard**!  
This interactive tool lets you explore player performance across goals, assists, passes, and more.

---

### 🧭 Features:
""")

# Feature Cards
col1, col2 = st.columns(2)
with col1:
    st.success("📈 Top Performers\n\nTrack the leading scorers and assist kings across the league.")
with col2:
    st.info("🧍 Player Comparison\n\nCompare any two players side-by-side across 15+ stats.")

st.markdown("---")

# Load sample data
df = pd.read_csv("epl_player_stats_24_25.csv")

st.subheader("👀 Sample of the Dataset")
st.dataframe(df.head())

st.markdown("---")
st.markdown("<small>Made with ❤️ using Streamlit</small>", unsafe_allow_html=True)