from distutils.log import error
from re import template
from flask import Flask, render_template, template_rendered
import threading
# from Score import *
from Utils import *
import os

print (BAD_RETURN_CODE)
sum_points = 0
file = open("Score.txt", "r")
for line in file:
    sum_points += int(line)  
file.close() 





html_score=f"""<html>
            <head>
    <title>Scores Game</title>
            </head>
            <body>
                <h1>
                    The score is <div id="score">{sum_points}</div>
                </h1>
            </body>
        </html>
        """

html_error=f"""<html>
            <head>
    <title>Scores Game</title>
            </head>
            <body>
                <h1>
                    <div id="score" style="color:red">{BAD_RETURN_CODE}</div>
                </h1>
            </body>
        </html>
        """    



app = Flask(__name__)

@app.route("/Score_Read")
def content():
    if open("Score.txt", "r").read():
        return html_score
    else:
        return html_error

# app.run(debug=True, port=5000)
def WebRun():
    app.run(host='127.0.0.1', debug=False, port=30000)

def run_script():
    Thread = threading.Thread(target=WebRun, args=())
    Thread.start()
    # from Utils import Screen_cleaner
    # return Screen_cleaner()
run_script()