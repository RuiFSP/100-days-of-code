from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
from flask_msearch import Search
import os
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv
import pdfkit

load_dotenv()

# returns the absolute path of the directory that contains the current file, which is often the root directory of the
# project
basedir = os.path.abspath(os.path.dirname(__file__))
# print(basedir)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["UPLOADED_PHOTOS_DEST"] = os.path.join(basedir, "static/images")  # needed for upload images

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
search = Search()
search.init_app(app)
migrate = Migrate(app, db)

# Set the path to wkhtmltopdf executable file
config = pdfkit.configuration(wkhtmltopdf=os.getenv('path_wkhtmltopdf'))

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "customers_login"
login_manager.login_message_category = "danger"
login_manager.login_message = "You need to login first"

with app.app_context():
    if db.engine.url.drivername == "sqlite":
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

from .admin import routes, models, forms
from .products import routes, models, forms
from .carts import carts
from .customers import routes, models, forms
