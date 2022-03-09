# DATA SCRAPING
CURRENT_SEASON = 2022
STANDING_OUTPUT_PATH = f"./{CURRENT_SEASON}_standings.json"
PLAYER_BASIC_STATS_OUTPUT_PATH = f"./{CURRENT_SEASON}_player_season_totals.json"
PLAYER_ADVANCED_STATS_OUTPUT_PATH = f"./{CURRENT_SEASON}_player_advanced_season_totals.json"

# DATA ANALYSIS
TOTAL_GAMES = 82
MINIMUM_PERCENTAGE = 0.7

# QUESTIONS
QUESTIONS = [
    "Who has the most points per game this season?",
    "Who has the most assists per game this season?",
    "Who has the most rebounds per game this season?"
    # "Who has the most win shares this season?",
    # "Who has the most turnovers this season?",
    # "Who has the highest plus minus this season?",
    # "Who has the most free throws attempt this season?",
    # "Who played the most minutes this season?",
    # "Who has the highest true shooting percentage this season?",
    # "Who made the most three pointers this season?"
]