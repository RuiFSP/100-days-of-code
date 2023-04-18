import os
from flask import Flask, render_template, request
import cv2
from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from modules.helper_functions import allowed_file, get_top_colors
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = 'static/uploads'
bootstrap = Bootstrap(app)


class UploadForm(FlaskForm):
    image = FileField('Upload Image', validators=[DataRequired()])


# Define a route to display the upload form
@app.route('/')
def index():
    form = UploadForm()
    return render_template('base.html', form=form)


# Define a route to handle the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file
    file = request.files.get('image')
    if file is None:
        return 'No file found', 400
    if not allowed_file(file.filename):
        return 'Invalid file type', 400

    # Save the file to the uploads directory
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    # Read the file
    img = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    if img is None:
        return 'Invalid image file', 400

    # Get the top colors
    top_colors = get_top_colors(img)

    # Render the result template with the top colors
    return render_template('result.html', image_filename=file.filename, top_colors=top_colors)


if __name__ == '__main__':
    app.run(debug=True)
