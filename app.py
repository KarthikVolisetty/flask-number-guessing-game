# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:08:35 2024

@author: karth
"""

from flask import Flask, render_template, request
import random
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        lowerBound = int(request.form["lowerBound"])
        upperBound = int(request.form["upperBound"])
        userGuess = int(request.form["userGuess"])

        x = random.randint(lowerBound, upperBound)
        guess = math.ceil(math.log(upperBound - lowerBound + 1, 2))

        if x == userGuess:
            result = f"Congratulations! You guessed the correct number {x} in 1 try!"
        elif x > userGuess:
            result = f"You guessed too small! The number was {x}."
        elif x < userGuess:
            result = f"You guessed too high! The number was {x}."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
