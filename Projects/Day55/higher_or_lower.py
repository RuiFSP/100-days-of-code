from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    if random_number > guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmQ2YjA3ZDBiZTVjYWYzM2I1ZjU2ZmE4YzRmZDQ2ZTJhZjgwN2ZlNiZjdD1n/Wq9RLX06zRg4UM42Qf/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmQ2YjA3ZDBiZTVjYWYzM2I1ZjU2ZmE4YzRmZDQ2ZTJhZjgwN2ZlNiZjdD1n/Wq9RLX06zRg4UM42Qf/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media4.giphy.com/media/9xt1MUZqkneFiWrAAD/giphy.gif?cid=ecf05e47z8evfmq4rdvf3pxtd5c21iyteuiaii76w73ilqr8&rid=giphy.gif&ct=g'/>"


if __name__ == "__main__":
    app.run(debug=True)