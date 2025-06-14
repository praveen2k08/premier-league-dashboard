import streamlit as st
import pandas as pd
import wikipedia

st.set_page_config(page_title="Ask Anything About a Player", page_icon="⚽")

st.title("⚽ Ask Anything About a Player")

@st.cache_data
def load_data():
    return pd.read_csv("epl_player_stats_24_25.csv")

df = load_data()

# Input
player_input = st.text_input("Search for a player name (even partial)")

# Filter logic
filtered = df[df["Player Name"].str.lower().str.contains(player_input.lower())] if player_input else pd.DataFrame()

if not filtered.empty:
    # If multiple players match, ask user to select
    if len(filtered) > 1:
        selected_name = st.selectbox("Multiple players found. Select one:", filtered["Player Name"].unique())
        player_data = filtered[filtered["Player Name"] == selected_name]
    else:
        selected_name = filtered["Player Name"].values[0]
        player_data = filtered

    st.subheader("📊 Player Stats")
    st.dataframe(player_data, use_container_width=True)

    # Wikipedia enhanced search
    try:
        search_results = wikipedia.search(selected_name)
        if search_results:
            best_match = search_results[0]
            summary = wikipedia.summary(best_match, sentences=2)
            page = wikipedia.page(best_match, auto_suggest=False)
            st.subheader("📖 Player Bio")
            st.write(summary)

            if page.images:
                st.image(page.images[0], width=250, caption=selected_name)
        else:
            st.warning("No matching Wikipedia page found.")
    except Exception as e:
        st.warning(f"Could not fetch Wikipedia info: {e}")

    # Key stat visuals
    st.subheader("⚡ Key Stats")
    col1, col2, col3 = st.columns(3)
    col1.metric("Goals", int(player_data['Goals'].values[0]))
    col2.metric("Assists", int(player_data['Assists'].values[0]))
    col3.metric("Minutes", int(player_data['Minutes'].values[0]))

else:
    if player_input:
        st.warning("No player found. Try another name.")