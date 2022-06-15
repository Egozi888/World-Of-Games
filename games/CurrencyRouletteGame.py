from random import randint
from Game_Live import *
import random
import json
import requests



url = 'https://api.exchangerate.host/convert?from=USD&to=ILS'
response = requests.get(url)
json = response.json()


rate = json.get("result")
rate = float(format(rate, ".2f"))
print(f'USD to ILS exchange rate is: {rate}')




def currncy_rolete_diff():
    global guess_range, t
    user_diff = diffculety()
    t = random.randrange(1, 100, 1)
    print(user_diff)
    if user_diff == 1: 
         guess_range = [(t - (5 - user_diff)) * float(rate), (t + (5 - user_diff)) * float(rate)]  
         print('Your range around the result will +-14ILS!')
    if user_diff == 2:
        guess_range = [(t - (5 - user_diff)) * float(rate), (t + (5 - user_diff)) * float(rate)] 
        print('Your range around the result will be +-10ILS!')
    if user_diff == 3:
        guess_range = [(t - (5 - user_diff)) * float(rate), (t + (5 - user_diff)) * float(rate)] 
        print('Your range around the result will be +-6ILS!')

def currncy_rolete():
    while True:
        try:
            guess = float(input(f'How much is it {t} USD in ILS:\n'))
            print(guess_range)
            print(t * rate)
        except ValueError:
            print("not an integer")
            continue
        if guess_range[0] <= guess <= guess_range[1]:
            print(guess)
            print("Won")
            from score_handling.Score import add_score
            return add_score()
            break
        else:
            print("Again", guess_range) 
            continue





