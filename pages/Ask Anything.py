import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Ask Anything", page_icon="⚽")
st.title("⚽ Ask Anything About a Player")

@st.cache_data
def load_data():
    return pd.read_csv("epl_player_stats_24_25.csv")

df = load_data()

player_input = st.text_input("Search for a player (partial match)")
filtered = df[df["Player Name"].str.lower().str.contains(player_input.lower())] if player_input else pd.DataFrame()

if not filtered.empty:
    if len(filtered) > 1:
        selected_name = st.selectbox("Multiple players found. Choose one:", filtered["Player Name"].unique())
        player_data = filtered[filtered["Player Name"] == selected_name]
    else:
        selected_name = filtered["Player Name"].iloc[0]
        player_data = filtered

    st.subheader("📊 Player Stats")
    st.dataframe(player_data, use_container_width=True)

    # 🧠 TheSportsDB API fetch
    api_key = st.secrets["SPORTSDB_API_KEY"]
    player_name_clean = selected_name.replace(" ", "%20")
    player_url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/searchplayers.php?p={player_name_clean}"
    player_resp = requests.get(player_url).json()

    if player_resp.get("player"):
        p = player_resp["player"][0]
        pid = p.get("idPlayer")

        # 🔹 Player Info
        st.subheader(f"📖 {p.get('strPlayer')} Profile")

        col1, col2 = st.columns([1, 2])
        if p.get("strCutout") or p.get("strThumb"):
            col1.image(p.get("strCutout") or p.get("strThumb"), width=200)

        col2.markdown(f"""
        - **Team:** {p.get('strTeam', '—')}
        - **Nationality:** {p.get('strNationality', '—')}
        - **Born:** {p.get('dateBorn', '—')} in {p.get('strBirthLocation', '—')}
        - **Position:** {p.get('strPosition', '—')}
        - **Shirt Number:** {p.get('strNumber', '—')}
        - **Height:** {p.get('strHeight', '—')}  
        - **Weight:** {p.get('strWeight', '—')}
        """)

        # 🔹 Bio
        if p.get("strDescriptionEN"):
            st.write(p["strDescriptionEN"])
        else:
            st.write("No bio available.")

        # 🔹 Social
        socials = []
        for k, icon in [("strTwitter", "🐦"), ("strInstagram", "📸"), ("strFacebook", "📘")]:
            if p.get(k):
                socials.append(f"[{icon}]({p[k]})")
        if socials:
            st.markdown(" ".join(socials))

        # 🔹 Team info
        if p.get("strTeam"):
            team_url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/searchteams.php?t={p['strTeam'].replace(' ', '%20')}"
            team_resp = requests.get(team_url).json()
            if team_resp.get("teams"):
                team = team_resp["teams"][0]
                st.subheader(f"🏟️ {team.get('strTeam')} Club Info")
                st.markdown(f"""
                - **Stadium:** {team.get('strStadium', '—')}
                - **Country:** {team.get('strCountry', '—')}
                - **League:** {team.get('strLeague', '—')}
                """)
                if team.get("strTeamBadge"):
                    st.image(team["strTeamBadge"], width=100)

        # 🔹 Former Teams
        former_url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/lookupformerteams.php?id={pid}"
        former_resp = requests.get(former_url).json()
        if former_resp.get("formerteams"):
            st.subheader("📋 Former Teams")
            former_teams = [t["strTeam"] for t in former_resp["formerteams"]]
            st.write(", ".join(former_teams))

        # 🔹 Honors
        honors_url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/lookupplayerhonours.php?id={pid}"
        honors_resp = requests.get(honors_url).json()
        if honors_resp.get("honours"):
            st.subheader("🏆 Honors")
            honors = [f"{h['strHonour']} ({h['strSeason']})" for h in honors_resp["honours"]]
            st.write(", ".join(honors))

    else:
        st.warning("Could not find player info in TheSportsDB.")

    # 🔹 Key Stats from CSV
    st.subheader("⚡ Key Stats")
    col1, col2, col3 = st.columns(3)
    col1.metric("Goals", int(player_data.Goals.values[0]))
    col2.metric("Assists", int(player_data.Assists.values[0]))
    col3.metric("Minutes", int(player_data.Minutes.values[0]))

elif player_input:
    st.warning("No matching player found. Try again.")