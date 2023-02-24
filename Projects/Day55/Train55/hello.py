from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"

    return wrapper


def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"

    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>this is a paragraph</p>' \
           '<img src="https://64.media.tumblr.com/5d1cbc790e5daaa7a7623dca6a13fdd3/tumblr_mg9hbrlLRG1rvgylco1_400.gifv" width=200>'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return 'Bye'


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)
