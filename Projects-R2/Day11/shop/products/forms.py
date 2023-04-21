from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import IntegerField, StringField, BooleanField, TextAreaField, validators, Form

DEFAULT_IMG = 'default.jpg'


class Addproduct(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = IntegerField('Price', [validators.DataRequired()])
    stock = IntegerField('Stock', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    description = TextAreaField('Description', [validators.DataRequired()])
    color = TextAreaField('Colors', [validators.DataRequired()])
    image_1 = FileField('Image 1', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg']), FileRequired()],
                        default=DEFAULT_IMG)
    image_2 = FileField('Image 2', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg']), FileRequired()],
                        default=DEFAULT_IMG)
    image_3 = FileField('Image 3', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg']), FileRequired()],
                        default=DEFAULT_IMG)
