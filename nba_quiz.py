import constants as CONSTANTS
import quiz_dict

def main():

    # Define variables
    score = 0
    nba_quiz_dict = quiz_dict.construct_quiz_dict(CONSTANTS.QUESTIONS)

    # Prompt to ask user play game or not
    playing = input("Are you REALLY a NBA fan?(Y/N) \n")

    # Quit the program if the player replies other than yes
    if playing.lower() == "y" or playing.lower() == "yes":
        print("Prove it then!")
    else:
        print("I knew it!")
        quit()

    # Ask questions and get answers
    for num in range(CONSTANTS.NUM_OF_QUESTIONS_IN_QUIZ):
        question = CONSTANTS.QUESTIONS[num]
        user_answer = input(question+"\n").lower()
        answer = nba_quiz_dict[question].lower()
        if user_answer == answer:
            print("Correct ;)")
            score += 1
        else:
            print("Incorrect :(")

    # Compute scores
    print(f"Your total score is {score} out of {CONSTANTS.NUM_OF_QUESTIONS_IN_QUIZ}")
    score_percentage = int(score/CONSTANTS.NUM_OF_QUESTIONS_IN_QUIZ*100)
    print(f"Your percentage is {score_percentage}%!")

main()