# from CurrencyRouletteGame import currncy_rolete_diff,currncy_rolete
# from GuessGame_copy import another_game

def welcome():
    name = input("Please enter your name:\n")
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")



games ={ 'game1': "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back", 
        'game2': "2. Guess Game - guess a number and see if you chose like the computer",
        'game3': "3. Currency Roulette - try and guess the value of a random amount of USD in ILS " 
        }
      
     

def load_game():
    for game,name in games.items():
        print(game, ":", name)
    good = True
    while good:
        try:
            game_choose = int(input("Please choose a game to play:\n"))
        except ValueError:
            print("not an integer")
            continue
        if game_choose==1:
            print("You choose this game:", games["game1"])
            from games.MemoryGame import memo_game_diff,memo_game 
            from games.GuessGame_copy import another_game
            return memo_game_diff(), memo_game(), another_game()
            break 
        elif game_choose==2:
            print("You choose this game:", games["game2"])
            from games.GuessGame_copy import diff_guess_game, guess_game, another_game
            return diff_guess_game(), guess_game(), another_game()
            break
        elif game_choose==3:
            print("You choose this game:", games["game3"])
            from games.CurrencyRouletteGame import currncy_rolete_diff,currncy_rolete
            from games.GuessGame_copy import another_game
            return currncy_rolete_diff(), currncy_rolete(), another_game()
            break    
        else:
            print("You didnt choose any") 
        continue
    



def diffculety():
    global user_diff
    ok = True
    while ok:
        try:
            user_diff = int(input("Please choose difficult level 1-3:\n"))
        except ValueError:
            print("Not an integer")
            continue    
        if user_diff >= 1 and user_diff <= 3:
            print("Your difficulety level is:", user_diff)
            return user_diff
            break 
        else:
            print("again")

# from GuessGame import game
# from Utils import Screen_cleaner

# def another_game():
#     global continue_play
#     # continue_play = input("Whould you like another game:\n")
#     while True:
#         continue_play = input("Whould you like another game:\n")
#         if continue_play == "yes":
#             return load_game()
#         #  break
#         if continue_play == "no":
#             # from Utils import Screen_cleaner
#             print("See Yaa")
#             break 
#         else:
#             print("Not the right answer")



    
