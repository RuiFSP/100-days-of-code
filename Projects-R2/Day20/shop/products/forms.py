from flask_wtf.file import FileField, FileAllowed
from wtforms import IntegerField, StringField, TextAreaField, validators, Form, DecimalField

DEFAULT_IMG = 'default.jpg'


class AddProductForm(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    stock = IntegerField('Stock', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    description = TextAreaField('Description', [validators.DataRequired()])
    color = TextAreaField('Colors', [validators.DataRequired()])
    image_1 = FileField('Image 1', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])], default=DEFAULT_IMG)
    image_2 = FileField('Image 2', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])], default=DEFAULT_IMG)
    image_3 = FileField('Image 3', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg']), ], default=DEFAULT_IMG)

