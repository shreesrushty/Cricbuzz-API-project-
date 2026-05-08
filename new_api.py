import requests
import pandas as pd

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
    "X-RapidAPI-Key": "2c62872599msh1f656194e14f7dap1787c2jsn68927f41004e",
    "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.json()

records = []

for type_match in data.get("typeMatches", []):
    for series_match in type_match.get("seriesMatches", []):

        series = series_match.get("seriesAdWrapper")
        if not series:
            continue

        series_name = series.get("seriesName", "")

        if "Indian Premier League" not in series_name and "ICC" not in series_name:
            continue

        for match in series.get("matches", []):

            info = match.get("matchInfo", {})
            score = match.get("matchScore", {})

            team1 = info.get("team1", {}).get("teamName", "NA")
            team2 = info.get("team2", {}).get("teamName", "NA")

            t1_runs = score.get("team1Score", {}).get("inngs1", {}).get("runs", 0)
            t1_wkts = score.get("team1Score", {}).get("inngs1", {}).get("wickets", 0)

            t2_runs = score.get("team2Score", {}).get("inngs1", {}).get("runs", 0)
            t2_wkts = score.get("team2Score", {}).get("inngs1", {}).get("wickets", 0)

            status = info.get("status", "")

            records.append([
                team1, team2,
                t1_runs, t1_wkts,
                t2_runs, t2_wkts,
                status, series_name
            ])

df = pd.DataFrame(records, columns=[
    "Team1", "Team2",
    "T1_Runs", "T1_Wickets",
    "T2_Runs", "T2_Wickets",
    "Status", "Series"
])

df.to_csv("C:/Users/Windows 10/Documents/recent_matches.csv", index=False)

print("Recent matches saved")
print("Rows:", len(df))




import requests
import pandas as pd

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/upcoming"

headers = {
    "X-RapidAPI-Key": "2c62872599msh1f656194e14f7dap1787c2jsn68927f41004e",
    "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Error:", response.status_code)
    exit()

data = response.json()

records = []

for type_match in data.get("typeMatches", []):
    for series_match in type_match.get("seriesMatches", []):

        series = series_match.get("seriesAdWrapper")
        if not series:
            continue

        series_name = series.get("seriesName", "")

        if "Indian Premier League" not in series_name and "ICC" not in series_name:
            continue

        for match in series.get("matches", []):

            info = match.get("matchInfo", {})

            team1 = info.get("team1", {}).get("teamName", "NA")
            team2 = info.get("team2", {}).get("teamName", "NA")
            status = info.get("status", "")

            records.append([
                team1, team2, status, series_name
            ])

df = pd.DataFrame(records, columns=[
    "Team1", "Team2", "Status", "Series"
])

df.to_csv("C:/Users/Windows 10/Documents/upcoming_matches.csv", index=False)

print("Upcoming matches saved")
print("Rows:", len(df))

import requests
import pandas as pd

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

headers = {
    "X-RapidAPI-Key": "2c62872599msh1f656194e14f7dap1787c2jsn68927f41004e",
    "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Error:", response.status_code)
    exit()

data = response.json()

records = []

for type_match in data.get("typeMatches", []):
    for series_match in type_match.get("seriesMatches", []):

        series = series_match.get("seriesAdWrapper")
        if not series:
            continue

        series_name = series.get("seriesName", "")

        if "Indian Premier League" not in series_name and "ICC" not in series_name:
            continue

        for match in series.get("matches", []):

            info = match.get("matchInfo", {})
            score = match.get("matchScore", {})

            team1 = info.get("team1", {}).get("teamName", "NA")
            team2 = info.get("team2", {}).get("teamName", "NA")

            t1_runs = score.get("team1Score", {}).get("inngs1", {}).get("runs", 0)
            t2_runs = score.get("team2Score", {}).get("inngs1", {}).get("runs", 0)

            status = info.get("status", "")

            records.append([
                team1, team2, t1_runs, t2_runs, status, series_name
            ])

df = pd.DataFrame(records, columns=[
    "Team1", "Team2", "T1_Runs", "T2_Runs", "Status", "Series"
])

df.to_csv("C:/Users/Windows 10/Documents/live_matches.csv", index=False)

print("Live matches saved")
print("Rows:", len(df))