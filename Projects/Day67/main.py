import binascii
import os

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from flask_forms import UpdateRateMovieForm, FindMovieForm

load_dotenv()

# links
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_API_KEY = os.getenv("MOVIE_DB_API_KEY")
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

# create the extension
db = SQLAlchemy()

# create the app
app = Flask(__name__)
# By default, Flask-WTF protects all forms against Cross-Site Request Forgery
# (CSRF) attacks. You need to set up an encryption key to generate an encrypted token in app
app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collections.db'
Bootstrap(app)
# initialize the app with the extension
db.init_app(app)


# DEFINE MODEL
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# CREATE TABLE
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    # This line creates a list of all the movies sorted by rating
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()

    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movie_list=all_movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit_movie():
    form = UpdateRateMovieForm()
    movie_id = request.args.get("id")
    movie_to_edit = Movie.query.get(movie_id)
    if form.validate_on_submit():
        # Make changes to db
        movie_to_edit.rating = float(form.rating.data)
        movie_to_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie_to_edit)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add_movie():
    form = FindMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        print(data)
        new_movie = Movie(
            title=data["title"],
            # The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            description=data["overview"],
            rating=0,
            ranking=0,
            review="None",
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit_movie", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
