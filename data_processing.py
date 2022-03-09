import constants as CONSTANTS
import numpy as np
import pandas as pd

# Read and clean data
# Standing
standing = pd.read_json(CONSTANTS.STANDING_OUTPUT_PATH)
standing.info()
standing["games_played_team"] = standing["losses"] + standing["wins"]
print(standing.head())

# Basic stats
basic_stats = pd.read_json(CONSTANTS.PLAYER_BASIC_STATS_OUTPUT_PATH)
# Add games played by team column to calculate minimum stats qualification
basic_stats = basic_stats.merge(standing[["team", "games_played_team"]], on="team")
basic_stats.set_index("name", inplace = True)
basic_stats.info()

# Advanced stats
advanced_stats = pd.read_json(CONSTANTS.PLAYER_ADVANCED_STATS_OUTPUT_PATH)
# print(advanced_stats.info())

# Data analytics
# Minimum qualifications for NBA stats leaders (https://www.nba.com/stats/help/statminimums/)
# 1. Who has the most points per game? (Play at least 70% of team's games)
points = basic_stats.loc[:, ["points", "games_played", "games_played_team"]]
points["qualify"] = points["games_played"] >= points["games_played_team"] * CONSTANTS.MINIMUM_PERCENTAGE
points = points[points["qualify"] == True]

points["points_per_game"] = points["points"] / points["games_played"]
points = points.sort_values(by="points_per_game", ascending=False)
print(points.head())

most_points_per_game_player = points.iloc[0].name
print(most_points_per_game_player)

# 2. Who has the most assists per game?
assists = basic_stats.loc[:, ["assists", "games_played", "games_played_team"]]
print(assists.sort_values(by="assists", ascending=False).head(10))
assists["qualify"] = assists["games_played"] >= assists["games_played_team"] * CONSTANTS.MINIMUM_PERCENTAGE
assists = assists[assists["qualify"] == True]

assists["assists_per_game"] = assists["assists"] / assists["games_played"]
assists = assists.sort_values(by="assists_per_game", ascending=False)
print(assists.head())
most_assists_per_game_player = assists.iloc[0].name
print(most_assists_per_game_player)

# TO-DO: Some players have multiple rows because they were traded in the season
print(basic_stats.loc["James Harden"])

# 3. Who has the most rebounds per game?
basic_stats["rebounds"] = basic_stats["defensive_rebounds"] + basic_stats["offensive_rebounds"]
rebounds = basic_stats.loc[:, ["rebounds", "games_played", "games_played_team"]]

print(rebounds.sort_values("rebounds"))
rebounds["qualify"] = rebounds["games_played"] >= rebounds["games_played_team"] * CONSTANTS.MINIMUM_PERCENTAGE
rebounds = rebounds[rebounds["qualify"] == True]

rebounds["rebounds_per_game"] = rebounds["rebounds"] / rebounds["games_played"]
rebounds.info()
rebounds = rebounds.sort_values(by="rebounds_per_game", ascending=False)
print(rebounds.head())
most_rebounds_per_game_player = rebounds.iloc[0].name
print(most_rebounds_per_game_player)

# 4. Who has the most win shares?
# 5. Who has the most turnovers?
# 6. Who has the highest plus minus?
# 7. Who has the most free throws attempt?
# 8. Who played the most minutes?
# 9. Who has the highest true shooting percentage?
# 10. Who made the most three pointers?
