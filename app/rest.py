from app import app, db
from flask import request, jsonify
from app.models import *
from app.utils import *

@app.route('/api/home')
def home():
	user_id = request.args.get('id')
	result = get_home_data(user_id)
	return jsonify(result)

@app.route('/api/getsnack')
def getsnack():
	user_id = request.args.get('id')
	otp = update_otp(user_id)
	result = {'otp': otp}
	return jsonify(result)

@app.route('/api/givesnack')
def givesnack():
	otp = request.args.get('otp')
	result = give_snack(otp)
	return jsonify(result)

@app.route('/api/login', methods=['POST'])
def login():
	user_data = request.form 
	uname = user_data['name']
	passwd = user_data['password']
	result = verify_uname_passwd(uname, passwd)
	return jsonify(result)

@app.route('/api/logout', methods=['POST'])
def logout():
	uname = request.form['name']
	result = verify_uname_logout(uname)
	return jsonify(result)

@app.route('/api/updateitem', methods=['POST'])
def update():
	item_data = request.form
	item_id = item_data['id']
	item_qty = item_data['quantity']
	result = update_item(item_id, item_qty)
	return jsonify(result)

@app.route('/api/itemlist')
def itemlist():
	result = item_list()
	return jsonify(result)

@app.route('/api/additem', methods=['POST'])
def additem():
	item_data = request.form
	item_name = item_data['name']
	item_qty = item_data['quantity']
	result = add_item(item_name, item_qty)
	return jsonify(result)

# @app.route('/api/check_login', methods=['POST'])
# def chk_login():
# 	user_id = request.form['id']
# 	result = check_login(user_id)
# 	if result == LOGGED_IN:
# 		return redirect(url_for('home', id=user_id))
# 	return redirect(url_for('login'))