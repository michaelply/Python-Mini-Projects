import constants as CONSTANTS
import data_processing as data

def construct_quiz_dict(question_lists):
    quiz_dict = {}

    # Load latest scrapped data
    standing = data.load_standing_data(CONSTANTS.STANDING_OUTPUT_PATH)
    basic_stats = data.load_basic_stats_data(CONSTANTS.PLAYER_BASIC_STATS_OUTPUT_PATH, standing)
    advanced_stats = data.load_advanced_stats_data(CONSTANTS.PLAYER_ADVANCED_STATS_OUTPUT_PATH, standing)

    for i in range(len(question_lists)):
        question = question_lists[i]
        if question not in quiz_dict:
            answer = get_answer(question, standing, basic_stats, advanced_stats)
            quiz_dict[question] = answer.lower()
    return quiz_dict

def get_answer(question, standing, basic_stats, advanced_stats):

    if question == CONSTANTS.QUESTIONS[0]:
        # Most points per game
        points = data.get_basic_points_data(basic_stats)
        answer = data.most_points_per_game(points)
        return answer
    elif question == CONSTANTS.QUESTIONS[1]:
        # Most assists per game
        assists = data.get_basic_assists_data(basic_stats)
        answer = data.most_assists_per_game(assists)
        return answer
    elif question == CONSTANTS.QUESTIONS[2]:
        rebounds = data.get_basic_rebounds_data(basic_stats)
        answer = data.most_rebounds_per_game(rebounds)
        return answer