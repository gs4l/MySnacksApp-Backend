from app import app, db
from flask import request, jsonify
from app.models import *
from app.utils import *

@app.route('/api/home')
def home():
	user_id = request.args.get('id')
	result = get_home_data(user_id)
	return jsonify(result)

@app.route('/api/getlays')
def getlays():
	user_id = request.args.get('id')
	otp = update_otp(user_id)
	result = {'otp': otp}
	return jsonify(result)

@app.route('/api/givelays')
def givelays():
	otp = request.args.get('otp')
	result = give_lays(otp)
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