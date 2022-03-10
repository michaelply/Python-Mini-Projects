import constants as CONSTANTS
import numpy as np
import pandas as pd

# Load and pre-process data
# Standing
def load_standing_data(json_file_path):
    standing = pd.read_json(json_file_path)
    # Add a column for total games each team played
    standing["games_played_team"] = standing["losses"] + standing["wins"]
    return standing

standing = load_standing_data(CONSTANTS.STANDING_OUTPUT_PATH)

# Basic stats
def load_basic_stats_data(json_file_path, standing):
    basic_stats = pd.read_json(json_file_path)
    # Add games played by team column to calculate minimum stats qualification
    basic_stats = basic_stats.merge(standing[["team", "games_played_team"]], on="team")
    basic_stats.set_index("name", inplace = True)
    return basic_stats

basic_stats = load_basic_stats_data(CONSTANTS.PLAYER_BASIC_STATS_OUTPUT_PATH, standing)

# Advanced stats
def load_advanced_stats_data(json_file_path, standing):
    advanced_stats = pd.read_json(json_file_path)
    # Add games played by team column to calculate minimum stats qualification
    advanced_stats = advanced_stats.merge(standing[["team", "games_played_team"]], on="team")
    advanced_stats.set_index("name", inplace = True)
    return advanced_stats

advanced_stats = load_advanced_stats_data(CONSTANTS.PLAYER_ADVANCED_STATS_OUTPUT_PATH, standing)
# print(advanced_stats.info())

# Functions to retrieve data
# Minimum qualifications for NBA stats leaders (https://www.nba.com/stats/help/statminimums/)

# Points
def get_basic_points_data(basic_stats):
    points = basic_stats.loc[:, ["points", "games_played", "games_played_team"]]
    points["qualify"] = points["games_played"] >= points["games_played_team"] * CONSTANTS.MINIMUM_PERCENTAGE
    points = points[points["qualify"] == True]
    points["points_per_game"] = points["points"] / points["games_played"]
    return points

def most_points_per_game(basic_points_data):
    most_points_ranking = basic_points_data.sort_values(by="points_per_game", ascending=False)
    most_points_per_game_player = most_points_ranking.iloc[0].name
    return most_points_per_game_player

def most_total_points(basic_points_data):
    points_ranking = basic_points_data.sort_values(by="points", ascending=False)
    most_total_points_player = points_ranking.iloc[0].name
    return most_total_points_player

# Assists
def get_basic_assists_data(basic_stats):
    assists = basic_stats.loc[:, ["assists", "games_played", "games_played_team"]]
    assists["qualify"] = assists["games_played"] >= assists["games_played_team"] * CONSTANTS.MINIMUM_PERCENTAGE
    assists = assists[assists["qualify"] == True]
    assists["assists_per_game"] = assists["assists"] / assists["games_played"]
    return assists

def most_assists_per_game(basic_assists_stats):
    assists_ranking = basic_assists_stats.sort_values(by="assists_per_game", ascending=False)
    most_assists_per_game_player = assists_ranking.iloc[0].name
    return most_assists_per_game_player

def most_total_assists(basic_assists_stats):
    assists_ranking = basic_assists_stats.sort_values(by="assists", ascending=False)
    most_total_assists_player = assists_ranking.iloc[0].name
    return most_total_assists_player

# TO-DO: Some players have multiple rows because they were traded in the season
# print(basic_stats.loc["James Harden"])

# 3. Who has the most rebounds per game?
def get_basic_rebounds_data(basic_stats):
    basic_stats["rebounds"] = basic_stats["defensive_rebounds"] + basic_stats["offensive_rebounds"]
    rebounds = basic_stats.loc[:, ["rebounds", "games_played", "games_played_team"]]
    rebounds["qualify"] = rebounds["games_played"] >= rebounds["games_played_team"] * CONSTANTS.MINIMUM_PERCENTAGE
    rebounds = rebounds[rebounds["qualify"] == True]
    rebounds["rebounds_per_game"] = rebounds["rebounds"] / rebounds["games_played"]
    return rebounds

def most_rebounds_per_game(basic_rebounds_stats):
    rebounds_ranking = basic_rebounds_stats.sort_values(by="rebounds_per_game", ascending=False)
    most_rebounds_per_game_player = rebounds_ranking.iloc[0].name
    return most_rebounds_per_game_player

def most_total_rebounds(basic_rebounds_stats):
    rebounds_ranking = basic_rebounds_stats.sort_values(by="rebounds_per_game", ascending=False)
    most_total_rebounds_player = rebounds_ranking.iloc[0].name
    return most_total_rebounds_player

# 4. Who has the most win shares?
def get_win_shares_data(advanced_stats):
    win_shares = advanced_stats["win_shares"]
    return win_shares

def most_win_shares(win_shares_stats):
    win_shares_ranking = win_shares_stats.sort_values(ascending=False)
    win_shares_leader = win_shares_ranking.index[0]
    return win_shares_leader

# 5. Who has the most turnovers?
def get_turnover_data(basic_stats):
    turnovers = basic_stats["turnovers"]
    return turnovers

def most_turnover_player(turnover_stats):
    turnover_ranking = turnover_stats.sort_values(ascending=False)
    print(turnover_ranking)
    turnover_leader = turnover_ranking.index[0]
    return turnover_leader

# 6. Who has the highest plus minus?
# 7. Who has the most free throws attempt?
# 8. Who played the most minutes?
# 9. Who has the highest true shooting percentage?
# 10. Who made the most three pointers?


# Tests
# points = get_basic_points_data(basic_stats)
# pts = most_total_points(points)
# ppg = most_points_per_game(points)
# print(ppg)
# print(pts)
#
# assists = get_basic_assists_data(basic_stats)
# apg = most_assists_per_game(assists)
# ast = most_total_assists(assists)
# print(apg)
# print(ast)
#
# rebounds = get_basic_rebounds_data(basic_stats)
# rpg = most_rebounds_per_game(rebounds)
# reb = most_total_rebounds(rebounds)
# print(rpg)
# print(reb)


