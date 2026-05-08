import streamlit as st
import pandas as pd
import altair as alt
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Cricket Dashboard", layout="wide")

st.title("Cricket Analytics Dashboard")

# AUTO REFRESH EVERY 3 MINUTES (180000 ms)
st_autorefresh(interval=180000, key="refresh")

# LOAD DATA
recent = pd.read_csv("C:/Users/Windows 10/Documents/LABMENTIX PROJECTS/new cricbuzz/recent_matches.csv")
upcoming = pd.read_csv("C:/Users/Windows 10/Documents/LABMENTIX PROJECTS/new cricbuzz/upcoming_matches.csv")
live = pd.read_csv("C:/Users/Windows 10/Documents/LABMENTIX PROJECTS/new cricbuzz/live_matches.csv")

# ---------------- KPI ----------------
st.subheader("Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Matches", len(recent))
col2.metric("Avg Team1 Runs", int(recent["T1_Runs"].mean()))
col3.metric("Avg Team2 Runs", int(recent["T2_Runs"].mean()))
col4.metric("Upcoming Matches", len(upcoming))

st.divider()

# ---------------- TABLE ----------------
st.subheader("Match Data Table")
st.dataframe(recent)

st.divider()

# ---------------- BAR CHART 1 ----------------
st.subheader("Team1 Runs per Match")

bar1 = alt.Chart(recent).mark_bar().encode(
    x="Team1",
    y="T1_Runs",
    color="Team1"
)

st.altair_chart(bar1, use_container_width=True)

st.divider()

# ---------------- BAR CHART 2 ----------------
st.subheader("Team2 Runs per Match")

bar2 = alt.Chart(recent).mark_bar().encode(
    x="Team2",
    y="T2_Runs",
    color="Team2"
)

st.altair_chart(bar2, use_container_width=True)

st.divider()

# ---------------- PIE CHART ----------------
st.subheader("Matches by Series")

pie_data = recent["Series"].value_counts().reset_index()
pie_data.columns = ["Series", "Count"]

pie = alt.Chart(pie_data).mark_arc().encode(
    theta="Count",
    color="Series"
)

st.altair_chart(pie, use_container_width=True)

st.divider()

# ---------------- LIVE ----------------
st.subheader("Live Matches")

if live.empty:
    st.warning("No live matches available")
else:
    st.dataframe(live)

st.divider()

# ---------------- UPCOMING ----------------
st.subheader("Upcoming Matches")

if upcoming.empty:
    st.warning("No upcoming matches")
else:
    st.dataframe(upcoming)