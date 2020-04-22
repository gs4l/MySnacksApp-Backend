from flask_sqlalchemy import SQLAlchemy 
from app import db

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(20), nullable=False)
	role = db.Column(db.Integer, nullable=False)
	password = db.Column(db.String(10), nullable=False)
	login = db.Column(db.Boolean, nullable=False, default=False)
	available = db.Column(db.Integer)
	otp = db.Column(db.Integer)

	def __init__(self, id, name, role, password, login, available, otp):
		self.id = id
		self.name = name
		self.role = role
		self.password = password
		self.login = login
		self.available = available
		self.otp = otp


class Items(db.Model):
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(10), nullable=False)
	quantity = db.Column(db.Integer, nullable=False)

	def __init__(self, id, name, quantity):
		self.id = id
		self.name = name
		self.quantity = quantity