import streamlit as st
import pandas as pd
import wikipedia

# Page config
st.set_page_config(page_title="Ask About Any Player", page_icon="🧠")

st.title("🧠 Ask About Any Premier League Player")

@st.cache_data
def load_data():
    return pd.read_csv("epl_player_stats_24_25.csv")

df = load_data()

# Input
player_query = st.text_input("Enter a player name:")

if player_query:
    player_query_lower = player_query.lower()
    player_data = df[df["Player Name"].str.lower().str.contains(player_query_lower)]

    if not player_data.empty:
        # Show player stats
        st.subheader("📊 Player Stats")
        st.dataframe(player_data, use_container_width=True)

        # Get the first matching name for Wikipedia
        try:
            wiki_summary = wikipedia.summary(player_query, sentences=2)
            page = wikipedia.page(player_query, auto_suggest=False)
            image_url = page.images[0] if page.images else None

            st.subheader("📖 Wikipedia Bio")
            st.write(wiki_summary)

            if image_url:
                st.image(image_url, width=250, caption=player_query)
        except Exception as e:
            st.warning("Wikipedia info not found or unclear name. Try full name.")
    else:
        st.error("Player not found in dataset. Try a different name.")