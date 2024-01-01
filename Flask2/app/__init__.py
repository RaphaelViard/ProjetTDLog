from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'my_secret_key_123'
db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'connexion'

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Import the User model (assuming it exists in your app.models module)
from app.models import User

@login_manager.user_loader
def load_user(user_id):
    # Load a user from the database using the user_id
    return User.query.get(int(user_id))

from app import routes  # Import routes after initializing the application and login manager
