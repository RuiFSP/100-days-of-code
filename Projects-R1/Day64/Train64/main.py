from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, AnyOf, Length, Email
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = EmailField(label='Email',
                       validators=[
                           DataRequired(),
                           Email(),
                           AnyOf(values=["admin@gmail.com"])])
    password = PasswordField(label='Password',
                             validators=[
                                 DataRequired(),
                                 Length(min=8, max=20, message="Field must be at least 8 characters long."),
                                 AnyOf(values=["12345678"])
                             ])
    submit = SubmitField(label='Enter')


def create_app():
    app = Flask(__name__)
    app.secret_key = "uhf9p34hrhdafu9pah"
    Bootstrap(app)

    return app

# create a Bootstrap App
app = create_app()


@app.route("/")
def home():
    return render_template('base.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if request.method == 'POST':
        if login_form.validate_on_submit():
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
