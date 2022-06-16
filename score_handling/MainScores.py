# from distutils.log import error
from re import template
import re
from flask import Flask, render_template
import threading
# from Score import sum_points 
from Utils import *
import os



# sum_points = 85
def read_score():
    sum_points = 0
    file = open("Score.txt", "r")
    for line in file:
        sum_points += int(line)      
    file.close() 




app = Flask(__name__, template_folder='../templates')

@app.route("/")
def content():
    try:
        with open("Score.txt", "r", encoding='utf-8') as f:
            f.readlines()
        return render_template('score.html', SCORE = sum_points)
    except:
        return render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')



# app = Flask(__name__, template_folder='../templates')

# @app.route('/')
# def read_score():
#     try:
#         with open("Score.txt", 'a', encoding='utf-8') as file:
#             score = file.readline()
#         return render_template('score.html', SCORE=sum_points)
#     except:
#         return render_template('error.html', ERROR=BAD_RETURN_CODE)


# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0')










# def WebRun():
#     app.run(host='127.0.0.1', debug=False, port=30000)

# def run_script():
#     Thread = threading.Thread(target=WebRun, args=())
#     Thread.start()
#     # from Utils import Screen_cleaner
#     # return Screen_cleaner()
# run_script()