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
        # Most rebounds per game
        answer = leaders_dict["rebounds per game"].loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[3]:
        # Most win shares
        answer = leaders_dict["win shares"].loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[4]:
        # Most turnovers
        answer = leaders_dict["turnovers"].loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[5]:
        # Highest plus minus
        answer = leaders_dict["box plus/minus"].loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[6]:
        # Most free throw attempts
        answer = leaders_dict["free throw attempts"].loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[7]:
        # Most minutes per game
        answer = leaders_dict["minutes per game"].loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[8]:
        # Highest true shooting percentage
        answer = leaders_dict["true shooting pct"].loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[9]:
        # Most three pointers made
        answer = leaders_dict["3-pt field goals"].loc[0, "name"]
        return answer