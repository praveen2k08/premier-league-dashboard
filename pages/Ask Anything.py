import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(page_title="Ask About Any Player", page_icon="🔍")

# Title
st.title("🔍 Ask About Any Premier League Player")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("epl_player_stats_24_25.csv")
    return df

df = load_data()

# Search box
player_query = st.text_input("Enter a player name (e.g., Haaland, Saka, Rice)")

# Search logic
if player_query:
    player_query_lower = player_query.lower()
    result = df[df["Player Name"].str.lower().str.contains(player_query_lower)]

    if not result.empty:
        st.success(f"Found {len(result)} player(s) matching '{player_query}':")
        st.dataframe(result, use_container_width=True)
    else:
        st.error(f"No players found matching '{player_query}'. Try a different name.")