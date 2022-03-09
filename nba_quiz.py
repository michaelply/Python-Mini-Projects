import data_processing as data

score = 0
total = 3

playing = input("Are you REALLY a NBA fan?(Y/N) \n")

# Quit the program if the player replies other than yes
if playing.lower() == "y" or playing.lower() == "yes":
    print("Prove it then!")
else:
    print("I knew it!")
    quit()
answer1 = input("Who has the most points per game this season?\n")
if answer1.lower() == data.most_points_per_game_player.lower():
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer2 = input("Who has the most assists per game this season?\n")
if answer2.lower() == data.most_assists_per_game_player.lower():
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer3 = input("Who has the most rebounds per game this season?\n")
if answer3.lower() == data.most_rebounds_per_game_player.lower():
    print("Correct")
    score += 1
else:
    print("Incorrect")

print(f"Your total score is {score} out of {total}\n")
score_percentage = int(score/total*100)
print(f"Your percentage is {score_percentage}%!\n")