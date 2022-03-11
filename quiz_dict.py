import constants as CONSTANTS
import scrape_basketball_reference as scrape

def construct_quiz_dict(question_lists):
    quiz_dict = {}

    # Load latest scrapped data
    leaders_dict = scrape.get_nba_leaders_dict()

    for i in range(len(question_lists)):
        question = question_lists[i]
        if question not in quiz_dict:
            answer = get_answer(leaders_dict, question)
            quiz_dict[question] = answer
    return quiz_dict

def get_answer(leaders_dict, question):

    if question == CONSTANTS.QUESTIONS[0]:
        # Most points per game
        answer = leaders_dict["points per game"].loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[1]:
        # Most assists per game
        answer = leaders_dict["assists per game"].loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[2]:
        answer = leaders_dict["rebounds per game"].loc[0, "name"]
        return answer
