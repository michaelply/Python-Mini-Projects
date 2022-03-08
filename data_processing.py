import constants as CONSTANTS
import numpy as np
import pandas as pd

# Read nba standing data
standing = pd.read_json(CONSTANTS.STANDING_OUTPUT_PATH)
print(standing)

# Read player basic stats
basic_stats = pd.read_json(CONSTANTS.PLAYER_BASIC_STATS_OUTPUT_PATH)
print(basic_stats.columns)

# Read player advanced stats
advanced_stats = pd.read_json(CONSTANTS.PLAYER_ADVANCED_STATS_OUTPUT_PATH)
print(advanced_stats.columns)
