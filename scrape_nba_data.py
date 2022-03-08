from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import constants as CONSTANTS

# Get current nba season standing
client.standings(
    season_end_year=CONSTANTS.CURRENT_SEASON,
    output_type=OutputType.JSON,
    output_file_path=CONSTANTS.STANDING_OUTPUT_PATH
)

# Get player season totals (basic statistics)
client.players_season_totals(
    season_end_year=CONSTANTS.CURRENT_SEASON,
    output_type=OutputType.JSON,
    output_file_path=CONSTANTS.PLAYER_BASIC_STATS_OUTPUT_PATH
)
# Get player season totals (advances statistics)
client.players_advanced_season_totals(
    season_end_year=CONSTANTS.CURRENT_SEASON,
    output_type=OutputType.JSON,
    output_file_path=CONSTANTS.PLAYER_ADVANCED_STATS_OUTPUT_PATH
)