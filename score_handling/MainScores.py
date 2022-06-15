# from distutils.log import error
from re import template
from flask import Flask, render_template
import threading
# from Score import sum_points 
from Utils import *
import os



sum_points = 0
file = open("Score.txt", "r")
for line in file:
    sum_points += int(line)  
file.close() 



app = Flask(__name__, template_folder='../templates')

@app.route("/Score_Read")
def content():
    if open("Score.txt", "r").read():
        return render_template('score.html', SCORE = sum_points)
    else:
         return render_template('error.html', ERROR = BAD_RETURN_CODE)

# app.run(debug=True, port=5000)
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

















# def WebRun():
#     app.run(host='127.0.0.1', debug=False, port=30000)

# def run_script():
#     Thread = threading.Thread(target=WebRun, args=())
#     Thread.start()
#     # from Utils import Screen_cleaner
#     # return Screen_cleaner()
# run_script()