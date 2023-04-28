from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
import os

# returns the absolute path of the directory that contains the current file, which is often the root directory of the
# project
basedir = os.path.abspath(os.path.dirname(__file__))
# print(basedir)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myshop.db"
app.config["SECRET_KEY"] = "7834yh434hfhd79p24379ph2438h5495h"
app.config["UPLOADED_PHOTOS_DEST"] = os.path.join(basedir, "static/images") # needed for upload images

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

with app.app_context():
    db.create_all()

from .admin import routes, models, forms
from .products import routes, models, forms
from .carts import carts