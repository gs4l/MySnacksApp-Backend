from app import db
from app.models import *
from random import randint
from app.config import *

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

def give_lays(otp):
	result = {}
	try:
		user = Users.query.filter_by(otp=otp).first()
		item = Items.query.filter_by(id=ITEM_LAYS).first()
		if user is None:
			result['message'] = 'Wrong OTP'
			result['code'] = 1
		elif item is None:
			result['message'] = 'Something went Wrong'
			result['code'] = 2
		elif item.quantity == 0:
			result['message'] = 'Item currently not available'
			result['code'] = 2
		elif user.available == 0:
			result['message'] = 'Today user limit reached'
			result['code'] = 2
		else:
			user.available = user.available - 1
			item.quantity = item.quantity - 1
			result['message'] = 'SUCCESS Allowed to take one unit of item'
			result['code'] = 2
		db.session.commit()
	except:
		db.session.rollback()
	return result

def verify_uname_passwd(uname, passwd):
	result = {}
	try:
		user = Users.query.filter_by(name=uname).first()
		if user is None:
			result['message'] = 'User not registered'
			result['code'] = 1
		elif user.password == passwd:
			user.login = True
			result['message'] = 'Login SUCCESS'
			result['code'] = 2
		elif user.password != passwd:
			result['message'] = 'Wrong Password'
			result['code'] = 3
		else:
			result['message'] = 'Something went Wrong'
			result['code'] = 4
		db.session.commit()
	except:
		db.session.rollback()
	return result

def verify_uname_logout(uname):
	result = {}
	try:
		user = Users.query.filter_by(name=uname).first()
		user.login = False
		db.session.commit()
		result['message'] = 'Logout SUCCESS'
	except:
		db.session.rollback()
	return result

def update_item(id, quantity):
	result = {}
	try:
		item = Items.query.get(id)
		item.quantity = item.quantity + int(quantity)
		db.session.commit()
		result['message'] = 'Item updated SUCCESS'
	except:
		db.session.rollback()
	return result

def item_list():
	result = {}
	data = []
	try:
		items = Items.query.all()
		for i in items:
			item = {}
			item['id'] = i.id
			item['name'] = i.name
			data.append(item)
		result['data'] = data
		db.session.commit()
	except:
		db.session.rollback()
	return result

def add_item(name, quantity):
	result = {}
	try:
		item = Items.query.order_by(Items.id.desc()).first()
		id = item.id + 1
		new_item = Items(id, name, int(quantity))
		db.session.add(new_item)
		db.session.commit()
		result['message'] = 'Item added SUCCESS'
	except:
		db.session.rollback()
	return result

# def check_login(id):
# 	result = LOGGED_OUT
# 	try:
# 		user = Users.query.get(id)
# 		if user.login is True:
# 			result = LOGGED_IN
# 		else:
# 			result = LOGGED_OUT
# 		db.session.commit()
# 	except:
# 		db.session.rollback()
# 	return result