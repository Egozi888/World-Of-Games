from random import randint
import random
from Live import diffculety




def diff_guess_game():
    global secret_number
    user_diff = diffculety()
    print(user_diff)
    if user_diff == 1:
        secret_number = random.randint(1, 3) 
        print("The range of the numbers will be 1-3")  
    if user_diff == 2:
        secret_number = random.randint(1, 6) 
        print("The range of the numbers will be 1-5") 
    if user_diff == 3:
        secret_number = random.randint(1, 11) 
        print("The range of the numbers will be 1-10") 

    print(secret_number)


def guess_game():
    while True:
                try:
                    usr_guess =int(input('please enter the number you guessed: \n'))
                except ValueError:
                    print("not an integer")
                    continue
                if usr_guess in range(secret_number + 1):
                    print(secret_number)
                else:
                    print("not in the range") 
                if usr_guess == secret_number:
                    print('You did it!!', secret_number)
                    from score_handling.Score import add_score 
                    return add_score() 
                    # another_game()
                    break
                # try:    
                else:
                    print("Again")
                # continue

                
    

             
# diff_guess_game()
# guess_game()







def another_game():
    another_game = input("whould you like to play another game?(yes/no)\n") 
    ok = True
    while ok:
            if another_game == ("Yes" and "yes"):
                from Live import load_game
                return load_game()
                # break
            if another_game == ("No" and "no"):
                from score_handling.Utils import Screen_cleaner
                return Screen_cleaner()
                break
            break


# another_game()        