import os

from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, jsonify, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


# Define your Cafe model
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    open_time = db.Column(db.String(250), nullable=False)
    close_time = db.Column(db.String(250), nullable=False)
    coffee_rating = db.Column(db.String(250), nullable=False)
    wifi_rating = db.Column(db.String(250), nullable=False)
    power_rating = db.Column(db.String(250), nullable=False)


class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Url - Location', validators=[DataRequired()])
    open_time = StringField('Open Time', validators=[DataRequired()])
    close_time = StringField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'],
                                validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating', choices=['✘', '💪', '💪💪️', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
                              validators=[DataRequired()])
    power_rating = SelectField('Power Outlet Rating', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
                               validators=[DataRequired()])

    submit = SubmitField('Submit')


# CREATE TABLE
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("base.html", cafes=Cafe.query.all())


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            location=form.location.data,
            open_time=form.open_time.data,
            close_time=form.close_time.data,
            coffee_rating=form.coffee_rating.data,
            wifi_rating=form.wifi_rating.data,
            power_rating=form.power_rating.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        flash('New cafe added successfully.')
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes', methods=['GET', 'POST'])
def cafes():
    coffees = Cafe.query.all()
    return render_template('cafes.html', cafes=coffees)


@app.route('/cafes/<int:id>/delete', methods=['POST'])
def delete_cafe(id):
    cafe = Cafe.query.get(id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        flash('Cafe successfully deleted.')
    else:
        flash('Cafe not found.')
    return redirect(url_for('cafes'))


@app.route('/cafes/<int:id>/edit', methods=['GET', 'POST'])
def edit_cafe(id):
    cafe = Cafe.query.get(id)
    if not cafe:
        flash('Cafe not found.')
        return redirect(url_for('cafes'))

    form = CafeForm(obj=cafe)
    if form.validate_on_submit():
        form.populate_obj(cafe)
        db.session.commit()
        flash('Cafe successfully updated.')
        return redirect(url_for('cafes'))

    return render_template('edit_cafe.html', form=form, cafe=cafe)


if __name__ == '__main__':
    app.run(debug=True)
