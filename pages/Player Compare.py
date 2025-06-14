import streamlit as st
import pandas as pd

st.set_page_config(page_title="Player Compare", layout="wide")
st.title("🧍 Player Comparison Tool")

df = pd.read_csv("epl_player_stats_24_25.csv")

all_players = df["Player Name"].dropna().unique()
player1 = st.selectbox("Select First Player", all_players, key="player1")
player2 = st.selectbox("Select Second Player", all_players, key="player2")

if player1 != player2:
    player1_data = df[df["Player Name"] == player1].reset_index(drop=True)
    player2_data = df[df["Player Name"] == player2].reset_index(drop=True)

    compare_cols = [
        "Club", "Position", "Appearances", "Minutes", "Goals", "Assists",
        "Shots", "Passes", "Successful Passes", "Passes%", "Touches",
        "Ground Duels", "gDuels Won", "gDuels %", "Yellow Cards", "Red Cards"
    ]

    comparison_df = pd.DataFrame({
        "Stat": compare_cols,
        player1: player1_data[compare_cols].iloc[0].values,
        player2: player2_data[compare_cols].iloc[0].values
    })

    st.dataframe(comparison_df)
else:
    st.warning("Please select two different players to compare.")