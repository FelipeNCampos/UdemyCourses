from flask import Flask
from random import randint

 
app = Flask(__name__)

number = randint(0, 9)


@app.route("/")
def hello():
    return "Guess a number between 0 and 9"

@app.route("/<int:guess>")
def guess(guess):
    if guess < number:
        return "<p>Too low, try again!</p>"
    elif guess > number:
        return "<p>Too high, try again!</p>"
    else:
        return f"<p>Congratulations! You guessed the number {number} correctly!</p>"


if __name__ == "__main__":
    app.run()