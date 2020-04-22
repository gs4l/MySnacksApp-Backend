from app import app, db
from flask import request, jsonify
from app.models import *

@app.route('/api/home')
def home():
	user_id = request.args.get('id')
	query = 'select * from users where id='+user_id+';'
	result = db.session.execute(query)
	for r in result:
		r_dict = dict(r.items())
	return jsonify(r_dict)

@app.route('/api/getlays')
def getlays():
	#create getlays
	return '0'

@app.route('/api/givelays')
def givelays():
	#create givelays
	return '0'

@app.route('/api/verify')
def verify():
	#create verify
	return '0'