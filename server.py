import requests
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template

server = Flask(__name__)

@server.route('/') 
@server.route('/index') 
def home(): 
	r = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=d9ba51a5")
	data = r.json()
	return render_template('index.html', movies=data)

server.run(debug=True)