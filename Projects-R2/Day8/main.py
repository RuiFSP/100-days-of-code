import os
import requests
from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
bootstrap = Bootstrap(app)

CACHE = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        card_name = request.form['cardname']
        card_data = make_request(card_name)
        if card_data is None:
            flash('Card not found, please try again.')
            return render_template('base.html')
        return render_template('index.html', card_data=card_data)
    return render_template('base.html')


def make_request(card_name):
    if card_name in CACHE:
        return CACHE[card_name]

    url = "https://api.scryfall.com/cards/named?fuzzy=" + card_name
    try:
        response = requests.get(url)
        if response.status_code == 404:
            CACHE[card_name] = None
            return None
        card_data = response.json()
        CACHE[card_name] = card_data
        return card_data
    except requests.exceptions.RequestException as e:
        CACHE[card_name] = None
        return None


if __name__ == '__main__':
    app.run(debug=True)
