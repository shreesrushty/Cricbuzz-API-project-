# Cricbuzz-API-project-
🏏 **Cricbuzz Data Analysis Project** A cricket analytics project built using Python, PostgreSQL, SQL, and Streamlit. The project fetches live and recent match data from the Cricbuzz API, stores it in a database, performs SQL analysis, and displays insights through an interactive Streamlit dashboard with charts, KPIs, and match statistics.
# Cricbuzz Data Analysis Project

## Overview

This project is a Cricket Data Analysis Dashboard developed using Python, PostgreSQL, SQL, and Streamlit. The application fetches live, recent, and upcoming cricket match data using the Cricbuzz API, stores the data in PostgreSQL, performs SQL analysis, and visualizes insights through an interactive Streamlit dashboard.

The project demonstrates practical implementation of API integration, database management, SQL query analysis, data visualization, and dashboard development.

---

## Features

* Fetch live, recent, and upcoming cricket match data
* Store structured data in PostgreSQL database
* Perform SQL queries for cricket analytics
* Interactive Streamlit dashboard
* KPI metrics and charts
* Team performance analysis
* Match statistics and winning margins
* Auto-refresh dashboard functionality

---

## Technologies Used

| Technology   | Purpose                      |
| ------------ | ---------------------------- |
| Python       | Data fetching and processing |
| Cricbuzz API | Real-time cricket data       |
| PostgreSQL   | Database storage             |
| pgAdmin      | Database management          |
| Pandas       | Data manipulation            |
| Streamlit    | Dashboard creation           |
| Altair       | Data visualization           |
| SQL          | Data analysis                |
| VS Code      | Development environment      |

---

## Project Structure

```bash id="hh8hso"
Cricbuzz-Data-Analysis/
│
├── app.py
├── recent_matches.csv
├── live_matches.csv
├── upcoming_matches.csv
├── sql_queries.sql
├── requirements.txt
└── README.md
```

---

## Database Tables

### recent_matches

* team1
* team2
* t1_runs
* t1_wickets
* t2_runs
* t2_wickets
* status
* series

### live_matches

* team1
* team2
* t1_runs
* t2_runs
* status
* series

### upcoming_matches

* team1
* team2
* status
* series

---

## SQL Analysis Performed

The project includes multiple SQL queries such as:

* Display all recent matches
* Show IPL matches
* Count total matches
* Average runs scored
* Highest scoring matches
* Team-wise total runs
* Match winners
* Winning margins
* Close match analysis
* Series-wise match count
* Combine live, recent, and upcoming matches

---

## Dashboard Features

The Streamlit dashboard includes:

* KPI Metrics

  * Total Matches
  * Average Runs
  * Highest Score

* Charts

  * Team Runs Comparison
  * Series-wise Match Distribution
  * Winning Margin Analysis

* Match Tables

  * Recent Matches
  * Live Matches
  * Upcoming Matches

* Auto Refresh Functionality

---

## Key Insights

* IPL matches showed high-scoring trends
* Punjab Kings and Sunrisers Hyderabad performed strongly
* Several close matches indicated competitive gameplay
* Most analyzed matches belonged to IPL tournaments

---

## Limitations

* Limited historical data
* Player-level statistics not available
* Live API data may sometimes be empty
* Some advanced analytics limited by API data

---

## Future Enhancements

* Add player statistics analysis
* Integrate multiple cricket APIs
* Implement machine learning predictions
* Add advanced filters and search options
* Automate live data updates

---

## Conclusion

This project demonstrates real-world data analytics concepts using cricket match data. It combines API integration, SQL analysis, database management, and interactive dashboard visualization into a complete end-to-end data analytics project.

---


