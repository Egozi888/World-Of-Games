from flask import Flask, render_template
from Score import *
from Utils import *

# print (BAD_RETURN_CODE)
# sum_points = 0
# file = open("Score.txt", "r")
# for line in file:
#     sum_points += int(line)  
# file.close() 



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

app.run(debug=True, port=5000)