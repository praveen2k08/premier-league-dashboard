import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ask About Any Player", page_icon="🔍")
st.title("🔍 Ask About Any Premier League Player")

@st.cache_data
def load_data():
    return pd.read_csv("epl_player_stats_24_25.csv")

df = load_data()

player_query = st.text_input("Enter a player name (e.g., Haaland, Saka, Rice)")

if player_query:
    result = df[df["Player Name"].str.lower().str.contains(player_query.lower())]

    if not result.empty:
        st.success(f"Found {len(result)} result(s):")
        st.dataframe(result, use_container_width=True)
    else:
        st.error("No player found. Try full name or another keyword.")