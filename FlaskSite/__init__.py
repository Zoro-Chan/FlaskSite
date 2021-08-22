from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

app.config['SECRET_KEY'] = 'KEY--afe0aa86371e5d84c1d5bb132bc82d1865869b0c5--KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
db = SQLAlchemy(app)

from FlaskSite import routes
