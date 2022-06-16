SCORES_FILE_NAME = open("Score.txt", 'a')
BAD_RETURN_CODE = 401

def Screen_cleaner():
    import os
    os.system('cls||clear')

sum_points = 0
file = open("Score.txt", "r")
for line in file:
    sum_points += int(line)  
file.close() 

# print(sum_points)