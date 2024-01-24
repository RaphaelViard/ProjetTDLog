from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "my_secret_key_123"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

current_directory = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.join(current_directory, "uploads")
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

login_manager = LoginManager(app)
login_manager.login_view = "connexion"

from app.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from app import routes
