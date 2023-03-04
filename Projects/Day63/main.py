import os
from flask import Flask, request
from flask import render_template
from flask import send_from_directory
import requests
import smtplib
from post import Post
from dotenv import load_dotenv

load_dotenv()

# GMAIL ACCOUNT
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
MAIL_PROVIDER_SMTP_ADDRESS = 'smtp.gmail.com'

posts = requests.get("https://api.npoint.io/92d366edff0c0b191438").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post['date'], post['image'],
                    post['author'])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/')
def home():
    return render_template('index.html', all_posts=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about_me():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact_me():
    if request.method == 'POST':

        # grabbing information from form
        name_entry = request.form['name']
        email_entry = request.form['email']
        phone_entry = request.form['phone']
        message_entry = request.form['message']

        # sending email
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)

            message = f'''Subject: New Subscriber\n
                Name: {name_entry}\n
                Email: {email_entry}\n
                Phone: {phone_entry}\n
                \n
                Message: {message_entry} 
                '''

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=message
            )

        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
