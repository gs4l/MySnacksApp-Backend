from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import *

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)

from app import rest