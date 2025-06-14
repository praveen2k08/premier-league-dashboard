import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Ask Anything About a Player", page_icon="⚽")
st.title("⚽ Ask Anything About a Player")

@st.cache_data
def load_data():
    return pd.read_csv("epl_player_stats_24_25.csv")

df = load_data()

player_input = st.text_input("Search for a player name (even partial)")

filtered = df[df["Player Name"].str.lower().str.contains(player_input.lower())] if player_input else pd.DataFrame()

if not filtered.empty:
    if len(filtered) > 1:
        selected_name = st.selectbox("Multiple players found. Select one:", filtered["Player Name"].unique())
        player_data = filtered[filtered["Player Name"] == selected_name]
    else:
        selected_name = filtered["Player Name"].values[0]
        player_data = filtered

    st.subheader("📊 Player Stats")
    st.dataframe(player_data, use_container_width=True)

    # TheSportsDB API integration
    try:
        player_name_clean = selected_name.replace(" ", "%20")
        api_key = st.secrets["SPORTSDB_API_KEY"]
        url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/searchplayers.php?p={player_name_clean}"
        response = requests.get(url)
        data = response.json()

        if data and data["player"]:
            player = data["player"][0]
            st.subheader("📖 Player Bio")
            st.write(player.get("strDescriptionEN", "No bio available."))

            if player.get("strCutout"):
                st.image(player["strCutout"], width=250, caption=selected_name)
            elif player.get("strThumb"):
                st.image(player["strThumb"], width=250, caption=selected_name)
        else:
            st.warning("No player info found in TheSportsDB.")
    except Exception as e:
        st.warning(f"Error fetching SportsDB info: {e}")

    st.subheader("⚡ Key Stats")
    col1, col2, col3 = st.columns(3)
    col1.metric("Goals", int(player_data['Goals'].values[0]))
    col2.metric("Assists", int(player_data['Assists'].values[0]))
    col3.metric("Minutes", int(player_data['Minutes'].values[0]))
else:
    if player_input:
        st.warning("No player found. Try another name.")