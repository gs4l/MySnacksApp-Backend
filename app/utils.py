from app import db
from app.models import *
from random import randint

def update_otp(id):
	otp = randint(100000,999999)
	try:
		user = Users.query.get(id)
		user.otp = otp
		db.session.commit()
	except:
		db.session.rollback()
	return otp

def get_home_data(id):
	result = {}
	try:
		user = Users.query.get(id)
		result['id'] = user.id
		result['name'] = user.name
		result['role'] = user.role
		result['available'] = user.available
		db.session.commit()
	except:
		db.session.rollback()
	return result
