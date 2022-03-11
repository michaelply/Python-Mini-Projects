import constants as CONSTANTS
import pandas as pd

def construct_quiz_dict(question_lists):
    quiz_dict = {}

    for i in range(len(question_lists)):
        question = question_lists[i]
        if question not in quiz_dict:
            answer = get_answer(question)
            quiz_dict[question] = answer
    return quiz_dict

def get_answer(question):
    if question == CONSTANTS.QUESTIONS[0]:
        # Most points per game
        df = pd.read_csv("nba_leaders_data/points per game.csv")
        answer = df.loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[1]:
        # Most assists per game
        df = pd.read_csv("nba_leaders_data/assists per game.csv")
        answer = df.loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[2]:
        # Most rebounds per game
        df = pd.read_csv("nba_leaders_data/rebounds per game.csv")
        answer = df.loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[3]:
        # Most win shares
        df = pd.read_csv("nba_leaders_data/win shares.csv")
        answer = df.loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[4]:
        # Most turnovers
        df = pd.read_csv("nba_leaders_data/turnovers.csv")
        answer = df.loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[5]:
        # Highest plus minus
        df = pd.read_csv("nba_leaders_data/box plus minus.csv")
        answer = df.loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[6]:
        # Most free throw attempts
        df = pd.read_csv("nba_leaders_data/free throw attempts.csv")
        answer = df.loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[7]:
        # Most minutes per game
        df = pd.read_csv("nba_leaders_data/minutes played.csv")
        answer = df.loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[8]:
        # Highest true shooting percentage
        df = pd.read_csv("nba_leaders_data/true shooting pct.csv")
        answer = df.loc[0, "name"]
        return answer
    elif question == CONSTANTS.QUESTIONS[9]:
        # Most three pointers made
        df = pd.read_csv("nba_leaders_data/3-pt field goals.csv")
        answer = df.loc[0, "name"]
        return answer