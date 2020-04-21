from flask import *
from flask_sqlalchemy import SQLAlchemy
from app import rest, config

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'SQLALCHEMY_DATABASE_URI'

db = SQLAlchemy(app)
