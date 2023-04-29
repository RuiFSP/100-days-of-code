from wtforms import StringField, PasswordField, validators, SubmitField, ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_wtf import FlaskForm
from .models import Register


class CustomerRegistrationForm(FlaskForm):
    name = StringField('Name:', [validators.DataRequired()])
    username = StringField('Username:', [validators.DataRequired()])
    email = StringField('Email:', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password:', [validators.DataRequired(),
                                           validators.equal_to('confirm', message='Both passwords must match')])
    confirm = PasswordField('Confirm Password:', [validators.DataRequired()])
    country = StringField('Country:', [validators.DataRequired()])
    city = StringField('City:', [validators.DataRequired()])
    contact = StringField('Contact:', [validators.DataRequired()])
    address = StringField('Address:', [validators.DataRequired()])
    zipcode = StringField('Zipcode:', [validators.DataRequired()])

    profile = FileField('Profile', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])

    submit = SubmitField('Register')

    def validate_username(self, username):
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError('Username already exists')

    def validate_email(self, email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError('Email already exists')


class CustomerLoginForm(FlaskForm):
    email = StringField('Email:', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password:', [validators.DataRequired()])
