CREATE TABLE recent_matches (
    id SERIAL PRIMARY KEY,
    team1 TEXT,
    team2 TEXT,
    t1_runs INT,
    t1_wickets INT,
    t2_runs INT,
    t2_wickets INT,
    status TEXT,
    series TEXT
);


CREATE TABLE live_matches (
    id SERIAL PRIMARY KEY,
    team1 TEXT,
    team2 TEXT,
    t1_runs INT,
    t2_runs INT,
    status TEXT,
    series TEXT
);


CREATE TABLE upcoming_matches (
    id SERIAL PRIMARY KEY,
    team1 TEXT,
    team2 TEXT,
    status TEXT,
    series TEXT
);

SELECT * FROM recent_matches;
SELECT * FROM live_matches;
SELECT * FROM upcoming_matches;

CREATE VIEW all_matches AS
SELECT team1, team2, status, series, t1_runs, t2_runs
FROM recent_matches

UNION ALL

SELECT team1, team2, status, series, t1_runs, t2_runs
FROM live_matches

UNION ALL

SELECT team1, team2, status, series, NULL AS t1_runs, NULL AS t2_runs
FROM upcoming_matches;




SELECT * FROM recent_matches;

SELECT *
FROM recent_matches
WHERE series LIKE '%Premier League%';

SELECT COUNT(*) AS total_matches
FROM recent_matches;

SELECT AVG(t1_runs) AS avg_team1_runs
FROM recent_matches;

SELECT AVG(t2_runs) AS avg_team2_runs
FROM recent_matches;

SELECT *
FROM recent_matches
WHERE t1_runs > t2_runs;


SELECT *
FROM recent_matches
WHERE t2_runs > t1_runs;

SELECT * FROM upcoming_matches;


SELECT team1, team2, (t1_runs + t2_runs) AS total_runs
FROM recent_matches
ORDER BY total_runs DESC
LIMIT 1;

SELECT series, COUNT(*) AS total_matches
FROM recent_matches
GROUP BY series;


SELECT team1, team2,
CASE
    WHEN t1_runs > t2_runs THEN team1
    WHEN t2_runs > t1_runs THEN team2
    ELSE 'Tie'
END AS winner
FROM recent_matches;

SELECT winner, COUNT(*) AS total_wins
FROM (
    SELECT 
        CASE
            WHEN t1_runs > t2_runs THEN team1
            WHEN t2_runs > t1_runs THEN team2
        END AS winner
    FROM recent_matches
) AS win_data
GROUP BY winner
ORDER BY total_wins DESC;

SELECT *
FROM recent_matches
WHERE ABS(t1_runs - t2_runs) < 20;


SELECT team, SUM(runs) AS total_runs
FROM (
    SELECT team1 AS team, t1_runs AS runs FROM recent_matches
    UNION ALL
    SELECT team2 AS team, t2_runs AS runs FROM recent_matches
) AS all_runs
GROUP BY team
ORDER BY total_runs DESC;

SELECT MAX(t1_runs) AS highest_team1_score
FROM recent_matches;

SELECT MAX(t2_runs) AS highest_team2_score
FROM recent_matches;

SELECT team1, team2,
ABS(t1_runs - t2_runs) AS margin
FROM recent_matches
ORDER BY margin DESC;


SELECT team1, team2, status, series FROM recent_matches
UNION ALL
SELECT team1, team2, status, series FROM live_matches
UNION ALL
SELECT team1, team2, status, series FROM upcoming_matches;