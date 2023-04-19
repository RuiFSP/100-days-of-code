import os

import bcrypt
import stripe
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    cart = db.relationship('Product', secondary='cart_products', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(200), nullable=False, default='static/images/default.jpg')

    def __repr__(self):
        return f"Product('{self.name}', '{self.price}', '{self.image}')"


cart_products = db.Table('cart_products',
                         db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                         db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
                         )


def seed_db():
    with app.app_context():
        # create the tables
        db.create_all()

        # create a sample user
        hashed_password = bcrypt.hashpw(os.getenv('SAMPLE_PASSWORD').encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user = User(username=os.getenv('SAMPLE_USERNAME'), email=os.getenv('SAMPLE_EMAIL'), password=hashed_password)
        db.session.add(user)
        db.session.commit()

        # create sample products
        products = [
            Product(name='Sample Product 1', price=100, image='static/images/default1.jpg'),
            Product(name='Sample Product 2', price=200, image='static/images/default2.jpg'),
            Product(name='Sample Product 3', price=300, image='static/images/default3.jpg')
        ]
        db.session.add_all(products)
        db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)


@app.route('/cart')
@login_required
def cart():
    user = current_user
    total_price = sum([product.price for product in user.cart])
    return render_template('cart.html', products=user.cart, total_price=total_price)


@app.route('/add_to_cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    product = Product.query.get(product_id)
    user = current_user
    user.cart.append(product)
    db.session.commit()
    return redirect(url_for('cart'))


@app.route('/remove_from_cart/<int:product_id>')
@login_required
def remove_from_cart(product_id):
    product = Product.query.get(product_id)
    user = current_user
    user.cart.remove(product)
    db.session.commit()
    return redirect(url_for('cart'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/checkout')
@login_required
def checkout():
    user = current_user

    checkout_items = []
    for product in user.cart:
        checkout_items.append({
            'name': product.name,
            'amount': int(product.price * 100),
            'quantity': 1,
            'currency': 'usd'
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=checkout_items,
        mode='payment',
        success_url=url_for('home', _external=True),
        cancel_url=url_for('home', _external=True),
    )

    return redirect(session.url, code=303)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.hashpw(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html', title='Log In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
    seed_db()
