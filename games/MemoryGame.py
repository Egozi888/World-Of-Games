from random import randint
import random
from os import system
from Game_Live import *
import time




def memo_game_diff():
    global user_diff
    user_diff = diffculety()
    print(user_diff)
    if user_diff == 1:
        user_diff = range(1, 6)   
        print("The lenght of the list will be 5")
    if user_diff == 2:
        user_diff = range(1, 11) 
        print("The lenght of the list will be 10")
    if user_diff == 3:
        user_diff = range(1, 16) 
        print("The lenght of the list will be 15")    


def memo_game():
    random_list = []
    for i in user_diff:
        # any random numbers from 0 to 101
        random_list.append(random.randint(1, 101))
    print(random_list)
    time.sleep(2)
    system('clear')

    memory_list = []
    for j in user_diff:
        while True:
                try:
                    user_list = int(input("Please enter the number you saw:\n"))
                except ValueError:
                    print("not an integer")
                    continue
                if user_list not in range (1,102):
                    print ("not in the range")  
                else:
                    memory_list.append(user_list) 
                    print(memory_list)
                    break 
    if memory_list == random_list:
        print("King, You did it!!!", memory_list)
        from score_handling.Score import add_score
    else:
        print("Try next time :(")    
 

# memo_game_diff()        
# memo_game()       
        
