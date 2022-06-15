import random
from Game_Live import user_diff




def add_score():
    from score_handling.Utils import SCORES_FILE_NAME
    global sum_points
    POINTS_OF_WINNING = (int(user_diff) * 3) + 5
    POINTS_OF_WINNING = str(POINTS_OF_WINNING)
    SCORES_FILE_NAME.write(POINTS_OF_WINNING )
    SCORES_FILE_NAME.write('\n')  
    sum_points = int(POINTS_OF_WINNING)
    file = open("Score.txt", "r")
    for line in file:
        sum_points += int(line)
    print(f'Points added: {POINTS_OF_WINNING}\nYour Total points are: {sum_points}')    
    file.close() 
    

  

# add_score()


