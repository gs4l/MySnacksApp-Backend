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
	query = 'update users set available=available-1 where otp='+otp+'; update items set quantity=quantity-1;'
	nonret_query(query)
	return '0'

@app.route('/api/verify')
def verify():
	#create verify
	return '0'