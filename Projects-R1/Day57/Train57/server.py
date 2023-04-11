import os
import random
import datetime
import requests

from flask import Flask
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.date.today().year
    return render_template(template_name_or_list='index2.html', num=random_number, year=current_year)


@app.route('/guess/<name>')
def guess(name):
    # APIs
    url_gender = f"https://api.genderize.io?name={name}"
    url_age = f"https://api.agify.io?name={name}"

    # requests
    gender_response = requests.get(url=url_gender)
    gender = gender_response.json()['gender']
    age_response = requests.get(url=url_age)
    age = age_response.json()['age']

    return render_template(template_name_or_list='guess.html', name=name, gender=gender, age=age)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template(template_name_or_list='blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
