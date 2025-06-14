import streamlit as st
import pandas as pd
import wikipedia

# Load your player dataset
@st.cache_data
def load_data():
    df = pd.read_csv("epl_player_stats_24_25.csv")
    return df

df = load_data()

st.title("⚽ Ask Anything About a Player")

player_name = st.text_input("Search for a player")

if player_name:
    # Filter data
    player_data = df[df['Player Name'].str.lower() == player_name.lower()]

    if not player_data.empty:
        # Show stats table
        st.subheader("📊 Player Stats")
        st.dataframe(player_data)

        # Try fetching from Wikipedia
        try:
            summary = wikipedia.summary(player_name, sentences=2)
            page = wikipedia.page(player_name, auto_suggest=False)
            image_url = page.images[0] if page.images else None

            st.subheader("🧠 Wikipedia Bio")
            st.write(summary)

            if image_url:
                st.image(image_url, width=200, caption=player_name)
        except Exception as e:
            st.warning(f"Could not fetch Wikipedia info: {e}")

        # KPIs
        st.subheader("⚡ Key Stats")
        col1, col2, col3 = st.columns(3)
        col1.metric("Goals", int(player_data['Goals'].values[0]))
        col2.metric("Assists", int(player_data['Assists'].values[0]))
        col3.metric("Minutes", int(player_data['Minutes'].values[0]))
    else:
        st.warning("Player not found. Please check spelling or try another name.")