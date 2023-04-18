import os
from flask import Flask
from flask import render_template
from flask import send_from_directory
import requests

from post import Post

posts = requests.get("https://api.npoint.io/92d366edff0c0b191438").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post['date'], post['image'],
                    post['author'])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html', all_posts=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route("/about")
def about_me():
    return render_template("about.html")


@app.route("/contact")
def contact_me():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
