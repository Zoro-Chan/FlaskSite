from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import random

app = Flask(__name__)

app.config['SECRET_KEY'] = 'KEY--[REDACTED]--KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from FlaskSite import routes
