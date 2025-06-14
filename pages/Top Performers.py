import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Top Performers", layout="wide")
st.title("⚽ Top Performers - Premier League 24/25")

# Load data
df = pd.read_csv("epl_player_stats_24_25.csv")
df = df.dropna(subset=["Goals", "Assists"])

# Filters
clubs = df["Club"].dropna().unique()
positions = ['All'] + sorted(df["Position"].dropna().unique().tolist())
nationalities = df["Nationality"].dropna().unique()

# Club filter
selected_clubs = st.multiselect("🏟️ Filter by Club", clubs)
if selected_clubs:
    df = df[df["Club"].isin(selected_clubs)]

# Position filter with 'All' option
selected_position = st.selectbox("🎯 Select Position", positions)
if selected_position != 'All':
    df = df[df["Position"] == selected_position]

# Nationality filter
selected_nationalities = st.multiselect("🌍 Filter by Nationality", nationalities)
if selected_nationalities:
    df = df[df["Nationality"].isin(selected_nationalities)]

# Minutes slider
min_minutes = int(df["Minutes"].min())
max_minutes = int(df["Minutes"].max())
minutes_range = st.slider("⏱️ Minutes Played", min_minutes, max_minutes, (min_minutes, max_minutes))
df = df[(df["Minutes"] >= minutes_range[0]) & (df["Minutes"] <= minutes_range[1])]

# KPI Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Players", df["Player Name"].nunique())
with col2:
    st.metric("Total Goals", int(df["Goals"].sum()))
with col3:
    st.metric("Avg Passes", round(df["Passes"].mean(), 2))

# Top Goal Scorers
st.subheader(f"🔥 Top 10 Goal Scorers - {selected_position if selected_position != 'All' else 'All Positions'}")
top_goals = df.sort_values("Goals", ascending=False).head(10)
st.dataframe(top_goals[["Player Name", "Club", "Goals"]].reset_index(drop=True))
st.altair_chart(
    alt.Chart(top_goals).mark_bar().encode(
        x=alt.X("Goals:Q", sort="-x"),
        y=alt.Y("Player Name:N", sort="-x"),
        tooltip=["Player Name", "Club", "Goals"]
    ).properties(width=600, height=400),
    use_container_width=True
)

# Top Assisters
st.subheader(f"🎯 Top 10 Assisters - {selected_position if selected_position != 'All' else 'All Positions'}")
top_assists = df.sort_values("Assists", ascending=False).head(10)
st.dataframe(top_assists[["Player Name", "Club", "Assists"]].reset_index(drop=True))
st.altair_chart(
    alt.Chart(top_assists).mark_bar(color="orange").encode(
        x=alt.X("Assists:Q", sort="-x"),
        y=alt.Y("Player Name:N", sort="-x"),
        tooltip=["Player Name", "Club", "Assists"]
    ).properties(width=600, height=400),
    use_container_width=True
)